# Workflow: Incident Response

## Catena agentica
`incident-analyst -> observability-agent -> security-auditor -> documentation-writer`

## Input
- Ticket o obiettivo tecnico.
- Repository pulito.
- Branch dedicato.

## Passi
1. Definisci scope e rischi.
2. Seleziona agenti minimi.
3. Esegui analisi read-only.
4. Applica modifiche piccole.
5. Esegui test/controlli.
6. Produci evidenze.
7. Prepara handoff umano.

## Stop condition
- Test principali passano oppure sono documentati i motivi del mancato run.
- Nessuna modifica a file segreti.
- Diff comprensibile in meno di 10 minuti.

## Output
- Sintesi per PR.
- Checklist completata.
- Rischi residui.
