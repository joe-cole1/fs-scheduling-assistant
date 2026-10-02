"""Reject setup materials leaking into the weekly operational System."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import check_packages as c


class PackageRoutingTests(unittest.TestCase):
    def test_weekly_system_is_accepted(self):
        c.validate_operational_inventory(c.operational_inventory())

    def test_first_time_guide_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'weekly operational'):
            c.validate_operational_inventory(c.operational_inventory()|{'System/Instructions/01 First time setup.docx'})

    def test_setup_prompt_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'weekly operational'):
            c.validate_operational_inventory(c.operational_inventory()|{'System/Prompts/01_First_Time_Setup.txt'})

    def test_blank_guidance_duplicates_are_rejected(self):
        for name in ('04 Stable References.docx','09 Playbook.docx'):
            with self.subTest(name=name),self.assertRaisesRegex(ValueError,'weekly operational'):
                c.validate_operational_inventory(c.operational_inventory()|{'System/Blank Forms/'+name})

    def test_setup_validation_reference_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'weekly operational'):
            c.validate_operational_inventory(c.operational_inventory()|{'System/Reference/Validation Plan.docx'})


if __name__=='__main__':unittest.main()
