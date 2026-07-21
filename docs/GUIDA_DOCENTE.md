# Guida docente

## Tono del corso
Il corso deve sembrare una dimostrazione di lavoro reale, non una rassegna di funzionalità.

## Ritmo consigliato
- Ogni concetto deve essere seguito da una micro-demo.
- Ogni demo deve partire da un problema concreto: PR troppo grande, test mancanti, README obsoleto, secret nei file, release notes manuali.
- Evitare demo fragili: preparare sempre output atteso e fallback testuale.

## Frasi chiave
- "Un agente non è più intelligente perché ha più tool: è più sicuro quando ha solo i tool necessari."
- "La `description` decide quando l'agente viene richiamato; il prompt decide come lavora."
- "Gli hook sono determinismo attorno a un sistema probabilistico."
- "La sicurezza agentica non è bloccare tutto: è rendere sicure le azioni ripetitive."

## Demo fallback
Se Claude Code non è disponibile in aula:
1. aprire gli agenti in `agents/`;
2. mostrare la configurazione `.claude/settings.json`;
3. eseguire gli script hook manualmente con input JSON simulato;
4. usare gli esempi in `examples/` per ragionare sul workflow.
