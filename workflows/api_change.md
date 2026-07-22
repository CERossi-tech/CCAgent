# Workflow: API Change

## Trigger
Modifica a endpoint/contratto pubblico: nuovo campo, nuovo endpoint, deprecazione.

## Catena agentica
`api-contract-reviewer -> spring-architect -> (developer: main session) -> test-generator -> documentation-writer -> release-manager`

## Input
- Contratto attuale (OpenAPI/spec) e modifica proposta.
- Politica di versioning del progetto.

## Passi
1. **Api-contract-reviewer**: classifica la modifica — `additive / breaking / comportamentale`; per breaking, richiede piano di deprecazione.
2. **Architect**: definisce strategia — versioning, default retro-compatibili, feature flag se serve.
3. Implementazione: prima lo spec/contratto, poi il codice che lo rispetta (contract-first).
4. **Test-generator**: contract test (request/response contro spec) + casi limite; test di retro-compatibilità per i client esistenti.
5. **Documentation-writer**: OpenAPI aggiornato, esempi richiesta/risposta, note di migrazione se breaking.
6. **Release-manager**: voce changelog; breaking marcati 🚨 con migrazione (skill release-notes).

## Guardrail
- Un breaking senza piano di deprecazione = `fail` del gate al passo 1.
- Diff dello spec sempre incluso nella PR.

## Stop condition
- Contract test verdi; spec e codice coerenti; doc aggiornata.
- Per breaking: migrazione documentata e versione/deprecation header previsti.

## Output e handoff
- PR con spec + codice + test + doc; tabella compatibilità client.
- Decisione umana: approvazione del breaking e timing di rilascio.
