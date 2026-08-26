# NEXT EXECUTION — AUTHORITATIVE ZERO-COST RETRIEVAL VERIFICATION + PDF ACTIVATION

schema_version: 6
status: READY

## Project
Naya Power Superbrain (`PRJ-NAYAPOWER-SUPERBRAIN`)

## North Star
A user should be able to give Naya knowledge—not configure infrastructure—and Naya should turn that knowledge into a verified, recoverable, high-recall personal Superbrain automatically.

## Current state
The current main head is `846529daea1bd35af564bdc061f3fb74a1b7f485`. It contains a dependency-free retrieval upgrade. The previous authoritative GREEN remains `9aefe57a71bd6425681bb435d70417ad33832198`, run `32909426069`, brain-gate `98000403862`. The protected GREEN boundary remains `0f82325a82ed37b5b3a3d097599025369c03a1ed`.

Current-head status is intentionally PENDING until authoritative CI observes the exact head.

## Implemented retrieval capabilities
- Exact event-ID/title/subject matching.
- BM25 lexical ranking.
- TF-IDF cosine ranking.
- Hard metadata filters: project, event type, status, tag, since/until.
- Transparent domain query expansion.
- Recency weighting.
- Authority and verification weighting.
- Relationship-aware reranking.
- Unknown queries fail closed instead of returning arbitrary zero-score events.
- Impossible metadata filters fail closed.
- Relevance-judged benchmark measures precision@5, recall@5, MRR, and token coverage.
- Positive and deliberate-failure retrieval tests are part of the authoritative gate.

## Architectural boundary
Canonical event JSON remains authoritative. Retrieval indexes and future vectors are derived representations. No vector database is required for this 1.0 baseline.

## P0 — Execute first
1. Verify exact `main` SHA.
2. Obtain a fresh authoritative `.github/workflows/superbrain-gate.yml` execution against that exact SHA.
3. Inspect the real `brain-gate` job and every substantive step.
4. Confirm retrieval quality regression and deliberate-failure tests pass.
5. Confirm retrieval benchmark executes and records precision/recall/MRR.
6. Confirm all previous GREEN boundaries remain GREEN.
7. Only promote the exact head to GREEN when authoritative evidence proves it.

## If RED
Preserve the exact failure evidence. Identify the smallest true root cause. Repair source, not validator. Rerun against the repaired head. Never call a previous commit's GREEN proof evidence for the new head.

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
