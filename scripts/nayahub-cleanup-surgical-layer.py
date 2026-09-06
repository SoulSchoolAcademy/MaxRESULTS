from pathlib import Path
p=Path('NAYAHUB.html')
s=p.read_text(encoding='utf-8')
start='<script id="NAYANET-V7-REMAINING-TODO-COMPLETION">'
if start not in s: raise SystemExit(0)
a=s.index(start); b=s.index('</script>',a)+len('</script>')
s=s[:a]+s[b:]
p.write_text(s,encoding='utf-8')
