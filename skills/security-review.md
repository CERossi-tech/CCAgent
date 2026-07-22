# Skill: Security Review

## Scopo
Checklist e metodo per review di sicurezza applicativa su diff o modulo, con severità e evidenze.

## Quando usarla
- Prima di commit/merge su codice sensibile (auth, input, dati, crypto).
- Gate pre-release.
- Audit periodico.

## Checklist
### Input e injection
- [ ] Input validato al confine (tipo, range, lunghezza, formato).
- [ ] SQL: query parametrizzate, mai concatenazione.
- [ ] Command/path: nessun input utente in comandi shell o path senza sanitizzazione.
- [ ] Deserializzazione di dati non fidati assente o vincolata.

### Segreti e dati
- [ ] Nessun segreto hardcoded (chiavi, token, password) — nemmeno in test/fixture.
- [ ] Log senza dati sensibili (token, password, PII in chiaro).
- [ ] Dati sensibili cifrati a riposo/in transito dove richiesto.

### AuthN/AuthZ
- [ ] Ogni endpoint ha controllo di autorizzazione esplicito (no security by obscurity).
- [ ] Controlli lato server, mai solo client.
- [ ] Sessioni/token: scadenza, revoca, scope minimi.

### Dipendenze e configurazione
- [ ] Dipendenze senza CVE note critiche (scanner locale se disponibile).
- [ ] Configurazioni di default sicure; debug/verbose disattivi in produzione.

## Severità
- **Critical**: sfruttabile ora, impatto su dati/controllo → blocca merge.
- **High**: sfruttabile con condizioni → blocca release.
- **Medium**: hardening necessario → ticket con scadenza.
- **Low/Info**: igiene → backlog.

## Prompt operativo
1. Perimetro: quali file/flussi sono nel diff.
2. Applica checklist; ogni finding = file:riga + scenario di attacco in 2 righe + fix proposto.
3. Nessun exploit completo nell'output: descrivi il rischio, non l'arma.

## Output atteso
Tabella `| Severità | File:riga | Vulnerabilità | Scenario | Fix |` + verdetto: `pass / pass con condizioni / fail`.

## Anti-pattern
- Report di soli tool automatici senza triage.
- Segnalare 40 low e perdere l'unico critical.
