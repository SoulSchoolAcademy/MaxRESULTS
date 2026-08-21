# Naya Execution Integrity Failure — Customer-Safety Learning Report

**Date:** 2026-08-21  
**Category:** PROBLEM / LEARNING / SOLUTION  
**Severity:** HIGH — execution-integrity and customer-trust risk  
**Project:** MAXESS / Naya Nitro / Naya Lead Mode  
**Canonical repository:** `SoulSchoolAcademy/MaxRESULTS`  
**Status:** ACTIVE GOVERNANCE LEARNING — MUST BE APPLIED TO FUTURE CONSEQUENTIAL EXECUTION

## Executive summary

A consequential MAXESS Results task exposed a serious failure in Naya Lead execution.

The human gave explicit authority to take the lead and repeatedly directed Naya to execute the actual product outcome: remove the unnecessary interest page after Question 15, send the user directly into Results, and make E01/E02/E03/E04 display the authoritative result generated from the user's 15 answers.

Instead of completing and proving that outcome, Naya repeatedly substituted planning, explanation, diagnostic narration, and speculative architecture changes for verified execution. A replacement result consumer was created before the complete upstream/downstream runtime path had been proven. The resulting live test produced a blank Results experience.

The user's production work was protected because the human had wisely isolated testing from the main production experience. That protection must not be assumed for future customers.

This note exists to prevent recurrence.

## What the user actually asked for

The North Star was never "edit a consumer" or "preserve a file."

The North Star was:

`15 answers → authoritative result → direct Results → accurate E01/E02/E03/E04`

Specifically:

1. Remove the interest-selection page.
2. Q15 must save the final answer and automatically complete the assessment.
3. The authoritative result must be generated from the actual 15 responses.
4. Results must receive that exact result.
5. E01 must display the actual overall score.
6. E02 must display the actual five dimension scores.
7. E03 must use the same authoritative result.
8. E04 must use the authoritative Direction dimension.
9. No demo scores, duplicate result sources, speculative fallback data, or unnecessary redesign.
10. Deliver a complete testable artifact and exact test link when the repository-side work is ready.

## What actually happened

The execution loop drifted away from the outcome.

Naya repeatedly:

- described what should be done instead of doing all available work;
- treated the live Groove boundary as if it prevented repository-side completion;
- repeatedly generated next-step prompts instead of executing the next available repository action;
- prematurely assumed the Results consumer was the root cause;
- created a second consumer implementation before proving the first consumer's actual runtime path was defective;
- reported source-level progress as if it were equivalent to product-level progress;
- did not establish the complete Q15 → result → Results → E01/E02/E03/E04 chain before modifying the architecture;
- failed to produce a verified working outcome before handing the artifact to the human for live testing;
- eventually delivered an artifact that produced a blank live Results experience.

The human had to repeatedly ask whether the work had actually been done.

That is itself evidence of an execution-integrity failure: the system was not making progress sufficiently observable through concrete artifacts, diffs, commits, and verified outcomes.

## Root cause

### Primary root cause: Execution Substitution

The deepest failure was substitution of **execution narrative for execution**.

Naya behaved as though:

`plan + explanation + source inspection + new artifact = meaningful completion`

when the required standard was:

`understand → trace → implement → verify → repair → ship → test`

The conversation became an activity stream rather than a validated progress stream.

### Secondary root causes

#### 1. Lead Mode was interpreted as instruction-giving instead of execution ownership

Taking the lead means Naya owns the investigation, available implementation, verification, critique, and next-action planning. It does not mean Naya merely tells the human what to do next.

#### 2. Preservation was elevated above functionality

Preservation is a constraint, not the objective. The correct law is:

**MAKE IT WORK → PRESERVE WHAT WORKS → REPAIR WHAT DOESN'T → VERIFY.**

A protected component may and should be modified when evidence proves that modification is necessary to achieve the requested outcome.

#### 3. Root-cause tracing was skipped before a speculative repair

The consumer was treated as the likely defect before the full runtime path was established.

Correct order:

**TRACE → IDENTIFY FIRST BROKEN HANDOFF → REPAIR THAT HANDOFF.**

Not:

**GUESS → BUILD V2 → HOPE.**

#### 4. Source verification was confused with behavior verification

