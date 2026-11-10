⬅️ [S7 - Ricostruire la macchina](%28STU%29%203EI%20sett-ott%20S7%20-%20Ricostruire%20la%20macchina.md) · 🏠 [Indice](../README.md)

# 🛠️ Eserciziario · 3EI Settembre-Ottobre — Come una macchina esegue un programma

**Classe:** 3EI · **Materia:** Sistemi e Reti · **Periodo:** Settembre-Ottobre (Unità S1–S7)  
**Strumenti consentiti:** solo carta e penna (nessuna calcolatrice: tutti i calcoli sono progettati per essere svolti a mente).

---

## 🧭 Come usare questo eserciziario

Ogni unità corrisponde a una settimana del percorso (S1–S6) più una scheda finale di riepilogo (S7) e segue sempre **quattro gradini**:

1. 🟢 **Modello svolto:** leggilo, copri la soluzione e prova a rifarlo.
2. 🟡 **Guidato (a buchi):** completa solo le parti mancanti per prendere confidenza con il metodo.
3. 🎯 **Autonomo (Coppia A / B):** due esercizi gemelli dello stesso livello. Usa **A** per allenarti subito, **B** a distanza di qualche giorno o per il recupero.
4. 🔍 **Caccia all'errore e ragionamento:** trova lo sbaglio nella soluzione di un altro o rispondi seguendo la regola *Tesi + Meccanismo + Esempio*.

### 🗺️ Percorsi consigliati

| Percorso | Obiettivo | Tempo stimato | Esercizi da svolgere |
|---|---|---:|---|
| ✅ **Percorso Base** | Consolidare i fondamentali (sufficienza piena) | ~50 min | Tutti i 🟢 e 🟡 + `1.3A`\*, `2.3A`, `3.3A`, `4.3A`, `5.3A`, `6.3A` |
| 🔍 **Percorso Completo** | Padroneggiare i meccanismi e i casi limite (voto alto) | ~40 min in più | Aggiungi tutte le **Cacce all'errore** (`1.4`, `2.4`, `3.4`, `4.4`, `5.4`, `6.4`) e l'**Unità 7** |
| ⚡ **Ripasso lampo pre-verifica** | Controllare di essere pronti il giorno prima | ~25 min | Svolgi la **Fila B** degli esercizi 🎯 (`1.3B`\*, `2.3B`, `3.3B`, `4.3B`, `5.3B`, `6.3B`) |

\* 🕓 **Non svolto quest'anno:** la parte su logica e relè (interruttori in serie/parallelo, AND/OR) non è stata trattata in classe. Saltala: `1.3A` e `1.3B` non rientrano nei percorsi di quest'anno.

---

## 🧰 Prontuario della macchina didattica (sempre valido)

Non serve imparare questi comandi a memoria: in verifica avrai sempre questa tabella.

| Istruzione | Effetto | Esempio |
|---|---|---|
| `LOAD Rd, [ind]` | **Copia** nel registro `Rd` il contenuto della cella di memoria `MEM[ind]`. La cella resta invariata. | `LOAD R1, [50]` → `R1 ← MEM[50]` |
| `STORE [ind], Rs` | **Copia** nella cella `MEM[ind]` il valore contenuto nel registro `Rs`. Il registro resta invariato. | `STORE [52], R3` → `MEM[52] ← R3` |
| `ADD Rd, Rs1, Rs2` | Somma i valori dei registri `Rs1` e `Rs2` e scrive il risultato nel **primo** registro (`Rd`). | `ADD R3, R1, R2` → `R3 ← R1 + R2` |
| `BEQ Rs1, Rs2, etichetta` | *(Facoltativo 🤓)* Se `Rs1` e `Rs2` sono uguali, salta all'istruzione indicata da `etichetta`. | `BEQ R1, R2, fine` |
| `HALT` | Ferma l'esecuzione del programma. | `HALT` |

**Regole fisse del modello:**
- Ogni istruzione occupa **1 cella** di memoria.
- Durante la fase di **fetch**, il registro `PC` avanza automaticamente di `1` (`PC ← PC + 1`).
- **Copiare non significa svuotare:** la sorgente conserva sempre il proprio valore finché non viene sovrascritta.

**Potenze di 2 utili a mente:**

| $2^0$ | $2^1$ | $2^2$ | $2^3$ | $2^4$ | $2^5$ | $2^6$ | $2^7$ | $2^8$ | $2^9$ | $2^{10}$ | $2^{11}$ | $2^{12}$ | $2^{13}$ | $2^{16}$ | $2^{20}$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | $1\,024$ (1 Ki) | $2\,048$ (2 Ki) | $4\,096$ (4 Ki) | $8\,192$ (8 Ki) | $65\,536$ (64 Ki) | $1\,048\,576$ (1 Mi) |

---

## 🔌 Unità 1 (S1) · Dalle macchine dedicate alla CPU

*Obiettivi: distinguere parte operativa e parte di controllo. 🕓 **Non svolto quest'anno:** logica degli interruttori e relè (serie/parallelo, AND/OR).*

> 🕓 **Parte non svolta quest'anno.** Il riquadro storico qui sotto e gli esercizi su interruttori, AND e OR (punto 1 di `1.1` e tutto `1.3`) riguardano un argomento che non abbiamo trattato in classe: puoi saltarli. Gli esercizi su parte operativa e parte di controllo (punto 2 di `1.1`, `1.2`, `1.4`) fanno invece parte del programma.

> 🕓 *(Non svolto quest'anno)* 📜 **Il contesto storico (1937).** Nella sua tesi al MIT, Claude Shannon dimostra che i circuiti elettrici fatti di interruttori (relè) realizzano l'algebra di Boole: due interruttori **in serie** corrispondono a un **AND** (devono essere entrambi chiusi), due **in parallelo** a un **OR** (basta che ne sia chiuso almeno uno). Dentro la CPU, i circuiti si dividono in **parte operativa** (conserva, sposta o trasforma i dati) e **parte di controllo** (decide quali operazioni attivare e quando).

### 1.1 🟢 Svolto · ✅ — Logica degli interruttori e ruoli nella CPU

**Consegna.**
1. 🕓 *(Non svolto quest'anno)* Una pressa industriale parte solo se l'operatore preme il **pedale** (`P`) **e** lo **sportello di sicurezza** (`S`) è chiuso, **oppure** se il tecnico attiva la **chiave di collaudo** (`C`). Scrivi la formula logica con `AND` / `OR` e stabilisci se la pressa parte quando `P = sì`, `S = no`, `C = sì`.
2. Durante un'operazione, la CPU usa: **(a)** l'ALU che somma due numeri; **(b)** la CU che invia il segnale «attiva la somma». Quale appartiene alla parte operativa e quale alla parte di controllo?

**Svolgimento passo-passo.**
1. 🕓 *(Non svolto quest'anno)* Pedale e sportello servono **insieme** → sono in serie (`P AND S`). La chiave di collaudo basta **da sola** → è in parallelo (`OR C`).
   - Formula: `(P AND S) OR C`.
   - Con `P = sì`, `S = no`, il ramo `P AND S` è aperto (falso), ma `C = sì` chiude il ramo in parallelo: **la pressa parte**.
2. Domanda-guida: *questo elemento tocca i dati o comanda chi li tocca?*
   - **(a) ALU:** trasforma i dati → **parte operativa**.
   - **(b) Segnale della CU:** dà un ordine senza contenere dati → **parte di controllo**.

---

### 1.2 🟡 Guidato (a buchi) · ✅ — Operativa o di controllo?

**Consegna.** Completa la tabella scrivendo **Operativa** oppure **Controllo**, e aggiungi il verbo mancante nella motivazione (*conserva*, *trasforma*, *trasferisce*, *coordina*).

| Elemento della CPU | Parte (Operativa / Controllo) | Perché? |
|---|---|---|
| 1. Il registro `R1` che tiene il numero `12` | `____________` | `____________` un dato durante il lavoro. |
| 2. La CU che interpreta il comando contenuto nell'`IR` | `____________` | `____________` le operazioni senza calcolare il dato. |
| 3. Il collegamento interno su cui viaggia il numero `12` da `R1` all'ALU | `____________` | `____________` fisicamente il dato da un blocco all'altro. |
| 4. Il segnale elettrico che apre l'ingresso del registro `R3` | `____________` | `____________` quando `R3` deve salvare il risultato. |
| 5. L'ALU che confronta due valori | `____________` | `____________` o confronta i dati ricevuti. |

<details>
<summary>🃏 <b>1.2 — Soluzione</b></summary>

1. **Operativa** (*conserva*).
2. **Controllo** (*coordina*).
3. **Operativa** (*trasferisce*).
4. **Controllo** (*coordina* / comanda).
5. **Operativa** (*trasforma*).

</details>

---

### 1.3 🎯 Autonomo (Coppia A / B) · ✅ — Serie, parallelo e condizioni

> 🕓 **Non svolto quest'anno:** logica e relè non sono stati trattati in classe. Salta questo esercizio.

#### Fila A
L'allarme di una sala server (`A`) suona se si verifica **almeno una** di queste due situazioni:
- viene rilevato **fumo** (`F`);
- la **porta è aperta** (`P`) **e** il **badge non è stato riconosciuto** (`N`).

a) Scrivi l'espressione logica con `AND` e `OR`.  
b) Disegna lo schema a interruttori (serie/parallelo).  
c) Compila l'esito per questi tre casi:
   - Caso 1: `F = no`, `P = sì`, `N = no`
   - Caso 2: `F = no`, `P = sì`, `N = sì`
   - Caso 3: `F = sì`, `P = no`, `N = no`

