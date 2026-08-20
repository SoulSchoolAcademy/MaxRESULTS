from pathlib import Path
import re

ASSESSMENT = Path('AIScoreMAXESS code')
MARKER = '/* MAXESS_RESULT_BRIDGE_V1 */'

BRIDGE = r'''
/* MAXESS_RESULT_BRIDGE_V1 */
(function(){
  'use strict';

  const RESULT_KEY = 'MAXESS_RESULT_V1';
  const RESULT_EVENT = 'MAXESS_RESULT_READY';
  const RESULTS_URL = 'https://results.nayanet.xyz/';

  function finite(value){
    const n = Number(value);
    return Number.isFinite(n) ? n : null;
  }

  function clampScore(value){
    const n = finite(value);
    return n === null ? null : Math.max(0, Math.min(100, n));
  }

  function safeJson(value){
    try { return JSON.stringify(value); } catch(e) { return null; }
  }

  function persist(contract){
    const json = safeJson(contract);
    if(!json) return false;
    try { sessionStorage.setItem(RESULT_KEY, json); } catch(e) {}
    try { localStorage.setItem(RESULT_KEY, json); } catch(e) {}
    return true;
  }

  function encodeContract(contract){
    const json = safeJson(contract);
    if(!json) return null;
    const bytes = new TextEncoder().encode(json);
    let binary = '';
    bytes.forEach(byte => binary += String.fromCharCode(byte));
    return btoa(binary)
      .replace(/\+/g,'-')
      .replace(/\//g,'_')
      .replace(/=+$/,'');
  }

  function dimensionLevel(score){
    if(score >= 90) return 'MASTERING';
    if(score >= 75) return 'ADVANCING';
    if(score >= 60) return 'DEVELOPING';
    return 'EMERGING';
  }

  function buildContract(){
    // These are lexical bindings from the authoritative assessment script.
    const questions = Array.isArray(MAXESS_ASSESSMENT.questions)
      ? [...MAXESS_ASSESSMENT.questions].sort((a,b)=>a.order-b.order)
      : [];
    const responses = Array.isArray(state.responses)
      ? state.responses.slice()
      : [];

    if(questions.length !== 15 || responses.length !== 15) return null;

    const dimensions = (MAXESS_ASSESSMENT.dimensions || []).map(dimension => {
      const relevant = responses.filter(r => r.dimensionId === dimension.id);
      if(!relevant.length) return null;
      const raw = relevant.reduce((sum,r)=>sum + Number(r.score || 0),0) / relevant.length;
      const score = Math.round(raw * 10) / 10;
      return {
        id: dimension.id,
        name: dimension.name,
        color: dimension.color,
        weight: dimension.weight,
        score,
        level: dimensionLevel(score)
      };
    }).filter(Boolean);

    if(dimensions.length !== 5) return null;

    const weightTotal = dimensions.reduce((sum,d)=>sum + Number(d.weight || 0),0);
    if(!weightTotal) return null;

    const overallScore = Math.round(
      (dimensions.reduce((sum,d)=>sum + d.score * Number(d.weight || 0),0) / weightTotal) * 10
    ) / 10;

    const band = (MAXESS_ASSESSMENT.scoreBands || []).find(
      item => overallScore >= item.min && overallScore <= item.max
    );
    if(!band) return null;

    const strongest = [...dimensions].sort((a,b)=>b.score-a.score)[0];
    const opportunity = [...dimensions].sort((a,b)=>a.score-b.score)[0];

    const selectedInterests = Array.from(state.selectedInterests || []);
    const interestMeta = (typeof AI_AREAS !== 'undefined' ? AI_AREAS : [])
      .filter(area => selectedInterests.includes(area.id));

    const interpretation = {
      strongestCapability: strongest.name,
      strongestScore: strongest.score,
      highestLeverageOpportunity: opportunity.name,
      opportunityScore: opportunity.score,
      masteryStage: band.label,
      summary: band.description
    };

    return {
      contractVersion: 'MAXESS_RESULT_V1',
      assessmentId: MAXESS_ASSESSMENT.id,
      assessmentVersion: MAXESS_ASSESSMENT.version,
      completedAt: state.completedAt || new Date().toISOString(),
      overallScore,
      masteryStage: band.label,
      masteryBand: band,
      fiveDimensions: dimensions,
      dimensions,
      strongestCapability: {
        id: strongest.id,
        name: strongest.name,
        score: strongest.score
      },
      highestLeverageOpportunity: {
        id: opportunity.id,
        name: opportunity.name,
        score: opportunity.score
      },
      overallPattern: dimensions.map(d => ({id:d.id,name:d.name,score:d.score,level:d.level})),
      personalizedInterpretation: interpretation,
      nextMove: {
        primary: `Strengthen ${opportunity.name}`,
        reason: `Your highest-leverage opportunity is ${opportunity.name}.`
      },
      responses,
      selectedInterests,
      selectedInterestMeta: interestMeta,
      naya: {
        name: 'Naya',
        image: 'https://i.postimg.cc/bw4fyKF8/Naya-Profile-black-face-zoom.jpg'
      }
    };
  }

  function validateContract(contract){
    if(!contract || contract.contractVersion !== 'MAXESS_RESULT_V1') return false;
    if(clampScore(contract.overallScore) === null) return false;
    if(!Array.isArray(contract.dimensions) || contract.dimensions.length !== 5) return false;
    if(!Array.isArray(contract.responses) || contract.responses.length !== 15) return false;
    return true;
  }

  function publish(){
    const contract = buildContract();
    if(!validateContract(contract)){
      console.error('MAXESS_RESULT bridge refused to publish invalid result.');
      return false;
    }

    window.MAXESS_RESULT = contract;
    persist(contract);
    window.dispatchEvent(new CustomEvent(RESULT_EVENT, {detail:contract}));
    window.dispatchEvent(new CustomEvent('maxess:result-updated', {detail:contract}));

    const encoded = encodeContract(contract);
    if(!encoded) return false;

    window.location.assign(`${RESULTS_URL}#maxess-result=${encoded}`);
    return true;
  }

  function ensureNayaFields(){
    MAXESS_ASSESSMENT.questions.forEach(question => {
      if(!Object.prototype.hasOwnProperty.call(question,'nayaScript')){
        question.nayaScript = question.teaching || '';
      }
      if(!Object.prototype.hasOwnProperty.call(question,'nayaAudio')){
        question.nayaAudio = null;
      }
    });
  }

  window.MAXESS_RESULT_BRIDGE = {buildContract, validateContract, publish, ensureNayaFields};
  ensureNayaFields();

  // Retire the old Results presentation. The new Results product is the sole renderer.
  window.finishInterestSelection = function(){ publish(); };
  const oldResults = document.getElementById('resultsView');
  if(oldResults){
    oldResults.setAttribute('data-retired-renderer','true');
    oldResults.style.display = 'none';
  }

  // Naya appears in the teaching popup only — not on every question slide.
  const interstitial = document.getElementById('teachingInterstitial');
  const cloud = interstitial && interstitial.querySelector('.teaching-cloud');
  if(cloud && !cloud.querySelector('.maxess-naya-teacher')){
    const style = document.createElement('style');
    style.textContent = `
      .maxess-naya-teacher{display:grid;grid-template-columns:auto minmax(0,1fr);align-items:center;gap:14px;margin:0 auto 22px;max-width:560px;text-align:left}
      .maxess-naya-teacher-image{width:58px;height:58px;border-radius:50%;object-fit:cover;border:2px solid rgba(255,255,255,.92);box-shadow:0 0 0 5px rgba(155,99,255,.14),0 0 28px rgba(155,99,255,.24)}
      .maxess-naya-teacher-copy{display:flex;flex-direction:column;min-width:0}
      .maxess-naya-teacher-copy strong{font-size:17px;font-weight:950;color:#fff}
      .maxess-naya-teacher-copy span{margin-top:4px;font-size:12px;color:#cfc8da;font-weight:700}
      .maxess-listen-naya{grid-column:1/-1;width:100%;margin-top:2px;min-height:54px}
      @media(max-width:600px){.maxess-naya-teacher{gap:11px}.maxess-naya-teacher-image{width:52px;height:52px}}
    `;
    document.head.appendChild(style);

    const teacher = document.createElement('div');
    teacher.className = 'maxess-naya-teacher';
    teacher.innerHTML = `
      <img src="https://i.postimg.cc/bw4fyKF8/Naya-Profile-black-face-zoom.jpg" alt="Naya" class="maxess-naya-teacher-image">
      <div class="maxess-naya-teacher-copy">
        <strong>Naya</strong>
        <span>Let me walk you through this.</span>
      </div>
      <button type="button" class="cloud-button maxess-listen-naya" id="listenToNaya" aria-label="Listen to Naya">LISTEN TO NAYA</button>
    `;
    const eyebrow = cloud.querySelector('.cloud-eyebrow');
    cloud.insertBefore(teacher, eyebrow || cloud.firstChild);

    document.getElementById('listenToNaya').addEventListener('click', function(){
      if(typeof closeTeachingCloud === 'function') closeTeachingCloud();
      const q = typeof currentQuestion === 'function' ? currentQuestion() : null;
      const audio = q && q.nayaAudio;
      if(audio && typeof audio === 'string'){
        try{
          const player = new Audio(audio);
          player.addEventListener('ended',()=>window.dispatchEvent(new CustomEvent('naya:audio-end')),{once:true});
          player.addEventListener('error',()=>window.dispatchEvent(new CustomEvent('naya:audio-error')),{once:true});
          window.__MAXESS_NAYA_AUDIO = player;
          player.play().then(()=>{
            window.dispatchEvent(new CustomEvent('naya:audio-start',{detail:{questionId:q.id}}));
          }).catch(()=>{});
        }catch(e){}
        return;
      }
      window.dispatchEvent(new CustomEvent('naya:audio-unavailable',{detail:{questionId:q && q.id}}));
    });
  }

})();
'''

s = ASSESSMENT.read_text(encoding='utf-8')
if MARKER not in s:
    idx = s.rfind('</script>')
    if idx < 0:
        raise SystemExit('No closing script tag found in assessment source')
    s = s[:idx] + '\n' + BRIDGE + '\n' + s[idx:]

pattern = re.compile(r'function finishInterestSelection\(\)\{.*?\n\}', re.S)
replacement = '''function finishInterestSelection(){\n\n  if(window.MAXESS_RESULT_BRIDGE && typeof window.MAXESS_RESULT_BRIDGE.publish === "function"){\n    window.MAXESS_RESULT_BRIDGE.publish();\n    return;\n  }\n\n  throw new Error("MAXESS_RESULT_BRIDGE unavailable; refusing legacy Results renderer.");\n\n}'''
s, count = pattern.subn(replacement, s, count=1)
if count != 1:
    raise SystemExit('Could not replace finishInterestSelection safely')

ASSESSMENT.write_text(s, encoding='utf-8')
print('patched assessment:', len(s.encode()), 'bytes')
