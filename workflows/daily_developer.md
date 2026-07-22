# Workflow: Daily Developer (Morning Report)

## Trigger
Avvio manuale a inizio giornata o SessionStart schedulato. Interamente read-only.

## Catena agentica
`observability-agent -> git-guardian (read-only) -> jira-assistant (opzionale) -> documentation-writer (formatter)`

## Input
- Repository locale aggiornato (`git fetch` eseguito).
- Facoltativo: accesso read-only a CI e ticketing.

## Passi
1. `git log --since=yesterday` su tutti i branch: cosa è cambiato e chi ha toccato cosa.
2. Branch aperti e loro distanza da main (ahead/behind).
3. Grep TODO/FIXME introdotti nelle ultime 24h (diff-based, non totale).
4. PR aperte in attesa di review propria o bloccate.
5. Stato ultimi run CI / test falliti.
6. Sintesi: 3 priorità e **una** prossima azione consigliata con motivo.

## Guardrail
- Agenti con soli Read/Grep/Glob + git read-only (`log`, `diff`, `branch`).
- `audit_log.py` attivo; nessuna scrittura di file oltre al report.

## Stop condition
- Report prodotto in ≤ 5 minuti di run; se una fonte non è raggiungibile, sezione marcata "non disponibile" senza retry infiniti.

## Output e handoff
- `reports/morning-YYYY-MM-DD.md`: sezioni Cambiamenti / In volo / Debito nuovo / Blocci / Prossima azione.
- Nessuna decisione richiesta: è un artefatto di orientamento.
