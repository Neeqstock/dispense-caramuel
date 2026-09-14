Ecco il piano operativo dettagliato per la **3ª EI** (disciplina **Sistemi e Reti**) per le prime 8 settimane (**Settembre e Ottobre**).

* **Monte ore:** **4 ore settimanali** (suddivise in **2 ore di teoria in aula** e **2 ore di laboratorio in compresenza con l'ITP**).
* **Obiettivo del bimestre:** Padroneggiare l'architettura interna del computer, sia dal punto di vista logico/funzionale (Von Neumann, CPU, ciclo macchina, memorie) sia dal punto di vista fisico/operativo (smontaggio, componenti, sicurezza ESD, Cisco NetAcad IT Essentials).

---

## 🧭 Quadro Sinottico Settimana per Settimana (Settembre – Ottobre)

Dal Relay/Relé

```
┌───────────┬──────────────────────────────────────┬────────────────────────────────────────┐
│ SETTIMANA │ TEORIA (2h - In aula)                │ LABORATORIO (2h - Con ITP)             │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 1   │ Presentazione Sistemi e Reti;        │ Norme di sicurezza elettrica ed ESD;   │
│           │ Dal transistor alla macchina compl.  │ Registrazione Cisco NetAcad (ITEv7/v8) │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 2   │ Macchina di Von Neumann;             │ Anatomia del PC: Ispezione case,       │
│           │ Struttura e tipologie di BUS di sist.│ alimentatore (PSU) e tensioni          │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 3   │ La CPU al microscopio (ALU, CU, Reg);│ Scheda madre, Socket CPU, montaggio    │
│           │ Calcolo spazio di memoria (2^n)      │ dissipatore, pasta termica e banchi RAM│
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 4   │ Ciclo Fetch-Decode-Execute;          │ Memorie di massa (HDD vs SSD SATA/NVMe)│
│           │ Filosofie di calcolo: CISC vs RISC   │ e schede di espansione PCI-Express     │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 5   │ Gerarchia delle memorie;             │ Attività pratica: Smontaggio totale    │
│           │ Memoria Cache e principio di località│ e rimontaggio guidato di un PC a banchi│
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 6   │ Tecniche di ottimizzazione CPU:      │ Test di accensione (POST / Beep Code)  │
│           │ Il Pipelining e i conflitti (Hazard) │ e avvio stesura Relazione Tecnica      │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 7   │ Ripasso attivo e simulazione         │ Finalizzazione e consegna su Classroom │
│           │ della prova scritta                  │ della Relazione Tecnica (VOTO PRATICO) │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 8   │ 📝 VERIFICA SCRITTA 1 (Architettura) │ Capitoli Cisco NetAcad e verifiche     │
│           │                                      │ interattive a quiz sulla piattaforma   │
└───────────┴──────────────────────────────────────┴────────────────────────────────────────┘
```

### RISC
ADD
SUB
MULT
BRANCH

### CISC
ADD
SUB
MULT
BRANCH
SIN



---

## 📝 Dettaglio Operativo dei Moduli

---

### SETTIMANA 1: L'Ingresso nel Triennio Tecnico e Cisco NetAcad
*Obiettivo: Posizionare la materia all'interno del percorso informatico e allestire gli strumenti di lavoro.*

* **Teoria (2h):**
  * **Il ruolo di Sistemi e Reti:** Spiegare che cosa differenzia questa materia da *Informatica* (in Informatica si scrive codice logico; in Sistemi si comprende la macchina che lo esegue e le infrastrutture che lo trasportano).
  * **Evoluzione:** Dal calcolo discreto ai microprocessori monolitici moderni.
  * Il concetto di architettura hardware: separazione tra parte operativa e parte di controllo.
* **Laboratorio (2h con ITP):**
  * **Sicurezza in laboratorio:** Il pericolo delle scariche elettrostatiche (**ESD** - *Electrostatic Discharge*); uso del braccialetto antistatico e tappetini conduttivi.
  * **Piattaforma Cisco Networking Academy:** Registrazione della classe al corso **IT Essentials (ITEv7/v8)**; spiegazione di come si sbloccano i capitoli e i test a crocette online.
* 📚 **Cosa devi ripassare tu:**
  * Dai un'occhiata rapida alla dashboard docente di NetAcad per capire come si crea o si attiva la classe (l'ITP spesso lo ha già fatto negli anni passati).

---

### SETTIMANA 2: Il Modello di Von Neumann e i Bus di Sistema
*Obiettivo: Comprendere la struttura classica dell'elaboratore e le autostrade su cui viaggiano i dati.*

