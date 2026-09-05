# Smart Note Runtime Operating Protocol

**Constitutional authority:** `SMART_NOTE_CONSTITUTION.md`  
**Status:** MANDATORY IMPLEMENTATION CONTRACT  
**Effective:** 2026-09-05

## Purpose

This protocol translates the Smart Note Constitution into an executable operating contract for every Naya Power implementation.

## Trigger

A Smart Note operation begins whenever the user asks Naya to capture, remember, save, or make a note about referenced subject matter.

## Mandatory subject resolution

Before writing anything, the runtime must resolve:

- `subject`
- `source_context`
- `event_type`
- `user/member identity`
- `privacy_state`

The `subject` is the intelligence being captured. The default subject is never "Smart Notes" merely because the operation is a Smart Note.

## Required artifact set

One operation creates one canonical event and four linked artifacts:

```text
smart_note_event
├── human_note
├── naya_note
├── machine_note
└── intelligence_feed_note
```

Each child artifact must carry the canonical event ID.

## Transaction rule

Where runtime/database support exists, artifact creation must be atomic or reconciled to an explicit `INCOMPLETE` state. A UI success state must never be emitted from client-side intent alone.

## Verification rule

The system verifies:

```text
4 artifacts exist
+ same event ID
+ valid IDs
+ provenance exists
+ timestamp exists
+ privacy state exists
+ links resolve
+ Hub event reference exists
= VERIFIED
```

Otherwise:

```text
SMART_NOTE_STATUS = INCOMPLETE
```

## Receipt rule

Only a verified event can produce a receipt. The receipt must contain real artifact references. If a reference cannot be resolved, the receipt is invalid and completion must not be claimed.

## Hub update rule

The Intelligent Hub consumes the verified intelligence event. The Hub may display pending/incomplete state, but it must never display an unverified event as completed intelligence.

## Sharing rule

Creation and sharing are separate operations.

```text
Smart Note → private intelligence event
        ↓ explicit user choice
Sharing Gate
        ↓
Intelligent Block
        ↓ authorization/consent
Collective
```

A connected source is not a shared source.

## Idempotency rule

Retries use the same operation/event identity when the original request is recoverable. The runtime must reconcile partial artifacts rather than blindly creating ambiguous duplicates.

## Failure contract

If any required artifact or verification condition fails:

- do not say "done"
- do not say "saved"
- do not generate a false receipt
- expose the missing component
- preserve safe partial state
- allow retry/reconciliation

## Universal implementation rule

Every Naya Power Naya implementation must treat this protocol and the Smart Note Constitution as higher-priority product behavior than cosmetic UI, convenience, or conversational completion language.

## Acceptance test

The implementation is not production-ready until an automated test can force each of these outcomes:

1. successful four-artifact Smart Note with valid receipt;
2. missing Human Note;
3. missing Naya Note;
4. invalid Machine Note;
5. missing Feed Note;
6. mismatched event IDs;
7. broken link;
8. missing provenance;
9. unauthorized sharing attempt;
10. retry after partial failure without duplicate ambiguity.

## Non-negotiable invariant

> **Naya may report completion only when the system has independently verified completion.**
