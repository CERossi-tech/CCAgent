# Skill: Java Code Review

## Scopo
Checklist e metodo per review Java/Spring ripetibili, con classificazione dei rischi.

## Quando usarla
- Diff che tocca codice Java/Spring.
- Review pre-merge o audit periodico.

## Checklist
### Correttezza
- [ ] Null safety: Optional usato dove serve, nessun `get()` nudo, annotazioni `@Nullable/@NonNull` coerenti.
- [ ] Eccezioni: mai catch generici silenziosi; eccezioni checked motivate; messaggi con contesto.
- [ ] Concorrenza: stato condiviso protetto; nessun `SimpleDateFormat` condiviso; collezioni thread-safe dove serve.

### Spring
- [ ] Transazioni: `@Transactional` sul livello giusto; nessuna chiamata self-invocation che la bypassa; readOnly dove possibile.
- [ ] Injection: constructor injection; nessun `@Autowired` su field in codice nuovo.
- [ ] Boundaries: validazione input al confine (`@Valid`, Bean Validation); DTO ≠ entity.

### Qualità
- [ ] Naming: intenzione, non implementazione.
- [ ] Logging: livello corretto, niente dati sensibili, contesto sufficiente (id, non payload).
- [ ] Test: casi limite presenti (null, vuoto, duplicato, concorrente); nessun test che testa il mock.
- [ ] Performance: query N+1, fetch eager ingiustificati, allocazioni in loop caldi.

## Prompt operativo
1. Leggi il diff, poi SOLO i file necessari a capire il contesto.
2. Applica la checklist; per ogni rilievo cita file:riga.
3. Classifica: **bloccante** (bug, sicurezza, perdita dati) / **raccomandato** (manutenzione) / **opzionale** (stile).
4. Proponi patch minima solo per i bloccanti.

## Output atteso
Tabella `| Severità | File:riga | Rilievo | Proposta |` + sintesi in 3 righe.

## Anti-pattern
- Review di stile su codice con bug bloccanti non segnalati.
- "Riscrivere tutto": la review propone la patch minima.
