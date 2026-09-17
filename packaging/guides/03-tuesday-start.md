# Tuesday — Start the week

Tuesday is the normal GenAI.mil startup day. Create the weekly workspace, start the main Gemini conversation, load the reusable instructions and available Monday inputs, and let the assistant infer the week's run state. Planning comes next in **04 Tuesday - Plan the Week.docx**.

## Create the weekly workspace

1. Copy **COPY THIS FOLDER FOR EACH NEW WEEK** beside itself. Rename the copy **Week of YYYY-MM-DD**, using the first date of the next execution week unless leadership selected another week.
2. Put source products in **Inputs**, schedule versions in **Schedules**, and reports, decisions and handoffs in **Working Record**. Preserve meaningful presented, Buy/Sell, published and signed-daily versions.
3. Open a new GenAI.mil conversation for this execution week using **Gemini 3.7 Flash** when available.
4. Enable the **DoW Policies Beta (GAMECHANGER)** connector in the main Gemini conversation if available. This connector is the only permitted AI-side source for publication-based regulatory QC. Do not substitute ordinary web search or model memory.
5. Upload **System → UPLOAD THIS TO START.docx** plus the current **Local Profile.docx**, **Stable References.docx**, **Playbook.docx**, needed local references and the available Monday inputs.

A normal fresh chat for a new execution week does not need a handoff. If an already-started week is moving to a replacement chat or another user, follow **12 Hand Off an Active Week.docx** instead. A handoff's recorded week overrides the normal next-week default.

Do not copy the whole System folder into each week. The chat cannot see a shared-drive file unless you upload it.

## Activate the assistant

Paste this after the files are uploaded:

```text
Read UPLOAD THIS TO START.docx and the attached approved local guidance.
Unless I explicitly say otherwise, treat this conversation as planning for the
next execution week under the approved local counting week.

Infer the exact execution dates, timezone, current workflow step, source
manifest, and any schedule/version roles from the current date, folder and file
names, schedule headers, uploaded products, and conversation. Do not ask me to
complete a run-control questionnaire or restate information already in the
products. Draft the run control and product manifest yourself. State only
consequential assumptions or limitations, and ask one question only when an
ambiguity would materially change the work. If more than one schedule could be
the active or authoritative version, ask me which one controls.

Confirm which startup and local files are readable and whether DoW Policies Beta
(GAMECHANGER) is actually available. Classify supplied products as CURRENT,
STALE, PARTIAL, CONFLICTED, INTEGRITY FAILED, UNREADABLE, or SUPERSEDED and
explain the affected checks.

Before using a calculated workbook for person-specific conclusions, verify its
reliable identity linkage (prefer a stable identifier when available), source
date, formulas, duplicate-name handling, and missing/error states. A material
identity or formula defect is INTEGRITY FAILED. Do not use affected cached values
merely because they look plausible; continue unaffected analysis.

For publication-derived currency, qualification, crew-rest/duty, evaluation,
syllabus/prerequisite, event-credit, recurring-training, or similar requirements,
use only publications retrieved through GAMECHANGER. Do not use model memory or
ordinary web search as regulatory evidence. If no sufficiently traceable
applicable publication is retrieved, mark the check CANNOT VERIFY and make no
regulatory determination.

Wait for my planning request. Schedulers will create the initial lineup; do not
create it for us.
```

**You should get:** a concise statement of the inferred next execution week and current task, confirmation of readable startup/local files, GAMECHANGER availability, an assistant-drafted product manifest, and only the consequential gaps or assumptions. You should not receive a blank field list to complete or a complete lineup.

If GAMECHANGER is unavailable, continue normal scheduling work. Publication-based regulatory checks remain **CANNOT VERIFY** until the connector is available; this must not trigger a web/model-memory fallback.

**Next:** immediately continue with **04 Tuesday - Plan the Week.docx**.
