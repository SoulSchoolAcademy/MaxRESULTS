# No-Report-Only Execution Gate

- Timestamp: 2026-08-19
- Category: LEARNING / EXECUTION
- Status: ACTIVE
- Scope: Naya Nitro / MAXESS execution
- Related: `E01-SECTION-01-WORKING.html`, `docs/NAYA-NITRO-MODE.md`, `docs/DEPLOYMENT-CONTRACT.md`

## Failure
A consequential execution can fail even when the assistant produces an accurate analysis, because reporting findings is not implementation. A plan, critique, or proposed diff is not evidence of completion.

## Required gate
For every requested material change, the execution must reach an observable mutation before the response may claim work was completed:

1. Fetch the authoritative current source.
2. Build the complete material-change checklist.
3. Execute every applicable checklist item in one coherent implementation batch.
4. Re-fetch the edited source.
5. Produce a source diff against the pre-edit baseline.
6. Run static QA.
7. Run behavior/regression QA to the extent the available tools permit.
8. Commit the actual edited artifact.
9. Return the exact raw source link and exact commit SHA.
10. Distinguish IMPLEMENTED / VERIFIED / LIVE VERIFIED / HUMAN REVIEW REQUIRED / UNKNOWN.

## Hard rule
**No report-only completion.** If the user asked for execution and a material edit is required, do not stop after analysis, recommendations, or a proposed patch. If the required mutation cannot be performed with available tools, state BLOCKED and identify the exact missing capability rather than claiming completion.

## Section 01 application
For E01, the protected Orb/Bead system and result plumbing remain source-locked. Refinements must be surgical, followed by re-fetch → diff → QA → regression. The final deliverable must point to the actual updated `E01-SECTION-01-WORKING.html`, not a reconstructed or second renderer.
