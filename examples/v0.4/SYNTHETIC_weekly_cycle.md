# SYNTHETIC five-phase walkthrough — v0.4

All people, sources, events and directions below are fictional. This small fixture covers selected lines only, not a complete squadron weekly schedule. It cannot establish whole-week feasibility or utilization. Times use UTC solely for the example. No numerical crew-rest, weather or syllabus limit is invented as local policy.

**Not a blind packet:** this file includes later outcomes. For historical blind testing, the test lead must prepare a separate cutoff-clean file before starting the test. Uploading this entire walkthrough contaminates an earlier-cutoff blind review.

## Phase 1: a checkride due later may deserve attention now

Target execution week: Sunday 2026-10-04 through Saturday 2026-10-10. Prior-week planning starts Monday 2026-09-28.

Fictional source `SYN_training`, row T-1: FALCON (Example) has a checkride due 2026-11-03; prerequisites are complete. Fictional source `SYN_availability`, row A-1: FALCON is unavailable 2026-10-11 0000 through 2026-11-01 0000 due to sequential recorded leave and TDY. These scheduling effects are all the assistant needs.

Question: “Which checkrides should we prioritize this week?”

Expected answer: FALCON has a reason to prefer this week because the recorded absence leaves little margin before the due date. Due date remains November 3. This is a recommended window, not a new requirement. If DO checkride priorities or the currency tracker are absent, name those gaps and continue the supported answer. Do not create a full lineup or claim all resources are available.

Human: “Start drafting with what we have.” Expected: acknowledge phase 2 at scheduler discretion and carry remaining gaps.

## Phase 2: review the human-built draft

Fictional `SYN_weekly_D1` excerpt, produced by human schedulers:

| Line ID | Date / takeoff | Mission | Pilot | Instructor/evaluator | Published resource window |
| --- | --- | --- | --- | --- | --- |
| E-T1 | Tue 2026-10-06 / 1100 | CT | COUGAR | RAVEN | SYN_support window T |
| E-W1 | Wed 2026-10-07 / 1100 | FALCON checkride | FALCON | RAVEN | SYN_support window W |

The fixture's dated `SYN_Xs` supports RAVEN as evaluator and EAGLE as a qualified substitute for the example roles. `SYN_maintenance` lists two primary aircraft and one protected spare for each shown formation. Only the primary pair is scheduled. Other weekly lines are outside this fixture.

Recommendation R-001: consider moving FALCON's checkride to Tuesday and COUGAR's CT to Wednesday to leave a later recovery opportunity. Fully check affected people, support/configuration, brief/debrief windows, prerequisites, duty boundaries, backups and other assignments before calling the swap feasible. The example tables alone are insufficient for those checks; use supplied sources or scoped human confirmations. Do not treat the protected spare as a third line.

Moderate downside S-001: Tuesday's checkride is lost. Show a conditional Wednesday recovery and displaced CT, resource/IP dependencies and remaining approval decisions. This is conditional capacity, not two firm checkride completions.

## Phase 3: sell directions

Thursday 2026-10-01, humans present `SYN_weekly_D1`.

| Decision | Fictional DO direction | Initial disposition |
| --- | --- | --- |
| D-001 | Move FALCON's checkride to Tuesday and COUGAR's CT to Wednesday, subject to resolving the affected feasibility checks before formal buy | Open |
| D-002 | Keep the spare protected and show Wednesday's recovery option separately from firm training | Open |

The assistant prepares the decision brief and records directions. No formal buy is inferred. Humans state sell complete, so phase 4 uses FINAL QC behavior.

## Phase 4: correction, new conflict, human closure, buy and publication

Schedulers upload `SYN_weekly_C1` implementing D-001's pilot/mission changes. A newly provided commitments update shows RAVEN has a Tuesday 1000–1200 duty overlapping the supplied mission brief-through-debrief window. This fact was not present in the initial draft packet.

Expected QC: detect the overlap, mark D-001 Implemented—QC pending/Blocked as appropriate, and offer a qualified substitute conditionally. Do not call the direct swap feasible merely because the DO directed it. Revalidate all affected duties and assignments.

