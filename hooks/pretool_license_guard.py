#!/usr/bin/env python3
import json, sys, re
p=json.load(sys.stdin)
s=str(p.get('tool_input') or {})
if re.search(r'(copy|paste|scarica|download).*licensed|proprietary', s, re.I):
    print('WARNING: verificare licenza prima di includere codice esterno.', file=sys.stderr)
sys.exit(0)
