#!/usr/bin/env bash
set -euo pipefail
# Esempio PostToolUse su Write/Edit: formatta senza rompere la sessione.
if command -v mvn >/dev/null 2>&1 && [ -f pom.xml ]; then
  mvn -q -DskipTests spotless:apply || true
fi
if command -v npm >/dev/null 2>&1 && [ -f package.json ]; then
  npm run format --if-present || true
fi
