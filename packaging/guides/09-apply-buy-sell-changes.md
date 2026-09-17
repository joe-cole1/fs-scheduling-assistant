# Thursday–Friday — Apply buy/sell changes

Use this after the Thursday buy/sell. The DO has already bought the schedule as part of that meeting. Schedulers now implement the recorded buy/sell directions; Gemini verifies implementation and downstream effects. **This is not a second approval event.**

Upload or identify:

- The corrected active schedule with a new filename/version.
- The buy/sell-presented schedule.
- The DO buy statement and decision record.
- The current Weekly Publication Rule Ledger.
- Updated products or human confirmations relevant to the corrections.

Paste:

```text
Phase 4 — Post-buy/sell implementation and QC.
Primary scheduler workflow: Gemini.
Corrected active schedule: [exact filename/version].
Buy/sell-presented baseline: [exact filename/version].
Previous corrected version, if any: [filename/version or NONE].
DO buy/sell directions: [decision-record filename or recorded directions].

Verify the disposition of EVERY buy/sell decision. Confirm the corrected schedule
faithfully implements the DO's recorded directions. Find implementation mistakes
and unintended second- and third-order effects, then check the complete corrected
schedule for conflicts. Keep new proposed changes separate from directed
corrections. Flag hard infeasibility and major upgrade risk.

For every correction that changes a person, role, event, timing, prerequisite,
currency/qualification state or other publication-relevant fact, run a delta
publication QC through DoW Policies Beta (GAMECHANGER). Update the affected P-###
entries or add new ones. Do not re-search unaffected rules merely for churn, but
do not rely on the prior ledger when the correction changes applicability.
Publication-based regulatory conclusions must still identify a connector-retrieved
publication number/title and paragraph/page/usable locator. No model-memory or web
fallback is allowed. Use SOURCE-BACKED OK, SOURCE-BACKED ISSUE, CANNOT VERIFY or
SOURCE CONFLICT.

Do not request or imply a routine second DO buy. If a direction cannot be
implemented as approved, or the necessary solution materially exceeds the scope
of the recorded direction, identify the exact issue and return it to the DO for
a supplemental decision. Do not silently expand the Thursday buy.
```

**You should get:** a disposition for every buy/sell direction, implementation/QC findings, affected publication-rule delta results, remaining issues, and any specific item that must return to the DO.

A scoped human confirmation can close the stated QC concern. It does not convert missing GAMECHANGER evidence into SOURCE-BACKED OK. Waivers still require the DO and applicable waiver authority.

**Next:** when the directed changes are implemented and QC'd, follow **10 Friday - Final QC and Publish.docx**.