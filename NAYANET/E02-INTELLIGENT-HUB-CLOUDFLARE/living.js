"use strict";
(() => {
  const $ = s => document.querySelector(s);
  const $$ = s => [...document.querySelectorAll(s)];
  const reduced = window.matchMedia?.("(prefers-reduced-motion: reduce)").matches;
  const toast = text => { const t=$("#toast"); if(!t)return; t.textContent=text; t.classList.add("show"); clearTimeout(toast.t); toast.t=setTimeout(()=>t.classList.remove("show"),2400); };
  const setState=(el,name)=>{ if(!el)return; el.dataset.state=name; ["aware","hovering","active","opening","working","complete"].forEach(x=>el.classList.remove("is-"+x)); const c={AWARE:"aware",HOVER:"hovering",ACTIVE:"active",OPENING:"opening",WORKING:"working",COMPLETE:"complete"}[name]; if(c)el.classList.add("is-"+c); };
  function bind(){
    $$(".node").forEach(n=>{
      n.addEventListener("focus",()=>setState(n,"AWARE"));
      n.addEventListener("mouseenter",()=>setState(n,"HOVER"));
      n.addEventListener("mouseleave",()=>{if(!n.classList.contains("active"))setState(n,"AWARE")});
      n.addEventListener("click",()=>{setState(n,"OPENING");setTimeout(()=>setState(n,"ACTIVE"),reduced?20:180);try{const j=JSON.parse(localStorage.getItem("nayanetJourney")||"{}");localStorage.setItem("nayanetJourney",JSON.stringify({...j,active:n.dataset.id,updatedAt:new Date().toISOString()}));}catch(e){}});
    });
    try{
      const j=JSON.parse(localStorage.getItem("nayanetJourney")||"null");
      if(j?.name&&!$(".resume-chip")){const w=$(".arrival");if(w){const c=document.createElement("div");c.className="resume-chip";c.innerHTML=`<span>◉</span><span>Welcome back, <strong>${j.name}</strong></span><button type="button">RESUME</button>`;w.appendChild(c);c.querySelector("button").onclick=()=>{$("#nameInput").value=j.name;$("#enterBtn").click();toast(j.active?"Returning to your intelligence journey.":"Welcome back.");if(j.active)setTimeout(()=>document.querySelector(`[data-id="${j.active}"]`)?.click(),700);};}}
    }catch(e){}
    const nav=$(".bottom-nav");
    if(nav&&!$("#powerBtn")){const b=document.createElement("button");b.id="powerBtn";b.className="nav-btn";b.type="button";b.textContent="Power Player";nav.insertBefore(b,$("#maxessBtn"));b.onclick=openPlayer;}
  }
  function openPlayer(){
    if(!$("#powerPlayer")){const p=document.createElement("section");p.id="powerPlayer";p.className="power-player";p.setAttribute("aria-hidden","true");p.innerHTML=`<div class="player-head"><div><div class="detail-kicker">NAYA POWER · THE HEARTBEAT</div><h2>Power Player</h2><p>18 real Powercasts. Learn with Naya. Let intelligence compound.</p></div><button id="closePlayer" class="close" type="button" aria-label="Close Power Player">×</button></div><div class="player-body"><div class="player-intent"><span class="player-orb">☀</span><div><strong>Choose what you need next.</strong><span>Listen, explore, then carry the useful idea forward.</span></div></div><div class="powercast-list"><p class="player-empty">The Power Player shell is live. The 18 source-linked Powercasts remain the canonical library and will be surfaced here without duplicating or rewriting their source assets.</p></div></div>`;$("#hubShell").appendChild(p);$("#closePlayer").onclick=()=>{p.classList.remove("open");p.setAttribute("aria-hidden","true");$("#scrim")?.classList.remove("show");};}
    const p=$("#powerPlayer");p.classList.add("open");p.setAttribute("aria-hidden","false");$("#scrim")?.classList.add("show");toast("The Naya Power heartbeat is open.");
  }
  if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",bind,{once:true});else bind();
})();
