# Thursday–Friday — Apply Buy/Sell changes

Schedulers apply the DO directions recorded at Thursday's Buy/Sell. Gemini verifies faithful implementation, complete downstream effects and affected publication-rule deltas. This is implementation QC, not a routine second buy.

Upload or identify the current decision record and corrected schedule. The assistant should infer the Buy/Sell-presented version and latest corrected version from the record, filenames and conversation. If either role is ambiguous, it should ask one focused version question.

Paste:

```text
Perform post-Buy/Sell implementation QC using the current decision record and
latest clearly identified corrected schedule. Infer the execution week,
Buy/Sell-presented version, approved directions, and prior corrected version from
the supplied record and conversation. Ask only if a version role is materially
ambiguous.

For every D-### direction show: exact scope; Open / Implemented-QC pending /
Verified / Human-confirmed / Blocked / Superseded; where it appears in the
corrected schedule; and the associated QC finding.

Distinguish DIRECTED CORRECTION from NEW PROPOSAL. Check all affected pilots,
availability, duty boundaries, qualifications, prerequisites, IP/evaluator roles,
formations, aircraft/configuration, primary lines, protected spares, simulator,
support, backups, displaced training, later events and complete resulting
schedule.

For any changed person, role, event, timing, prerequisite, currency/qualification
state or other publication-relevant fact, query DoW Policies Beta (GAMECHANGER)
for the affected rule and update/add the P-### entry. Preserve unaffected ledger
continuity. Do not use model memory or ordinary web search as fallback evidence.

If implementation is faithful and feasible, state that no routine second DO buy
is required and prepare the remaining publication-QC items. If a direction is
infeasible or the necessary solution materially exceeds the recorded scope,
return that specific issue to the DO with options for a supplemental decision.
Do not silently expand the Thursday approval.
```

**You should get:** a disposition for every direction, exact implementation differences, complete cascade QC, affected P-ledger delta results and a clear determination whether a supplemental DO decision is required.

**Next:** **10 Friday - Final QC and Publish.docx**.
