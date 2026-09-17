# Change log

## Unreleased — next-week inference and source integrity

- Default normal pre-execution weekly conversations to the next execution week unless a human selects another period, while execution reflows stay on the current published week and active handoffs/historical work preserve their recorded or explicit periods; infer dates, task/state and schedule roles from supplied evidence instead of requiring a startup run-control field list.
- Add assistant-drafted run control, consequential-assumption reporting and one-focused-question behavior for materially ambiguous weeks or versions.
- Add product statuses CURRENT, STALE, PARTIAL, CONFLICTED, INTEGRITY FAILED, UNREADABLE and SUPERSEDED, including a fail-closed identity/formula gate for calculated person-specific products.
- Standardize Wednesday's meeting as the Cross-Functional Schedule Integration Review and preserve Thursday as the formal Schedule Buy/Sell/DO buy.
- Add the artifact-responsibility map, Terra/Grok regulatory-question boundary, stronger P-ledger handoff continuity and validation cases for startup inference, integrity failure, stale/partial exports and affected-rule queries.
- Advance the local/development package marker to 0.5.6. This is a replaceable System update; Local Guidance and weekly work are unchanged and no persistent migration is required.

## Unreleased — GAMECHANGER publication-grounded QC

- Add DoW Policies Beta (GAMECHANGER) as the fail-closed publication-authority layer for publication-derived currency, qualification, crew-rest/duty, evaluation, syllabus/prerequisite, event-credit, recurring-training and similar regulatory determinations in the main Gemini workflow.
- Prohibit model memory, generic military knowledge, ordinary web search and uncited AI synthesis as fallback regulatory evidence. If a sufficiently traceable applicable publication is not retrieved, the affected check is CANNOT VERIFY; unresolved retrieved-source conflicts are SOURCE CONFLICT.
- Add a Weekly Publication Rule Ledger with stable P-### IDs. Tuesday planning creates the initial publication-rule/currency baseline; Thursday full QC re-queries GAMECHANGER against the complete near-final schedule; post-buy corrections and execution reflows perform delta checks for affected publication-driven facts.
- Carry publication-QC SOURCE-BACKED ISSUE, SOURCE CONFLICT and CANNOT VERIFY items into the Thursday Buy/Sell and Friday publication records without changing human approval, waiver or publication authority.
- Add operator prompts, architecture/report contracts, design decisions, crosswalk and validation cases for connector unavailability, insufficient citation, conflicting publications, Thursday refresh, execution delta checks and non-overclaiming of compliance.
- Preserve the core document-based scheduling workflow when GAMECHANGER is unavailable; unrelated scheduling analysis continues while publication-derived checks remain unverified.
- Advance the local/development package marker to 0.5.5. This is a replaceable System update; Local Guidance and weekly work are unchanged and no persistent migration is required.

## Unreleased — automatic patch release versioning

- Make the **Actions → Publish release** Version input optional. A blank value reads GitHub's latest published stable `vMAJOR.MINOR.PATCH` release and increments only the patch component by `0.0.1`.
- Keep explicit stable versions available for intentional major/minor/patch choices; malformed or prerelease values remain rejected by the normal workflow.
- Serialize all publication runs under one concurrency group so a blank auto-version run cannot race an explicitly entered version.
- Preserve safe retry behavior: a failed blank run resolves to the same next patch until that version successfully publishes; after publication the following blank run advances again.
- Advance the local/development package marker to 0.5.4. This maintainer automation change does not alter scheduling policy, authority, operator guides, Local Guidance or weekly-folder behavior.

## Unreleased — draft-first immutable release publishing

- Replace the publish-then-build release flow with one manual **Actions → Publish release** workflow. The maintainer enters a version number from the default branch; no manual tag or release publication is required.
- Validate the current default-branch commit, persistent-state declarations, two independent package builds, package/source coverage, byte reproducibility and regression tests before release publication.
- Generate structured release notes automatically from the maintained update note, standard install/update guidance, current-version migration declarations and GitHub-generated merged-PR/contributor notes.
- Create or resume only a matching mutable draft, upload and byte-verify all five release assets, write final notes/download links, and publish the draft only after final preflight. This is compatible with GitHub immutable releases.
- Make retries safe: failure before draft creation leaves no release; failure after draft creation leaves a resumable draft whose existing assets are verified before missing assets are added. Already-published releases and existing tags are never moved, repaired or overwritten.
- Add the release workflow itself to package-validation path triggers and update maintainer documentation/guardrails to the new one-action process.
- Bump the local/development package version to 0.5.3. This release-automation change does not alter scheduling policy, authority, operator guides, Local Guidance or weekly-folder behavior.

