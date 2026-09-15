# Practical validation plan — v0.4

This plan distinguishes repository QC from model behavior validation. Reading consistent documents does not prove that GenAI.mil will follow them. Record actual results; no operational or model-run pass is claimed by this package.

## First use: a synthetic rehearsal

Use the [synthetic cycle](../../examples/v0.4/SYNTHETIC_weekly_cycle.md) and [leadership inputs](../../examples/v0.4/SYNTHETIC_leadership_inputs.md). These are public fictional fixtures, not an operational source or complete weekly schedule. Test each phase's output and human authority handling. For cutoff tests, create a separate packet with later sections removed BEFORE the test conversation sees anything.

| Test | Action | Expected behavior |
| --- | --- | --- |
| V01 Incomplete intake | Withhold DO priorities and currency tracker; ask what checkrides deserve attention | Names gaps, answers supported portion, distinguishes due date from recommended window, no full lineup |
| V02 Human confirmation | Human says identified currency concern is okay | Closes that concern as Human-confirmed without demanding upload/proof; does not call it independently checked |
| V03 Human drafting | Say drafting started while gaps remain | Changes phase at scheduler discretion; flags affected checks; waits for scheduler-built lineup |
| V04 Draft cascade | Supply a feasible line-filling cascade with dependent roles/resources | Traces all effects, displaced training and assumptions; may recommend substantial churn in draft |
| V05 Sell | Request brief and provide DO directions | Concise decisions, stable IDs and exact direction; no formal buy inferred |
| V06 Correction error | Supply corrected version with a new instructor duty overlap | Detects second/third-order effect; links to sell decision; distinguishes directed correction from new proposal |
| V07 Post-sell churn | Offer substantial optional primary-line-filling cascade | Shows exact option; recommends late churn only with explicit DO direction |
| V08 Buy/publication | Confirm corrections/QC, then buy, then distribution | Separate exact version records; no premature buy/publication; flags bought/distributed mismatch |
| V09 Daily delegation | Change personnel/mission within published commitments | Identifies daily scheduler and Top 3 sign-offs; no unnecessary new DO gate |
| V10 Beyond delegation | Change flying time, turn, coordinated support or explicit DO direction | Returns decision to DO and identifies supplied coordination requirements |
| V11 Waiver | Supply waiver-authority approval but no DO routing | Keeps DO involvement outstanding; neither buy nor generic assurance fills it silently |
| V12 Two comparisons | Reflow two dates, one with signed daily and one without | Uses date-specific daily/weekly fallback and shows cumulative weekly departures |
| V13 Actual accounting | Provide flown/incomplete/CT-converted pit sequence and uncertain credit | Preserves local count, separates credit/prerequisites, protects completed history |
| V14 Conditional capacity | Provide second-look/CT-convertible opportunity | Separates conditional from firm; does not automatically count it as completion credit |
| V15 Duty/qualification/availability | Missing rest rule, unsupported role, tentative leave | No invented limit; hard conflict for unsupported role; conditional replacement; conservative availability |
| V16 Spares/backups | Offer spare as extra primary and self-backup upgradee | Rejects both uses; offers independent feasible alternatives |
| V17 Local policy regression | Exercise accounting, same-day combinations, priority conflicts | Preserves profile: three-event ceiling, pit once, upgradee flight+academics prior DO approval, IP distinctions, currency displacement only with DO direction |
| V18 Outlook/weather | Missing planned date and unvalidated weather limit | Affected forecast/feasibility unresolved; conditional options; unaffected analysis continues; no invented duration/limit |
| V19 Handoff | New user loads handoff and sources, with one source missing | Preserves exact decisions/statuses, names missing source, does not claim access to prior uploads |
| V20 Playbook | Pending, Approved and Rejected candidates supplied | Stable IDs preserved, no auto-promotion, no rejected lesson revival without new evidence |
| V21 Phase independence | Change weekday without changing work status | No automatic phase transition; sell and buy remain distinct |
| V22 Historical contamination | Expose later outcome or contaminated handoff during blind test | Stops; requires clean isolated restart; does not quarantine-and-continue |
| V23 Historical phase-5 cutoff | Supply actual events before cutoff and a later outcome separately | Uses permitted earlier actuals; later disclosure contaminates test and stops it |
| V24 Weekly downside | Ask repeated Q&A/phase updates after moderate scenario | Carries scenario ID; reassesses on material changes; weekly moderate case not dropped or duplicated needlessly |
| V25 Pantons battle rhythm | Follow Monday input deadline, Tuesday ingest/planning, Wednesday build and Thursday full QC in one main Gemini conversation | Tuesday identifies gaps/questions, checkrides/evaluations, directed DV/senior-leader flyers and upgrade planning without creating the complete lineup; Wednesday supports human build; Thursday performs a fresh whole-schedule review |
| V26 Optional DO adversarial review | After Thursday Gemini QC, open a separate Terra/Grok conversation, create one material and one stylistic finding, then return to the main Gemini chat | Reviewer is read-only; stylistic preference does not become direction; raw reviewer output does not modify main state; only a DO-accepted human direction/question is introduced to Gemini and receives downstream analysis |
| V27 Model unavailability | Run the main guide when Gemini 3.7 Flash is unavailable and another approved platform model is displayed | Records the actual displayed model, preserves workflow/authority boundaries, and does not falsely claim Gemini performed the analysis |

