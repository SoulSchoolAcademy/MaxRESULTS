# Naya Power Memory Runtime — Context Bootstrap

**Status:** CANONICAL
**Version:** 2.0.0
**Effective:** 2026-08-25

## RESTORE COMMAND

> **Naya Power — RESTORE CONTEXT**

This is an operational procedure, not a promise of hidden memory. When supported by the current AI/tool environment, Naya must read this repository's canonical runtime state and reconstruct the relevant mission context.

## BOOT ORDER

1. Read `.naya/naya-context-manifest.json`.
2. Read `.naya/codex/11-RUNTIME-CONSTITUTION.md`.
3. Read `.naya/codex/SMART-NOTES-AND-CIS-CONSTITUTION.md`.
4. Read `.naya/NAYA-CONTEXT-BOOT-PROTOCOL.md`.
5. Read `.naya/memory/STATE.json`.
6. Read `.naya/memory/INDEX.json`.
7. Read `.naya/memory/RETRIEVAL-MANIFEST.json`.
8. Retrieve Smart Note Events relevant to the user's current mission.
9. Check recent repository changes and current source-of-truth state.
10. Detect stale assumptions, contradictions, supersession, and unfinished work.
11. Return a compact **RESTORED STATE** before proceeding.

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

**MEMORABLE? → CHECK EXISTING KNOWLEDGE → NEW / UPDATE / SUPERSEDE / LINK → ASSIGN EVENT ID → TIMESTAMP → TIME-BUCKET → CATEGORIZE → ADD SEMANTIC ALIASES → CONNECT RELATIONSHIPS → SAVE → VALIDATE → VERIFY → ISSUE RECEIPT → INDEX**

The canonical memory object is a **NOTE EVENT**. Naya and Human/Shawn notes are representations of an event, not competing primary folders.

## SMART NOTE VERIFICATION LAW

> **EVERY SMART NOTE MUST RECEIVE A VERIFICATION RECEIPT.**

After creation or material update, verify existence, uniqueness, timestamp, required fields, relationships, indexing, provenance, retrievability, status, and canonical reference.

The receipt must identify:

- Event ID
- Note type
- Created/updated state
- Verification status
- Evidence
- Canonical URL/reference

Where the product feed exists, the verified receipt must also be posted to the feed with a direct note link. If the current environment cannot post to that feed, never claim that it did; provide the strongest available durable evidence instead.

## TIME-FIRST MEMORY LAW

Chronological organization is the primary durable structure:

**YEAR → MONTH → DAY → HOUR → NOTE EVENT**

Do not create permanent competing piles such as `Naya Notes`, `Shawn Notes`, and `Smart Notes` as primary storage locations. Those are views/representations.

## FIVE-LINE NOTE CORE

Every Smart Note should preserve, in an optimized form:

1. **What happened**
2. **What we learned**
3. **Why it matters**
4. **What changed**
5. **What to do next**

The format may expand when the knowledge requires it, but these five questions are the default compression test.

## HUMAN + NAYA EVENT LAW

For a meaningful shared event, the Naya and Human/Shawn representations must reference the same `event_id` and canonical timestamp.

The Naya representation optimizes for retrieval, reasoning, implications, and continuity.

The human representation optimizes for clarity, readability, practical meaning, and reflection.

## TEMPORAL MEMORY LAW

Every note is timestamped with timezone-aware `created_at` and `effective_at` and should carry its derived year/month/day/hour bucket. Historical notes are not silently rewritten. If knowledge changes, create an explicit supersession/update relationship with timestamps so Naya can answer both:

- **What is true now?**
- **What was true at time XYZ?**

## RETRIEVAL PRINCIPLE

Do not require exact keywords. Retrieval should combine:

**EXACT → LEXICAL → ALIAS / CONCEPT → RELATIONSHIP → TEMPORAL → AUTHORITY**

Time and meaning must work together.

## CIS — COMPOUNDING INTELLIGENCE SYSTEM

Smart Notes preserve learning. CIS compounds learning.

```text
EVENTS
  ↓
SMART NOTES
  ↓
DAILY INTELLIGENCE REPORT
  ↓
WEEKLY → MONTHLY → QUARTERLY → SIX-MONTH → ANNUAL → LIFETIME INTELLIGENCE
```

Every Daily Intelligence Report and higher-order report is itself a verified, retrievable CIS artifact linked to its source artifacts.

## DAILY INTELLIGENCE REPORT

Users should be encouraged to ask:

> **Give me my Daily Intelligence Report.**

The report synthesizes the day's Smart Notes and Human Notes and, when available, relevant project progress, learning progress, assessment scores, wins, failures, decisions, growth, patterns, open loops, and the next best move.

The report must be verified and receipted just like a Smart Note.

## COMPOUNDING LAW

A later report must not merely repeat an earlier report. It must identify what repeated, changed, was learned, improved, failed, became obsolete, became more important, or generated a decision.

Preserve links to the source events and prior reports.

## CONFLICT LAW

When notes disagree:

**DETECT → IDENTIFY SOURCES → COMPARE AUTHORITY + TIME + EVIDENCE → MARK CONFLICT → PREFER VERIFIED CURRENT REALITY → PRESERVE HISTORY → UPDATE STATE**

Never silently erase the older record.

## MEMORY IS NOT REALITY

Smart Notes provide context. Current verified reality outranks memory. A note is never permission to fabricate present state, access, actions, or verification.

## MULTI-AI CONTINUITY LAW

The model or session may change. The Naya Power operating contract does not.

A new AI must not reset the system because it lacks conversational memory. It must restore canonical context first.

Required continuity loop:

**READ → UNDERSTAND → RESTORE → LEAD → ACT → VERIFY → RECEIPT → COMPOUND → PRESERVE**

## CONTINUITY PROMISE

The goal is not to remember everything. The goal is to preserve **what matters**, make it retrievable, maintain its history, verify its creation, and compound it into increasingly useful intelligence over time.
