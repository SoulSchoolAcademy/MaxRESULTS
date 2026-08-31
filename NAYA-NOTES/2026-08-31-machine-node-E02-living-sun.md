# Machine Node — E02 Living Sun Intelligent Hub

Date: 2026-08-31
Status: SOURCE-VERIFIED

Repository: SoulSchoolAcademy/NayaPOWER
Branch: main
Implementation file: NAYANET/E02-INTELLIGENT-HUB-AAA/index.html
Implementation commit: bfb605bc879e57badd8d0045078ef7cd40f687ef
Scorecard commit: f8bf5cadf344f5014f92e8a84222ba0864911a8d

Technical state:
- Single static HTML package; no build step or runtime dependency.
- Front Door name entry persists identity in localStorage.
- Hub contains an enlarged layered Living Sun with orbital rings.
- Eight network destinations are represented; two are authoritative live links.
- Five identity jewels and persistent identity rail are implemented.
- Talk uses browser speech recognition when available.
- Listen uses browser speech synthesis when available.
- Type-to-Naya calls /api/naya/ask when that backend exists and reports a truthful not-connected state otherwise.
- Unfinished worlds open a truthful CONNECTED modal rather than a fake destination.
- Responsive CSS and prefers-reduced-motion support are included.

Verification limitation: source was re-read from GitHub after the implementation commit. Browser/device smoke testing and Cloudflare production verification were not available through the connected GitHub boundary and are therefore not claimed.