* **Teoria (2h):**
  * **Architettura di Von Neumann:** I 4 blocchi fondamentali (CPU, Memoria Centrale, Dispositivi di I/O, Bus). Il collo di bottiglia di Von Neumann (*Von Neumann Bottleneck*).
  * Differenza concettuale con l'**Architettura Harvard** (memoria dati e memoria istruzioni separate, tipica dei microcontrollori/DSP).
  * **I Bus di Sistema:**
    * **Data Bus (Bus Dati):** Bidirezionale, determina il parallelismo della macchina (a 32 o 64 bit).
    * **Address Bus (Bus Indirizzi):** Unidirezionale (CPU $\rightarrow$ Memoria), determina la massima capacità di memoria RAM indirizzabile.
    * **Control Bus (Bus Controllo):** Segnali di temporizzazione e comando (Read/Write, Interrupt, Clock).
* **Laboratorio (2h con ITP):**
  * **Ispezione del Case e dell'Alimentatore (PSU):**
  * Fattori di forma dei case (ATX, Micro-ATX, Mini-ITX).
  * L'alimentatore: trasformazione da corrente alternata (230V AC) a corrente continua (tensioni standard: $+3.3\text{V}$, $+5\text{V}$, $+12\text{V}$, $-12\text{V}$).
  * Riconoscimento connettori: Molex, SATA power, 24-pin ATX, 4/8-pin CPU, PCIe 6/8-pin.
* 📚 **Cosa devi ripassare tu:**
  * Formula: Se il bus indirizzi ha $k$ linee fisiche, lo spazio indirizzabile è pari a $2^k$ locazioni (es. con 32 linee $\rightarrow 2^{32} \text{ byte} = 4\text{ GiB}$).

---

### SETTIMANA 3: La CPU, i Registri e il Calcolo della Memoria
*Obiettivo: Guardare all'interno del processore e comprendere l'accoppiamento con la RAM.*

* **Teoria (2h):**
  * **Struttura interna della CPU:**
    * **ALU (Arithmetic Logic Unit):** Esegue operazioni aritmetiche (addizioni) e logiche (AND, OR, shift).
    * **CU (Control Unit):** Coordina il flusso dei dati e decodifica i comandi.
    * **Clock di sistema:** Concetto di frequenza (GHz) e tempo di ciclo ($T = \frac{1}{f}$).
  * **I Registri fondamentali:**
    * **PC (Program Counter):** Contiene l'indirizzo della prossima istruzione da eseguire.
    * **IR (Instruction Register):** Contiene l'istruzione attualmente in fase di decodifica.
    * **MAR (Memory Address Register)** e **MDR (Memory Data Register):** I registri "porta" verso il bus di sistema.
    * **PSW / Status Register (Flag):** Zero, Carry, Overflow, Segno.
  * **Esercizi numerici alla lavagna:** Calcolo della memoria massima indirizzabile in base alla larghezza del bus indirizzi e calcolo dei tempi di clock.
* **Laboratorio (2h con ITP):**
  * **La Scheda Madre (Motherboard) e il Socket:**
  * Esplorazione del PCB, piste in rame, chipset (Northbridge/Southbridge storici vs Chipset moderni integrati).
  * Riconoscimento dei socket (LGA Intel a pin sulla scheda vs PGA AMD storici a pin sul processore).
  * Procedura corretta di inserimento della CPU: allineamento del triangolo/tacche, applicazione del chicco di pasta termica e aggancio del dissipatore ad aria/liquido.
  * Inserimento moduli RAM negli slot DIMM (controllo del corretto orientamento della tacca e configurazione *Dual Channel* negli slot alternati 1-3 o 2-4).
* 📚 **Cosa devi ripassare tu:**
  * I passaggi fisici con cui MAR e MDR dialogano con la RAM durante un'operazione di lettura (`MEM[MAR] -> MDR`).

---

### SETTIMANA 4: Il Ciclo Macchina e le Filosofie CISC vs RISC
*Obiettivo: Capire come il processore esegue concretamente il codice macchina e la guerra tra filosofie costruttive.*

* **Teoria (2h):**
  * **Il Ciclo di Esecuzione delle Istruzioni (Instruction Cycle):**
    1. **Fetch:** Prelievo dell'istruzione dalla RAM all'IR tramite il PC.
    2. **Decode:** La CU interpreta i bit del codice operativo (*OpCode*) e individua gli operandi.
    3. **Execute:** L'ALU esegue il calcolo o la CU manipola i registri.
    4. *(Write-back):* Scrittura del risultato nei registri o in memoria.
    5. Incremento del Program Counter per l'istruzione successiva.
  * **Confronto CISC vs RISC:**
    * **CISC (Complex Instruction Set Computer):** Tante istruzioni complesse a lunghezza variabile, richiedono più cicli di clock per istruzione, memoria microprogrammata (esempio: architettura Intel x86 / AMD64).
    * **RISC (Reduced Instruction Set Computer):** Istruzioni semplici a lunghezza fissa (spesso a 32 bit), esecuzione in 1 solo ciclo di clock, architettura Load/Store (esempi: ARM, RISC-V, chip Apple serie M).
