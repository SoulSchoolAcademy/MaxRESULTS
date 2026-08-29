# 🔱 NayaPOWER — Canonical Runtime Briefing

## WHERE
- **Canonical repository:** `SoulSchoolAcademy/NayaPOWER`
- **Canonical branch:** `main`
- **Last observed HEAD before this briefing update:** `09e76ed0a684d8e9531b5074c9ec665c46bb1d06`; resolve live `main` again before every substantive execution because this update creates a new commit.
- **MAXIS application repository:** `SoulSchoolAcademy/Maxis`
- **MAXIS deployment path:** `SoulSchoolAcademy/Maxis` → Vercel project `maxis`.
- **Canonical mission roadmap:** `.naya/MAXIS-NAYAPOWER-MASTER-MISSION-ROADMAP.md`

## WHY
Build Naya into a trusted AI operating partner and complete MAXIS through the verified critical path: Governance Green → Source/Deployment Parity → Golden Path → Experience Quality → Save/Claim/Hub → Mastery Loop → Platform Expansion.

## BUILDING
- **P1 ACTIVE:** close the NayaPOWER governance proof gap.
- Priority execution law remains: restore → re-score → select one highest-value executable action → execute → verify → learn → re-score → pass torch.
- Naya owns continuation determination and authors the human-facing continuation; the human is not required to author the next prompt.

## PROTECTED
- NayaPOWER governance, continuity, evidence, authority boundaries, and UNKNOWN semantics.
- Action Delivery Law and Continuous Torch-Pass.
- Naya-owned human continuation: `human_continuation` + `human_continuation_naya_authored`; `human_prompt_authoring_required = false`.
- Deliberate-negative fixtures must remain capable of failing.
- One canonical source of truth; no competing governance architecture.
- IMPLEMENTED ≠ TESTED ≠ VERIFIED ≠ RUNTIME-PROVEN ≠ PRODUCTION-PROVEN.
- Historical continuity records must not be rewritten.

## BLOCKED
- P1 Governance Green is not yet proven.
- GitHub Actions governance runs repeatedly conclude `failure` with no executable step records and unavailable logs.
- The current exact `main` before this briefing update was `09e76ed0a684d8e9531b5074c9ec665c46bb1d06`.
- A direct rerun of the current `Superbrain Gate` brain-gate job also produced a second attempt that again completed `failure` with `steps=[]` and logs returning `BlobNotFound`.
- No repository/test defect has been proven from this evidence.
- P2–P7 remain blocked by P1.

## VERIFIED
- Live `main` resolved to `09e76ed0a684d8e9531b5074c9ec665c46bb1d06` immediately before this briefing update.
- The commit changed only the Intelligence Feed document `MASTER-NOTES/INTELLIGENCE-FEED/2026-08-29-HIGH-PERFORMANCE-NAYAPOWER.md` in the observed commit metadata.
- The canonical governance workflows contain explicit executable steps, including checkout and Python validation.
- `tools/qa_naya_context_boot.py` enforces the Runtime Briefing first in cold-start order and explicit RED/GREEN acceptance behavior.
- `tools/qa_naya_execution_mode.py` machine-enforces action/continuation delivery.
- `tools/qa_naya_torch_delivery.py` contains a positive Naya-owned continuation fixture plus deliberate missing-continuation and non-Naya-authored negative fixtures.
- `CONTINUITY-ENFORCEMENT-POLICY.json` requires both `human_continuation` and `human_continuation_naya_authored` and sets `human_prompt_authoring_required` to false.
- `continuity_enforcement.py` enforces the structured handoff fields at the effective boundary.
- Current `Superbrain Gate` run `33256734930` on `09e76ed0a684d8e9531b5074c9ec665c46bb1d06` completed `failure`; its jobs `brain-gate` and `system-health-master-node` both completed `failure` with no materialized steps through the connected job surface.
- Rerunning brain-gate job `99111675520` succeeded as an accepted rerun request; the resulting run moved to attempt 2 and produced new jobs `99111877257` and `99111877725`, both `completed → failure` with `steps=[]`.
- Job-log retrieval for `99111877257` returned GitHub `BlobNotFound`.
- The parent commit `57920db5e8d026b5ffc6954460a95d2fcf8bc6e1` also had GitHub Actions failures, establishing that the pattern predates the latest Intelligence Feed commit.

## UNKNOWN
- The exact root cause of the GitHub Actions pre-step failures.
- The contents of the failure annotations.
- Whether GitHub assigned a runner before the failures.
- Whether the governance Python suite executes on GitHub at all for these runs.
- Full local reproduction of the repository-wide governance suite is not currently available because no repository checkout/runtime is mounted in the current execution environment.
- Governance is NOT GREEN.

## THIS WEEK
**ONE OBJECTIVE:** Establish a genuinely green governance foundation, then prove MAXIS source/deployment parity and the golden path without scattering execution.

## NEXT ACTION
**P1 / Governance evidence:** obtain an executable repository checkout/runtime and reproduce the exact governance commands from current `main` locally, then use the result to distinguish repository defects from the external GitHub Actions execution boundary. Do not modify governance source speculatively. After local reproduction, fresh CI must still prove GREEN before P1 closes.

## PROOF
P1 closes only when the exact current SHA is known, applicable governance workflows demonstrably execute, the relevant tests pass, deliberate-negative fixtures remain RED, fresh authoritative CI is GREEN at the exact tested SHA, and no material governance regression exists.

## LAST LEARNING
Repeated opaque GitHub failures are no longer the highest-value target for repeated annotation retrieval. The diagnostic method must change: reproduce the governed commands outside the opaque CI boundary, use that result to classify the failure, and only then repair a proven defect. The rerun reproduced the same pre-step failure pattern, strengthening the evidence boundary without proving a repository cause.
