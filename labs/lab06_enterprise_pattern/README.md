# Lab 6 — Enterprise pattern (capstone)

## Obiettivo
Progettare in forma agentica un workflow REALE del tuo team, con agenti, hook, policy e metriche di adozione.

## Durata
30–40 minuti (in aula) oppure come esercizio post-corso.

## Prerequisiti
- Tutti i lab precedenti completati.
- Un'attività ripetitiva vera del tuo lavoro scelta come caso (review, release, triage, onboarding, report...).

## Passi
1. Leggi `skills/workflow-design.md`: userai il suo template come deliverable.
2. Definisci obiettivo e "done" verificabile del tuo workflow (se non è verificabile, ridefiniscilo).
3. Decomponi in ruoli: quali agenti del kit riusi? Quale manca e va scritto? (Scrivine al massimo UNO nuovo, minimale.)
4. Definisci i contratti tra i passi: cosa passa da un agente all'altro, in che formato.
5. Assegna i permessi per ruolo e individua i punti deterministici: quali hook del kit servono? (audit sempre; poi guard specifici.)
6. Scrivi stop condition e handoff umano: dove si ferma il sistema e cosa decide la persona.
7. Definisci 3 metriche di adozione (vedi `docs/COURSE_BOOK.md` e slide 43): almeno una di valore e una di sicurezza, con baseline da misurare PRIMA.
8. Compila il documento con il template della skill e salvalo in `workflows/` del tuo fork.

## Retrospettiva di gruppo
Presenta il tuo design in 3 minuti: obiettivo, catena, il guardrail più importante, la metrica che convincerà il tuo team. Le domande degli altri team sono parte del deliverable.

## Criteri di successo
- Documento workflow completo secondo il template (trigger, catena, guardrail, stop, metriche).
- Ogni passo ha output verificabile; chi scrive non si autovaluta.
- Piano di adozione incrementale: prima settimana read-only.