## Unreleased — day-based Word manual and Thursday buy/sell

- Reorganize the operator instructions around the actual workday instead of the internal phase name. The package now generates separate Word guides for Monday inputs, Tuesday startup, Tuesday planning, Wednesday build, Thursday full QC, optional DO adversarial review, Thursday schedule buy/sell, post-buy/sell implementation, Friday final QC/publication, execution reflows, active-week handoff, updates and setup checks.
- Correct the authority model: **the Thursday schedule buy/sell is the formal DO buy event when the DO explicitly approves the weekly schedule.** The exact presented version plus recorded DO directions forms the approved buy/sell baseline.
- Remove the routine second-buy concept. Schedulers implement buy/sell directions and Gemini checks implementation and downstream effects. A materially different solution outside the recorded direction returns to the DO for a supplemental decision; publication remains a separate human action.
- Keep the five internal phases underneath the chronological manual so holidays, delayed inputs and reopened work follow actual status rather than calendar date.
- Update START HERE, package generation/checks, primer, Pantons and generic local-profile seeds, phase/report references, decision record, synthetic walkthrough, validation plan, README, contributor instructions and migration metadata to the same workflow.
- Bump the local/development package version to 0.5.2 and append PERSIST-002 so existing Local Guidance is reviewed/merged rather than overwritten automatically.

## Unreleased — Pantons battle rhythm and model roles

- Make the operator flow match the actual battle rhythm: inputs due NLT COB Monday; Tuesday ingest/planning; Wednesday bulk schedule build; Thursday full scheduler/Gemini QC; optional DO adversarial review; Thursday buy/sell; post-buy/sell implementation/QC; Friday publication; execution-week reflows.
- Make Tuesday's first planning pass explicitly identify questions/gaps, checkrides/evaluations, directed DV or senior-leader flyers and each active upgrade's legal next events, windows and resource demand before the schedulers build the lineup.
- Split Wednesday build support from Thursday's deliberate full-schedule QC so intermediate drafting does not substitute for the final pre-buy/sell review.
- Use Gemini 3.7 Flash as the main GenAI.mil scheduler model when available while preserving human authority and workflow portability if the displayed model changes.
- Add an optional DO-only adversarial review using a separate GPT-5.6 Terra or Grok Expert 4.5 conversation. It is read-only, never an automatic scheduler dependency, and returns to the main Gemini workflow only through explicit DO-accepted human direction.
- Preserve status-based phase control underneath the day labels so holidays, delayed inputs, reopened drafts and late corrections do not automatically create approval or publication.

## Unreleased — adversarial-review hardening

- Add a read-only hosted operator-package CI gate that validates persistent-state declarations, builds/checks all three ZIPs and runs package/release regression tests before package-affecting changes merge.
- Register persistent installed artifacts and the reusable weekly-folder layout in an append-only migration declaration. Future persistent changes require a package-version bump plus explicit human migration instructions instead of silently diverging fresh and existing installs.
- Expand Markdown-to-Word source coverage across START HERE, every numbered guide, every blank form/reference, both local-profile seeds, the startup primer and update/migration instructions; verify meaningful table row content and full copy/paste prompts.
- Reconcile the current repository QC record with the successful hosted v0.4.1 asset/upload/release-note run while preserving the tagged v0.4.1 QC record as historical evidence.
- Distinguish structured human release summaries from GitHub-generated change notes. The generated download block no longer implies human validation exists when the required summary headings are absent.
- Add a tagged reproducibility contract for future releases: exact CPython 3.12.14, dependency-file hash, stored ZIP members, double-build byte comparison, and a frozen v0.4.1 legacy dependency path. Existing differing assets remain immutable by policy.
- Clarify that a normal new execution-week chat does not need a handoff; handoff-first wording now applies only when an already-started week's recorded state moves to a replacement chat/user.
- Replace the believable September 2026 reproducibility timestamps with the documented neutral 1980 ZIP-epoch sentinel and make the package number in generated document headers the authoritative installed-version signal.
- Add a prior-release System rollback procedure and package simulation. Rollback restores only System/START HERE and preserves local guidance, playbook, weekly schedules/records, approvals and human-approved persistent migrations.

