# 🔱 TEAM NAYA NOTE — Superbrain Recovery Operating Board — 2026-08-29

## PURPOSE
Give every Team Naya executor the same current mission, priorities, constraints, evidence, and next move so parallel work stays coordinated and high-value.

## NORTH STAR
Make NayaPOWER trustworthy, operational, continuously learning, self-continuing, and high-performance before using it as the engine for extraordinary downstream MAXIS work.

## CURRENT STATE

Canonical main:
`f875f85b025f880f4be2392980f2a8828019cea1`

Active branch:
`naya-action-delivery-contract-v1`

Active branch HEAD when recorded:
`0b8d4e8eac190f54e8175b79177247fd418b96be`

MAXIS: FROZEN.
Vercel: FROZEN.
Merge: FROZEN.

## TEAM PRIORITY BOARD

### P1 — GITHUB EXECUTION PLANE 🔴
Objective: restore actual GitHub-hosted runner execution.

Required proof:
`run created → job exists → runner assigned → Set up job → checkout → first executable step`.

Current evidence shows fresh runs can fail before executable jobs/steps. Exact GitHub subcause remains UNKNOWN.

Team behavior:
- preserve evidence;
- continue provider/account investigation only where authorized;
- do not edit higher layers to compensate for missing execution;
- do not create repeated diagnostics without a materially new question.

### P2 — SUCCESSOR TORCH 🟡
Objective: verify the implemented Next Action Delivery / Successor Torch contract.

Source implementation includes:
- canonical torch schema;
- successor template;
- project contract integration;
- continuity validator integration;
- deliberate-negative coverage;
- conditional human continuation;
- human return payload requirements.

Status: source-complete, execution-unverified.

When P1 clears, run in exact order:
1. `python .naya/runtime/project_execution_contract.py self-test`
2. `python .naya/tests/test_project_prompt_contracts.py`
3. `python .naya/runtime/continuity_enforcement.py self-test`
4. `python .naya/tests/test_continuity_enforcement.py`
5. `python tools/qa_naya_torch_delivery.py`

STOP AT FIRST REAL FAILURE.

### P3 — WORKFLOW GOVERNANCE + CONSOLIDATION 🟡
Objective: replace workflow swarm behavior with a controlled architecture.

Proven findings:
- substantial workflow fan-out;
- multiple workflows react to the same pushes;
- multiple workflows have write permission;
- multiple workflows mutate/push;
- overlapping E00/Results repair pipelines exist;
- governance/verification is fragmented across multiple workflow surfaces.

Causality warning:
The fan-out is proven. Whether it caused the current GitHub execution failure is UNKNOWN.

Current deliverable:
`NAYA POWER WORKFLOW GOVERNANCE & CONSOLIDATION SPECIFICATION`

This is analysis/specification first. No YAML changes until the specification is reviewed.

### P4 — PIS/CIS LEARNING 🟡
Promote only verified lessons.

Core candidate lessons:
- RED is a symptom, not a diagnosis.
- Lower-layer execution must be proven before higher-layer defects are inferred.
- Knowing the next action is insufficient; the successor must receive an executable torch.
- CI GREEN is technical evidence, not shipment authority.
- Deployment success does not equal product completion.
- Workflow fan-out is architectural debt.
- UNKNOWN remains UNKNOWN until evidence changes it.

### P5 — SUPERBRAIN GREEN 🔵
Finish only after lower layers are proven:
`real CI → narrow verification → authoritative gate → exact-SHA proof → durable learning → trustworthy Superbrain`.

## TWO-LANE OPERATING RULE

At most two active lanes:

LANE A: P1 execution-plane recovery.
LANE B: P2/P3 continuity and architecture advancement.

Do not create a third active workstream unless a higher-priority blocker makes it necessary and one existing lane is formally closed or paused.

## PROMOTION RULE

No work moves from:
`BUILDING → SHIPPED/DEPLOYED`
without:
`VERIFY → HUMAN REVIEW → OSCAR/NIA SCORE ≥9 → HUMAN AUTHORIZATION`.

Vercel is a deployment destination, not a debugging loop.

## DAILY STATUS REQUIREMENT

Every substantive Team Naya update must state:

`WHERE`
`WHY`
`CURRENT PRIORITIES`
`ACTIVE LANES`
`BLOCKERS`
`COMPLETED`
`VERIFIED`
`UNKNOWN`
`PROTECTED`
`NEXT DECISION`
`NEXT ACTOR`
`NEXT ACTION`
`READY-TO-RUN NEXT PROMPT`

## TEAM HANDOFF REQUIREMENT

Do not end with a summary only.
The final artifact of every execution cycle is an operational torch that lets the successor act without reconstructing the conversation.

## DO NOT

- touch MAXIS during the active NayaPOWER recovery mission;
- deploy to Vercel;
- merge unverified work;
- weaken validators;
- turn UNKNOWN into VERIFIED;
- launch redundant workflow experiments;
- optimize for number of workflow runs;
- let a blocked external lane create team-wide paralysis.

## SUCCESS CONDITION

`P1 REAL EXECUTION`
→ `P2 TORCH VERIFIED`
→ `FIRST REAL DEFECT FIXED`
→ `AUTHORITATIVE SUPERBRAIN GATE GREEN`
→ `P3 WORKFLOW CONSOLIDATION`
→ `P4 PIS/CIS LEARNING`
→ `SUPERBRAIN TRUSTWORTHY`
→ `HUMAN REVIEW`
→ `OSCAR/NIA ≥9`
→ `HUMAN AUTHORIZATION`
→ `DOWNSTREAM PRODUCT PROMOTION`

## NEXT ACTOR
Lane A execution Naya + Lane B architecture/continuity Naya.

## NEXT ACTION
Maintain the two active lanes: continue the GitHub execution-plane escalation, while Lane B produces the Workflow Governance & Consolidation Specification without changing any workflow yet.
