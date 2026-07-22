# Workbook studente

## Prima del corso
- [ ] Installa Claude Code e verifica l'avvio in un repo qualsiasi.
- [ ] Clona questo repository; `git status` pulito.
- [ ] Crea il branch `lab/claude-code-agentic`.
- [ ] Verifica di NON avere segreti reali (`.env`, chiavi) nella copia di lavoro.

## Scheda laboratorio (una per lab — copiala 6 volte)

### Lab n° ___ — Titolo: ______________________
| Campo | Note |
|---|---|
| Obiettivo del lab (con parole mie) | |
| Agenti usati | |
| Tool concessi a ciascuno | |
| Hook attivi | |
| Prompt che ha funzionato meglio | |
| Cosa è andato storto e perché | |
| Evidenze prodotte (file, log, diff) | |
| Rischi residui | |
| Un miglioramento che farei | |

## Domande di verifica (rispondi a fine giornata)
1. Cosa scrivo nella `description` perché un agente venga invocato al momento giusto?
2. Che differenza c'è tra exit code 0 e 2 in un hook PreToolUse, e chi legge lo stderr?
3. Perché il reviewer non deve avere `Write`? Cita il principio.
4. Cosa reinietta un hook PostCompact e perché serve?
5. Perché si autorizzano i singoli tool MCP e non "il server"?
6. Quali due metriche misureresti PRIMA di introdurre gli agenti nel tuo team?

## Dopo il corso — piano personale
Attività ripetitiva scelta: ______________________
1. **Agent**: nome, description ("quando usarlo"), tool minimi → file `.md`.
2. **Hook**: quale evento, cosa blocca/automatizza → script.
3. **Workflow**: catena, contratti, stop condition → documento (template in `skills/workflow-design.md`).
4. **Checklist sicurezza**: da `security/CHECKLIST_ENTERPRISE.md`, adattata.

Impegno: entro il ______ provo il punto 1 su un repo non critico, in sola lettura, con audit attivo.
