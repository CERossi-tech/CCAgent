# 50 usi poco conosciuti ma utili

## 1. PostCompact policy reinjection
Dopo la compattazione del contesto reinserisce regole critiche: niente segreti, niente push, diff piccolo.

## 2. Agent isolation con worktree
Eseguire agenti su worktree temporanei per analisi parallele senza sporcare il branch.

## 3. Reviewer read-only permanente
Un reviewer senza Edit riduce rischio e bias.

## 4. Prompt injection hunter
Un agente dedicato legge README, script, template e fixture cercando istruzioni malevole.

## 5. MCP allowlist nominale
Autorizzare `mcp__server__tool`, non l’intero server.

## 6. Branch guard
Hook che blocca modifiche su main/master.

## 7. Diff budget
Hook che segnala PR troppo grandi.

## 8. ADR automatico
Ogni decisione architetturale genera un ADR.

## 9. Confluence writer
Trasforma diff e ADR in pagina pronta per knowledge base.

## 10. Incident timeline
Da log e commit costruisce cronologia incidente.

## 11. Dependency risk radar
Controlla librerie abbandonate, licenze e versioni fuori standard.

## 12. License gate
Hook che avvisa se vengono introdotti file/codice con licenza non chiara.

## 13. SQL read-only lab
Hook che permette solo SELECT durante esercitazioni.

## 14. No binary edit
Blocca modifiche accidentali a zip, jar, pdf, immagini.

## 15. Large file guard
Evita commit di file enormi.

## 16. PR narrator
Scrive commento PR con cosa cambia, test, rischi, rollback.

## 17. Test gap finder
Individua classi modificate senza test corrispondenti.

## 18. Observability reviewer
Verifica correlation id, logging e metriche.

## 19. Release dry-run
Simula release notes e checklist senza taggare.

## 20. Runbook generator
Produce passi operativi e troubleshooting da codice/config.

## 21. Learning mentor
Spiega ai junior una classe o un modulo con esercizi.

## 22. Legacy strangler planner
Propone piano di migrazione incrementale.

## 23. Hotspot mapper
Combina git log e complessità per trovare zone calde.

## 24. Ticket acceptance writer
Trasforma codice/diff in criteri di accettazione.

## 25. Security exception register
Registra eccezioni motivate e scadenza.

## 26. Policy as code explainer
Spiega a sviluppatori perché un hook blocca.

## 27. Safe bash classifier
Classifica comando Bash prima di eseguirlo.

## 28. Network egress guard
Blocca curl/wget verso domini non allowlist.

## 29. Data classification reminder
Se vede dati personali, chiede trattamento appropriato.

## 30. Config drift detector
Confronta config ambiente con template.

## 31. Pipeline failure analyst
Legge log CI e suggerisce fix.

## 32. Flaky test analyst
Trova pattern di test instabili.

## 33. Commit message coach
Suggerisce conventional commit basato sul diff.

## 34. Semantic changelog
Raggruppa modifiche per impatto utente.

## 35. OpenAPI consistency checker
Confronta controller, DTO e documentazione.

## 36. Migration rollback checker
Verifica script rollback DB.

## 37. Cache correctness reviewer
Controlla invalidazione cache.

## 38. Concurrency reviewer
Cerca shared mutable state e race condition.

## 39. Performance budget
Segnala query/cicli/chiamate remote rischiose.

## 40. Accessibility reviewer
Per frontend controlla aria, keyboard, contrasto concettuale.

## 41. Secure logging reviewer
Blocca log di password/token/PII.

## 42. Environment variable catalog
Documenta env richieste e default.

## 43. Local onboarding bot
Genera istruzioni setup dal repository.

## 44. Architecture diagrammer
Produce Mermaid da codice reale.

## 45. Module owner suggester
Suggerisce ownership da cronologia commit.

## 46. Risk-based review
Ordina finding per probabilità/impatto.

## 47. Definition of Done bot
Verifica DoD prima di PR.

## 48. Backlog refiner
Spezza epic tecnica in task piccoli.

## 49. Meeting prep
Prepara sintesi tecnica per standup/community.

## 50. Retrospective bot
Da audit log suggerisce miglioramenti workflow.
