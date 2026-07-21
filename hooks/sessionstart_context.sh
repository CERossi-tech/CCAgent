#!/usr/bin/env bash
set -euo pipefail
cat <<EOF
# Project context auto-loaded
Branch: $(git branch --show-current 2>/dev/null || echo n/a)
Last commits:
$(git log --oneline -5 2>/dev/null || true)
EOF
