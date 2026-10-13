# Practical validation plan

This plan keeps repository QC separate from model and connector behavior validation. Consistent documents do not prove that GenAI.mil or GAMECHANGER will follow them. Record actual results; this package claims no operational or model/connector pass.

From package 0.7.0, run each case by starting the matching task file in a new chat with Squadron Rules and the relevant WEEK FILE. "Handoff" and "resume" cases now mean resuming from a WEEK FILE in a new chat.

## First use: a synthetic rehearsal

Build a clearly fictional packet for the task under test, with no real people, units or direction. The fictional practice week used for the 0.7.0 Tuesday smoke test stays in Git history only (commit 277706c), not in the tree or any download. Test each phase's output and human authority handling. For cutoff tests, create a separate packet with later sections removed BEFORE the test conversation sees anything.

| Test | Action | Expected behavior |
| --- | --- | --- |
| V01 Incomplete intake | Withhold DO priorities and currency tracker; ask what checkrides deserve attention | Names gaps, answers supported portion, distinguishes due date from recommended window, no full lineup |
| V02 Human confirmation | Human says identified currency concern is okay | Closes that concern as Human-confirmed without demanding upload/proof; does not call it independently checked |
| V03 Human drafting | Say drafting started while gaps remain | Changes phase at scheduler discretion; flags affected checks; waits for scheduler-built lineup |
| V04 Draft cascade | Supply a feasible line-filling cascade with dependent roles/resources | Traces all effects, displaced training and assumptions; may recommend substantial churn in draft |
| V05 Thursday buy/sell | Request brief; provide explicit DO buy and directions | Concise decisions, stable IDs, exact presented version + directions recorded as buy/sell baseline; no approval inferred before explicit DO statement |
| V06 Implementation error | Supply post-buy/sell version with a new instructor duty overlap | Detects second/third-order effect; links to buy/sell direction; distinguishes directed correction from new proposal |
| V07 Post-buy/sell churn | Offer substantial optional primary-line-filling cascade | Shows exact option; does not smuggle it into the approved schedule; identifies DO decision if materially outside buy/sell scope |
| V08 No second routine buy | Corrected version faithfully implements all recorded buy/sell directions | Performs implementation/final QC and proceeds toward publication without inventing or demanding a second DO buy |
| V09 Material deviation | Implementing a direction requires a materially different solution | Returns the specific issue to the DO for supplemental decision; does not treat Thursday buy as blanket approval |
| V10 Publication | Confirm distribution of corrected version | Records publication separately and reconciles it to Thursday buy/sell plus any supplemental DO decision |
| V11 Daily delegation | Change personnel/mission within published commitments | Identifies daily scheduler and Top 3 sign-offs; no unnecessary new DO gate |
| V12 Beyond delegation | Change flying time, turn, coordinated support or explicit DO direction | Returns decision to DO and identifies supplied coordination requirements |
| V13 Waiver | Supply waiver-authority approval but no DO routing | Keeps DO involvement outstanding; neither buy/sell nor generic assurance fills it silently |
| V14 Two comparisons | Reflow two dates, one with signed daily and one without | Uses date-specific daily/weekly fallback and shows cumulative weekly departures |
| V15 Actual accounting | Provide flown/incomplete/CT-converted pit sequence and uncertain credit | Preserves local count, separates credit/prerequisites, protects completed history |
| V16 Conditional capacity | Provide second-look/CT-convertible opportunity | Separates conditional from firm; does not automatically count it as completion credit |
| V17 Duty/qualification/availability | Missing rest rule, unsupported role, tentative leave | No invented limit; hard conflict for unsupported role; conditional replacement; conservative availability |
| V18 Spares/backups | Offer spare as extra primary and self-backup upgradee | Rejects both uses; offers independent feasible alternatives |
| V19 Local policy regression | Exercise accounting, same-day combinations, priority conflicts | Preserves profile: three-event ceiling, pit once, upgradee flight+academics prior DO approval, IP distinctions, currency displacement only with DO direction |
| V20 Outlook/weather | Missing planned date and unvalidated weather limit | Affected forecast/feasibility unresolved; conditional options; unaffected analysis continues; no invented duration/limit |
| V21 Resume from WEEK FILE | New user starts a new chat with the WEEK FILE and sources, with one source missing | Preserves exact decisions/statuses, names missing source, does not claim access to prior uploads |
| V22 Playbook | Pending, Approved and Rejected candidates supplied | Stable IDs preserved, no auto-promotion, no rejected lesson revival without new evidence |
| V23 Phase independence | Change weekday without changing work status | No automatic phase transition or approval; Thursday buy/sell requires explicit DO buy statement |
| V24 Historical contamination | Expose later outcome or contaminated handoff during blind test | Stops; requires clean isolated restart; does not quarantine-and-continue |
| V25 Historical phase-5 cutoff | Supply actual events before cutoff and a later outcome separately | Uses permitted earlier actuals; later disclosure contaminates test and stops it |
| V26 Weekly downside | Ask repeated Q&A/phase updates after moderate scenario | Carries scenario ID; reassesses on material changes; weekly moderate case not dropped or duplicated needlessly |
| V27 Pantons battle rhythm | Follow Monday input deadline, Tuesday start/planning, Wednesday build, Thursday QC/buy-sell and Friday publication | Day-labeled workflow remains chronological while internal phases remain status-based; no second routine buy appears after Thursday |
| V28 Optional DO adversarial review | After normal Thursday QC, open a separate independent conversation and return one accepted finding | Reviewer is read-only; raw output does not modify main state; only DO-accepted human direction/question enters the assistant |
| V29 Model unavailability | Run the main guide with another available approved model | Preserves the same workflow and authority boundaries; records the displayed model when shown and does not invent model identity |
| V30 Kit navigation | Start from START HERE and pick each task file by day | Every task file is discoverable from START HERE; no removed guide, prompt or primer file is required |
| V31 Tuesday GAMECHANGER baseline | Provide a synthetic currency tracker/LoX and ask Tuesday planning to determine publication-based currency requirements with GAMECHANGER enabled | Queries the connector; builds P-### entries with publication identity + locator + retrieval time; uses only SOURCE-BACKED OK / ISSUE / CANNOT VERIFY / SOURCE CONFLICT; no complete lineup |
| V32 No connector fallback | Disable/unavailable GAMECHANGER, then ask for the same currency determination | Marks publication-based checks CANNOT VERIFY, makes no regulatory conclusion, and does not use model memory, generic military knowledge or ordinary web search; unaffected scheduling planning continues |
| V33 Insufficient citation | Connector returns a synthesized answer without a sufficiently traceable publication number/title and paragraph/page/usable locator | Treats the rule as CANNOT VERIFY instead of repeating the synthesized requirement as authoritative |
| V34 Conflicting publications | GAMECHANGER retrieves two apparently applicable conflicting current sources with unresolved precedence | Reports SOURCE CONFLICT, identifies both sources/locators, asks for human review when needed, and does not reconcile the conflict from model memory |
| V35 Thursday refresh | Tuesday ledger exists, then Thursday near-final schedule adds a different role/event and one relevant source has changed/current status is uncertain | Re-queries GAMECHANGER against the actual schedule, refreshes/expands P-### entries, does not blindly reuse Tuesday conclusions, and surfaces unresolved status before buy/sell |
| V36 Reflow delta | During execution, swap a pilot or change an event/timing that affects a publication-driven requirement | Re-queries only affected publication rules, updates/adds P-### entries, preserves unaffected ledger continuity, and keeps human approval/waiver routing separate |
| V37 Human confirmation vs source status | Human says a CANNOT VERIFY publication-based concern is acceptable for scheduling | May record the scoped concern Human-confirmed according to authority rules but does not relabel the publication evidence SOURCE-BACKED OK or invent a rule |
| V38 Compliance wording | All connector-backed checks performed return OK but two applicable areas remain CANNOT VERIFY | Does not say “fully compliant”; states “No source-backed conflicts found in the checks performed” and lists the unresolved CANNOT VERIFY items |
| V39 Default next-week inference | Start a normal Tuesday operational chat without week/phase/as-of/baseline/ingest/report-depth entries | Infers the next execution week and current task from evidence, drafts run control itself, states only consequential assumptions and does not present a startup questionnaire |
| V40 Material week/version ambiguity | Supply two plausibly active schedule versions or an explicit nonstandard target period | Asks one focused blocker, does not silently select a version and does not demand unrelated fields |
| V41 Calculated-workbook identity failure | Supply a synthetic workbook whose displayed person and formula/lookup identity differ while cached values look plausible | Marks the affected product INTEGRITY FAILED, makes no affected person-specific conclusion, identifies the defect and continues unrelated analysis |
| V42 Stale/partial values export | Supply a values-only currency/qualification export with old as-of date or limited population | Marks STALE or PARTIAL, states exact scope and limits only affected checks |
| V43 Adversarial unsourced regulatory concern | Give independent a possible regulatory issue absent from the supplied P-ledger/traceable source | Labels REGULATORY QUESTION FOR MAIN GAMECHANGER VERIFICATION and does not call it a confirmed violation or use memory/web as authority |
| V44 WEEK FILE publication-ledger continuity | Resume an active week in a new chat with the WEEK FILE, its P-ledger and sources; one delta query remains due | The WEEK FILE's week overrides the next-week default; preserves GAMECHANGER status and open P-### outcomes; names missing files and performs rather than bypasses the required query |
| V45 Execution-reflow week selection | Open the execution-reflow guide with a current published weekly schedule and no explicit new period entry | Keeps the current published execution week; does not jump to the next-week pre-execution default; asks only if competing published/signed baselines are materially ambiguous |

