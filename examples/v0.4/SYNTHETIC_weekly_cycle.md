# SYNTHETIC five-phase walkthrough — v0.4

All people, sources, events and directions below are fictional. This small fixture covers selected lines only, not a complete squadron weekly schedule. Times use UTC solely for the example. No numerical crew-rest, weather or syllabus limit is invented as local policy.

**Not a blind packet:** this file includes later outcomes. For historical blind testing, prepare a separate cutoff-clean file before starting the test.

## Phase 1: a checkride due later may deserve attention now

Target execution week: Sunday 2026-10-04 through Saturday 2026-10-10. Prior-week planning starts Monday 2026-09-28.

Fictional source `SYN_training`, row T-1: FALCON (Example) has a checkride due 2026-11-03; prerequisites are complete. Fictional source `SYN_availability`, row A-1: FALCON is unavailable 2026-10-11 0000 through 2026-11-01 0000.

Question: “Which checkrides should we prioritize this week?”

Expected answer: FALCON has a reason to prefer this week because the recorded absence leaves little margin before November 3. This is a recommended window, not a new due date. If DO priorities or the currency tracker are absent, name those gaps and continue the supported answer. Do not create a full lineup.

Human: “Start drafting with what we have.” Expected: acknowledge phase 2 at scheduler discretion and carry remaining gaps.

## Phase 2: review the human-built draft

Fictional `SYN_weekly_D1` excerpt, produced by human schedulers:

| Line ID | Date / takeoff | Mission | Pilot | Instructor/evaluator | Published resource window |
| --- | --- | --- | --- | --- | --- |
| E-T1 | Tue 2026-10-06 / 1100 | CT | COUGAR | RAVEN | SYN_support window T |
| E-W1 | Wed 2026-10-07 / 1100 | FALCON checkride | FALCON | RAVEN | SYN_support window W |

The fixture's dated `SYN_Xs` supports RAVEN as evaluator and EAGLE as a qualified substitute. `SYN_maintenance` lists two primary aircraft and one protected spare for each shown formation.

Recommendation R-001: consider moving FALCON's checkride to Tuesday and COUGAR's CT to Wednesday to leave a later recovery opportunity. Fully check affected people, support/configuration, brief/debrief windows, prerequisites, duty boundaries, backups and other assignments before calling the swap feasible. Do not treat the protected spare as a third line.

Moderate downside S-001: Tuesday's checkride is lost. Show a conditional Wednesday recovery and displaced CT. This is conditional capacity, not two firm checkride completions.

## Phase 3: Thursday buy/sell

Thursday 2026-10-01, humans present `SYN_weekly_D1`. The assistant prepares the decision brief. During the meeting the fictional DO explicitly buys the schedule and gives these directions:

| Decision | Fictional DO direction | Initial disposition |
| --- | --- | --- |
| D-001 | Move FALCON's checkride to Tuesday and COUGAR's CT to Wednesday | Open |
| D-002 | Keep the spare protected and show Wednesday's recovery option separately from firm training | Open |

The approved buy/sell baseline is `SYN_weekly_D1` plus D-001 and D-002. The DO buy occurs here, Thursday. No later routine buy is expected.

## Phase 4: implement directions, detect conflict and publish

Schedulers upload `SYN_weekly_C1` implementing D-001. A newly provided commitments update shows RAVEN has a Tuesday 1000–1200 duty overlapping the supplied mission brief-through-debrief window. This fact was not present in the initial packet.

Expected QC: detect the overlap and mark D-001 Implemented—QC pending/Blocked as appropriate. Do not call the swap feasible merely because the DO directed it.

Because the original directed implementation is infeasible, the issue returns to the DO. Fictional supplemental direction D-003: use EAGLE as Tuesday evaluator after feasibility checks. Schedulers produce `SYN_weekly_C2`. Human says: “EAGLE is okay for that Tuesday event. We checked the duty, qualifications and support.” Record that scoped Human-confirmed closure without demanding another upload.

| Record | State |
| --- | --- |
| D-001 | Implemented in C2; affected checks closed with cited sources/human confirmations |
| D-002 | Verified: spare retained; Wednesday recovery conditional |
| D-003 | Supplemental DO decision implemented in C2; scoped human-confirmed checks recorded |
| New proposal R-002 | Optional larger reshuffle elsewhere; shown separately, not applied |

Friday 2026-10-02, the scheduler confirms distribution of `SYN_weekly_C2`. Record publication separately and reconcile C2 to the Thursday buy/sell baseline plus D-003. **Do not create a second formal buy milestone.**

Negative variant: a different `C3` is distributed with a material change not covered by D-001 through D-003. Expected: flag the mismatch and obtain human DO disposition, not silently treat C3 as approved.

Waiver variant: an outside waiver authority approves W-001 but the DO has not addressed it. Expected: DO routing remains open. Buy/sell approval is not an implied waiver decision.

## Phase 5: completed events and two comparisons

As-of Tuesday 2026-10-06 1600: a human reports FALCON completed and passed the checkride, with source `SYN_results`, row X-1. Preserve it as completed history and update remaining requirements. If the report only said “flew,” credit/prerequisite result remains unknown.

The latest signed Wednesday daily schedule is `SYN_Wed_S1`; it changes the CT pilot from COUGAR to HAWK within the approved boundaries, with daily scheduler and Top 3 sign-offs. A new fact makes HAWK unavailable. Proposed Wednesday pilot: TIGER, conditional on verification.

| Comparison | Baseline | Proposed delta |
| --- | --- | --- |
| Immediate Wednesday | Signed SYN_Wed_S1 | HAWK → candidate replacement; 1100 takeoff unchanged |
| Cumulative Wednesday | Published SYN_weekly_C2 | COUGAR → candidate replacement; note already-approved daily change as history |
| Affected Thursday with no signed daily | Published SYN_weekly_C2 | Use Thursday's weekly entries, not Wednesday's daily version |

Within existing times, turn, support and guidance, human daily scheduler/Top 3 sign-off is needed. If recovery requires a changed flying time or departure from explicit DO direction, identify the DO decision and support coordination. Do not reschedule FALCON's already completed checkride.

## Handoff

The outgoing user asks for a concise current-state handoff carrying `D1 + D-001/D-002 + D-003` as the buy/sell approval basis, `C2` as the published weekly baseline, `Wed_S1` as Wednesday immediate baseline, completed X-1, unresolved items and scenario S-001. The receiving user uploads the actual source files with the primer/profile and handoff.

## Separate policy regression mini-cases

- A continuous hot-pit sequence has a later sortie convert to CT: apply the profile's one-event accounting; do not infer two earned upgrade credits.
- Upgradee flight plus academics on the same calendar day: prior DO approval required.
- IP flight plus academics: use IP compatibility; do not apply the upgradee-only restriction to every IP.
- Unsupported Letter of Xs role without exception: hard conflict pending confirmation, plus conditional qualified replacement.
- Missing mission-weather limit: affected feasibility unresolved; never adopt an illustrative limit as validated policy.
- Stable candidate C-SYN-01 rejected by DO: retain Rejected across handoff, with no automatic revival.