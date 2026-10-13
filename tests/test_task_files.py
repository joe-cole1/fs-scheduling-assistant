"""Guard the self-contained task-file contract: no-delegation guard, end marker, size budget, model-neutral."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import build_packages as b


class TaskFileTests(unittest.TestCase):
    def good(self):
        return b.task_file_text(*b.TASKS[0])

    def test_all_shipped_task_files_meet_the_contract(self):
        for source, title in b.TASKS:
            with self.subTest(task=title):
                b.validate_task_file(b.task_file_text(source, title), title)

    def test_missing_no_delegation_guard_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'no-delegation'):
            b.validate_task_file(self.good().replace(b.DELEGATION_GUARD, '', 1), 'synthetic')

    def test_cut_off_task_file_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'END marker'):
            b.validate_task_file(self.good()[:-200], 'synthetic')

    def test_oversize_task_file_is_rejected(self):
        padded = self.good().replace(b.END_MARKER, 'x' * b.TASK_FILE_LIMIT + '\n' + b.END_MARKER)
        with self.assertRaisesRegex(ValueError, 'size budget'):
            b.validate_task_file(padded, 'synthetic')

    def test_named_model_requirement_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'named model'):
            b.validate_task_file(self.good().replace(b.END_MARKER, 'Use Gemini 3.7 Flash.\n' + b.END_MARKER), 'synthetic')

    def test_unfilled_template_field_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'template field'):
            b.validate_task_file(self.good().replace(b.END_MARKER, '{{PROFILE}}\n' + b.END_MARKER), 'synthetic')

    def test_every_task_file_carries_the_same_core_and_week_file_format(self):
        core = b.CORE_SOURCE.read_text().strip()
        week = b.WEEK_FILE_SOURCE.read_text().strip()
        for source, title in b.TASKS:
            text = b.task_file_text(source, title)
            with self.subTest(task=title):
                self.assertIn(core, text)
                self.assertIn(week, text)
                self.assertIn('THIS TASK: ' + title, text)

    def test_squadron_rules_contains_the_approved_profile(self):
        rules = b.squadron_rules_source()
        self.assertNotIn('{{PROFILE}}', rules)
        self.assertIn('Start a new GenAI.mil conversation for each task', rules)
        self.assertIn('three countable upgrade events per week', rules)

    def test_only_the_consolidated_migration_is_current(self):
        self.assertEqual([m['id'] for m in b.actionable_migrations()], ['PERSIST-005'])
        self.assertNotIn('Gemini', b.persistent_migration_source())


if __name__ == '__main__':
    unittest.main()
