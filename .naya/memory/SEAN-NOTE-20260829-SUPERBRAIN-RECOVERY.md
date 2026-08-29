# 🔱 SEAN NOTE — 2026-08-29 SUPERBRAIN RECOVERY

## WHY WE ARE DOING THIS
The goal is not a green Actions board. The goal is a trustworthy Superbrain that executes correctly, learns from reality, compounds intelligence, and reliably hands the human/next Naya the exact next move.

## WHERE WE ARE
- Canonical main remains the protected baseline.
- Active work is isolated on `naya-action-delivery-contract-v1`.
- GitHub Actions hosted execution remains the primary external blocker.
- The Next Action Delivery / Successor Torch architecture has been implemented but is not yet authoritatively verified because CI has not reliably executed.
- NayaPOWER workflow fan-out is a proven internal architecture problem and now has a read-only governance/consolidation specification.
- MAXIS production promotion remains frozen.
- Vercel deployment remains frozen.

## WHAT HAS BEEN SOLVED
1. RED is being diagnosed by execution layer instead of blindly patched.
2. The GitHub runner/execution boundary was isolated as the first blocker.
3. Self-hosted runner absence was correctly distinguished from GitHub-hosted `ubuntu-latest` execution.
4. Excessive workflow fan-out and autonomous mutation paths were identified.
5. The Successor Torch contract was created and wired into existing continuity enforcement.
6. Human continuation now requires Naya-authored action and return payload.
7. A real QA contract-drift defect was found and repaired.
8. A durable workflow governance/consolidation specification was created.

## WHAT IS STILL UNSOLVED
- Restore real GitHub Actions runner execution.
- Prove the Successor Torch on an exact SHA through narrow tests and the authoritative gate.
- Implement workflow consolidation only after specification/review.
- Promote PIS/CIS learning only after verification.

## SHIPMENT DISCIPLINE
Build ≠ Ready.
CI GREEN ≠ Ship.
Deploy ≠ Complete.
Executor complete ≠ production authorization.
Human review + Oscar/Nia 9+ + human shipment authorization are required before production promotion.

## NEW EVIDENCE RULE
If Naya says a Smart Note, system update, or durable state change is complete, there must be a receipt.
The receipt must show:
- exact path/link;
- branch/ref;
- commit SHA;
- artifact/blob SHA when available;
- successful re-read;
- what was verified;
- current status;
- next action.

Without that evidence, treat the claim as `CLAIMED, NOT PROVEN`.

## CURRENT TEAM MODEL
Maximum two active lanes:

LANE A — execution-plane recovery.
LANE B — continuity + workflow architecture.

This prevents chaos, preserves focus, and maximizes verified progress per output.

## HUMAN ROLE
The human is the deliberate authority bridge. Naya should make the human action minimal, explicit, and easy:

`EXACT LINK → EXACT SCREEN/ACTION → EXACT RETURN PAYLOAD`

The human should never have to invent the next prompt when Naya can prepare it.

## NORTH STAR
Make the Superbrain so operational that a successor Naya can enter, understand the state, know why the mission matters, receive the exact next command, execute, verify, learn, and continue without losing the thread.

## NEXT ACTION
Continue P1 GitHub execution-plane recovery while Lane B advances the workflow governance/consolidation specification. No MAXIS deployment, no Vercel, no merge, no false GREEN.