* **Laboratorio (2h con ITP):**
  * **Memorie Secondarie e Schede di Espansione:**
  * Differenza tra HDD meccanico (piatti, testine, tempi di seek latency) e SSD (memorie flash NAND).
  * Interfacce a confronto: SATA III (limite teorico a 6 Gbps $\approx 550 \text{ MB/s}$) vs **M.2 NVMe su bus PCIe** (velocità fino a diversi GB/s).
  * Riconoscimento degli slot di espansione: PCIe x16 (schede video discrete), PCIe x4, PCIe x1.
* 📚 **Cosa devi ripassare tu:**
  * L'equazione delle prestazioni del processore: $\text{Tempo CPU} = \text{Istruzioni} \times \text{CPI (Cicli Per Istruzione)} \times \text{Tempo di Clock}$. Serve a spiegare perché RISC minimizza i cicli per istruzione (CPI vicino a 1), mentre CISC riduce il numero totale di istruzioni.

---

### SETTIMANA 5: La Gerarchia delle Memorie e la Cache
*Obiettivo: Risolvere il paradosso tra memorie ultra-veloci (e costosissime) e memorie capienti (ma lente).*

* **Teoria (2h):**
  * **La piramide delle memorie:** Registri $\rightarrow$ Cache (L1, L2, L3) $\rightarrow$ RAM centrale (DRAM) $\rightarrow$ Memoria di massa (NAND/Magnetica).
  * Compromessi progettuali: tempo di accesso (ns vs ms), capacità (KB vs TB), costo per bit.
  * Static RAM (SRAM usata nelle cache, a transistor/flip-flop, velocissima, senza refresh) vs Dynamic RAM (DRAM usata nei moduli di sistema, a condensatori, necessita di refresh ciclico periodico).
  * **La Memoria Cache:**
    * Concetto di **Hit** (dato trovato) e **Miss** (dato assente, recupero dalla RAM).
    * **I Principi di Località:**
      * *Località Temporale:* Se accedo a un dato ora, è probabile che ci riacceda a breve (es. la variabile contatore in un ciclo).
      * *Località Spaziale:* Se accedo a un dato, è probabile che acceda a dati memorizzati in locazioni contigue (es. scansione di un array o istruzioni sequenziali).
* **Laboratorio (2h con ITP):**
  * **Laboratorio Operativo di Assemblaggio (Parte 1):**
  * A coppie di studenti: disassemblaggio completo di un computer da laboratorio non operativo.
  * Catalogazione ordinata della viteria e dei cavi.
  * Rimontaggio step-by-step su banco: posizionamento scheda madre nel case (attenzione ai distanziali per evitare cortocircuiti sul metallo del telaio).
* 📚 **Cosa devi ripassare tu:**
  * La formula dell'Average Memory Access Time (AMAT): $\text{AMAT} = \text{Hit Time} + (\text{Miss Rate} \times \text{Miss Penalty})$ (da usare come concetto qualitativo, senza terrorizzare gli studenti con calcoli complessi).

---

### SETTIMANA 6: Tecniche di Ottimizzazione della CPU: Il Pipelining
*Obiettivo: Capire come i moderni processori elaborano più istruzioni contemporaneamente.*

* **Teoria (2h):**
  * **Il concetto di Pipelining:**
    * Esecuzione sequenziale pura (ogni istruzione aspetta la fine completa della precedente: 5 cicli per istruzione).
    * Esecuzione in pipeline: sovrapposizione temporale delle fasi (mentre l'istruzione 1 fa l'*Execute*, l'istruzione 2 fa il *Decode* e l'istruzione 3 fa il *Fetch*).
    * A regime, la CPU completa idealmente **1 istruzione per ciclo di clock**.
  * **I Conflitti di Pipeline (Pipeline Hazards):**
    1. *Hazard Strutturali:* Due istruzioni richiedono contemporaneamente la stessa risorsa fisica (es. accesso alla stessa memoria).
    2. *Hazard sui Dati (Data Dependencies):* Un'istruzione necessita del risultato di un'istruzione precedente non ancora completata (Read After Write - RAW).
    3. *Hazard di Controllo (Branch Hazards):* In presenza di salti condizionati (`IF` / `GOTO`), la CPU non sa quale sarà la prossima istruzione da caricare prima del calcolo della condizione.
  * Soluzioni architetturali: stallo della pipeline (*bubble*), inoltro dati (*forwarding/bypassing*), predizione dei salti (*branch prediction*).
