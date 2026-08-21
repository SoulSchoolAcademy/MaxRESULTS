from pathlib import Path
import re, subprocess

# Pull the current assessment source from governance/main, then patch it into the active engineering branch.
assessment = Path('IASCORE.NAYANET.APP')
assessment.write_text(subprocess.check_output(['git','show','origin/main:IASCORE.NAYANET.APP'], text=True))
s = assessment.read_text()

# Replace every rendered purple Naya orb with the approved Naya profile image.
s = s.replace('<span class="naya-orb" aria-hidden="true"></span>', '<img class="naya-avatar" src="Naya%20Profile%206.jpg" alt="Naya" loading="eager" decoding="async">')
s = s.replace('<div class="presence-orb" id="presenceOrb" aria-hidden="true"></div>', '<img class="presence-avatar" id="presenceAvatar" src="Naya%20Profile%206.jpg" alt="Naya" loading="eager" decoding="async">')
s = s.replace('.naya-btn{display:flex;', '.naya-avatar{width:40px;height:40px;flex:0 0 40px;border-radius:50%;object-fit:cover;object-position:center;border:1px solid rgba(255,255,255,.9);box-shadow:0 0 0 3px rgba(149,104,255,.18),0 0 24px rgba(149,104,255,.32),0 7px 15px rgba(0,0,0,.62)}.naya-btn.playing .naya-avatar{animation:breathe 1.35s ease-in-out infinite}.presence-avatar{width:72px;height:72px;flex:0 0 72px;border-radius:50%;object-fit:cover;object-position:center;border:1px solid rgba(255,255,255,.95);box-shadow:0 0 0 5px rgba(149,104,255,.16),0 0 34px rgba(149,104,255,.34),0 12px 26px rgba(0,0,0,.58)}.presence-avatar.playing{animation:breathe 1.35s ease-in-out infinite}.naya-btn{display:flex;')

# Remove the post-question-15 Interest page and its dead styling/runtime.
s = re.sub(r'<section id="interestStage".*?</section>\s*', '', s, flags=re.S)
s = re.sub(r'\.interest-stage\{.*?@media\(max-width:420px\)', '@media(max-width:420px)', s, flags=re.S)
s = s.replace("const state={firstVisit:true,nayaText:'',index:0,selected:null,responses:[],interests:new Set(),nayaPlaying:false,completed:false};", "const state={firstVisit:true,nayaText:'',index:0,selected:null,responses:[],nayaPlaying:false,completed:false};")
s = s.replace("if(state.index===14){showInterestSelection();return}", "if(state.index===14){finishAssessment();return}")
s = re.sub(r'function showInterestSelection\(\).*?function finishInterests\(\)\{finishAssessment\(\)\}\n', '', s, flags=re.S)
s = re.sub(r"\$\('interestContinue'\)\.addEventListener\('click',finishInterests\);\$\('interestSkip'\)\.addEventListener\('click',finishInterests\);", '', s)
s = s.replace('selectedInterests:Array.from(state.interests),', 'selectedInterests:[],')
s = s.replace("window.NAYA_WELCOME_V1=true;", "window.NAYA_WELCOME_V1=true;window.MAXESS_INTEREST_STAGE_REMOVED=true;")
s = s.replace("$('presenceOrb').classList.toggle('playing',v);", "$('presenceAvatar').classList.toggle('playing',v);")
assessment.write_text(s)

# E02 keeps its approved visual system but consumes the authoritative five dimensions dynamically.
e02 = Path('E02-SECTION-02-WORKING.html').read_text()
new_e02 = '''<script>
(()=>{
'use strict';
const root=document.getElementById('maxess-e02-v3');
const host=document.getElementById('e02-orbs');
const missing=document.getElementById('e02-missing');
if(!root||!host)return;
const fallback=[{name:'Direction',key:'direction'},{name:'Context',key:'context'},{name:'Collaboration',key:'collaboration'},{name:'Evaluation',key:'evaluation'},{name:'Iteration',key:'iteration'}];
const colors=['purple','coral','emerald','blue','gold'];
function score(v){const n=Number(v);return Number.isFinite(n)&&n>=0&&n<=100?n:null}
function getDimensions(result){
 if(result&&Array.isArray(result.dimensions)&&result.dimensions.length===5)return result.dimensions.map((d,i)=>({name:d?.name||fallback[i].name,key:d?.id||fallback[i].key,score:score(d?.score)}));
 if(result&&Array.isArray(result.fiveDimensions)&&result.fiveDimensions.length===5)return result.fiveDimensions.map((d,i)=>({name:d?.name||fallback[i].name,key:d?.id||fallback[i].key,score:score(d?.score)}));
 return fallback.map(d=>({...d,score:null}));
}
function render(){
 const result=window.MAXESS_RESULT;const dims=getDimensions(result);const fragment=document.createDocumentFragment();let any=false;
 dims.forEach((dim,index)=>{
  if(dim.score!==null)any=true;
  const article=document.createElement('article');article.className='e02-dimension';article.dataset.dimension=dim.key;article.dataset.color=colors[index];article.setAttribute('aria-label',`${dim.name}: ${dim.score===null?'score unavailable':`${dim.score} out of 100`}`);
  const stage=document.createElement('div');stage.className='e02-orb-stage';
  const aura=document.createElement('div');aura.className='e02-aura';aura.setAttribute('aria-hidden','true');
  const orbit=document.createElement('div');orbit.className='e02-orbit';orbit.setAttribute('aria-hidden','true');
  const orb=document.createElement('div');orb.className='e02-orb';
  const core=document.createElement('div');core.className='e02-core';core.setAttribute('aria-hidden','true');
  const value=document.createElement('div');value.className='e02-score';value.textContent=dim.score===null?'—':String(Math.round(dim.score));
  const unit=document.createElement('div');unit.className='e02-score-unit';unit.textContent='/ 100';
  const access=document.createElement('span');access.className='e02-access';access.textContent=`${dim.name}, ${dim.score===null?'score unavailable':`${Math.round(dim.score)} out of 100`}`;
  orb.append(core,value,unit,access);stage.append(aura,orbit,orb);const name=document.createElement('div');name.className='e02-name';name.textContent=dim.name;article.append(stage,name);fragment.append(article);
 });
 host.replaceChildren(fragment);missing.classList.toggle('is-visible',!any);
}
render();window.addEventListener('MAXESS_RESULT_READY',render);window.addEventListener('maxess:result-updated',render);window.addEventListener('storage',render);
let attempts=0;const timer=setInterval(()=>{attempts++;render();if(window.MAXESS_RESULT||attempts>=20)clearInterval(timer)},250);
})();
</script>'''
e02 = re.sub(r'<script>\n\(\(\)=>\{.*?</script>', new_e02, e02, count=1, flags=re.S)
Path('E02-SECTION-02-WORKING.html').write_text(e02)

