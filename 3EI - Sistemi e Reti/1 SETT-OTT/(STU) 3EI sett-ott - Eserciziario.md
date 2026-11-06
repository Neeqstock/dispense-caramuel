⬅️ [S7 - Ricostruire la macchina](%28STU%29%203EI%20sett-ott%20S7%20-%20Ricostruire%20la%20macchina.md) · 🏠 [Indice](../README.md)

# 🛠️ Eserciziario · 3EI sett-ott

**3EI · Settembre-Ottobre · Casi reali e situazioni verosimili · Teoria e pratica scritta**

⏱️ **Ogni dossier richiede circa 10–20 minuti.** Il percorso ✅ essenziale dura circa 75 minuti; gli approfondimenti 🔍 richiedono circa altri 45 minuti. Gli esercizi 🤓 sono facoltativi. Non è un compito da svolgere tutto in una volta: scegli i dossier che ti servono e affrontane anche uno al giorno.

> **Legenda:** ✅ da sapere · 🔍 per capire fino in fondo · 🤓 facoltativo · 📜 caso vero o verosimile · 🛠️ restauro · 📖 teoria · ✏️ pratica scritta · 🟢 svolto: guarda come si fa · 🎯 da provare: soluzione nascosta · 🧠 da ricordare · ⚠️ errore comune · 📌 controllo · 🃏 soluzione

Un museo dell'informatica riceve in dono una stanza piena di macchine spente: un computer degli anni Quaranta, una scheda di bordo e un vecchio PC. Nessuno sa più come funzionano. Voi siete i tecnici del **laboratorio di restauro** (il museo è inventato). Per rimetterle in moto non servono martelli: bisogna capire **che cosa conserva ogni componente, chi coordina le operazioni e quanto tempo si perde ad aspettare**.

Ogni dossier parte da una macchina reale o da una situazione verosimile. Potreste dover individuare un guasto o leggere una scheda tecnica. Alla fine, ricostruirete il funzionamento della macchina.

<u>Un computer non è un mistero: è una catena di piccole regole.</u> Conoscerle è il modo per sapere dove guardare quando qualcosa non va.

## Come si usa

- 🟢 **Svolto.** Leggi i passaggi, poi copri la soluzione e rifai l'esercizio sul quaderno.
- 🎯 **Da provare.** Prima svolgi l'esercizio sul quaderno. Poi apri la soluzione 🃏 e confrontala con la tua.
- Ogni dossier contiene esercizi di teoria 📖 e di pratica scritta ✏️; alcuni includono anche un esempio svolto 🟢.
- **Le regole del gioco.** La nostra macchina conosce le istruzioni `LOAD`, `ADD`, `STORE` e `HALT`: ogni istruzione occupa una cella. Dopo il fetch, il PC passa all'indirizzo successivo. Per ripassare la notazione, consulta il [foglio sul linguaggio assembly](%28STU%29%203EI%20-%20Linguaggio%20assembly%20base.md).
- **Valori.** I nomi, gli indirizzi e i numeri degli esercizi sono inventati. Le informazioni storiche contrassegnate con 📜 sono accompagnate dalle fonti in fondo alla pagina.

| Dossier | Tema | Settimana | Caso |
| :-----: | ------------------------------- | :-------: | ------------------------------------ |
| 1 | Il programma entra in memoria | S1–S2 | ENIAC e EDSAC |
| 2 | Dentro la CPU | S1, S3 | Shannon e i relè; il debugger |
| 3 | Il ciclo macchina | S4 | La centralina di una serra |
| 4 | Indirizzi, bus e capacità | S5 | IBM PC, Apollo, EDSAC |
| 5 | Gerarchia e cache | S5–S6 | La scheda tecnica di un portatile |
| 6 | Il clock | S6 | La corsa ai GHz dei Pentium 4 |
| 7 | Ricostruisci la macchina | S1–S6 | Il collaudo del museo |

---

## 🛠️ Dossier 1 · Il programma entra in memoria

*Si usa S1–S2: Von Neumann, indirizzo e contenuto, i cinque blocchi.*

### 📜 Caso vero: da ENIAC a EDSAC

Nel 1946 l'ENIAC, uno dei primi calcolatori elettronici, si programmava manualmente, ricollegando cavi e impostando interruttori. Cambiare calcolo poteva richiedere giorni. A programmarlo era un gruppo di matematiche, fra cui Kay McNulty, Jean Jennings e Betty Snyder.

Il 6 maggio 1949 entra in funzione a Cambridge l'EDSAC. La sua memoria contiene **512 parole** e usa linee di ritardo a mercurio. La novità non è il materiale, ma l'idea di conservare **anche il programma in memoria**. Per cambiare compito non occorre più ricollegare i cavi: basta sostituire le istruzioni memorizzate.

🧠 <u>La macchina resta la stessa. Cambia ciò che sta in memoria.</u>

### 1.1 📖 Teoria · ✅ · 🟢 Svolto — Che cosa c'è nelle celle

**Consegna.** Nel laboratorio c'è un computer con queste celle (valori inventati):

```text
indirizzo:  60                61                 62      63    64
contenuto:  LOAD R1, [63]     STORE [64], R1     HALT    9     0
```

1. Quali celle contengono istruzioni e quali dati?
2. Che differenza c'è fra `63` e `MEM[63]`?
3. Che cosa cambia nella memoria dopo aver eseguito il programma?
4. Per far fare alla macchina un altro lavoro, che cosa cambiamo?

**Svolgimento.**

1. Le istruzioni stanno nelle celle **60, 61 e 62**. I dati stanno nelle celle **63 e 64**.
2. `63` è l'**indirizzo**: dice dove sta la cella. `MEM[63]` è il suo **contenuto**: qui vale 9.
3. La `LOAD` copia 9 in R1. La `STORE` copia R1 nella cella 64. Alla fine `MEM[64] = 9`. La cella 63 resta 9, perché una copia non svuota la sorgente.
4. Cambiamo le **istruzioni scritte in memoria**. I collegamenti e i circuiti restano gli stessi.

📌 **Controllo.** Istruzioni e dati stanno nella stessa memoria, ma in celle diverse. La memoria non li distingue da sola: è la CPU a interpretarli in base al modo in cui li usa.

🧠 <u>L'indirizzo dice dove. Il contenuto dice che cosa c'è.</u>

### 1.2 ✏️ Pratica · ✅ · 🎯 Da provare — Leggi la memoria

