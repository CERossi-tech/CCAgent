#!/usr/bin/env python3
import json, sys, datetime, pathlib
p=json.load(sys.stdin)
log=pathlib.Path('.claude/audit.jsonl')
log.parent.mkdir(exist_ok=True)
record={'ts': datetime.datetime.utcnow().isoformat()+'Z', 'event': p.get('hook_event_name'), 'tool': p.get('tool_name'), 'input': p.get('tool_input')}
with log.open('a', encoding='utf-8') as f: f.write(json.dumps(record, ensure_ascii=False)+'\n')
sys.exit(0)
