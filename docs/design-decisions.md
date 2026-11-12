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
| V04-18 | Historical model-role preference. **Superseded by V060-02.** The optional independent DO review remains separate and read-only. |
| V04-19 | **Current authority rule. The Thursday schedule buy/sell is the formal DO buy event.** The approved baseline is the exact presented schedule plus explicit DO directions recorded in that meeting. Schedulers implement those directions and the assistant verifies implementation/second-order effects. There is no routine second DO buy afterward. A material solution outside the recorded direction returns to the DO for a supplemental decision before publication. Publication remains a separate human action. V04-19 supersedes V04-04, V04-06 and any earlier wording that placed routine buy after correction/QC. |
| V04-20 | Operator instructions are organized chronologically by Monday, Tuesday start, Tuesday planning, Wednesday build, Thursday QC, optional DO review, Thursday buy/sell, post-buy/sell implementation, Friday final QC/publication, execution reflows, handoff, update and setup check. Internal phases remain underneath this day-based navigation. |
| V04-21 | **Publication-based regulatory findings are fail-closed and connector-grounded.** For currency, qualification, crew-rest/duty, evaluation, syllabus/prerequisite, event-credit, recurring-training or other publication-derived requirements, the main assistant workflow may make a regulatory determination only from a DoW Policies Beta (GAMECHANGER) publication retrieved in the current workflow. Model memory, generic military knowledge, ordinary web search and uncited AI synthesis are not acceptable regulatory evidence. If the connector does not return a sufficiently traceable applicable publication, report **CANNOT VERIFY** and make no regulatory determination. |
| V04-22 | Use a **Weekly Publication Rule Ledger** for the connector-grounded checks. Tuesday planning discovers relevant rules and builds the initial ledger/currency baseline; Thursday full QC refreshes and expands it against the complete schedule before buy/sell; post-buy/sell changes and execution reflows re-query affected rules as delta checks. Each rule records publication identity, applicability, current/effective status when available, paragraph/page/locator, retrieval time and result. Conflicting authoritative sources are reported as **SOURCE CONFLICT** for human review, not reconciled from model memory. |

| V04-23 | **Default next-week startup.** Unless a human explicitly selects another period, normal pre-execution weekly scheduling work targets the next execution week under the approved local counting week. Execution reflows use the current published execution week; active-week handoffs keep their recorded week; historical work keeps its explicit period/cutoff. The assistant infers dates, phase/task, as-of, version roles, source state and connector availability from evidence, drafts run control itself and does not require a startup field list. It asks one focused question only when a material ambiguity remains. |
| V04-24 | **Calculated-source integrity gate.** Products use CURRENT, STALE, PARTIAL, CONFLICTED, INTEGRITY FAILED, UNREADABLE or SUPERSEDED. A material person/event identity, duplicate-key, lookup/formula or similar integrity defect prevents affected person-specific conclusions even when cached values appear plausible; unaffected analysis continues. |
| V04-25 | **Wednesday integration terminology.** The cross-functional Wednesday meeting is the Cross-Functional Schedule Integration Review. It verifies inputs and assigns unresolved issues; it is not a Buy, Buy/Sell or approval event. Thursday remains the formal Schedule Buy/Sell and DO buy. |
| V04-26 | **Artifact responsibility map.** Governing publications answer publication requirements; the SOP answers process/roles; the Local Profile answers standing local rules; weekly direction answers target-week intent; functional products answer current facts; schedule versions answer planned state; AI ledgers preserve traceability; and the decision/release record proves human decisions and publication. AI output remains advisory. |

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
## Approved beginner workflow package 0.6.0

| ID | Approved decision |
| --- | --- |
| V060-01 | Apply the approved Tuesday/Thursday examples across the full package: one-page checklists, one action per checkbox, complete short copy/paste prompts, and one concrete next action from the assistant. Detailed contracts live in the upload primer. |
| V060-02 | Every complete prompt includes the exact instruction "Do not delegate to subagents". The assistant performs its own work in the current conversation. No specific model is required. This supersedes V04-18 and prior model-specific workflow wording. |
| V060-03 | Default intake to CONFLICTS ONLY. Keep all material findings visible and preserve complete evidence, ledgers, decisions, outlook, scenario and version roles in one cumulative weekly record with distinct sections. The short visible answer never narrows a required check. |
| V060-04 | Tuesday startup explicitly requests intake and planning together. Thursday’s short QC command still requests a fresh entire-schedule review and GAMECHANGER refresh. Upload alone remains insufficient to start another review. |
| V060-05 | Keep editable Word checklists and add complete plain-text prompts under replaceable System. Local Guidance and the reusable weekly-folder layout stay human maintained; existing installs review and merge the explicit model-neutral local-profile migration. |

## Approved package routing and weekly collection 0.6.1

