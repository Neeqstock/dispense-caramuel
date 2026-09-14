# 3EI - Settimana 6: LA PIPELINE E IL PRIMO RESPIRO DEL PC

Kit didattico completo. Il collegamento al percorso del bimestre e' nel [quadro 3EI - SETT-OTT](3EI%20-%20SETT-OTT.md).

```text
SETTIMANA 6
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] Perche' sovrapporre le istruzioni
│   ├── [1.2] IF, ID, EX, MEM, WB
│   ├── [1.3] Hazard strutturali, di dati e di controllo
│   ├── [1.4] Stallo, forwarding e branch prediction
│   └── [1.5] Lettura di una tabella temporale
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] Cablaggio del front panel
│   ├── [2.2] Checklist prima dell'accensione
│   ├── [2.3] POST e beep code
│   └── [2.4] Diagnosi e avvio della relazione tecnica
└── 📋 GUIDA DI REGIA PER IL DOCENTE
	├── Cronoprogramma di circa 110 minuti
	├── Disegno della pipeline alla lavagna
	└── Micro-task formativo per casa
```

## 🧠 MODULO TEORICO (2 Ore in Aula)

### ├── [1.1] La pipeline: piu' lavoro nello stesso tempo

Senza pipeline, una CPU potrebbe completare tutte le fasi di un'istruzione prima di iniziare la successiva. La pipeline divide il lavoro in stadi e sovrappone istruzioni diverse. E' simile a una catena di montaggio: una singola automobile non attraversa il reparto piu' rapidamente, ma a regime escono piu' automobili nello stesso intervallo.

Il modello didattico a cinque stadi e': **IF (Instruction Fetch), ID (Instruction Decode/Register Read), EX (Execute), MEM (Memory access), WB (Write-back)**. I registri tra stadi conservano dati e segnali per il ciclo successivo.

### ├── [1.2] I cinque stadi

1. **IF:** preleva l'istruzione e calcola normalmente il prossimo PC.
2. **ID:** decodifica l'IR, legge i registri e prepara gli operandi.
3. **EX:** esegue l'operazione ALU, calcola un indirizzo o valuta un confronto.
4. **MEM:** legge o scrive la memoria per load/store; per altre istruzioni il risultato attraversa lo stadio.
5. **WB:** scrive il risultato nel registro destinazione.

```text
ciclo       1    2    3    4    5    6    7
I1          IF   ID   EX   MEM  WB
I2               IF   ID   EX   MEM  WB
I3                    IF   ID   EX   MEM  WB
I4                         IF   ID   EX   MEM  WB
```

La pipeline aumenta il **throughput**, non elimina la latenza della singola istruzione. Il vantaggio teorico massimo si riduce se gli stadi hanno durate diverse, se una risorsa e' condivisa o se il flusso cambia a causa di un salto.

### ├── [1.3] Hazard strutturali, di dati e di controllo

Un **hazard** e' una situazione in cui l'istruzione successiva non puo' avanzare come previsto.

* **Strutturale:** due stadi richiedono nello stesso ciclo una risorsa unica, per esempio una sola memoria per fetch e accesso dati. Si risolve duplicando la risorsa o inserendo uno stallo.
* **Di dati:** un'istruzione usa un valore prodotto da una precedente non ancora arrivata al WB. Il caso piu' comune e' RAW (Read After Write). Esistono anche WAR e WAW in pipeline piu' complesse o con esecuzione fuori ordine.
* **Di controllo:** un branch modifica il PC, ma la pipeline ha gia' prelevato istruzioni dal percorso successivo. Finche' la decisione non e' nota, il flusso e' incerto.

**Esempio RAW:** `I1: ADD R1,R2,R3` seguito da `I2: SUB R4,R1,R5`. I2 ha bisogno di R1 prima che I1 abbia completato la scrittura.

### ├── [1.4] Stallo, forwarding e branch prediction

Uno **stallo** congela uno stadio e inserisce una bubble: il risultato e' corretto ma si perde throughput. Il **forwarding** inoltra il risultato direttamente dallo stadio in cui e' disponibile all'ingresso dell'ALU, senza attendere il WB. Non tutte le dipendenze sono risolvibili cosi': una load puo' rendere disponibile il dato solo dopo MEM.

