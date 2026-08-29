# 🔱 AI NOTE — DURABLE-STATE EVIDENCE RECEIPT REQUIREMENT

## STATUS
CANONICAL OPERATING REQUIREMENT • ACTIVE

## PURPOSE
Prevent unsupported claims that a Smart Note, system update, durable state change, learning promotion, or handoff was created.

## PRIME RULE
A durable-state action is NOT COMPLETE merely because Naya says it was completed.

Completion requires:

`WRITE → RECEIVE COMMIT/SHA → RE-READ ARTIFACT → VERIFY CONTENT → RETURN RECEIPT`

The receipt must identify the exact repository, branch, path, commit SHA, artifact SHA when available, and what was verified.

## EVIDENCE STANDARD

For every durable-state write, the responsible Naya must show:

1. exact artifact path;
2. exact branch/ref;
3. resulting commit SHA;
4. artifact/blob SHA when available;
5. successful re-read of the artifact from the resulting state;
6. concise statement of what was verified;
7. current readiness/status, distinguishing VERIFIED from UNVERIFIED/UNKNOWN.

If the artifact cannot be re-read and verified, the Naya MUST report:

`DURABLE STATE: UNVERIFIED`

and must not claim completion.

## SMART-NOTE RULE
When asked to create or update a Smart Note, Naya must return the note's exact repository link and verification evidence in the completion report.

A Smart Note without a receipt is treated as:

`CLAIMED, NOT PROVEN`

## TEAM RULE
The same evidence discipline applies to:

- Team Naya notes;
- Sean/Human notes;
- PIS/CIS learning promotion;
- runtime/state updates;
- handoffs;
- governance specifications;
- receipts;
- any other durable system state.

## NEXT-ACTION CONNECTION
Every durable-state receipt must itself include or point to the current operational torch:

`NEXT ACTOR → NEXT ACTION → READY-TO-RUN EXECUTION → EXPECTED OUTPUT → SUCCESS CRITERIA → VERIFICATION`

## NON-REGRESSION
Do not weaken existing validators or replace evidence with prose.

## GENERALIZED LEARNING
"Show me" means durable state must be inspectable and independently verifiable. A path, commit, and re-read receipt turn an assertion into evidence.