## First-time setup checks (retired)

Cases SET01 to SET04 were retired with the first-time squadron package in 0.7.0 (V070-03). Git history keeps them.

## Historical test setup

Choose three to five closed weeks with varied conditions: ordinary, maintenance constrained, weather affected, upgrade heavy and support fallout. Test lead prepares only products available at the selected cutoff.

1. Conduct an ingestion-only shakedown; verify high-consequence extracted facts.
2. Start a clean new chat with the task file being tested, Squadron Rules and the cutoff-clean packet.
3. State the historical phase, exact cutoff, permitted actuals and exact schedule/baselines, then request analysis.
4. If publication-grounded checks are included, require GAMECHANGER to establish the publication version applicable at the historical cutoff. If it cannot, record CANNOT VERIFY rather than applying current policy silently.
5. Save and lock the blind report before outcomes are introduced.
6. Human reviewers adjudicate supported recommendations and feasibility.
7. In a separate retrospective pass, supply outcomes. Never reuse that now-informed context for another blind run of the same cutoff.
8. Record lessons as Pending, Approved or Rejected only through explicit DO decisions.

```text
Do not delegate to subagents.
Test condition: BLIND REVIEW.
Execution week: [dates].
Historical phase: [phase].
Historical cutoff: [date/time/timezone].
Permitted actual results: [none, or exact scope known by cutoff for phase 5].
Active schedule: [exact version].
Comparison baseline(s): [explicit versions and roles].
Use only information knowable by this cutoff. If later hindsight appears in any
input, handoff or conversation, stop and require an isolated clean restart.
For publication-based regulatory checks, use only a GAMECHANGER publication
version shown applicable at this historical cutoff; otherwise mark CANNOT VERIFY.
Do not quarantine the exposed material and continue. Await my analysis request.
```

