# Panton Scheduling Assistant

Kit version 0.8.0

An AI scheduling partner for the Pantons (35th Fighter Squadron) weekly flying schedule. It runs in GenAI.mil using ordinary file uploads. People build, approve and publish the schedule; the assistant checks and advises.

Everything you need is in this one folder. There is nothing to install.

## Get it

1. Click the green **Code** button near the top of this page, then **Download ZIP**.
2. Right-click the downloaded file and choose **Extract All**.
3. Put the extracted folder in your approved scheduling location. Rename it **Panton Scheduling Assistant** if you like.
4. Open **START HERE.docx**.

## What is in the folder

| File or folder | What it is for |
| --- | --- |
| START HERE.docx | One page: the 4 moves, which task file to use on which day, and how to update. |
| TASK FILES | One file per task. You drag the one for today's task into the chat. |
| Squadron Rules.docx | The squadron's own rules, one per line. It is yours to keep and edit; the DO approves every rule. |
| WEEKS | Copy **_COPY ME - New week** each Monday. Its INPUT CHECKLIST says which products to collect. |
| REFERENCE | The squadron Scheduling SOP and the weekly QC and Buy-Sell checklist, for people to read. |

The REFERENCE documents are dated 17 Sept 2026. In a few places they still describe a working record and a handoff record that this kit no longer uses.

## Every task: the same 4 moves

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
| Any time, DO or a senior scheduler | RULES - Add or change squadron rules |
| Not sure | HELP - What do I do next |

The WEEK FILE carries the week's decisions, schedule versions, findings and regulation checks from one chat to the next. Anyone who picks up the week needs only the week folder.

## Squadron rules

**Squadron Rules.docx** holds one rule per line, each with an ID and how strict it is, grouped by category. A rule gets written down three ways:

- The **RULES** task file asks questions and hands back lines ready to paste.
- When someone corrects the assistant during a weekly task, it uses the correction that week and saves it in the WEEK FILE as a proposed rule.
- A person adds a line by hand.

Proposed rules sit in their own part of the file and are not applied until the DO approves them. The assistant never edits Squadron Rules and never suggests what a rule should say.

## Updating

1. Download and extract the kit again, **somewhere else**. Never extract it on top of your working folder.
2. In your working folder, delete **TASK FILES**. Copy in the new **TASK FILES** folder and the new **START HERE.docx**.
3. Keep your own **Squadron Rules.docx** and your **WEEKS** folder. Read "What changed" below; it says when Squadron Rules needs your attention.

Finish an active week with the task files you started it on.

## What changed in 0.8.0

- **Simpler download.** The kit is now this one folder. There are no separate release downloads or update packages.
- **Squadron Rules has a new layout:** one rule per line, each with an ID and how strict it is, grouped by category. No approved rule changed its wording.
- **New task file, RULES - Add or change squadron rules,** for the DO or a senior scheduler. It asks questions, writes each answer as one rule line and hands back lines to paste into Squadron Rules.
- **Tell the assistant when it misses something everyone knows.** It uses the correction that week and saves it in the WEEK FILE as a proposed rule for the DO.
- **A DO-approved squadron rule is enforced even when no regulation lookup is available.** The assistant calls it a squadron rule, never a regulation result. Regulation checks still run, and a squadron rule that seems to go against a regulation is flagged for the DO.
- **Every first reply now says how many rules it read,** so a broken or cut-off Squadron Rules shows up.

**If you already use an earlier kit, your Squadron Rules needs one step:**

- If nobody edited your Squadron Rules: rename the old file (for example Squadron Rules - old), then copy in the new **Squadron Rules.docx**. Have the DO confirm it.
- If your squadron did edit it: adopt the new file the same way, then add each of your own edits as a rule line in the right category. The RULES task file can walk you through it. Have the DO confirm the merged file.
- Part 1 of the new file holds the same approved rules as before. Part 2 holds proposals copied from the squadron SOP and two rules stated from experience. Nothing in Part 2 applies until the DO approves it and someone moves it into Part 1.
- The change-form triggers and the steps after a signed schedule changes moved out of the execution-week task file into Squadron Rules (lines PRI-08 and PRI-09).
- The new task files still work with an old Squadron Rules; the first reply tells you when it sees one.

These task files have not yet been tried in GenAI.mil.

## Approval and evidence

Humans create and edit schedules, coordinate, approve and publish.

- **Thursday Buy/Sell is the formal DO buy, and only when the DO explicitly approves.** The exact presented schedule plus the recorded directions is the approved version.
- **Carrying out those directions faithfully needs no routine second buy.** A materially different solution goes back to the DO.
- **Publication is a separate human action.** Every waiver needs the DO and the applicable waiver authority.

Regulation checks (currency, qualification, crew rest and duty, evaluations, syllabus and others) must come from traceable **DoW Policies Beta (GAMECHANGER)** publications. When the evidence is missing, the assistant says it couldn't confirm the item and a person checks it. When publications disagree, a person decides. The assistant's memory and ordinary web search never fill the gap.

No assistant output certifies full compliance or grants approval.

## Use it responsibly

Use only systems and locations authorized for your material. Keep real schedules, personnel data and saved WEEK FILEs in your approved scheduling location, never on GitHub.

## For maintainers

Every file here is generated. Do not edit files in this repository by hand: change the sources in the private maintainer repository and rebuild.
