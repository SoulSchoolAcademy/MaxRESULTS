# 🔱 NayaPOWER Workflow Governance & Consolidation Specification v1.0

## STATUS
READ-ONLY ARCHITECTURE SPECIFICATION • NO WORKFLOW CHANGES AUTHORIZED BY THIS DOCUMENT ALONE

## PURPOSE
Replace uncontrolled workflow fan-out with a governed Superbrain execution architecture while preserving required verification capability and the existing promotion/deployment separation.

## CURRENT MISSION
Restore and harden NayaPOWER before reopening downstream MAXIS promotion work.

## CURRENT PRIORITIES

1. **P1 — Restore real GitHub Actions execution.** Fresh runs have repeatedly failed before useful executable steps/jobs. Exact provider-side subcause remains UNKNOWN.
2. **P2 — Verify the Successor Torch / Next Action Delivery implementation** once real CI execution exists.
3. **P3 — Consolidate workflow architecture** using this specification and its frozen machine-readable inventory as the design baseline; no YAML changes are part of this specification.
4. **P4 — Promote only verified learning into PIS/CIS.**
5. **P5 — Earn trustworthy Superbrain GREEN and only then reopen downstream promotion.**

## TWO-LANE OPERATING MODEL

At most two active lanes:

- **Lane A:** P1 GitHub execution-plane recovery.
- **Lane B:** P2/P3 continuity + workflow architecture specification.

A blocked external lane must not create team-wide paralysis. A second lane may advance only if it does not modify or bypass the blocked proof boundary.

## FROZEN MACHINE-READABLE INVENTORY

Canonical inventory:

`.naya/memory/NAYA-POWER-WORKFLOW-INVENTORY-v1.json`

Inventory branch:
`naya-action-delivery-contract-v1`

Inventory source commit:
`70eaf17bad4fd95d6bb9898aaa6de5efbb18b490`

Inventory blob SHA:
`b4dc9bd8265d23a644f6fc3ecbf6f3285a629012`

Inventory URL:
https://github.com/SoulSchoolAcademy/NayaPOWER/blob/naya-action-delivery-contract-v1/.naya/memory/NAYA-POWER-WORKFLOW-INVENTORY-v1.json

The live branch contains **31 workflow files**, not 30. `intelligence-promotion.yml` was present in the live tree and was therefore included rather than silently omitted. The inventory records the discrepancy explicitly.

## KNOWN REPOSITORY FACTS

### Core / Superbrain
- `superbrain-gate.yml`
- `naya-control-plane.yml`
- `smart-brain-v3-enforcement.yml`
- `naya-memory-runtime.yml`
- `torch-pass-gate.yml`
- `naya-context-boot-guardrail.yml`
- `naya-claim-evidence-enforcement.yml`
- `naya-v3-architecture-lock.yml`

### Results / MAXESS / bridge / build
- `apply-maxess-result-bridge.yml`
- `build-aiscore-app-bridge.yml`
- `build-integrated-results.yml`
- `rebuild-integrated-results.yml`
- `rebuild-integrated-results-corrected.yml`
- `rebuild-integrated-results-final.yml`
- `rebuild-integrated-results-v3.yml`
- `maxess-result-hydration.yml`
- `maxess-step3-diagnostic.yml`
- `maxess-step3-runtime.yml`
- `maxess-terminal-isolation.yml`
- `maxess-v2-pretest.yml`

### Repair / execution / migration
- `repair-e00-terminal-state.yml`
- `repair-e00-results-handoff.yml`
- `repair-e00-results-handoff-v2.yml`
- `repair-e00-continue-v10.yml`
- `repair-e00-796-continue.yml`
- `patch-e00-continue.yml`
- `execute-score-hydration-v1.yml`
- `execute-maxess-section01.yml`
- `maxess-nitro-v2.yml`
- `e06-aaa-power-pass.yml`
- `intelligence-promotion.yml`

The machine-readable inventory is authoritative for the frozen pre-implementation topology. fileciteturn279file0