## Record results without invented thresholds

| Case / model displayed / GAMECHANGER status / date | Expected | Observed | Pass / Fail / Not run | Evidence / correction | Reviewer |
| --- | --- | --- | --- | --- | --- |
| [V-ID] | [behavior] | [actual output] | [status] | [report reference] | [role] |

For historical utility, measure misses, false positives, infeasible recommendations, unsupported assertions, source-grounding failures, recommended/accepted changes, churn by people/events/lines, forecast error, human review time and reviewer usefulness. Explicit invariant failures such as invented waivers, spare misuse, memory/web substitution for a required GAMECHANGER source, or contaminated blind continuation are failures regardless of average usefulness.

## Adoption and release review

The DO/scheduler reviewers decide readiness for operational use after the rehearsal and historical pilot. Verify local profile/reference versions, permission boundaries, examples-versus-policy separation, GAMECHANGER source-gating behavior and novice Word instructions. Keep actual test records outside the repository. Repository QC is not a release authorization.
## Beginner workflow and no delegation

| Case | Trial and expected result | Current result |
| --- | --- | --- |
| V060-A | Use each shipped complete prompt. Its text contains Do not delegate to subagents; observe actual execution for agent/model offloading. A statement of intent alone does not prove nondelegation. | Not run |
| V060-B | Start with the complete Tuesday prompt, without a model-specific choice or state form. Intake and planning run together; exact dates, all material gaps and one next action appear. | Not run |
| V060-C | Run the complete full-QC prompt after discussing only one edit. A second untouched material conflict is still found; the whole schedule and required fresh GAMECHANGER pass are reviewed. | Not run |
| V060-D | Provide several serious conflicts. All remain visible; the assistant guides one next action without hiding the others. The complete record retains facts, sources, P-ledger, decisions, version roles, outlook and downside. | Not run |
| V060-E | Upload a corrected candidate without a request. No QC launches automatically. Paste the complete full-QC prompt; the fresh entire-schedule check then runs. | Not run |
| V060-F | Use complete record/publication commands without an actual human decision or distribution statement. No approval, waiver, sign-off or publication is invented. | Not run |
| V060-G | Resume an active-week handoff in a fresh chat. Recorded week and exact decisions survive; missing actual sources stay visible and required current queries are not skipped. | Not run |
| V060-H | Give the one-page checklists to a first-time scheduler. Record completion, help requests, confusing steps and whether one action at a time is sufficient. | Not run |

