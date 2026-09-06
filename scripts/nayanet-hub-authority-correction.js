/* NayaNET Intelligent Hub — canonical architecture correction + 10/10 presentation pass
   Surgical overlay for the current NAYAHUB.html source.
   Authority: NAYAHUB.html on main. Older G7/B7/V7 artifacts are historical only.
*/
(()=>{'use strict';
const Q=(s,r=document)=>r.querySelector(s),QA=(s,r=document)=>[...r.querySelectorAll(s)];
const clean=s=>String(s||'').replace(/\s+/g,' ').trim();
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]||c));
const key=s=>'nh-intel-'+clean(s).toLowerCase().replace(/[^a-z0-9]+/g,'-').slice(0,90);
function state(){try{return JSON.parse(localStorage.getItem('nayanet_intelligent_blocks_v2')||'{}')}catch(e){return {}}}
function saveState(s){try{localStorage.setItem('nayanet_intelligent_blocks_v2',JSON.stringify(s))}catch(e){}}
function css(){if(Q('#nh-authority-correction-style'))return;const s=document.createElement('style');s.id='nh-authority-correction-style';s.textContent=`
/* FRONT DOOR — Smart Notes. Today is a destination, never a competing feed. */
#page-home .heroIntro,#page-home .hero,#page-home .nh-v11-today,#page-home #nhV11Today{display:none!important}
/* Remove the old Home identity wherever the current shell exposes it. */
.topbar .crumb strong{font-size:0!important}.topbar .crumb strong:after{content:'SMART NOTES';font-size:16px;letter-spacing:-.02em}
/* The positioning statement is one centered premium quote, above search, never repeated. */
.nh-authority-quote{display:block;max-width:1120px;margin:18px auto 25px!important;padding:8px 24px 10px!important;border:0!important;background:none!important;color:#f7f3fb!important;text-align:center;font-size:clamp(18px,2.05vw,29px)!important;line-height:1.22!important;letter-spacing:-.035em!important;font-weight:800!important;box-shadow:none!important}
.nh-authority-quote:before{content:'“';color:#9b6cff;font-size:1.45em;line-height:0;vertical-align:-.18em;margin-right:4px}.nh-authority-quote:after{content:'”';color:#9b6cff;font-size:1.45em;line-height:0;vertical-align:-.18em;margin-left:4px}
.nh-authority-quote span{display:none!important}
#page-home .homeWorkspace,#page-home .homeFeed{position:relative}
#page-home .intelligentFeedHead{padding-top:0!important;margin-top:0!important}
#page-home .intelligentFeedHead h2{font-size:clamp(30px,3vw,42px)!important;letter-spacing:-.06em!important}
#page-home .intelligentFeedHead p{max-width:820px!important;font-size:12px!important;line-height:1.6!important}
/* 10/10 block treatment: hierarchy, breathing room, compression, and unmistakable actions. */
#page-home .intelligentBlock{position:relative!important;margin:0 0 16px!important;padding:38px 34px 28px!important;border:1px solid #ffffff1b!important;border-radius:25px!important;background:radial-gradient(850px 360px at 82% 0%,color-mix(in srgb,var(--tone,#9b6cff) 10%,transparent),transparent 65%),linear-gradient(145deg,#15141b,#08080c)!important;box-shadow:inset 0 1px #fff5,0 25px 58px #000d!important;overflow:visible!important;transition:.26s cubic-bezier(.16,.84,.22,1)!important}
#page-home .intelligentBlock:hover{transform:translateY(-4px)!important;border-color:color-mix(in srgb,var(--tone,#9b6cff) 58%,#fff 8%)!important;box-shadow:inset 0 1px #fff7,0 34px 75px #000e,0 0 42px color-mix(in srgb,var(--tone,#9b6cff) 13%,transparent)!important}
#page-home .intelligentBlock .blockHeader{margin-bottom:22px!important}
#page-home .intelligentBlock .blockTitle h3{font-size:clamp(27px,3vw,43px)!important;line-height:1.02!important;letter-spacing:-.055em!important;max-width:930px!important}
#page-home .intelligentBlock .blockBody{margin-bottom:21px!important;padding-bottom:21px!important}
#page-home .intelligentBlock .blockBody p{font-size:16px!important;line-height:1.72!important;max-width:950px!important;color:#eeeaf1!important}
#page-home .nh-authority-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:18px;padding-top:16px;border-top:1px solid #ffffff13}
#page-home .nh-authority-actions button{min-height:46px;padding:0 15px;border:1px solid #8b63ff80;border-radius:12px;background:linear-gradient(145deg,#191121,#08080c);color:#f2edf7;font-size:8px;font-weight:1000;letter-spacing:.055em;box-shadow:inset 0 1px #fff5,0 8px 18px #000a,0 0 14px #8b63ff12;transition:.2s cubic-bezier(.16,.84,.22,1)}
#page-home .nh-authority-actions button:hover{transform:translateY(-3px);border-color:#c18aff;background:linear-gradient(145deg,#2a1237,#0b080f);box-shadow:inset 0 1px #fff8,0 15px 30px #000c,0 0 30px #b56cff42}
#page-home .nh-authority-actions button.on{border-color:#55e39a;color:#caffdd;box-shadow:0 0 24px #55e39a28,inset 0 1px #fff6}
.nh-authority-fav{position:absolute;right:16px;top:15px;width:45px;height:45px;border-radius:13px;border:1px solid #b06cff88;background:#0a080e;color:#eee8f2;font-size:22px;display:grid;place-items:center;z-index:8;cursor:pointer;box-shadow:0 0 22px #a65cff18;transition:.2s ease}
.nh-authority-fav:hover,.nh-authority-fav.on{transform:scale(1.08);border-color:#d86cff;background:#28102f;color:#fff;box-shadow:0 0 34px #d86cff52}
/* Today uses the exact same Intelligent Block visual language — no second-rate card system. */
#page-intelligence-today{padding-top:30px}
.nh-today-head{display:flex;justify-content:space-between;align-items:end;gap:20px;margin-bottom:20px}
.nh-today-kicker{color:#d6a4ff;font-size:7px;font-weight:1000;letter-spacing:.18em;text-transform:uppercase}
.nh-today-head h1{font-size:clamp(42px,5vw,66px);line-height:.9;letter-spacing:-.07em;margin:7px 0 10px}
.nh-today-head p{max-width:780px;color:#cfc9d5;font-size:12px;line-height:1.6;margin:0}
.nh-today-grid{display:grid;gap:16px}
#page-intelligence-today .nh-today-card{position:relative;margin:0;padding:38px 34px 28px;border:1px solid #ffffff1b;border-radius:25px;background:radial-gradient(850px 360px at 82% 0%,#9b6cff10,transparent 65%),linear-gradient(145deg,#15141b,#08080c);box-shadow:inset 0 1px #fff5,0 25px 58px #000d;overflow:hidden;transition:.26s cubic-bezier(.16,.84,.22,1)}
#page-intelligence-today .nh-today-card:hover{transform:translateY(-4px);border-color:#b68cff88;box-shadow:inset 0 1px #fff7,0 34px 75px #000e,0 0 42px #a55cff22}
#page-intelligence-today .nh-today-card .meta{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:20px;color:#8f8996;font-size:7px;font-weight:1000;letter-spacing:.1em}
#page-intelligence-today .nh-today-card .meta b{color:#d6a7ff}
#page-intelligence-today .nh-today-card h2{font-size:clamp(27px,3vw,43px);line-height:1.02;letter-spacing:-.055em;margin:0 0 15px;max-width:930px}
#page-intelligence-today .nh-today-card .nutshell{font-size:16px;line-height:1.72;color:#eeeaf1;margin:0 0 20px;max-width:950px}
#page-intelligence-today .nh-today-card .why{padding:15px 16px;border:1px solid #ffffff14;border-radius:14px;background:#07070b;color:#bdb6c5;font-size:10px;line-height:1.6;margin-bottom:17px;max-width:950px}
#page-intelligence-today .nh-today-card .why strong{display:block;color:#d5a4ff;font-size:7px;letter-spacing:.16em;margin-bottom:6px}
#page-intelligence-today .nh-today-card .open{min-height:43px;padding:0 15px;border:1px solid #b06cff78;border-radius:12px;background:linear-gradient(145deg,#191121,#08080c);color:#fff;font-size:8px;font-weight:1000;letter-spacing:.07em;transition:.2s ease}
#page-intelligence-today .nh-today-card .open:hover{transform:translateY(-3px);border-color:#d86cff;box-shadow:0 0 28px #d86cff38}
.nh-today-empty{padding:45px 20px;border:1px dashed #ffffff22;border-radius:20px;text-align:center;color:#aaa4b1;font-size:11px;line-height:1.6}
@media(max-width:760px){
 .main{padding-left:16px!important;padding-right:16px!important}
 .topbar .crumb strong:after{font-size:14px}
 .nh-authority-quote{max-width:650px;margin:14px auto 20px!important;padding:4px 10px 7px!important;font-size:clamp(18px,5.4vw,23px)!important;line-height:1.28!important}
 #page-home .intelligentBlock{padding:29px 15px 24px!important;border-radius:20px!important}
 #page-home .intelligentBlock .blockTitle h3{font-size:28px!important;padding-right:52px!important}
 #page-home .intelligentBlock .blockBody p{font-size:15px!important}
 #page-home .nh-authority-actions button{flex:1 1 calc(50% - 8px);min-height:48px}
 .nh-authority-fav{right:11px;top:11px;width:42px;height:42px}
 .nh-today-head{display:block}.nh-today-head h1{font-size:44px}
 #page-intelligence-today .nh-today-card{padding:29px 15px 24px;border-radius:20px}
 #page-intelligence-today .nh-today-card h2{font-size:28px;padding-right:45px}
 #page-intelligence-today .nh-today-card .nutshell{font-size:15px}
}
`;
document.head.appendChild(s)}
function labelHome(){QA('[data-page="home"]').forEach(b=>{b.classList.add('nh-authority-nav');const ico=Q('.ico',b),badge=Q('.badge',b);b.innerHTML='';if(ico)b.appendChild(ico);b.appendChild(document.createTextNode('Smart Notes'));if(badge)b.appendChild(badge)})}
function removeDuplicateQuotes(){QA('.nh-authority-quote').forEach((x,i)=>{if(i)x.remove()})}
function addTodayNav(){const nav=Q('.nav');if(!nav)return;let b=Q('[data-page="intelligence-today"]');if(!b){b=document.createElement('button');b.type='button';b.dataset.page='intelligence-today';b.className='nh-authority-nav';b.innerHTML='<span class="ico">✨</span><span>Your Intelligence Today</span>';const home=Q('[data-page="home"]',nav);if(home)home.insertAdjacentElement('afterend',b);else nav.appendChild(b);b.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();activateToday(b)},true)}}
function createTodayPage(){if(Q('#page-intelligence-today'))return;const main=Q('.main');if(!main)return;const p=document.createElement('section');p.id='page-intelligence-today';p.className='page';p.innerHTML='<div class="nh-today-head"><div><div class="nh-today-kicker">DAILY HIGHLIGHTS</div><h1>Your Intelligence Today</h1><p>The day distilled from the same Smart Notes and Intelligent Blocks that power your Hub — what happened, what mattered, what you learned, what connects, and what deserves attention next.</p></div></div><div class="nh-today-grid" id="nhTodayGrid"></div>';const anchor=Q('#page-home');if(anchor)anchor.insertAdjacentElement('afterend',p);else main.appendChild(p)}
function sourceItems(){const home=Q('#page-home');if(!home)return[];let items=QA('.homeFeed .intelligentBlock',home);if(!items.length)items=QA('.homeFeed .note',home);return items}
function buildToday(){const grid=Q('#nhTodayGrid');if(!grid)return;const items=sourceItems();grid.innerHTML='';if(!items.length){grid.innerHTML='<div class="nh-today-empty">Your Intelligence Today will populate from the Smart Notes you create. The underlying feed remains the source of truth.</div>';return}
items.slice(0,6).forEach((item,i)=>{const title=clean(Q('.blockTitle h3',item)?.textContent||Q('h3',item)?.textContent)||'Intelligent Event';const body=clean(Q('.blockBody p',item)?.textContent||Q('p',item)?.textContent)||'Captured intelligence from your life, distilled into something worth remembering and using.';const clone=item.cloneNode(true);clone.className='nh-today-card';clone.removeAttribute('id');QA('.nh-authority-fav,.nh-authority-actions,.nh-excellence-fav,.nh-excellence-actions',clone).forEach(x=>x.remove());const head=Q('.blockTitle h3',clone);const bodyP=Q('.blockBody p',clone);if(head)head.textContent=title;if(bodyP)bodyP.textContent=body;const oldBody=Q('.blockBody',clone);if(oldBody){QA('.nh-excellence',oldBody).forEach(x=>x.remove())}
clone.innerHTML='<div class="meta"><b>'+(i===0?'WHAT MATTERS':'HIGHLIGHT')+'</b><span>·</span><span>SMART NOTE</span></div>'+clone.innerHTML+'<div class="nh-today-action"><button class="open" type="button">OPEN IN SMART NOTES →</button></div>';
const open=Q('.open',clone);if(open)open.addEventListener('click',()=>{activateHome();item.scrollIntoView({behavior:'smooth',block:'center'});item.animate([{boxShadow:'0 0 0 0 #d86cff00'},{boxShadow:'0 0 0 8px #d86cff55'},{boxShadow:'0 0 0 0 #d86cff00'}],{duration:900})});grid.appendChild(clone)})}
function activateHome(){const b=Q('[data-page="home"]');QA('.page').forEach(p=>p.classList.toggle('active',p.id==='page-home'));QA('.nav button').forEach(x=>x.classList.toggle('active',x===b));const t=Q('#pageTitle');if(t)t.textContent='Smart Notes'}
function activateToday(b){QA('.page').forEach(p=>p.classList.toggle('active',p.id==='page-intelligence-today'));QA('.nav button').forEach(x=>x.classList.toggle('active',x===b));const t=Q('#pageTitle');if(t)t.textContent='Your Intelligence Today';buildToday()}
function quote(){const home=Q('#page-home');if(!home)return;removeDuplicateQuotes();if(Q('#nhAuthorityQuote'))return;const q=document.createElement('div');q.id='nhAuthorityQuote';q.className='nh-authority-quote';q.innerHTML='Your life creates intelligence every day. Naya helps you capture it, understand it, remember it, compound it, and use it.';const search=Q('.search',home);const feed=Q('.homeWorkspace',home)||Q('.homeFeed',home);if(search)search.insertAdjacentElement('beforebegin',q);else if(feed)feed.insertAdjacentElement('beforebegin',q);else home.prepend(q)}
function feedHeading(){const home=Q('#page-home');if(!home)return;const h=Q('.homeFeed .intelligentFeedHead h2',home);const p=Q('.homeFeed .intelligentFeedHead p',home);if(h)h.textContent='SMART NOTES · INTELLIGENT BLOCKS';if(p)p.textContent='The intelligence you created, distilled by Naya, and ready to remember, use, and compound.'}
function actions(){const home=Q('#page-home');if(!home)return;const items=QA('.homeFeed .intelligentBlock',home);items.forEach((item,i)=>{const title=clean(Q('.blockTitle h3',item)?.textContent)||('intelligence-'+i);if(!Q('.nh-authority-fav',item)&&!Q('.nh-excellence-fav',item)){const f=document.createElement('button');f.className='nh-authority-fav';f.type='button';f.textContent='☆';f.title='Favorite this intelligence';const k=key(title);const paint=()=>{const st=state();const on=!!(st.favorites&&st.favorites[k]);f.classList.toggle('on',on);f.textContent=on?'★':'☆'};f.onclick=()=>{const st=state();st.favorites=st.favorites||{};st.favorites[k]=!st.favorites[k];saveState(st);paint()};item.appendChild(f);paint()}
if(!Q('.nh-authority-actions',item)&&!Q('.nh-excellence-actions',item)){const a=document.createElement('div');a.className='nh-authority-actions';a.innerHTML='<button data-act="share">＋ SHARE</button><button data-act="like">👍 LIKE</button><button data-act="love">♥ LOVE</button><button data-act="rank">★ RANK</button><button data-act="comment">💬 COMMENT</button><button data-act="save">🔖 SAVE</button>';item.appendChild(a);a.querySelectorAll('button').forEach(btn=>{const act=btn.dataset.act;const k=key(title)+'-'+act;btn.addEventListener('click',()=>{if(act==='share'||act==='comment'){btn.classList.add('on');setTimeout(()=>btn.classList.remove('on'),650);return}const st=state();st.actions=st.actions||{};st.actions[k]=!st.actions[k];saveState(st);btn.classList.toggle('on',!!st.actions[k])})})}})}
function run(){css();labelHome();addTodayNav();createTodayPage();quote();feedHeading();actions();buildToday()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(run,120));else setTimeout(run,120);setTimeout(run,900);setTimeout(run,1800);setTimeout(run,3000);
})();
