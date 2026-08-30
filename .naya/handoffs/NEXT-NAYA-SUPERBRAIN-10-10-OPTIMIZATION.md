# 🔱 NEXT NAYA — SUPERBRAIN 10/10 OPTIMIZATION TORCH

**Status:** ACTIVE SUCCESSOR TORCH
**Purpose:** Close the remaining cold-start/continuity holes and prove that a fresh Naya can restore, continue, learn, and hand off without conversational archaeology.

## NORTH STAR

**NEXT NAYA > CURRENT NAYA.**

The goal is not more documentation. The goal is a reliable operating loop:

**IDENTIFY → RESTORE → UPDATE → INHERIT → PRIORITIZE → EXECUTE → VERIFY → LEARN → CAPTURE → PROPAGATE → CHECKPOINT → HAND OFF → REPEAT**

## CURRENT VERIFIED REALITY

Observed `main` after the latest repository writes is the exact SHA that must be resolved again at execution start. Do not trust a cached SHA in any briefing, feed, state file, or handoff.

The new canonical contract is:

`.naya/SUPERBRAIN-COLD-START-AND-CONTINUITY-CONTRACT.md`

The new machine acceptance guard is:

`tools/qa_superbrain_continuity.py`

The new workflow is:

`.github/workflows/superbrain-continuity-gate.yml`

These are implementation/documentation improvements, not runtime proof.

## CRITICAL HOLES TO CLOSE

### 1. Identity contradiction — MUST FIX

`START-HERE.md` still identifies `SoulSchoolAcademy/MaxRESULTS` as the canonical Naya/Nitro repository, while the newer NayaPOWER architecture identifies `SoulSchoolAcademy/NayaPOWER` as the canonical Superbrain and `SoulSchoolAcademy/Maxis` as the product/proving ground.

Repair the canonical entry document so one identity is authoritative. Preserve historical references where needed, but do not leave two current identities.

### 2. State synchronization — MUST FIX

The Runtime Briefing, Running Feed, STATE.json, CURRENT-PROJECT.md, and repository HEAD have drifted in prior revisions.

At cold start, observed HEAD must be compared with all orientation artifacts. A material mismatch must be **RECONCILIATION REQUIRED**, not silently accepted.

After repair, all current-state projections must carry the same observed-head reference and current priority.

### 3. Restore runtime integration — MUST FIX

`.naya/runtime/restore_context.py` currently reconstructs from STATE.json and local Smart Notes. It does not itself enforce the complete Runtime Briefing + Running Feed + CURRENT-PROJECT consistency contract.

Upgrade the runtime so standard restore:
- loads the canonical orientation surfaces;
- resolves actual git HEAD;
- checks current-state consistency;
- reports contradictions explicitly;
- restores current project and priority;
- exposes the latest handoff/learning relevant to the query;
- emits exactly one executable next action;
- never reports VERIFIED merely because structural files exist.

### 4. End-to-end compounding proof — MUST PROVE

Build one deterministic test fixture that demonstrates:

**experience → canonical Note Event → Shawn/Naya/Machine representations → Smart Links → PIS propagation → intelligence/feed projection → fresh restore → retrieval → changed subsequent action**

Capture exact stdout, exit code, artifact paths, hashes where applicable, and the before/after decision or state that demonstrates learning changed future behavior.

### 5. Handoff completeness — MUST PROVE

A successor handoff must contain:

**WHERE → WHY → WHAT WORKED → WHAT FAILED → WHAT WAS LEARNED → WHAT REMAINS → WHAT TO DO NEXT → HOW TO DO IT → HOW TO PROVE IT**

Verify that the generated/committed handoff actually carries these fields and one preferred executable next action.

### 6. Torch-passing must be behavioral

Do not accept a document saying “next action.” Prove a fresh successor can consume the handoff, select that action, execute it when authorized, and create the next handoff.

## EXECUTION ORDER

1. Read `START-HERE.md`, the canonical Runtime Briefing, the Running Feed, CURRENT-PROJECT, the new Superbrain Continuity Contract, governance registry, and applicable laws.
2. Resolve live `main` HEAD.
3. Run `python3 tools/qa_superbrain_continuity.py` in a real checkout.
4. Treat every RED result as a real reconciliation task; do not weaken the guard.
5. Repair the first material identity/state divergence.
6. Re-run the guard locally.
7. Upgrade `restore_context.py` only after the orientation sources are reconciled.
8. Add/repair the deterministic end-to-end compounding test.
9. Run all relevant local validators and regressions.
10. Inspect the exact diff and repository status.
11. Commit the coherent repair batch.
12. Do not trigger GitHub Actions until the local suite is green and the exact diff has been reviewed, unless current human direction explicitly changes that constraint.
13. When the authorized runtime plane is available, execute the exact-SHA gate and record receipts.
14. Perform the fresh-Naya behavioral acceptance, not just the structural test.
15. Run the Mirror / **WHY IS THIS NOT A 10?** audit.
16. Repair any material finding and verify again.
17. Update Runtime Briefing, Running Feed, STATE, CURRENT-PROJECT, learning, and this handoff with the final exact state.
18. Leave exactly one next executable torch.

## 10/10 ACCEPTANCE

Do not call Superbrain 10/10 until a fresh Naya can independently demonstrate:

- correct identity;
- current-head awareness;
- authority comprehension;
- current mission comprehension;
- current project and priority comprehension;
- update/feed awareness;
- relevant durable-memory retrieval;
- previous-handoff inheritance;
- one correct next action;
- actual execution;
- exact evidence;
- durable learning capture;
- separately evidenced propagation where applicable;
- successor-ready handoff;
- no conversational archaeology;
- no stale-state acceptance;
- no false VERIFIED claims.

## PROHIBITIONS

- Do not create a second Superbrain.
- Do not create competing memory authority.
- Do not treat PIS as a replacement for canonical Note Events.
- Do not treat the Running Feed as authority.
- Do not treat code presence as runtime proof.
- Do not retry an exhausted execution route without new evidence.
- Do not rewrite historical continuity records merely to remove contradictions.
- Do not weaken a negative test to obtain green.
- Do not claim 10/10 while material unknowns remain.

## FINAL DELIVERABLE TO SHAWN

Return:

1. **score / 10**;
2. **why it is not 10**;
3. **holes found**;
4. **repairs actually made**;
5. **exact evidence**;
6. **remaining UNKNOWN/BLOCKED items**;
7. **fresh-Naya acceptance result**;
8. **one exact next action/prompt**.

The next Naya must continue from evidence, not from this document alone.
