# Workflow: Documentation Refresh

## Trigger
Modifica ad API pubbliche, config o comandi; oppure audit periodico (settimanale).

## Catena agentica
`codebase-cartographer -> documentation-writer -> java-reviewer (verifica esempi) -> confluence-writer (opzionale)`

## Input
- Range di commit da coprire (default: ultimo refresh..HEAD).
- Elenco documenti sorgente di verità: README, docs/, OpenAPI.

## Passi
1. **Cartographer**: diff del range → elenco superfici pubbliche cambiate (endpoint, config, CLI, contratti).
2. **Documentation-writer**: per ogni superficie, confronta doc esistente vs codice reale; classifica: `mancante / obsoleta / corretta`.
3. Aggiorna i documenti obsoleti e crea i mancanti; ogni modifica cita il commit che la origina.
4. **Reviewer**: verifica che gli esempi di codice nei doc compilino/siano coerenti con le firme reali.
5. **Confluence-writer** (skill confluence-page): pubblica sintesi per il team se richiesto.

## Guardrail
- Write limitato a `README*`, `docs/**`, `*.md`, spec OpenAPI: hook allowlist path.
- Nessuna modifica a codice sorgente in questo workflow.

## Stop condition
- Ogni superficie cambiata nel range ha doc `corretta`, oppure è tracciata come TODO con ticket.
- Diff solo su file di documentazione.

## Output e handoff
- Diff dei documenti + tabella superfici→stato→commit.
- Decisione umana: merge del refresh.
