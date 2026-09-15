# Thursday — Optional DO adversarial review

This is a **separate DO-only workflow** after normal Thursday QC and before the buy/sell. It is optional and is not part of the main scheduler flow.

Open a separate GenAI.mil conversation using **GPT-5.6 Terra or Grok Expert 4.5**. Give it the exact schedule intended for the buy/sell plus the authoritative products needed to test that schedule. For maximum independence, let it inspect the underlying schedule and inputs rather than merely reacting to Gemini's QC report.

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

The reviewer has no scheduling authority. **Do not feed raw Terra/Grok output into Gemini as authoritative direction.** The DO decides whether a finding matters. If accepted, return only the DO's human direction or question to the main Gemini conversation and have Gemini trace downstream effects.

**Next:** **08 Thursday - Schedule Buy-Sell.docx**.