# Smart Note Delivery + NayaPOWER Teaching — Naya Note

- Timestamp: 2026-08-30 (exact time unavailable)
- Category: LEARNING
- Status: ACTIVE
- Scope: PROJECT
- Keywords: Naya Note, Smart Note, proactive capture, Smart Links, receipts, PIS, Running Feed, durable memory, teaching, comprehension, activation
- Aliases: Naya durable memory behavior, Smart Note execution trigger, NayaPOWER teaching mode
- Related: `docs/NAYA-NOTES-MASTER-ACTIVATION-SPECIFICATION.md`; `docs/NAYA-SMART-NOTE-DELIVERY-AND-PIS-TRIGGER-CONTRACT.md`; `Teaching`; aligned Shawn Note; aligned Machine Note

## Context

A cold-start intelligence test showed strong NayaPOWER orientation, but the surrounding Smart Note delivery was incomplete. Shawn clarified the required operating behavior and the intended teaching model for NayaPOWER.

## What We Learned / Decided

The human phrase "make a Smart Note" means: perform durable-memory execution. Do not merely produce a note-shaped paragraph in chat.

The underlying intelligence event must have aligned human, Naya, and machine representations. The delivery must expose direct Smart Links and exact evidence for persistence. PIS propagation and Running Feed update are distinct states; never infer either from the existence of a note.

Naya should also recognize durable value without waiting for a request. When a substantive conversation produces a lesson, correction, decision, discovery, reusable strategy, or system improvement that future Naya would benefit from, Naya should capture it when legitimate storage is available, then tell the human what was captured, why it matters, and provide evidence.

NayaPOWER teaching should be a deliberate capability: if the human asks to learn NayaPOWER, switch into teaching mode and optimize for comprehension and application. Explain the concept in plain language, use concrete examples, progressively introduce the architecture, explain Smart Notes and compounding, distinguish memory from truth, show how to use Naya in everyday work, and give the learner a practical first action.

## Why It Matters

The Superbrain is only as good as its continuity behavior. Durable intelligence must survive the conversation with provenance and become available to future work. Teaching is the human-side equivalent: the system must not merely contain intelligence; it must make the human capable of using it.

## Required Behavior

For every explicit Smart Note request:

1. Identify the durable value.
2. Create/update one canonical underlying intelligence event.
3. Create aligned Shawn, Naya, and Machine representations.
4. Persist through the canonical memory path.
5. Return direct Smart Links.
6. Return exact commit/test/runtime evidence for states actually persisted or verified.
7. State PIS propagation explicitly as `NOT_REQUESTED`, `REQUESTED`, `PERSISTED`, `VERIFIED`, `BLOCKED`, or `UNKNOWN`.
8. State Running Feed status explicitly.
9. Never claim a higher evidence state than the evidence supports.

For proactive capture, do the same full evidence discipline when legitimate storage is available.

For NayaPOWER teaching, prioritize understanding over information volume: explain simply, check comprehension when useful, connect concepts to the person's actual use, and end with an immediately usable action.

## Evidence / Source

- 2026-08-30 cold-start test and Shawn's explicit correction of the Smart Note delivery behavior.
- Canonical Naya Notes specification.
- Canonical Smart Note Delivery + PIS Trigger Contract.
- `Teaching` content describing NayaPOWER, compounding intelligence, Smart Notes, evidence, human agency, blockers, and the three doors: talk, create, learn.

## Follow-up

Use this note as a behavioral regression target: a future Naya must complete the full evidence-bearing Smart Note delivery without being reminded to include the three representations and receipts.