**Consegna.** Ecco la memoria di una macchina (valori inventati). Il PC parte da 200 e i registri valgono 0.

| Indirizzo | 200 | 201 | 202 | 203 | 204 | 205 | 206 | 207 |
|---|---|---|---|---|---|---|---|---|
| Contenuto | `LOAD R1, [205]` | `LOAD R2, [206]` | `ADD R3, R1, R2` | `STORE [207], R3` | `HALT` | 14 | 6 | 0 |

Sul quaderno rispondi:

a) Quanto vale `MEM[205]`?
b) A quale indirizzo sta l'istruzione `HALT`?
c) Quali sono le celle che contengono dati?
d) Quanto vale `MEM[207]` alla fine del programma?
e) Dopo la `LOAD R1, [205]`, la cella 205 è ancora 14?

<details>
<summary>🃏 <b>1.2 — Soluzione</b></summary>

a) 14. b) 204. c) 205, 206 e 207. d) 20, perché R3 = 14 + 6 e la `STORE` lo copia nella cella 207. e) Sì: la `LOAD` copia, non sposta.

⚠️ **Errore comune:** dire che `MEM[205]` è 205. Il numero 205 è l'indirizzo; il contenuto è 14.

</details>

### 1.3 📖 Teoria · 🔍 · 🎯 Da provare — Le frasi del restauratore

**Consegna.** Per ogni frase scrivi **vero** o **falso**. Se è falsa, correggila in una frase.

A. «Per fare un altro lavoro a un computer a programma memorizzato bisogna ricollegare i cavi, come per l'ENIAC.»
B. «Se in una cella c'è scritto 70, quel 70 è per forza un indirizzo.»
C. «In una macchina a programma memorizzato le istruzioni sono informazioni come i dati: si possono caricare e sostituire in memoria.»
D. «Nel modello di Von Neumann i dati e le istruzioni stanno nella stessa memoria.»

<details>
<summary>🃏 <b>1.3 — Soluzione</b></summary>

A. **Falso.** Basta sostituire le istruzioni in memoria. I cavi restano al loro posto.
B. **Falso.** Un numero in una cella può essere un dato, o la parte di un'istruzione che indica un indirizzo. Dipende da come la macchina lo usa.
C. **Vero.**
D. **Vero.**

</details>

### 1.4 ✏️ Pratica · ✅ · 🎯 Da provare — I cinque blocchi di un computer

**Consegna.** Un vecchio computer del museo ha una tastiera, una RAM che contiene il programma, un altoparlante, il processore che esegue le istruzioni e i collegamenti fra i pezzi. Sul quaderno assegna ciascun elemento a uno dei **cinque blocchi** del modello (CPU, memoria principale, ingresso, uscita, collegamenti). Poi rispondi: una scheda di rete è ingresso o uscita?

<details>
<summary>🃏 <b>1.4 — Soluzione</b></summary>

Tastiera → **ingresso**. RAM con il programma → **memoria principale**. Altoparlante → **uscita**. Processore → **CPU**. Fili e piste di collegamento → **collegamenti**. Una scheda di rete è **entrambi**: porta dati nel sistema e li porta fuori.

</details>

---

## 🛠️ Dossier 2 · Dentro la CPU

*Si usa S1 e S3: interruttori, parte operativa e di controllo, registri e notazione.*

### 📜 Caso vero: Shannon e i relè, 1937

Nel 1937 Claude Shannon, giovane ricercatore al MIT, scrive una tesi su un'idea sorprendente: i circuiti formati da **relè** — interruttori comandati da un segnale elettrico — possono rappresentare le operazioni dell'algebra di Boole. Due interruttori in serie lasciano passare la corrente solo se sono entrambi chiusi: è un **AND**. Due interruttori in parallelo la lasciano passare se ne basta uno: è un **OR**. Un interruttore che apre quando riceve corrente dà un **NOT**.

Da allora, i circuiti si possono **progettare** usando la logica, non solo per tentativi. Relè, valvole e transistor sono modi sempre più piccoli e veloci di costruire interruttori.

🧠 <u>I circuiti della CPU combinano segnali elettrici per elaborare i dati.</u>

### 2.1 📖 Teoria · ✅ · 🟢 Svolto — La porta del laboratorio

**Consegna.** La porta del laboratorio (scena inventata) si apre se vengono presentati **il badge e il codice giusto**, oppure se si usa **la chiave di emergenza**. Scrivi la condizione usando AND e OR, poi disegna gli interruttori.

**Svolgimento.**

1. Badge e codice servono **insieme**: sono due interruttori **in serie**. È un AND.
2. La chiave basta **da sola**: è un ramo **in parallelo**. È un OR.
3. Condizione: `(badge AND codice) OR chiave`.

```text
            badge        codice
      +-----/ -------/ ----------+
 ----+                           +----- serratura
      +----------/ --------------+
                chiave
```

| Badge | Codice | Chiave | La porta si apre? |
|:-:|:-:|:-:|:-:|
| sì | sì | no | sì |
| sì | no | no | no |
| no | no | sì | sì |
| sì | no | sì | sì |

📌 **Controllo.** Un solo interruttore chiuso nella serie non basta. Un ramo in parallelo chiuso basta.

⚠️ **Errore comune:** scambiare serie e parallelo. Serie = «tutti», AND. Parallelo = «almeno uno», OR.

### 2.2 ✏️ Pratica · ✅ · 🎯 Da provare — Operativa o di controllo?

**Consegna.** Per ciascun elemento della CPU, indica se appartiene alla **parte operativa** o alla **parte di controllo**. Per decidere, chiediti: *questo elemento elabora o trasferisce dati, oppure controlla le operazioni?*

1. Il registro R1, che contiene 7.
2. L'ALU, che trasforma 7 e 5 in 12.
3. La CU, che decide «qui si fa una somma, non una sottrazione».
4. Il collegamento che porta il contenuto di R1 verso l'ALU.
5. Il segnale «apri il collegamento da R2».
6. Il registro che conserva il risultato 12.

<details>
<summary>🃏 <b>2.2 — Soluzione</b></summary>

1. **Operativa**: conserva un dato.
2. **Operativa**: trasforma i dati.
3. **Controllo**: decide, non tocca i dati.
4. **Operativa**: sposta i dati; è aperto da un segnale di controllo.
5. **Controllo**: è un ordine, non un dato.
6. **Operativa**: conserva un dato.

🧠 La CU **non calcola** e **non conserva** i dati: li comanda.

</details>

