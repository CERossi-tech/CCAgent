# Guida operativa — Dove mettere i file e come verificare che tutto scatti

Il kit contiene i *sorgenti* (cartelle `agents/`, `skills/`, `hooks/`, `workflows/`). Perché Claude Code li usi davvero, vanno **installati** nella struttura `.claude/` del repository su cui lavori. Questa guida spiega, per ogni componente: dove va il file, cosa lo attiva, come verificare che funzioni.

## Mappa di installazione

```text
il-tuo-repo/
├── .claude/
│   ├── settings.json          ← permessi + registrazione hook (di team, versionato)
│   ├── settings.local.json    ← override personali (in .gitignore)
│   ├── agents/                ← subagent: un file .md per agente
│   │   └── java-reviewer.md
│   ├── skills/                ← skill: UNA CARTELLA per skill, con SKILL.md dentro
│   │   └── adr-writing/
│   │       └── SKILL.md
│   └── hooks/                 ← script richiamati da settings.json
│       └── pretool_block_dangerous_bash.py
├── CLAUDE.md                  ← contesto sempre attivo del progetto (breve!)
└── workflows/                 ← documenti workflow: restano qui, li segue l'orchestratore
```

Regola dei due livelli: tutto ciò che sta in `.claude/` del repo vale per quel progetto (e per il team, se versionato); la stessa struttura in `~/.claude/` della tua home vale per te su ogni progetto.

## 1. Agenti — attivazione e verifica

**Dove**: copia il file da `agents/<nome>.md` a `.claude/agents/<nome>.md`. Nient'altro: i subagent vengono caricati automaticamente da quella cartella.

**Cosa li attiva**: due vie.
- *Routing automatico*: Claude legge la `description` del frontmatter e delega quando il task corrisponde. È il motivo per cui le description del kit sono scritte come "usa proattivamente quando…": sono il criterio di attivazione.
- *Invocazione esplicita*: nominalo nel prompt ("usa l'agente java-reviewer per…") o menzionalo con `@java-reviewer`.

**Verifica**:
1. `/agents` in sessione: l'agente deve comparire nell'elenco.
2. Test di routing: dai un task che ricade nella description SENZA nominare l'agente (es. "fai una review di questo diff Java") e osserva se viene delegato.
3. Test dei limiti: chiedi all'agente read-only di modificare un file → deve rifiutare o fallire per mancanza del tool, e `git status` deve restare pulito.

**Se non scatta**: quasi sempre è la description troppo generica (dice "cosa fa" invece di "quando usarlo"). Secondo sospetto: file nella cartella sbagliata o frontmatter malformato (lo YAML deve aprire e chiudere con `---`).

## 2. Hook — attivazione e verifica

**Dove**: lo script va in `.claude/hooks/` (o dove preferisci nel repo), ma **la registrazione avviene in `.claude/settings.json`**: un hook non registrato non esiste. La struttura è `evento → matcher → comando`; l'esempio completo commentato è in `docs/SETTINGS_EXPLAINED.md`.

```json
"hooks": {
  "PreToolUse": [
    { "matcher": "Bash",
      "hooks": [ { "type": "command", "command": "python .claude/hooks/pretool_block_dangerous_bash.py" } ] }
  ]
}
```

**Cosa li attiva**: l'evento (SessionStart, PreToolUse, PostToolUse, PermissionRequest, Stop, PostCompact) filtrato dal `matcher` sul nome del tool. Il contratto è l'exit code: `0` passa, `2` blocca e lo stderr viene mostrato all'agente, altri codici = warning.

**Verifica — sempre in due tempi**:
1. *A freddo, senza Claude*: esegui lo script a mano con un input JSON simulato e controlla l'exit code:
   ```bash
   echo '{"tool_name":"Bash","tool_input":{"command":"rm -rf /"}}' | python .claude/hooks/pretool_block_dangerous_bash.py; echo "exit=$?"
   # atteso: messaggio BLOCKED su stderr, exit=2
   ```
2. *In sessione*: `/hooks` mostra gli hook registrati; poi induci l'evento (chiedi qualcosa che genererebbe il comando vietato) e osserva il blocco + la riformulazione del piano da parte dell'agente.
3. *Audit*: se hai registrato `audit_log.py`, apri `.claude/audit.jsonl` e verifica che gli eventi ci siano — e che non contengano segreti.

