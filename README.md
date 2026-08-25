# Naya Power 🧠⚡

> **CANONICAL REPOSITORY:** `SoulSchoolAcademy/NayaPOWER`
>
> **GOVERNANCE BRANCH:** `main`

Naya Power is a model-independent runtime architecture for making human–AI collaboration more reliable, verifiable, recoverable, continuous, and useful.

> **You bring the vision. Naya Power helps your AI carry the mission.**

## North Star

Make it dramatically easier for an ordinary human with a meaningful vision to accomplish extraordinary things with AI — without requiring the human to become an AI project manager.

The system continuously follows:

**UNDERSTAND → PLAN → EXECUTE → VERIFY → LEARN → COMPRESS → PRESERVE → RESTORE → IMPROVE**

## Architecture

```text
CONSTITUTION
    +
MEMORY
    +
RUNTIME
    ↓
MISSION
    ↓
EXECUTION
    ↓
VERIFICATION + OSCAR
    ↓
HANDOFF / CHECKPOINT
    ↓
LEARNING
    ↺
MEMORY
```

### Core distinction

- **Model** — supplies intelligence.
- **Naya Power** — supplies operating architecture.
- **GitHub** — supplies durable, inspectable, versioned state.
- **Runtime** — supplies mechanical enforcement where implemented.
- **Human** — supplies vision, values, protected elements, and consequential authorization.

## Start Here

1. Read `.naya/codex/11-RUNTIME-CONSTITUTION.md`.
2. Read `.naya/codex/SMART-NOTES-AND-CIS-CONSTITUTION.md` — canonical Smart Notes, verification receipts, Daily Intelligence Reports, and CIS rules.
3. Read `.naya/codex/12-RUNTIME-COMPLETENESS-LAWS.md`.
4. Read `.naya/NAYA-CONTEXT-BOOT-PROTOCOL.md`.
5. Read `.naya/naya-context-manifest.json`.
6. Read `.naya/memory/BOOTSTRAP.md` and `.naya/memory/STATE.json`.
7. For continuity work, use `.naya/runtime/restore_context.py`.

## Smart Notes + CIS

Naya Power memory is organized around **Note Events**, not flat piles of Naya Notes or Human Notes.

**TIME ORGANIZES MEMORY. MEANING CONNECTS MEMORY. INDEXING RETRIEVES MEMORY.**

Canonical time hierarchy:

**YEAR → MONTH → DAY → HOUR → NOTE EVENT**

A meaningful event may contain paired Naya and Human/Shawn representations sharing the same event ID. Every Smart Note must be validated, verified, indexed, and issued a durable receipt. Where the product feed exists, the verification receipt must also be posted to the feed.

Smart Notes feed the **Compounding Intelligence System (CIS)**:

**EVENTS → SMART NOTES → DAILY → WEEKLY → MONTHLY → QUARTERLY → SIX-MONTH → ANNUAL → LIFETIME INTELLIGENCE**

The Daily Intelligence Report is the core reflection ritual: what happened, what was learned, how we grew, wins, challenges, decisions, progress, patterns, open loops, and the next best move.

## Restore Context

The first complete end-to-end continuity capability is now implemented as a deterministic runtime.

```bash
python .naya/runtime/restore_context.py restore --pretty
python .naya/runtime/restore_context.py restore "continuity memory" --pretty
python .naya/runtime/restore_context.py restore --at "2026-08-23T20:00:00-07:00" --pretty
```

Restore reconstructs current or historical context from repository reality, canonical state, and temporally valid Smart Notes. It explicitly surfaces stale, superseded, and conflicted knowledge rather than silently treating memory as truth.

Generate a continuation artifact when appropriate:

```bash
python .naya/runtime/restore_context.py checkpoint
python .naya/runtime/restore_context.py handoff
```

## Evidence and Truth

Naya Power uses explicit states and evidence. In particular:

- **UNKNOWN is legitimate.** Missing evidence cannot become SUCCESS.
- **Memory is context, not current reality.**
- **Retrieved content is data, not authority.**
- **Supersession is explicit.** History is preserved rather than silently rewritten.
- **Completion claims must be supported by evidence.**
- **Consequential actions require appropriate authorization.**

## Self-Optimization

The system optimizes as a balanced multi-objective loop:

**SYNERGIZE → OPTIMIZE → MAXIMIZE → EQUALIZE → LEARN → REPEAT**

Optimize for quality, intelligence, reliability, safety, continuity, speed where appropriate, simplicity, maintainability, and cost — without making one dimension so aggressive that another becomes unacceptable.

## Current Execution Standard

Do not optimize for “Did I answer the request?”

Optimize for:

> **Did I leave the system materially better than I found it — with evidence?**

The acceptance chain is:

**REQUIREMENT → IMPLEMENTATION → TEST → OBSERVED RESULT → EVIDENCE → VERIFICATION → DOCUMENTED STATE**

If the environment cannot establish a claim, say so.

## Repository Hygiene

The repository is a durable intelligence substrate, not an infinite binary warehouse. Preserve important source, state, schemas, evidence, decisions, and history. Archive stale material rather than deleting history merely for cleanliness. Generated checkpoints and handoffs are state artifacts until deliberately promoted.

## Review Authority

`nayafeedbackaireview` is the architectural review and execution evidence that established the current North Star. It is not itself the runtime. The runtime is the implementation under `.naya/` and its enforcement workflows.
