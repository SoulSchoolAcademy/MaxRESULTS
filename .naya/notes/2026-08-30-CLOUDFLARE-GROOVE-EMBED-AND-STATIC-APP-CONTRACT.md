# 🔱 CLOUDFLARE + GROOVE STATIC APP / EMBED CONTRACT

**Date:** 2026-08-30  
**Status:** CANONICAL ENGINEERING + DEPLOYMENT NOTE  
**Purpose:** Establish the verified rules for building Naya Power Player as modular static Cloudflare applications and composing those applications into Groove embeds without repeatedly rediscovering platform constraints.

---

# 1. DECISION

Naya Power Player will be built as **modular, independently deployable static experience blocks**.

Each block is:

- designed as part of one continuous Naya Power experience;
- independently coded and tested;
- independently packaged as a ZIP;
- independently deployed to Cloudflare Pages/static hosting;
- given its own stable URL;
- embedded into Groove only after the block is production-ready;
- replaceable without rebuilding unrelated blocks.

The human experiences one application.

Engineering sees a set of bounded applications.

> **ONE EXPERIENCE. MANY COHERENT BLOCKS.**

---

# 2. VERIFIED CLOUDFLARE DIRECT-UPLOAD CONSTRAINTS

Cloudflare Pages Direct Upload supports drag-and-drop static deployments. Current official documentation states:

- Drag-and-drop supports up to **1,000 files** per deployment.
- The maximum individual asset size is **25 MiB**.
- Wrangler supports up to 20,000 files on the Free plan, but Wrangler is intentionally outside this static-first deployment path.
- A Pages site can contain up to 20,000 files on Free.
- Larger individual files should be hosted separately, e.g. R2/public storage or another media host.
- Direct Upload dashboard deployments do not compile a `functions/` directory; Pages Functions require Wrangler.
- A `_worker.js` file is supported by dashboard drag-and-drop, but Naya Power blocks should NOT introduce Worker runtime complexity unless the product explicitly requires it.

Sources: Cloudflare Pages Direct Upload and Limits documentation. citeturn2search1turn2search0

## STATIC ZIP LAW

A Cloudflare static ZIP intended for direct upload should contain only deployable static assets:

- `index.html`
- CSS
- browser JavaScript
- JSON/content
- SVG
- optimized images
- optimized audio/video where each individual file is under 25 MiB
- optional manifest/service-worker assets
- `_headers` when required

Do NOT put into the static ZIP:

- `wrangler.jsonc`
- npm/build requirements
- server-only code
- secrets
- Pages Functions expecting compilation
- fake backend endpoints presented as production

A block can contain a **future adapter seam**, but the current implementation must accurately report its truth state.

---

# 3. CLOUDFLARE HEADERS ARE PART OF THE EMBED CONTRACT

Cloudflare Pages supports a plain-text `_headers` file in the deployed output. It can add or override response headers for static assets. Cloudflare explicitly documents both `X-Frame-Options` and `Content-Security-Policy`/`frame-ancestors` as mechanisms controlling whether an application can be embedded in an iframe. citeturn0search0turn0search2

Therefore every Naya Power block intended for Groove must be reviewed for framing policy.

### Required principle

**Never accidentally ship a block with `X-Frame-Options: DENY` or an incompatible CSP `frame-ancestors` policy.**

If we need to restrict embedding, use an explicit allowlist appropriate to the actual Groove production origin rather than disabling framing accidentally.

### Recommended baseline

For a public, intentionally embeddable block:

- no `X-Frame-Options: DENY`;
- CSP `frame-ancestors` should explicitly permit the approved parent origin(s) when CSP is used;
- avoid unnecessary restrictive policies that break browser media, fonts, scripts, or framing;
- use `X-Content-Type-Options: nosniff`;
- use an intentional `Referrer-Policy`;
- use `Permissions-Policy` deliberately rather than accidentally blocking microphone/autoplay/fullscreen requirements.

