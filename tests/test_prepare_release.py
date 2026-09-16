"""Regression tests for manual draft-first release preparation."""
import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
SPEC = importlib.util.spec_from_file_location('prepare_release', SCRIPTS / 'prepare_release.py')
p = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(p)


class PrepareReleaseTests(unittest.TestCase):
    def _prepare_env(self, temp, version):
        return {
            'RELEASE_VERSION': version,
            'GITHUB_REPOSITORY': 'synthetic/example',
            'DEFAULT_BRANCH': 'main',
            'WORKFLOW_REF_NAME': 'main',
            'RELEASE_STATE': str(temp / 'state.json'),
            'GITHUB_OUTPUT': str(temp / 'output.txt'),
            'GITHUB_RUN_ID': '123',
            'GITHUB_SERVER_URL': 'https://github.com',
        }

    def _run(self, *args, input=None):
        if args == ('git', 'rev-parse', 'HEAD'):
            return 'a' * 40
        if args == ('git', 'rev-parse', 'origin/main'):
            return 'a' * 40
        self.fail(args)

    @staticmethod
    def _contract():
        return {
            'legacy': False,
            'requirements_path': 'release-source/packaging/requirements.txt',
            'python_version': '3.12.14',
        }

    def test_next_patch_version_uses_latest_published_stable_release(self):
        release = {'tag_name': 'v0.5.3', 'draft': False, 'prerelease': False}
        with patch.object(p.r, 'api', return_value=release):
            self.assertEqual(p.next_patch_version('synthetic/example'), ('0.5.4', 'v0.5.3'))

    def test_next_patch_version_rejects_nonstable_latest_release(self):
        for release in (
            {'tag_name': 'v0.5.3-rc.1', 'draft': False, 'prerelease': True},
            {'tag_name': 'release-five', 'draft': False, 'prerelease': False},
        ):
            with self.subTest(release=release), patch.object(p.r, 'api', return_value=release), self.assertRaises(ValueError):
                p.next_patch_version('synthetic/example')

    def test_explicit_version_input_is_release_identity(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            env = self._prepare_env(temp, '0.5.4')
            with patch.dict(os.environ, env), \
                 patch.object(p.r, 'run', side_effect=self._run), \
                 patch.object(p.r, 'validate_release_slot', return_value=None), \
                 patch.object(p.r, 'tagged_build_contract', return_value=self._contract()), \
                 patch.object(p, 'next_patch_version') as auto:
                p.prepare()

            prepared = json.loads((temp / 'state.json').read_text())
            self.assertEqual(prepared['version'], '0.5.4')
            self.assertEqual(prepared['tag'], 'v0.5.4')
            self.assertEqual(prepared['version_source'], 'manual')
            self.assertIsNone(prepared['previous_release_tag'])
            self.assertEqual(prepared['source_sha'], 'a' * 40)
            self.assertIn('package_version=0.5.4', (temp / 'output.txt').read_text())
            self.assertIn('version_source=manual', (temp / 'output.txt').read_text())
            auto.assert_not_called()

    def test_blank_version_increments_latest_patch(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            env = self._prepare_env(temp, '   ')
            with patch.dict(os.environ, env), \
                 patch.object(p.r, 'run', side_effect=self._run), \
                 patch.object(p.r, 'validate_release_slot', return_value=None) as slot, \
                 patch.object(p.r, 'tagged_build_contract', return_value=self._contract()), \
                 patch.object(p, 'next_patch_version', return_value=('0.5.4', 'v0.5.3')) as auto:
                p.prepare()

            prepared = json.loads((temp / 'state.json').read_text())
            self.assertEqual(prepared['version'], '0.5.4')
            self.assertEqual(prepared['tag'], 'v0.5.4')
            self.assertEqual(prepared['version_source'], 'automatic-patch')
            self.assertEqual(prepared['previous_release_tag'], 'v0.5.3')
            self.assertIn('package_version=0.5.4', (temp / 'output.txt').read_text())
            self.assertIn('version_source=automatic-patch', (temp / 'output.txt').read_text())
            auto.assert_called_once_with('synthetic/example')
            slot.assert_called_once_with('synthetic/example', 'v0.5.4', 'a' * 40)

    def test_non_default_workflow_ref_fails(self):
        env = {
            'RELEASE_VERSION': '0.5.4',
            'GITHUB_REPOSITORY': 'synthetic/example',
            'DEFAULT_BRANCH': 'main',
            'WORKFLOW_REF_NAME': 'feature',
        }
        with patch.dict(os.environ, env), self.assertRaisesRegex(ValueError, 'default branch'):
            p.prepare()

    def test_prerelease_version_is_rejected_explicitly(self):
        env = {'RELEASE_VERSION': '0.5.4-rc.1', 'GITHUB_REPOSITORY': 'synthetic/example'}
        with patch.dict(os.environ, env), self.assertRaisesRegex(ValueError, 'stable versions only'):
            p.prepare()

    def test_invalid_version_fails_before_release_slot(self):
        env = {'RELEASE_VERSION': '../bad', 'GITHUB_REPOSITORY': 'synthetic/example'}
        with patch.dict(os.environ, env), patch.object(p.r, 'validate_release_slot') as slot, self.assertRaises(ValueError):
            p.prepare()
        slot.assert_not_called()


if __name__ == '__main__':
    unittest.main()
