# SETT-OTT
Ecco il piano operativo dettagliato **settimana per settimana** per i primi due mesi (**Settembre e Ottobre**, circa 7–8 settimane di lezione) per la tua classe prima.

Il monte ore è strutturato sullo standard dell'istituto tecnico: **1 ora di teoria in classe** + **2 ore consecutive di laboratorio** (in compresenza con l'ITP).

---

## 🧭 Quadro Settimana per Settimana (Settembre – Ottobre)

```
┌───────────┬──────────────────────────────────┬─────────────────────────────────────┐
│ SETTIMANA │ TEORIA (1h - In classe)          │ LABORATORIO (2h - Con ITP)          │
├───────────┼──────────────────────────────────┼─────────────────────────────────────┤
│ Sett. 1   │ Accoglienza                      │ Login, regole lab, Google Workspace │
│ Sett. 2   │ Dato vs Info, Hardware vs SW     │ File System reale: cartelle ed estens.│
│ Sett. 3   │ Il Bit, il Byte e le potenze del 2│ Word/Writer: struttura e formattazione│
│ Sett. 4   │ Conversioni: Decimale ↔ Binario  │ Word/Writer: tabelle, immagini, layout│
│ Sett. 5   │ Sistema Esadecimale (e Ottale)   │ Inizio Relazione Tecnica sull'Hardware│
│ Sett. 6   │ Conversioni dirette Binario ↔ Hex│ Completamento e consegna Relazione   │
│ Sett. 7   │ Ripasso attivo e simulazione test│ Peer-review e gestione Google Drive  │
│ Sett. 8   │ 📝 VERIFICA SCRITTA 1 (Numeraz.) │ Laboratorio di recupero / approfond.│
└───────────┴──────────────────────────────────┴─────────────────────────────────────┘
```

---

## 📝 Dettaglio Operativo dei Moduli

---

### SETTIMANA 1: L'Inizio, la Cornice di Senso e le Regole
*L'obiettivo è rompere il ghiaccio, impostare il clima di lavoro e far accedere tutti ai sistemi scolastici.*

