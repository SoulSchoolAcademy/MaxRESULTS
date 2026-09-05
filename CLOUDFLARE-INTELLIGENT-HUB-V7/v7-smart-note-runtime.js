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
  let sb=null;
  let session=null;
  let lastTransaction=null;
  const nativeSave=window.saveNote;
  function localLoad(){try{return JSON.parse(localStorage.getItem(KEY)||'[]')}catch(_){return []}}
  function localSave(a){try{localStorage.setItem(KEY,JSON.stringify(a))}catch(_) {}}
  function msg(text,good){
    const el=document.getElementById('reportStatus');
    if(el){el.textContent=text;el.classList.toggle('good',!!good)}
    const st=document.getElementById('connectionStatus');
    if(st){st.textContent=text;st.classList.toggle('good',!!good)}
  }
  async function boot(){
    try{
      const cfg=await fetch(CONFIG,{headers:{Accept:'application/json'}}).then(r=>r.json());
      if(!cfg?.url||!cfg?.publishable_key) throw new Error('PUBLIC_CONFIG_INCOMPLETE');
      const mod=await import('https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm');
      sb=mod.createClient(cfg.url,cfg.publishable_key);
      const got=await sb.auth.getSession();
      session=got.data?.session||null;
      if(!session){
        const anon=await sb.auth.signInAnonymously();
        if(anon.error) throw new Error('AUTHENTICATION_FAILED: '+anon.error.message);
        session=anon.data?.session||null;
      }
      if(!session?.access_token||!session?.user?.id) throw new Error('AUTHENTICATED_SESSION_MISSING');
      await hydrate();
      window.V7SmartNoteRuntime={
        authenticated:true,
        userId:session.user.id,
        async reload(){await hydrate();return true},
        async duplicateLast(){
          if(!lastTransaction?.idempotency_key) throw new Error('NO_TRANSACTION_TO_DUPLICATE');
          return invokePipeline(lastTransaction.human_note,lastTransaction.idempotency_key,lastTransaction.naya_note,true);
        },
        getLastTransaction(){return lastTransaction}
      };
      msg('Authenticated V7 session established. Smart Note backend is available for runtime execution.',true);
    }catch(e){
      window.V7SmartNoteRuntime={authenticated:false,error:String(e)};
      msg('V7 Smart Note runtime blocked: '+e.message+'. No backend intelligence has been claimed.');
    }
  }
  async function hydrate(){
    if(!sb||!session)return;
    const {data,error}=await sb.rpc(RPC_LIST);
    if(error) throw error;
    const rows=Array.isArray(data)?data:[];
    const existing=localLoad();
    const merged=rows.map(row=>({
      id:row.id,
      createdAt:row.created_at,
      text:row.human_note?.text||row.human_note?.content||'',
      type:row.human_note?.type||'INSIGHT',
      transaction:row,
      serverPersisted:true
    }));
    const serverIds=new Set(merged.map(n=>n.id));
    const localOnly=existing.filter(n=>!n.serverPersisted&&!serverIds.has(n.id));
    localSave(merged.concat(localOnly));
    window.notes=merged.concat(localOnly);
    if(typeof window.renderNotes==='function') window.renderNotes();
    if(typeof window.updateMetrics==='function') window.updateMetrics();
    if(typeof window.renderReport==='function') window.renderReport();
    if(typeof window.renderEvidence==='function') window.renderEvidence();
  }
  async function callFunction(url,body){
    const r=await fetch(url,{method:'POST',headers:{Authorization:'Bearer '+session.access_token,'apikey':session.access_token,'Content-Type':'application/json'},body:JSON.stringify(body)});
    const payload=await r.json().catch(()=>({}));
    if(!r.ok) throw Object.assign(new Error(payload.reason||payload.error||('HTTP '+r.status)),{payload,status:r.status});
    return payload;
  }
  async function preserveFailure(human,idempotency,error){
    const {data,error:rpcError}=await sb.rpc(RPC_FAILURE,{p_idempotency_key:idempotency,p_user_id:session.user.id,p_human_note:human,p_failure_stage:error.payload?.failure_stage||'naya_note',p_failure_message:error.payload?.reason||error.message});
    if(rpcError) throw rpcError;
    lastTransaction=data;
    const local=localLoad();
    const note={id:idempotency,createdAt:human.created_at,text:human.text,type:human.type,serverPersisted:false,failed:true,failureStage:'naya_note',failureMessage:error.payload?.reason||error.message};
    local.unshift(note);localSave(local);
    if(typeof window.renderNotes==='function') window.renderNotes();
    msg('SMART NOTE BLOCKED AT NAYA NOTE — Human Note preserved. Reason: '+(error.payload?.reason||error.message)+' Recovery: configure the production Naya intelligence provider, then retry.',false);
    return data;
  }
  async function invokePipeline(human,idempotency,nayaOverride,duplicate){
    if(!session) throw new Error('AUTHENTICATED_SESSION_REQUIRED');
    let naya=nayaOverride;
    if(!naya){
      try{
        const out=await callFunction(NAYA,{human_note:human});
        if(!out.ok||!out.naya_note) throw Object.assign(new Error(out.reason||'NAYA_OUTPUT_MISSING'),{payload:out});
        naya=out.naya_note;
      }catch(e){
        if(duplicate) throw e;
        return preserveFailure(human,idempotency,e);
      }
    }
    const result=await callFunction(PIPE,{human_note:human,naya_note:naya,idempotency_key:idempotency});
    if(!result.ok||!result.transaction) throw new Error('SMART_NOTE_TRANSACTION_INCOMPLETE');
    lastTransaction=result.transaction;
    const tx=result.transaction;
    const local=localLoad();
    const note={id:tx.id,createdAt:tx.created_at,text:human.text,type:human.type,serverPersisted:true,transaction:tx};
    const idx=local.findIndex(n=>n.id===tx.id);if(idx>=0)local[idx]=note;else local.unshift(note);localSave(local);
    window.notes=local;
    if(typeof window.renderNotes==='function') window.renderNotes();
    if(typeof window.updateMetrics==='function') window.updateMetrics();
    if(typeof window.renderReport==='function') window.renderReport();
    if(typeof window.renderEvidence==='function') window.renderEvidence();
    msg((duplicate?'IDEMPOTENCY VERIFIED — ':'')+'Smart Note persisted: Human → Naya → Machine → Intelligent Feed → Intelligent Block → Hub → Evidence.',true);
    return tx;
  }
  function capture(){
    const input=document.getElementById('noteInput');
    if(!input)return;
    const text=input.value.trim();if(!text){input.focus();return}
    const type=(typeof window.noteType==='function'?window.noteType(text):'INSIGHT');
    const created_at=new Date().toISOString();
    const human={text,type,created_at,source:'human_input',privacy:'private'};
    const idempotency=crypto.randomUUID?crypto.randomUUID():('v7-'+Date.now()+'-'+Math.random().toString(36).slice(2));
    input.value='';
    invokePipeline(human,idempotency).catch(e=>msg('SMART NOTE ERROR — '+e.message+'. Human input was not falsely represented as completed intelligence.',false));
  }
  document.addEventListener('click',function(e){
    const b=e.target.closest('#saveNote');
    if(!b)return;
    e.preventDefault();e.stopImmediatePropagation();capture();
  },true);
  boot();
})();
