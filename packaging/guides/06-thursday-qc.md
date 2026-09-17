# Thursday — Full schedule QC

Thursday is the deliberate QC day. First conduct normal human scheduler QC. Then identify the exact near-final schedule version and ask Gemini to review the **entire schedule from scratch**, not merely the latest edits.

Upload or identify any products revised since Wednesday plus current DO/Flt CC guidance and unresolved questions. Also identify the Tuesday **Weekly Publication Rule Ledger** if it exists. Thursday does not blindly inherit Tuesday's regulatory conclusions; Gemini re-queries GAMECHANGER against the actual near-final schedule.

Paste:

```text
Thursday — full QC. Phase 2 INITIAL DRAFT.
Primary scheduler workflow: Gemini.
Active schedule: [exact filename/version].
Comparison baseline: [exact earlier filename/version, or NONE].
As of: [date/time/timezone].
Use DETAILED output and CONFLICTS ONLY ingestion.

Perform a fresh full-schedule review. Do not limit the review to recent edits.
First verify hard constraints, availability, local scheduling rules,
aircraft/configuration, simulator capacity and required support.
Then verify that checkrides/evaluations, directed DV or senior-leader flyers,
priority upgrades and other DO priorities are placed appropriately. Do not infer
qualification or priority from rank/title alone; use supplied guidance and the
Letter of Xs for person-specific status.

Run a separate publication-grounded QC pass using DoW Policies Beta
(GAMECHANGER). Refresh and expand the Weekly Publication Rule Ledger against the
people, roles, events, timing and prerequisites actually present in this schedule.
For every publication-based currency, qualification, crew-rest/duty, evaluation,
syllabus/prerequisite, event-credit or recurring-training determination:
- retrieve the applicable publication through GAMECHANGER;
- identify publication number/title and paragraph/page/usable locator;
- record version/effective/current status when available;
- check available evidence for supersession, more-specific applicable guidance
  and conflicting sources; and
- classify the result SOURCE-BACKED OK, SOURCE-BACKED ISSUE, CANNOT VERIFY or
  SOURCE CONFLICT.

Do NOT use model memory, generic military knowledge or ordinary web search as
regulatory evidence. If GAMECHANGER does not provide a sufficiently traceable
applicable publication, mark CANNOT VERIFY and make no regulatory conclusion.
Do not claim the schedule is fully compliant. If accurate, say only: “No
source-backed conflicts found in the checks performed,” followed by every CANNOT
VERIFY and SOURCE CONFLICT item.

Review upgrade sequence and pace, instructor/evaluator placement, IP workload,
formations/backups, primary-line use, configuration/support, weather placement,
and the 30-day outlook. Identify unused feasible training opportunities.
For every recommended change, trace the full second- and third-order cascade and
state displaced training or new risk. Re-run affected publication checks when a
proposed cascade changes a person, role, event, timing or prerequisite. Include
one moderate downside case. Recommend the minimum set of changes that materially
improves the schedule. Do not modify the schedule or imply that a recommendation
is approved.
```

**You should get:** a complete normal scheduling QC report plus a distinct publication-grounded QC section, refreshed P-### rule ledger, ranked issues, exact recommended corrections, unresolved decisions and remaining risk. Humans make corrections. If corrections are material, identify the new active version and recheck affected cascades and affected GAMECHANGER rules before the buy/sell.

The normal next step is **08 Thursday - Schedule Buy-Sell.docx**. The DO may first choose the separate optional **07 Thursday - DO Adversarial Review.docx**.