<details>
<summary>🃏 <b>1.3 Fila A — Soluzione</b></summary>

a) `F OR (P AND N)`.  
b) Un ramo con il solo interruttore `F`, in parallelo a un ramo che contiene `P` e `N` in serie.  
c) Caso 1: **non suona** (`P` è sì, ma `N` è no). Caso 2: **suona** (`P` e `N` entrambi sì). Caso 3: **suona** (basta `F = sì`).

</details>

#### Fila B
Una pompa di raffreddamento (`R`) si accende se **il livello dell'acqua è sufficiente** (`L`) **e** contemporaneamente vale almeno una di queste condizioni: **la temperatura supera la soglia** (`T`) **oppure** è attivo il **pulsante manuale** (`M`).

a) Scrivi l'espressione logica con `AND` e `OR` (attenzione alle parentesi).  
b) Se `L = no`, `T = sì`, `M = sì`, la pompa parte? Spiega in una riga perché.

<details>
<summary>🃏 <b>1.3 Fila B — Soluzione</b></summary>

a) `L AND (T OR M)`.  
b) **No, non parte.** `L` è in serie con tutto il resto: se manca l'acqua (`L = no`), il circuito resta aperto anche se `T` e `M` sono chiusi.

</details>

---

### 1.4 🔍 Caccia all'errore · Approfondimento

**Consegna.** Uno studente scrive: *«Quando eseguo `R2 ← R1` non c'è nessuna somma, quindi l'ALU non lavora; di conseguenza questa operazione viene svolta interamente dalla parte di controllo (CU).»*  
Individua l'errore e correggi l'affermazione distinguendo chi sposta il dato da chi dà il comando.

<details>
<summary>🃏 <b>1.4 — Soluzione</b></summary>

- **Tesi:** L'affermazione è sbagliata perché coinvolge **sia** la parte operativa **sia** la parte di controllo.
- **Meccanismo:** Anche senza calcoli dell'ALU, i registri `R1` e `R2` e il collegamento su cui viaggia il numero appartengono alla **parte operativa** (toccano e conservano il dato). La **parte di controllo (CU)** si limita a inviare i segnali per aprire l'uscita di `R1` e l'ingresso di `R2`.

</details>

---

## 🏛️ Unità 2 (S2) · La macchina di Von Neumann

*Obiettivi: spiegare il programma memorizzato; distinguere i 5 blocchi funzionali; distinguere indirizzo `x` e contenuto `MEM[x]`.*

> 📜 **Il contesto storico (1945–1949).** Per cambiare calcolo sull'ENIAC (1945) le programmatrici dovevano spostare cavi e interruttori per giorni. Con il modello di Von Neumann e macchine come l'EDSAC (1949, 512 parole di memoria), **le istruzioni entrano nella stessa memoria dei dati**: la macchina cambia mestiere senza cambiare un solo filo.

### 2.1 🟢 Svolto · ✅ — Indirizzo, contenuto, istruzioni e dati

**Consegna.** Osserva questo tratto di memoria (il programma inizia dalla cella `10`):

| Indirizzo | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|
| **Contenuto** | `LOAD R1, [13]` | `STORE [14], R1` | `HALT` | `25` | `0` |

1. Quali celle contengono istruzioni e quali contengono dati?
2. Qual è la differenza tra scrivere `13` e scrivere `MEM[13]`?
3. Quanto valgono `MEM[13]` e `MEM[14]` al termine del programma?

**Svolgimento passo-passo.**
1. Le celle **10, 11 e 12** contengono **istruzioni** (vengono raggiunte dal `PC`). Le celle **13 e 14** contengono **dati**.
2. `13` è l'**indirizzo** (il numero della casella); `MEM[13]` è il **contenuto** conservato dentro la casella `13`, che qui vale `25`.
3. `LOAD R1, [13]` copia `25` in `R1`. `STORE [14], R1` copia `25` nella cella `14`. Alla fine: **`MEM[13] = 25`** (la lettura non cancella la sorgente) e **`MEM[14] = 25`**.

---

### 2.2 🟡 Guidato (a buchi) · ✅ — Leggere la tabella della memoria

**Consegna.** Guarda la memoria qui sotto (`PC` iniziale = `20`, registri a `0`) e riempi gli spazi vuoti.

| Indirizzo | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 |
|---|---|---|---|---|---|---|---|---|
| **Contenuto** | `LOAD R1, [25]` | `LOAD R2, [26]` | `ADD R3, R1, R2` | `STORE [27], R3` | `HALT` | `14` | `6` | `0` |

- a) L'indirizzo dell'istruzione `HALT` è `____`.
- b) Il valore di `MEM[25]` è `____`, mentre `25` è il suo `____________`.
- c) Le tre celle che contengono dati sono `____`, `____` e `____`.
- d) Alla fine del programma, `R3` vale `____` e `MEM[27]` vale `____`.
- e) Alla fine del programma, `MEM[25]` vale ancora `____` perché l'istruzione `LOAD` esegue una `________`, non uno spostamento.

<details>
<summary>🃏 <b>2.2 — Soluzione</b></summary>

- a) **`24`**
- b) **`14`**; **indirizzo**
- c) **`25`**, **`26`** e **`27`**
- d) `R3 =` **`20`** (`14 + 6`); `MEM[27] =` **`20`**
- e) **`14`**; **copia**

</details>

---

### 2.3 🎯 Autonomo (Coppia A / B) · ✅ — I cinque blocchi e il modello di Von Neumann

#### Fila A
1. Assegna ciascun componente a uno dei **cinque blocchi** della macchina di Von Neumann (*CPU, Memoria principale, Input, Output, Collegamenti/Bus*):
   - Microfono · Modulo RAM con il programma in esecuzione · Piste della scheda madre · Monitor · Processore · SSD esterno quando invia un file alla RAM.
2. In memoria ci sono le celle: `MEM[40] = 8`, `MEM[41] = 40`.
   - Quanto vale `MEM[40]`?
   - Che differenza c'è tra il `40` usato in `MEM[40]` e il `40` contenuto dentro `MEM[41]`?

