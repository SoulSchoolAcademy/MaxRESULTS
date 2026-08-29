# NEXT EXECUTION — CCTB TWO-NAYA PROTOCOL PROOF

schema_version: 1
status: READY

## Project
Naya Power Superbrain → NayaNet / Collective Chain Technology (CCT) protocol foundation

## North Star
Enable permissioned personal AIs to exchange verified learning as portable intelligent blocks, preserving provenance, trust, ownership, and lineage while allowing useful knowledge to compound across the collective.

## Current State
CCTB v0.1 has been formally defined as the block protocol for Collective Chain Technology. The reference implementation defines deterministic block identity, evidence, verification state, permission scope, provenance, independent consumption, tamper detection, and parent lineage. The smallest two-Naya proof is implemented as a deterministic local self-test. No federation infrastructure or remote CI is required for this proof.

## Completed Work
- Defined CCT versus blockchain boundary: CCT is not a transaction ledger and does not require global consensus, mining, cryptocurrency, or one universal chain.
- Defined CCTB as the portable intelligent-block protocol.
- Defined Contract, Trust, Network, and Proof layers.
- Implemented deterministic canonical hashing and block IDs.
- Implemented verified evidence and permission checks.
- Implemented independent consumer validation with zero originating conversation context.
- Implemented linked successor creation and parent lineage verification.
- Implemented tamper detection and permission-denial tests.
- Recorded the protocol as GitHub Issue #83.

## Verified Evidence
- CCTB specification: `.naya/protocols/CCTB-PROTOCOL-v0.1.md`
- Reference implementation: `.naya/runtime/cct_protocol.py`
- The local CCTB self-test demonstrates A creates a verified block, B independently consumes it, B creates a linked successor, lineage verifies, tampering is detected, and unauthorized consumption is rejected.
- CCTB v0.1 intentionally stops at the smallest proof before federation-scale engineering.

## Unresolved Issues
- The two-Naya proof must be executed from the exact repository checkout and its output recorded as durable machine-readable evidence.
- Real transport, persistent block storage, key/signature infrastructure, revocation, conflict resolution, selective disclosure, reputation, and federation routing are not yet implemented.
- CCTB must not be marketed as a blockchain; the protocol comparison should remain explicit and accurate.

## Constraints
- Privacy by default; sharing is permissioned.
- Provenance and evidence must remain attached to every trusted block.
- Unverified claims must never be promoted to verified intelligence.
- Do not build federation-scale infrastructure before the smallest A→B→successor proof is GREEN.
- Preserve the Superbrain 1.0 GitHub-native, deterministic, zero-cost baseline.
- Follow MPA — Maximum Value Per Action: batch work, verify it, record it, and stop when evidence is sufficient.

## Current Objective
Prove CCTB v0.1 end-to-end with two independent Naya identities and establish the minimum machine-verifiable protocol boundary before adding network infrastructure.

## Next Action
Run `.naya/runtime/cct_protocol.py self-test` from a clean checkout of the exact current HEAD, capture the complete output, then add a machine-readable CCTB proof receipt if the test is GREEN. Do not build federation infrastructure until this proof is GREEN.

## Execution Instructions
1. Inspect the exact HEAD and confirm the CCTB specification and reference implementation are present.
2. Run `python .naya/runtime/cct_protocol.py self-test`.
3. Verify the output proves A→B consumption, B→successor creation, lineage, tamper detection, and permission enforcement.
4. Independently review the implementation for conversation/context dependencies: the proof inputs must be repository-local objects only.
5. If the test fails, repair the actual protocol defect and rerun the smallest failing proof.
6. If GREEN, create a durable machine-readable proof receipt containing tested SHA, root block ID, successor block ID, and verification result.
7. Do not add transport, database, federation routing, signatures, or UI until the smallest protocol proof is proven.

## Success Criteria
- CCTB v0.1 self-test exits successfully.
- Naya A creates a deterministic verified intelligent block.
- Naya B independently consumes A's block without conversation history.
- Naya B creates a new block linked to A by parent ID and parent hash.
- Parent lineage is independently verified.
- Tampering is detected.
- Unauthorized consumption is rejected.
- The result is recorded as durable evidence tied to the exact tested SHA.

## Verification Requirements
- Exact repository: `SoulSchoolAcademy/NayaPOWER`.
- Exact commit SHA must be recorded.
- Run the reference implementation rather than relying on static inspection.
- Confirm the root block ID recomputes deterministically.
- Confirm the successor parent ID/hash matches the root block.
- Confirm permission denial is enforced.
- Confirm tampering changes the validation result to RED.
- Confirm no originating chat/context is passed to the consumer.
- Record the final proof output and receipt in the repository.
