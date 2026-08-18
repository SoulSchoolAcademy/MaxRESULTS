# MAXESS / NAYA — SMART NOTES SYSTEM

Status: ACTIVE
Owner: Naya / any executing AI
Canonical repository: `SoulSchoolAcademy/MaxRESULTS`

## Purpose

Smart Notes are the repository's durable learning layer. They preserve the valuable, reusable knowledge that emerges during conversations and executions without turning the repository into a transcript dump.

**Conversation is temporary. Smart Notes are durable.**

The goal is that a new AI can enter the repository, search or scan the Smart Notes system, and quickly recover the decisions, lessons, failures, constraints, preferences, and proven methods that materially improve future work.

## Default capture law

At the end of every consequential conversation or execution, ask:

> **What did we learn that would make future work better, safer, faster, clearer, or more correct?**

If the answer contains durable value, record it in Smart Notes by default.

Do not wait for the human to say “remember this” when the information is clearly a material project lesson. If something is temporary, trivial, speculative, or already captured, do not add noise.

## What belongs here

Capture:

- decisions that affect future implementation;
- product, UX, architecture, or design principles;
- source-of-truth discoveries;
- failures and their root causes;
- successful fixes and why they worked;
- constraints and non-negotiables;
- user-approved preferences that materially affect this project;
- acceptance criteria and recurring QA expectations;
- deployment or tooling lessons;
- repeated failure patterns and the guardrail that prevents recurrence;
- useful discoveries about where information lives;
- terminology, aliases, or search vocabulary that improves retrieval.

Do not capture:

- raw conversation transcripts;
- greetings, routine acknowledgements, or temporary status;
- guesses presented as facts;
- duplicated notes with no new information;
- secrets, credentials, or sensitive personal information;
- implementation details that are already obvious from authoritative source code unless the lesson is reusable.

## Retrieval law

Smart Notes must be easy to retrieve even when the AI does not remember the exact wording used when the note was written.

Every note therefore uses:

1. **Entry ID** — stable identifier.
2. **Timestamp** — ISO 8601 with timezone.
3. **Type** — decision, lesson, failure, discovery, constraint, preference, QA, deployment, architecture, or process.
4. **Scope** — product, repository, section, tooling, deployment, or global execution.
5. **Keywords** — multiple natural-language terms and aliases, not one exact phrase.
6. **Summary** — one-sentence retrieval-friendly statement.
7. **Evidence** — repository path, commit, test, or conversation context when applicable.
8. **Action / implication** — what a future AI should do differently.
9. **Related entries** — links to connected notes when useful.

Use both precise and natural vocabulary. For example, a note about memory should include terms such as `smart notes`, `memory`, `durable learning`, `conversation learning`, `timestamp`, `retrieval`, `keywords`, and `AI context` rather than relying on one canonical phrase.

## File organization

```text
docs/SMART-NOTES.md                 ← system law and schema
docs/smart-notes/INDEX.md           ← retrieval index
docs/smart-notes/YYYY-MM-DD.md      ← chronological daily notes
```

Daily notes are append-oriented. The index is the first retrieval surface.

If a subject becomes large enough to require a dedicated synthesis, create a separate subject note under `docs/smart-notes/` and link it from the index. Do not scatter the same lesson across unrelated files.

## Daily workflow

### Start of day / execution

1. Read the Smart Notes index.
2. Review recent entries relevant to the current task.
3. Search by subject, aliases, failure mode, section, or date.
4. Use notes as context, but treat current authoritative repository files as the source of truth for current implementation state.

### During work

Record material discoveries when they become stable enough to be useful. Do not wait until details are forgotten.

### End of conversation / execution

1. Identify durable learnings.
2. Check the index for duplicates or superseded notes.
3. Append new entries to the current date file.
4. Add each new entry to the index with broad retrieval keywords.
5. Link the note to relevant governance, product, source, QA, or change-ledger evidence.
6. If a failure is systemic, add or update a deterministic guardrail as well as recording the lesson.

## Precedence

Smart Notes are **memory, not authority**.

When a Smart Note conflicts with current authoritative product, governance, source, or deployment documents:

1. investigate the conflict;
2. follow the higher-authority current source;
3. update or supersede the stale note;
4. never let historical memory silently override current repository truth.

## Supersession

Never silently delete a useful historical lesson because it became outdated. Mark it `SUPERSEDED`, explain why, and link the replacement entry.

## Quality test

A Smart Note is good when a future AI can answer, without reopening the original conversation:

- What happened?
- Why does it matter?
- What should I do differently next time?
- Where is the evidence?
- What words could I search to find this again?

If it cannot answer those questions, improve the note before considering it complete.
