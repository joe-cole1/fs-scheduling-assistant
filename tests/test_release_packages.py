"""Regression checks for draft-first immutable release publication; no real network writes."""
import hashlib
import importlib.util
import json
import os
import subprocess
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SPEC = importlib.util.spec_from_file_location('release_packages', Path(__file__).resolve().parents[1] / 'scripts/release_packages.py')
r = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(r)


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return json.dumps(self.payload).encode()


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name) / 'downloads'
        self.folder.mkdir()
        manifest = {'package_version': '0.5.3', 'packages': {}}
        for name in r.ZIPS:
            data = ('synthetic bytes: ' + name).encode()
            (self.folder / name).write_bytes(data)
            manifest['packages'][name] = {'sha256': hashlib.sha256(data).hexdigest()}
        (self.folder / 'manifest.json').write_text(json.dumps(manifest))
        self.state = {
            'repo': 'synthetic/example', 'tag': 'v0.5.3', 'version': '0.5.3',
            'source_sha': 'a' * 40, 'controller_sha': 'a' * 40,
            'build_contract': {'legacy': False}, 'workflow_run_url': 'https://example.invalid/run/1'
        }

    def draft(self, **changes):
        base = {
            'id': 7,
            'tag_name': 'untagged-abc123',
            'name': 'v0.5.3',
            'draft': True,
            'immutable': False,
            'target_commitish': 'a' * 40,
            'assets': [],
            'upload_url': 'https://uploads.github.com/repos/synthetic/example/releases/7/assets{?name,label}',
        }
        return base | changes

    def test_version_validation(self):
        self.assertEqual(r.tag_from_version('0.5.3'), 'v0.5.3')
        self.assertEqual(r.tag_from_version('1.0.0-rc.1'), 'v1.0.0-rc.1')
        for value in ('v0.5.3', '../0.5.3', '0.5', '0.5.3;bad'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                r.tag_from_version(value)

    def test_release_lookup_recognizes_untagged_draft_by_release_name(self):
        draft = self.draft()
        with patch.object(r, 'api', return_value=[draft]):
            self.assertEqual(r.release_for_tag('synthetic/example', 'v0.5.3'), draft)

    def test_release_slot_allows_matching_or_empty_retargetable_draft(self):
        with patch.object(r, 'release_for_tag', return_value=None), patch.object(r, 'remote_tag_commit', return_value=None):
            self.assertIsNone(r.validate_release_slot('synthetic/example', 'v0.5.3', 'a' * 40))

        matching = self.draft()
        with patch.object(r, 'release_for_tag', return_value=matching), patch.object(r, 'remote_tag_commit', return_value=None):
            self.assertEqual(r.validate_release_slot('synthetic/example', 'v0.5.3', 'a' * 40), matching)

        empty_old_source = self.draft(target_commitish='b' * 40)
        with patch.object(r, 'release_for_tag', return_value=empty_old_source), patch.object(r, 'remote_tag_commit', return_value=None):
            self.assertEqual(r.validate_release_slot('synthetic/example', 'v0.5.3', 'a' * 40), empty_old_source)

        populated_old_source = self.draft(
            target_commitish='b' * 40,
            assets=[{'id': 1, 'name': r.ZIPS[0]}],
        )
        with patch.object(r, 'release_for_tag', return_value=populated_old_source), patch.object(r, 'remote_tag_commit', return_value=None), self.assertRaises(ValueError):
            r.validate_release_slot('synthetic/example', 'v0.5.3', 'a' * 40)

        published = self.draft(draft=False, tag_name='v0.5.3')
        with patch.object(r, 'release_for_tag', return_value=published), patch.object(r, 'remote_tag_commit', return_value='a' * 40), self.assertRaises(ValueError):
            r.validate_release_slot('synthetic/example', 'v0.5.3', 'a' * 40)

        with patch.object(r, 'release_for_tag', return_value=None), patch.object(r, 'remote_tag_commit', return_value='a' * 40), self.assertRaises(ValueError):
            r.validate_release_slot('synthetic/example', 'v0.5.3', 'a' * 40)

    def test_reproducibility_contract(self):
        requirements = b'package==1\n'
        contract = r.SUPPORTED_REPRO | {'requirements_sha256': hashlib.sha256(requirements).hexdigest()}
        self.assertEqual(r.validate_reproducibility_contract(contract, requirements), contract)
        with self.assertRaises(ValueError):
            r.validate_reproducibility_contract(contract | {'python_version': '3.12.15'}, requirements)

    def test_build_contract_reads_prospective_source_commit(self):
        requirements = b'package==1\n'
        contract = r.SUPPORTED_REPRO | {'requirements_sha256': hashlib.sha256(requirements).hexdigest()}

        def source_bytes(sha, path):
            if path == 'packaging/requirements.txt':
                return requirements
            if path == 'packaging/reproducibility.json':
                return json.dumps(contract).encode()
            self.fail(path)

        with patch.object(r, 'git_show_bytes', side_effect=source_bytes):
            loaded = r.tagged_build_contract('c' * 40, 'v0.5.3')
        self.assertFalse(loaded['legacy'])
        self.assertEqual(loaded['requirements_path'], 'release-source/packaging/requirements.txt')

    def test_checksum_and_inventory(self):
        r.verify_build(self.folder, '0.5.3')
        self.assertEqual(len((self.folder / 'SHA256SUMS.txt').read_text().splitlines()), 4)
        (self.folder / r.ZIPS[0]).write_bytes(b'changed')
        with self.assertRaises(ValueError):
            r.verify_build(self.folder, '0.5.3')

    def test_asset_plan_resumes_matching_draft_without_overwrite(self):
        r.verify_build(self.folder, '0.5.3')
        release = {'assets': [{'id': 1, 'name': r.ZIPS[0], 'state': 'uploaded'}]}
        missing = r.asset_plan(release, self.folder, lambda asset: (self.folder / asset['name']).read_bytes())
        self.assertEqual(missing, list(r.FILES[1:]))
        with self.assertRaises(ValueError):
            r.asset_plan(release, self.folder, lambda asset: b'different bytes')
        with self.assertRaisesRegex(ValueError, 'incomplete'):
            r.asset_plan({'assets': [{'id': 1, 'name': r.ZIPS[0], 'state': 'starter'}]}, self.folder, lambda asset: b'')

    def test_duplicate_or_extra_draft_assets_fail(self):
        r.verify_build(self.folder, '0.5.3')
        duplicate = {'assets': [{'id': 1, 'name': r.ZIPS[0]}, {'id': 2, 'name': r.ZIPS[0]}]}
        with self.assertRaises(ValueError):
            r.asset_plan(duplicate, self.folder, lambda asset: (self.folder / asset['name']).read_bytes())
        extra = {'assets': [{'id': 3, 'name': 'unexpected.bin'}]}
        with self.assertRaises(ValueError):
            r.asset_plan(extra, self.folder, lambda asset: b'')

    def test_direct_draft_asset_upload_uses_returned_upload_url_and_raw_bytes(self):
        path = self.folder / r.ZIPS[0]
        draft = self.draft()
        seen = {}

        def fake_urlopen(request, timeout):
            seen['url'] = request.full_url
            seen['data'] = request.data
            seen['authorization'] = request.get_header('Authorization')
            seen['content_type'] = request.get_header('Content-type')
            seen['timeout'] = timeout
            return FakeResponse({'name': path.name, 'state': 'uploaded', 'id': 99})

        with patch.dict(os.environ, {'GH_TOKEN': 'synthetic-token'}), patch.object(r, 'urlopen', side_effect=fake_urlopen):
            result = r.upload_asset(draft, path)

        self.assertEqual(result['id'], 99)
        self.assertTrue(seen['url'].startswith('https://uploads.github.com/repos/synthetic/example/releases/7/assets?'))
        self.assertIn('name=Pantons_Setup.zip', seen['url'])
        self.assertEqual(seen['data'], path.read_bytes())
        self.assertEqual(seen['authorization'], 'Bearer synthetic-token')
        self.assertEqual(seen['content_type'], 'application/zip')
        self.assertEqual(seen['timeout'], 180)

    def test_transient_upload_failure_retries_after_reconciliation(self):
        path = self.folder / r.ZIPS[0]
        error = r.AssetUploadError(path.name, 'HTTP 500: error saving asset', status=500, detail='error saving asset')
        sleeps = []
        with patch.object(r, 'upload_asset', side_effect=[error, {'id': 99, 'name': path.name, 'state': 'uploaded'}]) as upload, \
             patch.object(r, 'api', return_value=self.draft()), \
             patch.object(r, 'time'):
            result = r.upload_asset_with_retry(
                'synthetic/example', self.draft(), path, lambda asset: path.read_bytes(), sleep=sleeps.append
            )
        self.assertEqual(result['id'], 99)
        self.assertEqual(upload.call_count, 2)
        self.assertEqual(sleeps, [1])

    def test_ambiguous_upload_failure_accepts_verified_saved_asset(self):
        path = self.folder / r.ZIPS[0]
        saved = {'id': 99, 'name': path.name, 'state': 'uploaded'}
        error = r.AssetUploadError(path.name, 'HTTP 500: error saving asset', status=500, detail='error saving asset')
        refreshed = self.draft(assets=[saved])
        with patch.object(r, 'upload_asset', side_effect=error) as upload, \
             patch.object(r, 'api', return_value=refreshed):
            result = r.upload_asset_with_retry(
                'synthetic/example', self.draft(), path, lambda asset: path.read_bytes(), sleep=lambda _: None
            )
        self.assertEqual(result, saved)
        self.assertEqual(upload.call_count, 1)

    def test_incomplete_expected_asset_is_removed_before_resume(self):
        starter = {'id': 55, 'name': r.ZIPS[0], 'state': 'starter'}
        draft = self.draft(assets=[starter])
        cleaned = self.draft(assets=[])
        calls = []

        def api(endpoint, method='GET', payload=None):
            calls.append((endpoint, method))
            if method == 'DELETE':
                return None
            return cleaned

        with patch.object(r, 'api', side_effect=api):
            result = r.remove_incomplete_expected_assets('synthetic/example', draft)
        self.assertEqual(result, cleaned)
        self.assertIn(('repos/synthetic/example/releases/assets/55', 'DELETE'), calls)

    def test_structured_notes_include_downloads_and_checksums(self):
        r.verify_build(self.folder, '0.5.3')
        summary = ('## What changed\n\nChange.\n\n'
                   '## What you need to do\n\nUpdate next week.\n\n'
                   '## Validation and known limitations\n\nPassed.\n\n'
                   '## Changes and contributors\n\nGenerated notes.')
        result = r.notes(summary, self.state, self.folder)
        self.assertTrue(r.has_structured_summary(result))
        self.assertEqual(result.count(r.START), 1)
        self.assertIn('/releases/download/v0.5.3/Pantons_Setup.zip', result)
        self.assertIn(hashlib.sha256((self.folder / r.ZIPS[0]).read_bytes()).hexdigest(), result)

    def test_malformed_or_unstructured_notes_fail(self):
        with self.assertRaises(ValueError):
            r.notes('## Changes only', self.state, self.folder)
        for body in (r.START + 'human', r.END + r.START, r.START * 2 + r.END):
            with self.subTest(body=body), self.assertRaises(ValueError):
                r.without_download_block(body)

    def test_release_summary_reports_current_migration_status(self):
        manifest = {'migrations': [{'id': 'P-1', 'introduced_in': '0.5.3', 'action': 'review-and-merge'}]}

        def source_bytes(sha, path):
            if path == 'packaging/update-note.md':
                return b'Automation changed.'
            if path == 'packaging/persistent-artifacts.json':
                return json.dumps(manifest).encode()
            self.fail(path)

        with patch.object(r, 'git_show_bytes', side_effect=source_bytes):
            result = r.release_summary(self.state)
        self.assertIn('Automation changed.', result)
        self.assertIn('PERSISTENT MIGRATIONS.docx', result)
        self.assertIn('Passed in this release workflow', result)

    def test_ensure_draft_retargets_empty_untagged_draft(self):
        old = self.draft(target_commitish='b' * 40)
        retargeted = self.draft(target_commitish='a' * 40)
        calls = []

        def api(endpoint, method='GET', payload=None):
            calls.append((endpoint, method, payload))
            if method == 'PATCH':
                self.assertEqual(payload['tag_name'], 'v0.5.3')
                self.assertEqual(payload['target_commitish'], 'a' * 40)
                return retargeted
            return retargeted

        with patch.object(r, 'validate_release_slot', return_value=old), patch.object(r, 'api', side_effect=api):
            release = r.ensure_draft(self.state, 'body')
        self.assertTrue(release['draft'])
        self.assertEqual(release['target_commitish'], 'a' * 40)
        self.assertTrue(any(method == 'PATCH' for _, method, _ in calls))

    def test_validate_draft_accepts_github_untagged_identity(self):
        r.validate_draft(self.draft(), self.state)
        with self.assertRaises(ValueError):
            r.validate_draft(self.draft(name='v0.5.4'), self.state)
        with self.assertRaises(ValueError):
            r.validate_draft(self.draft(tag_name='other'), self.state)

    def test_published_validation_requires_complete_assets(self):
        published = {
            'tag_name': 'v0.5.3',
            'name': 'v0.5.3',
            'draft': False,
            'assets': [{'name': n} for n in r.FILES],
        }
        r.validate_published(published, self.state)
        with self.assertRaises(ValueError):
            r.validate_published(published | {'draft': True}, self.state)
        with self.assertRaises(ValueError):
            r.validate_published(published | {'assets': []}, self.state)


if __name__ == '__main__':
    unittest.main()
