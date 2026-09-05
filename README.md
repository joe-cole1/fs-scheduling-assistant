# Fighter Squadron Scheduling Assistant

Download a ZIP, extract it into your scheduling location, and open **START HERE.docx**. Everything a scheduler needs is in Word. You do not need to understand GitHub or code.

## Download — package v0.4.1

- **[Pantons setup ZIP](downloads/Pantons_Setup.zip?raw=true)** — approved Pantons local profile plus the complete kit.
- **[First-time squadron setup ZIP](downloads/First_Time_Squadron_Setup.zip?raw=true)** — complete kit with a blank local profile and guided setup questions.
- **[Update an existing setup](downloads/Update_Existing_Setup.zip?raw=true)** — use next week; follow UPDATE INSTRUCTIONS.docx. Keeps local guidance and weekly work in place.

If GitHub shows a file page, click **Download raw file**. Right-click the downloaded ZIP and select **Extract All**. Open the extracted folder, then START HERE.docx. The repository is currently private; someone with access must download the ZIP and place it in your approved shared location. ChatGPT Mil itself needs no GitHub access.

Moving from the earlier Markdown kit? Use a full setup ZIP once and carry over your approved local guidance and weekly work. Subsequent updates replace only the System folder and START HERE. Do not extract a full setup over your existing files.

## What you do

1. **Set up once.** Follow Instructions → 01 First time setup.docx. Keep local guidance outside the replaceable System folder.
2. **Start each week.** Copy COPY THIS FOLDER FOR EACH NEW WEEK and rename the copy. Follow 02 Start a week.docx.
3. **Upload and chat.** Upload UPLOAD THIS TO START.docx, current local guidance and the available squadron products into ChatGPT Mil. Paste the short prompt in the guide.
4. **Follow your phase.** Separate Word guides walk through gathering products, reviewing your draft, selling the schedule, corrections/QC/buy/publication, and execution reflows. Each includes expected inputs and copy/paste prompts.

Use the trackers, calendars and schedules your squadron already maintains. Blank forms collect missing guidance and changes; they do not require retyping existing products. The assistant helps consolidate, answer questions and QC. **Schedulers build and edit the schedule; humans approve and publish it.**

One chat per execution week is convenient. A Word handoff plus the actual source files lets another user continue in a new chat. Shared-chat features, APIs, connectors and custom software are not required.

DOCX opening and package structure are checked separately from model behavior. **This package has not yet been tested in ChatGPT Mil.** Guide 10 provides the first-use checks. Use only systems and locations authorized for your material; actual operational data stays outside this repository.

## For maintainers

Read [AGENTS.md](AGENTS.md), [architecture](ARCHITECTURE.md) and [packaging instructions](packaging/README.md). Markdown is maintained source; the ZIPs are the operator product. Number deliberate package updates and rebuild the current downloads together. Earlier versions remain in Git history, not archive folders.

- [Approved decisions](docs/v0.4/design-decisions.md) and [policy preservation](docs/v0.4/policy-crosswalk.md)
- [Primer source](docs/v0.4/system-primer.md) and [Pantons local rules](local-profiles/pantons-v0.4.md)
- [Validation plan](docs/v0.4/validation-plan.md), [QC record](docs/v0.4/repository-qc.md) and [change log](CHANGELOG.md)
- [Data handling](docs/data-handling.md): only releasable content and synthetic examples may be publicly distributed. Human release review is required; private visibility is not approval to store operational data.

No open-source license has been selected. The owner decides licensing and public distribution.
