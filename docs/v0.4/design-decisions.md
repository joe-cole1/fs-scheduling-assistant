# Approved design decisions — v0.4

Authority: explicit DO/product-authority decisions in the v0.4 planning conversation. This document records product design, not a weekly operational approval. No person or real schedule is approved by these entries.

| ID | Approved decision |
| --- | --- |
| V04-01 | Use five phase-based operational controls; retain legacy modes only as behavior/migration references. Status, not weekday, controls transitions. |
| V04-02 | Schedulers create the initial lineup. Before that, the assistant consolidates inputs, flags missing/conflicting information and answers evidence-backed planning questions. |
| V04-03 | Schedulers decide when drafting starts. Missing DO priorities, currencies or other products are flagged with consequences rather than imposing a complete-packet gate. |
| V04-04 | The sell meeting records DO direction. Schedulers incorporate changes, assistant checks implementation and second/third-order effects, then DO formally buys the corrected schedule. Publication follows. This supersedes the earlier discussion's shorthand that equated the sell meeting with buy. |
| V04-05 | Apply FINAL QC behavior immediately after sell directions are established. Preserve hard-conflict/major-risk correction and show substantial additional churn as a DO option. |
| V04-06 | Formal buy approves the exact authoritative weekly schedule. Humans distribute it to Wing, OG, Maintenance and other recipients. Significant departures after publication are controlled. |
| V04-07 | Daily scheduler and Top 3 sign off on feasible personnel/mission changes within published times, aircraft turn pattern, coordinated support and explicit DO guidance. Changes outside those boundaries return to the DO. |
| V04-08 | Every waiver must go through the DO and the applicable waiver authority. Neither buy nor generic confirmation implicitly approves every waiver. |
| V04-09 | Execution immediate comparison uses the latest signed daily schedule for the affected day, or published weekly schedule if no daily exists. Cumulative comparison uses the published weekly schedule. Preserve bought and published versions and explain any difference. |
| V04-10 | Explicit human confirmation is sufficient to close the identified QC concern without mandatory supporting uploads or further proof. Record it as human-confirmed, not independently checked; retain waiver requirements. |
| V04-11 | Prefer one conversation per execution week spanning all phases. Target ChatGPT Mil without relying on multiuser shared-chat support, native export or automatic memory. |
| V04-12 | Use a concise current-state Markdown handoff plus actual applicable source products when changing users/conversations. Retain full transcripts separately when needed. |
| V04-13 | Use existing standard products; placeholder forms capture missing guidance, changes and recommendations. Draft missing guidance for human confirmation without inventing facts or authority. |
| V04-14 | Preserve v0.3 scheduling rules, advisory authority, evidence/normalization, availability/qualification checks, spares, accounting, local same-day rules, and stable playbook decisions. |
| V04-15 | Historical blind condition stays separate from phase. Use cutoff-valid evidence only. Hindsight contamination requires an isolated clean restart; legitimate live execution actuals are allowed. |
| V04-16 | Repository products must be usable by a pilot new to scheduling. README includes step-by-step actions, expected inputs and copy/paste phase prompts. |

## Routine implementation choices within the approved design

- Separate reusable primer from the Pantons local profile; both are loaded for Pantons operations. Another squadron supplies its own approved profile.
- Use one weekly decision/release record instead of recopying sell, waiver and approval entries across forms.
- Use stable fact, event, recommendation, decision and candidate references; their numbering is document bookkeeping, not a new authority requirement.
- Add a live execution update form distinct from historical retrospective outcomes.
- Map immediate baselines per affected date for multi-day reflows. Ask about a republished weekly baseline rather than silently resetting history.
- Retain current moderate downside analysis and reassess on material changes rather than run a fresh scenario for every chat message.

## Not assumed or changed

No platform collaboration/export feature is asserted. No API/custom software/agent prerequisite. No public release or repository merge is implied by creation of the review branch. No new numerical duty, rest, weather or syllabus limits. No mandatory documentary proof to accept a scoped human confirmation. No assistant source-file modification or lesson promotion.

## Approved beginner packaging decisions — v0.4.1

| ID | Approved decision |
| --- | --- |
| V041-01 | Two complete downloads: dedicated Pantons and first-time other-squadron setup. |
| V041-02 | Short START HERE plus separate numbered Word guides in Instructions; upload the startup primer and use short activation/phase prompts. |
| V041-03 | Permanent extracted folder with a ready-made weekly folder to copy. Keep local guidance and weekly work outside replaceable System. |
| V041-04 | Manual numbered updates adopted next week. No elaborate weekly system copies or automatic update mechanism. |
| V041-05 | Remove repository archives, including v0.3. Use branches, prior PRs and Git history instead. This supersedes archive retention instructions; original uploaded files are unchanged. |

V041-02 supersedes the Markdown-only presentation in V04-12 and V04-16; handoff content and actual-source transfer remain unchanged. v0.4.1 is a packaging release, not a scheduling-policy revision.
