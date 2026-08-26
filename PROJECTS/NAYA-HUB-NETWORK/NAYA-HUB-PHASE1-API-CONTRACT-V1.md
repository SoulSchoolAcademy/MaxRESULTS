# Naya Hub Phase 1 API Contract V1

**Status:** IMPLEMENTATION CONTRACT — runtime implementation pending verification

## Purpose

Provide the smallest secure application boundary for the first end-to-end Hub slice:

`MAXESS_RESULT_V1 → member identity → durable result → Hub read → My Results → report`

The API is an adapter, not a new source of truth.

## Truth ownership

| Concern | Authority |
|---|---|
| Stable member ID | Supabase Auth / `public.members` |
| Display name | `public.members` |
| Score | MAXESS canonical scoring engine |
| Result semantics | `MAXESS_RESULT_V1` |
| Historical result | `public.assessment_results` |
| Authentication/session | Supabase Auth |
| API execution | Vercel/server runtime where used |
| Presentation | Naya Hub UI / Groove where used |

## `GET /api/hub/me`

### Purpose
Return the authenticated member boundary and historical results required by Hub Home.

### Authentication
Authenticated session required. No anonymous member lookup.

### Response

```json
{
  "member": {
    "member_id": "uuid",
    "display_name": "Name",
    "email": "name@example.com",
    "created_at": "ISO-8601",
    "updated_at": "ISO-8601"
  },
  "results": [
    {
      "result_id": "uuid",
      "member_id": "uuid",
      "assessment_id": "ai-mastery",
      "assessment_version": "1.0.0",
      "score": 82,
      "mastery_band": "advancing",
      "dimension_results": [],
      "fingerprint": {},
      "result_payload": {},
      "created_at": "ISO-8601"
    }
  ]
}
```

### Rules

- Results are ordered newest first.
- No score calculation occurs.
- No historical result is mutated.
- The API returns stored values exactly as persisted.

## `POST /api/hub/results`

### Purpose
Persist one authoritative `MAXESS_RESULT_V1` for the authenticated member.

### Request

```json
{
  "result": {
    "contractVersion": "MAXESS_RESULT_V1",
    "assessmentId": "ai-mastery",
    "assessmentVersion": "1.0.0",
    "overallScore": 82,
    "masteryBand": "advancing",
    "dimensions": [],
    "responses": [],
    "fingerprint": {}
  }
}
```

### Server requirements

1. Authenticate the request.
2. Resolve the canonical `member_id` from the authenticated identity.
3. Validate the payload contract and required fields.
4. Validate the score range and payload consistency.
5. Preserve the payload as the historical record.
6. Do not recalculate the score.
7. Do not accept a client-supplied `member_id` as authority.
8. Use an idempotency strategy so retries cannot create duplicate authoritative outcomes.
9. Return the persisted `result_id` and canonical stored record.

### Response

```json
{
  "result_id": "uuid",
  "persisted": true,
  "result": {}
}
```

## `GET /api/hub/results/:resultId`

### Purpose
Open the authoritative historical result experience.

### Rules

- Authenticated member must own the result.
- The API returns the stored payload.
- No rescoring.
- No reinterpretation that changes canonical score semantics.

## Error states

- `401` — no authenticated member session.
- `403` — authenticated member does not own the requested result.
- `404` — result does not exist.
- `409` — duplicate/idempotency conflict.
- `422` — invalid `MAXESS_RESULT_V1` payload.
- `500` — persistence/runtime failure; never report success before durable write confirmation.

## Acceptance criteria

- One authenticated person resolves to one stable `member_id`.
- A valid `MAXESS_RESULT_V1` can be persisted exactly once.
- The Hub can retrieve the same stored score and payload after a fresh page load.
- `My Results` reads historical records without rescoring.
- `View Report` resolves the stored authoritative result.
- Client-only state is not required for recovery.
- A persistence failure is visible and never presented as a successful save.

## Next block

Implement the secure Vercel/API adapter against Supabase Auth + the Phase 1 schema, then run the full persistence/reload proof with a real MAXESS result.