### 2.3 ✏️ Pratica · ✅ · 🎯 Da provare — La notazione dei registri

**Consegna.** Stato iniziale: `R1 = 3`, `R2 = 0`, `MAR = 0`, `MDR = 0`, `MEM[95] = 11`. Esegui i quattro passi **uno alla volta** e riempi la tabella dopo ciascuno.

| Passo | R1 | R2 | MAR | MDR | MEM[95] |
|---|:-:|:-:|:-:|:-:|:-:|
| `R2 <- 5` | `__` | `__` | `__` | `__` | `__` |
| `MAR <- 95` | `__` | `__` | `__` | `__` | `__` |
| `MDR <- MEM[95]` | `__` | `__` | `__` | `__` | `__` |
| `R1 <- MDR` | `__` | `__` | `__` | `__` | `__` |

<details>
<summary>🃏 <b>2.3 — Soluzione</b></summary>

| Passo | R1 | R2 | MAR | MDR | MEM[95] |
|---|:-:|:-:|:-:|:-:|:-:|
| `R2 <- 5` | 3 | 5 | 0 | 0 | 11 |
| `MAR <- 95` | 3 | 5 | 95 | 0 | 11 |
| `MDR <- MEM[95]` | 3 | 5 | 95 | 11 | 11 |
| `R1 <- MDR` | 11 | 5 | 95 | 11 | 11 |

📌 La freccia **copia**: la sorgente non cambia. `MEM[95]` vale 11 dall'inizio alla fine.

⚠️ **Errore comune:** scrivere `MAR = 11`. Il MAR tiene l'**indirizzo** (95), l'MDR tiene il **contenuto** (11).

</details>

### 2.4 📖 Teoria · 🔍 · 🎯 Da provare — Il pannello del debugger

**Consegna.** Un debugger è un programma che mostra i registri mentre un altro programma è in esecuzione. Il restauratore osserva il pannello seguente (valori inventati). Nella cella 150 si trova l'istruzione `LOAD R2, [260]` e `MEM[260] = 18`.

| | PC | MAR | MDR | IR | R2 |
|---|:-:|:-:|:-:|:-:|:-:|
| **Pannello A** · fetch finito | 151 | 150 | `LOAD R2, [260]` | `LOAD R2, [260]` | 0 |
| **Pannello B** · dato arrivato | 151 | 260 | 18 | `LOAD R2, [260]` | 0 |

a) Quale registro dice dove prendere la **prossima istruzione**?
b) Perché nel pannello A il MAR vale 150 e non 151?
c) Perché nel pannello B il MAR vale 260 e l'IR è rimasto lo stesso?
d) Quanto vale R2 alla fine dell'istruzione?

<details>
<summary>🃏 <b>2.4 — Soluzione</b></summary>

a) Il **PC**.
b) Il MAR riceve il valore del PC **prima** che il PC avanzi: per prelevare l'istruzione ha usato 150. Poi il PC passa a 151.
c) Nel secondo accesso il MAR tiene l'indirizzo del **dato** (260). L'IR continua a tenere il comando finché l'istruzione non è finita: il dato arriva nell'MDR, non nell'IR.
d) 18, perché il contenuto dell'MDR viene copiato in R2.

⚠️ **Errore comune:** pensare che dopo la `LOAD` il PC salti a 260. Il PC continua con l'istruzione successiva; 260 è l'indirizzo di un dato.

</details>

---

## 🛠️ Dossier 3 · Il ciclo macchina

*Si usa S4: fetch, decode, execute, tracce di programma, bus.*

### 📜 Scena verosimile: la centralina della serra (inventata)

Nel museo c'è la centralina di una vecchia serra: un piccolo computer che controlla la temperatura. Ripete sempre la stessa sequenza: preleva la prossima istruzione, la interpreta, la esegue e poi passa alla successiva.

Prelevare, interpretare, eseguire: **fetch, decode, execute**. Se la centralina si blocca, il restauratore non può capire il guasto «a orecchio»: deve seguire il programma passo dopo passo, come fa la CPU.

🧠 <u>Una macchina a programma memorizzato fa sempre lo stesso giro: legge, capisce, esegue, passa alla prossima.</u>

### 3.1 ✏️ Pratica · ✅ · 🟢 Svolto — Alza la temperatura obiettivo

**Consegna.** In memoria c'è questo programma (valori inventati). La temperatura obiettivo della serra è in `MEM[300]` e il passo di aumento in `MEM[301]`.

| Cella | Istruzione |
|---:|---|
| 120 | `LOAD R1, [300]` |
| 121 | `LOAD R2, [301]` |
| 122 | `ADD R1, R1, R2` |
| 123 | `STORE [300], R1` |
| 124 | `HALT` |

**Stato iniziale:** `PC = 120`, `R1 = 0`, `R2 = 0`, `MEM[300] = 20`, `MEM[301] = 5`. Dopo il fetch il PC avanza di uno. Esegui le prime quattro istruzioni.

**Svolgimento.**

| Istruzione eseguita | PC | R1 | R2 | MEM[300] |
|---|:-:|:-:|:-:|:-:|
| (stato iniziale) | 120 | 0 | 0 | 20 |
| `LOAD R1, [300]` | 121 | 20 | 0 | 20 |
| `LOAD R2, [301]` | 122 | 20 | 5 | 20 |
| `ADD R1, R1, R2` | 123 | 25 | 5 | 20 |
| `STORE [300], R1` | 124 | 25 | 5 | 25 |

📌 **Controllo.** A ogni istruzione, oltre al PC, cambia al massimo un registro dei dati oppure una cella di memoria. Il PC passa sempre all'istruzione successiva: non diventa mai 300, perché 300 è l'indirizzo di un dato.

⚠️ **Errore comune:** scrivere `MEM[300] = 25` già dopo l'`ADD`. L'`ADD` cambia solo R1: la memoria cambia soltanto con la `STORE`.

🧠 <u>Un'istruzione alla volta, un cambiamento alla volta.</u>

### 3.2 ✏️ Pratica · ✅ · 🎯 Da provare — Tre volte la dose

**Consegna.** Ecco un altro programma (valori inventati).

| Cella | Istruzione |
|---:|---|
| 140 | `LOAD R1, [310]` |
| 141 | `ADD R2, R1, R1` |
| 142 | `ADD R3, R2, R1` |
| 143 | `STORE [311], R3` |
| 144 | `STORE [310], R2` |
| 145 | `HALT` |

