# Tuesday — Start the week

Tuesday is the normal GenAI.mil startup day. This step is mechanical: create the weekly workspace, start the main Gemini conversation, load the reusable instructions and available Monday inputs, and establish the week's run controls. Planning comes next in **04 Tuesday - Plan the Week.docx**.

## Create the weekly workspace

1. Copy **COPY THIS FOLDER FOR EACH NEW WEEK** beside itself. Rename the copy **Week of YYYY-MM-DD**, using the first date of the execution week.
2. Put source products in **Inputs**, schedule versions in **Schedules**, and reports, decisions and handoffs in **Working Record**. Preserve meaningful presented, buy/sell, published and signed daily versions.
3. Open a new GenAI.mil conversation for this execution week using **Gemini 3.7 Flash** when available.
4. Enable the **DoW Policies Beta (GAMECHANGER)** connector in the main Gemini conversation if it is available. This connector is the only permitted AI-side source for publication-based regulatory QC. Do not substitute ordinary web search or model memory if it is unavailable.
5. Upload **System → UPLOAD THIS TO START.docx** plus the current **Local Profile.docx**, **Stable References.docx**, **Playbook.docx**, needed local references and the available Monday inputs.

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
DoW Policies Beta (GAMECHANGER): [ENABLED / NOT AVAILABLE / UNKNOWN].

Confirm which startup/local files you can read and whether GAMECHANGER is
actually available in this conversation. Draft the weekly run control and product
manifest from uploads and my answers. Do not make me transcribe existing products.
Flag gaps and their effects.

For publication-based currency, qualification, crew-rest/duty, evaluation,
syllabus/prerequisite, event-credit or recurring-training requirements, use only
publications retrieved through GAMECHANGER. Do not use model memory or ordinary
web search as regulatory evidence. If a sufficiently traceable applicable
publication cannot be retrieved, mark that check CANNOT VERIFY and make no
regulatory determination.

Wait for my analysis request; answer planning questions when I ask them.
Schedulers will create the initial lineup. Do not create it for us.
```

**You should get:** confirmation of readable startup/local files, GAMECHANGER availability, a current product manifest, and a short list of missing or conflicting inputs. The assistant should not build the complete lineup.

If GAMECHANGER is unavailable, continue the normal scheduling workflow. Publication-based regulatory checks will remain **CANNOT VERIFY** until the connector is available; this must not trigger a web/model-memory fallback.

**Next:** immediately continue with **04 Tuesday - Plan the Week.docx**.