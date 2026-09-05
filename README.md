# Fighter Squadron Scheduling Assistant

**v0.4 — five-phase, human-led scheduling workflow.** The assistant consolidates evidence, answers planning questions, reviews scheduler-built schedules, recommends changes, and checks the result. Humans schedule, coordinate, approve, waive, and publish.

## Start here — no scheduling experience required

This is a set of instructions and forms to use in **ChatGPT Mil**. It is not scheduling software. You still build and edit the flying schedule in your normal squadron tools. The assistant helps you find missing information, decide what deserves a line, review your draft and catch mistakes after changes.

You do not need to understand the whole repository. Follow the steps below. Text in `[brackets]` is something you replace. If you do not know an answer, write `Unknown`; do not guess. A `.md` file is a plain-text document. On GitHub, open a file and use **Raw** to copy its text, or download it to upload into the chat. You can save assistant-produced Markdown using a plain-text editor with a `.md` filename.

**A baseline is simply the older schedule you want changes compared against.** An active schedule is the one being reviewed. A proposed change is not approved just because the assistant recommends it. In this guide, “sell” means the DO review meeting; “buy” means formal DO approval AFTER corrections and QC.

### 0. Set up the chat once for the execution week

1. Open a new ChatGPT Mil conversation. Name it for the week you will fly, for example `Scheduling — week of [date]`.
2. Open the [system primer](docs/v0.4/system-primer.md). Copy everything between **START OF PRIMER** and **END OF PRIMER** and paste it into the chat.
3. Upload the [Pantons local profile](local-profiles/pantons-v0.4.md), the latest approved squadron playbook if one exists, and available local rules/references. Another squadron must use its own approved local rules rather than adopt Pantons rules by accident.
4. Paste this setup message. Then upload your available products; you do not have to wait until everything is collected.

```text
We are using Scheduling Analysis System v0.4.
Execution week: [Sunday date] through [Saturday date].
Local timezone: [timezone].
As of: [date and time].
Test condition: OPERATIONAL.
Current phase: 1 — Product gathering.
Ingest gate: CONFLICTS ONLY.
Report depth: BRIEF.

I will upload available products. Help me draft the run control and product
manifest from those uploads; do not make me transcribe information already there.
List missing products and their effect. Do not start a full schedule review
until I request it, but answer planning questions when I ask them.
Do not create a complete initial lineup. Schedulers will do that.
```

