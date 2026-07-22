# Claude Code Agent Engineering — Enterprise Course Kit

Corso pratico da 3 ore sulla modalità agentica di Claude Code, con focus su subagent, hook, skill, MCP, sicurezza e workflow quotidiani per sviluppatori.

## Deliverable inclusi

- `slides/Claude_Code_Agent_Engineering_Enterprise_v2.pptx`
- `manual/Manuale_Claude_Code_Agent_Engineering_v2.docx`
- `docs/` materiali docente e studente (incluso `SPEECH_SLIDES.md`: discorso completo per ognuna delle 44 slide)
- `agents/` 24 agenti pronti all'uso
- `hooks/` 18 hook/script di guardrail e automazione
- `skills/` 10 skill operative
- `workflows/` 12 workflow agentici
- `labs/` 6 laboratori guidati
- `examples/` mini-progetti su cui esercitarsi
- `security/` policy, threat model, checklist

## Obiettivo del corso

Non insegnare solo un comando, ma un metodo: trasformare Claude Code in un orchestratore di agenti specializzati che sanno analizzare, modificare, testare, documentare e proteggere un repository.

## Come usare il kit

1. Aprire le slide.
2. Leggere `docs/AGENDA_180_MIN.md`.
3. Copiare `.claude/` dentro un repository demo.
4. Eseguire i laboratori in ordine.
5. Adattare policy, hook e permission per il proprio contesto aziendale.

## Nota sicurezza

Gli hook eseguono comandi locali: usarli prima in sandbox/devcontainer. Applicare allowlist e denylist coerenti con le policy aziendali.

Fonti principali: Anthropic Claude Code docs (subagents, hooks, security, SDK/permissions, MCP) consultate nel 2026.
