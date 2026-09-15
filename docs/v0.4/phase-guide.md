# Phase-by-phase operating guide — v0.4

Use the day-labeled Word guides in the download package for copy/paste commands and input lists. This reference defines responsibility, internal phase state, decisions and carried state. The operator manual is chronological; the five internal phases remain status-based controls underneath it.

For Pantons, the normal battle rhythm is:

| Day / step | Human work | Assistant role |
| --- | --- | --- |
| Monday | All scheduling inputs due NLT COB | No automatic action or assumption of completeness |
| Tuesday — start | Create weekly workspace/chat and upload startup/local/current products | Gemini confirms readable sources, records run controls and manifests gaps |
| Tuesday — plan | Ask planning questions; identify checkrides/evaluations, directed DV/senior-leader flyers and plan upgrades | Gemini reconciles products, identifies gaps and builds the planning picture |
| Wednesday | Schedulers build the bulk of the schedule | Gemini supports bounded planning questions, conflict checks and cascade analysis |
| Thursday — QC | Schedulers conduct QC on the near-final draft | Gemini performs a fresh full-schedule review |
| Thursday — optional DO review | DO may independently challenge the schedule | Separate Terra or Grok adversarial review; read-only, optional, not part of scheduler flow |
| Thursday — buy/sell | Schedulers present the chosen version; DO decides and buys the weekly schedule if satisfied | Gemini prepares decision support and records the explicit DO buy plus directions |
| Thu–Fri after buy/sell | Schedulers implement recorded directions | Gemini verifies implementation and second/third-order effects; no routine second buy |
| Friday | Humans publish the corrected schedule | Gemini verifies the publication candidate remains within the Thursday buy/sell and records publication separately |
| Execution week | Daily scheduler/Top 3 manage bounded changes; DO handles changes beyond delegation | Gemini analyzes reflows against current baselines |

The weekday labels describe the normal Pantons rhythm. Work status still controls the internal phase. A weekday, filename or meeting title does not create approval when the required human action did not occur.

The normal scheduler conversation uses Gemini 3.7 Flash when available. The optional DO adversarial review uses a separate GPT-5.6 Terra or Grok Expert 4.5 conversation. Raw reviewer output does not become scheduler direction. Only DO-accepted human direction returns to the main Gemini workflow.

## 1. Product gathering — Monday input deadline and Tuesday planning

**Contributors:** scheduling consolidates; DO provides priorities/intent; Flt CCs provide personnel effects; training, maintenance and support owners supply existing products. Inputs are normally due NLT COB Monday. Tuesday, schedulers upload the available packet and begin planning. The assistant may draft missing forms and answer planning questions. It does not create a full lineup.

**Inputs:** execution week and available planning products. Load approved local rules and stable references for any rule-based conclusion. Standard sources include upgrade/currency trackers, leave/commitments, dated qualifications, aircraft turn/configuration, sims, support, weather, training phase plan and roster.

**Tuesday first pass:** identify material missing/conflicting inputs; determine which checkrides/evaluations deserve deliberate placement; identify only directed DV/senior-leader flyers actually supported by guidance; and map each upgradee's next legal events, prerequisites, candidate windows, weekly pace and instructor/resource demand. Rank constraints that should shape Wednesday's build. Do not infer qualification or flying priority from rank/title alone.

**May remain provisional:** leadership priorities not yet issued, tentative support, early weather, missing trackers, future capacity. Missing high-consequence facts limit only affected recommendations. Tentative leave is unavailable until resolved. The scheduler may start drafting despite gaps.

**Outputs:** normalized facts and gaps; bounded Q&A; supported checkride/evaluation priorities; directed DV/senior-leader requirements; upgrade planning; prerequisite/window/resource demand; missing guidance clearly marked Proposed.

**Advance:** Wednesday the schedulers begin the bulk build, or earlier/later by explicit human status. **Carry:** current manifest, profile/playbook, confirmed guidance, human confirmations and unresolved items. Active schedule/baseline may still be None.

## 2. Initial draft — Wednesday build and Thursday full QC

**Contributors:** schedulers build and edit the lineup; assistant supports the build and later conducts the deliberate full review; DO/Flt CC/training/resource owners resolve their issues.

### Wednesday — build

Schedulers build the bulk of the schedule. Gemini provides bounded analysis during construction: check specific placements, identify hard blockers, examine checkride/DV/upgrade placement, test a cascade and identify major resource constraints. The purpose is to help humans construct the schedule without turning every intermediate draft into a complete weekly QC cycle.

