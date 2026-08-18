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

Score the current section against its explicit AAA criteria.

The score is diagnostic, not permission to declare the whole page finished.

## Step 3 — PRIORITIZE

Choose the highest-value unfinished section using the current Priority Matrix.

Product work outranks another tool or document unless the tool/document is a real release blocker.

## Step 4 — MUTATE

Change the actual product owner.

For the canonical V21 implementation, Batch 1 uses:

`tools/execute_maxess_batch1_v2.py`

This executor edits `tools/build_v21_canonical.py` at stable ownership anchors and refuses to report success when no source delta exists.

An existing AAA marker, Nitro layer, or previous patch is never treated as proof of completion.

## Step 5 — PROVE

Before build, prove:

- source hash changed;
- intended section implementation changed;
- no duplicate renderer was introduced;
- authoritative data source remains intact;
- preserved functionality remains.

## Step 6 — BUILD

Run the canonical builder.

## Step 7 — VERIFY

Run:

- Candidate QA
- Experience QA
- Runtime Contract QA
- Design System QA
- Interaction / Release QA

Classify any failure by ownership before changing code.

## Step 8 — RESCORE

Inspect the rebuilt artifact and rescore the changed section against its AAA criteria.

## Step 9 — FREEZE

Only freeze a section when the relevant human and technical evidence exists.

## Step 10 — CONTINUE

Immediately choose the next highest-value unfinished section. Do not reopen completed work without evidence that a higher-priority requirement requires it.

## Anti-no-op rule

Every meaningful execution cycle must either:

1. produce a real product source delta; or
2. report a real blocker with evidence.

A successful build of unchanged source is not product progress.

## Batch 1

1. Naya Arrival / Orientation
2. MAXESS Score / Signature Orb
3. What Your Score Means

The current executable path is:

`python tools/execute_maxess_batch1_v2.py`

followed by the standard build and QA chain.
