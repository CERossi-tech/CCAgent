# Catalogo hook

Ogni hook è uno script deterministico agganciato a un evento del ciclo di vita. Contratto: exit `0` = passa, exit `2` = blocca (lo stderr viene mostrato all'agente, che può correggersi), altri codici = warning non bloccante. Regola d'uso: leggere lo script prima di registrarlo, testarlo in sandbox con input JSON simulato, adattare pattern e path alle policy aziendali.

| Hook | Evento | Tipo | Cosa fa |
|---|---|---|---|
| `sessionstart_context.sh` | SessionStart | command | Inietta contesto dinamico a inizio sessione: branch corrente e ultimi 5 commit |
| `pretool_block_dangerous_bash.py` | PreToolUse (Bash) | command | Blocca comandi distruttivi: `rm -rf /`, `dd`, `mkfs`, `chmod -R 777`, push su main |
| `pretool_secret_guard.py` | PreToolUse (Read/Write/Edit) | command | Blocca lettura/scrittura di file sensibili: `.env`, chiavi SSH, `.pem`, `.p12`, credenziali |
| `pretool_branch_guard.sh` | PreToolUse (Write/Edit) | command | Blocca modifiche se il branch corrente è main/master: obbliga branch `lab/` o `feature/` |
| `pretool_no_binary_edit.py` | PreToolUse (Write/Edit) | command | Blocca modifiche accidentali a file binari: immagini, pdf, zip, jar, exe |
| `pretool_sql_select_only.py` | PreToolUse | command | Permette solo query SELECT: blocca INSERT/UPDATE/DELETE/DROP/ALTER/TRUNCATE (per i lab) |
| `pretool_license_guard.py` | PreToolUse | command | Warning (non bloccante) se l'input suggerisce copia di codice proprietario/licenziato |
| `pretool_mcp_allowlist.py` | PreToolUse (mcp__*) | command | Allowlist nominale dei tool MCP: blocca ogni `mcp__server__tool` non elencato |
| `audit_log.py` | PreToolUse / PostToolUse | command | Audit trail: appende su `.claude/audit.jsonl` timestamp, evento, tool e input di ogni invocazione |
| `permission_request_policy.py` | PermissionRequest | command | Classifica la richiesta (low / network / destructive) per instradare la decisione di permission |
| `posttool_format_changed_files.sh` | PostToolUse (Write/Edit) | command | Formatta i file toccati: `spotless:apply` se Maven, `npm run format` se Node — senza rompere la sessione |
| `posttool_diff_summary.sh` | PostToolUse (Write/Edit) | command | Stampa `git diff --stat` dopo ogni modifica: visibilità immediata su quanto è cambiato |
| `posttool_changelog_hint.sh` | PostToolUse | command | Appende una riga datata a `docs/CHANGELOG_DRAFT.md` come promemoria di changelog |
| `posttool_mermaid_validate.sh` | PostToolUse | command | Se `mmdc` è installato, individua i blocchi Mermaid nei doc per validarli |
| `precommit_no_large_files.sh` | pre-commit (git) | command | Blocca commit con file oltre 5 MB: intercetta binari e dump accidentali |
| `stop_verify_tests.sh` | Stop | command | A fine sessione tenta la suite (`mvn test` / `npm test`) come verifica finale, senza bloccare se i tool mancano |
| `postcompact_reinject_rules.md` | PostCompact | prompt | Reinietta le 7 regole non negoziabili dopo la compattazione del contesto (vedi il file) |
| `http_notify_example.json` | qualunque | http | Template di hook HTTP verso un endpoint aziendale (webhook da sostituire): notifiche a sistemi esterni |

## Note operative
- I PreToolUse bloccanti scrivono su stderr COSA fare in alternativa, non solo il divieto: l'agente legge il messaggio e riformula il piano.
- `audit_log.py` registra gli input dei tool: verificare periodicamente che nel log non finiscano dati sensibili.
- Gli hook girano in locale con i permessi dell'utente: la loro integrità è un asset (review di ogni modifica a `.claude/` e `hooks/`).
- La registrazione avviene in `.claude/settings.json`: l'esempio completo commentato è in `docs/SETTINGS_EXPLAINED.md`.
