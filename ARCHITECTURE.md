# Architecture - Panton Scheduling Assistant

This is a map of how the kit is built and how it works. It is not a second source of scheduling policy. Operators start with [README.md](README.md); contributors also follow [AGENTS.md](AGENTS.md). Approved decisions are in [design decisions](docs/design-decisions.md); exact local rules are in the [Pantons profile](local-profiles/pantons.md).

## System boundary

The product is a set of instruction files and Word documents for a human-led workflow in GenAI.mil. It is not a scheduling application, optimizer or database. There is no server, API, autonomous agent, custom code or shared chat. The assistant works only on uploaded files, the conversation and explicitly enabled platform capabilities. Humans maintain the actual schedule and products in their existing tools.

**Publication-grounded regulatory QC is a bounded connector exception.** When DoW Policies Beta (GAMECHANGER) is available, it is the only AI-side source for publication-derived determinations. That covers currency, qualification, crew rest and duty, evaluation, syllabus and prerequisite, event credit, recurring training and similar requirements. If it is unavailable or returns nothing traceable, those checks fail closed as CANNOT VERIFY while all other scheduling analysis continues. Model memory and ordinary web search are never fallback authorities.

## Components

| Component | Location | Responsibility |
| --- | --- | --- |
| Shared task-file core | `packaging/kit/core.md` | Role, plain-English step-by-step talk style, first-reply file check, week and version selection, and every authority, evidence, GAMECHANGER, scheduling, outlook, playbook and blind-test rule |
| Task scripts | `packaging/kit/tasks/` | One step-by-step script per task: Tuesday plan, Wednesday draft check, Thursday full QC, Buy/Sell, changes and publication, execution changes, DO-only review, help |
| WEEK FILE format | `packaging/kit/week-file.md` | The saved state carried between chats, with stable IDs, a COUNTS line and an end marker |
| Squadron Rules | `packaging/kit/squadron-rules.md` + `local-profiles/pantons.md` | Approved Pantons rules (Section 1), local reference index (Section 2), DO-approved lessons (Section 3) |
| Operator documents | `packaging/kit/start-here.md`, `packaging/kit/input-checklist.md` | One-page START HERE and the weekly input checklist |
| Build and checks | `scripts/build_packages.py`, `scripts/check_packages.py`, `tests/` | Deterministic packages; task-file contract, contract coverage, operator jargon, update safety |
| Release | `.github/workflows/release-packages.yml`, `scripts/release_packages.py`, `scripts/prepare_release.py` | Draft-first immutable release publication |
| Governance | `docs/design-decisions.md`, `docs/policy-crosswalk.md`, `CHANGELOG.md` | Approved design, contract preservation and change history |
| Validation | `docs/validation-plan.md`, `docs/repository-qc.md` | Behavior cases and the record of checks actually performed |

Each task file is self-contained: the no-delegation guard, a header, the shared core, its task script, the WEEK FILE format and an end marker. Operators never upload a separate primer.

## How a task runs

1. The operator opens a new chat, turns on DoW Policies, and drags in the task file, Squadron Rules and the newest WEEK FILE.
2. The assistant's first reply is a file check:
   - the files it actually read, and any missing, unreadable or cut off
   - whether GAMECHANGER is available
   - the inferred execution week, and why
3. The assistant runs the task's numbered steps. Every reply ends with one physical next action and the exact short reply to type, and every material issue stays visible. HELP, EVIDENCE, STATUS and SAVE work at any time.
4. The assistant hands back the next WEEK FILE as a download (or one copy block). The operator saves it in the week's folder under the name given.

Guards: the end markers detect a cut-off task file or WEEK FILE, and the WEEK FILE's NEXT TASK detects a task run out of order.

## Internal state

The assistant tracks three independent things in the WEEK FILE. The day of the week never changes any of them by itself.

| Dimension | Values | Key distinction |
| --- | --- | --- |
| Work status | 1 PRODUCT GATHERING; 2 INITIAL DRAFT; 3 SCHEDULE BUY/SELL; 4 POST-BUY/SELL IMPLEMENTATION / FINAL QC / PUBLICATION; 5 EXECUTION REFLOWS | Changes only with what humans actually do |
| Schedule and decision state | Working draft, presented, bought, corrected, published, signed daily, proposal | A work status never confers approval on a version |
| Test condition | OPERATIONAL, BLIND REVIEW, RETROSPECTIVE | Hindsight is prohibited in a blind test whatever the work status |

The WEEK FILE uses these identifiers:

| Identifier | What it tracks |
| --- | --- |
| D-### | decisions |
| W-### | waivers |
| R-### | findings and recommendations |
| P-### | regulation checks |
| F-### | key facts |
| S-### | downside scenario |
| E-### | events |
| X-### | changed facts |
| C-### | playbook candidates |

They are human-readable cross-references, not database keys.

## Versions and comparisons

| Use | Comparison or authority |
| --- | --- |
| Initial draft review | Human-selected earlier draft, or None for the first draft |
| Thursday Buy/Sell | Exact presented version plus the DO's explicit buy statement and D-### directions |
| After Buy/Sell | Buy/Sell presented version (cumulative); previous corrected version (incremental) |
| Publication | Exact distributed version reconciled to the Buy/Sell version and any supplemental DO decisions |
| Execution, immediate | Latest signed daily for each affected date; published weekly if none |
| Execution, cumulative | Published weekly schedule |

## Authority

**Thursday Buy/Sell is the formal DO buy, and only when the DO explicitly approves.** Schedulers then carry out the recorded directions and the assistant checks them. There is no routine second buy. A materially different solution returns to the DO for a supplemental decision. Publication is a separate human action.

During execution, the daily scheduler and Top 3 sign off on feasible changes within published times, turn pattern, coordinated support and DO guidance. Anything beyond that goes to the DO. Every waiver goes through the DO and the applicable waiver authority. GAMECHANGER output is evidence only.

## Continuity and historical testing

There is a new chat for every task, and the WEEK FILE is the continuity record. Shared chats, cross-chat memory and access to another user's uploads are not assumed. Each week has its own folder holding Inputs, Schedules and its WEEK FILEs, so anyone taking over needs only that folder. A regulation-check ledger carried in the WEEK FILE is continuity, never a substitute for a required current query.

A blind review starts only when a test lead states the period, task, cutoff and allowed inputs. Exposure to hindsight requires a clean restart in a new chat. Regulation checks must use the publication version applicable at the cutoff, or CANNOT VERIFY.

## Distribution

`Panton_Scheduling_Assistant.zip` contains:

```
Panton Scheduling Assistant/
  START HERE.docx
  TASK FILES/        8 task files
  Squadron Rules.docx
  WEEKS/_COPY ME - New week/
    INPUT CHECKLIST.docx
    Inputs/
    Schedules/
```

`Update.zip` contains only TASK FILES and START HERE, plus a read-me with reference copies when a release declares a Squadron Rules, input-checklist or weekly-folder migration. Operators delete TASK FILES and copy the update in, so Squadron Rules and weekly work are never touched by construction.

Releases are draft-first transactions owned by **Actions → Publish release**, with `packaging/version.txt` as the reviewed identity. Generated downloads live in GitHub Releases, outside the repository tree.
