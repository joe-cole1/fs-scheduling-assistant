# Weekly Run Control and Product Manifest — v0.4

Update the same weekly record; do not recreate unchanged source facts every session. The assistant may draft this record for human confirmation. Blank placeholders are not facts or authority.

## Run

| Field | Value |
| --- | --- |
| Execution week | [start date through end date under approved local counting week; Pantons: Sunday–Saturday] |
| Active phase | [1 Product gathering / 2 Initial draft / 3 Sell / 4 Corrections-QC-approval-publication / 5 Execution reflows] |
| Requested task | [planning question / full draft review / sell brief / correction QC / reflow / handoff] |
| Parallel or reopened work | [phase/task or None] |
| As-of / timezone | [date time timezone] |
| Requested by | [name/callsign/role as provided] |
| Test condition | [OPERATIONAL / BLIND REVIEW / RETROSPECTIVE] |
| Historical cutoff | [exact date/time/timezone, or N/A] |
| Authorized actual-results scope | [live results as of time / known by historical cutoff / later outcomes for retrospective / none] |
| Ingest gate | [CONFIRM / CONFLICTS ONLY] |
| Report depth | [BRIEF / DETAILED] |
| Local profile / approved playbook | [filenames and versions; missing if absent] |
| DO guidance / decision record | [filenames and versions] |
| Scenarios | [DO-directed / assistant selects weekly moderate case / carry forward scenario ID] |
| 30-day assumptions | [confirmed assumptions or gaps] |
| Model / version displayed | [as shown or Not displayed] |

## Version roles

| Role | Exact filename/version | State / confirming human statement |
| --- | --- | --- |
| Active schedule being analyzed | [value or None in phase 1] | [working / corrected / approved / published / daily / proposal] |
| Initial-draft comparison baseline | [human-selected value or explicitly None] | [confirmation] |
| Sell-presented schedule | [value or Not yet presented] | [presentation date] |
| Latest corrected version | [value or N/A] | [QC status] |
| Formally bought weekly schedule | [value or Not yet bought] | [DO decision ID/time] |
| Published weekly schedule | [value or Not yet published] | [publication confirmation/time] |
| Weekly cumulative comparison baseline | [published version] | [explicit selection if republished] |

| Affected execution date | Latest signed daily filename/version | Daily scheduler / Top 3 sign-off record | Immediate baseline used |
| --- | --- | --- | --- |
| [date] | [value or None] | [decision IDs or Not signed] | [signed daily, otherwise published weekly] |

List each affected date separately for multi-day reflows. An unsigned proposed daily update does not replace a signed baseline.

## Product manifest

| Product | Exact filename / source | Version / issued / effective / coverage | Current authority or status | Limitation / supersedes |
| --- | --- | --- | --- | --- |
| Schedule(s) and baselines | [files] | [values] | [roles above] | [value] |
| Maintenance / turn / configuration / spares | [source] | [values] | [status] | [value] |
| Upgrade / MQT tracker | [source] | [values] | [status] | [value] |
| Leave and exact-time commitments | [source] | [values] | [status] | [value] |
| Currency tracker | [source] | [values] | [status] | [value] |
| Letter of Xs / exceptions | [source] | [values] | [status] | [value] |
| Simulator schedule | [source] | [values] | [status] | [value] |
| Range / airspace / tanker / adversary / support | [source] | [values] | [status] | [value] |
| Forecast / weather guidance | [source] | [values] | [status] | [value] |
| Training phase/configuration plan | [source] | [values] | [status] | [value] |
| Callsign-name roster | [source] | [values] | [status] | [value] |
| DO / Flt CC inputs | [source] | [values] | [issued / proposed] | [value] |
| Stable references and approved playbook | [source] | [values] | [status] | [value] |
| Prior duty / knowable actuals | [source] | [values] | [status/cutoff] | [value] |
| Execution update / handoff / locked blind report | [source] | [values] | [authorized scope] | [value] |

## Gaps, conflicts, and confirmations

| Finding ID | Missing/conflicting input | Affected check or recommendation | Current restriction / uncertainty | Resolver / needed by | Human confirmation or disposition |
| --- | --- | --- | --- | --- | --- |
| [F-###] | [e.g. DO checkride priorities not provided] | [scope] | [effect] | [if known] | [exact confirmation if given] |

Schedulers decide when drafting begins. Missing products do not prevent unaffected planning. Human confirmation can close a specific concern without another upload. Do not infer a blanket waiver.

## Historical integrity only

- [ ] Cutoff and permitted actual-results scope are explicit.
- [ ] Every historical input, including handoff and transcript, is free of later hindsight.
- [ ] A contaminated blind review stops and restarts in an isolated conversation; no quarantine-and-continue.
- [ ] Retrospective has an identified locked blind report.

## Request

[Ask a bounded question now, or explicitly request the phase analysis when ready. Example: “Begin review of draft v2 using draft v1 as the baseline.”]
