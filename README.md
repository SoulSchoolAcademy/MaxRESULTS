# MAXESS Results

Canonical production workspace for the MAXESS Results experience.

## Mission

Deliver a premium, human, personalized AI-mastery experience that transforms:

DATA → INSIGHT → UNDERSTANDING → ACTION → CAPABILITY

## Current canonical paths

- `MAXESS-RESULTS-GROOVE.html` — canonical V21 working artifact.
- `BASELINE-WORKING.html` — frozen recovery baseline; do not edit during V21.
- `NAYA-OS.md` — optimized Naya operating system.
- `docs/` — product, deployment, QA, and memory documentation.

## Source-of-truth rules

- The production Results experience has one canonical HTML artifact.
- `window.MAXESS_RESULT` is the authoritative runtime result object.
- Do not create competing renderers, result sources, hero systems, or uncontrolled patch layers.
- Preserve the approved working experience before making structural changes.
- Test the complete experience before declaring a release complete.

## Development protocol

INSPECT → MAP → BASELINE → SOURCE-LOCK → IMPLEMENT → BUILD → REFETCH → DIFF → QA → OSCAR → FIX → QA AGAIN → RELEASE

## Product requirements

The Results experience must work as:

1. an interactive web experience;
2. a guided Naya experience;
3. a personalized written report; and
4. an intentionally designed printable/downloadable PDF.

## State model

The V21 candidate is an UPDATED EDITED FILE until explicitly approved.

Do not silently promote a new commit, newer filename, or verified build to APPROVED/AUTHORITATIVE status.

## Deployment

GitHub stores and verifies engineering artifacts. Groove is the external publishing mechanism. A GitHub commit does not prove public Groove deployment.
