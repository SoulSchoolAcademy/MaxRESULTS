# MAXESS Results — Deployment Contract

## Engineering source

The clean repository will contain one canonical complete Results artifact.

## External deployment

GitHub stores and versions the engineering source. Groove is the external publishing mechanism.

**OFFICIAL MAXESS RESULTS PRODUCTION/PUBLIC TARGET:** `https://results.nayanet.app/`

`.xyz` is obsolete for the MAXESS Results public target and MUST NOT be used in Results navigation, redirects, deployment instructions, embeds, prompts, AI instructions, or public-target documentation.

A GitHub commit does not prove Groove publication.

## Required chain

SOURCE BASELINE
→ EDITED ARTIFACT
→ DIFF
→ DETERMINISTIC QA
→ GROOVE DEPLOYMENT PAYLOAD
→ GROOVE PUBLISH
→ PUBLIC FETCH (`https://results.nayanet.app/`)
→ PARITY CHECK
→ VISUAL OSCAR
→ LIVE VERIFIED

## Cross-site MAXESS handoff

The assessment entry point is `https://aiscore.nayanet.app/`.

The required product handoff is:

`aiscore.nayanet.app` → authoritative `MAXESS_RESULT_V1` → `results.nayanet.app`

The Results application consumes the same authoritative result. The assessment must never substitute a demo score, static score, or fallback score for a missing result.

## Minimal deployment probe

Before replacing the live Results payload, a harmless deployment probe can establish that the intended Groove code element actually reaches the public URL. If the probe does not appear, the problem is external delivery, not the Results implementation.

## Hard rules

- Never use a GitHub loader as the production Results renderer.
- Never call a GitHub write “live.”
- Never declare public parity without fetching the actual public target.
- Never ask the user to test a known-invalid tiny replacement.
- If direct Groove publishing is unavailable, complete all upstream work and state `ENGINEERING COMPLETE — READY FOR GROOVE TEST` rather than entering a blocker loop.
- Never use `results.nayanet.xyz/` as the MAXESS Results destination.

## Public verification

The final live test must inspect the actual human-facing page for:

- hero hierarchy;
- score clarity;
- Naya presence;
- five dimensions;
- report;
- pattern;
- strength;
- lever;
- next move;
- Masters;
- Playground/ending;
- responsive behavior;
- accessibility;
- no horizontal overflow;
- performance;
- correct release markers/data.
