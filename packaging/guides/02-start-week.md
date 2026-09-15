# Start a week

The execution week is the week you will fly. The prior week is the week immediately before it.

For Pantons, **all scheduling inputs are due NLT COB Monday of the prior week. Tuesday is the normal GenAI.mil startup and planning day.** The named weekdays describe the normal battle rhythm; they do not invent approval or automatically advance the internal phase if the work is not actually complete.

## Weekly sequence

| When | What to do | Word guide |
| --- | --- | --- |
| Monday | All scheduling inputs due NLT COB | Human input deadline |
| Tuesday | Upload, reconcile, ask questions, identify checkrides/DVs, plan upgrades | **03 Gather products.docx — Tuesday: Ingest and plan** |
| Wednesday | Build the bulk of the schedule | **04 Review the draft.docx — Wednesday: Build the schedule** |
| Thursday | Scheduler QC plus fresh full Gemini review | **04 Review the draft.docx — Thursday: Full QC** |
| Thursday, optional | DO runs independent Terra/Grok challenge | **04 Review the draft.docx — Optional DO adversarial review** |
| Thursday | Schedule sell and capture DO directions | **05 Schedule sell.docx** |
| Thu–Fri | Apply directions, QC, formal buy and publication | **06 Correct QC buy and publish.docx** |
| Execution week | Reflow from published/current daily baselines | **07 Execution reflows.docx** |

## Current model assignment

For the normal scheduler workflow, select **Gemini 3.7 Flash** in GenAI.mil when available. Keep the main weekly scheduling conversation in Gemini through planning, build support, Thursday QC, sell support, corrections and execution reflows.

The optional DO adversarial review uses a separate conversation and is covered in the **Thursday — Optional DO adversarial review** section of **04 Review the draft.docx**. It is not part of the main scheduler flow.

If the named model is temporarily unavailable, the workflow and human authority boundaries still apply; record the displayed model/version rather than pretending Gemini was used.

## Create the weekly workspace

1. Copy **COPY THIS FOLDER FOR EACH NEW WEEK** beside itself. Rename the copy **Week of YYYY-MM-DD**, using the first date of the execution week. Use your approved local counting week.
2. Put existing source products in **Inputs**, schedule versions in **Schedules**, and reports, decisions and handoffs in **Working Record**. Keep filenames that identify the version. Preserve the presented, bought, published and signed daily schedules when they exist.
3. Open a new GenAI.mil conversation for this week using Gemini 3.7 Flash when available. Upload **System → UPLOAD THIS TO START.docx** and the current **Local Profile.docx**, **Stable References.docx**, **Playbook.docx** and needed source references from **Local Guidance**.

A normal fresh chat for a brand-new execution week does **not** need a handoff. Use **08 Hand off to another user.docx** only when the execution week already has recorded state and you are moving that ongoing week to another chat or user.

Do not copy the whole System folder into each week. These folders organize human work; the chat cannot see them unless you upload the files.

## Tuesday — activate the assistant

After uploading the available Monday inputs, paste this, replacing the brackets:

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

Then follow **03 Gather products.docx**, whose first heading is **Tuesday — Ingest and plan**. If this execution week is already underway and you are resuming its existing recorded state in a replacement chat, follow **08 Hand off to another user.docx** instead of declaring a fresh phase 1.

## Two terms you will use

**Active schedule:** the exact file you want reviewed. **Comparison baseline:** the exact older or approved schedule used to show changes. A proposed file can be active without being approved.

Use forms in **System → Blank Forms** only when useful. Ask the assistant to draft them, confirm the contents, and save completed copies in Working Record or Local Guidance. Unknown information stays Unknown.