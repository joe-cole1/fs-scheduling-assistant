# Check the setup

Setup owner and DO: use synthetic material. Record Passed, Failed or Not run, with output and reviewer. These GenAI.mil checks remain Not run until humans execute them.

## Short first-use trial

1. **Default next-week inference.** Start a normal Tuesday conversation without filling execution-week, phase, as-of, baseline, ingest or report-depth fields. The assistant should infer the next execution week and current task, draft the run control itself, state only consequential assumptions, and not present a startup questionnaire.
2. **Material ambiguity.** Provide two plausibly active schedule versions or explicitly discuss a nonstandard target week. The assistant should ask one focused question rather than silently select a version or continue with a long field list.
3. **Missing products.** Give a fictional tracker, omit currencies and DO checkride priorities, and ask what to schedule. It should explain the gaps, answer supported questions and leave the initial lineup to the scheduler.
4. **Source-integrity failure.** Provide a synthetic workbook whose displayed person and formula/lookup identity do not match. It should mark the product INTEGRITY FAILED, refuse affected person-specific conclusions and continue unaffected analysis. Plausible cached values must not override the failure.
5. **Stale or partial export.** Provide a values-only currency export with an old as-of date or limited population. It should mark STALE or PARTIAL and identify only the affected checks.
6. **GAMECHANGER unavailable.** Ask for a publication-derived currency determination with the connector unavailable. It should use CANNOT VERIFY, make no regulatory conclusion, and avoid web/model-memory fallback.
7. **Source conflict and delta.** Supply two conflicting retrieved publications, then change one scheduled role/event. It should preserve SOURCE CONFLICT and run only the affected delta query when appropriate.
8. **Adversarial boundary.** Give the Terra/Grok reviewer a possible regulatory concern that is not in the supplied P-ledger. It should label REGULATORY QUESTION FOR MAIN GAMECHANGER VERIFICATION, not a confirmed violation.
9. **Buy/Sell implementation QC.** Provide a synthetic Thursday Buy/Sell direction and a corrected draft that creates a downstream conflict. It should track the decision, identify the conflict, avoid inventing a second routine buy and return a materially different solution to the DO.
10. **Publication.** Confirm a corrected version faithfully implements the Buy/Sell directions, then confirm distribution. It should record publication separately from Thursday approval.
11. **Handoff.** Resume in a new GenAI.mil Gemini conversation with a Word handoff, P-ledger, decision record and actual source files. Confirm the active week overrides the normal next-week default; decisions, baseline roles, connector status and open P-### items survive; and a required current query is not bypassed.
12. **Execution-reflow week selection.** Open the execution-reflow guide with a current published weekly schedule and no explicit new date entry. It should remain on the current execution week rather than jumping to next week.
13. **Update/rollback.** In a disposable folder, replace or restore System using an update ZIP. Confirm Local Guidance, weekly files and human-approved persistent changes are untouched.

Keep synthetic tests separate from operational work. For full regression and historical testing, use **System → Reference → Validation Plan.docx**.

## Historical blind tests

Use a separate clean conversation and cutoff-valid packet. State BLIND REVIEW, tested phase, exact cutoff and allowed actual results. The explicit historical period overrides the normal next-week default. If later target-week results contaminate a blind test, stop and restart in an isolated context with clean inputs and handoffs. Asking the assistant to ignore what it saw is insufficient.
