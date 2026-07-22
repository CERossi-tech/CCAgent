# Skill: Release Notes

## Scopo
Generare release notes accurate a partire da git history e diff reali, non dalla memoria.

## Quando usarla
- Preparazione di una release/tag.
- Changelog periodico (settimanale/sprint).

## Procedura
1. Determina il range: `ultimo-tag..HEAD` (o range richiesto).
2. Raccogli: `git log --oneline`, `git diff --stat`, PR/ticket collegati.
3. Classifica ogni cambiamento:
   - 🚨 **Breaking** — richiede azione di chi aggiorna.
   - ✨ **Feature** — nuova capacità.
   - 🐛 **Fix** — difetto risolto.
   - 🔒 **Security** — correzione di sicurezza (senza dettagli sfruttabili).
   - 🧹 **Internal** — refactoring, deps, CI (sezione collassata).
4. Riscrivi ogni voce per l'utente: cosa cambia *per chi usa il software*, non il titolo del commit.
5. Breaking changes: sempre con istruzioni di migrazione.

## Template
```markdown
# vX.Y.Z — YYYY-MM-DD

## 🚨 Breaking changes
- <cambio> — **Migrazione**: <passi>
## ✨ Novità
## 🐛 Fix
## 🔒 Sicurezza
<details><summary>🧹 Interni</summary>...</details>

**Full diff**: vA.B.C...vX.Y.Z • **Commit**: N • **Contributor**: ...
```

## Criteri di qualità
- Ogni voce collega commit/PR.
- Nessuna voce inventata: se non è nel diff, non esiste.
- Leggibile da un utente che non conosce il codice.

## Anti-pattern
- Copiare i messaggi di commit verbatim.
- Nascondere i breaking changes in fondo.
