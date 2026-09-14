# 3EI - Settimana 7: COLLEGARE I PEZZI, SIMULARE E DOCUMENTARE

Kit didattico completo di ripasso attivo e laboratorio. Il quadro di riferimento resta [3EI - SETT-OTT](3EI%20-%20SETT-OTT.md).

```text
SETTIMANA 7
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] Mappa integrata del modulo
│   ├── [1.2] Ripasso attivo a stazioni
│   ├── [1.3] Simulazione della prova scritta
│   └── [1.4] Correzione ragionata e recupero mirato
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] Struttura della relazione tecnica
│   ├── [2.2] Completamento con dati e immagini
│   ├── [2.3] Peer review con griglia
│   └── [2.4] Esportazione PDF e consegna
└── 📋 GUIDA DI REGIA PER IL DOCENTE
	 ├── Cronoprogramma di circa 110 minuti
	 ├── Disegno di sintesi alla lavagna
	 └── Micro-task formativo per casa
```

## 🧠 MODULO TEORICO (2 Ore in Aula)

### ├── [1.1] La mappa integrata del modulo

Il ripasso non consiste nel rileggere tutto in ordine. La classe deve ricostruire i nessi: il modello di Von Neumann collega CPU, memoria, I/O e bus; dentro la CPU la CU usa registri e segnali per guidare ALU e memoria; la gerarchia riduce il costo degli accessi; ciclo macchina e pipeline spiegano come le istruzioni avanzano.

```text
PROGRAMMA
	│ istruzioni e dati
	▼
CPU: CU + registri + ALU
	│ ciclo fetch/decode/execute/write-back
	▼
pipeline IF-ID-EX-MEM-WB ---- hazard, stallo, forwarding
	│
memoria: registri-cache-RAM-SSD/HDD ---- hit, miss, localita'
	│
motherboard, alimentazione, POST e diagnosi
```

### ├── [1.2] Ripasso attivo a stazioni

La classe lavora in piccoli gruppi, con sei minuti per stazione e un cambio rapido. Ogni gruppo lascia una risposta tracciabile, non solo una discussione orale.

* **Stazione CPU:** etichettare ALU, CU, PC, IR, MAR, MDR e PSW in uno schema.
* **Stazione indirizzi:** calcolare la capacita' con 12, 16, 20 e 32 linee; indicare l'unita' di indirizzamento.
* **Stazione memorie:** ordinare registri, L1, L2, L3, RAM e massa; motivare due posizioni con latenza e capacita'.
* **Stazione ciclo:** riordinare fetch, decode, execute, memory e write-back per una `LOAD`.
* **Stazione architetture:** confrontare CISC/RISC senza usare l'errore “RISC sempre piu' veloce”.
* **Stazione pipeline:** classificare tre situazioni come hazard strutturale, di dati o di controllo.

### ├── [1.3] Simulazione della prova

La simulazione individuale dura 30 minuti e contiene un esercizio numerico, uno schema da completare, domande a risposta breve e una situazione diagnostica. Il procedimento vale: per $2^n$ si devono mostrare potenza e conversione; per la pipeline si devono indicare le istruzioni coinvolte; per un beep code si deve citare il manuale come fonte.

Esempio di consegna: “Un bus di indirizzi ha 20 linee e indirizza byte. Calcolare lo spazio. Descrivere poi il percorso di una istruzione dalla memoria al registro destinazione e indicare un possibile hazard per due istruzioni consecutive.”

### ├── [1.4] Correzione ragionata e recupero

La correzione separa errore di conoscenza, errore di procedimento ed errore di linguaggio. Ogni studente compila una tabella: risposta data, evidenza nel materiale, correzione, regola da ricordare. Chi confonde MAR e MDR rifà il diagramma del fetch; chi sbaglia $2^n$ riparte da bit e combinazioni; chi confonde cache e RAM spiega hit/miss con un esempio.

## 💻 MODULO LABORATORIO (2 Ore con ITP)

### ├── [2.1] Struttura della relazione tecnica

La relazione deve permettere a un altro tecnico di capire cosa e' stato fatto e ripeterlo in sicurezza. Struttura obbligatoria: titolo, autore e data; scopo; strumenti e componenti; norme ESD; procedura cronologica; osservazioni; diagnosi con sintomo-ipotesi-prova-esito; POST; conclusione e fonti.

### ├── [2.2] Completamento con dati e immagini

Il gruppo controlla modello della motherboard, socket, RAM, dischi, connettori e risultato del primo avvio. Le immagini devono avere didascalia e indicare il componente; non si inseriscono fotografie decorative o dati personali non necessari. Le tabelle devono riportare unita' di misura e distinguere dati dichiarati da osservazioni del gruppo.

### ├── [2.3] Peer review

Ogni coppia scambia la bozza con un'altra e usa tre domande: “La procedura e' ripetibile?”, “La diagnosi collega sintomo e prova?”, “Il linguaggio e le immagini sono leggibili?”. Il revisore segnala due punti riusciti e un miglioramento necessario. Non riscrive il documento del compagno: restituisce feedback motivato.

### ├── [2.4] Fasi operative (110 min)

* **FASE A - Indice e materiali (15 min):** aprire la relazione, controllare intestazione e creare le sezioni.
* **FASE B - Dati tecnici (25 min):** completare inventario e didascalie dalle schede raccolte.
* **FASE C - Procedura e diagnosi (25 min):** ordinare i passaggi e compilare la tabella sintomo/prova/esito.
* **FASE D - Peer review (20 min):** scambio tra gruppi e feedback firmato.
* **FASE E - Revisione (15 min):** recepire il miglioramento e controllare impaginazione.
* **FASE F - PDF e consegna (10 min):** esportare, riaprire il PDF, verificare e consegnare su Classroom.

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma teorico (110 minuti)
* **00-12:** recupero a risposta rapida su otto parole chiave.
* **12-32:** costruzione della mappa integrata alla lavagna.
* **32-62:** stazioni di ripasso attivo, con rotazione ogni sei minuti.
* **62-92:** simulazione individuale in condizioni analoghe alla verifica.
* **92-105:** correzione di due quesiti campione, mostrando il procedimento.
* **105-110:** exit ticket: un concetto sicuro e un concetto da recuperare.

### ✍️ Disegno alla lavagna
```text
Von Neumann -> CPU/Bus/Memoria
						 |
				 CU + ALU + registri
						 |
		 ciclo -> pipeline -> hazard
						 |
		 gerarchia memorie -> prestazioni
```

### 🎯 Micro-task formativo per casa
Creare una pagina di “ripasso a colpo d'occhio” con una formula ($2^n$, $T_{CPU}$ oppure AMAT), uno schema CPU, una tabella di memoria e una griglia pipeline. Aggiungere tre domande che potrebbero comparire nella verifica e rispondere senza consultare gli appunti.
