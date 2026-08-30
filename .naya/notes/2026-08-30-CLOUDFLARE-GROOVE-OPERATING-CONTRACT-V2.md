# 🔱 NAYA SMART NOTE — CLOUDFLARE + GROOVE OPERATING CONTRACT V2

**Date:** 2026-08-30
**Status:** CANONICAL / FUTURE-NAYA OPERATING AUTHORITY
**Scope:** Naya Power Player static-first Cloudflare deployment + Groove embedding
**Purpose:** Ensure every future Naya understands the proven operating model, constraints, integration seams, and evidence discipline before building another Player block.

## 1. CORE DECISION

Naya Power Player is built as **modular, independently deployable static experience blocks**.

Each block is:
- designed as one part of a unified Naya Power experience;
- coded and QA'd independently;
- packaged as a static ZIP suitable for Cloudflare Pages Direct Upload;
- deployed to its own URL;
- connected to Groove only after it is approved;
- replaceable without rebuilding unrelated blocks.

**GitHub = canonical source. Cloudflare = hosted experience. Groove = composition layer.**

> ONE EXPERIENCE. MANY COHERENT BLOCKS.

## 2. STATIC-FIRST CLOUDFLARE LAW

For the no-Wrangler path, the deployment artifact must be static.

Allowed:
- index.html
- CSS
- browser JavaScript
- JSON/content
- SVG/images
- audio/video where individual assets meet Cloudflare limits
- `_headers`
- other browser-deliverable static assets

Do not put Wrangler/build/runtime requirements into a direct-upload ZIP.
Do not include secrets.
Do not claim server functionality that does not exist.

Cloudflare Pages Direct Upload documentation establishes a maximum of 1,000 files for drag-and-drop and a maximum individual asset size of 25 MiB. The 25 MiB figure is **per file, not total project size**.

## 3. CLOUDFLARE ↔ GROOVE MODEL

The approved deployment chain is:

GitHub → static Cloudflare deployment → HTTPS block URL → Groove custom code/embed → human.

Groove does not need the block's source code. It embeds the deployed URL.

A block is not connected to Groove until it is production-ready.

## 4. IFRAME HEIGHT

There is no universal Naya Power iframe height.

Because Groove and Cloudflare are normally different origins, the iframe cannot directly resize its parent's DOM.

Use:
1. known responsive height for stable blocks;
2. aspect-ratio for predictable media compositions;
3. `postMessage` only when dynamic content proves that parent resizing is necessary.

Do not build a complex resize protocol into E01 merely because it may be useful later.

## 5. POSTMESSAGE

When required, use a small versioned protocol with origin validation.

Example envelope:

```json
{
  "protocol": "naya-power.embed.v1",
  "block": "E03",
  "type": "NAYA_BLOCK_HEIGHT",
  "payload": {}
}
```

Potential events:
- NAYA_BLOCK_READY
- NAYA_BLOCK_HEIGHT
- NAYA_BLOCK_NAVIGATE
- NAYA_BLOCK_EVENT
- NAYA_BLOCK_STATE
- NAYA_BLOCK_AUTH_REQUEST

Parent validates `event.origin`. Child validates intended parent origin where appropriate. Never accept arbitrary cross-origin commands.

## 6. EMBEDDING / FRAME SECURITY

Every embeddable Cloudflare block must be checked for framing policy.

Do not accidentally ship:
- `X-Frame-Options: DENY`
- CSP `frame-ancestors` that excludes the approved Groove origin
- restrictive Permissions Policy that breaks required media/microphone/fullscreen behavior

Cloudflare Pages supports `_headers`, including CSP and related response-header configuration.

The actual production Groove parent origin must be verified before locking an allowlist.

## 7. MOBILE

Groove controls the outer page. The Cloudflare block controls its own internal responsiveness.

Every block must include:

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

Requirements:
- no horizontal overflow;
- touch-friendly controls;
- readable typography;
- adaptive layout;
- no hover dependency;
- keyboard support;
- safe-area awareness where appropriate.

Vertical stacking is the default Player composition model. Horizontal swipe navigation is not foundational.

## 8. AUDIO / VIDEO / VOICE

Audio and video can operate inside the iframe. The principal browser constraint is autoplay policy, not iframe capability.

Design law:

> USER INITIATES MEDIA → MEDIA PLAYS.

Do not rely on guaranteed audible autoplay on initial load.

Where needed, Groove's iframe should grant relevant capabilities, for example:

```html
allow="autoplay; fullscreen; microphone"
```

Use real media elements and truthful playback state. Handle rejected `play()` calls. Provide visible controls and graceful permission/error states.

Microphone access must be requested in response to user intent and requires HTTPS plus browser permission.

## 9. SUPABASE

A static Cloudflare browser application can use the Supabase JavaScript client for authentication and browser-side API access.

Only a Supabase publishable/anon client key belongs in browser code. Never expose service-role keys, database passwords, or private secrets.

Use Supabase Auth + RLS for user identity/data boundaries. Trusted operations belong in a server/edge boundary when required.

Future architecture must avoid nine independent login experiences. Naya Power should have one coherent identity model shared across blocks.

## 10. AUTH + CROSS-ORIGIN RULE

Before production authentication is declared complete, test the actual Groove + Cloudflare embedding context for session persistence, redirects, browser privacy behavior, and cross-origin storage behavior.

Prefer a coherent Naya Power custom-domain strategy for production rather than permanently treating unrelated generated `pages.dev` URLs as the product identity.

## 11. BLOCK LIFECYCLE

For every Player block:

BUILD → STATIC QA → OSCAR → REPAIR → DEPLOY → HUMAN TEST → GROOVE EMBED → FREEZE → NEXT BLOCK.

Do not connect unfinished blocks to Groove.

Do not rebuild unrelated blocks when one block changes.

## 12. PERFORMANCE

The iframe is an additional loading boundary. Keep blocks lean:
- minimal dependencies;
- optimized images;
- lazy-load noncritical media;
- no unnecessary framework/runtime;
- no unused fonts;
- limited critical preloads;
- stable layout;
- efficient animation.

Use versioned/hashed asset filenames where practical to avoid stale cache problems.

## 13. TRUTH / EVIDENCE LAW

Never say a block is deployed because it is Cloudflare-compatible.
Never say Groove integration is verified because an iframe snippet exists.
Never say Supabase authentication is working until the actual flow has been tested.

The required distinction is:

**Implemented → Verified locally → Deployed → Production-tested → Groove-tested.**

When asked for a Naya Note / Smart Note / system update, provide the actual GitHub receipt: file path, commit SHA, and clickable repository URL. **Do not merely report that the note was created. SHOW THE EVIDENCE.**

## 14. FUTURE-NAYA STARTUP CHECK

Before building a new Player block, the next Naya must:
1. read this note;
2. inspect current Player state;
3. verify the current Cloudflare deployment method;
4. verify the actual Groove embedding environment when integration is involved;
5. preserve the static-first constraint unless dynamic functionality genuinely requires an edge/runtime layer;
6. use the smallest integration mechanism that proves the requirement;
7. leave a receipt for every claimed repository/system update.

## 15. SOURCE AUTHORITY

This note operationalizes the Cloudflare/Groove findings and the Naya Power Player modular-block strategy. Platform claims must remain tied to current official Cloudflare/browser/Supabase documentation and actual production tests. Groove-specific behavior must be verified against the actual Groove environment before being elevated from "documented/observed" to "production-proven."

## 16. BOTTOM LINE

> **Solve the platform once. Build the Player many times.**

The Player is one experience to the human, but a collection of bounded, independently deployable engineering blocks to Naya.
