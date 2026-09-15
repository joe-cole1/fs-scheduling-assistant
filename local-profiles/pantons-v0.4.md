# Pantons local scheduling profile — v0.4

Scope: Pantons F-16 Scheduling Analysis System. These are the approved scheduling decisions retained for v0.4, together with explicitly approved workflow authority changes. They are not universal USAF rules. Another squadron must replace this profile with its own approved local guidance. No numerical crew-rest, duty, syllabus ratio, or mission-weather limits are supplied here.

## Authority and priorities

- Advisory assistant only. Humans create and modify schedules, coordinate, approve and publish. **The DO formally buys the weekly schedule during Thursday's buy/sell when the DO explicitly approves it.** The approved baseline is the exact presented schedule plus the DO directions recorded in that meeting. Schedulers implement those directions and the assistant QC's implementation. There is no routine second DO buy. A materially different solution outside the recorded direction returns to the DO for a supplemental decision. Publication is a separate human action.
- Within published flying times, aircraft turn pattern, coordinated support and explicit DO guidance, the daily scheduler and Top 3 sign off on feasible daily personnel/mission changes. Changes outside these boundaries return to the DO. Times are normally stable, not absolutely immutable.
- Every waiver goes through the DO as well as the applicable waiver authority. A buy/sell, generic approval or human confirmation is not a blanket waiver.
- Human confirmation is sufficient to close the specific concern; record it without demanding supporting uploads. Preserve the distinction between human-confirmed and independently checked.
- Fixed commitments first, then evaluations/checkrides, then upgrades already assessed at risk. Resolve remaining contention using weekly DO priority notes. Currency may displace an upgrade only with DO direction. Use useful CT/currency to fill remaining feasible primary lines.
- Weekly DO notes can explicitly override standing preferences, apply only to the target week and expire afterward. They cannot silently override a hard constraint. Raise conflicts.

## Weekly battle rhythm and model roles

- **Monday:** all scheduling inputs are due NLT COB. This is the human input deadline; the assistant does not infer completeness merely because Monday ended.
- **Tuesday:** schedulers create the weekly GenAI.mil workspace, upload startup/local/current inputs, then perform product reconciliation and planning Q&A: material gaps/conflicts, checkrides/evaluations, explicitly directed DV or senior-leader flyers, active upgrades, next legal events, prerequisites, candidate windows and major instructor/resource constraints. Do not build the complete weekly lineup.
- **Wednesday:** schedulers build the bulk of the weekly schedule. The assistant provides bounded planning support, conflict checks and cascade analysis while humans construct the source schedule.
- **Thursday:** schedulers conduct QC and the main assistant performs a fresh full-schedule review. The DO may optionally run a separate adversarial review. Then the **buy/sell** occurs. If the DO explicitly buys the schedule, the presented version plus recorded DO directions becomes the approved buy/sell baseline. Schedulers implement those directions and the assistant checks second/third-order effects. No routine second buy follows. Material deviations return to the DO.
- **Friday:** after faithful implementation/final QC, humans publish the schedule. Publication is recorded separately from Thursday approval.
- **Execution week:** reflows start from the published weekly baseline and each affected day's latest signed daily schedule when available.
- The named weekdays define the normal Pantons battle rhythm. Work status still controls the internal phase. A holiday, delayed input, reopened draft or late correction does not create approval or automatically advance the phase merely because the calendar changed.
- Use **Gemini 3.7 Flash** as the normal scheduler model in GenAI.mil when available. Keep the main weekly scheduler workflow in Gemini through planning, build support, Thursday QC, buy/sell support, implementation QC, publication support and execution reflows.
- The optional DO adversarial review uses a **separate GPT-5.6 Terra or Grok Expert 4.5 conversation**. It is read-only and not a prerequisite for buy/sell. Raw reviewer output never becomes scheduler direction automatically. Only a finding the DO accepts returns to the main Gemini workflow as explicit human DO direction or a DO question.
- Model choice does not change human authority, qualification evidence, waiver routing, buy/sell approval or publication requirements.

## Upgrade accounting and flow

