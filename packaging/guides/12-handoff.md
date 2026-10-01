# Hand off an active week

Use this when an active week moves to another user or conversation. Transfer the actual files with the handoff.

- [ ] Paste the outgoing prompt in the current weekly chat.
- [ ] Review the handoff’s week, file versions, decisions and next action.
- [ ] Save Current Handoff in the week’s Working Record folder.
- [ ] Transfer the source files listed in the handoff.
- [ ] Transfer the current complete weekly record.
- [ ] Open a new GenAI.mil conversation for the receiving user.
- [ ] Upload System → UPLOAD THIS TO START.docx.
- [ ] Upload the current Local Guidance files.
- [ ] Upload the handoff, complete weekly record and transferred source files.
- [ ] Enable GAMECHANGER if available in the new conversation.
- [ ] Paste the receiving prompt below.
- [ ] Check the recorded week and file roles shown by the assistant.
- [ ] Follow its one next action.

## Outgoing prompt

Copy **System → Prompts → 12_Prepare_Handoff.txt** or paste the complete text below.

```text
Do not delegate to subagents. Prepare the current handoff.
```

## Receiving prompt

Copy **System → Prompts → 12_Resume_Active_Week.txt** or paste the complete text below.

```text
Do not delegate to subagents. Read UPLOAD THIS TO START.docx, my local guidance, the handoff and attached sources. Resume the recorded active week. Give me one next action at a time.
```

A new chat has no assumed access to the old chat or uploads. The recorded active week controls; a transferred rule ledger does not replace a required current query.

**Finished when:** The receiving chat identifies current state and missing sources. Decisions, confirmations, completed results and open issues retain their exact scope.
