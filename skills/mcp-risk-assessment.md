# Skill: MCP Risk Assessment

## Scopo
Valutare un server MCP prima di autorizzarlo: capacità, superficie d'attacco, permessi minimi.

## Quando usarla
- Onboarding di un nuovo server MCP.
- Audit periodico della configurazione MCP esistente.
- Dopo un aggiornamento di versione del server.

## Procedura
1. **Inventario**: elenca ogni tool esposto dal server (nome, descrizione dichiarata, parametri).
2. **Classificazione capacità** per ogni tool:
   - `READ` — legge dati; rischio: esfiltrazione.
   - `WRITE` — muta stato; rischio: integrità.
   - `EXEC` — esegue comandi/codice; rischio: massimo.
   - `NET` — comunica verso l'esterno; rischio: canale di esfiltrazione.
3. **Provenienza**: server interno versionato / vendor noto / repository pubblico sconosciuto.
4. **Dati raggiungibili**: quali dataset, con che sensibilità (pubblico/interno/confidenziale/segreti).
5. **Vulnerabilità classiche**: path traversal nei parametri file, command injection nei parametri stringa, SSRF nei parametri URL.
6. **Decisione** per ogni tool: `allow` / `allow con conferma` / `deny`.

## Matrice di rischio
| Capacità | Dati pubblici | Dati interni | Dati confidenziali |
|---|---|---|---|
| READ | allow | allow | conferma |
| WRITE | conferma | conferma | deny (default) |
| EXEC / NET | conferma | deny (default) | deny |

## Output atteso
```markdown
## Server: <nome> (<versione>, <provenienza>)
| Tool | Capacità | Dati | Rischi | Decisione | Motivo |
## Allowlist risultante
## Condizioni di revisione (quando rivalutare)
```

## Anti-pattern
- Autorizzare "il server" invece dei singoli tool.
- Fidarsi della descrizione dichiarata senza leggere il codice/contratto del tool.