- The countable-event week is Sunday through Saturday.
- Normal ceiling: three countable upgrade events per week. More requires DO approval.
- Each simulator, non-pit upgrade flight and evaluation/checkride counts. Count an entire continuous hot-pit sequence as one event regardless of missions, conversion to CT/adversary, an incomplete second sortie or training outcome. Academics count zero. An upgradee flying adversary as a backup receives no upgrade-event count for that role.
- Academics may share a day with a simulator or ordinary non-upgrade duties. For an upgradee, ANY flight plus academics on the same calendar day requires prior DO approval, whether academics occur before or after flight. Non-upgrade duties here must not be read as an exemption for flight plus academics.
- Several academics in a day, academics after a late simulator, or academics consuming needed planning time may be excessive. Use DO judgment without a fixed invented threshold. Academics may occur the day before a simulator/flight unless unusually demanding.
- Avoid sim-to-flight and different-mission flight-to-flight sequencing that removes needed planning time. This is a waivable preference. Consecutive same-mission flights can be useful for repeat looks, weather backup or a placeholder if the student does not pass. Do not create a universal one-day-buffer requirement.
- Conditional progression, protected instructor availability for reflow, and upgrade lines that convert to CT follow weekly DO direction. Do not force a universal progression rule. All prerequisites, event sequence, instructor/student ratios and evaluation rules come from the applicable syllabus or explicit notes.
- Conditional, reserved, tentative and CT-convertible opportunities are not automatically firm completion credit. Include conditional capacity in a risk-adjusted case only when all resources are protected or weekly DO notes direct it. Neither treatment invents earned credit or prerequisite completion.

## Instructor and personnel use

- IPs are generally eligible unless syllabus, dated Letter of Xs or DO notes restrict them. Verify the actual role; leadership position alone does not establish qualification.
- Rotate IPs for perspective unless a specific continuity requirement is stated. Weekly DO notes can require named instructors or groups. “FLUGs three times with any qualified IP,” “CALLSIGN with patch only,” and “IPUGs with CC, DO, patch, or OG” are examples of weekly guidance, not standing cohort restrictions.
- Assess IP burden using flights, simulators, academics, upgrade-event complexity, brief/debrief burden and consecutive complex days. Use the target week's schedule plus Flt CC inputs, DO notes and commitments; compare similarly available IPs. Show workload and ask before labeling an ambiguous case overloaded. Do not assume a workload discount for CC, DO, weapons or Flt CC duties.
- For non-upgrade pilots, check feasibility and obvious overload without applying the full upgrade/IP optimization model.
- Normally acceptable IP combinations: two flights in one pit sequence, flight plus academics, simulator plus academics, and multiple simulators. Do not assume flight plus simulator or unrelated flights in separate goes are acceptable. Ask or use weekly notes for ambiguous/person-specific combinations. For upgradees, the more restrictive upgradee rules govern.

## Availability, qualifications and duty

- Reconcile all-pilot leave and exact-time commitments conservatively. Tentative leave is unavailable. Any unresolved restriction means unavailable until confirmed otherwise. For an already scheduled pilot, flag a hard conflict and conditionally offer a qualified replacement or legal duty swap; do not silently change the source.
- The dated Letter of Xs is the qualification matrix. An unsupported role without a documented waiver or upgrade/evaluation exception is a hard conflict pending qualification/waiver confirmation. Ask whether the matrix is stale and offer a qualified replacement conditionally. Currency lapses are always flagged; a waivable lapse follows the supplied authority and DO routing.
- Commitments include partial/full/multiday absences, DNIF restrictions, leadership meetings, SOF/Top 3/SDO or equivalent duties, planning and exercise-control tasks. Use exact start/stop times. Any assignment overlap is a hard conflict. Qualified duty swaps may be recommended with full downstream checks.
- Flight availability is mission-specific brief-through-debrief, not just airborne time. Crew-rest analysis uses scheduled times, knowable actual times, commitments and unusual-duty DO notes. Pay attention to late upgrade sims and second-go-to-first-go transitions.
- Apply only supplied rest/duty intervals, start/stop boundaries, event types and exception processes with source/effective date. A prior full week's schedule is useful but may be absent; missing boundary data means manual verification, not an invented limit or a “feasible” conclusion.

## Aircraft, configuration, lines and backups

