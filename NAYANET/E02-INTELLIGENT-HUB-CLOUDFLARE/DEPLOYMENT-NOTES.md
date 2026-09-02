# Cloudflare Deployment Notes

## Canonical source

`NAYANET/E02-INTELLIGENT-HUB-CLOUDFLARE/`

## Required runtime files

The standalone Cloudflare build requires:

- `index.html`
- `styles.css`
- `compat.css`
- `app.js`
- `_headers`
- `404.html`

`index.html` explicitly references `/styles.css`, `/compat.css`, and `/app.js`. Therefore a deployment artifact containing only `index.html` and `_headers` is incomplete.

## Release gate

The packaging workflow must include every required runtime asset and verify the exact artifact before Cloudflare publication.

Do not claim the Cloudflare deployment is production-ready until the artifact has been verified and the deployed URL has been tested for:

1. HTML rendering
2. CSS loading
3. JavaScript loading
4. entry interaction
5. Hub transition
6. responsive behavior
7. 404 handling

## Important distinction

GitHub repository/project organization and Cloudflare deployment are separate concerns.

The repository is the source of truth. Cloudflare is the publication/runtime destination. The release artifact is the bridge between them.

**CONNECTED ≠ DEPLOYED. COMMITTED ≠ RELEASED. VERIFIED ≠ PRODUCTION-PROVEN.**
