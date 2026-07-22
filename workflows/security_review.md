# Workflow: Security Review

## Trigger
Pre-merge su aree sensibili (auth, input, dati), pre-release, o audit schedulato.

## Catena agentica
`workflow-orchestrator -> prompt-injection-hunter -> security-auditor -> dependency-auditor -> incident-analyst (solo se finding critici) -> documentation-writer`

## Input
- Perimetro: diff, modulo o intero repo (dichiararlo esplicitamente).
- Skill: security-review, prompt-injection-defense.

## Passi
1. **Prompt-injection-hunter**: scansione contenuti repo per injection (README, template, fixture, config).
2. **Security-auditor**: checklist skill security-review sul perimetro — input, segreti, authN/Z, config; ogni finding con file:riga, scenario, fix, severità.
3. **Dependency-auditor**: CVE note e licenze sul manifest.
4. Triage congiunto: dedup, severità finale, falsi positivi marcati con motivo.
5. Se ≥1 Critical: **incident-analyst** valuta se è già sfruttabile/sfruttato (log review) e apre procedura incident.
6. **Documentation-writer**: report finale + ticket per Medium/Low con scadenze.

## Guardrail
- Tutti gli agenti read-only; scanner locali via Bash allowlist.
- L'output non contiene exploit completi né segreti eventualmente trovati (solo posizione e tipo).

## Stop condition
- Verdetto emesso: `pass / pass con condizioni (ticket) / fail (blocco merge-release)`.
- Ogni Critical/High ha owner e azione; nessun finding "aperto senza assegnazione".

## Output e handoff
- Report severità-ordinato con evidenze; verdetto; ticket creati.
- Decisione umana: accettazione rischi residui documentata.
