# Execution week reflows

Use the current published execution week. Provide the changed facts; the assistant checks a complete proposed reflow.

- [ ] Upload the current published weekly schedule if missing from this chat.
- [ ] Upload each affected date’s latest signed daily schedule if available.
- [ ] Provide the changed facts or current execution update.
- [ ] Upload source products changed by the update.
- [ ] Paste the reflow prompt below.
- [ ] Check the week and baseline filenames shown by the assistant.
- [ ] Follow the assistant’s one next action.
- [ ] Obtain the required human sign-offs, DO decisions and waiver decisions.
- [ ] Make the authorized source changes in your normal tool.
- [ ] Complete required coordination and change distribution.
- [ ] Provide the actual signed version and decisions to the chat.
- [ ] Paste the human-decision prompt below.
- [ ] Save the current signed version in Schedules.
- [ ] Save the complete weekly record in Working Record.

## Reflow prompt

Copy **System → Prompts → 11_Analyze_Reflow.txt** or paste the complete text below.

```text
Do not delegate to subagents. Analyze the execution change I supplied.
```

## Human decision prompt

Copy **System → Prompts → Record_Human_Decision.txt** or paste the complete text below.

```text
Do not delegate to subagents. Record the human decision I supplied.
```

Daily scheduler and Top 3 cover feasible changes within published times, turn, coordinated support and DO guidance. Changes beyond those bounds return to the DO. The assistant never signs or sends.

**Finished when:** The actual decisions and each affected day’s current baseline are recorded. Changed publication rules are checked or remain explicitly unverified.
