
# 🗺️ SETTIMANA 1: L'INGRESSO NEL TRIENNIO TECNICO E LA MACCHINA DIGITALE

```text
SETTIMANA 1
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] Sistemi e Reti vs Informatica: la stessa medaglia, due facce
│   ├── [1.2] Dal Relè al Microprocessore: breve storia dell'evoluzione hardware
│   └── [1.3] L'Architettura a Due Anime: Parte Operativa vs Parte di Controllo
│
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] Il Nemico Invisibile: le Scariche Elettrostatiche (ESD)
│   ├── [2.2] Dispositivi di Protezione: Braccialetto e Tappetini Antistatici
│   ├── [2.3] La Piattaforma Cisco Networking Academy (NetAcad)
│   └── [2.4] Esercitazione Pratica Guidata (Missione: "Primo Accesso e Presa di Contatto")
│
└── 📋 GUIDA DI REGIA PER IL DOCENTE
    ├── Scaletta Minuto per Minuto
    ├── Schema da Disegnare alla Lavagna
    └── Micro-Task di Consolidamento (Formative Assessment)
```

---

## 🧠 MODULO TEORICO (2 Ore in Aula)

### ├── [1.1] Sistemi e Reti vs Informatica: la stessa medaglia, due facce
*Obiettivo: dare un senso alla materia, distinguendola da ciò che i ragazzi già conoscono.*

* 📌 **Informatica (il software, il "cosa"):**
  * Si occupa della scrittura del codice, degli algoritmi, della logica di programmazione: **cosa** deve fare la macchina.
* 📌 **Sistemi e Reti (l'hardware e l'infrastruttura, il "come" e il "dove"):**
  * Si occupa di **come** è fatta la macchina che esegue quel codice (CPU, memorie, bus) e di **come** le macchine comunicano tra loro (reti, protocolli, cablaggi).
  * **Metafora d'aula:** l'Informatica è lo spartito musicale; Sistemi e Reti sono lo strumento che lo suona e i cavi/amplificatori che portano il suono in tutta la sala.
* 📌 **Perché serve a un perito informatico:**
  * Un tecnico deve sapere **diagnosticare** un guasto fisico, **configurare** una rete, **assemblare** un PC: competenze che il solo codice non dà.
  * **Esempi reali di questa divisione:**
    * **Scenario 1 — Un'azienda ha un sito web lentissimo:** l'Informatico scrive il codice PHP/JavaScript per renderlo più veloce; il Tecnico di Sistemi verifica se il server ha RAM sufficiente, se il collegamento di rete non è saturo, se il database fisicamente non riesce a stare al passo. Senza questo dialogo, il codice più perfetto non risolverà il problema.
    * **Scenario 2 — Una video-conferenza Zoom continua a bloccarsi:** l'Informatico controlla il codice client; il Tecnico di Sistemi controlla se la larghezza di banda è insufficiente, se la CPU è al 100%, se la scheda di rete ha problemi driver. Spesso il colpevole è l'hardware, non il software.
    * **Scenario 3 — Un'app critica per l'ospedale si arresta casualmente:** l'Informatico debugga l'applicazione; il Tecnico di Sistemi scopre che il server fisico soffre di surriscaldamento (ventole intasate di polvere), provocando reset random della CPU.
  * **Conclusion per la classe:** In un'azienda vera, questi due ruoli **comunicano costantemente** e risolvono i problemi insieme; se conosci solo il tuo lato, sarai sempre "mezzo tecnico".



---

### ├── [1.2] Dal Relè al Microprocessore: breve storia dell'evoluzione hardware
*Obiettivo: dare profondità storica, mostrando che l'architettura moderna è il punto di arrivo di un percorso di miniaturizzazione.*