<details>
<summary>🃏 <b>2.3 Fila A — Soluzione</b></summary>

1. Microfono → **Input** · RAM → **Memoria principale** · Piste della scheda madre → **Collegamenti/Bus** · Monitor → **Output** · Processore → **CPU** · SSD esterno (in lettura/scrittura) → **Input/Output** (periferica di memoria di massa).
2. `MEM[40]` vale **`8`**. In `MEM[40]` il numero `40` è l'**indirizzo** della cella; in `MEM[41] = 40` il numero `40` è il **dato** contenuto nella cella `41` (che potrebbe anche rappresentare l'indirizzo di un'altra cella, ma resta un contenuto memorizzato lì).

</details>

#### Fila B
1. Spiega in due frasi qual è il vantaggio fondamentale del modello di **Von Neumann** rispetto a una macchina programmata a cavi come l'ENIAC.
2. Una scheda di rete Wi-Fi appartiene al blocco di Input o al blocco di Output? Motiva in una riga.
3. Se la cella di indirizzo `80` contiene il numero `5`, quale scrittura indica il numero `5` e quale indica la posizione della cella: `80` oppure `MEM[80]`?

<details>
<summary>🃏 <b>2.3 Fila B — Soluzione</b></summary>

1. Nel modello di Von Neumann **istruzioni e dati stanno nella stessa memoria**. Per cambiare compito alla macchina basta caricare in memoria un nuovo programma, senza modificare circuiti o cavi.
2. Appartiene a **entrambi (Input/Output)**: riceve dati dalla rete (input) e invia dati verso la rete (output).
3. `80` indica la **posizione (indirizzo)** della cella; `MEM[80]` indica il **contenuto**, cioè `5`.

</details>

---

### 2.4 🔍 Caccia all'errore · Approfondimento

**Consegna.** Correggi queste due frasi sbagliate spiegando **perché** non funzionano:
- **Frase 1:** *«Aprendo la RAM e guardando i bit di una cella, la memoria sa distinguere da sola se quel numero è un'istruzione oppure un dato.»*
- **Frase 2:** *«Per far eseguire un programma diverso a un computer di Von Neumann, bisogna sostituire i registri della CPU perché il programma è salvato tutto lì dentro.»*

<details>
<summary>🃏 <b>2.4 — Soluzione</b></summary>

- **Frase 1 (Falsa):** In memoria sia i dati sia le istruzioni sono sequenze di bit indistinguibili. A distinguerli è il **modo in cui la CPU li preleva**: se l'indirizzo arriva dal `PC` nella fase di fetch, il contenuto viene portato nell'`IR` e interpretato come istruzione; se arriva durante una `LOAD`, viene trattato come dato.
- **Frase 2 (Falsa):** Il programma in esecuzione risiede nella **memoria principale (RAM)**, non nei registri. I registri sono pochissimi e tengono soltanto l'istruzione corrente (`IR`) e i dati su cui la CPU sta lavorando in quell'istante.

</details>

---

## ⚙️ Unità 3 (S3) · Registri interni e percorsi dei dati

*Obiettivi: distinguere i ruoli di `PC`, `IR`, `MAR`, `MDR` e registri generali (`R1, R2...`); seguire micro-trasferimenti con `←`.*

> 📜 **Il contesto reale.** Quando un programmatore apre un **debugger** per capire perché un programma si è bloccato, vede una finestra con lo stato dei registri della CPU. Nel nostro modello didattico osserviamo quattro registri speciali: **`PC`** (indirizzo della prossima istruzione), **`IR`** (istruzione in corso), **`MAR`** (indirizzo della cella di memoria da leggere o scrivere), **`MDR`** (dato o istruzione appena transitato da/verso la memoria).

### 3.1 🟢 Svolto · ✅ — Seguire i passaggi tra `MAR`, `MDR` e registri

**Consegna.** Stato iniziale: `R1 = 4`, `R2 = 0`, `MAR = 0`, `MDR = 0`, `MEM[70] = 15`.  
Compila lo stato dopo ciascun micro-passo:

| Passo eseguito | R1 | R2 | MAR | MDR | MEM[70] |
|---|:-:|:-:|:-:|:-:|:-:|
| *(Stato iniziale)* | 4 | 0 | 0 | 0 | 15 |
| 1. `MAR ← 70` | **4** | **0** | **70** | **0** | **15** |
| 2. `MDR ← MEM[70]` | **4** | **0** | **70** | **15** | **15** |
| 3. `R2 ← MDR` | **4** | **15** | **70** | **15** | **15** |

