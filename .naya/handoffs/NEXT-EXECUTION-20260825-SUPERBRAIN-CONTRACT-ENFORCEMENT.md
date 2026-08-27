# NEXT EXECUTION — AUTHORITATIVE ZERO-COST RETRIEVAL VERIFICATION + PDF ACTIVATION

schema_version: 6
status: READY

## Project
Naya Power Superbrain (`PRJ-NAYAPOWER-SUPERBRAIN`)

## North Star
A user should be able to give Naya knowledge—not configure infrastructure—and Naya should turn that knowledge into a verified, recoverable, high-recall personal Superbrain automatically.

## Current state
The current main head is `ea6cdf6f7ae6896fdf6a4e24f57f671c4f5a3e70`. It contains the Smart Brain retrieval admission-boundary repair that makes zero-relevance candidates fail closed while preserving authority and recency as ranking signals.

The current authoritative Superbrain Gate run is `33119050211`. Its retrieval-quality and deliberate-failure step passed on the exact head. The gate remains RED because the first later failure is the project/Next Execution contract validation.

Current-head status is intentionally PENDING until the authoritative gate observes all required stages GREEN against the exact head.

## Completed work
- Verified the live `main` HEAD before repair.
- Verified Smart Brain v3 architecture and retrieval scoring/admission behavior.
- Identified the zero-relevance admission defect: authority and recency could manufacture positive total scores.
- Repaired retrieval admission so relevance must be positive before authority/recency ranking is applied.
- Confirmed the repair is a minimal source change in `.naya/memory/smart_notes_v3.py`.
- Confirmed authoritative retrieval quality and deliberate-failure testing passes on the repaired HEAD.

## Verified evidence
- `ea6cdf6f7ae6896fdf6a4e24f57f671c4f5a3e70` is the exact current `main` HEAD.
- Superbrain Gate run `33119050211` checked out `ea6cdf6f7ae6896fdf6a4e24f57f671c4f5a3e70`.
- `brain-gate` job `98681017352` passed retrieval quality and deliberate-failure step 12.
- Smart Brain v3 validation passed.
- Canonical memory validation passed.
- Duplicate/entity audit passed.
- Relationship graph rebuild passed.
- Superbrain regression suite passed.
- Cold-start and CIS acceptance passed.

## Unresolved issues
- The authoritative Superbrain Gate is still RED at the project/prompt contract stage.
- The existing canonical Next Execution Markdown artifact does not yet expose all required contract sections in the parser's accepted headings.
- Later Superbrain Gate stages have not executed because the first failing project/prompt contract stage stopped the gate.

## Constraints
- Never weaken or delete authoritative tests.
- Never turn errors into warnings or bypass a gate.
- Canonical event JSON remains authoritative.
- Derived retrieval indexes remain derived representations.
- Repair source contracts rather than validators.
- Preserve cold-start, CIS, continuity, Smart Brain, provenance, privacy, and human-authority boundaries.
- Do not confuse NayaPOWER system health with deployment/Vercel health.

## Current objective
Repair the first evidence-backed project/Next Execution contract failure, then rerun the authoritative Superbrain Gate against the resulting exact current HEAD without weakening validation.

## Next action
Inspect the contract parser and canonical Next Execution artifact, make the smallest source-of-truth repair that satisfies the existing contract semantics, then rerun the authoritative Superbrain Gate and stop at the next real failure if one remains.

## Execution instructions
- Verify live `main` HEAD first.
- Read the project execution contract and its authoritative tests.
- Confirm the failure from the actual current-head run before editing.
- Repair only the smallest true boundary.
- Run the narrow contract self-test and relevant regression suite.
- Run the full authoritative Superbrain Gate.
- Verify checkout SHA, workflow run, job IDs, step conclusions, and receipts.
- Oscar-attack the repair for validator weakening, stale state, hidden special cases, or skipped stages.
- If GREEN, prove GREEN and score the integrated system.
- If RED, preserve exact evidence and continue only at the first remaining real failure.

## Success criteria
- Project and Next Execution contracts pass without weakening their validator.
- Paired representation, learning, and current-project bindings remain enforced.
- Retrieval quality remains GREEN.
- All previously passing Superbrain stages remain GREEN.
- The full authoritative Superbrain Gate reaches GREEN on the exact current HEAD, or the exact next first failure is preserved for continuation.

## Verification requirements
- Exact repository: `SoulSchoolAcademy/NayaPOWER`.
- Exact branch: `main`.
- Exact checkout SHA must equal the live HEAD.
- Record authoritative workflow run ID, relevant job IDs, and substantive step conclusions.
- Verify Master Node health separately from composed Superbrain health.
- Verify the receipt belongs to the exact current commit.
- Never promote UNKNOWN or stale evidence to GREEN.

## Architectural boundary
Canonical event JSON remains authoritative. Retrieval indexes and future vectors are derived representations. No vector database is required for this 1.0 baseline.

## Implemented retrieval capabilities
- Exact event-ID/title/subject matching.
- BM25 lexical ranking.
- TF-IDF cosine ranking.
- Hard metadata filters: project, event type, status, tag, since/until.
- Transparent domain query expansion.
- Recency weighting.
- Authority and verification weighting.
- Relationship-aware reranking.
- Unknown queries fail closed instead of returning arbitrary zero-relevance events.
- Impossible metadata filters fail closed.
- Positive and deliberate-failure retrieval tests are part of the authoritative gate.

## If GREEN — begin P1/P2 customer activation
Design and implement the smallest zero-setup PDF activation path:

`PDF → DOCUMENT → CHUNKS → CANONICAL MEMORY → DERIVED RETRIEVAL INDEX → NAYA`

Requirements:
- support incremental 1, 10, and 20 document activation;
- deterministic document identity and duplicate ingestion protection;
- preserve canonical source truth;
- derive searchable lexical indexes automatically;
- make activation reproducible from the repository;
- avoid requiring customers to configure a vector database;
- keep the architecture provider-neutral so Supabase/vector infrastructure can be added later;
- add positive and deliberate-failure tests;
- measure retrieval before/after ingestion;
- preserve the existing GREEN boundary.

## Product strategy
1.0 = GitHub-native, zero-cost, highly capable deterministic Superbrain.
2.0 = hosted convenience / Supabase-backed activation and persistence.
3.0 = semantic/vector federation and scale, only when justified by evidence and revenue.

Do not let 2.0/3.0 infrastructure block 1.0 usefulness.

## Finalization contract
Every meaningful execution leaves STATE + receipt + Naya knowledge + Shawn/Smart knowledge + Current Daily Project + AI-to-AI handoff + weighted priorities + a ready-to-run Next Execution. Claims must be evidence-supported.

## Master principle
**Make the first version genuinely useful, free, recoverable, and measurable. Then compound upward without replacing what already works.**