# E04 consumes Direction from the same authoritative dimensions array used by E02.
e04 = Path('E04-SECTION-04-WORKING.html').read_text()
new_e04 = '''<script>
(function(){
'use strict';
var scoreEl=document.getElementById('e04-score'),markerEl=document.getElementById('e04-marker'),stageEl=document.getElementById('e04-stage'),copyEl=document.getElementById('e04-copy'),waitingEl=document.getElementById('e04-waiting');
var texts={FOUNDATION:'Your Direction capability is currently in the Foundation stage. This means you may sometimes know what you want AI to help you accomplish, but the instruction you give it may not yet consistently provide enough clarity, context, or desired outcome for AI to produce its best work. The opportunity here isn’t to write longer prompts. It’s to become clearer about what you’re actually asking AI to accomplish.',DEVELOPING:'Your Direction capability is currently Developing. You already understand that better instructions create better results, and you’re beginning to give AI more useful context and intention. Your next opportunity is consistency — learning to establish the destination clearly before asking AI to start moving.',ADVANCING:'Your Direction capability is Advancing. You already know how to establish useful context, intention, and outcomes for AI. Your next level is precision — knowing which details matter most and giving AI exactly what it needs without unnecessary complexity.',MASTERY:'Your Direction capability is at the Mastery stage. You have developed a strong instinct for translating intention into direction AI can act on. You understand that the quality of the destination you define has enormous influence on the quality of the journey. Your opportunity now is to turn that instinct into a repeatable system you can apply across increasingly complex work.'};
function result(){try{var r=window.MAXESS_RESULT;return r&&typeof r==='object'?r:null}catch(e){return null}}
function direction(r){if(!r)return null;var lists=[r.dimensions,r.fiveDimensions];for(var l=0;l<lists.length;l++){var a=lists[l];if(!Array.isArray(a))continue;for(var i=0;i<a.length;i++){var d=a[i],id=String(d&&(d.id||d.name||'')).toLowerCase().replace(/[^a-z0-9]/g,'');if(id==='direction'){var n=Number(d.score);return isFinite(n)?n:null}}}var direct=Number(r.directionScore);return isFinite(direct)?direct:null}
function render(r){var score=direction(r);if(score===null){scoreEl.textContent='—';markerEl.textContent='—';markerEl.style.left='0%';stageEl.textContent='RESULT PENDING';copyEl.innerHTML='<strong>Your Direction result is awaiting the MAXESS result contract.</strong> This section will populate from your real result as soon as it arrives.';waitingEl.hidden=false;return}score=Math.max(0,Math.min(100,score));var stage=score<50?'FOUNDATION':score<75?'DEVELOPING':score<90?'ADVANCING':'MASTERY';var range=stage==='FOUNDATION'?'0–49':stage==='DEVELOPING'?'50–74':stage==='ADVANCING'?'75–89':'90–100';var prefix={FOUNDATION:'Foundation',DEVELOPING:'Developing',ADVANCING:'Advancing',MASTERY:'Mastery'}[stage];scoreEl.textContent=Math.round(score);markerEl.textContent=Math.round(score);markerEl.style.left=score+'%';stageEl.innerHTML=prefix+' <span>· '+range+'</span>';var sentence=texts[stage],p=sentence.indexOf('.');copyEl.innerHTML='<strong>'+sentence.slice(0,p+1)+'</strong>'+sentence.slice(p+1);waitingEl.hidden=true}
render(result());window.addEventListener('MAXESS_RESULT_READY',function(e){render(e.detail&&typeof e.detail==='object'?e.detail:result())});window.addEventListener('maxess:result-updated',function(e){render(e.detail&&typeof e.detail==='object'?e.detail:result())});window.addEventListener('storage',function(){render(result())});
})();
</script>'''
e04 = re.sub(r'<script>\n\(function\(\)\{.*?</script>', new_e04, e04, count=1, flags=re.S)
Path('E04-SECTION-04-WORKING.html').write_text(e04)

# Fail closed if the requested changes did not actually apply.
assert 'MAXESS_INTEREST_STAGE_REMOVED' in assessment.read_text()
assert 'Naya%20Profile%206.jpg' in assessment.read_text()
assert 'function getDimensions' in e02
assert 'function direction' in e04
assert 'E01-SECTION-01-WORKING.html' not in subprocess.check_output(['git','status','--porcelain'],text=True)
