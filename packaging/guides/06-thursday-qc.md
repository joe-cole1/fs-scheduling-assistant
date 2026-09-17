# Thursday — Full schedule QC

Complete the scheduler's normal checklist first. Then use Gemini for a fresh whole-schedule review of the exact near-final version intended for the Buy/Sell. This is not a delta-only review.

The assistant should infer the execution week, as-of state, current source manifest and most recent clearly identified near-final schedule. If multiple files could be the intended Buy/Sell version, it should ask one version-selection question rather than require a run-control form.

## Upload or confirm

- The exact near-final schedule.
- Any Monday-Wednesday source changes.
- Current decision record and unresolved integration-review issues.
- Current P-### Weekly Publication Rule Ledger.
- Weather/support updates that materially affect the plan.

## Full-QC prompt

```text
Perform Thursday full-schedule QC for the inferred execution week. Review the
entire latest clearly identified near-final schedule from scratch, not only its
recent edits. If more than one schedule could be the intended Buy/Sell version,
ask me which one controls; otherwise infer the version and proceed.

Reconcile all source products first. Classify each as CURRENT, STALE, PARTIAL,
CONFLICTED, INTEGRITY FAILED, UNREADABLE, or SUPERSEDED. Do not use values from a
calculated person-specific source with a material identity/formula integrity
failure. Explain exactly which checks are limited and continue unaffected work.

Check hard constraints, approval and waiver needs, availability, exact-time
commitments, prior/next duty boundaries, qualifications, prerequisites,
instructor/evaluator placement, ratios, formations, aircraft/configuration,
primary lines, protected spares, simulator capacity, range/airspace/tanker and
other support, backups, weather placement, checkrides/evaluations, directed DVs,
upgrade progression, IP workload, 30-day outlook, unused feasible opportunities,
and one moderate downside case. Validate every proposed cascade completely.

Run a fresh publication-grounded pass through DoW Policies Beta (GAMECHANGER)
against the people, roles, events, timing and prerequisites actually scheduled.
Refresh and expand the P-### ledger. For publication-derived requirements, use
only sufficiently traceable connector-retrieved publications. Do not use model
memory, generic military knowledge, or ordinary web search. Preserve
SOURCE-BACKED ISSUE, SOURCE CONFLICT, and CANNOT VERIFY items. Do not claim the
schedule is fully compliant.

Provide:
1. bottom-line advisory readiness: BUY READY, READY WITH DO DECISIONS, or NOT READY;
2. packet/source limitations and high-consequence unverified checks;
3. hard conflicts and approval/waiver needs;
4. ranked exact corrections with full downstream effects;
5. checkrides, directed DVs, at-risk upgrades, primary-line use, protected spares,
   configuration and resource/IP bottlenecks;
6. refreshed P-ledger exceptions and limits;
7. exact DO decisions required; and
8. a concise change list for the scheduler.

This review is advisory. Do not infer approval, coordination, waiver, publication,
or a Thursday DO buy.
```

**Save:** the exact QC schedule version, full report, refreshed P-ledger and corrected decision record in **Working Record**. Keep the schedule source file in **Schedules**.

**Next:** optional **07 Thursday - DO Adversarial Review.docx**, then **08 Thursday - Schedule Buy-Sell.docx**.
