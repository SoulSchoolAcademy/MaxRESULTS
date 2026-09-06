/* NayaNET Intelligent Hub V7 — presentation refinement layer. Surgical only: preserves the existing V7 feed and intelligence behaviors. */
(()=>{'use strict';
const Q=(s,r=document)=>r.querySelector(s), QA=(s,r=document)=>[...r.querySelectorAll(s)];
function css(){if(Q('#nh-v10-refinement-style'))return;const s=document.createElement('style');s.id='nh-v10-refinement-style';s.textContent=`
/* V7 refinement: the Smart Notes / Intelligent Blocks are the star */
#page-home .heroIntro{display:none!important}
#page-home .hero{display:none!important}
#nh72Search{margin:0 0 22px!important;max-width:none}
#nh72Search input{border-color:#8b63ff!important;box-shadow:inset 0 1px #fff6,0 0 22px #8b63ff18,0 18px 40px #000b!important}
.nh-v10-quote{margin:28px 0 22px;padding:16px 20px;border-left:2px solid #d86cff;border-top:1px solid #ffffff12;border-bottom:1px solid #ffffff12;background:linear-gradient(90deg,#120d19,#09090d 72%,transparent);color:#eeeaf2;font-size:15px;line-height:1.55;letter-spacing:-.012em;box-shadow:0 0 28px #d86cff0b}
.nh-v10-quote span{display:block;margin-top:6px;color:#8e8798;font-size:7px;font-weight:1000;letter-spacing:.16em;text-transform:uppercase}
#page-home .homeFeed{margin-top:4px!important}
#page-home .homeFeed .intelligentFeedHead{display:flex!important;align-items:end!important;justify-content:space-between!important;gap:20px!important;margin:0 0 16px!important}
#page-home .homeFeed .intelligentFeedHead h2{font-size:30px!important;letter-spacing:-.055em!important;margin:0!important}
#page-home .homeFeed .intelligentFeedHead p{max-width:620px!important;font-size:11px!important;color:#a9a4b1!important}
/* Make the real feed cards unmistakably premium and alive */
#page-home .homeFeed .note,#page-home .homeFeed .intelligentBlock,#page-home .homeFeed [class*="intelligent-block"]{position:relative;transition:.24s cubic-bezier(.16,.84,.22,1)!important}
#page-home .homeFeed .note:hover,#page-home .homeFeed .intelligentBlock:hover,#page-home .homeFeed [class*="intelligent-block"]:hover{transform:translateY(-3px);border-color:#a989ff99!important;box-shadow:inset 0 1px #fff5,0 24px 55px #000c,0 0 32px #8b63ff16!important}
#page-home .homeFeed .noteTop{background:linear-gradient(90deg,#ffffff03,transparent)!important}
#page-home .homeFeed .noteBody h3{font-size:21px!important;letter-spacing:-.035em!important}
#page-home .homeFeed .noteBody p{font-size:12px!important;line-height:1.68!important;color:#ddd8e3!important}
#page-home .homeFeed .noteView{background:linear-gradient(145deg,#09080d,#0d0b12)!important;border-color:#ffffff18!important}
/* Electric persistent actions */
#page-home .nh72-actions button,.nh72-actions button{position:relative!important;border-color:#8b63ff66!important;background:linear-gradient(145deg,#15101d,#08080c)!important;color:#eeeaf4!important;box-shadow:inset 0 1px #fff5,0 7px 16px #0009,0 0 12px #8b63ff08!important;transition:.2s ease!important}
#page-home .nh72-actions button:hover,.nh72-actions button:hover{transform:translateY(-2px)!important;border-color:#d86cff!important;color:#fff!important;background:linear-gradient(145deg,#24112f,#0b080f)!important;box-shadow:inset 0 1px #fff7,0 12px 24px #000b,0 0 22px #d86cff2c!important}
#page-home .nh72-actions button.nh72-action-on,.nh72-actions button.nh72-action-on{border-color:#55e39a!important;color:#c7ffdc!important;box-shadow:0 0 18px #55e39a20,inset 0 1px #fff5!important}
/* Favorite star gets visual priority without becoming a giant control */
.nh-v10-fav{position:absolute;right:14px;top:12px;width:34px;height:34px;border-radius:10px;border:1px solid #d86cff66;background:#0b0910;color:#d7d0df;font-size:16px;display:grid;place-items:center;box-shadow:0 0 16px #d86cff10;cursor:pointer;transition:.2s ease;z-index:3}
.nh-v10-fav:hover,.nh-v10-fav.on{border-color:#d86cff;background:#201027;color:#fff;box-shadow:0 0 24px #d86cff38}
.nh-v10-saved{display:inline-flex!important;align-items:center;gap:5px}
@media(max-width:760px){.nh-v10-quote{margin-top:18px;font-size:13px;padding:14px}.nh72-search{margin-bottom:16px!important}#page-home .homeFeed .intelligentFeedHead{display:block!important}#page-home .homeFeed .intelligentFeedHead h2{font-size:25px!important;margin-bottom:6px!important}}
` ;document.head.appendChild(s)}
function removeInjectedToday(){
 QA('#page-home .nh72-today,#page-home .nh72-section,#page-home .nh72-answer').forEach(el=>el.remove());
 const today=QA('#page-home [class*="nh72"]');
 today.forEach(el=>{if(el.id==='nh72Search'||el.id==='nh72Answer')return;if(el.closest('.homeFeed'))return; if(el.classList.contains('nh72-privacy'))el.remove();});
}
function quote(){const home=Q('#page-home');if(!home||Q('#nhV10Quote',home))return;const q=document.createElement('div');q.id='nhV10Quote';q.className='nh-v10-quote';q.innerHTML='Your life creates intelligence every day. Naya helps you capture it, understand it, remember it, compound it, and use it.<span>NayaNET · Intelligent Hub</span>';const search=Q('#nh72Search');if(search)search.insertAdjacentElement('afterend',q);else home.prepend(q)}
function identity(){
 QA('[data-page="home"]').forEach(b=>{const ico=Q('.ico',b);b.textContent='';if(ico)b.appendChild(ico);b.appendChild(document.createTextNode('Your Intelligence Today'))});
 const pt=Q('#pageTitle');if(pt&&Q('#page-home')?.classList.contains('active'))pt.textContent='';
}
function strengthenFeed(){
 const home=Q('#page-home');if(!home)return;
 const head=Q('.homeFeed .intelligentFeedHead',home);if(head){const h=Q('h2',head);const p=Q('p',head);if(h)h.textContent='SMART NOTES · INTELLIGENT BLOCKS';if(p)p.textContent='The intelligence you created, distilled by Naya, and ready to remember, use, and compound.')}
 QA('.homeFeed .note',home).forEach(n=>{
   n.style.position='relative';
   const id=n.id||('note-'+Math.random().toString(36).slice(2));n.id=id;
   if(!Q('.nh-v10-fav',n)){
     const key='nh72';const title=Q('.noteBody h3',n)?.textContent||id;const safe=encodeURIComponent(title.slice(0,100));
     const b=document.createElement('button');b.className='nh-v10-fav';b.type='button';b.title='Favorite this intelligence';b.dataset.favKey=key+'-'+safe;b.textContent='☆';
     n.appendChild(b);
     b.onclick=()=>{const on=b.classList.toggle('on');b.textContent=on?'★':'☆';try{const raw=JSON.parse(localStorage.getItem('nayanet_intelligent_blocks_v2')||'{}');raw.favorites=raw.favorites||{};raw.favorites[b.dataset.favKey]=on;localStorage.setItem('nayanet_intelligent_blocks_v2',JSON.stringify(raw))}catch(e){}};
   }
 });
}
function hideDuplicateIdentity(){
 QA('body *').forEach(el=>{
   if(el.children.length) return;
   const t=(el.textContent||'').trim();
   if(t==='YOUR INTELLIGENCE TODAY' && !el.closest('.nav') && !el.closest('#nhV10Quote')) el.style.display='none';
 });
}
function run(){css();removeInjectedToday();identity();quote();strengthenFeed();hideDuplicateIdentity()}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(run,50));else setTimeout(run,50);
setTimeout(run,700);setTimeout(run,1600);
})();
