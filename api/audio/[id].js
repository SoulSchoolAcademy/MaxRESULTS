export default async function handler(req, res) {
  const id = req.query?.id;

  if (!id || !/^[A-Za-z0-9_-]+$/.test(id)) {
    return res.status(400).json({ error: 'Invalid audio file ID' });
  }

  const driveUrl = `https://drive.google.com/uc?export=download&id=${encodeURIComponent(id)}`;
  const headers = {};
  if (req.headers.range) headers.Range = req.headers.range;

  try {
    let response = await fetch(driveUrl, { headers, redirect: 'follow' });

    // Google Drive can return an HTML confirmation page instead of media bytes
    // for files that trigger its download confirmation flow. Follow that flow
    // server-side so the browser always receives actual audio bytes.
    const contentType = response.headers.get('content-type') || '';
    if (contentType.includes('text/html')) {
      const html = await response.text();
      const tokenMatch = html.match(/confirm=([0-9A-Za-z_-]+)/);
      const formActionMatch = html.match(/<form[^>]+action="([^"]+)"/i);
      const token = tokenMatch?.[1];
      const action = formActionMatch?.[1];

      if (token) {
        const confirmedUrl = action
          ? new URL(action, driveUrl)
          : new URL(driveUrl);
        confirmedUrl.searchParams.set('confirm', token);
        confirmedUrl.searchParams.set('id', id);
        confirmedUrl.searchParams.set('export', 'download');
        response = await fetch(confirmedUrl, { headers, redirect: 'follow' });
      }
    }

    if (!response.ok) {
      return res.status(response.status).json({
        error: 'Google Drive audio request failed',
        status: response.status
      });
    }

    const finalType = response.headers.get('content-type') || 'audio/mpeg';
    if (finalType.includes('text/html') || finalType.includes('application/json')) {
      return res.status(502).json({
        error: 'Google Drive returned a non-audio response'
      });
    }

    res.setHeader('Content-Type', finalType);
    res.setHeader('Accept-Ranges', 'bytes');
    res.setHeader('Cache-Control', 'public, max-age=3600, s-maxage=86400');

    const length = response.headers.get('content-length');
    const range = response.headers.get('content-range');
    if (length) res.setHeader('Content-Length', length);
    if (range) res.setHeader('Content-Range', range);

    res.status(response.status === 206 ? 206 : 200);

    if (!response.body) return res.end();

    const reader = response.body.getReader();
    try {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        res.write(Buffer.from(value));
      }
    } finally {
      reader.releaseLock();
    }
    res.end();
  } catch (error) {
    console.error('Powercast audio proxy error:', error);
    return res.status(502).json({ error: 'Unable to retrieve Powercast audio' });
  }
}
