# NayaPOWER — Collective Intelligence Event Schema v1

**STATUS:** CANONICAL / ACTIVE DESIGN CONTRACT
**EFFECTIVE:** 2026-08-30

A Collective Intelligence Event (CIE) is a derived intelligence object created from an explicitly authorized wisdom contribution. It is **not** a copy of the source Note Event, repository, conversation, or contributor.

## Canonical shape

```json
{
  "event_id": "cie_<stable-id>",
  "schema_version": "1.0",
  "event_type": "insight|lesson|pattern|solution|warning|decision|principle",
  "created_at": "<timezone-aware ISO-8601>",
  "effective_at": "<timezone-aware ISO-8601>",
  "subject": "<concise subject>",
  "wisdom": "<generalized reusable intelligence>",
  "why_it_matters": "<practical significance>",
  "applicability": ["<context>"],
  "evidence": [],
  "confidence": 0.0,
  "provenance": {
    "source_kind": "authorized_wisdom_contribution",
    "source_event_count": 0,
    "validation_state": "unverified|validated|superseded"
  },
  "privacy": {
    "identity_included": false,
    "raw_source_included": false,
    "privacy_review": "passed|review_required|rejected"
  },
  "relationships": [],
  "supersedes": [],
  "status": "candidate|published|validated|superseded|rejected",
  "verification_receipt": {
    "verified": false,
    "verified_at": null,
    "checks": []
  }
}
```

## Required invariants

1. `event_id` is unique and durable.
2. `schema_version` is explicit.
3. `created_at` and `effective_at` are timezone-aware.
4. `wisdom` is generalized and reusable rather than raw personal memory.
5. `identity_included` MUST be `false` for the collective object.
6. `raw_source_included` SHOULD be `false`; raw source MUST NOT be included when unnecessary.
7. `confidence` MUST NOT be represented as certainty.
8. Provenance MUST remain distinguishable from the wisdom itself.
9. Contradictions and supersession MUST be explicit.
10. Publication MUST NOT be represented as validation unless validation evidence exists.
11. A rejected event is preserved as history where required; it is not silently transformed into a different claim.
12. The collective event does not create authority over a person's sovereign Superbrain.

## Evidence

Evidence entries SHOULD identify the kind of support available (observation, repeated result, test, human report, external evidence, or other authorized source) and its verification state. Sensitive raw source details should be minimized.

## Relationships

Relationships may link the event to concepts, other collective events, contradictions, superseding events, domains, or applicable contexts. Relationships must not become an undeclared identity graph.

## Lifecycle

`CANDIDATE → REVIEWED → PUBLISHED → VALIDATED → SUPERSEDED`

`CANDIDATE → REJECTED` is also valid.

## Collective Chain

Validated CIEs may enter the Collective Chain, where later events can reinforce, qualify, contradict, or supersede earlier intelligence. The chain preserves lineage and uncertainty instead of manufacturing consensus.

## Security and privacy boundary

This schema intentionally has no contributor name, email, GitHub username, repository URL, access token, conversation transcript, or private-memory field. Internal contribution records may retain the minimum information required for consent, abuse prevention, audit, and revocation, but those records are not the collective intelligence object.

## Compatibility

CIEs are downstream of canonical Note Events and Wisdom Contribution Protocol decisions. They do not replace `.naya/memory/events/...` or create a second personal-memory system.
