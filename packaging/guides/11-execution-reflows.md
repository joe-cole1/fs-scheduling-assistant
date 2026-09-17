# Execution week — Reflows

Use this for maintenance, weather, personnel, support, result or other changes after publication. **Execution reflow stays on the current published execution week; do not apply the normal next-week planning default.** Protect completed history and use the smallest fully feasible change that preserves the highest priorities.

The assistant should infer the published weekly schedule and each affected date's latest signed daily schedule from the supplied files and record. The latest signed daily is the immediate baseline for that date; the published weekly schedule remains the cumulative baseline. If more than one file could control a date, the assistant should ask one focused question.

Upload the changed fact or execution update plus any new schedule version. Do not fill out a general run-control list.

Paste:

```text
Analyze the execution reflow from the current supplied change/update. Infer the
execution week, as-of time, published weekly baseline, and each affected date's
latest signed daily schedule from the files and decision record. Ask only if more
than one version could control an affected date.

Preserve completed events and confirmed earned credit. Separate completed,
remaining firm, conditional, cancelled/incomplete, and newly changed facts. Do
not equate flown with passed or credited without evidence or human confirmation.

Recommend the minimum-change fully feasible reflow. Check the complete cascade:
pilots, availability, duty boundaries, qualifications, prerequisites,
instructor/evaluator placement, formation roles, aircraft/configuration, primary
lines, protected spares, simulator/support windows, backups, displaced training,
next-duty-day effects, at-risk upgrades, outlook and the current downside case.

Report immediate deltas against the latest signed daily schedule for each affected
date, falling back to the published weekly schedule when no signed daily exists.
Report cumulative departure against the published weekly schedule.

For every changed/proposed person, role, event, timing, prerequisite or other
publication-relevant fact, query DoW Policies Beta (GAMECHANGER) for the affected
rule and update/add the P-### entry. Do not re-query unaffected rules merely to
create churn. Do not use model memory or ordinary web search as fallback.

Identify required daily scheduler/Top 3 sign-off, DO decision, waiver routing,
possible 2407 trigger, source-system updates, numbered-change distribution and
positive two-way notification. Do not imply any of those actions occurred until
a human confirms them.
```

Changes within published times, turn pattern, coordinated support and explicit DO guidance use daily scheduler and Top 3 sign-off when feasible. Changes outside those boundaries return to the DO. Every waiver still requires the DO and the applicable waiver authority.