**Inputs:** a named scheduler-built draft and exact times, known products supporting affected assignments, and a human-selected draft baseline or explicit None for the first draft. Do not call assignments feasible where prerequisites, resources or duty checks are unresolved.

### Thursday — full QC

Once substantially complete, schedulers conduct their own QC and Gemini performs a fresh review of the entire active schedule rather than only the latest edits. Cover hard constraints, approvals, checkrides, directed flyers, upgrade flow, primary lines/spares/configuration/formations/backups, IP/evaluator workload, support/weather placement, 30-day outlook, unused feasible opportunities and one moderate downside case. Validate every proposed cascade completely.

### Optional Thursday DO adversarial review

After normal Thursday QC and before the buy/sell, the DO may open a separate Terra or Grok conversation and challenge the schedule independently. This review is optional, read-only and outside the main scheduler state. If the DO accepts a finding, return the DO's human direction or question to Gemini.

**Advance:** humans identify the version to present at the buy/sell. **Carry:** presented version, chosen draft baseline, latest report, source versions, unresolved decisions and proposals.

## 3. Schedule buy/sell — Thursday

**Contributors:** schedulers present; DO reviews, decides and buys the weekly schedule if satisfied; Gemini prepares decision support and records the human decision.

**Inputs:** exact presented version, latest evidence/limits, priorities/outlook, alternatives and unresolved decisions. Any accepted adversarial issue enters only as explicit DO direction/question, not raw model authority.

**Outputs:** concise decision package answering whether the plan is feasible, what it accomplishes, where it is fragile, what capacity remains unused, and what decisions the DO must make. Record the exact DO buy statement and each D-### direction with scope.

**Authority:** the Thursday buy/sell is the formal DO buy event. The approved buy/sell baseline is the exact presented schedule plus the explicit DO directions recorded in that meeting. A meeting with no explicit DO buy does not create approval. Waivers remain separate and still require the applicable authority plus DO routing.

**Advance:** if bought, phase 4 begins and schedulers implement the recorded directions. If not bought, return the schedule to the appropriate earlier work. **Carry:** exact presented version, DO buy statement, directions/dispositions, unresolved questions and current evidence.

## 4. Post-buy/sell implementation, final QC and publication — Thursday through Friday

**Contributors:** schedulers edit; Gemini checks; humans close findings; DO resolves material departures beyond the buy/sell; humans publish through the normal distribution process.

**Inputs:** buy/sell-presented baseline, DO directions/decision record, corrected active version and updated evidence/confirmations.

**Outputs:** disposition of every buy/sell decision; exact comparison to the presented schedule and incremental corrected versions; revalidated second/third-order effects; complete-schedule conflict check; separately identified new proposals.

**No routine second buy:** implementing a recorded buy/sell direction does not require the DO to buy the schedule again. Gemini verifies that the corrected version faithfully implements the approved direction. If implementation is infeasible or the necessary solution materially exceeds the recorded direction, return that specific issue to the DO for a supplemental decision. Do not silently expand the Thursday buy.

**Final-publication check:** reconcile every buy/sell direction; expose open hard conflicts, waiver gaps and material unexplained differences; distinguish directed corrections from new proposals; verify that the publication candidate remains within the approved buy/sell plus any later explicit DO decisions. Human approval/publication remain human actions.

**Advance:** human confirms publication, normally Friday. **Carry:** buy/sell baseline, decision record, published artifact, waiver records and report. Preserve the relationship between presented and published versions rather than inventing a second buy milestone.

## 5. Execution-week reflows

**Inputs:** as-of time, current weekly publication, signed daily version for each affected day if available, actual results/credit and changed facts.

**Outputs:** completed history versus remaining firm versus conditional state; exact reflow cascade; today/next-duty-day and at-risk upgrade effects; updated outlook and impacted scenario. Report immediate changes against the signed daily for each date, falling back to weekly; report cumulative departures against the published weekly.

**DO involvement:** changes beyond published times/turn/support/guidance; every waiver also follows applicable authority. Routine feasible personnel/mission changes within these boundaries receive daily scheduler/Top 3 sign-off.

**Close:** humans confirm each new signed daily version or end of execution. No automatic retrospective or playbook promotion.

## Across users and weeks

Prefer one weekly Gemini conversation for the main scheduler workflow; use the handoff form only when an active week moves chats/users. The optional DO adversarial review is deliberately separate. Preserve the published weekly baseline unless humans explicitly reissue it. Next week uses a fresh weekly record with current inputs. Weekly guidance expires unless explicitly renewed. Only DO-approved playbook lessons carry as standing rules.