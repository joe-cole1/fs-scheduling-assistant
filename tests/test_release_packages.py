"""Regression checks for publication integrity; no network or release mutations."""
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


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name) / 'downloads'
        self.folder.mkdir()
        manifest = {'package_version': '0.4.1', 'packages': {}}
        for name in r.ZIPS:
            data = ('synthetic bytes: ' + name).encode()
            (self.folder / name).write_bytes(data)
            manifest['packages'][name] = {'sha256': hashlib.sha256(data).hexdigest()}
        (self.folder / 'manifest.json').write_text(json.dumps(manifest))
        self.release = {'id': 7, 'tag_name': 'v0.4.1', 'draft': False, 'immutable': False, 'assets': [], 'body': 'Human notes.'}
        self.state = {'repo': 'synthetic/example', 'id': 7, 'tag': 'v0.4.1', 'version': '0.4.1', 'source_sha': 'a' * 40, 'controller_sha': 'b' * 40}

    def test_tag_and_version(self):
        r.validate_release(self.release, 'v0.4.1', '0.4.1')
        for tag, version in [('v0.4.2', '0.4.1'), ('v0.4.1', '0.4.2'), ('v0.4.1; touch bad', '0.4.1'), ('../v0.4.1', '0.4.1')]:
            with self.subTest(tag=tag, version=version), self.assertRaises(ValueError):
                r.validate_release(self.release, tag, version)

    def test_draft_and_immutable(self):
        for changes in ({'draft': True}, {'immutable': True}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                r.validate_release(self.release | changes, 'v0.4.1', '0.4.1')
        r.validate_release(self.release | {'immutable': True, 'assets': [{'name': n} for n in r.FILES]}, 'v0.4.1', '0.4.1')

    def test_prerelease_requires_matching_source_version(self):
        release = self.release | {'tag_name': 'v0.4.2-rc.1', 'prerelease': True}
        r.validate_release(release, 'v0.4.2-rc.1', '0.4.2-rc.1')

    def test_checksum_and_inventory(self):
        r.verify_build(self.folder, '0.4.1')
        self.assertEqual(len((self.folder / 'SHA256SUMS.txt').read_text().splitlines()), 4)
        (self.folder / r.ZIPS[0]).write_bytes(b'changed')
        with self.assertRaises(ValueError):
            r.verify_build(self.folder, '0.4.1')

    def test_wrong_version_and_extra_file(self):
        with self.assertRaises(ValueError):
            r.verify_build(self.folder, '0.4.2')
        (self.folder / 'unrelated.txt').write_text('not authorized for attachment')
        with self.assertRaises(ValueError):
            r.verify_build(self.folder, '0.4.1')

    def test_rerun_only_uploads_missing_files(self):
        r.verify_build(self.folder, '0.4.1')
        release = self.release | {'assets': [{'name': r.ZIPS[0]}]}
        missing = r.asset_plan(release, self.folder, lambda n: (self.folder / n).read_bytes())
        self.assertEqual(missing, list(r.FILES[1:]))
        with self.assertRaises(ValueError):
            r.asset_plan(release, self.folder, lambda _: b'different published bytes')

    def test_duplicate_assets_fail(self):
        r.verify_build(self.folder, '0.4.1')
        release = self.release | {'assets': [{'name': r.ZIPS[0]}] * 2}
        with self.assertRaises(ValueError):
            r.asset_plan(release, self.folder, lambda n: (self.folder / n).read_bytes())

    def test_notes_preserve_human_text_and_are_idempotent(self):
        r.verify_build(self.folder, '0.4.1')
        human = '## Operator impact\n\nKeep this exact human decision.\n'
        first = r.notes(human, self.state, self.folder)
        self.assertTrue(first.startswith(human))
        self.assertEqual(first, r.notes(first, self.state, self.folder))
        self.assertEqual(first.count(r.START), 1)
        self.assertIn('/releases/download/v0.4.1/Pantons_Setup.zip', first)
        self.assertIn(hashlib.sha256((self.folder / r.ZIPS[0]).read_bytes()).hexdigest(), first)
        self.assertIn('does not establish visual review', first)

    def test_malformed_notes_fail_without_discarding_text(self):
        for body in (r.START + 'human', r.END + r.START, r.START * 2 + r.END):
            with self.subTest(body=body), self.assertRaises(ValueError):
                r.without_download_block(body)

    def publication_mocks(self, *, mismatch=False, moved=False):
        r.verify_build(self.folder, '0.4.1')
        state_file = Path(self.temp.name) / 'state.json'
        state_file.write_text(json.dumps(self.state))
        assets = {r.ZIPS[0]: b'changed' if mismatch else (self.folder / r.ZIPS[0]).read_bytes()}
        patches, uploads = [], []
        def api(endpoint, method='GET', payload=None):
            if '/git/ref/tags/' in endpoint:
                return {'object': {'type': 'commit', 'sha': 'c' * 40 if moved else self.state['source_sha']}}
            if method == 'PATCH':
                patches.append(payload)
                return {}
            if '/generate-notes' in endpoint:
                self.fail('Human notes must not be replaced by generated PR notes')
            return self.release | {'assets': [{'name': n} for n in assets]}
        def run(*args, input=None):
            if args[0] == 'git':
                return self.state['source_sha']
            if args[2] == 'download':
                name = args[args.index('--pattern') + 1]
                (Path(args[args.index('--dir') + 1]) / name).write_bytes(assets[name])
            elif args[2] == 'upload':
                self.assertNotIn('--clobber', args)
                for path in args[4:args.index('--repo')]:
                    uploads.append(Path(path).name)
                    assets[Path(path).name] = Path(path).read_bytes()
            else:
                self.fail(args)
            return ''
        env = {'RELEASE_STATE': str(state_file), 'PACKAGE_OUTPUT': self.temp.name,
               'GITHUB_STEP_SUMMARY': str(Path(self.temp.name) / 'summary')}
        return env, api, run, patches, uploads

    def test_publication_resumes_then_verifies_and_preserves_notes(self):
        env, api, run, edits, uploads = self.publication_mocks()
        with patch.dict(os.environ, env), patch.object(r, 'api', side_effect=api), patch.object(r, 'run', side_effect=run):
            r.publish()
        self.assertEqual(uploads, list(r.FILES[1:]))
        self.assertEqual(len(edits), 1)
        self.assertTrue(edits[0]['body'].startswith('Human notes.'))

    def test_mismatch_or_moved_tag_makes_no_writes(self):
        for flags in ({'mismatch': True}, {'moved': True}):
            with self.subTest(flags=flags):
                env, api, run, edits, uploads = self.publication_mocks(**flags)
                with patch.dict(os.environ, env), patch.object(r, 'api', side_effect=api), patch.object(r, 'run', side_effect=run), self.assertRaises(ValueError):
                    r.publish()
                self.assertEqual(edits, [])
                self.assertEqual(uploads, [])

    def test_prepare_uses_tagged_version_and_rejects_unmerged_source(self):
        repo = Path(self.temp.name) / 'repo'
        repo.mkdir()
        def git(*args):
            return subprocess.run(['git', '-C', str(repo), *args], check=True, capture_output=True, text=True).stdout.strip()
        git('init', '-b', 'main')
        git('config', 'user.email', 'synthetic@example.invalid')
        git('config', 'user.name', 'Synthetic Test')
        (repo / 'packaging').mkdir()
        (repo / 'packaging/version.txt').write_text('0.4.1\n')
        git('add', '.')
        git('commit', '-m', 'Synthetic released source')
        git('tag', 'v0.4.1')
        expected = git('rev-parse', 'HEAD')
        event = Path(self.temp.name) / 'event.json'
        event.write_text('{}')
        state = Path(self.temp.name) / 'prepared.json'
        env = {'RELEASE_TAG': 'v0.4.1', 'GITHUB_REPOSITORY': 'synthetic/example',
               'GITHUB_EVENT_PATH': str(event), 'GITHUB_EVENT_NAME': 'workflow_dispatch',
               'RELEASE_STATE': str(state), 'GITHUB_OUTPUT': str(Path(self.temp.name) / 'outputs')}
        original = Path.cwd()
        try:
            os.chdir(repo)
            with patch.dict(os.environ, env), patch.object(r, 'api', return_value=self.release):
                r.prepare()
            self.assertEqual(json.loads(state.read_text())['source_sha'], expected)
            git('checkout', '-b', 'unmerged')
            (repo / 'packaging/version.txt').write_text('0.4.2\n')
            git('commit', '-am', 'Unmerged source')
            git('tag', 'v0.4.2')
            git('checkout', 'main')
            state.unlink()
            with patch.dict(os.environ, env | {'RELEASE_TAG': 'v0.4.2'}), patch.object(r, 'api', return_value=self.release | {'tag_name': 'v0.4.2'}), self.assertRaises(subprocess.CalledProcessError):
                r.prepare()
            self.assertFalse(state.exists())
        finally:
            os.chdir(original)

    def test_empty_notes_use_generated_pr_notes(self):
        self.release['body'] = ''
        env, api, run, edits, uploads = self.publication_mocks()
        def with_generated(endpoint, method='GET', payload=None):
            if '/generate-notes' in endpoint:
                self.assertEqual(payload, {'tag_name': 'v0.4.1'})
                return {'body': '## Changes\n\nSynthetic PR list and contributor credit.'}
            return api(endpoint, method, payload)
        with patch.dict(os.environ, env), patch.object(r, 'api', side_effect=with_generated), patch.object(r, 'run', side_effect=run):
            r.publish()
        self.assertIn('Synthetic PR list and contributor credit.', edits[0]['body'])


if __name__ == '__main__':
    unittest.main()
