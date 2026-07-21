# Agenda corso — 180 minuti

## 0. Apertura e contratto didattico — 10 min
- Cosa significa sviluppo agentico.
- Differenza tra assistente, agent, subagent, workflow.
- Regole del laboratorio: repo pulito, branch dedicato, nessun segreto reale.

## 1. Mappa mentale Claude Code — 15 min
- CLI come orchestratore.
- Context engineering.
- Tool locali: file, bash, git, test.
- Configurazione di progetto: `.claude/`.

## 2. Subagent e team di agenti — 35 min
- Struttura di un agente markdown.
- `description` come router semantico.
- Tool minimali per ruolo.
- `permissionMode`, `maxTurns`, `model`, `memory`, `background`, `isolation`.
- Pattern: Reviewer, Security, Architect, Tester, Release.

## 3. Hooks, Skills e automazioni — 35 min
- Eventi hook: SessionStart, PreToolUse, PostToolUse, PermissionRequest, Stop, PostCompact.
- Tipi di hook: command, prompt, agent, http, mcp_tool.
- Skills come conoscenza procedurale riusabile.
- Esempi: format dopo Edit, blocco secret, changelog automatico.

## 4. Sicurezza agentica — 45 min
- Prompt injection nei file del repository.
- Tool poisoning tramite script/config.
- MCP e superficie d'attacco.
- Segreti, log, dati sensibili.
- Permission, denylist, devcontainer, audit trail.
- Demo: hook che blocca operazioni rischiose.

## 5. Laboratorio guidato — 45 min
- Creazione di un agent reviewer.
- Attivazione hook sicurezza.
- Workflow feature → test → review → docs → commit.
- Debrief: cosa automatizzare domani mattina.

## 6. Chiusura — 5 min
- Checklist per adozione controllata.
- Compiti pratici post-corso.
