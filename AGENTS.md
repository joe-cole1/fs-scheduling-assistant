# Repository instructions for AI contributors

These instructions apply throughout `fs-scheduling-assistant`. Read this file at the start of work and check for any more-specific `AGENTS.md` in directories you change. This is repository-development guidance; operational users load the system primer and approved local profile in GenAI.mil. Do not assume a new chat automatically has this repository, prior chats, or uploaded source files.

## Purpose and working relationship

This is a Word-facing, human-led fighter-squadron scheduling analysis package. The squadron DO is the product authority. Act as a planning, design, implementation and QC partner. The core operational workflow must work through document uploads and conversation in GenAI.mil without APIs, custom software, autonomous agents, shared chats or any particular model as prerequisites. Platform connectors may add explicitly bounded capabilities. In particular, publication-grounded regulatory QC may use the DoW Policies Beta (GAMECHANGER) connector; if it is unavailable, the rest of scheduling continues while those checks fail closed as CANNOT VERIFY.

- For an unresolved substantive product/policy decision, explain why it matters, recommend an answer with relevant tradeoffs, ask exactly one question, and wait.
- Once the user approves a design or requests implementation, carry out the authorized work. Resolve routine implementation details without repeated permission.
- Preserve approved decisions. Do not reopen scheduling policy without a specific conflict or new evidence. Distinguish approved rules, proposals, examples and unknowns.
- Do not import model preferences or delegation arrangements from unrelated repositories.

## Start from the actual repository state

1. Read [README.md](README.md), [ARCHITECTURE.md](ARCHITECTURE.md), [approved design decisions](docs/v0.4/design-decisions.md), [policy crosswalk](docs/v0.4/policy-crosswalk.md) and [data handling](docs/data-handling.md).
2. For behavior changes, read the affected sections of [the primer](docs/v0.4/system-primer.md), [Pantons local profile](local-profiles/pantons-v0.4.md), [phase reference](docs/v0.4/phase-guide.md), and relevant templates/reports/examples before editing.
3. Check branch, remote state and relevant PR status. Preserve unrelated user edits.
4. Use the narrowest change that fully satisfies the request. Read historical sources when exact policy wording matters; do not reconstruct them from memory.

## Authority and policy preservation

This file is a maintenance guardrail, not a second source of scheduling policy. Exact scheduling rules belong in the approved local profile and references; approved workflow changes are recorded in design decisions.

Preserve these contracts:

- **Humans schedule and approve.** Schedulers create the initial lineup. The assistant consolidates inputs, answers planning questions, reviews drafts, recommends changes and performs QC. It never autonomously modifies operational source files, coordinates, publishes, grants waivers or promotes playbook lessons.
- **Five internal phases, selected by work status:** product gathering; initial draft; schedule buy/sell; post-buy/sell implementation/final QC/publication; execution reflows. The operator manual is day-based, but weekdays do not automatically change phase.
- **Thursday buy/sell is the formal DO buy.** Only an explicit DO approval creates the buy. The approved baseline is the exact presented schedule plus recorded DO directions. Schedulers then implement those directions and the assistant verifies implementation and downstream effects. There is **no routine second DO buy**. If implementation requires a materially different solution outside the recorded direction, return that specific issue to the DO for a supplemental decision. Publication remains a separate human action.
- **Publication-derived regulatory findings are connector-gated.** Currency, qualification, crew-rest/duty, evaluation, syllabus/prerequisite, event-credit, recurring-training and other publication-based regulatory determinations must be grounded in a sufficiently traceable DoW Policies Beta (GAMECHANGER) publication retrieved by the main workflow. Do not use model memory, generic military knowledge, ordinary web search or uncited AI synthesis as fallback regulatory evidence. If the connector/source is insufficient, use CANNOT VERIFY; if retrieved authorities conflict, use SOURCE CONFLICT. GAMECHANGER evidence never grants approval or a waiver.
- **Weekly publication-rule state is explicit.** Preserve stable P-### entries with applicability, requirement, publication identity, current/effective status when available, paragraph/page/locator, retrieval time and QC outcome. Tuesday creates the initial ledger, Thursday refreshes it against the complete schedule, and post-buy/reflow changes trigger affected-rule delta queries. A transferred ledger is continuity evidence, not permission to bypass a required connector query.
- **Human confirmation closes the stated concern.** Record it as human-confirmed, not independently verified, without demanding another upload or proof. Do not broaden its scope. Human confirmation does not convert missing connector evidence into SOURCE-BACKED OK.
- **Every waiver goes through the DO and the applicable waiver authority.** Generic confirmation, buy/sell approval and publication do not silently grant waivers.
- **Daily authority stays bounded.** Feasible personnel/mission changes within published times, turn pattern, coordinated support and explicit DO guidance use daily scheduler and Top 3 sign-off. Changes outside those boundaries return to the DO.
- **Version roles stay explicit.** Preserve the Thursday presented version and buy/sell decision record; reconcile the final published version to that approved baseline. Execution immediate comparison uses each affected day's latest signed daily schedule, falling back to published weekly; cumulative comparison uses the published weekly schedule.
- **Keep original scheduling safeguards.** Preserve conservative availability, qualification verification, protected spares, event accounting, applicable same-day rules, complete cascade checks, phase-appropriate churn, 30-day outlook and weekly moderate downside analysis. Never invent crew-rest, duty, weather, syllabus, qualification or future-capacity limits.
- **Facts remain traceable.** Maintain normalized facts and source locations; distinguish facts, interpretations and recommendations. Missing products limit affected checks, not all planning. Schedulers decide when drafting starts.
- **Actuals and blind tests are different.** Live execution results and historical actuals knowable by the declared cutoff are legitimate. Disallowed hindsight in a blind test requires a clean isolated restart. Historical publication checks must not silently apply a later policy version to an earlier cutoff.
- **Playbook governance persists.** Preserve stable candidate IDs and Pending/Approved/Rejected history. No automatic lesson promotion.

