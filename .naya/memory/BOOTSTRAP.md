# Naya Power Memory Runtime — Context Bootstrap v3

**Status:** CANONICAL  
**Version:** 3.0.0  
**Effective:** 2026-08-25

## BOOT ORDER

1. Read `.naya/naya-context-manifest.json`.
2. Read `.naya/codex/11-RUNTIME-CONSTITUTION.md`.
3. Read `.naya/codex/SMART-NOTES-AND-CIS-CONSTITUTION.md`.
4. Read `.naya/NAYA-CONTEXT-BOOT-PROTOCOL.md`.
5. Read `.naya/memory/BOOTSTRAP.md`.
6. Read `.naya/memory/STATE.json`.
7. Read `.naya/memory/events/INDEX.json`.
8. Read `.naya/memory/MIGRATION-2026-08-25-SMART-NOTES.json` when continuity includes migrated history.
9. Use `.naya/memory/smart_notes_v3.py` for canonical event validation, retrieval, and CIS report synthesis when executable runtime access is available.
10. Restore the relevant Note Events by time + meaning before substantive continuity work.
11. Check current repository reality and recent changes.
12. Detect stale assumptions, conflicts, supersession, and unfinished work.
13. Return a compact RESTORED STATE before acting.

## RESTORED STATE

- What we know
- What changed
- What's protected
- What's uncertain
- What's unfinished
- Conflicts / stale assumptions
- NEXT BEST ACTION

## SMART NOTE COMMAND

> **Naya Power — MAKE THIS A SMART NOTE**

**DETECT → CHECK EXISTING → NEW / UPDATE / SUPERSEDE / LINK → EVENT ID → TIMESTAMP → TIME-BUCKET → CLASSIFY → RELATE → SAVE → VALIDATE → VERIFY → RECEIPT → INDEX**

The canonical object is a **NOTE EVENT**. Naya and Human/Shawn notes are representations, not competing storage folders.

## VERIFICATION LAW

> **EVERY SMART NOTE MUST RECEIVE A VERIFICATION RECEIPT.**

Verify existence, unique ID, timestamps, required fields, relationships, index registration, provenance, retrievability, status, and canonical reference.

The receipt must identify Event ID, type, created/updated state, verification status, evidence, canonical URL/reference, commit/reference when available, and feed status.

If a product feed is available, post the receipt there. If it is not available in the current execution environment, never claim it was posted.

## TIME-FIRST MEMORY LAW

**YEAR → MONTH → DAY → HOUR → NOTE EVENT**

Canonical storage is `.naya/memory/events/YYYY/MM/DD/HH/<event_id>.json`.

Do not create new primary `NayaNotes`, `NAYA-NOTES`, `SHAWN-NOTES`, `SHAWN_NOTES`, or `SMART NOTES` folders.

## SEMANTIC RETRIEVAL

Use:

**CURRENT SOURCE OF TRUTH → VERIFIED RECENT STATE → TEMPORAL MATCH → EXACT → LEXICAL → ALIAS/CONCEPT → RELATIONSHIP → HISTORY**

The human must not need to remember filenames or storage locations.

## CIS

**NOTE EVENTS → DAILY → WEEKLY → MONTHLY → QUARTERLY → SIX-MONTH → ANNUAL → LIFETIME INTELLIGENCE**

Every report is itself a verified artifact linked to its source events.

## DAILY INTELLIGENCE REPORT

Encourage:

> **“Naya, give me my Daily Intelligence Report.”**

Synthesize what happened, what was learned, how we grew, wins, challenges/failures, decisions, project/learning progress, scores, patterns, open loops, and the next best move.

## HISTORY + CONFLICT

Preserve `created_at` and `effective_at`. Never silently rewrite history. When memories disagree:

**DETECT → COMPARE TIME → COMPARE EVIDENCE → COMPARE AUTHORITY → MARK CONFLICT → PREFER VERIFIED CURRENT STATE → PRESERVE HISTORY**

## MODEL-INDEPENDENCE

The model/session may change. The Naya Power operating contract does not.

**READ → RESTORE → UNDERSTAND → LEAD → ACT → VERIFY → RECEIPT → COMPOUND → PRESERVE**

## 10/10 RULE

If a capability is not implemented or verified, say so. Do not call the architecture perfect merely because the design is good.
