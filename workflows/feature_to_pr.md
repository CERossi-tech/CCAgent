# Workflow: Feature to PR

## Trigger
Ticket/obiettivo tecnico approvato; repository pulito; branch dedicato creato.

## Catena agentica
`workflow-orchestrator -> codebase-cartographer -> spring-architect -> (developer: main session) -> test-generator -> java-reviewer + security-auditor -> documentation-writer -> git-guardian`

## Input
- Ticket con acceptance criteria (o obiettivo in 3 righe).
- Branch `feature/<slug>` attivo.
- Test esistenti verdi (baseline).

## Passi
1. **Cartographer** (read-only): mappa i file/moduli impattati e le dipendenze; output: tabella impatto.
2. **Architect** (read-only): definisce vincoli — cosa non si tocca, pattern da rispettare, punto di validazione; output: vincoli in 10 righe.
3. **Developer**: implementa la patch minima dentro i vincoli; nessuna riscrittura opportunistica.
4. **Test-generator**: matrice casi limite (skill test-strategy) e implementazione test; esegue la suite.
5. **Gate**: java-reviewer (skill java-code-review) e security-auditor (skill security-review) in parallelo; ognuno emette `pass / pass con condizioni / fail`. Un `fail` riporta al passo 3.
6. **Documentation-writer**: aggiorna README/OpenAPI se toccati; produce PR summary con evidenze.
7. **Git-guardian**: verifica branch, dimensione diff, assenza file sensibili; suggerisce commit message. **Il commit/push lo fa l'umano.**

## Guardrail
- Hook: `pretool_secret_guard.py`, `pretool_branch_guard.sh`, `posttool_format_changed_files.sh`, `audit_log.py`.
- Diff budget: > 400 righe modificate → stop e richiesta di split.

## Stop condition
- Tutti i test passano (o motivo del mancato run documentato) E entrambi i gate ≥ `pass con condizioni`.
- Nessuna modifica a file segreti; diff comprensibile in < 10 minuti.
- Budget: max 2 iterazioni sviluppo→gate; alla terza, escalation umana.

## Output e handoff
- PR summary (sintesi, evidenze, rischi residui, checklist gate).
- Commit message suggerito.
- Decisione umana richiesta: merge sì/no.
