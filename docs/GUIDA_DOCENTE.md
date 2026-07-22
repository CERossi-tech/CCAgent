# Guida docente

## Tono del corso
Il corso deve sembrare una dimostrazione di lavoro reale, non una rassegna di funzionalità. Ogni concetto nasce da un problema che l'aula riconosce: PR troppo grandi, test mancanti, README obsoleto, secret nei file, release notes manuali.

## Prima del corso (checklist docente)
- [ ] Repo del kit clonato e testato sulla macchina di aula; branch `demo/` pronto.
- [ ] Claude Code funzionante offline dalle credenziali personali (account demo o di team).
- [ ] `.claude/` demo preconfigurato con java-reviewer + hook block-bash + audit, già collaudato.
- [ ] Output attesi delle demo salvati come fallback testuale in `demo-fallback/` locale.
- [ ] `docs/SPEECH_SLIDES.md` riletto: contiene lo speech e i punti di demo per ogni slide.
- [ ] Timer visibile; foglio "parking lot" per le domande deep-dive.

## Ritmo consigliato
- Ogni concetto è seguito da una micro-demo (le demo dal vivo sono marcate nello speech alle slide 7, 15, e nei lab).
- Ogni demo parte da un problema concreto, mai da "guardate questa feature".
- Evitare demo fragili: preparare sempre output atteso e fallback testuale.
- Sicurezza (slide 22–29): rallentare. È il blocco dove si gioca l'adozione aziendale; le domande qui vanno accolte, non parcheggiate.

## Gestione dei laboratori in aula
- In 180 minuti si completano dal vivo Lab 1 e Lab 2; il Lab 3 si avvia insieme e si lascia proseguire.
- Formare coppie: un "driver" e un "security officer" che controlla diff e log.
- Giro d'aula durante i lab con tre domande fisse: "quali tool ha il tuo agente?", "cosa c'è nell'audit log?", "il diff lo capiresti tra un mese?".
- Errori comuni da intercettare: description generiche (agente mai invocato), hook registrato ma non eseguibile (permessi file), lavoro su main invece che sul branch di lab.

## Frasi chiave
- "Un agente non è più intelligente perché ha più tool: è più sicuro quando ha solo i tool necessari."
- "La `description` decide quando l'agente viene richiamato; il prompt decide come lavora."
- "Gli hook sono determinismo attorno a un sistema probabilistico."
- "La sicurezza agentica non è bloccare tutto: è rendere sicure le azioni ripetitive."
- "Chi scrive non si autovaluta."

## Demo fallback
Se Claude Code non è disponibile in aula:
1. aprire gli agenti in `agents/` e leggerli come "job description";
2. mostrare la configurazione `.claude/settings.json` commentata (`docs/SETTINGS_EXPLAINED.md`);
3. eseguire gli script hook manualmente con input JSON simulato (il Lab 2 lo prevede comunque);
4. usare gli esempi in `examples/` per una review "umana con checklist" usando le skill come guida;
5. proiettare gli output attesi salvati in `demo-fallback/`.

## Valutazione e chiusura
- Criterio di successo del corso: ogni partecipante esce con il Lab 6 impostato sul PROPRIO caso.
- Ultimi 5 minuti: impegno esplicito individuale ("entro questa settimana: repo non critico, agente read-only, hook audit").
- Follow-up consigliato a 2 settimane: retrospettiva sui primi pattern adottati.
