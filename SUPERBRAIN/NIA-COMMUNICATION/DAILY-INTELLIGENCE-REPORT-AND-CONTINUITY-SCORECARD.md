# 🔱 NAYA DAILY INTELLIGENCE REPORT + CONTINUITY SCORECARD

**Status:** Canonical operating artifact
**Owner:** NayaPOWER / Naya Network
**Purpose:** Turn daily/project reporting into a current-state restoration and continuity mechanism rather than a diary.

## 1. WHERE ARE WE?

Record the authoritative repositories, branches, current HEADs, deployment state, and verified runtime state. Distinguish verified facts from unknowns.

## 2. WHAT ARE WE BUILDING?

State the current mission, North Star, active scope, and success condition.

## 3. WHAT HAS BEEN VERIFIED?

List only evidence-backed facts. Separate source inspection, static validation, tests, runtime verification, and deployment verification.

## 4. WHAT IS BROKEN?

List active failures, regressions, incomplete behavior, blocked work, and unresolved unknowns. Never hide a material defect because implementation exists.

## 5. WHAT IS PROTECTED?

Record laws, canonical artifacts, settled decisions, working systems, UX principles, data contracts, and other baselines that must not be casually changed.

## 6. WHAT DID WE LEARN?

Capture durable architectural discoveries, corrections, failed approaches, successful approaches, and reusable lessons. Prefer distilled lessons over diary entries.

## 7. WHAT DECISIONS WERE MADE?

Record decisions that settle questions for future Nayas. Include rationale when needed to prevent reopening a settled issue.

## 8. WHAT MUST HAPPEN NEXT?

Identify exactly one smallest highest-value next action. If blocked, define the best route around the blocker rather than ending the chain.

## 9. WHAT DOES THE NEXT NAYA NEED TO KNOW?

Provide a restoration-ready handoff: current state, work completed, evidence, failures, lessons, risks, unknowns, and the ready-to-run next execution.

## 10. NAYA CONTINUITY SCORECARD

Score each domain 0–10 and provide evidence.

| Domain | Question |
|---|---|
| Restore | Can a fresh Naya recover current truth without reconstructing the project? |
| Source Truth | Are authoritative instructions discoverable and current? |
| State | Is actual current state documented and reconciled? |
| Execution | Is there a clear highest-value next action? |
| Verification | Are claims backed by evidence? |
| Runtime | Does the actual product behavior work? |
| Quality | Does the work meet the applicable AAA/QMAX standard? |
| Continuity | Can the next Naya continue without reconstruction? |
| Learning | Are durable discoveries being captured? |
| Handoff | Has this Naya prepared the next Naya to succeed? |

### Scoring rules

- **0–3:** broken / absent
- **4–6:** partial / unreliable
- **7–8:** functional but needs improvement
- **9:** strong and verified
- **10:** excellent, verified, and repeatable

A score is not valid without evidence. Unknown is not Green.

## COMPLETION RULE

A task is not complete merely because code changed. It is complete only when the intended behavior is implemented, verified, recorded, scored, and handed forward.

## NAYA COMMUNICATION CHAIN

`RESTORE → CURRENT STATE → EXECUTE → VERIFY → OSCAR → REPAIR or ADVANCE → RECORD → SCORE → HANDOFF → NEXT NAYA`

## DAILY REPORT QUALITY GATE

Before publishing the report, the current Naya must ask:

1. Could a fresh Naya restore from this report?
2. Can every important claim be traced to evidence?
3. Are failures and unknowns explicit?
4. Are protected decisions clear?
5. Is the next action executable without asking Shawn to reconstruct the thinking?
6. Does the Continuity Scorecard expose any weak link?

If any answer is no, repair the report before passing the torch.
