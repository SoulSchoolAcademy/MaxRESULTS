/* NayaNET Intelligent Hub V7 — presentation refinement layer. Surgical only: preserves the existing V7 feed and intelligence behaviors. */
(()=>{'use strict';
const Q=(s,r=document)=>r.querySelector(s), QA=(s,r=document)=>[...r.querySelectorAll(s)];
const clean=s=>String(s||'').replace(/\s+/g,' ').trim();
const esc=s=>String(s??'').replace(/[&<>\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\\':'&#92;','"':'&quot;'}[c]||c));
function css(){if(Q('#nh-v11-refinement-style'))return;const s=document.createElement('style');s.id='nh-v11-refinement-style';s.textContent=`
/* V11 — intelligence-first presentation */
#page-home .heroIntro,#page-home .hero{display:none!important}
#nh72Search{margin:0 0 18px!important;max-width:none}
#nh72Search input{min-height:64px!important;border:1px solid #a989ff!important;border-radius:18px!important;background:linear-gradient(145deg,#15101d,#07070b)!important;box-shadow:inset 0 1px #fff7,0 0 30px #8b63ff1c,0 20px 45px #000d!important;font-size:15px!important}
#nh72Search input:focus{border-color:#d86cff!important;box-shadow:inset 0 1px #fff8,0 0 42px #d86cff2a,0 20px 50px #000e!important}
.nh-v11-quote{margin:0 0 24px;padding:12px 17px;border-left:2px solid #d86cff;border-top:1px solid #ffffff10;border-bottom:1px solid #ffffff10;background:linear-gradient(90deg,#120d19,#09090d 70%,transparent);color:#eeeaf2;font-size:13px;line-height:1.5;box-shadow:0 0 24px #d86cff09}
.nh-v11-quote span{display:block;margin-top:5px;color:#7f7889;font-size:7px;font-weight:1000;letter-spacing:.17em;text-transform:uppercase}
.nh-v11-today{display:grid;grid-template-columns:1fr auto;gap:16px;align-items:center;margin:0 0 25px;padding:17px 19px;border:1px solid #ffffff16;border-radius:19px;background:radial-gradient(500px 150px at 80% 0%,#d86cff13,transparent 70%),linear-gradient(145deg,#111018,#08080c);box-shadow:inset 0 1px #fff3,0 18px 38px #0009}
.nh-v11-today .label{font-size:7px;font-weight:1000;letter-spacing:.18em;color:#d6a9ff}
.nh-v11-today h3{margin:5px 0 3px;font-size:18px;letter-spacing:-.035em}
.nh-v11-today p{margin:0;color:#aaa4b1;font-size:9px;line-height:1.5}
.nh-v11-today .stats{display:flex;gap:7px;flex-wrap:wrap;justify-content:flex-end}
.nh-v11-today .stat{min-width:74px;padding:9px 10px;text-align:center;border:1px solid #ffffff16;border-radius:11px;background:#07070b}
.nh-v11-today .stat b{display:block;font-size:16px;color:#fff}.nh-v11-today .stat span{display:block;margin-top:2px;color:#77717f;font-size:6px;font-weight:1000;letter-spacing:.12em}
#page-home .homeFeed{margin-top:0!important}
#page-home .homeFeed .intelligentFeedHead{display:flex!important;align-items:end!important;justify-content:space-between!important;gap:20px!important;margin:0 0 14px!important}
#page-home .homeFeed .intelligentFeedHead h2{font-size:31px!important;line-height:1!important;letter-spacing:-.06em!important;margin:0!important}
#page-home .homeFeed .intelligentFeedHead p{max-width:680px!important;font-size:10px!important;color:#a9a4b1!important;line-height:1.55!important}
/* The real Smart Notes are the hero content */
#page-home .homeFeed .note{position:relative!important;border:1px solid #ffffff22!important;border-radius:23px!important;background:radial-gradient(700px 230px at 85% 0%,#8b63ff0d,transparent 65%),linear-gradient(145deg,#16151c,#08080c)!important;box-shadow:inset 0 1px #fff5,0 22px 50px #000c!important;overflow:visible!important;transition:.25s cubic-bezier(.16,.84,.22,1)!important}
#page-home .homeFeed .note:hover{transform:translateY(-5px)!important;border-color:#b18dff9c!important;box-shadow:inset 0 1px #fff7,0 30px 65px #000e,0 0 38px #8b63ff1b!important}
#page-home .homeFeed .noteTop{padding:15px 20px 12px!important;background:linear-gradient(90deg,#ffffff05,transparent)!important;border-bottom:1px solid #ffffff14!important}
#page-home .homeFeed .noteTop span:first-child{color:#d7d0df!important;font-size:8px!important;letter-spacing:.13em!important}
#page-home .homeFeed .noteTop .type{color:#c9ffe0!important;border-color:#55e39a44!important;background:#55e39a0f!important}
#page-home .homeFeed .noteBody{padding:20px 20px 13px!important}
#page-home .homeFeed .noteBody h3{font-size:24px!important;line-height:1.05!important;letter-spacing:-.045em!important;margin:0 0 10px!important;max-width:850px!important}
#page-home .homeFeed .noteBody p{font-size:13px!important;line-height:1.68!important;color:#e0dbe5!important;max-width:900px!important}
#page-home .homeFeed .noteTabs{padding:0 20px 13px!important;gap:7px!important}
#page-home .homeFeed .noteTab{min-height:35px!important;border-color:#ffffff20!important;background:#09090d!important;color:#aaa4b1!important}
#page-home .homeFeed .noteTab.active{background:#f6f4f7!important;color:#050507!important;border-color:#fff!important;box-shadow:0 0 18px #fff3!important}
#page-home .homeFeed .noteView{margin:0 20px 20px!important;padding:15px!important;border-color:#ffffff18!important;border-radius:15px!important;background:linear-gradient(145deg,#09090e,#060609)!important;color:#d7d1dc!important;font-size:10px!important;line-height:1.65!important}
#page-home .homeFeed .noteView strong{font-size:7px!important;color:#d7a9ff!important;letter-spacing:.16em!important}
/* Premium intelligence metadata added without replacing existing architecture */
.nh-v11-intel{display:grid;grid-template-columns:1.1fr .9fr;gap:9px;margin:0 20px 14px}
.nh-v11-panel{padding:12px 13px;border:1px solid #ffffff14;border-radius:13px;background:#07070b}
.nh-v11-panel b{display:block;font-size:7px;letter-spacing:.15em;color:#d5a5ff;margin-bottom:5px}.nh-v11-panel span{display:block;font-size:9px;line-height:1.5;color:#a9a4b1}
.nh-v11-actions{display:flex!important;gap:7px!important;flex-wrap:wrap!important;margin:0 20px 20px!important;padding-top:14px!important;border-top:1px solid #ffffff13!important}
.nh-v11-actions button{min-height:40px!important;padding:0 13px!important;border:1px solid #8b63ff66!important;border-radius:11px!important;background:linear-gradient(145deg,#17111f,#08080c)!important;color:#eeeaf4!important;font-size:8px!important;font-weight:1000!important;letter-spacing:.04em!important;box-shadow:inset 0 1px #fff5,0 8px 18px #000a,0 0 12px #8b63ff0b!important;transition:.2s ease!important}
.nh-v11-actions button:hover{transform:translateY(-3px)!important;border-color:#d86cff!important;color:#fff!important;background:linear-gradient(145deg,#291132,#0b080f)!important;box-shadow:inset 0 1px #fff8,0 13px 28px #000c,0 0 26px #d86cff35!important}
.nh-v11-actions button.nh-v11-on{border-color:#55e39a!important;color:#c8ffdd!important;box-shadow:0 0 22px #55e39a24,inset 0 1px #fff6!important}
.nh-v11-fav{position:absolute!important;right:14px!important;top:12px!important;width:42px!important;height:42px!important;border-radius:12px!important;border:1px solid #d86cff77!important;background:#0a080e!important;color:#d9d0df!important;font-size:20px!important;display:grid!important;place-items:center!important;cursor:pointer!important;z-index:5!important;box-shadow:0 0 18px #d86cff13!important;transition:.2s ease!important}
.nh-v11-fav:hover,.nh-v11-fav.on{transform:scale(1.06)!important;border-color:#d86cff!important;background:#24102d!important;color:#fff!important;box-shadow:0 0 30px #d86cff45!important}
.nh-v11-rank{color:#ffd98a!important}
/* Keep the daily destination compact and unmistakable — no repeated giant title */
body .nh72-today,body .nh72-section{display:none!important}
body .nh72-privacy{display:none!important}
@media(max-width:760px){.nh-v11-today{grid-template-columns:1fr}.nh-v11-today .stats{justify-content:flex-start}.nh-v11-intel{grid-template-columns:1fr}#page-home .homeFeed .intelligentFeedHead{display:block!important}#page-home .homeFeed .intelligentFeedHead h2{font-size:27px!important;margin-bottom:7px!important}#page-home .homeFeed .noteBody h3{font-size:21px!important}.nh-v11-actions button{flex:1 1 auto}.nh-v11-quote{font-size:12px}}
`;
document.head.appendChild(s)}
function removeOldToday(){QA('#page-home .nh72-today,#page-home .nh72-section,#page-home .nh72-answer').forEach(el=>el.remove());QA('#page-home [class*="nh72"]').forEach(el=>{if(el.id==='nh72Search'||el.id==='nh72Results')return;if(el.closest('.homeFeed'))return;if(el.classList.contains('nh72-privacy'))el.remove()})}
function quote(){const home=Q('#page-home');if(!home||Q('#nhV11Quote',home))return;const q=document.createElement('div');q.id='nhV11Quote';q.className='nh-v11-quote';q.innerHTML='Your life creates intelligence every day. Naya helps you capture it, understand it, remember it, compound it, and use it.<span>NayaNET · Intelligent Hub</span>';const search=Q('#nh72Search');if(search)search.insertAdjacentElement('afterend',q);else home.prepend(q)}
function identity(){QA('[data-page="home"]').forEach(b=>{const ico=Q('.ico',b);b.innerHTML='';if(ico)b.appendChild(ico);b.appendChild(document.createTextNode('Your Intelligence Today'))});QA('body *').forEach(el=>{if(el.children.length)return;const t=clean(el.textContent);if(t==='YOUR INTELLIGENCE TODAY'&&!el.closest('.nav')&&!el.closest('#nhV11Quote'))el.style.display='none'});const pt=Q('#pageTitle');if(pt&&Q('#page-home')?.classList.contains('active'))pt.textContent=''}
function todaySnapshot(home){if(Q('#nhV11Today',home))return;const list=Q('.homeFeed .noteList',home);if(!list)return;const count=QA('.note',list).length;const types={};QA('.note .type',list).forEach(x=>{const t=clean(x.textContent)||'INTELLIGENCE';types[t]=(types[t]||0)+1});const primary=Object.keys(types)[0]||'INTELLIGENCE';const box=document.createElement('div');box.id='nhV11Today';box.className='nh-v11-today';box.innerHTML='<div><div class="label">TODAY · HIGHLIGHTS</div><h3>Your intelligence, in a nutshell.</h3><p>The strongest Smart Notes from today are captured below. Your Intelligence Today is the daily highlight layer — the deeper Intelligence Report remains the place for full analysis.</p></div><div class="stats"><div class="stat"><b>'+count+'</b><span>NOTES</span></div><div class="stat"><b>'+esc(primary)+'</b><span>LEAD TYPE</span></div></div></div>';const feed=Q('.homeFeed',home);if(feed)feed.insertBefore(box,feed.firstChild)}
function enrichNotes(){const home=Q('#page-home');if(!home)return;const notes=QA('.homeFeed .note',home);notes.forEach((n,i)=>{n.style.position='relative';const title=clean(Q('.noteBody h3',n)?.textContent)||'Intelligent Event';const body=clean(Q('.noteBody p',n)?.textContent)||'Captured intelligence from your life, ready to understand and compound.';if(!Q('.nh-v11-fav',n)){const b=document.createElement('button');b.className='nh-v11-fav';b.type='button';b.title='Favorite this intelligence';b.setAttribute('aria-label','Favorite this intelligence');b.textContent='☆';b.dataset.key='v11-'+title.slice(0,100);const sync=()=>{try{const st=JSON.parse(localStorage.getItem('nayanet_intelligent_blocks_v2')||'{}');return !!(st.favorites&&st.favorites[b.dataset.key])}catch(e){return false}};const paint=()=>{const on=sync();b.classList.toggle('on',on);b.textContent=on?'★':'☆'};b.onclick=()=>{try{const st=JSON.parse(localStorage.getItem('nayanet_intelligent_blocks_v2')||'{}');st.favorites=st.favorites||{};st.favorites[b.dataset.key]=!st.favorites[b.dataset.key];localStorage.setItem('nayanet_intelligent_blocks_v2',JSON.stringify(st));paint()}catch(e){}};n.appendChild(b);paint()}
if(!Q('.nh-v11-intel',n)){const p=document.createElement('div');p.className='nh-v11-intel';const nutshell=body.length>220?body.slice(0,217).replace(/\s+\S*$/,'')+'…':body;const why=i===0?'This is the intelligence worth remembering and using — not just the event itself.':'This note becomes more valuable when connected to what you do next.';p.innerHTML='<div class="nh-v11-panel"><b>NUTSHELL</b><span>'+esc(nutshell)+'</span></div><div class="nh-v11-panel"><b>WHY IT MATTERS</b><span>'+esc(why)+'</span></div>';const tabs=Q('.noteTabs',n);if(tabs)tabs.insertAdjacentElement('beforebegin',p);else n.appendChild(p)}
const tabs=Q('.noteTabs',n);if(tabs&& !Q('.nh-v11-actions',n)){const a=document.createElement('div');a.className='nh-v11-actions';a.innerHTML='<button type="button">＋ SHARE</button><button type="button">👍 LIKE</button><button type="button">♥ LOVE</button><button type="button" class="nh-v11-rank">★ RANK</button><button type="button">💬 COMMENT</button><button type="button">🔖 SAVE</button>';tabs.insertAdjacentElement('afterend',a);a.querySelectorAll('button').forEach(btn=>{btn.addEventListener('click',()=>btn.classList.toggle('nh-v11-on'))})}
});}
function strengthenFeed(){const home=Q('#page-home');if(!home)return;const head=Q('.homeFeed .intelligentFeedHead',home);if(head){const h=Q('h2',head),p=Q('p',head);if(h)h.textContent='SMART NOTES · INTELLIGENT BLOCKS';if(p)p.textContent='The intelligence you created, distilled by Naya, and ready to remember, use, and compound. Every block is a piece of intelligence you can keep, act on, and share.'}todaySnapshot(home);enrichNotes()}
function run(){css();removeOldToday();identity();quote();strengthenFeed()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(run,80));else setTimeout(run,80);setTimeout(run,700);setTimeout(run,1600);setTimeout(run,2800);
})();
