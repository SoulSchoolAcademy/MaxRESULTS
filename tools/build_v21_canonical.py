#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import hashlib
import importlib.util
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BASELINE = ROOT / "BASELINE-WORKING.html"
SOURCE = ROOT / "20260817 912am RESULTS PAGE CODE"
REPORT = ROOT / "V21-CANONICAL-BUILD-RESULT.md"
MARKER = 'id="maxess-results-v21-canonical-js"'

CSS = """
<style id="maxess-results-v21-canonical-css">
#maxess-results-10.v21-canonical{--v21-bg:#050307;--v21-white:#fff;--v21-black:#09070b;--v21-purple:#9b63ff;--v21-purple2:#5f2eb5;--v21-muted:rgba(255,255,255,.68);background:#050307!important;color:#fff!important}
#maxess-results-10.v21-canonical *{box-sizing:border-box}
#maxess-results-10.v21-canonical .v21-shell{width:100%;overflow:hidden}
#maxess-results-10.v21-canonical .v21-section{width:100%;padding:clamp(58px,8vw,110px) 20px}
#maxess-results-10.v21-canonical .v21-inner{width:min(1180px,100%);margin:auto}
#maxess-results-10.v21-canonical .v21-dark{background:linear-gradient(180deg,#050307,#09050f);color:#fff}
#maxess-results-10.v21-canonical .v21-light{background:linear-gradient(180deg,#fbfbfd,#fff);color:#111}
#maxess-results-10.v21-canonical .v21-purple{background:linear-gradient(145deg,#2a0d4d,#5d2ba8 48%,#8d58eb);color:#fff}
#maxess-results-10.v21-canonical .v21-kicker{font-size:10px;font-weight:950;letter-spacing:.18em;text-transform:uppercase;color:#caa8ff}
#maxess-results-10.v21-canonical h1,#maxess-results-10.v21-canonical h2,#maxess-results-10.v21-canonical h3{margin:0;letter-spacing:-.05em}
#maxess-results-10.v21-canonical p{line-height:1.65}
#maxess-results-10.v21-canonical .v21-naya{display:grid;grid-template-columns:auto 1fr auto;gap:20px;align-items:center;max-width:1040px;margin:auto;padding:22px;border:1px solid rgba(255,255,255,.14);border-radius:28px;background:linear-gradient(135deg,rgba(255,255,255,.07),rgba(155,99,255,.10));box-shadow:0 24px 70px rgba(0,0,0,.32),inset 0 1px rgba(255,255,255,.12)}
#maxess-results-10.v21-canonical .v21-avatar{width:74px;height:74px;border-radius:50%;object-fit:cover;border:1px solid rgba(255,255,255,.25);box-shadow:0 0 0 5px rgba(155,99,255,.12),0 16px 34px rgba(0,0,0,.35)}
#maxess-results-10.v21-canonical .v21-naya-title{font-size:clamp(24px,3vw,38px);font-weight:900}
#maxess-results-10.v21-canonical .v21-naya-sub{margin:8px 0 0;color:rgba(255,255,255,.72);max-width:700px}
#maxess-results-10.v21-canonical .v21-listen{appearance:none;border:1px solid #b990ff;border-radius:18px;min-height:56px;padding:0 22px;background:#050507;color:#fff;font-weight:950;letter-spacing:.04em;box-shadow:inset 0 0 0 1px rgba(255,255,255,.10),0 12px 28px rgba(0,0,0,.38);cursor:pointer;transition:transform .18s ease,box-shadow .18s ease,border-color .18s ease}
#maxess-results-10.v21-canonical .v21-listen:hover{transform:translateY(-2px);box-shadow:inset 0 0 0 1px rgba(255,255,255,.15),0 18px 38px rgba(0,0,0,.48)}
#maxess-results-10.v21-canonical .v21-listen:focus-visible{outline:2px solid #fff;outline-offset:4px}
#maxess-results-10.v21-canonical .v21-score-wrap{text-align:center}
#maxess-results-10.v21-canonical .v21-score-orb{width:min(510px,78vw);aspect-ratio:1;border-radius:50%;margin:0 auto;display:grid;place-items:center;position:relative;background:radial-gradient(circle at 34% 24%,rgba(255,255,255,.20),transparent 12%),radial-gradient(circle at 50% 52%,rgba(155,99,255,.20),transparent 50%),#09070d;border:1px solid rgba(255,255,255,.18);box-shadow:inset 0 0 90px rgba(155,99,255,.18),0 45px 110px rgba(0,0,0,.55),0 0 110px rgba(155,99,255,.15)}
#maxess-results-10.v21-canonical .v21-score-orb::before{content:"";position:absolute;inset:10px;border-radius:50%;border:1px solid rgba(255,255,255,.16);box-shadow:0 0 50px rgba(155,99,255,.12)}
#maxess-results-10.v21-canonical .v21-score-number{font-size:clamp(94px,13vw,170px);font-weight:950;line-height:.78;letter-spacing:-.09em}
#maxess-results-10.v21-canonical .v21-score-label{margin-top:18px;font-size:10px;font-weight:950;letter-spacing:.20em;color:#d2b6ff;text-transform:uppercase}
#maxess-results-10.v21-canonical .v21-stage{display:inline-flex;margin-top:18px;padding:10px 14px;border-radius:999px;background:#120a18;border:1px solid rgba(202,168,255,.30);font-size:10px;font-weight:950;letter-spacing:.14em;text-transform:uppercase}
#maxess-results-10.v21-canonical .v21-section-title{font-size:clamp(36px,5vw,72px);line-height:.94}
#maxess-results-10.v21-canonical .v21-section-copy{max-width:760px;margin:15px 0 0;color:var(--v21-muted);font-size:16px}
#maxess-results-10.v21-canonical .v21-light .v21-section-copy{color:#58535f}
#maxess-results-10.v21-canonical .v21-dims{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:16px;margin-top:28px}
#maxess-results-10.v21-canonical .v21-dim{appearance:none;min-height:214px;border-radius:50%;padding:26px 20px;display:grid;place-items:center;align-content:center;text-align:center;border:1px solid rgba(20,15,30,.14);background:radial-gradient(circle at 34% 24%,rgba(255,255,255,.9),transparent 13%),radial-gradient(circle at 50% 52%,rgba(155,99,255,.16),transparent 52%),#faf9fd;color:#111;box-shadow:inset 0 0 0 1px rgba(255,255,255,.60),0 22px 50px rgba(30,15,50,.12);cursor:pointer;transition:.2s ease}
#maxess-results-10.v21-canonical .v21-dim:hover,#maxess-results-10.v21-canonical .v21-dim:focus-visible{transform:translateY(-5px);border-color:rgba(125,73,193,.45);box-shadow:0 28px 60px rgba(30,15,50,.18)}
#maxess-results-10.v21-canonical .v21-dim-score{font-size:56px;font-weight:950;line-height:.8;letter-spacing:-.07em}
#maxess-results-10.v21-canonical .v21-dim-name{margin-top:14px;font-size:10px;font-weight:950;letter-spacing:.11em;text-transform:uppercase;color:#7141ad}
#maxess-results-10.v21-canonical .v21-detail{margin-top:18px;padding:20px 22px;border-radius:18px;background:#09070d;color:#fff;border:1px solid rgba(155,99,255,.22)}
#maxess-results-10.v21-canonical .v21-detail b{display:block;color:#cfadff;font-size:11px;letter-spacing:.14em;text-transform:uppercase}
#maxess-results-10.v21-canonical .v21-detail p{margin:8px 0 0;color:rgba(255,255,255,.72)}
#maxess-results-10.v21-canonical .v21-report{margin-top:28px;padding:clamp(30px,5vw,64px);border-radius:34px;background:linear-gradient(135deg,#fff,#f4f0f9);color:#17131d;border:1px solid rgba(25,15,35,.10);box-shadow:0 30px 90px rgba(20,10,40,.12)}
#maxess-results-10.v21-canonical .v21-report-mark{width:58px;height:8px;border-radius:999px;background:linear-gradient(90deg,#5f2eb5,#b990ff)}
#maxess-results-10.v21-canonical .v21-report h2{margin-top:18px;font-size:clamp(38px,5vw,72px)}
#maxess-results-10.v21-canonical .v21-report p{max-width:820px;margin:16px 0 0;color:#4d4754;font-size:17px}
#maxess-results-10.v21-canonical .v21-report-stage{display:inline-flex;margin-top:16px;padding:9px 13px;border-radius:999px;background:#120a18;color:#fff;font-size:10px;font-weight:950;letter-spacing:.12em;text-transform:uppercase}
#maxess-results-10.v21-canonical .v21-report-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-top:28px}
#maxess-results-10.v21-canonical .v21-cell{padding:18px;border-radius:18px;background:rgba(255,255,255,.72);border:1px solid rgba(25,15,35,.10)}
#maxess-results-10.v21-canonical .v21-cell span{display:block;font-size:9px;font-weight:950;letter-spacing:.14em;color:#7445ad}
#maxess-results-10.v21-canonical .v21-cell b{display:block;margin-top:7px;font-size:15px}
#maxess-results-10.v21-canonical .v21-cell small{display:block;margin-top:5px;color:#6a6470;line-height:1.45}
#maxess-results-10.v21-canonical .v21-story{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:stretch;margin-top:30px}
#maxess-results-10.v21-canonical .v21-card{border-radius:28px;padding:30px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);box-shadow:0 22px 65px rgba(0,0,0,.22)}
#maxess-results-10.v21-canonical .v21-light .v21-card{background:#fff;border-color:rgba(20,15,30,.09);box-shadow:0 22px 65px rgba(20,15,30,.10)}
#maxess-results-10.v21-canonical .v21-card h3{font-size:clamp(28px,3vw,46px)}
#maxess-results-10.v21-canonical .v21-card p{margin:12px 0 0;color:var(--v21-muted)}
#maxess-results-10.v21-canonical .v21-light .v21-card p{color:#56515b}
#maxess-results-10.v21-canonical .v21-three{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:26px}
#maxess-results-10.v21-canonical .v21-action{padding:22px;border-radius:22px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12)}
#maxess-results-10.v21-canonical .v21-light .v21-action{background:#fff;border-color:rgba(20,15,30,.09)}
#maxess-results-10.v21-canonical .v21-action b{display:block;font-size:12px;letter-spacing:.08em}
#maxess-results-10.v21-canonical .v21-action p{margin:8px 0 0;color:var(--v21-muted);font-size:14px}
#maxess-results-10.v21-canonical .v21-light .v21-action p{color:#56515b}
#maxess-results-10.v21-canonical .v21-legacy-wrap{margin-top:28px}
#maxess-results-10.v21-canonical .v21-masters{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
#maxess-results-10.v21-canonical .v21-master{padding:20px;border-radius:22px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12)}
#maxess-results-10.v21-canonical .v21-master a{color:#fff;text-decoration:none}
#maxess-results-10.v21-canonical .v21-master h3{font-size:19px}
#maxess-results-10.v21-canonical .v21-master p{margin:8px 0 0;color:rgba(255,255,255,.65);font-size:13px}
#maxess-results-10.v21-canonical .v21-playground{background:#fff;color:#111;border-radius:32px;padding:30px}
#maxess-results-10.v21-canonical .v21-playground a,#maxess-results-10.v21-canonical .v21-playground button{max-width:100%}
#maxess-results-10.v21-canonical #v21-video-host{margin-top:24px;min-height:260px;border-radius:28px;overflow:hidden;background:#050307;border:1px solid rgba(255,255,255,.12);box-shadow:0 28px 75px rgba(0,0,0,.34)}
#maxess-results-10.v21-canonical #v21-video-host iframe,#maxess-results-10.v21-canonical #v21-video-host video{display:block;width:100%;min-height:420px;border:0}
#maxess-results-10.v21-canonical #v21-playground-host{margin-top:20px}
#maxess-results-10.v21-canonical #v21-playground-host > *{max-width:100%}
#maxess-results-10.v21-canonical .v21-cta-final{text-align:center}
#maxess-results-10.v21-canonical .v21-cta-final h2{font-size:clamp(40px,6vw,84px)}
#maxess-results-10.v21-canonical .v21-cta-final p{max-width:680px;margin:14px auto 0;color:rgba(255,255,255,.72)}
#maxess-results-10.v21-canonical .v21-cta-link{display:inline-flex;margin-top:24px;align-items:center;justify-content:center;min-height:56px;padding:0 24px;border-radius:18px;background:#fff;color:#111;text-decoration:none;font-weight:950;box-shadow:0 16px 32px rgba(0,0,0,.28)}
@media(max-width:980px){#maxess-results-10.v21-canonical .v21-dims{grid-template-columns:repeat(3,minmax(0,1fr))}#maxess-results-10.v21-canonical .v21-masters{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:760px){#maxess-results-10.v21-canonical .v21-naya{grid-template-columns:auto 1fr}.v21-listen{grid-column:1/-1;width:100%}#maxess-results-10.v21-canonical .v21-dims,#maxess-results-10.v21-canonical .v21-story,#maxess-results-10.v21-canonical .v21-three{grid-template-columns:1fr}#maxess-results-10.v21-canonical .v21-report-grid{grid-template-columns:1fr}#maxess-results-10.v21-canonical .v21-masters{grid-template-columns:1fr}}
@media(max-width:480px){#maxess-results-10.v21-canonical .v21-section{padding-left:14px;padding-right:14px}#maxess-results-10.v21-canonical .v21-score-orb{width:min(360px,84vw)}#maxess-results-10.v21-canonical .v21-dim{width:min(220px,76vw);justify-self:center}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v21-canonical *{scroll-behavior:auto!important;transition:none!important}}
@media print{#maxess-results-10.v21-canonical{background:#fff!important;color:#111!important}#maxess-results-10.v21-canonical .v21-dark{background:#fff!important;color:#111!important}#maxess-results-10.v21-canonical .v21-purple{background:#fff!important;color:#111!important;border:1px solid #ddd}.v21-listen,.v21-cta-link{display:none!important}#maxess-results-10.v21-canonical .v21-section{padding:34px 34px;break-inside:auto}#maxess-results-10.v21-canonical .v21-card,#maxess-results-10.v21-canonical .v21-report,.v21-dim{break-inside:avoid}#maxess-results-10.v21-canonical .v21-report-grid,#maxess-results-10.v21-canonical .v21-three{break-inside:avoid}
}

/* MAXESS-AAA-CONSOLIDATED-CSS */
#maxess-results-10.v21-canonical .v21-aaa-fingerprint{display:grid;grid-template-columns:minmax(260px,.9fr) minmax(0,1.1fr);gap:34px;align-items:center;margin-top:30px;padding:26px;border-radius:34px;background:linear-gradient(145deg,rgba(155,99,255,.10),rgba(255,255,255,.78));border:1px solid rgba(80,45,120,.12);box-shadow:0 30px 90px rgba(30,15,50,.12)}
#maxess-results-10.v21-canonical .v21-fingerprint-visual{position:relative;aspect-ratio:1;display:grid;place-items:center}
#maxess-results-10.v21-canonical .v21-fingerprint-visual svg{width:100%;height:100%;overflow:visible}
#maxess-results-10.v21-canonical .v21-fp-core{position:absolute;inset:0;display:grid;place-items:center;text-align:center;pointer-events:none}
#maxess-results-10.v21-canonical .v21-fp-core b{display:block;font-size:clamp(54px,8vw,92px);line-height:.8;letter-spacing:-.08em;color:#17131d}
#maxess-results-10.v21-canonical .v21-fp-core span{display:block;margin-top:12px;font-size:9px;font-weight:950;letter-spacing:.18em;text-transform:uppercase;color:#7445ad}
#maxess-results-10.v21-canonical .v21-fp-reading{display:grid;gap:12px}
#maxess-results-10.v21-canonical .v21-fp-reading .v21-card{padding:20px;background:#fff}
#maxess-results-10.v21-canonical .v21-aaa-naya-note{display:grid;grid-template-columns:auto 1fr;gap:14px;align-items:start;margin-top:24px;padding:18px 20px;border-radius:24px;background:linear-gradient(135deg,rgba(155,99,255,.10),rgba(255,255,255,.92));border:1px solid rgba(115,68,170,.14);box-shadow:0 18px 45px rgba(35,18,60,.10)}
#maxess-results-10.v21-canonical .v21-aaa-naya-note img{width:52px;height:52px;border-radius:50%;object-fit:cover;border:2px solid #fff;box-shadow:0 8px 22px rgba(30,15,50,.18)}
#maxess-results-10.v21-canonical .v21-aaa-naya-note b{display:block;font-size:9px;letter-spacing:.15em;text-transform:uppercase;color:#7445ad}
#maxess-results-10.v21-canonical .v21-aaa-naya-note strong{display:block;margin-top:4px;font-size:17px;color:#17131d}
#maxess-results-10.v21-canonical .v21-aaa-naya-note p{margin:6px 0 0;color:#5d5764;font-size:14px;line-height:1.55}
#maxess-results-10.v21-canonical .v21-aaa-orb-live{animation:v21AaaOrb 7s ease-in-out infinite}
#maxess-results-10.v21-canonical .v21-masters .v21-master{position:relative;overflow:hidden;transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease}
#maxess-results-10.v21-canonical .v21-masters .v21-master:hover{transform:translateY(-5px);box-shadow:0 28px 60px rgba(0,0,0,.25);border-color:rgba(201,166,255,.42)}
#maxess-results-10.v21-canonical .v21-master-match{display:inline-flex;margin-bottom:10px;padding:6px 9px;border-radius:999px;background:rgba(202,168,255,.12);border:1px solid rgba(202,168,255,.22);color:#e4d2ff;font-size:8px;font-weight:950;letter-spacing:.12em;text-transform:uppercase}
#maxess-results-10.v21-canonical .v21-media-section{position:relative;overflow:hidden}
#maxess-results-10.v21-canonical .v21-media-host{display:grid;gap:18px;margin-top:28px}
#maxess-results-10.v21-canonical .v21-media-host>section,#maxess-results-10.v21-canonical .v21-media-host>.mx-reading,#maxess-results-10.v21-canonical .v21-media-host>.mx-section{margin:0!important;max-width:none!important;width:100%!important}
#maxess-results-10.v21-canonical .v21-aaa-pulse{box-shadow:inset 0 0 80px rgba(155,99,255,.16),0 30px 100px rgba(0,0,0,.52),0 0 100px var(--v21-orb-color,rgba(155,99,255,.14))}
@keyframes v21AaaOrb{0%,100%{transform:scale(1);filter:saturate(1)}50%{transform:scale(1.012);filter:saturate(1.08)}}
@media(max-width:820px){#maxess-results-10.v21-canonical .v21-aaa-fingerprint{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v21-canonical .v21-aaa-orb-live{animation:none!important}}
@media print{#maxess-results-10.v21-canonical .v21-aaa-naya-note,#maxess-results-10.v21-canonical .v21-aaa-fingerprint{break-inside:avoid;page-break-inside:avoid}.v21-media-section .v21-media-host{display:block}}


/* MAXESS-AAA-FINAL-PRODUCT-CSS */
#maxess-results-10.v21-canonical .v21-fingerprint-panel{display:grid;grid-template-columns:minmax(280px,.9fr) minmax(0,1.1fr);gap:28px;align-items:center;margin-top:30px;padding:28px;border-radius:36px;background:linear-gradient(145deg,#faf9fd,#f1eafa);border:1px solid rgba(90,52,130,.12);box-shadow:0 28px 80px rgba(30,15,50,.12)}
#maxess-results-10.v21-canonical .v21-fingerprint-visual{position:relative;aspect-ratio:1;display:grid;place-items:center}
#maxess-results-10.v21-canonical .v21-fingerprint-visual svg{width:100%;height:100%;overflow:visible}
#maxess-results-10.v21-canonical .v21-fingerprint-core{position:absolute;inset:0;display:grid;place-items:center;text-align:center;pointer-events:none}
#maxess-results-10.v21-canonical .v21-fingerprint-core b{display:block;font-size:clamp(56px,8vw,94px);line-height:.8;letter-spacing:-.08em;color:#17131d}
#maxess-results-10.v21-canonical .v21-fingerprint-core span{display:block;margin-top:10px;font-size:9px;font-weight:950;letter-spacing:.18em;text-transform:uppercase;color:#7445ad}
#maxess-results-10.v21-canonical .v21-meaning-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:24px}
#maxess-results-10.v21-canonical .v21-meaning-item{padding:20px;border-radius:22px;background:#fff;border:1px solid rgba(30,20,40,.10);box-shadow:0 18px 45px rgba(30,15,50,.08)}
#maxess-results-10.v21-canonical .v21-meaning-item b{display:block;font-size:12px;letter-spacing:.08em}
#maxess-results-10.v21-canonical .v21-meaning-item p{margin:8px 0 0;color:#5d5764;font-size:14px}
#maxess-results-10.v21-canonical .v21-naya-note{display:grid;grid-template-columns:auto 1fr;gap:14px;align-items:start;margin-top:22px;padding:18px 20px;border-radius:24px;background:linear-gradient(135deg,rgba(155,99,255,.08),rgba(255,255,255,.94));border:1px solid rgba(115,68,170,.13);box-shadow:0 18px 48px rgba(30,15,50,.09)}
#maxess-results-10.v21-canonical .v21-naya-note img{width:52px;height:52px;border-radius:50%;object-fit:cover;border:2px solid #fff;box-shadow:0 8px 22px rgba(30,15,50,.18)}
#maxess-results-10.v21-canonical .v21-naya-note b{display:block;font-size:9px;letter-spacing:.15em;text-transform:uppercase;color:#7445ad}
#maxess-results-10.v21-canonical .v21-naya-note strong{display:block;margin-top:4px;font-size:17px;color:#17131d}
#maxess-results-10.v21-canonical .v21-naya-note p{margin:6px 0 0;color:#5d5764;font-size:14px;line-height:1.55}
#maxess-results-10.v21-canonical .v21-stage-five{margin-top:18px;display:flex;flex-wrap:wrap;justify-content:center;gap:7px}
#maxess-results-10.v21-canonical .v21-stage-five span{padding:7px 10px;border-radius:999px;border:1px solid rgba(202,168,255,.22);background:rgba(18,10,24,.72);color:rgba(255,255,255,.68);font-size:8px;font-weight:950;letter-spacing:.10em;text-transform:uppercase}
#maxess-results-10.v21-canonical .v21-stage-five span.v21-active{background:#fff;color:#17131d;border-color:#fff}
#maxess-results-10.v21-canonical .v21-next-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:26px}
#maxess-results-10.v21-canonical .v21-next-card{padding:24px;border-radius:26px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12)}
#maxess-results-10.v21-canonical .v21-next-card .v21-number{font-size:10px;letter-spacing:.14em;font-weight:950;color:#d8baff}
#maxess-results-10.v21-canonical .v21-next-card h3{margin-top:9px;font-size:25px}
#maxess-results-10.v21-canonical .v21-next-card p{margin:8px 0 0;color:rgba(255,255,255,.70);font-size:14px}
#maxess-results-10.v21-canonical .v21-master{transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease}
#maxess-results-10.v21-canonical .v21-master:hover{transform:translateY(-5px);box-shadow:0 28px 60px rgba(0,0,0,.24);border-color:rgba(202,168,255,.40)}
#maxess-results-10.v21-canonical .v21-match{display:inline-flex;margin-bottom:10px;padding:6px 9px;border-radius:999px;background:rgba(202,168,255,.12);border:1px solid rgba(202,168,255,.22);color:#e4d2ff;font-size:8px;font-weight:950;letter-spacing:.12em;text-transform:uppercase}
#maxess-results-10.v21-canonical .v21-playground-premium{display:grid;grid-template-columns:1.1fr .9fr;gap:22px;align-items:center}
#maxess-results-10.v21-canonical .v21-playground-panel{padding:26px;border-radius:28px;background:#fff;border:1px solid rgba(30,20,40,.09);box-shadow:0 24px 62px rgba(30,15,50,.10)}
#maxess-results-10.v21-canonical .v21-media-host{display:grid;gap:16px;margin-top:18px}
#maxess-results-10.v21-canonical .v21-media-host>video,#maxess-results-10.v21-canonical .v21-media-host>iframe{width:100%;max-width:100%;border-radius:22px;display:block}
#maxess-results-10.v21-canonical .v21-final-note{max-width:760px;margin:18px auto 0;color:rgba(255,255,255,.74)}
@media(max-width:860px){#maxess-results-10.v21-canonical .v21-fingerprint-panel,#maxess-results-10.v21-canonical .v21-playground-premium{grid-template-columns:1fr}#maxess-results-10.v21-canonical .v21-meaning-grid,#maxess-results-10.v21-canonical .v21-next-grid{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){#maxess-results-10.v21-canonical .v21-master{transition:none!important}}
@media print{#maxess-results-10.v21-canonical .v21-fingerprint-panel,#maxess-results-10.v21-canonical .v21-naya-note,#maxess-results-10.v21-canonical .v21-next-card,#maxess-results-10.v21-canonical .v21-master{break-inside:avoid;page-break-inside:avoid}}

</style>
"""

