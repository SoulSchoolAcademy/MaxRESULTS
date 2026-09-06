export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/' || url.pathname === '/index.html' || url.pathname.startsWith('/intelligence/')) {
      const response = await env.ASSETS.fetch(new Request(new URL('/index.html', request.url), request));
      const html = await response.text();
      const upgraded = html.replace('</body>', '<script src="/v7-intelligence-distribution.js"></script></body>');
      return new Response(upgraded, { status: response.status, headers: new Headers(response.headers) });
    }
    return env.ASSETS.fetch(request);
  }
};