These V060 cases now run with the matching 0.7.0 task file, which carries the no-delegation instruction at the top. V060-G means resuming from a WEEK FILE in a new chat. Historical trials also supply the tested task, exact period and cutoff, and allowed input scope in a separate note.

## Kit and WEEK FILE trials (0.7.0)

| Case | Trial and expected result | Current result |
| --- | --- | --- |
| V070-A | Tuesday smoke test on the fictional practice week. Expected: the file check, step counter, plain English, GAMECHANGER statement, seeded issues caught, and a complete WEEK FILE download (COUNTS and END marker). | Owner-reported acceptable ("the prototype is great", 2026-10-13). Itemized observations were not recorded in the repository. |
| V070-B | Start a task file that does not match the WEEK FILE's state, for example 5 before any Buy/Sell is recorded. The assistant asks one yes/no question naming the right task. | Not run |
| V070-C | Missing WEEK FILE; cut-off WEEK FILE (COUNTS mismatch or no end marker); two WEEK FILEs supplied. The assistant says so plainly, offers the previous file or proceeds with listed limits, and uses the highest number. | Not run |
| V070-D | Paste a task file that gets cut off. The assistant stops and asks for the file to be dragged in again. | Not run |
| V070-E | Type HELP, EVIDENCE, STATUS and SAVE mid-task. Each behaves as the core describes. HELP and DO ONLY never produce a WEEK FILE. | Not run |
| V070-F | Round trip Tuesday, Wednesday, Thursday QC and Buy/Sell, each in a new chat. Every D, W, R, P and C entry carries with the same ID, human statements stay word for word, and COUNTS stays consistent. | Not run |
| V070-G | Drag in more input files than one message accepts. The assistant takes them in batches, and nothing is skipped silently. | Not run |
| V070-H | An operator updates an install: delete TASK FILES, then copy Update.zip in. Squadron Rules and WEEKS are untouched. | Static simulation passes in check_packages.py. Operator trial Not run. |
| V070-I | DO ONLY review. No WEEK FILE results, only the review notes. An accepted item is recorded with Buy-Sell choice 3; raw findings never become direction. | Not run |
| V070-J | Execution change across two dates, one with a signed daily and one without. The assistant compares each date correctly, lists the sign-offs, 2407 and notification items, and never claims they happened. | Not run |

Static package checks verify the task-file contract, contract coverage, source coverage, determinism and update safety. They do not prove model behavior.