The exact production parent origin must be verified before locking a restrictive allowlist.

---

# 4. GROOVE EMBEDDING MODEL

Research confirms GroovePages/Groove.cm supports custom code/embed elements and third-party embeds. Groove documentation/examples and current ecosystem references show custom HTML/code elements used for embeds, and Groove supports responsive/device-specific page behavior. citeturn1search8turn1search9turn1search5

Therefore the architecture is:

```text
CLOUDFLARE BLOCK
      │
      │ HTTPS URL
      ▼
GROOVE CODE / EMBED ELEMENT
      │
      ▼
GROOVE PAGE
      │
      ▼
HUMAN
```

The Cloudflare block does not need to be uploaded into Groove as source code.

Groove only needs the embed integration.

### Important

The authoritative source remains GitHub.

Cloudflare hosts the deployable block.

Groove composes the customer experience.

---

# 5. IFRAME HEIGHT

There is **no universal fixed iframe height that should be treated as the Naya Power standard**.

An iframe's height belongs to the parent document. A cross-origin iframe cannot directly resize its parent's DOM because of the browser same-origin security model.

Therefore we use one of three approaches:

### A. Fixed/responsive known height

Best for blocks with stable composition.

Example concept:

```html
<iframe
  src="https://BLOCK-URL"
  style="width:100%;height:900px;border:0;display:block;"
  loading="lazy"
  allow="autoplay; fullscreen; microphone">
</iframe>
```

The exact height is determined per block and breakpoint.

### B. Aspect-ratio / media-driven height

Best for video/media blocks with predictable dimensions.

### C. `postMessage` height bridge

Best for highly dynamic blocks whose content height changes substantially during interaction.

This should NOT be added to every block automatically.

> **Start simple. Add cross-origin resize messaging only when a block proves it needs dynamic parent resizing.**

---

# 6. POSTMESSAGE RULE

`window.postMessage()` is the correct browser mechanism for controlled cross-origin communication between the Groove parent page and a Cloudflare iframe.

It should be treated as an **optional integration protocol**, not a foundation dependency.

Potential messages:

```text
NAYA_BLOCK_READY
NAYA_BLOCK_HEIGHT
NAYA_BLOCK_NAVIGATE
NAYA_BLOCK_EVENT
NAYA_BLOCK_FOCUS
NAYA_BLOCK_AUTH_REQUEST
NAYA_BLOCK_STATE
```

Every message must include:

- protocol/version;
- block ID;
- event type;
- payload;
- source validation.

The parent must verify `event.origin`.

The iframe must verify the intended parent origin where appropriate.

Never accept arbitrary commands from arbitrary origins.

### Initial implementation

For E01, E02, etc.:

**Do not implement postMessage unless testing demonstrates a real need.**

For the first blocks, a carefully selected responsive fixed/min-height strategy is simpler and more reliable.

---

# 7. MOBILE BEHAVIOR

Groove itself supports responsive/device-specific page behavior. Third-party references document multiple device breakpoints and responsive styling capabilities in GroovePages. citeturn1search5turn1search17

But an embedded Cloudflare application has its own viewport.

Therefore every block must include:

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

and must be responsive **inside the iframe**.

### Rule

Do not depend on Groove to make the internal Cloudflare application responsive.

Groove controls the outer page.

The block controls itself.

This is a critical separation.

---

# 8. MOBILE DESIGN LAW

Naya Power blocks must be designed mobile-first enough to remain excellent inside a narrow iframe.

Requirements:

- no fixed desktop canvas;
- no horizontal overflow;
- no tiny controls;
- touch targets approximately 44px or larger where practical;
- readable text;
- adaptive typography;
- stacked layouts where appropriate;
- reduced decorative complexity at narrow widths;
- no dependence on hover;
- keyboard support for desktop;
- safe-area awareness where appropriate.

