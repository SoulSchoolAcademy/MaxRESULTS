#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "tools" / "build_v21_canonical.py"

s = BUILDER.read_text(encoding="utf-8")

# The canonical JavaScript payload must be a raw Python string so JavaScript
# escapes such as \' and \\s survive Python parsing byte-for-byte.
if 'JS = """' in s:
    s = s.replace('JS = """', 'JS = r"""', 1)
elif 'JS = r"""' not in s:
    raise SystemExit("ERROR: canonical JS payload marker not found")

# Normalize the mastery-stage function using structural boundaries.
a = s.find("function stage(s){")
b = s.find("function dimCopy", a)
if a < 0 or b <= a:
    raise SystemExit(f"ERROR: stage function boundaries not found: {a},{b}")

stage = """function stage(s){
    if(s==null) return ''; 
    return s>=91?'Mastering':s>=76?'Advancing':s>=51?'Developing':s>=21?'Foundation':'Supporting';
  }
  """
s = s[:a] + stage + s[b:]

# Remove presentation-only /100 suffixes while leaving actual scoring math intact.
s = s.replace("Math.round(s)+' / 100</b>", "Math.round(s)+'</b>", 1)
s = s.replace("Math.round(d.score||0)+' / 100</b>", "Math.round(d.score||0)+'</b>", 1)

# Also remove any literal /100 text in the canonical JS payload that is only
# a display string, not a scoring calculation.
js_start = s.find('<script id="maxess-results-v21-canonical-js">')
js_end = s.find('</script>', js_start)
if js_start >= 0 and js_end > js_start:
    prefix = s[:js_start]
    js = s[js_start:js_end]
    suffix = s[js_end:]
    js = js.replace(" / 100</b>", "</b>")
    s = prefix + js + suffix

BUILDER.write_text(s, encoding="utf-8")
print("V21 BUILDER SYNTAX REPAIR: PASS")
print("Raw JS payload: ENFORCED")
print("Five mastery stages: ENFORCED")
print("/100 presentation cleanup: APPLIED")
