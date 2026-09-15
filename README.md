# Fighter Squadron Scheduling Assistant

Download a ZIP, extract it into your scheduling location, and open **START HERE.docx**. Everything a scheduler needs is in Word. You do not need to understand GitHub or code.

## Download the latest release

- **[Pantons setup ZIP](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest/download/Pantons_Setup.zip)** — approved Pantons local profile plus the complete kit.
- **[First-time squadron setup ZIP](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest/download/First_Time_Squadron_Setup.zip)** — complete kit with a blank local profile and guided setup questions.
- **[Update an existing setup](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest/download/Update_Existing_Setup.zip)** — use next week; follow UPDATE INSTRUCTIONS.docx. Keeps local guidance and weekly work in place.

You can also open the [latest release](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest) and choose a named ZIP under **Assets**. Use the named setup ZIPs; GitHub’s automatic **Source code** downloads do not contain the built Word kit.

Right-click the downloaded ZIP and select **Extract All**. Open the extracted folder, then START HERE.docx. The repository is currently private; someone with access must download the ZIP and place it in your approved shared location. GenAI.mil itself needs no GitHub access.

Immediately after a release is published, its ZIPs may still be building. If downloads are missing, the maintainer should check **Actions → Build release downloads** before distributing it.

Moving from the earlier Markdown kit? Use a full setup ZIP once and carry over your approved local guidance and weekly work. Subsequent updates replace only System and START HERE. Do not extract a full setup over your existing files.

## Pantons weekly battle rhythm

The operator guides are written around the actual weekly flow:

1. **Monday — Inputs due.** All scheduling inputs are due NLT COB. Monday is a human deadline; the assistant does not assume the packet is complete just because the deadline passed.
2. **Tuesday — Ingest and plan.** Schedulers upload the available products to the main GenAI.mil conversation using **Gemini 3.7 Flash** when available. First reconcile gaps/conflicts, identify checkrides/evaluations and directed DV/senior-leader flyers, and plan upgrade events/windows/resources.
3. **Wednesday — Build.** Schedulers build the bulk of the weekly schedule. Gemini supports targeted planning questions, conflict checks and cascade analysis while humans construct the lineup.
4. **Thursday — Full QC.** Schedulers perform QC and Gemini independently reviews the complete near-final schedule. The DO may then run a **separate optional adversarial review** using GPT-5.6 Terra or Grok Expert 4.5 before the sell.
5. **Thursday — Sell.** Schedulers present the chosen version; the DO directs. Any accepted adversarial finding enters the main workflow only as human DO direction.
6. **Post-sell — Correct, QC, buy and publish.** Schedulers implement directions, Gemini checks second/third-order effects, the DO formally buys the exact corrected version, and humans publish it.
7. **Execution week — Reflow.** Gemini supports reflows from the published weekly baseline and current signed daily schedules while human approval boundaries remain in force.

The named weekdays are the normal Pantons rhythm. They do not automatically create phase advancement, approval, buy or publication.

## What you do

1. **Set up once.** Follow Instructions → 01 First time setup.docx. Keep local guidance outside the replaceable System folder.
2. **Start each week.** Copy COPY THIS FOLDER FOR EACH NEW WEEK and rename the copy. Follow 02 Start a week.docx.
3. **Upload and chat Tuesday.** Upload UPLOAD THIS TO START.docx, current local guidance and the available squadron products into GenAI.mil. Paste the short prompt in the guide.
4. **Follow the day-labeled steps in Guides 03–07.** Tuesday planning, Wednesday build, Thursday full QC, optional DO adversarial review, sell, post-sell correction/buy/publication and execution reflows are separated explicitly.

Use the trackers, calendars and schedules your squadron already maintains. Blank forms collect missing guidance and changes; they do not require retyping existing products. The assistant helps consolidate, answer questions and QC. **Schedulers build and edit the schedule; humans approve and publish it.**

Prefer one main Gemini conversation per execution week. The optional DO adversarial review is intentionally a separate conversation and never becomes an automatic second scheduler. A Word handoff plus the actual source files lets another user continue in a new chat. Shared-chat features, APIs, connectors and custom software are not required.

DOCX opening and package structure are checked separately from model behavior. **This package has not yet been operationally validated in GenAI.mil.** Guide 10 provides the first-use checks. Use only systems and locations authorized for your material; actual operational data stays outside this repository.

## For maintainers

Read [AGENTS.md](AGENTS.md), [architecture](ARCHITECTURE.md) and [packaging instructions](packaging/README.md). Markdown is maintained source; the ZIPs are the operator product. Number deliberate package updates. Publishing a release builds and checks the ZIPs from its tagged source and attaches them to that release. Generated ZIPs are not stored in the repository file tree. See [how to publish](packaging/README.md#publish-a-release). Earlier versions remain in Git history and Releases, not archive folders.

- [Approved decisions](docs/v0.4/design-decisions.md) and [policy preservation](docs/v0.4/policy-crosswalk.md)
- [Primer source](docs/v0.4/system-primer.md) and [Pantons local rules](local-profiles/pantons-v0.4.md)
- [Validation plan](docs/v0.4/validation-plan.md), [QC record](docs/v0.4/repository-qc.md) and [change log](CHANGELOG.md)
- [Data handling](docs/data-handling.md): only releasable content and synthetic examples may be publicly distributed. Human release review is required; private visibility is not approval to store operational data.

No open-source license has been selected. The owner decides licensing and public distribution.
