↩️ [Torna a S6 - Ripasso in flashcard](%28STU%29%204CI%20nov-dic%20S6%20-%20Ripasso%20in%20flashcard.md) · 🏠 [Indice](../README.md)

# ✏️ Eserciziario di Python

**4CI · Novembre-Dicembre · Eserciziario · Ripasso e casi**

⏱️ **Tempo: ✅ circa 50 minuti** (svolti e primi esercizi) · **🔍 altri 30 minuti** (per il voto alto) · **🤓 facoltativo.** Nessun compito obbligatorio a casa. Per ogni esercizio: prima prevedi, poi apri la soluzione.

> **Legenda:** 📜 caso reale · 🟢 svolto · 🎯 da provare · 📖 teoria · ✏️ pratica scritta · 📌 controllo · ⚠️ errore comune · 🧠 da ricordare · 🛠️ strumento · 🔧 lo faremo in laboratorio · ✅ da sapere · 🔍 per capire fino in fondo · 🤓 per curiosi · 🃏 soluzione: apri solo dopo aver provato.

Ogni caso parla di un problema vicino alla vita reale. Dati, nomi e scenari sono **inventati**, salvo i fatti dei 📜 che hanno una fonte in fondo. Gli esempi sono verificati eseguendoli con Python 3.12; funzionano anche con 3.10 o superiore.

---

## 1 · Ambiente e lettura degli errori

*Settimana S1 · ✅ 10 min · 🔍 5 min*

### 📜 Un errore è una risposta

Nel 1991 Guido van Rossum rilascia Python al CWI, un centro di ricerca di Amsterdam. Il nome non viene dal serpente, ma dai Monty Python. Il linguaggio ha una regola semplice: se qualcosa non va, la macchina ti dice **dove** e **perché**. Imparare a leggere quel messaggio vale quanto imparare la sintassi.

### 🟢 1.S · Leggere un traceback (📖 ✅)

**Consegna.** Il file `prova.py` si ferma con un errore. Trova la riga colpita e la causa.

```python
forza = "7"
danno = forza + 3
print(danno)
```

**Ragionamento.**
1. La prima riga crea `forza`, che punta al testo `"7"`.
2. La seconda riga prova a sommare un testo e un numero: non è un'operazione possibile.
3. Il traceback si legge **dal basso**: l'ultima riga dice *che cosa* è successo, le righe sopra dicono *dove*.

