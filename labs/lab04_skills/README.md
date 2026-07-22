# Lab 4 — Skill riusabili: ADR

## Obiettivo
Usare la skill `adr-writing` da un agente (spring-architect) per produrre un ADR reale sulla scelta fatta nel Lab 3.

## Durata
20–25 minuti.

## Prerequisiti
- Lab 3 completato (c'è una decisione tecnica reale da documentare).
- Branch `lab/lab04_skills`.

## Passi
1. Leggi `skills/adr-writing.md`: template, prompt operativo, anti-pattern.
2. Copia la skill in `.claude/skills/adr-writing.md`.
3. Verifica che `agents/spring-architect.md` citi la skill nel protocollo (nel kit già lo fa).
4. Chiedi:
   ```text
   Come spring-architect, usa la skill adr-writing per documentare la decisione del Lab 3:
   dove vive la validazione dell'input utente (DTO con Bean Validation vs service vs controller).
   Minimo 2 alternative reali. Salva come docs/adr/ADR-001-input-validation.md, stato: proposta.
   ```
5. Valuta l'ADR contro i criteri della skill: leggibile in <3 minuti? Alternative con motivi di scarto? Rollback presente?
6. Prova la riusabilità: fai produrre un secondo ADR (argomento a scelta) a un agente DIVERSO (documentation-writer) con la stessa skill. I due documenti sono strutturalmente identici?

## Attività bonus
- Modifica il template nella skill (es. aggiungi la sezione "Metriche di successo") e rigenera: la modifica si propaga a entrambi gli agenti.
- Crea una micro-skill tua (es. formato standard dei commit message) e usala dal git-guardian.

## Criteri di successo
- ADR-001 completo e conforme al template.
- Stessa skill, due agenti, struttura identica: hai separato il "come" dal "chi".
