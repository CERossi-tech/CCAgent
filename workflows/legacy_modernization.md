# Workflow: Legacy Modernization

## Trigger
Modulo legacy da modernizzare: senza test, con dipendenze obsolete o pattern deprecati.

## Catena agentica
`codebase-cartographer -> legacy-modernizer (lead) -> test-generator (golden master) -> refactoring-coach -> java-reviewer -> documentation-writer`

## Input
- Perimetro del modulo legacy (path espliciti).
- Obiettivo di modernizzazione (es. "estrarre servizio", "aggiornare a Spring Boot 3", "rendere testabile").

## Passi
1. **Cartographer**: mappa del modulo — entry point, dipendenze in/out, accoppiamenti, zone morte.
2. **Test-generator** (skill test-strategy, sezione golden master): registra il comportamento attuale su input rappresentativi. Questo è il contratto: nessun refactoring prima che esista.
3. **Legacy-modernizer**: piano a passi PICCOLI, ognuno reversibile, ordinati per rischio crescente; ogni passo dichiara il proprio test di verifica.
4. Ciclo per ogni passo: `refactoring-coach` guida la modifica → golden master + test verdi → diff summary → commit atomico. Rosso? Revert del passo, non "fix in avanti".
5. **Java-reviewer**: review di ogni batch (max 400 righe).
6. **Documentation-writer**: ADR per le decisioni strutturali (skill adr-writing); mappa aggiornata a fine ciclo.

## Guardrail
- Golden master obbligatorio come gate d'ingresso: hook Stop verifica presenza ed esito.
- Diff budget per passo; branch dedicato; worktree separato se in parallelo ad altro sviluppo.

## Stop condition
- Obiettivo dichiarato raggiunto con golden master sempre verde, OPPURE
- Budget passi esaurito: si consolida quanto fatto e si ripianifica — mai lasciare il modulo a metà in stato peggiore.

## Output e handoff
- Serie di commit atomici, ADR delle scelte, mappa before/after, rischi residui.