**Osserva:**
- Nel passo 1 nel `MAR` entra **`70`** (l'indirizzo), **non** `15`.
- Nel passo 2 nell'`MDR` entra **`15`** (il contenuto della cella `70`).
- Questa sequenza di tre passi è esattamente ciò che succede dentro la CPU durante la fase di esecuzione di `LOAD R2, [70]`.

---

### 3.2 🟡 Guidato (a buchi) · ✅ — Chi fa cosa tra `PC`, `IR`, `MAR`, `MDR`

**Consegna.** Nella cella `10` si trova l'istruzione `LOAD R1, [50]` e nella cella `50` c'è il numero `9`.  
Osserva i due istanti fotografati dal debugger e completa le celle mancanti (`____`).

| Istante | PC | MAR | MDR | IR | R1 |
|---|:-:|:-:|:-:|:-:|:-:|
| **Istante A** · Appena concluso il *fetch* dell'istruzione | `11` | `10` | `LOAD R1, [50]` | `______________` | `0` |
| **Istante B** · Appena letto il dato dalla memoria (prima di copiarlo in `R1`) | `____` | `50` | `____` | `LOAD R1, [50]` | `0` |
| **Istante C** · Fine dell'istruzione `LOAD R1, [50]` | `11` | `50` | `9` | `LOAD R1, [50]` | `____` |

<details>
<summary>🃏 <b>3.2 — Soluzione</b></summary>

- **Istante A:** `IR =` **`LOAD R1, [50]`** (l'istruzione prelevata dall'`MDR` viene copiata nell'`IR`).
- **Istante B:** `PC =` **`11`** (non cambia durante la lettura del dato!); `MDR =` **`9`** (il contenuto di `MEM[50]`).
- **Istante C:** `R1 =` **`9`** (copiato dall'`MDR`).

</details>

---

### 3.3 🎯 Autonomo (Coppia A / B) · ✅ — Micro-passi e ruoli dei registri

#### Fila A
Stato iniziale: `R1 = 8`, `R2 = 3`, `MAR = 0`, `MDR = 0`, `MEM[60] = 20`.  
Compila la tabella eseguendo i passi in ordine:

| Passo | R1 | R2 | MAR | MDR | MEM[60] |
|---|:-:|:-:|:-:|:-:|:-:|
| *(Stato iniziale)* | 8 | 3 | 0 | 0 | 20 |
| 1. `R1 ← R2` | `__` | `__` | `__` | `__` | `__` |
| 2. `MAR ← 60` | `__` | `__` | `__` | `__` | `__` |
| 3. `MDR ← R1` | `__` | `__` | `__` | `__` | `__` |
| 4. `MEM[60] ← MDR` | `__` | `__` | `__` | `__` | `__` |

Domanda: a quale istruzione del nostro linguaggio corrisponde la sequenza dei passi 2–3–4 (`LOAD` oppure `STORE`)?

<details>
<summary>🃏 <b>3.3 Fila A — Soluzione</b></summary>

| Passo | R1 | R2 | MAR | MDR | MEM[60] |
|---|:-:|:-:|:-:|:-:|:-:|
| 1. `R1 ← R2` | **3** | 3 | 0 | 0 | 20 |
| 2. `MAR ← 60` | 3 | 3 | **60** | 0 | 20 |
| 3. `MDR ← R1` | 3 | 3 | 60 | **3** | 20 |
| 4. `MEM[60] ← MDR` | 3 | 3 | 60 | 3 | **3** |

I passi 2–3–4 corrispondono all'esecuzione di **`STORE [60], R1`**.

</details>

#### Fila B
Stato iniziale: `R1 = 0`, `R2 = 10`, `MAR = 0`, `MDR = 0`, `MEM[80] = 7`.  
Compila la tabella eseguendo i passi in ordine:

| Passo | R1 | R2 | MAR | MDR | MEM[80] |
|---|:-:|:-:|:-:|:-:|:-:|
| *(Stato iniziale)* | 0 | 10 | 0 | 0 | 7 |
| 1. `MAR ← 80` | `__` | `__` | `__` | `__` | `__` |
| 2. `MDR ← MEM[80]` | `__` | `__` | `__` | `__` | `__` |
| 3. `R1 ← MDR` | `__` | `__` | `__` | `__` | `__` |
| 4. `R2 ← R1` | `__` | `__` | `__` | `__` | `__` |

Domanda: a quale istruzione corrisponde la sequenza dei passi 1–2–3?

<details>
<summary>🃏 <b>3.3 Fila B — Soluzione</b></summary>

| Passo | R1 | R2 | MAR | MDR | MEM[80] |
|---|:-:|:-:|:-:|:-:|:-:|
| 1. `MAR ← 80` | 0 | 10 | **80** | 0 | 7 |
| 2. `MDR ← MEM[80]` | 0 | 10 | 80 | **7** | 7 |
| 3. `R1 ← MDR` | **7** | 10 | 80 | 7 | 7 |
| 4. `R2 ← R1` | 7 | **7** | 80 | 7 | 7 |

I passi 1–2–3 corrispondono all'esecuzione di **`LOAD R1, [80]`**.

</details>

---

### 3.4 🔍 Caccia all'errore · Approfondimento

**Consegna.** Durante l'esecuzione dell'istruzione `LOAD R2, [90]` (che si trova nella cella `15`, mentre `MEM[90] = 42`), uno studente afferma:
1. *«Alla fine della `LOAD R2, [90]`, il registro `PC` vale `90`.»*
2. *«Quando il dato `42` arriva dalla memoria, entra nel registro `IR`.»*

Spiega perché entrambe le frasi sono sbagliate e indica il registro corretto in ciascun caso.

<details>
<summary>🃏 <b>3.4 — Soluzione</b></summary>

1. **Errore sul `PC`:** Il `PC` tiene l'indirizzo della **prossima istruzione**, quindi dopo il fetch dalla cella `15` passa a **`16`**. L'indirizzo `90` è l'indirizzo di un **dato** e va nel **`MAR`**, mai nel `PC`.
2. **Errore sull'`IR`:** L'`IR` conserva l'**istruzione in corso** (`LOAD R2, [90]`) fino al termine della sua esecuzione. Il dato `42` proveniente dalla memoria transita nell'**`MDR`** e da lì viene copiato in **`R2`**.

</details>

---

## 🔄 Unità 4 (S4) · Il ciclo macchina, i bus e le tracce di programma

*Obiettivi: tracciare programmi con `LOAD`, `ADD`, `STORE`, `HALT`; distinguere bus indirizzi, dati e controllo; contare gli accessi in memoria.*

> 📜 **Il contesto reale.** Un microcontrollore dentro un termostato o una centralina ripete milioni di volte al secondo lo stesso ciclo a tre fasi: **Fetch** (preleva l'istruzione indicata dal `PC` e incrementa il `PC`), **Decode** (la CU interpreta l'istruzione nell'`IR`), **Execute** (esegue l'operazione usando ALU, registri o memoria). CPU e memoria comunicano attraverso tre **bus**: **indirizzi** (*dove*), **dati** (*che cosa*), **controllo** (*quale azione: `READ` o `WRITE`*).

### 4.1 🟢 Svolto · ✅ — Tracciare un programma e leggere i bus

**Consegna.** Segui le prime 4 istruzioni del programma qui sotto.
- **Stato iniziale:** `PC = 10`, `R1 = 0`, `R2 = 0`, `MEM[50] = 20`, `MEM[51] = 5`.

| Cella | Istruzione |
|---:|---|
| 10 | `LOAD R1, [50]` |
| 11 | `LOAD R2, [51]` |
| 12 | `ADD R1, R1, R2` |
| 13 | `STORE [50], R1` |
| 14 | `HALT` |

**Svolgimento della traccia:**

| Istruzione eseguita | PC | R1 | R2 | MEM[50] | Cosa è successo? |
|---|:-:|:-:|:-:|:-:|---|
| *(Stato iniziale)* | 10 | 0 | 0 | 20 | — |
| `LOAD R1, [50]` | **11** | **20** | 0 | 20 | Fetch da `10` (`PC→11`), poi legge `MEM[50]` in `R1`. |
| `LOAD R2, [51]` | **12** | 20 | **5** | 20 | Fetch da `11` (`PC→12`), poi legge `MEM[51]` in `R2`. |
| `ADD R1, R1, R2` | **13** | **25** | 5 | 20 | Somma `R1 + R2` in `R1`. **`MEM[50]` non cambia ancora!** |
| `STORE [50], R1` | **14** | 25 | 5 | **25** | Scrive il valore di `R1` (`25`) nella cella `MEM[50]`. |

**Che cosa transita sui tre bus durante la `STORE [50], R1` (cella 13)?**
- **Fase di Fetch:** Bus indirizzi = `13` · Bus controllo = `READ` · Bus dati = istruzione `STORE [50], R1` (Memoria → CPU).
- **Fase di Execute:** Bus indirizzi = `50` · Bus controllo = `WRITE` · Bus dati = `25` (CPU → Memoria).

---

### 4.2 🟡 Guidato (a buchi) · ✅ — Il fetch passo-passo e i tre bus

**Consegna.**
1. Il `PC` vale `12` e nella cella `12` c'è `ADD R3, R1, R2`. Completa i 5 passi del **fetch**:

| Passo del Fetch | MAR | MDR | IR | PC |
|---|:-:|:-:|:-:|:-:|
| 1. `MAR ← PC` | `12` | `0` | *(vuoto)* | `12` |
| 2. La CU invia `READ` sul bus di controllo | `12` | `0` | *(vuoto)* | `12` |
| 3. La memoria invia l'istruzione all'`MDR` | `12` | `______________` | *(vuoto)* | `12` |
| 4. `IR ← MDR` | `12` | `ADD R3, R1, R2` | `______________` | `12` |
| 5. `PC ← PC + 1` | `12` | `ADD R3, R1, R2` | `ADD R3, R1, R2` | `____` |

2. Durante la successiva fase di **execute**, l'istruzione `ADD R3, R1, R2` ha bisogno di usare di nuovo i bus verso la memoria? Perché?

<details>
<summary>🃏 <b>4.2 — Soluzione</b></summary>

1. Passo 3: `MDR =` **`ADD R3, R1, R2`**. Passo 4: `IR =` **`ADD R3, R1, R2`**. Passo 5: `PC =` **`13`**.
2. **No**, perché `ADD R3, R1, R2` opera solo sui registri interni alla CPU (`R1`, `R2`, `R3`). A differenza di `LOAD` e `STORE` (che accedono alla memoria **due volte**: una nel fetch e una nell'execute), la `ADD` accede alla memoria **una sola volta** (nel fetch).

</details>

---

### 4.3 🎯 Autonomo (Coppia A / B) · ✅ — Traccia completa e tabella dei bus

#### Fila A
**Programma in memoria:**

| Cella | Istruzione |
|---:|---|
| 10 | `LOAD R1, [50]` |
| 11 | `ADD R2, R1, R1` |
| 12 | `ADD R3, R2, R1` |
| 13 | `STORE [51], R3` |
| 14 | `STORE [50], R2` |
| 15 | `HALT` |

**Stato iniziale:** `PC = 10`, `R1 = 0`, `R2 = 0`, `R3 = 0`, `MEM[50] = 6`, `MEM[51] = 0`.

a) Compila la tabella di traccia per le 5 istruzioni (celle 10–14):

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[50] | MEM[51] |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| *(Stato iniziale)* | 10 | 0 | 0 | 0 | 6 | 0 |
| `LOAD R1, [50]` | `__` | `__` | `__` | `__` | `__` | `__` |
| `ADD R2, R1, R1` | `__` | `__` | `__` | `__` | `__` | `__` |
| `ADD R3, R2, R1` | `__` | `__` | `__` | `__` | `__` | `__` |
| `STORE [51], R3` | `__` | `__` | `__` | `__` | `__` | `__` |
| `STORE [50], R2` | `__` | `__` | `__` | `__` | `__` | `__` |

b) Compila cosa transita sui tre bus in questi tre momenti:

| Momento | Bus indirizzi | Bus controllo | Bus dati (e direzione) |
|---|---|---|---|
| Fetch della cella `10` | `____` | `____` | `____________________` |
| Execute di `LOAD R1, [50]` | `____` | `____` | `____________________` |
| Execute di `STORE [51], R3` | `____` | `____` | `____________________` |

<details>
<summary>🃏 <b>4.3 Fila A — Soluzione</b></summary>

a) **Traccia:**

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[50] | MEM[51] |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| `LOAD R1, [50]` | **11** | **6** | 0 | 0 | 6 | 0 |
| `ADD R2, R1, R1` | **12** | 6 | **12** | 0 | 6 | 0 |
| `ADD R3, R2, R1` | **13** | 6 | 12 | **18** | 6 | 0 |
| `STORE [51], R3` | **14** | 6 | 12 | 18 | 6 | **18** |
| `STORE [50], R2` | **15** | 6 | 12 | 18 | **12** | 18 |

b) **Bus:**
- Fetch cella `10`: Indirizzi = **`10`** · Controllo = **`READ`** · Dati = **`LOAD R1, [50]`** (Memoria → CPU).
- Execute `LOAD R1, [50]`: Indirizzi = **`50`** · Controllo = **`READ`** · Dati = **`6`** (Memoria → CPU).
- Execute `STORE [51], R3`: Indirizzi = **`51`** · Controllo = **`WRITE`** · Dati = **`18`** (CPU → Memoria).

