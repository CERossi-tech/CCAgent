# Workflow: Architecture Decision

## Trigger
Scelta tecnica strutturante: framework, pattern, boundary tra servizi, storage, contratto.

## Catena agentica
`spring-architect (lead) -> codebase-cartographer -> security-auditor (consulto) -> documentation-writer (ADR)`

## Input
- Problema da decidere, in una frase.
- Vincoli noti (budget, competenze team, compliance, deadline).

## Passi
1. **Architect**: formula la decisione come domanda chiusa; se emergono due domande, split in due ADR.
2. **Cartographer**: evidenze dal codice reale — come si fa oggi, quanto costa cambiare, cosa si rompe.
3. **Architect**: minimo 2 alternative reali oltre alla proposta (inclusa "non fare nulla" quando sensata); per ognuna pro/contro/costo di rollback.
4. **Security-auditor**: implicazioni di sicurezza di ogni alternativa (superficie, dati, dipendenze nuove).
5. Raccomandazione motivata dell'architect; la DECISIONE è umana (review del documento).
6. **Documentation-writer** (skill adr-writing): ADR numerato in `docs/adr/`; stato `proposta` finché l'umano non approva.

## Guardrail
- Tutto read-only: questo workflow non modifica codice.
- Ogni claim sul codebase cita file/evidenza; niente "si sa che...".

## Stop condition
- ADR completo (contesto, decisione proposta, ≥2 alternative, conseguenze, rollback) e leggibile in < 3 minuti.

## Output e handoff
- ADR in stato `proposta` + sintesi per la discussione di team; decisione e cambio stato: umani.
