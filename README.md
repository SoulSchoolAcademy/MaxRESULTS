# MAXESS Results

Canonical production workspace for the MAXESS Results experience.

## Mission

Deliver a premium, human, personalized AI-mastery experience that transforms:

DATA → INSIGHT → UNDERSTANDING → ACTION → CAPABILITY

## Source-of-truth rules

- The production Results experience has one canonical HTML artifact.
- `window.MAXESS_RESULT` is the authoritative runtime result object.
- Do not create competing renderers, result sources, hero systems, or uncontrolled patch layers.
- Preserve the approved working experience before making structural changes.
- Test the complete experience before declaring a release complete.

## Development protocol

INSPECT → MAP → IMPLEMENT → BUILD → QA → FIX → QA AGAIN → RELEASE

Never stop after one or two visible fixes when the release checklist contains additional work.

## Product requirements

The Results experience must work as:

1. an interactive web experience;
2. a guided Naya experience;
3. a personalized written report; and
4. an intentionally designed printable/downloadable PDF.

## Preservation

The original MAXESS repository remains the historical/backup source until a clean production baseline is independently verified. This repository is intentionally kept minimal while the canonical production artifact and supporting documentation are established.
