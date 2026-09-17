# Wednesday — Build the schedule and integrate inputs

Wednesday is the human build day. Schedulers construct the bulk of the Week + 1 schedule. Gemini supports bounded questions, conflict checks and cascade analysis; it does not replace the scheduler-built lineup.

The day ends with the **Cross-Functional Schedule Integration Review**. Flight Commanders and material functional owners verify that their inputs are represented, assign unresolved issues and identify DO decisions needed Thursday. This is not a schedule approval event and should not be called the Buy or Buy/Sell.

## During the build

Upload the current working draft when it changes materially. The assistant should use the latest clearly identified working version and infer the week, as-of state and prior draft from the chat and filenames. If more than one version could be active, it should ask which version controls rather than present a state-entry form.

Paste for bounded support:

```text
Use the inferred execution week, current manifest, and latest clearly identified
working draft. Support the human schedule build without replacing it.

Review the placement, conflict, or cascade I am asking about. Check every affected
pilot, availability, duty boundary, qualification, prerequisite, IP/evaluator,
formation role, aircraft/configuration, primary line, protected spare, simulator,
range/airspace/tanker/support window, backup, displaced training, and later event.
If the question depends on a publication-derived rule, use the current P-###
ledger or query GAMECHANGER as required. Do not fill a publication gap from memory
or ordinary web search.

Give the smallest fully feasible change first, then any broader option that
materially improves priorities. Distinguish facts, assumptions, recommendations,
and required human decisions. Do not run a full Thursday QC unless I request it.
```

## Cross-Functional Schedule Integration Review

Before ending Wednesday:

- Identify the exact integrated draft proceeding to Thursday QC.
- Confirm Flight Commanders and the material CCV, DOT, DOW, DOS, DOX, maintenance and support inputs are represented.
- Assign every unresolved source conflict, personnel issue, resource issue or missing decision to an owner and due time.
- Confirm checkrides/evaluations, directed DVs, at-risk upgrades, primary lines, protected spares, configuration and support are either represented or have a documented reason.
- Record specific questions that require a Thursday DO decision.

Paste when preparing the integration review:

```text
Prepare an exception-based Cross-Functional Schedule Integration Review for the
latest clearly identified working draft. This is an integration and issue-
disposition review, not a DO approval event.

Show: source-owner inputs not represented; unresolved source conflicts; hard
blockers; unassigned actions; checkrides/evaluations, directed DVs and at-risk
upgrades not visibly supported; line/configuration/support inconsistencies; and
exact DO decisions needed Thursday. Infer the current version and ask only if more
than one draft could reasonably control.
```

**Exit condition:** an exact integrated draft is selected for Thursday human QC and full Gemini review; unresolved issues have owners or are framed as DO decisions.

**Next:** **06 Thursday - Full Schedule QC.docx**.
