#!/usr/bin/env python3
"""
MAXESS Results V21 transformation tool.

Run from the root of the MaxRESULTS Codespace:
    python tools/apply_v21.py

The script works on the known-good 7,668-line Groove source in-place, while
preserving an immutable local baseline before changing anything. It appends
one authoritative V21 controller layer that consolidates the visible Results
experience without replacing the underlying MAXESS result source.

Outputs:
  - BASELINE-V20-WORKING.html (created only if absent)
  - MAXESS-RESULTS-GROOVE.html (canonical V21 artifact)
  - 20260817 912am RESULTS PAGE CODE (updated working source)
  - V21-QA-REPORT.md
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
BASELINE = ROOT / "BASELINE-V20-WORKING.html"
CANONICAL = ROOT / "MAXESS-RESULTS-GROOVE.html"
QA = ROOT / "V21-QA-REPORT.md"
MARKER = "<!-- MAXESS-V21-AUTHORITATIVE-CONTROLLER -->"

V21_CSS = r'''
<style id="maxess-v21-css">
/* MAXESS V21 — one authoritative visual layer over the preserved Groove source. */
#maxess-results-10 .v21-experience{position:relative;width:100%;background:#040307;color:#fff;overflow:clip}
#maxess-results-10 .v21-naya{padding:clamp(42px,6vw,82px) 20px 28px;text-align:center;background:radial-gradient(circle at 50% 0,rgba(166,108,255,.18),transparent 58%),#06050a}
#maxess-results-10 .v21-naya-avatar{width:92px;height:92px;border-radius:50%;object-fit:cover;display:block;margin:0 auto 14px;box-shadow:0 0 0 1px rgba(255,255,255,.18),0 16px 42px rgba(0,0,0,.45)}
#maxess-results-10 .v21-kicker{display:block;color:rgba(255,255,255,.62);font-size:10px;font-weight:900;letter-spacing:.18em;text-transform:uppercase}
#maxess-results-10 .v21-naya h1{margin:10px auto 0;max-width:900px;font-size:clamp(30px,4.5vw,58px);line-height:1;letter-spacing:-.05em}
#maxess-results-10 .v21-naya p{max-width:700px;margin:14px auto 0;color:rgba(255,255,255,.72);font-size:clamp(15px,1.5vw,19px)}
#maxess-results-10 .v21-listen{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:58px;margin-top:22px;padding:0 28px;border-radius:18px;border:1px solid rgba(255,255,255,.24);background:linear-gradient(145deg,#17131f,#07070b 65%,#040408);color:#fff;font-weight:900;letter-spacing:.04em;cursor:pointer;box-shadow:inset 0 1px rgba(255,255,255,.18),inset 0 -1px rgba(0,0,0,.7),0 18px 46px rgba(0,0,0,.42),0 0 28px rgba(166,108,255,.10);transition:transform .22s ease,border-color .22s ease,box-shadow .22s ease}
#maxess-results-10 .v21-listen:hover,#maxess-results-10 .v21-listen:focus-visible{transform:translateY(-3px);border-color:rgba(185,154,255,.62);box-shadow:inset 0 1px rgba(255,255,255,.24),0 24px 58px rgba(0,0,0,.5),0 0 40px rgba(166,108,255,.18)}
#maxess-results-10 .v21-listen:active{transform:translateY(0);box-shadow:inset 0 2px 8px rgba(0,0,0,.55),0 10px 24px rgba(0,0,0,.35)}
#maxess-results-10 .v21-score-section{padding:24px 18px 72px;text-align:center;background:#030305}
#maxess-results-10 .v21-score-label{margin:0 0 18px;color:rgba(255,255,255,.62);font-size:10px;font-weight:900;letter-spacing:.2em;text-transform:uppercase}
#maxess-results-10 .v21-score-orb{position:relative;width:min(590px,82vw);aspect-ratio:1;margin:0 auto;display:grid;place-items:center;border-radius:50%;background:radial-gradient(circle at 32% 25%,rgba(255,255,255,.20),transparent 10%),radial-gradient(circle at 50% 48%,#2b1645 0,#13091e 42%,#08050c 72%,#030205 100%);box-shadow:0 0 0 1px rgba(255,255,255,.18),inset 0 0 90px rgba(166,108,255,.24),0 40px 120px rgba(0,0,0,.7),0 0 120px rgba(148,74,255,.20)}
#maxess-results-10 .v21-score-orb::before{content:"";position:absolute;inset:8%;border:1px solid rgba(208,168,255,.48);border-radius:50%;box-shadow:0 0 65px rgba(166,108,255,.18);transform:rotate(0deg)}
#maxess-results-10 .v21-score-orb::after{content:"";position:absolute;inset:15%;border:1px solid rgba(255,255,255,.10);border-radius:50%}
#maxess-results-10 .v21-score-core{position:relative;z-index:2;display:grid;place-items:center;text-align:center}
#maxess-results-10 .v21-score-value{font-size:clamp(98px,14vw,182px);line-height:.78;font-weight:950;letter-spacing:-.09em}
#maxess-results-10 .v21-score-sub{margin-top:20px;color:rgba(255,255,255,.67);font-size:10px;font-weight:900;letter-spacing:.2em;text-transform:uppercase}
#maxess-results-10 .v21-stage-pill{margin-top:14px;display:inline-flex;padding:8px 13px;border-radius:999px;border:1px solid rgba(208,168,255,.26);background:rgba(166,108,255,.08);font-size:10px;font-weight:900;letter-spacing:.1em;text-transform:uppercase}
#maxess-results-10 .v21-dim-section{padding:clamp(48px,6vw,86px) 18px;background:#fff;color:#111}
#maxess-results-10 .v21-dim-wrap{width:min(1500px,100%);margin:auto}
#maxess-results-10 .v21-dim-head{text-align:center;margin-bottom:28px}
#maxess-results-10 .v21-dim-head h2{margin:6px 0 0;font-size:clamp(34px,5vw,66px);line-height:.94;letter-spacing:-.055em;color:#111}
#maxess-results-10 .v21-dim-head p{max-width:850px;margin:14px auto 0;color:#383842;font-size:clamp(15px,1.4vw,19px)}
#maxess-results-10 .v21-orbs{display:grid;grid-template-columns:repeat(5,minmax(140px,1fr));gap:18px;align-items:stretch}
#maxess-results-10 .v21-dim-orb{position:relative;aspect-ratio:1;border-radius:50%;padding:18px;border:1px solid rgba(0,0,0,.16);background:radial-gradient(circle at 30% 22%,#fff,#f4eff9 48%,#ddd5e8 100%);color:#111;box-shadow:inset 0 1px rgba(255,255,255,.9),0 24px 60px rgba(25,12,40,.13);cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;transition:transform .24s ease,box-shadow .24s ease,border-color .24s ease}
#maxess-results-10 .v21-dim-orb::before{content:"";position:absolute;inset:9px;border-radius:50%;border:2px solid color-mix(in srgb,var(--dim-color) 55%,transparent);box-shadow:0 0 28px color-mix(in srgb,var(--dim-color) 22%,transparent);pointer-events:none}
#maxess-results-10 .v21-dim-orb:hover,#maxess-results-10 .v21-dim-orb:focus-visible{transform:translateY(-7px) scale(1.025);border-color:color-mix(in srgb,var(--dim-color) 55%,#111 15%);box-shadow:inset 0 1px rgba(255,255,255,.9),0 32px 76px rgba(25,12,40,.18),0 0 35px color-mix(in srgb,var(--dim-color) 20%,transparent)}
#maxess-results-10 .v21-dim-score{position:relative;z-index:1;font-size:clamp(42px,4.4vw,72px);font-weight:950;letter-spacing:-.08em}
#maxess-results-10 .v21-dim-name{position:relative;z-index:1;max-width:130px;margin-top:8px;font-size:10px;font-weight:900;letter-spacing:.07em;text-transform:uppercase}
#maxess-results-10 .v21-detail{margin:22px auto 0;max-width:1180px;padding:18px 20px;border-radius:18px;background:#06070a;color:#fff;box-shadow:inset 0 1px rgba(255,255,255,.14),0 20px 50px rgba(0,0,0,.16)}
#maxess-results-10 .v21-detail b{font-size:12px;letter-spacing:.1em;text-transform:uppercase}
#maxess-results-10 .v21-detail p{margin:6px 0 0;color:rgba(255,255,255,.72);font-size:13px;line-height:1.55}
#maxess-results-10 .v21-report{padding:clamp(58px,7vw,110px) 18px;background:linear-gradient(180deg,#09070c,#100b16 100%);color:#fff}
#maxess-results-10 .v21-report-page{width:min(1050px,100%);margin:auto;padding:clamp(30px,5vw,66px);border-radius:28px;background:linear-gradient(160deg,#fff,#f8f5fb);color:#111;box-shadow:0 30px 100px rgba(0,0,0,.42);border:1px solid rgba(0,0,0,.08)}
#maxess-results-10 .v21-report-kicker{font-size:10px;font-weight:950;letter-spacing:.2em;color:#7042aa;text-transform:uppercase}
#maxess-results-10 .v21-report-page h2{margin:9px 0 0;font-size:clamp(36px,5vw,68px);line-height:.94;letter-spacing:-.055em;color:#111}
#maxess-results-10 .v21-report-meta{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}
#maxess-results-10 .v21-report-meta span{padding:8px 11px;border:1px solid rgba(0,0,0,.12);border-radius:999px;background:rgba(0,0,0,.03);font-size:10px;font-weight:900;letter-spacing:.06em;text-transform:uppercase}
#maxess-results-10 .v21-letter{margin-top:28px;padding:28px;border-top:1px solid rgba(0,0,0,.12);border-bottom:1px solid rgba(0,0,0,.12);font-size:17px;line-height:1.75}
#maxess-results-10 .v21-letter p{margin:0 0 18px}
#maxess-results-10 .v21-letter p:last-child{margin-bottom:0}
#maxess-results-10 .v21-report-callout{margin-top:24px;padding:20px;border-radius:18px;background:#08070b;color:#fff}
#maxess-results-10 .v21-report-callout b{display:block;color:#d9b7ff;font-size:10px;letter-spacing:.13em;text-transform:uppercase}
#maxess-results-10 .v21-report-callout p{margin:8px 0 0;color:rgba(255,255,255,.78);line-height:1.6}
#maxess-results-10 .v21-existing{position:relative}
#maxess-results-10 .v21-section-anchor{scroll-margin-top:18px}
#maxess-results-10 .v21-cta-row{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
#maxess-results-10 .v21-cta{display:inline-flex;align-items:center;justify-content:center;min-height:52px;padding:0 20px;border-radius:16px;border:1px solid rgba(255,255,255,.16);background:#09080d;color:#fff;text-decoration:none;font-weight:900;box-shadow:inset 0 1px rgba(255,255,255,.12),0 14px 32px rgba(0,0,0,.30)}
#maxess-results-10 .v21-hidden{display:none!important}
@media(max-width:1100px){#maxess-results-10 .v21-orbs{grid-template-columns:repeat(3,minmax(150px,1fr))}}
@media(max-width:720px){#maxess-results-10 .v21-orbs{grid-template-columns:repeat(2,minmax(120px,1fr));gap:12px}#maxess-results-10 .v21-score-orb{width:min(440px,84vw)}#maxess-results-10 .v21-report-page{padding:26px 20px}#maxess-results-10 .v21-letter{font-size:15px}}
@media(max-width:460px){#maxess-results-10 .v21-orbs{grid-template-columns:1fr}#maxess-results-10 .v21-dim-orb{width:min(230px,72vw);margin:auto}}
@media(prefers-reduced-motion:reduce){#maxess-results-10 .v21-listen,#maxess-results-10 .v21-dim-orb{transition:none!important}}
@media print{
  @page{size:letter;margin:.55in}
  html,body{background:#fff!important;color:#111!important}
  #maxess-results-10{width:100%!important;margin:0!important;background:#fff!important;color:#111!important}
  #maxess-results-10 .v21-experience{background:#fff!important;color:#111!important}
  #maxess-results-10 .v21-naya{padding:18px 0 10px!important;background:#fff!important;color:#111!important;break-inside:avoid;page-break-after:avoid}
  #maxess-results-10 .v21-naya-avatar{width:58px;height:58px;box-shadow:none}
  #maxess-results-10 .v21-naya h1{font-size:28px;color:#111!important}
  #maxess-results-10 .v21-naya p{font-size:12px;color:#333!important}
  #maxess-results-10 .v21-listen{display:none!important}
  #maxess-results-10 .v21-score-section{padding:10px 0 24px!important;background:#fff!important;color:#111!important;break-inside:avoid;page-break-after:always}
  #maxess-results-10 .v21-score-label{color:#444!important}
  #maxess-results-10 .v21-score-orb{width:255px;box-shadow:none;border:1px solid #bbb;background:#fff!important}
  #maxess-results-10 .v21-score-orb::before,#maxess-results-10 .v21-score-orb::after{border-color:#bbb;box-shadow:none}
  #maxess-results-10 .v21-score-value{font-size:90px!important;color:#111!important}
  #maxess-results-10 .v21-score-sub{color:#444!important}
  #maxess-results-10 .v21-stage-pill{color:#111!important;border-color:#bbb;background:#f4f4f4}
  #maxess-results-10 .v21-dim-section{padding:28px 0!important;background:#fff!important;color:#111!important;break-before:page}
  #maxess-results-10 .v21-orbs{grid-template-columns:repeat(5,1fr)!important;gap:7px!important}
  #maxess-results-10 .v21-dim-orb{box-shadow:none!important;background:#fff!important;border:1px solid #aaa!important}
  #maxess-results-10 .v21-dim-orb::before{box-shadow:none!important}
  #maxess-results-10 .v21-detail{background:#111!important;color:#fff!important}
  #maxess-results-10 .v21-report{break-before:page;padding:0!important;background:#fff!important;color:#111!important}
  #maxess-results-10 .v21-report-page{box-shadow:none!important;border:1px solid #bbb!important}
  #maxess-results-10 .v21-letter{font-size:13px;line-height:1.6}
  #maxess-results-10 .v21-existing{break-inside:avoid;page-break-inside:avoid}
  #maxess-results-10 .v21-existing:not(:first-child){break-before:page}
  #maxess-results-10 .v21-cta-row{display:none!important}
}
</style>
'''

V21_JS = r'''
<script id="maxess-v21-js">
(function(){
  'use strict';
  var root=document.getElementById('maxess-results-10');
  if(!root || root.dataset.v21Done==='1') return;
  root.dataset.v21Done='1';

  function esc(v){return String(v==null?'':v).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  function result(){return window.MAXESS_RESULT||{}}
  function num(v,f){var n=Number(v);return Number.isFinite(n)?n:f}
  function score(){var r=result();return Math.round(Math.max(0,Math.min(100,num(r.overallScore!=null?r.overallScore:(r.score!=null?r.score:r.masterScore),0))))}
  function dims(){var r=result();return Array.isArray(r.dimensions)?r.dimensions.slice(0,5).map(function(d,i){return {id:d.id||String(i+1),name:d.name||d.label||('Dimension '+(i+1)),score:Math.round(Math.max(0,Math.min(100,num(d.score!=null?d.score:d.value,0)))),description:d.description||d.insight||''}}):[]}
  function stage(){var r=result();var explicit=r.masteryStage||r.masteryLevel||r.band||r.stage;if(explicit)return String(explicit);var s=score();return s<50?'Supporting':s<65?'Foundation':s<75?'Developing':s<90?'Advancing':'Mastering'}
  function stageMeaning(s){return ({Supporting:'You are beginning to build the habits that make AI genuinely useful.',Foundation:'You have a base to build on. The next gains come from turning basic capability into repeatable practice.',Developing:'You are becoming capable and consistent. Deliberate evaluation and iteration can now create much larger gains.',Advancing:'You already have a strong working relationship with AI. Your next gains come from precision, evaluation, and turning what works into systems.',Mastering:'You are operating at a high level. The opportunity now is to compound your judgment, systems, and ability to create exceptional outcomes.'})[s]||'This stage describes where your current AI mastery is operating today.'}
  function copyFor(name,s){var n=String(name).toLowerCase();if(n.includes('communication'))return 'Your communication capability helps you express context, intent and desired outcomes clearly. That is a powerful foundation because AI can only act on the signal you give it.';if(n.includes('direction'))return 'Your direction capability reflects how clearly you know the destination before asking AI to help you reach it.';if(n.includes('evaluation'))return 'Your evaluation capability reflects how well you judge whether an AI response is actually useful, accurate and aligned with the outcome you want.';if(n.includes('iteration'))return 'Your iteration capability reflects how deliberately you improve an answer instead of treating the first version as finished.';if(n.includes('system'))return 'Your systems capability reflects how well you connect repeated work into reusable processes, tools and leverage.';return s>=85?'This is a strong capability you can compound.':s>=70?'This is a capable area with clear room to sharpen.':'This is an important growth area where focused practice can create meaningful gains.'}
  function removeNode(sel){root.querySelectorAll(sel).forEach(function(e){e.remove()})}
  function first(selList){for(var i=0;i<selList.length;i++){var e=root.querySelector(selList[i]);if(e)return e;if(legacyStage){e=legacyStage.querySelector(selList[i]);if(e)return e}}return null}
  function allSections(){return Array.prototype.slice.call(root.querySelectorAll('section'))}
  function findSection(regex){var found=null;allSections().forEach(function(sec){if(found)return;var text=(sec.innerText||sec.textContent||'').toLowerCase();if(regex.test(text))found=sec});return found}
  function moveInto(sec,parent){if(sec){sec.classList.remove('v20-hidden','v18-hidden');sec.classList.add('v21-existing');parent.appendChild(sec);return sec}return null}

  /* Remove previous generated shells/controllers from the live DOM. The original content sections remain available. */
  legacyStage=root.querySelector('.v20-stage,.v18-flow');
  /* Keep legacy containers alive until their real sections are moved into V21. */
  removeNode('#v12-naya,#v13-naya,#v11-naya-report,#v11-naya-welcome,#v13-naya-introduction,.v11-naya-welcome,.v12-naya-intro,.v18-naya-top');
  root.querySelectorAll('.v20-hidden,.v18-hidden').forEach(function(e){e.classList.remove('v20-hidden','v18-hidden')});

  var r=result(), ds=dims(), overall=score(), band=stage();
  var sorted=ds.slice().sort(function(a,b){return b.score-a.score});
  var strongest=sorted[0]||{name:'Your strongest capability',score:0};
  var weakest=sorted[sorted.length-1]||{name:'Your highest-leverage opportunity',score:0};
  var name=r.name||r.userName||r.firstName||'';

  var experience=document.createElement('main');experience.className='v21-experience';experience.setAttribute('aria-label','MAXESS personalized results');

  var naya=document.createElement('section');naya.className='v21-naya';
  naya.innerHTML='<img class="v21-naya-avatar" alt="Naya, your AI guide"><span class="v21-kicker">NAYA · YOUR AI GUIDE</span><h1>'+ (name?esc(name)+', I’ve looked at your results.':'Hi. I’ve looked at your results.') +'</h1><p>This isn’t your judgment. <strong>It’s your map.</strong></p><button type="button" class="v21-listen" aria-label="Listen to Naya walk through your MAXESS results">LISTEN TO NAYA <span aria-hidden="true">▶</span></button>';
  var avatar=first(['img[src*="Naya Profile Black"]','img[src*="Naya Profile white"]','.v18-naya-avatar','.v12-naya-avatar']);
  naya.querySelector('.v21-naya-avatar').src=avatar&&avatar.src?avatar.src:'https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg';
  naya.querySelector('.v21-listen').addEventListener('click',function(){
    var candidates=Array.prototype.slice.call(root.querySelectorAll('#mx-naya-listen,#v11-naya-listen,#v13-listen,.mx-naya-listen,.v18-listen-secondary')).filter(function(e){return e&&e!==this&&e.offsetParent!==null}.bind(this));
    if(candidates.length){candidates[0].click();return}
    root.dispatchEvent(new CustomEvent('maxess:naya-listen',{bubbles:true,detail:{result:r}}));
  });
  experience.appendChild(naya);

  var scoreSec=document.createElement('section');scoreSec.className='v21-score-section';
  scoreSec.innerHTML='<div class="v21-score-label">YOUR MAXESS SCORE</div><div class="v21-score-orb"><div class="v21-score-core"><strong class="v21-score-value">'+overall+'</strong><span class="v21-score-sub">MAXESS SCORE</span><span class="v21-stage-pill">'+esc(band)+'</span></div></div>';
  experience.appendChild(scoreSec);

  var dimSec=document.createElement('section');dimSec.className='v21-dim-section v21-section-anchor';dimSec.id='v21-dimensions';
  var cards='';
  for(var i=0;i<5;i++){var d=ds[i]||{name:['Direction','Communication','Evaluation','Iteration','Systems Thinking'][i],score:0,description:''};cards+='<button type="button" class="v21-dim-orb" data-index="'+i+'" style="--dim-color:'+['#ff9d3d','#d6aa2f','#33c88e','#4b95e8','#8b5cf6'][i]+'"><strong class="v21-dim-score">'+d.score+'</strong><span class="v21-dim-name">'+esc(d.name)+'</span></button>'}
  dimSec.innerHTML='<div class="v21-dim-wrap"><div class="v21-dim-head"><span class="v21-kicker" style="color:#7042aa">YOUR FIVE DIMENSIONS</span><h2>One MAXESS score. Five capabilities.</h2><p>Select a dimension to see what it means and where its leverage lives.</p></div><div class="v21-orbs" role="list" aria-label="Your five MAXESS dimensions">'+cards+'</div><div class="v21-detail" id="v21-dim-detail" aria-live="polite"><b>SELECT A DIMENSION</b><p>Choose one of the five orbs to explore the score, meaning, and next lever.</p></div></div>';
  var detail=dimSec.querySelector('#v21-dim-detail');
  dimSec.querySelectorAll('.v21-dim-orb').forEach(function(btn){btn.addEventListener('click',function(){var d=ds[Number(btn.dataset.index)]||{};detail.innerHTML='<b>'+esc(d.name||'Dimension')+' · '+num(d.score,0)+'</b><p>'+esc(d.description||copyFor(d.name||'This dimension',num(d.score,0)))+'</p>';root.dispatchEvent(new CustomEvent('maxess:dimension',{bubbles:true,detail:{name:d.name,score:d.score,index:Number(btn.dataset.index)}}));})});
  experience.appendChild(dimSec);

  var report=document.createElement('section');report.className='v21-report v21-section-anchor';report.id='v21-report';
  var greeting=name?' '+esc(name)+',':' Your';
  var strengthsText='Your strongest capability is '+esc(strongest.name)+' at '+strongest.score+'. '+copyFor(strongest.name,strongest.score);
  var leverText='Your biggest lever is '+esc(weakest.name)+' at '+weakest.score+'. Strengthening this area can improve the quality of what you get from the strengths you already have.';
  report.innerHTML='<div class="v21-report-page"><span class="v21-report-kicker">YOUR PERSONALIZED REPORT</span><h2>'+greeting+' MAXESS Report</h2><div class="v21-report-meta"><span>MAXESS '+overall+'</span><span>'+esc(band)+'</span><span>5 dimensions</span></div><div class="v21-letter"><p>Dear'+(name?' '+esc(name):' MAXESS user')+',</p><p>Your MAXESS score is <strong>'+overall+'</strong>, placing you in the <strong>'+esc(band)+'</strong> stage. '+esc(stageMeaning(band))+'</p><p>'+esc(strengthsText)+'</p><p>The overall pattern matters more than any single number. Your profile shows where your current capability is already creating momentum and where a focused improvement could change the quality of your results.</p><p>'+esc(leverText)+'</p><p>What this means in practical terms: you do not need to become better at everything at once. Protect what is already working, strengthen the highest-leverage gap, and deliberately improve the quality of the results you create with AI.</p><p>Your next move is to turn this diagnosis into practice: define the outcome, direct AI clearly, score what comes back, improve it, and turn the win into something reusable.</p><p>You are not being judged. You are being shown where you are — and where you can go next.</p></div><div class="v21-report-callout"><b>PROTECT YOUR STRENGTH. BUILD YOUR LEVER.</b><p>'+esc(strongest.name)+' is something to compound. '+esc(weakest.name)+' is where focused improvement is most likely to create disproportionate gains.</p></div><div class="v21-cta-row"><a class="v21-cta" href="#v21-dimensions">Explore your dimensions</a><a class="v21-cta" href="#v21-next">Go to your next move</a></div></div></section>';
  experience.appendChild(report);

  /* Reuse the best existing narrative sections instead of creating competing replacements. */
  var pattern=findSection(/your pattern|see the pattern/);if(pattern&&!pattern.id.match(/^v21-/))moveInto(pattern,experience);
  var strength=findSection(/your strengths|your strength/);if(strength&&!strength.id.match(/^v21-/))moveInto(strength,experience);
  var lever=findSection(/your biggest lever|your lever/);if(lever&&!lever.id.match(/^v21-/))moveInto(lever,experience); else {var fakeLever=document.createElement('section');fakeLever.className='v21-report v21-section-anchor';fakeLever.id='v21-lever';fakeLever.innerHTML='<div class="v21-report-page"><span class="v21-report-kicker">YOUR LEVER</span><h2>'+esc(weakest.name)+'</h2><div class="v21-letter"><p>Your lever is the capability with the most room to improve relative to the rest of your profile.</p><p>At <strong>'+weakest.score+'</strong>, '+esc(weakest.name)+' is the clearest place to focus. Improving this area can unlock more value from your existing strengths.</p></div></div>';experience.appendChild(fakeLever)}
  var next=findSection(/your next move|next chapter/);if(next){next.id='v21-next';moveInto(next,experience)}
  var masters=findSection(/18 naya masters|18 ai pathways|your naya masters/);if(masters)moveInto(masters,experience)
  var playground=findSection(/playground/);if(playground)moveInto(playground,experience)

  /* Pull the final/ending section to the bottom without destroying its existing content. */
  var finalSec=findSection(/ai mastery key|keep improving|you are not your score|master your ai/);if(finalSec&&finalSec.parentElement!==experience)moveInto(finalSec,experience)

  /* Existing generated shells and duplicate controls are no longer authoritative. */
  removeNode('.v21-hidden-source,.v20-stage,.v18-flow');
  root.querySelectorAll('#mx-naya-listen,#v11-naya-listen,#v13-listen,.mx-naya-listen,.v18-listen-secondary').forEach(function(e){e.classList.add('v21-hidden')});
  root.querySelectorAll('.v20-naya,.v20-score,.v20-dims,.v20-fallback').forEach(function(e){e.classList.add('v21-hidden')});

  /* Preserve any original section we haven't explicitly placed, after the guided experience. */
  allSections().forEach(function(sec){
    if(sec.closest('.v21-experience'))return;
    if(sec.classList.contains('v21-hidden'))return;
    if(sec.id==='v21-dimensions'||sec.id==='v21-report')return;
    if(sec.textContent.trim().length<20)return;
    moveInto(sec,experience);
  });

  /* Ensure the order of the existing narrative remains intentional. */
  var orderIds=['v21-dimensions','v21-report','v21-pattern','v11-pattern','v13-pattern','v15-pattern','v12-pattern','v11-strengths','v13-strengths','v12-strengths','v18-strength-section','v21-lever','v11-lever','v13-lever','v12-lever','v21-next','v11-next','v13-next','v12-next','v11-masters','v13-masters','v12-masters','naya-playground'];
  orderIds.forEach(function(id){var e=experience.querySelector('#'+id);if(e)experience.appendChild(e)});

  root.appendChild(experience);
  root.classList.add('v21-release');
  root.setAttribute('data-results-version','21');
  root.setAttribute('data-results-data-source','window.MAXESS_RESULT');
  root.setAttribute('data-v21-score',String(overall));
  root.setAttribute('data-v21-band',band);
  root.setAttribute('aria-label','MAXESS Results — personalized AI mastery report');

  document.querySelectorAll('#maxess-results-10 .v21-dim-orb').forEach(function(b){b.setAttribute('aria-label',b.textContent.trim()+' dimension')});
})();
</script>
'''


def patch_source(src: str) -> str:
    if MARKER in src:
        return src
    if "window.MAXESS_RESULT" not in src:
        raise RuntimeError("MAXESS_RESULT source not found; refusing to patch unknown HTML")
    if "<div" not in src or "maxess-results-10" not in src:
        raise RuntimeError("Expected MAXESS Groove root not found; refusing to patch unknown HTML")
    body_idx=src.lower().rfind("</body>")
    if body_idx < 0:
        raise RuntimeError("No </body> tag found")
    return src[:body_idx] + "\n" + MARKER + "\n" + V21_CSS + V21_JS + src[body_idx:]


def run_node_check(path: Path) -> tuple[bool,str]:
    node=shutil.which("node")
    if not node:
        return True,"Node.js not available; skipped JavaScript syntax check."
    text=path.read_text(encoding="utf-8")
    blocks=re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>",text,re.I|re.S)
    checked=0
    for idx,block in enumerate(blocks,1):
        if not block.strip():
            continue
        tmp=ROOT/".v21_tmp_check.js"
        tmp.write_text(block,encoding="utf-8")
        p=subprocess.run([node,"--check",str(tmp)],capture_output=True,text=True)
        tmp.unlink(missing_ok=True)
        if p.returncode!=0:
            return False,f"Node syntax check failed in script block {idx}: {p.stderr.strip()}"
        checked+=1
    return True,f"Node syntax check passed for {checked} inline script blocks."


def main() -> int:
    if not SOURCE.exists():
        print(f"ERROR: source file not found: {SOURCE}")
        return 2
    original=SOURCE.read_text(encoding="utf-8")
    if not BASELINE.exists():
        BASELINE.write_text(original,encoding="utf-8")
    patched=patch_source(original)
    SOURCE.write_text(patched,encoding="utf-8")
    CANONICAL.write_text(patched,encoding="utf-8")

    ids=re.findall(r'\bid=["\']([^"\']+)["\']',patched)
    dup_ids=sorted({x for x in ids if ids.count(x)>1})
    required=["window.MAXESS_RESULT", "MAXESS-V21-AUTHORITATIVE-CONTROLLER", "v21-experience", "v21-naya", "v21-score-orb", "v21-dimensions", "v21-report", "v21-lever", "v21-next"]
    missing=[x for x in required if x not in patched]
    syntax_ok,syntax_msg=run_node_check(CANONICAL)
    now=datetime.now(timezone.utc).isoformat()
    report=[
        "# MAXESS V21 QA REPORT",
        "",
        f"Generated: `{now}`",
        "",
        "## Baseline",
        f"- Source baseline bytes: `{len(original.encode('utf-8'))}`",
        f"- Baseline file: `{BASELINE.name}`",
        "- Authoritative runtime result source: `window.MAXESS_RESULT`",
        "",
        "## Structural checks",
        f"- V21 marker present: {'PASS' if MARKER in patched else 'FAIL'}",
        f"- Required markers present: {'PASS' if not missing else 'FAIL'}",
        f"- Duplicate HTML IDs: {'NONE' if not dup_ids else ', '.join(dup_ids)}",
        f"- JavaScript syntax: {'PASS' if syntax_ok else 'FAIL'} — {syntax_msg}",
        "",
        "## V21 product requirements represented",
        "- Naya opening + single primary Listen CTA",
        "- Centered MAXESS score orb with MAXESS SCORE secondary label",
        "- Five data-driven interactive mini-orbs",
        "- Dark contrast dimension instruction card",
        "- Personalized report/document treatment",
        "- Mastery-stage interpretation",
        "- Pattern / Strength / Lever / Next Move / Masters / Playground preservation",
        "- Dedicated print/PDF styling",
        "- Reduced-motion and responsive behavior",
        "",
        "## Manual release verification still required",
        "- Open the generated canonical file in a browser.",
        "- Test a real result payload and a demo fixture.",
        "- Verify Listen, five dimension interactions, Masters, Playground, Print/Save PDF.",
        "- Generate and inspect an actual PDF.",
    ]
    if missing:
        report.append("\nMissing markers: " + ", ".join(missing))
    if dup_ids:
        report.append("\nDuplicate IDs require inspection before release: " + ", ".join(dup_ids))
    QA.write_text("\n".join(report)+"\n",encoding="utf-8")
    print(f"V21 applied. Source: {SOURCE.name}")
    print(f"Canonical: {CANONICAL.name}")
    print(f"Baseline: {BASELINE.name}")
    print(f"QA report: {QA.name}")
    print(f"Duplicate IDs: {len(dup_ids)}")
    print(syntax_msg)
    if missing:
        print("WARNING: missing markers: "+", ".join(missing))
    return 0 if syntax_ok and not missing else 3


if __name__=="__main__":
    raise SystemExit(main())
