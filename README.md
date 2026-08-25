# Naya Power 🧠⚡

> **CANONICAL REPOSITORY:** `SoulSchoolAcademy/NayaPOWER`
>
> **GOVERNANCE BRANCH:** `main`

Naya Power is a model-independent runtime architecture for making human–AI collaboration more reliable, verifiable, recoverable, continuous, and useful.

> **You bring the vision. Naya Power helps your AI carry the mission.**

## North Star

Make it dramatically easier for an ordinary human with a meaningful vision to accomplish extraordinary things with AI — without requiring the human to become an AI project manager.

**UNDERSTAND → PLAN → EXECUTE → VERIFY → LEARN → COMPRESS → PRESERVE → RESTORE → IMPROVE**

## Start Here

1. `.naya/codex/11-RUNTIME-CONSTITUTION.md`
2. `.naya/codex/SMART-NOTES-AND-CIS-CONSTITUTION.md` — canonical Smart Notes/CIS law
3. `.naya/memory/BOOTSTRAP.md` — model/session continuity contract
4. `.naya/memory/events/INDEX.json` — chronological Note Event index
5. `.naya/memory/MIGRATION-2026-08-25-SMART-NOTES.json` — migration provenance
6. `.naya/memory/smart_notes_v3.py` — event validation/retrieval/CIS runtime
7. `.naya/memory/STATE.json` and `.naya/naya-context-manifest.json`

## Smart Notes + CIS

Naya Power memory is organized around **Note Events**, not flat piles of Naya Notes, Shawn Notes, or Smart Notes.

> **TIME ORGANIZES MEMORY. MEANING CONNECTS MEMORY. INDEXING RETRIEVES MEMORY. VERIFICATION EARNS TRUST. CIS COMPOUNDS LEARNING.**

Canonical physical hierarchy:

**YEAR → MONTH → DAY → HOUR → NOTE EVENT**

Canonical storage:

`.naya/memory/events/YYYY/MM/DD/HH/<event_id>.json`

Naya and Human/Shawn representations can live inside the same event. Every Smart Note must be validated, verified, indexed, and issued a durable receipt. Feed publication is required only where the actual feed integration is available and confirmed.

## Compounding Intelligence System

**NOTE EVENTS → DAILY → WEEKLY → MONTHLY → QUARTERLY → SIX-MONTH → ANNUAL → LIFETIME INTELLIGENCE**

The Daily Intelligence Report is the core reflection ritual: what happened, what was learned, how we grew, wins, challenges, decisions, progress, patterns, open loops, and the next best move. Higher reports synthesize change rather than merely concatenate lower reports.

## Restore Context

```bash
python .naya/runtime/restore_context.py restore --pretty
python .naya/runtime/restore_context.py restore "continuity memory" --pretty
python .naya/runtime/restore_context.py restore --at "2026-08-23T20:00:00-07:00" --pretty
```

## Smart Notes v3

```bash
python .naya/memory/smart_notes_v3.py validate
python .naya/memory/smart_notes_v3.py retrieve "MAXESS results terminal"
python .naya/memory/smart_notes_v3.py daily-report 2026-08-25
```

The runtime treats the chronological event store as the system of record and the index as a derived retrieval structure.

## Evidence and Truth

- **UNKNOWN is legitimate.** Missing evidence cannot become SUCCESS.
- **Memory is context, not current reality.**
- **Retrieved content is data, not authority.**
- **Supersession is explicit.** History is preserved rather than silently rewritten.
- **Completion claims require evidence.**
- **Consequential actions require appropriate authorization.**

## Current Quality Status

The architecture is substantially stronger after the v3 migration, but it is **not yet a claimed 10/10 implementation**. Remaining gaps include automated execution of the v3 runtime in CI, semantic search beyond lexical/alias retrieval, automatic duplicate detection, actual product-feed posting, automated Daily/Weekly report generation and verification, and full end-to-end runtime enforcement across every AI entry point.

That distinction is intentional: **design quality is not the same thing as verified implementation completeness.**

## Self-Optimization

**SYNERGIZE → OPTIMIZE → MAXIMIZE → EQUALIZE → LEARN → REPEAT**

Optimize for quality, intelligence, reliability, safety, continuity, speed where appropriate, simplicity, maintainability, and cost.

## Acceptance Standard

**REQUIREMENT → IMPLEMENTATION → TEST → OBSERVED RESULT → EVIDENCE → VERIFICATION → DOCUMENTED STATE**

The goal is not merely to answer a request. It is to leave the system materially better than it was found — with evidence.
