/* Final surgical cleanup for the canonical Hub. */
(()=>{'use strict';
const Q=(s,r=document)=>r.querySelector(s),QA=(s,r=document)=>[...r.querySelectorAll(s)];
function run(){
  QA('.nh-authority-actions').forEach(x=>{if(x.closest('.intelligentBlock')?.querySelector('.nh-excellence-actions'))x.remove()});
  QA('.nh-authority-fav').forEach(x=>{if(x.closest('.intelligentBlock')?.querySelector('.nh-excellence-fav'))x.remove()});
  QA('.nh-v11-quote,#nhV11Quote').forEach(x=>x.remove());
  QA('#page-home .nh-v11-today,#page-home #nhV11Today').forEach(x=>x.remove());
  QA('#nhTodayGrid .nh-today-kicker').forEach(x=>x.textContent='DAILY HIGHLIGHTS');
  const crumb=Q('.topbar .crumb');
  if(crumb){const w=document.createTreeWalker(crumb,NodeFilter.SHOW_TEXT),nodes=[];while(w.nextNode())nodes.push(w.currentNode);nodes.forEach(n=>{if(String(n.nodeValue||'').trim()==='Home')n.nodeValue='Smart Notes'})}
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(run,180));else setTimeout(run,180);setTimeout(run,1100);setTimeout(run,2300);setTimeout(run,3600);
})();