| ID | Approved decision |
| --- | --- |
| V061-01 | System contains weekly operational materials only. First-time guides 01/14, setup prompts, administrative setup primer and validation reference are outside System in a separate First Time Setup folder supplied only in the first-time squadron package. Duplicate blank local-guidance seed forms are excluded from System. |
| V061-02 | Pantons and update START HERE enter weekly work using established local guidance. The first-time package has a distinct START HERE that routes to one-time guidance setup. No automatic restart or replacement of approved local guidance. |
| V061-03 | The reusable weekly folder includes Inputs/INPUT CHECKLIST.docx with required weekly products and optional or applicable extras. Use existing products and record missing items; missing inputs limit affected checks. A source-backed manual migration adds the list to existing templates without overwriting guidance, schedules or weekly records. |

## Approved simplification decisions 0.7.0

The product authority made these decisions in the 2026-10-12 planning session and the 2026-10-13 release decision; the DO approved the Squadron Rules wording on 2026-10-12. They take effect with package 0.7.0 and supersede the earlier records named below. The 0.7.0 kit carries no separate upload primer, so V041-02 and V060-01 are superseded in full.

| ID | Approved decision |
| --- | --- |
| V070-01 | Start a new GenAI.mil conversation for each task. A saved WEEK FILE carries the week's state between conversations: schedule versions, human decisions, findings, the regulation-check record, outlook and open items. A person picking up a week uses the week folder; no separate handoff procedure is needed. Supersedes V04-11 and V04-12 at release. |
| V070-02 | Use one self-contained, day-named task file per task. Each task file carries the shared core instructions, its own step-by-step script and the WEEK FILE format. It replaces the separate upload primer plus short activation prompts (supersedes V041-02 and V060-01). Every task file still includes "Do not delegate to subagents" (V060-02 unchanged). |
| V070-03 | Ship a Pantons kit only. First-time and other-squadron setup leaves the release downloads, with Git history retaining it; it returns as an add-on if another squadron asks. Supersedes V041-01, V061-01 and V061-02 at release. |
| V070-04 | The DO approved this Pantons profile wording on 2026-10-12. Tuesday: "schedulers start the week with the Tuesday task file and the current inputs." Conversation: "Start a new GenAI.mil conversation for each task with its task file, these Squadron Rules and the newest WEEK FILE. The WEEK FILE carries the week's decisions and state from one conversation to the next." Existing installs review and merge it through PERSIST-005. |
| V070-05 | Simplicity budget, recorded in AGENTS.md: every task uses the same 4 moves; at most 10 task files and about a dozen operator-visible files; plain English in everything operators see, with internal codes only in the WEEK FILE; one concrete next action per reply without hiding any material issue. Adding an operator step or file needs DO approval and should remove another. Supersedes V04-20 and V060-01 (one-page checklist per day). |
| V070-06 | Squadron Rules is one human-maintained file: the approved profile (Section 1), the local reference index (Section 2) and DO-approved lessons (Section 3). The former run-control, decision-record, execution-update and handoff forms become WEEK FILE sections. The DO and Flight Commander input forms are removed; those inputs arrive as the squadron's own emails or notes. V04-13 still holds: there is no duplicate transcription. Updates replace only TASK FILES and START HERE. |
| V070-07 | Release decision (2026-10-13): publish 0.7.0 after the build checks pass. Only the Tuesday task was smoke-tested in GenAI.mil; the other task files are released with their behavior trials recorded as Not run. The fictional practice data used for the Tuesday test is removed from the repository and every download (Git history retains it). |

These decisions change only the operator workflow and packaging. All authority, Buy/Sell, waiver, GAMECHANGER source-gate, evidence and local scheduling rules above remain in force.

## Approved reply layout 0.7.1

The repository owner requested this change on 2026-11-07, supplying task-file revisions drafted in GenAI.mil for the shared core, 3 THURSDAY - Full QC and 4 THURSDAY - Buy-Sell. It takes effect with package 0.7.1.

| ID | Approved decision |
| --- | --- |
| V071-01 | Replies present findings, issues and recommendations as a compact checklist table grouped by category, with columns # / Day / Time / Pilot / Event / Issue (1-line summary) / Quick Fix / Action Required, and avoid long narrative paragraphs. This replaces the numbered "Needs attention" list in core section 3 rule 4. Every material issue stays visible as its own row (V070-05 unchanged). Category headings give the plain meaning before the exact status, as core section 3 rule 2 requires. The Buy/Sell brief uses ultra-concise bullets and compact tables, ending in a numbered DO-decision table that keeps affected resources and states that waivers need the DO plus the applicable waiver authority. Full QC presents source problems, whole-schedule findings, regulation items and readiness results as compact tables. Only the reply layout changes; no check, authority, evidence or WEEK FILE rule changes. |

## Approved squadron-rule decisions 0.8.0

