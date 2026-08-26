import { test, expect } from '@playwright/test';
import fs from 'node:fs';

function buildHarness(){
  const groove=fs.readFileSync('PROJECTS/MAXESS/E00 MAXESS V2 — AUTHORITATIVE GROOVE.html','utf8');
  const engine=fs.readFileSync('PROJECTS/MAXESS/ENGINEERING/MAXESS-E00-AUTHORITATIVE-ENGINE-V2.js','utf8');
  const definition=fs.readFileSync('PROJECTS/MAXESS/ENGINEERING/MAXESS-AI-SCORE-DEFINITION-V1.js','utf8');
  const consumer=fs.readFileSync('MAXESS-RESULT-CONSUMER-V2.html','utf8');
  const e01=fs.readFileSync('E01','utf8');
  const e01Styles=[...e01.matchAll(/<style[\\s\\S]*?<\\/style>/gi)].map(m=>m[0]).join('\\n');
  const e01Body=(e01.match(/<body[^>]*>([\\s\\S]*?)<\\/body>/i)||[, ''])[1];
  const localGroove=groove
    .replace(/<script src="https:\\/\\/raw\\.githubusercontent\\.com[^>]*MAXESS-E00-AUTHORITATIVE-ENGINE-V2\\.js"><\\/script>/i,`<script>${engine}<\\/script>`)
    .replace(/<script src="https:\\/\\/raw\\.githubusercontent\\.com[^>]*MAXESS-AI-SCORE-DEFINITION-V1\\.js"><\\/script>/i,`<script>${definition}<\\/script>`);
  return `<!doctype html><html><head><meta charset="utf-8">${e01Styles}</head><body>${localGroove}<div id="E01-HARNESS">${e01Body}</div>${consumer}</body></html>`;
}

async function completeAssessment(page, scoreMode){
  await page.goto('about:blank');
  await page.setContent(buildHarness(), {waitUntil:'domcontentloaded'});
  await page.evaluate(()=>{
    window.__MAXESS_TEST__={ready:0,updated:0,last:null};
    window.addEventListener('MAXESS_RESULT_READY',e=>{window.__MAXESS_TEST__.ready++;window.__MAXESS_TEST__.last=e.detail});
    window.addEventListener('maxess:result-updated',e=>{window.__MAXESS_TEST__.updated++});
  });
  await expect(page.locator('#MAXESS-E00-V2 #mx-q')).toContainText('');
  for(let qi=0;qi<15;qi++){
    const idx=await page.evaluate(({qi,scoreMode})=>{
      const q=window.MAXESS_AI_SCORE_DEFINITION_V1.questions[qi];
      const target=scoreMode==='min'?0:4;
      const i=q.answers.findIndex(a=>a.score===target);
      if(i<0)throw new Error(`No ${scoreMode} answer for Q${qi+1}`);
      return i;
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
    e01Score:document.querySelector('#e01 #score-number')?.textContent||null,
    released:window.MAXESS_RESULTS_RELEASED===true
  }));
  return result;
}

test('MAXESS V2 minimum golden browser path', async ({page})=>{
  const errors=[];
  page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
  page.on('pageerror',e=>errors.push(e.message));
  const r=await completeAssessment(page,'min');
  expect(r.score).toBe(0);
  expect(r.contract).toBe('MAXESS_RESULT_V1');
  expect(r.responses).toBe(15);
  expect(r.frozen).toBe(true);
  expect(r.ready).toBe(1);
  expect(r.updated).toBe(1);
  expect(r.completionCount).toBe(1);
  expect(r.released).toBe(true);
  expect(Number(r.e01Score)).toBe(0);
  expect(errors).toEqual([]);
});

test('MAXESS V2 maximum golden browser path and duplicate Continue guard', async ({page})=>{
  const errors=[];
  page.on('console',m=>{if(m.type()==='error')errors.push(m.text())});
  page.on('pageerror',e=>errors.push(e.message));
  const r=await completeAssessment(page,'max');
  expect(r.score).toBe(100);
  expect(r.contract).toBe('MAXESS_RESULT_V1');
  expect(r.responses).toBe(15);
  expect(r.frozen).toBe(true);
  expect(r.ready).toBe(1);
  expect(r.updated).toBe(1);
  expect(r.completionCount).toBe(1);
  const before=await page.evaluate(()=>window.MAXESS_E00_V2.getState().completionCount);
  await page.locator('#MAXESS-E00-V2 #mx-cont').click();
  await page.locator('#MAXESS-E00-V2 #mx-cont').click();
  const after=await page.evaluate(()=>({count:window.MAXESS_E00_V2.getState().completionCount,score:window.MAXESS_RESULT.overallScore}));
  expect(after.count).toBe(before);
  expect(after.score).toBe(100);
  expect(errors).toEqual([]);
});

test('MAXESS V2 required mobile widths remain usable', async ({page})=>{
  for(const width of [320,360,375,390,414,480,600,768,900,1024,1280]){
    await page.setViewportSize({width,height:900});
    await page.setContent(buildHarness(),{waitUntil:'domcontentloaded'});
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
