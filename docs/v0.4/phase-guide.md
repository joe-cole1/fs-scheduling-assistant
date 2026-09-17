# Phase-by-phase operating guide — v0.4

Use the day-labeled Word guides in the download package for copy/paste commands and input lists. This reference defines responsibility, internal phase state, decisions and carried state. The operator manual is chronological; the five internal phases remain status-based controls underneath it.

For Pantons, the normal battle rhythm is:

| Day / step | Human work | Assistant role |
| --- | --- | --- |
| Monday | All scheduling inputs due NLT COB | No automatic action or assumption of completeness |
| Tuesday — start | Create weekly workspace/chat, enable GAMECHANGER when available and upload startup/local/current products | Gemini confirms readable sources, connector availability, run controls and gaps |
| Tuesday — plan | Ask planning questions; identify checkrides/evaluations, directed DV/senior-leader flyers and plan upgrades | Gemini reconciles products, builds the planning picture, queries GAMECHANGER for relevant publication rules and creates the initial P-### rule/currency baseline |
| Wednesday | Schedulers build the bulk of the schedule | Gemini supports bounded planning questions, conflict checks and cascade analysis |
| Thursday — QC | Schedulers conduct QC on the near-final draft | Gemini performs a fresh full-schedule review and refreshes/expands publication-grounded QC through GAMECHANGER |
| Thursday — optional DO review | DO may independently challenge the schedule | Separate Terra or Grok adversarial review; read-only, optional, not part of scheduler flow |
| Thursday — buy/sell | Schedulers present the chosen version; DO decides and buys the weekly schedule if satisfied | Gemini prepares decision support, surfaces publication-QC exceptions/limits and records the explicit DO buy plus directions |
| Thu–Fri after buy/sell | Schedulers implement recorded directions | Gemini verifies implementation and second/third-order effects; re-queries affected publication rules; no routine second buy |
| Friday | Humans publish the corrected schedule | Gemini verifies the publication candidate remains within the Thursday buy/sell, preserves publication-QC limits and records publication separately |
| Execution week | Daily scheduler/Top 3 manage bounded changes; DO handles changes beyond delegation | Gemini analyzes reflows against current baselines and runs GAMECHANGER delta checks for affected regulatory facts |

The weekday labels describe the normal Pantons rhythm. Work status still controls the internal phase. A weekday, filename or meeting title does not create approval when the required human action did not occur.

The normal scheduler conversation uses Gemini 3.7 Flash when available. The optional DO adversarial review uses a separate GPT-5.6 Terra or Grok Expert 4.5 conversation. Raw reviewer output does not become scheduler direction. Only DO-accepted human direction returns to the main Gemini workflow.

**DoW Policies Beta (GAMECHANGER)** is the publication-authority layer for the main Gemini workflow. For publication-derived currency, qualification, crew-rest/duty, evaluation, syllabus/prerequisite, event-credit, recurring-training or similar regulatory requirements, Gemini may make a regulatory determination only from a sufficiently traceable publication retrieved through that connector. Model memory, generic military knowledge and ordinary web search are not fallback authorities. If the connector/source is insufficient, the affected check is CANNOT VERIFY while unrelated scheduling analysis continues.

## 1. Product gathering — Monday input deadline and Tuesday planning

**Contributors:** scheduling consolidates; DO provides priorities/intent; Flt CCs provide personnel effects; training, maintenance and support owners supply existing products. Inputs are normally due NLT COB Monday. Tuesday, schedulers upload the available packet and begin planning. The assistant may draft missing forms and answer planning questions. It does not create a full lineup.

**Inputs:** execution week and available planning products. Load approved local rules and stable references for local rule/source context. Standard sources include upgrade/currency trackers, leave/commitments, dated qualifications, aircraft turn/configuration, sims, support, weather, training phase plan and roster. Publication-based regulatory conclusions additionally require GAMECHANGER retrieval under the primer's source gate.

