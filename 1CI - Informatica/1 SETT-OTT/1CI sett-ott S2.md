Ecco il kit didattico completo per la **Settimana 2**, strutturato come una **mappa concettuale espansa (mindmap ad albero)** con tutti i contenuti pronti per essere spiegati alla lavagna e svolti al PC.

---

# 🗺️ SETTIMANA 2: DATO, HARDWARE & IL DOMINIO DEL FILE SYSTEM

```text
SETTIMANA 2
├── 🧠 LEZIONE 1: TEORIA (1 ORA IN CLASSE)
│   ├── [1.1] La Piramide della Conoscenza (Dato → Informazione → Conoscenza)
│   ├── [1.2] La Dualità Informatica (Hardware vs Software)
│   └── [1.3] Il Modello Funzionale I-P-O-S (Input, Processing, Output, Storage)
│
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] Lo Shock Culturale: Smartphone vs Computer
│   ├── [2.2] L'Architettura del File System (L'Albero Rovesciato)
│   ├── [2.3] Anatomia di un File: Nome, Estensione e Metadati
│   └── [2.4] Esercitazione Pratica Guidata (Missione: "Architettura Dati")
│
└── 📋 GUIDA DI REGIA PER IL DOCENTE
    ├── Scaletta Minuto per Minuto
    ├── Schema da Disegnare alla Lavagna
    └── Micro-Task di Consolidamento (Formative Assessment)
```

---

## 🧠 MODULO TEORICO (1 Ora in Classe)

### ├── [1.1] La Piramide della Conoscenza
*Non sono sinonimi: spiegare la trasformazione dalla materia grezza alla decisione.*

* 📌 **DATO (Il mattone grezzo)**
  * **Definizione:** Rappresentazione oggettiva, elementare e non interpretata di un fatto o di una misura. Privo di significato autonomo.
  * **Esempio:** `38,5` oppure `"Rosso"` oppure `120`.
  * **Metafora d'aula:** È come un chicco di caffè crudo o una lettera dell'alfabeto staccata dalle altre.
* 📌 **INFORMAZIONE (Il dato contestualizzato)**
  * **Definizione:** Il risultato dell'elaborazione o della contestualizzazione del dato, a cui viene associato un significato comprensibile per l'essere umano.
  * **Formula logica:** $\text{Informazione} = \text{Dato} + \text{Contesto / Chiave di lettura}$.
  * **Esempio:** `38,5 °C di temperatura corporea` $\rightarrow$ adesso sappiamo cosa misura.
