# Workflow: MCP Onboarding

## Trigger
Richiesta di aggiungere un server MCP alla configurazione di progetto/team.

## Catena agentica
`mcp-gatekeeper (lead) -> security-auditor -> enterprise-policy-agent -> documentation-writer`

## Input
- Server candidato: sorgente, versione, motivo della richiesta, caso d'uso.
- Skill: mcp-risk-assessment.

## Passi
1. **Mcp-gatekeeper** (skill mcp-risk-assessment): inventario tool esposti; classifica capacità READ/WRITE/EXEC/NET; provenienza e versioning.
2. **Security-auditor**: review del codice/contratto del server se disponibile — path traversal, command injection, SSRF nei parametri; dati raggiungibili e loro sensibilità.
3. **Mcp-gatekeeper**: applica matrice di rischio → decisione per tool: `allow / allow con conferma / deny`; produce allowlist nominale.
4. **Enterprise-policy-agent**: traduce l'allowlist in configurazione `.claude/settings.json` versionata + hook `pretool_mcp_allowlist.py`; definisce logging invocazioni.
5. Periodo di prova: 2 settimane con log attivo e solo tool READ; poi review dei log e sblocco graduale.
6. **Documentation-writer**: scheda del server in docs (cosa fa, cosa può, quando rivalutare).

## Guardrail
- Nessun server attivo prima del passo 4; niente "provo intanto in locale" fuori sandbox.
- Deny by default: ogni tool non esplicitamente in allowlist è bloccato.

## Stop condition
- Allowlist versionata, hook attivo, log funzionante, scheda documentata, data di revisione fissata.
- Un server `deny` complessivo viene documentato con motivo: la valutazione negativa è un deliverable valido.

## Output e handoff
- Risk assessment, allowlist, config versionata, scheda server; approvazione finale: owner sicurezza.
