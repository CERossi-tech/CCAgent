# Skill: ADR Writing

## Scopo
Produrre Architecture Decision Record brevi, verificabili e versionati insieme al codice.

## Quando usarla
- Una scelta tecnica vincola il futuro (framework, pattern, database, contratto API).
- Un refactoring cambia un'assunzione architetturale.
- Un incidente rivela una decisione mai documentata.

## Template
```markdown
# ADR-NNN: <titolo della decisione>

- **Data**: YYYY-MM-DD
- **Stato**: proposta | accettata | superata da ADR-XXX
- **Owner**: <team/persona>

## Contesto
Qual è il problema e perché va deciso ora. Vincoli tecnici e di business.

## Decisione
Cosa si è deciso, in una frase. Poi il dettaglio.

## Alternative considerate
| Alternativa | Pro | Contro | Perché scartata |
|---|---|---|---|

## Conseguenze
Positive, negative, debiti accettati.

## Rollback
Come si torna indietro e quanto costa.
```

## Prompt operativo
1. Leggi il diff o la discussione che origina la decisione.
2. Identifica la decisione in UNA frase; se sono due, sono due ADR.
3. Compila il template; le alternative scartate sono obbligatorie (minimo 2).
4. Cita file/commit come evidenze del contesto.
5. Numera come `docs/adr/ADR-NNN-<slug>.md` (progressivo).

## Criteri di qualità
- Leggibile in < 3 minuti.
- Nessun gergo non spiegato.
- Rollback sempre presente, anche se è "non praticabile: motivo".

## Anti-pattern
- ADR come verbale di riunione.
- Decisione mescolata a tutorial di implementazione.
- ADR aggiornato invece che superato: gli ADR sono append-only.
