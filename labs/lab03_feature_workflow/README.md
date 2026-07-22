# Lab 3 — Feature workflow completo

## Obiettivo
Portare una piccola feature (validazione input su `UserService`) attraverso la catena completa: architect → developer → tester → gate → docs → git.

## Durata
35–45 minuti.

## Prerequisiti
- Lab 1 e 2 completati (agenti e hook in `.claude/`).
- Branch `lab/lab03_feature_workflow`; suite di esempio eseguibile.
- Agenti necessari copiati in `.claude/agents/`: spring-architect, test-generator, java-reviewer, security-auditor, documentation-writer, git-guardian, workflow-orchestrator.

## Passi
1. Leggi `workflows/feature_to_pr.md`: è la mappa di questo lab.
2. Avvia con il prompt:
   ```text
   Lavora come workflow-orchestrator seguendo workflows/feature_to_pr.md.
   Obiettivo: aggiungere validazione dell'input (email valida, nome non vuoto) alla creazione utente
   in examples/springboot/UserService.java. Prima piano e rischi, poi passi piccoli.
   Non toccare file segreti, non fare commit né push.
   ```
3. Approva (o correggi) il piano proposto prima dell'esecuzione.
4. Osserva la delega: l'orchestratore invoca gli agenti giusti senza che tu li nomini? Se no, il problema è nelle description.
5. Al gate: leggi i verdetti di reviewer e security-auditor; se c'è un `fail`, segui l'iterazione.
6. Verifica gli artefatti finali: diff piccolo, test verdi, README aggiornato, PR summary, commit message suggerito.
7. Il commit lo fai TU, manualmente, dopo aver letto il diff.

## Attività bonus
- Introduci di proposito un difetto (es. logging dell'email in chiaro) e verifica che il gate lo intercetti.
- Misura: quanto tempo ha richiesto il workflow vs quanto avresti impiegato a mano?

## Criteri di successo
- Catena completata con delega corretta per description.
- Diff < 200 righe, test verdi, doc aggiornata.
- Gate esitato con verdetti espliciti; commit finale eseguito da te.