La **branch prediction** prova a prevedere se un salto sara' preso. Se la previsione e' corretta la pipeline continua; se e' errata le istruzioni speculative vengono scartate e si paga una penalita'. La predizione non “indovina il risultato del programma”: accelera un percorso che poi viene verificato.

### ├── [1.5] Tabella temporale e CPI effettivo

Il CPI ideale di una pipeline a regime puo' avvicinarsi a 1, ma hazard e cache miss aggiungono cicli. In modo semplificato:

$$CPI_{effettivo} = CPI_{ideale} + cicli\ di\ stallo\ medi\ per\ istruzione$$

La classe completa una griglia marcando `-` per una bubble e motivando ogni pausa. L'obiettivo non e' memorizzare sigle isolate, ma collegare la dipendenza all'intervento hardware.

## 💻 MODULO LABORATORIO (2 Ore con ITP)

### ├── [2.1] Cablaggio del front panel

Individuare sul manuale il connettore `F_PANEL` e collegare `Power SW`, `Reset SW`, LED di alimentazione, LED disco e buzzer/speaker. Gli switch non hanno polarita'; i LED invece devono rispettare positivo e negativo. Non basarsi sulla posizione “a memoria”: si legge la serigrafia e si verifica il manuale.

### ├── [2.2] Checklist prima dell'accensione

Controllare ATX 24-pin, CPU 4/8-pin, RAM completamente inserita, dissipatore e `CPU_FAN`, schede fissate, nessuna vite libera e cavi lontani dalle ventole. Collegare monitor e tastiera solo dopo aver verificato alimentazione e interruttore PSU. In caso di dubbio, si chiama l'ITP prima del pulsante.

### ├── [2.3] POST e beep code

Il **POST (Power-On Self-Test)** e' il controllo iniziale del firmware. Puo' mostrare logo, messaggi, memoria riconosciuta e codici di errore. I **beep code** non sono universali: cambiano con produttore, firmware e speaker installato. Si annota la sequenza esatta e la si confronta con il manuale della motherboard; non si attribuisce un significato generico senza fonte.

### ├── [2.4] Procedura a fasi e relazione (110 min)

* **FASE A - Ruoli e manuale (15 min):** assegnare responsabile sicurezza, cablaggio, osservazione e relazione.
* **FASE B - Front panel (25 min):** leggere serigrafia/manuale, collegare un gruppo alla volta e far verificare all'ITP.
* **FASE C - Preflight (20 min):** checklist firmata su alimentazioni, RAM, CPU_FAN, viti e ventilazione.
* **FASE D - Primo avvio (20 min):** osservare POST, video e beep; spegnere prima di qualsiasi intervento.
* **FASE E - Diagnosi guidata (20 min):** compilare sintomo, ipotesi, prova, risultato e prossima azione.
* **FASE F - Relazione (10 min):** aprire il documento e inserire titolo, scopo, componenti ed esito.

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma teorico (110 minuti)
* **00-10:** recupero attivo su fetch/decode/execute e domanda: “Perche' non aspettare sempre la fine?”.
* **10-30:** analogia della catena di montaggio e costruzione dei cinque stadi.
* **30-55:** griglia temporale con tre istruzioni indipendenti.
* **55-78:** inserire una dipendenza RAW e far scoprire lo stallo.
* **78-98:** forwarding, branch prediction e classificazione degli hazard.
* **98-110:** esercizio individuale, correzione e checklist del laboratorio.

### ✍️ Disegno alla lavagna
```text
I1: IF | ID | EX | MEM | WB
I2:    IF | ID | EX | MEM | WB
I3:       IF | ID | EX | MEM | WB
		  ^
		  hazard -> bubble oppure forwarding
```

### 🎯 Micro-task formativo per casa
Disegnare la pipeline di `I1: ADD R1,...` e `I2: SUB ...,R1,...`, inserendo una bubble se non e' disponibile il forwarding. Scrivere tre righe su come distinguere un problema di front panel da un errore RAM durante il POST.
