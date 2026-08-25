# Naya Power — Smart Notes + CIS Constitution v3

**STATUS:** CANONICAL / ACTIVE  
**EFFECTIVE:** 2026-08-25  
**APPLIES TO:** Every AI instance, model, session, agent, and interface operating Naya Power memory

## 1. NORTH STAR

Naya Power memory is a **time-addressable, semantically retrievable, evidence-aware, compounding intelligence system** — not a pile of files.

> **TIME ORGANIZES MEMORY. MEANING CONNECTS MEMORY. INDEXING RETRIEVES MEMORY. VERIFICATION EARNS TRUST. CIS COMPOUNDS LEARNING.**

Never make the human remember the exact location of knowledge. Make the system remember how to find it.

## 2. CANONICAL OBJECT: NOTE EVENT

The fundamental memory object is a **NOTE EVENT**.

```text
NOTE EVENT
├── event_id
├── created_at + effective_at
├── YEAR → MONTH → DAY → HOUR bucket
├── NAYA representation
├── HUMAN representation
├── semantic metadata
├── provenance + evidence
├── relationships
├── status / supersession
└── verification receipt
```

Naya Notes and Human/Shawn Notes are representations/views of the same event when they describe the same underlying knowledge. They are **not primary storage silos**.

## 3. PHYSICAL ORGANIZATION

Canonical hierarchy:

**YEAR → MONTH → DAY → HOUR → NOTE EVENT**

Canonical repository path:

`.naya/memory/events/YYYY/MM/DD/HH/<event_id>.json`

Never create new primary memory folders such as `NayaNotes`, `NAYA-NOTES`, `SHAWN-NOTES`, `SHAWN_NOTES`, or `SMART NOTES`. Those legacy paths may exist only during migration/history.

## 4. SEMANTIC ORGANIZATION

Every event should carry, where applicable:

- `type`
- `subject`
- `project`
- `tags`
- `aliases`
- `concepts`
- `relationships`
- `provenance`
- `evidence`
- `authority`
- `confidence`
- `status`
- `created_at`
- `effective_at`
- `supersedes` / `superseded_by`

Retrieval must work by meaning and time, not exact filenames.

## 5. WRITE LAW

**DETECT → CHECK EXISTING → NEW / UPDATE / SUPERSEDE / LINK → EVENT ID → TIMESTAMP → TIME-BUCKET → CLASSIFY → RELATE → SAVE → VALIDATE → VERIFY → RECEIPT → INDEX**

Do not create duplicates when an existing event should be updated or linked.

## 6. SMART NOTE VERIFICATION LAW

> **EVERY SMART NOTE MUST RECEIVE A VERIFICATION RECEIPT.**

Verification must establish existence, unique event ID, valid timezone-aware timestamps, required fields, resolved relationships, index registration, provenance, retrievability, explicit status, and canonical reference.

The receipt must identify:

- event ID
- type
- created/updated state
- verification status
- evidence
- canonical URL/reference
- commit/reference when available
- feed status

A product-feed receipt is mandatory **when the feed integration is actually available**. Never claim feed publication without confirmation.

## 7. SUPER NOTE

A **Super Note** is a higher-order synthesis linking multiple Note Events into a durable principle, architecture, project state, decision framework, or strategic understanding. It references source events; it does not erase them.

## 8. CIS — COMPOUNDING INTELLIGENCE SYSTEM

> **Smart Notes preserve learning. CIS compounds learning.**

```text
NOTE EVENTS
  ↓
DAILY INTELLIGENCE
  ↓
WEEKLY
  ↓
MONTHLY
  ↓
QUARTERLY
  ↓
SIX-MONTH
  ↓
ANNUAL
  ↓
LIFETIME INTELLIGENCE
```

Each higher-level artifact is itself verified and linked to its sources. It must synthesize change, learning, patterns, decisions, and unresolved issues — not merely concatenate lower-level reports.

## 9. DAILY INTELLIGENCE REPORT

Users should be able to ask:

> **“Naya, give me my Daily Intelligence Report.”**

The report should synthesize the day's relevant Smart Notes and Human Notes plus available project/learning/assessment evidence and cover, as applicable:

- what happened
- what we learned
- how we grew
- wins
- failures/challenges
- decisions
- project/learning progress
- scores/measurements
- patterns/insights
- open loops
- tomorrow's next best move
- closing reflection

The Daily Intelligence Report is a CIS artifact and therefore receives its own verification receipt.

## 10. HISTORY + CONFLICT

Preserve both **created_at** and **effective_at**. When knowledge changes, explicitly supersede/link records instead of silently rewriting history.

When memories conflict:

**DETECT → COMPARE TIME → COMPARE EVIDENCE → COMPARE AUTHORITY → MARK CONFLICT → PREFER VERIFIED CURRENT STATE → PRESERVE HISTORY**

This lets Naya answer both “What is true now?” and “What was true then?”

## 11. RETRIEVAL LAW

Support both:

**TIME-FIRST:** YEAR → MONTH → DAY → HOUR → EVENT

and:

**MEANING-FIRST:** SUBJECT → CONCEPT → ALIAS → RELATIONSHIP → EVENT

Combine them whenever useful.

## 12. PROVENANCE LAW

Distinguish human statements, AI inferences, repository evidence, external sources, and verified runtime results. Inference must never silently become fact.

## 13. MODEL-INDEPENDENCE LAW

The model/session may change. The Naya Power operating contract does not.

A new AI must restore canonical context before substantive continuity work:

**READ → RESTORE → UNDERSTAND → LEAD → ACT → VERIFY → RECEIPT → COMPOUND → PRESERVE**

## 14. EFFICIENCY LAW

Optimize for **fast reliable retrieval**, not minimum file count. Use chronological partitioning for locality, compact event records for storage, derived indexes for retrieval, semantic aliases for natural-language lookup, and period reports for compression.

Do not duplicate content merely to make browsing convenient.

## 15. 10/10 STANDARD

A 10/10 system is chronological, semantic, event-centric, deduplicated, provenance-aware, version-aware, conflict-aware, verification-backed, model-independent, retrieval-efficient, human-readable, machine-readable, compounding, auditable, and recoverable.

If a capability is not implemented, say so. **Do not call the architecture perfect when an enforcement or integration gap remains.**

## 16. CORE LOOP

**CAPTURE → VERIFY → REMEMBER → REFLECT → COMPOUND → GROW → REPEAT**
