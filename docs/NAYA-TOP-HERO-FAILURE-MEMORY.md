# Naya Top Hero — Nitro Failure Memory

## Scope
MAXESS Results Section 01 / Naya welcome hero.

## Failure
A top-presentation refinement could be written into the Section 01 runtime owner yet still fail to become the human-facing result because the generated Results artifact was not rebuilt, and because later Golden Master/runtime layers could overwrite earlier DOM text.

## Root cause
There are multiple governed runtime layers around Section 01. A successful source edit is therefore not proof of final presentation. The source owner, generated artifact, and deployed/live page must be treated as separate states.

## Immediate fix
1. Keep the refinement at the canonical V21 owner level.
2. Add an idempotent post-render Naya hero refinement that runs after the existing Section 01 layers.
3. Preserve the existing score source, Orb, Orbital Bead, and listen control.
4. Use the exact approved Naya asset already referenced by the current implementation.
5. Add deterministic static checks for the Naya copy, score label, Orbital Bead, and reduced-motion contract.
6. Require the governed Section 01 workflow to rebuild the generated Results artifact.

## System guardrails
- Never claim the live experience changed from a source-only edit.
- Never treat a GitHub commit as proof of Groove publication.
- Never treat a generated artifact as current until its SHA/state is re-fetched after the owner build.
- After every Section 01 owner change, verify the generated artifact contains the change.
- If a later runtime layer can overwrite a refinement, the refinement must either own the final runtime position or use an explicit post-render synchronization guard.
- Preserve one Results renderer; do not create a parallel preview/production renderer.
- If live visual inspection is unavailable, report `BLOCKED — LIVE VISUAL TEST UNAVAILABLE`; never convert that state to PASS.

## Current target copy
Naya title: `Hi, I'm Naya.`

Naya message: `I've got your results. Take a look through your report, and when you're ready, listen to me walk you through what it means.`

Primary action: `LISTEN TO NAYA`

Score identifier: `YOUR AI SCORE`

Score context: `Your score isn't a judgment. It's a signal — a snapshot of your current AI capability and a clue to where your next breakthrough could create the most leverage.`

## Protected components
- Approved Naya identity and asset
- Existing Naya listen/audio behavior
- Existing Section 01 order
- Existing score data binding
- Existing Orb
- Existing Orbital Bead core behavior
- Existing downstream Results sequence

## Verification state
- Repository identity: VERIFIED — `SoulSchoolAcademy/MaxRESULTS`
- Working branch: VERIFIED — `maxess-results-v21-working`
- Owner refinement commit: `df99347f04e69434cacffc45b79db05652a2875c`
- Workflow-trigger commit: `ddf7134cfb91e49e5a0ef9fb4908563f083f9c4e`
- Generated artifact rebuild: UNVERIFIED
- Live Results visual inspection: BLOCKED — public page could not be rendered by the available web inspector
- Groove visual inspection: BLOCKED — direct Groove rendering capability unavailable

## Lesson
The permanent standard is:

`OWNER PATCH → GENERATED REBUILD → REFETCH → RENDER → VISUAL INSPECTION → OSCAR → REPAIR → REGRESSION`

Anything shorter is engineering progress, not release completion.
