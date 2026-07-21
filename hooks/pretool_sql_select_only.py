#!/usr/bin/env python3
import json, re, sys
p=json.load(sys.stdin)
q=str(p.get('tool_input') or {})
if re.search(r'\b(insert|update|delete|drop|alter|truncate|merge)\b', q, re.I):
    print('BLOCKED: solo query SELECT nel corso/lab.', file=sys.stderr)
    sys.exit(2)
sys.exit(0)
