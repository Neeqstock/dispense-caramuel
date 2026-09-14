# 3EI - Settimana 8: VERIFICARE, INTERPRETARE, RECUPERARE

Kit didattico completo per la verifica del modulo. Il collegamento al quadro delle otto settimane e' [3EI - SETT-OTT](3EI%20-%20SETT-OTT.md).

```text
SETTIMANA 8
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] Prova scritta completa: struttura e consegne
│   ├── [1.2] Griglia di valutazione e criteri osservabili
│   ├── [1.3] Somministrazione e controllo del procedimento
│   └── [1.4] Lettura degli errori e piano di recupero
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] NetAcad: hardware e assemblaggio
│   ├── [2.2] NetAcad: diagnostica e quiz
│   ├── [2.3] Feedback individuale e correzione degli errori
│   └── [2.4] Chiusura del portfolio del bimestre
└── 📋 GUIDA DI REGIA PER IL DOCENTE
		├── Cronoprogramma di circa 110 minuti
		├── Disegno di sintesi e restituzione
		└── Micro-task formativo per casa
```

## 🧠 MODULO TEORICO (2 Ore in Aula)

### ├── [1.1] Prova scritta completa

La prova verifica conoscenze, procedimenti e capacita' di collegamento. Durata indicativa 60-75 minuti, con Fila A e Fila B equivalenti per difficolta'. Una possibile distribuzione su 10 punti e':

1. **2,5 punti - indirizzamento e prestazioni:** calcolo di $2^n$ e applicazione di $T_{CPU}$ o AMAT, con unita' corrette;
2. **2,5 punti - scelta multipla e vero/falso motivato:** CPU, ALU, CU, registri, bus, CISC/RISC;
3. **3 punti - risposte aperte:** gerarchia e localita', oppure pipeline e hazard;
4. **2 punti - comunicazione tecnica:** schema leggibile, lessico, motivazione e ordine del procedimento.

Le formule necessarie sono dichiarate nella consegna, ma lo studente deve scegliere quella corretta e spiegare i simboli. Un risultato senza passaggi permette di controllare poco il ragionamento.

### ├── [1.2] Griglia e criteri osservabili

| Indicatore | Punteggio | Evidenza attesa |
|---|---:|---|
| Conoscenze | 0-3 | definizioni corrette e distinzione tra blocchi |
| Procedimento | 0-3 | formule, passaggi e unita' coerenti |
| Collegamenti | 0-2 | relazione tra CPU, memoria, ciclo e prestazioni |
| Linguaggio e schema | 0-2 | termini tecnici, ordine e rappresentazioni leggibili |

La soglia e' accompagnata da descrittori, non solo da un numero. Per esempio, una risposta “la cache e' veloce” e' incompleta; una risposta adeguata indica livello della gerarchia, localita' e conseguenza di hit/miss.

### ├── [1.3] Somministrazione

Prima della prova il docente chiarisce tempo, materiali ammessi, gestione delle domande e consegna. Durante la prova osserva i procedimenti senza suggerire la soluzione. Gli schemi possono essere richiesti a mano per verificare se lo studente sa rappresentare `PC -> MAR -> MDR -> IR`, la gerarchia e `IF-ID-EX-MEM-WB`.

### ├── [1.4] Errori e recupero

La restituzione separa quattro percorsi: errore in $2^n$ -> tabella potenze e conversioni; errore nei registri -> sequenza di fetch; errore nella memoria -> ordinamento e AMAT; errore nella pipeline -> griglia con stalli; lessico debole -> glossario usato in una risposta breve. Il recupero deve chiedere una nuova prestazione osservabile, non la sola rilettura.

## 💻 MODULO LABORATORIO (2 Ore con ITP)

### ├── [2.1] NetAcad: hardware e assemblaggio

Accedere alla classe Cisco IT Essentials e verificare capitoli assegnati, percentuale di completamento e tentativi precedenti. Svolgere i moduli su sicurezza, motherboard, CPU, memoria, dispositivi di archiviazione e assemblaggio. Per ogni risposta errata si torna alla sezione teorica e si scrive una spiegazione di una riga.

### ├── [2.2] NetAcad: diagnostica

Completare i quiz e le attivita' relative a POST, alimentazione, RAM, dischi e procedure di troubleshooting. La diagnosi deve seguire il metodo: raccogliere sintomo, formulare ipotesi, proporre una prova non distruttiva, osservare l'esito e decidere il passo successivo. Non si sostituisce un componente “a caso”.

### ├── [2.3] Feedback e recupero in laboratorio

Il docente e l'ITP consultano il report NetAcad e la relazione PDF. Chi ha difficolta' riceve una stazione mirata: riconoscimento connettori, schema CPU, gerarchia memorie oppure classificazione dei beep code con manuale. Chi ha gia' raggiunto gli obiettivi puo' motivare una diagnosi per un compagno, senza svolgere il quiz al suo posto.

### ├── [2.4] Attivita' a fasi (110 min)

* **FASE A - Accesso e controllo (15 min):** login, classe corretta, capitoli assegnati e regole di consegna.
* **FASE B - Quiz hardware (30 min):** componenti, sicurezza, motherboard, CPU e RAM.
* **FASE C - Assemblaggio/diagnostica (30 min):** simulazioni NetAcad o postazione reale con checklist e manuale.
* **FASE D - Correzione documentata (20 min):** per ogni errore indicare concetto, fonte e correzione.
* **FASE E - Portfolio finale (15 min):** ordinare PDF, schemi, prova e report; annotare l'obiettivo di recupero.

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma teorico (110 minuti)
* **00-10:** spiegare struttura, criteri e materiali della verifica.
* **10-20:** esempio di risposta completa con formula e schema.
* **20-82:** somministrazione della prova scritta, con tempo scandito.
* **82-95:** raccolta, controllo delle pagine e autovalutazione silenziosa.
* **95-105:** anticipare i percorsi di feedback e recupero.
* **105-110:** exit ticket: una competenza raggiunta e una prova da rifare.

### ✍️ Disegno alla lavagna dopo la prova
```text
BUS -> CPU (CU + ALU + REGISTRI) -> CICLO -> PIPELINE
	\-> memoria: REG -> CACHE -> RAM -> SSD/HDD
						 diagnosi: sintomo -> ipotesi -> prova -> esito
```

### 🎯 Micro-task formativo per casa
Scrivere una pagina di riflessione tecnica: scegliere un errore della prova o del quiz, riportare il concetto corretto, un piccolo schema e una domanda di controllo. Allegare il glossario personale di dieci termini del modulo. Il lavoro apre il successivo percorso su boot, BIOS/UEFI, partizioni e virtualizzazione.
