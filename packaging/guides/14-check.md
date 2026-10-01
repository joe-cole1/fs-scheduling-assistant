# Check the setup

Use a clean chat and clearly fictional inputs. Record Passed, Failed or Not run with actual output and reviewer.

- [ ] Open a new GenAI.mil conversation.
- [ ] Upload System → UPLOAD THIS TO START.docx.
- [ ] Upload local guidance suitable for the trial.
- [ ] Paste the setup-check prompt below.
- [ ] Confirm the assistant identifies readable files and one next action.
- [ ] Try Tuesday startup with a small fictional input packet.
- [ ] Confirm it infers dates without a startup questionnaire.
- [ ] Run full QC on a fictional draft containing a known conflict.
- [ ] Confirm the conflict and unverified checks stay visible.
- [ ] Confirm it performs the work without subagent delegation.
- [ ] Run the applicable cases in System → Reference → Validation Plan.
- [ ] Save actual outputs and reviewer results in an approved test location.

## Setup check prompt

Copy **System → Prompts → 14_Check_Setup.txt** or paste the complete text below.

```text
Do not delegate to subagents. Check the uploaded setup.
```

Check unavailable GAMECHANGER, conflicting publications, affected deltas, calculated-source integrity, Buy/Sell, publication, reflow and handoff. A self-reported pass is not test evidence.

**Finished when:** The setup owner and DO have reviewed the actual trial. Package generation alone does not prove GenAI.mil behavior or operational readiness.