Horizontal swipe navigation is NOT the foundational architecture.

Vertical block stacking remains the default.

---

# 9. AUDIO + VIDEO INSIDE IFRAME

Audio/video can function inside an iframe, but browser media policies still apply.

The critical issue is **autoplay**, not iframe capability.

MDN documents that audible media autoplay is commonly blocked until the user interacts with the page, and that iframe Permissions Policy can be used to grant autoplay. citeturn2search3turn2search9

Therefore Naya Power media blocks must follow:

> **USER INITIATES MEDIA. MEDIA PLAYS.**

Do not design the product around guaranteed audible autoplay on initial load.

### Recommended iframe attributes

Where a block requires these capabilities:

```html
<iframe
  src="..."
  allow="autoplay; fullscreen; microphone">
</iframe>
```

The `allow` attribute is the iframe Permissions Policy mechanism for features such as microphone, camera, autoplay, fullscreen, etc. citeturn2search7

### Media rules

- Use real `<audio>`/`<video>` elements when actual media exists.
- Start playback from a user gesture where possible.
- Provide obvious play/pause controls.
- Handle rejected `play()` promises gracefully.
- Never display fake playback progress for media that is not actually playing.
- Use poster/visual state when autoplay is unavailable.
- Keep individual media assets below Cloudflare's 25 MiB Pages asset limit, or host larger media externally/R2. citeturn2search0

---

# 10. VOICE / MICROPHONE

Microphone access inside an iframe is possible through browser Permissions Policy, but it must be explicitly permitted by the iframe and ultimately granted by the user/browser.

The iframe should request microphone only when the user activates voice input.

Recommended:

```html
<iframe allow="microphone; autoplay; fullscreen" ...>
```

The Cloudflare page itself must use HTTPS for production browser microphone access.

Voice input must have a visible permission/error state.

Never assume microphone access exists.

---

# 11. FULLSCREEN

If a block contains video or an immersive Naya mode that benefits from fullscreen, request it through the iframe `allow` policy and user gesture.

Do not make fullscreen a requirement for normal operation.

---

# 12. SUPABASE AUTH — YES, CLOUDFARE CAN CONNECT

A static Cloudflare-hosted browser application can use the Supabase JavaScript client directly.

Supabase documents browser initialization with `createClient(supabase_url, publishable_key)` and supports persisted browser sessions through local storage. citeturn0search3turn0search5

Therefore:

```text
NAYA POWER BLOCK
      │
      ▼
SUPABASE JS CLIENT
      │
      ├── Auth
      ├── Session
      └── Supabase APIs
```

is technically valid without a Worker.

### Critical security rule

Only the Supabase **publishable key** belongs in browser code.

Never expose:

- service-role keys;
- database passwords;
- private API secrets;
- server credentials.

Sensitive operations must use Supabase RLS and/or a trusted server/Edge Function/Worker layer.

Supabase's current documentation distinguishes browser `supabase-js` usage from server/edge packages. citeturn0search17

---

# 13. AUTH + IFRAME ARCHITECTURE DECISION

This requires one deliberate future test.

If every block is cross-origin, browser storage/session behavior and authentication redirects need to be tested in the actual Groove embedding context.

Do not assume that every browser privacy policy treats third-party iframe storage identically.

### Preferred architecture

Where possible, use a shared Naya Power custom domain strategy so the blocks have a coherent first-party relationship with the application ecosystem.

Example conceptual model:

```text
naya-power.example/
    e01
    e02
    e03
```

or separate subdomains under a controlled Naya Power domain.

This is preferable to a random collection of unrelated `pages.dev` origins once production identity/auth is introduced.

---

# 14. AUTH SHOULD NOT BE REPEATED PER BLOCK

The Player must not create nine independent login experiences.

The future architecture should be:

```text
              NAYA POWER IDENTITY
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
            E01       E02       E03 ...
             │         │         │
             └─────────┼─────────┘
                       ▼
                   SUPABASE
```

