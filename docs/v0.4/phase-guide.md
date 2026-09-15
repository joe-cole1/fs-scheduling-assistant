# Phase-by-phase operating guide — v0.4

Use the numbered Word guides in the download package for copy/paste commands and input lists. This guide defines responsibility, readiness, decisions and carried state.

For Pantons, the normal battle rhythm is explicit:

| Day / step | Human work | Assistant role |
| --- | --- | --- |
| Monday | All scheduling inputs due NLT COB | No automatic action or assumption of completeness |
| Tuesday | Upload inputs, ask planning questions, identify checkrides/evaluations, directed DV/senior-leader flyers and plan upgrades | Gemini ingests/reconciles products, identifies gaps and builds the planning picture |
| Wednesday | Schedulers build the bulk of the schedule | Gemini supports bounded planning questions, conflict checks and cascade analysis |
| Thursday — QC | Schedulers conduct QC on the near-final draft | Gemini performs a fresh full-schedule review |
| Thursday — optional DO review | DO may independently challenge the schedule | Separate Terra or Grok adversarial review; read-only, optional, not part of scheduler flow |
| Thursday — sell | Schedulers present the chosen version; DO directs | Gemini prepares decision support and records human DO directions |
| Thu–Fri post-sell | Schedulers implement directions; DO buys exact corrected version; humans publish | Gemini checks implementation and second/third-order effects |
| Execution week | Daily scheduler/Top 3 manage bounded changes; DO handles changes beyond delegation | Gemini analyzes reflows against current baselines |

The weekday labels describe the normal Pantons rhythm. The five internal phases still follow actual work status; a weekday does not automatically create approval, buy, publication, or advancement when the underlying work has not occurred.

The normal scheduler conversation uses Gemini 3.7 Flash when available. The optional DO adversarial review uses a separate GPT-5.6 Terra or Grok Expert 4.5 conversation. Raw reviewer output does not become scheduler direction. Only DO-accepted human direction returns to the main Gemini workflow.

## 1. Product gathering and generation — Tuesday ingest and planning

**Contributors:** scheduling consolidates; DO provides priorities/intent; Flt CCs provide personnel effects; training, maintenance and support owners supply their existing products. Inputs are normally due NLT COB Monday. Tuesday, schedulers upload the available packet and begin planning. The assistant may draft missing forms and answer planning questions. It does not create a full lineup.

**Inputs now:** execution week and available planning products. Load approved local rules and stable references for any rule-based conclusion. Manifest what is available and missing. No active lineup is required. Standard sources include upgrade/currency trackers, leave/commitments, dated qualifications, aircraft turn/configuration, sims, support, weather, training phase plan and roster.

**Tuesday first pass:** identify material missing/conflicting inputs; determine which checkrides/evaluations deserve deliberate placement; identify only directed DV/senior-leader flyers actually supported by guidance; and map each upgradee's next legal events, prerequisites, candidate windows, weekly pace and instructor/resource demand. Rank constraints that should shape Wednesday's build. Do not infer qualification or flying priority from rank/title alone.

**May remain provisional:** leadership priorities not yet issued, tentative support, early weather, missing trackers, future capacity. Missing high-consequence facts limit only affected recommendations. Tentative leave is unavailable until resolved; “provisional” does not make it assignable. The scheduler may start drafting despite gaps.

**Outputs:** normalized facts and gaps; bounded Q&A; checkride/evaluation priorities supported by evidence; directed DV/senior-leader requirements; upgrade planning; prerequisite/window/resource demand; missing guidance clearly marked Proposed. Capture an early checkride opportunity caused by future absence without inventing a new due date.

**DO involvement:** confirm DO guidance and discretionary priorities/restrictions; resolve decisions beyond provided authority. Flt CC recommendations remain recommendations until adopted by the proper human.

**Advance:** Wednesday the schedulers begin the bulk schedule build, or earlier/later by explicit human status. **Carry:** current manifest, local profile/playbook, confirmed guidance, human confirmations and unresolved items with affected checks. Active schedule/baseline may still be None.

## 2. Initial draft — Wednesday build and Thursday full QC

**Contributors:** schedulers build and edit the lineup; assistant supports the build and later conducts the deliberate full review; DO/Flt CC/training/resource owners resolve their issues.

### Wednesday — build

Schedulers build the bulk of the schedule. Gemini provides bounded analysis during construction: check specific placements, identify hard blockers, examine checkride/DV/upgrade placement, test a cascade and identify major resource constraints. The purpose is to help humans construct the schedule without turning every intermediate draft into a complete weekly QC cycle.

**Inputs now:** a named scheduler-built draft and exact times, known products supporting affected assignments, and a human-selected draft baseline or explicit None for the first draft. Do not call assignments feasible where prerequisites, resources or duty checks are unresolved.

**May remain provisional:** resource/weather assumptions and unresolved decisions for presentation, all labeled. Human confirmations can close specific concerns.

### Thursday — full QC

Once the schedule is substantially complete, schedulers conduct their own QC and Gemini performs a fresh review of the entire active schedule rather than only the latest edits.

The full review covers hard conflicts, approval needs, checkrides/evaluations, directed DV/senior-leader flyers, upgrade sequencing and pace, primary-line/spare/configuration/formation/backup analysis, IP/evaluator placement and workload, support/weather placement, the 30-day outlook, unused feasible opportunities and one moderate downside scenario. Every recommended change receives complete second/third-order cascade validation.

