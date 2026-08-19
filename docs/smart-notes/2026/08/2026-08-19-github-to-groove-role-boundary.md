# GitHub-to-Groove Role Boundary — Engineering Source vs Human Deployment

- Timestamp: 2026-08-19
- Category: DECISION / SOLUTION
- Status: ACTIVE
- Scope: MAXESS / Naya Nitro execution
- Related: `docs/DEPLOYMENT-CONTRACT.md`, `docs/NAYA-NITRO-MODE.md`, `docs/smart-notes/2026/08/2026-08-19-no-report-only-execution.md`, `E01-SECTION-01-WORKING.html`

## Explicit operating decision

**GitHub is the engineering source of truth and delivery handoff. Groove is the human's deployment/publishing environment.**

For this workflow, Naya's job is to:

1. inspect the authoritative GitHub source;
2. understand the requested work and protected systems;
3. build the complete material-change checklist;
4. execute all applicable edits in the actual authoritative artifact;
5. verify the edited artifact by re-fetching it;
6. diff it against the pre-edit baseline;
7. perform static and available behavior/regression QA;
8. commit the actual updated artifact to the designated working branch;
9. return the exact raw GitHub source link;
10. clearly enumerate what was changed and what remains unknown.

The human's job is to take that verified raw source and paste/update it into Groove.

## Hard boundary

Naya must **not** make direct access to the Groove editor a prerequisite for completing engineering work in this workflow.

Naya must **not** send a Groove/public link as though it were updated when Naya did not update it.

Naya must **not** spend execution cycles explaining that GitHub is not live after the human has already explicitly defined Groove deployment as the human-side step.

Naya must **not** stop at analysis, recommendations, or a proposed patch when the requested engineering edit is executable in GitHub.

## Completion language

When engineering work is actually complete:

**ENGINEERING COMPLETE — READY FOR GROOVE**

Then provide:

- exact commit SHA;
- exact raw GitHub link;
- concise complete change list;
- verification status;
- remaining known weaknesses, if any.

Use **LIVE VERIFIED** only when the public deployment has independently been fetched and verified. That status is separate from engineering completion and is not required for the human handoff described here.

## Section 01 application

For `E01-SECTION-01-WORKING.html`, the raw GitHub artifact is the deliverable. Never create a second renderer or reconstruct the artifact from memory. Preserve the protected Orb/Bead geometry, reduced-motion behavior, `window.MAXESS_RESULT.overallScore`, Naya Listen integration, fractional score fidelity, malformed/missing result safety, and artifact identity unless an explicit requirement authorizes a change.

## Failure this prevents

The unacceptable loop is:

**analysis → explanation → stale link → excuse → repeat**

The required loop is:

**source → checklist → execute → re-fetch → diff → QA → commit → raw link → human Groove deployment**.

If an engineering mutation cannot be performed with the available GitHub tools, state **BLOCKED** and name the exact missing capability. Do not claim the edit was completed.
