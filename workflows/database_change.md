# Workflow: Database Change

## Trigger
Necessità di modifica schema/dati: nuova colonna, indice, migrazione.

## Catena agentica
`spring-architect -> sql-reviewer -> (developer: main session) -> test-generator -> security-auditor -> documentation-writer`

## Input
- Obiettivo della modifica e volumetria attesa della tabella.
- Ambiente: SOLO sviluppo/demo. Mai credenziali di produzione nel contesto.

## Passi
1. **Architect**: valuta impatto — compatibilità all'indietro, downtime, ordine deploy/migrazione (expand-contract se breaking).
2. Scrittura migrazione versionata (Flyway/Liquibase): script `up` + strategia di rollback esplicita.
3. **Sql-reviewer**: controlla la migrazione — lock attesi, indici, tipi, default su tabelle grandi, idempotenza.
4. **Test-generator**: test di migrazione (schema before/after) e test dei repository toccati.
5. Esecuzione su DB locale/demo; verifica con query di controllo SELECT-only.
6. **Security-auditor**: nessun dato sensibile negli script/seed; permessi DB minimi.
7. **Documentation-writer**: aggiorna doc schema/ADR se la modifica è architetturale (skill adr-writing).

## Guardrail
- Hook `pretool_sql_select_only.py` per ogni accesso interattivo al DB: mutazioni solo via migrazione versionata.
- Denylist: `DROP`, `TRUNCATE` fuori da file di migrazione revisionati.

## Stop condition
- Migrazione applicata e rollback testato su DB demo; test verdi.
- Nessuna mutazione eseguita fuori dai file di migrazione.

## Output e handoff
- File migrazione + rollback, esito test, note di deploy (ordine, durata lock stimata).
- Decisione umana: pianificazione dell'applicazione in ambienti superiori.
