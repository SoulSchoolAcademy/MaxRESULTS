# 🔱 NEXT EXECUTION — MAXESS V2 BROWSER GATE 03 POST-FIX

NAYA MASTER ON.
NAYA LAW ON.
NAYA LEAD MODE ON.
CONTINUOUS EXECUTION + LEARNING LAW ON.
TEN-STAR SERVICE MODE ON.

## OBJECTIVE
Restore MAXESS from current `main` and complete the machine proof required before one clean human test.

## SOURCE OF TRUTH
Start with current GitHub `main`.
Do not start from memory.
Do not ask Shawn to test.

## KNOWN FIX
The authoritative E00 Groove selector helper previously prefixed `#` while callers already supplied `#`, producing selectors such as `##mx-cont` and preventing E00 runtime publication.

The source fix is:

```js
const $=id=>ROOT.querySelector(id.charAt(0)==='#'?id:'#'+id);
```

No new scorer, state authority, result authority, bridge, or replacement Continue path was introduced.

## FIRST ACTION
Locate the GitHub Actions `MAXESS V2 Pre-Test Excellence Gate` execution triggered by the source-fix push for commit:
`d9e1f0ba1d8e6cd97acd8df6d1807935cd6a1f0a`

Inspect:
- completed conclusion;
- browser job;
- browser evidence artifact;
- `maxess-browser-diagnostics.json`;
- screenshots;
- Playwright traces;
- exact browser assertions.

## IF BROWSER IS GREEN
Verify executed evidence for:

- Q1 renders;
- five answers render;
- Continue disabled before selection;
- Continue enables after selection;
- Q1→Q15 exactly once;
- final answer commits exactly once;
- result contract is `MAXESS_RESULT_V1`;
- result is frozen;
- exactly one `MAXESS_RESULT_READY`;
- exactly one `maxess:result-updated`;
- `completionCount = 1`;
- duplicate Continue cannot create another completion;
- E01 receives the identical result;
- no downstream rescoring;
- no console errors;
- no failed requests;
- all required widths pass: 320, 360, 375, 390, 414, 480, 600, 768, 900, 1024, 1280.

Then inspect the hardened Groove source and E01 handoff.

## IF BROWSER IS NOT GREEN
Use the uploaded evidence to classify the failure:

PRODUCT / TEST HARNESS / ENVIRONMENT / INTEGRATION / EVIDENCE

Fix the correct layer only, then rerun the affected verification.

Do not create another scorer.
Do not create another state authority.
Do not create another result authority.
Do not create another bridge.
Do not rewrite Continue without new evidence.
Preserve premium visual work.

## RELEASE CONDITION
Do not declare Browser GREEN without executed evidence.
Do not request the human test until Browser is GREEN.
The goal is not “browser passes.”
The goal is ONE CLEAN HUMAN TEST.

## NAYA POWER KNOWLEDGE
The canonical knowledge trifecta is now official:

I. Naya Power — A Letter From the Founder
II. Naya Power — The Next Way We Operate Intelligence
III. Naya Power — The Intelligence Operating Model

Use them as WHY → WHAT → HOW references for Naya Power questions.

## FINALIZATION
After meaningful work:
1. update Smart Note;
2. update Naya Apprentice Handoff;
3. update human receipt;
4. update current project truth;
5. answer “WHY IS THIS NOT A 10?”;
6. create the next copy-paste-ready execution prompt.
