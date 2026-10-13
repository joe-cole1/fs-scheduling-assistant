"""Reject anything but the operator kit in the full ZIP, and anything persistent in the update."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import check_packages as c


class PackageRoutingTests(unittest.TestCase):
    def test_expected_layouts_are_accepted(self):
        c.validate_full_inventory(c.full_inventory())
        c.validate_update_inventory(c.update_inventory())

    def test_old_system_folder_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'exactly the operator files'):
            c.validate_full_inventory(c.full_inventory() | {c.KIT + '/System/UPLOAD THIS TO START.docx'})

    def test_practice_or_test_data_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'exactly the operator files'):
            c.validate_full_inventory(c.full_inventory() | {c.KIT + '/PRACTICE WEEK (fictional)/Inputs/Roster.csv'})

    def test_update_never_carries_squadron_rules_or_weeks(self):
        for path in (c.RULES_DOC, 'WEEKS/_COPY ME - New week/INPUT CHECKLIST.docx'):
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, 'never contain'):
                c.validate_update_inventory(c.update_inventory() | {path})

    def test_missing_task_file_is_rejected(self):
        missing = c.update_inventory() - {c.TASK_DIR + '/HELP - What do I do next.txt'}
        with self.assertRaisesRegex(ValueError, 'only replaceable'):
            c.validate_update_inventory(missing)

    def test_operator_jargon_is_rejected(self):
        for bad in ('Check the P-001 ledger', 'baseline', 'CANNOT VERIFY'):
            with self.subTest(text=bad), self.assertRaisesRegex(ValueError, 'internal jargon'):
                c.jargon_free('START HERE.docx', bad)
        c.jargon_free('START HERE.docx', 'Open a new chat and turn on DoW Policies (GAMECHANGER).')


if __name__ == '__main__':
    unittest.main()
