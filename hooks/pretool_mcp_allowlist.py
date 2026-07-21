#!/usr/bin/env python3
import json, sys, re
p=json.load(sys.stdin)
tool=p.get('tool_name','')
allowed_prefixes=['mcp__filesystem__read','mcp__git__status','mcp__jira__get']
if tool.startswith('mcp__') and not any(tool.startswith(a) for a in allowed_prefixes):
    print(f'MCP tool non in allowlist: {tool}', file=sys.stderr)
    sys.exit(2)
sys.exit(0)
