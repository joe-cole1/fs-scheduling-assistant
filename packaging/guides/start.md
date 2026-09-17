# START HERE

Open this folder in Windows File Explorer. You will use Word documents and GenAI.mil. You do not need GitHub access inside the chat.

1. Keep this extracted folder in your squadron's approved scheduling location.
2. Open **System → Instructions → 01 First time setup.docx** once for the squadron.
3. Then use the Word guide for the day or step you are on.

## Weekly guide

- **Monday:** 02 Monday - Inputs Due.docx
- **Tuesday, first:** 03 Tuesday - Start the Week.docx
- **Tuesday, then:** 04 Tuesday - Plan the Week.docx
- **Wednesday build and integration review:** 05 Wednesday - Build the Schedule.docx
- **Thursday QC:** 06 Thursday - Full Schedule QC.docx
- **Optional DO-only challenge:** 07 Thursday - DO Adversarial Review.docx
- **Thursday approval meeting:** 08 Thursday - Schedule Buy-Sell.docx
- **After the Buy/Sell:** 09 Thursday-Friday - Apply Buy-Sell Changes.docx
- **Friday:** 10 Friday - Final QC and Publish.docx
- **Execution-week changes:** 11 Execution Week - Reflows.docx
- **Changing users/chats during an active week:** 12 Hand Off an Active Week.docx
- **Installing next week's update:** 13 Update for Next Week.docx
- **Testing/troubleshooting:** 14 Check the Setup.docx

## Normal startup behavior

For normal **pre-execution** weekly scheduling work (Monday through Friday planning, build, QC, Buy/Sell and publication support), the assistant defaults to the **next execution week** unless a human selects another period. Execution-week reflows use the current published execution week, and an active-week handoff keeps its recorded week. The assistant infers the exact dates, timezone, current workflow step, active schedule, baselines, source status and connector availability from the current date, folder/file names, schedule headers, uploaded products and conversation.

Do not fill out a startup questionnaire. The assistant drafts the run-control record and product manifest. Correct an inference when it is wrong. The assistant should ask only when an unresolved ambiguity would materially change the analysis, especially when more than one schedule version could be active or authoritative.

**The DO buys the schedule during Thursday's Buy/Sell.** Wednesday's cross-functional meeting is the **Cross-Functional Schedule Integration Review** and is not an approval event. Post-Buy/Sell corrections implement the approved direction and receive QC; there is no routine second DO buy. A material solution outside the recorded Buy/Sell direction returns to the DO.

The assistant helps; humans build, edit, approve and publish the schedule. A model recommendation is never an approval. Every waiver still goes through the DO and the applicable waiver authority.

Keep squadron guidance in **Local Guidance**. Keep each week's inputs, schedules and working record in that week's folder. **System** contains replaceable instructions and blank forms. Never save completed work inside System.

The package number in each generated document header identifies the installed System release. Most prompts now infer the week and state. Enter only decisions, changed facts or task-specific information that the assistant cannot derive from supplied products.
