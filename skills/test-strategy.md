# Skill: Test Strategy

## Scopo
Decidere COSA testare e COME, prima di scrivere test: pochi test significativi battono molti test decorativi.

## Quando usarla
- Feature nuova senza copertura.
- Prima di un refactoring (baseline / golden master).
- Review di una PR che aggiunge test.

## Procedura
1. **Identifica i comportamenti**, non le funzioni: cosa promette questo codice all'esterno?
2. **Matrice dei casi** per ogni comportamento:
   - Happy path (1 caso rappresentativo, non 10 varianti).
   - Limiti: vuoto, null, zero, massimo, unicode, duplicato.
   - Errori attesi: input invalido, dipendenza che fallisce, timeout.
   - Concorrenza/idempotenza dove rilevante.
3. **Scegli il livello**: unit (logica pura) / integration (confini reali: DB, HTTP) / e2e (solo flussi critici). Regola: il livello più basso che dà confidenza.
4. **Legacy senza test**: golden master — registra output attuale su input rappresentativi; quello è il contratto durante il refactoring.
5. **Definisci l'oracolo**: ogni test sa dire perché fallisce.

## Qualità di un test
- Nome = comportamento: `rejects_duplicate_email`, non `test2`.
- Arrange-Act-Assert visibili; un concetto per test.
- Nessun test che verifica il mock invece del codice.
- Deterministico: niente sleep, clock e random iniettabili.

## Output atteso
```markdown
## Comportamenti sotto test
## Matrice casi (tabella comportamento × caso × livello)
## Test proposti (nome + intento, poi implementazione)
## Cosa NON testiamo e perché
```

## Anti-pattern
- Coverage come obiettivo invece che come sintomo.
- Snapshot test su tutto: congelano bug e rumore.
