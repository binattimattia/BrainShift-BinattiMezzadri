# Uso dell'IA nel progetto

## Strumenti usati

- Claude (modello: Sonnet 4.6)
- Gemini (modello: 3 Flash, 3.1 Pro)

## Uso granulare per modulo / parte

### Controller

**Dove**: `main.py`

**Cosa abbiamo chiesto**: Abbiamo notato che molte volte riscrivevamo le stesse parti di codice, soprattutto per quanto riguarda la gestione dei tasti freccia destra e sinistra. Perciò abbiamo chiesto all'IA di riscrivere in modo più ordinato e leggibile il controller, per migliorarne la manutenibilità.

**Cosa ci ha suggerito**: Ci ha suggerito di inserire più parametri nella stessa condizione (esempio: riga 46).

**Cosa abbiamo fatto**:
- Abbiamo accettato il suggerimento dopo aver compreso appieno il funzionamento del codice.

**Perché**: Il codice risultante era nettamente più compatto, ordinato e leggibile rispetto alla versione originale.

### Refactoring delle costanti (Applicazione generale)

**Dove**: `main.py`, `ui.py`, `generator.py`, `scoring.py`, `rules.py`, `models.py`, `config.py`

**Cosa abbiamo chiesto**: Abbiamo chiesto all'IA di verificare se fossero presenti "magic numbers" che potevano essere raggruppati in costanti. Questo riguardava in particolare la grafica (colori, dimensioni delle finestre) e i parametri di gioco (durata, punteggio, ecc.).

**Cosa ci ha suggerito**: Di estrarre questi valori e centralizzarli in costanti apposite.

**Cosa abbiamo fatto**:
- Abbiamo accettato la modifica dopo aver controllato attentamente che tutto fosse in ordine e corretto e che non alterasse il gioco.

**Perché**: Migliora in modo sostanziale la leggibilità e la manutenibilità del codice (ad esempio, per cambiare un colore basta modificare un solo valore).

## Cosa NON abbiamo chiesto all'IA

Ad eccezione del refactoring e della correzione formale menzionati sopra, la logica di business è stata scritta interamente da noi. In particolare, NON abbiamo fatto scrivere all'IA:

- Tutti i test (`pytest`)
- La documentazione di progetto (`docs/devlog.md`, `docs/scelte.md`, `docs/uso-ia.md`)
- `requirements.txt`
- La logica di generazione (`generator.py`)
- La logica dei punteggi (`scoring.py`)
- Le regole di gioco (`rules.py`)
- La struttura dei dati (`models.py`)
