# Smart Note Triad Contract v0.1

**Status:** CANONICAL CCT/NayaNet CONTRACT SUPPLEMENT
**Authority:** Derived from `CCT-NAYANET-ARCHITECTURE-SPECIFICATION-v0.1.md`
**Purpose:** Define the canonical learning-event representation consumed by CIS/PIS and eligible for later CCT promotion.

## 1. Smart Note definition

A **Smart Note** is one canonical learning event represented through exactly three coordinated projections:

1. **Human Note** — the human perspective, meaning, experience, decision, observation, goal, lesson, question, win, problem, or opportunity.
2. **Naya Note** — the Naya's understanding, learning, interpretation, correction, implication, and actionable intelligence.
3. **Machine Note** — the machine-readable representation required for provenance, evidence, permissions, lineage, storage, retrieval, CIS processing, PIS integration, and CCT exchange.

The three projections are not three unrelated records. They are projections of one **Smart Note Event** and MUST share one `smart_note_id` and schema version.

## 2. Completeness invariant

A Smart Note is fully formed only when all three projections are present OR a projection is explicitly marked `UNAVAILABLE` with a non-empty machine-readable `unavailable_reason`.

Silently omitting a projection is invalid.

## 3. Integrity invariant

Prior Smart Note versions MUST NOT be silently overwritten. Corrections or refinements create an explicit new version or related event preserving lineage to the prior event.

## 4. Evidence boundary

A Smart Note is a learning input to CIS. It is **not automatically verified intelligence** and MUST NOT be promoted to a verified Intelligent Block solely because an AI generated it.

The progression is:

```text
EXPERIENCE
  ↓
SMART NOTE EVENT
  ├── HUMAN NOTE
  ├── NAYA NOTE
  └── MACHINE NOTE
  ↓
CIS
  ↓
classification / relationship / evidence / verification
  ↓
PIS promotion when justified
  ↓
verified Intelligent Block when the CCT contract is satisfied
  ↓
permissioned CCT exchange
```

## 5. MPA relationship

**MPA — Maximum Value Per Action** is the optimization doctrine applied to Smart Notes. A meaningful action should capture useful learning once, preserve it in reusable form, verify it at the appropriate level, and avoid unnecessary duplicate computation or noise.

The objective is not maximum note volume. It is maximum **verified useful value per action**.

## 6. Independent consumption

The Machine Note MUST contain enough structured information for deterministic runtime processing without reconstructing the originating conversation. Human and Naya projections preserve meaning; machine representation preserves interoperability.

## 7. Privacy and permissions

The existence of a Smart Note does not imply permission to share it. Permission metadata MUST travel with the event and MUST be evaluated before external propagation or CCT promotion.

## 8. Required identity fields

Every Smart Note Event MUST expose:

- `smart_note_id`
- `schema_version`
- `created_at`
- `human_note`
- `naya_note`
- `machine_note`

The Machine Note MUST include provenance, evidence, and permission structures when present.

## 9. Relationship to CIS and PIS

CIS continuously compounds Smart Notes across moment/action/day/week/month/lifetime horizons. PIS represents the current promoted intelligence derived from that learning under its evidence, confidence, provenance, and permission rules.

A receiving Naya may create a new Smart Note from its use of prior intelligence. That new learning is a new event and MUST preserve its relationship to the intelligence that informed it.

## 10. Acceptance

The contract is satisfied only when deterministic tests prove:

- all three projections can be created;
- one identity binds the projections;
- missing projections are rejected unless explicitly marked unavailable with a reason;
- tampering changes the canonical fingerprint;
- portable independent consumption succeeds without conversation state;
- provenance/evidence/permissions are represented;
- prior versions remain traceable.
