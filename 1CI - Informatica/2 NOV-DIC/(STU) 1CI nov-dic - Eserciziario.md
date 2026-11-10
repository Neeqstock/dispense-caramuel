⬅️ [S6 - Ripasso attivo](%28STU%29%201CI%20nov-dic%20S6%20-%20Ripasso%20attivo.md)

# 🏋️ Eserciziario · 1CI nov-dic

**1CI · Novembre-Dicembre · Eserciziario di ripasso**

⏱️ **Tempo: ✅ circa 30 minuti · 🔍 circa 25 minuti in più** · nessun compito a casa obbligatorio.

> **Legenda:** 📜 caso reale · 🟢 svolto: guarda come si fa · 🎯 da provare: prova da solo · ✅ base · 🔍 più impegnativo · 📖 teoria · ✏️ pratica scritta · 📌 controllo · ⚠️ errore comune · 🧠 da ricordare · 🃏 soluzione: prova prima, poi apri

Ogni parte nasce da un caso: una scena, un problema da risolvere. Prima guarda il 📜, poi il 🟢 svolto, poi prova i 🎯 da solo.

| Parte | Argomento | Livello | Esercizi |
|---|---|:-:|---:|
| 1 | Sistema operativo: processore, memoria, kernel | ✅ 🔍 | 6 |
| 2 | Boot: dalla staffetta di avvio al loop | ✅ 🔍 | 4 |
| 3 | Relè e porte: NOT, AND, OR, XOR | ✅ 🔍 | 5 |
| 4 | NAND: un mattone per tutto | ✅ 🔍 | 4 |
| 5 | Somma binaria: XOR, AND e riporto | ✅ 🔍 | 5 |

---

## Parte 1 · Il regista: sistema operativo ✅ 🔍

### 📜 1202 sulla Luna

Luglio 1969, discesa dell'Apollo 11. Il computer di bordo inizia a segnalare allarmi con codici 1201 e 1202: troppi compiti da svolgere nello stesso momento. Il software, scritto al MIT sotto la guida di Margaret Hamilton, non si blocca: scarta i compiti meno importanti e tiene quelli necessari all'atterraggio. Il problema, in parole semplici: **più lavori che tempo**. Chi decide che cosa passa per primo?

### 🟢 1.1 · Chi lavora: sistema operativo o app? ✅

**Consegna.** Per ogni voce scrivi **SO** (sistema operativo) o **App** (programma per l'utente):
a) decidere quale programma usa il processore; b) correggere l'ortografia di un documento; c) dare a due programmi spazi di memoria separati; d) far parlare la tastiera con il programma che scrivi.

**Passaggi.**
1. Chiediti: la voce parla di una **risorsa condivisa** (processore, memoria, periferiche) o di un **compito dell'utente**?
2. Risorsa condivisa → SO. Compito dell'utente → App.

Risposte: a) SO · b) App · c) SO · d) SO (il driver della tastiera è di base).

📌 **Controllo:** se un programma non può decidere da solo, lo fa il SO.
⚠️ **Errore comune:** «Word è il sistema operativo». Word è un'app: usa il SO per usare il processore.
🧠 <u>Il sistema operativo gestisce le risorse; le app le chiedono a lui.</u>

### 🟢 1.2 · Quattro turni per tre processi 🔍

**Consegna.** Tre processi arrivano tutti a t = 0, nell'ordine A, B, C. Lavoro necessario: **A = 5 ms**, **B = 3 ms**, **C = 2 ms** (dati inventati). Il processore dà a ciascuno un turno di al massimo **2 ms** (quanto), poi passa al successivo in coda. Scrivi i turni e l'istante in cui finisce ognuno.

**Passaggi.**
1. Coda iniziale: A, B, C.
2. A usa 2 ms (resta 3). Coda: B, C, A.
3. B usa 2 ms (resta 1). Coda: C, A, B.
4. C usa 2 ms: **finisce a 6 ms**. Coda: A, B.
5. A usa 2 ms (resta 1). Coda: B, A.
6. B usa 1 ms: **finisce a 9 ms**. Coda: A.
7. A usa 1 ms: **finisce a 10 ms**.

