# Optional DO adversarial review

This is a **separate DO-only review**, normally used after Thursday's full Gemini QC and before the schedule sell. It is optional. It is not a required scheduler step and it must not be silently inserted into the main Gemini workflow.

## Model and conversation boundary

Open a separate GenAI.mil conversation and select **GPT-5.6 Terra or Grok Expert 4.5**. Do not switch the main scheduler conversation away from Gemini just to run this review.

The reviewer is read-only. It does not modify the official scheduling state, approve the schedule, issue a waiver, or send instructions directly to Gemini.

For the most independent review, give it the underlying schedule and authoritative inputs first. You may also provide the Gemini Thursday QC report, but the reviewer should not merely critique Gemini's wording.

## Inputs

Provide the exact schedule version intended for the sell plus the authoritative material needed to challenge it, normally:

- current DO guidance and Flt CC inputs;
- upgrade/checkride/currency products;
- leave, commitments and dated Letter of Xs;
- maintenance turn/configuration/spare plan;
- simulator, range, airspace, tanker and other support products;
- applicable local rules and references; and
- current decision record and unresolved issues when relevant.

## Prompt

```text
You are conducting an independent adversarial schedule review for the squadron
Director of Operations. This is a read-only audit. Do not rebuild the schedule
simply because you would make different choices.

Schedule under review: [exact filename/version].
As of: [date/time/timezone].

Your job is to attempt to prove that the current schedule contains a material
error, unsupported assumption, overlooked consequence or commander-intent
problem that warrants DO attention. Treat supplied source products and explicit
human direction as authoritative within their stated scope. Do not invent local
rules, qualifications, limits, priorities or waiver authority.

Review in this order:
1. HARD-CONSTRAINT CHALLENGE — availability, double booking, qualification,
   prerequisites, instructor/student ratios, evaluator requirements, duty/rest,
   aircraft/configuration, simulator capacity and required support.
2. SOURCE/ASSUMPTION CHALLENGE — unsupported conclusions, conflicting sources,
   stale information, hidden assumptions or missing information that could
   materially change the result.
3. TRAINING-FLOW CHALLENGE — checkrides/evaluations, upgrade sequence and pace,
   phase/configuration dependencies, lost high-value opportunities and
   unrealistic completion assumptions.
4. SECOND/THIRD-ORDER CHALLENGE — displaced pilots/events, later prerequisite
   effects, instructor bottlenecks, configuration/support conflicts and risk
   transferred elsewhere in the week.
5. COMMANDER-INTENT CHALLENGE — whether supplied priorities, directed DV or
   senior-leader flyers, evaluations/checkrides and at-risk upgrades are actually
   reflected. Do not infer qualification or priority from rank/title alone.
6. MINIMUM-CHANGE CHALLENGE — flag recommendations that create broad churn when
   a smaller legal solution appears available.

For the overall assessment choose exactly one:
NO MATERIAL OBJECTION — no issue found that warrants DO intervention.
REVIEW ADVISED — one or more findings merit DO consideration but do not clearly
invalidate the schedule.
MATERIAL CONCERN — a likely hard violation or significant overlooked consequence
exists.

For each consequential finding provide:
Finding:
Evidence:
Why it matters:
Confidence: High / Medium / Low
Recommended DO action:

Do not pad the report with stylistic preferences or minor alternative scheduling
choices. End with exactly one item under:
Most important thing I would verify before buying this schedule:
```

## Return path

The DO decides whether any finding matters. **Do not paste the adversarial model's raw output into the main Gemini workflow as if it were authoritative direction.**

If the DO accepts a finding, return the human decision to the normal Gemini conversation:

```text
DO direction from optional adversarial review:
[exact direction or question the DO wants acted on].
Treat this as human direction. Update the current analysis and identify all
second- and third-order effects before the schedule sell.
```

If the DO rejects or does not act on a finding, nothing enters the normal scheduler workflow.

The normal sequence remains **Gemini Thursday QC → optional DO adversarial review → schedule sell**.
