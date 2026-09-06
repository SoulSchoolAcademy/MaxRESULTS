/* NAYANETHUB-FINAL-EXECUTION-V2 */
/* RELEASE TRIGGER: publish current NAYANETHUB to index.html */
/* Purpose: add only the personal welcome line at the very top. No briefing, boards, feed, or new dashboard UI. */
(function(){
  'use strict';
  const NAME='nayanet_smart_name';
  const esc=s=>String(s??'').replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]));
  const getName=()=>{
    try{
      const p=new URLSearchParams(location.search).get('name');
      if(p && p.trim()){localStorage.setItem(NAME,p.trim());return p.trim();}
      return localStorage.getItem(NAME)||'';
    }catch(e){return '';}
  };
  const getCountry=()=>{
    try{
      const tz=Intl.DateTimeFormat().resolvedOptions().timeZone||'';
      const map={
        'America/St_Johns':'Canada','America/Halifax':'Canada','America/Glace_Bay':'Canada','America/Moncton':'Canada','America/Goose_Bay':'Canada','America/Toronto':'Canada','America/Nipigon':'Canada','America/Thunder_Bay':'Canada','America/Iqaluit':'Canada','America/Winnipeg':'Canada','America/Resolute':'Canada','America/Rankin_Inlet':'Canada','America/Regina':'Canada','America/Swift_Current':'Canada','America/Edmonton':'Canada','America/Cambridge_Bay':'Canada','America/Inuvik':'Canada','America/Dawson':'Canada','America/Creston':'Canada','America/Whitehorse':'Canada','America/Dawson_Creek':'Canada','America/Vancouver':'Canada',
        'America/New_York':'United States','America/Detroit':'United States','America/Chicago':'United States','America/Denver':'United States','America/Phoenix':'United States','America/Los_Angeles':'United States','America/Anchorage':'United States','Pacific/Honolulu':'United States',
        'Europe/London':'United Kingdom','Europe/Dublin':'Ireland','Europe/Paris':'France','Europe/Berlin':'Germany','Europe/Madrid':'Spain','Europe/Rome':'Italy','Europe/Amsterdam':'Netherlands','Europe/Brussels':'Belgium','Europe/Zurich':'Switzerland','Europe/Vienna':'Austria','Europe/Stockholm':'Sweden','Europe/Oslo':'Norway','Europe/Copenhagen':'Denmark','Europe/Helsinki':'Finland','Europe/Warsaw':'Poland','Europe/Lisbon':'Portugal',
        'Asia/Tokyo':'Japan','Asia/Seoul':'South Korea','Asia/Shanghai':'China','Asia/Hong_Kong':'Hong Kong','Asia/Singapore':'Singapore','Asia/Kolkata':'India','Asia/Dubai':'United Arab Emirates','Asia/Jerusalem':'Israel','Asia/Bangkok':'Thailand',
        'Australia/Sydney':'Australia','Australia/Melbourne':'Australia','Australia/Brisbane':'Australia','Australia/Perth':'Australia','Pacific/Auckland':'New Zealand'
      };
      return map[tz]||'';
    }catch(e){return '';}
  };
  function style(){
    if(document.getElementById('nayanethub-personal-style'))return;
    const s=document.createElement('style');s.id='nayanethub-personal-style';
    s.textContent=`#nayanethub-personal-welcome{display:flex;align-items:center;justify-content:space-between;gap:20px;margin:0 0 18px;padding:15px 18px;border:1px solid #d86cff38;border-radius:16px;background:linear-gradient(145deg,#14101b,#09090d);box-shadow:inset 0 1px #fff3,0 14px 30px #0008}#nayanethub-personal-welcome .greeting{font-size:16px;font-weight:900;letter-spacing:-.02em}#nayanethub-personal-welcome .details{margin-top:4px;color:#aaa4b0;font-size:9px;font-weight:700;letter-spacing:.04em}@media(max-width:700px){#nayanethub-personal-welcome{display:block;padding:14px 15px}#nayanethub-personal-welcome .greeting{font-size:15px}}`;
    document.head.appendChild(s);
  }
  function render(){
    style();
    const name=esc(getName());
    const now=new Date();
    const h=now.getHours();
    const greeting=h<12?'Good morning':h<17?'Good afternoon':'Good evening';
    const time=now.toLocaleTimeString([], {hour:'numeric',minute:'2-digit'});
    const date=now.toLocaleDateString([], {weekday:'long',year:'numeric',month:'long',day:'numeric'});
    const country=esc(getCountry());
    let el=document.getElementById('nayanethub-personal-welcome');
    if(!el){el=document.createElement('section');el.id='nayanethub-personal-welcome';const root=document.querySelector('#page-home')||document.querySelector('main')||document.body;root.prepend(el);}
    el.innerHTML=`<div><div class="greeting">${greeting}${name?', '+name:''}.</div><div class="details">${time} · ${date}${country?' · '+country:''}</div></div>`;
  }
  document.addEventListener('DOMContentLoaded',render);
  [250,1000,2000].forEach(ms=>setTimeout(render,ms));
})();