Turni: A 0–2 · B 2–4 · C 4–6 · A 6–8 · B 8–9 · A 9–10.

📌 **Controllo:** 5 + 3 + 2 = 10 ms, e l'ultimo istante è 10.
⚠️ **Errore comune:** dare per finito un processo solo perché ha avuto un turno. Se gli restano ms, torna in coda.
🧠 <u>Il round robin non sceglie per importanza: fa il giro.</u> A Hamilton servivano le priorità, come nel 1202.

### 🎯 1.3 · Il telefono sovraccarico ✅ ✏️

**Consegna.** Il telefono è pieno: navigatore (priorità alta), musica (media), notifiche di un gioco (bassa). La memoria si esaurisce. Quali processi tiene il sistema operativo, e quale scarta per primo? Spiega in una frase perché, come sulla Luna.

<details>
<summary>🃏 <b>1.3 — Soluzione</b></summary>

Scarta le notifiche del gioco: hanno priorità bassa e non servono a nulla di essenziale. Tiene il navigatore, il compito essenziale, come l'atterraggio nel 1202.

</details>

### 🎯 1.4 · Kernel o sistema operativo? ✅ 📖

**Consegna.** In una frase, spiega la differenza fra **kernel** e **sistema operativo**.

<details>
<summary>🃏 <b>1.4 — Soluzione</b></summary>

Il kernel è il nucleo che parla direttamente con l'hardware; il sistema operativo è l'insieme: kernel, servizi, interfaccia e programmi di base.

</details>

### 🎯 1.5 · RAM e disco dopo lo spegnimento ✅ ✏️

**Consegna.** Il PC si spegne all'improvviso. Scrivi che cosa si **perde** e che cosa **resta**: un documento non salvato; una foto salvata sul disco.

<details>
<summary>🃏 <b>1.5 — Soluzione</b></summary>

Si perde il documento non salvato, che stava nella RAM. Resta la foto, che sta sul disco.

</details>

### 🎯 1.6 · Perché l'app non tocca il disco da sola? 🔍 ✏️

**Consegna.** Un'app vuole leggere un file. Perché non parla direttamente con il disco? Scrivi due motivi, con una frase ciascuno.

<details>
<summary>🃏 <b>1.6 — Soluzione</b></summary>

1. Protezione: il SO controlla i permessi, così un programma non rovina i dati di un altro.
2. Semplicità: il SO nasconde i dettagli del disco e offre un servizio uguale per tutti.

</details>

---

## Parte 2 · La staffetta: il boot ✅ 🔍

### 📜 Un aggiornamento e un riavvio infinito (2024)

Il 19 luglio 2024 un aggiornamento di un software di sicurezza (CrowdStrike Falcon) ha mandato in errore milioni di computer Windows. Il componente aggiornato girava nel **kernel**, cioè nella parte che parte per prima. Il PC si bloccava **prima** dei servizi e si riavviava di nuovo, in loop. Secondo le stime riportate, circa 8,5 milioni di dispositivi furono colpiti. Lezione del caso: se un passo della staffetta cade, quelli dopo non partono.

### 🟢 2.1 · Riordina la staffetta ✅

**Consegna.** Metti in ordine: schermata di accesso · kernel · firmware · bootloader · servizi.

**Passaggi.**
1. Chi parte per primo, all'accensione? Un programma fisso nella scheda: il **firmware**.
2. Il firmware cerca un programma di avvio: il **bootloader**.
3. Il bootloader carica il **kernel**.
4. Il kernel avvia i **servizi**.
5. Solo alla fine compare la **schermata di accesso**.

Ordine: firmware → bootloader → kernel → servizi → schermata di accesso.

