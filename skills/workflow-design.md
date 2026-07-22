# Skill: Workflow Design

## Scopo
Metodo per progettare un workflow agentico: catena di ruoli, permessi, stop condition, evidenze.

## Quando usarla
- Un'attività ripetitiva del team va trasformata in workflow.
- Un workflow esistente produce risultati incoerenti.

## Procedura di design
1. **Obiettivo e done**: qual è l'output finale e come si verifica che è "fatto"? Se non è verificabile, ridefinisci.
2. **Decomposizione in ruoli**: quali competenze servono in sequenza? Un ruolo = un agente = un output.
3. **Contratti tra ruoli**: l'output di ogni agente è l'input del successivo — definisci il formato (sezioni markdown, tabella, file).
4. **Permessi per ruolo**: chi legge, chi scrive, chi esegue. Chi scrive non si autovaluta: incornicia i writer con reader.
5. **Punti deterministici**: dove servono hook (blocco, verifica, audit) invece di fiducia nel modello?
6. **Stop condition**: quando il workflow si ferma da solo (successo, fallimento, budget turni/diff superato)?
7. **Handoff umano**: cosa riceve la persona alla fine, e cosa deve decidere?

## Template del documento workflow
```markdown
# Workflow: <nome>
## Trigger (quando parte)
## Catena agentica (ruolo → ruolo, con contratto tra i passaggi)
## Input richiesti
## Passi (numerati, ognuno con owner-agente e output)
## Guardrail (hook e permessi coinvolti)
## Stop condition
## Output e handoff
## Metriche (come misuri che funziona)
```

## Criteri di qualità
- Ogni passo ha un output verificabile.
- Il fallimento di un passo ha un comportamento definito (retry, stop, escalation).
- Il diff totale prodotto resta comprensibile in < 10 minuti.

## Anti-pattern
- Un mega-agente che fa tutto il workflow: non è un workflow, è una speranza.
- Workflow senza stop condition: gira finché non fa danni.
- Passi il cui output è "l'agente ha detto ok" senza artefatto controllabile.
