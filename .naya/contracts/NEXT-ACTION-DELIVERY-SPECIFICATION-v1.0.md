# 🔱 NAYA POWER — NEXT ACTION DELIVERY / SUCCESSOR TORCH SPECIFICATION v1.0

**STATUS:** CANONICAL RUNTIME SPECIFICATION
**QUALITY STANDARD:** 9.0+
**AUTHORITY:** Extends `NAYA-ACTION-DELIVERY-LAW.md`; does not replace it.

## PURPOSE

Guarantee that every substantive Naya execution leaves a complete operational torch that the next actor can execute without reconstructing the prior conversation.

## CANONICAL FLOW

```text
MISSION
→ DESIRED OUTCOME
→ CURRENT STATE
→ VERIFIED / UNKNOWN / PROTECTED / BLOCKED
→ DECISION / RECOMMENDATION
→ NEXT ACTOR
→ NEXT ACTION
→ READY-TO-RUN EXECUTION
→ EXPECTED OUTPUT
→ SUCCESS CRITERIA
→ VERIFICATION
→ HANDOFF
```

## MANDATORY DELIVERY OBJECT

The canonical machine-readable object is defined in:

`.naya/contracts/NEXT-ACTION-DELIVERY-CONTRACT-v1.json`

It is the single source of schema truth for successor-torch validation.

## HUMAN CONTINUATION

When `next_actor` is `human`, `shawn`, or `user`:

```text
human_prompt_authoring_required = true
human_action = required
human_return_payload = required
```

The human receives the smallest possible action plus exactly what to return. Naya owns interpretation whenever the available tooling permits it.

## EXECUTABLE CONTEXT

`ready_to_run_execution` must contain or reference enough information to execute without conversational archaeology:

- WHERE
- WHY
- CURRENT STATE
- WHAT WAS VERIFIED
- WHAT IS UNKNOWN
- WHAT IS PROTECTED
- WHAT IS BLOCKED
- WHAT TO READ
- WHAT TO DO
- WHAT NOT TO DO
- WHAT TO PRESERVE
- WHAT TO VERIFY
- EXPECTED RESULT
- FAILURE HANDLING
- NEXT DECISION POINT

## ZERO-DROPOFF RULE

A substantive execution without a valid successor torch is incomplete.

The validator must fail closed for missing required fields and known vague actions.

## SURVIVAL TEST

A successor that receives only the handoff and authoritative state must be able to begin the next action without asking the predecessor to reconstruct the context.

## RESPONSE BOUNDARY

Naya responses are interface outputs; this repository can machine-enforce the structured handoff artifact and its tests. Actual model/UI response emission remains an external integration boundary and must consume this contract rather than invent a parallel format.

## NON-REGRESSION

Do not weaken existing validators, human authority, UNKNOWN handling, evidence requirements, or protected baselines to satisfy this contract.

## SUCCESS CONDITION

```text
EVERY SUBSTANTIVE EXECUTION
→ VALID SUCCESSOR TORCH
→ NEXT ACTOR KNOWN
→ NEXT ACTION EXECUTABLE
→ EXPECTED OUTPUT KNOWN
→ SUCCESS / VERIFICATION KNOWN
→ SUCCESSOR CAN CONTINUE
→ NO “NOW WHAT?”
```
