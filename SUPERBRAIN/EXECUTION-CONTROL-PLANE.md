# 🔱 NayaPOWER — Execution Control Plane

**STATUS:** CANONICAL / GOVERNING
**PURPOSE:** Turn the Team Naya execution doctrine into a machine-checkable control surface without replacing Mission State or repository-specific authority.

## 1. Authority

NayaPOWER governs the execution method.

Each governed product repository retains its own canonical Mission State, architecture, and product truth.

This control plane records execution metadata and validates consistency. It does **not** become a second product or project truth source.

## 2. Required State Object

Every active execution must be representable by one machine-readable state object containing:

```text
project
repository
branch
current_head
production_head
deployment
active_block
block_status
owner
start_head
target_state
dependencies
protected_scope
evidence
checkpoint
unknowns
failures
next_action
updated_at
```

## 3. Allowed Block States

```text
PENDING
ACTIVE
VERIFIED
BLOCKED
FAILED
SUPERSEDED
```

`VERIFIED` requires evidence. `UNKNOWN` is never upgraded by assumption.

## 4. Single Next Action

The state must contain exactly one `next_action` for the active execution.

If multiple candidates exist, the execution owner must rank them and retain only the highest-value executable move as the primary action. Other work remains in the block plan, not as competing next actions.

## 5. Evidence Contract

Material claims follow:

```text
REQUIREMENT
→ IMPLEMENTATION
→ TEST
→ OBSERVED RESULT
→ EVIDENCE
→ VERIFICATION
→ COMMIT
→ DOCUMENTED STATE
```

Minimum evidence fields should identify:

- requirement/block;
- claim;
- evidence type;
- exact observation;
- source URL/path or artifact;
- commit/deployment SHA where applicable;
- timestamp;
- verification state.

## 6. Drift Rules

The control plane must flag:

- declared HEAD != actual HEAD;
- declared production SHA != observed production SHA;
- VERIFIED claim without evidence;
- VERIFIED block without exit evidence;
- multiple primary next actions;
- stale owner/lease;
- unresolved contradiction;
- deployment marked production without a real READY deployment;
- runtime evidence attached to a different commit than the claimed execution state.

A drift finding becomes `UNKNOWN`, `STALE`, or `FAILED` according to the evidence. It never becomes green automatically.

## 7. Ownership / Concurrency

For shared execution scope:

```text
CLAIM
→ RECORD START HEAD
→ RECORD SCOPE
→ EXECUTE
→ VERIFY
→ RELEASE
```

A stale claim must not silently overwrite a newer verified execution.

## 8. Contradiction / Supersession

Durable contradictions must be resolved through:

```text
DETECT
→ IDENTIFY AUTHORITIES
→ APPLY PRECEDENCE
→ MARK SUPERSEDED
→ LINK REPLACEMENT
→ RECORD WHY
→ VERIFY CURRENT STATE
```

Historical evidence remains discoverable; obsolete authority does not remain ambiguous.

## 9. Cold-Naya Acceptance Contract

A cold Naya must independently recover:

```text
WHAT
WHY
WHERE
AUTHORITY
PROTECTED
CURRENT STATE
CURRENT GAP
NEXT ACTION
PROOF METHOD
HANDOFF METHOD
```

Then execute one low-risk repository task and leave a verified handoff.

Acceptance:

```text
RESTORE → IDENTIFY → EXECUTE → TEST → VERIFY → RECORD → HANDOFF
```

## 10. Completion Law

A block is not complete because code exists.

A block is complete only when:

```text
IMPLEMENTED
+
TESTED
+
VERIFIED
+
DOCUMENTED
+
INTEGRATED
```

## 11. Project Adapter Rule

Project repositories should keep their own canonical Mission State and product architecture.

NayaPOWER supplies the execution grammar; the project supplies the product truth.

This prevents the Superbrain from becoming a second source of truth for MAXIS, NayaNET, or any future governed product.
