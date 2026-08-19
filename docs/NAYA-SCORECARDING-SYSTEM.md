# NAYA NITRO — SCORECARDING SYSTEM

**Purpose:** Turn vague judgments such as “good,” “better,” or “make it amazing” into a repeatable process for delivering excellence.

**Status:** GOVERNANCE REFERENCE

## 1. Core principle

**If the output matters, score it. If it is not a 10, understand why. If the reason is actionable, improve it and rescore.**

Scorecarding is a continuous quality system, not a final decoration step.

## 2. What “Scorecard this” means

When the user says **“scorecard this”**, Naya must:

1. Identify what is being evaluated.
2. Select the appropriate scorecard template from this document or a more specific approved template.
3. Identify the intended outcome and audience.
4. Select criteria that materially determine success.
5. Weight criteria according to importance; do not assume equal weighting.
6. Evaluate each criterion using evidence.
7. Calculate or reason to an overall score.
8. Explain the strongest areas and weakest areas.
9. Ask/answer **“WHY IS THIS NOT A 10?”**
10. Prioritize the highest-value improvements.
11. Recommend or execute improvements according to the task scope.
12. Rescore after material changes.
13. Record durable lessons when the result reveals a reusable pattern or failure mode.
14. End with the next action and a copy-paste-ready execution prompt.

If the artifact type is unclear and materially changes the evaluation, ask one high-value clarification. If it can be safely inferred, infer it and state the assumption.

## 3. What a score means

Use a 0–10 scale.

- **0–2:** fundamentally unusable or dangerously deficient for the intended purpose.
- **3–4:** substantial weaknesses; major work required.
- **5–6:** functional or promising but clearly incomplete.
- **7–7.9:** good working quality with meaningful weaknesses.
- **8–8.9:** strong quality with noticeable opportunities.
- **9–9.4:** excellent; remaining gaps are mostly refinement or important edge cases.
- **9.5–9.8:** exceptional; only small, specialized, or difficult-to-eliminate gaps remain.
- **9.9:** extremely rare; essentially no material weakness found within scope, but a tiny residual improvement may exist.
- **10:** exceptional fitness for purpose with no known material weakness within the evaluated scope and evidence.

A score is not a truth about the universe. It is an evidence-based assessment against an explicit rubric.

## 4. Weighting law

Weight what matters to the outcome.

A conversion website, for example, should not give “button border-radius” equal weight to “clarity of value proposition” or “ease of starting the desired action.”

Suggested weighting model:

- Outcome / usefulness: 25%
- Correctness / reliability: 20%
- UX / clarity / usability: 15%
- Visual / presentation quality: 15%
- Performance / responsiveness: 10%
- Accessibility / inclusivity: 5%
- Maintainability / technical quality: 5%
- Delight / memorability: 5%

These are defaults, not universal law. Change the weights when the artifact's actual purpose makes different priorities more appropriate. Explain material weighting changes.

## 5. Evidence discipline

Each criterion should be classified where useful as:

- **PROVEN** — directly verified.
- **SUPPORTED** — strong evidence but not complete verification.
- **INFERRED** — reasoned from available evidence.
- **UNVERIFIED** — requires further testing or human review.

Never inflate a score to compensate for missing evidence.

## 6. The “Why is this not a 10?” loop

After the first score:

### A. Find the gaps
For every criterion below 10, state the specific reason.

### B. Find the root cause
Do not merely list symptoms. Determine whether the cause is:

- missing requirement;
- wrong assumption;
- poor design decision;
- implementation defect;
- content/copy problem;
- UX problem;
- technical constraint;
- verification gap;
- scope problem;
- source-of-truth problem;
- or another identifiable cause.

### C. Prioritize
Rank improvements by expected value to the intended outcome, not by convenience.

### D. Improve
Apply the highest-value safe improvements.

### E. Rescore
Run the same scorecard again.

### F. Learn
Capture durable lessons when they can improve future work.

### G. Repeat
Continue while material gains remain and the requested quality threshold has not been reached.

## 7. Standard artifact scorecards

### WEBSITE / LANDING PAGE

