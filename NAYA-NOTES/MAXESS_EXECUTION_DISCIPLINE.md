# NAYA NOTE — MAXESS EXECUTION DISCIPLINE

**Purpose:** Keep Naya from falling into the 5→6→7→8→9→8 loop.

## Operating law
Optimize → Maximize → Synergize → Equalize.

The goal is not to perform a small action correctly. The goal is to move the system as far forward as safely possible in one execution pass while preserving every verified gain.

### Cause-and-effect rule
Before changing code, zoom in, zoom out, and zoom around:
- What problem does this change solve?
- What downstream code depends on the current behavior?
- What new failure could this change create?
- Does the repair preserve the existing contract?
- Can adjacent verification be performed in the same pass?

A change that fixes one defect but creates several new defects is not an improvement. It is a regression.

### Anti-loop rule
Never return to an already-proven lower rung without explicit evidence that the higher rung was invalid. Preserve verified state and build upward.

### Execution batch rule
Each pass should target the current milestone and complete as many safe adjacent actions as possible: inspect → diagnose → repair → re-fetch → verify → test downstream → record evidence → prepare next command.

### Current mission
Start MAXESS and prove the full terminal scoring chain. Do not add Name/Topic generation until the existing fixed assessment can reliably produce and distribute `MAXESS_RESULT_V1` to E01–E04.

### Success evidence
The standard is executable evidence, not plausible code. A green result means one complete 15-question run reaches the authoritative result contract and renders the real result experience without leaving MAXESS.