The product authority approved these on 2026-11-12: "yes, it should. DO authority overrides. We should flag things that seem blatantly against a regulation though. I like your way forward. Proceed." They take effect with package 0.8.0. The request behind them was to make the kit simpler for pilots who are not used to AI, and to make squadron rules that are known only through experience easy to write down and to edit by hand.

| ID | Approved decision |
| --- | --- |
| V080-01 | **A DO-approved squadron rule is its own kind of evidence.** A line in Squadron Rules Part 1 is enforced on the DO's authority, including where a regulation covers the same ground (who flies with whom, upgrade supervision, qualifications). It needs no GAMECHANGER support, and an unavailable connector never switches it off. It is reported as a squadron rule with its ID. It is never reported as a regulation result, never given a P-### outcome, never used as evidence of what a regulation says and never treated as a waiver. V04-21 and V04-22 are unchanged: regulation determinations still come only from GAMECHANGER. |
| V080-02 | **Flag a squadron rule that seems plainly against a regulation.** Regulation checks still run beside squadron rules. A squadron rule may be stricter than a regulation. When one seems plainly against a regulation, the assistant looks it up. If a retrieved publication disagrees, it shows both with the locator as RULE VS REGULATION for the DO. If nothing traceable is retrieved, it raises the concern only as a NOT VERIFIED question for a person and never states from memory what a regulation requires. It keeps applying the squadron rule as written; only the DO changes it. Waiver routing (V04-08) is unchanged. |
| V080-03 | **Squadron Rules is one rule per line by category.** Each rule has an ID (category code and number) and a strictness: Must, Ask the DO first, Prefer or Method. The strictness sets the finding type: HARD CONFLICT, APPROVAL NEEDED, OPTIMIZATION, or none for Method. The file has five parts: rules the assistant applies; proposals waiting for the DO; retired or rejected lines; local words and reference documents; ground rules for authority and the week. It ends with an end marker, and the first reply of every task says how many rules were read in each category. This supersedes the three-section layout in V070-06; the rest of V070-06 stands. |
| V080-04 | **Three ways a rule is written down, each ending in a DO approval and a human edit.** (1) The RULES task file asks questions one category at a time and hands back lines to paste. (2) A correction a human makes during a weekly task is applied to that concern that week as Human-confirmed and saved in the WEEK FILE as a proposed rule. (3) A person adds a line by hand. The assistant never suggests what a rule should say from its own knowledge, never applies a proposed or retired line and never edits Squadron Rules. Playbook governance (V04-14) is unchanged: stable candidate IDs, Pending/Approved/Rejected history, and no automatic promotion. |
| V080-05 | **A ninth task file, RULES - Add or change squadron rules.** The simplicity budget (V070-05) says a new operator-visible file should replace another. Nothing was removed; the product authority approved the addition after being told so. The cap of 10 task files stands and is now a unit test. |
| V080-06 | **Conversion without a policy change.** Every sentence of the earlier approved profile is kept word for word. The rule lines in Part 1 only split it up; the authority, battle-rhythm and evidence wording moved unchanged to Part 5. The change-form (AFIMT 2407) triggers and the steps after a signed schedule changes moved from task file 6 into Squadron Rules as PRI-08 and PRI-09, so a task file no longer carries squadron-specific forms or system names. Lines copied from the Scheduling SOP v4.0 that were never in Squadron Rules, and the two experience rules the product authority stated, are proposals in Part 2 and are not applied until the DO approves them. |

Routine implementation choices within these decisions:

- **Lines, not Word tables.** The proposal showed a table. The build has never produced Word tables (the package checker rejects them), and whether GenAI.mil reads Word tables reliably is untested, so each rule is one bulleted line. Adding a rule is copy, paste and retype.
- **Strictness labels on carried-over rules are the maintainer's reading of the existing words, for the DO to check when adopting the file.** A label was set to Must, Ask the DO first or Prefer only where the approved wording already said so: "hard conflict" or "never"/"cannot" is Must; "requires DO approval", "only with DO direction" and "waivable preference" are Ask the DO first, because the core already treats a waivable preference as APPROVAL NEEDED; "rotate", "fill" and "use useful" are Prefer. Everything else is Method, which leaves the assistant applying the words exactly as before. The [policy crosswalk](policy-crosswalk.md) lists every line.
- **Fourth strictness value.** The proposal named three. Most of the earlier profile says how to count or judge something, so those lines are labelled Method and create no finding by themselves.
- **Older Squadron Rules keep working.** An update replaces only the task files, so the core tells the assistant to apply an older-layout Squadron Rules as written and to say once that a newer layout exists.

Not decided or not done: the two Word continuity guides (Scheduling SOP v4.0 and the QC checklist) were not edited; they are the squadron's own dated documents and still describe the pre-0.7.0 working record. No GenAI.mil trial of 0.8.0 has been run.
