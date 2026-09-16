# Fighter Squadron Scheduling Assistant

Download a ZIP, extract it into your scheduling location, and open **START HERE.docx**. The operator workflow is Word-first; schedulers do not need GitHub access inside GenAI.mil.

## Download the latest release

- **[Pantons setup ZIP](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest/download/Pantons_Setup.zip)** — approved Pantons local profile plus the complete kit.
- **[First-time squadron setup ZIP](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest/download/First_Time_Squadron_Setup.zip)** — complete kit with a blank local profile and guided setup questions.
- **[Update an existing setup](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest/download/Update_Existing_Setup.zip)** — use at the next-week boundary; follow UPDATE INSTRUCTIONS.docx. It preserves Local Guidance and weekly work.

You can also open the [latest release](https://github.com/joe-cole1/fs-scheduling-assistant/releases/latest) and choose a named ZIP under **Assets**. GitHub's automatic Source code downloads do not contain the built Word kit.

Right-click the downloaded ZIP, select **Extract All**, open the extracted folder, and open **START HERE.docx**. GenAI.mil itself needs no GitHub access. The release workflow publishes only after the operator ZIPs, manifest, checksums and release notes have been generated and verified, so a newly published release should already be complete.

Moving from the earlier Markdown kit? Use a full setup ZIP once and carry over approved Local Guidance and weekly work. Subsequent updates replace only **System** and **START HERE.docx** unless an explicit persistent migration requires human review.

## Pantons weekly battle rhythm

The operator manual follows the actual workday instead of making schedulers navigate by internal phase name:

1. **Monday — Inputs due.** All scheduling inputs are due NLT COB. Use **02 Monday - Inputs Due.docx**.
2. **Tuesday — Start the week.** Create the weekly folder/chat, upload startup/local/current products, and establish run controls with **03 Tuesday - Start the Week.docx**.
3. **Tuesday — Plan the week.** Reconcile gaps/conflicts, identify checkrides/evaluations and directed DV/senior-leader flyers, and plan upgrades/resources with **04 Tuesday - Plan the Week.docx**.
4. **Wednesday — Build.** Schedulers build the bulk of the weekly schedule while Gemini provides bounded support using **05 Wednesday - Build the Schedule.docx**.
5. **Thursday — Full QC.** Human scheduler QC is followed by a fresh whole-schedule Gemini review using **06 Thursday - Full Schedule QC.docx**.
6. **Thursday — Optional DO adversarial review.** The DO may independently challenge the schedule in a separate Terra or Grok conversation using **07 Thursday - DO Adversarial Review.docx**.
7. **Thursday — Schedule buy/sell.** Schedulers present the selected version and the DO makes the scheduling decision using **08 Thursday - Schedule Buy-Sell.docx**. **This is the formal DO buy event when the DO explicitly approves the schedule.**
8. **Thursday–Friday — Implement buy/sell directions.** Schedulers make the directed changes and Gemini verifies implementation/cascades using **09 Thursday-Friday - Apply Buy-Sell Changes.docx**. There is no routine second DO buy. A materially different solution outside the recorded direction returns to the DO.
9. **Friday — Final QC and publish.** Verify faithful implementation, resolve any required supplemental DO decision, and publish using **10 Friday - Final QC and Publish.docx**. Publication is a separate human action.
10. **Execution week — Reflows.** Analyze changes from the published weekly baseline and current signed daily schedules using **11 Execution Week - Reflows.docx**.

The five internal phases still follow actual work status. A calendar day does not automatically create phase advancement, approval or publication.

## What the Thursday buy/sell approves

The approved buy/sell baseline is the **exact presented schedule plus the explicit DO directions recorded during the Thursday meeting**. Post-buy/sell corrections are implementation of that decision, not a second approval cycle. Gemini checks whether the corrected file faithfully implements the directions and whether the changes create downstream conflicts.

If implementing a direction is infeasible or requires a materially different solution, that specific issue goes back to the DO for a supplemental decision. Every waiver still goes through the DO and the applicable waiver authority. Publication is recorded separately from approval.

## Other operator guides

- **12 Hand Off an Active Week.docx** — use only when an already-started week moves to another chat/user.
- **13 Update for Next Week.docx** — replace the reusable System safely at a week boundary.
- **14 Check the Setup.docx** — synthetic first-use checks and troubleshooting.

Use the trackers, calendars and schedules the squadron already maintains. Blank forms capture missing guidance and changes; they do not require retyping supplied products. Schedulers build and edit the schedule; humans approve and publish it.

Prefer one main Gemini conversation per execution week. The optional DO adversarial review is intentionally separate and never becomes an automatic second scheduler. A Word handoff plus the actual source files lets another user continue in a new chat. Shared-chat features, APIs, connectors and custom software are not required.

DOCX/package structure checks are separate from model behavior. **Operational GenAI.mil behavior still requires the documented rehearsal/pilot validation.** Use only systems and locations authorized for the material; actual operational data stays outside this repository.

## For maintainers

Read [AGENTS.md](AGENTS.md), [architecture](ARCHITECTURE.md), [approved design decisions](docs/v0.4/design-decisions.md), [the primer](docs/v0.4/system-primer.md), [validation plan](docs/v0.4/validation-plan.md), and [packaging instructions](packaging/README.md). Markdown is maintained source; release ZIPs are the operator product. Generated ZIPs are not stored in the repository tree.

To publish after a reviewed PR is merged, open **Actions → Publish release** and run it from `main`. Normally leave **Version** blank; the workflow increments the latest published stable release by `0.0.1` (for example, `0.5.3` becomes `0.5.4`). Enter a stable version without a leading `v` only when you deliberately want a different version. The workflow builds/tests first, generates release notes, creates or resumes a matching draft release, attaches and verifies all assets, then publishes the release as its final action. **Do not manually create/publish the normal release or move an existing tag.** Package updates are manual and normally adopted at the next scheduling-week boundary.

No open-source license has been selected. The owner decides licensing and public distribution.