</details>

#### Fila B
**Programma in memoria:**

| Cella | Istruzione |
|---:|---|
| 20 | `LOAD R1, [60]` |
| 21 | `LOAD R2, [61]` |
| 22 | `ADD R3, R1, R2` |
| 23 | `ADD R3, R3, R2` |
| 24 | `STORE [62], R3` |
| 25 | `HALT` |

**Stato iniziale:** `PC = 20`, `R1 = 0`, `R2 = 0`, `R3 = 0`, `MEM[60] = 9`, `MEM[61] = 4`, `MEM[62] = 0`.

a) Compila la tabella di traccia per le 5 istruzioni (celle 20–24):

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[60] | MEM[62] |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| *(Stato iniziale)* | 20 | 0 | 0 | 0 | 9 | 0 |
| `LOAD R1, [60]` | `__` | `__` | `__` | `__` | `__` | `__` |
| `LOAD R2, [61]` | `__` | `__` | `__` | `__` | `__` | `__` |
| `ADD R3, R1, R2` | `__` | `__` | `__` | `__` | `__` | `__` |
| `ADD R3, R3, R2` | `__` | `__` | `__` | `__` | `__` | `__` |
| `STORE [62], R3` | `__` | `__` | `__` | `__` | `__` | `__` |

b) Quanti accessi alla memoria (letture + scritture, compreso il fetch) compie in tutto la CPU per eseguire le prime 3 istruzioni (celle 20, 21 e 22)?

<details>
<summary>🃏 <b>4.3 Fila B — Soluzione</b></summary>

a) **Traccia:**

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[60] | MEM[62] |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| `LOAD R1, [60]` | **21** | **9** | 0 | 0 | 9 | 0 |
| `LOAD R2, [61]` | **22** | 9 | **4** | 0 | 9 | 0 |
| `ADD R3, R1, R2` | **23** | 9 | 4 | **13** | 9 | 0 |
| `ADD R3, R3, R2` | **24** | 9 | 4 | **17** | 9 | 0 |
| `STORE [62], R3` | **25** | 9 | 4 | 17 | 9 | **17** |

