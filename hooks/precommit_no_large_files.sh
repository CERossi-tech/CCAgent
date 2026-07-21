#!/usr/bin/env bash
set -euo pipefail
limit=$((5*1024*1024))
while IFS= read -r f; do
  [ -f "$f" ] || continue
  size=$(wc -c < "$f")
  if [ "$size" -gt "$limit" ]; then
    echo "File troppo grande: $f ($size bytes)" >&2
    exit 1
  fi
done < <(git diff --cached --name-only)
