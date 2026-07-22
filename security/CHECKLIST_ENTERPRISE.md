# Checklist Enterprise Claude Code

## Setup e configurazione
- [ ] Repository senza segreti reali (scan iniziale eseguito).
- [ ] `.claude/settings.json` versionato solo per regole condivise di team.
- [ ] `.claude/settings.local.json` in `.gitignore`.
- [ ] Ogni regola in settings ha un commento: cosa protegge, chi l'ha decisa.

## Agenti
- [ ] Ogni subagent ha tool minimi e `disallowedTools` espliciti.
- [ ] Description scritte come "quando usarlo" (routing verificato nei lab).
- [ ] `maxTurns` impostato su ogni agente; nessun agente "tutti i tool sempre".
- [ ] Chi scrive non si autovaluta: writer incorniciati da reviewer read-only.

## Hooks
- [ ] Hook testati in sandbox con input simulato prima della registrazione.
- [ ] PreToolUse attivi: block-dangerous-bash, secret-guard, branch-guard.
- [ ] Audit log JSONL attivo su ogni tool use; verificato che NON contenga segreti.
- [ ] Hook PostCompact che reinietta le policy critiche.
- [ ] Messaggi stderr degli hook indicano l'alternativa, non solo il divieto.

## MCP
- [ ] Tool MCP autorizzati nominalmente (per tool, non per server).
- [ ] Nessun server MCP di provenienza sconosciuta; preferiti interni e versionati.
- [ ] Risk assessment documentato per ogni server (skill mcp-risk-assessment).
- [ ] Invocazioni MCP loggate; data di rivalutazione fissata.

## Operazioni
- [ ] Push, tag, release e azioni di rete sempre manuali/con conferma.
- [ ] Diff budget definito; diff grandi → split obbligatorio.
- [ ] Branch dedicati per il lavoro agentico; mai su main.
- [ ] CI come gate finale anche per il codice prodotto dagli agenti.

## Governance
- [ ] Audit periodico con `/permissions` e `/hooks` (cadenza fissata).
- [ ] Metriche attive: tempo review, falsi positivi, block/allow ratio, incidenti secret = 0.
- [ ] Processo di promozione dei pattern: da esperimento locale a config di team.
- [ ] Owner della policy identificato; canale per segnalare finding/injection.