b) **5 accessi alla memoria in tutto:**
- Cella 20 (`LOAD`): 2 accessi (1 fetch + 1 lettura dato).
- Cella 21 (`LOAD`): 2 accessi (1 fetch + 1 lettura dato).
- Cella 22 (`ADD`): 1 solo accesso (1 fetch; l'execute usa solo i registri).

</details>

---

### 4.4 🔍 Caccia all'errore + 🤓 Salto condizionato `BEQ`

**Consegna 1 (🔍 Caccia all'errore).** Guarda questa traccia compilata da uno studente per il programma `10: LOAD R1, [50]` / `11: ADD R1, R1, R1` (con `PC = 10`, `R1 = 0`, `MEM[50] = 7`):
- Riga 1 (`LOAD R1, [50]`): `PC = 50`, `R1 = 7`, `MEM[50] = 0`
- Riga 2 (`ADD R1, R1, R1`): `PC = 51`, `R1 = 14`, `MEM[50] = 14`

Elenca i **tre errori concettuali** commessi dallo studente.

**Consegna 2 (🤓 Facoltativo — `BEQ`).** Nel programma qui sotto `R2` vale `0` e `MEM[71] = 9`.

| Cella | Istruzione |
|---:|---|
| 30 | `LOAD R1, [70]` |
| 31 | `BEQ R1, R2, fine` |
| 32 | `STORE [71], R1` |
| 33 | `fine: HALT` |

Quali celle vengono eseguite e quanto vale `MEM[71]` alla fine:
- nel Caso 1 (`MEM[70] = 0`)?
- nel Caso 2 (`MEM[70] = 5`)?

<details>
<summary>🃏 <b>4.4 — Soluzione</b></summary>

**Consegna 1 (I tre errori):**
1. **`PC = 50`:** ha messo nel `PC` l'indirizzo del dato (`50`) invece dell'istruzione successiva (`11`).
2. **`MEM[50] = 0` dopo la `LOAD`:** ha pensato che `LOAD` sposti il dato svuotando la cella, invece di copiarlo (`MEM[50]` resta `7`).
3. **`MEM[50] = 14` dopo la `ADD`:** ha pensato che `ADD` aggiorni automaticamente la memoria, mentre `ADD` modifica solo il registro `R1` (per scrivere in memoria serve una `STORE`).

**Consegna 2 (`BEQ`):**
- **Caso 1 (`MEM[70] = 0`):** `R1 = 0`, che è uguale a `R2 = 0` → il salto avviene. Celle eseguite: **`30 → 31 → 33`** (la `32` viene saltata). `MEM[71]` resta **`9`**.
- **Caso 2 (`MEM[70] = 5`):** `R1 = 5 ≠ 0` → il salto non avviene. Celle eseguite: **`30 → 31 → 32 → 33`**. `MEM[71]` diventa **`5`**.

</details>

---

## 📐 Unità 5 (S5) · Spazio di indirizzamento e gerarchia delle memorie

*Obiettivi: calcolare locazioni ($2^n$), ultimo indirizzo ($2^n - 1$) e capacità totale; distinguere spazio indirizzabile e RAM installata; ordinare la gerarchia delle memorie.*

> 📜 **Il contesto storico (1969 e 1981).** L'Apollo Guidance Computer aveva una RAM di $2\,048$ parole ($2^{11}$, quindi 11 bit di indirizzo), con parole da 16 bit (2 byte). L'IBM PC del 1981 (processore Intel 8088) aveva **20 bit di indirizzo**, pari a $2^{20} = 1\text{ MiB}$ di posizioni distinguibili, ma solo i primi $640\text{ KiB}$ erano usati per la RAM dei programmi: gli altri $384\text{ KiB}$ di indirizzi puntavano a ROM e periferiche. **Lo spazio di indirizzamento non coincide per forza con la RAM montata.**

### 5.1 🟢 Svolto · ✅ — Dai bit di indirizzo alla capacità (e viceversa)

**Consegna.**
1. Una memoria ha un bus indirizzi di **12 bit** e ogni locazione contiene **2 byte**. Calcola: numero di locazioni, ultimo indirizzo (partendo da `0`) e capacità totale in byte e in KiB.
2. Quanti bit di indirizzo servono **al minimo** per distinguere almeno **3 000 locazioni**?

**Svolgimento passo-passo.**
1. **Con 12 bit di indirizzo:**
   - **Numero di locazioni:** $2^{12} = 4\,096\text{ locazioni}$.
   - **Ultimo indirizzo:** poiché si parte da `0`, l'ultimo indirizzo è $4\,096 - 1 =$ **`4 095`**.
   - **Capacità totale:** $\text{locazioni} \times \text{byte per locazione} = 4\,096 \times 2\text{ byte} = 8\,192\text{ byte}$. Poiché $1\text{ KiB} = 1\,024\text{ byte}$, $8\,192 \div 1\,024 =$ **`8 KiB`**.
2. **Per almeno 3 000 locazioni:**
   - Cerco la prima potenza di 2 maggiore o uguale a $3\,000$: con 11 bit ho $2^{11} = 2\,048$ (non bastano); con **12 bit** ho $2^{12} = 4\,096$ (bastano). Servono **12 bit**.

---

### 5.2 🟡 Guidato (a buchi) · ✅ — Cosa cambia se raddoppio le celle o la larghezza?

**Consegna.** Una memoria ha **10 bit di indirizzo** e locazioni da **1 byte**. Completa la tabella:

| Situazione | Bit di indirizzo | Numero di locazioni ($2^n$) | Ultimo indirizzo | Byte per locazione | Capacità totale |
|---|:-:|:-:|:-:|:-:|:-:|
| **1. Memoria di partenza** | 10 bit | $2^{10} = 1\,024$ | `1 023` | 1 byte | `1 024 byte` (`1 KiB`) |
| **2. Raddoppio i byte per ogni locazione** (da 1 a 2 byte), lasciando 10 bit di indirizzo | `10 bit` | `________` | `________` | `2 byte` | `________________` |
| **3. Aggiungo 1 bit al bus indirizzi** (da 10 a 11 bit), con locazioni da 1 byte | `11 bit` | `________` | `________` | `1 byte` | `________________` |

<details>
<summary>🃏 <b>5.2 — Soluzione</b></summary>

- **Riga 2 (celle da 2 byte):** Locazioni = **`1 024`** (invariate!) · Ultimo indirizzo = **`1 023`** · Capacità = **`2 048 byte` (`2 KiB`)**.
- **Riga 3 (11 bit di indirizzo):** Locazioni = **`2 048`** (raddoppiate!) · Ultimo indirizzo = **`2 047`** · Capacità = **`2 048 byte` (`2 KiB`)**.

📌 **Regola d'oro:** cambiare la dimensione della cella cambia la **capacità**, ma **non** il numero di indirizzi. Aggiungere **1 bit** all'indirizzo **raddoppia** il numero di locazioni.

</details>

---

### 5.3 🎯 Autonomo (Coppia A / B) · ✅ — Calcoli di indirizzamento e gerarchia

#### Fila A
1. Una scheda di acquisizione dati usa indirizzi a **13 bit** e ogni locazione contiene **1 byte**.
   - a) Quante locazioni possiede?
   - b) Qual è l'indirizzo dell'ultima locazione?
   - c) Qual è la capacità in byte e in KiB?
   - d) Se ogni locazione passasse a **4 byte** mantenendo 13 bit di indirizzo, quante locazioni avrebbe e quale sarebbe la nuova capacità in KiB?
2. Ordina i 4 livelli della gerarchia (*RAM, Registri, SSD, Cache*) dal **più veloce** al **più lento** e indica per ciascuno se è **volatile** oppure **non volatile**.

<details>
<summary>🃏 <b>5.3 Fila A — Soluzione</b></summary>

1. a) $2^{13} =$ **`8 192` locazioni**.  
   b) **`8 191`**.  
   c) **`8 192 byte`**, cioè **`8 KiB`**.  
   d) Le locazioni restano **`8 192`**; la capacità quadruplica: $8\text{ KiB} \times 4 =$ **`32 KiB`** ($32\,768\text{ byte}$).
2. Dal più veloce al più lento: **Registri** (volatili) → **Cache** (volatile) → **RAM** (volatile) → **SSD** (non volatile).

</details>

#### Fila B
1. Una memoria contiene **512 locazioni**, ciascuna da **2 byte**.
   - a) Quanti bit servono per indirizzare le 512 locazioni?
   - b) Qual è l'ultimo indirizzo?
   - c) Qual è la capacità totale in byte e in KiB?
   - d) Quanti bit di indirizzo servirebbero al minimo se le locazioni diventassero **1 500**?
2. Nella scheda tecnica di un portatile leggi: *«Cache 16 MB · RAM 16 GB · SSD 512 GB»*. Spiega perché è sbagliato dire che quel computer ha «528 GB di RAM» e indica il ruolo specifico di ciascuno dei tre livelli.

<details>
<summary>🃏 <b>5.3 Fila B — Soluzione</b></summary>

1. a) $512 = 2^9 \rightarrow$ **`9 bit`**.  
   b) **`511`**.  
   c) $512 \times 2\text{ byte} =$ **`1 024 byte`**, cioè **`1 KiB`**.  
   d) Per $1\,500$ locazioni: $2^{10} = 1\,024$ (poche), $2^{11} = 2\,048$ (bastano) $\rightarrow$ **`11 bit`**.
2. Non si sommano perché hanno ruoli e tecnologie diverse: la **Cache** (volatile, velocissima) tiene copie dei blocchi usati più di frequente vicino alla CPU; la **RAM** (volatile) contiene i programmi e i dati in uso in quel momento; l'**SSD** (non volatile, più lento) conserva file e programmi anche a computer spento.

</details>

---

### 5.4 🔍 Caccia all'errore · Approfondimento