**Se non scatta**: script non eseguibile (`chmod +x`), path relativo sbagliato rispetto alla root del repo, matcher che non corrisponde al nome reale del tool, o JSON di settings non valido (un errore di sintassi disattiva silenziosamente tutto il blocco).

## 3. Skill — attivazione e verifica

**Dove**: attenzione, qui il kit e Claude Code differiscono. Nel kit le skill sono file piatti (`skills/adr-writing.md`) per leggibilità didattica; Claude Code le vuole come **cartelle** con un file `SKILL.md` dentro:

```bash
mkdir -p .claude/skills/adr-writing
cp skills/adr-writing.md .claude/skills/adr-writing/SKILL.md
```

Aggiungi in testa al file un frontmatter minimo con `name` e `description` (la description è il criterio di caricamento automatico, come per gli agenti):

```yaml
---
name: adr-writing
description: Usa quando serve documentare una decisione architetturale come ADR.
---
```

**Cosa le attiva**: invocazione diretta (`/adr-writing` in sessione) oppure caricamento automatico quando Claude giudica il task pertinente alla description. Gli agenti del kit le richiamano nel protocollo ("carica la skill adr-writing"): funziona se la skill è installata.

**Verifica**: chiedi esplicitamente "usa la skill adr-writing per documentare la decisione X" e controlla che l'output segua il template della skill (sezioni, alternative, rollback). Poi ripeti senza nominarla, con un task pertinente, per testare il caricamento automatico.

**Se non scatta**: manca la struttura a cartella (file piatto in `.claude/skills/` non basta), manca il frontmatter, o la description non matcha il task.

## 4. Workflow — come si "rispetta la sequenza"

Qui serve chiarezza concettuale: **i workflow non sono un meccanismo nativo di Claude Code**. Sono documenti di orchestrazione (i file in `workflows/`) che diventano vincolanti in tre modi, dal più semplice al più robusto:

1. *Riferimento nel prompt*: "Lavora come workflow-orchestrator seguendo `workflows/feature_to_pr.md`". L'orchestratore legge il documento e ne segue catena, contratti e stop condition. È l'approccio dei lab.
2. *Skill di workflow*: converti il documento in una skill (`.claude/skills/feature-to-pr/SKILL.md`): diventa richiamabile con `/feature-to-pr` e caricabile in automatico.
3. *Guardrail deterministici sui punti critici*: la sequenza la tiene l'orchestratore (probabilistico), ma i passaggi non negoziabili li tengono gli hook (deterministici): branch-guard impedisce di lavorare su main, secret-guard impedisce le letture vietate, lo Stop hook verifica i test prima della chiusura. Il documento dice l'ordine; gli hook rendono impossibile saltare i gate.

**Verifica**: esegui il workflow su un caso piccolo (Lab 3) e controlla il log di orchestrazione: ogni passo ha prodotto l'output che il passo successivo richiedeva? I gate hanno emesso un verdetto esplicito? Lo stop condition ha chiuso il ciclo?

## 5. Checklist di collaudo completa (dopo l'installazione)

- [ ] `/agents` elenca tutti gli agenti copiati; `/hooks` elenca gli hook registrati; `/permissions` riflette allow/deny attesi.
- [ ] Ogni hook bloccante è stato testato a freddo con JSON simulato (exit 2 verificato).
- [ ] Test di routing: un task per categoria (Java, SQL, security…) delega all'agente giusto senza nominarlo.
- [ ] Test negativo: l'agente read-only non riesce a modificare file; il comando vietato viene bloccato con messaggio utile.
- [ ] `.claude/audit.jsonl` si popola e non contiene segreti.
- [ ] Una skill invocata per nome produce l'output nel formato del suo template.
- [ ] Il workflow di prova (Lab 3) arriva all'handoff con tutti gli artefatti attesi.
- [ ] `git status`: dopo tutti i test read-only, il working tree è pulito.

## Riferimenti

- Registrazione hook e permessi: `docs/SETTINGS_EXPLAINED.md`
- Cataloghi: `docs/AGENT_CATALOG.md`, `docs/HOOK_CATALOG.md`
- Percorso guidato: `labs/lab01` (agenti) → `labs/lab02` (hook) → `labs/lab03` (workflow) → `labs/lab04` (skill)
- Documentazione ufficiale Claude Code: https://code.claude.com/docs (subagents, skills, hooks, settings)
