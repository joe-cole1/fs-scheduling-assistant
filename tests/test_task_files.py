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
        self.assertEqual([m['id'] for m in b.actionable_migrations()], ['PERSIST-006'])
        self.assertNotIn('Gemini', b.persistent_migration_source())

    def test_task_file_count_stays_inside_the_simplicity_budget(self):
        self.assertLessEqual(len(b.TASKS), 10)


class SquadronRulesTests(unittest.TestCase):
    """Squadron Rules is one rule per line by category, with proposals kept apart from approved rules."""

    def good(self):
        return b.squadron_rules_source()

    def test_shipped_squadron_rules_meet_the_rule_format(self):
        counts = b.validate_squadron_rules(self.good())
        self.assertEqual(list(counts), ['PAIR', 'UPG', 'DAY', 'PPL', 'ACFT', 'BKUP', 'SUP', 'PRI'])
        self.assertEqual(sum(counts.values()), 54)

    def test_cut_off_squadron_rules_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'END marker'):
            b.validate_squadron_rules(self.good().replace(b.RULES_END_MARKER, ''))

    def test_unknown_strictness_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Unknown strictness'):
            b.validate_squadron_rules(self.good().replace('**UPG-02 (Ask the DO first).**', '**UPG-02 (Usually).**'))

    def test_duplicate_or_misfiled_rule_id_is_rejected(self):
        with self.assertRaisesRegex(ValueError, 'unique and in order'):
            b.validate_squadron_rules(self.good().replace('**UPG-02 (', '**UPG-01 ('))
        with self.assertRaisesRegex(ValueError, 'wrong category'):
            b.validate_squadron_rules(self.good().replace('**UPG-02 (', '**PAIR-09 ('))

    def test_a_retired_rule_may_leave_a_gap_in_the_numbers(self):
        lines = [line for line in self.good().splitlines() if not line.startswith('- **UPG-05 (')]
        self.assertEqual(b.validate_squadron_rules('\n'.join(lines) + '\n')['UPG'], 11)

    def test_unformatted_part_1_line_is_rejected(self):
        broken = self.good().replace('### BKUP Backups\n', '### BKUP Backups\n\n- Always have a backup.\n')
        with self.assertRaisesRegex(ValueError, 'not in rule format'):
            b.validate_squadron_rules(broken)

    def test_a_waiting_proposal_cannot_carry_a_rule_id(self):
        broken = self.good().replace('- **Proposed (PAIR, Must).** A pilot flying', '- **PAIR-05 (Must).** A pilot flying')
        with self.assertRaisesRegex(ValueError, 'must not carry a rule ID'):
            b.validate_squadron_rules(broken)

    def test_experience_rules_wait_for_the_do_and_are_not_applied_rules(self):
        rules = self.good()
        part_1 = rules.split('## Part 2 Waiting for DO approval')[0]
        waiting = rules.split('## Part 2 Waiting for DO approval')[1].split('## Part 3 Retired or rejected')[0]
        for phrase in ('Local Area Orientation (LAO) flight flies with an IP', 'flies with an IP as number 2',
                       'Avoid Monday upgrades'):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, waiting)
                self.assertNotIn(phrase, part_1)
        self.assertIn('The assistant does not apply anything in Part 2.', waiting)

    def test_change_form_specifics_live_in_squadron_rules_not_a_task_file(self):
        self.assertIn('AFIMT 2407', self.good())
        for source, title in b.TASKS:
            with self.subTest(task=title):
                self.assertNotIn('2407', b.task_file_text(source, title))


if __name__ == '__main__':
    unittest.main()
