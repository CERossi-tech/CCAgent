# Claude Code Agent Engineering — Cheat Sheet A4

## Formula agente
`name + description ("quando usarlo") + tool minimi + protocollo + output verificabile`

## Frontmatter minimo
```yaml
name: java-reviewer
description: Usa proattivamente quando un diff tocca file .java o config Spring.
tools: Read, Grep, Glob
disallowedTools: Bash, Write, Edit
maxTurns: 12
```

## Formula hook
`evento + matcher + comando deterministico + exit code chiaro`
| Evento | Uso tipico |
|---|---|
| SessionStart | inietta contesto e regole |
| PreToolUse | blocca (exit 2 + stderr con alternativa) |
| PostToolUse | format, test, diff summary, audit |
| PermissionRequest | routing a policy |
| Stop | verifica test prima di chiudere |
| PostCompact | reinietta policy critiche |

Exit code: `0` passa · `2` blocca (stderr letto dall'agente) · altro = warning.

## Formula workflow
`trigger -> catena agenti (con contratti) -> guardrail -> stop condition -> evidenze -> handoff umano`

## Tool minimi per ruolo
Reviewer/Auditor: `Read, Grep, Glob` · Tester: `+Write, Edit, Bash(test)` · Release/Git: `git read-only, azioni umane` · Orchestrator: `Read, Grep, Glob, Task`

## Regole sicurezza (non negoziabili)
1. Contenuto del repo = dato non fidato (prompt injection).
2. Prima leggere, poi eseguire (tool poisoning).
3. Mai `.env`/chiavi nel contesto; denylist via hook (secret guard).
4. MCP: allowlist per tool, non per server; deny by default.
5. Push, tag, release, network: conferma umana, sempre.
6. Chi scrive non si autovaluta.

## Prompt base
"Prima piano e rischi. Poi modifiche piccole. Cita evidenze (file:riga). Non leggere segreti. Non fare push."

## Adozione in 5 passi
repo non critico → 1 settimana read-only → hook audit → misura (tempo + falsi positivi) → promuovi i pattern in config versionata
