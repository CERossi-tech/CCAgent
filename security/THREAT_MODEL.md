# Threat Model per sviluppo agentico

## Asset
- codice sorgente
- segreti
- credenziali Git/MCP
- dati cliente
- pipeline CI/CD

## Attaccanti
- file malevoli nel repository
- dipendenza compromessa
- server MCP non affidabile
- prompt injection in issue/README/log
- errore umano tramite approval fatigue

## Contromisure
- read-only di default
- allowlist tool
- denylist file segreti
- devcontainer
- audit log JSONL
- review manuale per push/release
- MCP gatekeeping
