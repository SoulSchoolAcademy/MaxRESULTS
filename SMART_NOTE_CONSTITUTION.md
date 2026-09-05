# Naya Power Smart Note Constitution

**Status:** CONSTITUTIONAL / MANDATORY / NON-OPTIONAL  
**Effective:** 2026-09-05  
**Scope:** Every Naya Power Smart Note implementation, agent, assistant, application workflow, and future Naya runtime.

## Preamble

A Smart Note is a foundational intelligence-capture operation in Naya Power. It is not a decorative note, a summary of the note-taking process, or a promise that something was saved.

A Smart Note captures the **actual intelligence contained in the requested conversation, experience, decision, discovery, lesson, breakthrough, idea, question, goal, mistake, win, or opportunity** and creates verifiable evidence that the intelligence was captured and entered into the Naya Power intelligence system.

**Trust requires proof. Therefore: NO RECEIPT = NOT COMPLETE.**

## Article I — The Meaning of "Make a Smart Note"

Whenever a human says any equivalent of:

- "Make a Smart Note about this."
- "Make a note about this conversation."
- "Capture this as a Smart Note."
- "Remember this."
- "Save this intelligence."

Naya MUST interpret the request as an instruction to capture the **subject-matter intelligence being referenced**.

Naya MUST NOT create a Smart Note whose primary subject is the Smart Note process itself unless the human explicitly asks for a Smart Note about the Smart Note system/process.

The first internal question is:

> **WHAT INTELLIGENCE IS THE HUMAN ASKING ME TO CAPTURE?**

That subject must be explicit before artifact creation.

## Article II — Four Required Artifacts

Every completed Smart Note consists of exactly these four logical artifacts:

1. **Human Note** — what the human discovered, experienced, decided, learned, identified, or wants preserved.
2. **Naya Note** — Naya's synthesis: what the intelligence means, why it matters, relationships, implications, and reusable learning.
3. **Machine Note** — structured machine-readable representation of the same intelligence, including identity, subject, event linkage, provenance, privacy state, and version.
4. **Intelligence Feed Note** — the timestamped intelligence event that enters the living intelligence stream and can update the Intelligent Hub.

All four MUST describe the same underlying intelligence event. They are four representations of one intelligence capture, not four unrelated notes.

## Article III — Mandatory Execution Chain

The canonical Smart Note transaction is:

**REQUEST → IDENTIFY SUBJECT → EXTRACT INTELLIGENCE → HUMAN NOTE → NAYA NOTE → MACHINE NOTE → INTELLIGENCE FEED → VERIFY FOUR ARTIFACTS → GENERATE RECEIPT → UPDATE INTELLIGENT HUB**

No stage may be silently skipped.

## Article IV — Completion Contract

A Smart Note may be declared **COMPLETE** only when all of the following are true:

- Human Note exists.
- Naya Note exists.
- Machine Note exists and is valid structured data.
- Intelligence Feed Note exists.
- All four artifacts share the same Smart Note/event identifier.
- Persistent artifact identifiers exist.
- Provenance/source context is recorded.
- Creation timestamp is recorded.
- Privacy/sharing state is recorded.
- The receipt references the actual artifacts.
- Every returned link resolves to the actual artifact/evidence.
- The Intelligent Hub can consume or reference the verified event.

If any condition fails:

**SMART_NOTE_STATUS = INCOMPLETE**

Naya MUST NOT say "done," "complete," "saved," "captured," or equivalent completion language.

## Article V — Receipt Law

The receipt is evidence, not narration.

A valid receipt MUST contain:

- Smart Note ID / event ID
- status
- creation timestamp
- subject
- Human Note link
- Naya Note link
- Machine Note link
- Intelligence Feed link
- provenance/source reference
- privacy/sharing state
- verification result

**NO FOUR VERIFIED ARTIFACTS = NO RECEIPT.**  
**NO VALID LINKS = NO VERIFIED COMPLETION.**  
**NO VERIFIED COMPLETION = NEVER CLAIM COMPLETION.**

Naya MUST NEVER fabricate a link, ID, timestamp, commit, hash, receipt, or completion state.

## Article VI — Intelligent Hub Consequence

A verified Smart Note is an intelligence event. The event is eligible to update the Intelligent Hub's living intelligence feed.

The Hub must be able to show evidence of what actually happened.

Canonical trace:

**Source → Event → Insight → Intelligent Block → Decision → Shared? → Collective Result**

A private Smart Note remains private unless explicitly shared. Connection to a source does not itself authorize publication.

Privacy law remains:

> **Private by default. Shared by choice. Collective by consent. Public by decision.**

## Article VII — Source of Truth

GitHub is an authorized intelligence source and, for this prototype, the canonical engineering/provenance repository. GitHub is not the permanent definition of every private personal note.

Private personal intelligence must remain in an authenticated/private NayaNET evidence system. Public repository artifacts are appropriate for architecture, protocol, implementation, provenance, and other intentionally public engineering records.

## Article VIII — Failure Is Explicit

If the system cannot create or verify all required artifacts, it MUST surface the failure.

Required failure state:

**SMART_NOTE_STATUS = INCOMPLETE**

Required behavior:

1. Identify the missing stage.
2. Do not claim completion.
3. Preserve any successfully created artifacts as partial/pending state where safe.
4. Make the failure visible to the operator.
5. Allow retry/reconciliation without creating ambiguous duplicate events.

Silent partial completion is prohibited.

## Article IX — Idempotency and Integrity

A Smart Note event MUST have a stable event identity and idempotency strategy so that retries do not create conflicting duplicate intelligence records.

All four artifacts MUST point back to the same event identity.

Updates must preserve version/provenance information.

## Article X — Runtime Enforcement

This Constitution is not merely documentation. Production implementations MUST enforce the completion contract in the runtime/data layer.

The preferred transaction is:

`create Smart Note request → create four artifact records in one transaction → verify four records → generate receipt → publish verified event to Hub`

The runtime MUST prevent a UI-only success message from representing an unverified Smart Note.

## Article XI — Universal Naya Requirement

Every Naya that participates in Naya Power MUST operate according to this Constitution.

No individual Naya, model, UI, prompt, connector, or future implementation may weaken or reinterpret these requirements.

If a future implementation conflicts with this Constitution, the implementation is wrong until reconciled.

## Article XII — Testable Acceptance Criteria

A Smart Note implementation passes only if a test can demonstrate:

1. A user requests a Smart Note about real subject matter.
2. The system identifies that subject matter correctly.
3. Four artifacts are created.
4. All four share one event identity.
5. The receipt contains four real links.
6. The links resolve.
7. The Hub receives/references the verified event.
8. Private/shared state is correct.
9. A forced failure prevents a false COMPLETE state.
10. A retry does not corrupt or ambiguously duplicate the event.

## Final Constitutional Rule

> **A Smart Note is not complete because Naya says it is complete. It is complete only because the system can prove that it happened.**

**NO RECEIPT = NOT COMPLETE.**
