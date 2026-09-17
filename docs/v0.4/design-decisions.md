# Approved design decisions — v0.4

Authority: explicit DO/product-authority decisions in the v0.4 planning conversation. This document records product design, not a weekly operational approval.

| ID | Approved decision |
| --- | --- |
| V04-01 | Use five phase-based operational controls; status, not weekday, controls transitions. |
| V04-02 | Schedulers create the initial lineup. Before that, the assistant consolidates inputs, flags missing/conflicting information and answers evidence-backed planning questions. |
| V04-03 | Schedulers decide when drafting starts. Missing products are flagged with consequences rather than imposing a complete-packet gate. |
| V04-04 | Historical decision: sell directions were originally followed by corrections/QC and a later formal DO buy. **Superseded by V04-19.** |
| V04-05 | Apply FINAL QC behavior after the DO establishes directions. Preserve hard-conflict/major-risk correction and show substantial additional churn as a DO option. |
| V04-06 | Historical decision: formal buy approved the exact corrected schedule after QC. **Superseded by V04-19.** |
| V04-07 | Daily scheduler and Top 3 sign off on feasible personnel/mission changes within published times, aircraft turn pattern, coordinated support and explicit DO guidance. Changes outside those boundaries return to the DO. |
| V04-08 | Every waiver must go through the DO and the applicable waiver authority. Buy/sell approval never implicitly approves every waiver. |
| V04-09 | Execution immediate comparison uses the latest signed daily schedule for the affected day, or published weekly schedule if no daily exists. Cumulative comparison uses the published weekly schedule. |
| V04-10 | Explicit human confirmation is sufficient to close the identified QC concern without mandatory supporting uploads. Record it as human-confirmed, not independently checked. |
| V04-11 | Prefer one main conversation per execution week. Do not rely on shared-chat support, native export or automatic memory. |
| V04-12 | Use a concise current-state Word handoff plus actual applicable source products when an active week changes users/conversations. |
| V04-13 | Use existing standard products; placeholder forms capture missing guidance, changes and recommendations without duplicate transcription. |
| V04-14 | Preserve v0.3 scheduling rules, advisory authority, evidence/normalization, availability/qualification checks, spares, accounting, local same-day rules and stable playbook decisions. |
| V04-15 | Historical blind condition stays separate from phase. Hindsight contamination requires an isolated clean restart; legitimate live execution actuals are allowed. |
| V04-16 | Repository products must be usable by a pilot new to scheduling. Operator instructions are Word-first and executable. |
| V04-17 | Pantons normal battle rhythm: inputs due NLT COB Monday; Tuesday upload/ingest and planning; Wednesday bulk build; Thursday scheduler plus assistant full QC; optional DO adversarial review; Thursday buy/sell; post-buy/sell implementation/QC; Friday publication; execution-week reflows. |
| V04-18 | Main GenAI.mil scheduler workflow uses Gemini 3.7 Flash when available. Optional DO adversarial review uses a separate GPT-5.6 Terra or Grok Expert 4.5 conversation and is read-only. |
| V04-19 | **Current authority rule. The Thursday schedule buy/sell is the formal DO buy event.** The approved baseline is the exact presented schedule plus explicit DO directions recorded in that meeting. Schedulers implement those directions and Gemini verifies implementation/second-order effects. There is no routine second DO buy afterward. A material solution outside the recorded direction returns to the DO for a supplemental decision before publication. Publication remains a separate human action. V04-19 supersedes V04-04, V04-06 and any earlier wording that placed routine buy after correction/QC. |
| V04-20 | Operator instructions are organized chronologically by Monday, Tuesday start, Tuesday planning, Wednesday build, Thursday QC, optional DO review, Thursday buy/sell, post-buy/sell implementation, Friday final QC/publication, execution reflows, handoff, update and setup check. Internal phases remain underneath this day-based navigation. |
| V04-21 | **Publication-based regulatory findings are fail-closed and connector-grounded.** For currency, qualification, crew-rest/duty, evaluation, syllabus/prerequisite, event-credit, recurring-training or other publication-derived requirements, the main Gemini workflow may make a regulatory determination only from a DoW Policies Beta (GAMECHANGER) publication retrieved in the current workflow. Model memory, generic military knowledge, ordinary web search and uncited AI synthesis are not acceptable regulatory evidence. If the connector does not return a sufficiently traceable applicable publication, report **CANNOT VERIFY** and make no regulatory determination. |
| V04-22 | Use a **Weekly Publication Rule Ledger** for the connector-grounded checks. Tuesday planning discovers relevant rules and builds the initial ledger/currency baseline; Thursday full QC refreshes and expands it against the complete schedule before buy/sell; post-buy/sell changes and execution reflows re-query affected rules as delta checks. Each rule records publication identity, applicability, current/effective status when available, paragraph/page/locator, retrieval time and result. Conflicting authoritative sources are reported as **SOURCE CONFLICT** for human review, not reconciled from model memory. |

## Routine implementation choices within the approved design

- Separate reusable primer from the Pantons local profile; another squadron supplies its own approved profile.
- Use one weekly decision/release record instead of recopying decisions across forms.
- Use stable fact, event, recommendation, decision and candidate references; numbering is bookkeeping, not new authority.
- Add a live execution update form distinct from historical retrospective outcomes.
- Map immediate baselines per affected date for multi-day reflows.
- Retain current moderate downside analysis and reassess on material changes rather than every chat message.
- Model roles never create or remove human authority.
- Publication-grounded QC is a bounded connector capability layered on the existing scheduling workflow. If GAMECHANGER is unavailable, unaffected scheduling analysis continues, but publication-based checks remain explicitly unverified rather than falling back to model knowledge or the web.

## Not assumed or changed

No platform collaboration/export feature is asserted. No API/custom software/agent prerequisite for the core scheduling workflow. No public release or repository merge is implied by creation of a review branch. No new numerical duty, rest, weather or syllabus limits. No mandatory documentary proof to accept a scoped human confirmation. No assistant source-file modification or lesson promotion. The optional DO adversarial review is not a second mandatory scheduler review and does not independently approve or reject a schedule. GAMECHANGER does not grant approval or waiver authority and does not replace human interpretation when publications conflict or applicability is unclear.

## Approved beginner packaging decisions — v0.4.1

| ID | Approved decision |
| --- | --- |
| V041-01 | Two complete downloads: dedicated Pantons and first-time other-squadron setup. |
| V041-02 | Short START HERE plus separate numbered Word guides in Instructions; upload the startup primer and use short activation/phase prompts. |
| V041-03 | Permanent extracted folder with a ready-made weekly folder to copy. Keep local guidance and weekly work outside replaceable System. |
| V041-04 | Manual numbered updates adopted next week. No elaborate weekly system copies or automatic update mechanism. |
| V041-05 | Remove repository archives. Use branches, prior PRs and Git history instead. |

## Approved release automation follow-up

- Publishing a release triggers dynamic ZIP generation and attachment from the tagged source; manual trigger supports recovery.
- Release assets are the download source; ZIP copies are not kept in the repository tree.
- Release notes describe user impact, update actions, validation and limitations. Squadron updates remain manual and are adopted next week.