📌 **Controllo:** il kernel parte prima dei servizi, e lo schermo è l'ultimo gradino.
⚠️ **Errore comune:** «il kernel si carica da solo». Lo carica il bootloader.
🧠 <u>Ogni gradino prepara il successivo.</u>

### 🟢 2.2 · Dove si ferma il PC? 🔍

**Consegna.** Il firmware parte, poi il bootloader parte, ma il kernel non si carica e compare un messaggio di errore. A quale passo ci si è fermati? Perché la schermata di accesso non compare?

**Passaggi.**
1. Individua l'ultimo passo riuscito: il bootloader.
2. Il passo che fallisce è il caricamento del kernel.
3. Servizi e schermata vengono dopo: se il kernel non parte, non partono nemmeno loro.

Risposta: ci si ferma al caricamento del kernel; la schermata non compare perché viene per ultima.

📌 **Controllo:** se un passo fallisce, tutti quelli dopo non partono.
⚠️ **Errore comune:** «non compare lo schermo, quindi il problema è lo schermo». Lo schermo è l'ultimo gradino, non il primo.
🧠 <u>Un guasto nel boot si cerca dal passo che manca, non dall'ultimo che si vede.</u>

### 🎯 2.3 · Che cosa fa il firmware? ✅ 📖

**Consegna.** In una frase, dì che cosa fa il firmware all'accensione.

<details>
<summary>🃏 <b>2.3 — Soluzione</b></summary>

È un programma fisso, nella scheda madre, che controlla l'hardware e cerca il programma di avvio (bootloader).

</details>

### 🎯 2.4 · Il riavvio che non finisce mai 🔍 ✏️

**Consegna.** Un PC mostra un errore, si riavvia, mostra di nuovo lo stesso errore, e così via. Quale tipo di guasto è più probabile: un programma che l'utente apre, o un componente che si carica a ogni avvio? Scrivi la tua risposta e il motivo in due frasi.

<details>
<summary>🃏 <b>2.4 — Soluzione</b></summary>

Un componente che si carica a ogni avvio, per esempio un driver nel kernel. Il guasto ritorna ogni volta perché il file viene caricato di nuovo; un programma aperto dall'utente parte solo dopo il sistema, quindi non può bloccarne l'avvio.

</details>

---

## Parte 3 · Un interruttore che decide: relè e porte ✅ 🔍

### 📜 Una falena nel relè (1947)

Il 9 settembre 1947, nel laboratorio di Harvard, il calcolatore Mark II, fatto di relè (interruttori comandati elettricamente), si fermò. La squadra, fra cui Grace Hopper, trovò una **falena** incastrata in un relè. La incollò nel registro con la scritta *«First actual case of bug being found»*. La pagina è conservata allo Smithsonian. Il termine *bug* esisteva già, ma questo è il caso che lo rese famoso. Il relè è il mattone; la porta è la funzione che il mattone realizza.

### 🟢 3.1 · Serie e parallelo ✅

