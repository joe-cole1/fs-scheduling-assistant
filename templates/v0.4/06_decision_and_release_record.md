# Weekly Decision and Release Record — v0.4

One cumulative human decision record for the week. The assistant drafts entries; humans supply decisions. An assistant recommendation never creates an approval. Keep stable IDs through revisions and handoffs.

Execution week: [dates]  
Record version / as-of / timezone: [values]

## Decisions, proposals and buy/sell dispositions

| D-### | Origin: buy/sell direction / new proposal / human confirmation / waiver | Exact direction or proposal | Person/role and time as provided | Scope / effective period | Affected schedule/event IDs | Disposition | Evidence / QC finding / superseding decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ID] | [type] | [exact substance] | [values] | [values] | [values] | [status] | [reference] |

Directed correction statuses: Open → Implemented—QC pending → Verified or Human-confirmed. Use Blocked when infeasible; return to DO. Superseded requires a recorded human decision. For proposals, retain Pending/Accepted/Rejected/Withdrawn and link any resulting direction.

Every buy/sell direction must have a disposition. Mark new proposed changes separately; do not hide them inside corrections. A human's scoped “it's okay” can close a QC concern without additional evidence demands.

## Waivers

| Waiver ID / linked D-### | Requirement and exact exception | Scope/effective/expiry | Applicable waiver authority as supplied | Authority decision/status | DO involvement/decision | Evidence or exact human confirmation | Remaining action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [W-###] | [value] | [value] | [value or unknown] | [pending/approved/rejected] | [pending/completed and statement] | [value] | [value] |

All waivers go through the DO and the applicable authority. If the DO is the supplied waiver authority, one explicit decision may satisfy both roles. Do not assume that role. Buy/sell approval or publication never substitutes for an unrecorded waiver.

## Thursday buy/sell record

| Milestone | Exact schedule filename/version | Human decision/confirmation | Date/time/timezone | Notes / directions |
| --- | --- | --- | --- | --- |
| Presented at buy/sell | [value] | [presentation record] | [value] | [open decisions] |
| DO buy | [value or Not bought] | [explicit DO approval statement] | [value] | [scope] |
| Buy/sell directions | [same presented version + D-IDs] | [exact directions] | [value] | [directions become part of approved baseline] |

The formal DO buy occurs during the Thursday buy/sell when the DO explicitly approves the schedule. The approved baseline consists of the presented version plus the recorded DO directions. Do not infer buy merely because the meeting occurred.

## Post-buy/sell implementation and final QC

| Corrected filename/version | Buy/sell-presented baseline | Previous corrected version | Directed decisions implemented | New proposals | Downstream checks and findings | Human-confirmed closures | Remaining issues / supplemental DO decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [value] | [value] | [value/None] | [D-IDs] | [R/D-IDs] | [report/reference] | [D-IDs] | [IDs/None] |

Check exact direction disposition, complete cascades, affected duty/role/resource/training relationships, and cross-cutting conflicts. There is no routine second DO buy. If the needed solution materially exceeds the recorded direction, return that item to the DO and record the supplemental decision.

## Weekly publication

| Exact published filename/version | Distribution confirmation | Date/time/timezone | Reconciliation to Thursday buy/sell | Supplemental DO decisions / differences |
| --- | --- | --- | --- | --- |
| [value or Not yet published] | [human statement] | [value] | [faithful implementation / differences] | [D-IDs/None] |

Do not infer publication from approval. The assistant never sends the schedule. Material differences not covered by buy/sell direction or a later explicit DO decision remain unresolved.

## Daily sign-off and current baseline

| Execution date | Daily schedule filename/version | Daily scheduler sign-off | Top 3 sign-off | Changes outside published commitments / DO decision | Linked waiver IDs | Current signed baseline confirmed by human |
| --- | --- | --- | --- | --- | --- | --- |
| [date] | [value] | [statement/time] | [statement/time] | [None or decision ID] | [None or W-IDs] | [value] |

## Changes from weekly commitment

| Change ID | Weekly baseline → resulting plan | Times / turn / support / directed guidance affected? | Required DO decision | Other coordination | Disposition |
| --- | --- | --- | --- | --- | --- |
| [ID] | [exact change] | [scope] | [record or pending] | [known owners/status] | [value] |