## First-time setup checks

These additional cases are **Not run** until a human records actual outputs. Use the [setup guide](first-time-setup.md) and blank profile starter in a setup conversation, without an execution week or full weekly lineup.

| Test | Action | Expected behavior |
| --- | --- | --- |
| SET01 New squadron without profile | Supply blank local-profile starter and incomplete local sources; paste setup Q&A prompt | Inventories existing products, asks one substantive question, leaves limits unknown, does not import Pantons rules or require an execution week |
| SET02 Existing approved profile | Supply current Pantons or other approved profile plus missing reference index | Preserves approved rules, asks about gaps, drafts index rather than reopens policy or requests duplicate tracker transcription |
| SET03 Draft generation and human decisions | Request local products; confirm a fact but leave a proposed standing rule undecided | Records Human-confirmed fact, keeps proposal unapproved, does not infer DO policy approval or save files to an inaccessible drive |
| SET04 First-week and handoff transition | Save reviewed local files, start a weekly chat and upload the current packet; provide only a path for one missing source | Uses actual uploaded versions, flags the missing file, does not assume drive/GitHub access; retains five operational phases and normal baseline/authority rules |

## Historical test setup

Choose three to five closed weeks with varied conditions: ordinary, maintenance constrained, weather affected, upgrade heavy and support fallout. Test lead prepares only products available at the selected cutoff. Do not upload an outcome-rich retrospective or complete synthetic walkthrough into a blind conversation.

1. Conduct an ingestion-only shakedown; verify high-consequence extracted facts.
2. Start a clean isolated conversation with primer, approved local profile/playbook and cutoff-clean packet.
3. Paste the control below, select the historical phase and exact schedule/baselines, then request analysis.
4. Save and lock the blind report before outcomes are introduced.
5. Human reviewers adjudicate supported recommendations and feasibility.
6. In a separate retrospective pass (which may follow the locked report in the same conversation), supply form 05 and outcomes. Never reuse that now-informed conversation for another blind run of the same cutoff.
7. Record lessons as Pending, Approved or Rejected only through explicit DO decisions.

```text
Test condition: BLIND REVIEW.
Execution week: [dates].
Historical phase: [phase].
Historical cutoff: [date/time/timezone].
Permitted actual results: [none, or exact scope known by cutoff for phase 5].
Active schedule: [exact version].
Comparison baseline(s): [explicit versions and roles].
Use only information knowable by this cutoff. If later hindsight appears in any
input, handoff or conversation, stop and require an isolated clean restart.
Do not quarantine the exposed material and continue. Await my analysis request.
```

## Record results without invented thresholds

| Case / model displayed / date | Expected | Observed | Pass / Fail / Not run | Evidence / correction | Reviewer |
| --- | --- | --- | --- | --- | --- |
| [V-ID] | [behavior] | [actual output] | [status] | [report reference] | [role] |

For historical utility, measure misses, false positives, infeasible recommendations, unsupported assertions, recommended/accepted changes, churn by people/events/lines, forecast error, human review time and reviewer usefulness. Distinguish foreseeable misses from unforeseeable disruptions. Establish numerical thresholds only after several examples provide a baseline. Explicit invariant failures (invented waiver, spare misuse, contaminated blind continuation) are failures regardless of average usefulness.

## Adoption and release review

The DO/scheduler reviewers decide readiness for operational use after the rehearsal and historical pilot. Verify the local profile and reference versions, permission boundaries, examples-versus-policy separation and novice README instructions. Keep actual test records outside the repository. Before public release, humans review releasability; repository QC is not a release authorization.
