# Lab 5 — MCP risk assessment

## Obiettivo
Valutare una configurazione MCP come farebbe un security officer: inventario, classificazione, allowlist, gate policy.

## Durata
25–35 minuti.

## Prerequisiti
- Branch `lab/lab05_mcp_risk`.
- Agente `mcp-gatekeeper` e skill `mcp-risk-assessment` copiati in `.claude/`.
- Scenario: valutare un ipotetico server MCP "filesystem+fetch" che espone `read_file`, `write_file`, `list_dir`, `http_get`.

## Passi
1. Leggi `skills/mcp-risk-assessment.md`: procedura e matrice di rischio.
2. Chiedi:
   ```text
   Come mcp-gatekeeper, esegui un risk assessment del server MCP descritto:
   tool read_file, write_file, list_dir, http_get; provenienza: repository pubblico, non versionato internamente.
   Caso d'uso richiesto dal team: leggere documentazione di progetto per generare report.
   Applica la skill mcp-risk-assessment e produci la tabella con decisione per ogni tool.
   ```
3. Verifica il ragionamento: `write_file` e `http_get` sono giustificati dal caso d'uso? (No: il caso d'uso è read-only. La risposta attesa è deny/conferma.)
4. Fai produrre l'allowlist risultante e la bozza di configurazione con `enterprise-policy-agent`.
5. Scrivi la gate policy: cosa passa, cosa chiede conferma, cosa è negato, quando si rivaluta.
6. Confronta con `hooks/pretool_mcp_allowlist.py`: come si applica deterministicamente la tua allowlist?

## Attività bonus
- Ripeti l'assessment cambiando la provenienza in "server interno versionato": quali decisioni cambiano e perché?
- Aggiungi al server un tool `exec_command` e osserva la matrice: deve risultare deny.

## Criteri di successo
- Tabella completa `tool | capacità | dati | rischi | decisione | motivo`.
- Allowlist minima coerente col caso d'uso (least privilege dimostrato).
- Gate policy scritta e collegabile all'hook.
