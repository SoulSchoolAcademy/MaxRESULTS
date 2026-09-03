export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // Workers Static Assets normally serves matching files before invoking
    // this handler. Keep an explicit root fallback so the deployed Worker
    // always has a deterministic document response.
    if (url.pathname === "/" || url.pathname === "") {
      return env.ASSETS.fetch(new Request(new URL("/index.html", request.url), request));
    }

    return env.ASSETS.fetch(request);
  },
};
