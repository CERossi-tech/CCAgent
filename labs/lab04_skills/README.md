# Skills riusabili

## Obiettivo
creare una skill ADR e usarla in un agent.

## Durata
25-35 minuti.

## Prerequisiti
- Branch `lab/lab04_skills`.
- Nessun segreto reale nel repository.
- Claude Code avviato nella root del progetto.

## Esercizio guidato
1. Leggi il materiale in `agents/`, `hooks/`, `skills/` rilevante.
2. Copia la configurazione necessaria in `.claude/`.
3. Avvia Claude Code e chiedi di operare solo sullo scope indicato.
4. Verifica output, diff e log.
5. Compila la retrospettiva.

## Prompt suggerito
```text
Lavora come workflow-orchestrator. Usa gli agenti minimi necessari per creare una skill ADR e usarla in un agent. Prima proponi piano e rischi, poi procedi con modifiche piccole e verificabili. Non leggere file segreti e non fare push.
```

## Attività bonus
- Riduci i tool concessi all'agente.
- Aggiungi una denylist.
- Trasforma l'output in commento PR.

## Criteri di successo
- Output ripetibile.
- Evidenze citate.
- Diff piccolo.
- Rischi residui espliciti.
