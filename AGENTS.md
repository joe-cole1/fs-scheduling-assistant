# Repository instructions for AI contributors

These instructions apply throughout `fs-scheduling-assistant`. Read this file at the start of work and check for any more-specific `AGENTS.md` in the directories you change. This is repository-development guidance; operational users load the system primer and approved local profile in ChatGPT Mil. Do not assume a new chat automatically has this repository, prior chats, or uploaded source files.

## Purpose and working relationship

This is a Markdown-first, human-led fighter-squadron scheduling analysis package. The squadron DO is the product authority. Act as a planning, design, implementation and quality-control partner. The first operational workflow must work through document uploads and conversation in ChatGPT Mil, without APIs, custom software, connectors, autonomous agents, shared chats or any particular model as prerequisites.

- For an unresolved substantive product/policy decision, explain why it matters, recommend an answer with relevant tradeoffs, ask exactly one question in ordinary chat, and wait.
- Once the user approves a design or requests implementation, carry out the authorized work. Resolve routine formatting and implementation details yourself; do not ask for repeated permission.
- Preserve approved decisions. Do not reopen scheduling policy without a specific conflict or new evidence. Clearly distinguish approved rules, proposals, examples and unknowns.
- Do not import model preferences, delegation arrangements or workflows from unrelated repositories. Do not introduce subagents unless the user explicitly requests them.

## Start every task from the actual repository state

1. Read [README.md](README.md), [ARCHITECTURE.md](ARCHITECTURE.md), [the approved design decisions](docs/v0.4/design-decisions.md), [the policy crosswalk](docs/v0.4/policy-crosswalk.md) and [data handling](docs/data-handling.md).
2. For behavior changes, read the affected sections of [the primer](docs/v0.4/system-primer.md), [Pantons local profile](local-profiles/pantons-v0.4.md), [phase guide](docs/v0.4/phase-guide.md), and relevant templates, reports and examples before editing.
3. Check the current branch, working changes, remote state and relevant PR status. Do not assume a PR from a previous chat is still open or that its branch is the current baseline. Preserve unrelated user edits.
4. Identify the requested outcome and affected documents. Use the narrowest change that fully satisfies the request. Read historical sources when exact policy wording matters; do not reconstruct them from memory.

These links describe the v0.4 layout. If a later release changes the layout, follow its documented migration and update these instructions rather than guessing at missing files. Report unreadable or unavailable required sources and continue unaffected work.

## Authority and policy preservation

This file is a maintenance guardrail, not a second source of scheduling policy. Exact scheduling rules belong in the approved local profile and references; explicit approved workflow changes are recorded in the design decisions. Historical material and synthetic examples cannot override them. A newly requested policy change is a proposal until the DO explicitly approves it; record approved changes and their scope rather than silently changing the baseline.

Preserve these essential contracts across every edit:

- **Humans schedule and approve.** Schedulers create the initial lineup. The assistant consolidates inputs, answers planning questions, reviews drafts, recommends exact changes and performs QC. It never autonomously modifies operational source files, coordinates, publishes, grants waivers or promotes playbook lessons. This restriction does not prohibit authorized edits to this repository's reusable documents and forms.
- **Five phases, selected by work status:** product gathering; initial draft; sell; corrections/final QC/approval/publication; execution reflows. Weekdays do not automatically change phase. Legacy modes remain behavior/migration references, not a second required operational control.
- **Sell is not buy.** Sell directions → scheduler corrections → assistant QC of mistakes and second/third-order effects → formal DO buy of the exact corrected version → human publication. FINAL QC limits begin after sell directions are established.
- **Human confirmation closes the stated concern.** Do not demand another upload or documentary proof when a human explicitly says an identified issue is okay. Record it as human-confirmed, not independently verified, and do not broaden its scope.
- **Every waiver goes through the DO and the applicable waiver authority.** Generic confirmation, formal buy and publication do not silently grant waivers.
- **Daily authority stays bounded.** Feasible personnel/mission changes within published times, turn pattern, coordinated support and explicit DO guidance use daily scheduler and Top 3 sign-off. Changes outside those boundaries return to the DO.
- **Version roles stay explicit.** Execution immediate comparison uses each affected day's latest signed daily schedule, falling back to the published weekly schedule. Cumulative comparison uses the identified published weekly schedule. Preserve bought/published identities and explain differences. Never silently select among competing versions or adopt an unsigned proposal as a signed baseline.
- **Keep original scheduling safeguards.** Preserve conservative availability, qualification verification, protected spares, event accounting, applicable same-day rules, complete cascade checks, phase-appropriate churn, the 30-day outlook and weekly moderate downside analysis. Never invent crew-rest, duty, weather, syllabus, qualification or future-capacity limits. Read the profile for exact rules rather than substituting a summary from this file.
- **Facts remain traceable.** Maintain normalized facts and source locations; distinguish facts, interpretations and recommendations. Missing products limit affected checks, not all planning. Schedulers decide when drafting starts.
- **Actuals and blind tests are different.** Live execution results and historical actuals knowable by the declared cutoff are legitimate. Disallowed hindsight during a historical blind test requires a clean restart in an isolated context, including clean handoffs/transcripts. Never quarantine-and-continue after exposure.
- **Playbook governance persists.** Preserve stable candidate IDs and Pending/Approved/Rejected history. No automatic lesson promotion, weekly-to-standing conversion or revival of rejected lessons without materially new evidence.

