"""Regression tests for persistent installed-state migration declarations."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
SPEC = importlib.util.spec_from_file_location('persistent', SCRIPTS / 'check_persistent_migrations.py')
p = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(p)


class PersistentMigrationTests(unittest.TestCase):
    def test_current_manifest_matches_registered_sources(self):
        manifest = p.validate_current()
        self.assertIn('pantons_local_profile', manifest['artifacts'])
        self.assertEqual(manifest['artifacts']['weekly_folder_layout']['directories'], ['Inputs','Schedules','Working Record'])

    def test_source_fingerprint_detects_undeclared_edit(self):
        manifest = p.load_manifest()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'packaging').mkdir()
            for spec in manifest['artifacts'].values():
                if 'source' not in spec:
                    continue
                src = p.ROOT / spec['source']
                dst = root / spec['source']
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(src.read_bytes())
            (root / 'packaging/persistent-artifacts.json').write_text(
                (p.ROOT / 'packaging/persistent-artifacts.json').read_text()
            )
            changed = root / manifest['artifacts']['pantons_local_profile']['source']
            changed.write_text(changed.read_text() + '\nintentional change\n')
            with self.assertRaisesRegex(ValueError, 'changed without updating'):
                p.validate_current(root)

    def test_persistent_change_requires_version_and_migration(self):
        previous = p.load_manifest()
        current = copy.deepcopy(previous)
        current['artifacts']['pantons_local_profile']['git_blob_sha'] = '1' * 40
        with self.assertRaisesRegex(ValueError, 'new package version'):
            p.validate_change_declaration(previous,current,'0.4.1','0.4.1')
        with self.assertRaisesRegex(ValueError, 'appended migration record'):
            p.validate_change_declaration(previous,current,'0.4.1','0.4.2')

    def test_declared_review_and_merge_migration_covers_change(self):
        previous = p.load_manifest()
        current = copy.deepcopy(previous)
        current['artifacts']['pantons_local_profile']['git_blob_sha'] = '1' * 40
        current['migrations'].append({
            'id': 'PERSIST-001',
            'introduced_in': '0.4.2',
            'artifacts': ['pantons_local_profile'],
            'action': 'review-and-merge',
            'summary': 'Synthetic policy-seed migration.',
            'instructions': ['Review the new seed and explicitly merge approved changes.'],
        })
        changed = p.validate_change_declaration(previous,current,'0.4.1','0.4.2')
        self.assertEqual(changed, {'pantons_local_profile'})

    def test_migration_history_is_append_only(self):
        previous = p.load_manifest()
        current = copy.deepcopy(previous)
        current['migrations'][0]['summary'] = 'rewritten history'
        with self.assertRaisesRegex(ValueError, 'append-only'):
            p.validate_change_declaration(previous,current,'0.4.1','0.4.2')


if __name__ == '__main__':
    unittest.main()
