# Weekly Run Control and Product Manifest — v0.4

Assistant-generated and human-reviewable. The operator does **not** complete this form before startup. For normal pre-execution weekly work, the assistant defaults to the next execution week unless a human selects another period. Execution reflows use the current published execution week; an active-week handoff keeps its recorded week; historical work uses its explicit cutoff/period. The assistant infers the remaining fields from the current date, approved local counting week, selected guide, folder/file names, schedule headers, uploaded products and conversation. It asks only when an ambiguity materially changes the work.

Update the same weekly record; do not recreate unchanged source facts every session. Blank placeholders are not facts or authority.

## Run

| Field | Value |
| --- | --- |
| Execution week | [assistant-inferred next week for pre-execution work; current published week for execution reflow; handoff/historical/explicit human-selected period when applicable] |
| Basis for week selection | [current date/local profile/folder/header/handoff/human statement] |
| Active phase / requested task | [assistant-inferred status and task] |
| Parallel or reopened work | [phase/task or None] |
| As-of / timezone | [inferred from current conversation/products; ask only if material] |
| Requested by | [name/callsign/role when provided] |
| Test condition | [OPERATIONAL unless BLIND REVIEW or RETROSPECTIVE is explicitly established] |
| Historical cutoff | [exact value when applicable, otherwise N/A] |
| Authorized actual-results scope | [live results / cutoff-valid results / retrospective / none] |
| Ingest gate | [assistant-selected CONFIRM or CONFLICTS ONLY based on task; human may override] |
| Report depth | [assistant-selected BRIEF or DETAILED based on task; human may override] |
| Local profile / approved playbook | [filenames and versions; Missing if absent] |
| DO guidance / decision record | [filenames and versions] |
| Scenarios / 30-day assumptions | [current IDs, assumptions or gaps] |
| GAMECHANGER availability | [Available / Not available / Unknown in this conversation] |
| Model / version displayed | [as shown or Not displayed] |
| Consequential assumptions requiring attention | [None, or compact list; do not list routine inferred fields] |

## Version roles

| Role | Exact filename/version | State / confirming human statement |
| --- | --- | --- |
| Active schedule being analyzed | [inferred value or None in product gathering] | [working / implementation / published / daily / proposal] |
| Initial-draft comparison baseline | [inferred human-selected value or None] | [basis/confirmation] |
| Thursday Buy/Sell-presented schedule | [value or Not yet presented] | [presentation date] |
| DO Buy/Sell approval | [same presented version or Not bought] | [explicit DO statement / decision ID / time] |
| Buy/Sell directions forming approved baseline | [D-IDs or None] | [exact scope] |
| Latest post-Buy/Sell implementation version | [value or N/A] | [faithful / blocked / material deviation] |
| Supplemental DO decision(s), if required | [D-IDs or None] | [scope/time] |
| Published weekly schedule | [value or Not yet published] | [publication confirmation/time] |
| Weekly cumulative comparison baseline | [published version] | [explicit selection if republished] |

If more than one file could reasonably fill a controlling version role, ask one focused question. Never select among competing schedules silently. The approved Thursday Buy/Sell baseline is the exact presented schedule plus recorded DO directions. A faithful corrected file does not require a routine second DO buy.

| Affected execution date | Latest signed daily filename/version | Daily scheduler / Top 3 sign-off record | Immediate baseline used |
| --- | --- | --- | --- |
| [date] | [value or None] | [decision IDs or Not signed] | [signed daily, otherwise published weekly] |

## Product manifest

Use only these source statuses: **CURRENT, STALE, PARTIAL, CONFLICTED, INTEGRITY FAILED, UNREADABLE, SUPERSEDED**. Assign the most consequential primary status for the intended use and record any additional limitation in the limitation column.

| Product | Exact filename / source | Version / issued / effective / coverage | Status | Integrity / identity check | Limitation / supersedes |
| --- | --- | --- | --- | --- | --- |
| Schedule(s) and baselines | [files] | [values] | [status] | [N/A or check] | [value] |
| Maintenance / turn / configuration / spares | [source] | [values] | [status] | [check] | [value] |
| Upgrade / MQT tracker | [source] | [values] | [status] | [stable person/event linkage] | [value] |
| Leave and exact-time commitments | [source] | [values] | [status] | [person/date linkage] | [value] |
| Currency / qualification input | [source] | [values] | [status] | [stable identity, duplicates, formula/errors, as-of] | [value] |
| Letter of Xs / exceptions | [source] | [values] | [status] | [person/role linkage] | [value] |
| Simulator schedule | [source] | [values] | [status] | [slot/date linkage] | [value] |
| Range / airspace / tanker / adversary / support | [source] | [values] | [status] | [date/time linkage] | [value] |
| Forecast / weather guidance | [source] | [values] | [status] | [issue time/coverage] | [value] |
| Training phase/configuration plan | [source] | [values] | [status] | [effective period] | [value] |
| Callsign-name roster | [source] | [values] | [status] | [duplicate/alias handling] | [value] |
| DO / Flt CC inputs | [source] | [values] | [status] | [scope/effective week] | [value] |
| Stable references and approved playbook | [source] | [values] | [status] | [version/effective date] | [value] |
| Prior duty / knowable actuals | [source] | [values] | [status] | [date/person linkage] | [value] |
| Execution update / handoff / locked blind report | [source] | [values] | [status] | [cutoff/scope] | [value] |

A calculated person-specific product is **INTEGRITY FAILED** when it cannot reliably tie displayed values to the correct person/event, has unresolved duplicate identity, broken lookups/formulas, or another material integrity defect. Do not use affected values merely because cached outputs appear plausible. Continue unaffected analysis.

## Artifact responsibility map

| Artifact | It answers |
| --- | --- |
| Connector-retrieved governing publication | Applicable publication-derived requirement and waiver/approval language |
| Official squadron SOP | Who acts, when the process occurs and local administrative steps |
| Approved Local Profile | Standing local scheduling rules and preferences |
| Weekly priorities / explicit human direction | What matters for the target week |
| Functional products and trackers | Current personnel, aircraft, support, accomplishment and availability facts |
| Schedule artifact | What is planned in that exact version |
| AI fact and publication ledgers | Traceability and limitations of checks performed; evidence only |
| Decision and release record | What human authorities decided and what was published |
| AI output | Advisory interpretation and recommendation only |

## Gaps, conflicts, and confirmations

| Finding ID | Missing/conflicting/integrity-limited input | Affected check or recommendation | Current restriction / uncertainty | Resolver / needed by | Human confirmation or disposition |
| --- | --- | --- | --- | --- | --- |
| [F-###] | [value] | [scope] | [effect] | [if known] | [exact confirmation if given] |

Schedulers decide when drafting begins. Missing or failed products do not prevent unaffected planning. Human confirmation may close a specific scheduling concern but does not repair source integrity, establish a publication rule, or imply a blanket waiver.

## Historical integrity only

- [ ] Cutoff and permitted actual-results scope are explicit.
- [ ] Every historical input, including handoff and transcript, is free of later hindsight.
- [ ] A contaminated blind review stops and restarts in an isolated conversation.
- [ ] Retrospective has an identified locked blind report.

## Request

[The assistant infers the current task from the selected guide and conversation. Add only a bounded question, changed fact or explicit human direction that is not already present in the products.]