**Stato iniziale:** `PC = 140`, `R1 = R2 = R3 = 0`, `MEM[310] = 6`, `MEM[311] = 0`. Esegui le prime cinque istruzioni, una alla volta, e riempi la tabella.

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[310] | MEM[311] |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| `LOAD R1, [310]` | `__` | `__` | `__` | `__` | `__` | `__` |
| `ADD R2, R1, R1` | `__` | `__` | `__` | `__` | `__` | `__` |
| `ADD R3, R2, R1` | `__` | `__` | `__` | `__` | `__` | `__` |
| `STORE [311], R3` | `__` | `__` | `__` | `__` | `__` | `__` |
| `STORE [310], R2` | `__` | `__` | `__` | `__` | `__` | `__` |

<details>
<summary>🃏 <b>3.2 — Soluzione</b></summary>

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[310] | MEM[311] |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| `LOAD R1, [310]` | 141 | 6 | 0 | 0 | 6 | 0 |
| `ADD R2, R1, R1` | 142 | 6 | 12 | 0 | 6 | 0 |
| `ADD R3, R2, R1` | 143 | 6 | 12 | 18 | 6 | 0 |
| `STORE [311], R3` | 144 | 6 | 12 | 18 | 6 | 18 |
| `STORE [310], R2` | 145 | 6 | 12 | 18 | 12 | 18 |

⚠️ **Errori comuni:** `ADD R2, R1, R1` letta come R2 = 1 o R2 = 6 (somma R1 con se stesso: 12). `STORE [310], R2` scambiata con una `LOAD` (R2 invariato) invece di modificare `MEM[310]`.

📌 `R3 = R2 + R1 = 12 + 6 = 18`. La destinazione è sempre il **primo** registro indicato nell'istruzione `ADD`.

</details>

### 3.3 📖 Teoria · ✅ · 🎯 Da provare — Che cosa passa sui bus

**Consegna.** Completa la tabella indicando che cosa passa sui tre bus durante le operazioni descritte. Usa il programma dell'esercizio 3.2; nella terza riga, considera `R3 = 18`.

| Che cosa succede | Bus indirizzi | Bus di controllo | Bus dati |
|---|---|---|---|
| Fetch dell'istruzione della cella 140 | `__` | `__` | `__` |
| Lettura del dato richiesto dalla `LOAD R1, [310]` | `__` | `__` | `__` |
| Scrittura della `STORE [311], R3` | `__` | `__` | `__` |

<details>
<summary>🃏 <b>3.3 — Soluzione</b></summary>

| Che cosa succede | Bus indirizzi | Bus di controllo | Bus dati |
|---|---|---|---|
| Fetch della cella 140 | 140 | READ | `LOAD R1, [310]`, dalla memoria alla CPU |
| Lettura del dato | 310 | READ | 6, dalla memoria alla CPU |
| Scrittura della `STORE` | 311 | WRITE | 18, dalla CPU alla memoria |

🧠 <u>Indirizzi: dove. Dati: che cosa. Controllo: quale azione.</u> Nel modello semplificato di questi esercizi, la CPU invia l'indirizzo alla memoria.

</details>

### 3.4 📖 Teoria · 🔍 · 🎯 Da provare — Il fetch con MAR e MDR

**Consegna.** Prima del fetch dell'istruzione della cella 142, `ADD R3, R2, R1`, il PC vale 142 e `MAR = 0`, `MDR = 0`, l'IR è vuoto. Scrivi i valori di MAR, MDR, IR e PC **dopo ciascun passo**. Poi rispondi: la `ADD` ha bisogno di leggere la memoria nella fase di execute? E la `LOAD` della cella 140?

| Passo | Che cosa succede | MAR | MDR | IR | PC |
|---:|---|:-:|:-:|:-:|:-:|
| 1 | Il MAR riceve il valore del PC. | `__` | `__` | `__` | `__` |
| 2 | La CU chiede **READ**. | `__` | `__` | `__` | `__` |
| 3 | L'istruzione passa dalla memoria all'MDR. | `__` | `__` | `__` | `__` |
| 4 | L'istruzione passa dall'MDR all'IR. | `__` | `__` | `__` | `__` |
| 5 | Il PC avanza. | `__` | `__` | `__` | `__` |

<details>
<summary>🃏 <b>3.4 — Soluzione</b></summary>

| Passo | MAR | MDR | IR | PC |
|---:|:-:|:-:|:-:|:-:|
| 1 | 142 | 0 | vuoto | 142 |
| 2 | 142 | 0 | vuoto | 142 |
| 3 | 142 | `ADD R3, R2, R1` | vuoto | 142 |
| 4 | 142 | `ADD R3, R2, R1` | `ADD R3, R2, R1` | 142 |
| 5 | 142 | `ADD R3, R2, R1` | `ADD R3, R2, R1` | 143 |

Nel passo 2 i registri non cambiano: la CU invia il segnale di lettura alla memoria.

