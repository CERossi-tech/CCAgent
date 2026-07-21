#!/usr/bin/env python3
"""PreToolUse hook: blocca comandi bash pericolosi.
Input atteso: JSON Claude Code hook su stdin.
Exit 0 = allow, exit 2 = block.
"""
import json, re, sys
payload=json.load(sys.stdin)
cmd=(payload.get('tool_input') or {}).get('command','')
blocked=[r'\brm\s+-rf\s+/', r'\bdd\s+if=', r'\bmkfs\.', r'\bchmod\s+-R\s+777\b', r'\bgit\s+push\s+.*\bmain\b']
for pat in blocked:
    if re.search(pat, cmd, re.I):
        print(f"BLOCKED by pretool policy: {pat}", file=sys.stderr)
        sys.exit(2)
sys.exit(0)
