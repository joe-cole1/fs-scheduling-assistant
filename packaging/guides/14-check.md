# Check the setup

Setup owner and DO: use synthetic material. Record Passed, Failed or Not run, with output and reviewer. These GenAI.mil checks remain Not run until humans execute them.

## Short first-use trial

1. **Read the upload.** Upload startup and local documents. Ask the assistant to name the five phases, explain that Thursday buy/sell is the DO approval event, explain the post-buy/sell implementation boundary, and state both waiver requirements.
2. **Missing products.** Give a fictional tracker, omit currencies and DO checkride priorities, and ask what to schedule. It should explain those gaps, answer supported questions and leave the initial lineup to the scheduler.
3. **Local setup.** For a blank squadron, ask for guidance with no numeric limits supplied. It must leave unknown rules unresolved and keep drafts distinct from approved guidance.
4. **Buy/sell implementation QC.** Provide a synthetic Thursday buy/sell direction and a corrected draft that creates a downstream conflict. It should track the decision, identify the conflict, avoid inventing a second routine buy, and return a materially different solution to the DO.
5. **Publication.** Confirm a corrected version faithfully implements the buy/sell directions, then confirm distribution. It should record publication separately from Thursday approval.
6. **Handoff.** Save a Word handoff and resume in a new chat with the actual source files. Confirm decisions, baseline roles, open checks and next task survive.
7. **Update/rollback.** In a disposable folder, replace or restore System using an update ZIP. Confirm Local Guidance, weekly files and human-approved persistent changes are untouched.

Keep synthetic tests separate from operational work. For full regression and historical testing, use **System → Reference → Validation Plan.docx**.

## Historical blind tests

Use a separate clean conversation and cutoff-valid packet. State BLIND REVIEW, tested phase, exact cutoff and allowed actual results. If later target-week results contaminate a blind test, stop and restart in an isolated context with clean inputs and handoffs. Asking the assistant to ignore what it saw is insufficient.