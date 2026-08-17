#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / 'tools' / 'build_v21_canonical.py'
text = PATH.read_text(encoding='utf-8')

replacements = [
    (
        "function stage(s){ if(s==null) return ''; return s>=91?'Mastering':s>=76?'Advancing':s>=51?'Developing':'Foundation'; }",
        "function stage(s){ if(s==null) return ''; return s>=91?'Mastering':s>=76?'Advancing':s>=51?'Developing':s>=26?'Foundation':'Supporting'; }",
        'five-stage mastery model',
    ),
    (
        "'<div class=\"v21-shell\">'+",
        "'<div class=\"v21-shell\" data-results-data-source=\"window.MAXESS_RESULT\">'+",
        'canonical result-source marker',
    ),
    (
        "<b>'+Math.round(s)+' / 100</b>",
        "<b>'+Math.round(s)+'</b>",
        'report score presentation',
    ),
    (
        "'<b>'+escapeHtml(d.name)+' · '+Math.round(d.score||0)+' / 100</b><p>'",
        "'<b>'+escapeHtml(d.name)+' · '+Math.round(d.score||0)+'</b><p>'",
        'dimension detail score presentation',
    ),
]

for old, new, label in replacements:
    if old not in text:
        raise SystemExit(f'ERROR: expected {label} literal not found')
    text = text.replace(old, new, 1)

PATH.write_text(text, encoding='utf-8')
print('FINAL V21 CONTRACT PATCH APPLIED')
print('Five mastery stages: Supporting / Foundation / Developing / Advancing / Mastering')
print('Canonical data-source marker: PRESENT')
print('Score presentation: /100 suffix removed')
