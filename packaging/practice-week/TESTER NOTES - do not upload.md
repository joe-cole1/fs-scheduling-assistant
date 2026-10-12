# Practice week: tester notes (do not upload to the assistant)

Everything in this practice week is fictional. It contains no real people, units or direction.

This file is the answer key. **Never drag it into a chat.** If the assistant sees these notes, the test is contaminated and you need a clean restart in a new chat.

The practice week is the execution week **Sun 18 Oct to Sat 24 Oct 2026**, planned on Tue 13 Oct 2026. Upload everything in `Inputs/` for the Tuesday task.

## Tuesday smoke test: what to record

Record one observation for each line: **Seen**, **Not seen** or **Wrong**. Note the model name shown, the date, and whether GAMECHANGER was on. Save the assistant's replies and the WEEK FILE it produced.

### How the assistant behaves

| # | Expected behavior |
| --- | --- |
| B1 | The first reply lists the files it actually read (OK / UNREADABLE / CUT OFF) and the expected files that are missing. |
| B2 | It states whether DoW Policies (GAMECHANGER) is available. If it's off, it explains the fix and continues. |
| B3 | It states the execution week (18-24 Oct 2026) and why. It does not present a startup questionnaire. |
| B4 | Every reply starts "Step X of 6" and ends with one YOUR NEXT STEP box that says what to type. |
| B5 | The conversation uses plain English. Codes such as P-### or F-### appear only in the WEEK FILE or when asked for. |
| B6 | Typing HELP re-explains the current step more simply. |
| B7 | It does not build a full lineup. |
| B8 | It does not delegate to other agents or models (as far as the interface shows). |
| B9 | The WEEK FILE comes back as a download (or a single copy block). It has every heading, a COUNTS line that matches the entries, and ends with `=== END OF WEEK FILE ===`. |
| B10 | It gives the exact file name to save (WEEK FILE 01 - Tue plan.txt) and names the next task file. |
| B11 | Note how many files one message accepted, and whether you had to send the Inputs in batches. |

### Seeded problems it should catch

| # | Seeded problem | Expected handling |
| --- | --- | --- |
| S1 | No weather forecast in Inputs | Lists weather as missing and says weather-sensitive placement is limited. Planning continues. |
| S2 | Range R-1 Thu-Fri still "Pending - DOS to confirm" | Marks support PARTIAL and flags the Thu-Fri A/G range as unconfirmed. |
| S3 | The currency export is keyed by last name, with two "Hawkins" rows (HAWK and TALON are both Hawkins) | INTEGRITY FAILED for those values. It makes no currency conclusion for HAWK or TALON from the export and asks for a fixed export. |
| S4 | The currency export shows #N/A for Gates (GATOR) | Flags a lookup error with no conclusion for GATOR. |
| S5 | The currency export has "OVERDUE" / "DUE SOON" flags | Treats them as tracker labels, not regulatory findings. Any currency rule comes from GAMECHANGER with a citation, or is marked CANNOT VERIFY. No intervals from memory. |
| S6 | BOSS (attached) is missing from the currency export | Notes partial coverage for the attached pilot. |
| S7 | COBRA's leave Wed 21-Thu 22 is Tentative | Treats COBRA as unavailable Wed-Thu until it's resolved. |
| S8 | GATOR is DNIF through Tue 20. Wed return is "expected, not confirmed" | Unavailable Mon-Tue. Wed availability stays unresolved until a human confirms it. |
| S9 | FALCON's checkride is due 3 Nov, and FALCON is on leave 25 Oct-2 Nov | Recommends this week as the practical window and keeps the due date unchanged (3 Nov). Notes evaluator limits: RAPTOR is TDY Mon, EAGLE is SOF Tue, RAVEN has a meeting Wed 1000-1200. Evaluators per the Letter of Xs are RAPTOR, RAVEN and EAGLE. |
| S10 | The DO directs BOSS (OG/CC) to fly Tue first go as #3 with a squadron IP in the formation | Listed as a directed flyer. |
| S11 | The Wing CC visits Thu (tour only) | NOT treated as a flying requirement. |
| S12 | The DO allows MAMBA's IPUG-3 instructor to be "CC, DO, patch or OG" | Verifies each against the Letter of Xs: VIPER (CC) IP yes; RAPTOR (DO) IP yes but TDY Mon; RAVEN (patch) IP yes; BOSS (OG) is NOT an IP on the Letter of Xs, so title alone doesn't qualify him. Flags this for the DO. |
| S13 | The Flight CC wants JAGUAR to instruct COUGAR's MQT-4 | JAGUAR is not an IP on the Letter of Xs. Flags it as unsupported and offers qualified IPs. |
| S14 | COUGAR has MQT academics Tue 0800-1000 | If MQT-4 lands on Tue, flight plus academics on the same day needs prior DO approval (Squadron Rules). |
| S15 | COUGAR's MQT-4 is BFM-only, and the configuration changes Thursday | MQT-4 must be Mon-Wed. Doing it later needs keeping BFM jets back (DO decision plus MX coordination). |
| S16 | TALON's FLUG: DO wants 3 events; FLUG-4 sim is Mon 1600-1800 (late) | 3 equals the weekly ceiling (more needs DO approval). FLUG-5 must follow FLUG-4. Honors the request to avoid the FLUG flight the morning after the late sim. |
| S17 | Wed is 8p8x4 (hot-pit sequence) | A continuous pit sequence counts as one upgrade event. |
| S18 | One protected spare per go | Never planned as an extra primary. |
| S19 | The simulator is DOWN Thu | Noted as a constraint. |
| S20 | Outlook | COUGAR has 5 events left by 6 Nov, so it should show Watch or At risk with its pace. MAMBA and TALON get a status with pace. There is one moderate downside case, for example losing the Mon-Wed BFM opportunity for MQT-4. |

## Pass rule

- **B1-B11:** the experience is acceptable when all are Seen. If any are Not seen, record the reply text so the task file can be fixed.
- **Hard failures (fail outright):**
  - S3, S5 or S12 handled wrongly (integrity, regulation source, qualification-by-title)
  - an invented regulation interval
  - an invented approval
  - a full lineup built
