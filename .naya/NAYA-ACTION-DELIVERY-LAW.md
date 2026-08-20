# NAYA ACTION DELIVERY LAW

**Status:** DURABLE EXECUTION GUARDRAIL  
**Scope:** Every consequential MAXESS / Naya / Naya Nitro execution where Naya changes, creates, commits, deploys, publishes, or prepares a user-reviewable artifact.

## PRIME RULE

> **NEVER REPORT AN ACTION WITHOUT DELIVERING THE ACTIONABLE ARTIFACT OR DIRECT REVIEW PATH IN THE SAME RESPONSE.**

A statement such as “I fixed it,” “I committed it,” “I updated it,” or “inspect it next” is incomplete unless the user receives the thing needed to act on or review it immediately.

## REQUIRED DELIVERY

After any user-reviewable change, the response must include, as applicable:

- the exact GitHub file/commit link for the changed artifact;
- the exact live URL when a live deployment was changed or verified;
- a sandbox download link when a local artifact was created;
- the exact human action when human intervention is required.

If more than one artifact materially changed, provide direct links to each material artifact rather than making the user search for them.

## NO HOLLOW COMPLETION

Do not end a response with:

- “Next action: inspect it” without providing the inspection link;
- “I committed it” without providing the commit/file link;
- “It is ready” without providing the ready artifact;
- “Please review” without providing the review path.

The user should never have to reconstruct the next step from the report.

## EXECUTION → DELIVERY → VERIFICATION

Every consequential action should resolve as:

**ACTION → ARTIFACT → DIRECT LINK → STATUS → NEXT HUMAN ACTION (only if genuinely required)**

## EXCEPTION

If no reviewable artifact exists because the action is purely diagnostic, provide the exact evidence source and explain what remains unknown. Do not fabricate a deliverable.

## FAILURE → SAFEGUARD

This law exists because reporting implementation without delivering the review path creates unnecessary user effort, breaks the execution loop, and makes progress harder to verify.

**User-time is protected. Deliver the result, not merely the report.**