JS = r"""
<script id="maxess-results-v21-canonical-js">
(function(){
  'use strict';
  if(window.__MAXESS_V21_CANONICAL__) return;
  window.__MAXESS_V21_CANONICAL__ = true;

  var root = document.getElementById('maxess-results-10');
  if(!root) return;

  function escapeHtml(value){ return String(value == null ? '' : value).replace(/[&<>\"']/g,function(c){ return ({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'})[c]; }); }
  function clamp(value){ var n=Number(value); return Number.isFinite(n) ? Math.max(0,Math.min(100,n)) : null; }
  function result(){ return (window.MAXESS_RESULT && typeof window.MAXESS_RESULT==='object') ? window.MAXESS_RESULT : null; }
  function score(r){ if(!r) return null; return clamp(r.overallScore != null ? r.overallScore : (r.masterScore != null ? r.masterScore : (r.score != null ? r.score : r.overall))); }
  function dimensions(r){
    if(!r) return [];
    var list = Array.isArray(r.dimensions) ? r.dimensions : [];
    return list.slice(0,5).map(function(d,i){ return { name:String(d && (d.name || d.label) || ('Dimension '+(i+1))), score:clamp(d && (d.score != null ? d.score : d.value)), description:String(d && (d.description || d.insight) || '') }; });
  }
  function person(r){
    if(!r) return '';
    var bags=[r.profile,r.user,r.person,r.identity,r];
    for(var i=0;i<bags.length;i++){ var b=bags[i]; if(b && typeof b==='object'){ var v=b.name || b.displayName || b.firstName; if(v) return String(v); } }
    return '';
  }
<<<<<<< Updated upstream
  function stage(s){
    if(s==null) return '';
    return s>=91?'Mastering':s>=76?'Advancing':s>=51?'Developing':s>=21?'Foundation':'Supporting';
  }
=======
  function stage(s){if(s==null) return "";return s>=91?"Mastering":s>=76?"Advancing":s>=51?"Developing":s>=21?"Foundation":"Supporting";}
>>>>>>> Stashed changes
  function dimCopy(name,sc){
    var n=name.toLowerCase();
    if(n.indexOf('communication')>=0) return 'This shows how effectively you express intent, context, constraints and the outcome you want from AI.';
    if(n.indexOf('direction')>=0) return 'This shows how clearly you define the result before asking AI to produce it.';
    if(n.indexOf('evaluation')>=0) return 'This shows how deliberately you judge AI output before accepting it. Quality improves when judgment is visible.';
    if(n.indexOf('iteration')>=0) return 'This shows how naturally you improve an answer instead of treating the first response as final.';
    if(n.indexOf('system')>=0) return 'This shows whether you turn repeated AI work into reusable workflows, assets and leverage.';
    if(sc!=null && sc>=85) return 'A strong current capability you can deliberately compound.';
    if(sc!=null && sc>=70) return 'A capable area with meaningful room to sharpen.';
    return 'A high-value area for focused improvement.';
  }
  function listen(){
    var ids=['#mx-naya-listen','#v11-naya-listen','#v13-listen','.mx-naya-listen','.v18-listen'];
    for(var i=0;i<ids.length;i++){
      var nodes=root.querySelectorAll(ids[i]);
      for(var j=0;j<nodes.length;j++){
        var n=nodes[j];
        if(n && getComputedStyle(n).display!=='none'){ n.click(); return; }
      }
    }
    root.dispatchEvent(new CustomEvent('maxess:naya-listen',{bubbles:true,detail:{result:result()}}));
  }
  function masters(){
    var cards=[];
    root.querySelectorAll('.mx-naya-door,.mx-area').forEach(function(el){
      if(cards.length>=18) return;
      var title=el.querySelector('h3,h4,strong,.mx-area-main') || el;
      var text=(el.textContent||'').trim().replace(/\\\\\s+/g,' ');
      var name=(title.textContent||text).trim().replace(/\\\\\s+/g,' ').slice(0,90);
      var href=el.querySelector('a') && el.querySelector('a').getAttribute('href') || '';
      if(name) cards.push({name:name,href:href,text:text.slice(0,220)});
    });
    return cards;
  }
  
/* MAXESS-AAA-CONSOLIDATED-JS */
  function aaaScoreColor(value){
    var s=Math.max(0,Math.min(100,Number(value)||0));
    var h=178+(s*1.05), l=55+(s*.10);
    return 'hsl('+h.toFixed(0)+' 78% '+l.toFixed(0)+'%)';
  }
  function aaaNayaNote(title,body){
    var el=document.createElement('div');
    el.className='v21-aaa-naya-note';
    el.innerHTML='<img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>'+escapeHtml(title)+'</strong><p>'+escapeHtml(body)+'</p></div>';
    return el;
  }
  function aaaFingerprint(ds,total){
    var wrap=document.createElement('section');
    wrap.className='v21-section v21-light v21-aaa-fingerprint-section';
    wrap.innerHTML='<div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">YOUR AI FINGERPRINT</span><h2 class="v21-section-title">See the shape of your capability.</h2><p class="v21-section-copy">Your five dimensions are not isolated scores. Their shape shows how your strengths and opportunities work together.</p><div class="v21-aaa-fingerprint"><div class="v21-fingerprint-visual"><svg viewBox="0 0 430 430" role="img" aria-label="Your five-dimension AI capability fingerprint"><defs><radialGradient id="v21FpFill"><stop offset="0" stop-color="#9b63ff" stop-opacity=".38"/><stop offset="1" stop-color="#44d9ce" stop-opacity=".10"/></radialGradient></defs><g class="v21-fp-grid">'+[1,2,3,4].map(function(k){var rr=42*k;var pts=[];for(var i=0;i<5;i++){var a=-Math.PI/2+i*Math.PI*2/5;pts.push((215+Math.cos(a)*rr)+','+(215+Math.sin(a)*rr))}return '<polygon points="'+pts.join(' ')+'" fill="none" stroke="rgba(30,20,40,.12)"/>';}).join('')+'</g><g>'+ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5;return '<line x1="215" y1="215" x2="'+(215+Math.cos(a)*168)+'" y2="'+(215+Math.sin(a)*168)+'" stroke="rgba(30,20,40,.10)"/>';}).join('')+'</g><polygon points="'+ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5,r=168*(Number(d.score)||0)/100;return (215+Math.cos(a)*r)+','+(215+Math.sin(a)*r)}).join(' ')+'" fill="url(#v21FpFill)" stroke="#7445ad" stroke-width="3"/><g>'+ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5,r=168*(Number(d.score)||0)/100;return '<circle cx="'+(215+Math.cos(a)*r)+'" cy="'+(215+Math.sin(a)*r)+'" r="7" fill="'+aaaScoreColor(d.score)+'" stroke="#fff" stroke-width="3"/>';}).join('')+'</g></svg><div class="v21-fp-core"><b>'+Math.round(total)+'</b><span>MAXESS SCORE</span></div></div><div class="v21-fp-reading">'+ds.map(function(d){return '<div class="v21-card"><span class="v21-kicker" style="color:#7445ad">'+escapeHtml(d.name)+'</span><h3 style="font-size:34px;margin-top:7px">'+Math.round(d.score||0)+'</h3><p style="margin-top:6px">'+escapeHtml(d.description||dimCopy(d.name,d.score))+'</p></div>';}).join('')+'</div></div></div></section>';
    return wrap;
  }
  function aaaEnhance(r,ds,strongest,lowest,preservedPlay,preservedMedia){
    var scoreValue=score(r)||0;
    var sections=[].slice.call(root.querySelectorAll('.v21-section'));
    var dimSection=sections.find(function(s){return (s.textContent||'').indexOf('YOUR FIVE DIMENSIONS')>=0});
    if(dimSection && !root.querySelector('.v21-aaa-fingerprint-section')) dimSection.parentNode.insertBefore(aaaFingerprint(ds,scoreValue),dimSection);
    var orb=root.querySelector('.v21-score-orb');
    if(orb){orb.classList.add('v21-aaa-orb-live','v21-aaa-pulse');orb.style.setProperty('--v21-orb-color',aaaScoreColor(scoreValue));orb.style.borderColor=aaaScoreColor(scoreValue)}
    var report=root.querySelector('.v21-report');if(report&&!report.querySelector('.v21-aaa-naya-note'))report.appendChild(aaaNayaNote('Here is the part I want you to notice.', 'Your score tells you where you are. The pattern, strength and lever tell you what to do with that information.'));
    var pattern=sections.find(function(s){return (s.textContent||'').indexOf('YOUR PATTERN')>=0});if(pattern&&!pattern.querySelector('.v21-aaa-naya-note'))pattern.appendChild(aaaNayaNote('Your pattern is the story between the numbers.', 'Look for the capability that is naturally supporting the others—and the one that, when strengthened, could change the shape of the whole profile.'));
    var strength=sections.find(function(s){return (s.textContent||'').indexOf('YOUR STRENGTH')>=0});if(strength&&!strength.querySelector('.v21-aaa-naya-note'))strength.appendChild(aaaNayaNote('Protect what is already working.', 'Your strongest capability is a resource. The goal is not to admire it; the goal is to compound it until it becomes leverage.'));
    var lever=sections.find(function(s){return (s.textContent||'').indexOf('YOUR LEVER')>=0});if(lever&&!lever.querySelector('.v21-aaa-naya-note'))lever.appendChild(aaaNayaNote('This is an opportunity, not a verdict.', 'The lowest dimension is simply the clearest place to focus. One deliberate improvement here can create a disproportionate return.'));
    var next=sections.find(function(s){return (s.textContent||'').indexOf('YOUR NEXT MOVE')>=0});if(next&&!next.querySelector('.v21-aaa-naya-note'))next.appendChild(aaaNayaNote('Small actions beat abstract ambition.', 'Protect your strength. Build your lever. Then create, score and improve one real AI workflow.'));
    var mastersSection=sections.find(function(s){return (s.textContent||'').indexOf('18 NAYA MASTERS')>=0});
    if(mastersSection){var cards=[].slice.call(mastersSection.querySelectorAll('.v21-master'));cards.forEach(function(card){var txt=(card.textContent||'').toLowerCase(),rel=0;if(txt.indexOf(String(lowest.name||'').toLowerCase())>=0)rel+=60;if(txt.indexOf(String(strongest.name||'').toLowerCase())>=0)rel+=35;if(/practice|workflow|prompt|system|evaluation|communication/.test(txt))rel+=5;card.dataset.v21Relevance=String(rel)});cards.sort(function(a,b){return Number(b.dataset.v21Relevance)-Number(a.dataset.v21Relevance)}).forEach(function(card,i){var pill=card.querySelector('.v21-master-match');if(pill)pill.remove();if(i<3){var p=document.createElement('span');p.className='v21-master-match';p.textContent=i===0?'BEST MATCH':'STRONG MATCH';card.insertBefore(p,card.firstChild)}mastersSection.querySelector('.v21-masters').appendChild(card)})}
    var host=document.createElement('section');host.className='v21-section v21-dark v21-media-section';host.innerHTML='<div class="v21-inner"><span class="v21-kicker">NAYA · IN PRACTICE</span><h2 class="v21-section-title">Turn insight into experience.</h2><p class="v21-section-copy">Use the existing walkthrough, video and working controls here. Nothing valuable from the original experience should disappear.</p><div class="v21-media-host"></div></div>';
    var playground=sections.find(function(s){return (s.textContent||'').indexOf('PLAYGROUND')>=0});if(playground&&!root.querySelector('.v21-media-section'))playground.parentNode.insertBefore(host,playground);
    var mediaHost=root.querySelector('.v21-media-host');if(mediaHost){if(preservedPlay)mediaHost.appendChild(preservedPlay);(preservedMedia||[]).forEach(function(n){if(n&&n.parentNode!==mediaHost)mediaHost.appendChild(n)})}
    var listens=root.querySelectorAll('.v21-listen');for(var i=listens.length-1;i>0;i--)listens[i].remove();
  }

  function build(r){
    var legacyPlayNode=root.querySelector('#naya-playground');
    var legacyVideoNode=root.querySelector('video,iframe[src*="youtube"],iframe[src*="vimeo"],[class*="video"]');

    var s=score(r), ds=dimensions(r), name=person(r), st=(r && ['Supporting','Foundation','Developing','Advancing','Mastering'].indexOf(r.masteryStage)>=0 ? r.masteryStage : stage(s));
    if(s==null || ds.length!==5){
      root.setAttribute('data-results-state','awaiting');
      root.innerHTML='<section class="v21-section v21-dark"><div class="v21-inner" style="text-align:center;padding-top:120px;padding-bottom:120px"><span class="v21-kicker">MAXESS RESULTS</span><h1 class="v21-section-title" style="margin-top:18px">Your result is not loaded yet.</h1><p class="v21-section-copy" style="margin:18px auto 0;max-width:650px">Complete the MAXESS assessment and return with your Result Contract. This page does not invent a score when real result data is unavailable.</p></div></section>';
      return;
    }

    var sorted=ds.slice().sort(function(a,b){return (b.score||0)-(a.score||0)});
    var strongest=sorted[0], lowest=sorted[sorted.length-1];
    var reportName=name ? escapeHtml(name)+', here is what I see.' : 'Here is what I see.';
    var media=[];
    root.querySelectorAll('video,iframe,#naya-playground,.mx-reading,.mx-section').forEach(function(n){ if(media.indexOf(n)<0) media.push(n); });
    var mastersList=masters();
    var stageLabels=['Supporting','Foundation','Developing','Advancing','Mastering'];
    var stageHTML=stageLabels.map(function(x){return '<span class="'+(x===st?'v21-active':'')+'">'+x+'</span>';}).join('');
    var colorFor=function(v){var x=Math.max(0,Math.min(100,Number(v)||0));return 'hsl('+(178+x*1.05).toFixed(0)+' 78% '+(55+x*.10).toFixed(0)+'%)'};
    var dimensionsCopy=ds.map(function(d){return '<div class="v21-meaning-item"><b>'+escapeHtml(d.name)+'</b><p>'+escapeHtml(d.description||dimCopy(d.name,d.score))+'</p></div>';}).join('');
    var fpPoints=ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5,r=175*(Number(d.score)||0)/100;return (215+Math.cos(a)*r)+','+(215+Math.sin(a)*r)}).join(' ');
    var fpAxes=ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5;return '<line x1="215" y1="215" x2="'+(215+Math.cos(a)*175)+'" y2="'+(215+Math.sin(a)*175)+'" stroke="rgba(30,20,40,.11)"/>'}).join('');
    var fpGrid=[1,2,3,4].map(function(k){var rr=43*k,pts=[];for(var i=0;i<5;i++){var a=-Math.PI/2+i*Math.PI*2/5;pts.push((215+Math.cos(a)*rr)+','+(215+Math.sin(a)*rr))}return '<polygon points="'+pts.join(' ')+'" fill="none" stroke="rgba(30,20,40,.11)"/>'}).join('');
    var fpDots=ds.map(function(d,i){var a=-Math.PI/2+i*Math.PI*2/5,r=175*(Number(d.score)||0)/100;return '<circle cx="'+(215+Math.cos(a)*r)+'" cy="'+(215+Math.sin(a)*r)+'" r="7" fill="'+colorFor(d.score)+'" stroke="#fff" stroke-width="3"/>'}).join('');

    root.classList.add('v21-canonical');
    root.innerHTML='<div class="v21-shell">'+
      '<section class="v21-section v21-dark"><div class="v21-inner">'+
<<<<<<< Updated upstream
        '<div class="v21-naya"><img class="v21-avatar" src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><span class="v21-kicker">NAYA · YOUR AI GUIDE</span><h1 class="v21-naya-title">'+(name?reportName:'Hi. I\'ve looked at your results.')+'</h1><p class="v21-naya-sub">This isn\'t your judgment. <strong>It\'s your map.</strong></p></div><button class="v21-listen" type="button" aria-label="Listen to Naya interpret your MAXESS results">LISTEN TO NAYA <span aria-hidden="true">▶</span></button></div>'+ 
      '</div></section>'+ 
      '<section class="v21-section v21-dark"><div class="v21-inner v21-score-wrap"><span class="v21-kicker">YOUR RESULT</span><div class="v21-score-orb"><div><div class="v21-score-number">'+Math.round(s)+'</div><div class="v21-score-label">MAXESS SCORE</div></div></div><span class="v21-stage">'+st+'</span><div class="v21-stage-five">'+stageHTML+'</div><p class="v21-final-note">Your score is a starting point. The report below explains the shape of your capability and where your next improvement can create the most leverage.</p></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">WHAT YOUR SCORES MEAN</span><h2 class="v21-section-title">The number is useful. The meaning is the value.</h2><p class="v21-section-copy">MAXESS is not here to judge you. It is here to make your current AI capability understandable enough to act on.</p><div class="v21-meaning-grid">'+dimensionsCopy+'</div></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><article class="v21-report"><div class="v21-report-mark"></div><span class="v21-kicker" style="color:#7445ad">YOUR PERSONALIZED REPORT</span><h2>'+reportName+'</h2><span class="v21-report-stage">'+st+'</span><p>Your strongest visible capability is <strong>'+escapeHtml(strongest.name)+'</strong>. Your clearest leverage opportunity is <strong>'+escapeHtml(lowest.name)+'</strong>. Together, those two signals tell us more than the overall number ever could.</p><div class="v21-report-grid"><div class="v21-cell"><span>MAXESS SCORE</span><b>'+Math.round(s)+'</b><small>Your current overall capability signal.</small></div><div class="v21-cell"><span>MASTERY STAGE</span><b>'+st+'</b><small>Supporting → Mastering.</small></div><div class="v21-cell"><span>STRONGEST SIGNAL</span><b>'+escapeHtml(strongest.name)+'</b><small>Protect and compound this capability.</small></div></div><div class="v21-naya-note"><img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>Here is what I want you to notice.</strong><p>Your score tells you where you are. Your pattern, strength and lever tell you what to do with that information.</p></div></div></article></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">YOUR AI FINGERPRINT</span><h2 class="v21-section-title">See the shape of your capability.</h2><p class="v21-section-copy">Your five dimensions create a fingerprint. The shape shows where you are balanced, where you are naturally strong, and where focused development can reshape the whole profile.</p><div class="v21-fingerprint-panel"><div class="v21-fingerprint-visual"><svg viewBox="0 0 430 430" role="img" aria-label="Your five-dimension AI capability fingerprint"><defs><radialGradient id="v21FinalFp"><stop offset="0" stop-color="#9b63ff" stop-opacity=".35"/><stop offset="1" stop-color="#44d9ce" stop-opacity=".08"/></radialGradient></defs>'+fpGrid+fpAxes+'<polygon points="'+fpPoints+'" fill="url(#v21FinalFp)" stroke="#7445ad" stroke-width="3"/>'+fpDots+'</svg><div class="v21-fingerprint-core"><div><b>'+Math.round(s)+'</b><span>MAXESS SCORE</span></div></div></div><div class="v21-fp-reading">'+ds.map(function(d){return '<div class="v21-card"><span class="v21-kicker" style="color:#7445ad">'+escapeHtml(d.name)+'</span><h3 style="font-size:34px;margin-top:7px">'+Math.round(d.score||0)+'</h3><p style="margin-top:6px">'+escapeHtml(d.description||dimCopy(d.name,d.score))+'</p></div>';}).join('')+'</div></div></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">YOUR STRENGTH</span><h2 class="v21-section-title">Protect what is already working.</h2><div class="v21-card"><h3>'+escapeHtml(strongest.name)+'</h3><p>You already have meaningful capability here. Compound it deliberately. Your strongest capability is not a trophy—it is the foundation you can build the rest of the system on.</p><div class="v21-naya-note"><img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>Keep this. Make it stronger.</strong><p>When you know what you naturally do well, you can stop trying to improve everything at once and start creating leverage.</p></div></div></div></div></section>'+ 
      '<section class="v21-section v21-purple"><div class="v21-inner"><span class="v21-kicker" style="color:#eadcff">YOUR LEVER</span><h2 class="v21-section-title">Build the capability that can move the whole system.</h2><div class="v21-card"><h3>'+escapeHtml(lowest.name)+'</h3><p>Your highest-leverage opportunity is <strong>'+escapeHtml(lowest.name)+'</strong>. This is not a weakness label. It is simply the clearest place to focus one deliberate improvement.</p><div class="v21-naya-note"><img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>This is where I would focus next.</strong><p>Protect your strength. Build your lever. Then watch how the shape of your whole profile changes.</p></div></div></div></div></section>'+ 
      '<section class="v21-section v21-dark"><div class="v21-inner"><span class="v21-kicker">YOUR FIVE DIMENSIONS</span><h2 class="v21-section-title">Go one layer deeper.</h2><div class="v21-dims" role="list">'+ds.map(function(d){return '<button class="v21-dim" type="button" role="listitem" aria-label="'+escapeHtml(d.name)+' score '+Math.round(d.score||0)+'"><span class="v21-dim-score">'+Math.round(d.score||0)+'</span><span class="v21-dim-name">'+escapeHtml(d.name)+'</span></button>';}).join('')+'</div><div class="v21-detail"><b>SELECT A DIMENSION</b><p>Choose one of the five orbs to explore the score, meaning and next lever.</p></div></div></section>'+ 
      '<section class="v21-section v21-dark"><div class="v21-inner"><span class="v21-kicker">YOUR PATTERN</span><h2 class="v21-section-title">See the pattern, not just the score.</h2><p class="v21-section-copy">Your strongest capability and your biggest opportunity are not separate facts. They describe the shape of the system you are building with AI.</p><div class="v21-story">'+ds.map(function(d){return '<div class="v21-card"><span class="v21-kicker">'+escapeHtml(d.name)+'</span><h3>'+Math.round(d.score||0)+'</h3><p>'+escapeHtml(d.description || dimCopy(d.name,d.score))+'</p></div>';}).join('')+'</div><div class="v21-naya-note"><img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>The pattern is the story between the numbers.</strong><p>Look for what is already supporting the rest of your profile—and what could change the shape if you strengthened it.</p></div></div></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">YOUR NEXT MOVE</span><h2 class="v21-section-title">Three things to do next.</h2><div class="v21-next-grid"><div class="v21-next-card"><div class="v21-number">01 · PROTECT</div><h3>Your strength</h3><p>Use '+escapeHtml(strongest.name)+' in a real AI workflow this week and capture the result.</p></div><div class="v21-next-card"><div class="v21-number">02 · BUILD</div><h3>Your lever</h3><p>Choose one workflow where '+escapeHtml(lowest.name)+' is limiting you and improve it deliberately.</p></div><div class="v21-next-card"><div class="v21-number">03 · REPEAT</div><h3>Create → Score → Improve</h3><p>Do not stop at the first answer. Judge the quality, improve one thing, and repeat.</p></div></div><div class="v21-naya-note"><img src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide"><div><b>Naya · your guide</b><strong>Small actions beat abstract ambition.</strong><p>One good workflow repeated and improved is worth more than a dozen ideas you never use.</p></div></div></div></section>'+ 
      '<section class="v21-section v21-dark"><div class="v21-inner"><span class="v21-kicker">18 NAYA MASTERS</span><h2 class="v21-section-title">Choose the doors that fit your next step.</h2><p class="v21-section-copy">These are not just 18 cards. They are potential pathways. The strongest matches are the ones that can help you build your current lever while compounding your strongest capability.</p><div class="v21-masters">'+(mastersList.length?mastersList.map(function(m,i){var txt=(m.text||'').toLowerCase(),match=(txt.indexOf(String(lowest.name||'').toLowerCase())>=0||txt.indexOf(String(strongest.name||'').toLowerCase())>=0);return '<article class="v21-master">'+(match?'<span class="v21-match">'+(i===0?'BEST MATCH':'STRONG MATCH')+'</span>':'')+(m.href?'<a href="'+escapeHtml(m.href)+'">':'')+'<h3>'+escapeHtml(m.name)+'</h3>'+(m.href?'</a>':'')+'<p>'+escapeHtml(m.text)+'</p></article>';}).join(''):'<article class="v21-master"><h3>Naya Masters</h3><p>Your specialist pathways will appear here when the authoritative library content is available.</p></article>')+'</div></div></section>'+ 
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">PLAYGROUND</span><h2 class="v21-section-title">Understand → Decide → Practice.</h2><div class="v21-playground-premium"><div class="v21-playground-panel"><p>Turn your result into action. Take what you learned, choose one improvement, and practice it on a real task.</p><div class="v21-legacy-wrap" id="v21-playground-host"></div></div><div class="v21-playground-panel"><span class="v21-kicker" style="color:#7445ad">NAYA · IN PRACTICE</span><h3 style="font-size:32px;margin-top:10px">Your report should change what you do next.</h3><p style="margin-top:10px;color:#5d5764">The point of MAXESS is not a score. The point is capability you can use, improve and turn into leverage.</p></div></div></div></section>'+ 
      '<section class="v21-section v21-purple"><div class="v21-inner v21-cta-final"><span class="v21-kicker" style="color:#eadcff">YOUR AI MASTERY JOURNEY</span><h2>Now you know where you are. Let’s turn that into your next level.</h2><p>MAXESS gives you a map. Naya helps you use it.</p><a class="v21-cta-link" href="https://nayanet.xyz/">CONTINUE WITH NAYANET</a></div></section>'+ 
      '</div>';

    var btn=root.querySelector('.v21-listen');if(btn)btn.addEventListener('click',listen);
    var detail=root.querySelector('.v21-detail');root.querySelectorAll('.v21-dim').forEach(function(btn,i){btn.addEventListener('click',function(){var d=ds[i]||{};detail.innerHTML='<b>'+escapeHtml(d.name)+' · '+Math.round(d.score||0)+'</b><p>'+escapeHtml(d.description||dimCopy(d.name,d.score))+'</p>';});});
    var host=root.querySelector('#v21-playground-host');if(host){media.forEach(function(n){if(n && n!==root && n.parentNode!==host)host.appendChild(n);});}
    var orb=root.querySelector('.v21-score-orb');if(orb){orb.style.borderColor=colorFor(s);orb.style.boxShadow='inset 0 0 90px '+colorFor(s)+'33,0 45px 110px rgba(0,0,0,.55),0 0 110px '+colorFor(s)+'22';}
    root.setAttribute('data-results-version','v21-final-aaa');
    root.setAttribute('data-results-data-source','window.MAXESS_RESULT');
    root.setAttribute('data-results-state','ready');
=======
        '<div class="v21-naya">'+
          '<img class="v21-avatar" src="https://raw.githubusercontent.com/SoulSchoolAcademy/maxess/main/Naya%20Profile%20Black.jpg" alt="Naya, your AI guide">'+
          '<div><span class="v21-kicker">NAYA · YOUR AI GUIDE</span><h1 class="v21-naya-title">'+(name ? reportName : 'Hi. I have looked at your results.')+'</h1><p class="v21-naya-sub">This is not your judgment. <strong>It is your map.</strong></p></div>'+
          '<button class="v21-listen" type="button" aria-label="Listen to Naya interpret your MAXESS results">LISTEN TO NAYA <span aria-hidden="true">▶</span></button>'+        
        '</div>'+      
      '</div></section>'+
      '<section class="v21-section v21-dark"><div class="v21-inner v21-score-wrap">'+
        '<span class="v21-kicker">YOUR RESULT</span><div class="v21-score-orb"><div><div class="v21-score-number">'+Math.round(s)+'</div><div class="v21-score-label">MAXESS SCORE</div></div></div><span class="v21-stage">'+st+'</span>'+ 
      '</div></section>'+
      '<section class="v21-section v21-light"><div class="v21-inner">'+
        '<span class="v21-kicker" style="color:#7445ad">YOUR FIVE DIMENSIONS</span><h2 class="v21-section-title">One score. Five capabilities.</h2><p class="v21-section-copy">These five dimensions show what is shaping your overall MAXESS result. Select one to understand it, not just score it.</p>'+
        '<div class="v21-dims" role="list">'+ds.map(function(d){ return '<button class="v21-dim" type="button" role="listitem" aria-label="'+escapeHtml(d.name)+' score '+Math.round(d.score||0)+'"><span class="v21-dim-score">'+Math.round(d.score||0)+'</span><span class="v21-dim-name">'+escapeHtml(d.name)+'</span></button>'; }).join('')+'</div><div class="v21-detail"><b>SELECT A DIMENSION</b><p>Choose one of the five orbs to explore what the capability means and where its leverage lives.</p></div>'+ 
      '</div></section>'+
      '<section class="v21-section v21-light"><div class="v21-inner"><article class="v21-report"><div class="v21-report-mark"></div><span class="v21-kicker" style="color:#7445ad">YOUR PERSONALIZED REPORT</span><h2>'+reportName+'</h2><span class="v21-report-stage">'+st+'</span><p>Your MAXESS score is <strong>'+Math.round(s)+'</strong>. That number is not a judgment; it is a map of your current AI capability. Your strongest visible signal is <strong>'+escapeHtml(strongest.name)+'</strong>, while <strong>'+escapeHtml(lowest.name)+'</strong> is the clearest place to create focused improvement.</p><div class="v21-report-grid"><div class="v21-cell"><span>OVERALL RESULT</span><b>'+Math.round(s)+'</b><small>Your current MAXESS score.</small></div><div class="v21-cell"><span>MASTERY STAGE</span><b>'+st+'</b><small>Where your current capability sits.</small></div><div class="v21-cell"><span>STRONGEST SIGNAL</span><b>'+escapeHtml(strongest.name)+'</b><small>Use your strength as a foundation.</small></div></div></article></div></section>'+
      '<section class="v21-section v21-dark"><div class="v21-inner"><span class="v21-kicker">YOUR PATTERN</span><h2 class="v21-section-title">See the pattern, not just the score.</h2><p class="v21-section-copy">The value is in the relationship between your five dimensions. Together they show how your current AI capability is shaped.</p><div class="v21-story">'+ds.map(function(d){return '<div class="v21-card"><span class="v21-kicker">'+escapeHtml(d.name)+'</span><h3>'+Math.round(d.score||0)+'</h3><p>'+escapeHtml(d.description || dimCopy(d.name,d.score))+'</p></div>';}).join('')+'</div></div></section>'+
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">YOUR STRENGTH</span><h2 class="v21-section-title">Protect what is already working.</h2><div class="v21-card"><h3>'+escapeHtml(strongest.name)+'</h3><p>You already have meaningful capability here. Compound it deliberately instead of trying to improve everything at once. The best next move is to turn this strength into a repeatable advantage.</p></div></div></section>'+
      '<section class="v21-section v21-purple"><div class="v21-inner"><span class="v21-kicker" style="color:#eadcff">YOUR LEVER</span><h2 class="v21-section-title">Build the capability that can move the whole system.</h2><div class="v21-card"><h3>'+escapeHtml(lowest.name)+'</h3><p>Your strongest opportunity is '+escapeHtml(lowest.name)+'. This is not a verdict about you. It is the area furthest behind the rest of your profile, so focused improvement here can create disproportionate gains.</p></div></div></section>'+
      '<section class="v21-section v21-dark"><div class="v21-inner"><span class="v21-kicker">YOUR NEXT MOVE</span><h2 class="v21-section-title">Three things to do next.</h2><div class="v21-three"><div class="v21-action"><b>01 · PROTECT YOUR STRENGTH</b><p>Use '+escapeHtml(strongest.name)+' in a real AI workflow this week and capture the result.</p></div><div class="v21-action"><b>02 · BUILD YOUR LEVER</b><p>Choose one workflow where '+escapeHtml(lowest.name)+' is holding you back and improve it deliberately.</p></div><div class="v21-action"><b>03 · CREATE → SCORE → IMPROVE</b><p>Do not stop at the first answer. Measure quality, make one improvement, then repeat.</p></div></div></div></section>'+
      '<section class="v21-section v21-dark"><div class="v21-inner"><span class="v21-kicker">18 NAYA MASTERS</span><h2 class="v21-section-title">Choose the doors that fit your next step.</h2><p class="v21-section-copy">These specialist pathways become useful once you know what you want to improve.</p><div class="v21-masters">'+(mastersList.length ? mastersList.map(function(m){return '<article class="v21-master">'+(m.href?'<a href="'+escapeHtml(m.href)+'">':'')+'<h3>'+escapeHtml(m.name)+'</h3>'+(m.href?'</a>':'')+'<p>'+escapeHtml(m.text)+'</p></article>';}).join('') : '<article class="v21-master"><h3>Naya Masters</h3><p>Your 18 specialist pathways will appear here when the authoritative library content is available.</p></article>')+'</div></div></section>'+
      '<section class="v21-section v21-light"><div class="v21-inner"><span class="v21-kicker" style="color:#7445ad">PLAYGROUND</span><h2 class="v21-section-title">Understand → Decide → Practice.</h2><div class="v21-playground"><p>Turn your result into action. Take what you learned, choose one improvement, and practice it on a real task.</p><div class="v21-legacy-wrap" id="v21-video-host"></div><div class="v21-legacy-wrap" id="v21-playground-host"></div></div></div></section>'+
      '<section class="v21-section v21-purple"><div class="v21-inner v21-cta-final"><span class="v21-kicker" style="color:#eadcff">YOUR AI MASTERY JOURNEY</span><h2>Now you know where you are. The next step is becoming better.</h2><p>MAXESS is designed for people who want exceptional results from AI—not ‘good enough.’</p><a class="v21-cta-link" href="https://nayanet.xyz/">CONTINUE WITH NAYANET</a></div></section>'+
      '</div>';

    var videoHost=root.querySelector('#v21-video-host');
    if(legacyVideoNode && videoHost) videoHost.appendChild(legacyVideoNode);
    var playHost=root.querySelector('#v21-playground-host');
    if(legacyPlayNode && playHost) playHost.appendChild(legacyPlayNode);
    var btn=root.querySelector('.v21-listen'); if(btn) btn.addEventListener('click',listen);
    var detail=root.querySelector('.v21-detail'); root.querySelectorAll('.v21-dim').forEach(function(btn,i){btn.addEventListener('click',function(){var d=ds[i];detail.innerHTML='<b>'+escapeHtml(d.name)+' · '+Math.round(d.score||0)+'</b><p>'+escapeHtml(d.description || dimCopy(d.name,d.score))+'</p>';detail.scrollIntoView({behavior:'smooth',block:'nearest'});});});
    var oldPlay=document.getElementById('naya-playground'); var host=document.getElementById('v21-playground-host'); if(oldPlay && host) host.appendChild(oldPlay);
    root.setAttribute('data-results-version','v21-canonical');root.setAttribute('data-results-data-source','window.MAXESS_RESULT');root.setAttribute('data-results-state','ready');
>>>>>>> Stashed changes
  }
  function enforce(){
    var rootNow=document.getElementById('maxess-results-10');
    if(!rootNow) return;
    if(rootNow.dataset.v21Enforcing==='1') return;
    rootNow.dataset.v21Enforcing='1';
    var observer=new MutationObserver(function(){
      if(window.__MAXESS_V21_CANONICAL_RENDERING__) return;
      if(!rootNow.querySelector('.v21-shell')){
        window.__MAXESS_V21_CANONICAL_RENDERING__=true;
        try{ build(result()); } finally { window.__MAXESS_V21_CANONICAL_RENDERING__=false; }
      }
    });
    observer.observe(rootNow,{childList:true,subtree:true});
    window.__MAXESS_V21_CANONICAL_OBSERVER__=observer;
    window.__MAXESS_V21_CANONICAL_ENFORCE__=true;
    window.__MAXESS_V21_CANONICAL_RENDERING__=true;
    try{ build(result()); } finally { window.__MAXESS_V21_CANONICAL_RENDERING__=false; }
    [0,100,400,1000].forEach(function(ms){setTimeout(function(){
      if(!rootNow.querySelector('.v21-shell')){
        window.__MAXESS_V21_CANONICAL_RENDERING__=true;
        try{ build(result()); } finally { window.__MAXESS_V21_CANONICAL_RENDERING__=false; }
      }
    },ms);});
  }
  function boot(){ enforce(); }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',boot,{once:true}); else boot();
})();
</script>
"""


