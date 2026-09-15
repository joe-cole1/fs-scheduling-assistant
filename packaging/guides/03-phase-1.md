# Tuesday — Ingest and plan

Use this after **02 Start a week.docx**. Pantons scheduling inputs are due NLT COB Monday; Tuesday is the normal day to upload them into the main Gemini scheduling conversation, reconcile the planning picture, ask questions and decide what must drive the week.

In a continuing chat, upload only new or revised inputs. If this execution week already has recorded state and you are moving it to a replacement chat or another user, follow **08 Hand off to another user.docx** first. A normal fresh chat for a brand-new execution week does not need a handoff.

Excel, PDFs, readable screenshots, calendar exports and plain-text notes are acceptable. You do not need to reformat existing squadron products into these forms.

| Get this input | What it tells the assistant |
| --- | --- |
| Upgrade/MQT tracker | Who needs which event next, prerequisites, planned completion and recent results |
| Checkride/currency tracker | What evaluations are due and when |
| Leave and commitments, including known upcoming TDYs | Who is available, exact unavailable times, and future scheduling windows |
| Current dated Letter of Xs and roster | Who is qualified for each role and callsign/name matching |
| Maintenance turn, configuration and spare plan | How many primary aircraft can fly each go, in which configuration |
| Simulator schedule | Available devices, slots and assigned events |
| Range, airspace, tanker and other support allocations | Which missions have the support they require |
| Weather forecast, when available | Forecast timing and risks; early forecasts may be provisional |
| Training phase/configuration plan | Mission emphasis and upcoming configuration transitions |
| DO guidance and Flt CC inputs | Priorities, pairings, workload recommendations, directed DV/senior-leader flyers and new restrictions |
| Stable rules and approved playbook | Syllabus sequences/ratios, rest/duty rules, brief/debrief windows and validated weather rules |
| Prior-week schedule/actual duty times, if available | Rest and duty checks at the start of the execution week |

Missing a product? Tell Gemini. It should explain the limitation and continue unaffected planning. Use **02 DO Weekly Guidance.docx** and **03 Flight Commander Input.docx** from **System → Blank Forms** only for information not already captured elsewhere.

## Tuesday first pass

The first planning pass should answer four questions before the schedulers start building Wednesday's schedule:

1. **What needs clarification?** Identify missing, conflicting, stale or unreadable inputs and ask only questions that materially affect planning.
2. **Which checkrides/evaluations matter this week?** Use documented due dates, future leave/TDY, prerequisites, qualified evaluators, resources and DO guidance. Distinguish a due date from a recommended earlier window.
3. **Which DV or senior-leader flyers require deliberate placement?** Identify only flyers actually directed or supported by the inputs, such as OG/CC, WG/CC or other designated visitors/leaders. Do not infer qualification, priority or a flying requirement from rank/title alone.
4. **How should upgrades be planned?** Identify each upgradee's next legal events, prerequisites, desired weekly pace, completion risk, instructor/resource demand and useful candidate windows. Do not build the complete lineup.

Paste:

```text
Tuesday — ingest and planning. Phase 1 PRODUCT GATHERING.
I have uploaded the scheduling inputs available after Monday's input deadline.
Primary scheduler workflow: Gemini.

First reconcile the products and identify missing, conflicting, stale or unreadable
information. Ask the planning questions that materially affect this week.
Then identify and prioritize:
1. checkrides/evaluations and the evidence for their scheduling windows;
2. explicitly directed DV or senior-leader flyers and their constraints;
3. every active upgradee's next legal events, prerequisites, weekly pace,
   instructor/resource demand, candidate windows and completion risk.
Also identify major aircraft/configuration, simulator, range, tanker, support,
weather and personnel constraints that should shape Wednesday's build.

Distinguish facts, human direction, assumptions and recommendations. Do not infer
qualification or priority from rank/title alone. If leadership guidance is
missing, draft questions or PROPOSED guidance for human confirmation. Do not
create the complete weekly lineup; schedulers will build it Wednesday.
```

Ask bounded follow-up questions whenever useful. Example:

```text
Which checkrides should we prioritize this week? Consider actual due dates,
upcoming leave/TDY, prerequisites, available evaluators and resources, and DO
guidance. Distinguish the documented due date from a recommended earlier window.
Cite the facts that support the recommendation and flag missing information.
```

**You should get:** a reconciled planning picture, targeted questions, a checkride/evaluation priority list, directed DV/senior-leader requirements, an upgrade plan, major resource constraints and clearly marked assumptions/proposed guidance.

**Move on:** Wednesday the schedulers begin the bulk schedule build. Missing information does not automatically stop drafting, but any affected assignment remains conditional or unresolved.

**Save:** keep source products in **Inputs** and the planning report, current run control and cumulative decision record in **Working Record**.