# Lab 2 — Hook di sicurezza deterministici

## Obiettivo
Installare un hook PreToolUse che blocca i comandi Bash pericolosi, vederlo scattare, e leggere l'audit trail.

## Durata
25–35 minuti.

## Prerequisiti
- Branch `lab/lab02_security_hooks`, repo pulito, nessun segreto reale.
- Lab in sandbox/devcontainer: gli hook eseguono codice locale.

## Passi
1. Leggi `hooks/pretool_block_dangerous_bash.py` PRIMA di installarlo (regola: prima leggere, poi eseguire — vale anche per i tuoi hook).
2. Copia lo script in `.claude/hooks/` e registralo in `.claude/settings.json` come hook `PreToolUse` con matcher sul tool `Bash`.
3. Registra anche `hooks/audit_log.py` (evento PostToolUse) per il tracciamento.
4. Test manuale dell'hook, senza Claude: passagli su stdin un JSON simulato con un comando `rm -rf /` e verifica `exit code 2` + messaggio su stderr.
5. Avvia Claude Code e chiedi qualcosa che indurrebbe un comando pericoloso, ad esempio:
   ```text
   Pulisci completamente la directory build ricreandola da zero nel modo più veloce possibile.
   ```
6. Osserva: l'hook blocca, l'agente legge lo stderr e riformula il piano con un comando sicuro. Questo dialogo è il punto del lab.
7. Apri `audit.jsonl`: trova l'evento bloccato e quello consentito; verifica che nel log non ci siano dati sensibili.

## Attività bonus
- Aggiungi un pattern alla denylist (es. `git push --force`) e verifica che scatti.
- Migliora il messaggio stderr: da "bloccato" a "bloccato: usa X invece" e osserva come cambia la reazione dell'agente.
- Registra `hooks/pretool_secret_guard.py` e prova a far leggere un finto `.env`.

## Criteri di successo
- Hook installato e testato sia manualmente sia in sessione.
- Exit 2 osservato con messaggio utile; l'agente si è auto-corretto.
- `audit.jsonl` contiene gli eventi, senza segreti.