La **`ADD`** usa solo registri: la memoria non viene letta di nuovo. La **`LOAD R1, [310]`** invece legge la memoria **due volte**: prima con MAR = 140 (MDR = l'istruzione), poi con MAR = 310 (MDR = 6).

</details>

### 3.5 🤓 · 🎯 Da provare — Non annaffiare

> Un salto condizionato `BEQ R1, R2, fine` cambia il PC solo se `R1` e `R2` sono uguali. Qui R2 vale sempre 0.
>
> | Cella | Istruzione |
> |---:|---|
> | 160 | `LOAD R1, [320]` |
> | 161 | `BEQ R1, R2, fine` |
> | 162 | `STORE [321], R1` |
> | 163 | `fine: HALT` |
>
> **Consegna.** Con `MEM[321] = 9` all'inizio, scrivi gli indirizzi delle istruzioni eseguite e il valore finale di `MEM[321]` in due casi: `MEM[320] = 0` e `MEM[320] = 4`.

<details>
<summary>🃏 <b>3.5 — Soluzione</b></summary>

- `MEM[320] = 0`: R1 = 0 = R2, la `BEQ` salta. Indirizzi: **160 → 161 → 163**. `MEM[321]` resta 9.
- `MEM[320] = 4`: R1 = 4 ≠ 0, la `BEQ` non salta. Indirizzi: **160 → 161 → 162 → 163**. `MEM[321]` diventa 4.

Il salto cambia **quale istruzione viene dopo**, non il valore dei registri.

</details>

---

## 🛠️ Dossier 4 · Indirizzi, bus e capacità

*Si usa S5: bit e indirizzi, byte e parole, bus.*

### 📜 Caso vero: tre macchine, tre potenze di due

Tre macchine, alcuni numeri che sembrano casuali e invece si collegano alle **potenze di due**.

- **EDSAC** (1949): 512 parole di memoria. Sono 2⁹: bastano 9 bit per scrivere un indirizzo.
- **Apollo Guidance Computer**, il computer di bordo delle missioni Apollo: 2 048 parole di RAM (2¹¹) e 36 864 parole di memoria a sola lettura. Girava a 2,048 MHz. Una parola era fatta di 16 bit: 15 di dato e 1 di controllo.
- **IBM PC** (1981), con il processore Intel 8088: **20 linee di indirizzo**. Con 20 bit si distinguono 2²⁰ = 1 048 576 posizioni, cioè **1 MiB**. Ma la RAM arrivava a **640 KB**: i restanti 384 KB dello spazio erano riservati a ROM, memoria video e altre periferiche.

È la storia più famosa del «limite dei 640 KB». <u>Lo spazio degli indirizzi non è la RAM che hai montato</u>: dice quante posizioni si possono distinguere, non quante ne esistono.

🧠 <u>Con n bit si distinguono 2ⁿ posizioni. Ogni bit in più le raddoppia.</u>

### 4.1 ✏️ Pratica · ✅ · 🟢 Svolto — Da quante celle a quanti bit

**Consegna.** Per ogni macchina, calcola il numero di bit dell'indirizzo oppure il numero di locazioni richiesto.

| Macchina | Dato | Da trovare |
|---|---|---|
| EDSAC | 512 locazioni | bit dell'indirizzo |
| Apollo (RAM) | 2 048 locazioni | bit dell'indirizzo |
| IBM PC | 20 bit di indirizzo, 1 byte per locazione | locazioni e capacità |

**Svolgimento.**

1. **EDSAC.** Raddoppia: 1, 2, 4, 8, 16, 32, 64, 128, 256, **512**. Ci vogliono 9 raddoppi: **9 bit**. Indirizzi da 0 a 511.
2. **Apollo.** Dopo 512 (2⁹) si raddoppia due volte: 1 024, **2 048**. Sono 2¹¹: **11 bit**. Indirizzi da 0 a 2 047.
3. **IBM PC.** 2²⁰ = **1 048 576 locazioni**. Con 1 byte per locazione sono 1 048 576 byte, cioè **1 MiB**. L'ultimo indirizzo è 1 048 575.

📌 **Controllo.** Il numero di locazioni non è l'ultimo indirizzo: parte da 0, quindi l'ultimo è uno in meno.

⚠️ **Errore comune:** pensare che 11 bit diano 11 locazioni, o 22. Il numero di locazioni cresce **per raddoppi**, non in proporzione.

### 4.2 ✏️ Pratica · ✅ · 🎯 Da provare — La memoria della stazione meteo

**Consegna.** Una stazione meteo registra una misura di temperatura ogni minuto. Ogni misura occupa 8 bit, cioè **1 byte**. Il museo la conserva in una memoria con indirizzi a **13 bit** (valori inventati).

a) Quante locazioni ha questa memoria?
b) Qual è l'ultimo indirizzo?
c) Qual è la capacità, se ogni locazione è da 1 byte?
d) Se ogni locazione contenesse **2 byte** invece di 1, che cosa cambierebbe: il numero di locazioni o la capacità totale?

<details>
<summary>🃏 <b>4.2 — Soluzione</b></summary>

a) 2¹³ = **8 192** locazioni. b) **8 191**. c) 8 192 × 1 byte = **8 192 byte**, cioè 8 KiB. d) Cambia la **capacità**: 8 192 × 2 = 16 384 byte, cioè 16 KiB. Il numero di indirizzi resta 8 192.

⚠️ **Errore comune:** dire che, raddoppiando i byte per locazione, servono più bit di indirizzo. Servirebbe un bit in più solo se raddoppiassero le **locazioni**.

</details>

### 4.3 ✏️ Pratica · 🔍 · 🎯 Da provare — Quanti bit servono

**Consegna.** Il museo vuole poter raggiungere almeno **3 000 locazioni**. Qual è il numero minimo di bit necessario per gli indirizzi? Quante locazioni si possono distinguere con quel numero di bit? E se dovesse raggiungerne 36 864, come la ROM dell'Apollo, quanti bit servirebbero nel nostro modello?

<details>
<summary>🃏 <b>4.3 — Soluzione</b></summary>

Con 11 bit si distinguono 2 048 locazioni: poche. Con **12 bit** se ne distinguono **4 096**: bastano. Quindi servono **12 bit**, e le locazioni distinte sono 4 096 (ne avanzano 1 096).

Per 36 864: con 15 bit sono 32 768, poche; con **16 bit** sono 65 536. Nel nostro modello servono **16 bit**. Il vero computer dell'Apollo usava altri meccanismi che qui non studiamo.

📌 Si cerca la prima potenza di due **maggiore o uguale** al numero richiesto.

</details>

### 4.4 📖 Teoria · ✅ · 🎯 Da provare — Quale bus?

**Consegna.** Per ciascuna frase, indica a quale bus si riferisce: indirizzi, dati o controllo.

A. «Voglio la cella 305.»
B. «Scrivi!»
C. «Il valore da scrivere è 17.»

Poi spiega in una frase: un bus dati largo 16 bit dimostra che la memoria ha solo 2¹⁶ byte?

<details>
<summary>🃏 <b>4.4 — Soluzione</b></summary>

A. **Indirizzi** (dove). B. **Controllo** (quale azione, qui WRITE). C. **Dati** (quale contenuto).

**No.** La larghezza del bus dati dice quanto si trasferisce in un colpo; è la larghezza del bus **indirizzi** a dire quante posizioni si distinguono.

</details>

### 4.5 📖 Teoria · 🔍 · 🎯 Da provare — Perché 640 e non 1 024

**Consegna.** L'IBM PC poteva indirizzare 1 MiB di spazio, ma solo 640 KB erano disponibili come RAM per i programmi. Spiega in due o tre frasi a che cosa era riservata la parte restante. Poi rispondi: se oggi la scheda tecnica di un computer indica «16 GB di RAM» e «512 GB di SSD», che cosa non devi fare con questi due valori?

<details>
<summary>🃏 <b>4.5 — Soluzione</b></summary>

