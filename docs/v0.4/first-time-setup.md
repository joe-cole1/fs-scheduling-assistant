# First-time squadron setup — v0.4

Use this once before your squadron's first weekly run. You will download the reusable kit, organize a shared working location, identify your existing products, and use a planning conversation to draft any missing local guidance. After that, use the [README's weekly steps](../../README.md#0-set-up-the-chat-once-for-the-execution-week).

**ChatGPT Mil does not need access to GitHub or your shared drive.** A human copies the instructions into the chat and uploads the needed files. A path written in a document does not give the assistant access to that path. No installation, code execution, connector, or shared-chat capability is required.

## 1. Choose a location and an owner

Have the scheduling shop choose a setup owner and identify the DO who will confirm local guidance. The owner keeps the current-file list organized; this role does not create scheduling or waiver authority.

Use an existing squadron shared-drive location authorized for the material and accessible to the people who need it. The example below uses `S:\Operations\Scheduling_Assistant\`. Your drive letter and path will differ. This is an organization recommendation, not authorization to store a particular category of information. Follow existing access, handling and retention rules; do not change drive permissions just to follow this guide.

Keep the operational working area **outside any Git checkout or folder synchronized back to GitHub**. You may copy the reusable GitHub documents into it. Never send the local working area back to the repository.

## 2. Create the folders

Create one folder named `Scheduling_Assistant`. Under it, use the following paths. Folder names and dates are illustrative; no script is needed.

| Path under `Scheduling_Assistant` | Put this here |
| --- | --- |
| `00_Reference_Kit\v0.4\` | Downloaded GitHub instructions and blank forms, preserving their original subfolders and filenames |
| `01_Local_Config\Drafts\` | Proposed local profile, unresolved rules and unfinished setup products |
| `01_Local_Config\Current\` | Current local profile, reference index, approved playbook and any tailored blank forms; include explicit status inside each file |
| `01_Local_Config\Superseded\` | Prior local configurations retained under your normal records practices |
| `01_Local_Config\Reference_Copies\` | Dated reference copies needed for upload, if not already readily available elsewhere |
| `02_Weekly_Work\YYYY-MM-DD\Inputs\` | Current weekly products and actual-result updates; use the execution week's Sunday date for Pantons |
| `02_Weekly_Work\YYYY-MM-DD\Schedules\` | Drafts, sell-presented, corrected, bought, published and signed daily versions |
| `02_Weekly_Work\YYYY-MM-DD\Analysis\` | Assistant draft reviews, sell briefs, QC reports and reflow recommendations |
| `02_Weekly_Work\YYYY-MM-DD\Decisions\` | Run control/manifest, weekly leadership inputs, sell dispositions, confirmations, waivers and release/sign-off records |
| `02_Weekly_Work\YYYY-MM-DD\Handoffs\` | Current-state Markdown for the next user; optional full transcripts clearly labeled |
| `03_Validation\CASE-ID\Blind_Inputs\` | A deliberately cutoff-clean historical test packet |
| `03_Validation\CASE-ID\Locked_Blind_Report\` | Completed blind report saved before later outcomes are introduced |
| `03_Validation\CASE-ID\Later_Outcomes\` | Outcomes and retrospective material kept separate from blind inputs |

Put `Setup_Record.md` directly inside `01_Local_Config\`. It is the short index of setup status, current filenames, owners and unresolved items described in step 6.

Create the weekly and validation subfolders only when needed. If your squadron already has an equivalent layout, reuse it and record the mapping. You do not need a second copy of every official tracker. Keep the originals in their established authoritative locations and take dated upload snapshots only when needed. Record their source and effective date.

**Folder placement is not approval.** A file in `Current` can still contain clearly marked unresolved rows. A schedule in `Schedules` is not bought or published until the actual human action is recorded. Do not overwrite the sold, bought, published or signed daily baseline just to keep a tidy folder.

The validation folders are an organizational aid, not a technical barrier: never upload the entire case folder into a blind test. Transfer only the files allowed by its cutoff. A contaminated chat requires an isolated restart even if you later move the offending file elsewhere.

## 3. Copy the reusable kit from GitHub

A human with repository access downloads the files and places them under `00_Reference_Kit\v0.4\`, preserving relative paths. You can download a repository ZIP and extract it, or copy the items below individually. Record the repository revision or download date in `Setup_Record.md`. ChatGPT Mil itself needs no GitHub credentials.

| Repository item to copy | Purpose | What to put in ChatGPT Mil |
| --- | --- | --- |
| [README.md](../../README.md) | Human weekly checklist and phase prompts | Paste the relevant phase prompt, not necessarily the entire README |
| [docs/v0.4/system-primer.md](system-primer.md) | Assistant's reusable operating instructions | Paste between START OF PRIMER and END OF PRIMER at the start of a new chat |
| [docs/v0.4/first-time-setup.md](first-time-setup.md) | This guide | Paste the setup prompt below; optional upload of the guide |
| [docs/v0.4/phase-guide.md](phase-guide.md) and [report-contracts.md](report-contracts.md) | More detailed workflow and output guidance | Optional reference when needed |
| [templates/setup/local_profile_template.md](../../templates/setup/local_profile_template.md) | Blank starting point for a new squadron's local profile | Upload for the setup Q&A; all rows start unresolved |
| [templates/v0.4](../../templates/v0.4) — all nine forms | Reusable form masters | Upload forms 04 and 09 for setup; other forms as needed |
| [local-profiles/pantons-v0.4.md](../../local-profiles/pantons-v0.4.md) | Approved Pantons scheduling profile | Pantons: upload as governing local profile. Other squadrons: do not load it as governing policy |
| [docs/data-handling.md](../data-handling.md) | Repository/operational-data boundary | Human reference; optional upload |
| [docs/v0.4/validation-plan.md](validation-plan.md) and [examples/v0.4](../../examples/v0.4) | Rehearsal and historical testing instructions/fixtures | Only deliberately selected test material, not routine operational inputs |

If you copy individual files and need a linked document, copy that document at its original relative path too. Downloading the whole kit is easier for offline link navigation, but **do not upload the whole kit into the assistant**. It includes historical policy and outcome-rich examples that are not current operational instructions.

`AGENTS.md`, `ARCHITECTURE.md`, development decision records and the v0.3 archive are for maintainers/reference. They are not required operational uploads. Keep the downloaded kit unchanged; put your squadron's working products in `01_Local_Config` or the weekly area.

## 4. Gather what the squadron already has

You do not need all of this to start the setup conversation. Bring what exists and have the assistant list the gaps. This is an inventory of sources, not a demand to rewrite them into forms.

| Existing product or knowledge | What setup needs from it | Typical contributor |
| --- | --- | --- |
| Local scheduling guidance and actual approval process | Who directs, who signs daily schedules, how sell/buy/publication work, how waivers go through DO and applicable authority | DO / scheduling |
| Upgrade/MQT syllabi and training guidance | Event sequence, credit, prerequisites, ratios, accounting and applicable same-day rules | Training / DO |
| Crew-rest/duty guidance and mission timelines | Governing limits, calculation boundaries, brief/debrief windows and exceptions | Designated local owner |
| Validated mission-weather guidance | Mission-specific rules with applicability and status; unresolved items stay unresolved | Designated local owner |
| Maintenance/turn/configuration conventions | Meaning of line/turn notation, protected spares, configurations and transitions | Maintenance / scheduling |
| Qualification and currency products | Which product establishes what, effective dates, update process and location | Training / qualification owner |
| Leave and commitments products | Where to get them, exact-time fields and how discrepancies are resolved | Scheduling / Flt CCs |
| Simulator and external-support products | Who supplies bookings and updates, and how capacity/support is represented | Scheduling / support owners |
| Roster and glossary | Callsign/name matching, local event codes and aliases | Scheduling |
| Current training phase plan | Mission/configuration emphasis and source owner; actual dates remain current planning inputs | DO / scheduling |

Use product names, locations and sample column headings for an initial inventory when full files are unnecessary. Actual content must be uploaded when the assistant needs to inspect it. Do not include personal explanations when only a scheduling effect is needed.

For Pantons, begin with the existing approved Pantons profile; setup fills missing source references and local-file organization, not a fresh policy rewrite. For a different squadron, use the blank profile starter. Do not transfer the Pantons three-event ceiling, pairing examples or any other local convention into another squadron by default. If that squadron's process conflicts with the reusable primer, identify the conflict and obtain an explicit product-authority decision; do not silently rewrite either side.

## 5. Start a first-time planning Q&A conversation

Use a separate chat named, for example, `Scheduling Assistant — Squadron Setup`. This is an administrative setup conversation, **not a sixth operational phase** and not a request for a weekly review. You do not need an execution week, active schedule or comparison baseline yet.

1. Paste the v0.4 system primer.
2. Upload your existing approved local profile, if one exists; otherwise upload the blank local-profile starter.
3. Upload forms [04 Stable references](../../templates/v0.4/04_stable_local_rules_and_references.md) and [09 Playbook](../../templates/v0.4/09_playbook.md), plus any current local versions of them.
4. Upload the available local guidance/source products needed for setup.
5. Paste this prompt. “Planning Q&A” is an instruction to the assistant, not a platform feature or menu setting.

```text
We are setting up Scheduling Analysis System v0.4 for our squadron for the first
time. Work in planning Q&A mode for this administrative setup task. This is not
a sixth operational phase and not a weekly schedule review. No execution week,
active schedule or baseline is assigned yet; do not ask for them just to start.

Squadron: [name].
My role: [DO / scheduler / other].
DO or product authority: [role/name if known].
Local timezone: [timezone or Unknown].
Shared working location: [path or Not decided].
Existing approved local profile: [filename/version or NONE].
Existing approved playbook: [filename/version or NONE].

Use the uploaded v0.4 primer, blank forms and our supplied sources. You cannot
access GitHub or our shared drive just because I name a path. Tell me which
actual files you need uploaded. Inventory existing products before proposing
new forms, and do not make us retype information already supplied elsewhere.

If an approved local profile exists, preserve it and ask only about genuine
gaps or conflicts. If none exists, draft our profile from our sources and human
answers. Do not import Pantons-specific rules, synthetic examples, numerical
limits or general military knowledge as our approved policy.

Ask exactly one substantive setup question at a time. Explain why it matters,
give a recommended approach and relevant tradeoffs, then wait for my answer.
Recommend process choices, not invented scheduling limits. Skip questions our
sources already answer; resolve routine formatting yourself. Start by briefly
listing the existing products you recognize and the most important missing
information, then ask the single most useful question.

Maintain a setup record distinguishing supplied facts, human confirmations,
proposed guidance, approved standing rules and unresolved items. Cite source
locations or the human statement. A scoped human confirmation can close a
concern without more documentary proof, but does not silently approve new
standing policy or waive a requirement. Every waiver still goes through the DO
and applicable authority. Record approval of new enduring rules only when
explicitly given by the DO. If I am not that authority, prepare the decision
for them instead of treating my preference as DO direction.

Help us prepare, when I request the drafts:
1. Local_Profile_v1_DRAFT.md — enduring local scheduling rules and open items.
2. Stable_References_v1_DRAFT.md — source index and only needed missing parameters.
3. Approved_Playbook_v1_DRAFT.md — existing approved lessons if supplied;
   otherwise no approved lessons yet. Preserve Pending/Approved/Rejected IDs.
4. Setup_Record.md — current file/version list, product owners/locations, gaps,
   decisions, and the next action.
5. Optional tailored blank DO/Flt CC input forms if our existing products do
   not already cover the need. Do not invent a target week's guidance.

Do not generate a complete lineup, modify our source files, publish anything or
pretend you saved files on the drive. Produce copyable Markdown that a human
can save. Keep proposed content unmistakably draft until humans confirm it.
```

Expected result: a short inventory and one useful question. Continue answering and uploading requested references. You can ask, “Which parts can you already fill from our documents?” or “What is still waiting on the DO?” without triggering a full schedule review.

## 6. Generate, review and save the local products

Once the meaningful setup questions are answered, request the draft files:

```text
Generate the setup drafts now from our supplied sources and recorded answers.
Keep unknowns and unapproved proposals visible; do not fill them from examples.
Use the agreed filenames and keep cross-references consistent with them.
Show the unresolved decisions separately and identify which need DO action.
Do not invent approvals, qualified personnel, limits or completed validation.
```

If a downloadable Markdown file is available, save it. Otherwise copy each document into a plain-text editor and save with the stated `.md` extension. Ensure the filename is not accidentally `.md.txt`. The assistant's saying “saved” is not a substitute for the human actually saving the file.

| Product to create or adopt | Starting point | Save while drafting / after review |
| --- | --- | --- |
| `Local_Profile_v1_DRAFT.md` | Existing squadron profile or [blank starter](../../templates/setup/local_profile_template.md) | `Drafts`; after explicit local-policy approval, save the identified current version in `Current` and preserve its status/scope |
| `Stable_References_v1_DRAFT.md` | Form 04 and existing references | `Drafts`, then current reference index in `Current`; actual source files remain in their established locations or dated reference copies |
| `Approved_Playbook_v1_DRAFT.md` | Existing approved playbook or form 09 | `Drafts`, then `Current`; if no lessons are approved, explicitly say “No approved lessons yet” and leave candidate decisions Pending |
| `Setup_Record.md` | Inventory and decisions from the Q&A | `01_Local_Config`; update to point to exact current and draft filenames |
| Optional tailored blank DO/Flt CC forms | Forms 02/03 | `Current` once accepted for use; keep weekly directions and personnel entries blank |

You may keep an existing approved profile/playbook filename instead of renaming it. `v1` above is a naming example, not a mandatory reset of existing version history. After approval, a name such as `Local_Profile_v1.md` is convenient, but **the explicit approval inside the file matters more than its name**. Renaming a draft cannot approve it. Record scope: unresolved rows stay unresolved even when confirmed portions are ready for use.

Keep `Setup_Record.md` short:

- Setup owner, DO/product authority, timezone and chosen root path.
- Downloaded kit revision/date and local profile/reference/playbook versions.
- Exact current filenames and approval/confirmation status; list drafts separately.
- Product inventory: product, existing location, supplying role, update timing, and known gap. A path is a human retrieval instruction, not assistant access.
- DO decisions, human confirmations and unresolved items with affected checks/next action.
- What was actually rehearsed, what remains Not run, and the intended next weekly task.

Have the relevant humans review the drafts. Explicit DO approval is needed to establish new standing rules or promote lessons. Do not request repeated proof for a concern a human has already confirmed. If information remains missing, retain that limitation; setup does not introduce a complete-packet gate before schedulers can begin useful planning.

## 7. Check the setup and start the first week

Before calling setup usable, walk through these practical checks with a scheduler:

- They can find the primer, current local profile/reference index/playbook and source product locations.
- The profile clearly separates approved rules, human-confirmed facts, proposals and unknowns; it has not adopted another squadron's examples as policy.
- The scheduling shop knows how to record sell directions, correction QC, formal buy, publication, daily sign-offs and DO/waiver routing.
- They can paste a planning question, see a missing-input warning and save a Markdown handoff. Mark any action not tried as Not run.

Use deliberately synthetic inputs for the first rehearsal. Follow the [validation plan](validation-plan.md) for historical testing; never mix later outcomes into an earlier-cutoff blind packet. A successful setup chat is not proof of operational reliability.

Create the first weekly folder. Start a new weekly conversation using [README step 0](../../README.md#0-set-up-the-chat-once-for-the-execution-week), upload the current local configuration and available weekly products, and proceed to phase 1. For another squadron, use its current approved local profile in place of the README's Pantons profile. For Pantons, the counting week remains Sunday–Saturday. Weekly DO priorities, Flt CC effects and waivers belong to that week, not automatically in standing setup files.

## 8. Maintain it without repeating the whole setup

The owner updates source locations and current-version pointers when products change. Keep dated snapshots/baselines and superseded configuration under normal retention practices. Download a newer GitHub kit into a new version folder; review its change log and compatibility before using it. Do not overwrite local guidance with the downloaded example profile.

When changing users in setup, save `Setup_Record.md`, current drafts and relevant source products; tell the next chat this is unfinished administrative setup with no execution week yet. For an operational weekly handoff, use form 08 and the README's resume prompt. Both require actual source uploads, not just the previous conversation's text.
