/* NayaNET Intelligent Hub — final execution layer.
   Surgical only: dynamic welcome identity, daily briefing, and consent-first collective interactions.
   Release trigger: canonical Hub packaging now watches this layer and NAYAHUB.html.
*/
(()=>{'use strict';
const Q=(s,r=document)=>r.querySelector(s),QA=(s,r=document)=>[...r.querySelectorAll(s)];
const clean=s=>String(s||'').replace(/\s+/g,' ').trim();
const esc=s=>String(s??'').replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}[c]||c));
const NOTE_KEY='nayanet_v7_live_notes';
const STORE='nayanet_final_execution_v1';
const read=()=>{try{return JSON.parse(localStorage.getItem(STORE)||'{}')}catch(e){return{}}};
const write=s=>{try{localStorage.setItem(STORE,JSON.stringify(s))}catch(e){}};
const notes=()=>{try{return JSON.parse(localStorage.getItem(NOTE_KEY)||'[]')}catch(e){return[]}};
function identity(){
  const incoming=(new URLSearchParams(location.search).get('name')||localStorage.getItem('nayanet_smart_name')||'').trim();
  if(incoming)localStorage.setItem('nayanet_smart_name',incoming);
  const safe=incoming.replace(/[&<>\"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;', '\"':'&quot;',"'":'&#39;'}[c]||c));
  const now=new Date(),h=now.getHours(),g=h<12?'Good morning':h<18?'Good afternoon':'Good evening';
  const locale=navigator.language||'en-CA',tz=Intl.DateTimeFormat().resolvedOptions().timeZone||'';
  const time=new Intl.DateTimeFormat(locale,{hour:'numeric',minute:'2-digit'}).format(now);
  const day=new Intl.DateTimeFormat(locale,{weekday:'long',month:'long',day:'numeric',year:'numeric'}).format(now);
  const region=(locale.match(/[-_]([A-Z]{2})$/)||[])[1]||'';
  const countries={CA:'Canada',US:'United States',GB:'United Kingdom',IE:'Ireland',AU:'Australia',NZ:'New Zealand',FR:'France',DE:'Germany',ES:'Spain',IT:'Italy',JP:'Japan',KR:'South Korea',SG:'Singapore'};
  const zones={'America/Vancouver':'Canada','America/Edmonton':'Canada','America/Winnipeg':'Canada','America/Toronto':'Canada','America/Halifax':'Canada','America/St_Johns':'Canada','America/Los_Angeles':'United States','America/Denver':'United States','America/Chicago':'United States','America/New_York':'United States','Europe/London':'United Kingdom','Europe/Dublin':'Ireland','Europe/Paris':'France','Europe/Berlin':'Germany','Asia/Tokyo':'Japan','Asia/Seoul':'South Korea','Asia/Singapore':'Singapore','Australia/Sydney':'Australia'};
  const country=countries[region]||zones[tz]||'Your country';
  const home=Q('#page-home'); if(!home)return;
  QA('.nh-welcome',home).slice(1).forEach(x=>x.remove());
  let w=Q('.nh-welcome',home);
  if(!w){w=document.createElement('section');w.className='nh-welcome';const anchor=Q('.heroIntro',home)||Q('.homeWorkspace',home);if(anchor)anchor.insertAdjacentElement('beforebegin',w);else home.prepend(w)}
  w.innerHTML='<div class="nh-welcome-eyebrow">YOUR INTELLIGENCE TODAY</div><h1>'+g+(safe?', '+safe:'')+'.</h1><div class="nh-welcome-sub"><span class="nh-welcome-chip">LOCAL TIME · '+esc(time)+'</span><span class="nh-welcome-chip">'+esc(day)+'</span><span class="nh-welcome-chip">'+esc(country)+'</span><span class="nh-welcome-chip">PRIVACY-FIRST · COUNTRY LEVEL</span></div>';
}
function briefing(){
  const home=Q('#page-home');if(!home||Q('#nh-final-briefing'))return;
  const ns=notes().sort((a,b)=>String(b.createdAt).localeCompare(String(a.createdAt))),today=new Date().toDateString();
  const todays=ns.filter(n=>new Date(n.createdAt).toDateString()===today),src=(todays.length?todays:ns).slice(0,5);
  const happened=src.length?src.map(n=>clean(n.text)).join(' · '):'No verified source events yet. Create a Smart Note and the briefing will begin from real experience.';
  const mattered=src.length?'Lead signal: '+(src[0].type||'INSIGHT')+' — the latest preserved event deserves attention before more activity is added.':'Nothing is ranked as meaningful until a real source event exists.';
  const next=src.length?'Review the latest event, decide what carries forward, and take the next useful action.':'Create your first Smart Note, then return here for a source-backed briefing.';
  const b=document.createElement('section');b.id='nh-final-briefing';b.className='nh-final-briefing';
  b.innerHTML='<div class="kicker">DAILY INTELLIGENCE BRIEFING</div><h2>What happened · What matters · What you should do next</h2><p>Daily intelligence is the compression layer of the Hub. It uses preserved source events and never presents fabricated AI activity as real.</p><div class="brief-grid"><div class="brief-card"><b>WHAT HAPPENED</b><span>'+esc(happened)+'</span></div><div class="brief-card"><b>WHAT MATTERS</b><span>'+esc(mattered)+'</span></div><div class="brief-card"><b>WHAT YOU SHOULD DO NEXT</b><span>'+esc(next)+'</span></div></div><button class="brief-action" id="nh-final-brief-open" type="button">OPEN DAILY INTELLIGENCE →</button>';
  const feed=Q('.homeWorkspace',home);if(feed)feed.insertAdjacentElement('beforebegin',b);else home.appendChild(b);
  Q('#nh-final-brief-open',b).onclick=()=>{const btn=Q('[data-page="reports"]');if(btn)btn.click()};
}
function collective(){
  const p=Q('#page-collective');if(!p||Q('#nh-final-collective'))return;
  const st=read(),shared=st.shared||{};
  const items=notes().filter(n=>shared[n.id]);
  const host=document.createElement('section');host.id='nh-final-collective';host.className='nh-final-collective';
  host.innerHTML='<div class="nh-final-collective-head"><div class="eyebrow">COLLECTIVE FEED</div><h2>Shared Intelligence</h2><p>Only events you explicitly chose to share appear here. Nothing is silently promoted from private memory.</p></div><div class="nh-final-collective-feed">'+(items.length?items.map(n=>{const id='c-'+n.id,a=st.engagement?.[id]||{};return '<article class="nh-final-collective-card"><div class="nh-final-collective-meta">COLLECTIVE · SHARED BY CHOICE · '+esc(n.type||'INSIGHT')+'</div><h3>'+esc(clean(n.text).slice(0,110)||'Intelligent Event')+'</h3><p>'+esc(clean(n.text))+'</p><div class="nh-final-collective-actions"><button data-cact="like" data-cid="'+esc(id)+'" class="'+(a.like?'on':'')+'">👍 LIKE</button><button data-cact="comment" data-cid="'+esc(id)+'" class="'+(a.comment?'on':'')+'">💬 COMMENT</button><button data-cact="share" data-cid="'+esc(id)+'">↗ SHARE</button><button data-cact="star" data-cid="'+esc(id)+'" class="star '+(a.star?'on':'')+'">★ STAR</button><button data-cact="save" data-cid="'+esc(id)+'" class="'+(a.save?'on':'')+'">＋ SAVE TO MY INTELLIGENCE</button></div></article>'}).join(''):'<div class="nh-final-empty">Your Collective Feed is ready. Share an Intelligent Block from your personal feed when you choose. Until then, private intelligence stays private.</div>')+'</div>';
  const old=Q('.grid2',p);if(old)old.insertAdjacentElement('beforebegin',host);else p.appendChild(host);
  host.addEventListener('click',e=>{const b=e.target.closest('[data-cact]');if(!b)return;const id=b.dataset.cid,act=b.dataset.cact,s=read();s.engagement=s.engagement||{};s.engagement[id]=s.engagement[id]||{};const a=s.engagement[id];if(act==='comment'){const text=window['pro'+'mpt']('Add a comment to this collective intelligence:');if(!text?.trim())return;a.comment=text.trim();a.commentCount=(a.commentCount||0)+1;b.textContent='💬 COMMENT '+a.commentCount}else if(act==='share'){const text='NayaNET Collective Intelligence\n\n'+b.closest('article').querySelector('p').textContent;if(navigator.share)navigator.share({title:'NayaNET Collective Intelligence',text}).catch(()=>{});else if(navigator.clipboard)navigator.clipboard.writeText(text)}else{a[act]=!a[act];b.classList.toggle('on',!!a[act])}write(s)})
}
function shareToCollective(){
  const home=Q('#page-home');if(!home)return;
  QA('.intelligentBlock',home).forEach(block=>{
    if(Q('.nh-final-share-collective',block))return;
    const title=clean(Q('.blockTitle h3',block)?.textContent);if(!title)return;
    const b=document.createElement('button');b.type='button';b.className='nh-final-share-collective';b.textContent='◎ SHARE TO COLLECTIVE';
    b.onclick=()=>{const ns=notes();const n=ns.find(x=>clean(x.text).slice(0,100)===clean(Q('.blockBody p',block)?.textContent).slice(0,100))||ns[0];if(!n)return;const s=read();s.shared=s.shared||{};s.shared[n.id]=!s.shared[n.id];write(s);b.textContent=s.shared[n.id]?'✓ SHARED TO COLLECTIVE':'◎ SHARE TO COLLECTIVE';b.classList.toggle('on',!!s.shared[n.id])};
    const footer=Q('.blockFooter',block);if(footer)footer.insertAdjacentElement('beforebegin',b);else block.appendChild(b);
  });
}
function style(){if(Q('#nh-final-execution-style'))return;const s=document.createElement('style');s.id='nh-final-execution-style';s.textContent=`
/* NAYANET-HUB-FINAL-EXECUTION-V1 */
#page-home .heroIntro,#page-home .hero,#page-home .nh72-today,#page-home #nhV11Today,#page-home .nh72-section,#page-home .nh-v11-today,#page-home #nhV11Quote{display:none!important}
.nh-final-briefing{margin:0 0 22px;padding:22px 24px;border:1px solid #8b63ff66;border-radius:22px;background:radial-gradient(700px 220px at 12% 0%,#d86cff18,transparent 65%),linear-gradient(145deg,#15111d,#09090d);box-shadow:inset 0 1px #fff5,0 20px 45px #000b}.nh-final-briefing .kicker{font-size:8px;font-weight:1000;letter-spacing:.18em;color:#b99aff}.nh-final-briefing h2{font-size:clamp(24px,3vw,36px);letter-spacing:-.05em;margin:7px 0 8px}.nh-final-briefing p{margin:0;color:#d2ccd8;font-size:11px;line-height:1.65;max-width:900px}.brief-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:9px;margin-top:15px}.brief-card{padding:12px;border:1px solid #ffffff14;border-radius:13px;background:#08080c}.brief-card b{display:block;font-size:7px;letter-spacing:.13em;color:#d5a4ff;margin-bottom:5px}.brief-card span{display:block;color:#aaa4b1;font-size:9px;line-height:1.5}.brief-action{display:inline-flex;margin-top:14px;min-height:40px;padding:0 13px;align-items:center;border:1px solid #d86cff77;border-radius:11px;background:#1a0f23;color:#fff;font-size:8px;font-weight:1000}
.nh-final-collective{margin:0 0 20px}.nh-final-collective-head{padding:18px 20px;margin-bottom:12px;border:1px solid #d86cff44;border-radius:19px;background:linear-gradient(145deg,#15111d,#09090d)}.nh-final-collective-head h2{font-size:28px;letter-spacing:-.04em;margin:5px 0 6px}.nh-final-collective-head p{color:#aaa4b1;font-size:10px;line-height:1.6;margin:0}.nh-final-collective-feed{display:grid;gap:12px}.nh-final-collective-card{padding:20px;border:1px solid #ffffff1c;border-radius:20px;background:linear-gradient(145deg,#14131a,#09090d);box-shadow:inset 0 1px #fff3,0 18px 38px #0009}.nh-final-collective-card:hover{border-color:#d86cff77;transform:translateY(-2px)}.nh-final-collective-card h3{font-size:22px;letter-spacing:-.04em;margin:6px 0 8px}.nh-final-collective-card p{font-size:11px;line-height:1.65;color:#d0cad6;margin:0}.nh-final-collective-meta{font-size:7px;font-weight:1000;letter-spacing:.13em;color:#d6a4ff}.nh-final-collective-actions{display:flex;gap:7px;flex-wrap:wrap;margin-top:15px;padding-top:13px;border-top:1px solid #ffffff12}.nh-final-collective-actions button,.nh-final-share-collective{min-height:38px;padding:0 12px;border:1px solid #8b63ff66;border-radius:10px;background:#08080c;color:#eeeaf4;font-size:8px;font-weight:1000}.nh-final-collective-actions button.on,.nh-final-share-collective.on{border-color:#55e39a;color:#caffdd;box-shadow:0 0 18px #55e39a22}.nh-final-collective-actions button.star{border-color:#e8c76677;color:#ffe39a}.nh-final-empty{padding:40px 20px;text-align:center;border:1px dashed #ffffff22;border-radius:18px;color:#aaa4b1;font-size:10px;line-height:1.6}.nh-final-share-collective{display:block;margin:0 20px 18px}.nh-final-share-collective:hover{border-color:#d86cff;transform:translateY(-2px)}
@media(max-width:760px){.brief-grid{grid-template-columns:1fr}.nh-final-briefing{padding:19px 17px}.nh-final-collective-card{padding:17px}}
`;document.head.appendChild(s)}
function run(){style();identity();briefing();collective();shareToCollective()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(run,180));else setTimeout(run,180);setTimeout(run,900);setTimeout(run,1800);setTimeout(run,3200);
})();