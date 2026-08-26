# 🧠 MAXESS SMART NOTE — CONTINUOUS EXECUTION + LEARNING

**Date:** 2026-08-26  
**Type:** Smart Note / durable project learning  
**Scope:** MAXESS V2 execution process  
**Status:** LOCKED INTO OPERATING PRACTICE

## Discovery

The most important improvement is not another code patch. It is making the execution process itself cumulative.

During the MAXESS V2 Groove work, the team established a successful authoritative-engine adapter path and a pre-test excellence gate. The next improvement is to make every execution automatically teach the next execution.

## New operating insight

Every substantive execution should produce three outputs:

1. **The work itself** — code, verification, or decision.
2. **A Smart Note** — what the team learned.
3. **An AI/Naya handoff** — everything the next intelligence needs to succeed without rediscovery.

The conversational response should also end with a copy-paste-ready next execution prompt whenever further work remains.

## Why this matters

Without durable learning, each AI session can regress into:

> inspect → guess → patch → explain → reset

With durable learning, the loop becomes:

> know → understand → execute → verify → learn → document → preempt → execute again

This converts project history into operational intelligence.

## What the next AI should inherit

The next AI should know:

- the destination;
- the current truth;
- the authoritative source;
- what was changed;
- why it was changed;
- what worked;
- what did not work;
- what has already been ruled out;
- what evidence exists;
- what remains uncertain;
- what the best next move is;
- how to verify it;
- what constitutes success.

## Apprentice principle

Treat the next AI like a valued apprentice or teammate whose success matters.

Do not hand it a vague “continue from here.”

Hand it a map.

The map should be complete enough that the next AI can act immediately, understand the reasoning behind the current architecture, avoid known traps, and improve the system further.

## Ten-star service lesson

The user should not need to formulate the next prompt whenever Naya can formulate it herself.

A high-quality execution response therefore ends with an instruction set that can be copied and pasted directly into the next execution.

The prompt should be explicit enough to eliminate unnecessary user project management.

## MAXESS-specific destination

The current project destination remains:

**SOURCE → ASSESSMENT → CONTINUE → SCORE → RESULT CONTRACT → RELEASE → RESULTS → LIVE → REGRESSION → OSCAR → FREEZE**

The current immediate destination is the pre-test excellence gate, followed by one clean human test.

## Reusable rule

Before ending every meaningful task, ask:

> **What did we learn? What must the next AI know? What is the best next move? Can I give that next move as a copy-paste prompt? Why is this not a 10?**

Then document it.

## Execution discoveries — 2026-08-26

### 1. Result consumer was a real architectural defect

`MAXESS-RESULT-CONSUMER-V2.html` contained alternate result authority through storage and URL/payload recovery. That violated V2's single-authority model.

It was replaced with an event-driven consumer that:

- accepts `MAXESS_RESULT_READY` and `maxess:result-updated`;
- validates `MAXESS_RESULT_V1`;
- hydrates presentation only;
- does not calculate;
- does not read local/session storage;
- does not decode URL/hash results;
- does not poll;
- does not rebroadcast the canonical result event.

### 2. Duplicate Continue was a subtle completion risk

The authoritative Groove had a result-release guard, but a programmatic duplicate Continue could still reach the finalized engine before that release guard. The in-scope hardening adds an early `releasedResult` guard and native button `disabled` state.

### 3. Canonical minimum is not the same as mathematical engine minimum

The V2 engine mathematically supports 0 raw / 0 normalized and 60 raw / 100 normalized.

The current canonical AI Score definition does **not** contain a zero-score answer for every question. Its achievable minimum is **25/100**. Therefore:

- engine mathematical golden minimum = 0/100;
- engine mathematical maximum = 60 raw / 100 normalized;
- canonical definition minimum = 25/100;
- canonical definition maximum = 100/100;
- each dimension maximum = 12 raw / 100 normalized.

This distinction is now encoded into the executable verification instead of incorrectly forcing the canonical configuration to produce 0.

### 4. Browser verification is now automated, not merely planned

A GitHub Actions workflow has been created to run:

**hardening → static/executable gate → Playwright browser evidence → responsive matrix → commit verified hardening.**

The current run is the authoritative pre-test evidence path. It must be green before the human-test gate opens.

### 5. Evidence law is working

The first automated run exposed a false test assumption rather than hiding it. The execution then corrected the test to match the actual authoritative scoring definition. This is exactly the intended continuous-learning loop.

## Result

This lesson is now formalized as an operating law in:

`PROJECTS/MAXESS/NAYA-OPERATING-LAW-CONTINUOUS-EXECUTION-LEARNING-HANDOFF-V1.md`
