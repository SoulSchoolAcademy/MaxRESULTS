# 🔱 NayaPOWER — Cold-Start Runtime Briefing Gate

**STATUS:** MANDATORY BOOT GATE
**SCOPE:** Every substantive NayaPOWER / MAXIS execution
**CANONICAL BRIEFING:** `.naya/memory/NAYAPOWER-RUNTIME-BRIEFING.md`

## Rule

Before any substantive execution, the successor Naya MUST read the canonical Runtime Briefing before making project changes, giving state-dependent operational instructions, or declaring project state.

The cold-start sequence is:

1. Read `.naya/memory/NAYAPOWER-RUNTIME-BRIEFING.md`.
2. Read the governing Naya Law / START-HERE authority chain.
3. Resolve live repository HEAD and relevant runtime/deployment state.
4. Compare current evidence with the briefing.
5. If the briefing is stale or contradicted, STOP substantive execution, reconcile the briefing, and record the discrepancy.
6. Identify the active BLOCK and exactly one NEXT ACTION.
7. Proceed only when the applicable authority, state, protection, and proof requirements are understood.

## Required briefing fields

The briefing MUST contain exactly these orientation fields:

**WHERE → WHY → BUILDING → PROTECTED → BLOCKED → VERIFIED → UNKNOWN → THIS WEEK → NEXT ACTION → PROOF → LAST LEARNING**

No competing runtime briefing may be created for the same purpose without explicit governance approval.

## Enforcement rule

A cold-start acceptance is **RED** if the canonical Runtime Briefing was not read, if any required field is missing, or if current HEAD/state materially contradicts it without reconciliation.

A briefing is context, not proof. Current repository/runtime evidence always outranks stale briefing content.

## Maintenance rule

Every substantive execution that materially changes state, blockers, verification, priorities, next action, proof requirements, or learning MUST update the canonical briefing before handoff.

**NEXT NAYA > CURRENT NAYA.**
