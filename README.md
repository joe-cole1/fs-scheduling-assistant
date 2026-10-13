# Panton Scheduling Assistant

An AI scheduling partner for the Pantons (35th Fighter Squadron) weekly flying schedule. It runs in GenAI.mil using ordinary file uploads. People build, approve and publish the schedule; the assistant checks and advises.

## Download

- **[Full kit](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest/download/Panton_Scheduling_Assistant.zip)**: use this for a new install or when moving from 0.6.x.
- **[Update](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest/download/Update.zip)**: for an existing 0.7 or later install, adopted at a week boundary.

The [latest release](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest) lists both under Assets. GitHub's automatic "Source code" downloads are maintainer sources, not the kit.

**New install:** right-click the full kit and choose Extract All. Put the **Panton Scheduling Assistant** folder in your approved scheduling location and open **START HERE.docx**.

**Update:**
1. Delete the TASK FILES folder.
2. Double-click Update.zip, press Ctrl+A, and drag everything into your Panton Scheduling Assistant folder.
3. If a READ ME file comes with it, follow it, then delete it.

Squadron Rules and WEEKS are never touched.

**Moving from 0.6.x:** download the full kit into a new folder; don't use the update on an old install. If your squadron edited its old Local Guidance, copy those edits into the matching section of the new **Squadron Rules.docx** and have the DO confirm it. Finish any active week with the kit you started it on, and start the next week with the new kit.

## How schedulers use it

Every task uses the same 4 moves:

1. Open a **new** GenAI.mil chat and turn on **DoW Policies (GAMECHANGER)**.
2. Drag in the **task file** for the day, **Squadron Rules**, and this week's **newest WEEK FILE**.
3. Do exactly what the assistant says. It goes one step at a time, asks for any other files it needs, and explains things again when you type **HELP**.
4. When it hands you a new **WEEK FILE**, save it in the week's folder with the name it gives.

| When | Task file |
| --- | --- |
| Monday | No AI: copy the weekly folder and collect the inputs on its checklist |
| Tuesday | 1 TUESDAY - Plan next week |
| Wednesday | 2 WEDNESDAY - Check my draft |
| Thursday | 3 THURSDAY - Full QC, then 4 THURSDAY - Buy-Sell |
| Thursday to Friday | 5 THU-FRI - Check changes and publish |
| Execution week | 6 EXECUTION WEEK - Schedule change |
| Optional, DO only | DO ONLY - Independent review |
| Not sure | HELP - What do I do next |

The WEEK FILE carries the week's decisions, schedule versions, findings and regulation checks from one chat to the next. Anyone who picks up the week, such as a daily scheduler or a relief scheduler, needs only the week folder. Every task file includes **Do not delegate to subagents**, and no specific model is required.

## Approval and evidence

Humans create and edit schedules, coordinate, approve and publish.

- **Thursday Buy/Sell is the formal DO buy, and only when the DO explicitly approves.** The exact presented schedule plus the recorded directions is the approved version.
- **Carrying out those directions faithfully needs no routine second buy.** A materially different solution goes back to the DO.
- **Publication is a separate human action.** Every waiver needs the DO and the applicable waiver authority.

Regulation checks (currency, qualification, crew rest and duty, evaluations, syllabus and others) must come from traceable **DoW Policies Beta (GAMECHANGER)** publications:

- Missing or inadequate evidence stays **CANNOT VERIFY**.
- Conflicting authorities stay **SOURCE CONFLICT**.
- Model memory and ordinary web search never fill the gap.

Other planning continues either way. No assistant output certifies full compliance or grants approval.

Use only systems and locations authorized for your material. Keep actual schedules, personnel data and records out of this repository. Package checks do not prove GenAI.mil behavior or operational readiness.

## Maintainers

Read [AGENTS.md](AGENTS.md), [architecture](ARCHITECTURE.md), [design decisions](docs/design-decisions.md), [validation](docs/validation-plan.md) and [packaging](packaging/README.md). Kit sources are in `packaging/kit` and the Pantons profile is in `local-profiles/pantons.md`. Build with `scripts/build_packages.py`; generated ZIPs stay out of Git.

`packaging/version.txt` is the reviewed release identity. After a reviewed PR is merged, use **Actions → Publish release** from main and leave Version blank. The workflow validates, builds, stages a matching draft, verifies all assets and publishes last. Do not create the release manually or move a tag.

No open-source license has been selected; the owner decides licensing and public distribution.