* 🕰️ **La preistoria del calcolo: Relè e Valvole Termoioniche (fino agli anni '40)**
  * **Il Relè (1835 ~ invenzione di Samuel Morse):** interruttore **elettromeccanico** — una bobina elettrica attira un braccio di metallo che chiude un circuito. Quando la corrente si spegne, una molla lo riporta alla posizione iniziale.
    * ✅ **Vantaggio:** affidabile, semplice da fabbricare, utilizza l'acqua come refrigerante.
    * ❌ **Difetti fatali:** **estremamente lento** (ha parti meccaniche che si muovono fisicamente, microsecondi!), consuma enormi quantità di energia, genera calore intenso, i contatti si consumano e ossidano dopo poche milioni di operazioni.
    * 📸 **Immagine storica:** le macchine ENIAC (1946, Università della Pennsylvania) — primo calcolatore "general purpose" — occupavano un'intera stanza (30 tonnellate!), consumavano 150 kW (come 150 piastre elettriche accese), e usavano **relè con registrazione su schede perforate**. Poteva eseguire solo ~300 operazioni/secondo.
    * [Video](https://youtu.be/Em8Kh7WcLEw?si=uSp2T6XBoTSl0s2T)
  * **La Valvola Termoionica (1906 ~ Lee De Forest):** progresso su relè — niente parti mobili, solo electron flow in vuoto dentro una ampolla di vetro, molto più veloce (millisecondi).
    * https://www.youtube.com/watch?v=i3u-IMShs5g
    * ✅ **Vantaggio rispetto al relè:** circa 1000× più veloce, permetteva velocità di switch in milliseccondi.
    * ❌ **Difetti ancora peggiori:** consumavano **ancora più energia e calore** del relè (una valvola da sola dissipava watts), si bruciavano/invecchiavano rapidamente (durata media: 1000 ore), richiedevano bassissime temperature per non degradarsi, e l'intera stanza doveva essere climatizzata (anzi, la maggior parte dell'energia andava in refrigerazione!). Se una valvola si bruciava, la macchina intera si fermava e dovevi trovare quale tra migliaia.
    * 📸 **Immagine storica:** ENIAC aveva **18.000 valvole termoioniche**, e i tecnici scherzavano dicendo che il calore generato era sufficiente per riscaldare una casa intera. Rompere una valvola ogni 5-10 ore era considerato "accettabile".
    * **Aneddoto memorabile:** Nel 1947, gli ingegneri di ENIAC notarono comportamenti stranissimi e casuali. Dopo giorni di debug, scoprirono che una **falena era rimasta intrappolata dentro una valvola**, cortocircuitando il componente. Da quel giorno, il termine **"bug" informatico** (insetto in inglese) nacque qui. La falena è ancora conservata presso lo Smithsonian Institution!

---

* 🕰️ **La Rivoluzione: Il Transistor (1947 ~ Bell Labs)**
  * https://www.youtube.com/watch?v=IcrBqCFLHIY
  * **Il Transistor** è un interruttore **puramente elettronico** (nessuna parte meccanica, niente vuoto nella lampada): tre terminali di materiale semiconduttore (silicio) combinati in modo che una piccola corrente su uno dei tre terminali (*base*) controlla il flusso di corrente tra gli altri due (*collettore* ed *emettitore*).
    * ✅ **Vantaggi rivoluzionari:**
      * **Velocità:** switch in nanosecondi (milioni di volte più veloce di un relè), perché non ci sono parti fisiche da muovere—solo electron flow.
      * **Energia:** consuma migliaia di volte **meno energia** di una valvola (milliwatt invece di watt).
      * **Affidabilità:** praticamente infinita (i transistor moderni possono essere switchati un trilione di volte senza degradarsi).
      * **Miniaturizzazione:** un transistor è grande pochi millimetri; una valvola era grande come un dito.
      * **Costo:** dopo il 1960, massicciamente conveniente da produrre in serie.
  * **Impatto storico:** premio Nobel per la Fisica nel 1956 ai tre inventori (Bardeen, Brattain, Shockley). Ha fatto iniziare l'era dell'Informatica moderna.

---

* 🕰️ **Il Circuito Integrato (1960 ~ Texas Instruments & Fairchild)**
  * **L'idea:** anziché saldare transistor discreti uno a uno, integra **migliaia di transistor su un singolo cristallo di silicio** usando processi fotolitografici (come la stampa).
  * **Milestone:** 
    * 1960: Intel 4004 → 2.300 transistor su pochi millimetri quadrati.
    * 1980: Intel 8086 → 29.000 transistor.
    * 2024: Apple M4 Pro → **21 miliardi** di transistor su superficie più piccola di un'unghia.
  * **L'effetto:** ogni chip integrato può contenere un'architettura intera (CPU, memoria, peripheral controller) in un unico package, riducendo drasticamente costi e spazi.

---

* 📈 **La Legge di Moore (1965 ~ Gordon Moore, co-fondatore Intel):**
  * **Enunciato:** *"Il numero di transistor su un chip raddoppia ogni 18-24 mesi (spesso detta "ogni 2 anni"), a parità di costo e superficie."*
  * **Implicazioni pratiche:**
    * Ogni 2 anni, la CPU ha il doppio della potenza di calcolo nello stesso spazio fisico.
    * Conseguenza: i prezzi dei computer crollano esponenzialmente (cosa che costava $10.000 nel 1980 costa oggi $100).
    * **Limite fisico:** verso il 2025-2030 iniziamo a toccare il limite della miniaturizzazione (i transistor diventano grandi come pochi atomi di silicio, e gli effetti quantistici cominciano a dominare). Moore ha predetto che la legge cesserebbe intorno al 2025, e infatti è quello che stiamo osservando ora.
  * 🎯 **Messaggio per la classe:** tutto quello che studieremo quest'anno (CPU, bus, memorie, architetture) è il **risultato diretto** di 80 anni di questa corsa della miniaturizzazione. Una CPU moderna integra componenti che 50 anni fa occupavano una stanza intera, dentro uno spazio microscopico.

---

* 📚 **Fonti storiche per chi vuole approfondire:**

### Integrazione storica: una linea del tempo minima dell'informatica

Per evitare che la storia dell'hardware sembri una semplice successione di invenzioni, si puo' proporre questa linea del tempo:

| Periodo | Tappa | Idea fondamentale |
|---|---|---|
| Antichita' | abaco e strumenti di calcolo | delegare all'oggetto il conteggio ripetitivo |
| XVII secolo | Pascalina e calcolatori meccanici | automatizzare somme e operazioni con ruote dentate |
| XIX secolo | macchina analitica di Charles Babbage | separare memoria, calcolo, controllo e ingresso/uscita |
| XIX secolo | schede perforate di Jacquard | rappresentare istruzioni come una sequenza codificata |
| 1940-1950 | valvole termoioniche | costruire calcolatori elettronici programmabili |
| 1947-1960 | transistor e circuiti integrati | ridurre consumi, dimensioni e costi |
| dagli anni '70 | microprocessore | concentrare la CPU in un singolo chip |
| oggi | sistemi multicore e SoC | integrare CPU, GPU, memoria e periferiche nello stesso sistema |

Il filo conduttore e' la **programmabilita'**: prima si automatizza il calcolo, poi si separano dati e istruzioni, infine si costruiscono macchine capaci di eseguire programmi diversi senza essere ricostruite fisicamente.

### Integrazione: Ada Lovelace e il primo programma

**Ada Lovelace (1815-1852)** lavoro' sulle idee di Charles Babbage per la macchina analitica. Nelle sue note alla traduzione di un articolo dell'ingegnere Luigi Menabrea descrisse un procedimento per calcolare i numeri di Bernoulli: per questo viene spesso ricordata come la prima programmatrice della storia.

Il punto importante per Sistemi e Reti non e' soltanto il primato cronologico. Ada capi' che una macchina programmabile avrebbe potuto manipolare non solo numeri, ma anche simboli, musica o testo, se rappresentati secondo regole precise. Anticipo' quindi la distinzione tra **macchina fisica** e **istruzioni** che la guidano: la stessa architettura puo' svolgere compiti diversi cambiando il programma.

In classe si puo' collegare questa intuizione alla Settimana 2: la macchina analitica anticipava gia' blocchi concettuali simili a memoria, unita' di calcolo, controllo e dispositivi di ingresso/uscita.

* **Domanda guida:** se l'hardware resta uguale ma cambiano le istruzioni, che cosa cambia nel comportamento della macchina?

  * **Wikipedia sulla storia del computer:** https://en.wikipedia.org/wiki/History_of_computing_hardware
  * **Articolo su ENIAC e il primo "bug":** https://en.wikipedia.org/wiki/Debugging#Moth_in_the_machine
  * **Transistor e la rivoluzione:** https://en.wikipedia.org/wiki/Transistor
  * **Legge di Moore:** https://en.wikipedia.org/wiki/Moore%27s_law
  * **Immagini storiche ENIAC:** https://commons.wikimedia.org/wiki/ENIAC (pubblico dominio, perfette per slide/presentazione)

---

### ├── [1.3] L'Architettura a Due Anime: Parte Operativa vs Parte di Controllo
*Obiettivo: introdurre subito il concetto-chiave che accompagnerà tutto il modulo di architettura (CPU, ALU, CU nelle settimane successive).*

```text
                    OGNI SISTEMA DIGITALE HA DUE ANIME
┌───────────────────────────────┐      ┌───────────────────────────────┐
│      PARTE OPERATIVA          │◄────►│      PARTE DI CONTROLLO       │
│  (esegue materialmente         │      │  (decide COSA e QUANDO       │
│   le operazioni: calcola,      │      │   deve accadere: sequenzia   │
│   sposta dati, confronta)      │      │   i comandi, sincronizza)     │
└───────────────────────────────┘      └───────────────────────────────┘
```

* ⚙️ **Parte Operativa:** i circuiti che eseguono materialmente il lavoro.
  * Include: ALU (Arithmetic-Logic Unit), registri di lavoro, circuiti di shift, multiplexer, bus interni.
  * Funzione: esegue operazioni **su richiesta** — addizioni, sottrazioni, confronti logici, spostamento di dati, lettura/scrittura memoria.
  * Esempio: l'ALU riceve l'ordine "somma il contenuto del registro R1 con il registro R2 e metti il risultato in R3" e **lo fa**, ma non sa in che ordine eseguirlo, né sa cosa fare dopo.

* 🧭 **Parte di Controllo (Control Unit, CU):** il "direttore d'orchestra" — un insieme di circuiti logici che sequenzia l'esecuzione.
  * Funzione: legge un'istruzione dalla memoria, la **decodifica** (capisce cosa significa), e genera una serie di **segnali di controllo** che guidano la Parte Operativa passo dopo passo.
  * Meccanismo preciso:
    1. La CU invia un indirizzo di memoria al modulo di memoria (via Address Bus).
    2. La memoria ritorna l'istruzione (via Data Bus).
    3. La CU la decodifica e capisce "questo è un ADD (addizione)".
    4. La CU genera i segnali: *"Leggi da R1, Leggi da R2, Abilita ALU per somma, Scrivi risultato in R3, Incrementa il Program Counter (PC) per la prossima istruzione"*.
    5. Tutti questi segnali avvengono in sincronia con il clock (impulsi regolari, es. 3 GHz = 3 miliardi di cicli al secondo).
  * **Differenza critica dalla Parte Operativa:** la CU **non fa operazioni**, ma **coordina** chi le fa e in che ordine.

* **Metafora d'aula (espansa):** in una cucina di ristorante:
  * **Parte Operativa** = i cuochi ai fornelli (eseguono: tagliano, cuociono, mescolano).
  * **Parte di Controllo** = lo chef/sous-chef che grida gli ordini al tavolo di attesa (sequenzia: *"Antipasti subito! Piatto 3 tra 5 minuti! Dolce dopo!"*). Senza il chef, i cuochi potrebbero essere geniali, ma ogni cliente riceverebbe il dolce prima del primo piatto!
  * La **sincronizzazione** è il clock: il metronomo che fa sì che tutti i cuochi procedano al passo.

* **Anticipazione per la Settimana 3:** Vedrai in dettaglio che la CU è fatta di:
  * **Decoder:** circuito che legge il bytecode dell'istruzione e capisce quale operazione richiedere.
  * **Sequencer:** genera i segnali di controllo nella giusta sequenza e tempistica.
  * **Registro PC (Program Counter):** tiene traccia di quale istruzione eseguire successivamente.
  * Tutti insieme, fanno la "choreografia" di ogni singolo ciclo di CPU (fetch → decode → execute → store).

---

## 💻 MODULO LABORATORIO (2 Ore con ITP)

### ├── [2.1] Il Nemico Invisibile: le Scariche Elettrostatiche (ESD)
*Obiettivo: instillare da subito la cultura della sicurezza, prima ancora di toccare un componente.*

* ⚡ **Cos'è una ESD (*Electrostatic Discharge*):** un trasferimento improvviso di elettricità statica tra due corpi a diverso potenziale (es. il corpo umano e un componente elettronico).
* 🧨 **Perché fa paura in laboratorio:**
  * Il corpo umano può accumulare migliaia di volt camminando su una moquette, senza che ce ne accorgiamo (la soglia di percezione umana è molto più alta della soglia che danneggia un chip).
  * Componenti come RAM, CPU e schede madri hanno circuiti a scala nanometrica: una scarica anche minima e impercettibile può bruciare permanentemente un transistor.
* 🔎 **Il pericolo "silenzioso":** un componente danneggiato da ESD spesso non si guasta subito, ma dopo settimane o mesi di uso normale (danno latente) — per questo la prevenzione è più importante della diagnosi a posteriori.

---

### ├── [2.2] Dispositivi di Protezione: Braccialetto e Tappetini Antistatici
*Obiettivo: rendere operativa la teoria dell'ESD con gli strumenti reali del laboratorio.*

* 🖐️ **Il braccialetto antistatico (*wrist strap*):**
  * Si indossa al polso e si collega tramite un cavetto con resistenza calibrata a una massa comune (es. il telaio metallico del case o una presa di terra).
  * Funzione: scaricare a terra in modo **controllato e graduale** l'elettricità statica accumulata dal corpo, prima che possa scaricarsi di colpo sul componente.
* 🟦 **Il tappetino antistatico (*mat*):**
  * Superficie dissipativa su cui si appoggiano i componenti e gli attrezzi durante il lavoro, collegata anch'essa a massa.
* 📦 **Le buste antistatiche (*anti-static bags*):** i componenti nuovi arrivano sempre in buste metallizzate grigio/rosa: mai togliere un componente dalla busta senza essere già collegati a massa.
* 🚫 **Regola d'oro del laboratorio:** mai toccare i piedini (pin) dorati/metallici di un componente a mani nude senza scarico preventivo; afferrare sempre i componenti dai bordi.

---

### ├── [2.3] La Piattaforma Cisco Networking Academy (NetAcad)
*Obiettivo: allestire lo strumento didattico che accompagnerà tutto il modulo hardware (IT Essentials).*

* 🌐 **Cos'è NetAcad:** piattaforma didattica globale di Cisco che eroga corsi gratuiti (per le scuole convenzionate) su reti, sicurezza e hardware, con capitoli teorici, simulazioni e quiz interattivi a punteggio.
* 📚 **Il corso di quest'anno: IT Essentials (ITEv7 / ITEv8):** copre l'hardware del PC, l'assemblaggio, la diagnostica di base e i primi concetti di rete — perfettamente in linea con il programma del primo bimestre.
* 🔑 **Meccanica operativa:**
  * Ogni studente crea/riceve un account personale collegato alla classe virtuale del docente.
  * I capitoli si sbloccano progressivamente; ogni capitolo termina con un quiz a punteggio che il docente può monitorare dalla dashboard.
  * I risultati sono tracciabili in tempo reale dal docente per capire chi è indietro.

---

### ├── [2.4] Esercitazione Pratica Guidata al PC (Durata: 60-70 minuti)

#### FASE A: Simulazione ESD "a mani nude" (15 min)
1. Far strofinare a ogni studente un righello di plastica sui capelli o su un panno di lana, poi avvicinarlo a piccoli pezzetti di carta: osservare l'attrazione elettrostatica.
2. Discussione guidata: *"Se questo pezzetto di carta fosse un transistor, cosa pensate sarebbe successo?"*
3. Mostrare fisicamente in laboratorio un braccialetto e un tappetino antistatico, far indossare il braccialetto a turno a qualche studente e spiegarne il collegamento a massa.

#### FASE B: Registrazione su Cisco NetAcad (25 min)
1. Accesso al portale NetAcad con le credenziali fornite dal docente/ITP.
2. Iscrizione alla classe virtuale tramite il codice/link fornito dal docente.
3. Esplorazione guidata dell'interfaccia: indice dei capitoli, barra di avanzamento, primo quiz di prova (non a voto) per familiarizzare col formato delle domande.

#### FASE C: Ricognizione del Laboratorio (15 min)
1. Tour guidato del laboratorio: postazioni PC, armadio dei componenti, cassetto degli attrezzi (cacciaviti, pinzette, bracciale antistatico), quadro elettrico e interruttore di emergenza.
2. Regole di comportamento: niente cibo/bevande vicino ai componenti, uso ordinato degli attrezzi, come richiedere l'attrezzo mancante all'ITP.

#### FASE D: Primo Contatto col Materiale del Corso (10-15 min)
* Apertura del Capitolo 1 di IT Essentials su NetAcad e lettura guidata collettiva dei primi paragrafi introduttivi (panoramica sulla professione del tecnico informatico).
* Consegna del primo compito leggero su Google Classroom: completare il quiz del Capitolo 1 per la prossima lezione.

---

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma Lezione Teorica (110 min, 2h)
* **00-10 min | Accoglienza e presentazione:** saluto, verifica presenze, breve presentazione tua e della materia (chi sei, cosa aspettarti dall'anno).
* **10-25 min | L'Hook d'apertura:** chiedi *«Secondo voi, qual è la differenza tra un informatico e un tecnico di sistemi e reti?»*. Raccogli risposte libere, poi arriva alla distinzione software/hardware-infrastruttura con la metafora spartito/strumento.
* **25-50 min | Viaggio nel tempo:** racconta in modo narrativo l'evoluzione da relè a microprocessore, mostrando (se possibile) immagini di valvole termoioniche, primi transistor e chip moderni a confronto di dimensioni.
* **50-70 min | Lavagna partecipata sull'architettura a due anime:** disegna lo schema Parte Operativa / Parte di Controllo e usa la metafora della cucina di ristorante; chiedi alla classe di trovare altri esempi quotidiani della stessa dualità (es. orchestra e direttore, squadra sportiva e allenatore).
* **70-95 min | Presentazione del percorso annuale:** panoramica veloce di cosa affronteranno nei 5 bimestri (architettura, comunicazione, reti, apparati, sicurezza), per dare loro una mappa mentale dell'anno.
* **95-110 min | Chiusura e domande a bruciapelo:** 3 domande rapide di verifica della comprensione (*«Fammi un esempio di parte operativa e uno di parte di controllo nella vita reale»*).

### ✍️ Disegno Guida da fare alla Lavagna (Lezione 1)

```text
    ┌─────────────────────────────────────────────────────────┐
    │        L'ARCHITETTURA A DUE ANIME (visione d'insieme)     │
    │                                                         │
    │   PARTE OPERATIVA  ◄──────────────►  PARTE DI CONTROLLO │
    │   (esegue: ALU,                      (decide: Control   │
    │    registri dati)                     Unit, sequenza)   │
    │                                                         │
    │   Metafora: i cuochi ai fornelli  ↔  lo chef che dirige │
    └─────────────────────────────────────────────────────────┘
```

### 🎯 Micro-Task Formativa per Casa (Spaced Retrieval - 5 minuti)
Carica su Google Classroom questo brevissimo compito (senza voto punitivo, solo spunta di completamento):
> *"Cerca un esempio quotidiano (non informatico) in cui riconosci una 'parte operativa' e una 'parte di controllo' che lavorano insieme. Descrivilo in 3-4 righe."*
> *(Esempio vietato: la cucina di ristorante usata dal prof!)*

Da completare inoltre entro la lezione successiva: **quiz del Capitolo 1 di IT Essentials su NetAcad**.
