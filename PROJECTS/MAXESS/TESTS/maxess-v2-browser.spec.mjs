import { test, expect } from '@playwright/test';
import fs from 'node:fs';

test.setTimeout(30000);
const browserDiagnostics={runtimeErrors:[],failedRequests:[]};
test.use({trace:'retain-on-failure',screenshot:'only-on-failure'});

test.afterEach(async ({page},testInfo)=>{
  if(testInfo.status!==testInfo.expectedStatus){
    const runtime=await page.evaluate(()=>({
      hasEngine:!!window.MAXESS_E00_ENGINE_V2,
      hasDefinition:!!window.MAXESS_AI_SCORE_DEFINITION_V1,
      hasRuntime:!!window.MAXESS_E00_V2,
      phase:window.MAXESS_E00_V2?.getState?.().phase||null,
      questionIndex:window.MAXESS_E00_V2?.getState?.().questionIndex??null,
      responses:window.MAXESS_E00_V2?.getState?.().responses?.length??null,
      result:window.MAXESS_RESULT?{score:window.MAXESS_RESULT.overallScore,contract:window.MAXESS_RESULT.contractVersion}:null
    })).catch(e=>({evaluateError:String(e)}));
    const diagnostics={
      url:page.url(),
      title:await page.title().catch(()=>''),
      runtime,
      runtimeErrors:browserDiagnostics.runtimeErrors,
      failedRequests:browserDiagnostics.failedRequests
    };
    await fs.promises.writeFile(testInfo.outputPath('maxess-browser-diagnostics.json'),JSON.stringify(diagnostics,null,2));
  }
});

function buildHarness(){
  const groove=fs.readFileSync('PROJECTS/MAXESS/E00 MAXESS V2 — AUTHORITATIVE GROOVE.html','utf8');
  const engine=fs.readFileSync('PROJECTS/MAXESS/ENGINEERING/MAXESS-E00-AUTHORITATIVE-ENGINE-V2.js','utf8');
  const definition=fs.readFileSync('PROJECTS/MAXESS/ENGINEERING/MAXESS-AI-SCORE-DEFINITION-V1.js','utf8');
  const consumer=fs.readFileSync('MAXESS-RESULT-CONSUMER-V2.html','utf8');
  const e01=fs.readFileSync('E01','utf8');
  const e01Styles=[...e01.matchAll(/<style[\s\S]*?<\/style>/gi)].map(m=>m[0]).join('\n');
  const e01Body=(e01.match(/<body[^>]*>([\s\S]*?)<\/body>/i)||[, ''])[1];
  const scriptMatches=[...groove.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)];
  const runtimeMatches=scriptMatches.filter(m=>/window\.MAXESS_E00_V2\s*=/.test(m[1]));
  if(runtimeMatches.length!==1)throw new Error(`Expected exactly one authoritative E00 runtime script, found ${runtimeMatches.length}`);
  const runtime=runtimeMatches[0][1];
  const firstScriptIndex=groove.indexOf('<script');
  if(firstScriptIndex<0)throw new Error('Authoritative E00 scripts not found in Groove');
  const grooveMarkup=groove.slice(0,firstScriptIndex);
  const html=`<!doctype html><html><head><meta charset="utf-8">${e01Styles}</head><body>${grooveMarkup}<div id="E01-HARNESS">${e01Body}</div>${consumer}</body></html>`;
  return {html,engine,definition,runtime};
}

