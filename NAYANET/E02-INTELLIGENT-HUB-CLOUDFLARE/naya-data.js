"use strict";
(() => {
  const SUPABASE_URL = "https://dahisasgpfvziswqvmvm.supabase.co";
  const SUPABASE_KEY = "sb_publishable_oQFKOYFuJ9bT-E9QkJUb4g_lAUyInue";
  const LOCAL_KEY = "nayanet:intelligence:v1";
  let client = null;
  let memberId = null;
  let ready = false;

  function localState(){ try{return JSON.parse(localStorage.getItem(LOCAL_KEY)||"{}")}catch{return{}} }
  function remember(){ return localStorage.getItem("nayanetName") || localState().name || ""; }
  function slug(name){return (name||"friend").toLowerCase().replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"")||"friend"}
  function notify(){ window.dispatchEvent(new CustomEvent("naya:data-ready",{detail:{memberId,ready}})); }

  async function boot(){
    try{
      const mod = await import("https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/+esm");
      client = mod.createClient(SUPABASE_URL,SUPABASE_KEY,{auth:{persistSession:true,autoRefreshToken:true,detectSessionInUrl:false}});
      let {data:{session}} = await client.auth.getSession();
      if(!session){ const r=await client.auth.signInAnonymously(); session=r.data?.session||null; if(r.error) throw r.error; }
      if(!session?.user?.id) throw new Error("No authenticated session");
      memberId=session.user.id;
      const name=remember();
      if(name){
        await client.from("members").upsert({id:memberId,display_name:name},{onConflict:"id"});
        await client.from("nayanet_profiles").upsert({member_id:memberId,smart_id:`naya/${slug(name)}`,public_alias:name},{onConflict:"member_id"});
      }
      ready=true;
      await hydrate();
      notify();
    }catch(error){
      ready=false;
      console.warn("NayaNET persistence bridge unavailable; local continuity remains active.",error);
      notify();
    }
  }

  async function hydrate(){
    if(!client||!memberId)return;
    const [notes,challenge,spaces,profile] = await Promise.all([
      client.from("nayanet_notes").select("note_type,human_note,created_at").eq("member_id",memberId).order("created_at",{ascending:false}).limit(100),
      client.from("nayanet_challenges").select("goal,current_day,completed_days").eq("member_id",memberId).maybeSingle(),
      client.from("nayanet_spaces").select("name,purpose,created_at").eq("owner_member_id",memberId).order("created_at",{ascending:false}).limit(50),
      client.from("nayanet_profiles").select("smart_id,public_alias").eq("member_id",memberId).maybeSingle()
    ]);
    const s=localState();
    if(notes.data?.length) s.notes=notes.data.map(n=>({type:n.note_type,text:n.human_note,at:new Date(n.created_at).getTime()}));
    if(challenge.data) s.challenge={day:challenge.data.current_day,goal:challenge.data.goal,done:challenge.data.completed_days||[]};
    if(spaces.data?.length) s.spaces=spaces.data.map(x=>({name:x.name,purpose:x.purpose,at:new Date(x.created_at).getTime()}));
    if(profile.data?.public_alias){ s.name=profile.data.public_alias; localStorage.setItem("nayanetName",profile.data.public_alias); }
    localStorage.setItem(LOCAL_KEY,JSON.stringify({...s,lastSeen:Date.now()}));
  }

  async function sync(){
    if(!client||!memberId)return;
    const s=localState();
    if(s.notes?.length){
      const latest=s.notes[s.notes.length-1];
      await client.from("nayanet_notes").upsert({member_id:memberId,note_type:latest.type,human_note:latest.text,created_at:new Date(latest.at||Date.now()).toISOString()},{onConflict:"id"});
    }
    if(s.challenge){ await client.from("nayanet_challenges").upsert({member_id:memberId,goal:s.challenge.goal||"",current_day:s.challenge.day||1,completed_days:s.challenge.done||[]},{onConflict:"member_id"}); }
    if(s.spaces?.length){
      const latest=s.spaces[s.spaces.length-1];
      await client.from("nayanet_spaces").insert({owner_member_id:memberId,name:latest.name,purpose:latest.purpose});
    }
    if(s.name){ await client.from("members").upsert({id:memberId,display_name:s.name},{onConflict:"id"}); await client.from("nayanet_profiles").upsert({member_id:memberId,smart_id:`naya/${slug(s.name)}`,public_alias:s.name},{onConflict:"member_id"}); }
  }

  window.NayaData={get ready(){return ready},get memberId(){return memberId},sync,hydrate};
  const originalSet=Storage.prototype.setItem;
  Storage.prototype.setItem=function(key,value){
    originalSet.call(this,key,value);
    if(key===LOCAL_KEY && ready) queueMicrotask(()=>sync());
  };
  window.addEventListener("naya:data-save",()=>sync());
  boot();
})();
