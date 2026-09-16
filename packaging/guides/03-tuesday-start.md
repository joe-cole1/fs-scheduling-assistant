# Tuesday — Start the week

Tuesday is the normal GenAI.mil startup day. This step is mechanical: create the weekly workspace, start the main Gemini conversation, load the reusable instructions and available Monday inputs, and establish the week's run controls. Planning comes next in **04 Tuesday - Plan the Week.docx**.

## Create the weekly workspace

1. Copy **COPY THIS FOLDER FOR EACH NEW WEEK** beside itself. Rename the copy **Week of YYYY-MM-DD**, using the first date of the execution week.
2. Put source products in **Inputs**, schedule versions in **Schedules**, and reports, decisions and handoffs in **Working Record**. Preserve meaningful presented, buy/sell, published and signed daily versions.
3. Open a new GenAI.mil conversation for this execution week using **Gemini 3.7 Flash** when available.
4. Upload **System → UPLOAD THIS TO START.docx** plus the current **Local Profile.docx**, **Stable References.docx**, **Playbook.docx**, needed local references and the available Monday inputs.

A normal fresh chat for a new execution week does not need a handoff. If an already-started week is moving to a replacement chat or another user, follow **12 Hand Off an Active Week.docx** instead.

Do not copy the whole System folder into each week. The chat cannot see a shared-drive file unless you upload it.

## Activate the assistant

Paste this after the files are uploaded:

```text
Read UPLOAD THIS TO START.docx and follow it as the scheduling primer.
Use the attached approved local profile, references and playbook.
Execution week: [start date] through [end date]. Timezone: [timezone].
As of: [date/time]. Test condition: OPERATIONAL.
Current phase: 1 PRODUCT GATHERING. Ingest gate: CONFLICTS ONLY.
Report depth: BRIEF. Active schedule and comparison baseline: NONE yet.
Primary scheduler workflow: Gemini.
Confirm which startup/local files you can read and identify missing ones.
Draft the weekly run control and product manifest from uploads and my answers.
Do not make me transcribe existing products. Flag gaps and their effects.
Wait for my analysis request; answer planning questions when I ask them.
Schedulers will create the initial lineup. Do not create it for us.
```

**You should get:** confirmation of readable startup/local files, a current product manifest, and a short list of missing or conflicting inputs. The assistant should not build the complete lineup.

**Next:** immediately continue with **04 Tuesday - Plan the Week.docx**.