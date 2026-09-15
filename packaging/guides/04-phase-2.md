# Wednesday + Thursday — Build and QC

Use this after **03 Tuesday — Ingest and plan.docx**. This guide contains three clearly separated steps:

1. **Wednesday — Build the schedule** in the main Gemini conversation.
2. **Thursday — Full QC** in that same Gemini conversation.
3. **Thursday — Optional DO adversarial review** in a separate Terra or Grok conversation before the sell.

The schedulers own the lineup. Gemini supports the build and performs the main Thursday review; it does not replace the human schedule build.

## Wednesday — Build the schedule

Wednesday is the normal day for schedulers to get the bulk of the weekly schedule built using Tuesday's planning picture.

Upload or identify:

- The current working draft, with a clear filename/version and exact event/go times.
- Any products updated since Tuesday.
- The Tuesday planning report or the same conversation state.
- An earlier draft if you want change comparison. For the first draft, say there is no comparison baseline.

During the build, ask Gemini targeted questions such as:

- Is this checkride placement feasible with the evaluator, aircraft, support and surrounding duty?
- Which legal upgrade event best fits this open line?
- What does moving this formation do to the rest of the week?
- Are we missing a directed DV/senior-leader flyer?
- Can this unused primary line be filled without displacing a higher priority?

For a broad Wednesday review, paste:

```text
Wednesday — schedule build support. Phase 2 INITIAL DRAFT.
Primary scheduler workflow: Gemini.
Active schedule: [exact filename/version].
Comparison baseline: [exact earlier filename/version, or NONE — first draft].
As of: [date/time/timezone].

Support the scheduler-built draft while we continue constructing it. Identify
blocking hard conflicts, approval needs, obvious checkride/DV/upgrade placement
problems, important missed training opportunities and major resource constraints.
Recommend exact feasible changes where useful and trace the downstream effects
of each proposed cascade. Do not modify the schedule or imply approval.

Use Tuesday's priorities and planning state. Do not infer qualification or
priority from rank/title alone. This is build support, not the deliberate
Thursday full-schedule QC unless I explicitly request the full review now.
```

**Wednesday goal:** a substantially complete working schedule ready for deliberate Thursday review. It does not need to be formally ready for sell yet.

## Thursday — Full QC

Thursday is the deliberate QC day for both the schedulers and Gemini. First conduct normal human scheduler QC. Then identify the exact near-final schedule version and ask Gemini to review the entire schedule from scratch, not merely the latest edits.

Upload or identify any products revised since Wednesday plus current DO/Flt CC guidance and unresolved questions.

```text
Thursday — full QC. Phase 2 INITIAL DRAFT.
Primary scheduler workflow: Gemini.
Active schedule: [exact filename/version].
Comparison baseline: [exact earlier filename/version, or NONE].
As of: [date/time/timezone].
Use DETAILED output and CONFLICTS ONLY ingestion.

Perform a fresh full-schedule review. Do not limit the review to recent edits.
First verify hard constraints, availability, qualifications, prerequisites,
duty/rest checks, aircraft/configuration, simulator capacity and required support.
Then verify that checkrides/evaluations, directed DV or senior-leader flyers,
priority upgrades and other DO priorities are placed appropriately. Do not infer
qualification or priority from rank/title alone; use supplied guidance and the
Letter of Xs.

Review upgrade sequence and pace, instructor/evaluator placement, IP workload,
formations/backups, primary-line use, configuration/support, weather placement,
and the 30-day outlook. Identify unused feasible training opportunities.
For every recommended change, trace the full second- and third-order cascade and
state displaced training or new risk. Include one moderate downside case.
Recommend the minimum set of changes that materially improves the schedule.
Do not modify the schedule or imply that a recommendation is approved.
```

**You should get:** a complete scheduler QC report, ranked issues, exact recommended corrections, unresolved decisions and a clear description of remaining risk. Humans make corrections. If they are material, identify the new active version and ask Gemini to recheck the affected cascades before the sell.

## Thursday — Optional DO adversarial review

This is a separate DO-only workflow after normal Thursday QC and before the sell. It is **optional** and is not part of the main scheduler flow.

Open a separate GenAI.mil conversation using **GPT-5.6 Terra or Grok Expert 4.5**. Give it the exact schedule intended for the sell plus the authoritative products needed to test that schedule. For maximum independence, let it inspect the underlying schedule and inputs rather than merely reacting to Gemini's QC report.

Paste:

```text
You are conducting an independent adversarial schedule review for the squadron
Director of Operations. This is a read-only audit. Do not rebuild the schedule
simply because you would make different choices.

Schedule under review: [exact filename/version].
As of: [date/time/timezone].

Attempt to prove that the schedule contains a material error, unsupported
assumption, overlooked consequence or commander-intent problem that warrants DO
attention. Treat supplied source products and explicit human direction as
authoritative within their stated scope. Do not invent local rules,
qualifications, limits, priorities or waiver authority.

Review in order:
1. Hard constraints: availability, double booking, qualification, prerequisites,
   ratios/evaluators, duty/rest, aircraft/configuration, simulator and support.
2. Sources/assumptions: conflicts, stale data, unsupported conclusions or missing
   information that could materially change the result.
3. Training flow: checkrides, upgrades, phase/configuration dependencies, lost
   high-value opportunities and unrealistic completion assumptions.
4. Second/third-order effects: displaced events, later prerequisites, instructor
   bottlenecks, configuration/support conflicts and risk moved elsewhere.
5. Commander intent: whether supplied priorities, directed DV/senior-leader
   flyers, evaluations/checkrides and at-risk upgrades are actually reflected.
6. Minimum change: broad churn where a smaller legal solution appears available.

Overall assessment must be exactly one of:
NO MATERIAL OBJECTION
REVIEW ADVISED
MATERIAL CONCERN

For each consequential finding provide:
Finding:
Evidence:
Why it matters:
Confidence: High / Medium / Low
Recommended DO action:

Do not pad the report with stylistic preferences. End with exactly one item under:
Most important thing I would verify before buying this schedule:
```

The reviewer has no scheduling authority. The DO decides whether a finding matters. **Do not feed raw Terra/Grok output directly into Gemini as authoritative direction.** If the DO accepts a finding, return only the DO's human direction or question to the main Gemini conversation and have Gemini trace its downstream effects.

The normal sequence is **Thursday Gemini QC → optional DO adversarial review → schedule sell**.

**Next:** follow **05 Schedule sell.docx**.

**Save:** keep meaningful draft versions in **Schedules** and the Tuesday/Wednesday/Thursday analysis, accepted DO directions and decisions in **Working Record**.