Keep [archive/v0.3](archive/v0.3/README.md) and original baseline files unchanged. It is historical reference, not the current operational primer. Do not rewrite an archive to make it agree with a later release. Label text extractions as extractions and retain provenance hashes; do not claim they preserve the original binary or page layout.

## Write for a pilot new to scheduling

The README is the operator's entry point. Assume the reader understands flying but has never built the schedule or used this package.

- For each phase, state what to do, which existing products to upload, what may be missing, the exact prompt to paste, what output to expect and when to move on.
- Keep copy/paste prompts executable after replacing clearly marked placeholders. Define terms such as active schedule, baseline, sell and buy in plain language.
- Keep setup, human approval/publication statements, reflow and handoff/resume instructions consistent with the primer. Never make example approvals look like decisions already made.
- Use standard squadron products as inputs. Forms capture missing guidance, changes and recommendations; do not require users to transcribe information already supplied elsewhere.
- Personnel forms capture actionable effects, exact effective times and mandatory/recommended status without unnecessary personal explanations.
- Keep reusable workflow separate from Pantons-specific policy. Another squadron must be able to identify which local rules it must supply or approve.
- Preserve concise Markdown handoffs plus actual source products. Full transcripts are optional reference. Do not assume native export, shared multiuser chat, cross-chat memory or access to another user's uploads. Verify current platform features only when they materially affect the task.

## Repository and GitHub practices

- Prefer the existing authenticated GitHub connection. Local git is fine when available and authorized. Inspect tool results; never invent a successful commit, push, PR or merge. If local git authentication is unavailable, use supported connector actions rather than seeking credentials in unrelated files.
- Work on a scoped branch from the current base, or continue the appropriate open task branch. Prepare a reviewable PR for repository changes. Do not merge, change repository visibility or make a public release without user authorization. Existing authorization in the current conversation still applies.
- Inspect the diff before sending changes. Do not force-push, delete unrelated files, rewrite history or alter repository settings as incidental cleanup.
- Keep real operational products, personnel data, generated operational reports and real handoffs outside the repository, even while it is private. Examples must be unmistakably synthetic. An ignored directory is not an access control or release approval.
- Do not add dependencies, automation, model-specific infrastructure or generated binary exports solely to make this documentation repository appear more complete. Create additional formats when requested or needed for the deliverable.

## Validate proportionately and report honestly

For each change, inspect the affected contracts across README prompts, primer, local profile, forms, report instructions and examples. When behavior changes, update the relevant design record, crosswalk, change log and validation cases. Routine editorial changes do not require rewriting all of them.

Check relative links, anchors, table structure, fenced prompts, filenames, version labels and synthetic-example labeling where affected. Check baseline hashes if baseline preservation is relevant. For changes sent through connector APIs, verify the resulting remote files or blob hashes against the reviewed contents. Use `rg` for file/text searches when available.

Use [the validation plan](docs/v0.4/validation-plan.md) for meaningful behavior checks. Do not add tests that merely mirror prose or perform broad repeated testing without a concrete risk. Distinguish static document review from actual model runs, historical adjudication and operational validation. Cases not run stay **Not run**. Never carry an old QC result forward as proof of checks on newly changed content.

PR descriptions and final responses should explain what changed, why, what was checked, and material limitations. Link the PR or relevant file. Do not claim ChatGPT Mil access, model reliability, operational readiness or public releasability without the corresponding evidence and human decisions.
