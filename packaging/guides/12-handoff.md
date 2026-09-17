# Hand off an active week

Use this only when an already-started execution week changes users or conversations. A fresh chat for a new week does not need a handoff. The recorded active week in a handoff overrides the normal next-week default.

## Outgoing user

Paste:

```text
Draft a concise current-state handoff from the current weekly record and supplied
files. Infer the week, as-of time, active phase, next action and exact version
roles; do not ask me to complete a field list unless a material ambiguity cannot
be resolved from the record.

Include:
- exact active, Buy/Sell-presented, corrected, published and signed-daily versions;
- DO Buy/Sell statement, D-### directions, supplemental decisions and waivers;
- current source files to transfer and each material source limitation;
- human confirmations with exact scope;
- completed results/earned credit, remaining firm and conditional events;
- open findings, outlook/scenario state and playbook-candidate decisions;
- current P-### ledger filename/version;
- GAMECHANGER availability in this conversation;
- last required Tuesday/Thursday/delta connector query completed;
- outstanding delta queries;
- SOURCE-BACKED ISSUE, SOURCE CONFLICT and CANNOT VERIFY entries; and
- the actual source files needed to reproduce each material fact.

State the test condition and historical cutoff. Preserve attribution and scope.
Do not carry superseded discussion forward as current direction. Provide a Word
document if supported; otherwise provide text for the Session Handoff Word form.
Do not claim you saved to the shared drive.
```

Review and save **Current Handoff.docx** in **Working Record**. Transfer the actual source files, current decision record and current P-### ledger too. A transcript is optional and does not replace them.

## Receiving user

Open a new **GenAI.mil Gemini conversation**. Upload **UPLOAD THIS TO START.docx**, current local guidance/references, **Current Handoff.docx**, the current decision record, current P-### ledger and the actual files listed in the handoff.

Paste:

```text
Read the startup document, approved local guidance, current handoff, P-### ledger,
decision record and attached source files. The handoff's recorded active week
overrides the normal next-week default.

Reconcile versions and identify missing files, source limitations or conflicting
state. Preserve human decisions and confirmations with their exact scope. State
the current phase, active/baseline versions and next action, then continue my
requested task. Do not ask me to restate run-control fields already supported by
the handoff and files.

A transferred P-### ledger is continuity evidence, not permission to bypass a
Tuesday, Thursday or affected-rule delta query required by the active workflow.
Preserve SOURCE-BACKED ISSUE, SOURCE CONFLICT and CANNOT VERIFY status until the
required connector work or human decision changes it. Do not assume access to the
prior conversation or its uploads.

Apply the recorded test condition and cutoff. If prohibited hindsight is present,
stop the blind review and require an isolated clean restart.
```

Humans reconcile competing proposals before identifying a new active or signed schedule. Never share CAC credentials.
