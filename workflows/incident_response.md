# Workflow: Incident Response

## Trigger
Alert di produzione, segnalazione utente grave, o sospetto secret leak.

## Catena agentica
`incident-analyst (lead) -> observability-agent -> security-auditor (se security-related) -> documentation-writer (postmortem)`

## Input
- Descrizione sintomo + orario di inizio (anche approssimato).
- Accesso read-only a log/metriche disponibili localmente.

## Passi
1. **Incident-analyst**: classifica severità e tipo (disponibilità / integrità / sicurezza); apre il documento incident con timeline vuota.
2. **Observability-agent** (skill observability): quattro segnali d'oro, correlazione con deploy/config recenti, restringimento a componente; ogni evidenza timestampata.
3. Mitigazione proposta (rollback, feature flag off, scale): l'agente PROPONE, l'umano ESEGUE le azioni su produzione.
4. Se security: **security-auditor** valuta perimetro compromesso; se secret leak → rotazione immediata proposta come priorità 1.
5. Timeline consolidata in tempo reale (UTC) nel documento incident.
6. A incidente chiuso: **documentation-writer** produce il postmortem blameless — timeline, causa radice, fattori contribuenti, azioni con owner/data.

## Guardrail
- NESSUNA azione di scrittura su sistemi di produzione da parte degli agenti: solo analisi e proposte.
- Log citati in forma anonimizzata; niente PII/segreti nel documento incident.

## Stop condition
- Mitigazione confermata dall'umano e sintomo rientrato → si passa a postmortem.
- Se dopo 2 cicli di ipotesi non c'è restringimento: escalation a on-call senior, l'agente resta in supporto documentale.

## Output e handoff
- Documento incident con timeline; postmortem entro 48h; azioni correttive come ticket.