* **Laboratorio (2h con ITP):**
  * **Completamento Cablaggio e Primo Test (Parte 2):**
  * Cablaggio del pannello frontale (Front Panel Connectors: Power SW, Reset SW, Power LED, HDD LED).
  * Collegamento alimentazione e cavi dati SATA.
  * **Il momento della verità:** Prima accensione.
  * Diagnostica di avvio: comprendere i **Beep Code** della scheda madre emessi dal buzzer di sistema (es. 1 beep lungo + 2 brevi: problema alla scheda video; beep continui: assenza o mancato riconoscimento della RAM).
* 📚 **Cosa devi ripassare tu:**
  * Disegna su un foglio il diagramma temporale a griglia con le 5 fasi classiche (IF, ID, EX, MEM, WB) per poterlo riprodurre con scioltezza alla lavagna.

---

### SETTIMANA 7: Ripasso Attivo e Stesura Relazione Tecnica
*Obiettivo: Fissare i concetti architetturali prima della prova scritta e chiudere il primo voto di laboratorio.*

* **Teoria (2h):**
  * **Sessione di Retrieval Practice (Simulazione d'Esame):**
    * Distribuzione di una scheda di autovalutazione (30 minuti di lavoro individuale):
      * 1 schema a blocchi da etichettare (CPU, bus e registri).
      * 1 calcolo di spazio di memoria partendo dai bit del bus indirizzi.
      * 2 quesiti a risposta aperta sintetica (es. *"Spiega la differenza tra SRAM e DRAM"* e *"Cosa accade alla pipeline in caso di salto condizionato?"*).
    * Correzione incrociata guidata alla lavagna e chiarimento dubbi.
* **Laboratorio (2h con ITP):**
  * **Stesura della Relazione Tecnica sull'Hardware del PC:**
  * Gli studenti lavorano individualmente al computer per redigere il documento tecnico definitivo:
    1. *Scopo dell'attività:* Descrizione dell'intervento di assemblaggio e verifica funzionale.
    2. *Scheda tecnica dei componenti manipolati:* Modello CPU, tipologia socket, quantità e frequenza RAM, modello scheda madre, tipologia memoria di massa.
    3. *Procedura operativa:* Fasi cronologiche del montaggio e norme di sicurezza ESD rispettate.
    4. *Esito del collaudo:* Riscontro del POST e rilevamento periferiche da BIOS.
  * Esportazione in PDF e consegna entro il termine della lezione su Google Classroom.
  * 🎯 **Questa consegna costituisce la 1ª Valutazione Sommativa di Laboratorio.**
* 📚 **Cosa devi ripassare tu:**
  * Prepara il testo della verifica scritta per la settimana successiva (due file bilanciate: Fila A e Fila B) e concorda con l'ITP la scala di punteggio per la relazione.

---

### SETTIMANA 8: La Prima Verifica Sommativa Teorica
*Obiettivo: Valutare l'apprendimento teorico del primo modulo di architettura degli elaboratori.*

* **Teoria (2h):**
  * 📝 **VERIFICA SCRITTA N. 1 (Sistemi di Elaborazione e Architettura)**
  * *Durata effettiva:* 60–75 minuti.
  * *Struttura consigliata della prova (Totale 10 punti su griglia d'istituto):*
    * **Esercizio Applicativo (2.5 pt):** Calcolo numerico dello spazio di indirizzamento RAM e dei tempi di esecuzione CPU con/senza pipeline.
    * **Quesiti Tecnici a Risposta Multipla / Vero-Falso con Giustificazione (2.5 pt):** Funzione dei registri MAR/MDR/PC, differenze CISC vs RISC, tipologie di bus.
    * **Domande Aperte a Risposta Sintetica (3 pt):**
      1. *"Descrivi il principio di località temporale e spaziale e spiega come viene sfruttato dalla memoria cache."*
      2. *"Illustra cosa si intende per Hazard (conflitto) sui dati nel pipelining e come può essere gestito."*
    * **Precisione Lessicale e Formalismo Tecnico (2 pt):** Uso corretto dei termini tecnici in lingua italiana e inglese.
* **Laboratorio (2h con ITP):**
  * **Sessione Cisco NetAcad (Capitoli 1, 2 e 3):**
  * Risoluzione in aula dei quiz di autovalutazione del corso Cisco IT Essentials relativi all'hardware e all'assemblaggio.
  * Feedback immediato sui risultati dei test Cisco a schermo.
* 📚 **Cosa devi fare tu:**
  * Correggi le verifiche scritte entro pochi giorni annotando commenti precisi: il confronto con i ragazzi sul primo test definisce la loro percezione di serietà ed equità della tua materia per tutto l'anno.