**Tuesday first pass:** identify material missing/conflicting inputs; determine which checkrides/evaluations deserve deliberate placement; identify only directed DV/senior-leader flyers actually supported by guidance; and map each upgradee's next legal events, prerequisites, candidate windows, weekly pace and instructor/resource demand. Rank constraints that should shape Wednesday's build. Do not infer qualification or flying priority from rank/title alone.

Then use the currency tracker, Letter of Xs, upgrade/evaluation status and planned activities to identify relevant publication-driven checks. Query GAMECHANGER, record each sufficiently traceable rule in the **Weekly Publication Rule Ledger** with a stable P-### ID, and classify it SOURCE-BACKED OK, SOURCE-BACKED ISSUE, CANNOT VERIFY or SOURCE CONFLICT. Record publication number/title, current/effective status when available, paragraph/page/usable locator and retrieval time. Do not use the web or model memory to fill a missing rule.

**May remain provisional:** leadership priorities not yet issued, tentative support, early weather, missing trackers, future capacity, and publication checks that are CANNOT VERIFY or SOURCE CONFLICT. Missing high-consequence facts limit only affected recommendations. Tentative leave is unavailable until resolved. The scheduler may start drafting despite gaps.

**Outputs:** normalized facts and gaps; bounded Q&A; supported checkride/evaluation priorities; directed DV/senior-leader requirements; upgrade planning; prerequisite/window/resource demand; initial P-### publication-rule/currency baseline; missing guidance clearly marked Proposed.

**Advance:** Wednesday the schedulers begin the bulk build, or earlier/later by explicit human status. **Carry:** current manifest, profile/playbook, confirmed guidance, human confirmations, P-### ledger and unresolved items. Active schedule/baseline may still be None.

## 2. Initial draft — Wednesday build and Thursday full QC

**Contributors:** schedulers build and edit the lineup; assistant supports the build and later conducts the deliberate full review; DO/Flt CC/training/resource owners resolve their issues.

### Wednesday — build

Schedulers build the bulk of the schedule. Gemini provides bounded analysis during construction: check specific placements, identify hard blockers, examine checkride/DV/upgrade placement, test a cascade and identify major resource constraints. The purpose is to help humans construct the schedule without turning every intermediate draft into a complete weekly QC cycle. If a bounded answer depends on a publication-derived rule, the same GAMECHANGER source gate applies.

**Inputs:** a named scheduler-built draft and exact times, known products supporting affected assignments, and a human-selected draft baseline or explicit None for the first draft. Do not call assignments feasible where prerequisites, resources, duty checks or required publication evidence are unresolved.

### Thursday — full QC

Once substantially complete, schedulers conduct their own QC and Gemini performs a fresh review of the entire active schedule rather than only the latest edits. Cover hard constraints, approvals, checkrides, directed flyers, upgrade flow, primary lines/spares/configuration/formations/backups, IP/evaluator workload, support/weather placement, 30-day outlook, unused feasible opportunities and one moderate downside case. Validate every proposed cascade completely.

Run a distinct publication-grounded QC pass. Re-query GAMECHANGER against the people, roles, events, timing and prerequisites actually scheduled; refresh and expand the P-### ledger; check available evidence for current/superseded/more-specific guidance and source conflicts. Do not claim “fully compliant.” List SOURCE-BACKED ISSUE, SOURCE CONFLICT and CANNOT VERIFY items explicitly.

### Optional Thursday DO adversarial review

After normal Thursday QC and before the buy/sell, the DO may open a separate Terra or Grok conversation and challenge the schedule independently. This review is optional, read-only and outside the main scheduler state. If the DO accepts a finding, return the DO's human direction or question to Gemini.

**Advance:** humans identify the version to present at the buy/sell. **Carry:** presented version, chosen draft baseline, latest report, P-### ledger, source versions, unresolved decisions and proposals.

## 3. Schedule buy/sell — Thursday

**Contributors:** schedulers present; DO reviews, decides and buys the weekly schedule if satisfied; Gemini prepares decision support and records the human decision.

**Inputs:** exact presented version, latest evidence/limits, priorities/outlook, alternatives, unresolved decisions and the Thursday publication-grounded QC summary. Any accepted adversarial issue enters only as explicit DO direction/question, not raw model authority.

