# NEXT EXECUTION — CCT MVP PROOF

## project
SoulSchoolAcademy/NayaPOWER — CCTB / NayaNet

## north_star
Maximize verified value per action while enabling permissioned, provenance-preserving exchange and compounding of intelligence between autonomous Nayas.

## current_state
CCTB v0.1 Intelligent Block reference implementation and focused MVP proof are implemented on the isolated branch `cctb-v0.1-proof`. The proof was executed locally against the implementation model and a separate second-pass verifier independently re-read and recomputed the generated machine-readable proof.

## completed_work
- Hardened `.naya/runtime/cct_protocol.py` with required source-context semantics, deterministic content hashing, validation, permissions, provenance, consumption, and lineage verification.
- Added `.naya/runtime/cct_mvp_proof.py` for the two-Naya proof and negative attack matrix.
- Added `.naya/runtime/cct_mvp_second_pass.py` as a separate proof verifier.
- Added `tests/test_cct_mvp.py` with five focused regression tests.
- Recorded `.naya/proofs/cctb-v0.1-mvp-proof.json`.

## verified_evidence
Local execution on 2026-08-29 produced GREEN for Block A creation/validation/evidence/provenance/permissions, independent Naya B consumption, Block B creation, B→A lineage, independent lineage verification, negative tests, tamper detection, permission enforcement, conversation independence, machine-readable proof, and second-pass verification. Focused regression suite: `5 passed`.

Proof block IDs:
- A: `sha256:f05d6fe8b072927a89f2756d7f9d0fa2bcf4c70840c34e846b2cfc9ee25a1bef`
- B: `sha256:64d74b222bd5d0e1c71706a63f9912b503b52ce48cc92a5005a3ad17dc85e063`

## unresolved_issues
- This local proof does not establish GitHub-hosted clean-checkout execution.
- The implementation has not yet been integrated with CIS/PIS; that is intentionally deferred until the MVP proof is independently verified.
- The repository branch must still undergo normal review/merge governance before becoming canonical.

## constraints
- Do not trigger GitHub Actions during this handoff unless a later execution explicitly authorizes the single high-value remote gate.
- Do not claim repository-wide GREEN from local proof alone.
- Do not integrate CIS/PIS before the two-Naya proof remains GREEN after repository-native execution.

## current_objective
Establish the CCTB v0.1 two-independent-Naya proof as repeatable repository-native evidence, then integrate the proven protocol with CIS/PIS.

## next_action
Review the isolated-branch diff, then run the exact CCT MVP proof and focused tests from the repository working tree. If those remain GREEN, prepare one deliberately scoped remote CI gate whose sole purpose is clean GitHub-hosted checkout verification.

## execution_instructions
1. Inspect current HEAD and diff.
2. Run `python -m py_compile .naya/runtime/cct_protocol.py .naya/runtime/cct_mvp_proof.py .naya/runtime/cct_mvp_second_pass.py`.
3. Run the CCT MVP proof.
4. Run the separate second-pass verifier against the generated proof.
5. Run the focused CCT tests.
6. Inspect the machine-readable proof and verify every acceptance line.
7. Do not touch CIS/PIS until all above remain GREEN.
8. Record results and preserve the proof artifact.

## success_criteria
- CCT MVP proof GREEN.
- Second-pass verification GREEN.
- Focused regression GREEN.
- No false remote-CI claim.
- Evidence artifact is machine-readable and inspectable.

## verification_requirements
Verification must be based on execution evidence, not file existence or prior claims. The independent verifier must recompute block hashes, permissions, and lineage from the stored proof. Any failure is RED and must be repaired before advancement.
