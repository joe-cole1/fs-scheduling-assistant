# Repository instructions for AI contributors

These instructions apply throughout `fs-scheduling-assistant`. Read this file at the start of work and check for any more-specific `AGENTS.md` in directories you change. This is repository-development guidance. Operators use the built kit in GenAI.mil. Do not assume a new chat automatically has this repository, prior chats, or uploaded source files.

## Purpose and working relationship

This is a human-led fighter-squadron scheduling analysis kit for the Pantons (35 FS). The squadron DO is the product authority. Act as a planning, design, implementation and QC partner. The operational workflow must work through file uploads and conversation in GenAI.mil, without APIs, custom software, autonomous agents, shared chats or any particular model as prerequisites. Platform connectors may add explicitly bounded capabilities. In particular, publication-grounded regulatory QC uses the DoW Policies Beta (GAMECHANGER) connector. If it is unavailable, the rest of scheduling continues while those checks fail closed as CANNOT VERIFY.

- For an unresolved substantive product or policy decision, explain why it matters, recommend an answer with relevant tradeoffs, ask exactly one question, and wait.
- Once the user approves a design or requests implementation, carry out the authorized work. Resolve routine implementation details without repeated permission.
- Preserve approved decisions. Do not reopen scheduling policy without a specific conflict or new evidence. Distinguish approved rules, proposals, examples and unknowns.
- Do not import model preferences or delegation arrangements from unrelated repositories.

## Start from the actual repository state

1. Read [README.md](README.md), [ARCHITECTURE.md](ARCHITECTURE.md), [approved design decisions](docs/design-decisions.md), [policy crosswalk](docs/policy-crosswalk.md) and [data handling](docs/data-handling.md).
2. For behavior changes, read the affected parts of [the shared task-file core](packaging/kit/core.md), [the task scripts](packaging/kit/tasks), [the WEEK FILE format](packaging/kit/week-file.md) and [the Pantons local profile](local-profiles/pantons.md) before editing.
3. Check branch, remote state and relevant PR status. Preserve unrelated user edits.
4. Use the narrowest change that fully satisfies the request. Read historical sources when exact policy wording matters; do not reconstruct them from memory.

## Authority and policy preservation

This file is a maintenance guardrail, not a second source of scheduling policy. Exact scheduling rules belong in the approved local profile and references; approved workflow changes are recorded in design decisions.

Preserve these contracts:

- **Humans schedule and approve.** Schedulers create the initial lineup. The assistant consolidates inputs, answers planning questions, reviews drafts, recommends changes and performs QC. It never autonomously modifies operational source files, coordinates, publishes, grants waivers or promotes playbook lessons.
- **Five internal phases, selected by work status:** product gathering; initial draft; schedule buy/sell; post-buy/sell implementation/final QC/publication; execution reflows. Task files are named by day, but weekdays do not automatically change phase.
- **Thursday buy/sell is the formal DO buy.** Only an explicit DO approval creates the buy. The approved baseline is the exact presented schedule plus recorded DO directions. Schedulers then implement those directions and the assistant verifies implementation and downstream effects. There is **no routine second DO buy**. If implementation requires a materially different solution outside the recorded direction, return that specific issue to the DO for a supplemental decision. Publication remains a separate human action.
- **Publication-derived regulatory findings are connector-gated.** Currency, qualification, crew-rest/duty, evaluation, syllabus/prerequisite, event-credit, recurring-training and other publication-based regulatory determinations must be grounded in a sufficiently traceable DoW Policies Beta (GAMECHANGER) publication retrieved by the main workflow. Do not use model memory, generic military knowledge, ordinary web search or uncited AI synthesis as fallback regulatory evidence. If the connector/source is insufficient, use CANNOT VERIFY; if retrieved authorities conflict, use SOURCE CONFLICT. GAMECHANGER evidence never grants approval or a waiver.
- **Weekly publication-rule state is explicit.** Preserve stable P-### entries with applicability, requirement, publication identity, current/effective status when available, paragraph/page/locator, retrieval time and QC outcome. Tuesday creates the initial ledger, Thursday refreshes it against the complete schedule, and post-buy/reflow changes trigger affected-rule delta queries. A ledger carried in the WEEK FILE is continuity evidence, not permission to bypass a required connector query.
- **Human confirmation closes the stated concern.** Record it as human-confirmed, not independently verified, without demanding another upload or proof. Do not broaden its scope. Human confirmation does not convert missing connector evidence into SOURCE-BACKED OK.
- **Every waiver goes through the DO and the applicable waiver authority.** Generic confirmation, buy/sell approval and publication do not silently grant waivers.
- **Daily authority stays bounded.** Feasible personnel/mission changes within published times, turn pattern, coordinated support and explicit DO guidance use daily scheduler and Top 3 sign-off. Changes outside those boundaries return to the DO.
- **Version roles stay explicit.** Preserve the Thursday presented version and buy/sell decision record; reconcile the final published version to that approved baseline. Execution immediate comparison uses each affected day's latest signed daily schedule, falling back to published weekly; cumulative comparison uses the published weekly schedule.
- **Keep original scheduling safeguards.** Preserve conservative availability, qualification verification, protected spares, event accounting, applicable same-day rules, complete cascade checks, phase-appropriate churn, 30-day outlook and weekly moderate downside analysis. Never invent crew-rest, duty, weather, syllabus, qualification or future-capacity limits.
- **Facts remain traceable.** Maintain normalized facts and source locations; distinguish facts, interpretations and recommendations. Missing products limit affected checks, not all planning. Schedulers decide when drafting starts.
- **Actuals and blind tests are different.** Live execution results and historical actuals knowable by the declared cutoff are legitimate. Disallowed hindsight in a blind test requires a clean isolated restart. Historical publication checks must not silently apply a later policy version to an earlier cutoff.
- **Playbook governance persists.** Preserve stable candidate IDs and Pending/Approved/Rejected history. No automatic lesson promotion.