## PROVEN FAN-OUT CHARACTERISTICS

The audit has directly established these characteristics in multiple workflows:

- multiple workflows trigger on pushes to `main` or relevant push paths;
- multiple workflows hold `contents: write` permission;
- multiple workflows can mutate repository files;
- multiple workflows can commit and push;
- some mutation workflows include workflow-file paths inside push trigger scopes;
- overlapping E00/Results repair workflows exist;
- verification/governance logic is distributed across multiple independent workflow files.

Representative examples include the E00 repair family, Results/build workflows, and the intelligence promotion path.

## CAUSALITY DISCIPLINE

### PROVEN
Substantial workflow fan-out and autonomous mutation paths exist.

### POSSIBLE
This fan-out can amplify Actions demand, complicate concurrency, and increase diagnostic noise.

### UNKNOWN
Whether NayaPOWER fan-out caused the current GitHub hosted-runner execution failure.

Never convert POSSIBLE or UNKNOWN into PROVEN without new evidence.

## TARGET ARCHITECTURE

### Layer 1 — Authoritative Superbrain Control Plane

`superbrain-gate.yml` becomes the primary technical decision surface.

Its jobs may contain logically separate checks for:

- context/boot;
- continuity;
- claim/evidence integrity;
- architecture lock;
- successor torch;
- PIS/CIS integrity;
- retrieval/control-plane validation;
- other mandatory technical proofs.

Independent jobs are acceptable inside one authoritative control-plane workflow when they represent genuinely distinct checks.

### Layer 2 — Candidate Builders

Specialized build/repair workflows may create candidate state or artifacts.

They should normally NOT autonomously promote themselves to protected/main production state.

### Layer 3 — Verification

Verification may be invoked directly or as jobs in the control plane. Independent proof surfaces remain allowed where the evidence is genuinely distinct.

### Layer 4 — Human Promotion Gate

`BUILD → VERIFY → REPORT → HUMAN → OSCAR/NIA ≥9 → HUMAN AUTHORIZATION → SHIP`

### Layer 5 — Deployment

Vercel is downstream only after the promotion gate is satisfied.

## DISPOSITION FRAMEWORK

### KEEP / CONTROL-PLANE

`superbrain-gate.yml` — authoritative technical control plane nucleus.

Likely absorbed into its governed job structure where appropriate:
- `torch-pass-gate.yml`
- `naya-context-boot-guardrail.yml`
- `naya-claim-evidence-enforcement.yml`
- `naya-v3-architecture-lock.yml`
- `naya-control-plane.yml`
- `smart-brain-v3-enforcement.yml`
- `naya-memory-runtime.yml`
- `intelligence-promotion.yml`

Absorption must preserve independent check semantics and evidence, not merely delete files.

### CONSOLIDATE — E00 / Results Repair Family

Candidate family:
- `repair-e00-terminal-state.yml`
- `repair-e00-results-handoff.yml`
- `repair-e00-results-handoff-v2.yml`
- `repair-e00-continue-v10.yml`
- `repair-e00-796-continue.yml`
- `patch-e00-continue.yml`
- `build-integrated-results.yml`
- `rebuild-integrated-results.yml`
- `rebuild-integrated-results-corrected.yml`
- `rebuild-integrated-results-final.yml`
- `rebuild-integrated-results-v3.yml`

Target: one governed E00/Results candidate pipeline plus one verification surface, unless a specific independent proof requirement justifies separation.

### CONSOLIDATE — Results / Bridge / Hydration Family

Candidate family:
- `apply-maxess-result-bridge.yml`
- `build-aiscore-app-bridge.yml`
- `maxess-result-hydration.yml`
- `execute-score-hydration-v1.yml`

Target: one coherent Results transport/hydration candidate pipeline with explicit verification and no autonomous promotion.

### CONSOLIDATE / MANUAL-ONLY — MAXESS Execution Family

