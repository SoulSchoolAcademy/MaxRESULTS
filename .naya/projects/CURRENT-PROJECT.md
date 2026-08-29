# NayaPOWER — CURRENT PROJECT

**Status:** ACTIVE CANONICAL PROJECT STATE
**Updated:** 2026-08-29
**Branch:** `cctb-v0.1-proof`

## MISSION
Make NayaPOWER a trusted, high-performance, continuously improving AI operating system whose intelligence, execution, verification, continuity, and learning compound across successor Nayas.

## OBJECTIVE
Move the proven CCTB v0.1 in-memory A→B→successor primitive across its smallest durable interchange boundary while preserving deterministic identity, independent consumption, permissions, provenance, and lineage.

## CURRENT STATE
- NayaPOWER Runtime Briefing remains the canonical runtime authority.
- CURRENT-PROJECT is the canonical active project execution state; it does not replace the Runtime Briefing.
- CCTB v0.1 deterministic A→B→successor proof is established.
- Minimal durable JSON serialization/reload implementation and acceptance tests have now been added on this branch.
- GitHub repository operations are available; GitHub Actions are intentionally paused.

## VERIFIED
- Existing CCTB protocol implementation was inspected before modification.
- Existing CCTB durable work is constrained to repository-local JSON serialization and tests; no database, network daemon, federation service, or UI was introduced.
- Canonical fixture A has deterministic block ID `sha256:0eb22f69d13d717682895e92441db20e44b9a2888fa69213e3fbaff04b27a5ac`.
- Durable boundary includes canonical UTF-8 serialization, artifact hashing, validation on write/read, canonical-byte enforcement, and reload identity.
- Acceptance coverage includes durable A→B→successor lineage, tampering, unauthorized consumers, broken lineage, and malformed artifacts.

## BLOCKED
- Full local repository test execution cannot be claimed from the current ChatGPT execution environment because the private repository checkout is not locally mounted.
- GitHub Actions execution is paused because the monthly Actions allocation is exhausted; do not trigger it.
- Therefore this durable implementation is NOT YET declared TESTED, VERIFIED, RUNTIME-PROVEN, or PRODUCTION-PROVEN until an actual executable environment runs it.

## RISKS
- Never convert source inspection into a false test claim.
- The durable format must remain canonical and deterministic; formatting drift must be rejected.
- CCTB must remain protocol-focused; do not prematurely add federation infrastructure.
- Preserve the distinction IMPLEMENTED ≠ TESTED ≠ VERIFIED ≠ RUNTIME-PROVEN ≠ PRODUCTION-PROVEN.

## PRIORITIES
1. **P0 — Execute and verify the durable CCTB acceptance suite in an actual local checkout.**
2. **P0 — Record a machine-readable durable proof receipt tied to the exact tested commit.**
3. **P1 — Integrate durable proof into the broader CCTB proof publication path without duplicating verification logic.**
4. **P1 — Continue Promotion Engine V1 deterministic/local readiness while Actions remain paused.**
5. **P2 — Optimize runtime retrieval, source-of-truth enforcement, and execution efficiency after correctness is proven.**

## ACTIVE WORK
CCTB durable interchange proof.

## COMPLETED
- Established canonical CURRENT-PROJECT on the main project state.
- Added minimal durable CCTB serialization/reload runtime.
- Added canonical durable Block A fixture.
- Added durable acceptance and negative-test coverage.

## DISCOVERIES
- The existing CCTB contract already provides the necessary deterministic identity and lineage primitives; durable storage can remain very small.
- Canonical bytes must be enforced on reload, not merely JSON-decode the artifact.
- The durable consumer path can remain explicitly conversation-independent by accepting only serialized block data plus consumer identity.

## DECISIONS
- Use canonical UTF-8 JSON as the first durable interchange boundary.
- Keep persistence repository-local and dependency-free for v0.1.
- Do not trigger GitHub Actions during this work.
- Do not claim verification without executable evidence.

## NAYA NOTES
- Every execution must leave one concrete next action.
- Maximize verified value per action.
- UNKNOWN stays UNKNOWN.
- Preserve exact evidence and tested commit identity.

## NEXT EXECUTION
**In an actual local NayaPOWER checkout of `cctb-v0.1-proof`, run the full available CCTB suite plus `tests/test_cct_durable.py`, run syntax checks, generate a durable machine-readable proof receipt containing exact commit SHA, A/B IDs and hashes, artifact hashes, lineage results, and negative-test results, then independently recompute the recorded identities; do not trigger GitHub Actions.**

## PROOF
- Protocol: `.naya/protocols/CCTB-PROTOCOL-v0.1.md`
- Runtime: `.naya/runtime/cct_protocol.py`
- Durable runtime: `.naya/runtime/cct_durable.py`
- Fixture: `tests/fixtures/cctb/a.json`
- Tests: `tests/test_cct_durable.py`
- CCTB continuation handoff: `.naya/handoffs/NEXT-EXECUTION-20260829-CCTB-TWO-NAYA-PROOF.md`
- Current state deliberately records implementation as awaiting executable test evidence.
