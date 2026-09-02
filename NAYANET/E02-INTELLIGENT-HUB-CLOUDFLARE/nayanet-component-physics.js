/* NayaNET — Component Physics Runtime
   One interaction language for every surface.
   DEPTH -> LIGHT -> STATE -> RESPONSE -> CONSEQUENCE */
(()=>{'use strict';
  const root=document.documentElement, body=document.body;
  const q=(s,c=document)=>c.querySelector(s), qa=(s,c=document)=>[...c.querySelectorAll(s)];
  const buttonSelector='button,[role="button"]';
  const inputSelector='input,textarea,select';
  const iconSelector='.brand-symbol,.ask-orb,.world-glyph,.core-eye,.player-live,.center-status i,.field-callout span';
  const classify=()=>{
    qa(buttonSelector).forEach(el=>{
      if(el.closest('#frontDoor')) return;
      el.classList.add('np-power-object');
      if(el.matches('.world,.world-card,.cast')) el.classList.add('np-intelligence-surface');
      if(el.matches('.naya-core,.ask-naya,.play-button')) el.dataset.npTone='intelligence';
      else if(el.matches('.world,.world-card')) el.dataset.npTone='knowledge';
      else if(el.matches('.world-secondary,.return-button')) el.dataset.npTone='connection';
      else if(el.matches('[data-action="goal"],[data-action="note"]')) el.dataset.npTone='growth';
      else if(el.matches('[data-action="copyid"],[data-action="copylink"]')) el.dataset.npTone='significance';
    });
    qa(inputSelector).forEach(el=>{
      if(el.closest('#frontDoor')) return;
      el.classList.add('np-identity-portal');
      if(el.value.trim()) el.classList.add('np-valid');
    });
    qa(iconSelector).forEach(el=>el.classList.add('np-intelligence-icon'));
    const seek=q('#seek'); if(seek) seek.classList.add('np-energy-path');
    const waveform=q('#waveform'); if(waveform) waveform.classList.add('np-energy-path');
  };
  const sunState=(name)=>{
    body.classList.remove('np-state-idle','np-state-approach','np-state-touch','np-state-intelligence','np-state-speaking','np-state-playing','np-state-return');
    body.classList.add(`np-state-${name}`);
  };
  sunState('idle');

  document.addEventListener('pointerover',e=>{
    const el=e.target.closest(buttonSelector); if(!el) return;
    if(el.matches('.naya-core,.ask-naya')) sunState('approach');
  },{passive:true});
  document.addEventListener('pointerout',e=>{
    const el=e.target.closest(buttonSelector); if(!el) return;
    if(el.matches('.naya-core,.ask-naya')) sunState(body.classList.contains('audio-live')?'playing':'idle');
  },{passive:true});
  document.addEventListener('pointerdown',e=>{
    const el=e.target.closest(buttonSelector); if(!el||el.disabled) return;
    el.classList.add('np-pressed');
    if(el.matches('.naya-core,.ask-naya,.world,.world-card')) sunState('touch');
  },{passive:true});
  ['pointerup','pointercancel'].forEach(type=>document.addEventListener(type,e=>{
    const el=e.target.closest(buttonSelector); if(!el) return;
    window.setTimeout(()=>el.classList.remove('np-pressed'),90);
    if(el.matches('.naya-core,.ask-naya')) window.setTimeout(()=>sunState(body.classList.contains('audio-live')?'playing':'intelligence'),120);
  },{passive:true}));

  document.addEventListener('input',e=>{
    const el=e.target.closest(inputSelector); if(!el) return;
    el.classList.toggle('np-valid',!!el.value.trim());
    el.classList.toggle('np-invalid',false);
  });
  document.addEventListener('change',e=>{
    const el=e.target.closest(inputSelector); if(el) el.classList.toggle('np-valid',!!String(el.value||'').trim());
  });
  document.addEventListener('focusin',e=>{
    const el=e.target.closest(inputSelector); if(el) el.dataset.npState='active';
    if(e.target.closest('#nameInput')) sunState('touch');
  });
  document.addEventListener('focusout',e=>{
    const el=e.target.closest(inputSelector); if(el) el.dataset.npState=el.value.trim()?'ready':'idle';
  });

  document.addEventListener('click',e=>{
    const el=e.target.closest(buttonSelector); if(!el) return;
    if(el.matches('.world,.world-card')){
      qa('.world,.world-card').forEach(x=>x.classList.remove('np-selected'));
      el.classList.add('np-selected');
      sunState('intelligence');
    }
  });

  window.addEventListener('naya:audio-state',e=>{
    const playing=!!e.detail?.playing;
    body.classList.toggle('audio-live',playing);
    sunState(playing?'playing':'idle');
    const seek=q('#seek'); if(seek) seek.classList.toggle('np-active',playing);
    const waveform=q('#waveform'); if(waveform) waveform.classList.toggle('np-active',playing);
  });
  const audio=q('#audio');
  if(audio){
    audio.addEventListener('play',()=>{body.classList.add('audio-live');sunState('playing');});
    audio.addEventListener('pause',()=>{body.classList.remove('audio-live');sunState('idle');});
    audio.addEventListener('ended',()=>{body.classList.remove('audio-live');sunState('return');window.setTimeout(()=>sunState('idle'),700);});
  }
  window.addEventListener('naya:data-ready',()=>classify());
  const observer=new MutationObserver(()=>classify());
  observer.observe(document.body,{childList:true,subtree:true});
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',classify,{once:true}); else classify();
  window.NayaNETPhysics={version:'1.0',state:sunState,refresh:classify};
})();
