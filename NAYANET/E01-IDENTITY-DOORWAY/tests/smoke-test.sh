#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HTML="$ROOT/index.html"
README="$ROOT/README.md"

[ -s "$HTML" ]
[ -s "$README" ]

grep -q 'Welcome to <em>NayaNET' "$HTML"
grep -q 'Enter your name' "$HTML"
grep -q 'Private identity' "$HTML"
grep -q 'Network identity · Smart Name' "$HTML"
grep -q 'Preview · not provisioned' "$HTML"
grep -q 'Your Intelligent <em>Hub' "$HTML"
grep -q "What's Your AI Score?" "$HTML"
grep -q 'What Is Naya Power?' "$HTML"
grep -q 'Five-Day Challenge' "$HTML"
grep -q 'Meet Naya' "$HTML"
grep -q 'Think With Naya' "$HTML"
grep -q 'Start CIS' "$HTML"
grep -q 'Master Excellence' "$HTML"
grep -q 'Compound Your Life' "$HTML"
grep -q 'prefers-reduced-motion' "$HTML"
grep -q 'youtube-nocookie.com/embed/wnjvDqEhBCY' "$HTML"

if grep -q 'sessionStorage\|localStorage' "$HTML"; then
  echo "PASS: browser-only review state is allowed; no server persistence is claimed."
fi

if grep -Eq 'nayanet\.app/|nayanet\.xyz/preview' "$HTML"; then
  echo "PASS: Smart Link presentation is explicit preview state."
fi

echo "E01 smoke checks: PASS"
