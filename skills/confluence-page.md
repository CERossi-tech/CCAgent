# Skill: Confluence Page

## Scopo
Trasformare output tecnici (review, report, ADR, postmortem) in pagine Confluence leggibili da audience mista.

## Quando usarla
- Un artefatto agentico deve essere condiviso fuori dal repository.
- Serve una pagina di stato per management o team non tecnici.

## Struttura pagina
```markdown
# <Titolo azione-orientato>

> **TL;DR** — 3 righe massimo: cosa, perché, cosa serve dal lettore.

## Contesto (5 righe max)
## Cosa è stato fatto / trovato
## Evidenze (tabella o elenco con link a PR/commit/ticket)
## Prossimi passi (owner + data)
## Appendice tecnica (collassabile)
```

## Prompt operativo
1. Identifica l'audience: tecnica, mista, management. Adatta il livello di dettaglio.
2. Il TL;DR si scrive per ultimo ma si mette per primo.
3. Ogni affermazione fattuale ha un link (PR, commit, log, ticket).
4. I dettagli tecnici vanno in appendice, mai nel corpo.
5. Nessun segreto, hostname interno o dato cliente nella pagina.

## Criteri di qualità
- Un lettore capisce cosa deve fare in 60 secondi.
- I prossimi passi hanno sempre owner e data.

## Anti-pattern
- Copiare l'output grezzo dell'agente nella pagina.
- Pagine senza owner: diventano archeologia in un mese.
