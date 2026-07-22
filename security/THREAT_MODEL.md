# Threat Model per sviluppo agentico

## Asset da proteggere
| Asset | Impatto se compromesso |
|---|---|
| Codice sorgente | integrità del prodotto, IP |
| Segreti (API key, chiavi SSH, certificati) | accesso a sistemi, il danno più rapido |
| Credenziali Git/MCP | movimento laterale, supply chain |
| Dati cliente | compliance, fiducia, obblighi legali |
| Pipeline CI/CD | esecuzione arbitraria a valle |
| Config `.claude/` (agenti, hook, policy) | disattivazione delle difese stesse |

## Attori e vettori
| Vettore | Come agisce | Difesa primaria |
|---|---|---|
| Prompt injection nel repo (README, issue, log, fixture) | istruzioni nei contenuti letti dall'agente | contenuto repo = dato non fidato; agenti read-only; hunter |
| Tool poisoning (script, package script, hook alterati) | l'agente esegue in buona fede codice malevolo | prima leggere, poi eseguire; review degli script; hook |
| Server MCP malevolo o vulnerabile | tool diversi dal dichiarato; traversal/injection nei parametri | gatekeeping, allowlist per tool, provenienza |
| Dipendenza compromessa (supply chain) | codice ostile via upgrade | dependency-auditor, lockfile, changelog letti prima |
| Esfiltrazione segreti | lettura `.env`/chiavi → riemersione in output/log | secret-guard PreToolUse, log senza payload, secret manager |
| Approval fatigue | l'umano approva tutto per stanchezza | permission routing, allowlist mirate, meno prompt migliori |
| Agente fuori scope (errore, non malizia) | modifiche eccessive, comandi distruttivi | least privilege, diff budget, branch guard, sandbox |

## Contromisure a strati
1. **Identità e permessi**: read-only by default; allowlist esplicita; denylist distruttiva; conferma umana per push/release/network.
2. **Contenimento**: branch dedicati, devcontainer, worktree per agenti paralleli, dati demo, CI come gate finale.
3. **Determinismo**: hook PreToolUse (blocco), PostToolUse (verifica), Stop (test), PostCompact (reiniezione policy).
4. **Osservabilità**: audit JSONL per tool use, diff stat dopo ogni Edit, report di sessione, collegamento a ticket/PR.
5. **Processo**: chi scrive non si autovaluta; review umana finale; metriche (block/allow, falsi positivi, incidenti secret = 0).

## Assunzioni e limiti
- Il modello può sempre essere manipolato: la difesa non è "prompt più fermi" ma rendere la manipolazione inutile (tool e hook).
- Gli hook girano in locale: la loro integrità è essa stessa un asset (review dei cambi a `.claude/`).
- Questo threat model va rivisto: a ogni nuovo server MCP, a ogni incidente, e comunque ogni trimestre.