- Read exact primary lines by go and mission-compatible configuration. Protected spares are separate replacement capacity and never additional planned lines.
- `8x4`: eight primary aircraft first go, four second go. `8p8x4`: eight aircraft/pilots in a continuous hot-pit sequence yielding sixteen sorties, then a four-ship go, twenty scheduled sorties total. The continuous pit sequence counts once for upgrade-event accounting.
- A spare replaces a broken primary; it cannot turn an `8x6` into an `8x7`. Evaluate formation packages, roles and configuration rather than treating lines as interchangeable.
- The training phase/configuration plan is a strong DO-waivable preference, distinct from the five workflow phases. Extract transitions, mission emphasis, configuration dates/counts, support dependencies, phase-bound events and batching opportunities.
- An unfinished phase-bound event can delay transition or require a costly split configuration. Quantify costs from evidence; warn qualitatively if counts are missing. The v0.3 worked example retains two BFM primary aircraft plus a BFM spare when transitioning to a tank-equipped air-to-ground configuration. Those three aircraft reduce the pool available in the new configuration. This is an illustrative configuration case, not a universal aircraft requirement.
- Configuration alternatives require DO approval and maintenance coordination. Never invent coordination, maintenance feasibility or an approval authority.
- Fill every feasible primary line. In early planning, draft review and recovery, recommend fully feasible cascading reshuffles when needed, even with substantial churn. In product gathering, provide allocation/planning options without generating a complete initial lineup. **After the Thursday buy/sell**, show new substantial reshuffles separately and recommend them only when required by a hard conflict/major risk or explicitly directed by the DO; do not silently broaden the approved baseline.
- Before backfill, verify formation qualifications, range/airspace/support, duty/commitments, spares and protection of higher priorities. If no feasible cascade fills a line, state go/configuration/reason, lost opportunity and nearest alternative; do not label a constraint-explained gap inefficient.
- Provide risk-based backup pilots for every flying go. Emphasize high-priority upgrades/evaluations, hard-to-reshuffle lineups, weekly direction and visitor/DV fallout risk.
- A backup must be reachable, awake, uncommitted and able to arrive by brief; verify qualification, formation role, rest, commitments and mission compatibility. An upgradee cannot back up their own upgrade event. They may be adversary/CT backup on another formation without upgrade credit for that role.
- Count standby toward workload, not upgrade events or firm completion capacity unless flown in a qualifying role. Flag repeated standby that harms a priority.
- Verify flight-lead/wingman composition, instructor/evaluator placement, student ratios and adversary roles. Use each person's labeled event and DO secondary objectives; do not infer credit from mission type alone. Identify useful combinations of upgrades, currency, evaluations, formation training, instructor/flight-lead development and adversary training.
- Revalidate every affected person/resource and prior/next duty boundary through the full cascade. Partial checks are insufficient.

## Weather, outlook and recovery

- Use provided next-week forecasts: ceiling/visibility, thunderstorms/lightning, precipitation/icing, timing and confidence. Later-week climatological risk must be clearly labeled. Never invent mission-weather limits. The v0.3 “clear above roughly 10,000 feet” discussion is an unvalidated question, not a governing threshold.
- Missing validated weather rules leave only the affected event unresolved. Offer conditional alternatives, ask a true blocker only when needed, and continue other analysis. Move vulnerable events when evidence supports it; preserve useful repeats and acknowledge uncertainty when a move is not justified.
- Detailed next-week analysis plus a 30-day outlook. Judge On track/Watch/At risk against planned completion: supports plan / shrinking margin / likely miss. Show phase dependency, IP/resource bottleneck, raw required pace, capacity-adjusted pace, best-case and risk-adjusted dates.
- Raw pace is remaining countable events divided by weeks to planned completion. Adjust capacity for known no-fly/low-capacity weeks. Missing/stale planned dates produce unresolved forecasts, a warned current-pace estimate, and a nonblocking request; never invent syllabus duration or completion dates.
- Use future turn patterns, support bookings, simulator availability, absences, skeleton schedules and training phase plans where supplied. Otherwise show required capacity, projected pace and bottlenecks, and request planning assumptions. For CT-convertible lines, identify the recipient, formation/IP changes and continued configuration/support validity.
- Include one moderate downside case each week: a lost upgrade event, weather-sensitive day, key instructor, reduced lines/delayed configuration or lost external support. DO selects or the assistant chooses the plausible case most consequential to feasibility/at-risk progress. Show recovery, completion impact, aircraft/IP effects, displaced CT, deadline and residual risk. Ask before extensive scenarios.
- Recovery focuses first on today's remaining execution, then the next duty day, protects the most at-risk upgrade and minimizes unnecessary pilot/support churn. The explicit full-primary-line cascade policy still applies; approval boundaries remain in force.

## Evidence and learning

Maintain a source-backed normalized ledger; CONFIRM displays all, CONFLICTS ONLY displays gaps/conflicts/low confidence. Cite filename and page/sheet/row/note, separate interpretation and recommendation, ask one blocker at a time and group nonblocking questions. Preserve exact active and baseline roles.

Keep stable playbook candidate IDs and Pending/Approved/Rejected status. A single well-supported example may become standing guidance only by explicit DO approval with evidence, scope and limitations. Never automatically promote weekly guidance or revive rejected lessons without material new evidence.

Historical blind reviews use only information knowable by their cutoff and require an isolated restart after hindsight exposure. Live execution actuals and cutoff-valid historical execution actuals are legitimate. Retrospective outcomes stay separate from the locked blind report. Measure misses, false positives, infeasibility, churn, forecast error and usefulness over several examples before setting numerical performance thresholds.