Do not keep historical archives in the current repository tree or download packages. Use Git history, prior PRs and Releases for provenance. Preserve external original source files.

## Operator experience and the simplicity budget

The operators are schedulers who may be new to scheduling and to AI. Simplicity is a requirement, not a polish step. Every change must respect this budget unless the DO explicitly approves an exception, recorded in the design decisions:

- **The same 4 moves for every task.**
  1. Open a new GenAI.mil chat and turn on DoW Policies (GAMECHANGER).
  2. Drag in the task file, Squadron Rules and the newest WEEK FILE.
  3. Do what the assistant says.
  4. Save the new WEEK FILE.

  The assistant asks for any other files it needs. Never add a separate upload primer, activation prompt, startup form or handoff procedure.
- **New chat per task.** The WEEK FILE carries the week's state between chats. Anyone who takes over a week needs only the week folder.
- **About a dozen operator-visible files.** START HERE, at most 10 task files, Squadron Rules, and the weekly folder template with its input checklist. Adding an operator-visible file or step needs DO approval and should remove another.
- **Self-contained task files.** Each task file is built from `packaging/kit/core.md`, its task script and `packaging/kit/week-file.md`. It must:
  - start with the exact instruction **Do not delegate to subagents**
  - end with `=== END OF TASK FILE ===`
  - be plain ASCII and no larger than the build's size budget
  - name no model
- **No delegation.** The assistant performs the analysis itself in the current conversation, and no specific model is required. Do not add automatic agent or model offloading.
- **Plain English in everything the operator sees.** START HERE, the input checklist and the assistant's conversation avoid internal codes such as P-###, "ledger", "baseline" and phase names. Codes and exact statuses live in the WEEK FILE. When the assistant reports a formal status, it gives the plain meaning first and the exact status in brackets.
- **One concrete next action.** Every assistant reply ends with one physical next step and the exact short reply to type. Every material issue still stays visible, and a short reply never narrows a required check.
- **Use the squadron's existing products.** Never make operators retype trackers or fill in run-control forms. Missing inputs limit only the affected checks.
- **Keep the separation.** Reusable workflow lives in the task files; Pantons-specific policy lives in Squadron Rules (the profile). Squadron Rules and weekly work are human-maintained and are never overwritten by an update.
- **Test behavior with a fictional packet before relying on it.** Build a clearly fictional packet for the trial and keep real operational material out of the repository.

## Repository and GitHub practices

- Prefer the existing authenticated GitHub connection. Inspect tool results; never invent a successful commit, push, PR or merge.
- Work on a scoped branch and prepare a reviewable PR. Do not merge, change visibility or make a public release without user authorization.
- Inspect the diff before sending changes. Do not force-push, delete unrelated files, rewrite history or alter repository settings as incidental cleanup.
- Keep real operational products, personnel data, generated operational reports and real handoffs outside the repository. Examples must be unmistakably synthetic.
- Do not add dependencies, automation or generated binaries merely to make documentation appear more complete.

## Validate proportionately and report honestly

For behavior changes, inspect the affected contracts across the core, task scripts, WEEK FILE format, Squadron Rules and the contract-coverage test (`tests/test_contract_coverage.py`). Update the design decisions, crosswalk, change log and validation cases. A new non-negotiable rule needs a phrase in the contract-coverage test. Routine editorial changes do not require rewriting everything.

Check links, filenames, version labels and the size budget. Persistent installed-state changes require a package-version bump and an append-only migration declaration. Verify remote file and blob hashes after connector writes where relevant.

Use [the validation plan](docs/validation-plan.md) for meaningful behavior checks. Publication-grounded behavior must include negative cases proving:

- no fallback to model memory or the web
- correct behavior when the connector is unavailable
- source conflicts are reported
- changed-schedule delta checks run

Keep these kinds of evidence separate: static package checks, actual model and connector runs, historical adjudication, and operational validation. Cases not run stay **Not run**.

PR descriptions and final responses should explain what changed, why, what was checked, and material limitations. Do not claim operational readiness, connector reliability or model reliability without evidence and human decisions.

## Packages and updates

Maintain kit sources in `packaging/kit` and the profile in `local-profiles/pantons.md`. Generate release ZIPs with `scripts/build_packages.py`. Read `packaging/README.md` before changing the build. Keep generated ZIPs and manifests out of the repository tree. GitHub Releases hold `Panton_Scheduling_Assistant.zip` (the full kit) and `Update.zip`; README points to the latest published release. Do not hand-edit generated ZIP contents.

`Update.zip` holds only replaceable files: TASK FILES and START HERE. Operators delete TASK FILES and copy the update in, normally at a week boundary. Never overwrite Squadron Rules or weekly work automatically. If Squadron Rules, the input checklist or the weekly folder layout changes:

- append a migration record
- let the update carry a read-me with reference copies for human review and merge

Actual GenAI.mil behavior requires separate testing.

The authorized release path is **Actions → Publish release** from the default branch. `packaging/version.txt` is the reviewed stable release identity. Normally leave the workflow Version field blank so the workflow uses that source version; an entered Version is only a confirmation and must match exactly. All publish runs are serialized.

The workflow:
1. validates, builds and tests before creating the release
2. generates notes
3. creates or resumes only a matching mutable draft
4. safely retries and reconciles transient asset-upload failures
5. verifies all release assets
6. publishes the draft as the final action

Do not:
- manually create or publish the normal release
- move an existing tag
- overwrite differing completed assets
- try to repair an already-published immutable release

A failed matching draft may be resumed by rerunning the same source version.