* **Teoria (1h):**
  * **Discorso di inizio anno:** *«Perché studiamo informatica?»* (la cornice di senso: diventare creatori consapevoli, non consumatori passivi).
  * Il gioco del "Robot Umano" (l'alunno-computer che esegue solo comandi letterali) per mostrare l'esigenza del rigore logico.
  * Presentazione del patto formativo (come funzionano le verifiche, niente paura degli errori).
* **Laboratorio (2h):**
  * Consegna credenziali istituzionali (`nome.cognome@caramuelroncalli.it`).
  * Assegnazione fissa delle postazioni PC (fondamentale per la disciplina e per responsabilizzarli sull'hardware).
  * Accesso a **Google Classroom** e primo messaggio di prova.
  * Regole del laboratorio: niente cibo/bevande, rispetto delle periferiche, come lasciare la postazione a fine ora.
* 📌 **Cosa devi ripassare tu:**
  * Nessuna teoria complessa: accertati solo con la segreteria o con l'animatore digitale che le credenziali degli allievi siano attive.

---

### SETTIMANA 2: Dato vs Informazione e il File System Reale
*L'obiettivo è smontare l'idea che il computer sia magico e insegnare dove finiscono fisicamente i file.*

* **Teoria (1h):**
  * **Dato vs Informazione vs Conoscenza:**
    * Dato: grezzo, privo di contesto (es. `39`).
    * Informazione: dato contestualizzato con significato (es. `39 °C di febbre`).
  * **Hardware vs Software:** le componenti visibili (ferro) contro i programmi (istruzioni).
  * Il modello a blocchi essenziale: Input $\rightarrow$ Elaborazione $\rightarrow$ Output $\rightarrow$ Memorizzazione.
* **Laboratorio (2h):**
  * **Il dramma moderno dei nativi digitali:** spiegare cos'è una cartella e un percorso (*Path*).
  * La struttura ad albero: radice (`C:\`), directory genitore, sottocartelle.
  * Le **estensioni dei file**: abilitare in Windows *«Mostra estensioni nomi file»* (spiegare cosa succede se rinomini un `.docx` in `.txt`).
  * **Esercizio pratico:** creare sul desktop una cartella di lavoro ordinata:
    `Informatica_2026/` $\rightarrow$ `Teoria/`, `Laboratorio/`, `Verifiche/`.
* 📚 **Cosa devi ripassare tu:**
  * La differenza tra percorso assoluto (es. `C:\Scuola\Doc.txt`) e relativo (es. `..\Doc.txt`).

---

### SETTIMANA 3: Perché il Binario? Bit, Byte e Multipli
*L'obiettivo è far capire perché il computer conta solo fino a 1 e come quantificare la memoria.*

* **Teoria (1h):**
  * Il transistor come interruttore (Stato Alto / Basso, $1 / 0$, Vero / Falso).
  * Il **Bit** (Binary Digit) come unità minima.
  * La combinatoria base: quanti stati posso rappresentare con $N$ bit? Formula: $2^N$.
    * Con 1 bit: $2^1 = 2$ stati ($0, 1$).
    * Con 2 bit: $2^2 = 4$ stati ($00, 01, 10, 11$).
    * Con 8 bit (il **Byte**): $2^8 = 256$ combinazioni ($0 \dots 255$).
  * I multipli moderni (KB, MB, GB, TB) e la discrepanza tra prefissi decimali ($10^3 = 1000$) e binari ($2^{10} = 1024$, KiB).
* **Laboratorio (2h):**
  * **Elaborazione Testi (Word / LibreOffice Writer):**
  * Impostazione della pagina: margini standard (2.5 cm), orientamento, interlinea 1.15.
  * Uso corretto della tastiera: maiuscole con `Shift` (non con `Caps Lock`), punteggiatura attaccata alla parola precedente e seguita da uno spazio.
  * Gerarchia del testo: usare gli **Stili** (Titolo 1, Titolo 2, Corpo testo), non ingrandire il font a caso.
* 📚 **Cosa devi ripassare tu:**
  * Ricordati a memoria le potenze del 2 da $2^0$ a $2^{10}$ ($1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024$).

---

### SETTIMANA 4: Matematica Binaria (Decimale $\leftrightarrow$ Binario)
*L'obiettivo è rendere operativi gli studenti con la conversione tra base 10 e base 2.*

* **Teoria (1h):**
  * Concetto di **notazione posizionale** (ripasso di come funziona la base 10: $345 = 3\cdot10^2 + 4\cdot10^1 + 5\cdot10^0$).
  * **Da Binario a Decimale (Metodo dei pesi):**
    * $(1101)_2 = 1\cdot2^3 + 1\cdot2^2 + 0\cdot2^1 + 1\cdot2^0 = 8 + 4 + 0 + 1 = 13_{10}$.
  * **Da Decimale a Binario (Metodo delle divisioni successive per 2):**
    * Spiegare come raccogliere i resti dal basso verso l'alto (dal meno significativo al più significativo).
* **Laboratorio (2h):**
  * **Word/Writer Avanzato:**
  * Inserimento e formattazione di **Tabelle** (utile per costruire la tabella delle potenze del 2).
  * Inserimento immagini con posizionamento "incorniciato" o "in linea con il testo".
  * Inserimento di formule matematiche semplici tramite l'editor di equazioni di Word.
  * Esercizio: redigere una scheda di riepilogo impaginata con 5 conversioni svolte e commentate.
* 📚 **Cosa devi ripassare tu:**
  * Fai rapidamente alla lavagna 3 esempi numerici: un numero dispari piccolo (es. 25), uno pari (es. 42), uno vicino a una potenza di 2 (es. 63).

---

### SETTIMANA 5: L'Esadecimale e il colore dei pixel
*L'obiettivo è introdurre la base 16 non come tortura matematica, ma come "scorciatoia comoda" per gli informatici.*

* **Teoria (1h):**
  * Perché l'uomo usa la base 10 (10 dita), il PC la base 2, ma gli informatici amano la base 16 (**Esadecimale**).
  * I simboli: $0 \dots 9$ e le lettere $A (10), B (11), C (12), D (13), E (14), F (15)$.
  * Cenni sul sistema Ottale (base 8, raggruppamento a 3 bit).
  * Il legame magico tra binario ed esadecimale: $2^4 = 16 \rightarrow$ **1 cifra esadecimale rappresenta esattamente 4 bit (un nibble).**
  * Esempi pratici nel mondo reale: i codici colore RGB sul web (`#FF0000` = Rosso puro) e gli indirizzi MAC.
* **Laboratorio (2h):**
  * **Avvio del Compito Autentico (Relazione Tecnica di Laboratorio):**
  * Consegna: *"Relazione descrittiva sull'architettura interna del computer"*.
  * Gli studenti devono strutturare un documento Word formale contenente:
    1. Frontespizio (Titolo, Nome, Classe, Data).
    2. Sommario automatico (generato dagli Stili Titolo 1 e 2).
    3. Descrizione delle componenti hardware (CPU, RAM, SSD, Scheda Madre).
    4. Tabella riassuntiva con grandezze e multipli.
* 📚 **Cosa devi ripassare tu:**
  * La tabella di corrispondenza rapida:
    * `0000` = `0`, `0001` = `1` ... `1010` = `A`, `1111` = `F`.

---

### SETTIMANA 6: Conversioni Dirette e Chiusura della Relazione
*L'obiettivo è consolidare la conversione rapida Binario $\leftrightarrow$ Esadecimale e chiudere la prima valutazione pratica.*

* **Teoria (1h):**
  * **La conversione rapida (senza passare dal decimale):**
    * Da Binario a Hex: raggruppare a blocchi di 4 bit da destra verso sinistra.
      * Esempio: `11010110` $\rightarrow$ `1101` (`D`) e `0110` (`6`) $\rightarrow$ `D6`.
    * Da Hex a Binario: "esplodere" ogni cifra esadecimale in 4 bit.
      * Esempio: `3A` $\rightarrow$ `3` (`0011`) e `A` (`1010`) $\rightarrow$ `00111010`.
* **Laboratorio (2h):**
  * Revisione finale del documento Word: correzione ortografica automatica, numeri di pagina (esclusa la prima).
  * Esportazione del lavoro in **formato PDF** (spiegare perché ai professori e nei contesti professionali si invia il PDF e non il file modificabile `.docx`).
  * Consegna ufficiale del file su Google Classroom entro fine ora.
  * 🎯 **Questa consegna rappresenta il tuo primo voto pratico di laboratorio!**
* 📚 **Cosa devi ripassare tu:**
  * Come valutare rapidamente la relazione: prepara una griglietta da 10 punti (3 pt struttura/stili, 3 pt correttezza nozioni hardware, 2 pt formattazione tabelle/immagini, 2 pt rispetto tempi e consegna in PDF).

---

### SETTIMANA 7: Ripasso Attivo e Preparazione alla Verifica
*L'obiettivo è applicare il principio di "Retrieval Practice" per abbattere l'ansia e colmare i vuoti prima del test sommativo.*

* **Teoria (1h):**
  * **Simulazione di Verifica (Mock Test):**
    * Assegna alla lavagna 4 esercizi identici a quelli della verifica (2 conversioni dec-bin, 1 bin-hex, 1 domanda teorica a risposta sintetica).
    * Dai loro 15 minuti di tempo per risolverli in silenzio su un foglio.
    * Correzione collettiva alla lavagna: fai salire gli studenti a scrivere i passaggi, evidenziando gli errori tipici (es. dimenticarsi lo zero nei resti delle divisioni).
* **Laboratorio (2h):**
  * **Attività di Peer Review (Valutazione tra pari):**
    * A coppie, ciascuno studente legge il PDF della relazione del compagno e gli segnala due punti di forza e un errore di impaginazione o di contenuto.
  * Configurazione avanzata di Google Drive: condivisione cartelle, permessi di visualizzazione vs modifica, creazione di copie di backup nel cloud.
* 📚 **Cosa devi ripassare tu:**
  * Prepara il testo della verifica scritta (prevedendo due file: Fila A e Fila B per evitare che copino).

---

### SETTIMANA 8: La Prima Verifica Sommativa
*L'obiettivo è misurare l'acquisizione delle competenze teoriche del primo bimestre.*

* **Teoria (1h):**
  * 📝 **VERIFICA SCRITTA N. 1 (Sistemi di Numerazione e Teoria Base)**
  * *Struttura ideale (tempo: 50 minuti):*
    * Parte 1: 4 domande a risposta multipla su Concetti IT, Dato/Informazione, Bit/Byte (2 punti).
    * Parte 2: 2 conversioni Decimale $\rightarrow$ Binario con divisioni visibili (2.5 punti).
    * Parte 3: 2 conversioni Binario $\rightarrow$ Decimale con calcolo dei pesi (2.5 punti).
    * Parte 4: 2 conversioni dirette Binario $\leftrightarrow$ Esadecimale (2 punti).
    * Parte 5: 1 domanda aperta: *"Spiega con parole tue perché il computer usa la numerazione binaria invece di quella decimale"* (1 punto).
* **Laboratorio (2h):**
  * Lezione di decompressione: introduzione a **PowerPoint / Impress** (inizia il modulo della Fase 2).
  * Regole d'oro per creare slide: la regola del contrasto cromatico, dimensioni minime dei font (mai sotto i 24pt), uso di elenchi puntati sintetici.
* 📚 **Cosa devi fare tu:**
  * Correggi le verifiche entro massimo una settimana (il feedback deve essere tempestivo per avere valore pedagogico).

---

### 💡 Consigli di sopravvivenza per queste prime 8 settimane:
1. **L'ora di teoria dura poco:** 50-55 minuti volano. Non spendere 30 minuti a spiegare; fai **15 minuti di teoria netta alla lavagna** e poi **fai fare esercizi a loro sul quaderno**, girando tra i banchi a controllare.
2. **Pretendi il quaderno di informatica:** Anche se siamo al computer, le conversioni binarie e i conti si fanno **a penna**. Chi non scrive a mano non fissa l'algoritmo di calcolo nel cervello.
3. **Fai squadra con l'ITP:** Prima di ogni blocco di laboratorio di 2 ore, spendi 2 minuti alla ricreazione con lui: *«Oggi facciamo impaginare questo documento Word, io seguo la fila destra e tu la sinistra per verificare che usino gli stili corretti»*. Dividersi l'aula a metà dimezza lo stress.

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