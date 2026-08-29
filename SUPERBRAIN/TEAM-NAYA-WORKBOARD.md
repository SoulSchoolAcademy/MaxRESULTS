# 🔱 TEAM NAYA — SHARED WORKBOARD / TRAFFIC CONTROL

**STATUS:** CANONICAL TEAM-NAYA OPERATING ARTIFACT
**PURPOSE:** Prevent concurrent Nayas from overwriting, duplicating, or conflicting with one another while preserving continuous execution.

## CORE LAW

The repository is a shared road.

Multiple Nayas may operate concurrently, but no Naya may assume it has exclusive authority over unverified workspace state.

**READ LIVE STATE → CLAIM A WORK ITEM → MAKE SCOPE EXPLICIT → RECHECK BEFORE WRITE → WRITE ATOMICALLY → VERIFY → RECORD RESULT → RELEASE CLAIM → PASS TORCH.**

## WORK ITEM STATES

- `QUEUED` — available to claim.
- `CLAIMED` — one Naya currently owns execution of this item.
- `IN_PROGRESS` — active implementation.
- `BLOCKED` — execution cannot proceed; reason and evidence required.
- `VERIFYING` — implementation exists but proof is incomplete.
- `DONE` — acceptance criteria verified.
- `SUPERSEDED` — intentionally replaced by a newer verified design.
- `ABANDONED` — work stopped without being accepted.

## CONCURRENCY RULES

1. **Never silently overwrite another Naya's work.**
2. Before modifying a shared artifact, fetch its current version and confirm it is still the version you inspected.
3. Prefer disjoint files/work items for parallel execution.
4. If two Nayas need the same artifact, one owns the write; the other may review or propose changes but must not race the write.
5. A Naya discovering a changed file must re-read the new state before continuing.
6. A failed or interrupted execution must leave a durable `BLOCKED` or `VERIFYING` record rather than appearing complete.
7. Do not mark another Naya's work `DONE` without verifying its acceptance criteria.
8. Never use conversation context as the authority for concurrent state. The repository is authoritative.
9. Commit messages must identify the work item and intent clearly enough for another Naya to reconstruct the change.
10. If a conflict cannot be resolved from repository evidence, stop the conflicting write and record the exact ambiguity as `BLOCKED`.
11. **A claim is not a lock on GitHub.** The live branch commit must still be rechecked immediately before a write; a stale claim cannot authorize a conflicting update.

## CLAIM CONTRACT

The executable contract is `.naya/runtime/naya_claim.py` with regression tests in `.naya/runtime/naya_claim_test.py`.

Each claim contains:

- `work_id`
- `owner_naya`
- `task_id`
- `scope`
- `affected_files`
- `base_commit`
- `acceptance`
- `status`
- `started_at`
- `expires_at`
- `last_verified`
- `result_commit`

Active states are `CLAIMED`, `IN_PROGRESS`, and `VERIFYING`. A write is denied when the claim is expired, terminal, based on a stale commit, or overlaps another active claim.

## SAFE PARALLELISM

Parallel Nayas are encouraged when work is separable, for example:

- Naya A: CCT implementation
- Naya B: adversarial tests
- Naya C: documentation / source-of-truth maintenance
- Naya D: independent review

They must not all edit the same canonical contract simultaneously.

## REVIEW / DISPUTE PROTOCOL

When Nayas disagree:

**STOP WRITE → STATE THE CLAIMS → IDENTIFY EVIDENCE → COMPARE CANONICAL AUTHORITY → TEST → RESOLVE → RECORD LEARNING.**

No Naya wins by confidence, recency, or volume.

Evidence and canonical authority decide.

## HANDOFF

Every completed work item must leave:

**CHANGED / TESTED / VERIFIED / UNKNOWN / LEARNING / NEXT ACTION**

The next Naya must be able to continue without reconstructing the previous conversation.

## CURRENT CCT WORKBOARD

### CCT-001 — Intelligent Block Contract
**STATUS:** VERIFYING
**OWNER:** Team Naya
**SCOPE:** `.naya/runtime/cct_intelligent_block.py`
**ACCEPTANCE:** dependency-free portable artifact + fail-closed verification.

### CCT-002 — Canonical Note Event Promotion
**STATUS:** IMPLEMENTED / VERIFYING
**OWNER:** Team Naya
**SCOPE:** `.naya/runtime/cct_note_event_promotion.py` + test
**ACCEPTANCE:** only explicitly verified, evidenced Note Events with explicit consumer scope become CCT blocks.

