# MAXESS SECTION EXECUTION WORKFLOW

Status: AUTHORITATIVE EXECUTION WORKFLOW
Version: V21 AAA Reference Implementation

## Goal

Turn the MAXESS design specification into visible product progress.

This workflow exists to prevent the project from spending cycles on infrastructure while the product remains visually unchanged.

## The loop

READ → SCORE → PRIORITIZE → MUTATE → PROVE → BUILD → VERIFY → RESCORE → FREEZE → CONTINUE

## Step 1 — READ

Before changing a section, read:

- Master Contract
- Section Design Specification
- Priority Matrix
- Change Ledger
- Smart Notes
- relevant HMC reference/design files
- actual current source owner

Do not rely on conversation memory for durable decisions.

## Step 2 — SCORE

Score the current section 0–10 across:

- purpose
- clarity
- personalization
- content
- interpretation
- visual communication
- design
- tactility
- UX
- function
- data integrity
- reliability
- responsive
- accessibility
- performance
- emotional impact
- trust
- release confidence

Create one section score and one largest-gap statement.

## Step 3 — PRIORITIZE

Use `docs/MAXESS-PRIORITY-MATRIX.md`.

Choose the highest-value section/gap currently available.

Do not choose work merely because it is easy.

Do not choose tooling work when a safe product improvement is available.

## Step 4 — MUTATE

Change the actual product source owned by the section.

Do not finish a section by only changing:

- QA scripts;
- repair scripts;
- documentation;
- inventories;
- reports;
- generated metadata.

A section requires a real product delta.

## Step 5 — PROVE

Immediately prove:

- source hash changed;
- expected selectors/classes/content changed;
- no duplicate renderer was introduced;
- no second result source was introduced;
- preservation requirements still exist;
- real data remains authoritative.

If the source does not change, the execution is NOT COMPLETE.

## Step 6 — BUILD

Rebuild the canonical artifact from the authoritative source.

Record:

- baseline hash;
- candidate hash;
- line count;
- build result.

A changed source with an unchanged candidate means the builder may not own that source correctly. Diagnose the ownership layer.

## Step 7 — VERIFY

Run only the verification required for the changed area plus the regression suite.

Classify failures:

PRODUCT
BUILD
VALIDATOR
DATA
DEPENDENCY
ENVIRONMENT

Fix the correct owner.

Never change product code just to satisfy a stale validator.

## Step 8 — RESCORE

Review the actual section again.

Ask:

“Why is this not a 10?”

Then identify the largest remaining gap.

Do not polish random details while a major visible weakness remains.

## Step 9 — FREEZE

A section can become FROZEN only when all applicable evidence exists.

Freeze means:

- preserve unless a later contract change explicitly reopens it;
- no casual redesign while working elsewhere;
- regression protection remains active.

## Step 10 — CONTINUE

Immediately select the next highest-value incomplete section.

Do not ask the human what to do next unless a material decision genuinely requires the human.

## Batch rules

Preferred batch size: 3 coherent sections.

Do not create five different executor scripts for one batch.

One batch should ideally produce:

- 3 real product mutations;
- 1 build;
- targeted verification;
- regression verification;
- one updated scorecard.

## Communication protocol

Every meaningful execution report must include:

WHAT I DID
WHAT I FOUND
WHAT REMAINS
YOUR NEXT MOVE
SUGGESTED PROMPT

The Suggested Prompt must preserve current state and identify the next objective so context can continue without reconstruction.

## Smart Notes protocol

Record only durable lessons that can prevent future failure.

Good Smart Note:

“Builder source was a giant JS string; line-oriented regex was brittle. Use structural HTML markers or an explicit section manifest.”

Bad Smart Note:

“Build failed.”

## Reference-learning protocol

When a high-quality reference is discovered:

REFERENCE → OBSERVE → EXTRACT PRINCIPLE → DEFINE STANDARD → APPLY → SCORE → VERIFY → STORE LESSON

Do not blindly copy references. Extract the underlying principle.

## Definition of progress

Real progress is one of:

1. a material product source change;
2. a material candidate artifact change;
3. a section reaching verified FROZEN state;
4. a release blocker being removed;
5. a reusable execution safeguard that prevents a known recurring failure.

Anything else is support work and should remain subordinate to product progress.

## Definition of completion

MAXESS is complete only when:

- all material sections are FROZEN or explicitly accepted as complete;
- all cross-section quality layers pass;
- real result handoff is proven;
- PDF/print is proven;
- deployment is proven;
- human review is complete;
- no critical regression remains;
- the project can serve as the reference proof for the AI Product Creation System.
