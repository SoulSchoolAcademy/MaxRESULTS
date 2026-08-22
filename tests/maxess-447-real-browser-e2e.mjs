import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';

const PORT = 4173;
const assessmentPath = join(process.cwd(), 'AISCORE-447-e2e.html');
const resultsUrl = 'https://results.nayanet.app/';

async function startServer() {
  const html = await readFile(assessmentPath, 'utf8');
  const server = createServer((req, res) => {
    if (req.url === '/' || req.url === '/AISCORE-447-e2e.html') {
      res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
      res.end(html);
      return;
    }
    res.writeHead(404);
    res.end('Not found');
  });
  await new Promise((resolve) => server.listen(PORT, '127.0.0.1', resolve));
  return server;
}

async function dismissNaya(page) {
  const dialog = page.locator('#nayaDialog');
  if (await dialog.isVisible().catch(() => false)) {
    const close = page.locator('#closeNaya');
    if (await close.isVisible().catch(() => false)) await close.click();
    await dialog.waitFor({ state: 'hidden', timeout: 5000 }).catch(() => {});
  }
}

async function completeAssessment(page, answerIndexes, label) {
  await page.goto(`http://127.0.0.1:${PORT}/AISCORE-447-e2e.html`, { waitUntil: 'domcontentloaded' });
  await page.locator('#nayaDialog.open').waitFor({ state: 'visible', timeout: 10000 });
  await dismissNaya(page);

  for (let i = 0; i < 15; i += 1) {
    await page.locator('#questionTitle').waitFor({ state: 'visible', timeout: 10000 });
    await page.waitForTimeout(220);
    await dismissNaya(page);

    const answerCount = await page.locator('#answers .answer').count();
    if (answerCount !== 5) throw new Error(`${label}: question ${i + 1} has ${answerCount} answers`);

    await page.locator('#answers .answer').nth(answerIndexes[i]).click();
    if (await page.locator('#continueButton').isDisabled()) throw new Error(`${label}: Continue remained disabled on question ${i + 1}`);
    await page.locator('#continueButton').click();
  }

  await page.waitForURL((url) => url.toString().startsWith(resultsUrl), { timeout: 30000, waitUntil: 'domcontentloaded' });
  const navigatedUrl = page.url();
  if (!navigatedUrl.startsWith(resultsUrl)) throw new Error(`${label}: did not navigate to ${resultsUrl}: ${navigatedUrl}`);

  await page.waitForFunction(() => window.MAXESS_RESULT?.contractVersion === 'MAXESS_RESULT_V1', undefined, { timeout: 10000 }).catch(async (error) => {
    const diagnostics = await page.evaluate(() => ({
      href: location.href,
      hashLength: location.hash.length,
      result: window.MAXESS_RESULT || null,
      scoreText: document.querySelector('.score-number')?.textContent?.trim() || '',
      bodyPrefix: document.body.innerText.slice(0, 1000)
    }));
    throw new Error(`${label}: Results contract did not hydrate: ${JSON.stringify(diagnostics)}; ${error.message}`);
  });

  const contract = await page.evaluate(() => window.MAXESS_RESULT);
  if (!contract) throw new Error(`${label}: MAXESS_RESULT missing`);
  if (contract.contractVersion !== 'MAXESS_RESULT_V1') throw new Error(`${label}: wrong contract version`);
  if (!Number.isFinite(Number(contract.overallScore)) || Number(contract.overallScore) < 0 || Number(contract.overallScore) > 100) throw new Error(`${label}: invalid overall score`);
  if (!Array.isArray(contract.dimensions) || contract.dimensions.length !== 5) throw new Error(`${label}: expected five dimensions`);
  if (!Array.isArray(contract.responses) || contract.responses.length !== 15) throw new Error(`${label}: expected fifteen responses`);

  const resultView = await page.evaluate(() => {
    const text = document.body.innerText;
    return {
      score: document.querySelector('.score-number')?.textContent?.trim() || '',
      sections: ['e01','e05','e06','e07','e08','e09'].map((id) => ({ id, present: !!document.getElementById(id) })),
      bodyLength: text.length,
      hasDemo: /demo score|preview score 82|DEMO_SCORE=82/i.test(text)
    };
  });

  if (resultView.hasDemo) throw new Error(`${label}: fabricated/demo score detected`);
  for (const section of resultView.sections) {
    if (!section.present) throw new Error(`${label}: required section ${section.id} missing`);
  }

  return { contract, navigatedUrl, resultView };
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
const page = await context.newPage();
page.on('pageerror', (error) => console.error(`PAGEERROR: ${error.message}`));
page.on('console', (message) => { if (message.type() === 'error') console.error(`CONSOLE ERROR: ${message.text()}`); });
const server = await startServer();

try {
  const profileA = Array(15).fill(0);
  const profileB = Array(15).fill(4);
  const a = await completeAssessment(page, profileA, 'PROFILE A');
  const b = await completeAssessment(page, profileB, 'PROFILE B');

  const different = {
    overallScore: Number(a.contract.overallScore) !== Number(b.contract.overallScore),
    dimensions: JSON.stringify(a.contract.dimensions) !== JSON.stringify(b.contract.dimensions),
    responses: JSON.stringify(a.contract.responses) !== JSON.stringify(b.contract.responses)
  };
  if (!different.overallScore || !different.dimensions || !different.responses) {
    throw new Error(`Differentiation proof failed: ${JSON.stringify(different)}`);
  }

  console.log(JSON.stringify({
    status: 'PASS',
    profileA: { score: a.contract.overallScore, dimensions: a.contract.dimensions, url: a.navigatedUrl },
    profileB: { score: b.contract.overallScore, dimensions: b.contract.dimensions, url: b.navigatedUrl },
    differentiation: different,
    sections: b.resultView.sections
  }, null, 2));
} finally {
  await browser.close();
  await new Promise((resolve) => server.close(resolve));
}
