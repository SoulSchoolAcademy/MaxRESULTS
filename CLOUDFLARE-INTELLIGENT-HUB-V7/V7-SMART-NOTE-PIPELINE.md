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
- Edge Function `v7-smart-note`

The Edge Function requires a valid authenticated user, accepts the Human Note and Naya Note, deterministically constructs the Machine Note, Intelligent Feed event, Intelligent Block, Evidence receipt, and Hub state, and commits the complete transaction through the database RPC.

## Safety invariants
- No anonymous execution.
- The database function rejects a user ID that does not equal `auth.uid()`.
- RLS is enabled on the transaction table.
- Idempotency key prevents duplicate transactions.
- Incomplete pipeline payloads are rejected.
- Failed transactions must be surfaced rather than represented as successful intelligence.

## Acceptance test
A release does not pass the Smart Note gate until one authenticated test event can be observed end-to-end after refresh/re-entry, with every stage present and linked by event/receipt identity.

## Operational rule
If Naya recognizes that an interaction qualifies as a Smart Note, the application must invoke this pipeline or explicitly report the blocked stage and recovery action. It must never silently stop at acknowledgement.

## Current status
Backend transaction boundary: **IMPLEMENTED**.
Security boundary: **HARDENED** — anonymous RPC execution is denied; authenticated execution is allowed; RLS is enabled; the RPC enforces `auth.uid()` ownership.
Frontend invocation: **NOT YET VERIFIED**.
End-to-end runtime proof: **NOT YET PASSED**.

Those last two gates are intentionally not represented as complete until an authenticated V7 runtime event is observed in the actual Hub.
