# Policy preservation crosswalk

This document shows where each approved contract lives, so that simplifying the operator kit never silently drops a safeguard. The v0.6 → v0.7 map below is current. The older v0.3 → v0.4 table is kept for provenance; read its "Primer §" references as the matching rule groups in [the task-file core](../packaging/kit/core.md), as mapped below. Historical copies of earlier files are in Git history, not the current tree.

The Pantons profile (Squadron Rules Section 1) together with the task files preserves the operational contract. Another squadron must not treat Pantons rules as universal policy.

## v0.6 → v0.7 contract map (package 0.7.0)

Package 0.7.0 replaces the upload primer, 12 checklists, 20 prompts and 9 forms with 8 self-contained task files. Each one carries the same core (`packaging/kit/core.md`) plus its own script. The approving decisions are [V070-01 to V070-07](design-decisions.md). `tests/test_contract_coverage.py` checks every row's key phrase in every task file, or in the named task.

| Contract (v0.6 location) | v0.7 location |
| --- | --- |
| No delegation; no named model (every prompt) | Guard line at the top of every task file; core section 1 |
| Humans schedule, approve, publish; no assistant lineup (primer §1 intro) | Core section 1 |
| Thursday Buy/Sell is the formal DO buy; no routine second buy; supplemental decision; publication separate (primer §1, §6) | Core rule A; tasks 4 and 5 |
| Daily scheduler/Top 3 bounds; waivers need DO plus authority (primer §1) | Core rule A; task 6 |
| Human confirmation closes only the stated concern (primer §1) | Core rule A; tasks 3, 4 and 5 |
| GAMECHANGER-only regulatory evidence; four outcomes; no compliance claim; P-### ledger and cadence (primer §1 GAMECHANGER) | Core rule B; WEEK FILE section 5; tasks 1, 3, 5, 6 |
| Facts versus interpretations; never invent; product statuses; integrity gate; CONFLICTS ONLY default; missing inputs limit only affected checks (primer §1, §3, §4) | Core rule C |
| Artifact responsibility map (primer §4) | Core rule A ("Who answers what") |
| Five internal phases by work status; no weekday approval (primer §2) | Core section 5; WEEK FILE header "Work status" |
| Next-week default; reflows on the current published week; no startup questionnaire (primer §2) | Core section 5; tasks 1 and 6 |
| Version roles and comparison baselines (primer §7) | Core section 5; WEEK FILE section 2 |
| Scheduling categories, availability, qualifications, spares, cascades, phase-appropriate churn (primer §5) | Core rule D; Squadron Rules Section 1 |
| 30-day outlook; one moderate downside; recommendation format (primer §8) | Core rule E; WEEK FILE section 7 |
| Playbook governance (primer §9) | Core rule E; WEEK FILE section 9; Squadron Rules Section 3 |
| Blind-test integrity and historical publication versions (primer §10) | Core rule F |
| One next action; all material issues visible; complete weekly record (primer §11) | Core sections 3 and 7; the WEEK FILE replaces the weekly working record |
| Handoff and resume (primer §9, §11; form 08) | The WEEK FILE plus a new chat per task; HELP covers recovery |
| Wednesday integration review is not approval (primer §11) | Task 2 |
| Thursday fresh whole-schedule QC and readiness statuses (primer §11) | Task 3 |
| Optional DO review: read-only; REGULATORY QUESTION label (primer §11) | DO ONLY task; accepted items recorded with task 4 |
| Run control/manifest, decision record, execution update forms (forms 01, 06, 07) | WEEK FILE sections 2, 3, 6 and 8 |
| Stable references and playbook (forms 04, 09) | Squadron Rules Sections 2 and 3 |
| DO and Flight Commander input forms (forms 02, 03) | Removed. Those inputs arrive as the squadron's own emails or notes listed on the input checklist |

## v0.3 → v0.4 crosswalk (historical)

