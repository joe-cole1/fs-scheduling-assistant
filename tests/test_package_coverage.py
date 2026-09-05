"""Focused tests for Markdown-to-DOCX source coverage checks."""
import importlib.util
from pathlib import Path
import sys
import unittest

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
SPEC = importlib.util.spec_from_file_location('package_checks', SCRIPTS / 'check_packages.py')
c = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c)


class SourceCoverageTests(unittest.TestCase):
    def test_missing_prose_fails(self):
        with self.assertRaises(AssertionError):
            c.source_coverage('# Title\n\nCritical operator sentence.', 'Title')

    def test_missing_prompt_fails(self):
        source = '# Guide\n\n```text\nFirst required prompt line.\nSecond required prompt line.\n```\n'
        with self.assertRaises(AssertionError):
            c.source_coverage(source, 'Guide First required prompt line.')

    def test_missing_table_row_label_fails(self):
        source = '| Topic | Value |\n| --- | --- |\n| Important constraint | [value] |\n'
        with self.assertRaises(AssertionError):
            c.source_coverage(source, 'Topic Value')

    def test_complete_fragments_pass(self):
        source = '# Guide\n\nImportant sentence.\n\n| Topic | Value |\n| --- | --- |\n| Important constraint | [value] |\n'
        c.source_coverage(source, 'Guide Important sentence. Topic Value Important constraint')


if __name__ == '__main__':
    unittest.main()
