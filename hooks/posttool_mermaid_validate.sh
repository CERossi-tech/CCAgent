#!/usr/bin/env bash
set -euo pipefail
# Placeholder: validazione diagrammi Mermaid se mmdc installato.
command -v mmdc >/dev/null 2>&1 || exit 0
find docs -name '*.md' -print0 | xargs -0 grep -n "```mermaid" || true
