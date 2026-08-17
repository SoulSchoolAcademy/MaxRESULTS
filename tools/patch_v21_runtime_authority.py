#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'tools' / 'build_v21_canonical.py'

s = BUILDER.read_text(encoding='utf-8')
old = "  function boot(){ build(result()); }\n  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',boot,{once:true}); else boot();"
new = """  function enforce(){
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
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',boot,{once:true}); else boot();"""
if old not in s:
    raise SystemExit('V21 boot block not found')
s = s.replace(old,new,1)
BUILDER.write_text(s,encoding='utf-8')
print('V21 RUNTIME AUTHORITY PATCH APPLIED')
print('Late boot: ON')
print('Post-load rechecks: ON')
print('MutationObserver dominance: ON')