**Outputs:** concise decision package answering whether the plan is feasible, what it accomplishes, where it is fragile, what capacity remains unused, what publication-grounded issues/limits remain, and what decisions the DO must make. Record the exact DO buy statement and each D-### direction with scope.

**Authority:** the Thursday buy/sell is the formal DO buy event. The approved buy/sell baseline is the exact presented schedule plus the explicit DO directions recorded in that meeting. A meeting with no explicit DO buy does not create approval. Waivers remain separate and still require the applicable authority plus DO routing. A GAMECHANGER result supplies evidence, not approval or waiver authority.

**Advance:** if bought, phase 4 begins and schedulers implement the recorded directions. If not bought, return the schedule to the appropriate earlier work. **Carry:** exact presented version, DO buy statement, directions/dispositions, P-### ledger, unresolved questions and current evidence.

## 4. Post-buy/sell implementation, final QC and publication — Thursday through Friday

**Contributors:** schedulers edit; Gemini checks; humans close findings; DO resolves material departures beyond the buy/sell; humans publish through the normal distribution process.

**Inputs:** buy/sell-presented baseline, DO directions/decision record, corrected active version, current P-### ledger and updated evidence/confirmations.

**Outputs:** disposition of every buy/sell decision; exact comparison to the presented schedule and incremental corrected versions; revalidated second/third-order effects; complete-schedule conflict check; affected GAMECHANGER delta checks; separately identified new proposals.

**No routine second buy:** implementing a recorded buy/sell direction does not require the DO to buy the schedule again. Gemini verifies that the corrected version faithfully implements the approved direction. If implementation is infeasible or the necessary solution materially exceeds the recorded direction, return that specific issue to the DO for a supplemental decision. Do not silently expand the Thursday buy.

**Publication-rule delta:** if a correction changes a person, role, event, timing, prerequisite, currency/qualification state or other publication-relevant fact, re-query the affected rule through GAMECHANGER and update/add the P-### entry. Human confirmation can close a stated scheduling concern, but it does not transform missing connector evidence into SOURCE-BACKED OK.

**Final-publication check:** reconcile every buy/sell direction; expose open hard conflicts, waiver gaps, publication-QC exceptions/limits and material unexplained differences; distinguish directed corrections from new proposals; verify that the publication candidate remains within the approved buy/sell plus any later explicit DO decisions. Human approval/publication remain human actions.

**Advance:** human confirms publication, normally Friday. **Carry:** buy/sell baseline, decision record, final P-### ledger, published artifact, waiver records and report. Preserve the relationship between presented and published versions rather than inventing a second buy milestone.

## 5. Execution-week reflows

**Inputs:** as-of time, current weekly publication, signed daily version for each affected day if available, actual results/credit, changed facts and current P-### ledger.

**Outputs:** completed history versus remaining firm versus conditional state; exact reflow cascade; today/next-duty-day and at-risk upgrade effects; updated outlook and impacted scenario. Report immediate changes against the signed daily for each date, falling back to weekly; report cumulative departures against the published weekly. Re-query GAMECHANGER for every publication-driven check affected by a changed/proposed person, role, event, timing, prerequisite or regulatory state and update the P-### ledger.

**DO involvement:** changes beyond published times/turn/support/guidance; every waiver also follows applicable authority. Routine feasible personnel/mission changes within these boundaries receive daily scheduler/Top 3 sign-off. GAMECHANGER does not alter these authority boundaries.

**Close:** humans confirm each new signed daily version or end of execution. No automatic retrospective or playbook promotion.

## Across users and weeks

Prefer one weekly Gemini conversation for the main scheduler workflow; use the handoff form only when an active week moves chats/users. The optional DO adversarial review is deliberately separate. Preserve the published weekly baseline unless humans explicitly reissue it. Preserve the P-### ledger as continuity evidence, but do not use a handoff copy to bypass a required current connector check. Next week uses a fresh weekly record with current inputs and a new Tuesday publication-discovery pass. Weekly guidance expires unless explicitly renewed. Only DO-approved playbook lessons carry as standing rules.