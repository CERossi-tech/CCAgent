#!/usr/bin/env python3
import json, sys, re
p=json.load(sys.stdin)
s=str(p.get('tool_input') or {})
if re.search(r'\.(png|jpg|jpeg|gif|pdf|zip|jar|class|exe|dll)\b', s, re.I):
    print('BLOCKED: modifica binari non consentita dal hook demo.', file=sys.stderr)
    sys.exit(2)
sys.exit(0)
