# NAYA PRODUCT EXECUTION LANES

Status: AUTHORITATIVE OPERATING RULE
Repository: SoulSchoolAcademy/MaxRESULTS
Branch: maxess-results-v21-working

## Purpose
Prevent the AI Product Creation System from getting trapped in a verification loop where tooling changes continue but the actual product does not materially change.

## Two-Lane Model

### LANE A — PRODUCT MUTATION

The AI must make measurable changes to the real product whenever the Change Ledger contains actionable incomplete requirements.

Required sequence:

1. Read the Master Contract.
2. Read the Change Ledger.
3. Inspect the real authoritative product source.
4. Select the highest-value coherent product batch.
5. Modify the real product source.
6. Prove the source changed by diff/hash/line or structural evidence.
7. Record the change immediately.

### LANE B — VERIFICATION

After a product batch is created:

1. Build.
2. Validate syntax.
3. Run static QA.
4. Run runtime QA.
5. Run regression tests.
6. Run responsive/accessibility/release checks.
7. Run Oscar.

Verification can prevent release, but a non-release-critical QA failure does not automatically cancel safe product work.

## Progress Law

A run is not considered productive merely because:
- a Python script ran;
- a QA script passed;
- documentation changed;
- a repair tool changed;
- an executor reported "already present".

Product progress requires at least one of:

- real product source changed;
- real canonical output changed;
- a material product requirement moved to VERIFIED COMPLETE with evidence.

## Idempotency Law

An existing marker, CSS layer, JavaScript layer, renderer, or executor output is NOT evidence that requested product work is complete.

Executors must reconcile against the Change Ledger and implement outstanding requirements.

## Failure Handling

If verification fails:

1. classify the failure;
2. identify the owning layer;
3. fix the correct owner;
4. preserve product progress;
5. rerun the smallest relevant verification;
6. continue with safe product work when practical.

Never alter the product merely to satisfy a stale or incorrectly scoped test.

## Required End State

The system must continuously move:

VISION → CONTRACT → PRODUCT MUTATION → VERIFICATION → LEARNING → NEXT PRODUCT MUTATION

and must not remain in:

REPAIR → BUILD → QA → REPAIR → BUILD → QA

without measurable product improvement.

## Masterclass Lesson

AI engineering systems need separate representations for:

- what we want;
- what we changed;
- whether it works;
- what we learned;
- what is next.

One cannot substitute for the others.
