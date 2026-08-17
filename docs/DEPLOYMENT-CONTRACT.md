# MAXESS Results — Deployment Contract

## Engineering source

The clean repository will contain one canonical complete Results artifact.

## External deployment

GitHub stores and versions the engineering source. Groove is the external publishing mechanism. `https://results.nayanet.xyz/` is the public verification target.

A GitHub commit does not prove Groove publication.

## Required chain

SOURCE BASELINE
→ EDITED ARTIFACT
→ DIFF
→ DETERMINISTIC QA
→ GROOVE DEPLOYMENT PAYLOAD
→ GROOVE PUBLISH
→ PUBLIC FETCH
→ PARITY CHECK
→ VISUAL OSCAR
→ LIVE VERIFIED

## Minimal deployment probe

Before replacing the live Results payload, a harmless deployment probe can establish that the intended Groove code element actually reaches the public URL. If the probe does not appear, the problem is external delivery, not the Results implementation.

## Hard rules

- Never use a GitHub loader as the production Results renderer.
- Never call a GitHub write “live.”
- Never declare public parity without fetching the actual public target.
- Never ask the user to test a known-invalid tiny replacement.
- If direct Groove publishing is unavailable, complete all upstream work and state `ENGINEERING COMPLETE — READY FOR GROOVE TEST` rather than entering a blocker loop.

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
