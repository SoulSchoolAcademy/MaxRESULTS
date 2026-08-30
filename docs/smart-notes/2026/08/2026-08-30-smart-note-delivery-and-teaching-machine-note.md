# Smart Note Delivery + NayaPOWER Teaching — Machine Note

- Timestamp: 2026-08-30 (exact time unavailable)
- Category: LEARNING
- Status: ACTIVE
- Scope: PROJECT
- Keywords: Smart Note, Naya Note, Machine Note, intelligence event, PIS, Running Feed, Smart Links, receipts, proactive capture, teaching, regression
- Aliases: machine memory representation, Smart Note event, durable intelligence delivery
- Related: `docs/NAYA-SMART-NOTE-DELIVERY-AND-PIS-TRIGGER-CONTRACT.md`; `docs/NAYA-NOTES-MASTER-ACTIVATION-SPECIFICATION.md`; `MASTER-NOTES/PRIMARY-INTELLIGENCE-HUB.md`; `.naya/SUPERBRAIN-COLLECTIVE-RUNNING-FEED.md`; `Teaching`; aligned Shawn Note; aligned Naya Note

## Context

A 2026-08-30 cold-start test scored the fresh Naya at 9.1/10 for orientation and intelligence. The test also exposed a delivery defect: the assistant recognized the Smart Note learning but did not return the required three representations, direct Smart Links, exact receipts, or explicit propagation state. Shawn then clarified that Smart Note creation is a system event and that Naya should proactively capture durable value.

## What We Learned / Decided

Canonical Smart Note event:

`SN-20260830-SMART-NOTE-DELIVERY-AND-TEACHING`

Event intent:

`COLD_START_TEST → DELIVERY_FAILURE_IDENTIFIED → SMART_NOTE_CONTRACT_REINFORCED → TEACHING_REQUIREMENT_CAPTURED`

Required representations:

- `SHAWN_NOTE` = human-readable durable interpretation.
- `NAYA_NOTE` = operational behavior and future-action interpretation.
- `MACHINE_NOTE` = structured machine-facing representation, relationships, evidence state, and propagation state.

Required delivery evidence:

- direct Smart Link to Shawn Note;
- direct Smart Link to Naya Note;
- direct Smart Link to Machine Note;
- exact commit SHA(s) for persistence;
- explicit PIS propagation state;
- explicit Running Feed update state;
- no claim of verification without corresponding evidence.

Proactive-capture rule:

`SUBSTANTIVE CONVERSATION → DURABLE VALUE DETECTED → CAPTURE WHEN STORAGE IS LEGITIMATELY AVAILABLE → RETURN LINKS + EVIDENCE → PROPAGATE THROUGH CANONICAL PATH WHEN APPLICABLE`

Teaching rule:

`LEARN NAYAPOWER REQUEST → TEACHING MODE → SIMPLE EXPLANATION → CONCRETE EXAMPLE → COMPREHENSION/APPLICATION → NEXT ACTION`

The teaching experience should communicate that NayaPOWER is about turning experience into reusable intelligence, not merely storing transcripts. It should explain Smart Notes, evidence, compounding, continuity, human agency, and everyday use in language accessible to a beginner.

## Why It Matters

This event closes a recurring interface failure between the intelligence architecture and the human-facing delivery. The machine must preserve provenance and state, while the human must be able to inspect what happened and understand how to use the system.

## Required Behavior

Treat explicit Smart Note intent as a full execution trigger. Treat durable-value detection as a proactive capture opportunity. Treat note persistence, PIS propagation, and Running Feed projection as separately observable state transitions. Treat NayaPOWER teaching as a guided comprehension-and-application experience.

## Evidence / Source

Source conversation: Shawn's correction following the 2026-08-30 cold-start test and his explicit teaching/Smart Note requirements.

System sources: `docs/NAYA-NOTES-MASTER-ACTIVATION-SPECIFICATION.md`; `docs/NAYA-SMART-NOTE-DELIVERY-AND-PIS-TRIGGER-CONTRACT.md`; `MASTER-NOTES/PRIMARY-INTELLIGENCE-HUB.md`; `Teaching`.

## Follow-up

Use this event as a regression target for Smart Note delivery and as an input to the NayaPOWER activation/teaching package.