Candidate family:
- `execute-maxess-section01.yml`
- `maxess-nitro-v2.yml`
- `maxess-v2-pretest.yml`
- `maxess-terminal-isolation.yml`
- `maxess-step3-runtime.yml`
- `maxess-step3-diagnostic.yml`
- `e06-aaa-power-pass.yml`

Disposition depends on whether each is an implementation operation, independent verification surface, or historical migration artifact. They must not silently become production promotion authorities.

### RETIRE CANDIDATES

`execute-score-hydration-v1.yml` is a strong retirement candidate because it is a one-shot execution/migration pattern rather than a durable control-plane responsibility.

Other retirement candidates must be proven redundant before removal.

## MUTATION RULES FOR TARGET ARCHITECTURE

### Rule A — No autonomous self-promotion
A workflow may not combine implementation/repair with unilateral protected-branch promotion unless explicitly designated as part of a governed control-plane mechanism.

### Rule B — Minimize push-triggered mutation
Prefer candidate artifacts/branches and explicit human-controlled promotion over `workflow → git push → new workflow` chains.

### Rule C — No workflow-file self-trigger loops
A workflow that mutates workflow files must not use broad push triggers that cause uncontrolled recursive execution.

### Rule D — One decision surface
Checks that answer the same governance question should converge into the authoritative Superbrain control plane instead of becoming independent push-triggered workflows.

### Rule E — Preserve independent proof
Do not consolidate genuinely independent evidence merely to reduce run count. Consolidation is justified when the checks are redundant, causally coupled, or part of one decision.

### Rule F — Concurrency is deliberate
Every workflow must have an explicit reason for `cancel-in-progress: true` or `false`.

## PROPOSED EVENT FLOW

```text
CHANGE
  ↓
CONTROL-PLANE TRIGGER
  ↓
AUTHORITATIVE TECHNICAL CHECKS
  ↓
CANDIDATE / EVIDENCE
  ↓
HUMAN REVIEW
  ↓
OSCAR / NIA SCORECARD
  ↓
≥ 9.0 ?
  ├─ NO → REMEDIATION → VERIFY → RESCORE
  └─ YES → HUMAN SHIPMENT AUTHORIZATION
                         ↓
                       SHIP
                         ↓
                     DEPLOYMENT
                         ↓
                 PRODUCTION VERIFY
                         ↓
                   PIS / CIS LEARN
```

## REQUIRED PRE-IMPLEMENTATION INVENTORY

Before any YAML change, every workflow must be captured in the machine-readable inventory with:

- filename;
- trigger;
- branch filters;
- path filters;
- permissions;
- write capability;
- repository mutation;
- push/commit behavior;
- concurrency;
- downstream trigger possibility;
- duplicate family;
- independent-evidence justification;
- target disposition;
- replacement job/workflow;
- migration dependency;
- retirement condition.

Fields that have not been directly observed remain `UNKNOWN` in the inventory.

## IMPLEMENTATION ORDER

1. Freeze the current inventory as evidence. **COMPLETE.**
2. Finish the machine-readable workflow inventory. **COMPLETE at 31 live workflows.**
3. Produce the final target topology. **DEFINED in this specification; not yet implemented.**
4. Human review of this specification.
5. Implement the smallest consolidation tranche.
6. Verify the tranche independently.
7. Continue one tranche at a time.
8. Remove/retire legacy paths only after replacement proof exists.

## NON-REGRESSION

Never consolidate by:

- deleting a check without replacement evidence;
- weakening assertions;
- converting negative tests to positive;
- removing evidence requirements;
- suppressing failures;
- hiding workflows from the UI;
- using Vercel as a substitute verification environment.

## CURRENT READINESS

This document remains a **design baseline**, not authorization to change `.github/workflows/` yet.

The machine-readable inventory is now frozen and bound to this specification.

## NEXT ACTOR
Lane B — Naya architecture/continuity executor.

## NEXT ACTION
Obtain human review of the frozen 31-workflow inventory and target topology. Do not change workflow YAML until that review is complete and the smallest consolidation tranche is explicitly selected.
