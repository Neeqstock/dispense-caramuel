[🛠️ Officina](README.md) · [🏠 Dispense](../../README.md)

# 📋 Bacheca delle missioni

**4CI · Novembre-Dicembre · Laboratorio**

Ogni riga è una missione chiusa: un file di partenza, un contratto di test, un risultato. <u>Non si apre la successiva prima di aver chiuso la precedente</u>, salvo il 🔍.

La classe non va avanti tutta insieme: chi finisce prima prende dalla colonna 🔍 della stessa missione. Così nessuno ha una pista diversa, solo un pezzo in più.

> **Stato** (lo aggiorna il docente): ⬜ da fare · 🟨 in corso · 🟥 bloccata · ✅ fatta

---

## 🦸 S1 - L'eroe

📁 [S1 - L'eroe](S1%20-%20L%27eroe/) · 📄 `eroe.py` · 🧪 `test_eroe.py` (6 test)

**Obiettivo.** Il primo personaggio del dungeon: chiede i dati, li controlla, stampa una scheda.

| # | Che cosa deve funzionare | Dispensa |
| --- | --- | --- |
| 1 | `saluta(nome)` restituisce un saluto con il nome dentro | [S1](../%28STU%29%204CI%20nov-dic%20S1%20-%20Primi%20passi%20con%20Python.md) |
| 2 | `scheda()` mette insieme testo e numeri in una riga sola | f-string |
| 3 | `meta_forza()` e `meta_forza_intera()`: `/` e `//` | operatori |
| 4 | `leggi_vita()` trasforma quello che arriva da `input` in un numero | tipi |
| 5 | `tipo()` dice di che tipo è un valore | `type()` |

**🔍 In più, per chi ha finito.** Aggiungi una funzione `scheda_lunga()` che restituisce tre righe (nome, vita, forza) usando un solo testo con `\n`. Poi rompi apposta il programma in tre modi diversi e scrivi nel diario, per ognuno, **la riga del traceback che spiega il perché**.

---

## 🎲 S2 - Il dado e il combattimento

📁 [S2 - Il dado e il combattimento](S2%20-%20Il%20dado%20e%20il%20combattimento/) · 📄 `combattimento.py` · 🧪 `test_combattimento.py` (9 test)

**Obiettivo.** La fortuna entra nel gioco: un dado, un ciclo, e nessuno scende sotto zero.

| # | Che cosa deve funzionare | Dispensa |
| --- | --- | --- |
| 1 | `tira_dado()` restituisce un numero nell'intervallo, usando `random` | [S2](../%28STU%29%204CI%20nov-dic%20S2%20-%20Decisioni%2C%20cicli%20e%20funzioni.md) |
| 2 | `subisci_danno()` non scende sotto zero | `max` |
| 3 | `cura()` non supera la vita massima | `min` |
| 4 | `e_vivo()` risponde vero o falso | `bool` |
| 5 | `combatti()` fa i turni finché uno cade | `while` |
| 6 | `conta_vittorie()` ripete il combattimento sui mostri | `for` |

**🔍 In più.** Apri il **debugger** su `combatti()` e fermati dentro il `while`: osserva `vita` del mostro a ogni giro. Poi scrivi nel diario, con parole tue, che differenza c'è fra `print` e `return` in questa funzione.

---

## 🎒 S3 - Zaino e mappa

📁 [S3 - Zaino e mappa](S3%20-%20Zaino%20e%20mappa/) · 📄 `zaino_mappa.py` · 🧪 `test_zaino_mappa.py` (12 test)

**Obiettivo.** Tante cose con un nome solo: la lista per lo zaino, la lista di liste per la mappa.

| # | Che cosa deve funzionare | Dispensa |
| --- | --- | --- |
| 1 | creare una lista vuota e aggiungere in fondo | [S3](../%28STU%29%204CI%20nov-dic%20S3%20-%20Liste%20e%20matrici.md) |
| 2 | togliere un oggetto, contare, sapere se c'è | `remove`, `len`, `in` |
| 3 | sommare i valori, anche con la lista vuota | `sum` |
| 4 | **copiare** una lista e non creare un secondo nome per la stessa | aliasing |
| 5 | costruire una matrice in cui le righe sono indipendenti | cicli annidati |
| 6 | mettere un simbolo, trovarlo, contarlo | riga e colonna |

**🔍 In più.** Due prove da fare e una domanda da rispondere nel diario.
- Prova `mappa = [["."] * 3] * 3` e modifica una cella: quante celle cambiano? Perché?
- Prova `riga = ["."] * 3` in due celle diverse: funziona?

<u>Qui c'è il bug più famoso di Python: se non lo scopri da solo, la mappa del dungeon resterà storta.</u>

---

## 📇 S4 - Scheda e bestiario

📁 [S4 - Scheda e bestiario](S4%20-%20Scheda%20e%20bestiario/) · 📄 `bestiario.py` · 🧪 `test_bestiario.py` (9 test)

**Obiettivo.** Trovare un dato dal suo nome invece che dalla sua posizione.

| # | Che cosa deve funzionare | Dispensa |
| --- | --- | --- |
| 1 | creare una scheda con quattro chiavi | [S4](../%28STU%29%204CI%20nov-dic%20S4%20-%20Dizionari.md) |
| 2 | leggere una chiave che c'è e una che non c'è | `get` |
| 3 | scrivere una chiave nuova e aumentarne una esistente | `[]` |
| 4 | elencare le chiavi | `keys` |
| 5 | cercare un mostro per nome in una lista di dizionari | `for` |
| 6 | costruire una rubrica nome → mostro | comprensione |

**🔍 In più.** Nel diario, rispondi in due righe: per la **mappa** del dungeon useresti una lista di liste o un dizionario? Per il **bestiario**? Motiva con un caso concreto. Non esiste una risposta sola: conta il motivo.

---

## 🏰 S5 - Il gioco intero

📁 [S5 - Il gioco intero](S5%20-%20Il%20gioco%20intero/) · 📄 `gioco.py` · 🧪 `test_gioco.py` (10 test)

**Obiettivo.** Montare i pezzi in un programma che si usa, con un menu e un ciclo principale.

| # | Che cosa deve funzionare | Dispensa |
| --- | --- | --- |
| 1 | creare eroe e bestiario | [S5](../%28STU%29%204CI%20nov-dic%20S5%20-%20Progettare%20un%20programma.md) |
| 2 | danno e cura con i limiti | riuso |
| 3 | mostrare la scheda | f-string |
| 4 | togliere il primo mostro dalla lista | `pop` |
| 5 | un turno di combattimento con il dado già tirato | funzioni |
| 6 | bere una pozione | zaino |
| 7 | il ciclo principale, con i comandi e la fine | progetto |

<u>Questo è il test più difficile del bimestre, e non è un caso: è il primo programma che ha una forma.</u> Se ti blocchi su `gioca()`, guarda come i test simulano `input` e `print`: il gioco non deve leggere la tastiera davvero per essere provato. Questo si chiama *testabile*.

**🔍 In più.** Aggiungi tu un comando `"4"` che stampa i mostri rimasti, e un test tuo. Poi refactor: se `gioca()` supera le 40 righe, estrai una funzione `turno_combattimento()`.

---

## 🐞 S6 - Bug bounty (ora singola)

Non c'è un file: si lavora sui repository delle altre coppie.

| Regola | Dettaglio |
| --- | --- |
| Chi cerca | ogni coppia riceve un repository di un'altra coppia |
| Cosa si cerca | un caso che i test non coprono e che rompe il programma |
| Come si segnala | una issue con: comando eseguito, risultato atteso, risultato ottenuto |
| Punteggio | 1 per bug vero, **2** se quel bug lo trova un altro nel tuo codice |
| Cosa non vale | «il nome della variabile è brutto» (quello va in revisione, non nel bounty) |

<u>Il codice degli altri non si modifica: si legge e si segnala.</u> Chi trova un bug lo spiega, chi lo ha scritto lo chiude. Entrambi hanno imparato qualcosa.

---

## 📅 Il calendario delle sette settimane

| Sett. | 2 ore | 1 ora |
| --- | --- | --- |
| 1 | S1 | S1 🔍 + demo + diario |
| 2 | S2 | S2 🔍 + debugger |
| 3 | S3 | S3 🔍 + il bug della matrice |
| 4 | S4 | revisione fra coppie |
| 5 | S5 | retrospettiva del progetto |
| 6 | rifinitura + recupero | **bug bounty** |
| 7 | verifica | — |

---

[🏠 Dispense](../../README.md) · [🛠️ Come si lavora](README.md)