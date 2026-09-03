const AUDIO_HEADERS = [
  "accept-ranges",
  "cache-control",
  "content-length",
  "content-range",
  "content-type",
  "etag",
  "last-modified",
];

const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS",
  "Access-Control-Allow-Headers": "Range,Content-Type",
  "Access-Control-Expose-Headers": "Accept-Ranges,Content-Length,Content-Range,Content-Type,ETag,Last-Modified",
};

function withCors(headers = {}) {
  const out = new Headers(headers);
  Object.entries(cors).forEach(([k, v]) => out.set(k, v));
  return out;
}

function isDriveId(value) {
  return /^[A-Za-z0-9_-]{10,}$/.test(value || "");
}

function copyMediaHeaders(source) {
  const out = new Headers();
  for (const name of AUDIO_HEADERS) {
    const value = source.get(name);
    if (value) out.set(name, value);
  }
  return out;
}

function looksLikeHtml(response) {
  const type = (response.headers.get("content-type") || "").toLowerCase();
  return type.includes("text/html") || type.includes("application/xhtml");
}

async function driveFetch(id, request) {
  const range = request.headers.get("Range");
  const headers = new Headers();
  headers.set("Accept", "audio/*,application/octet-stream;q=0.9,*/*;q=0.1");
  if (range) headers.set("Range", range);

  const urls = [
    `https://drive.usercontent.google.com/download?id=${encodeURIComponent(id)}&export=download&confirm=t`,
    `https://drive.google.com/uc?export=download&id=${encodeURIComponent(id)}&confirm=t`,
  ];

  let lastResponse = null;
  for (const target of urls) {
    const response = await fetch(target, { method: request.method, headers, redirect: "follow" });
    lastResponse = response;
    if (!looksLikeHtml(response)) return response;

    // Google Drive can return a confirmation HTML page for some files. If it
    // contains a confirmation token, replay the request with that token and
    // the response cookie so the Worker receives the actual media bytes.
    const html = request.method === "HEAD" ? "" : await response.clone().text();
    const token = html.match(/name="confirm" value="([^"]+)"/i)?.[1] ||
                  html.match(/[?&]confirm=([0-9A-Za-z_-]+)/i)?.[1];
    const cookie = response.headers.get("set-cookie")?.split(";")[0];
    if (token) {
      const retryHeaders = new Headers(headers);
      if (cookie) retryHeaders.set("Cookie", cookie);
      const retryUrl = `https://drive.usercontent.google.com/download?id=${encodeURIComponent(id)}&export=download&confirm=${encodeURIComponent(token)}`;
      const retry = await fetch(retryUrl, { method: request.method, headers: retryHeaders, redirect: "follow" });
      lastResponse = retry;
      if (!looksLikeHtml(retry)) return retry;
    }
  }
  return lastResponse;
}

function isPlayableContentType(type) {
  const t = (type || "").toLowerCase();
  return t.startsWith("audio/") || t.includes("application/octet-stream") || t.includes("binary/octet-stream");
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: withCors() });

    if (url.pathname === "/health") {
      return new Response(JSON.stringify({ ok: true, service: "nayanet-powercast", version: "audio-proxy-v1" }), {
        headers: withCors({ "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" }),
      });
    }

    if (url.pathname === "/audio" || url.pathname === "/audio/") {
      if (request.method !== "GET" && request.method !== "HEAD") {
        return new Response("Method Not Allowed", { status: 405, headers: withCors({ Allow: "GET,HEAD,OPTIONS" }) });
      }

      const id = url.searchParams.get("id") || "";
      if (!isDriveId(id)) {
        return new Response(JSON.stringify({ ok: false, error: "Invalid Google Drive file id" }), {
          status: 400,
          headers: withCors({ "Content-Type": "application/json; charset=utf-8" }),
        });
      }

      try {
        const upstream = await driveFetch(id, request);
        if (!upstream) throw new Error("No upstream response");

        const contentType = upstream.headers.get("content-type") || "";
        const status = upstream.status;
        if (looksLikeHtml(upstream) || !isPlayableContentType(contentType)) {
          return new Response(JSON.stringify({
            ok: false,
            error: "Google Drive did not return playable audio bytes",
            upstreamStatus: status,
            upstreamContentType: contentType || null,
          }), {
            status: 502,
            headers: withCors({ "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" }),
          });
        }

        const headers = withCors(copyMediaHeaders(upstream.headers));
        headers.set("Cache-Control", "public, max-age=300, s-maxage=3600");
        return new Response(request.method === "HEAD" ? null : upstream.body, { status, headers });
      } catch (error) {
        return new Response(JSON.stringify({ ok: false, error: String(error?.message || error) }), {
          status: 502,
          headers: withCors({ "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" }),
        });
      }
    }

    if (url.pathname === "/" || url.pathname === "") {
      return env.ASSETS.fetch(new Request(new URL("/index.html", request.url), request));
    }

    return env.ASSETS.fetch(request);
  },
};