Gli altri 384 KB dello spazio di indirizzi erano **riservati** a ROM, memoria video e altre periferiche: non erano RAM per i programmi. Lo spazio di indirizzi dice quante posizioni si possono distinguere, non quanta RAM è installata.

Non devi **sommarli**: RAM e SSD hanno funzioni diverse. La RAM contiene i programmi e i dati in uso; l'SSD conserva i file anche quando il computer è spento. Dire «528 GB di RAM» sarebbe quindi sbagliato.

</details>

### 4.6 🤓 · 🎯 Da provare — Perché i PC a 32 bit «perdevano» RAM

> Con 32 bit di indirizzo e 1 byte per locazione si distinguono 2³² = 4 294 967 296 posizioni, cioè **4 GiB**. Ma non tutti gli indirizzi corrispondono a RAM: una parte era riservata ai dispositivi. Per questo molti PC con sistemi a 32 bit «vedevano» meno RAM di quella montata.
>
> **Consegna.** In una frase, che somiglianza c'è con il limite dei 640 KB?

<details>
<summary>🃏 <b>4.6 — Soluzione</b></summary>

In entrambi i casi lo spazio degli indirizzi era più grande della RAM utilizzabile: una parte era riservata ad altro. <u>Una formula è affidabile quando le sue ipotesi sono scritte chiaramente.</u>

</details>

---

## 🛠️ Dossier 5 · Gerarchia e cache

*Si usa S5 e S6: livelli di memoria, volatilità, hit e miss, località.*

### 📜 Scena verosimile: la scheda del portatile (inventata)

Chiara deve comprare un portatile per la scuola. Il negozio le mostra la scheda (valori inventati): *processore con 8 MB di cache, 8 GB di RAM, 256 GB di SSD.* Lei chiede: «Quindi ho 8 + 8 + 256 gigabyte di memoria, giusto?». Il tecnico sorride: «Sono tre cose diverse».

Nessuna memoria è insieme grande, veloce, economica e capace di tenere i dati senza corrente. Per questo i computer ne usano **più livelli**. I programmi e i file in uso vengono caricati in RAM; la cache, invece, la gestisce l'hardware da solo.

🧠 <u>«Grande» non vuol dire «veloce». E «veloce» non vuol dire «permanente».</u>

### 5.1 📖 Teoria · ✅ · 🟢 Svolto — Leggi la scheda

**Consegna.** Per la scheda di Chiara, dì per ogni riga **a che cosa serve** e **che cosa succede se si spegne la corrente**.

**Svolgimento.**

| Riga | A che cosa serve | Se si spegne la corrente |
|---|---|---|
| Cache 8 MB | Tiene **copie** di pezzi usati spesso, vicino alla CPU | Si perde (volatile) |
| RAM 8 GB | Tiene i programmi e i dati **in uso ora** | Si perde (volatile) |
| SSD 256 GB | Conserva i file e i progetti a lungo | Resta (non volatile) |

📌 **Controllo.** I tre numeri non si sommano: sono memorie diverse, con ruoli diversi. Più RAM permette di tenere pronti più dati; non rende più veloce il calcolo della CPU.

⚠️ **Errore comune:** pensare che la cache sia «un pezzo di RAM in più» dove il programma sceglie dove scrivere. È una **copia** gestita dall'hardware.

### 5.2 ✏️ Pratica · ✅ · 🎯 Da provare — La scala delle memorie

**Consegna.** Completa la tabella per i quattro livelli. Per «velocità» e «capacità», indica se il valore è maggiore o minore rispetto al livello successivo. Per l'SSD, confronta i valori con quelli della RAM.

| Livello | Volatile? | Velocità | Capacità |
|---|:-:|:-:|:-:|
| Registri | `__` | `__` | `__` |
| Cache | `__` | `__` | `__` |
| RAM | `__` | `__` | `__` |
| SSD | `__` | `__` | `__` |

<details>
<summary>🃏 <b>5.2 — Soluzione</b></summary>

| Livello | Volatile? | Velocità | Capacità |
|---|:-:|:-:|:-:|
| Registri | sì | più veloce di tutti | meno di tutti |
| Cache | sì | più veloce della RAM | meno della RAM |
| RAM | sì | più veloce dell'SSD | meno dell'SSD |
| SSD | **no** | meno veloce | più capiente |

⚠️ **Errore comune:** pensare che la persistenza cresca un po' alla volta scendendo nella gerarchia. È una proprietà **separata**: o c'è o non c'è.

</details>

### 5.3 ✏️ Pratica · ✅ · 🟢 Svolto — Hit e miss, blocchi da 4

**Consegna.** La cache conserva **blocchi di 4 posizioni consecutive** (… 48-51, 52-55, 56-59 …). Un programma legge, in ordine, gli indirizzi **52, 53, 54, 55, 56, 57, 58**. Cache vuota all'inizio; nessun blocco viene sostituito. Per ogni lettura scrivi HIT o MISS.

**Svolgimento.**

| Lettura | Blocco | Esito | Perché |
|---:|---|---|---|
| 52 | 52-55 | **MISS** | Cache vuota: carica tutto il blocco |
| 53 | 52-55 | HIT | Era già stato caricato |
| 54 | 52-55 | HIT | Idem |
| 55 | 52-55 | HIT | Idem |
| 56 | 56-59 | **MISS** | Blocco nuovo |
| 57 | 56-59 | HIT | Era già stato caricato |
| 58 | 56-59 | HIT | Idem |

📌 **Controllo.** 2 MISS e 5 HIT. I MISS sono uno per ogni blocco nuovo. Un hit può riguardare un indirizzo **mai chiesto prima**: basta che il suo blocco sia già in cache.

🧠 <u>Dopo un indirizzo possono servire i vicini: è la località spaziale.</u>

### 5.4 ✏️ Pratica · 🔍 · 🎯 Da provare — Il loop che si ripete

**Consegna.** Un programma legge in sequenza tre misure agli indirizzi **90, 91 e 92**, poi ricomincia dall'indirizzo 90. Ripete questa sequenza **100 volte**. I blocchi della cache contengono 4 posizioni (88-91 e 92-95). All'inizio la cache è vuota.

a) Se la cache ha spazio per più blocchi, quanti MISS ci sono in tutto?
b) Quale tipo di località rende le ripetizioni più veloci?
c) Ora il programma ripete per **100 volte** la coppia di letture **90, 92**. La cache ha **una sola linea**: ogni MISS sostituisce il blocco presente. Quanti MISS si verificano in tutto?

