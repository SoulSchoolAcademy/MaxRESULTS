# 🔱 AI NOTE — NayaPOWER Superbrain Recovery Priority Status — 2026-08-29

## STATUS
ACTIVE • OPERATIONAL HANDOFF • NOT A GREEN CERTIFICATION

## MISSION
Make NayaPOWER trustworthy, operational, continuously learning, self-continuing, and high-performance so it can reliably produce extraordinary downstream work without premature promotion or deployment.

## CURRENT TRUTH

Canonical `main` remains:
`f875f85b025f880f4be2392980f2a8828019cea1`

Active implementation branch:
`naya-action-delivery-contract-v1`

Active branch HEAD at this note:
`0b8d4e8eac190f54e8175b79177247fd418b96be`

MAXIS: FROZEN.
Vercel: FROZEN.
Merge: FROZEN.
Authoritative CI verification: BLOCKED.

## WHAT HAS BEEN ACCOMPLISHED

1. The RED Actions board was reframed as a diagnosis problem rather than a code-editing problem.
2. GitHub Actions execution was isolated as the first blocker because affected runs fail below executable-step level.
3. A minimal `ubuntu-latest` diagnostic proved the failure boundary is before meaningful step execution.
4. Repository Actions UI was inspected; Actions are not visibly disabled. The self-hosted runner page reports no self-hosted runners, which is not a defect because the affected jobs request GitHub-hosted `ubuntu-latest` runners.
5. GitHub-side evidence and current community reports support an external hosted-runner/Actions execution anomaly, but the exact provider subcause remains UNKNOWN.
6. NayaPOWER workflow architecture was audited and substantial fan-out was proven: multiple workflows respond to the same commits; multiple workflows have write authority; several mutate and push; overlapping E00/Results repair pipelines exist.
7. The fan-out is a proven internal architectural problem. Whether it caused the external GitHub execution failure is UNKNOWN.
8. The Successor Torch / Next Action Delivery architecture was implemented on the isolated branch:
   - canonical Next Action Delivery contract;
   - reusable successor-torch template;
   - project execution validator integration;
   - continuity validator integration;
   - deliberate-negative contract coverage;
   - human continuation requirements;
   - successor context requirements.
9. Existing torch QA drift was discovered and corrected rather than weakening the new contract.

## PRIORITY ORDER

### PRIORITY 1 — RESTORE REAL GITHUB EXECUTION
Owner: execution/infrastructure lane + human/GitHub Support.
Status: BLOCKED.
Required proof:
`run created → job exists → runner assigned → Set up job → checkout → first executable step`.
Do not fix higher layers until this is real.

### PRIORITY 2 — PROVE THE SUCCESSOR TORCH
Owner: continuity/intelligence lane.
Status: SOURCE-COMPLETE / EXECUTION-UNVERIFIED.
No further semantic redesign is needed before real CI execution. Verification order is preserved below.

### PRIORITY 3 — WORKFLOW GOVERNANCE + CONSOLIDATION
Owner: architecture lane.
Status: READY TO ADVANCE.
Read-only specification must map every workflow to KEEP / CONTROL-PLANE / CONSOLIDATE / MANUAL ONLY / RETIRE before YAML changes.

### PRIORITY 4 — PIS / CIS LEARNING PROMOTION
Status: WAITING FOR VERIFIED ROOT-CAUSE EVENTS.
Do not promote hypotheses as verified learning.

### PRIORITY 5 — AUTHORITATIVE SUPERBRAIN GREEN
Only after the lower layers are genuinely proven.

## OPERATING MODEL

Maintain no more than two active lanes:

LANE A = Priority 1 execution-plane recovery.
LANE B = Priority 2/3 continuity + architecture advance.

A blocked lane does not freeze the entire mission. Advance the highest-value independent dependency while preserving the blocker.

## WHAT NOT TO DO

- Do not touch MAXIS.
- Do not deploy to Vercel.
- Do not merge unverified work.
- Do not repeatedly rerun a pre-execution failure.
- Do not add diagnostic workflows unless a materially new question requires one.
- Do not weaken validators.
- Do not convert UNKNOWN to VERIFIED.
- Do not treat CI GREEN as shipment authority.
- Do not treat deployment as product completion.
- Do not create workflow churn merely to provoke GitHub Actions.

## NAYA PERFORMANCE STANDARD

Every substantive execution must leave a complete operational torch:

`WHERE → WHY → CURRENT STATE → VERIFIED → UNKNOWN → PROTECTED → BLOCKED → DECISION → NEXT ACTOR → NEXT ACTION → READY-TO-RUN EXECUTION → EXPECTED OUTPUT → SUCCESS CRITERIA → VERIFICATION`.

When the human is the next actor, Naya authors the human action and exact return payload. The human should never have to invent the next prompt merely because Naya finished a task.

## NEXT VERIFICATION ORDER WHEN CI RETURNS

1. `python .naya/runtime/project_execution_contract.py self-test`
2. `python .naya/tests/test_project_prompt_contracts.py`
3. `python .naya/runtime/continuity_enforcement.py self-test`
4. `python .naya/tests/test_continuity_enforcement.py`
5. `python tools/qa_naya_torch_delivery.py`

STOP at the first real failure.

Then fix only that defect, rerun, and only after narrow GREEN run the authoritative Superbrain Gate against the exact tested SHA.

## GENERALIZED LEARNING

- RED is a symptom, not a diagnosis.
- Prove lower-layer execution before inferring higher-layer defects.
- Knowing the next action internally is not enough; Naya must deliver the executable torch.
- CI evidence and shipment authority are different controls.
- Excessive workflow fan-out is architectural debt even when individual workflows are valid.
- UNKNOWN must remain UNKNOWN until evidence changes it.

## SUCCESS CONDITION

`REAL EXECUTION → TORCH VERIFIED → FIRST REAL DEFECT FIXED → SUPERBRAIN GATE GREEN → WORKFLOW ARCHITECTURE CONSOLIDATED → PIS/CIS LEARN → SUPERBRAIN TRUSTWORTHY → HUMAN REVIEW → OSCAR/NIA ≥ 9 → HUMAN AUTHORIZATION → DOWNSTREAM PROMOTION`

## NEXT ACTOR
Team Naya / next execution Naya.

## NEXT ACTION
Restore the GitHub Actions execution plane and prove a real `ubuntu-latest` job reaches `Set up job`, checkout, and a first executable step. Do not proceed to contract tests until that proof exists.
