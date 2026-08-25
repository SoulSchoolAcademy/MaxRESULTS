# NEXT EXECUTION — P1 CANONICAL WRITE COVERAGE HARDENING

schema_version: 5
status: READY

## Project
Naya Power Superbrain (`PRJ-NAYAPOWER-SUPERBRAIN`)

## North Star
Make the personal Superbrain more canonical, continuous, recoverable, accountable, measurable, intelligent, and self-improving while preserving the protected GREEN boundary.

## Current state
Main is currently at `a728f6ad99cd68b0fbc4bff49337630911e75387`. The authoritative Superbrain Gate is GREEN on run `32908858867`, brain-gate job `97998707598`. The gate now includes a machine-enforced canonical event-write coverage audit.

## Completed work
- Added `.naya/runtime/canonical_write_inventory.py` as a conservative AST-based production event-write coverage audit.
- Added `.naya/tests/test_canonical_write_inventory.py` with a positive canonical caller case and a deliberate direct-event-write bypass case.
- Integrated the coverage audit into `.github/workflows/superbrain-gate.yml`.
- Obtained a genuinely fresh authoritative GREEN execution on main.
- The audit observed 7 relevant findings: A=1, B=0, C=0, D=6, E=0, blockers=0.
- Identified `.naya/memory/emit_daily_intelligence.py` as a real canonical event caller using `create_or_replay`.
- Identified six derived/audit producers that do not write canonical event JSON.
- Created a durable P1 receipt, Naya note, Shawn/Smart Note, and this continuation handoff.

## Verified evidence
- Workflow: `.github/workflows/superbrain-gate.yml`
- Run: `32908858867`
- brain-gate: `97998707598`
- Verified commit: `a728f6ad99cd68b0fbc4bff49337630911e75387`
- Fresh checkout restoration: VERIFIED
- Canonical memory: GREEN; 19 canonical events
- Duplicate/entity audit: GREEN; 0 exact duplicates
- Relationship graph: GREEN; 19 nodes / 32 edges
- Superbrain regression: GREEN
- Continuity regression + deliberate failure: GREEN
- PROJECT / Next Execution / paired representation / learning: GREEN
- Prompt Architect: GREEN
- Intelligence layer: GREEN
- Derived index: GREEN
- Retrieval baseline: GREEN; expected token coverage 1.0 across four cases
- Health: GREEN; 19 events, 0 parse errors, 0 orphan relationships
- Daily CIS: GREEN
- Continuity receipt: VERIFIED
- Receipt artifact: ID `9585796589`; SHA256 `9768ac0ca3cb0b6a173b0ea205a6887ee94375817a27ef04909ee7f71946d286`

## Unresolved issues
- Universal semantic production adoption is not yet proven beyond the current static audit rules.
- Dynamic and indirect event persistence may require stronger detection.
- No B/C/E caller was detected in the current audit scope, so no migration was required in this pass.
- Semantic/vector retrieval, deeper entity/contradiction persistence, durable CIS persistence, durable outbox/retry, teaching-specific runtime enforcement, and AI Operating Feed integration remain future P1/P2/P3 work.

## Constraints
- Protected GREEN boundary: `0f82325a82ed37b5b3a3d097599025369c03a1ed`.
- Never weaken validators.
- Never delete historical knowledge.
- Never bypass canonical event creation silently.
- Never call a heuristic GREEN result universal proof.
- Preserve all existing GREEN behavior and schemas.

## Current objective
Harden canonical event-write coverage until the inventory can account for dynamic and indirect production event persistence with materially lower false-negative risk.

## Next action
1. Restore STATE, Current Daily Project, this handoff, latest receipt, Naya note, and Shawn/Smart Note.
2. Verify current main SHA and latest authoritative Gate.
3. Inspect `canonical_write_inventory.py` and its test.
4. Enumerate every production Python module under `.naya/memory` and `.naya/runtime`, not only modules already matched by the current heuristic.
5. Detect indirect writers: helper functions, aliased write methods, file handles, `json.dump`/`json.dumps` flows, `Path.open`, `open(..., 'w')`, `os.open`, copy/rename/move operations, and event-path construction through variables/constants.
6. Detect promotion paths that do not literally write `SE-` strings at the write site.
7. Explicitly classify every discovered semantic event-producing path A/B/C/D/E.
8. For every B caller, migrate through the canonical boundary with the smallest compatible change.
9. For C callers, define the smallest adapter without creating a parallel memory system.
10. For D callers, record the architectural reason in machine-readable evidence.
11. For E callers, fail the audit visibly and preserve the unresolved state.
12. Strengthen positive and deliberate-failure fixtures to cover the newly detected bypass classes.
13. Run the complete local/CI regression suite.
14. Run the authoritative `.github/workflows/superbrain-gate.yml` against the resulting main.
15. Inspect the actual `brain-gate` job and substantive logs.
16. Only promote the resulting head to GREEN when authoritative evidence proves it.

## Execution instructions
Trace before building. Treat the repository as the source of truth. Inventory first; classify second; migrate only proven-safe callers; enforce the boundary; test both success and deliberate bypass failure; then run authoritative CI. Do not claim universal adoption from a partial inventory. Batch compatible work only when it preserves the existing green boundary.

## Success criteria
- Production source coverage is explicitly enumerated.
- Dynamic/indirect writer classes are covered by tests.
- No genuine B/C/E bypass remains unclassified.
- Any migration preserves existing behavior.
- Positive and deliberate-failure tests pass.
- Authoritative Superbrain Gate is GREEN on the resulting main.
- Receipt, STATE, Naya knowledge, Shawn/Smart knowledge, and this handoff all reflect the same evidence.

## Verification requirements
Record exact current SHA, workflow run ID, brain-gate job ID, substantive step results, actual logs for failures, receipt ID, artifact ID, and artifact SHA256. Only authoritative Actions evidence can promote a head to GREEN.

## Weighted priorities
P0 — authoritative GREEN on every resulting main head
P1 — harden universal canonical event-write coverage
P1 — durable outbox/retry integration and continuity completeness
P2 — entity-resolution persistence and contradiction/supersession depth
P2 — semantic/vector retrieval with measured precision/recall improvement
P3 — automatic CIS compounding
P3 — teaching/project runtime enforcement
P3 — AI Operating Feed integration
P4 — polish

## Finalization contract
Before ending, update STATE, receipt, Naya technical knowledge, Shawn/Smart representation, Current Daily Project, AI-to-AI handoff, weighted priorities, and a ready-to-run NEXT EXECUTION. Claims must be evidence-supported.

## Master principle
**Inventory is not adoption. A GREEN scanner is not universal proof. Prove the coverage model, then prove the architecture.**

Leave the next Naya ahead of where this Naya began.
