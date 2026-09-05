# V7 Operating Application Contract

## Purpose
V7 is an intelligent application, not a webpage. Its completion standard is not visual polish alone. Every meaningful feature must execute a real action, create truthful state, persist the result where required, expose evidence, and provide a recovery path when execution cannot complete.

## Core laws
- **LAW 01 — Smart Note + Receipt:** capture what matters, represent it correctly, verify it, and prove it.
- **LAW 02 — Continuous Action + No Dead End:** every actionable interaction must either complete or surface the exact blocked stage and recovery action.
- **LAW 03 — Continuous Context + Always-in-Tune:** intelligence must preserve continuity across events, views, sessions, and reports.
- **LAW 04 — AAA Excellence / 10-Star Human Service:** the system should actively help the human succeed rather than merely report failure.
- **NO FABRICATION. NO SILENT FAILURE. NO SILENT EXIT.**

## Smart Note invariant
A GitHub commit, issue, engineering document, receipt, or assistant acknowledgement is **not** a Smart Note.

A real Smart Note transaction is complete only when the system creates and persists this chain:

**Human Note → Naya Note → Machine Note → Intelligent Feed → Intelligent Block → Intelligent Hub state → Evidence / receipt**

The chain must be authenticated, idempotent, observable, and persistent.

### Required behavior
When Naya determines that an interaction qualifies as a Smart Note, the application must invoke the real Smart Note pipeline. It may not merely acknowledge the request or create a development artifact.

If any stage cannot execute, the system must explicitly report:
1. the exact stage that is blocked,
2. why it is blocked,
3. what state was safely preserved,
4. the concrete recovery action.

### Current backend gate
The V7 Supabase backend now contains the executable transaction boundary for this chain:
- `public.v7_smart_note_transactions`
- `public.v7_create_smart_note(...)`
- Edge Function `v7-smart-note`

Security requirements are enforced at the database boundary: authenticated execution only, `p_user_id = auth.uid()`, RLS enabled, idempotency protection, and rejection of incomplete payloads.

**Important:** backend existence does not by itself mean the Hub release has passed. The frontend must invoke the authenticated endpoint, render the returned transaction, and pass the end-to-end runtime test.

## Four perspectives
Every Intelligent Block exposes:
1. **Human** — what the human actually experienced, said, noticed, decided, or wanted remembered.
2. **Naya** — Naya's interpretation and synthesis.
3. **Machine** — structured, machine-readable representation.
4. **Intelligent Feed** — operational intelligence activity representation.

Default perspective: Human.

## Privacy
**Private by default. Shared by choice. Collective by consent. Public by decision.**

## Release gate
A V7 release is not complete until an authenticated test event is observed end-to-end after refresh/re-entry with every stage present and linked by event/receipt identity.

Required verification chain:

**SOURCE → BUILD ARTIFACT → DEPLOYMENT → EXACT PUBLIC URL → INDEPENDENT RUNTIME OBSERVATION**

Source integrity is release-critical. Never replace substantial application source with a loader, iframe, bootstrap shortcut, or truncated reconstruction.
