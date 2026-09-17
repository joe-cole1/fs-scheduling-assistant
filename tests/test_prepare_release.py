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

    def test_explicit_version_must_match_source_identity(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            env = self._prepare_env(temp, '0.5.6')
            with patch.dict(os.environ, env), \
                 patch.object(p, 'source_version', return_value='0.5.6'), \
                 patch.object(p.r, 'run', side_effect=self._run), \
                 patch.object(p.r, 'validate_release_slot', return_value=None), \
                 patch.object(p.r, 'tagged_build_contract', return_value=self._contract()):
                p.prepare()

            prepared = json.loads((temp / 'state.json').read_text())
            self.assertEqual(prepared['version'], '0.5.6')
            self.assertEqual(prepared['tag'], 'v0.5.6')
            self.assertEqual(prepared['version_source'], 'explicit-match')
            self.assertEqual(prepared['source_sha'], 'a' * 40)
            self.assertIn('package_version=0.5.6', (temp / 'output.txt').read_text())
            self.assertIn('version_source=explicit-match', (temp / 'output.txt').read_text())

    def test_blank_version_uses_source_version(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            env = self._prepare_env(temp, '   ')
            with patch.dict(os.environ, env), \
                 patch.object(p, 'source_version', return_value='0.5.6'), \
                 patch.object(p.r, 'run', side_effect=self._run), \
                 patch.object(p.r, 'validate_release_slot', return_value=None) as slot, \
                 patch.object(p.r, 'tagged_build_contract', return_value=self._contract()):
                p.prepare()

            prepared = json.loads((temp / 'state.json').read_text())
            self.assertEqual(prepared['version'], '0.5.6')
            self.assertEqual(prepared['tag'], 'v0.5.6')
            self.assertEqual(prepared['version_source'], 'source')
            self.assertIn('package_version=0.5.6', (temp / 'output.txt').read_text())
            self.assertIn('version_source=source', (temp / 'output.txt').read_text())
            slot.assert_called_once_with('synthetic/example', 'v0.5.6', 'a' * 40)

    def test_explicit_version_mismatch_fails_before_release_slot(self):
        env = {
            'RELEASE_VERSION': '0.5.5',
            'GITHUB_REPOSITORY': 'synthetic/example',
        }
        with patch.dict(os.environ, env), \
             patch.object(p, 'source_version', return_value='0.5.6'), \
             patch.object(p.r, 'validate_release_slot') as slot, \
             self.assertRaisesRegex(ValueError, 'does not match packaging/version.txt'):
            p.prepare()
        slot.assert_not_called()

    def test_non_default_workflow_ref_fails(self):
        env = {
            'RELEASE_VERSION': '',
            'GITHUB_REPOSITORY': 'synthetic/example',
            'DEFAULT_BRANCH': 'main',
            'WORKFLOW_REF_NAME': 'feature',
        }
        with patch.dict(os.environ, env), patch.object(p, 'source_version', return_value='0.5.6'), self.assertRaisesRegex(ValueError, 'default branch'):
            p.prepare()

    def test_prerelease_version_is_rejected_explicitly(self):
        env = {'RELEASE_VERSION': '0.5.6-rc.1', 'GITHUB_REPOSITORY': 'synthetic/example'}
        with patch.dict(os.environ, env), patch.object(p, 'source_version', return_value='0.5.6'), self.assertRaisesRegex(ValueError, 'stable versions only'):
            p.prepare()

    def test_prerelease_source_version_is_rejected(self):
        with patch.object(Path, 'read_text', return_value='0.5.6-rc.1\n'), self.assertRaisesRegex(ValueError, 'stable version'):
            p.source_version()

    def test_invalid_version_fails_before_release_slot(self):
        env = {'RELEASE_VERSION': '../bad', 'GITHUB_REPOSITORY': 'synthetic/example'}
        with patch.dict(os.environ, env), \
             patch.object(p, 'source_version', return_value='0.5.6'), \
             patch.object(p.r, 'validate_release_slot') as slot, \
             self.assertRaises(ValueError):
            p.prepare()
        slot.assert_not_called()


if __name__ == '__main__':
    unittest.main()