<details>
<summary>🃏 <b>5.4 — Soluzione</b></summary>

a) **2 MISS**: uno per il blocco 88-91 (con 90 e 91) e uno per il blocco 92-95. Le altre 298 letture sono HIT.
b) La **località temporale**: si riusano gli stessi dati. (Il 91 è anche un caso di località spaziale: è nel blocco del 90.)
c) **200 MISS**: 90 e 92 stanno in blocchi diversi. A ogni lettura il blocco giusto è appena stato sostituito dall'altro.

⚠️ **Errore comune:** credere che rileggere un dato garantisca un HIT. Dipende dallo spazio: con una sola linea il blocco viene sostituito prima di tornare utile.

</details>

### 5.5 📖 Teoria · ✅ · 🎯 Da provare — Le frasi del tecnico

**Consegna.** Correggi ciascuna frase in una riga.

A. «Un miss significa che il programma è rotto.»
B. «La cache da 8 MB è un pezzo di RAM in più.»
C. «Se raddoppio la RAM, il processore calcola il doppio più in fretta.»

<details>
<summary>🃏 <b>5.5 — Soluzione</b></summary>

A. **No.** Un miss è un evento previsto: il dato non è in cache e va preso dal livello successivo, con un'attesa in più.
B. **No.** La cache è una **copia** di alcuni contenuti, tenuta vicino alla CPU: non è uno spazio in più in cui scegliere dove scrivere.
C. **No.** Più RAM permette di tenere pronti più programmi e dati; non cambia la velocità con cui la CPU calcola.

</details>

---

## 🛠️ Dossier 6 · Il clock

*Si usa S6: clock, frequenza, periodo.*

### 📜 Caso vero: la corsa ai GHz

Nel novembre del 2000 Intel presenta il **Pentium 4**. La sua frequenza di clock sale, negli anni, da **1,3 GHz a 3,8 GHz**. Per un periodo, la scritta «GHz» sulla scatola diventa il numero con cui si confrontano i computer: più è alto, si pensa, meglio è.

Ma il clock è solo un **ritmo**: dice quanto dura un ciclo, non quanto lavoro si fa in ciascuno. Un processore veloce può restare fermo ad aspettare i dati.

🧠 <u>Il clock dà il tempo. Quanto lavoro si fa in quel tempo è un'altra domanda.</u>

### 6.1 ✏️ Pratica · ✅ · 🟢 Svolto — Dal GHz al nanosecondo

**Consegna.** Calcola la durata di un ciclo di clock (il **periodo**) per un processore con frequenza di 3,8 GHz e per uno con frequenza di 1,3 GHz.

**Svolgimento.** Il periodo è l'inverso della frequenza: `T = 1 ÷ f`.

1. **3,8 GHz** = 3,8 × 10⁹ Hz. `T = 1 ÷ (3,8 × 10⁹) ≈ 0,263 ns`.
2. **1,3 GHz** = 1,3 × 10⁹ Hz. `T = 1 ÷ (1,3 × 10⁹) ≈ 0,769 ns`.

📌 **Controllo.** Frequenza più alta, periodo più corto: 3,8 GHz ha un ciclo più breve di 1,3 GHz.

⚠️ **Errore comune:** dire che 3,8 GHz «completa 3,8 miliardi di istruzioni al secondo». Sono **cicli** al secondo.

### 6.2 ✏️ Pratica · ✅ · 🎯 Da provare — Quanto dura un ciclo

**Consegna.** Due processori (valori inventati): **A** ha un clock da 2,5 GHz, **B** da 500 MHz.

a) Quanto dura un ciclo di A? E uno di B?
b) Quale dei due ha il ciclo più corto?
c) Quanti cicli compie ciascuno in **1 microsecondo** (1 µs = 10⁻⁶ s)?

<details>
<summary>🃏 <b>6.2 — Soluzione</b></summary>

a) A: `1 ÷ (2,5 × 10⁹) = 0,4 ns`. B: `1 ÷ (5 × 10⁸) = 2 ns`.
b) **A**: frequenza più alta, periodo più corto.
c) A: 2,5 × 10⁹ × 10⁻⁶ = **2 500 cicli**. B: 5 × 10⁸ × 10⁻⁶ = **500 cicli**.

📌 Frequenza e periodo sono **inversi**: se uno cresce, l'altro cala.

</details>

### 6.3 📖 Teoria · ✅ · 🎯 Da provare — Vero o falso, GHz

**Consegna.** Scrivi vero o falso, e correggi se serve.

A. «Un clock da 3 GHz significa tre miliardi di istruzioni al secondo.»
B. «A 1 GHz un ciclo dura un nanosecondo.»
C. «Più GHz significano una cache più grande.»

<details>
<summary>🃏 <b>6.3 — Soluzione</b></summary>

A. **Falso.** Sono tre miliardi di **cicli** al secondo. Quante istruzioni si completano dipende da quanti cicli ne servono.
B. **Vero.** `T = 1 ÷ 10⁹ s = 1 ns`.
C. **Falso.** Frequenza e capacità della cache sono cose diverse.

</details>

### 6.4 ✏️ Pratica · 🔍 · 🎯 Da provare — Chi fa più lavoro?

**Consegna.** Considera due processori (valori inventati). Il processore **A** ha una frequenza di 2 GHz e completa un'istruzione ogni 2 cicli. Il processore **B** ha una frequenza di 3 GHz e completa un'istruzione ogni 4 cicli. Quante istruzioni al secondo completa ciascun processore? Quale dei due ne completa di più?

<details>
<summary>🃏 <b>6.4 — Soluzione</b></summary>

A: 2 × 10⁹ cicli al secondo ÷ 2 cicli per istruzione = **1 miliardo** di istruzioni al secondo.
B: 3 × 10⁹ ÷ 4 = **750 milioni** di istruzioni al secondo.

Ne fa di più **A**, anche con meno GHz. Per confrontare due sistemi bisogna guardare il lavoro svolto e il tempo impiegato, non solo i GHz sulla scatola.

⚠️ È un modello semplificato: le CPU reali fanno più cose insieme. Lo vedremo a novembre-dicembre.

</details>

### 6.5 🤓 · 🎯 Da provare — Più transistor, non per forza più veloce

> Nel 1965 Gordon Moore descrisse una tendenza: il numero di componenti inseribili in un chip aumentava nel tempo. Non si tratta di una legge della natura.
>
> **Consegna.** Perché un programma non diventa necessariamente più veloce quando un chip contiene più transistor? Fai un esempio che riguardi la cache.