def sha_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def remove_old_v21(text: str) -> str:
    text = re.sub(r'<!-- MAXESS-NITRO-AAA-UPGRADE v3 -->.*?<!-- /MAXESS-NITRO-AAA-UPGRADE -->\s*', '', text, flags=re.S)
    text = re.sub(r'<style id="maxess-results-v21-authority-css">.*?</style>\s*', '', text, flags=re.S)
    text = re.sub(r'<script id="maxess-results-v21-authority-js">.*?</script>\s*', '', text, flags=re.S)
    text = re.sub(r'<style id="maxess-results-v21-canonical-css">.*?</style>\s*', '', text, flags=re.S)
    text = re.sub(r'<script id="maxess-results-v21-canonical-js">.*?</script>\s*', '', text, flags=re.S)
    return text


def repair_recognition(text: str) -> str:
    start = text.find('<script id="maxess-recognition-flow-10-4-js">')
    if start < 0:
        return text
    end = text.find('</script>', start)
    if end < 0:
        raise RuntimeError('Recognition flow script closing tag missing')
    block = text[start:end + len('</script>')]
    pattern = re.compile(r"\n\s*const s=document\.createElement\('style'\);s\.id='maxess-recognition-flow-10-4';s\.textContent=.*?document\.head\.appendChild\(s\);\n", re.S)
    block2 = pattern.sub('\n', block)
    if block2 == block and "document.createElement('style')" in block:
        raise RuntimeError('Recognition runtime CSS injection was not removed')
    return text[:start] + block2 + text[end + len('</script>'):]


