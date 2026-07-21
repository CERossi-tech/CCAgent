#!/usr/bin/env bash
set -euo pipefail
branch=$(git branch --show-current 2>/dev/null || echo unknown)
if [ "$branch" = "main" ] || [ "$branch" = "master" ]; then
  echo "BLOCKED: creare un branch lab/ o feature/ prima di modificare." >&2
  exit 2
fi