async function completeAssessment(page, scoreMode){
  const runtimeErrors=[];
  const failedRequests=[];
  browserDiagnostics.runtimeErrors=[];
  browserDiagnostics.failedRequests=[];
  page.on('pageerror',e=>runtimeErrors.push(e.message));
  page.on('console',m=>{if(m.type()==='error')runtimeErrors.push(m.text())});
  page.on('requestfailed',r=>failedRequests.push(`${r.method()} ${r.url()} :: ${r.failure()?.errorText||'unknown'}`));
  await page.goto('about:blank');
  const harness=buildHarness();
  await page.setContent(harness.html, {waitUntil:'domcontentloaded'});
  await page.addScriptTag({content:harness.engine});
  await page.addScriptTag({content:harness.definition});
  await page.addScriptTag({content:harness.runtime});
  await page.waitForFunction(()=>!!window.MAXESS_E00_ENGINE_V2&&!!window.MAXESS_AI_SCORE_DEFINITION_V1);
  await page.waitForFunction(()=>!!window.MAXESS_E00_V2);
  await page.evaluate(()=>{
    window.__MAXESS_TEST__={ready:0,updated:0,last:null};
    window.addEventListener('MAXESS_RESULT_READY',e=>{window.__MAXESS_TEST__.ready++;window.__MAXESS_TEST__.last=e.detail});
    window.addEventListener('maxess:result-updated',e=>{window.__MAXESS_TEST__.updated++});
  });
  await expect(page.locator('#MAXESS-E00-V2 #mx-q')).not.toHaveText('');
  for(let qi=0;qi<15;qi++){
    const idx=await page.evaluate(({qi,scoreMode})=>{
      const q=window.MAXESS_AI_SCORE_DEFINITION_V1.questions[qi];
      return scoreMode==='min'
        ? q.answers.reduce((best,a,j)=>a.score<q.answers[best].score?j:best,0)
        : q.answers.reduce((best,a,j)=>a.score>q.answers[best].score?j:best,0);
    },{qi,scoreMode});
    const answers=page.locator('#MAXESS-E00-V2 .ans');
    await expect(answers).toHaveCount(5);
    const cont=page.locator('#MAXESS-E00-V2 #mx-cont');
    await expect(cont).toBeDisabled();
    await answers.nth(idx).click();
    await expect(cont).toBeEnabled();
    if(qi<14){
      await cont.click();
      await expect(page.locator('#MAXESS-E00-V2 #mx-pl')).toHaveText(`QUESTION ${qi+2} OF 15`);
    }else{
      await cont.click();
    }
  }
  await expect(page.locator('#MAXESS-E00-V2 #mx-done')).toHaveClass(/on/);
  const result=await page.evaluate(()=>({
    score:window.MAXESS_RESULT?.overallScore,
    contract:window.MAXESS_RESULT?.contractVersion,
    responses:window.MAXESS_RESULT?.responses?.length,
    frozen:Object.isFrozen(window.MAXESS_RESULT),
    ready:window.__MAXESS_TEST__.ready,
    updated:window.__MAXESS_TEST__.updated,
    completionCount:window.MAXESS_E00_V2.getState().completionCount,
    e01Score:document.querySelector('#e01 #score-number')?.textContent||null
  }));
  browserDiagnostics.runtimeErrors=[...runtimeErrors];
  browserDiagnostics.failedRequests=[...failedRequests];
  return {result,runtimeErrors,failedRequests};
}

test('MAXESS V2 canonical minimum golden browser path', async ({page})=>{
  const {result:r,runtimeErrors,failedRequests}=await completeAssessment(page,'min');
  expect(r.score).toBe(25);
  expect(r.contract).toBe('MAXESS_RESULT_V1');
  expect(r.responses).toBe(15);
  expect(r.frozen).toBe(true);
  expect(r.ready).toBe(1);
  expect(r.updated).toBe(1);
  expect(r.completionCount).toBe(1);
  expect(Number(r.e01Score)).toBe(25);
  expect(failedRequests).toEqual([]);
  expect(runtimeErrors).toEqual([]);
});

test('MAXESS V2 maximum golden browser path and duplicate Continue guard', async ({page})=>{
  const {result:r,runtimeErrors,failedRequests}=await completeAssessment(page,'max');
  expect(r.score).toBe(100);
  expect(r.contract).toBe('MAXESS_RESULT_V1');
  expect(r.responses).toBe(15);
  expect(r.frozen).toBe(true);
  expect(r.ready).toBe(1);
  expect(r.updated).toBe(1);
  expect(r.completionCount).toBe(1);
  const before=await page.evaluate(()=>window.MAXESS_E00_V2.getState().completionCount);
  await page.evaluate(()=>{
    const b=document.querySelector('#MAXESS-E00-V2 #mx-cont');
    b.dispatchEvent(new MouseEvent('click',{bubbles:true,cancelable:true}));
    b.dispatchEvent(new MouseEvent('click',{bubbles:true,cancelable:true}));
  });
  const after=await page.evaluate(()=>({count:window.MAXESS_E00_V2.getState().completionCount,score:window.MAXESS_RESULT.overallScore}));
  expect(after.count).toBe(before);
  expect(after.score).toBe(100);
  expect(failedRequests).toEqual([]);
  expect(runtimeErrors).toEqual([]);
});

test('MAXESS V2 required mobile widths remain usable', async ({page})=>{
  for(const width of [320,360,375,390,414,480,600,768,900,1024,1280]){
    await page.setViewportSize({width,height:900});
    const harness=buildHarness();
    await page.setContent(harness.html,{waitUntil:'domcontentloaded'});
    await page.addScriptTag({content:harness.engine});
    await page.addScriptTag({content:harness.definition});
    await page.addScriptTag({content:harness.runtime});
    await page.waitForFunction(()=>!!window.MAXESS_E00_V2);
    const overflow=await page.evaluate(()=>({
      body:document.documentElement.scrollWidth>document.documentElement.clientWidth+1,
      groove:document.querySelector('#MAXESS-E00-V2')?.scrollWidth>document.querySelector('#MAXESS-E00-V2')?.clientWidth+1,
      q:!!document.querySelector('#MAXESS-E00-V2 #mx-q'),
      answers:document.querySelectorAll('#MAXESS-E00-V2 .ans').length
    }));
    expect(overflow.body,`body overflow at ${width}px`).toBe(false);
    expect(overflow.groove,`Groove overflow at ${width}px`).toBe(false);
    expect(overflow.q).toBe(true);
    expect(overflow.answers).toBe(5);
  }
});