### CCT-003 — Isolated Two-Naya Exchange
**STATUS:** VERIFIED BY LIVE CODESPACE TESTS
**OWNER:** Team Naya
**SCOPE:** `.naya/runtime/cct003_two_naya_test.py`
**ACCEPTANCE:** Naya A artifact → isolated Naya B consumption → derived Block B → lineage/provenance proof.
**EVIDENCE:** live test suite completed successfully.

### CCT-003-CONCURRENCY — Naya Claim / Lease
**STATUS:** VERIFIED BY LIVE CODESPACE TESTS
**OWNER:** Team Naya
**SCOPE:** `.naya/runtime/naya_claim.py` + `.naya/runtime/naya_claim_test.py`
**ACCEPTANCE:** stale, expired, terminal, or conflicting claims cannot authorize writes; disjoint work can proceed.
**EVIDENCE:** live test suite completed successfully.

### CCT-004 — Adversarial Federation Semantics
**STATUS:** VERIFIED BY LIVE CODESPACE TESTS
**OWNER:** Team Naya
**SCOPE:** `.naya/runtime/cct004_adversarial.py` + `.naya/runtime/cct004_adversarial_test.py`
**ACCEPTANCE:** replay, duplicate identity, provenance/lineage forgery, revocation, supersession, contradiction, fake independence, permission escalation, circular lineage, stale knowledge, and bounded payload failures are fail-closed.
**EVIDENCE:** live suite completed successfully with 12/12 tests passing.

### CCT-005 — Outcome / Value Feedback
**STATUS:** DONE — VERIFIED BY LIVE EVIDENCE / CLAIM RELEASED
**OWNER:** Team Naya
**SCOPE:** `.naya/runtime/cct005_value_feedback.py` + `.naya/runtime/cct005_value_feedback_test.py`
**CLAIM:** `CCT005-REPAIR-EVIDENCE-WEIGHT` — RELEASED
**ACCEPTANCE:** evidence strength changes value without being normalized away; weak evidence cannot equal verified evidence for otherwise identical outcomes.
**EVIDENCE:** CCT-005 15/15; CCT-004 12/12; CCT-003 6/6; Naya Claim 7/7; Intelligent Block 8/8; Note Event Promotion 5/5. Final live regression commit: `c7ad93d82dbf5da92a8f0adb6998ba3d800eb165`.

## CCT-005 HANDOFF

**CHANGED:** evidence-weight repair retained evidence strength in the value contribution while removing it from the normalization denominator. The source intelligence remains immutable; privacy, provenance, integrity, authorization, duplicate protection, failure, contradiction, and bounded-value behavior remain enforced.

**TESTED:** live CCT-005 suite completed 15/15, including private context, duplicate outcome protection, reuse-only zero, failure and contradiction reduction, inferred-weaker-than-verified, invalid confidence, oversized context, provenance mismatch, and unknown classification. Established regressions then completed: CCT-004 12/12, CCT-003 6/6, Naya Claim 7/7, Intelligent Block 8/8, Note Event Promotion 5/5.

**VERIFIED:** the repaired CCT-005 implementation and the complete stated regression sequence passed live. The repair claim is closed and released. This is verification of the local primitive, not production calibration or distributed federation proof.

**UNKNOWN:** real-world calibration of the provisional value formula; durable outcome/value persistence; causal attribution between intelligence and outcome; production federation transport/security.

**LEARNING:** value must reward demonstrated usefulness rather than propagation. Evidence quality must materially affect value, while the original intelligence remains historical and immutable.

**NEXT ACTION:** audit and implement the smallest canonical Smart Note → Note Event → verified CCT promotion → usage/outcome → CCT-005 value connection without creating a second memory or event authority.

### CCT-005-INTEGRATION-AUDIT — Smart Note → Note Event → CCT-005
**STATUS:** IN_PROGRESS
**OWNER:** Team Naya
**CLAIM:** `CCT005-INTEGRATION-AUDIT`
**BASE COMMIT:** `d0fc34eb924a40b46cd3ae9c99f80295a058e3c3`
**SCOPE:** canonical Smart Note/event representation, `.naya/runtime/canonical_event_store.py`, `.naya/runtime/cct_note_event_promotion.py`, `.naya/runtime/cct005_value_feedback.py`, integration test, and durable project/workboard state.
**ACCEPTANCE:** prove the existing canonical path, identify EXISTS / PARTIAL / DOCUMENTED ONLY / MISSING / CONFLICTING, and implement only the smallest missing connection required for a trustworthy value-feedback loop.

