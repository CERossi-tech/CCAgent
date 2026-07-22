# Workflow: Dependency Upgrade

## Trigger
CVE segnalata, dependency bot, o audit periodico di obsolescenza.

## Catena agentica
`dependency-auditor -> spring-architect (se major) -> (developer: main session) -> test-generator -> security-auditor -> release-manager`

## Input
- Manifest dipendenze (pom.xml, package.json, requirements...).
- Report scanner se disponibile.

## Passi
1. **Dependency-auditor**: inventario aggiornamenti disponibili; classifica: `security / major / minor / patch`; licenze compatibili (hook license guard).
2. Priorità: prima le security, poi major con breaking noti, poi il resto in batch.
3. Per ogni upgrade (uno alla volta per i major): leggere il changelog upstream PRIMA di aggiornare; annotare breaking changes.
4. Aggiornare, buildare, eseguire suite completa.
5. **Security-auditor**: verificare che la CVE risulti chiusa; nessuna nuova dipendenza transitiva sospetta.
6. **Release-manager**: voce di changelog per gli upgrade rilevanti.

## Guardrail
- Un major = un commit dedicato; mai "upgrade all" cieco.
- Hook `pretool_license_guard.py` su nuove dipendenze; lockfile sempre committato.
- Nessuna esecuzione di script post-install non letti (tool poisoning).

## Stop condition
- Build e test verdi dopo ogni upgrade; CVE target chiuse.
- Un upgrade che rompe la suite viene isolato in branch dedicato con ticket, non forzato.

## Output e handoff
- Tabella `dipendenza | da → a | motivo | breaking | esito test`.
- Decisione umana: merge; per major con breaking, review obbligatoria.
