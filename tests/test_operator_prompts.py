"""Guard the requested no-delegation and model-neutral prompt contract."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import build_packages as b


class OperatorPromptTests(unittest.TestCase):
    def test_missing_no_delegation_instruction_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'no-delegation'):
            b.validate_prompt('Run full schedule QC.','synthetic.txt')

    def test_named_model_requirement_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'named model'):
            b.validate_prompt(b.DELEGATION_GUARD+' Use Gemini 3.7 Flash for QC.','synthetic.txt')

    def test_guard_without_an_action_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'needs a task'):
            b.validate_prompt(b.DELEGATION_GUARD,'synthetic.txt')

    def test_unfilled_state_field_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'unfilled field'):
            b.validate_prompt(b.DELEGATION_GUARD+' Review [schedule].','synthetic.txt')

    def test_all_shipped_prompts_are_complete_and_model_neutral(self):
        for name in b.PROMPTS:
            with self.subTest(name=name):
                b.validate_prompt((b.ROOT/'packaging/prompts'/name).read_text(),name)

    def test_current_migration_does_not_reintroduce_superseded_model_roles(self):
        self.assertEqual([m['id'] for m in b.actionable_migrations()],['PERSIST-003','PERSIST-004'])
        self.assertNotIn('Gemini',b.persistent_migration_source())


if __name__=='__main__': unittest.main()
