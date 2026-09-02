# 🔱☀️ NayaNET — Release Handoff

## Current source

Repository: `SoulSchoolAcademy/NayaPOWER`
Branch: `main`

The canonical release artifact is the repository state on `main`. Do not create a parallel application or Worker for this mission.

## What is complete in source

The E02 NayaNET runtime remains intact and the presentation layer has been reconstructed around a visual-first living environment. The current shell retains the single experience controller, nine-world model, 18 real Powercasts, real artwork/audio mappings, native playback, persistent mini-player, world destinations, and existing state/persistence behavior.

The reconstruction is intentionally presentation-only: it changes how the experience is expressed without replacing the working runtime.

## Release sequence

1. Use the canonical deployment governance already present in the repository.
2. Release the exact `main` commit selected by the authorized workflow.
3. Open the resulting deployment URL.
4. Verify the front door, Hub, world field, Power Player, all artwork, playback, responsive behavior, and core interactions.
5. Record evidence against the exact deployed commit.

## Do not

- create a new Cloudflare app/Worker for this build;
- use a stale Worker URL as proof;
- create a second runtime;
- replace the runtime with a ZIP-only artifact;
- claim live verification from source inspection;
- claim 10/10 without rendered verification.

## Operator handoff

The operator's only required action should be to use the existing governed deployment/rebuild path once the exact release commit is ready, then open the resulting URL for visual verification. The build system owns the decision about infrastructure and release method.

## Final status vocabulary

- **IMPLEMENTED** = source exists.
- **SOURCE VERIFIED** = source structure and wiring inspected.
- **TESTED** = automated checks passed.
- **DEPLOYED** = release system reports deployment.
- **LIVE VERIFIED** = resulting URL was successfully checked.
- **PRODUCTION-PROVEN** = live behavior and evidence are recorded.
- **10/10** = all release and human visual gates pass.