## Unreleased — release automation

- Fixed GitHub rejection of runner-only contexts in job-level environment values. Initialize temporary paths inside a runner step and validate workflow definitions with actionlint on PRs.
- Build and check all three ZIPs when a release is published; support manual backfill of an existing release. Build the tagged source and require a matching package version.
- Store downloads as release assets and point README to the latest release; remove committed ZIPs and manifest. No repository archive folders or branch writeback.
- Add categorized GitHub release notes, a human summary template, verified download links and checksums. Existing human notes are preserved; differing release assets cannot be silently replaced.
- Make the update change note a maintained source file. Scheduling behavior and Word contents remain unchanged in this infrastructure follow-up.

## v0.4.1 — Word downloads and simple updates

- Added dedicated Pantons and first-time squadron ZIPs, short START HERE, uploadable primer, numbered Word guides, Word forms and reusable weekly folders.
- Added one manual update ZIP that replaces System next week while preserving local guidance and weekly work.
- Made README downloads-first. Maintained sources and a reproducible build utility accompany current packages.
- Removed current-tree v0.3 archive at the product authority’s direction; earlier PRs and Git history retain provenance. External originals are untouched.
- Word-compatible reports/handoffs replace Markdown as an operator requirement. No scheduling rules changed. ChatGPT Mil ingestion and model behavior remain untested.

## v0.4 documentation follow-up — first-time squadron setup

- Added a shared-drive folder recommendation, explicit GitHub copy/local-create mapping, existing-product inventory and first-time planning Q&A prompt.
- Added a blank local-profile starter for adopting squadrons; no Pantons policy values are prefilled.
- Documented setup draft generation, human confirmation/approval, current-file indexing, first-week transition and configuration updates. Setup is administrative work, not a sixth operational phase or platform feature.
- Linked the guide from README and architecture; added unrun setup-specific validation cases. Operational scheduling policy and original archives are unchanged.

## v0.4 — approved design implemented, operational validation pending

- Reorganized the system around product gathering, initial draft, sell, corrections/QC/approval/publication and execution reflows. Phase transitions follow work status, not weekday.
- Retained scheduler-built initial lineups; expanded explicit pre-draft consolidation and planning Q&A. Drafting starts at scheduler discretion despite documented gaps.
- Defined sell direction → human correction → assistant QC → formal DO buy → human publication. This historical v0.4 authority sequence is superseded by current design decision V04-19, which places formal DO buy in the Thursday buy/sell.
- Defined daily scheduler/Top 3 scope and return-to-DO boundaries. Every waiver goes through the DO and applicable authority.
- Defined immediate execution deltas against each day's signed daily schedule or weekly fallback, and cumulative deltas against published weekly.
- Accepted scoped human confirmation as concern closure without documentary proof demands, labeled distinctly from model verification.
- Added live execution update, decision/release record and concise handoff. Source products accompany handoffs; shared chat/export/memory are not assumed.
- Separated reusable workflow from the Pantons local rule profile. Preserved original event accounting, availability/qualification/spare/same-day/priority/forecast/backup rules.
- Corrected v0.3's target-week-actuals restriction for legitimate live execution and cutoff-valid historical reflows; preserved isolated restart after hindsight contamination.
- Updated input forms to reference existing products rather than require duplicate transcription. Preserved independent playbook governance and stable candidate IDs.
- Added a novice operator README with paste-ready prompts, expected input lists and phase exit instructions, synthetic examples, crosswalk and practical validation cases.
- Original v0.3 DOCX and starter ZIP remain unchanged outside the repository. Earlier Git history retains provenance.

## Source baselines

- Pantons F-16 Scheduling Analysis System v0.3: approved scheduling baseline.
- Pantons Scheduling Starter Kit v0.1: companion inputs, examples and GitHub guidance.
- v0.4 planning conversation: explicit DO-approved workflow decisions, consolidated in `docs/v0.4/design-decisions.md`.
