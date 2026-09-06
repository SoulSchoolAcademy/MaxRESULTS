# V7 Smart Note Pipeline

## Non-negotiable invariant
A development artifact is not a Smart Note.

A real Smart Note transaction is complete only when the system has created and persisted:

1. Human Note
2. Naya Note
3. Machine Note
4. Intelligent Feed event
5. Intelligent Block
6. Hub state update
7. Evidence / receipt

The transaction must be idempotent, authenticated, observable, and persistent.

## Backend implementation
The V7 Supabase project contains:

- `public.v7_smart_note_transactions`
- `public.v7_create_smart_note(...)`
- `public.v7_list_smart_notes()`
- `public.v7_preserve_smart_note_failure(...)`
- Edge Function `v7-smart-note`
- Edge Function `v7-public-config`
- Edge Function `v7-naya-note`

The `v7-smart-note` Edge Function requires a valid authenticated user, accepts the Human Note and a genuine Naya Note, deterministically constructs the Machine Note, Intelligent Feed event, Intelligent Block, Evidence receipt, and Hub state, and commits the complete transaction through the database RPC.

The `v7-naya-note` Edge Function is deliberately non-fabricating. It requires an authenticated request and a configured production Naya intelligence provider. If that provider is unavailable, it returns an explicit `NAYA_INTELLIGENCE_UNAVAILABLE` failure at the Naya stage rather than generating browser-side substitute intelligence.

## Safety invariants
- No anonymous RPC execution.
- The database function rejects a user ID that does not equal `auth.uid()`.
- RLS is enabled on the transaction table.
- Idempotency key prevents duplicate transactions.
- Incomplete pipeline payloads are rejected.
- Failed transactions must be surfaced rather than represented as successful intelligence.
- Human Notes must be preserved when the Naya stage is blocked.
- No service-role or secret key is permitted in browser code.

## Current verified backend state — 2026-09-05
The three V7 transaction RPCs exist and their permissions were independently checked:

- `v7_create_smart_note`: `anon_execute=false`, `authenticated_execute=true`
- `v7_list_smart_notes`: `anon_execute=false`, `authenticated_execute=true`
- `v7_preserve_smart_note_failure`: `anon_execute=false`, `authenticated_execute=true`

The transaction table has an RLS policy restricting authenticated reads to rows where `user_id = auth.uid()`.

The three V7 Edge Functions are ACTIVE:

- `v7-smart-note` — JWT required
- `v7-public-config` — public configuration endpoint only
- `v7-naya-note` — JWT required

## Source-preserving frontend integration
The source-preserving runtime file exists at:

`CLOUDFLARE-INTELLIGENT-HUB-V7/v7-smart-note-runtime.js`

The runtime is now embedded directly into the existing V7 `index.html`. It does not replace, reconstruct, truncate, iframe, or bootstrap a second application.

The current `index.html` blob is:

`66b387db8e1e346189be1cadec225757f7ffa48a`

A repository comparison from the known-good V7 visual baseline `5808ec7a2b517ede1d0d1bcd3c8a4debc6f0684e` reports:

- `index.html`: **136 additions / 0 deletions**
- `v7-smart-note-runtime.js`: **130 additions / 0 deletions**

This verifies that the V7 source was preserved and the integration was additive rather than destructive.

The embedded runtime now performs:

`existing composer → authenticated Supabase session → v7-naya-note → v7-smart-note → server transaction → persisted Smart Note`

It also performs server hydration and exposes an idempotency-test hook through `window.V7SmartNoteRuntime.duplicateLast()`.

## Actual transaction rendering
The embedded runtime no longer substitutes browser-only descriptions for the four perspectives when a server transaction exists.

Each persisted transaction is rendered from the same server transaction identity as:

- **HUMAN** — `human_note`
- **NAYA** — `naya_note`
- **MACHINE** — `machine_note`
- **INTELLIGENT FEED** — `intelligent_feed`
- **INTELLIGENT BLOCK** — `intelligent_block`

The card also exposes the server receipt/transaction ID and idempotency key. Failed transactions render the exact failure stage and recovery state instead of appearing successful.

## Authentication blocker
A SQL check currently shows `0` anonymous identities in `auth.identities`. That does not by itself prove whether anonymous sign-in is enabled or disabled in Auth configuration; it only proves no anonymous identities currently exist.

The browser integration must therefore verify the actual Auth configuration/runtime result rather than infer it.

The application is intentionally prepared to execute:

`supabase.auth.getSession() → supabase.auth.signInAnonymously() → authenticated JWT`

when anonymous sign-in is enabled. The actual browser session has **not yet been independently observed**.

## Naya intelligence blocker
The Naya Edge Function is intentionally refusing to fabricate output because no production `NAYA_INTELLIGENCE_URL` / `NAYA_INTELLIGENCE_API_KEY` provider configuration has been verified as available to it.

This is a real release blocker, not a cosmetic limitation.

Required recovery:

1. Configure an authorized production Naya intelligence provider server-side.
2. Keep the provider credential server-side as a Supabase secret.
3. Establish a real authenticated V7 session.
4. Execute an authenticated V7 Smart Note.
5. Observe the genuine Naya Note.
6. Continue the complete transaction and persistence tests.

## Acceptance test
A release does not pass the Smart Note gate until one authenticated test event can be observed end-to-end after refresh/re-entry, with every stage present and linked by event/receipt identity.

Required runtime sequence:

`Human → Naya → Machine → Intelligent Feed → Intelligent Block → Hub → Evidence → Persistence`

Then:

- repeat with the same idempotency key and verify no duplicate transaction;
- execute a controlled failure and verify exact failed stage, reason, preserved state, and recovery action;
- recover and re-run successfully;
- independently verify the exact public runtime.

## Operational rule
If Naya recognizes that an interaction qualifies as a Smart Note, the application must invoke this pipeline or explicitly report the blocked stage and recovery action. It must never silently stop at acknowledgement.

## Current status
Backend transaction boundary: **IMPLEMENTED**.
Security boundary: **HARDENED** — anonymous RPC execution is denied; authenticated execution is allowed; RLS is enabled; the RPC enforces `auth.uid()` ownership.
Failure-preservation boundary: **IMPLEMENTED**.
Persistent read boundary: **IMPLEMENTED**.
Source-preserving runtime integration: **ATTACHED TO EXISTING V7 SOURCE**.
Server-backed four-perspective rendering: **IMPLEMENTED IN SOURCE; RUNTIME NOT YET INDEPENDENTLY OBSERVED**.
Naya provider boundary: **IMPLEMENTED / BLOCKED UNTIL PROVIDER CONFIGURATION**.
Frontend invocation: **NOT YET VERIFIED**.
Authenticated browser runtime: **NOT YET VERIFIED**.
End-to-end runtime proof: **NOT YET PASSED**.
Idempotency runtime proof: **NOT YET PASSED**.
Controlled-failure recovery proof: **NOT YET PASSED**.
Deployment/runtime release gate: **NOT PASSED**.

Those gates are intentionally not represented as complete until an authenticated V7 runtime event is observed in the actual Hub.
