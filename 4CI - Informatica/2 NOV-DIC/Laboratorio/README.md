**IMPORTANTE: FILE IN SCRITTURA! Da rivedere**
# 🛠️ Officina Python - 4CI, novembre-dicembre

Come si lavora in laboratorio. <u>Non è una dispensa: è il manuale della stanza.</u>

Le dispense del bimestre stanno nella cartella sopra: [2 NOV-DIC](../). Qui c'è solo che cosa fare, in che ordine, e come sapere se hai finito.

## 🕐 Le due ore e l'ora

Le ore di laboratorio sono **due di fila più una in un altro giorno**.

| Blocco | Che cosa succede | Chi comanda |
| --- | --- | --- |
| **2 ore** | Missione. Si scrive codice, a coppie. | il computer |
| **1 ora** | Officina: demo, retrospettiva, caccia ai bug, recupero. | la classe |
- [ ] #ai no. Due ore per applicare e scrivere codice a coppie. L'altra ora, quella extra, facciamo solo teoria o Q&A

Le due ore non si interrompono ogni dieci minuti. Se hai una domanda, prima guarda il semaforo.

## 🚦 Il semaforo

Sul bordo del tavolo (o nella lavagna condivisa), sempre visibile:

| Colore | Significato | Che cosa fai |
| --- | --- | --- |
| 🟢 verde | sto andando | continua |
| 🟡 giallo | ho una domanda ma posso continuare | **scrivi la domanda in `diario.md`** e vai avanti su un'altra parte |
| 🔴 rosso | sono fermo e non so come uscirne | metti il rosso. Il docente passa dai rossi per primi. |

<u>Il giallo esiste per non fermare il lavoro: scrivi la domanda e la fai dopo.</u>

## 📋 La bacheca delle missioni

Ogni missione è un lavoro chiuso, con il suo file di partenza e i suoi test. La bacheca è [Missioni - bacheca](Missioni%20-%20bacheca.md): si aggiorna a fine ora, non durante.

- [ ] #ai da rivedere, questa idea, vorrei rivederla io. Prima testo l'idea "liberi, ognuno scrive codice giocando su ciò che preferisce"

## ✅ Come si esegue un test

<u>Si esegue dentro la cartella della missione</u>, non in `Laboratorio`.

```text
python -m pytest -q
```

⚠️ Se lanci `pytest` dalla cartella `Laboratorio`, esegue **tutte** le missioni insieme e vedrai una valanga di rossi: sono quelli delle missioni che non hai ancora fatto. Non è un errore. Il comando giusto è sempre dentro la cartella della tua missione.

La prima volta, se pytest non c'è:

```text
python -m pip install pytest
```

Oppure, dalla cartella `Laboratorio`, con la lista della spesa già pronta:

```text
python -m pip install -r requirements.txt
```

La risposta si legge così:

```text
......                                              [100%]
6 passed in 0.02s
```

- **6 passed**: la missione è finita, per quei test.
- **5 failed, 1 passed**: cinque cose non tornano, una sì. Non è un voto: è una lista di cose da fare.
- **1 failed più una riga rossa con `E`**: leggi quella riga. Dice **che cosa** si aspettava e **che cosa** ha trovato.

<u>Non si tocca `test_*.py`.</u> Se un test ti sembra sbagliato, non è sbagliato: è il contratto. Lo segnali al docente.

## 🧭 Quando sei bloccato: quattro passi, in quest'ordine

1. **Leggi il messaggio d'errore dal basso.** L'ultima riga dice *che cosa*; quelle sopra dicono *dove*.
2. **Guarda `test_*.py`.** Dice esattamente il risultato atteso. Non è un segreto, è la specifica.
3. **Riduci.** Prova la funzione nel REPL con i valori del test: `>>> meta_forza(7)`.
4. **Poi** metti il giallo e scrivi la domanda nel diario.

Domanda utile: «mi aspettavo X, ho ottenuto Y, ho provato Z». Domanda inutile: «non funziona».

## 📓 Il diario

In ogni repository c'è `diario.md`, compilato **a fine ora**, cinque righe al massimo:

```text
## 12 novembre
Fatto: saluta() e scheda()
Non ho capito: perché meta_forza(8) dà 4.0 e non 4
Da riprovare: il test di tipo()
```

Non si scrive per il docente. Si scrive perché <u>fra una settimana non ti ricorderai dove ti eri fermato</u>.

## 🔁 Il rituale della demo

Nell'ora singola, ogni coppia ha **due minuti**:

1. mostra **una sola cosa** che ora funziona (non tutto);
2. dichiara **un bug aperto** o un limite;
3. dice **una cosa** che ha scoperto.

Dire «questa parte non è pronta» vale più che nasconderla.

## 🤝 Le regole del codice condiviso

- Il repository è di tutti e due. Nessuno dice «non toccare, l'ho fatto io».
- Si committa spesso, con messaggi che si capiscono fra un mese.
- Chi non ha scritto una funzione deve saperla spiegare. Se non ci riesci, non è finita.
- Nel dubbio, si esegue: un test vale più di un'opinione.

## 🧯 Da fare e da non fare

| ✅ | ❌ |
| --- | --- |
| eseguire i test ogni pochi minuti | scrivere tutto e testare alla fine |
| copiare dal `test_*.py` il valore atteso | indovinare i valori |
| chiedere «perché» | chiedere «me lo fai tu» |
| un commit a ogni test verde | un commit alla fine delle due ore |
| leggere il traceback | cancellare il codice e riscrivere a caso |

## 🆘 Se perdi il lavoro

I test e le missioni sono pubblici: li ritrovi qui. Il tuo lavoro sta nel tuo repository, che è **privato** e ha una cronologia. Se hai committato spesso, non hai perso niente: `git log` e torni indietro.

---

🏠 [Dispense Novembre-Dicembre](../../README.md) · 📋 [Bacheca delle missioni](Missioni%20-%20bacheca.md)