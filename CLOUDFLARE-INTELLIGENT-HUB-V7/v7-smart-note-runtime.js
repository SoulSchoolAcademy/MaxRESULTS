/* V7 SMART NOTE RUNTIME — source-preserving integration layer. */
(function(){
  'use strict';
  if(window.__V7_SMART_NOTE_RUNTIME__) return;
  window.__V7_SMART_NOTE_RUNTIME__=true;
  const PROJECT='https://dahisasgpfvziswqvmvm.supabase.co';
  const CONFIG=PROJECT+'/functions/v1/v7-public-config';
  const NAYA=PROJECT+'/functions/v1/v7-naya-note';
  const PIPE=PROJECT+'/functions/v1/v7-smart-note';
  const RPC_FAILURE='v7_preserve_smart_note_failure';
  const RPC_LIST='v7_list_smart_notes';
  const KEY='nayanet_v7_smart_notes';
  let sb=null,session=null,lastTransaction=null;
  const nativeRenderNotes=window.renderNotes;
  const nativeUpdateMetrics=window.updateMetrics;
  const nativeRenderReport=window.renderReport;
  const nativeRenderEvidence=window.renderEvidence;
  function localLoad(){try{return JSON.parse(localStorage.getItem(KEY)||'[]')}catch(_){return []}}
  function localSave(a){try{localStorage.setItem(KEY,JSON.stringify(a))}catch(_) {}}
  function esc(v){return String(v??'').replace(/[&<>'"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c]))}
  function pretty(v){return typeof v==='string'?v:JSON.stringify(v??{},null,2)}
  function msg(text,good){
    const a=document.getElementById('reportStatus');if(a){a.textContent=text;a.classList.toggle('good',!!good)}
    const b=document.getElementById('connectionStatus');if(b){b.textContent=text;b.classList.toggle('good',!!good)}
  }
  function txFor(n){return n?.transaction||n}
  function perspective(n,tab){
    const tx=txFor(n);
    if(!tx||!tx.human_note)return n?.text||'';
    if(tab==='human')return tx.human_note?.text||tx.human_note?.content||'';
    if(tab==='naya')return tx.naya_note?pretty(tx.naya_note):'Naya Note unavailable. The transaction is preserved at the exact blocked stage.';
    if(tab==='machine')return pretty(tx.machine_note||{event_id:tx.id,created_at:tx.created_at,idempotency_key:tx.idempotency_key,status:tx.status});
    return pretty(tx.intelligent_feed||{event_id:tx.id,status:tx.status});
  }
  function renderServerNotes(){
    const q=(document.getElementById('noteSearch')?.value||'').toLowerCase();
    const filter=window.activeFilter||'ALL';
    const all=Array.isArray(window.notes)?window.notes:[];
    const list=all.filter(n=>(filter==='ALL'||n.type===filter)&&(!q||String(n.text||'').toLowerCase().includes(q)||String(n.type||'').toLowerCase().includes(q))).sort((a,b)=>new Date(b.createdAt)-new Date(a.createdAt));
    const root=document.getElementById('noteList');if(!root)return;
    if(!list.length){root.innerHTML='<div class="empty"><b>No matching Intelligent Blocks.</b><span>Write a Smart Note above, or change your search/filter. The feed stays empty rather than inventing personal intelligence.</span></div>';return}
    root.innerHTML=list.map(n=>{
      const tx=txFor(n), tab=(window.activeNoteTab&&window.activeNoteTab[n.id])||'human';
      const failed=tx?.status==='failed'||n.failed;
      const block=tx?.intelligent_block;
      const title=failed?'Smart Note Preserved — Recovery Required':'Intelligent Block';
      const status=failed?'BLOCKED AT '+String(tx.failure_stage||n.failureStage||'UNKNOWN').toUpperCase():'SERVER PERSISTED';
      const receipt=tx?.id||n.id;
      const blockText=block?pretty(block):failed?('Failure: '+(tx.failure_message||n.failureMessage||'Unknown failure')+'\nRecovery: configure the blocked dependency, then retry this event.'):'Awaiting server transaction.';
      return '<article class="noteCard"><div class="noteTop"><span class="noteTime">'+esc(new Date(n.createdAt).toLocaleTimeString([], {hour:'2-digit',minute:'2-digit'}))+' · '+esc(n.type)+'</span><span class="noteType">'+esc(status)+'</span></div><div class="noteBody"><h3>'+title+'</h3><p>'+esc(n.text)+'</p><div class="statusBox">RECEIPT · '+esc(receipt)+'<br>IDEMPOTENCY · '+esc(tx?.idempotency_key||'—')+'</div></div><div class="noteTabs">'+['human','naya','machine','feed'].map(t=>'<button class="noteTab '+(tab===t?'active':'')+'" data-note-tab="'+t+'" data-note-id="'+esc(n.id)+'">'+(t==='feed'?'INTELLIGENT FEED':t.toUpperCase())+'</button>').join('')+'</div><div class="noteView"><strong>'+(tab==='feed'?'INTELLIGENT FEED':tab.toUpperCase()+' NOTE')+'</strong><span>'+esc(perspective(n,tab))+'</span></div><div class="noteView"><strong>INTELLIGENT BLOCK</strong><span>'+esc(blockText)+'</span></div></article>'
    }).join('');
  }
  function renderServerMetrics(){
    if(nativeUpdateMetrics)nativeUpdateMetrics();
    const rows=Array.isArray(window.notes)?window.notes:[];
    const persisted=rows.filter(n=>n.serverPersisted);
    const el=document.getElementById('metricBlocks');if(el)el.textContent=persisted.length;
    const src=document.getElementById('metricSource');if(src&&persisted.length)src.textContent='SUPABASE';
  }
  function renderServerReport(){
    if(nativeRenderReport)nativeRenderReport();
    if(lastTransaction){
      const st=document.getElementById('reportStatus');if(st)st.textContent='Server transaction observed: '+lastTransaction.id+'. Status: '+lastTransaction.status+'.';
    }
  }
  function renderServerEvidence(){
    if(nativeRenderEvidence)nativeRenderEvidence();
    const el=document.getElementById('evidenceEvents');if(el)el.textContent=(Array.isArray(window.notes)?window.notes.filter(n=>n.serverPersisted).length:0)+' server-persisted Smart Note events in this authenticated session.';
  }
  window.renderNotes=renderServerNotes;
  window.updateMetrics=renderServerMetrics;
  window.renderReport=renderServerReport;
  window.renderEvidence=renderServerEvidence;
  async function hydrate(){
    const {data,error}=await sb.rpc(RPC_LIST);if(error)throw error;
    const rows=Array.isArray(data)?data:[];
    const mapped=rows.map(row=>({id:row.id,createdAt:row.created_at,text:row.human_note?.text||row.human_note?.content||'',type:row.human_note?.type||'INSIGHT',transaction:row,serverPersisted:true,failed:row.status==='failed',failureStage:row.failure_stage,failureMessage:row.failure_message}));
    if(mapped[0])lastTransaction=mapped[0].transaction;
    const existing=localLoad(),ids=new Set(mapped.map(n=>n.id));
    const localOnly=existing.filter(n=>!n.serverPersisted&&!ids.has(n.id));
    const merged=mapped.concat(localOnly);window.notes=merged;localSave(merged);
    renderServerNotes();renderServerMetrics();renderServerReport();renderServerEvidence();
  }
  async function callFunction(url,body){
    const r=await fetch(url,{method:'POST',headers:{Authorization:'Bearer '+session.access_token,'apikey':session.access_token,'Content-Type':'application/json'},body:JSON.stringify(body)});
    const payload=await r.json().catch(()=>({}));
    if(!r.ok)throw Object.assign(new Error(payload.reason||payload.error||('HTTP '+r.status)),{payload,status:r.status});
    return payload;
  }
  async function preserveFailure(human,idempotency,error){
    const {data,error:rpcError}=await sb.rpc(RPC_FAILURE,{p_idempotency_key:idempotency,p_user_id:session.user.id,p_human_note:human,p_failure_stage:error.payload?.failure_stage||'naya_note',p_failure_message:error.payload?.reason||error.message});
    if(rpcError)throw rpcError;
    lastTransaction=data;
    const local=localLoad();const note={id:data.id,createdAt:data.created_at,text:human.text,type:human.type,serverPersisted:true,transaction:data,failed:true,failureStage:data.failure_stage,failureMessage:data.failure_message};
    const idx=local.findIndex(n=>n.id===note.id);if(idx>=0)local[idx]=note;else local.unshift(note);window.notes=local;localSave(local);renderServerNotes();renderServerMetrics();renderServerEvidence();
    msg('SMART NOTE BLOCKED AT NAYA NOTE — Human Note preserved. Reason: '+(data.failure_message||error.message)+' Recovery: configure the production Naya intelligence provider, then retry.',false);return data;
  }
  async function invokePipeline(human,idempotency,nayaOverride,duplicate){
    if(!session)throw new Error('AUTHENTICATED_SESSION_REQUIRED');
    let naya=nayaOverride;
    if(!naya){
      try{const out=await callFunction(NAYA,{human_note:human});if(!out.ok||!out.naya_note)throw Object.assign(new Error(out.reason||'NAYA_OUTPUT_MISSING'),{payload:out});naya=out.naya_note}
      catch(e){if(duplicate)throw e;return preserveFailure(human,idempotency,e)}
    }
    const result=await callFunction(PIPE,{human_note:human,naya_note:naya,idempotency_key:idempotency});
    if(!result.ok||!result.transaction)throw new Error('SMART_NOTE_TRANSACTION_INCOMPLETE');
    lastTransaction=result.transaction;const tx=result.transaction;
    const local=localLoad(),note={id:tx.id,createdAt:tx.created_at,text:human.text,type:human.type,serverPersisted:true,transaction:tx};
    const idx=local.findIndex(n=>n.id===tx.id);if(idx>=0)local[idx]=note;else local.unshift(note);window.notes=local;localSave(local);renderServerNotes();renderServerMetrics();renderServerReport();renderServerEvidence();
    msg((duplicate?'IDEMPOTENCY VERIFIED — ':'')+'Smart Note persisted: Human → Naya → Machine → Intelligent Feed → Intelligent Block → Hub → Evidence.',true);return tx;
  }
  function capture(){
    const input=document.getElementById('noteInput');if(!input)return;const text=input.value.trim();if(!text){input.focus();return}
    const type=(typeof window.noteType==='function'?window.noteType(text):'INSIGHT');const human={text,type,created_at:new Date().toISOString(),source:'human_input',privacy:'private'};
    const idempotency=crypto.randomUUID?crypto.randomUUID():('v7-'+Date.now()+'-'+Math.random().toString(36).slice(2));input.value='';
    invokePipeline(human,idempotency).catch(e=>msg('SMART NOTE ERROR — '+e.message+'. Human input was not falsely represented as completed intelligence.',false));
  }
  document.addEventListener('click',function(e){const b=e.target.closest('#saveNote');if(!b)return;e.preventDefault();e.stopImmediatePropagation();capture()},true);
  async function boot(){
    try{
      const cfg=await fetch(CONFIG,{headers:{Accept:'application/json'}}).then(r=>r.json());if(!cfg?.url||!cfg?.publishable_key)throw new Error('PUBLIC_CONFIG_INCOMPLETE');
      const mod=await import('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm');sb=mod.createClient(cfg.url,cfg.publishable_key);
      const got=await sb.auth.getSession();session=got.data?.session||null;if(!session){const anon=await sb.auth.signInAnonymously();if(anon.error)throw new Error('AUTHENTICATION_FAILED: '+anon.error.message);session=anon.data?.session||null}
      if(!session?.access_token||!session?.user?.id)throw new Error('AUTHENTICATED_SESSION_MISSING');
      window.V7SmartNoteRuntime={authenticated:true,userId:session.user.id,async reload(){await hydrate();return true},async duplicateLast(){if(!lastTransaction?.idempotency_key)throw new Error('NO_TRANSACTION_TO_DUPLICATE');return invokePipeline(lastTransaction.human_note,lastTransaction.idempotency_key,lastTransaction.naya_note,true)},getLastTransaction(){return lastTransaction}};
      await hydrate();msg('Authenticated V7 session established. Server Smart Note rendering is active.',true);
    }catch(e){window.V7SmartNoteRuntime={authenticated:false,error:String(e)};msg('V7 Smart Note runtime blocked: '+e.message+'. No backend intelligence has been claimed.',false)}
  }
  boot();
})();