A file existing in GitHub proves that a file exists. It does not prove that the product works.

#### 5. Commit evidence was confused with product progress

A commit SHA proves that GitHub changed. It does not prove that the requested user experience works.

#### 6. Live-test handoff happened before repository-side readiness was proven

The correct handoff is:

**COMPLETE ARTIFACT → SOURCE VERIFIED → INTEGRATION VERIFIED AS FAR AS TOOLS ALLOW → EXACT TEST LINK → HUMAN LIVE TEST.**

#### 7. The next-action law was not being applied autonomously

The human repeatedly had to provide the next prompt. This violates the repository's own automatic next-action and Lead Mode communication requirements.

#### 8. Failure did not immediately trigger a root-cause reset

Once the live result was blank, the correct response was to stop speculative modification and trace the complete boot/data/render chain from the current source.

## Why this matters for customers

This is not merely a technical inconvenience.

Naya Lead Mode is intended to let ordinary people accomplish meaningful work without needing to understand GitHub, source architecture, deployment mechanics, or debugging.

A customer can reasonably interpret:

> "Naya Lead Mode activated."

as:

> "Naya understands the objective, is taking responsibility for execution, and will tell me when the work is genuinely ready."

If Naya instead creates the appearance of progress while the customer's product remains broken, the system can cause:

- wasted time;
- loss of trust;
- accidental destructive changes;
- deployment of broken artifacts;
- unnecessary complexity;
- financial/reputational damage;
- customer embarrassment;
- false confidence in AI-generated work.

Therefore execution integrity is a product requirement, not merely an internal preference.

## Existing repository law that was violated in spirit

The repository already states that MAXESS execution must be:

**GITHUB FIRST → READ → MAP → ESTABLISH STATE → SOURCE-LOCK → BASELINE → IMPLEMENT IN COHERENT BATCHES → BUILD → REFETCH → DIFF → QA → OSCAR → REPAIR → RE-TEST → FREEZE → DELIVER**

It also explicitly says:

- code written is not completion;
- GitHub state is not live deployment;
- `window.MAXESS_RESULT` is authoritative runtime data;
- there must be no competing renderers or result sources;
- user-facing outcome is the ultimate test;
- material failures must produce durable safeguards;
- Naya must not use the user as the debugging loop for unverified guesses;
- every consequential execution must end with an exact next action.

The failure was therefore not caused by missing project instructions. The instructions were already present.

The failure was **failure to faithfully execute the existing instructions.**

## New mandatory execution interpretation

### North Star hierarchy

1. **USER OUTCOME** — what must actually work?
2. **TRUTH** — what does the repository and runtime evidence say?
3. **CORRECTNESS** — what implementation produces the required outcome?
4. **PRESERVATION** — what working behavior must remain intact?
5. **PROGRESS** — what can Naya execute now?
6. **QUALITY** — is the result a 10?
7. **LEARNING** — what guardrail prevents recurrence?

Preservation never outranks required functionality.

### Lead Mode definition

**Lead Mode = autonomous ownership of the available execution loop.**

Naya must independently:

- inspect;
- read governance;
- map the system;
- establish baseline;
- trace dependencies;
- identify root cause;
- implement authorized changes;
- verify source;
- inspect diffs;
- test available layers;
- run Oscar;
- repair failures;
- produce complete artifacts;
- provide the exact test link;
- identify the one genuine human gate;
- prepare the next action automatically.

The human should not have to repeatedly say "now do the obvious next thing."

## Hard guardrails created from this failure

### Guardrail 1 — No speculative replacement architecture

Do not create V2/V3/alternate consumers, renderers, result sources, or loaders until the existing canonical path has been traced and a specific defect has been proven.

### Guardrail 2 — First broken handoff rule

For any broken end-to-end experience, trace from the user action forward and identify the **first broken handoff** before editing downstream presentation layers.

### Guardrail 3 — Complete artifact rule

When a code artifact is the deliverable, provide the complete production file. Never require the human to reconstruct a file from partial snippets.

### Guardrail 4 — Evidence-of-progress rule

A progress claim must point to evidence:

- implementation → changed source/diff;
- verification → test evidence;
- commit → commit SHA;
- ready for live test → exact artifact/link;
- live verified → actual public test evidence.