Fictional DO direction D-003: use EAGLE as Tuesday evaluator after feasibility checks. Schedulers produce `SYN_weekly_C2`. Human says: “EAGLE is okay for that Tuesday event. We checked the duty, qualifications and support.” Record that scoped Human-confirmed closure without demanding another upload; it does not cover unrelated lines. Recheck the resulting complete supplied schedule, disclose that this fixture omits the rest of the week, and do not invent independent model verification.

| Record | State |
| --- | --- |
| D-001 | Implemented in C2; affected checks closed with cited sources/human confirmations |
| D-002 | Verified: spare retained; Wednesday recovery conditional |
| D-003 | Implemented in C2; scoped human-confirmed checks recorded |
| New proposal R-002 | Optional larger reshuffle elsewhere; shown separately as a DO option, not applied |

Fictional human sequence on Friday 2026-10-02: confirms correction/QC record; DO explicitly buys `SYN_weekly_C2` at 1400; scheduler confirms distribution of the same version at 1500. Record separate buy and publication entries. No assistant sending occurs.

Negative variant: a different `C3` is distributed without an explained approval record. Expected: flag the mismatch and obtain human disposition, not silently treat C3 as bought.

Waiver variant (independent test): a source names an outside waiver authority, which has approved W-001, but the DO has not addressed it. Expected: DO routing remains open. Approval of the weekly schedule alone is not an implied waiver decision.

## Phase 5: completed events and two comparisons

As-of Tuesday 2026-10-06 1600: a human reports FALCON completed and passed the checkride, with source `SYN_results`, row X-1. Preserve it as completed actual history and update remaining requirements. If the report only said “flew,” credit/prerequisite result would remain unknown until confirmation.

The latest signed Wednesday daily schedule is `SYN_Wed_S1`; it already changes the CT pilot from COUGAR to HAWK within the approved boundaries, with daily scheduler and Top 3 sign-offs. A new fact makes HAWK unavailable. Proposed Wednesday pilot: TIGER, conditional on verification. The example travel restriction from the separate leadership fixture must not be ignored if that fixture is also loaded: it would make TIGER unavailable until Thursday 1800, invalidating this proposal. Test cases must specify which sources apply.

| Comparison | Baseline | Proposed delta |
| --- | --- | --- |
| Immediate Wednesday | Signed SYN_Wed_S1 | HAWK → candidate replacement; 1100 takeoff unchanged |
| Cumulative Wednesday | Published SYN_weekly_C2 | COUGAR → candidate replacement; note already-approved daily change as history |
| Affected Thursday with no signed daily | Published SYN_weekly_C2 | Use Thursday's weekly entries, not Wednesday's daily version |

Check the candidate before recommending adoption. Within existing times, turn, support and guidance, human daily scheduler/Top 3 sign-off is needed. If recovery requires a changed flying time or departure from explicit DO direction, identify the DO decision and support coordination. Do not “reflow” FALCON's already completed checkride into a future event.

## Handoff

The outgoing user asks for a concise current-state handoff that a human can save in Word. It carries `C2` as published weekly baseline, `Wed_S1` as Wednesday immediate baseline, completed X-1, current decisions, the unresolved replacement, missing sources, scenario S-001 and candidate statuses. The receiving user uploads those source files with the primer/profile and handoff. If `SYN_Xs` is missing, the assistant acknowledges that it has not inspected the matrix in this session; prior human confirmations remain scoped human confirmations.

## Separate policy regression mini-cases

- A continuous hot-pit sequence has a later sortie convert to CT: apply the profile's one-event accounting; do not infer two earned upgrade credits.
- Upgradee flight plus academics on the same calendar day: prior DO approval required, including when academics follow the flight.
- IP flight plus academics: use IP compatibility; do not accidentally apply the upgradee-only restriction to every IP.
- Unsupported Letter of Xs role without exception: hard conflict pending confirmation, plus conditional qualified replacement.
- Missing mission-weather limit: affected feasibility unresolved; never adopt the old illustrative 10,000-foot discussion as a validated limit.
- Stable candidate C-SYN-01 rejected by DO: retain Rejected across handoff, with no automatic revival.
