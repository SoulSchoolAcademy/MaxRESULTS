# MAXIS / SUPER BRAIN — AI OPERATING MANDATE

## 1. Mission

Every AI entering this project is joining an existing engineering system. The job is not to restart the investigation. The job is to read the current state, preserve truth, move the project forward, verify the work, and leave the next AI with a complete handoff.

## 2. North Star

**MAKE THE ENGINE WORK.**

For MAXIS/MAXESS this means the complete assessment and results system must function as one page:

- 15 questions render.
- Answers can be selected.
- Continue advances correctly.
- State is preserved correctly.
- Score is calculated correctly.
- The authoritative result is created exactly once.
- The result crosses the release boundary.
- E01–E09 receive the same authoritative result.
- The correct score, mastery band, dimensions, and fingerprint appear.
- No section races another section.
- No duplicate scoring engine competes with the canonical engine.

## 3. Required operating sequence

**READ → UNDERSTAND → LEAD → ACT → VERIFY → DOCUMENT → HANDOFF**

Never skip directly to editing code when the project state can be inspected first.

## 4. Source of truth

For substantive project work:

1. Read `MAXIS/PROJECT_INDEX.md`.
2. Read `MAXIS/PROJECT_FEED.md`.
3. Read `MAXIS/WORKBENCH.md`.
4. Read the relevant source artifact(s).
5. Inspect the current live implementation before proposing replacement.
6. Treat explicit user-confirmed live state as authoritative until verified otherwise.

## 5. One problem at a time

Separate:

- scoring problems
- state problems
- event/communication problems
- DOM/isolation problems
- result-schema problems
- visual problems
- content problems

Do not mix unrelated repairs into a single debugging hypothesis.

## 6. Contract law

A shared runtime result is a contract, not an informal object.

The canonical contract must define at minimum:

- `contractVersion`
- `overallScore` (0–100 integer)
- `masteryBand`
- exactly 5 dimensions
- exactly 15 responses
- stable question/answer identifiers
- any additional derived fingerprint required downstream

The producer owns creation. Controllers validate. Presentation sections consume. Presentation sections must not recalculate the official score.

## 7. Single-authority law

There must be one canonical producer and one canonical release authority.

If two components can both declare the result released, the architecture is suspect and must be simplified.

## 8. Event law

Every event must have:

- a unique semantic purpose
- a known producer
- a known consumer
- a documented payload
- deterministic ordering or recovery behavior

Events are signals, not substitutes for state. The canonical result must remain recoverable from a stable shared location.

## 9. Recovery law

A component must work even when it loads slightly before or after another component.

Therefore every consumer should support:

1. event-driven hydration when the event is received;
2. state-driven recovery when the event was missed.

Do not solve ordering problems with aggressive infinite polling.

## 10. Preservation law

Do not rewrite working visual/content code simply because the architecture is broken.

Make the smallest change that fully solves the actual failure.

## 11. Verification law

Never report “fixed” because code looks correct.

A fix is complete only after verification against the actual failure path.

Required MAXESS verification:

- E00 loads.
- 15 questions work.
- every answer can be selected.
- Continue advances through all 15.
- Q15 completion gate fires.
- score is calculated.
- result contract exists.
- controller accepts it.
- isolation changes from waiting to released.
- E01–E09 hydrate from the same result.
- no section remains pending incorrectly.
- no duplicate release occurs.

## 12. No fabrication

Never invent:

- test results
- code changes
- GitHub state
- file contents
- remembered project state
- successful execution

Explicitly distinguish **verified**, **observed**, **inferred**, and **pending verification**.

## 13. Project communication law

While actively working on a project, important findings belong in the project feed. Do not create isolated notes that the next project worker cannot discover.

Every meaningful work session should update:

- current state
- what changed
- what was learned
- what failed
- what remains
- next action

## 14. Handoff law — NON-NEGOTIABLE

Before finishing work, every AI must provide a complete handoff containing:

1. Mission / North Star
2. Starting state
3. Files inspected
4. Exact work performed
5. Exact findings
6. Verified behavior
7. Unverified assumptions
8. Problems remaining
9. Recommended next action
10. Any code/version decision made
11. Tests performed and results
12. Risks / regressions to watch

The next AI must be able to continue without reconstructing the previous investigation from memory.

## 15. Learning / exploration / creation

All project knowledge belongs to one of three operating modes:

### CREATE
Building or modifying a project/artifact.

### LEARN
Recording what was learned, tested, role-played, demonstrated, or discovered during a learning activity.

### EXPLORE
Researching possibilities, comparing approaches, investigating unknowns, or evaluating alternatives.

Each mode must leave a durable project record.

## 16. Oscar rule

The AI must challenge its own work before declaring success.

Ask:

- What could still be wrong?
- What assumption am I making?
- What competing authority exists?
- What happens if scripts load in a different order?
- What happens if an event is missed?
- What happens if the result is malformed?
- What happens on refresh?
- What happens in the actual live embed?

## 17. Completion standard

The goal is not “code changed.”

The goal is **observable system behavior working end-to-end**.

If the engine is not running, the job is not finished.