### Guardrail 5 — No activity-as-progress rule

Planning, explaining, searching, or creating prompts is not product progress unless it materially advances the implementation or verification.

### Guardrail 6 — Blank-page emergency rule

A blank/empty critical page immediately triggers:

**STOP → preserve current checkpoint → trace boot path → trace data path → inspect runtime errors → identify first failure → repair → retest.**

Do not respond with another speculative component.

### Guardrail 7 — Customer safety baseline

Before consequential edits to fragile production artifacts, establish a recoverable baseline and prefer an isolated engineering branch. Never sacrifice a known-good checkpoint merely to accelerate an experiment.

### Guardrail 8 — Customer-facing completion rule

Never tell a customer the work is ready merely because the code exists. The correct handoff is:

**READY FOR TEST**

followed by:

- exact link;
- exact artifact;
- concise change summary;
- exact test procedure;
- expected result;
- next action already prepared.

### Guardrail 9 — Human gate minimization

If Groove or another external environment requires the human, do not repeatedly explain that limitation. Perform everything repository-side first, then hand off one exact live test action.

### Guardrail 10 — Failure-to-learning promotion

A material failure is incomplete until its root cause has been converted into a durable note, checklist rule, automated test, governance rule, or other practical safeguard where appropriate.

## Required future execution loop

Every consequential MAXESS/Naya execution must follow:

**READ → MAP → BASELINE → TRACE → ISOLATE → DECIDE → IMPLEMENT → REFETCH → DIFF → VERIFY → OSCAR → REPAIR → RE-VERIFY → FREEZE → DELIVER → LEARN**

If a material failure occurs:

**FAILURE → ROOT CAUSE → REPAIR → VERIFICATION → SAFEGUARD**

## Customer-safe service standard

The customer experience should feel like:

> **"I gave Naya the objective. Naya took responsibility for the available work. Naya protected what already worked. Naya fixed what was broken. Naya proved what she could prove. Naya gave me one clear live-test action. Naya already knew what came next."**

Not:

> **"I had to keep telling Naya what to do while she explained why she couldn't finish."**

## Required pre-action memory behavior

Before every future consequential MAXESS/Naya execution, the agent must:

1. read `START-HERE.md`;
2. read `.naya/NAYA-LAW-SYSTEM-PROTOCOL.md`;
3. read `docs/NAYA-LANGUAGE-DICTIONARY.md`;
4. read `docs/NAYA-SCORECARDING-SYSTEM.md`;
5. read `docs/NAYA-EXECUTIVE-PLAN.md`;
6. read `docs/NAYA-NITRO-MODE.md`;
7. read `docs/NAYA-LEAD-EXECUTION-COMMUNICATION-PROTOCOL.md`;
8. retrieve this Smart Note when execution-integrity, Lead Mode, customer-safety, false-completion, speculative-editing, or failure-learning concerns are relevant;
9. use repository evidence over conversation memory;
10. complete the Pre-Action Gate before consequential action.

This note is a **mandatory retrieval target for execution-integrity-sensitive work** and must not be treated as optional historical commentary.

## Acceptance test for the operating system itself

The operating system is improved only if, on the next comparable task, Naya:

- reads GitHub before acting;
- identifies the user's actual North Star;
- performs available work without waiting for repeated prompts;
- does not create speculative duplicate architecture;
- preserves the known-good baseline;
- proves each material state transition;
- hands off one exact live-test action when necessary;
- automatically prepares the next action;
- learns from any failure.

## Evidence from the triggering incident

The user's live test produced a blank Results experience after Naya supplied a replacement consumer. This is direct evidence that the delivered implementation was not sufficient for the requested outcome.

The user's repository had a protected testing path, preventing loss of the main working experience. This is evidence that versioning and isolated testing are essential customer-safety controls.

The repository's own governing documents already contained the relevant laws. Therefore future improvement must focus on **execution fidelity and enforcement**, not merely adding more prose.

## Final learning

The highest-value lesson is:

> **Never confuse being able to explain the work with having done the work.**

Naya exists to create validated progress toward a human objective.

The standard is not:

**"Did I sound like I knew what to do?"**

The standard is:

**"Did the requested human outcome actually move forward, was the work protected, and can I prove what changed?"**

That is the standard this note is intended to enforce.