**Outputs:** hard conflicts, approval needs, exact improvements and fully revalidated cascades; upgrade flow, 30-day outlook, comparable IP workload and moderate downside scenario. BRIEF and DETAILED adjust depth without changing policy.

**DO involvement:** waivers (also routed to applicable authority), discretionary priority changes, configuration alternatives and explicit exceptions. The assistant does not execute its recommendations.

### Optional Thursday DO adversarial review

After normal Thursday QC and before the sell, the DO may open a separate Terra or Grok conversation and challenge the schedule independently. This review is optional, read-only and outside the normal scheduler workflow. It does not modify official state or issue direction directly to Gemini. If the DO accepts a finding, the DO returns the human direction or question to the main Gemini conversation for normal downstream analysis.

**Advance:** humans identify the version to present at the sell. Not all issues must be resolved to discuss the draft. **Carry:** presented version, chosen draft baseline, latest report, source versions, unresolved decisions and proposals.

## 3. Schedule sell — Thursday

**Contributors:** schedulers present; DO reviews and directs; Gemini prepares decision support and records the human directions.

**Inputs now:** exact presented version, latest evidence/limits, priorities/outlook, alternatives and unresolved decisions. Any accepted issue from the optional adversarial review enters only as explicit DO direction/question, not as raw model authority. **Provisional:** correction proposals and unresolved resource facts; do not hide them as confirmed feasibility.

**Outputs:** a concise package answering whether the plan is feasible, what it accomplishes, where it is fragile, what training/primary capacity remains unused, and what decisions the DO must make. Each request includes options, recommendation, tradeoff, deadline, and authority/coordination as known. Record D-### directions and preserve rejected proposals.

**DO involvement:** provides exact direction. The meeting itself is not formal buy, and no implicit waiver occurs.

**Advance:** humans state sell is complete and corrections are identified. A returned draft can reopen phase 2 explicitly; there is no automatic progression. **Carry:** exact presented version, all directions/dispositions, unresolved questions and current evidence. Post-sell work uses FINAL QC limits.

## 4. Corrections, final QC, DO buy and publication — Thursday through Friday

**Contributors:** schedulers edit; Gemini checks; humans close findings; DO formally buys; humans publish through the normal distribution process.

**Inputs now:** sell-presented baseline, directed corrections, corrected active version and updated evidence/confirmations. **Provisional:** unresolved correction effects or new proposals remain labeled; no assumption of authority or feasibility.

**Outputs:** disposition of every sell decision; exact comparison to the presented schedule and incremental corrected versions; revalidated second/third-order effects; complete-schedule conflict check; separately identified new proposals. Hard infeasibility and major upgrade risks remain actionable. Substantial extra cascades are DO options, not automatic optimization.

**Final-publication check:** identify the exact version; reconcile every sell direction; report correction and whole-schedule QC; record human-confirmed closures; expose open issues and waiver/DO routing; record formal DO buy after corrections/QC; verify that distributed version matches the buy or explain differences and human disposition. “QC complete” does not mean every fact was independently verified by the model. Human approval/publication remain human actions.

**DO involvement:** resolves infeasible directions/new decisions and all waiver routing; formally buys the corrected, QC'd version. No conditional buy of an uncorrected draft is assumed.

**Advance:** human confirms publication, normally Friday for the entire following week; phase 5 starts when humans request execution work. **Carry:** bought artifact, distributed artifact, decision/waiver records and report. Preserve both identities even when bytes match. A changed post-buy weekly file is not silently approved by the earlier buy.

## 5. Execution-week reflows

**Contributors:** daily scheduler and Top 3 provide current facts and sign daily schedules; source owners update products; DO handles changes beyond delegation and every waiver; Gemini analyzes.

**Inputs now:** as-of time, current weekly publication, signed daily version for each affected day if available, actual results/credit and changed facts. **Provisional:** future resources, forecast changes and conditional opportunities; actual credit unknown until evidence/confirmation.

**Outputs:** completed-history versus remaining-firm versus conditional state; exact reflow cascade; today/next-duty-day and at-risk upgrade effects; updated outlook and impacted scenario. Report immediate changes against the signed daily for each date, falling back to weekly; report cumulative departures against the published weekly. Today's signed daily is not tomorrow's baseline.

**DO involvement:** changes beyond published times/turn/support/guidance; every waiver also follows applicable authority. Routine feasible personnel/mission changes within these boundaries receive daily scheduler/Top 3 sign-off.

**Advance/close:** humans confirm each new signed daily version or end of execution. No automatic retrospective or playbook promotion. **Carry:** completed actuals, current schedules, baseline roles, approvals, unresolved items and the concise handoff. Repeated reflows do not reschedule completed events or turn every conditional line into forecast credit.

## Across users and weeks

Prefer one weekly Gemini conversation for the main scheduler workflow; use the handoff form when needed. The optional DO adversarial review is deliberately a different conversation and does not replace the main state. Preserve the original published weekly baseline unless humans explicitly select a new publication after reissue. Every affected daily baseline has its own date. If two users submit competing changes, reconcile them as proposals against the identified current versions; do not assume the last uploaded filename wins.

Next week uses a fresh weekly record with current inputs. Weekly guidance expires unless explicitly renewed. Only DO-approved playbook lessons carry as standing rules. Historical tests require isolated cutoff-clean inputs, including handoffs and transcripts.
