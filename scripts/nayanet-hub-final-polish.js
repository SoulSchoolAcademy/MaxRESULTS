/* Final surgical cleanup: remove duplicate action/favorite layers when the canonical feed already owns them. */
(()=>{'use strict';
const Q=(s,r=document)=>r.querySelector(s), QA=(s,r=document)=>[...r.querySelectorAll(s)];
function run(){
  QA('.nh-authority-actions').forEach(x=>{if(x.closest('.intelligentBlock')?.querySelector('.nh-excellence-actions'))x.remove()});
  QA('.nh-authority-fav').forEach(x=>{if(x.closest('.intelligentBlock')?.querySelector('.nh-excellence-fav'))x.remove()});
  QA('#nhTodayGrid .nh-today-kicker').forEach(x=>x.textContent='DAILY HIGHLIGHTS');
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',()=>setTimeout(run,180));else setTimeout(run,180);setTimeout(run,1100);setTimeout(run,2300);setTimeout(run,3600);
})();