Use the [run-control form](templates/v0.4/01_run_control_and_manifest.md) if helpful; the assistant can fill a draft from your inputs. You confirm the result. If this is a historical test, **do not use the OPERATIONAL setup unchanged**; follow [historical test instructions](docs/v0.4/validation-plan.md#historical-test-setup).

### 1. Gather products and ask planning questions

**Usually Monday–Tuesday before the execution week.** Get the products your squadron already uses. Excel, PDFs, readable screenshots, calendar exports and plain-text notes are acceptable. You do not need to reformat everything into our forms.

| Get this input | What it tells the assistant |
| --- | --- |
| Upgrade/MQT tracker | Who needs which event next, prerequisites, planned completion and recent results |
| Checkride/currency tracker | What is due and when |
| Leave and commitments, including known upcoming TDYs | Who is available, exact unavailable times, and future scheduling windows |
| Current dated Letter of Xs and roster | Who is qualified for each role and callsign/name matching |
| Maintenance turn, configuration and spare plan | How many primary aircraft can fly each go, in which configuration |
| Simulator schedule | Available devices, slots and assigned events |
| Range, airspace, tanker and other support allocations | Which missions have the support they require |
| Weather forecast, when available | Forecast timing and risks; early forecasts may be provisional |
| Training phase/configuration plan | Mission emphasis and upcoming configuration transitions |
| DO guidance and Flt CC inputs | Priorities, pairings, workload recommendations and new restrictions |
| Stable rules and approved playbook | Syllabus sequences/ratios, rest/duty rules, brief/debrief windows and validated weather rules |
| Prior-week schedule/actual duty times, if available | Rest and duty checks at the start of the execution week |

No draft exists yet? That is normal. Missing a product? Tell the assistant. It will explain the limitation and continue the work it can do. Use [DO guidance](templates/v0.4/02_do_weekly_guidance.md) and [Flt CC input](templates/v0.4/03_flight_commander_input.md) only for direction and information not already captured elsewhere.

```text
Phase 1 — Product gathering.
I have uploaded the products currently available.
Consolidate the inputs and tell me what is missing or conflicting.
Explain which planning questions or checks are limited by each gap.
Identify likely priority events and instructor/resource constraints from evidence.
If leadership guidance is missing, draft questions or proposed guidance for human
confirmation. Do not invent priorities or treat proposed guidance as issued.
```

Ask questions whenever useful:

```text
Which checkrides should we prioritize this week? Consider actual due dates,
upcoming leave/TDY, prerequisites, available instructors and resources, and DO
guidance. Distinguish the due date from a recommended earlier scheduling window.
Cite the facts that support your recommendation and flag missing information.
```

**You should get:** an input/gap list, useful planning answers and clearly marked proposed guidance. **Move on when the scheduler decides to start drafting.** A missing product does not automatically stop drafting.

### 2. Build your draft, then have it reviewed

**Usually Wednesday–Thursday.** Build the initial lineup yourself using the squadron's normal schedule. Upload:

- Your draft, with a clear filename/version and exact event/go times.
- Any updated products from phase 1.
- An earlier draft if you want a comparison. For the first draft, say there is no comparison baseline.

```text
Phase 2 — Initial draft. Begin review.
Active schedule: [exact filename and version].
Comparison baseline: [exact earlier filename/version, or NONE — first draft].
As of: [date/time/timezone].
Use DETAILED output and CONFLICTS ONLY ingestion.

Review the scheduler-built draft. Find hard conflicts, approval needs, upgrade
risks, unused feasible primary lines and worthwhile training opportunities.
Recommend exact changes and alternatives. Fully check every downstream effect
of a cascade, including displaced training, before calling it feasible.
Include the 30-day outlook and one moderate downside case for this week.
Do not modify the schedule or imply that a recommendation is approved.
```

**You should get:** ranked changes with evidence, feasibility checks, tradeoffs and decisions needed. Humans edit the source schedule. If you upload a revised draft, identify it as the new active version. **Move on when the humans choose the version to present at the sell.**

### 3. Prepare for the sell and record DO directions

**Usually Thursday.** Upload:

- The exact draft that will be presented.
- The latest guidance, unresolved findings and any revised resource/personnel products.

```text
Phase 3 — Schedule sell.
Presented schedule: [exact filename/version].
Prepare a BRIEF decision package for the DO: feasibility and limits, priority
checkrides/upgrades, progress and 30-day risk, primary-line use, resource and IP
constraints, tradeoffs, unresolved issues and exact decisions needed.
For each decision, give the recommendation, alternatives and consequences.
This meeting records DO direction; it is not yet formal DO buy.
```

After the meeting, paste the actual directions:

```text
The sell is complete. Here are the DO's directions: [paste actual directions].
Record each direction with a stable weekly decision ID and exact scope.
Begin phase 4. Switch to FINAL QC behavior, and keep any new proposals separate
from directed corrections. Schedulers will incorporate the changes.
```

**You should get:** a decision brief and a list of DO-directed corrections. **Next:** schedulers apply those directions to the schedule. Do not describe the meeting as formal approval of an uncorrected version.

### 4. Correct, QC, obtain DO buy, then publish

**Usually Thursday–Friday.** Upload:

- The corrected schedule, with its new version.
- The sell-presented schedule and DO directions/decision record.
- Updated products or human confirmations relevant to the corrections.

```text
Phase 4 — Corrections and final QC.
Corrected active schedule: [exact filename/version].
Sell-presented baseline: [exact filename/version].
Previous corrected version, if any: [filename/version or NONE].
DO directions: [decision-record filename or refer to recorded directions].

Verify the disposition of EVERY sell decision. Find implementation mistakes and
unintended second- and third-order effects, then check the complete corrected
schedule for conflicts. Keep new proposed changes separate from corrections.
Flag hard infeasibility and major upgrade risk. Show substantial additional
cascades as DO decision options rather than reopening routine optimization.
List remaining issues and recognize explicit human confirmations as closures.
Do not infer waivers, DO approval or publication.
```

**Before presenting the final version to the DO:** check that each sell direction has a disposition, correction QC is complete or its limits are visible, and waiver items have gone through the DO and applicable authority. Humans resolve findings; a clear human confirmation can close the stated concern without another upload.

Only after it actually happens, record the buy:

```text
The DO formally buys [exact corrected schedule filename/version].
DO approval: [actual statement/record and date/time, as available].
Record this exact version as the bought weekly schedule. Do not record it as
published yet unless I separately confirm distribution.
```

After a human distributes the schedule, normally Friday:

```text
Publication confirmed: [exact filename/version] was distributed on [date/time]
for the execution week [dates]. Record it as the published weekly schedule and
the cumulative weekly baseline. Identify any difference from the bought version
and its recorded human disposition; do not silently assume they match.
```

**You should get:** a correction/QC record and separate entries for formal buy and publication. The assistant does not send the schedule to Wing, OG, Maintenance or anyone else.

### 5. Reflow during execution

Upload:

- The published weekly schedule.
- The latest signed daily schedule for each affected day, if one exists.
- Actual results so far and changed personnel, maintenance, support or weather facts.
- Relevant updated trackers, commitments and approval records.

Use the [execution update form](templates/v0.4/07_execution_update.md) if useful, or upload existing logs and describe only what changed.

```text
Phase 5 — Execution reflow. Test condition: OPERATIONAL.
As of: [date/time/timezone].
Published weekly baseline: [exact filename/version].
Latest signed daily schedule(s): [date: filename/version; or NONE for that day].
Changed facts and actual results: [describe or identify uploaded sources].
Question: [what needs to be recovered or changed].

Separate completed results, remaining firm events and conditional opportunities.
Protect completed events; do not infer a pass or credit just because an event flew.
Recommend a fully checked reflow and update downstream upgrade effects.
Show immediate changes against each day's latest signed daily schedule, using
the published weekly schedule if no signed daily exists. Also show cumulative
departures from the published weekly schedule.
Identify daily scheduler/Top 3 sign-offs, DO decisions and waiver/coordination
requirements. Keep proposals separate from approved daily schedules.
```

Feasible personnel and mission changes within published times, turn pattern, coordinated support and DO guidance use daily scheduler and Top 3 sign-off. Changes outside those boundaries return to the DO. **Every waiver goes through the DO and the applicable waiver authority.** After humans sign a daily revision, tell the assistant its exact version so it can become that day's immediate baseline.

### Changing users or finishing a session

```text
Draft a concise current-state Markdown handoff using the v0.4 handoff template.
Include current phase/as-of, exact schedule and baseline versions, current source
files to transfer, DO decisions, human confirmations, sell/QC dispositions,
waiver status, completed results, open issues, playbook candidate statuses and
the next action. Preserve attribution and scope. Do not include superseded
discussion as current direction. State the test condition and historical cutoff.
```

Save the result as a `.md` file and pass it **with the current source products** to the next user through an authorized location. Keep the full transcript separately if needed. The next user pastes the primer, uploads the local profile, handoff and source products, then sends:

```text
Resume this execution week's work from the attached handoff and source products.
Reconcile the versions, flag missing files or conflicting state, and preserve
recorded human decisions. Tell me the current phase and next action. Do not
assume you can access uploads or conversation history from the previous user.
```

**If something is unclear:** say so. The assistant should ask one genuinely blocking question at a time and continue unaffected work. If it reports a wrong fact, correct that fact explicitly. If a human has checked a flagged concern and says it is okay, state that confirmation and the concern it closes.

No API, connector, custom application, autonomous agent, or particular model is required. Shared-chat support and native export availability in ChatGPT Mil are unverified and are not prerequisites.

## Weekly cycle

“Prior week” is the week immediately before execution. Weekdays describe normal timing, not automatic phase changes.

| Phase | Normal timing | Outcome |
| --- | --- | --- |
| 1. Product gathering and generation | Mon–Tue, prior week | Consolidated products, gaps, proposed guidance, planning Q&A |
| 2. Initial draft | Wed–Thu, prior week | Scheduler-built lineup and evidence-backed review |
| 3. Schedule sell | Thu, prior week | DO review and recorded directions; not yet formal buy |
| 4. Corrections, final QC, approval, publication | Thu–Fri, prior week | Corrections → QC → formal DO buy → Friday publication for the following week |
| 5. Execution reflows | Execution week | Approved daily changes with immediate and cumulative comparisons |

## Products

| Product | Contributor | Use |
| --- | --- | --- |
| [01 Run control and manifest](templates/v0.4/01_run_control_and_manifest.md) | Scheduler | Current phase, version roles, cutoff, products and gaps |
| [02 DO guidance](templates/v0.4/02_do_weekly_guidance.md) | DO; assistant may draft | Weekly intent, cadence, pairings, CT priorities |
| [03 Flight Commander input](templates/v0.4/03_flight_commander_input.md) | Flt CC | New personnel effects, recommendations and discrepancies |
| [04 Stable references](templates/v0.4/04_stable_local_rules_and_references.md) | Local designated owners | Source-backed local parameters, not weekly notes |
| [05 Retrospective outcomes](templates/v0.4/05_retrospective_outcomes.md) | Test lead and reviewers | Outcomes after a locked historical blind report |
| [06 Decision and release record](templates/v0.4/06_decision_and_release_record.md) | Scheduler records human decisions | Sell dispositions, waivers, buy, publication and daily approvals |
| [07 Execution update](templates/v0.4/07_execution_update.md) | Daily scheduler / Top 3 / source owners | Changed facts and outcomes during live execution |
| [08 Session handoff](templates/v0.4/08_session_handoff.md) | Outgoing user, assisted | Current state for a new user/conversation |
| [09 Playbook](templates/v0.4/09_playbook.md) | DO-approved local owner | Approved lessons plus Pending/Approved/Rejected ledger |

Use existing schedules, trackers, leave/commitment products, maintenance plans, qualification matrices, simulator and support schedules. Forms capture missing direction and changes, not another transcription of those products. Assistant-generated forms and guidance require human confirmation before being treated as issued direction.

## Review and adoption

- Contributors: read [AGENTS.md](AGENTS.md) for working instructions and [ARCHITECTURE.md](ARCHITECTURE.md) for the system map.
- [Report contracts](docs/v0.4/report-contracts.md)
- [Approved design decisions](docs/v0.4/design-decisions.md)
- [Policy preservation crosswalk](docs/v0.4/policy-crosswalk.md)
- [Validation plan](docs/v0.4/validation-plan.md) and [repository QC record](docs/v0.4/repository-qc.md)
- [Synthetic five-phase walkthrough](examples/v0.4/SYNTHETIC_weekly_cycle.md)
- [Synthetic leadership inputs](examples/v0.4/SYNTHETIC_leadership_inputs.md)
- [Change log](CHANGELOG.md) and [v0.3 provenance](archive/v0.3/README.md)

The repository contains instructions, blank forms, and synthetic examples. Keep real weekly packets and generated operational reports outside this repository, including while it is private. See [data handling](docs/data-handling.md). No open-source license is selected by this change; the owner decides licensing before broader distribution.
