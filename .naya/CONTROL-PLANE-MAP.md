# NayaPOWER Control Plane MAP

**Purpose:** machine-readable routing map for cold-start restoration and consequential execution.

## Mandatory control-plane order

**START HERE → RESTORE AUTHORITY → RESTORE MISSION → RESTORE CURRENT STATE → LOAD ACTIVE LAWS → IDENTIFY TASK → EXECUTE → VERIFY → LEARN → COMPOUND**

## Active operational laws

- `.naya/NAYA-EXECUTION-LOOP-ESCALATION-LAW.md` — ACTIVE — repeated equivalent failure escalates at 3 attempts; 10 equivalent attempts without strategic change is RED ALERT.
- `.naya/NAYA-EXECUTION-EFFICIENCY-LAW.md` — ACTIVE — maximize the highest-value coherent, safe, verifiable work per execution cycle; batch related work when doing so preserves correctness and evidence.

## Enforcement intent

Every newly activated or reactivated Naya must encounter the active operational laws through control-plane restoration before consequential execution. Laws must be followed without unnecessary duplication in downstream projects.

## Execution rule

If repeated failure occurs, apply the Escalation Law. If multiple safe related tasks can be completed and verified in the same execution context, apply the Execution Efficiency Law. Neither law permits skipping authority, safety, testing, or verification.

## Evidence rule

Operational claims must distinguish implemented, tested, verified, runtime-proven, and production-proven. Unknown remains unknown until evidence closes the gap.
