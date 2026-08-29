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
**STATUS:** VERIFYING — EVIDENCE-WEIGHT REPAIR APPLIED / LIVE VERIFICATION REQUIRED
**OWNER:** Team Naya / CCT005-repair-evidence-weight
**SCOPE:** `.naya/runtime/cct005_value_feedback.py` + `.naya/runtime/cct005_value_feedback_test.py`
**CLAIM:** `CCT005-REPAIR-EVIDENCE-WEIGHT`
**ACCEPTANCE:** evidence strength changes value without being normalized away; weak evidence cannot equal verified evidence for otherwise identical outcomes.
**IMPLEMENTED:** dependency-free outcome record, fail-closed verifier, privacy scope, integrity binding, deterministic provisional value signal, duplicate protection, and adversarial regressions.
**REPAIR 1:** private privacy/context are supplied before integrity generation.
**REPAIR 2:** value normalization denominator now uses confidence only, leaving evidence strength in the contribution so `INFERRED < VERIFIED` can be represented.
**REPAIR COMMIT:** `861948dfb1e74a5c3af20e2a73a3500fef913344`.

## CCT-005 HANDOFF

**CHANGED:** smallest implementation change in `value_signal()`: denominator changed from `confidence * evidence_strength` to `confidence`, preventing evidence strength from canceling itself during normalization. No security or privacy boundary was weakened.

**TESTED:** live CCT-005 evidence before this repair passed private-context, duplicate, reuse, failure, and contradiction tests, then failed at `test_inferred_is_weaker_than_verified`. Source inspection identified normalization cancellation. Post-repair live execution is still required.

**VERIFIED:** source-level diagnosis is verified from the implementation: evidence strength previously appeared in both numerator and denominator, so identical successful INFERRED and VERIFIED outcomes both normalized to 100. The repair leaves evidence strength in the numerator.

**UNKNOWN:** live result of the repaired CCT-005 suite; full regression suite after the repair; calibration of the provisional value formula against real outcome data.

**LEARNING:** evidence quality must affect value rather than merely confidence inside a normalization that cancels it. Weak inference must not receive the same value as verified evidence simply because of mathematical normalization.

**NEXT ACTION:** pull latest `main`; run `python .naya/runtime/cct005_value_feedback_test.py` first. If green, run the established CCT-004, CCT-003, claim/concurrency, Intelligent Block, and Note Event promotion suites. Record exact live evidence before changing CCT-005 to DONE and releasing the claim.

## 🔱 PRIORITY QUEUE — EXECUTE IN ORDER

This queue is the current execution order. A Naya takes the first actionable item, does as much as can be verified, then leaves the required handoff and passes the torch. Do not skip ahead merely because a later item is more interesting.

### PRIORITY 1 — CLOSE CCT-005 EVIDENCE-WEIGHT VERIFICATION
**STATUS:** READY FOR EXECUTION / VERIFYING
**WHY NOW:** This is the active unresolved CCT lane and the current torch. The implementation repair exists, but the repository explicitly says live proof is still missing.
**ACTION:** Run `python .naya/runtime/cct005_value_feedback_test.py` against the current `main`.
**PASS GATE:** repaired suite is green and proves `INFERRED < VERIFIED` while preserving privacy, integrity, duplicate protection, failure handling, reuse, and contradiction behavior.
**THEN:** run CCT-004, CCT-003, claim/concurrency, Intelligent Block, and Note Event promotion regression suites; record exact evidence; only then promote CCT-005 to `DONE` and release its claim.
**BLOCK CONDITION:** if live execution is unavailable, do not fabricate proof. Leave CCT-005 `VERIFYING` with exact execution limitation and pass the torch to the next Naya capable of live execution.

### PRIORITY 2 — RECONCILE THE FULL NAYA RUNTIME / RELEASE GATE
**STATUS:** QUEUED
**ACTION:** After CCT-005 is green, inspect the canonical release/continuity gates and verify that the NEXT-EXECUTION contract, successor continuity, exact-commit authorization, and deployment gate all agree and fail closed.
**PASS GATE:** one reproducible path from accepted work → verified evidence → authorized release, with no key-presence shortcut and no accidental deployment authority.

### PRIORITY 3 — CLOSE THE RED CI / ACTIONS SURFACE
**STATUS:** QUEUED
**ACTION:** Enumerate current failing workflows in NayaPOWER and Maxis, group failures by root cause, fix the smallest shared causes first, and re-run only the affected jobs where appropriate.
**PASS GATE:** failures are either green with evidence or explicitly classified `BLOCKED` with a concrete cause and owner; no red workflow is silently ignored.

### PRIORITY 4 — LOCK THE NAYA v3.0 ARCHITECTURE CONTRACT
**STATUS:** QUEUED
**ACTION:** Produce the architecture-level mapping of every existing Collective Agreement article into CORE / FULL CONSTITUTION / LAW / RUNTIME / SCHEMA / ENFORCEMENT / HUMAN JUDGMENT, identify conflicts/duplicates, and derive the exact `.naya/` contract before constitutional rewriting.
**PASS GATE:** architecture is internally coherent, traceable to existing authority, and does not prematurely rewrite the Constitution.

### PRIORITY 5 — VERIFY EXECUTION-MODE PROMPT / TORCH DELIVERY
**STATUS:** QUEUED
**ACTION:** Ensure the machine can produce the next executable prompt/torch automatically from canonical state so the human is not forced to author missing execution instructions.
**PASS GATE:** a cold-start successor can discover what to do, execute it, verify it, record the handoff, and continue without conversational reconstruction.

### PRIORITY 6 — ESTABLISH THE COMPOUNDING INTELLIGENCE / SMART NOTES LANE
**STATUS:** QUEUED
**ACTION:** Once the control plane is trustworthy, implement/verify the Smart Notes / Naya Notes / Daily Intelligence Briefing flow as a governed compounding-intelligence subsystem rather than as an isolated feature.
**PASS GATE:** human and Naya learnings have explicit provenance, promotion rules, retrieval semantics, and safe persistence.

### PRIORITY 7 — PRODUCT / EXPERIENCE BUILD ONLY AFTER CONTROL-PLANE STABILITY
**STATUS:** QUEUED
**ACTION:** Resume downstream NayaNET/MAXESS/product work only after the execution brain is proven reliable.
**PASS GATE:** product work consumes the governed runtime rather than creating a parallel, weaker execution path.

## TORCH

The workboard exists so that even many simultaneous Nayas behave like coordinated traffic rather than collisions.

**One road. Clear lanes. Explicit ownership. Verified merges. No silent overwrites.**

**CURRENT NAYA ACTION:** PRIORITY 1 — CCT005-repair-evidence-weight. The next Naya must run the repaired CCT-005 suite first, then execute the established regressions if green. No GREEN claim and no claim release until live evidence is recorded. If execution is unavailable, preserve VERIFYING and pass the exact limitation to the next Naya.