<details>
<summary>🃏 <b>6.5 — Soluzione</b></summary>

Più transistor possono diventare più cache, più core o nuove funzioni. Il vantaggio dipende da come sistema e programma li usano: un calcolatore velocissimo può comunque restare fermo ad aspettare i dati. La domanda utile è: **quale risorsa limita questo lavoro?**

</details>

---

## 🛠️ Dossier 7 · Ricostruisci la macchina

*Livello finale. Si usa tutto S1–S6.*

Il museo ha rimesso in funzione la macchina. Prima di riaprire la sala, vi chiede di collaudarla con tre prove che mettono insieme gli argomenti studiati.

### 7.1 ✏️ Pratica · 🔍 · 🎯 Da provare — Somma tre misure

**Consegna.** Usando solo le istruzioni `LOAD`, `ADD`, `STORE` e `HALT`, scrivi un programma che **sommi le misure di tre sensori**. Le misure si trovano nelle celle `MEM[410]`, `MEM[411]` e `MEM[412]`; il programma deve scrivere la somma in `MEM[413]`. Ogni istruzione occupa una cella. Inizia dalla cella 500.

| Cella | Istruzione |
|---:|---|
| 500 | `______________________` |
| 501 | `______________________` |
| 502 | `______________________` |
| 503 | `______________________` |
| 504 | `______________________` |
| 505 | `______________________` |
| 506 | `______________________` |

<details>
<summary>🃏 <b>7.1 — Soluzione</b></summary>

| Cella | Istruzione |
|---:|---|
| 500 | `LOAD R1, [410]` |
| 501 | `LOAD R2, [411]` |
| 502 | `LOAD R3, [412]` |
| 503 | `ADD R1, R1, R2` |
| 504 | `ADD R1, R1, R3` |
| 505 | `STORE [413], R1` |
| 506 | `HALT` |

Sono corretti i programmi che:
1. leggono i tre valori con tre istruzioni `LOAD`;
2. li sommano con due istruzioni `ADD` (il registro di destinazione è il primo indicato);
3. scrivono il risultato in `MEM[413]` con `STORE` (l'indirizzo è il primo argomento);
4. terminano con `HALT`.

Puoi scegliere registri e ordine diversi, purché il risultato scritto in memoria sia la somma dei tre valori.

⚠️ **Errori comuni:** `LOAD R1, 410` senza parentesi (il numero 410 al posto del contenuto); `STORE R1, [413]` con gli argomenti scambiati; una `ADD` prima di aver caricato i registri.

</details>

### 7.2 ✏️ Pratica · 🔍 · 🎯 Da provare — Il collaudo del programma

**Consegna.** Esegui il programma dell'esercizio 7.1 con questi valori iniziali: `MEM[410] = 5`, `MEM[411] = 10`, `MEM[412] = 15`, `MEM[413] = 0`, `PC = 500` e tutti i registri a 0.

a) Quanto valgono R1, R2 e R3 alla fine?
b) Quanto vale `MEM[413]`?
c) Durante l'esecuzione della `STORE`, che cosa passa sul bus degli indirizzi, sul bus dati e sul bus di controllo?
d) In quel momento, quanto valgono MAR e MDR?

<details>
<summary>🃏 <b>7.2 — Soluzione</b></summary>

a) **R1 = 30**, **R2 = 10**, **R3 = 15**. b) **`MEM[413] = 30`**.

c) Bus indirizzi: **413**. Bus dati: **30**, dalla CPU alla memoria. Bus di controllo: **WRITE**.
d) **MAR = 413** e **MDR = 30**: il MAR tiene l'indirizzo, l'MDR il contenuto che viene scritto.

</details>

### 7.3 📖 Teoria · 🔍 · 🎯 Da provare — «Basta più GHz»?

**Consegna.** Un compagno vuole comprare un portatile per programmare e dice: «Basta scegliere il processore con più GHz». Rispondi in tre o quattro frasi. Cita almeno tre elementi fra questi: clock, cache, RAM e SSD.

<details>
<summary>🃏 <b>7.3 — Soluzione</b></summary>

Una risposta buona dice **che cosa** (la tesi), **come** funziona (il meccanismo) e porta un **esempio**. Per esempio:

«No, i GHz da soli non bastano. Indicano quanti cicli di clock avvengono in un secondo, non quante istruzioni si completano. Se il processore deve aspettare i dati, una frequenza più alta può non essere sufficiente: conta anche se i dati sono già nella cache (hit) o devono essere letti dalla RAM (miss). I programmi in uso sono conservati nella RAM, che perde i dati quando il computer si spegne; l'SSD, invece, conserva i file. Per esempio, più RAM può aiutare a lavorare con progetti più grandi, ma non aumenta da sola la velocità di calcolo della CPU.»

📌 Controlla: hai separato **clock**, **cache**, **RAM** e **SSD**? Hai evitato «è più veloce» senza dire perché?

</details>

---

## 📚 Fonti e risorse

Le informazioni storiche contrassegnate con 📜 provengono dalle pagine seguenti. Sono un buon punto di partenza; se ti serve un dato per una ricerca, verificalo anche su un'altra fonte.

- **EDSAC.** [EDSAC](https://en.wikipedia.org/wiki/EDSAC): 6 maggio 1949; 512 parole da 17 bit in linee di ritardo a mercurio.
- **Apollo.** [Apollo Guidance Computer](https://en.wikipedia.org/wiki/Apollo_Guidance_Computer): 2 048 parole di RAM, 36 864 parole di ROM, 2,048 MHz, parola da 15 bit più 1 di controllo.
- **IBM PC.** [Conventional memory](https://en.wikipedia.org/wiki/Conventional_memory): il processore 8088 aveva 20 linee di indirizzo (1 MB); i primi 640 KB erano la RAM, i restanti 384 KB riservati a sistema e periferiche.
- **Pentium 4.** [Pentium 4](https://en.wikipedia.org/wiki/Pentium_4): lanciato il 20 novembre 2000; frequenze da 1,3 GHz a 3,8 GHz.
- **ENIAC e Shannon.** Nelle dispense [S1](%28STU%29%203EI%20sett-ott%20S1%20-%20Dalle%20macchine%20alla%20CPU.md) e [S2](%28STU%29%203EI%20sett-ott%20S2%20-%20La%20macchina%20di%20Von%20Neumann.md).
