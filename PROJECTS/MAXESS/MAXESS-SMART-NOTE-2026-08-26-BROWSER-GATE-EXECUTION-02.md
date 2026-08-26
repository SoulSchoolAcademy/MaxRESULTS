# 🧠 MAXESS SMART NOTE — BROWSER GATE EXECUTION 02

**Date:** 2026-08-26
**Priority:** P0
**Status:** EXECUTING / HUMAN TEST STILL GATED

## Current source truth

Main is now at commit `4229d3ce39bd653e6f536b42dd3cdcbf54716e6c`.

The V2 architecture remains:

**ONE APPLICATION → ONE STATE AUTHORITY → ONE ASSESSMENT DEFINITION → ONE SCORER → ONE MAXESS_RESULT_V1 → ONE RELEASE PATH → E01–E09 PRESENTATION.**

The canonical engine and score definition are authoritative. The result consumer is presentation-only and event-driven.

## Execution performed

### 1. Idempotent hardening

The prior deterministic Groove hardening script was not safe to run repeatedly: after a successful hardening commit, its exact replacement targets would no longer exist and a future workflow could fail before verification.

Fixed by making `PROJECTS/MAXESS/TESTS/maxess-v2-auto-hardening.mjs` idempotent.

It now:

- applies only missing hardening changes;
- accepts already-hardened source;
- asserts the complete hardened invariants afterward;
- fails only when a required hardened invariant is genuinely absent.

Commit: `ddd0f7ace71de84a2ca56cfc6f9f639faf48afaf`.

## 2. Browser evidence hardening

The browser harness was strengthened to leave evidence rather than merely returning a red CI status.

Updated:

`PROJECTS/MAXESS/TESTS/maxess-v2-browser.spec.mjs`

It now includes:

- longer explicit test budget for the full browser suite;
- Playwright trace on failure;
- screenshot on failure;
- machine-readable browser diagnostics on failure;
- request-failure capture;
- runtime/page-error capture;
- explicit runtime/engine/definition/result state diagnostics;
- duplicate Continue testing through dispatched click events rather than relying only on forced UI clicks.

Commit: `653fb7c369619ecdfe9d4adebf2f70f325d9f103`.

## 3. CI evidence retention

Updated `.github/workflows/maxess-v2-pretest.yml` to upload `test-results/**` and `playwright-report/**` on both success and failure.

This means a failed browser gate will produce inspectable evidence instead of forcing the next AI to guess from a red status.

Commit: `4229d3ce39bd653e6f536b42dd3cdcbf54716e6c`.

## 4. Executed workflow evidence

The new MAXESS V2 Pre-Test Excellence Gate is run `33002378451`.

Observed:

- checkout = successful;
- Node setup = successful;
- deterministic Groove hardening = successful;
- static architecture gate = successful;
- Playwright installation = successful;
- browser evidence gate = currently executing at the latest observation.

Human testing remains blocked.

## Prior browser evidence

Run `33001382999` reached the browser evidence step and failed. Its static/executable prerequisites passed. The exact browser log was not retained by the prior workflow, which is why the new workflow now uploads evidence artifacts.

## Important lesson

A red browser gate without preserved browser artifacts is insufficient diagnostic evidence.

The correct operating pattern is:

**EXECUTE → CAPTURE → CLASSIFY → FIX → RERUN.**

Never guess at the browser failure when the browser can produce an artifact proving it.

## Current board

- Engine: 🟢
- Canonical definition: 🟢
- Static architecture: 🟢
- Executable golden: 🟢
- Groove hardening: 🟢 in executed CI prerequisite
- Browser smoke: 🟡 pending current run
- Browser Q1→Q15: 🟡 pending current run
- Responsive browser: 🟡 pending current run
- E01 same-result proof: 🟡 pending current run
- Evidence receipt: 🟡 pending current run
- Human test: 🔴 gated

## Ten-star question

**Why is this not a 10?**

Because browser evidence has not yet produced a completed green receipt. The highest-leverage move is to let the current evidence run finish, inspect the actual artifacts if red, fix the real failing layer, and rerun. No premature human test.

## Next AI must know

Do not repeat generic Continue rewrites.
Do not treat the test harness as authoritative over the product.
Do not call browser GREEN without executed evidence.
Do not ask Shawn to test until the evidence gate is green.

The next execution should begin by inspecting run `33002378451` and its browser evidence artifacts before changing product code.
