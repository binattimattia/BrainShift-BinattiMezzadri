# Devlog — Brain Shift

> Diario di bordo del gruppo Binatti-Mezzadri. 

### Settimana 1 (22-28 aprile 2026)

Questa prima settimana ci siamo dedicati al setup iniziale del progetto e alla definizione della logica di base del gioco, senza ancora toccare la grafica.
Come prima cosa, abbiamo inizializzato la struttura del repository.
Successivamente, ci siamo concentrati sulle regole core: abbiamo implementato i controlli per verificare se un numero è pari o se una lettera è una vocale, oltre alla logica per determinare quale debba essere la risposta attesa.
Per organizzare meglio le informazioni, abbiamo preso la decisione di introdurre una dataclass `Trial`, che ci aiuterà a rappresentare in modo pulito i dati generati e le risposte dell'utente. Insieme a questo, abbiamo scritto la funzione `generate_trial()` per creare test casuali combinando posizione (TOP/BOTTOM), lettera e numero.
Abbiamo speso un po' di tempo a fare refactoring iniziale: abbiamo sistemato la gestione degli errori e rinominato le funzioni di calcolo per renderle più descrittive. Voler avere una base solida fin da subito ci ha rallentato leggermente, ma ci eviterà problemi futuri.
Abbiamo imparato quanto le dataclass in Python rendano il codice più leggibile quando si devono manipolare strutture dati ricorrenti.
Per la settimana prossima, pianifichiamo di espandere le meccaniche di gioco e iniziare a lavorare sull'interfaccia grafica.

### Settimana 2 (29 aprile - 5 maggio 2026)

Questa settimana ci siamo concentrati sull'implementazione delle meccaniche core del gioco e sull'avvio della parte grafica.
Per prima cosa, abbiamo scritto la logica di calcolo dei punteggi tramite la funzione `apply_answer()`, che valuta la correttezza delle risposte date.
Successivamente, ci siamo buttati su Pygame: abbiamo inizializzato l'applicazione, configurato lo schermo e impostato la gestione base degli eventi. Capire come impostare correttamente il game loop principale ci ha fatto perdere un po' di tempo iniziale.
Una volta pronto il setup, abbiamo implementato la generazione dei trial e il rendering dell'UI per poter finalmente visualizzare le carte a schermo. Abbiamo deciso di cercare di mantenere la logica di generazione separata da quella di disegno vero e proprio.
Abbiamo imparato molto su come Pygame gestisce i draw e le interazioni.
Per la settimana prossima, pianifichiamo di completare le meccaniche di interazione per le risposte dell'utente, gestire i feedback di fine turno e chiudere il ciclo completo di una partita.


### Settimana 3 (6-12 maggio 2026)

Questa terza settimana ci siamo dedicati in modo particolare al refactoring e a migliorare l'integrazione tra la grafica e il sistema di input.
Per prima cosa, abbiamo sistemato il rendering della UI, facendo in modo di disegnare correttamente i trial con la lettera e il numero direttamente sopra gli elementi grafici delle carte. Capire come posizionare e centrare i testi con precisione all'interno delle figure geometriche ha richiesto un bel po' di tentativi e piccoli aggiustamenti manuali che ci hanno fatto perdere un po' di tempo.
L'altra grande parte del lavoro è stata l'ottimizzazione del game loop principale. Abbiamo snellito e riorganizzato la gestione dei trial in corso e il modo in cui vengono processati gli input del giocatore dalla tastiera. 
Abbiamo preso la decisione di centralizzare e pulire questa gestione per evitare comportamenti imprevisti durante il gioco. Questo lavoro ci ha fatto capire quanto sia cruciale separare nettamente l'aggiornamento dello stato logico dal momento in cui Pygame ridisegna lo schermo.
Per la prossima settimana puntiamo a completare l'esperienza aggiungendo il timer globale, la schermata dei risultati, gli ultimi feedback visivi e qualche obiettivo avanzato.

### Settimana finale (13-17 maggio 2026)

Questa settimana, essendo l'ultima, ci siamo dedicati a chiudere il ciclo di gioco, aggiungere i feedback visivi e sistemare la documentazione.
Abbiamo implementato il timer globale della partita e la schermata finale dei risultati, introducendo anche la funzionalità di reset per poter avviare una nuova partita senza dover riavviare il programma.
Un aspetto che ci ha fatto perdere un po' di tempo è stato il sistema di feedback visivo: abbiamo aggiunto un feedback con colori per i risultati dei trial e un delay sull'input. Gestire correttamente queste tempistiche e il delay all'interno del game loop di Pygame, senza bloccare la ricezione di altri eventi, ha richiesto diverse prove.
Infine, abbiamo preso la decisione di dedicare gli ultimi sforzi alla pulizia generale: abbiamo aggiornato i layout della UI, aggiunto i docstrings ai metodi helper per migliorare la leggibilità del codice e steso la documentazione finale.

## Bilancio finale

Arrivati alla fine di questo progetto, siamo molto soddisfatti del risultato ottenuto, in particolar modo per la solidità della logica che abbiamo costruito.
Uno degli aspetti più importanti che portiamo a casa da questa esperienza è l'aver compreso a fondo come funzionano e come si manipolano i rettangoli `pygame.Rect` in Pygame. All'inizio il posizionamento degli elementi e l'ancoraggio ci sembravano complessi, ma una volta padroneggiati si sono rivelati lo strumento migliore per gestire l'intera UI.

Abbiamo anche imparato moltissimo sul lavoro di squadra. Abbiamo capito fin da subito come suddividerci bene i compiti: la divisione è stata bilanciata ed efficiente. Aver rispettato i reciproci spazi e limiti ci ha permesso di procedere senza conflitti, unendo le forze per risolvere i bug più ostici senza calpestare il lavoro dell'altro.

La parte che invece abbiamo decisamente sottovalutato all'inizio è stata la gestione del controller all'interno del loop `main()`. Ci è capitato svariate volte che il programma si rompesse o non si avviasse semplicemente a causa di if annidati in modo scorretto o problemi di indentazione nel ciclo degli eventi.

Se avessimo avuto a disposizione un'altra settimana di tempo ci saremmo probabilmente dedicati a implementare molti più obiettivi avanzati, arrivando anche ad avere gli effetti sonori.

In conclusione, se dovessimo assegnare un voto al nostro progetto, ci daremmo un **7.5**.
Riteniamo che questa valutazione sia onesta e giustificata: la logica di base è robusta e funzionante, abbiamo imparato le meccaniche di Pygame e, soprattutto, abbiamo dimostrato di saper lavorare in team in modo davvero equilibrato e produttivo.