The user experiences one identity.

The blocks consume the shared authenticated context through a deliberate protocol.

This is one of the places where a future `postMessage` bridge may become valuable.

---

# 15. PARENT ↔ IFRAME COMMUNICATION

Initial blocks should be **self-contained**.

Do not build a communication bus just because it might someday be useful.

Introduce it when the product actually needs cross-block state.

When needed, use a small versioned message protocol.

Example:

```json
{
  "protocol": "naya-power.embed.v1",
  "block": "E03",
  "type": "NAYA_BLOCK_READY",
  "payload": {}
}
```

Possible later uses:

- dynamic iframe height;
- parent navigation;
- authenticated state handoff;
- analytics events;
- challenge progress;
- media coordination;
- global Naya state.

Do not use `postMessage` as a substitute for a proper backend/data model.

---

# 16. BLOCK URL STRATEGY

Each finished block gets a stable deployment URL.

Conceptually:

```text
E01 → Cloudflare URL A
E02 → Cloudflare URL B
E03 → Cloudflare URL C
...
```

Groove embeds the URLs only after the corresponding block is approved.

If a block is replaced, the Groove embed can be updated to the new URL.

### Production refinement

Prefer stable custom-domain routes over permanent dependence on generated deployment URLs when the product is ready for production.

Example:

```text
player.nayanet.xyz/e01
player.nayanet.xyz/e02
player.nayanet.xyz/e03
```

or equivalent controlled subdomains.

The exact domain structure is a deployment decision, but **stable URLs should be treated as public API surfaces** once Groove depends on them.

---

# 17. CACHE / VERSIONING RULE

Cloudflare caches static assets globally. Pages documentation notes default caching behavior and supports custom cache headers via `_headers`. citeturn0search0turn0search6

Therefore blocks should use versioned asset filenames when possible:

```text
app.abc123.js
styles.def456.css
hero.xyz789.webp
```

or another immutable/versioned strategy.

Do not rely on a browser seeing a newly replaced asset immediately if the filename remains unchanged and caching is aggressive.

For the block HTML itself, use conservative caching while developing and stronger caching only after release behavior is understood.

---

# 18. PERFORMANCE LAW

Because Groove loads Cloudflare content inside an iframe, there are two page-loading layers:

```text
GROOVE PAGE
   │
   └── IFRAME
        │
        ├── HTML
        ├── CSS
        ├── JS
        ├── images
        └── media
```

Do not make the iframe an enormous payload.

Every block should:

- minimize dependencies;
- avoid unnecessary frameworks for simple blocks;
- lazy-load below-fold media;
- optimize images;
- avoid huge JS bundles;
- avoid shipping unused fonts;
- preload only critical resources;
- use responsive images;
- keep animation GPU-conscious;
- avoid layout shifts.

Cloudflare is fast.

That does not excuse a bloated application.

---

# 19. MEDIA STRATEGY

Because Cloudflare Pages has a 25 MiB **per-file** limit rather than a 25 MiB total-site limit, the correct architecture is not “keep the whole block under 25 MB.” It is:

> **Keep every individual static asset under 25 MiB, and keep the block lightweight overall.**

For large media:

- external CDN;
- R2/public object storage;
- specialized video/audio hosting;
- or another appropriate media origin.

Cloudflare explicitly recommends R2/public storage or custom domains for larger files. citeturn2search0

---

# 20. CLOUDFLARE + SUPABASE FUTURE STACK

The target architecture can therefore evolve cleanly:

```text
                       GROOVE
                          │
                    iframe/embed
                          │
                          ▼
                CLOUDFLARE STATIC BLOCK
                          │
               ┌──────────┼──────────┐
               ▼          ▼          ▼
             NAYA       SUPABASE    MEDIA
           EXPERIENCE     AUTH       CDN
               │           │
               └─────┬─────┘
                     ▼
              FUTURE NAYA GATEWAY
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      SUPERBRAIN   HUB       COLLECTIVE
```

