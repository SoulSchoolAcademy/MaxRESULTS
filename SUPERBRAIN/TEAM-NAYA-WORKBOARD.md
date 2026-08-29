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
**STATUS:** VERIFYING
**OWNER:** Team Naya
**SCOPE:** `.naya/runtime/cct004_adversarial.py` + `.naya/runtime/cct004_adversarial_test.py`
**ACCEPTANCE:** replay, duplicate identity, provenance/lineage forgery, revocation, supersession, contradiction, fake independence, permission escalation, circular lineage, stale knowledge, and bounded payload failures are fail-closed.
**IMPLEMENTED:** dependency-free semantic guard layer and 11-test adversarial suite.
**RUNTIME STATUS:** pending live Codespace execution.

### CCT-005 — Outcome / Value Feedback
**STATUS:** QUEUED
**OWNER:** UNCLAIMED
**ACCEPTANCE:** intelligence use produces measurable outcome evidence that can update future value/retrieval decisions.

## TORCH

The workboard exists so that even many simultaneous Nayas behave like coordinated traffic rather than collisions.

**One road. Clear lanes. Explicit ownership. Verified merges. No silent overwrites.**

**CURRENT NAYA ACTION:** Pull the latest `main`, run the CCT-004 adversarial suite, then rerun the complete CCT regression suite. Do not declare CCT-004 green without live evidence. If a test fails, repair only the first evidence-backed defect and rerun.
