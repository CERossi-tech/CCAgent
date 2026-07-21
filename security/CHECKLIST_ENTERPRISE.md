# Checklist Enterprise Claude Code

- [ ] Repository senza segreti reali.
- [ ] `.claude/settings.json` versionato solo per regole condivise.
- [ ] `.claude/settings.local.json` escluso da Git.
- [ ] Hook testati in sandbox.
- [ ] Tool MCP autorizzati nominalmente.
- [ ] Nessun server MCP sconosciuto.
- [ ] Log senza dati sensibili.
- [ ] Push e release sempre manuali.
- [ ] Subagent con tool minimi.
- [ ] Audit periodico con `/permissions` e `/hooks`.