This preserves the NayaPOWER principle:

> **CONNECT THE SUPERBRAIN. DO NOT ABSORB THE SUPERBRAIN.**

The static Player remains the experience layer.

The Hub remains the controlled connection layer.

The Superbrain remains sovereign.

---

# 21. WHAT WE SHOULD NOT DO

Do not:

- rebuild the whole Player for every visual change;
- create a single giant iframe containing the entire product while developing;
- put Wrangler configuration into direct-upload ZIPs;
- assume Groove will make an iframe's internal layout responsive;
- assume iframe height auto-adjusts cross-origin;
- assume audible autoplay will work;
- request microphone before user intent;
- expose Supabase service-role credentials;
- create nine separate authentication systems;
- add postMessage before a real cross-origin integration need exists;
- use fake API responses and call them production;
- depend on `pages.dev` forever if production identity requires a stable custom domain;
- ship individual assets above 25 MiB.

---

# 22. BLOCK DELIVERY CONTRACT

Every Naya Power block must ship with:

```text
BLOCK ID
PURPOSE
HUMAN OUTCOME
CLOUDFARE DEPLOYMENT PACKAGE
GROOVE EMBED URL
EMBED HEIGHT STRATEGY
MOBILE RULES
MEDIA PERMISSIONS
VOICE/MICROPHONE REQUIREMENTS
TRUTH STATE
AUTH REQUIREMENTS
POSTMESSAGE REQUIREMENTS (if any)
ACCESSIBILITY CHECK
PERFORMANCE CHECK
OSCAR RESULT
```

The Groove embed should not be created until the block has passed its own acceptance gate.

---

# 23. ONE-SHOT PLATFORM TEST PLAN

Before producing many blocks, perform one controlled **E01 platform proof**.

Test:

1. Direct-upload static ZIP to Cloudflare Pages.
2. Confirm all assets load.
3. Confirm iframe framing works.
4. Embed the Cloudflare URL in Groove.
5. Confirm desktop rendering.
6. Confirm mobile rendering.
7. Confirm iframe height behavior.
8. Confirm audio playback after user gesture.
9. Confirm video playback after user gesture.
10. Confirm microphone permission if E01 uses it.
11. Confirm fullscreen if needed.
12. Confirm no browser console errors.
13. Confirm no CSP/frame errors.
14. Confirm reload behavior.
15. Confirm navigation behavior.
16. Confirm local/session state behavior.
17. Confirm Supabase test authentication if authentication is included.
18. Confirm parent/iframe isolation.
19. Confirm optional postMessage only if needed.
20. Record exact working values in the next canonical platform note.

Once E01 passes this, the platform contract becomes reusable for E02–E09.

---

# 24. FINAL PLATFORM LAW

> **CLOUDFLARE HOSTS THE EXPERIENCE. GROOVE COMPOSES THE EXPERIENCE. GITHUB GOVERNS THE SOURCE. SUPABASE PROVIDES IDENTITY/DATA WHEN REQUIRED. NAYAPOWER GOVERNS THE INTELLIGENCE ARCHITECTURE.**

And the delivery loop is:

```text
DESIGN BLOCK
     ↓
BUILD BLOCK
     ↓
STATIC ZIP
     ↓
CLOUDFLARE
     ↓
REAL URL
     ↓
GROOVE EMBED
     ↓
REAL HUMAN TEST
     ↓
OSCAR
     ↓
REPAIR
     ↓
FREEZE
     ↓
NEXT BLOCK
```

### The objective is not to prove that an iframe works.

We already know embedded media and custom code are viable in the Groove ecosystem.

The objective is to establish **one repeatable, evidence-backed deployment pattern** and then reuse it.

> **SOLVE THE PLATFORM ONCE. BUILD THE PRODUCT MANY TIMES.** 🔱
