/* NayaNET Intelligent Hub — canonical architecture correction layer
   Surgical overlay for the current NAYAHUB.html source.
   Authority: NAYAHUB.html on main. Older G7/B7/V7 artifacts are historical only.
*/
(()=>{'use strict';
const Q=(s,r=document)=>r.querySelector(s), QA=(s,r=document)=>[...r.querySelectorAll(s)];
const clean=s=>String(s||'').replace(/\s+/g,' ').trim();
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]||c));
const key=s=>'nh-intel-'+clean(s).toLowerCase().replace(/[^a-z0-9]+/g,'-').slice(0,90);
function state(){try{return JSON.parse(localStorage.getItem('nayanet_intelligent_blocks_v2')||'{}')}catch(e){return {}}}
function saveState(s){try{localStorage.setItem('nayanet_intelligent_blocks_v2',JSON.stringify(s))}catch(e){}}
function css(){if(Q('#nh-authority-correction-style'))return;const s=document.createElement('style');s.id='nh-authority-correction-style';s.textContent=`
/* Canonical Hub architecture: Smart Notes is the front door; Today is a destination. */
#page-home .heroIntro,#page-home .hero{display:none!important}
#page-home .nh-v11-today{display:none!important}
.nh-authority-quote{margin:0 0 22px;padding:11px 15px;border-left:2px solid #9b6cff;border-top:1px solid #ffffff10;border-bottom:1px solid #ffffff10;background:linear-gradient(90deg,#120d19,#09090d 68%,transparent);color:#eeeaf3;font-size:12px;line-height:1.5;box-shadow:0 0 24px #8b63ff0b}
.nh-authority-quote span{display:block;margin-top:4px;color:#80798a;font-size:6px;font-weight:1000;letter-spacing:.18em;text-transform:uppercase}
.nh-authority-nav{border-color:#9b6cff55!important}
.nh-authority-nav:hover{border-color:#d86cff!important;box-shadow:0 12px 25px #0008,0 0 24px #d86cff25!important}
#page-intelligence-today{padding-top:34px}
.nh-today-head{display:flex;justify-content:space-between;align-items:end;gap:20px;margin-bottom:22px}
.nh-today-head h1{font-size:clamp(40px,5vw,64px);line-height:.9;letter-spacing:-.07em;margin:7px 0 10px}
.nh-today-head p{max-width:760px;color:#cfc9d5;font-size:12px;line-height:1.6;margin:0}
.nh-today-kicker{color:#d7a9ff;font-size:7px;font-weight:1000;letter-spacing:.18em}
.nh-today-grid{display:grid;gap:13px}
.nh-today-card{border:1px solid #ffffff1c;border-radius:21px;background:radial-gradient(600px 180px at 88% 0%,#8b63ff10,transparent 68%),linear-gradient(145deg,#15141b,#08080c);box-shadow:inset 0 1px #fff4,0 20px 44px #000b;padding:20px;transition:.22s cubic-bezier(.16,.84,.22,1)}
.nh-today-card:hover{transform:translateY(-3px);border-color:#b28dff88;box-shadow:inset 0 1px #fff6,0 27px 55px #000d,0 0 30px #8b63ff17}
.nh-today-card .meta{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:10px;color:#8f8996;font-size:7px;font-weight:1000;letter-spacing:.1em}
.nh-today-card .meta b{color:#d6a7ff}
.nh-today-card h2{font-size:23px;line-height:1.08;letter-spacing:-.045em;margin:0 0 9px}
.nh-today-card .nutshell{color:#e0dbe5;font-size:12px;line-height:1.65;margin:0 0 14px;max-width:900px}
.nh-today-card .why{padding:12px 13px;border:1px solid #ffffff12;border-radius:13px;background:#07070b;color:#aaa4b1;font-size:9px;line-height:1.55;margin-bottom:13px}
.nh-today-card .why strong{display:block;color:#d5a4ff;font-size:6px;letter-spacing:.16em;margin-bottom:5px}
.nh-today-card .open{min-height:36px;padding:0 12px;border:1px solid #9b6cff66;border-radius:11px;background:#100c17;color:#fff;font-size:7px;font-weight:1000;letter-spacing:.08em}
.nh-today-card .open:hover{border-color:#d86cff;box-shadow:0 0 20px #d86cff25;transform:translateY(-2px)}
.nh-today-empty{padding:45px 20px;border:1px dashed #ffffff22;border-radius:20px;text-align:center;color:#aaa4b1;font-size:11px;line-height:1.6}
#page-home .homeFeed .intelligentFeedHead{margin-top:0!important}
#page-home .homeFeed .intelligentFeedHead h2{font-size:31px!important;letter-spacing:-.06em!important}
#page-home .homeFeed .intelligentFeedHead p{max-width:760px!important;line-height:1.55!important}
#page-home .homeFeed .note,#page-home .homeFeed .intelligentBlock{position:relative}
.nh-authority-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:17px;padding-top:15px;border-top:1px solid #ffffff13}
.nh-authority-actions button{min-height:43px;padding:0 14px;border:1px solid #8b63ff70;border-radius:12px;background:linear-gradient(145deg,#17101f,#08080c);color:#eeeaf4;font-size:8px;font-weight:1000;letter-spacing:.045em;box-shadow:inset 0 1px #fff5,0 8px 18px #000a,0 0 12px #8b63ff0b;transition:.2s cubic-bezier(.16,.84,.22,1)}
.nh-authority-actions button:hover{transform:translateY(-3px);border-color:#d86cff;box-shadow:inset 0 1px #fff7,0 13px 28px #000c,0 0 27px #d86cff35}
.nh-authority-actions button.on{border-color:#55e39a;color:#caffdd;box-shadow:0 0 24px #55e39a25,inset 0 1px #fff6}
.nh-authority-fav{position:absolute;right:15px;top:13px;width:42px;height:42px;border-radius:12px;border:1px solid #9b6cff77;background:#09070d;color:#d9d0df;font-size:20px;display:grid;place-items:center;z-index:5;box-shadow:0 0 18px #9b6cff15;transition:.2s ease}
.nh-authority-fav:hover,.nh-authority-fav.on{transform:scale(1.06);border-color:#d86cff;background:#24102d;color:#fff;box-shadow:0 0 30px #d86cff45}
@media(max-width:760px){.nh-today-head{display:block}.nh-today-head h1{font-size:44px}.nh-authority-actions button{flex:1 1 auto}.nh-authority-quote{font-size:11px}}
`;
document.head.appendChild(s)}
function labelHome(){QA('[data-page="home"]').forEach(b=>{b.classList.add('nh-authority-nav');const ico=Q('.ico',b);const badge=Q('.badge',b);b.innerHTML='';if(ico)b.appendChild(ico);b.appendChild(document.createTextNode('Smart Notes'));if(badge)b.appendChild(badge)});}
function addTodayNav(){const nav=Q('.nav');if(!nav||Q('[data-page="intelligence-today"]'))return;const b=document.createElement('button');b.type='button';b.dataset.page='intelligence-today';b.className='nh-authority-nav';b.innerHTML='<span class="ico">✨</span><span>Your Intelligence Today</span>';const home=Q('[data-page="home"]',nav);if(home)home.insertAdjacentElement('afterend',b);else nav.appendChild(b);b.addEventListener('click',e=>{e.preventDefault();e.stopPropagation();activateToday(b)},true)}
function createTodayPage(){if(Q('#page-intelligence-today'))return;const main=Q('.main');if(!main)return;const p=document.createElement('section');p.id='page-intelligence-today';p.className='page';p.innerHTML='<div class="nh-today-head"><div><div class="nh-today-kicker">YOUR INTELLIGENCE TODAY</div><h1>Today, distilled.</h1><p>Your daily highlight reel from the same Smart Notes and Intelligent Blocks that power the Hub. What happened, what mattered, what you learned, what connects, and what deserves your attention next.</p></div></div><div class="nh-today-grid" id="nhTodayGrid"></div>';const anchor=Q('#page-home');if(anchor)anchor.insertAdjacentElement('afterend',p);else main.appendChild(p)}
function sourceItems(){const home=Q('#page-home');if(!home)return[];let items=QA('.homeFeed .intelligentBlock',home);if(!items.length)items=QA('.homeFeed .note',home);return items}
function buildToday(){const grid=Q('#nhTodayGrid');if(!grid)return;const items=sourceItems();grid.innerHTML='';if(!items.length){grid.innerHTML='<div class="nh-today-empty">Your Intelligence Today will populate from the Smart Notes you create. The underlying feed remains the source of truth.</div>';return}items.slice(0,6).forEach((item,i)=>{const title=clean(Q('h3',item)?.textContent)||'Intelligent Event';const ps=QA('p',item).map(x=>clean(x.textContent)).filter(Boolean);const nutshell=ps[0]||'Captured intelligence from your life, distilled into something worth remembering and using.';const card=document.createElement('article');card.className='nh-today-card';card.innerHTML='<div class="meta"><b>'+(i===0?'WHAT MATTERS':'HIGHLIGHT')+'</b><span>·</span><span>SMART NOTE</span></div><h2>'+esc(title)+'</h2><p class="nutshell">'+esc(nutshell.length>420?nutshell.slice(0,417).replace(/\s+\S*$/,'')+'…':nutshell)+'</p><div class="why"><strong>WHY IT MATTERS</strong>'+esc(i===0?'This is one of today’s strongest intelligence signals — a piece of understanding worth carrying forward and using.':'This becomes more valuable when connected to the decisions, actions, and patterns that follow.')+'</div><button class="open" type="button">OPEN IN SMART NOTES →</button>';card.querySelector('.open').addEventListener('click',()=>{activateHome();item.scrollIntoView({behavior:'smooth',block:'center'});item.animate([{boxShadow:'0 0 0 0 #d86cff00'},{boxShadow:'0 0 0 8px #d86cff55'},{boxShadow:'0 0 0 0 #d86cff00'}],{duration:900})});grid.appendChild(card)})}
function activateHome(){const b=Q('[data-page="home"]');QA('.page').forEach(p=>p.classList.toggle('active',p.id==='page-home'));QA('.nav button').forEach(x=>x.classList.toggle('active',x===b));const t=Q('#pageTitle');if(t)t.textContent='Smart Notes'}
function activateToday(b){QA('.page').forEach(p=>p.classList.toggle('active',p.id==='page-intelligence-today'));QA('.nav button').forEach(x=>x.classList.toggle('active',x===b));const t=Q('#pageTitle');if(t)t.textContent='Your Intelligence Today';buildToday()}
function quote(){const home=Q('#page-home');if(!home||Q('#nhAuthorityQuote'))return;const q=document.createElement('div');q.id='nhAuthorityQuote';q.className='nh-authority-quote';q.innerHTML='Your life creates intelligence every day. Naya helps you capture it, understand it, remember it, compound it, and use it.<span>NayaNET · Intelligent Hub</span>';const feed=Q('.homeWorkspace',home)||Q('.homeFeed',home);if(feed)feed.insertAdjacentElement('beforebegin',q);else home.prepend(q)}
function removeTodayFromHome(){QA('#page-home .nh-v11-today,#page-home [id="nhV11Today"]').forEach(x=>x.remove())}
function feedHeading(){const home=Q('#page-home');if(!home)return;const h=Q('.homeFeed .intelligentFeedHead h2',home);const p=Q('.homeFeed .intelligentFeedHead p',home);if(h)h.textContent='SMART NOTES · INTELLIGENT BLOCKS';if(p)p.textContent='The intelligence you created, distilled by Naya, and ready to remember, use, and compound.'}
function actions(){const home=Q('#page-home');if(!home)return;const items=[...QA('.homeFeed .intelligentBlock',home),...QA('.homeFeed .note',home)];items.forEach((item,i)=>{const title=clean(Q('h3',item)?.textContent)||('intelligence-'+i);if(!Q('.nh-authority-fav',item)){const f=document.createElement('button');f.className='nh-authority-fav';f.type='button';f.textContent='☆';f.title='Favorite this intelligence';const k=key(title);const paint=()=>{const st=state();const on=!!(st.favorites&&st.favorites[k]);f.classList.toggle('on',on);f.textContent=on?'★':'☆'};f.onclick=()=>{const st=state();st.favorites=st.favorites||{};st.favorites[k]=!st.favorites[k];saveState(st);paint()};item.appendChild(f);paint()}
if(!Q('.nh-authority-actions',item)){const a=document.createElement('div');a.className='nh-authority-actions';a.innerHTML='<button data-act="share">＋ SHARE</button><button data-act="like">👍 LIKE</button><button data-act="love">♥ LOVE</button><button data-act="rank">★ RANK</button><button data-act="comment">💬 COMMENT</button><button data-act="save">🔖 SAVE</button>';item.appendChild(a);a.querySelectorAll('button').forEach(btn=>{const act=btn.dataset.act;const k=key(title)+'-'+act;btn.addEventListener('click',()=>{if(act==='share'||act==='comment'){btn.classList.add('on');setTimeout(()=>btn.classList.remove('on'),650);return}const st=state();st.actions=st.actions||{};st.actions[k]=!st.actions[k];saveState(st);btn.classList.toggle('on',!!st.actions[k])})})}})}
function run(){css();labelHome();addTodayNav();createTodayPage();removeTodayFromHome();quote();feedHeading();actions();buildToday()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(run,120));else setTimeout(run,120);setTimeout(run,900);setTimeout(run,1800);setTimeout(run,3000);
})();
