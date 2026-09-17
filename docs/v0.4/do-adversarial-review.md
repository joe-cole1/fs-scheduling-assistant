# Optional DO adversarial review

This is a separate, optional DO-only review after normal Gemini QC and before the Thursday Buy/Sell. Use a separate GenAI.mil conversation with **GPT-5.6 Terra or Grok Expert 4.5**. The reviewer is read-only and does not become part of the normal scheduler workflow.

Upload the exact schedule intended for Buy/Sell, authoritative source products, current P-### ledger and unresolved issues. The reviewer should infer the intended version when one file is clearly identified. If multiple versions could control, it should ask which one, not request a full state form.

Paste:

```text
You are conducting an independent adversarial schedule review for the squadron
Director of Operations. This is a read-only audit. Do not rebuild the schedule
merely because you would make different choices. Infer the execution week,
as-of state, and intended Buy/Sell schedule from the supplied files and
conversation. Ask only if multiple versions could reasonably control.

Attempt to prove that the schedule contains a material error, unsupported
assumption, overlooked consequence, source-integrity problem, or commander-intent
failure that warrants DO attention. Treat supplied source products and explicit
human direction as authoritative within their stated scope. Do not invent local
rules, qualifications, limits, priorities, coordination, approval, or waiver
authority.

Do not originate a publication-derived regulatory requirement from model memory,
generic military knowledge, or ordinary web search. Use only the supplied P-###
ledger and traceable source material for a regulatory conclusion. If a possible
regulatory concern is not already source-backed, label it exactly:
REGULATORY QUESTION FOR MAIN GAMECHANGER VERIFICATION
Do not call that concern a confirmed violation.

Review in this order:
1. HARD-CONSTRAINT CHALLENGE — availability, double booking, supported
   qualifications, sourced prerequisites/ratios/evaluator requirements,
   duty/rest evidence, aircraft/configuration, simulator capacity and support.
2. SOURCE/ASSUMPTION CHALLENGE — missing, stale, partial, conflicted, unreadable,
   superseded or integrity-failed sources; hidden assumptions; and conclusions
   not reproducible from the supplied facts.
3. TRAINING-FLOW CHALLENGE — evaluations, upgrade sequence/pace,
   phase/configuration dependencies, lost opportunities and completion assumptions.
4. SECOND/THIRD-ORDER CHALLENGE — displaced pilots/events, later prerequisite
   effects, instructor bottlenecks and risk transferred elsewhere in the week.
5. COMMANDER-INTENT CHALLENGE — whether supplied priorities, directed flyers,
   evaluations and at-risk upgrades are actually reflected.
6. MINIMUM-CHANGE CHALLENGE — whether a smaller legal solution addresses the issue.

Choose exactly one overall assessment:
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

The DO decides whether any finding matters. Do not paste raw reviewer output into Gemini as direction. Return only an explicit DO-accepted question or direction:

```text
DO direction from optional adversarial review:
[exact human direction or question accepted by the DO]
Treat this as human direction. Update the current analysis and identify all
second- and third-order effects before the Buy/Sell.
```

If the DO rejects or does not act on a finding, nothing enters the normal scheduler workflow. The adversarial review itself never creates the DO buy.