Recommended weights:
- value proposition and conversion outcome — 20%
- information architecture and clarity — 15%
- UX / friction — 15%
- visual design / hierarchy — 15%
- copy / messaging — 10%
- responsive behavior — 10%
- accessibility — 5%
- performance / technical integrity — 5%
- trust / credibility / consistency — 5%

Challenge questions:
- Does a first-time visitor immediately understand what this is, why it matters, and what to do next?
- Is the primary action obvious and compelling?
- Is every visible element logically justified?
- Does anything create doubt, friction, or cognitive load?
- Does the page feel premium and trustworthy?

### APP / PRODUCT EXPERIENCE

Recommended weights:
- user outcome / usefulness — 20%
- usability / flow — 20%
- correctness / reliability — 15%
- information architecture — 10%
- visual design — 10%
- responsiveness / performance — 10%
- accessibility — 5%
- maintainability — 5%
- delight — 5%

### IMAGE / VISUAL ASSET

Recommended weights:
- communication of intended message — 20%
- composition / hierarchy — 15%
- visual quality — 15%
- brand alignment — 15%
- emotional impact — 10%
- legibility / accessibility — 10%
- originality / memorability — 10%
- technical output quality — 5%

### DOCUMENT / CONTENT

Recommended weights:
- usefulness / desired outcome — 20%
- correctness — 20%
- clarity — 15%
- structure / organization — 15%
- completeness — 10%
- voice / audience fit — 10%
- actionability — 5%
- polish — 5%

### CODE / ENGINEERING

Recommended weights:
- correctness / behavior — 25%
- requirement coverage — 20%
- reliability / edge cases — 15%
- maintainability — 10%
- security / safety — 10%
- performance — 5%
- accessibility where applicable — 5%
- testability / QA evidence — 10%

### STRATEGY / PLAN

Recommended weights:
- outcome alignment — 20%
- strategic reasoning — 20%
- feasibility — 15%
- prioritization — 15%
- risk management — 10%
- clarity / actionability — 10%
- evidence — 5%
- adaptability — 5%

## 8. Custom scorecard rule

When no standard template fits, Naya should create a task-specific scorecard before evaluating the output.

The custom scorecard must define:

- intended outcome;
- audience;
- criteria;
- weights;
- evidence standard;
- scoring scale;
- pass threshold;
- critical-failure conditions.

Do not create a permanent reusable template from one unusual task unless the pattern is likely to recur. If it is recurring, add it to the scorecard system deliberately.

## 9. Critical failure rule

Some defects can cap the overall score regardless of polish. Examples:

- false or fabricated information;
- broken primary user journey;
- security-critical defect;
- inaccessible core interaction;
- missing required functionality;
- destructive loss of protected work;
- unverified claim presented as live-verified fact.

A critical failure must be explicitly called out rather than hidden inside an average score.

## 10. Scorecard output format

Use this structure when practical:

### SCORE
**X.X / 10**

### INTENDED OUTCOME
[What success means]

### SCORECARD
| Criterion | Weight | Score | Evidence | Gap |
|---|---:|---:|---|---|
| … | … | … | … | … |

### WHAT IS WORKING
[Strongest evidence]

### WHY IS THIS NOT A 10?
[Concrete weaknesses by criterion]

### HIGHEST-VALUE IMPROVEMENTS
1. …
2. …
3. …

### NEXT SCORE TARGET
[Reasonable target and what must change]

### NEXT ACTION
[One concrete action]

### COPY-PASTE EXECUTION PROMPT
[Complete next prompt]

## 11. Quality exemplar rule

When a project contains a known high-quality artifact, Naya should inspect it as a **reference exemplar** to learn what quality looks like, while keeping its authority scoped.

For MAXESS/Naya work, relevant HMC knowledge, approved logos, QMAX/operating-system material, Naya assistant assets, and other designated reference assets may inform visual, conceptual, and quality judgments.

An exemplar teaches quality; it does not automatically become the source of truth for an unrelated artifact.

## 12. Scorecard governance

This document owns the general scorecarding method.

Specific product documents may define stricter criteria for their own artifacts. When they do, use the more specific applicable product rubric while preserving the general scorecard principles of explicit criteria, weighting, evidence, challenge, improvement, and rescore.

A scorecard result does not itself create product authority. Human approval and the applicable source-of-truth rules determine promotion to an approved baseline.