* 📌 **CONOSCENZA (L'informazione applicata)**
  * **Definizione:** L'informazione interiorizzata e integrata con l'esperienza pregressa, utilizzabile per prendere decisioni o risolvere problemi.
  * **Esempio:** `Ho 38,5 °C di febbre → Ho un'infezione in corso, devo stare a riposo e valutare un antipiretico`.

---

### ├── [1.2] La Dualità Informatica: Hardware vs Software
*Come il corpo e la mente, nessuno dei due ha valore senza l'altro.*

```text
                  L'ECOSISTEMA DEL COMPUTER
┌─────────────────────────────────────────────────────────────┐
│  UTENTE (Scopo / Bisogno da risolvere)                      │
│     │                                                       │
│  SOFTWARE APPLICATIVO (Word, Browser, Videogioco)           │
│     │                                                       │
│  SOFTWARE DI BASE (Sistema Operativo: Windows, Linux, macOS)│
│     │                                                       │
│  HARDWARE (Silicio, Metallo, Elettricità: CPU, RAM, Disco)  │
└─────────────────────────────────────────────────────────────┘
```

* 🔩 **HARDWARE ("La ferraglia")**
  * **Definizione:** Tutte le componenti fisiche, elettroniche, magnetiche e meccaniche tangibili del computer (ciò che si può toccare o rompere con una caduta).
  * **Esempi:** Circuiti integrati, cavi, transistor, monitor, tastiera, moduli RAM.
* 💾 **SOFTWARE ("Le istruzioni")**
  * **Definizione:** L'insieme delle istruzioni, dei programmi logici e dei dati che dicono all'hardware *cosa* fare e *quando* farlo. È intangibile.
  * **Classificazione essenziale:**
    * **Software di Base:** Il **Sistema Operativo** (Windows, Linux, Android), fa da interprete e ponte tra l'hardware e l'uomo.
    * **Software Applicativo:** I programmi creati per compiti specifici dell'utente (browser, fogli di calcolo, IDE per programmare).

---

### ├── [1.3] Il Modello Funzionale I-P-O-S
*Il ciclo di vita di ogni processo informatico, dal clic del mouse al risultato.*

```text
     ┌───────────┐      ┌─────────────────┐      ┌───────────┐
     │   INPUT   │ ───> │   PROCESSING    │ ───> │  OUTPUT   │
     └───────────┘      │  (Elaborazione) │      └───────────┘
                        └────────┬────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │     STORAGE     │
                        │ (Archiviazione) │
                        └─────────────────┘
```

* 📥 **1. INPUT (Ingresso dati):**
  * Ricezione di stimoli o dati dall'esterno.
  * *Periferiche:* Tastiera, mouse, microfono, webcam, scanner, sensori.
* ⚙️ **2. PROCESSING (Elaborazione):**
  * Trasformazione logico-matematica dei dati in ingresso secondo un programma.
  * *Componente chiave:* **CPU** (Central Processing Unit).
* 📤 **3. OUTPUT (Uscita risultati):**
  * Comunicazione del risultato dell'elaborazione all'utente o a un'altra macchina.
  * *Periferiche:* Monitor, altoparlanti, stampante, attuatori.
* 🗄️ **4. STORAGE (Memorizzazione / Archiviazione):**
  * Salvataggio dei dati per renderli persistenti nel tempo quando l'alimentazione si spegne.
  * *Supporti:* SSD, Hard Disk, chiavette USB, memorie cloud.

---

## 💻 MODULO LABORATORIO (2 Ore Consecutive)

### ├── [2.1] Lo Shock Culturale: Smartphone vs Computer
*Punto critico generazionale: smontare l'illusione della "galleria" o dei "download magici".*

* **Il modello "App-Centrico" dello smartphone:**
  * I file sono nascosti dentro le singole app (Instagram gestisce le foto, WhatsApp i messaggi).
  * I ragazzi non sanno dove risieda il file sul disco: usano la ricerca globale o la galleria.
* **Il modello "File-Centrico" del PC da tecnico:**
  * Un perito informatico **deve sapere esattamente il percorso fisico** di una risorsa.
  * Il disco rigido è un magazzino unico in cui ogni singolo elemento ha una "via, numero civico e piano".

---

### ├── [2.2] L'Architettura del File System (L'Albero Rovesciato)
*Come il sistema operativo organizza miliardi di byte in modo deterministico.*

```text
C:\ (Radice / Root Directory)
├── Programmi\
│   └── VideoLAN\
│       └── vlc.exe
├── Windows\
└── Utenti\
    └── MarioRossi\
        ├── Documenti\
        │   └── Scuola\
        │       └── Informatica\          <-- Cartella di lavoro
        │           ├── Teoria\
        │           └── Esercizi\
        │               └── compito1.txt  <-- Foglia dell'albero (File)
        └── Desktop\
```

* 🌳 **Regole della struttura gerarchica ad albero:**
  * **Root (Radice):** In ambiente Windows è identificata dalla lettera dell'unità seguita da due punti e barra rovesciata (`C:\`). Nei sistemi Linux è semplicemente lo slash (`/`).
  * **Nodi intermedi:** Le **Cartelle (Directory)**, che contengono altre cartelle (sottocartelle) o file.
  * **Foglie:** I **File**, che non possono contenere altri file al loro interno.
* 📍 **Percorso Assoluto vs Percorso Relativo:**
  * **Percorso Assoluto (*Absolute Path*):** L'indirizzo completo partendo dalla radice.
    * *Sintassi:* `C:\Utenti\MarioRossi\Documenti\Scuola\compito1.txt`
    * *Regola:* È univoco in tutto il sistema.
  * **Percorso Relativo (*Relative Path*):** La posizione di un file a partire dalla cartella in cui ci si trova in questo momento.
    * *Se mi trovo in:* `C:\Utenti\MarioRossi\Documenti\Scuola\`
    * *Il file si trova in:* `.\compito1.txt` oppure per salire di un livello `..\`

---

### ├── [2.3] Anatomia di un File: Nome, Estensione e Sicurezza
*Il file non è solo un'icona: è un flusso binario con etichette.*

```text
             RELAZIONE_HARDWARE . docx
             └────────┬───────┘   └─┬┘
                      │             │
                NOME BASE      ESTENSIONE
         (Significato umano)   (Formato dati / Associazione OS)
```

* 🏷️ **1. Nome Base:**
  * Descrive il contenuto (regola d'oro: *vietati caratteri speciali come `\ / : * ? " < > |` che il file system riserva per i comandi*).
* 🏷️ **2. Estensione (da 3 a 4 caratteri dopo il punto):**
  * Dice al Sistema Operativo **come interpretare i bit** e quale programma predefinito lanciare per aprirlo.
  * *Tipi di estensione comuni:*
    * Documenti: `.txt` (testo puro), `.docx` (Word compresso/XML), `.pdf` (formato fisso).
    * Immagini: `.jpg` / `.jpeg` (compresso con perdita), `.png` (trasparenza), `.svg` (vettoriale).
    * Eseguibili: `.exe` (binario eseguibile Windows), `.bat` / `.sh` (script di comandi).
    * Codice sorgente: `.cpp` (C++), `.java` (Java), `.py` (Python).
* ⚠️ **3. Il Rischio Sicurezza ("L'inganno della doppia estensione"):**
  * Mostrare perché Windows nasconde le estensioni di default per gli utenti comuni.
  * Esempio di malware: un file malevolo chiamato `foto_vacanze.jpg.exe`. Se le estensioni sono nascoste, l'utente vede solo `foto_vacanze.jpg` con l'icona di un'immagine, ci clicca sopra e avvia un virus eseguibile.

---

### ├── [2.4] Esercitazione Pratica Guidata al PC (Durata: 60 minuti)

#### FASE A: Smascherare il Sistema Operativo (10 min)
1. Aprire **Esplora File** (`Tasto Windows + E`).
2. Andare nella barra superiore: menu **Visualizza** $\rightarrow$ **Mostra** (oppure *Opzioni Cartella*).
3. Mettere la spunta obbligatoria su: **☑ Estensioni nomi file** e **☑ Elementi nascosti**.
4. Spiegare visivamente alla classe come tutte le icone del desktop ora mostrino il suffisso (es. `.lnk`, `.png`).

#### FASE B: Costruzione dell'Infrastruttura Annuale (20 min)
Ogni studente deve creare manualmente la propria struttura di archiviazione dati personale sul disco locale (o sulla partizione dati `D:\` se configurata in istituto):

```text
[TuoCognome]_Informatica_1CI/
├── 01_Teoria_Appunti/
├── 02_Relazioni_Laboratorio/
│   ├── Bozze/
│   └── Consegne_PDF/
├── 03_Algoritmi_Flowgorithm/
└── 04_Risorse_Condivise/
```

#### FASE C: L'Esperimento dell'Estensione (15 min)
1. Entrare nella cartella `01_Teoria_Appunti/`.
2. Fare clic destro $\rightarrow$ *Nuovo* $\rightarrow$ *Documento di testo* (`Nuovo documento di testo.txt`).
3. Ridenominarlo in `test_lettura.txt`, aprirlo con Blocco Note, scrivere *"Benvenuto nel mondo dell'informatica"* e salvare (`Ctrl + S`).
4. Ridenominare il file da `test_lettura.txt` a `test_lettura.doc`.
5. Osservare l'avviso di Windows: *"Se si modifica l'estensione, il file potrebbe essere inutilizzabile. Modificare l'estensione?"* $\rightarrow$ Cliccare **Sì**.
6. Notare che l'icona è diventata quella di Word.
7. Ridenominarlo infine in `test_lettura.xyz`. Provare ad aprirlo con doppio clic.
8. **Momento didattico:** Far vedere che il computer chiede *"Come vuoi aprire questo file?"* perché non ha più la tabella di associazione per l'estensione `.xyz`.

#### FASE D: Il Gioco dei Percorsi Assoluti (15 min)
* Aprire il file creato, cliccare sulla barra degli indirizzi in alto in Esplora File: il percorso si trasforma in testo.
* Copiare il percorso assoluto (es. `C:\Users\Postazione04\Rossi_Informatica_1CI\01_Teoria_Appunti\test_lettura.txt`).
* Incollarlo come testo nel primo compito aperto su Google Classroom.

---

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma Lezione Teorica (55 min)
* **00-05 min | Accoglienza e richiamo:** Saluto veloce, verifica presenze al registro.
* **05-15 min | L'Hook d'apertura:** Scrivi alla lavagna solo il numero `40`. Chiedi: *«Che cos'è?»*. Raccogli risposte (*«Un numero», «L'età di mio papà», «I gradi oggi»*). Da qui fai scattare la definizione: finché non do il contesto, è solo un **dato**.
* **15-30 min | Lavagna Partecipata:** Disegna la piramide Dato-Info-Conoscenza e il diagramma a blocchi Input-CPU-Output-Memoria. Fai associare dagli studenti gli oggetti reali della stanza (mouse, tastiera, schermo) ai blocchi.
* **30-45 min | Hardware vs Software:** Chiarisci la metafora della musica: lo spartito e le note (Software) contro lo strumento musicale fisico (Hardware). Nessuno dei due suona da solo.
* **45-55 min | Chiusura e verifica rapida:** Fai 3 domande a trabocchetto a bruciapelo a tutta la classe (*«Lo scanner è input o output? E una stampante multifunzione?»*).

### ✍️ Disegno Guida da fare alla Lavagna (Lezione 1)

```text
    ┌─────────────────────────────────────────────────────────┐
    │              PIRAMIDE DELL'INFORMAZIONE                 │
    │                                                         │
    │                   /  CONOSCENZA  \   -> Decisione       │
    │                  /────────────────\                     │
    │                 /   INFORMAZIONE   \  -> Dato + Senso   │
    │                /────────────────────\                   │
    │               /         DATO         \ -> Grezzo (38.5) │
    │              /────────────────────────\                 │
    └─────────────────────────────────────────────────────────┘
```

### 🎯 Micro-Task Formativa per Casa (Spaced Retrieval - 5 minuti)
Carica su Google Classroom questo brevissimo compito (senza voto punitivo, solo spunta di completamento):
> *"Trova un esempio reale nella tua vita quotidiana che mostri il passaggio da:  
> 1. Un Dato grezzo  
> 2. L'Informazione contestualizzata  
> 3. La Conoscenza/Azione che ne deriva"*  
> *(Esempio vietato: la febbre usato dal prof!)*