**Consegna.** Esamina queste due affermazioni e correggile:
- **Affermazione A:** *«Un microprocessore ha un bus dati da 16 bit; questo dimostra che può indirizzare al massimo $2^{16} = 65\,536$ locazioni di memoria.»*
- **Affermazione B:** *«Scendendo lungo la gerarchia delle memorie (dai registri all'SSD), la capacità e la persistenza dei dati senza corrente aumentano un po' a ogni gradino.»*

<details>
<summary>🃏 <b>5.4 — Soluzione</b></summary>

- **Affermazione A (Falsa):** Il numero di locazioni distinguibili dipende dalla larghezza del **bus indirizzi**, non dal bus dati. Il bus dati da 16 bit dice soltanto quanti bit viaggiano in un singolo trasferimento (2 byte alla volta).
- **Affermazione B (Parzialmente falsa):** La capacità aumenta scendendo nella gerarchia, ma la **persistenza (non volatilità) non cresce per gradi**: registri, cache e RAM sono tutti **volatili** (perdono tutto senza corrente), mentre la memoria di massa (SSD) e la ROM sono **non volatili**.

</details>

---

## ⚡ Unità 6 (S6) · Cache, località e clock

*Obiettivi: simulare hit e miss con blocchi consecutivi; distinguere località spaziale e temporale; calcolare periodo $T = 1/f$ a mente e confrontare prestazioni senza confondere GHz e velocità.*

> 📜 **Il contesto storico (1965 e 2000).** Negli anni '60 Maurice Wilkes propone una piccola memoria veloce (*cache* in SRAM) accanto alla CPU per non aspettare ogni volta la RAM (DRAM): funziona perché i programmi mostrano **località temporale** (riusano da lì a poco gli stessi dati/istruzioni, es. nei cicli) e **località spaziale** (leggono indirizzi vicini, caricati insieme nello stesso **blocco**). Nel 2000 la «corsa ai GHz» dei Pentium 4 rese evidente che alzare la frequenza di clock non basta se la CPU passa il tempo ferma ad aspettare i dati dalla memoria.

### 6.1 🟢 Svolto · ✅ — Simulare Hit/Miss a blocchi e calcolare il periodo del clock

**Consegna.**
1. Una cache è **vuota** all'inizio e carica dalla RAM **blocchi di 4 indirizzi consecutivi** (`40–43`, `44–47`, `48–51`). Il programma legge in sequenza gli indirizzi: `40, 41, 42, 40, 44, 45`. Per ogni accesso indica **HIT** o **MISS** e il tipo di località sfruttato.
2. Calcola a mente la durata di un ciclo di clock (**periodo $T$**) per una CPU a **2 GHz** e per una CPU a **500 MHz**.

**Svolgimento passo-passo.**

**1. Tabella della cache:**

| Accesso | Indirizzo richiesto | Blocco | Esito | Spiegazione e località |
|:-:|---|---|:-:|---|
| 1° | `40` | `40–43` | **MISS** | Cache vuota: la cache preleva dalla RAM **tutto il blocco `40–43`**. |
| 2° | `41` | `40–43` | **HIT** | È già in cache grazie al 1° accesso (**località spaziale**: indirizzo vicino). |
| 3° | `42` | `40–43` | **HIT** | Già nel blocco `40–43` (**località spaziale**). |
| 4° | `40` | `40–43` | **HIT** | Stesso indirizzo già usato poco prima (**località temporale**). |
| 5° | `44` | `44–47` | **MISS** | Blocco nuovo: la cache carica dalla RAM il blocco `44–47`. |
| 6° | `45` | `44–47` | **HIT** | Già caricato insieme al `44` (**località spaziale**). |

Totale: **2 MISS** (uno per ogni blocco nuovo) e **4 HIT**.

**2. Calcolo del periodo ($T = 1 / f$) a mente:**
- Ricorda: a **$1\text{ GHz}$** ($10^9\text{ cicli/s}$), un ciclo dura esattamente **$1\text{ ns}$** ($10^{-9}\text{ s}$).
- A **$2\text{ GHz}$** la frequenza è il doppio di $1\text{ GHz}$, quindi il ciclo dura la metà: $T = 1 \div 2 =$ **`0,5 ns`**.
- **$500\text{ MHz}$** corrispondono a $0{,}5\text{ GHz}$ (la metà di $1\text{ GHz}$), quindi il ciclo dura il doppio: $T = 1 \div 0{,}5 =$ **`2 ns`**.

---

### 6.2 🟡 Guidato (a buchi) · ✅ — Hit, Miss e confronto tra due CPU

**Consegna.**
1. La cache è vuota e usa blocchi da 4 posizioni (`80–83`, `84–87`). Completa gli esiti per la sequenza `80, 81, 84, 85, 80` (la cache ha spazio per tenere entrambi i blocchi):
   - `80`: **MISS** (carica il blocco `80–83`)
   - `81`: `______` (per località `__________`, perché era nello stesso blocco di `80`)
   - `84`: `______` (carica il blocco `______`)
   - `85`: `______` (per località `__________`)
   - `80`: `______` (per località `__________`, perché rilegge un indirizzo già usato)
2. Completa la tabella del clock a mente (ricorda che a $1\text{ GHz}$ il periodo è $1\text{ ns}$):

| Frequenza $f$ | Periodo $T$ (in nanosecondi) | Cicli compiuti in $1\text{ ns}$ |
|:-:|:-:|:-:|
| $1\text{ GHz}$ | `1 ns` | `1 ciclo` |
| $4\text{ GHz}$ | `________` | `4 cicli` |
| $2{,}5\text{ GHz}$ | `________` | `2,5 cicli` (5 cicli in 2 ns) |

<details>
<summary>🃏 <b>6.2 — Soluzione</b></summary>

1. `81`: **HIT** (località **spaziale**) · `84`: **MISS** (blocco **`84–87`**) · `85`: **HIT** (località **spaziale**) · `80`: **HIT** (località **temporale**).
2. A $4\text{ GHz}$: $1 \div 4 =$ **`0,25 ns`**. A $2{,}5\text{ GHz}$: $1 \div 2{,}5 =$ **`0,4 ns`**.

</details>

---

### 6.3 🎯 Autonomo (Coppia A / B) · ✅ — Simulazione cache e calcoli sul clock

#### Fila A
1. **Cache.** La cache è vuota, ha spazio per più blocchi e usa blocchi da 4 indirizzi (`60–63`, `64–67`). Un programma esegue un ciclo che legge gli indirizzi **`60, 61, 62, 63`** e ripete questa stessa sequenza per **10 volte** (40 letture totali).
   - a) Quanti **MISS** e quanti **HIT** avvengono nel **primo** giro (prime 4 letture)?
   - b) Quanti **MISS** e quanti **HIT** avvengono nei **9 giri successivi**?
   - c) Quale località spiega gli HIT del primo giro e quale località spiega gli HIT dei giri successivi?
2. **Clock.** Il processore **A** lavora a **$2\text{ GHz}$** e completa in media 1 istruzione ogni **2 cicli**. Il processore **B** lavora a **$4\text{ GHz}$**, ma a causa delle attese completa 1 istruzione ogni **5 cicli**.
   - a) Quanto dura un ciclo di clock di A e quanto dura un ciclo di B (in ns)?
   - b) Quante istruzioni al secondo completa A e quante ne completa B? Quale dei due svolge più lavoro al secondo?

<details>
<summary>🃏 <b>6.3 Fila A — Soluzione</b></summary>

1. a) Nel primo giro: **1 MISS** (su `60`, che carica tutto `60–63`) e **3 HIT** (su `61, 62, 63`).  
   b) Nei 9 giri successivi (36 letture): **0 MISS** e **36 HIT** (il blocco `60–63` è già in cache). In totale su 40 letture: **1 MISS e 39 HIT**.  
   c) Nel primo giro agisce la **località spaziale** (indirizzi consecutivi nello stesso blocco); nei giri successivi agisce la **località temporale** (riuso degli stessi indirizzi nel ciclo).
2. a) Periodo di A: $1 \div 2 =$ **`0,5 ns`**. Periodo di B: $1 \div 4 =$ **`0,25 ns`**.  
   b) Istruzioni al secondo di A: $2\text{ miliardi di cicli/s} \div 2 =$ **`1 miliardo di istruzioni/s`**.  
      Istruzioni al secondo di B: $4\text{ miliardi di cicli/s} \div 5 =$ **`800 milioni di istruzioni/s` (`0,8 miliardi`)**.  
      Completa più istruzioni **A**, pur avendo metà dei GHz di B.

</details>

