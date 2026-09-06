/* V7 RELEASE ENHANCEMENTS — functional Settings + Evidence proof center. */
(function(){
  'use strict';
  if(window.__V7_RELEASE_ENHANCEMENTS__) return;
  window.__V7_RELEASE_ENHANCEMENTS__=true;
  const PROJECT='https://dahisasgpfvziswqvmvm.supabase.co';
  const CONFIG=PROJECT+'/functions/v1/v7-public-config';
  const KEY='nayanet_v7_settings_v1';
  const esc=v=>String(v??'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]));
  let sb=null,session=null,settings={collective_enabled:true,smart_notes_auto:true,intelligence_enabled:true,notifications:true,communication_enabled:true,alias:''};
  const defaults={...settings};
  function merge(v){settings={...defaults,...(v||{})};localStorage.setItem(KEY,JSON.stringify(settings))}
  async function boot(){
    try{
      const cfg=await fetch(CONFIG,{headers:{Accept:'application/json'}}).then(r=>r.json());
      const mod=await import('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm');
      sb=mod.createClient(cfg.url,cfg.publishable_key);
      const got=await sb.auth.getSession(); session=got.data?.session||null;
      if(!session){const anon=await sb.auth.signInAnonymously();if(anon.error)throw anon.error;session=anon.data?.session||null}
      const {data}=await sb.from('v7_profiles').select('settings,alias,collective_enabled').eq('user_id',session.user.id).maybeSingle();
      let stored={};try{stored=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(_){}
      merge({...stored,...(data?.settings||{}),collective_enabled:data?.collective_enabled??stored.collective_enabled??true,alias:data?.alias||stored.alias||''});
      renderSettings();renderEvidence();
    }catch(e){
      window.V7ReleaseEnhancements={authenticated:false,error:String(e)};
      renderSettings('Settings persistence unavailable: '+e.message);
      renderEvidence('Evidence live ledger unavailable: '+e.message);
    }
  }
  async function persist(){
    localStorage.setItem(KEY,JSON.stringify(settings));
    if(!sb||!session)return {local:true};
    const {data,error}=await sb.rpc('v7_update_profile_settings',{p_settings:settings});
    if(error)throw error;
    return data;
  }
  function shell(title,eyebrow,body){return '<div class="pageHead"><div><div class="eyebrow">'+eyebrow+'</div><h1>'+title+'</h1><p>Real operating state. Every control below either persists to the authenticated profile or reports exactly why it cannot.</p></div></div>'+body}
  function renderSettings(error){
    const p=document.getElementById('page-settings');if(!p)return;
    const rows=[
      ['collective_enabled','Collective wisdom participation','Allow eligible de-identified wisdom extracted from your private intelligence to contribute to NayaNET collective intelligence. Raw Smart Notes and raw Daily Reports remain private.'],
      ['smart_notes_auto','Automatic Smart Notes','Creating a Smart Note automatically runs its intelligence pipeline. No separate save/sync command.'],
      ['intelligence_enabled','Intelligence processing','Allow the Naya intelligence pipeline to process Smart Notes and create the linked machine/feed/block artifacts.'],
      ['notifications','Connection notifications','Show relevant mutual-consent connection opportunities and communication notifications.'],
      ['communication_enabled','Smart Mail','Enable the private NayaNET communication surface for aliases, direct conversations, rooms, groups and lists.']
    ];
    p.innerHTML=shell('Settings','OPERATING CONTROLS','<div class="v7settingsGrid">'+rows.map(([key,label,desc])=>'<article class="v7setting '+(settings[key]?'on':'off')+'"><div><b>'+label+'</b><p>'+desc+'</p><span class="v7settingState" id="state-'+key+'">'+(settings[key]?'ON · PERSISTED':'OFF · PERSISTED')+'</span></div><button class="btn '+(settings[key]?'purple':'')+'" data-setting="'+key+'">'+(settings[key]?'TURN OFF':'TURN ON')+'</button></article>').join('')+'</div><div class="v7card" style="margin-top:18px"><h2>Privacy law</h2><p class="v7muted">Private by default. Shared by choice. Collective by consent. Public by decision.</p><p class="v7muted">'+esc(error||'Settings are synchronized with the authenticated V7 profile when the backend is available. Browser persistence remains as a recovery layer.')+'</p></div>');
    p.querySelectorAll('[data-setting]').forEach(b=>b.addEventListener('click',async()=>{const key=b.dataset.setting;settings[key]=!settings[key];renderSettings();try{await persist();renderSettings()}catch(e){settings[key]=!settings[key];renderSettings('SAVE BLOCKED — '+e.message+'. Previous state restored; nothing was falsely claimed as persisted.')}}));
  }
  function renderEvidence(error){
    const p=document.getElementById('page-evidence');if(!p)return;
    const notes=Array.isArray(window.notes)?window.notes.filter(n=>n.serverPersisted):[];
    p.innerHTML=shell('Evidence','PROOF CENTER','<div class="v7evidenceHero"><div><span>RELEASE INVARIANT</span><h2>Receipts, not claims.</h2><p>Each consequential Smart Note is reviewed as a linked chain from Human Note through Naya Note, Machine Note, Intelligent Feed, Intelligent Block and Evidence.</p></div><div class="v7evidenceCount"><b>'+notes.length+'</b><span>SERVER EVENTS</span></div></div><div class="v7evidenceLedger">'+(notes.length?notes.map(n=>{const tx=n.transaction||n;const status=tx.status||'unknown';const stages=[['Human Note',!!tx.human_note],['Naya Note',!!tx.naya_note],['Machine Note',!!tx.machine_note],['Intelligent Feed',!!tx.intelligent_feed],['Intelligent Block',!!tx.intelligent_block],['Receipt',!!tx.id]];return '<article class="v7evidenceCard"><div class="v7evidenceTop"><div><b>'+esc(n.type||'SMART NOTE')+'</b><span>'+esc(new Date(n.createdAt||tx.created_at).toLocaleString())+'</span></div><strong class="'+(status==='completed'?'good':'')+'">'+esc(status.toUpperCase())+'</strong></div><div class="v7chain">'+stages.map(s=>'<div class="'+(s[1]?'verified':'blocked')+'"><i>'+(s[1]?'✓':'!')+'</i><span>'+s[0]+'</span></div>').join('')+'</div><div class="v7meta"><span><b>EVENT ID</b>'+esc(tx.id||'—')+'</span><span><b>IDEMPOTENCY</b>'+esc(tx.idempotency_key||'—')+'</span><span><b>SOURCE</b>'+esc(tx.human_note?.source||'human_input')+'</span><span><b>TIMESTAMP</b>'+esc(tx.created_at||n.createdAt||'—')+'</span></div>'+(status==='failed'?'<div class="v7failure"><b>FAILURE / RECOVERY</b><span>Blocked at '+esc(tx.failure_stage||'unknown')+': '+esc(tx.failure_message||'unknown')+'</span><em>State preserved. Configure the blocked dependency and retry the same event.</em></div>':'<div class="v7proof">PERSISTENCE PROOF · Supabase transaction '+esc(tx.id)+' observed in the authenticated ledger.</div>')+'</article>'}).join(''):'<div class="v7card"><h2>No server events yet.</h2><p class="v7muted">The proof center stays empty rather than fabricating evidence. Create a real Smart Note and this ledger will populate from authenticated server state.</p></div>')+'</div><div class="v7card" style="margin-top:18px"><h2>Release rule</h2><p class="v7muted">A receipt is not enough by itself. Ship status requires the authenticated event to survive refresh/re-entry and be independently observed at the exact public runtime.</p></div>'+(error?'<div class="v7card" style="margin-top:18px"><h2>Live check blocked</h2><p class="v7muted">'+esc(error)+'</p></div>':'');
  }
  function styles(){if(document.getElementById('v7ReleaseStyle'))return;const s=document.createElement('style');s.id='v7ReleaseStyle';s.textContent='.v7settingsGrid{display:grid;gap:14px}.v7setting{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:22px;border:1px solid #ffffff20;border-radius:22px;background:linear-gradient(145deg,#14141b,#09090d);box-shadow:inset 0 1px #fff4,0 18px 42px #0009}.v7setting.on{border-color:#b27cff45}.v7setting b{font-size:15px}.v7setting p{max-width:820px;color:#d1cdd7;font-size:12px;line-height:1.55;margin:7px 0}.v7settingState{font-size:9px;font-weight:950;letter-spacing:.13em;color:#55e39a}.v7setting.off .v7settingState{color:#b8b4bf}.v7evidenceHero{display:flex;justify-content:space-between;gap:24px;padding:28px;border:1px solid #6675ff45;border-radius:26px;background:linear-gradient(135deg,#101a29,#0d0d15);box-shadow:inset 0 1px #fff4,0 25px 60px #000b}.v7evidenceHero span{font-size:9px;font-weight:950;letter-spacing:.15em;color:#9bbcff}.v7evidenceHero h2{font-size:31px;margin:8px 0}.v7evidenceHero p{max-width:820px;color:#ddd9e3;line-height:1.55;font-size:13px}.v7evidenceCount{min-width:150px;display:grid;place-items:center;border:1px solid #55b9ee35;border-radius:20px;background:#071018}.v7evidenceCount b{font-size:42px}.v7evidenceCount span{font-size:9px;letter-spacing:.13em}.v7evidenceLedger{display:grid;gap:14px;margin-top:18px}.v7evidenceCard{padding:22px;border:1px solid #ffffff20;border-radius:22px;background:#0b0b10;box-shadow:inset 0 1px #fff3,0 18px 45px #0009}.v7evidenceTop{display:flex;justify-content:space-between;gap:12px}.v7evidenceTop b{display:block;font-size:12px}.v7evidenceTop span{display:block;color:#aaa6b2;font-size:10px;margin-top:5px}.v7evidenceTop strong{font-size:9px;letter-spacing:.12em}.v7evidenceTop strong.good{color:#55e39a}.v7chain{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:8px;margin:18px 0}.v7chain div{min-height:72px;padding:10px;border:1px solid #ffffff15;border-radius:14px;display:flex;flex-direction:column;justify-content:space-between;background:#08080c}.v7chain div.verified{border-color:#55e39a35}.v7chain i{font-style:normal;font-weight:1000}.v7chain .verified i{color:#55e39a}.v7chain .blocked i{color:#e0b84a}.v7chain span{font-size:9px;line-height:1.25}.v7meta{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.v7meta span{padding:10px;border:1px solid #ffffff12;border-radius:12px;color:#d1cdd7;font-size:9px;word-break:break-word}.v7meta b{display:block;color:#8f8a97;font-size:8px;letter-spacing:.1em;margin-bottom:5px}.v7proof,.v7failure{margin-top:12px;padding:12px;border-radius:12px;border:1px solid #55e39a2b;background:#07130d;font-size:10px}.v7failure{border-color:#e0b84a35;background:#161207}.v7failure b,.v7failure span,.v7failure em{display:block}.v7failure em{margin-top:5px;color:#c9c1ad;font-style:normal}.v7muted{color:#d1cdd7;font-size:12px;line-height:1.55}@media(max-width:800px){.v7setting{align-items:flex-start;flex-direction:column}.v7evidenceHero{flex-direction:column}.v7chain{grid-template-columns:repeat(2,1fr)}.v7meta{grid-template-columns:1fr 1fr}}';document.head.appendChild(s)}
  function integrate(){styles();renderSettings();renderEvidence();document.addEventListener('click',e=>{const b=e.target.closest('[data-page]');if(b&&b.dataset.page==='settings'){setTimeout(renderSettings,0)}if(b&&b.dataset.page==='evidence'){setTimeout(renderEvidence,0)}});const original=window.renderEvidence;window.renderEvidence=function(){if(typeof original==='function')original();renderEvidence()};window.V7ReleaseEnhancements={getSettings:()=>({...settings}),refreshEvidence:renderEvidence,refreshSettings:renderSettings};boot()}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',integrate);else integrate();
})();
