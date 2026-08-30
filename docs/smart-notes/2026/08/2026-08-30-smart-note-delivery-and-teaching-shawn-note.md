# Smart Note Delivery + NayaPOWER Teaching — Shawn Note

- Timestamp: 2026-08-30 (exact time unavailable)
- Category: LEARNING
- Status: ACTIVE
- Scope: PROJECT
- Keywords: Smart Note, Naya Note, Machine Note, Shawn Note, receipts, Smart Links, PIS, Running Feed, proactive capture, teaching, NayaPOWER, cold-start test
- Aliases: Smart Note delivery contract, Naya Notes, durable memory, Naya teaching activation
- Related: `docs/NAYA-NOTES-MASTER-ACTIVATION-SPECIFICATION.md`; `docs/NAYA-SMART-NOTE-DELIVERY-AND-PIS-TRIGGER-CONTRACT.md`; `MASTER-NOTES/PRIMARY-INTELLIGENCE-HUB.md`; `.naya/SUPERBRAIN-COLLECTIVE-RUNNING-FEED.md`; `Teaching`; aligned Naya Note; aligned Machine Note

## Context

Shawn explicitly requested a Smart Note after reviewing the 2026-08-30 cold-start intelligence test and then identified a serious delivery failure: the assistant had understood the lesson but did not return the required Shawn Note, Naya Note, Machine Note, direct Smart Links, exact evidence, or explicit PIS/Running Feed state. Shawn also clarified the intended NayaPOWER teaching experience: people should be able to ask Naya to teach them NayaPOWER in simple, effective language, with the goal of comprehension and practical use rather than merely receiving a curriculum dump.

## What We Learned / Decided

1. An explicit Smart Note request is an execution request, not a request to draft prose.
2. A completed Smart Note delivery must contain three aligned representations of one underlying intelligence event: Shawn Note, Naya Note, and Machine Note.
3. The human-facing response must include direct Smart Links and exact receipts/evidence for what was actually persisted or verified.
4. Note creation, PIS propagation, and Running Feed update are separate state transitions and must each be reported honestly.
5. Naya should proactively recognize durable value in substantive conversations and capture it when legitimate storage is available, without waiting for the human to ask.
6. NayaPOWER teaching should optimize for rapid comprehension, practical understanding, and immediate use. It should explain what NayaPOWER is, why it matters, how it works, what Smart Notes do, how learning compounds, how evidence works, and how a person can begin using the system.
7. The customer activation experience should teach while it activates rather than dumping documents and requiring the customer to reconstruct the system themselves.

## Why It Matters

This closes a critical gap between understanding intelligence and delivering durable intelligence. If Naya can learn something but cannot reliably preserve, expose, and propagate that learning, the Superbrain cannot be trusted to compound. Likewise, if people cannot understand NayaPOWER quickly enough to use it, the technology's value remains inaccessible.

## Required Behavior

When Shawn asks for a Smart Note, Naya must execute the canonical Smart Note delivery lifecycle and return the complete evidence bundle in the same response. When Naya independently detects durable value, she should capture it proactively when legitimate storage is available and tell the human what she captured, why it matters, and where the evidence is. When teaching NayaPOWER, Naya should use simple language, concrete examples, progressive disclosure, comprehension checks when useful, and an immediate next action rather than a document-dump teaching style.

## Evidence / Source

- 2026-08-30 cold-start intelligence test supplied by Shawn and its resulting fresh-Naya response.
- `docs/NAYA-SMART-NOTE-DELIVERY-AND-PIS-TRIGGER-CONTRACT.md` explicitly requires Shawn/Naya/Machine representations, Smart Links, receipts, propagation state, and Running Feed state.
- `Teaching` already teaches NayaPOWER as experience → learning → captured intelligence → future use and identifies talk/create/learn as the three starting doors.
- `MASTER-NOTES/PRIMARY-INTELLIGENCE-HUB.md` records the Smart Note evidence rule and the durable lesson that activation must teach while it activates.

## Follow-up

Use this learning as a regression target for future explicit Smart Note requests and as source material for the customer activation teaching experience.
