#!/usr/bin/env python3
"""Blocca lettura/scrittura di file che probabilmente contengono segreti."""
import json, re, sys, pathlib
payload=json.load(sys.stdin)
text=str(payload.get('tool_input') or {})
patterns=[r'\.env(\.|$)', r'id_rsa', r'id_ed25519', r'\.pem$', r'\.p12$', r'credentials', r'secrets?\.ya?ml']
if any(re.search(p, text, re.I) for p in patterns):
    print('BLOCKED: file potenzialmente sensibile. Usa secret manager o file demo.', file=sys.stderr)
    sys.exit(2)
sys.exit(0)
