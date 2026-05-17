# Documentazione delle Scelte Progettuali

## Struttura del progetto

* **Scelta:** Dividere il progetto in moduli (`main.py`, `ui.py`, `generator.py`, `scoring.py`, `rules.py`, `models.py`, `config.py`).

* **Perché:** Più facile capire, testare e modificare singole parti; `rules.py` è logica pura, `ui.py` solo rendering.

* **Alternative considerate:** Nessuna alternativa considerata.

* **Conseguenze:** Nessuna.

## Scoring

* **Scelta:** Funzione pura `apply_answer(score, is_correct) -> new_score` in `scoring.py`.

* **Perché:** Semplicità, testabilità e nessun effetto collaterale.

* **Alternative considerate:** Dataclass mutabile per lo stato del punteggio. Scartata per non introdurre complessità.

* **Conseguenze:** Facilità di test; leggero overhead nel passare il punteggio.

## Generatore

* **Scelta:** Usare `random.Random(SEED)` passato a `generate_trial(rng)`; generazione con `rng.choice`/`rng.randint`, senza bilanciamento attivo.

* **Perché:** Riproducibilità e codice semplice.

* **Alternative considerate:** Rigenerare trials sbilanciati o post-processare la lista per bilanciarla. Scartata per semplicità e tempo.

* **Conseguenze:** Sessioni riproducibili; possibili sbilanciamenti casuali accettabili per la demo.

## Gestione del tempo

* **Scelta:** Usare `time.time()` per misurare elapsed e confrontarlo con `GAME_DURATION`.

* **Perché:** Semplice, preciso per il nostro caso e facile da testare fuori da Pygame.

* **Alternative considerate:** `pygame.time.get_ticks()` o misurare delta con `Clock.tick()`. Scartate per chiarezza.

* **Conseguenze:** Codice leggibile; test più semplice.

## Inter-trial interval

* **Scelta:** Variabile `feedback_until` con timestamp oltre il quale si accetta la prossima risposta.

* **Perché:** Evita `sleep()` e mantiene il main loop reattivo.

* **Alternative considerate:** Stato `PAUSED` o contatore di frame. Scartato per semplicità.

* **Conseguenze:** Implementazione non bloccante e leggibile; richiede gestire correttamente la variabile di stato.

## Input

* **Scelta:** Normalizzare l'input su valori booleani (freccia destra = True, sinistra = False) all'evento.

* **Perché:** Mappatura semantica semplice; resto del codice lavora su valori chiari.

* **Alternative considerate:** Un modulo `input_handler.py` per tradurre eventi. Scartato perché la mappatura è breve.

* **Conseguenze:** Codice lineare; se aggiungiamo altri input (touch/gamepad) servirà refactor.

## Feedback visivo

* **Scelta:** Colorare la carta (verde/rosso) per `FEEDBACK_DURATION` usando `last_answer_correct` + `feedback_until`.

* **Perché:** Semplice da implementare e non rallenta il loop.

* **Alternative considerate:** Animazioni frame-by-frame con interpolazione. Scartata per complessità/tempo.

* **Conseguenze:** Feedback reattivo; manca fluidità animata più sofisticata.

## Fading istruzioni

* **Scelta:** Fading progressivo dell'opacità (alpha blending) in base al numero di `correct_answers`. La funzione `draw_rules` in `ui.py` calcola il livello di alpha (255, 70%, 40%, 0%) tramite una superficie temporanea `SRCALPHA`.

* **Perché:** Migliora l'esperienza dell'utente e l'estetica, offrendo al giocatore una transizione morbida invece di un'improvvisa scomparsa del testo. Rende il progetto completo in un obiettivo avanzato richiesto dalla traccia.

* **Alternative considerate:** Un semplice interruttore on/off (`if correct_answers < 10`) utilizzato nella prima bozza. Scartato in favore di un effetto visivo migliore e completo.

* **Conseguenze:** Transizione più gradevole e professionale; l'utilizzo di una surface temporanea con `set_alpha` ha un costo di prestazioni impercettibile, ma giustificato per l'effetto richiesto.

## Cosa non siamo riusciti a fare e perché
* Abbiamo sacrificato la gestione di uno scoring con "meter" e moltiplicatori (obiettivo avanzato) preferendo invece un sistema di base più robusto e facile da debuggare per via delle tempistiche ristrette.