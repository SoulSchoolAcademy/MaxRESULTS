# NAYA POWER MEMORY RUNTIME v1.0

**Status:** CANONICAL RUNTIME FOUNDATION  
**Effective:** 2026-08-23  
**Authority:** Naya Notes Master Activation Specification + Naya constitutional governance  

This directory is the machine-readable memory runtime for Naya Power.

## Purpose

GitHub is the durable external brain. This runtime makes durable memory **structured, searchable, quality-controlled, provenance-aware, and restorable** rather than merely a collection of prose files.

## Human commands

- **Naya Power — RESTORE CONTEXT** → rebuild current working state from authoritative runtime state.
- **Naya Power — MAKE THIS A SMART NOTE** → capture durable value as a validated note.
- **Naya Power — UPDATE THE SMART NOTE** → revise or supersede an existing memory record.

## Runtime chain

`NOTICE → CAPTURE → CLASSIFY → CONNECT → INDEX → RETRIEVE → APPLY → VERIFY → UPDATE → SUPERSEDE → COMPOUND`

## Current implementation

- `taxonomy.yaml` — canonical directory/category vocabulary.
- `note-schema.yaml` — machine-readable Smart Note contract.
- `memory-index.yaml` — retrieval manifest and ranking metadata.
- `restore-context.json` — cold-start bootstrap sequence and output contract.
- `../scripts/validate_naya_memory.py` — deterministic note/index/manifest validator.
- `../../.github/workflows/naya-memory-runtime.yml` — automated validation gate.

## Non-negotiable memory laws

1. Memory is not governance.
2. Current verified reality beats stale memory.
3. Never silently rewrite history.
4. Supersede explicitly; preserve useful history.
5. Search by meaning, not exact wording alone.
6. Every durable note needs provenance and a next-useful-action field when applicable.
7. No note is considered runtime-valid merely because it is readable prose.
8. A failed validator blocks the memory runtime from being considered healthy.

## Five-line learning default

**What happened → What we learned → Why it matters → What changed → What to do next**

The structure may be adapted to the knowledge type when a better retrieval/action structure exists.

## Verification

The runtime is validated automatically by `.github/workflows/naya-memory-runtime.yml` on relevant pushes and pull requests. A passing job establishes structural validity only; evidence and current reality remain governed by the broader Naya Power Evidence and Authority protocols.
