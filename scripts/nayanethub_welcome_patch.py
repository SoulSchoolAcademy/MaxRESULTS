from pathlib import Path

path = Path('NAYANETHUB.html')
source = path.read_text(encoding='utf-8')

if 'id="nh-greeting-script"' in source:
    raise SystemExit('Welcome already present; refusing duplicate insertion')

css = '''<style id="nh-greeting-style">
#nh-welcome{margin:18px 0 18px;padding:22px 24px;border:1px solid #d86cff55;border-radius:20px;background:linear-gradient(135deg,#181321,#0b0a0f 65%,#08080b);box-shadow:inset 0 1px #fff5,0 20px 45px #000a;position:relative;overflow:hidden}
#nh-welcome:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 85% 25%,#d86cff16,transparent 42%);pointer-events:none}
#nh-greeting{position:relative;margin:0;color:#fff;font-size:clamp(25px,3vw,38px);line-height:1.05;letter-spacing:-.045em}
#nh-welcome-meta{position:relative;display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.nh-welcome-chip{display:inline-flex;align-items:center;min-height:30px;padding:0 10px;border:1px solid #ffffff20;border-radius:999px;background:#08080c;color:#cfc8d6;font-size:8px;font-weight:950;letter-spacing:.08em}
@media(max-width:900px){#nh-welcome{margin:14px 0;padding:19px 18px}.nh-welcome-chip{font-size:7px}}
</style>'''

html = '''<section id="nh-welcome" aria-label="Personalized welcome">
  <h1 id="nh-greeting">Good morning, Shawn.</h1>
  <div id="nh-welcome-meta" aria-live="polite">
    <span class="nh-welcome-chip">TIME · <span id="nh-current-time"></span></span>
    <span class="nh-welcome-chip">DATE · <span id="nh-current-date"></span></span>
    <span class="nh-welcome-chip">COUNTRY · <span id="nh-current-country"></span></span>
  </div>
</section>'''

js = '''<script id="nh-greeting-script">
(function(){
  function countryFromTimezone(tz){
    var map={
      "America/Vancouver":"Canada","America/Edmonton":"Canada","America/Winnipeg":"Canada","America/Toronto":"Canada","America/Halifax":"Canada","America/St_Johns":"Canada","America/Regina":"Canada","America/Moncton":"Canada","America/Whitehorse":"Canada","America/Dawson":"Canada",
      "America/Los_Angeles":"United States","America/Denver":"United States","America/Phoenix":"United States","America/Chicago":"United States","America/New_York":"United States","America/Anchorage":"United States","Pacific/Honolulu":"United States",
      "Europe/London":"United Kingdom","Europe/Dublin":"Ireland","Europe/Paris":"France","Europe/Berlin":"Germany","Europe/Rome":"Italy","Europe/Madrid":"Spain","Europe/Amsterdam":"Netherlands","Europe/Brussels":"Belgium","Europe/Zurich":"Switzerland","Europe/Stockholm":"Sweden","Europe/Oslo":"Norway","Europe/Copenhagen":"Denmark","Europe/Helsinki":"Finland",
      "Asia/Tokyo":"Japan","Asia/Seoul":"South Korea","Asia/Shanghai":"China","Asia/Singapore":"Singapore","Asia/Kolkata":"India","Asia/Dubai":"United Arab Emirates","Australia/Sydney":"Australia","Australia/Melbourne":"Australia","Pacific/Auckland":"New Zealand"
    };
    return map[tz]||((tz||"").split("/")[0]==="America"?"United States":"Local");
  }
  function updateIdentity(){
    var d=new Date(),h=d.getHours();
    var greeting=h<12?"Good morning, Shawn.":h<17?"Good afternoon, Shawn.":"Good evening, Shawn.";
    var time=d.toLocaleTimeString([], {hour:"numeric",minute:"2-digit"});
    var date=d.toLocaleDateString([], {weekday:"long",year:"numeric",month:"long",day:"numeric"});
    var tz=Intl.DateTimeFormat().resolvedOptions().timeZone||"";
    var country=countryFromTimezone(tz);
    var g=document.getElementById("nh-greeting"),t=document.getElementById("nh-current-time"),dt=document.getElementById("nh-current-date"),c=document.getElementById("nh-current-country");
    if(g)g.textContent=greeting;if(t)t.textContent=time;if(dt)dt.textContent=date;if(c)c.textContent=country;
  }
  window.updateIdentity=updateIdentity;
  updateIdentity();
  setInterval(updateIdentity,1000);
})();
</script>'''

if '</head>' not in source or '<main class="main">' not in source or '</body>' not in source:
    raise SystemExit('Canonical anchors missing; refusing mutation')

source = source.replace('</head>', css + '</head>', 1)
source = source.replace('<main class="main">', '<main class="main">' + html, 1)
source = source.replace('</body>', js + '</body>', 1)
path.write_text(source, encoding='utf-8')
print('Surgical personalized welcome inserted into current NAYANETHUB.html:', len(source), 'bytes')