| v0.3 topic | v0.4 location | Disposition |
| --- | --- | --- |
| Advisory role / no invented facts | Primer §§1,3,5 | Preserved |
| Learning system | Primer §9; playbook form | Preserved with explicit DO promotion |
| Run controls | Primer §2; form 01 | Five phases; historical condition separate |
| PRE-DRAFT | Phase 1; profile | No complete initial lineup; interactive planning explicit |
| DRAFT REVIEW | Phase 2 | Preserved exact changes, cascades and primary-line emphasis |
| FINAL QC | Phase 4 after buy/sell | Preserved hard-infeasibility/major-risk focus and explicit DO direction for substantial late churn |
| RECOVERY | Phase 5 | Preserved recovery priorities and daily authority boundaries |
| Upload/ingest | Primer §3; form 01 | Full review waits for request; scoped questions permitted |
| Evidence / history restriction | Primer §§1–4,10; forms 05,07 | Live/cutoff-valid actuals distinguished from hindsight; publication-derived regulatory conclusions now fail closed through GAMECHANGER rather than model memory/web fallback |
| Hierarchy, qualifications, availability | Primer §§1,5; profile | Preserved conservative treatment and human-confirmed closure; publication-derived qualification/currency consequences require connector-grounded rule evidence |
| Upgrade accounting / same-day rules | Pantons profile | Preserved exact local policy |
| IP/personnel use | Pantons profile | Preserved qualification, rotation and workload rules |
| Availability / crew rest | Primer §§1,5; profile; form 04 | Preserved exact-time checks and unknown-boundary manual verification; publication-derived rest/duty rule requires GAMECHANGER evidence |
| Aircraft / turn / spares | Pantons profile | Preserved protected-spare and primary-line rules |
| Configuration / weather | Pantons profile; primer §5 | Preserved local-source requirement and uncertainty treatment |
| Full-line use / backups | Pantons profile; primer §5 | Preserved feasible cascade and backup checks |
| Outlook / stress tests | Primer §8; profile | Preserved 30-day and weekly moderate downside analysis |
| Reports / stops / blind integrity | Primer §§8–10; report contracts | Preserved; P-### publication ledger and connector-specific stop/uncertainty behavior added |
| Starter forms | Forms 01–09 | Existing-source references and change capture replace duplicate transcription; no new persistent form required for the weekly P-### ledger |
| Products | README, day guides, phase reference | Standard products retained; no mandatory manual re-entry gate |

## Current workflow overlays

- **Pantons battle rhythm:** inputs due NLT COB Monday; Tuesday start/ingest/planning; Wednesday bulk build; Thursday full QC; optional DO adversarial review; **Thursday buy/sell and formal DO buy**; post-buy/sell implementation/QC; Friday publication; execution reflows.
- **Default weekly context:** unless a human explicitly selects another period, pre-execution work targets the next execution week; execution reflows use the current published week, and active-week handoffs/historical work keep their recorded or explicit periods. The assistant infers run/version state from evidence and drafts run control without a startup questionnaire.
- **Wednesday integration:** the Cross-Functional Schedule Integration Review verifies source-owner inputs and assigns unresolved issues; it is not a Buy/Buy-Sell/approval event.
- **Calculated-source integrity:** products use CURRENT, STALE, PARTIAL, CONFLICTED, INTEGRITY FAILED, UNREADABLE or SUPERSEDED. Material identity/formula defects prevent affected person-specific conclusions even when cached values appear plausible.
- **Day-based operator manual:** operator navigation follows actual workdays and steps. Internal five-phase state control remains status-based.
- **Tuesday planning focus:** checkrides/evaluations, directed DV/senior-leader flyers and upgrade windows/resources are explicit before the human schedule build.
- **Conversation roles:** model-neutral; all prompts prohibit subagent delegation. The DO may use a separate human-started conversation for an optional independent review.
- **Publication-grounded QC:** DoW Policies Beta (GAMECHANGER) is the required AI-side source for publication-derived regulatory determinations. Tuesday builds the initial P-### Weekly Publication Rule Ledger and currency/regulatory baseline; Thursday refreshes it against the near-final schedule; post-buy and execution changes re-query affected rules.
- **Source gate:** model memory, generic military knowledge, ordinary web search and uncited synthesis cannot establish a publication-derived requirement. Missing support is CANNOT VERIFY; conflicting retrieved authorities are SOURCE CONFLICT. Unaffected scheduling work continues.
- **Adversarial boundary:** reviewer is read-only. Only explicit DO-accepted human direction returns to the assistant.

## Conflicts resolved explicitly

1. **Buy/sell authority:** V04-19 is current. The Thursday buy/sell is the formal DO buy event. The presented schedule plus explicit DO directions form the approved baseline. Post-buy/sell implementation receives QC but no routine second buy. A material deviation beyond the recorded direction returns to the DO for supplemental decision before publication.
2. **Publication authority:** V04-21/V04-22 are current for AI-side regulatory evidence. Local scheduling rules remain sourced from the approved profile/human direction, but a publication-derived currency/qualification/duty/evaluation/syllabus/credit requirement cannot be supplied from model memory or web search. GAMECHANGER evidence is advisory evidence, not approval or waiver authority.
3. **Actual results:** distinguish live execution and cutoff-valid actuals from later hindsight.
4. **Quiet ingestion versus questions:** bulk uploads remain quiet while explicit planning questions receive bounded answers.
5. **Missing evidence versus human confirmation:** missing-check warnings remain, but an explicit human confirmation may close the stated concern without a new proof requirement. It does not transform missing GAMECHANGER evidence into SOURCE-BACKED OK.
6. **Recovery churn versus daily authority:** full-line recovery cascades remain analyzable; human approval boundaries determine the required action.
## Approved beginner workflow in package 0.6.0

One action per checkbox replaces the long operator prose. Complete short prompts are supplied as plain-text files and printed in each relevant checklist. Every prompt starts with "Do not delegate to subagents." No named model is required. The reusable primer contains the detailed command contracts. Intake defaults to CONFLICTS ONLY; all required facts and evidence remain in one complete weekly record with distinct sections. Full Thursday QC remains a fresh entire-schedule review, with the existing source and human-authority gates.