#### Fila B
1. **Cache.** La cache è vuota e usa blocchi da 4 indirizzi (`90–93`, `94–97`). Un programma legge la sequenza **`90, 91, 94`** e la ripete identica per **20 volte** (60 letture totali).
   - a) Se la cache può contenere **almeno 2 blocchi**, quanti MISS ci sono in tutte le 60 letture?
   - b) Se invece la cache avesse **una sola linea** (può tenere **1 solo blocco** alla volta, quindi ogni nuovo blocco sostituisce quello precedente), cosa succederebbe ripetendo per 20 volte la coppia **`90, 94`** (40 letture)? Quanti MISS ci sarebbero?
2. **Clock.** Una CPU ha frequenza di **$1\text{ GHz}$**, un'altra di **$5\text{ GHz}$**.
   - a) Quanto dura il periodo $T$ di ciascuna (in ns)?
   - b) Quanti cicli compie ciascuna CPU in **$1\text{ microsecondo}$** ($1\text{ \mu s} = 1\,000\text{ ns}$)?

<details>
<summary>🃏 <b>6.3 Fila B — Soluzione</b></summary>

1. a) Con spazio per 2 blocchi: solo **2 MISS** in tutto (il primo accesso a `90` carica `90–93`; il primo accesso a `94` carica `94–97`). Tutte le altre **58 letture sono HIT**.  
   b) Con una sola linea, `90` e `94` appartengono a blocchi diversi e si cacciano a vicenda a ogni lettura: ci sono **40 MISS su 40 letture** (0 HIT).
2. a) A $1\text{ GHz}$: **`1 ns`**. A $5\text{ GHz}$: $1 \div 5 =$ **`0,2 ns`**.  
   b) In $1\,000\text{ ns}$: la CPU a $1\text{ GHz}$ compie **`1 000 cicli`**; quella a $5\text{ GHz}$ compie **`5 000 cicli`**.

</details>

---

### 6.4 🔍 Caccia all'errore e ragionamento tecnico

**Consegna.**
1. Correggi questa frase: *«Quando si verifica un cache miss significa che c'è stato un errore e la CPU deve andare a leggere il file direttamente sull'SSD.»*
2. Un compagno dice: *«Ho comprato una CPU da 4 GHz invece che da 3 GHz, quindi qualunque programma girerà certamente più veloce, anche se il PC ha pochissima RAM e una cache minuscola.»* Rispondi in 3–4 frasi usando la struttura **Tesi + Meccanismo + Esempio** e citando **clock**, **cache (hit/miss)** e **RAM**.

<details>
<summary>🃏 <b>6.4 — Soluzione</b></summary>

1. **Correzione sul cache miss:** Un *miss* **non è un guasto**, ma un evento normale: significa solo che il dato cercato non è ancora copiato in cache. Inoltre la CPU non va sull'SSD, ma chiede il blocco al **livello successivo della gerarchia** (un altro livello di cache oppure la **RAM**), pagando un'attesa maggiore rispetto all'*hit*.
2. **Risposta strutturata (Tesi + Meccanismo + Esempio):**
   - **Tesi:** Non basta avere più GHz per garantire che un programma sia più veloce.
   - **Meccanismo:** La frequenza di **clock** indica solo quanti cicli avvengono in un secondo, non quante istruzioni vengono completate. Se la **cache** è piccola e si verificano molti **miss**, la CPU deve aspettare i dati dalla **RAM** (molto più lenta); e se anche la RAM è insufficiente per i programmi aperti, il sistema rallenta ancora di più.
   - **Esempio:** Una CPU a 3 GHz che trova quasi sempre i dati in cache (*hit*) completa un ciclo di calcoli in meno tempo di una CPU a 4 GHz costretta a restare ferma per decine di cicli in attesa della RAM.

</details>

---

## 🏆 Unità 7 (S7) · Ricostruire la macchina (Prova integrata)

*Obiettivi: collegare scrittura di un breve programma, tracciamento dei registri, bus, calcolo della memoria e ruolo della cache in un unico problema (stesso formato della Parte 4 della verifica).*

### 7.1 🔍 Problema completo — Dal programma alla cache

Una centralina deve calcolare la somma di **tre sensori** memorizzati nelle celle `MEM[50]`, `MEM[51]` e `MEM[52]`, e salvare il totale nella cella `MEM[53]`.

#### Parte A · Scrivere il programma
Usando solo le istruzioni `LOAD`, `ADD`, `STORE` e `HALT` (una per cella, partendo dalla cella `10`), scrivi il programma completo nella tabella:

| Cella | Istruzione |
|---:|---|
| 10 | `______________________` |
| 11 | `______________________` |
| 12 | `______________________` |
| 13 | `______________________` |
| 14 | `______________________` |
| 15 | `______________________` |
| 16 | `______________________` |

#### Parte B · Collaudo di registri e bus
Supponi che all'inizio `PC = 10`, i registri valgano `0` e in memoria ci siano: `MEM[50] = 5`, `MEM[51] = 10`, `MEM[52] = 15`, `MEM[53] = 0`.
1. Quanto vale `MEM[53]` al termine del programma? E quanto vale `MEM[50]`?
2. Durante la fase di **execute** dell'istruzione `STORE` finale, quanto valgono `MAR` e `MDR`? Che cosa transita sui tre bus (indirizzi, dati, controllo)?

#### Parte C · Effetto della cache sul programma
Supponi che la cache sia **vuota** all'inizio e carichi dalla RAM **blocchi di 4 celle consecutive**:
- il blocco `10–13` contiene le prime quattro istruzioni;
- il blocco `14–17` contiene le ultime tre istruzioni;
- il blocco `50–53` contiene i tre dati dei sensori e la cella del risultato.

1. Quando la CPU fa il fetch della prima istruzione nella cella `10` (che produce un **MISS**), perché i fetch delle istruzioni nelle celle `11`, `12` e `13` risultano tutti **HIT** anche se quelle istruzioni non erano mai state eseguite prima? Quale principio di località entra in gioco?
2. Quando la prima `LOAD` legge `MEM[50]` (producendo un **MISS** sul blocco `50–53`), le due `LOAD` successive su `MEM[51]` e `MEM[52]` trovano il dato in cache (**HIT**) o devono tornare in RAM (**MISS**)?

<details>
<summary>🃏 <b>7.1 — Soluzione completa</b></summary>

#### Parte A · Programma
| Cella | Istruzione |
|---:|---|
| 10 | `LOAD R1, [50]` |
| 11 | `LOAD R2, [51]` |
| 12 | `LOAD R3, [52]` |
| 13 | `ADD R1, R1, R2` |
| 14 | `ADD R1, R1, R3` |
| 15 | `STORE [53], R1` |
| 16 | `HALT` |

*(È corretta qualsiasi variante che carichi le tre celle con tre `LOAD`, esegua due `ADD` mettendo il registro di destinazione al primo posto, salvi la somma in `[53]` con `STORE [53], Rd` e termini con `HALT`.)*

#### Parte B · Registri e bus
1. `MEM[53] =` **`30`** ($5 + 10 + 15$). `MEM[50]` vale ancora **`5`** (la `LOAD` copia senza cancellare).
2. Durante l'execute di `STORE [53], R1`:
   - **`MAR = 53`**, **`MDR = 30`**.
   - **Bus indirizzi:** `53` · **Bus dati:** `30` (dalla CPU alla memoria) · **Bus controllo:** `WRITE`.

#### Parte C · Cache e località
1. Il MISS sulla cella `10` porta in cache l'intero blocco `10–13`. Perciò le istruzioni `11`, `12` e `13` sono già presenti in cache e generano **3 HIT** grazie alla **località spaziale** (istruzioni memorizzate in celle consecutive).
2. Trovano il dato già in cache (**2 HIT**), perché il MISS su `MEM[50]` ha caricato l'intero blocco `50–53`, che contiene anche `MEM[51]` e `MEM[52]` (ancora **località spaziale**, questa volta sui dati).

</details>

