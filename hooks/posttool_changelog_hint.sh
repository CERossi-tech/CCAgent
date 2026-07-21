#!/usr/bin/env bash
set -euo pipefail
mkdir -p docs
printf "- %s: modifiche da revisionare\n" "$(date +%F)" >> docs/CHANGELOG_DRAFT.md
