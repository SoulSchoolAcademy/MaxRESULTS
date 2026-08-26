# MAXIS PROJECT FEED

## 2026-08-26 — Initial Super Brain Engineering Sync

### Work mode
CREATE / ENGINEERING RECOVERY

### North Star
**Get the MAXESS engine running end-to-end.**

### What was inspected

The project repository `SoulSchoolAcademy/NayaPOWER` was inspected directly. The supplied E00 candidates and E00.01–E09 artifacts were opened and analyzed at the architecture level.

### Major discovery

The problem is not primarily that one file is “too long.” The stronger problem is that the page contains **multiple overlapping communication authorities**.

The current architecture has:

- E00 producing the assessment result.
- E00.01 acting as a bridge but also capable of releasing results.
- E00.02 acting as the visual isolation/release gate.
- E00.03 acting as another release controller.
- downstream sections using different recovery/transport paths.

This can create exactly the type of “each part works alone, but they do not communicate reliably together” failure we have been seeing.

### Important verified evidence

E00.01 uses `MAXESS_RESULT_V1`, validates score + 5 dimensions + 15 responses, and can release results. fileciteturn1171file0L2-L10

E00.02 establishes `waiting/released` state, hides E01–E09 while waiting, and listens for `MAXESS_ISOLATION_RELEASE`. fileciteturn1172file0L2-L10

E00.03 independently validates the result and also emits `MAXESS_ISOLATION_RELEASE`. It additionally requires `masteryBand`. fileciteturn1173file0L2-L10

E02 and E03 identify `window.MAXESS_RESULT` as their runtime authority, while E04 independently implements multiple result recovery paths. fileciteturn1175file0L1-L2 fileciteturn1176file0L1-L2 fileciteturn1177file0L2-L2

### Engineering decision

Do **not** choose E00 796 vs E00 1800 based on line count.

Do **not** replace the user-reported live E118 blindly.

First establish the exact behavior and result schema of the live E118 and compare both candidates against it.

The winning E00 will be the implementation that produces the correct canonical result and preserves required UX behavior with the least unnecessary complexity.

### Target architecture

`E00 → MAXESS_RESULT_V1 → E00.01 bridge → E00.03 sole release authority → E00.02 visual gate → E01–E09`

### Rules now locked into the project

Every AI working on MAXIS must:

1. Read the MAXIS project index/workbench/feed first.
2. Treat the engine as one system, not isolated snippets.
3. Use one canonical result contract.
4. Avoid competing authorities.
5. Verify before declaring success.
6. Record findings in the project feed.
7. Leave a complete handoff.

The full reusable mandate is stored in `MAXIS/AI_OPERATING_MANDATE.md`.

### Next action

**Inspect the live E118, diff it against E00 796 and E00 1800, identify the exact final-result writer, then repair the contract/release chain before touching presentation code.**

---

## Handoff status

**Current phase:** Source/architecture analysis complete.

**Verified:** Repository access, supplied artifact existence, result bridge architecture, isolation gate architecture, downstream result dependencies.

**Not yet verified:** Actual live E118 runtime behavior, exact final result object emitted by E118, full candidate diff, browser execution of the integrated page.

**Do not claim the engine is fixed yet.**