**Consegna.** Due interruttori A e B controllano una lampadina.
- Caso 1: interruttori **in serie** (uno dopo l'altro). La lampadina è accesa solo se sono chiusi **entrambi**.
- Caso 2: interruttori **in parallelo** (uno accanto all'altro). La lampadina è accesa se è chiuso **almeno uno**.

Quale porta realizza ciascun caso? Scrivi la tabella a mano.

**Passaggi.**
1. Scrivi le quattro righe in ordine: 00, 01, 10, 11.
2. Serie: accesa solo in 11 → **AND**.
3. Parallelo: accesa in 01, 10 e 11 → **OR**.

| A | B | Serie (AND) | Parallelo (OR) |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |

📌 **Controllo:** l'AND ha un solo 1 in uscita; l'OR ne ha tre.
⚠️ **Errore comune:** scambiare serie e parallelo.
🧠 <u>Serie = tutti devono essere chiusi (AND). Parallelo = basta uno (OR).</u>

### 🟢 3.2 · L'allarme di casa 🔍

*Scenario verosimile e inventato.*

**Consegna.** Un allarme suona se **(la porta è aperta o la finestra è aperta) e** l'allarme è armato. Chiamiamo P (porta), F (finestra), R (armato). Scrivi la tabella delle 8 righe e segna quelle in cui l'allarme suona.

**Passaggi.**
1. Tre ingressi: P, F, R. Le righe sono 2³ = 8.
2. Prima calcola la parentesi: P OR F.
3. Poi fai AND con R.
4. Riga per riga, controlla il risultato.

Righe in cui suona: P=0 F=1 R=1; P=1 F=0 R=1; P=1 F=1 R=1. In tutte e tre R = 1: con l'allarme spento non suona mai.

📌 **Controllo:** la riga 110 (porta aperta, finestra aperta, allarme spento) deve dare 0.
⚠️ **Errore comune:** pensare che con due aperture suoni meno. Con l'OR suona anche se sono aperte entrambe.
🧠 <u>Prima la parentesi, poi l'AND con il terzo ingresso.</u>

### 🎯 3.3 · Dal simbolo al nome ✅ 📖

**Consegna.** Scrivi il nome della porta per ciascun simbolo: ¬ · ∧ · ∨ · ⊻ · ↔.

<details>
<summary>🃏 <b>3.3 — Soluzione</b></summary>

¬ = NOT · ∧ = AND · ∨ = OR · ⊻ = XOR (la «o… o…») · ↔ = XNOR (vero quando gli ingressi sono uguali).

</details>

### 🎯 3.4 · Trova l'errore nella tabella dell'OR 🔍 ✏️

**Consegna.** Questa tabella dell'OR contiene un errore. Trovalo, correggilo e scrivi come lo hai visto.

| A | B | A OR B |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

<details>
<summary>🃏 <b>3.4 — Soluzione</b></summary>

L'ultima riga è sbagliata: con 1 OR 1 l'uscita è **1**. L'OR è vero anche quando entrambi gli ingressi sono veri; l'«o… o…» esclusivo è lo XOR.

</details>

### 🎯 3.5 · Il Wi-Fi e la modalità aereo ✅ ✏️

**Consegna.** Il Wi-Fi è attivo se la modalità aereo **NON** è attiva. Scrivi la tabella delle due righe: modalità aereo spenta (0) e accesa (1). Quale porta è?

<details>
<summary>🃏 <b>3.5 — Soluzione</b></summary>

Spenta (0) → Wi-Fi attivo (1). Accesa (1) → Wi-Fi spento (0). È la porta **NOT**: inverte il valore.

</details>

---

## Parte 4 · Un solo mattone: NAND ✅ 🔍

### 📜 Un solo tipo di porta

Il computer di bordo dell'Apollo, progettato al MIT, fu costruito con chip che realizzavano un solo tipo di porta: la **NOR** a tre ingressi. Con un solo tipo di mattone si costruiscono tutte le altre porte. La NAND, sorella della NOR, fa lo stesso lavoro: è il punto della parte. Il vantaggio è pratico: meno tipi di pezzi da fabbricare e controllare.

### 🟢 4.1 · La NAND e il NOT ✅

**Consegna.** Completa la tabella della NAND, poi costruisci un NOT con una sola NAND.

**Passaggi.**
1. La NAND è un AND **capovolto**: prima calcola l'AND, poi inverti.
2. AND: vale 1 solo in 11. Capovolto: vale 0 solo in 11.
3. NOT: se colleghi i due ingressi della NAND insieme (entrambi A), ottieni NAND(A, A).

| A | B | A NAND B |
|:-:|:-:|:-:|
| 0 | 0 | 1 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

NOT: A = 0 → 1; A = 1 → 0. Ecco il NOT.

📌 **Controllo:** la NAND vale 0 solo quando tutti e due gli ingressi sono 1.
⚠️ **Errore comune:** NAND(0, 1) = 0 perché «c'è uno zero». No: 0 AND 1 = 0, capovolto è 1.
🧠 <u>Con gli ingressi uniti, la NAND diventa un NOT.</u>

### 🟢 4.2 · AND e OR con sole NAND 🔍

**Consegna.** Disegna un AND usando solo NAND: quante ti servono? Poi un OR: quante ti servono?

**Passaggi.**
1. AND = NOT(NAND): la prima NAND calcola NAND(A, B); la seconda, con gli ingressi uniti, la capovolge. **2 NAND.**
2. OR: negare A e B con due NAND (ingressi uniti), poi combinarli con una NAND. **3 NAND**: NAND(NAND(A, A), NAND(B, B)).
3. Verifica l'OR con la tabella: 00 → 0, 01 → 1, 10 → 1, 11 → 1.

📌 **Controllo:** AND in 2 NAND, OR in 3 NAND.
⚠️ **Errore comune:** pensare che OR = NAND(A, B). È l'AND capovolto, non l'OR.
🧠 <u>Una porta non basta per avere tutte: serve combinarle.</u>

### 🎯 4.3 · Vero o falso: «NAND = NOT A AND NOT B» ✅ 📖

**Consegna.** Con A = 1 e B = 0 calcola il valore di NAND(A, B) e di NOT A AND NOT B. L'affermazione è vera o falsa?

<details>
<summary>🃏 <b>4.3 — Soluzione</b></summary>

NAND(1, 0) = 1. NOT A AND NOT B = 0 AND 1 = 0. I valori sono diversi: **falso**. La NAND nega il risultato dell'AND, non i singoli ingressi.

</details>

### 🎯 4.4 · Lo XOR con quattro NAND 🔍 ✏️

**Consegna.** Costruisci questo circuito con quattro NAND: t = NAND(A, B); X = NAND(NAND(A, t), NAND(B, t)). Compila la tabella per le quattro combinazioni di A e B. Quale porta hai costruito?

| A | B | X |
|:-:|:-:|:-:|
| 0 | 0 | ? |
| 0 | 1 | ? |
| 1 | 0 | ? |
| 1 | 1 | ? |

<details>
<summary>🃏 <b>4.4 — Soluzione</b></summary>

X vale 0, 1, 1, 0: è lo **XOR**, vero quando gli ingressi sono diversi. Lo hai costruito con sole NAND.

</details>

---

## Parte 5 · Un circuito che conta: somma binaria ✅ 🔍

### 📜 La macchina che sommava con gli ingranaggi

Nel Seicento, intorno al 1642, Blaise Pascal costruì una macchina meccanica che sommava con ingranaggi. Il punto difficile era il **riporto**: quando una cifra supera la base, bisogna passare la cifra successiva. Oggi lo stesso problema si risolve con due porte: lo XOR per la cifra di somma, l'AND per il riporto.

### 🟢 5.1 · Sommare due bit ✅

**Consegna.** Scrivi la somma **S** e il riporto **C** per tutte le coppie: 0+0, 0+1, 1+0, 1+1.

**Passaggi.**
1. 0 + 0 = 0: S = 0, C = 0.
2. 0 + 1 = 1: S = 1, C = 0 (e lo stesso per 1 + 0).
3. 1 + 1 = 10 in binario: S = 0, C = 1.

| A | B | S | C |
|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

📌 **Controllo:** S è uno XOR di A e B; C è un AND.
⚠️ **Errore comune:** scrivere 1 + 1 = 2. In binario 2 non esiste: si scrive 10.
🧠 <u>In binario 1 + 1 = 10: somma 0, riporto 1.</u>

### 🟢 5.2 · Somma in colonna con i riporti 🔍

**Consegna.** Calcola 0110 + 0011 in colonna, da destra verso sinistra, segnando i riporti. Poi converti il risultato in decimale: che cosa ottieni?

**Passaggi.**
1. Colonna più a destra: 0 + 1 = 1, riporto 0.
2. Colonna successiva: 1 + 1 = 10 → scrivi 0, riporto 1.
3. Colonna successiva: 1 + 0 + 1 (riporto) = 10 → scrivi 0, riporto 1.
4. Colonna successiva: 0 + 0 + 1 (riporto) = 1 → scrivi 1.

Risultato: **1001**. In decimale: 8 + 1 = **9**, cioè 6 + 3.

📌 **Controllo:** il risultato decimale deve essere 6 + 3 = 9.
⚠️ **Errore comune:** dimenticare il riporto nella terza colonna, o scrivere 2 invece di 10.
🧠 <u>Il riporto entra nella colonna successiva: non si perde.</u>

### 🎯 5.3 · Lo XOR in una frase ✅ 📖

**Consegna.** Scrivi la tabella dello XOR e, in una frase, quando la sua uscita vale 1.

<details>
<summary>🃏 <b>5.3 — Soluzione</b></summary>

Tabella: 00 → 0, 01 → 1, 10 → 1, 11 → 0. L'uscita vale 1 quando i due ingressi sono **diversi**.

</details>

### 🎯 5.4 · Somma a quattro bit 🔍 ✏️

**Consegna.** Calcola 1011 + 0110 in colonna, con i riporti. Scrivi il risultato in binario e in decimale. Perché il risultato ha una cifra in più degli addendi?

<details>
<summary>🃏 <b>5.4 — Soluzione</b></summary>

Colonne da destra: 1+0 = 1; 1+1 = 10 → 0, riporto 1; 0+1+1 = 10 → 0, riporto 1; 1+0+1 = 10 → 0, riporto 1; 0+0+1 = 1. Risultato: **10001** = 17 (11 + 6). Ha una cifra in più perché il riporto finale non trova posto nelle quattro colonne.

</details>

### 🎯 5.5 · Ripasso: controlla con le conversioni ✅ ✏️

**Consegna.** Converti in decimale 1001, e in esadecimale 1010 e 1100 1000.

<details>
<summary>🃏 <b>5.5 — Soluzione</b></summary>

1001 = 9 · 1010 = A · 1100 1000 = C8 (cioè 200 in decimale).

</details>

---

## 🚪 Uscita

Scrivi su un foglio, senza guardare gli appunti:
1. un esercizio che hai fatto da solo e che ti è riuscito;
2. un errore che hai commesso e come l'hai corretto;
3. una domanda per il docente.

---

## 📚 Fonti e risorse

- [Apollo 11 Lunar Surface Journal: Program Alarms (NASA)](https://www.nasa.gov/wp-content/uploads/static/history/alsj/a11/a11.1201-fm.html): i codici 1201 e 1202 e il loro significato. Leggi la parte introduttiva.
- [CrowdStrike, Tech Alert del 19 luglio 2024](https://www.crowdstrike.com/wp-content/uploads/2024/07/Tech-Alert-Windows-crashes-related-to-Falcon-Sensor-2024-07-19.pdf): il comunicato ufficiale sull'errore. Serve a capire il loop di riavvio, non a fare operazioni sul PC.
- [Computer History Museum: 9 settembre 1947](https://www.computerhistory.org/tdih/september/9/) e [Smithsonian: registro con la falena](https://www.si.edu/object/log-book-computer-bug:nmah_334663): il caso del Mark II.
- [Apollo Guidance Computer, documentazione MIT (klabs.org)](https://www.klabs.org/history/history_docs/mit_docs/1716.pdf): le porte NOR del computer di bordo. Per curiosi.
- Gli scenari del telefono, dell'allarme di casa e i valori di 1.2 (5, 3, 2 ms) sono **verosimili e inventati**.

---

⬅️ [S6 - Ripasso attivo](%28STU%29%201CI%20nov-dic%20S6%20-%20Ripasso%20attivo.md)
