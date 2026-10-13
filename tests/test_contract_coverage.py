"""Prove the compressed task files still carry every non-negotiable contract (AGENTS.md and design decisions)."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import build_packages as b

# Contracts every task file must carry (they live in the shared core or WEEK FILE format).
EVERY_TASK = {
    'no delegation': 'Do not delegate to subagents.',
    'humans own the schedule': 'Humans build, edit, coordinate, approve and publish the schedule.',
    'no assistant lineup': 'never build the initial complete lineup',
    'Thursday formal buy': 'THURSDAY BUY/SELL IS THE FORMAL DO BUY',
    'no routine second buy': 'NO routine second DO buy',
    'supplemental decision': 'supplemental decision before publication',
    'publication separate': 'Publication is a separate human action.',
    'daily authority': ('Daily scheduler and Top 3 sign-off covers feasible personnel and mission changes within the '
                        'published flying times, aircraft turn pattern, coordinated support and explicit DO guidance'),
    'waiver routing': 'Every waiver goes through the DO AND the applicable waiver authority.',
    'human confirmation scope': 'Record it as Human-confirmed, not independently verified.',
    'confirmation is not source evidence': 'never turns missing regulation evidence into SOURCE-BACKED OK',
    'weekly notes limits': 'Weekly DO notes may override standing preferences only explicitly',
    'no invented hierarchy': 'Never invent a source hierarchy.',
    'proposed guidance label': 'PROPOSED - NOT ISSUED',
    'GAMECHANGER only': 'ONLY from an applicable publication retrieved through DoW Policies Beta (GAMECHANGER)',
    'no memory or web fallback': ('Model memory, remembered Air Force guidance, generic military knowledge, ordinary web '
                                  'search, uncited AI synthesis and earlier answers are NOT acceptable regulatory evidence.'),
    'outcome OK': 'SOURCE-BACKED OK: ',
    'outcome ISSUE': 'SOURCE-BACKED ISSUE: ',
    'outcome CANNOT VERIFY': 'CANNOT VERIFY: ',
    'outcome SOURCE CONFLICT': 'SOURCE CONFLICT: ',
    'no assumed pass': 'Never turn CANNOT VERIFY into a pass.',
    'no compliance claim': 'Never say a schedule is "fully compliant."',
    'bounded wording': 'No source-backed conflicts found in the checks performed',
    'ledger cadence': 'Thursday full QC re-queries, refreshes and expands it against the complete near-final schedule.',
    'ledger is not a bypass': 'Earlier entries in the WEEK FILE are continuity, never permission to skip a required query.',
    'evidence grants nothing': 'It never grants approval or a waiver',
    'product statuses': 'CURRENT, STALE, PARTIAL, CONFLICTED, INTEGRITY FAILED, UNREADABLE or SUPERSEDED',
    'integrity gate': "Don't use the affected values just because they look plausible.",
    'upload is not a request': 'Uploading a file never starts a review by itself.',
    'no personal explanations': 'Never ask for diagnoses, leave reasons or other personal explanations.',
    'conservative availability': 'Conflicting availability and tentative leave mean unavailable until resolved.',
    'qualification evidence': 'Never infer qualification from rank, title or callsign.',
    'protected spares': 'Protected spares are replacement capacity, never planned extra primary lines.',
    'no self backup': "An upgradee can't back up their own upgrade event.",
    'complete cascades': 'Never call a partial cascade executable.',
    'post buy churn': "final-QC limits apply",
    'flown is not credit': 'Never treat "flown" as passed or credited',
    'moderate downside': 'Keep one moderate downside scenario each week',
    '30-day outlook': 'Weekly analysis includes a 30-day outlook',
    'playbook governance': 'Only an explicit DO approval promotes a lesson.',
    'blind test restart': 'require a clean restart in a new chat',
    'daily comparison per date': 'latest signed daily schedule for EACH affected date',
    'cumulative comparison': 'Execution cumulative changes: compare to the published weekly schedule.',
    'no weekday approval': 'Never infer a buy, publication or daily sign-off from a weekday',
    'explicit versions': 'never choose silently between competing versions',
    'next-week default': 'default to the NEXT execution week',
    'no startup questionnaire': "Don't present a startup questionnaire",
    'nothing hidden': 'Never hide or drop a serious issue',
    'one next action': 'YOUR NEXT STEP:',
    'no claimed saving': 'Never say or imply that you saved, sent, coordinated, approved, signed or published anything.',
    'WEEK FILE end marker': '=== END OF WEEK FILE ===',
    'WEEK FILE counts': 'COUNTS: decisions=N',
    'carry every entry': 'Carry forward EVERY existing entry with its existing ID.',
}

# Contracts specific to one task file.
TASK_SPECIFIC = {
    '1 TUESDAY - Plan next week': ['Do not build a lineup.', 'Create stable P-### entries'],
    '2 WEDNESDAY - Check my draft': ['is NOT a buy, a Buy/Sell or an approval', 'this is not Thursday\'s full QC'],
    '3 THURSDAY - Full QC': ['Run a FRESH review of the ENTIRE exact schedule', '[BUY READY]', '[READY WITH DO DECISIONS]',
                             '[NOT READY]', 'ACTUALLY scheduled in the candidate', 'Uploading a file never starts a review'],
    '4 THURSDAY - Buy-Sell': ['ONLY when the DO explicitly approves', 'Never infer approval.', 'NOT BOUGHT',
                              'Raw reviewer output is never direction.'],
    '5 THU-FRI - Check changes and publish': ['There is NO routine second DO buy.', 'DIRECTED CORRECTION or NEW PROPOSAL',
                                              'Never infer publication from approval'],
    '6 EXECUTION WEEK - Schedule change': ['Never switch to next-week planning.',
                                           'Never say any of these happened unless a human confirms it.'],
    'DO ONLY - Independent review': ['REGULATORY QUESTION FOR MAIN GAMECHANGER VERIFICATION', 'Do NOT produce a WEEK FILE',
                                     '[NO MATERIAL OBJECTION]', '[REVIEW ADVISED]', '[MATERIAL CONCERN]'],
    'HELP - What do I do next': ['Never invent a decision.', 'do NOT produce a WEEK FILE'],
}


class ContractCoverageTests(unittest.TestCase):
    def test_every_task_file_carries_every_shared_contract(self):
        for source, title in b.TASKS:
            text = b.task_file_text(source, title)
            for contract, phrase in EVERY_TASK.items():
                with self.subTest(task=title, contract=contract):
                    self.assertIn(phrase, text)

    def test_task_specific_contracts(self):
        titles = {title: source for source, title in b.TASKS}
        self.assertEqual(set(TASK_SPECIFIC), set(titles))
        for title, phrases in TASK_SPECIFIC.items():
            text = b.task_file_text(titles[title], title)
            for phrase in phrases:
                with self.subTest(task=title, phrase=phrase):
                    self.assertIn(phrase, text)


if __name__ == '__main__':
    unittest.main()
