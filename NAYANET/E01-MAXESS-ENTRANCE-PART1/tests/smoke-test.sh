#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
test -s "$ROOT/index.html"
grep -q "Welcome to NayaNET" "$ROOT/index.html"
grep -q "Enter your name" "$ROOT/index.html"
grep -q "Begin MAXESS" "$ROOT/index.html"
grep -q "Preview only" "$ROOT/index.html"
! grep -q "Living Sun" "$ROOT/index.html"
! grep -q "nayanet.xyz" "$ROOT/index.html"
echo "PASS: static artifact smoke checks"
