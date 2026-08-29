# NayaPOWER — CURRENT PROJECT

**Status:** ACTIVE CANONICAL PROJECT STATE
**Updated:** 2026-08-29
**Branch:** `cctb-v0.1-proof`

## MISSION
Make NayaPOWER a trusted, high-performance, continuously improving AI operating system whose intelligence, execution, verification, continuity, and learning compound across successor Nayas.

## OBJECTIVE
Integrate the CCTB v0.1 durable proof receipt into one canonical publication path without duplicating the independent verifier, while preserving the tested/verified versus runtime-proven boundary.

## CURRENT STATE
- NayaPOWER Runtime Briefing remains the canonical runtime authority.
- CURRENT-PROJECT is the canonical active project execution state; it does not replace the Runtime Briefing.
- CCTB v0.1 deterministic A→B→successor proof is established.
- Minimal durable JSON serialization/reload implementation, canonical fixture, acceptance tests, and machine-readable durable proof receipt are present.
- A canonical publication manifest now links the existing MVP proof and durable proof receipt and explicitly records that runtime/production proof is not required for this local publication state.
- GitHub repository operations are available; GitHub Actions remain intentionally paused.

## VERIFIED
- Existing canonical MVP proof remains `proofs/cctb-v0.1-mvp-proof.json` and its independent verifier remains `.naya/runtime/cct_mvp_second_pass.py`.
- Durable proof receipt remains `proofs/cctb-v0.1-durable-proof-receipt.json` and records 12 locally executed CCTB tests with independent recomputation.
- The durable receipt records A/B identities, artifact hashes, lineage ID/hash, independent consumption, and all four required durable negative-test categories.
- `proofs/cctb-v0.1-publication.json` is now the canonical publication manifest linking the MVP proof and durable receipt without introducing a second CCTB verifier.
- Publication manifest explicitly preserves `TESTED/VERIFIED LOCALLY` and does not claim runtime-proven or production-proven.

## BLOCKED
- A fresh private-repository checkout cannot be performed inside the current ChatGPT container because outbound GitHub network/DNS access is unavailable.
- GitHub Actions execution is paused because the monthly Actions allocation is exhausted; do not trigger it.
- Therefore newly integrated publication-path changes have not been locally executed in a real checkout in this environment.

## RISKS
- The publication manifest currently references the Git blob identities of the two canonical proof artifacts; any artifact-content change requires the manifest references to be regenerated.
- Do not duplicate CCTB verification logic in the publication layer.
- Do not convert repository inspection into test evidence.
- Preserve the distinction IMPLEMENTED ≠ TESTED ≠ VERIFIED ≠ RUNTIME-PROVEN ≠ PRODUCTION-PROVEN.

## PRIORITIES
1. **P0 — Execute and independently verify the publication manifest integration in a real local checkout when an execution-capable local environment is available, without triggering GitHub Actions.**
2. **P0 — Maintain deterministic durable interchange and independent A→B→successor verification.**
3. **P1 — Continue Promotion Engine V1 deterministic/local readiness while Actions remain paused.**
4. **P1 — Audit NayaPOWER source-of-truth duplication and runtime enforcement.**
5. **P2 — Optimize runtime retrieval, context recovery, and execution efficiency after correctness remains stable.**

## ACTIVE WORK
CCTB durable interchange is TESTED/VERIFIED through isolated exact-source execution at the recorded tested commit. Publication-path integration is implemented as a minimal manifest but awaits executable local validation of the new repository state.

## COMPLETED
- Established canonical CURRENT-PROJECT.
- Added minimal durable CCTB serialization/reload runtime.
- Added canonical durable Block A fixture.
- Added durable acceptance and negative-test coverage.
- Executed 12 available CCTB tests in isolated local execution of the exact repository source.
- Independently recomputed durable identities and lineage.
- Created `proofs/cctb-v0.1-durable-proof-receipt.json`.
- Added `proofs/cctb-v0.1-publication.json` as the smallest canonical publication manifest linking the existing proof artifacts.

## DISCOVERIES
- The existing independent second-pass verifier is already the correct verification authority; the publication layer should link to it, not reproduce it.
- The durable receipt already contains the durable evidence needed for publication, so no new durable verifier is required.
- A small deterministic manifest is sufficient to establish one canonical publication surface without databases, services, federation, or UI.

## DECISIONS
- Keep canonical MVP proof and durable receipt as separate evidence artifacts.
- Use one publication manifest to link those artifacts and state their proof boundary.
- Reuse `.naya/runtime/cct_mvp_second_pass.py` as the independent verifier.
- GitHub Actions remain paused.
- Do not claim runtime-proven or production-proven without corresponding execution evidence.
- Every execution must leave one concrete next action.

## NAYA NOTES
- Maximize verified value per action.
- UNKNOWN stays UNKNOWN.
- Back-to-back Nayas must inherit CURRENT-PROJECT rather than reconstructing state from conversation.
- Repository access is allowed; only GitHub Actions are paused.

## NEXT EXECUTION
**In an execution-capable local checkout of `cctb-v0.1-proof`, run the complete CCTB MVP + durable suites and a publication-manifest validation that confirms both canonical proof artifacts are present, their recorded identities match, the existing independent verifier remains authoritative, and the manifest does not elevate local TESTED/VERIFIED evidence to runtime/production proof; independently recompute the artifact identities, then update this project state with exact results. Do not trigger GitHub Actions.**

## PROOF
- Protocol: `.naya/protocols/CCTB-PROTOCOL-v0.1.md`
- Core runtime: `.naya/runtime/cct_protocol.py`
- Durable runtime: `.naya/runtime/cct_durable.py`
- MVP proof runtime: `.naya/runtime/cct_mvp_proof.py`
- Independent verifier: `.naya/runtime/cct_mvp_second_pass.py`
- MVP tests: `tests/test_cct_mvp.py`
- Durable tests: `tests/test_cct_durable.py`
- Durable proof receipt: `proofs/cctb-v0.1-durable-proof-receipt.json`
- Publication manifest: `proofs/cctb-v0.1-publication.json`
- Previously tested source commit: `68aee910dcdf14c328185de788817c7392f52f68`
- Current integration commit: `bd3740f3f5c436e4c8df0228ee2716b71c606e00`
