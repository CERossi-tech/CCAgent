#!/usr/bin/env bash
set -euo pipefail
# Stop hook: suggerisce verifica finale, ma non blocca se tool assenti.
[ -f pom.xml ] && mvn -q test || true
[ -f package.json ] && npm test -- --runInBand || true
