"""Regression tests for tag-authoritative release preparation."""
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
    def test_release_tag_is_package_version_authority(self):
        with tempfile.TemporaryDirectory() as temp:
            temp = Path(temp)
            event = temp / 'event.json'
            event.write_text('{}')
            state = temp / 'state.json'
            output = temp / 'output.txt'
            release = {
                'id': 55,
                'tag_name': 'v0.5.0',
                'draft': False,
                'immutable': False,
                'assets': [],
            }
            contract = {
                'legacy': False,
                'requirements_path': 'release-source/packaging/requirements.txt',
                'python_version': '3.12.14',
            }

            def run(*args, input=None):
                if args[:3] == ('git', 'rev-parse', 'refs/tags/v0.5.0^{commit}'):
                    return 'a' * 40
                if args[:3] == ('git', 'merge-base', '--is-ancestor'):
                    return ''
                if args == ('git', 'rev-parse', 'HEAD'):
                    return 'b' * 40
                self.fail(args)

            env = {
                'RELEASE_TAG': 'v0.5.0',
                'GITHUB_REPOSITORY': 'synthetic/example',
                'GITHUB_EVENT_PATH': str(event),
                'GITHUB_EVENT_NAME': 'workflow_dispatch',
                'RELEASE_STATE': str(state),
                'GITHUB_OUTPUT': str(output),
            }
            with patch.dict(os.environ, env), \
                 patch.object(p.r, 'api', return_value=release), \
                 patch.object(p.r, 'run', side_effect=run), \
                 patch.object(p.r, 'tagged_build_contract', return_value=contract):
                p.prepare()

            prepared = json.loads(state.read_text())
            self.assertEqual(prepared['version'], '0.5.0')
            self.assertEqual(prepared['tag'], 'v0.5.0')
            self.assertEqual(prepared['source_sha'], 'a' * 40)
            self.assertIn('package_version=0.5.0', output.read_text())

    def test_invalid_tag_still_fails(self):
        with patch.dict(os.environ, {'RELEASE_TAG': '../bad'}, clear=False), self.assertRaises(ValueError):
            p.prepare()


if __name__ == '__main__':
    unittest.main()
