# NAYA EXECUTION INCIDENT LOG

**Purpose:** Durable record of execution/procedure failures and the guardrails created to prevent recurrence.

## INCIDENT 2026-08-20 — ACTION WITHOUT IMMEDIATE DELIVERY EVIDENCE

**Failure:** Naya reported a GitHub change but did not consistently place the direct review artifact/link in the same response.

**User impact:** The user had to ask for the link, creating unnecessary interaction, wasted time, and loss of trust in the execution process.

**Root cause:** The communication law existed, but delivery evidence was not enforced as a hard pre-delivery gate. The model could satisfy the narrative portion of the response while omitting the actionable artifact.

**Guardrail:** `docs/NAYA-MASTER-EXECUTION-GATE.md`

**New mandatory rule:** A material action is incomplete until the same response contains the appropriate direct artifact/evidence.

**Delivery mapping:**
- GitHub file → direct file link
- commit → direct commit link
- branch → branch link
- PR → PR link
- live deployment → live URL
- generated artifact → download link
- prompt → complete copy/paste prompt
- human review → exactly one concrete review action

**Verification:** The gate explicitly defines the required mapping and forbids telling the user to “inspect it” without providing the artifact.

**Status:** GUARDRAIL IMPLEMENTED.

---

## INCIDENT 2026-08-20 — REPEATED PROCEDURE DRIFT DESPITE EXISTING LAWS

**Failure:** Naya had governing laws and Lead-Service documentation but still occasionally bypassed the intended procedure in live conversation.

**Root cause:** Documentation alone was treated as sufficient. There was no single explicit stop-the-line execution gate requiring a preflight before action/communication and a postflight before delivery claims.

**Guardrail:** `docs/NAYA-MASTER-EXECUTION-GATE.md`

**New mandatory model:**

**GATE A:** READ → MAP → ESTABLISH STATE → PLAN → SCOPE-LOCK

**GATE B:** VERIFY → DELIVER EVIDENCE → STATE LIMITS → NEXT ACTION

**Status:** GUARDRAIL IMPLEMENTED.

---

## LEARNING PRINCIPLE

Repeated execution failures must become durable system improvements.

The process is:

**FAILURE → ROOT CAUSE → GUARDRAIL → TEST → LOG**

Do not rely on apology, memory, or good intentions as the control.
