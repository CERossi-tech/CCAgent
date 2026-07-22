# Workflow: Release Train

## Trigger
Cadenza di release raggiunta (sprint/settimana) o release on-demand approvata.

## Catena agentica
`release-manager (lead) -> git-guardian -> security-auditor (gate) -> test-generator (smoke) -> documentation-writer -> confluence-writer (annuncio)`

## Input
- Range: `ultimo-tag..HEAD`.
- Criteri di rilascio del progetto (definition of releasable).

## Passi
1. **Git-guardian**: verifica branch di release pulito, nessun commit fuori processo, nessun file sensibile nel range.
2. **Release-manager**: raccoglie commit/PR del range; classifica (skill release-notes); identifica breaking.
3. **Gate security**: workflow security_review in modalità rapida sul range; Critical aperti bloccano il treno.
4. **Smoke**: esecuzione suite completa + smoke test; esiti allegati.
5. **Release-manager**: propone versione (semver in base ai contenuti), tag message e release notes.
6. **Umano**: crea tag e pubblica. L'agente non pusha e non pubblica MAI.
7. **Confluence-writer**: annuncio interno con TL;DR e link.

## Guardrail
- Hook `pretool_branch_guard.sh` (solo branch release), conferma umana su qualunque `git tag`/`push`.
- Un breaking non documentato con migrazione = stop del treno.

## Stop condition
- Checklist releasable completa: test verdi, gate pass, notes pronte, versione approvata.
- Qualsiasi item fallito → la release slitta, il report spiega perché.

## Output e handoff
- Release notes, tag message, esiti test, verdetto gate; azione umana: tag+publish.
