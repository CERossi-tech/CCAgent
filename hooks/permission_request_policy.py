#!/usr/bin/env python3
"""Esempio: classifica una richiesta di permission prima di approvare manualmente."""
import json, sys, re
p=json.load(sys.stdin)
cmd=str(p)
risk='low'
if re.search(r'(curl|wget|Invoke-WebRequest|ssh|scp)', cmd, re.I): risk='network'
if re.search(r'(rm|del|rmdir|git push|chmod|chown)', cmd, re.I): risk='destructive'
print(f"Permission risk: {risk}")
sys.exit(0)
