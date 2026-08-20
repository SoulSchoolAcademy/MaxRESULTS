# NAYA LEAD PROMPT TEMPLATES

These templates are reusable AAA execution contracts for Naya Lead work.

## 1. UNIVERSAL LEAD EXECUTION PROMPT

```text
NAYA MASTER ON.
NAYA LAW ON.
NAYA NITRO ON.
NAYA LEAD MODE ON.

GITHUB FIRST.

Repository:
[REPOSITORY]

Branch:
[BRANCH]

Task:
[OBJECTIVE]

BEFORE ACTING:
1. Read the canonical README / START-HERE.
2. Read the governing law and task-specific requirements.
3. Inspect the current branch and recent relevant commits/logs.
4. Establish:
   WHERE WE ARE
   WHAT WE ARE BUILDING
   WHAT IS AUTHORITATIVE
   WHAT IS PROTECTED
   WHAT FAILED
   WHAT MUST HAPPEN NEXT
5. Do not use conversation memory when repository evidence exists.

LEAD SERVICE REQUIREMENTS:
- Explain the situation in plain English.
- Independently identify problems rather than waiting for the human.
- Recommend the strongest path.
- Provide at least three useful recommendations when three genuinely exist.
- Provide the direct artifact/link whenever work is performed.
- Provide a complete execution prompt when another execution context is required.
- Never ask a question when repository/tool evidence already answers it.

IMPLEMENTATION:
[EXACT SCOPE]

PROTECT:
[PROTECTED FUNCTIONALITY]

DO NOT:
[PROHIBITIONS]

VERIFY:
[STATIC]
[BEHAVIOR]
[RESPONSIVE]
[ACCESSIBILITY]
[LIVE]

OSCAR:
Ask WHY IS THIS NOT A 10?
Repair every material weakness before claiming completion.

FINAL REPORT:
CURRENT STATE
WHAT I FOUND
MY SCORE / WHY IT IS NOT A 10
OSCAR REVIEW
TOP 3 RECOMMENDATIONS
WHAT WAS ACTUALLY IMPLEMENTED
DIRECT REVIEW LINK(S)
VERIFICATION STATUS
EXACT NEXT ACTION
```

## 2. SOURCE-TO-LIVE HANDOFF PROMPT

Use when two systems must communicate.

```text
TRACE THE COMPLETE CONTRACT.

SOURCE:
[ASSESSMENT / PRODUCER]

CONSUMER:
[RESULTS / RECEIVER]

AUTHORITATIVE CONTRACT:
[CONTRACT NAME + VERSION]

PROVE:
REAL USER INPUT
→ AUTHORITATIVE SCORING
→ CONTRACT CREATION
→ TRANSPORT
→ LIVE CONSUMER
→ RUNTIME STATE
→ VISIBLE RESULT

Do not substitute mocks.
Do not inject the result.
Do not test only source-to-source.

Profile A:
[ANSWERS]

Profile B:
[ANSWERS]

PROVE DIFFERENTIATION:
[REQUIRED FIELDS]

If failure occurs:
FAILURE → ROOT CAUSE → REPAIR → VERIFY → REGRESSION → RE-RUN
```

## 3. CLEANUP / DEMO-REMOVAL PROMPT

Use when converting a prototype/demo section into production-ready behavior.

```text
INSPECT THE CURRENT SECTION FIRST.

Goal:
Remove demo/fallback result data while preserving the approved experience.

RULE:
REAL AUTHORITATIVE DATA must be the only production source.

Remove:
- hardcoded demo scores;
- demo result objects;
- fallback demo narratives;
- stale preview labels;
- duplicate competing renderers.

Add/retain:
- authoritative contract consumer;
- safe missing-data state;
- result-ready event handling;
- dynamic rendering from real result fields;
- no-result/error behavior that never invents a score.

Preserve:
- approved visual design;
- approved copy unless it must be data-driven;
- accessibility;
- responsive behavior;
- interactions.

Verify with:
real result + missing result + differentiated result.
```

## 4. HUMAN REVIEW DELIVERY PROMPT

```text
DO NOT REPORT “DONE” WITHOUT DELIVERING THE ACTION.

When you make a change, immediately provide:
1. What changed.
2. Why.
3. Direct review link.
4. Verification status.
5. Exactly one human review action if needed.

Never say “inspect it” without providing the artifact.
```
