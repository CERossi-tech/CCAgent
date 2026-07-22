# Skill: Observability

## Scopo
Metodo per leggere log, metriche e tracce e produrre diagnosi con evidenze, non impressioni.

## Quando usarla
- Analisi di un'anomalia (latenza, errori, saturazione).
- Report periodico sullo stato di un servizio.
- Supporto a incident response.

## Procedura
1. **Definisci la domanda**: "perché X?" con X misurabile (p95 latenza, error rate, throughput).
2. **Quattro segnali d'oro**: latenza, traffico, errori, saturazione. Parti sempre da qui.
3. **Correlazione temporale**: cosa è cambiato nell'intorno (deploy, config, dipendenza, cron)?
4. **Restringi**: da servizio → endpoint → componente → riga di log rappresentativa.
5. **Falsifica**: cerca attivamente evidenze contro la tua ipotesi prima di affermarla.

## Regole sulle evidenze
- Ogni affermazione cita: fonte (file di log, dashboard, query) + timestamp + estratto minimo.
- Distingui sempre: **osservato** / **inferito** / **ipotesi da verificare**.
- Mai incollare log grezzi con dati sensibili: usa estratti anonimizzati.

## Output atteso
```markdown
## Sintomo (misurato)
## Timeline (UTC)
## Evidenze
## Ipotesi (ordinate per probabilità, con test per verificarle)
## Azioni consigliate (mitigazione ora / fix dopo)
```

## Anti-pattern
- Conclusioni da un singolo log.
- Confondere correlazione temporale con causa senza test di verifica.
