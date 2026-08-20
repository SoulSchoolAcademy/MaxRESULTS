import { chromium } from 'playwright';
import { createServer } from 'node:http';
import { readFile } from 'node:fs/promises';
import { join } from 'node:path';

const PORT = 4173;
const assessmentPath = join(process.cwd(), 'AIScoreMAXESS-e2e.html');
const resultsUrl = 'https://results.nayanet.xyz/';

async function startServer() {
  const html = await readFile(assessmentPath);
  const server = createServer((req, res) => {
    if (req.url === '/' || req.url === '/AIScoreMAXESS-e2e.html') {
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

async function completeAssessment(page, answerIndexes, profileName) {
  await page.goto(`http://127.0.0.1:${PORT}/AIScoreMAXESS-e2e.html`, { waitUntil: 'domcontentloaded' });

  for (let i = 0; i < 15; i += 1) {
    await page.locator('#teachingInterstitial.visible').waitFor({ state: 'visible', timeout: 10000 });

    if (i === 0) {
      const nayaUi = await page.evaluate(() => ({
        image: !!document.querySelector('.maxess-naya-teacher-image'),
        name: document.querySelector('.maxess-naya-teacher-copy strong')?.textContent?.trim() || '',
        listen: !!document.querySelector('#listenToNaya'),
        close: !!document.querySelector('#cloudContinue')
      }));
      if (!nayaUi.image || nayaUi.name !== 'Naya' || !nayaUi.listen || !nayaUi.close) {
        throw new Error(`${profileName}: Naya teaching popup is incomplete: ${JSON.stringify(nayaUi)}`);
      }

      await page.evaluate(() => {
        window.__MAXESS_AUDIO_UNAVAILABLE = false;
        window.addEventListener('naya:audio-unavailable', () => { window.__MAXESS_AUDIO_UNAVAILABLE = true; }, { once: true });
      });
      await page.locator('#listenToNaya').click();
      await page.waitForFunction(() => !document.querySelector('#teachingInterstitial')?.classList.contains('visible'));
      await page.waitForFunction(() => window.__MAXESS_AUDIO_UNAVAILABLE === true);
      if (await page.locator('#questionTitle').isVisible() === false) throw new Error(`${profileName}: question disappeared after Listen to Naya`);
      if (await page.locator('#answers .answer').count() !== 5) throw new Error(`${profileName}: answers disappeared after Listen to Naya`);
    } else {
      await page.locator('#cloudContinue').click();
    }

    const answers = page.locator('#answers .answer');
    await answers.nth(answerIndexes[i]).click();
    await page.locator('#continueButton').click();
  }

  await page.locator('#interestsView.visible').waitFor({ state: 'visible', timeout: 10000 });
  await page.locator('.interest-area').first().click();
  await page.locator('#interestContinue').click();

  const contract = await page.evaluate(() => window.MAXESS_RESULT);
  if (!contract) throw new Error(`${profileName}: MAXESS_RESULT missing after real assessment completion`);
  if (contract.contractVersion !== 'MAXESS_RESULT_V1') throw new Error(`${profileName}: wrong contract version`);
  if (!Number.isFinite(Number(contract.overallScore)) || Number(contract.overallScore) < 0 || Number(contract.overallScore) > 100) throw new Error(`${profileName}: invalid overallScore`);
  if (!Array.isArray(contract.dimensions) || contract.dimensions.length !== 5) throw new Error(`${profileName}: dimensions != 5`);
  if (!Array.isArray(contract.responses) || contract.responses.length !== 15) throw new Error(`${profileName}: responses != 15`);
  if (!Array.isArray(contract.selectedInterests) || contract.selectedInterests.length !== 1) throw new Error(`${profileName}: selectedInterests missing`);
  if (!contract.strongestCapability) throw new Error(`${profileName}: strongestCapability missing`);
  if (!contract.highestLeverageOpportunity) throw new Error(`${profileName}: highestLeverageOpportunity missing`);
  if (!contract.overallPattern) throw new Error(`${profileName}: overallPattern missing`);
  if (!contract.personalizedInterpretation) throw new Error(`${profileName}: personalizedInterpretation missing`);
  if (!contract.nextMove) throw new Error(`${profileName}: nextMove missing`);
  if (!contract.naya) throw new Error(`${profileName}: naya metadata missing`);

  const navigatedUrl = page.url();
  if (!navigatedUrl.startsWith(resultsUrl)) throw new Error(`${profileName}: did not navigate to public Results URL: ${navigatedUrl}`);

  await page.goto(navigatedUrl, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => window.MAXESS_RESULT && window.MAXESS_RESULT.contractVersion === 'MAXESS_RESULT_V1', null, { timeout: 30000 });

  const resultsSnapshot = await page.evaluate(() => ({
    contract: window.MAXESS_RESULT,
    visibleScore: document.querySelector('.score-number, [data-maxess-result-score], #score')?.textContent?.trim() || '',
    bodyText: document.body.innerText
  }));

  if (Number(resultsSnapshot.contract.overallScore) !== Number(contract.overallScore)) {
    throw new Error(`${profileName}: Results contract score does not match assessment score`);
  }

  const scoreText = resultsSnapshot.visibleScore.replace(/[^0-9.]/g, '');
  if (!scoreText) throw new Error(`${profileName}: Results visible score did not hydrate`);
  if (Number(scoreText) !== Math.round(Number(contract.overallScore))) {
    throw new Error(`${profileName}: visible Results score ${scoreText} != ${Math.round(contract.overallScore)}`);
  }

  if (/demo score|preview score 82|DEMO_SCORE=82/i.test(resultsSnapshot.bodyText)) {
    throw new Error(`${profileName}: fabricated/demo score detected in Results`);
  }

  return { contract, resultsUrl: navigatedUrl };
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
const page = await context.newPage();
const server = await startServer();

try {
  const profileA = Array(15).fill(0);
  const profileB = [4,4,4,4,0,4,4,4,4,0,4,4,4,4,0];

  const a = await completeAssessment(page, profileA, 'PROFILE A');
  const b = await completeAssessment(page, profileB, 'PROFILE B');

  const different = {
    overallScore: Number(a.contract.overallScore) !== Number(b.contract.overallScore),
    dimensions: JSON.stringify(a.contract.dimensions) !== JSON.stringify(b.contract.dimensions),
    masteryStage: a.contract.masteryStage !== b.contract.masteryStage,
    strongestCapability: a.contract.strongestCapability?.id !== b.contract.strongestCapability?.id,
    highestLeverageOpportunity: a.contract.highestLeverageOpportunity?.id !== b.contract.highestLeverageOpportunity?.id,
    overallPattern: JSON.stringify(a.contract.overallPattern) !== JSON.stringify(b.contract.overallPattern),
    personalizedInterpretation: JSON.stringify(a.contract.personalizedInterpretation) !== JSON.stringify(b.contract.personalizedInterpretation),
    nextMove: JSON.stringify(a.contract.nextMove) !== JSON.stringify(b.contract.nextMove)
  };

  if (!different.overallScore || !different.dimensions || !different.masteryStage || !different.strongestCapability || !different.overallPattern || !different.personalizedInterpretation) {
    throw new Error(`Differentiation proof failed: ${JSON.stringify(different)}`);
  }

  console.log(JSON.stringify({
    status: 'PASS',
    profileA: { overallScore: a.contract.overallScore, masteryStage: a.contract.masteryStage, strongest: a.contract.strongestCapability, opportunity: a.contract.highestLeverageOpportunity, resultsUrl: a.resultsUrl },
    profileB: { overallScore: b.contract.overallScore, masteryStage: b.contract.masteryStage, strongest: b.contract.strongestCapability, opportunity: b.contract.highestLeverageOpportunity, resultsUrl: b.resultsUrl },
    differentiation: different
  }, null, 2));
} finally {
  await browser.close();
  await new Promise((resolve) => server.close(resolve));
}