def validate_fragment(js_text: str) -> None:
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as fh:
        fh.write(js_text)
        path = fh.name
    proc = subprocess.run(['node','--check',path],capture_output=True,text=True)
    Path(path).unlink(missing_ok=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip())


def main() -> int:
    if not BASELINE.exists():
        print('ERROR: BASELINE-WORKING.html missing'); return 2
    baseline = BASELINE.read_text(encoding='utf-8')
    text = repair_recognition(remove_old_v21(baseline))
    js_body = re.search(r'<script id="maxess-results-v21-canonical-js">(.*?)</script>', JS, re.S).group(1)
    validate_fragment(js_body)
    candidate = text
    insertion = CSS + '\n' + JS
    candidate = candidate.replace('</body>', insertion + '\n</body>', 1) if '</body>' in candidate else candidate + '\n' + insertion
    if candidate.count(MARKER) != 1:
        print(f'ERROR: canonical V21 marker count = {candidate.count(MARKER)}'); return 3
    if candidate.count('id="maxess-results-v21-canonical-css"') != 1:
        print('ERROR: canonical V21 CSS marker incorrect'); return 4
    SOURCE.write_text(candidate,encoding='utf-8')
    REPORT.write_text('\n'.join([
        '# MAXESS V21 — CANONICAL BUILD',
        '',
        f'- Baseline SHA-256: `{sha_text(baseline)}`',
        f'- Candidate SHA-256: `{sha_text(candidate)}`',
        f'- Candidate lines: `{len(candidate.splitlines())}`',
        '- Canonical V21 JS syntax: `PASS`',
        '- Recognition 10.4 runtime CSS injection: `REMOVED`',
        '- Previous V21 layers: `REMOVED BEFORE REBUILD`',
        '- Runtime source of truth: `window.MAXESS_RESULT`',
        '- Production user score hard-coding: `NONE`',
    ])+'\n',encoding='utf-8')
    print('V21 CANONICAL BUILD COMPLETE')
    print(f'Baseline SHA-256: {sha_text(baseline)}')
    print(f'Candidate SHA-256: {sha_text(candidate)}')
    print(f'Lines: {len(candidate.splitlines())}')
    print('Canonical V21 JS syntax: PASS')
    print('Recognition 10.4 runtime CSS injection: REMOVED')
    print('Previous V21 layers: REMOVED BEFORE REBUILD')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
