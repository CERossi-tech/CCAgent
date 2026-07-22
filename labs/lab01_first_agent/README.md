# Lab 1 — Primo subagent: java-reviewer

## Obiettivo
Creare (o adattare) un agente reviewer minimale read-only e ottenere 3 finding con evidenze su `examples/springboot/UserService.java`.

## Durata
25–35 minuti.

## Prerequisiti
- Branch `lab/lab01_first_agent` attivo, `git status` pulito.
- Nessun segreto reale nel repository.
- Claude Code avviato nella root del progetto.

## Passi
1. Copia `agents/java-reviewer.md` in `.claude/agents/java-reviewer.md` e leggilo per intero: frontmatter, description, tools, protocollo.
2. Verifica il least privilege: i tool devono essere solo `Read, Grep, Glob` (con `disallowedTools: Bash, Write, Edit`).
3. Avvia Claude Code e chiedi:
   ```text
   Fai una code review di examples/springboot/UserService.java usando l'agente java-reviewer.
   Voglio almeno 3 finding con file:riga, severità e patch proposta come testo.
   ```
4. Verifica l'output: ogni finding cita `file:riga`? Le severità sono classificate (bloccante/raccomandato/opzionale)? C'è un verdetto?
5. Rilancia la stessa richiesta: l'output è strutturato allo stesso modo? La ripetibilità è il criterio chiave.
6. Compila la retrospettiva nel workbook: quale finding ti ha sorpreso? Quale è un falso positivo?

## Esperimento sulla description
Cambia la description in "Agente esperto di Java" (senza il "quando"), riavvia e chiedi genericamente "controlla il progetto". Osserva se e come cambia il routing verso l'agente. Poi ripristina la description originale.

## Attività bonus
- Togli `Grep` dai tool e osserva come degrada l'analisi.
- Aggiungi al protocollo "massimo 5 finding, ordinati per severità" e verifica che venga rispettato.
- Trasforma l'output in un commento PR con `documentation-writer`.

## Criteri di successo
- ≥3 finding reali con evidenze `file:riga`.
- Output ripetibile con la stessa struttura.
- L'agente non ha modificato alcun file (verifica con `git status`).
- Hai osservato l'effetto della description sul routing.
