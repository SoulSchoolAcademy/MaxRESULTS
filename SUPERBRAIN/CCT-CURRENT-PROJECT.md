# 🔱 CCT + SUPER BRAIN — CURRENT PROJECT / TEAM NAYA TORCH

**STATUS:** ACTIVE BUILD
**REPOSITORY:** `SoulSchoolAcademy/NayaPOWER`
**BRANCH:** `main`
**PURPOSE:** Build and prove the first executable Collective Chain Technology (CCT) intelligence exchange loop.

## MISSION

Build a continuously improving intelligence system in which human experience, Naya reasoning, memory, verified learning, and permissioned collective intelligence compound to produce increasing value for humans and AI.

## NORTH STAR

**Maximum verified useful value per unit of effort, with compounding intelligence, continuity, provenance, safety, and human benefit.**

## CURRENT TARGET

Prove the smallest complete CCT loop:

**Naya A → Intelligent Block A → isolated Naya B → independent consumption → Intelligent Block B → explicit lineage/provenance → verification**

Full distributed NayaNET federation is downstream of this proof.

## SOURCE OF TRUTH

Read in this order before substantive execution:

1. `SUPERBRAIN/NAYA-REPOSITORY-OPERATING-STANDARD.md`
2. `.naya/control-plane/STATE.json`
3. `.naya/control-plane/BLOCKS.json`
4. `.naya/control-plane/MAP.json`
5. `.naya/codex/SMART-BRAIN-OPERATING-SYSTEM.md`
6. `.naya/codex/SMART-NOTES-AND-CIS-CONSTITUTION.md`
7. `SUPERBRAIN/TEAM-NAYA-WORKBOARD.md`
8. CCT implementation/tests under `.naya/runtime/`

The control-plane active block remains authoritative until its own exit criteria are verified. Do not silently supersede it.

## VERIFIED FOUNDATION

- Naya Repository Operating Standard is canonical and active.
- Smart Brain OS is canonical and active.
- Smart Notes + CIS Constitution is canonical and active.
- Canonical Note Event storage is implemented with idempotent create/replay behavior.
- Deployment governance is fail-closed; repository activity is not itself a release.
- Repository control-plane MAP / STATE / BLOCK / PROOF artifacts exist.
- CCT Intelligent Block v1 contract exists as a dependency-free local artifact/verifier.
- CCT promotion adapter now connects verified canonical Note Events to the Intelligent Block boundary.
- Team Naya shared workboard now defines concurrency, ownership, conflict, and handoff rules.

## CURRENT CCT IMPLEMENTATION

### Intelligent Block
`.naya/runtime/cct_intelligent_block.py`

Provides schema/version, stable identity, producer, content, provenance/lineage, evidence, verification, permissions, lifecycle, SHA-256 integrity, fail-closed verification, and parent validation before derivation.

### Acceptance Harness
`.naya/runtime/cct_intelligent_block_test.py`

Covers valid acceptance and fail-closed handling of unverified, unevidenced, tampered, unauthorized, revoked, and provenance-invalid blocks plus derived lineage.

### Canonical Promotion Boundary
`.naya/runtime/cct_note_event_promotion.py`

Converts an existing canonical Note Event into a CCT block only when:

- the event has a valid event ID;
- verification status is exactly `VERIFIED`;
- evidence exists;
- provenance exists;
- consumers are explicitly authorized;
- purpose scope is explicit.

No parallel memory store is created.

### Promotion Tests
`.naya/runtime/cct_note_event_promotion_test.py`

Covers verified promotion, unverified denial, missing-evidence denial, missing consumer authorization denial, and unauthorized consumer denial.

## IMPORTANT BOUNDARY

The current implementation and tests prove a portable artifact contract and canonical promotion boundary. They do **not** yet prove real network transport, an actual LLM-to-LLM exchange, or independent model execution.

Do not claim two Nayas communicated over CCT until the isolated integration proof passes.

## CONCURRENCY CONTROL

`SUPERBRAIN/TEAM-NAYA-WORKBOARD.md` is the shared traffic-control artifact.

Multiple Nayas may work concurrently, but each must claim a work item, keep scope explicit, re-read shared files before writing, avoid silent overwrites, and leave durable status/evidence. Repository state outranks conversational state.

## CURRENT EXECUTION QUEUE

1. Run `.naya/runtime/cct_intelligent_block_test.py` in a live repository checkout and record actual output.
2. Run `.naya/runtime/cct_note_event_promotion_test.py` in the same checkout and record actual output.
3. Build the isolated Naya-A producer fixture from a verified canonical Note Event.
4. Build the isolated Naya-B consumer fixture with originating conversation context excluded.
5. Prove independent consumption and derived Block B.
6. Add adversarial replay, duplicate identity, circular derivation, stale/superseded parent, permission escalation, contradictory evidence, and bounded-payload tests.
7. Add descendant dependency behavior for revocation/supersession.
8. Add outcome/value feedback: intelligence → use → outcome → measurement → value update.
9. Only after the local two-Naya proof is green, design the minimal CCT transport/federation boundary for NayaNET.

## CURRENT UNKNOWNs

- Live execution output for both CCT harnesses from this connector session.
- Whether the isolated Naya A/B exchange can be proven without unnecessary transport infrastructure.
- Production federation security/privacy controls.
- Exact integration with any future model runtime; the current boundary intentionally remains model-independent.

## SUCCESS CRITERIA

CCT MVP is not complete until a reproducible test proves:

**verified canonical intelligence → authorized CCT block → isolated consumer → independent validation/use → derived block → preserved lineage → adversarial rejection of invalid/unauthorized variants.**

## VERIFICATION STANDARD

Every substantive Naya execution records:

**CHANGED / TESTED / VERIFIED / UNKNOWN / LEARNING / NEXT ACTION**

Implemented is not verified. Verified is not production-proven. Recorded is not necessarily current. Unknown is not green.

## EXACT NEXT ACTION

**In a live repository checkout, run both CCT acceptance harnesses: `python .naya/runtime/cct_intelligent_block_test.py` and `python .naya/runtime/cct_note_event_promotion_test.py`. If both are green, build CCT-003: an isolated Naya-A producer and isolated Naya-B consumer integration harness. If either is red, repair only the first evidence-backed defect and rerun.**

## TORCH

The next Naya must restore live state, verify these claims, execute the exact next action, record actual evidence, update this document and the shared workboard, and leave one highest-value next action for its successor.

**NEXT NAYA > CURRENT NAYA.**
