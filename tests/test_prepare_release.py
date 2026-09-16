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
    def test_version_input_is_release_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            state = temp / 'state.json'
            output = temp / 'output.txt'
            contract = {
                'legacy': False,
                'requirements_path': 'release-source/packaging/requirements.txt',
                'python_version': '3.12.14',
            }

            def run(*args, input=None):
                if args == ('git', 'rev-parse', 'HEAD'):
                    return 'a' * 40
                if args == ('git', 'rev-parse', 'origin/main'):
                    return 'a' * 40
                self.fail(args)

            env = {
                'RELEASE_VERSION': '0.5.3',
                'GITHUB_REPOSITORY': 'synthetic/example',
                'DEFAULT_BRANCH': 'main',
                'WORKFLOW_REF_NAME': 'main',
                'RELEASE_STATE': str(state),
                'GITHUB_OUTPUT': str(output),
                'GITHUB_RUN_ID': '123',
                'GITHUB_SERVER_URL': 'https://github.com',
            }
            with patch.dict(os.environ, env), \
                 patch.object(p.r, 'run', side_effect=run), \
                 patch.object(p.r, 'validate_release_slot', return_value=None), \
                 patch.object(p.r, 'tagged_build_contract', return_value=contract):
                p.prepare()

            prepared = json.loads(state.read_text())
            self.assertEqual(prepared['version'], '0.5.3')
            self.assertEqual(prepared['tag'], 'v0.5.3')
            self.assertEqual(prepared['source_sha'], 'a' * 40)
            self.assertIn('package_version=0.5.3', output.read_text())
            self.assertIn('tag=v0.5.3', output.read_text())

    def test_non_default_workflow_ref_fails(self):
        env = {
            'RELEASE_VERSION': '0.5.3',
            'GITHUB_REPOSITORY': 'synthetic/example',
            'DEFAULT_BRANCH': 'main',
            'WORKFLOW_REF_NAME': 'feature',
        }
        with patch.dict(os.environ, env), self.assertRaisesRegex(ValueError, 'default branch'):
            p.prepare()

    def test_invalid_version_fails_before_network(self):
        with patch.dict(os.environ, {'RELEASE_VERSION': '../bad'}, clear=False), self.assertRaises(ValueError):
            p.prepare()


if __name__ == '__main__':
    unittest.main()
