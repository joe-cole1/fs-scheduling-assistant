# Fighter Squadron Scheduling Assistant

Choose the package that matches your situation, extract it into an approved scheduling location, and open **START HERE.docx**. The Pantons package starts weekly work with the agreed guidance. The first-time package starts a separate guidance-setup checklist.

## Downloads

- **[Pantons — guidance already established](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest/download/Pantons_Setup.zip)** — agreed Pantons profile and weekly workflow; open START HERE and use 02 or 03. No first-time setup folder is included.
- **[First-time squadron setup](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest/download/First_Time_Squadron_Setup.zip)** — draft local guidance and a separate First Time Setup folder; establish and review your squadron’s guidance before weekly use.
- **[Update an existing setup](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest/download/Update_Existing_Setup.zip)** — adopt before next week’s planning; follow UPDATE INSTRUCTIONS.docx.

The [latest published release](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest) contains the named ZIPs under Assets. GitHub’s automatic Source code downloads are maintainer sources, not the operator kit. A reviewed source change appears in these downloads only after the release workflow publishes it.

## What operators use

| Location | Use |
| --- | --- |
| START HERE.docx | Weekly entry point for Pantons/updates; setup entry point in the first-time package |
| System → Instructions | Twelve weekly-work checklists, numbered 02–13, with one action per box |
| System → Prompts | Complete weekly prompts, also printed on the relevant checklist |
| System → UPLOAD THIS TO START.docx | Detailed instructions for the assistant to read |
| Local Guidance | Human-maintained local rules, references and playbook |
| First Time Setup (first-time package only) | One-time guides 01 and 14, setup prompts, setup primer and validation reference |
| COPY THIS FOLDER FOR EACH NEW WEEK → Inputs → INPUT CHECKLIST.docx | Required weekly products and optional or situation-specific inputs |
| Each weekly folder | Inputs, Schedules and the complete Working Record |

Every complete prompt includes **Do not delegate to subagents**. No specific model is required. Prefer one main GenAI.mil conversation per execution week. The optional DO review uses a separate human-started conversation and follows the same no-delegation rule.

## Weekly rhythm

1. **Monday:** inputs due NLT COB; collect existing squadron products.
2. **Tuesday:** start the weekly chat and planning together; identify checkrides, directed flyers, upgrade windows and constraints.
3. **Wednesday:** schedulers build the lineup; the Cross-Functional Schedule Integration Review verifies inputs and assigns remaining issues.
4. **Thursday:** human QC followed by fresh full-schedule assistant QC; optional independent DO review; then formal Buy/Sell.
5. **Thursday–Friday:** humans implement DO directions; the assistant checks implementation and the complete result.
6. **Friday:** final QC, then human publication.
7. **Execution week:** analyze changes against the published week and each affected day’s current signed daily schedule.

The assistant infers dates and file roles, asks only about material ambiguities, and keeps all material findings visible. It retains detailed facts, sources, publication checks, decisions, version roles, outlook and downside analysis in one complete weekly record with distinct sections. Operators do not fill out a startup questionnaire or duplicate trackers.

## Approval and evidence

Humans create and edit schedules, coordinate, approve and publish. Thursday’s Buy/Sell becomes the formal DO buy only when the DO explicitly approves. The exact presented schedule plus recorded directions is the approved baseline. Faithful implementation needs no routine second buy; a materially different solution returns to the DO. Publication is separate. Every waiver requires the DO and applicable waiver authority.

Publication-derived regulatory checks require sufficiently traceable **DoW Policies Beta (GAMECHANGER)** publications. Tuesday creates the initial rule ledger; Thursday refreshes it against the entire candidate; later changes query affected rules. Unavailable or inadequate evidence stays **CANNOT VERIFY**; conflicting authorities stay **SOURCE CONFLICT**. Model memory and ordinary web search cannot fill these gaps. Other supported planning continues. No assistant output certifies full compliance or grants approval.

## Install and update

**Pantons:** extract the Pantons package into a new folder, retain current approved guidance, and start weekly work with 02 or 03. **New squadron guidance:** extract the first-time package and follow First Time Setup → Instructions → 01. System contains weekly materials only; duplicate blank stable-reference and playbook templates are not included there.

**Existing install:** use the update ZIP and replace the entire **System** folder and **START HERE** before next week. Preserve Local Guidance and weekly work. Review explicit persistent migrations, including the new weekly input checklist, and apply only their listed changes manually. Never extract a full package over an existing install.

Use checklist 12 to transfer an active week with its actual source files. A new chat has no assumed access to earlier chats or uploads. Use checklist 13 for updates/rollback. First-time guidance trials use 14 in the separate First Time Setup folder.

Use only systems and locations authorized for your material. Keep actual schedules, personnel data, reports and handoffs outside this repository. Static package/layout checks do not prove native Word, GenAI.mil, connector behavior or operational readiness; those trials require observed outputs and human review.

## Maintainers

Read [AGENTS.md](AGENTS.md), [architecture](ARCHITECTURE.md), [approved design](docs/v0.4/design-decisions.md), [the primer](docs/v0.4/system-primer.md), [validation](docs/v0.4/validation-plan.md) and [packaging instructions](packaging/README.md). Edit maintained sources and rebuild through scripts/build_packages.py. Generated ZIPs remain outside Git.

The reviewed stable release identity is packaging/version.txt. After a reviewed PR is merged and publication is authorized, use **Actions → Publish release** from main. Leave Version blank to use the source version; an entered value must match. The workflow validates and builds, stages a matching draft, verifies all assets, and publishes last. Do not manually create the normal release or move an existing tag.

No open-source license has been selected; the owner decides licensing and public distribution.