```text
Traceback (most recent call last):
  File "prova.py", line 2, in <module>
    danno = forza + 3
            ~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

📌 **Controllo.** La riga colpita è la 2, il tipo di errore è `TypeError`.

⚠️ **Errore comune.** Il messaggio non dice «hai sbagliato il gioco»: dice che un'operazione non ha senso per quei due valori.

🧠 <u>Leggi il traceback dal basso: l'ultima riga dice che cosa, quelle sopra dove.</u>

### 🎯 Da provare

**1.1 · ✅ · ✏️ · Di che famiglia è l'errore?** Per ogni riga di codice, scrivi se l'errore è di **sintassi**, di **esecuzione** o di **logica**. Per la terza, dì quale valore ottieni e quale dovresti ottenere.

```python
print("Ciao"
```

```python
print(10 / 0)
```

```python
media = 6 + 8 / 2
print(media)
```

<details>
<summary>🃏 <b>1.1 — Soluzione</b></summary>

- `print("Ciao"`: **sintassi**. La parentesi non è chiusa e Python non esegue nulla.
- `print(10 / 0)`: **esecuzione**. Il programma parte e si ferma su quella riga con `ZeroDivisionError`.
- `media = 6 + 8 / 2`: **logica**. Nessun messaggio: `print` mostra `10.0`, ma la media di 6 e 8 è `7.0`. Serve `media = (6 + 8) / 2`.

</details>

**1.2 · 🔍 · ✏️ · Correggi senza toccare la prima riga.** Nel file dell'esempio, cambia solo la seconda riga in modo che il programma stampi `10`. Il valore di `forza` deve restare `"7"`.

<details>
<summary>🃏 <b>1.2 — Soluzione</b></summary>

```python
forza = "7"
danno = int(forza) + 3
print(danno)
```

Output: `10`. `int(forza)` trasforma il testo `"7"` nel numero 7 prima della somma.

</details>

---

## 2 · Variabili, tipi, input e operatori

*Settimana S1 · ✅ 15 min · 🔍 10 min*

### 📜 Il 22 per cento

Dal 1° ottobre 2013 l'aliquota IVA ordinaria in Italia è il 22%. Chi compra un articolo al netto vede sul conto il prezzo **con** IVA: il calcolo è una moltiplicazione con un fattore. Lo fanno ogni giorno i registratori di cassa e i gestionali. Conferma l'aliquota sul sito dell'Agenzia delle Entrate.

### 🟢 2.S · Calcolare il prezzo lordo (✅ · ✏️)

**Consegna.** Un articolo costa 40,00 € al netto. Calcola il prezzo con IVA al 22%.

```python
prezzo_netto = 40.0
iva = 22
prezzo_lordo = prezzo_netto * (1 + iva / 100)
print("Prezzo con IVA:", prezzo_lordo)
```

**Ragionamento.**
1. Ogni nome è una freccia che punta a un valore: `prezzo_netto` punta a `40.0`, `iva` a `22`.
2. `iva / 100` dà un numero con la virgola (`float`), anche se `22` è un intero: `/` restituisce sempre un `float`.
3. `1 + 0.22` diventa il fattore `1.22`; moltiplicando per 40 si ottiene il lordo.

```text
Prezzo con IVA: 48.8
```

📌 **Controllo.** Il lordo è più alto del netto di circa il 22%: 40 + 8,80 = 48,80.

⚠️ **Errore comune.** Se scrivi `iva = "22"` con le virgolette, `iva / 100` dà `TypeError`: `"22"` è testo, non un numero.

🧠 <u>In Python il tipo appartiene al valore, non alla variabile.</u>

### 🎯 Da provare

**2.1 · ✅ · ✏️ · Prevedi prima di eseguire.**

```python
print(7 / 2, 7 // 2, 7 % 2, 2 ** 3)
print("3" + "4")
print(int("3") + 4)
```

<details>
<summary>🃏 <b>2.1 — Soluzione</b></summary>

```text
3.5 3 1 8
34
7
```

`/` divide con la virgola, `//` tiene solo la parte intera, `%` dà il resto, `**` è la potenza. Con due testi, `+` li unisce (`"34"`); con `int(...)` il testo diventa un numero.

</details>

**2.3 · ✅ · 📖 · Che tipo è?** Completa la tabella con il tipo di ciascun valore, scrivendo `int`, `float`, `str` o `bool`: `5`, `"5"`, `7.0`, `True`. Poi spiega in una frase che cosa cambia fra `5` e `"5"`.

<details>
<summary>🃏 <b>2.3 — Soluzione</b></summary>

`5` è `int`, `"5"` è `str`, `7.0` è `float`, `True` è `bool`. Il numero `5` si può sommare a `2`; il testo `"5"` no, perché il tipo appartiene al valore, e le virgolette lo rendono testo. Con `type(valore)` lo verifichi nel REPL.

</details>

**2.2 · 🔍 · ✏️ · Scrivi il programma dello scontrino.** Il programma chiede il prezzo netto (`input`), calcola il lordo con IVA al 22% e stampa il risultato con due decimali, per esempio `Prezzo con IVA: 61.00 euro` se l'utente digita `50`.

<details>
<summary>🃏 <b>2.2 — Soluzione</b></summary>

```python
netto = float(input("Prezzo netto: "))
lordo = netto * (1 + 22 / 100)
print(f"Prezzo con IVA: {lordo:.2f} euro")
```

`input` restituisce sempre testo: `float(...)` lo trasforma in numero. La f-string `{lordo:.2f}` stampa due cifre decimali, come su uno scontrino. Con `50` l'output è `Prezzo con IVA: 61.00 euro`.

</details>

---

## 3 · Condizioni e cicli

*Settimana S2 · ✅ 15 min · 🔍 10 min*

### 📜 Centotrenta all'ora

Il limite generale di velocità in autostrada in Italia è 130 km/h (Codice della strada, art. 142: il dettaglio ha eccezioni, verificalo sul testo ufficiale). Un sensore che registra velocità deve contare quante volte il limite viene superato: è un ciclo con una condizione dentro. Per questo esempio i valori sono inventati.

### 🟢 3.S · Contare i superamenti (✅ · 📖)

**Consegna.** Una lista contiene cinque rilevazioni. Conta quante superano 130.

```python
velocita = [118, 135, 127, 142, 130]
superamenti = 0
for v in velocita:
    if v > 130:
        superamenti += 1
print("Superamenti:", superamenti)
```

**Ragionamento.**
1. `superamenti = 0` crea il contatore **prima** del ciclo.
2. Il `for` passa una rilevazione per volta: `v` vale 118, poi 135, poi 127, e così via.
3. `if v > 130` decide; solo dentro quel blocco il contatore sale di 1 (`+= 1`).

```text
Superamenti: 2
```

📌 **Controllo.** Superano 130 solo 135 e 142: sono due.

⚠️ **Errore comune.** Se `superamenti = 0` finisce **dentro** il `for`, il contatore torna a zero a ogni giro e il risultato è sempre 0 o 1. In Python è l'indentazione a decidere.

🧠 <u>Il contatore si crea prima del ciclo e si aggiorna dentro.</u>

### 🎯 Da provare

**3.1 · ✅ · ✏️ · Prevedi l'output di due cicli.**

```python
for i in range(3, 9, 2):
    print(i)

for n in range(1, 6):
    if n == 3:
        continue
    print(n)
```

<details>
<summary>🃏 <b>3.1 — Soluzione</b></summary>

```text
3
5
7
1
2
4
5
```

`range(3, 9, 2)` parte da 3, arriva prima di 9, salta di 2. Nel secondo ciclo `continue` salta il giro in cui `n` vale 3, ma il ciclo prosegue.

</details>

**3.2 · 🔍 · ✏️ · Quanti giorni?** Metti da parte 37 € al giorno. Con un `while`, calcola dopo quanti giorni il totale supera 1000 €, e quanto vale il totale. Stampa `Giorni: ..., totale: ...`.

<details>
<summary>🃏 <b>3.2 — Soluzione</b></summary>

```python
totale = 0
giorni = 0
while totale < 1000:
    totale += 37
    giorni += 1
print(f"Giorni: {giorni}, totale: {totale}")
```

Output: `Giorni: 28, totale: 1036`. Dopo 27 giorni il totale è 999, ancora sotto 1000: il `while` continua un giro in più.

</details>

---

## 4 · Funzioni e moduli

*Settimana S2 · ✅ 10 min · 🔍 15 min*

### 📜 Il termometro di Fahrenheit

Nel 1724 Daniel Gabriel Fahrenheit propone una scala di temperatura in cui l'acqua gela a 32 gradi e bolle a 212 (a pressione standard). Ancora oggi negli Stati Uniti molte persone leggono la temperatura in °F. Per convertire serve una formula: una funzione è il posto giusto dove metterla, così la si usa tutte le volte che serve.

### 🟢 4.S · Una funzione che restituisce (✅ · ✏️)

**Consegna.** Scrivi `celsius_a_fahrenheit` e stampa la conversione di 100 e di 0 gradi Celsius.

```python
def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32


print(celsius_a_fahrenheit(100))
print(celsius_a_fahrenheit(0))
```

**Ragionamento.**
1. `def` crea la funzione: il corpo non gira finché non la chiami.
2. `c` è il parametro: riceve il valore della chiamata (100, poi 0).
3. `return` consegna il risultato a chi ha chiamato, e la chiamata diventa un valore da stampare.

```text
212.0
32.0
```

📌 **Controllo.** La formula dà 32 per 0 e 212 per 100, come nella scala di Fahrenheit.

⚠️ **Errore comune: `print` non è `return`.** Osserva la differenza:

```python
def fahrenheit_stampato(c):
    print(c * 9 / 5 + 32)


x = fahrenheit_stampato(100)
print(x)
```

```text
212.0
None
```

La funzione stampa ma non consegna nulla: `x` vale `None`.

🧠 <u>`print` mostra il risultato, `return` lo consegna.</u>

### 🎯 Da provare

**4.1 · ✅ · ✏️ · Prevedi con il valore predefinito.**

```python
def somma(a, b=10):
    return a + b


print(somma(5))
print(somma(5, 1))
```

<details>
<summary>🃏 <b>4.1 — Soluzione</b></summary>

```text
15
6
```

Il parametro `b` ha un valore predefinito, 10. Nella prima chiamata non viene passato, quindi vale 10; nella seconda vale 1.

</details>

**4.2 · 🔍 · ✏️ · Area del cerchio.** Scrivi la funzione `area_cerchio(raggio)` che restituisce l'area, usando `math.pi` e `import math`. Stampa l'area per raggio 2, arrotondata a due decimali.

<details>
<summary>🃏 <b>4.2 — Soluzione</b></summary>

```python
import math


def area_cerchio(raggio):
    return math.pi * raggio ** 2


print(round(area_cerchio(2), 2))
```

```text
12.57
```

`raggio ** 2` è il quadrato. `round(..., 2)` arrotonda a due decimali.

</details>

**4.3 · 🔍 · 📖 · Dove vive la variabile?** Prevedi che cosa stampa il programma, poi spiega in una frase perché `x` fuori non cambia.

```python
x = 1


def cambia():
    x = 50
    return x


print(cambia(), x)
```

<details>
<summary>🃏 <b>4.3 — Soluzione</b></summary>

```text
50 1
```

Dentro `cambia` il nome `x` è una variabile **locale**: nasce nella funzione e muore con la chiamata. La `x` del programma principale non viene toccata. Per cambiarla servirebbe `global`, da evitare nei programmi semplici.

</details>

---

## 5 · Liste

*Settimana S3 · ✅ 15 min · 🔍 10 min*

### 📜 Lo scontrino del bar

Python ordina le liste con un algoritmo chiamato Timsort, ideato da Tim Peters nel 2002. Per noi basta una cosa: una lista è una fila di valori, e ci si lavora con pochi metodi (`append`, `len`, `sum`, `max`). I prezzi dello scontrino qui sotto sono inventati, ma il modo di sommarli è quello di un registratore di cassa.

### 🟢 5.S · Totale e massimo (✅ · ✏️)

**Consegna.** Lo scontrino ha tre articoli. Aggiungine un quarto da 0,80 €, poi stampa il numero di articoli, il totale e il prezzo più alto.

```python
scontrino = [2.5, 1.2, 4.0]
scontrino.append(0.8)
print(len(scontrino), sum(scontrino), max(scontrino))
```

**Ragionamento.**
1. Una lista si scrive fra quadre; `append` aggiunge in fondo.
2. `len` conta le caselle, `sum` somma tutti i valori, `max` trova il più alto.
3. Gli indici partono da zero: `scontrino[0]` è 2.5, `scontrino[-1]` è 0.8.

```text
4 8.5 4.0
```

📌 **Controllo.** Il totale è 2,50 + 1,20 + 4,00 + 0,80 = 8,50.

⚠️ **Errore comune.** `scontrino[4]` fallisce con `IndexError`: con quattro elementi gli indici validi vanno da 0 a 3.

🧠 <u>Gli indici partono da zero, e `-1` è sempre l'ultimo elemento.</u>

### 🎯 Da provare

**5.1 · 🔍 · ✏️ · Due nomi per la stessa lista.** Prevedi che cosa stampa il programma. Poi spiega in una frase perché la lista `a` cambia quando modifichi `b`.

```python
a = [1, 2, 3]
b = a
b.append(4)
c = a[:]
c.append(5)
print(a, b, c)
```

<details>
<summary>🃏 <b>5.1 — Soluzione</b></summary>

```text
[1, 2, 3, 4] [1, 2, 3, 4] [1, 2, 3, 4, 5]
```

`b = a` non copia la lista: fa puntare `b` allo stesso oggetto di `a`. Due frecce, una sola lista. `a[:]` crea invece una copia nuova, per questo `c` cambia senza toccare `a`.

</details>

**5.2 · ✅ · ✏️ · Solo i promossi.** Dati i voti `voti = [6, 4, 8, 5, 7]`, costruisci con un ciclo `for` e `append` la lista `promossi` che contiene solo i voti maggiori o uguali a 6, e stampala.

<details>
<summary>🃏 <b>5.2 — Soluzione</b></summary>

```python
voti = [6, 4, 8, 5, 7]
promossi = []
for voto in voti:
    if voto >= 6:
        promossi.append(voto)
print(promossi)
```

```text
[6, 8, 7]
```

`promossi` nasce vuota e cresce a ogni voto valido. Il ciclo scorre gli **elementi**, non gli indici.

</details>

**5.3 · ✅ · 📖 · Completa la frase.** Con `voti = [6, 4, 8, 5, 7]`: `voti[0]` vale ..., `voti[-2]` vale ..., e `voti[len(voti)]` causa un errore di tipo ...

<details>
<summary>🃏 <b>5.3 — Soluzione</b></summary>

`voti[0]` vale 6; `voti[-2]` vale 5; `voti[len(voti)]` causa `IndexError: list index out of range`. Con cinque elementi l'ultimo indice è 4, perché si parte da zero.

</details>

---

## 6 · Matrici

*Settimana S3 · ✅ 10 min · 🔍 10 min*

### 📜 Una foto è una tabella di numeri

Un'immagine Full HD ha 1920 colonne e 1080 righe di pixel: in tutto 1920 × 1080 = 2 073 600 pixel. Ogni pixel è un numero o una terna di numeri. L'immagine è quindi una **matrice**: una lista di righe, dove ogni riga è una lista di colonne. In Python le matrici si fanno con liste di liste, senza librerie esterne. Il valore 1920 × 1080 è un fatto standard della risoluzione Full HD.

### 🟢 6.S · Controllare la diagonale (✅ · ✏️)

**Consegna.** Una tabella 3×3 rappresenta un gioco del tris. Controlla se la diagonale principale contiene solo `X`.

```python
tabella = [
    ["X", "O", "X"],
    [" ", "X", "O"],
    [" ", " ", "X"],
]
vinto = True
for i in range(3):
    if tabella[i][i] != "X":
        vinto = False
print("Diagonale tutta X:", vinto)
```

**Ragionamento.**
1. `tabella` è una lista di tre righe; `tabella[i]` è la riga `i`.
2. `tabella[i][i]` prende la cella di riga `i` e colonna `i`: la diagonale.
3. Basta un valore diverso da `X` per cambiare `vinto` in `False`.

```text
Diagonale tutta X: True
```

📌 **Controllo.** Sulla diagonale ci sono `X`, `X`, `X`: il risultato è `True`.

⚠️ **Errore comune.** In Python `tabella[i][i]`, non `tabella[i, i]`: la sintassi con la virgola è di altri strumenti, come NumPy. Con le liste dà `TypeError`.

🧠 <u>In una matrice si scrive prima la riga, poi la colonna: `tabella[riga][colonna]`.</u>

### 🎯 Da provare

**6.1 · ✅ · 📖 · Righe e colonne.** Con la `tabella` dell'esempio, quanto valgono `len(tabella)`, `len(tabella[0])` e `tabella[1][2]`?

<details>
<summary>🃏 <b>6.1 — Soluzione</b></summary>

`len(tabella)` vale 3 (le righe), `len(tabella[0])` vale 3 (le colonne), `tabella[1][2]` vale `O`: riga 1 (la seconda), colonna 2 (la terza).

</details>

**6.2 · 🔍 · ✏️ · Conta le X.** Scrivi la funzione `conta_x(tabella)` che restituisce quante celle contengono `X`, usando due cicli `for` annidati. Applicala alla `tabella` dell'esempio.

<details>
<summary>🃏 <b>6.2 — Soluzione</b></summary>

```python
def conta_x(tabella):
    conteggio = 0
    for riga in tabella:
        for cella in riga:
            if cella == "X":
                conteggio += 1
    return conteggio


tabella = [
    ["X", "O", "X"],
    [" ", "X", "O"],
    [" ", " ", "X"],
]
print(conta_x(tabella))
```

```text
4
```

Il ciclo esterno scorre le righe, quello interno le celle di ogni riga. Le X sono 2 + 1 + 1 = 4.

</details>

---

## 7 · Dizionari

*Settimana S4 · ✅ 15 min · 🔍 15 min*

### 📜 Un nome, un indirizzo

Quando digiti il nome di un sito, un server DNS lo trasforma in un indirizzo IP, il numero che identifica la macchina sulla rete. In prima approssimazione è una tabella **chiave → valore**: al nome corrisponde un indirizzo. Gli indirizzi qui sotto appartengono ai blocchi riservati alla documentazione (RFC 5737, `192.0.2.0/24`) e i nomi usano il dominio riservato `.example`: sono finti, ma il meccanismo è quello vero.

### 🟢 7.S · Cercare per chiave (✅ · ✏️)

**Consegna.** Costruisci la tabella dei nomi e stampa l'indirizzo della posta. Poi prova a chiedere un nome che non c'è.

```python
indirizzi = {
    "www.esempio.example": "192.0.2.10",
    "posta.esempio.example": "192.0.2.25",
}
print(indirizzi["posta.esempio.example"])
print(indirizzi.get("ftp.esempio.example", "non trovato"))
print(indirizzi["ftp.esempio.example"])
```

**Ragionamento.**
1. `{ }` crea il dizionario; ogni voce è `chiave: valore`.
2. Il dizionario si interroga con la **chiave**, fra quadre: `indirizzi["posta..."]`.
3. `get` restituisce un valore di riserva se la chiave manca. La scrittura con `[ ]` invece fallisce.

```text
192.0.2.25
non trovato
Traceback (most recent call last):
  File "prova.py", line 7, in <module>
    print(indirizzi["ftp.esempio.example"])
          ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
KeyError: 'ftp.esempio.example'
```

📌 **Controllo.** Le prime due righe stampano, la terza si ferma con `KeyError`: la chiave non esiste.

⚠️ **Errore comune.** Un dizionario non ha posizioni: `indirizzi[0]` non dà il primo elemento, cerca la chiave `0`, che non c'è.

🧠 <u>Il dizionario si cerca per chiave, non per posizione.</u>

### 🎯 Da provare

**7.1 · ✅ · ✏️ · Prevedi il magazzino.**

```python
stock = {"pane": 3, "latte": 0}
stock["latte"] += 2
stock["uova"] = 12
print(stock)
```

<details>
<summary>🃏 <b>7.1 — Soluzione</b></summary>

```text
{'pane': 3, 'latte': 2, 'uova': 12}
```

`stock["latte"] += 2` modifica il valore della chiave `"latte"`. `stock["uova"] = 12` aggiunge una voce nuova.

</details>

**7.2 · 🔍 · ✏️ · Il prodotto più caro.** Dati i prodotti sotto, scrivi `prodotto_piu_caro(prodotti)` che restituisce il **nome** del prodotto con il prezzo più alto. Applicala all'esempio.

```python
prodotti = [
    {"nome": "pane", "prezzo": 1.5},
    {"nome": "latte", "prezzo": 1.2},
    {"nome": "formaggio", "prezzo": 6.8},
]
```

<details>
<summary>🃏 <b>7.2 — Soluzione</b></summary>

```python
prodotti = [
    {"nome": "pane", "prezzo": 1.5},
    {"nome": "latte", "prezzo": 1.2},
    {"nome": "formaggio", "prezzo": 6.8},
]


def prodotto_piu_caro(prodotti):
    migliore = prodotti[0]
    for p in prodotti:
        if p["prezzo"] > migliore["prezzo"]:
            migliore = p
    return migliore["nome"]


print(prodotto_piu_caro(prodotti))
```

```text
formaggio
```

La lista contiene dizionari: ogni `p` è un record, e `p["prezzo"]` ne legge un campo. Si confrontano i prezzi e si restituisce il nome del vincitore.

</details>

**7.3 · 🔍 · 📖 · Lista o dizionario?** Per ogni caso scegli la struttura e motiva in una frase:
1. l'ordine di arrivo dei clienti alla cassa;
2. il voto di uno studente cercato per nome;
3. le righe di un registro presenze, una per alunno, con data e stato.

<details>
<summary>🃏 <b>7.3 — Soluzione</b></summary>

1. **Lista**: conta la posizione, l'ordine è il dato.
2. **Dizionario**: si cerca per chiave (il nome), non per posizione.
3. **Lista di dizionari**: ogni riga è un record con campi diversi, e le righe si scorrono una per una.

</details>

---

## 8 · Progettare un piccolo programma

*Settimana S5 · ✅ 15 min · 🔍 15 min*

### 📜 Il test che non sapeva l'unità

Il 23 settembre 1999 la sonda Mars Climate Orbiter della NASA si perde nello spazio vicino a Marte. Secondo il rapporto dell'inchiesta, una parte del lavoro calcolava le spinte in libbre-forza per secondo, l'altra si aspettava newton per secondo. Il programma funzionava: sbagliavano l'unità di misura. Un test con il caso giusto l'avrebbe fermato prima del lancio. Verifica i dettagli sul rapporto ufficiale della NASA.

> 🛠️ **Il debugger** ferma il programma su un punto scelto (breakpoint) e lo fa avanzare riga per riga, mostrando i valori. Lo userai in laboratorio 🔧: per ora sappi che esiste.

### 🟢 8.S · Un test per ogni regola (✅ · ✏️)

**Consegna.** Scrivi la funzione `applica_sconto` e verifica tre casi con `assert`.

```python
def applica_sconto(prezzo, percentuale):
    return prezzo - prezzo * percentuale / 100


assert applica_sconto(100, 10) == 90
assert applica_sconto(50, 0) == 50
assert applica_sconto(80, 100) == 0
print("Test superati")
```

**Ragionamento.**
1. La funzione fa un solo compito: calcola il prezzo scontato, senza stampare.
2. Ogni `assert` scrive una frase: «il risultato deve essere questo». Se è falsa, Python si ferma con `AssertionError`.
3. I tre casi non sono scelti a caso: un normale, uno senza sconto, uno che azzera il prezzo.

```text
Test superati
```

📌 **Controllo.** Tre casi scelti bene valgono più di cento chiamate fatte a occhio.

⚠️ **Errore comune.** «Il programma non dà errori» non vuol dire «funziona». Un errore di logica passa in silenzio.

🧠 <u>Un test scrive che cosa ti aspetti: se il risultato cambia, lo sai subito.</u>

### 🎯 Da provare

**8.1 · 🔍 · ✏️ · Trova il caso limite.** Prevedi che cosa stampa il programma e perché.

```python
def media(voti):
    return sum(voti) / len(voti)


assert media([6, 8]) == 7
print("primo test ok")
assert media([]) == 0
print("secondo test ok")
```

<details>
<summary>🃏 <b>8.1 — Soluzione</b></summary>

```text
primo test ok
Traceback (most recent call last):
  File "prova.py", line 7, in <module>
    assert media([]) == 0
           ^^^^^^^^^
  File "prova.py", line 2, in media
    return sum(voti) / len(voti)
           ~~~~~~~~~~^~~~~~~~~~~
ZeroDivisionError: division by zero
```

Il primo test passa. Il secondo fallisce per un **caso limite**: una lista vuota non ha media. Un buon test prova anche i casi estremi: lista vuota, valore zero, valore massimo.

</details>

**8.2 · 🔍 · ✏️ · Separa il calcolo dalla stampa.** La funzione sotto calcola e stampa insieme. Scrivi `nuova_quantita(magazzino, nome, quantita)` che **restituisce** la nuova quantità senza stampare, poi due `assert`: uno per un prodotto già presente (`{"pane": 2}`, aggiungi 3) e uno per un prodotto nuovo (`{}`, aggiungi 4).

```python
def registra_acquisto(magazzino, nome, quantita):
    magazzino[nome] = magazzino.get(nome, 0) + quantita
    print("Ora", nome, "sono", magazzino[nome])
```

<details>
<summary>🃏 <b>8.2 — Soluzione</b></summary>

```python
def nuova_quantita(magazzino, nome, quantita):
    return magazzino.get(nome, 0) + quantita


assert nuova_quantita({"pane": 2}, "pane", 3) == 5
assert nuova_quantita({}, "latte", 4) == 4
print("Test superati")
```

```text
Test superati
```

Ora il calcolo è una funzione che si può provare. La stampa, se serve, si fa a parte, nel punto del programma che parla con l'utente.

</details>

**8.3 · ✅ · 📖 · Un test passato basta?** Rispondi in una frase: perché i test `assert` passati non dimostrano che il programma sia giusto?

<details>
<summary>🃏 <b>8.3 — Soluzione</b></summary>

Un test prova solo i casi che hai scelto. Se il bug sta in un caso che non hai pensato (lista vuota, unità di misura diversa), il test passa lo stesso. Per questo si scelgono casi normali e casi limite.

</details>

**Uscita di chiusura.** Completa: «Divido un programma in funzioni che ...; so che una funzione è giusta quando ...; a gennaio i dati e le funzioni che li usano si ritroveranno dentro ...».

---

## 📚 Fonti e risorse

- [The Python Tutorial](https://docs.python.org/3/tutorial/): capitoli 3, 4 e 5 coprono quasi tutti gli esercizi. Leggi le sezioni sulle liste e sui dizionari prima della verifica.
- [Python Tutor](https://pythontutor.com): incolla un esercizio dei livelli 🔍 e confronta le frecce con il tuo disegno.
- [RFC 5737](https://www.rfc-editor.org/rfc/rfc5737): gli indirizzi `192.0.2.0/24` riservati alla documentazione, usati nel caso 7.
- Agenzia delle Entrate, [aliquote IVA](https://www.agenziaentrate.gov.it/): conferma dell'aliquota ordinaria del 22% (caso 2).
- NASA, rapporto sull'inchiesta sulla perdita di Mars Climate Orbiter, 1999: il dettaglio dell'unità di misura (caso 8). Leggi solo il riassunto iniziale.
- [Think Python](https://allendowney.github.io/ThinkPython/), Allen B. Downey, licenza Creative Commons: esercizi aggiuntivi sugli stessi argomenti, da fare solo se ti servono.

---

↩️ [Torna a S6 - Ripasso in flashcard](%28STU%29%204CI%20nov-dic%20S6%20-%20Ripasso%20in%20flashcard.md) · 🏠 [Indice](../README.md)
