/* NayaNET V7 — Intelligent Feed Excellence layer. Surgical enhancement of the existing Intelligent Blocks. */
(()=>{'use strict';
const Q=(s,r=document)=>r.querySelector(s), QA=(s,r=document)=>[...r.querySelectorAll(s)];
const KEY='nayanet_intelligent_feed_actions_v1';
const read=()=>{try{return JSON.parse(localStorage.getItem(KEY))||{}}catch(e){return{}}};
const save=s=>{try{localStorage.setItem(KEY,JSON.stringify(s))}catch(e){}};
const clean=s=>String(s||'').replace(/\s+/g,' ').trim();
const esc=s=>String(s??'').replace(/[&<>\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\\':'&#92;','"':'&quot;'}[c]||c));
const keyFor=b=>'ibx-'+clean(Q('.blockTitle h3',b)?.textContent||b.id||'intelligence').slice(0,180);
function css(){if(Q('#nh-feed-excellence-style'))return;const s=document.createElement('style');s.id='nh-feed-excellence-style';s.textContent=`
/* 10/10 Intelligent Block presentation */
#page-home .intelligentFeedHead{padding:10px 4px 20px!important}
#page-home .intelligentFeedHead h2{font-size:34px!important;letter-spacing:-.06em!important}
#page-home .intelligentFeedHead p{font-size:11px!important;max-width:760px!important;line-height:1.6!important}
#page-home .intelligentBlock{position:relative!important;margin:0 0 12px!important;padding:38px 34px 30px!important;border:1px solid #ffffff1b!important;border-radius:25px!important;background:radial-gradient(800px 330px at 82% 0%,color-mix(in srgb,var(--tone) 9%,transparent),transparent 65%),linear-gradient(145deg,#14131a,#08080c)!important;box-shadow:inset 0 1px #fff5,0 25px 58px #000d!important;overflow:visible!important;transition:.26s cubic-bezier(.16,.84,.22,1)!important}
#page-home .intelligentBlock:hover{transform:translateY(-5px)!important;border-color:color-mix(in srgb,var(--tone) 58%,#fff 8%)!important;box-shadow:inset 0 1px #fff7,0 34px 75px #000e,0 0 42px color-mix(in srgb,var(--tone) 12%,transparent)!important}
#page-home .intelligentBlock:first-child{padding-top:38px!important}
#page-home .intelligentBlock:last-child{border-bottom:1px solid #ffffff1b!important}
#page-home .intelligentBlock:before{left:10px!important;top:48px!important;bottom:48px!important;opacity:.8!important}
#page-home .intelligentBlock .blockHeader{margin-bottom:23px!important}
#page-home .intelligentBlock .blockTitle h3{font-size:clamp(28px,3vw,43px)!important;line-height:1.02!important;max-width:900px!important}
#page-home .intelligentBlock .blockBody{margin-bottom:22px!important;padding-bottom:22px!important}
#page-home .intelligentBlock .blockBody p{font-size:16px!important;line-height:1.72!important;max-width:940px!important;color:#eeeaf1!important}
#page-home .nh-excellence{display:grid;grid-template-columns:1.15fr .85fr;gap:9px;margin:0 0 24px}
#page-home .nh-excellence .panel{padding:13px 14px;border:1px solid #ffffff15;border-radius:14px;background:#07070b}
#page-home .nh-excellence b{display:block;color:#d9a9ff;font-size:7px;font-weight:1000;letter-spacing:.16em;margin-bottom:6px}
#page-home .nh-excellence span{display:block;color:#b9b2c0;font-size:9px;line-height:1.55}
#page-home .nh-excellence-actions{display:flex;gap:7px;flex-wrap:wrap;margin-top:20px;padding-top:15px;border-top:1px solid #ffffff13}
#page-home .nh-excellence-actions button{min-height:42px;padding:0 13px;border:1px solid #8b63ff70;border-radius:11px;background:linear-gradient(145deg,#17111f,#08080c);color:#eeeaf4;font-size:8px;font-weight:1000;letter-spacing:.045em;box-shadow:inset 0 1px #fff5,0 8px 18px #000a,0 0 13px #8b63ff0c;transition:.2s ease}
#page-home .nh-excellence-actions button:hover{transform:translateY(-3px);border-color:#d86cff;background:linear-gradient(145deg,#2a1233,#0b080f);box-shadow:inset 0 1px #fff8,0 14px 28px #000c,0 0 28px #d86cff38}
#page-home .nh-excellence-actions button.on{border-color:#55e39a;color:#c8ffdd;box-shadow:0 0 23px #55e39a24,inset 0 1px #fff6}
#page-home .nh-excellence-actions button.rank{color:#ffd98a}
#page-home .nh-excellence-fav{position:absolute;right:16px;top:15px;width:44px;height:44px;border-radius:13px;border:1px solid #d86cff77;background:#0a080e;color:#ddd4e4;font-size:21px;display:grid;place-items:center;z-index:8;cursor:pointer;box-shadow:0 0 19px #d86cff12;transition:.2s ease}
#page-home .nh-excellence-fav:hover,#page-home .nh-excellence-fav.on{transform:scale(1.07);border-color:#d86cff;background:#25102f;color:#fff;box-shadow:0 0 32px #d86cff4a}
#page-home .nh-excellence-fav.on{color:#fff}
@media(max-width:760px){#page-home .intelligentBlock{padding:29px 14px 25px!important;border-radius:20px!important}#page-home .intelligentBlock:before{left:0!important;top:42px!important;bottom:42px!important}#page-home .intelligentBlock .blockTitle h3{font-size:28px!important;padding-right:48px!important}#page-home .intelligentBlock .blockBody p{font-size:15px!important}.nh-excellence{grid-template-columns:1fr!important}.nh-excellence-actions button{flex:1 1 auto;min-width:105px}}
`;
document.head.appendChild(s)}
function nutshell(text){text=clean(text);if(text.length<=260)return text;const cut=text.slice(0,275);const p=Math.max(cut.lastIndexOf('. '),cut.lastIndexOf(' '));return cut.slice(0,p>150?p:260).replace(/[,:;—-]+$/,'')+'…'}
function actButton(label,action,active,extra){return '<button type="button" class="'+(extra||'')+' '+(active?'on':'')+'" data-nh-action="'+action+'">'+label+'</button>'}
function enrichBlock(b,i){if(Q('.nh-excellence-actions',b))return;const title=clean(Q('.blockTitle h3',b)?.textContent)||'Intelligent Block';const body=clean(Q('.blockBody p',b)?.textContent)||clean(Q('.perspective p',b)?.textContent)||'Preserved intelligence from this event.';const state=read(),a=state[keyFor(b)]||{};
const bodyHost=Q('.blockBody',b);if(bodyHost&&!Q('.nh-excellence',bodyHost)){const strip=document.createElement('div');strip.className='nh-excellence';const signal=i===0?'Lead intelligence — worth remembering, acting on, and connecting.':'Useful intelligence — designed to become more valuable when you apply it.';strip.innerHTML='<div class="panel"><b>NUTSHELL</b><span>'+esc(nutshell(body))+'</span></div><div class="panel"><b>INTELLIGENCE SIGNAL</b><span>'+esc(signal)+'</span></div>';bodyHost.insertAdjacentElement('afterbegin',strip)}
const fav=document.createElement('button');fav.type='button';fav.className='nh-excellence-fav '+(a.favorite?'on':'');fav.textContent=a.favorite?'★':'☆';fav.title='Favorite this intelligence';fav.onclick=()=>{const st=read();st[keyFor(b)]=st[keyFor(b)]||{};st[keyFor(b)].favorite=!st[keyFor(b)].favorite;save(st);fav.classList.toggle('on',st[keyFor(b)].favorite);fav.textContent=st[keyFor(b)].favorite?'★':'☆'};b.appendChild(fav);
const bar=document.createElement('div');bar.className='nh-excellence-actions';bar.innerHTML=actButton('＋ SHARE','share',false)+actButton('👍 LIKE','like',!!a.like)+actButton('♥ LOVE','love',!!a.love)+actButton('★ RANK '+(a.rank?a.rank+'/5':''),'rank',false,'rank')+actButton('💬 COMMENT'+(a.commentCount?' '+a.commentCount:''),'comment',false)+actButton('🔖 SAVE','save',!!a.save);const footer=Q('.blockFooter',b);if(footer)footer.insertAdjacentElement('beforebegin',bar);else b.appendChild(bar);
bar.querySelectorAll('[data-nh-action]').forEach(btn=>btn.addEventListener('click',()=>handle(btn.dataset.nhAction,b,btn,title,body)))}
function handle(action,b,btn,title,body){const st=read();st[keyFor(b)]=st[keyFor(b)]||{};const a=st[keyFor(b)];if(action==='like'||action==='love'||action==='save'){a[action]=!a[action];btn.classList.toggle('on',a[action]);save(st);return}if(action==='rank'){const v=prompt('How valuable is this intelligence? Enter 1–5.',a.rank||'');const n=Number(v);if(!Number.isFinite(n)||n<1||n>5)return;a.rank=Math.round(n*10)/10;btn.textContent='★ RANK '+a.rank+'/5';save(st);return}if(action==='comment'){const text=prompt('Add a comment to this Intelligent Block:');if(!text?.trim())return;a.commentCount=(a.commentCount||0)+1;a.lastComment=text.trim();btn.textContent='💬 COMMENT '+a.commentCount;save(st);return}if(action==='share'){const text=title+'\n\n'+nutshell(body)+'\n\nNayaNET — Create. Connect. Grow with US.';if(navigator.share){navigator.share({title,text}).catch(()=>{})}else if(navigator.clipboard){navigator.clipboard.writeText(text).then(()=>{btn.textContent='✓ COPIED';setTimeout(()=>btn.textContent='＋ SHARE',1400)}).catch(()=>alert(text))}else alert(text)}}
function run(){css();const home=Q('#page-home');if(!home)return;QA('.intelligentBlock',home).forEach(enrichBlock)}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(run,120));else setTimeout(run,120);setTimeout(run,900);setTimeout(run,1900);setTimeout(run,3200);
})();
