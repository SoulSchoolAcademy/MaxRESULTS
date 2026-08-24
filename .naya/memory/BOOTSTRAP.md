# Naya Power Memory Runtime — Context Bootstrap

**Status:** CANONICAL
**Version:** 1.0.0
**Effective:** 2026-08-23T22:00:00-07:00

## RESTORE COMMAND

> **Naya Power — RESTORE CONTEXT**

This is an operational procedure, not a promise of hidden memory. When supported by the current AI/tool environment, Naya should read this repository's canonical runtime state and reconstruct the relevant mission context.

## BOOT ORDER

1. Read `.naya/naya-context-manifest.json`.
2. Read `.naya/codex/11-RUNTIME-CONSTITUTION.md`.
3. Read `.naya/NAYA-CONTEXT-BOOT-PROTOCOL.md`.
4. Read `.naya/memory/STATE.json`.
5. Read `.naya/memory/INDEX.json`.
6. Read `.naya/memory/RETRIEVAL-MANIFEST.json`.
7. Retrieve Smart Notes relevant to the user's current mission.
8. Check recent repository changes and current source-of-truth state.
9. Detect stale assumptions, contradictions, supersession, and unfinished work.
10. Return a compact **RESTORED STATE** before proceeding.

## RESTORED STATE OUTPUT

- **What we know**
- **What changed**
- **What's protected**
- **What's uncertain**
- **What's unfinished**
- **Conflicts / stale assumptions**
- **NEXT BEST ACTION**

## SMART NOTE COMMAND

> **Naya Power — MAKE THIS A SMART NOTE**

When a user or Naya identifies durable, reusable, consequential, corrective, or strategically valuable knowledge:

**MEMORABLE? → CHECK EXISTING KNOWLEDGE → NEW / UPDATE / SUPERSEDE / LINK → TIMESTAMP → CATEGORIZE → ADD SEMANTIC ALIASES → CONNECT RELATIONSHIPS → SAVE → VALIDATE → INDEX**

## FIVE-LINE NOTE CORE

Every Smart Note should preserve, in an optimized form:

1. **What happened**
2. **What we learned**
3. **Why it matters**
4. **What changed**
5. **What to do next**

The format may expand when the knowledge requires it, but these five questions are the default compression test.

## TEMPORAL MEMORY LAW

Every note is timestamped with timezone-aware `created_at` and `effective_at`. Historical notes are not silently rewritten. If knowledge changes, create an explicit supersession/update relationship with timestamps so Naya can answer both:

- **What is true now?**
- **What was true at time XYZ?**

A historical note can remain valuable even after it becomes non-current.

## RETRIEVAL PRINCIPLE

Do not require exact keywords. Retrieval should combine:

**EXACT → LEXICAL → ALIAS / CONCEPT → RELATIONSHIP → TEMPORAL → AUTHORITY**

If a user remembers the idea but not the terminology, aliases and related concepts should still surface the note.

## CONFLICT LAW

When notes disagree:

**DETECT → IDENTIFY SOURCES → COMPARE AUTHORITY + TIME + EVIDENCE → MARK CONFLICT → PREFER VERIFIED CURRENT REALITY → PRESERVE HISTORY → UPDATE STATE**

Never silently erase the older record.

## MEMORY IS NOT REALITY

Smart Notes provide context. Current verified reality outranks memory. A note is never permission to fabricate present state, access, actions, or verification.

## CONTINUITY PROMISE

The goal is not to remember everything. The goal is to preserve **what matters**, make it retrievable, maintain its history, and restore enough context that a new Naya session can begin meaningfully ahead rather than from zero.