Do not keep historical archives in the current repository tree or download packages. Use Git history, prior PRs and Releases for provenance. Preserve external original source files.

## Write for a pilot new to scheduling

The README is the download entry point; START HERE.docx and numbered Word guides are the operator instructions. The manual is chronological by day/step so a scheduler can open the document for the task being performed.

- Maintain separate Word guides for Monday inputs, Tuesday start, Tuesday planning, Wednesday build, Thursday full QC, optional DO adversarial review, Thursday buy/sell, post-buy/sell implementation, Friday final QC/publication, execution reflows, active-week handoff, updates and setup check.
- State what to do, which existing products to upload, what may be missing, the exact prompt to paste, expected output and next step.
- Keep copy/paste prompts executable after replacing marked placeholders. Define terms such as active schedule, comparison baseline, buy/sell baseline and publication in plain language.
- Explain GAMECHANGER setup and the fail-closed source rule in the Tuesday/Thursday/reflow guides without making schedulers memorize policy values.
- Keep setup, buy/sell authority, implementation/QC, publication, reflow and handoff instructions consistent with the primer.
- Use standard squadron products as inputs. Forms capture missing guidance/changes; do not require users to transcribe information already supplied elsewhere.
- Keep reusable workflow separate from Pantons-specific policy.
- Preserve concise Word-compatible handoffs plus actual source products. Do not assume native export, shared multiuser chat, cross-chat memory or access to another user's uploads.

## Repository and GitHub practices

- Prefer the existing authenticated GitHub connection. Inspect tool results; never invent a successful commit, push, PR or merge.
- Work on a scoped branch and prepare a reviewable PR. Do not merge, change visibility or make a public release without user authorization.
- Inspect the diff before sending changes. Do not force-push, delete unrelated files, rewrite history or alter repository settings as incidental cleanup.
- Keep real operational products, personnel data, generated operational reports and real handoffs outside the repository. Examples must be unmistakably synthetic.
- Do not add dependencies, automation or generated binaries merely to make documentation appear more complete.

## Validate proportionately and report honestly

For behavior changes, inspect the affected contracts across operator guide prompts, primer, local profile, forms, report instructions and examples. Update the relevant design record, crosswalk, change log and validation cases. Routine editorial changes do not require rewriting everything.

Check links, table structure, fenced prompts, filenames, version labels and synthetic-example labeling. Persistent installed-state changes require a package-version bump and append-only migration declaration. Verify remote file/blob hashes after connector writes where relevant.

Use [the validation plan](docs/v0.4/validation-plan.md) for meaningful behavior checks. Publication-grounded behavior must include negative cases proving no model-memory/web fallback, connector-unavailable behavior, source conflicts and changed-schedule delta checks. Distinguish static document/package checks from actual model/connector runs, historical adjudication and operational validation. Cases not run stay **Not run**.

PR descriptions and final responses should explain what changed, why, what was checked and material limitations. Do not claim operational readiness, connector reliability or model reliability without evidence and human decisions.

## Word packages and updates

Maintain guide sources in `packaging/guides` and generate release ZIPs with `scripts/build_packages.py`. Read `packaging/README.md` before changing the build. Keep generated ZIPs/manifests out of the repository tree. GitHub Releases hold the full packages/update; README points to the latest published release. Do not hand-edit generated ZIP contents.

Updates replace **System** and **START HERE** only and are normally adopted next week. Never overwrite Local Guidance or weekly work automatically. If persistent local seeds change, append a migration record and provide reference-only copies for human review/merge. Actual GenAI.mil behavior requires separate testing.

The authorized release path is **Actions → Publish release** from the default branch. The Version input is optional: blank means increment the latest published stable release by `0.0.1`; an explicit stable version overrides automatic selection. All publish runs are serialized to prevent version races. The workflow validates/builds/tests before release creation, generates the notes, creates or resumes only a matching mutable draft, verifies all release assets, then publishes the draft as the final action. Do not manually create/publish the normal release, move an existing tag, overwrite differing assets, or attempt to repair an already-published immutable release. A failed matching draft may be resumed by rerunning the same resolved version; for an auto-selected patch, leaving Version blank again resolves to that same patch until it publishes.