# Esempi vulnerabili didattici

Mini-progetti con difetti **intenzionali** per esercitare code review, sicurezza e refactoring. Non usare in produzione; non copiare pattern da qui.

## Contenuto
| Path | Stack | Usato nei lab | Difetti seminati (categorie) |
|---|---|---|---|
| `springboot/UserService.java` + `pom.xml` | Java / Spring Boot | Lab 1, Lab 3 | validazione input assente, gestione eccezioni, logging di dati sensibili, transazioni, null safety |
| `python/app.py` | Python | esercizi extra | injection, gestione errori, segreti hardcoded finti |
| `react/Profile.jsx` | React | esercizi frontend | hook mal usati, XSS potenziale, stato incoerente |

## Regole d'uso
- Lavorare sempre su un branch `lab/*`; mai su main.
- I "segreti" presenti sono finti e servono a far scattare i guard: non sostituirli con valori reali.
- Ogni difetto trovato va riportato con `file:riga` e severità: l'obiettivo è la review con evidenze, non la caccia al tesoro.
- Le soluzioni non sono incluse di proposito: il criterio di successo è nel README di ciascun lab.