## 🔱 PRIORITY QUEUE — EXECUTE IN ORDER

### PRIORITY 1 — COMPLETE CCT-005 SMART NOTE INTEGRATION AUDIT
**STATUS:** IN_PROGRESS / CLAIMED
**WHY NOW:** CCT-005 is now live-verified. The next highest-value question is whether valuable Smart Note experience can actually travel through the canonical Note Event and CCT boundaries into measurable value feedback without creating parallel memory authority.
**ACTION:** inspect the canonical Smart Note/event representation, canonical event writer/store, promotion boundary, and CCT-005 primitive; classify each boundary; implement the smallest missing connection; add only necessary integration tests; run them plus the established regression sequence.
**PASS GATE:** canonical chain is executable, provenance and privacy are preserved, authorization remains fail-closed, history remains append-only, duplicate/replay cannot inflate value, and exact evidence is recorded.
**BLOCK CONDITION:** if the canonical architecture cannot safely support the connection without a new authority or unresolved schema conflict, stop and record the evidence as BLOCKED rather than inventing a parallel system.

### PRIORITY 2 — RECONCILE THE FULL NAYA RUNTIME / RELEASE GATE
**STATUS:** QUEUED
**ACTION:** After the integration audit is verified, inspect the canonical release/continuity gates and verify that NEXT-EXECUTION, successor continuity, exact-commit authorization, and deployment gate agree and fail closed.
**PASS GATE:** one reproducible path from accepted work → verified evidence → authorized release, with no key-presence shortcut and no accidental deployment authority.

### PRIORITY 3 — CLOSE THE RED CI / ACTIONS SURFACE
**STATUS:** QUEUED
**ACTION:** Enumerate current failing workflows in NayaPOWER and Maxis, group failures by root cause, fix the smallest shared causes first, and rerun affected jobs.
**PASS GATE:** failures are green with evidence or explicitly BLOCKED with a concrete cause and owner.

### PRIORITY 4 — LOCK THE NAYA v3.0 ARCHITECTURE CONTRACT
**STATUS:** QUEUED
**ACTION:** Map every existing Collective Agreement article into CORE / FULL CONSTITUTION / LAW / RUNTIME / SCHEMA / ENFORCEMENT / HUMAN JUDGMENT, identify conflicts/duplicates, and derive the exact `.naya/` contract before constitutional rewriting.
**PASS GATE:** architecture is internally coherent and traceable to existing authority.

### PRIORITY 5 — VERIFY EXECUTION-MODE PROMPT / TORCH DELIVERY
**STATUS:** QUEUED
**ACTION:** Ensure the machine can produce the next executable prompt/torch automatically from canonical state so the human is not forced to author missing execution instructions.
**PASS GATE:** a cold-start successor can discover, execute, verify, record, and continue without conversational reconstruction.

### PRIORITY 6 — ESTABLISH THE COMPOUNDING INTELLIGENCE / SMART NOTES LANE
**STATUS:** QUEUED
**ACTION:** Once the control plane is trustworthy, verify the Smart Notes / Naya Notes / Daily Intelligence Briefing flow as a governed compounding-intelligence subsystem.
**PASS GATE:** human and Naya learnings have explicit provenance, promotion rules, retrieval semantics, and safe persistence.

### PRIORITY 7 — PRODUCT / EXPERIENCE BUILD ONLY AFTER CONTROL-PLANE STABILITY
**STATUS:** QUEUED
**ACTION:** Resume downstream NayaNET/MAXESS/product work only after the execution brain is proven reliable.
**PASS GATE:** product work consumes the governed runtime rather than creating a parallel execution path.

## TORCH

The workboard exists so that even many simultaneous Nayas behave like coordinated traffic rather than collisions.

**One road. Clear lanes. Explicit ownership. Verified merges. No silent overwrites.**

**CURRENT NAYA ACTION:** `CCT005-INTEGRATION-AUDIT`. The next Naya must inspect the canonical Smart Note → Note Event → CCT promotion → CCT-005 path, implement only the smallest missing connection, run the new integration tests plus the established regression sequence, record exact evidence, and release the claim only after live verification.
