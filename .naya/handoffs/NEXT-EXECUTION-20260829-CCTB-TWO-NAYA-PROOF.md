# NEXT EXECUTION — CCTB v0.1 → DURABLE BLOCK/TRANSPORT PROOF

schema_version: 2
status: READY

## Project
Naya Power Superbrain → NayaNet / Collective Chain Technology (CCT) protocol foundation

## North Star
Enable permissioned personal AIs to exchange verified learning as portable intelligent blocks, preserving provenance, trust, ownership, and lineage while allowing useful knowledge to compound across the collective.

## Current State
CCTB v0.1 is formally defined and its deterministic two-Naya reference proof has been executed locally against the exact implementation commit `ddb772234704c2d5926c8c37100c0d2fae1d3d87`. Naya A creates a verified block; Naya B independently consumes it with no originating conversation; B creates a linked successor; lineage, tamper detection, and permission enforcement all pass. Remote GitHub Actions were intentionally not triggered because the account Actions allocation is exhausted/blocked externally.

## Completed Work
- Defined CCT as an intelligence-provenance network architecture, not a blockchain transaction ledger.
- Defined CCTB as the portable intelligent-block protocol.
- Defined Contract, Trust, Network, and Proof layers.
- Implemented deterministic canonical hashing and block IDs.
- Implemented evidence and verification requirements.
- Implemented permission-scoped consumption.
- Implemented independent consumption without conversation context.
- Implemented parent ID/hash lineage.
- Implemented tamper detection and unauthorized-consumer rejection.
- Executed the two-Naya A→B→successor proof locally.
- Recorded machine-readable evidence in `.naya/memory/CCTB-V0.1-PROOF-RECEIPT.json`.
- Recorded the durable protocol definition in `.naya/protocols/CCTB-PROTOCOL-v0.1.md`.
- Recorded the protocol work in GitHub Issue #83.

## Verified Evidence
- Reference implementation: `.naya/runtime/cct_protocol.py`.
- Protocol specification: `.naya/protocols/CCTB-PROTOCOL-v0.1.md`.
- Proof receipt: `.naya/memory/CCTB-V0.1-PROOF-RECEIPT.json`.
- Tested SHA: `ddb772234704c2d5926c8c37100c0d2fae1d3d87`.
- Root block: `sha256:f607e8a69fbb7f4502e1c737f7f3bc5928c502f87a72e6d642d1316721e8e94a`.
- Successor block: `sha256:37476ab0f9a2bc073ec32c6dcffeecb10b764a3e38186e3abe969bb33e420ebd`.
- Proof output: A creates GREEN; B consumes independently GREEN; B creates linked successor GREEN; lineage GREEN; tamper detection GREEN; permission enforcement GREEN.

## Unresolved Issues
- The proof currently uses in-memory blocks; durable block persistence and transport are not implemented.
- Cryptographic signing/identity, revocation, selective disclosure, contradiction resolution, reputation, discovery, routing, and federation policy remain future layers.
- The protocol must remain clearly differentiated from blockchain: no global consensus or transaction ledger is required.
- A remote clean-checkout verification should occur later when GitHub Actions is available, but it is not a prerequisite for the local protocol proof.

## Constraints
- Privacy by default; sharing is permissioned.
- Provenance, evidence, verification state, and uncertainty must remain attached to trusted intelligence.
- Never promote an unverified claim to verified intelligence.
- Do not build federation-scale infrastructure before the smallest protocol remains stable.
- Preserve the Superbrain 1.0 deterministic, GitHub-native baseline.
- Follow MPA — Maximum Value Per Action: batch, execute, verify, record, compound, stop.
- Do not trigger GitHub Actions merely to repeat deterministic local proof.

## Current Objective
Turn the proven in-memory CCTB primitive into the smallest durable interchange format and storage/transport boundary while preserving independent verification and lineage.

## Next Action
Design and implement a minimal durable CCTB fixture format plus a repository-local A→B acceptance test that writes A's block to durable storage, loads it as B with no conversation context, verifies it, writes B's linked successor, reloads both, and verifies the lineage end-to-end.

## Execution Instructions
1. Inspect `.naya/protocols/CCTB-PROTOCOL-v0.1.md` and `.naya/runtime/cct_protocol.py` before changing them.
2. Preserve the existing deterministic block contract and current self-test.
3. Add the smallest repository-local durable fixture/consumer path; do not introduce a database, external vector service, network daemon, or UI.
4. Make the consumer receive only the serialized block and explicit permission identity.
5. Prove the serialized block recomputes the same block ID after reload.
6. Prove B's successor references A by both parent block ID and parent block hash.
7. Add negative tests for tampering and unauthorized consumption after serialization/reload.
8. Run local syntax, CCTB self-test, and durable two-Naya acceptance tests.
9. Record exact tested SHA and machine-readable proof evidence.
10. Do not trigger remote Actions unless the local proof is completely GREEN and a later execution explicitly authorizes the high-value clean-checkout verification.

## Success Criteria
- Durable serialization/reload preserves canonical block identity.
- B independently consumes the durable A block without chat history.
- B creates a durable linked successor.
- Parent ID/hash lineage survives reload and verifies.
- Tampering after storage is detected.
- Unauthorized consumption remains RED.
- Existing CCTB self-test remains GREEN.
- Evidence is tied to the exact tested commit.

## Verification Requirements
- Exact repository: `SoulSchoolAcademy/NayaPOWER`.
- Record exact tested SHA.
- Run the actual repository implementation, not a recreated approximation.
- Demonstrate A→B independent consumption from durable storage.
- Demonstrate B→successor durable lineage.
- Demonstrate tamper detection and permission denial.
- Confirm zero originating conversation/context dependency.
- Preserve existing protocol specification and self-test.
- Record a machine-readable receipt before declaring the execution complete.
