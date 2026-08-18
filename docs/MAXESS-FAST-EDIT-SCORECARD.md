# MAXESS FAST EDIT SCORECARD

## North Star

Make common MAXESS edits finish in minutes:

`REQUEST → LOCATE → PATCH → VALIDATE → LOCAL QA → COMMIT → REPORT`

## Proof standard

Five consecutive real micro-edits must each produce:

- exact owner match;
- non-zero source delta;
- target-language validation pass;
- local QA pass or explicitly recorded limitation;
- immediate Git checkpoint;
- no unrelated whole-page rewrite.

## Current proof runs

| # | Request | Owner | Source delta | Syntax | Local QA | Commit | Status |
|---:|---|---|---|---|---|---|---|
| 1 | Make the Orb 15% smaller | V21 Score Orb | Pending Codespace run | Pending | Pending | Pending | READY |
| 2 | Move the Naya section up | V21 Naya Arrival | Pending Codespace run | Pending | Pending | Pending | READY |
| 3 | Make primary button electric purple | V21 Listen button | Pending Codespace run | Pending | Pending | Pending | READY |
| 4 | Increase score size 10% | V21 Score typography | Pending Codespace run | Pending | Pending | Pending | READY |
| 5 | Add 16px headline spacing | V21 Naya subtext | Pending Codespace run | Pending | Pending | Pending | READY |

## Important

Do not mark an edit successful based on tool output alone. The five-edit proof must be executed in the target Codespace against the actual working tree.
