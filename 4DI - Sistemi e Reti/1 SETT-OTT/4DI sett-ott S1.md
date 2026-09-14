Ecco il kit didattico completo per la **Settimana 1**, strutturato come una **mappa concettuale espansa (mindmap ad albero)** con tutti i contenuti pronti per essere spiegati alla lavagna e svolti al PC.

> Nota: il quadro sinottico delle 8 settimane e il dettaglio sintetico settimana per settimana si trovano in [4DI - SETT-OTT.md](4DI%20-%20SETT-OTT.md).

---

# 🗺️ SETTIMANA 1: RIPARTENZA DALLO STACK — ISO/OSI, TCP/IP E INCAPSULAMENTO

```text
SETTIMANA 1
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] Presentazione del Corso e del Percorso Cisco CCNA1
│   ├── [1.2] Il Modello ISO/OSI: 7 Livelli, 7 Compiti
│   ├── [1.3] Il Modello TCP/IP: la Versione "Pratica" dello Stack
│   └── [1.4] PDU e Incapsulamento/Decapsulamento
│
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] Iscrizione alla Piattaforma Cisco NetAcad (CCNA1)
│   ├── [2.2] Ripasso Rapido di Cisco Packet Tracer
│   ├── [2.3] Prima Topologia: PC – Switch – Router
│   └── [2.4] Esercitazione Pratica Guidata (Missione: "Segui il Pacchetto")
│
└── 📋 GUIDA DI REGIA PER IL DOCENTE
    ├── Scaletta Minuto per Minuto
    ├── Schema da Disegnare alla Lavagna
    └── Micro-Task di Consolidamento (Formative Assessment)
```

---

## 🧠 MODULO TEORICO (2 Ore in Aula)

### ├── [1.1] Presentazione del Corso e del Percorso Cisco CCNA1
*Obiettivo: dare un quadro chiaro dell'anno, motivando l'ingresso nella certificazione Cisco.*

* 📌 **Il programma dell'anno:** dal livello Network (IP, subnetting, routing) al livello Transport (TCP/UDP) fino al livello Applicativo (HTTP, FTP, DNS, posta elettronica) e sicurezza di base.
* 📌 **La certificazione Cisco CCNA1 (*Introduction to Networks*):** un percorso strutturato in capitoli con quiz di autovalutazione, che accompagnerà tutto l'anno in parallelo al programma curricolare.
* 🎯 **Perché ripartire da ISO/OSI e TCP/IP:** sono la "mappa" concettuale che permette di collocare correttamente ogni protocollo che studieremo (IP, TCP, HTTP, ...) al livello giusto.

---

### ├── [1.2] Il Modello ISO/OSI: 7 Livelli, 7 Compiti
*Obiettivo: ripassare la struttura completa del modello di riferimento teorico.*

#### **Introduzione: Perché 7 livelli?**

Immagina un'azienda grande con reparti diversi:
- Chi risponde al telefono (comunicazione con il cliente esterno).
- Chi "traduce" le richieste in linguaggio interno (segreteria).
- Chi organizza il lavoro vero e proprio (ufficio operazioni).
- Chi scrive i dati su carta (archivio).
- Chi spedisce le lettere (corriere).
- Chi guida il furgone (autista).
- Il motore e le ruote (mezzo fisico).

Ognuno di questi **non ha bisogno di sapere cosa fa l'altro**: il colloquio con il cliente non cambia, che sia scritto su carta o salvato al computer. Il corriere non sa quali documenti sta portando, sa solo che ne ha un pacco da spedire. Il motore non sa niente della lettera che trasporta.

**Lo stesso accade in una rete di computer.** Il modello ISO/OSI (International Organization for Standardization / Open Systems Interconnection) definisce **7 livelli separati**, ognuno con un compito preciso, e nessuno "sa" cosa fanno gli altri livelli oltre a ricevere servizi da quelli sotto e fornire servizi a quelli sopra.

---

#### **La Torre ISO/OSI: i 7 Livelli in Dettaglio**

```text
        MODELLO ISO/OSI (dall'alto verso il basso)
┌───┬─────────────────────────────────────────────────┐
│ 7 │ APPLICATION   → interfaccia con l'utente/app     │
│ 6 │ PRESENTATION  → formato dati, cifratura, compress.│
│ 5 │ SESSION       → apertura/gestione/chiusura sessioni│
│ 4 │ TRANSPORT     → comunicazione end-to-end, porte  │
│ 3 │ NETWORK       → indirizzamento logico, instradam.│
│ 2 │ DATA LINK     → indirizzamento fisico (MAC), frame│
│ 1 │ PHYSICAL      → trasmissione dei bit sul mezzo   │
└───┴─────────────────────────────────────────────────┘
```

---

##### **LIVELLO 7 — APPLICATION (Applicativo)**
* **Chi lo gestisce:** il software che usi (browser Firefox, client email Outlook, Telegram, WhatsApp).
* **Cosa fa:** fornisce un'interfaccia tra l'utente/applicazione e la rete. Non si occupa di come i dati viaggiano, ma **cosa** i dati rappresentano: una richiesta HTTP per una pagina web, una query SMTP per spedire un'email, una richiesta FTP per scaricare un file.
* **Esempi di protocolli:** HTTP (web), HTTPS (web sicuro), SMTP (spedire email), IMAP (ricevere email), FTP (trasferimento file), DNS (traduzione nomi in indirizzi), SSH (connessione remota sicura).
* **Metafora:** il bancario che accoglie il cliente, capisce cosa vuole (aprire conto, fare trasferimento) e genera il modulo giusto.

---

##### **LIVELLO 6 — PRESENTATION (Presentazione)**
* **Chi lo gestisce:** software di medio-livello, codec, librerie di compressione e crittografia.
* **Cosa fa:** **trasforma il formato dei dati** in modo che siano "intelligibili" a destinazione.
  * **Compressione:** riduce la dimensione dei dati (es. JPG è JPEG compresso da BMP).
  * **Crittografia:** trasforma dati leggibili in dati cifrati (es. HTTPS cifra la comunicazione HTTP).
  * **Conversione di codifiche:** trasforma un file scritto in UTF-8 in ANSI, o viceversa.
* **Esempi:** codifica video H.264, compressione MP3, SSL/TLS (cifratura HTTPS), JPEG (compressione immagini).
* **Metafora:** il traduttore che converte il modulo dal bancario da carta a formato digitale, lo crittografa se sensibile, lo comprime se pesante.

---

##### **LIVELLO 5 — SESSION (Sessione)**
* **Chi lo gestisce:** software di medio-livello, spesso invisibile all'utente.
* **Cosa fa:** **apre, mantiene e chiude in modo ordinato la comunicazione** tra due applicazioni.
  * Quando accedi a Facebook, il livello Session apre una "sessione": una conversazione logica tra il tuo browser e il server Facebook.
  * Se il collegamento si interrompe, la sessione "sa" da dove ricominciare (non devi ricominciare da zero).
  * Quando esci da Facebook, il livello Session **chiude ordinatamente** la sessione.
* **Esempi:** gestione delle sessioni utente, checkpoint di una download interrotta, login/logout ordinato.
* **Metafora:** lo "sportellista di gestione" che assegna una pratica a un operatore, la segue finché non termina, e la archivia quando è finita.

---

##### **LIVELLO 4 — TRANSPORT (Trasporto)**
* **Chi lo gestisce:** il sistema operativo (Windows, Linux, macOS) tramite stack TCP/IP.
* **Cosa fa:** **garantisce una comunicazione end-to-end affidabile (o veloce)** tra due applicazioni su computer diversi.
  * **TCP (Transmission Control Protocol):** garantisce che i dati arrivino **completi, intatti e nell'ordine giusto**, ma è più lento (controlla errori, ritrasmette, ordina i pacchetti).
  * **UDP (User Datagram Protocol):** manda i dati **velocemente senza garanzie** (non controlla errori, non ritrasmette): perfetto per video/audio live dove perdere qualche frame è accettabile.
  * **Porte:** identifica quale applicazione deve ricevere i dati (es. porta 80 per HTTP, porta 443 per HTTPS, porta 25 per SMTP).
* **Esempi:** TCP per email e file transfer (dati critici), UDP per video live e gaming (velocità prioritaria).
* **Metafora:** il **corriere** che controlla se il pacco è arrivato intatto (TCP) o se lo vuol fare in fretta anche a rischio di rotture (UDP).

---

##### **LIVELLO 3 — NETWORK (Rete)**
* **Chi lo gestisce:** il router e lo stack TCP/IP del sistema operativo.
* **Cosa fa:** **instrada i pacchetti da una rete a un'altra usando indirizzi IP**.
  * Quando invii dati, il livello Network sa che il destinatario è in una rete diversa dalla tua, quindi decide quale percorso seguire   (routing).
  * Usa **indirizzi IP** (es. `192.168.1.1`) per identificare la sorgente e la destinazione a livello logico/software.
  * Divide i segmenti del livello 4 in "pacchetti", aggiungendo l'intestazione IP (source/destination IP).
* **Esempi:** protocollo IP (IPv4, IPv6), routing dinamico (OSPF, BGP), ICMP (ping/traceroute).
* **Metafora:** il **numero civico della casa** — identifica la destinazione finale a livello geografico (anche se il corriere non sa esattamente dove sia fisicamente).

---

##### **LIVELLO 2 — DATA LINK (Collegamento Dati)**
* **Chi lo gestisce:** la scheda di rete (NIC — Network Interface Card) e lo switch.
* **Cosa fa:** **collega direttamente due dispositivi nello stesso "pezzo di rete" (LAN) usando indirizzi MAC**.
  * Un **indirizzo MAC (Media Access Control)** è l'indirizzo **fisico** della scheda di rete (es. `00:1A:2B:3C:4D:5E`), diverso dall'indirizzo IP.
  * Lo switch (livello 2) usa la tabella MAC per sapere su quale porta fisica deve mandare il frame (blocco di dati incapsulato).
  * I pacchetti del livello Network (che contengono IP) vengono incapsulati in **frame** del livello Data Link (che contengono MAC).
* **Esempi:** Ethernet (standard cablato LAN), WiFi/802.11 (wireless), MAC addressing, ARP (traduce IP in MAC).
* **Metafora:** l'**indirizzo della strada** — una volta che conosci il numero civico (IP), devi sapere anche il nome della strada (MAC) per arrivare alla casa vicina a destra.

---

##### **LIVELLO 1 — PHYSICAL (Fisico)**
* **Chi lo gestisce:** il cavo di rete, la scheda di rete, il trasmettitore/ricevitore wireless.
* **Cosa fa:** **trasmette i bit grezzi (0 e 1) sul mezzo fisico**.
  * Un frame del livello Data Link è una sequenza ordinata di bit: `01001101010101...`
  * Il livello Physical prende questi bit e li trasmette:
    * **Su cavo Ethernet:** come impulsi elettrici (voltaggio alto = 1, basso = 0).
    * **Su WiFi:** come onde radio.
    * **Su fibra ottica:** come impulsi di luce.
  * Definisce anche le caratteristiche fisiche: tipologie di cavi (Cat5e, Cat6), frequenze radio (2.4 GHz, 5 GHz), velocità di trasmissione (100 Mbps, 1 Gbps).
* **Esempi:** cablo Ethernet RJ45, WiFi 802.11a/b/g/n/ac, fibra ottica, connettori, voltaggio, frequenze.
* **Metafora:** il **foglio di carta e l'inchiostro** — il mezzo fisico su cui scrivi il messaggio.

---

#### **Principio Chiave: Astrazione per Strati**

Ogni livello fornisce un **servizio** al livello superiore e si appoggia ai **servizi** del livello inferiore, **senza "vedere" cosa succede oltre i suoi vicini immediati**.

**Esempio pratico:** quando apri una pagina web:
1. **Livello 7 (Application):** il browser dice "voglio la pagina `www.google.com`" → genera richiesta HTTP
2. **Livello 6 (Presentation):** nessuna trasformazione particolare per HTTP (ma se fosse HTTPS, cifra qui)
3. **Livello 5 (Session):** apre una sessione con il server Google
4. **Livello 4 (Transport):** TCP incapsula il dati in segmenti, usa porta 80 (HTTP) o 443 (HTTPS)
5. **Livello 3 (Network):** IP aggiunge l'indirizzo di Google (es. `142.250.185.46`), il router decide il percorso
6. **Livello 2 (Data Link):** la scheda di rete traduce l'indirizzo IP in MAC (tramite ARP), lo switch lo inoltra
7. **Livello 1 (Physical):** i bit viaggiano sul cavo/WiFi fino al server Google

**Al destinatario, il processo si inverte:** il server riceve i bit, li decodifica, toglie un layer di intestazione dopo l'altro (decapsulamento), finché non ottiene i dati originali HTTP.

---

#### **Tecnica Mnemonica Classica**

*"**All People Seem To Need Data Processing**"*

- **A**pplication (7)
- **P**resentation (6)
- **S**ession (5)
- **T**ransport (4)
- **N**etwork (3)
- **D**ata Link (2)
- **P**rocessing = Physical (1)

---

### ├── [1.3] Il Modello TCP/IP: la Versione "Pratica" dello Stack
*Obiettivo: mostrare come il modello realmente implementato in Internet sia una versione semplificata dell'OSI.*

#### **Introduzione: ISO/OSI vs TCP/IP**

Quando l'ISO/OSI fu proposto negli anni '80, era teoricamente perfetto. Ma **Internet** (che nel frattempo cresceva selvaggiamente) aveva già scelto un approccio diverso e più pragmatico: il **modello TCP/IP a 4 livelli**.

**Perché TCP/IP ha "vinto"?**
1. **Arrivò prima:** il protocollo IP fu sviluppato negli anni '70 per il progetto ARPANET (precursore di Internet), molto prima che ISO/OSI fosse finito.
2. **Era più semplice:** 4 livelli invece di 7, meno ambiguità su dove mettere certe cose.
3. **Funzionava (e funziona):** Internet è costruita su TCP/IP, e ancora oggi è lo standard di facto.
4. **ISO/OSI rimane prezioso:** per insegnare i concetti teorici e per ragionare a "compartimenti stagni".

**In questo corso useremo entrambi:**
- L'**ISO/OSI** per parlare di concetti astratti ("quale livello fa cosa?").
- Il **TCP/IP** quando parliamo di protocolli reali ("IP è un protocollo di livello 3").

---

#### **Il Modello TCP/IP: 4 Livelli**

```text
     ISO/OSI (7 livelli)              TCP/IP (4 livelli)
┌─────────────────────┐          ┌─────────────────────┐
│ 7 Application        │          │                     │
│ 6 Presentation       │  ────►  │  APPLICATION        │
│ 5 Session            │          │  (HTTP, SMTP, FTP,  │
│                      │          │   DNS, SSH, ...)    │
├─────────────────────┤          ├─────────────────────┤
│ 4 Transport          │  ────►  │  TRANSPORT          │
│                      │          │  (TCP, UDP)         │
├─────────────────────┤          ├─────────────────────┤
│ 3 Network            │  ────►  │  INTERNET (Network) │
│                      │          │  (IP, ICMP, ARP)    │
├─────────────────────┤          ├─────────────────────┤
│ 2 Data Link          │  ────►  │  NETWORK ACCESS      │
│ 1 Physical           │          │  (Link Layer)       │
│                      │          │  (Ethernet, WiFi)   │
└─────────────────────┘          └─────────────────────┘
```

---

#### **Dettaglio dei 4 Livelli TCP/IP**

##### **LIVELLO 4 — APPLICATION (Applicativo)**
* **Combina i livelli ISO/OSI 5, 6, 7** in un unico livello perché in TCP/IP non c'è distinzione rigida tra "cosa gestisce la sessione", "cosa formatta i dati", e "cosa parla con l'utente".
* **Cosa fa:** fornisce protocolli direttamente usabili dalle applicazioni finali.
* **Esempi di protocolli:**
  * **HTTP/HTTPS:** web (port 80/443)
  * **SMTP:** spedire email (port 25)
  * **IMAP/POP3:** ricevere email (port 143/110)
  * **FTP:** file transfer (port 21)
  * **DNS:** traduce nomi in indirizzi IP (port 53)
  * **SSH:** accesso remoto sicuro (port 22)
  * **Telnet:** accesso remoto insicuro (port 23, **deprecato**)

---

##### **LIVELLO 3 — TRANSPORT**
* **Identico all'ISO/OSI livello 4.**
* **Cosa fa:** garantisce la comunicazione end-to-end e identifica le applicazioni tramite le porte.
* **TCP (Transmission Control Protocol):**
  * **Orientato alla connessione:** stabilisce una connessione (handshake a 3 vie) prima di spedire, verifica l'arrivo, e chiude ordinatamente.
  * **Affidabile:** se un pacchetto non arriva, lo ritrasmette; ordina i pacchetti fuori sequenza.
  * **Più lento** perché fa tanti controlli.
  * **Usato per:** email, web, FTP, SSH — tutto quello dove perdere dati è inaccettabile.
* **UDP (User Datagram Protocol):**
  * **Senza connessione:** spedisce i dati direttamente senza stabilire una connessione prima.
  * **Inaffidabile:** se un pacchetto si perde, non se ne accorge, non ritrasmette, non ordina.
  * **Velocissimo** perché non fa controlli.
  * **Usato per:** video live (YouTube, streaming), audio (Spotify), online gaming, Voice over IP (VoIP) — situazioni dove la **velocità è prioritaria rispetto all'affidabilità** (perdere un frame di video è meno grave di avere 2 secondi di ritardo).

---

##### **LIVELLO 2 — INTERNET (Network)**
* **Identico all'ISO/OSI livello 3.**
* **Cosa fa:** instrada i pacchetti da una rete all'altra usando **indirizzi IP**.
* **Protocolli principali:**
  * **IP (IPv4 / IPv6):** il protocollo di base che identifica sorgente e destinazione a livello logico.
  * **ICMP:** Internet Control Message Protocol, usato per diagnostic tool come `ping` e `traceroute`.
  * **ARP:** Address Resolution Protocol, traduce indirizzi IP in indirizzi MAC (vedremo in dettaglio nelle prossime settimane).
* **Concetto chiave:** lavora con **indirizzi IP** (es. `192.168.1.1`), non con indirizzi fisici.

---

##### **LIVELLO 1 — NETWORK ACCESS (Link Layer)**
* **Combina i livelli ISO/OSI 1 e 2** in un unico livello perché la distinzione tra "formattazione del frame" e "trasmissione fisica" non è sempre rigida.
* **Cosa fa:** gestisce il collegamento fisico tra due dispositivi nella stessa rete locale (LAN).
* **Protocolli/Tecnologie:**
  * **Ethernet:** standard cablato LAN (le prese RJ45 che usi).
  * **WiFi (802.11):** standard wireless.
  * **PPP:** Point-to-Point Protocol, per connessioni seriali (storicamente, ora raro).
* **Lavora con:** indirizzi **MAC** (es. `00:1A:2B:3C:4D:5E`), ossia indirizzi fisici della scheda di rete.

---

#### **Perché questo corso userà entrambi i Modelli?**

**Quando dirò "livello di rete", intendo:**
- **Livello 3 (ISO/OSI) = Livello Internet (TCP/IP)** → gestisce IP, routing, indirizzi logici.

**Quando dirò "livello di collegamento", intendo:**
- **Livello 2 (ISO/OSI) = Parte del Livello Network Access (TCP/IP)** → gestisce MAC, switch, frame.

Questa "confusione" di nomi è storica, ma capendo la mappa sopra, non ti perderai mai.

---

### ├── [1.4] PDU e Incapsulamento/Decapsulamento
*Obiettivo: introdurre il meccanismo fondamentale con cui i dati "viaggiano" attraverso lo stack, cruciale per capire ogni protocollo futuro.*

#### **Introduzione: Il Concetto di PDU**

**PDU = Protocol Data Unit** = l'unità di dati che ogni livello dello stack vede e manipola.

Ogni livello **aggiunge il proprio "involucro" (header)** ai dati ricevuti dal livello superiore, creando una nuova PDU per quel livello. Questo processo è chiamato **INCAPSULAMENTO**.

Al destinatario, ogni livello **toglie il proprio involucro** dai dati ricevuti dal livello inferiore, risalendo verso l'applicazione. Questo processo è chiamato **DECAPSULAMENTO**.

---

#### **I Nomi delle PDU a Ogni Livello**

```text
LIVELLO      NOME DELLA PDU       CONTENUTO
═════════════════════════════════════════════════════════════════
7 (App)      DATI                 Dati grezzi (es. HTML, JSON)
4 (Transport)SEGMENTO (TCP)        [Header TCP/UDP | DATI]
             DATAGRAM (UDP)
3 (Network)  PACCHETTO             [Header IP | Segmento]
2 (Data Link)FRAME                 [Header MAC | Pacchetto | Trailer CRC]
1 (Physical) STREAM DI BIT         01001101010101110... (impulsi su cavo)
```

**Nomi fondamentali da memorizzare:**
- **Segmento** = PDU al livello 4 (Transport)
- **Pacchetto** = PDU al livello 3 (Network)
- **Frame** = PDU al livello 2 (Data Link)

---

#### **Incapsulamento Dettagliato: Lato Mittente**

Immaginiamo che tu voglia spedire un'email di 100 byte dal tuo PC al server Gmail. Ecco come i dati scendono attraverso lo stack:

##### **Fase 1: Applicazione genera i DATI**
```
L7 (Application):
┌─────────────────────────────────────┐
│ DATI (corpo email)                  │ ← 100 byte
│ "Ciao, come stai?"                  │
└─────────────────────────────────────┘
```
Il client SMTP (livello applicativo) crea il messaggio di 100 byte.

---

##### **Fase 2: Transport aggiunge il suo Header → SEGMENTO**
```
L4 (Transport - TCP):
┌──────────────────────────────────────────────────────────┐
│ Header TCP (20-60 byte)                                  │
│ ├─ Source Port: 54321 (porta del tuo PC)               │
│ ├─ Dest Port: 25 (porta SMTP di Gmail)                 │
│ ├─ Sequence Number: 1001                               │
│ ├─ ACK Number: 2001                                    │
│ └─ Flags: SYN, ACK, ...                                │
├──────────────────────────────────────────────────────────┤
│ DATI (corpo email)                                       │ ← 100 byte
│ "Ciao, come stai?"                                      │
└──────────────────────────────────────────────────────────┘
   SEGMENTO TOTALE ≈ 120-160 byte
```
**Cosa fa TCP:**
- Identifica quale applicazione sulla **tua macchina** sta spedendo (Source Port = 54321, assegnata dal tuo OS).
- Identifica quale **servizio** sul computer remoto deve ricevere il dato (Dest Port = 25, il servizio SMTP di Gmail).
- Aggiunge un numero di sequenza (importante per TCP: se più segmenti arrivano fuori ordine, TCP li riordina).
- Aggiunge il numero di ACK (riconoscimento dell'ultimo dato ricevuto dal server).

**Principio:** TCP non sa niente del contenuto dell'email, sa solo che deve consegnarlo al "servizio porta 25" del computer remoto.

---

##### **Fase 3: Network aggiunge il suo Header → PACCHETTO**
```
L3 (Network - IP):
┌────────────────────────────────────────────────────────────────┐
│ Header IP (20 byte, può diventare 60 con opzioni)             │
│ ├─ Version: IPv4 (4 bit)                                      │
│ ├─ Source IP: 192.168.1.100 (il tuo PC)                       │
│ ├─ Dest IP: 142.250.185.46 (server Gmail)                    │
│ ├─ TTL: 64 (Time To Live, quanti "salti" massimi)            │
│ ├─ Protocol: 6 (significa "è TCP")                           │
│ └─ Checksum: 0xAB12 (controllo di integrità)                │
├────────────────────────────────────────────────────────────────┤
│ SEGMENTO (da Fase 2)                                           │ ← 120-160 byte
│ ├─ Header TCP                                                  │
│ └─ DATI originali                                             │
└────────────────────────────────────────────────────────────────┘
   PACCHETTO TOTALE ≈ 140-180 byte
```
**Cosa fa IP:**
- Identifica il **computer sorgente** (Source IP: il tuo PC in rete locale è `192.168.1.100`).
- Identifica il **computer destinatario** (Dest IP: il server Gmail è `142.250.185.46`).
- Aggiunge il TTL (Time To Live) = numero massimo di router che il pacchetto può attraversare (evita loop infiniti di inoltri).
- Aggiunge il campo "Protocol" per dire al livello 4 del destinatario quale protocollo deve aspettarsi (6 = TCP, 17 = UDP).
- Calcola un checksum (hash) per controllare se l'header IP non è stato corrotto durante il viaggio.

**Principio:** IP non sa niente di TCP, porte, email, o dati utente. Sa solo "devo mandare questo blocco di byte dal PC 192.168.1.100 al PC 142.250.185.46".

---

##### **Fase 4: Data Link aggiunge il suo Header → FRAME**
```
L2 (Data Link - Ethernet):
┌──────────────────────────────────────────────────────────────────────────┐
│ Header Ethernet (14 byte)                                               │
│ ├─ Dest MAC: 00:1A:2B:3C:4D:5E (MAC dello switch/router prossimo)      │
│ ├─ Source MAC: AA:BB:CC:DD:EE:FF (MAC della tua scheda di rete)        │
│ └─ EtherType: 0x0800 (significa "è IPv4")                             │
├──────────────────────────────────────────────────────────────────────────┤
│ PACCHETTO (da Fase 3)                                                   │ ← 140-180 byte
│ ├─ Header IP                                                             │
│ └─ SEGMENTO TCP (incl. dati)                                           │
├──────────────────────────────────────────────────────────────────────────┤
│ Trailer Ethernet (4 byte CRC)                                           │
│ └─ FCS (Frame Check Sequence) = 0xABCD1234 (checksum per errori fisici)│
└──────────────────────────────────────────────────────────────────────────┘
   FRAME TOTALE ≈ 158-198 byte (minimo 64 byte, massimo 1500 byte standard)
```
**Cosa fa Ethernet (livello Data Link):**
- Identifica il **computer/dispositivo fisicamente vicino** (Dest MAC: l'indirizzo hardware dello switch o del router a cui sei collegato).
- Aggiunge il tuo indirizzo MAC (Source MAC: quello della tua scheda di rete).
- Aggiunge il campo EtherType per dire al ricevente quale protocollo del livello 3 è incapsulato (0x0800 = IPv4).
- Aggiunge un CRC (Cyclic Redundancy Check) al fondo per controllare se il frame non è stato corrotto durante la trasmissione fisica.

**Principio:** Ethernet non sa niente di IP, porte, TCP. Sa solo "devo spedire questo blob di byte al dispositivo con MAC `00:1A:2B:3C:4D:5E` (che potrebbe essere il router di casa)".

---

##### **Fase 5: Physical trasmette i BIT**
```
L1 (Physical):
Impulsi su cavo (Ethernet) o onde radio (WiFi):

  10110101 01001101 00110010 11010011 ... (fino ai ~198 byte)
  ───────────────────────────────────────────────────────
  impulsi di corrente su cavo Ethernet
  o onde radio su frequenza 2.4 GHz (WiFi)
```
**Cosa fa il livello Physical:**
- Prende il frame dal livello Data Link e lo trasmette come sequenza di impulsi fisici.
- Su Ethernet cablato: impulsi di voltaggio (alto = 1, basso = 0) sul cavo RJ45.
- Su WiFi: onde radio sulla frequenza 2.4 GHz o 5 GHz.
- Non "sa" niente di quello che sta trasmettendo, è solo un trasportatore di bit.

---

#### **Riepilogo Visivo dell'Incapsulamento Lato Mittente**

```text
                INCAPSULAMENTO (Scendendo lo Stack)
┌─────────────────────────────────────────────────────────────────┐
│  L7: [DATI: "Ciao"]                                             │
│         ↓ (tcp aggiunge intestazione)                          │
│  L4: [TCP Header | DATI: "Ciao"]     = SEGMENTO               │
│         ↓ (ip aggiunge intestazione)                           │
│  L3: [IP Header | TCP Header | DATI]  = PACCHETTO             │
│         ↓ (ethernet aggiunge intestazione + trailer)          │
│  L2: [MAC Header | IP | TCP | DATI | CRC] = FRAME            │
│         ↓ (trasmissione fisica)                               │
│  L1: 01101010 10110101 01001101 ... = BIT STREAM             │
└─────────────────────────────────────────────────────────────────┘
```

**REGOLA FONDAMENTALE:** ogni livello aggiunge il suo header (e il livello 2 aggiunge anche un trailer), incapsulando tutto quello che viene dai livelli superiori.

---

#### **Decapsulamento Dettagliato: Lato Destinatario**

Quando il frame arriva al server Gmail, accade il processo inverso:

```text
                DECAPSULAMENTO (Salendo lo Stack)
┌─────────────────────────────────────────────────────────────────┐
│  L1: 01101010 10110101 01001101 ... = BIT STREAM              │
│         ↑ (decodifica impulsi fisici)                         │
│  L2: [MAC Header | IP | TCP | DATI | CRC]                    │
│       └─ Verifica CRC, estrae il pacchetto IP                │
│         ↑ (toglie header MAC e trailer)                      │
│  L3: [IP Header | TCP Header | DATI]                          │
│       └─ Verifica checksum IP, cerca il protocol (6 = TCP)   │
│         ↑ (toglie header IP)                                 │
│  L4: [TCP Header | DATI]                                      │
│       └─ Legge Dest Port (25), riordina segmenti se fuori ord.│
│         ↑ (toglie header TCP)                                │
│  L7: [DATI: "Ciao"]  ← il server SMTP riceve il messaggio   │
└─────────────────────────────────────────────────────────────────┘
```

**Processi paralleli di controllo:**
- **L2 (Data Link):** se il CRC del frame non corrisponde, scarta il frame (errore su cavo/radio).
- **L3 (Network):** se il checksum IP non corrisponde, scarta il pacchetto.
- **L4 (Transport):** se TCP rileva perdita di segmenti, richiede la ritrasmissione.

---

#### **Metafora Finale: Le Scatole Cinesi**

```text
Mittente: Scrivo una lettera      →  La metto in una busta      →  La busta in uno scatolone
          →  Lo scatolone in un pacco  →  Il pacco su un furgone  →  Il furgone viaggia

Destinatario: Il furgone arriva    →  Apro il pacco               →  Estraggo lo scatolone
             →  Apro la busta       →  Leggo la lettera
```

Ogni "strato di confezionamento" (scatola/busta/furgone) è necessario e ha uno scopo:
- **La busta** (L4) identifica il destinatario preciso (porta).
- **Lo scatolone** (L3) sa dove consegnare geograficamente (indirizzo IP).
- **Il pacco** (L2) sa come consegnare fisicamente il giorno stesso (MAC).
- **Il furgone** (L1) è il mezzo che realizza fisicamente la consegna (cavo/radio).

Se tolgo una busta, il corriere non sa chi deve ricevere. Se tolgo lo scatolone, non sa l'indirizzo. Se tolgo il pacco, il furgone non sa dove mettere la roba.

---

#### **Concetto Cruciale: Gerarchia e Indipendenza**

Un punto chiave che spesso confonde i principianti:

**L'indirizzo IP (livello 3) è INDIPENDENTE dall'indirizzo MAC (livello 2).**

- Un PC con IP `192.168.1.100` potrebbe avere MAC `AA:BB:CC:DD:EE:FF`.
- Se spegni il PC e lo riaccendi, l'indirizzo MAC **rimane lo stesso** (è scritto nella scheda di rete).
- Ma l'indirizzo IP potrebbe **cambiare** (se ricevuto da DHCP, dynamic allocation).
- Se un router cambia l'indirizzo MAC del pacchetto da uno schema a un altro (passaggio tra reti diverse), **l'indirizzo IP rimane lo stesso** nel header IP (perché il percorso di rete è lo stesso).

**Conseguenza pratica:** puoi mandare un pacchetto dallo stesso IP a due destinazioni MAC diverse (es. due router diversi), e il pacchetto seguirà percorsi diversi, ma sarà sempre "riconoscibile" come proveniente dallo stesso mittente IP.

---

## 💻 MODULO LABORATORIO (2 Ore con ITP)

### ├── [2.1] Iscrizione alla Piattaforma Cisco NetAcad (CCNA1)
*Obiettivo: allestire lo strumento didattico che accompagnerà tutto l'anno.*

#### **Cos'è Cisco NetAcad?**

Cisco Networking Academy è una piattaforma didattica globale, **gratuita per le scuole convenzionate**, che eroga corsi strutturati su reti, sicurezza e hardware. È usata da migliaia di scuole e università in tutto il mondo.

#### **Il Corso di Quest'Anno: CCNA1 (*Introduction to Networks*)**

**CCNA1** è il primo modulo del percorso **Cisco Certified Network Associate (CCNA)**, uno dei certificati di rete più riconosciuti a livello internazionale.

**Cosa copre CCNA1:**
- Concetti fondamentali di rete (ISO/OSI, TCP/IP).
- Protocolli di livello Network (IPv4, IPv6, subnetting FLSM/VLSM).
- Protocolli di livello Transport (TCP, UDP).
- Nozioni di routing di base e configurazione minima di router.
- Introduzione alla sicurezza di rete.

**Correlazione con il nostro programma curricolare:** CCNA1 copre esattamente i temi che affronteremo nelle 8 settimane (più approfondito) — quindi completare CCNA1 entro maggio sarà un plus per il voto e una certificazione riconosciuta globalmente.

#### **Meccanica di NetAcad**

**Struttura del corso:**
- **~12 capitoli** (uno ogni settimana circa, ma puoi anche accelerare).
- Ogni capitolo contiene:
  - Lezioni teoriche interattive (testo + immagini + video).
  - **Esercitazioni simulate** in Cisco Packet Tracer (allegate alla piattaforma).
  - Quiz di autovalutazione (non-valutato) dopo ogni sezione teorica.
  - **Quiz capitolare** (valutato) alla fine di ogni capitolo, con scoring automatico.

**Tracciamento dei progressi:**
- Il docente ha una **dashboard** che mostra in tempo reale:
  - Chi ha completato/iniziato ogni capitolo.
  - I punteggi dei quiz.
  - Chi è rimasto indietro.
- I dati sono **tracciabili e certificati** — puoi usarli per motivare gli studenti.

**Certificazione finale:**
- Dopo aver completato tutti i capitoli e superato il test finale di CCNA1, ricevi un **certificato digitale** riconosciuto da Cisco.
- Accesso a uno sconto su esame ufficiale CCNA 200-301 di Pearson Vue (se decidi di sostenere l'esame completo).

#### **Procedura di Iscrizione (per il docente)**

1. Vai su https://www.netacad.com/
2. Crea un account personale (oppure usa l'account d'istituto se esiste).
3. Verifica/crea una "Classe Virtuale" per il corso CCNA1.
4. **Genera il codice di iscrizione** della classe (un codice univoco tipo `XXXXXX-XXXXXX-XX`).
5. Condividi il codice agli studenti via Google Classroom o email.

#### **Procedura di Iscrizione (per lo studente)**

1. Vai su https://www.netacad.com/
2. Crea un account personale (nome, cognome, email, password).
3. Vai su "Accedi ai Corsi" e digita il **codice della classe** fornito dal docente.
4. Seleziona il corso **CCNA1 - Introduction to Networks**.
5. Accetta i termini di servizio e premi "Enroll".
6. Il corso **si sblocca immediatamente** e puoi iniziare a studiare.

---

### ├── [2.2] Ripasso Rapido di Cisco Packet Tracer
*Obiettivo: recuperare la familiarità con lo strumento di simulazione già usato in 3° anno.*

#### **Cos'è Cisco Packet Tracer?**

È un **simulatore di rete** gratuito (scaricabile con iscrizione a NetAcad) che permette di costruire topologie di rete virtuali e osservare come i pacchetti viaggiano attraverso i dispositivi.

**Non è come un vero router/switch fisico, è una simulazione**, ma è estremamente fedele al comportamento reale e sufficientemente realistica per imparare i concetti.

#### **L'Interfaccia Principale**

```
┌────────────────────────────────────────────────────────────┐
│ Menu (File, Edit, View, Help...)                          │
├────────────────────────────────────────────────────────────┤
│ Toolbar: [PC] [Router] [Switch] [Connection]...            │
├────────────────────────────────────────────────────────────┤
│                                                            │
│                  AREA DI LAVORO                           │
│              (canvas bianco dove disegni)                 │
│                                                            │
│                                                            │
├────────────────────────────────────────────────────────────┤
│ [Realtime] [Simulation] | Pantalla della topologia       │
└────────────────────────────────────────────────────────────┘
```

**Componenti principali:**

1. **Toolbar a sinistra:** categorie di dispositivi simulabili.
   - **Networking Devices:** Router, Switch, Hub, Modem, Access Point.
   - **End Devices:** PC, Laptop, Server, Printer.
   - **Connections:** cavi Ethernet (dritto, incrociato), cavi seriali, connessioni wireless.

2. **Area di lavoro (canvas):** zona bianca dove posizioni i dispositivi e li colleghi.

3. **Pulsanti di Modalità (in basso a sinistra):**
   - **Realtime:** i pacchetti vengono inoltrati in tempo reale, velocissimo. Utile per testare la topologia ma non per osservare il traffico.
   - **Simulation:** i pacchetti vengono visualizzati **passo-passo**, congelando la simulazione tra un salto e l'altro. **Perfetto per capire l'incapsulamento**.

4. **Scheda Topology:** visualizza la topologia intera.

5. **Scheda Physical (se attiva):** mostra la disposizione fisica dei dispositivi (opzionale).

#### **Come Costruire una Topologia Minima**

**Passo 1: Posizionamento dei dispositivi**
- Clicca sulla categoria "End Devices" e trascina 2 **PC** nell'area di lavoro.
- Clicca sulla categoria "Networking Devices" e trascina 1 **Switch** e 1 **Router**.

**Passo 2: Collegamento dei dispositivi**
- Clicca sulla categoria "Connections" e seleziona il cavo **Copper Straight-Through** (cavo dritto, color rame).
- Clicca e trascina dal **PC1** alla **porta Ethernet della scheda switch** (solitamente porta Fa0/1, Fast Ethernet).
- Ripeti per **PC2** → **Switch porta Fa0/2**.
- Collega il **Switch** al **Router** (per es., Switch porta Fa0/24 al Router porta Fa0/0).

**Passo 3: Configurazione Minima degli Indirizzi IP**
- Fai doppio-click su **PC1** per aprire la finestra di configurazione.
- Vai su scheda "IP Configuration".
- **Static** (non DHCP per ora):
  - IP Address: `192.168.1.10`
  - Subnet Mask: `255.255.255.0`
- Premi OK.
- Ripeti per **PC2:**
  - IP Address: `192.168.1.20`
  - Subnet Mask: `255.255.255.0`

**Passo 4: Configurazione del Router** (solo configurazione basilare)
- Fai doppio-click su **Router** → scheda "Config".
- Clicca su interfaccia **Fa0/0** (porta che collega allo switch).
- IP Address: `192.168.1.1`
- Subnet Mask: `255.255.255.0`
- Porta: On (accesa).
- (Router tra reti diverse richiede configurazioni più complesse, per ora limitiamoci a questo).

#### **Modalità Realtime vs Simulation**

**Realtime (veloce):**
- Premi il pulsante **Realtime** in basso a sinistra.
- Fai un **ping** da PC1 a PC2: clicca su PC1, vai su "Desktop" → "Command Prompt", digita `ping 192.168.1.20`.
- La risposta arriva quasi istantaneamente.
- **Non vedi i pacchetti** che volano — sono troppo veloci.

**Simulation (osservabile passo-passo):**
- Premi il pulsante **Simulation** in basso a sinistra.
- Compariranno nuovi elementi: "Event List", "PDU List", pannello a destra con dettagli.
- Fai un **ping** da PC1 a PC2 (stesse istruzioni di prima).
- Vedrai nell'**Event List** una sequenza di eventi:
  - "PC1: ICMP Echo Request created" (il PC1 crea la richiesta ping).
  - Vedrai rettangolini colorati che scendono sui cavi (è il pacchetto che viaggia).
  - Potrai cliccare su ogni evento e vedere il dettaglio completo della PDU (header di ogni livello).
- Premendo il pulsante **Capture/Forward** avanzi di un passo alla volta.

---

### ├── [2.3] Prima Topologia: PC – Switch – Router
*Obiettivo: costruire l'infrastruttura minima su cui osservare l'incapsulamento in pratica.*

#### **Architettura della Topologia**

```
                    Internet (non collegato)
                            |
                         ROUTER (L3)
                        Fa0/0: 192.168.1.1
                            |
                            | Ethernet cavo dritto
                            |
                          SWITCH (L2)
                      Fa0/1 | Fa0/2 | Fa0/24
                          |   |       |
       Fa0     Fa0        |   |       |
      PC1 ─────┐         |   |       └── [al Router]
   192.168.1.10│         |   |
               └─────────┘   │
                  Fa0/1      │
                        Fa0/2│
                             PC2
                      192.168.1.20
```

#### **Componenti della Topologia**

1. **PC1:**
   - IP: `192.168.1.10`
   - Subnet Mask: `255.255.255.0`
   - Gateway (verrà impostato): `192.168.1.1` (il router)

2. **PC2:**
   - IP: `192.168.1.20`
   - Subnet Mask: `255.255.255.0`
   - Gateway (verremo impostato): `192.168.1.1` (il router)

3. **Switch (L2):**
   - Dispositivo "stupido" che incamella i frame in base al MAC address.
   - Non ha indirizzo IP (per ora).
   - Ha porte: Fa0/1, Fa0/2, ... Fa0/24 (FastEthernet a 100 Mbps, standard su switch 2960 Cisco).
   - Funge da **ponte tra i PC**.

4. **Router (L3):**
   - IP sulla porta Fa0/0 (che guarda verso lo switch): `192.168.1.1`.
   - Funge da **gateway** (porta d'accesso a reti esterne).
   - In questa topologia semplice, il router non fa granché, ma è presente per illustrare il concetto.

#### **Cosa Ci Insegna Questa Topologia**

- **Switch (L2):** crea una rete locale (LAN) e inoltra frame in base a MAC address.
- **Router (L3):** fornisce una porta di "uscita" dalla rete locale e inoltrerebbe pacchetti verso altre reti.
- **Incapsulamento:** quando PC1 ping PC2, puoi osservare come il messaggio ICMP sia incapsulato in TCP/UDP (no, in realtà ICMP è direttamente nel livello 3, scusami), poi in IP, poi in Ethernet frame.

---

### ├── [2.4] Esercitazione Pratica Guidata al PC (Durata: 70-80 minuti)

#### **FASE A: Iscrizione e Primo Accesso a NetAcad (20 min)**

**Azione 1: Accesso al portale**
1. Ogni studente apre il browser e va su https://www.netacad.com/
2. Clicca su "Sign In" (in alto a destra) → "Create new account".
3. Compila il form:
   - Name: [nome e cognome]
   - Email: [email di istituto o personale]
   - Password: [password sicura, minimo 8 caratteri, maiuscole/minuscole/numeri]
   - Accetta i termini di servizio.
4. Premi "Create Account".
5. Riceverà un'email di verifica: clicca sul link di conferma.

**Azione 2: Iscrizione al corso tramite codice di classe**
1. Accedi a NetAcad con le tue credenziali.
2. Clicca su "Access Courses" o "Enroll in a Course".
3. Digita il **codice della classe** fornito dal docente (tipo `XXXXXX-XXXXXX-XX`).
4. Seleziona "CCNA1 - Introduction to Networks".
5. Premi "Enroll" o "Join Class".
6. Attendi il caricamento (può impiegare 30 secondi).

**Azione 3: Esplorazione dell'interfaccia**
1. Vai alla scheda "My Courses" e clicca su "CCNA1".
2. Visualizzerai:
   - Indice dei capitoli (Chapters 1-12).
   - Barra di avanzamento generale (es. "Chapter 1 - 0% Complete").
   - Un primo **Capitolo 1** già disponibile.
3. Clicca su "Chapter 1: Explore the Network".
4. All'interno, vedrai:
   - Lezioni numeriche (1.1, 1.2, 1.3, ...).
   - Quiz di prova dopo ogni lezione (marchiati come "Knowledge Check").
   - Un capitolare finale.

**Azione 4: Primo Quiz di Prova (non-valutato)**
1. Completa almeno la lezione **1.1** leggendo velocemente.
2. Dopo la lezione 1.1, compare il "Knowledge Check" (quiz di prova).
3. Compila il quiz (4-5 domande su concetti base).
4. Premi "Submit" — riceverai il punteggio istantaneo (es. 4/5 = 80%).
5. **Non è valutato**, è solo per capire il formato delle domande e vederne le soluzioni.

**Azione 5: Registrazione dei dati**
- Su Google Classroom, condividi uno **screenshot** della tua pagina NetAcad con il titolo "Chapter 1: Explore the Network" visibile.
- Così il docente verifica che tutti si sono iscritti correttamente.

---

#### **FASE B: Costruzione della Topologia in Packet Tracer (25 min)**

**Azione 1: Apertura e Creazione di Nuovo Progetto**
1. Apri Cisco Packet Tracer (già installato dal corso dell'anno scorso, o scaricabile da NetAcad).
2. Clicca "File" → "New".
3. Vedrai una tela bianca — questa è l'area di lavoro.

**Azione 2: Posizionamento dei Dispositivi PC**
1. Sulla **sinistra**, clicca su "End Devices" (icona con computer).
2. Seleziona **"PC"** e trascina 2 istanze nell'area di lavoro.
3. Rinomina (doppio-click sul nome):
   - Primo PC → **PC1**
   - Secondo PC → **PC2**

**Azione 3: Posizionamento dello Switch e del Router**
1. Sulla **sinistra**, clicca su "Networking Devices" (icona con switch).
2. Seleziona **"Switch"** (ricerca "2960" se richiesto, il modello standard) e trascinalo nell'area.
3. Seleziona **"Router"** (ricerca "2901" o "1941") e trascinalo più in alto nell'area.
4. Rinomina:
   - Switch → **Switch**
   - Router → **Router**

**Azione 4: Collegamento dei Dispositivi con Cavi**
1. Sulla **sinistra**, clicca su "Connections" (icona con spinotti).
2. Seleziona il cavo **"Copper Straight-Through"** (rame, dritto).
3. Clicca e trascina da **PC1** verso il **porto Fa0/1 dello Switch**.
   - Una finestra popup ti chiede quale porta del PC usare: accetta il default (Fa0 = Fast Ethernet 0).
   - Una seconda popup ti chiede quale porta dello switch: digita **Fa0/1** o accetta il default.
4. Ripeti per **PC2 → Switch porta Fa0/2**.
5. Ripeti per **Switch porta Fa0/24 → Router porta Fa0/0**.

**Azione 5: Verifica della Topologia**
- Se tutto è collegato correttamente, vedrai linee verdi tra i dispositivi (connessione attiva).
- Se una linea è rossa, c'è un errore di collegamento — controlla le porte.

---

#### **FASE C: Configurazione IP Minima dei PC (15 min)**

**Azione 1: Configurazione PC1**
1. Doppio-click su **PC1** → si apre una finestra di configurazione.
2. Seleziona la scheda **"IP Configuration"** (in alto).
3. Seleziona **"Static"** (non DHCP per ora).
4. Compila i campi:
   - IPv4 Address: **192.168.1.10**
   - Subnet Mask: **255.255.255.0**
   - Default Gateway: **192.168.1.1** (l'indirizzo che daremo al router)
   - DNS Server: (lasciato vuoto per ora)
5. Premi il pulsante **"X"** in alto a destra per chiudere.

**Azione 2: Configurazione PC2**
1. Doppio-click su **PC2** → scheda "IP Configuration".
2. Seleziona **"Static"**.
3. Compila:
   - IPv4 Address: **192.168.1.20**
   - Subnet Mask: **255.255.255.0**
   - Default Gateway: **192.168.1.1**
4. Chiudi.

**Azione 3: Configurazione del Router** (versione semplificata)
1. Doppio-click su **Router** → scheda **"Config"** (non "CLI" per ora, che è a riga di comando).
2. Nel pannello di sinistra, clicca su **"FastEthernet 0/0"** (la porta Fa0/0).
3. Nel pannello di destra, compila:
   - Port Status: **On** (assicurati che sia spuntato).
   - IPv4 Address: **192.168.1.1**
   - Subnet Mask: **255.255.255.0**
4. Premi il pulsante **"Apply"** in basso a sinistra.
5. Chiudi.

**Verifica:** Se tutto è corretto, vedrai i tre dispositivi con linee **verde** di collegamento.

---

#### **FASE D: Osservazione dell'Incapsulamento (20 min)**

**Azione 1: Passaggio in Modalità Simulation**
1. In basso a sinistra, premi il pulsante **"Simulation"** (accanto a "Realtime").
2. Comparirà un pannello aggiuntivo a destra: "Event List", "PDU List", "Outgoing PDU Details", etc.
3. Vedrai anche sulla toolbar in basso: bottoni "Capture/Forward" (freccia destra), "Reset" (X), etc.

**Azione 2: Invio di un Ping da PC1 a PC2**
1. Clicca su **PC1** per selezionarlo.
2. Vai sulla scheda che appare ("Desktop", "Physical", "Config").
3. Clicca su **"Command Prompt"** (o "Terminal").
4. Si apre una finestra dove digitare.
5. Digita: `ping 192.168.1.20`
6. Premi **Enter**.

**Azione 3: Osservazione Passo-Passo del Traffico**
1. Nell'**Event List** (a destra), vedrai una sequenza di eventi:
   - "PC1: ICMP Echo Request created"
   - "PC1 to Switch: ICMP Echo Request in Ethernet Frame"
   - "Switch to PC2: ICMP Echo Request in Ethernet Frame"
   - "PC2: ICMP Echo Request received"
   - "PC2 to Switch: ICMP Echo Reply in Ethernet Frame"
   - ... e così via.
2. Sul canvas, vedrai rettangoli colorati che si muovono sui cavi (rappresentano i pacchetti).

**Azione 4: Analisi Dettagliata della PDU (Protocol Data Unit)**
1. Nella lista degli eventi, clicca su uno degli eventi che dice "Ethernet Frame" (es. "PC1 to Switch: ICMP Echo Request in Ethernet Frame").
2. Nel pannello **"PDU Details"** (in basso a destra), vedrai la **struttura completa del pacchetto**:
   ```
   Outgoing PDU Details:
   ┌─────────────────────────────────────┐
   │ Ethernet II Frame                   │
   │ ├─ Source MAC: 00:00:00:00:00:00   │
   │ ├─ Dest MAC: 00:00:00:00:00:01     │
   │ └─ Type: IPv4 (0x0800)             │
   │                                     │
   │ IPv4 Packet                         │
   │ ├─ Source IP: 192.168.1.10          │
   │ ├─ Dest IP: 192.168.1.20            │
   │ ├─ Protocol: ICMP (1)               │
   │ └─ TTL: 128                         │
   │                                     │
   │ ICMP Echo Request                   │
   │ ├─ Type: 8 (Echo)                   │
   │ ├─ Sequence: 0                      │
   │ └─ Data: "..."                      │
   └─────────────────────────────────────┘
   ```
3. Questo è l'**incapsulamento visuale**: vedi come ICMP è dentro IPv4, che è dentro l'Ethernet frame.

**Azione 5: Seguire il Pacchetto Attraverso la Rete**
1. Premi il tasto **"Capture/Forward"** (freccia destra) per avanzare di un evento.
2. Vedrai come il pacchetto passa da PC1 allo Switch.
3. Premi ancora **"Capture/Forward"**: il pacchetto passa dallo Switch a PC2.
4. Continua: vedrai la risposta (Echo Reply) che ritorna da PC2 a PC1.

---

#### **FASE E: Consegna e Riflessione (10 min)**

**Azione 1: Screenshot della Simulazione**
1. Quando il pacchetto è visibile nel PDU Details (con tutti gli header esplosi), premi **Stamp** o **Print Screen** e salva l'immagine.
2. Carica lo screenshot su **Google Classroom** con il nome "4DIs1_Simulation_Screenshot.png".
3. Scrivi una breve didascalia: *"Pacchetto ICMP Echo Request incapsulato in IPv4 e Ethernet Frame"*.

**Azione 2: Domanda di Riflessione**
1. Su Google Classroom, rispondi brevemente a questa domanda (3-5 righe):
   > *"Perché il pacchetto ha bisogno di **tre** involucri (Ethernet, IPv4, ICMP) invece di uno solo con tutte le informazioni?*
   >
   > *Che cosa farebbe lo Switch che non potrebbe fare se non ci fosse il frame Ethernet? E il Router?"*

**Esempio di risposta attesa:**
> *"Lo Switch (L2) deve sapere solo il MAC del destinatario per inoltrar il frame alla porta giusta — se leggesse l'IP (che è dentro il frame) sarebbe inutile per il suo compito. Il Router, viceversa, ha bisogno dell'IP per decidere se il pacchetto va a lui o a una rete diversa. Se ci fosse un solo involucro, ogni dispositivo dovrebbe decodificare tutto, perdendo modularità e velocità."*

---

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma Lezione Teorica (110 min, 2 ore)

* **00-10 min | Accoglienza e Presentazione del Corso (10 min)**
  * Saluto agli studenti, presentazione breve della tua esperienza in reti.
  * Panoramica rapida del programma annuale: "Quest'anno parleremo di come Internet funziona davvero — dai cavi ai servizi come email e web."
  * Menzione della certificazione CCNA1: "Se completate il corso e il lavoro, avrete una certificazione riconosciuta da Cisco a livello mondiale — utile per il vostro futuro."
  * Mostra un video di 60 secondi di un router/switch che funziona (esempio: YouTube "Cisco Router switching packets" o simile).

* **10-25 min | L'Hook d'Apertura: La Lettera Imbustata (15 min)**
  * Disegna alla lavagna una **lettera** scritta a mano, poi mostri come la metti **in una busta**, poi in uno **scatolone**, poi in un **pacco**, infine in un **furgone**.
  * Fai una domanda provocatoria agli studenti: *"Secondo voi, perché la posta non mette la lettera direttamente nel furgone? Perché tutte queste scatole?"*
  * Ascolta le ipotesi (protezione, identificazione del destinatario, etc.).
  * **Collegamento:** "Esattamente! Una rete di computer fa la stessa cosa con i dati: li avvolge in vari "involucri" (header) perché ogni dispositivo sulla strada ha un compito diverso."
  * Disegna una freccia dalla "lettera" ai "dati", dalla "busta" al "Header TCP", etc.

* **25-55 min | Il Modello ISO/OSI: La Torre a 7 Livelli (30 min)**
  * Disegna alla lavagna la **torre di 7 livelli** (potete disegnare un rettangolo diviso in 7 sezioni).
  * **Metodo:** leggi lentamente ogni livello dalla tua guida e disegna accanto una metafora quotidiana.
    * L7 Application → "Il bancario che accoglie il cliente"
    * L6 Presentation → "Il traduttore che converte i documenti"
    * L5 Session → "Lo sportellista che apre/chiude la pratica"
    * L4 Transport → "Il corriere che controlla i pacchi"
    * L3 Network → "Le mappe stradale (routing)"
    * L2 Data Link → "L'indirizzo della strada (MAC)"
    * L1 Physical → "Il foglio di carta e l'inchiostro"
  * **Coinvolgimento:** chiedi agli studenti di trovare **loro stessi** esempi quotidiani per ogni livello (non informatici).
    * Esempio: "L3 Network è come... le coordinate GPS?" → "Sì! Proprio così!"
    * Esempio: "L1 Physical è come... il cavo del telefono?" → "Esattamente!"
  * **Mnemonica:** insegna "All People Seem To Need Data Processing" e fai memorizzare cantando o ripetendo 2-3 volte.

* **55-75 min | Il Modello TCP/IP: La Versione Pratica (20 min)**
  * Disegna il **confronto fianco a fianco** tra ISO/OSI (7 livelli) e TCP/IP (4 livelli).
  * Sottolinea come **TCP/IP ha vinto** perché Internet fu costruita su TCP/IP, non su ISO/OSI.
  * Mostra le **corrispondenze:** Application (TCP/IP) = Application + Presentation + Session (ISO/OSI), etc.
  * Fai una domanda: *"Se TCP/IP è più semplice, perché studiamo ISO/OSI?"* 
    * Risposta: "Perché ISO/OSI insegna i concetti astratti e separati. TCP/IP è 'la realtà', ma ISO/OSI è 'la teoria che spiega come funziona'."
  * Nota importante: "D'ora in poi, quando dico 'livello 3', intendo sia ISO/OSI-L3 che TCP/IP-Internet. Sono la stessa cosa."

* **75-100 min | PDU e Incapsulamento: il Cuore del Concetto (25 min)**
  * Questo è il **pezzo chiave** — richiede attenzione massima.
  * Disegna alla lavagna il **diagramma dell'incapsulamento in 5 fasi:**
    ```
    L7:  [DATI: "Ciao"]
         ↓
    L4:  [TCP | DATI]         = SEGMENTO
         ↓
    L3:  [IP | TCP | DATI]    = PACCHETTO
         ↓
    L2:  [MAC | IP | TCP | DATI | CRC] = FRAME
         ↓
    L1:  01101010101...       = BIT STREAM
    ```
  * **Spiega lentamente ogni fase:**
    * Fase 1: Livello applicativo crea dati grezzi (100 byte).
    * Fase 2: TCP aggiunge un header di ~20 byte (source port, dest port, sequence). Ora il segmento è ~120 byte.
    * Fase 3: IP aggiunge un header di ~20 byte (source IP, dest IP, TTL). Ora il pacchetto è ~140 byte.
    * Fase 4: Ethernet aggiunge un header (~14 byte) + trailer CRC (~4 byte). Ora il frame è ~158 byte.
    * Fase 5: Livello Physical trasmette i 158 byte come sequenza di bit su cavo/WiFi.
  * **Connessione visiva:** fai vedere come questa è **esattamente** la metafora della lettera imbustata di prima!
  * **Domanda di controllo:** *"Se i dati originali erano 100 byte, perché il frame è 158 byte?"* → "Perché ogni livello aggiunge il suo 'involucro' (header/trailer)."
  * **Decapsulamento:** mostra il processo inverso al destinatario (il server Gmail riceve il frame e toglie layer per layer).

* **100-110 min | Chiusura e Verifiche Rapide (10 min)**
  * Chiedi **3 domande rapide a bruciapelo** per verificare la comprensione:
    1. *"Quanti livelli ha il modello ISO/OSI?"* → "7"
    2. *"Come si chiama la PDU al livello 3 (Network)?"* → "Pacchetto"
    3. *"Quale livello aggiunge l'indirizzo MAC?"* → "Livello 2, Data Link"
    4. *"Quale porta usa il protocollo SMTP per inviare email?"* → "Porta 25"
  * Non è un quiz punitivo, è per capire chi ha seguito.
  * Loda chi risponde bene: "Esattamente! Vedete che è logico?"
  * Se qualcuno non sa rispondere: "Non ti preoccupare, lo riprenderemo; è tutto nuovo."
  * Accenna al prossimo argomento (Settimana 2): "La prossima volta parleremo di come questi indirizzi IP vengono assegnati (subnetting) e come i router li usano per prendere decisioni."

### ✍️ Disegni Guida da Fare alla Lavagna (Lezione 1)

**Disegno 1: La Lettera Imbustata**
```
    ┌────────────────┐
    │   Furgone      │     L1 Physical: il mezzo fisico
    │ ┌────────────┐ │
    │ │ Pacco      │ │     L2 Data Link: indirizzo MAC
    │ │ ┌────────┐ │ │
    │ │ │Scatola │ │ │     L3 Network: indirizzo IP
    │ │ │┌──────┐│ │ │
    │ │ ││Busta ││ │ │     L4 Transport: porta
    │ │ ││┌────┐││ │ │
    │ │ │││Ltr ││ │ │     L7 Application: dati
    │ │ ││└────┘││ │ │
    │ │ │└──────┘│ │ │
    │ │ └────────┘ │ │
    │ └────────────┘ │
    └────────────────┘
```

**Disegno 2: La Torre ISO/OSI**
```
    7 │ APPLICATION      │  Browser, Email Client
      ├──────────────────┤
    6 │ PRESENTATION     │  Compressione, Crittografia
      ├──────────────────┤
    5 │ SESSION          │  Apertura/Chiusura Sessioni
      ├──────────────────┤
    4 │ TRANSPORT        │  TCP, UDP, Porte
      ├──────────────────┤
    3 │ NETWORK          │  IP, Routing
      ├──────────────────┤
    2 │ DATA LINK        │  MAC, Switch, Frame
      ├──────────────────┤
    1 │ PHYSICAL         │  Cavi, WiFi, Bit
```

**Disegno 3: L'Incapsulamento in 5 Fasi**
```
    LATO MITTENTE (Incapsulamento)
    ──────────────────────────────
    
    L7: [DATI: 100 byte]
           ↓ aggiunge header TCP
    L4: [TCP-Header (20) | DATI (100)]  = 120 byte
           ↓ aggiunge header IP
    L3: [IP-H (20) | TCP-H | DATI]      = 140 byte
           ↓ aggiunge header MAC + CRC
    L2: [MAC-H (14) | IP | TCP | DATI | CRC (4)]  = 158 byte
           ↓ trasmette come bit
    L1: 01101010101010... (158 byte = 1264 bit)
    
    
    LATO DESTINATARIO (Decapsulamento)
    ───────────────────────────────────
    
    L1: 01101010101010... (riceve bit)
           ↓ decodifica
    L2: [MAC-H | IP | TCP | DATI | CRC]
           ↓ toglie MAC-H e CRC
    L3: [IP-H | TCP-H | DATI]
           ↓ toglie IP-H
    L4: [TCP-H | DATI]
           ↓ toglie TCP-H
    L7: [DATI] ← applicazione riceve il messaggio!
```

### 🎯 Micro-Task Formativa per Casa (Spaced Retrieval — 5-10 minuti di lavoro)

Carica su Google Classroom questo compito **senza voto punitivo**, solo spunta di completamento:

> **Attività 1: Disegno della Torre ISO/OSI**
>
> Disegna su un foglio (carta, tablet, computer — va bene qualsiasi) la torre ISO/OSI a 7 livelli. Accanto a ciascun livello, scrivi:
> - Il nome del livello
> - Un esempio quotidiano **non informatico** che ricorda quella funzione (es. Physical = il tubo dell'acqua; Application = il bancario che accoglie il cliente).
> 
> **Scadenza:** entro la lezione prossima.
> **Consegna:** foto/screenshot del tuo disegno su Google Classroom.

> **Attività 2: Primo Quiz di CCNA1 su NetAcad**
>
> Completate almeno le lezioni 1.1 e 1.2 del Capitolo 1 di CCNA1 su NetAcad e risolvete il **Knowledge Check** (il quiz dopo le lezioni).
> 
> **Scadenza:** entro 3-4 giorni.
> **Consegna:** screenshot della pagina NetAcad che mostra "Chapter 1 - 50% Complete" (almeno).

### 📝 Note di Insegnamento Avanzate

**Punti che gli studenti confondono spesso:**

1. **Confusione tra IP e MAC:**
   * **Chiarimento:** "L'IP è come il numero civico della tua casa (dove devi andare geograficamente). Il MAC è come il cognome della persona che vive lì (come la identifico fisicamente quando arriva il furgone alla via). Due diversi destinazioni MAC possono ricevere lo stesso IP se risiedono su reti diverse."
   * **Analogia estesa:** "Se spedisco una lettera al '10 Via Roma' ma cambio il cognom

e del destinatario (MAC), la posta non sa chi deve ricevere. Se spedisco al '10 Via Roma' (IP) ma cambio il furgone (MAC del router), il percorso rimane lo stesso, ma la modalità di trasporto cambia."

2. **Confusione tra TCP/IP (il protocollo IP) e TCP/IP (il modello a 4 livelli):**
   * **Chiarimento:** "Quando dico 'modello TCP/IP' intendo il modello a 4 livelli. Quando dico 'protocollo TCP/IP', potrebbe significare sia il protocollo TCP che il protocollo IP singolarmente. Spesso significato è chiaro dal contesto."

3. **Perché ogni livello aggiunge un header?**
   * **Risposta:** "Perché ogni livello ha un compito diverso e ha bisogno di informazioni diverse per farlo. Switch non sa cosa è un IP, quindi non potrebbe usarlo — ha bisogno del MAC. Router non sa cosa è una porta, ha bisogno dell'IP. Se mettessimo tutto in un unico header, ogni dispositivo dovrebbe capire tutto, perdendo modularità."

4. **Dimensione crescente dei pacchetti:**
   * **Chiarimento:** "Sì, aggiungendo header il pacchetto diventa più grande. Ma è il prezzo pagato per avere modularità e che ogni livello faccia il suo compito."

### 🛠️ Troubleshooting Domande Comuni

**D: "Ma se il MAC è l'indirizzo fisico della scheda, perché non è fisso come un nome?"**
- R: "Il MAC è fisso sulla scheda (riporta il numero seriale della scheda stessa), ma puoi anche **cambiarlo (MAC spoofing)** con software. L'IP, invece, è assegnato dal server DHCP della rete e può cambiare ogni volta che ti riconnetti."

**D: "Come fa il router a sapere dove mandare il pacchetto se non conosce il MAC?"**
- R: "Il router guarda l'IP nel pacchetto, lo confronta con la sua **tabella di routing** (una lista di 'se il destinatario è nella rete X, mandalo al gateway Y'), e decide. Il MAC serve solo al livello 2 per sapere il dispositivo fisico prossimo, non è responsabilità del router."

**D: "Perché su WiFi usiamo indirizzi MAC se siamo wireless?"**
- R: "WiFi è ancora a livello 2 (Data Link), quindi ha bisogno dei MAC. WiFi trasporta comunque IP dentro i frame WiFi, proprio come Ethernet. È solo un mezzo diverso (onde radio invece di fili), ma il concetto di livelli rimane."

**D: "Se il pacchetto è grande 158 byte, come fa a passare da PC a Router se il cavo Ethernet ha un'MTU di 1500 byte?"**
- R: "L'MTU (Maximum Transmission Unit) è la dimensione **massima** di un frame; se il nostro frame è 158 byte, è ben dentro il limite. Non c'è problema. Se il file fosse più grande (es. scaricamento di video), il TCP dividerebbe i dati in più segmenti, ognuno incapsulato in un suo frame."

---

## 🧭 DALLA DEFINIZIONE ALL'USO: COME LEGGERE UN PACCHETTO

Questa sezione serve a non fermarsi alla memoria dei nomi. Davanti a un traffico di rete, la domanda utile e': **quale dispositivo deve leggere quale informazione?**

### Un ping tra due PC della stessa LAN

Supponiamo che PC-A (`192.168.1.10`) esegua `ping 192.168.1.20`.

1. Il comando genera un messaggio **ICMP Echo Request**. ICMP non usa TCP o UDP: e' un protocollo di controllo del livello Internet/Network.
2. PC-A confronta la destinazione con la propria maschera. Capisce che PC-B e' nella stessa rete.
3. Per costruire il frame, PC-A deve conoscere il MAC di PC-B. Se non lo conosce, usa ARP: lo vedremo piu' avanti nel bimestre.
4. Il frame Ethernet contiene MAC sorgente e MAC destinazione; dentro il frame c'e' un pacchetto IPv4; dentro il pacchetto c'e' il messaggio ICMP.
5. Lo switch legge il MAC di destinazione e inoltra il frame sulla porta corretta. Non decide il percorso IP.

```text
ICMP Echo Request
  dentro IPv4
    dentro Ethernet
      dentro segnali fisici
```

Se invece la destinazione fosse `8.8.8.8`, PC-A capirebbe che e' fuori dalla propria rete e consegnerebbe il frame al MAC del **gateway**, non al MAC del server remoto. L'IP di destinazione resterebbe quello del server; cambierebbe il destinatario locale del frame.

### La stessa comunicazione osservata su due collegamenti

```text
PC-A -------- Switch -------- Router -------- Internet
    frame 1              frame 2
       MAC A -> MAC router   MAC router -> MAC next-hop
       IP A -> IP server     IP A -> IP server
```

Questa e' una delle idee piu' importanti dell'anno: l'IP descrive la comunicazione end-to-end, mentre il MAC descrive il **prossimo tratto**. A ogni router il frame viene rimosso e ricostruito; il pacchetto IP prosegue, normalmente con TTL diminuito.

### Attivita' di ragionamento

Per ogni scenario indicare il livello principalmente coinvolto e l'informazione da osservare:

| Scenario | Livello iniziale | Informazione utile |
|---|---|---|
| Il cavo e' scollegato | Physical | link, LED, segnale |
| Lo switch inoltra verso la porta sbagliata | Data Link | tabella MAC e frame |
| Il PC sceglie il gateway sbagliato | Network | IP, maschera, routing |
| Il browser contatta il servizio sbagliato | Transport/Application | porta e protocollo |
| Il testo arriva illeggibile | Presentation/Application | codifica o formato |

La risposta non deve essere solo “livello 2” o “livello 3”: va completata con **che cosa osserveresti** e **quale prova faresti per primo**.

### Mini-verifica conclusiva della settimana

1. Disegna il percorso di un `ping` tra due PC della stessa LAN e indica PDU e indirizzi a ogni passaggio.
2. Spiega perche' un router non puo' inoltrare un pacchetto basandosi soltanto sul MAC originale del mittente.
3. Un ping fallisce, ma il link Ethernet e' verde. Quali due livelli controlleresti prima e perche'?
4. **Intuizione:** se sostituisci Ethernet con Wi-Fi, quali informazioni restano concettualmente necessarie e quale parte cambia?
5. **Intuizione:** perche' e' utile che un'applicazione non sappia se i dati viaggiano su rame, fibra o onde radio?

### Riferimenti per continuare

- [RFC 1122 - Requirements for Internet Hosts](https://www.rfc-editor.org/rfc/rfc1122)
- [Cisco Networking Academy - Introduction to Networks](https://www.netacad.com/courses/networking)
- [Wikipedia italiana - Modello OSI](https://it.wikipedia.org/wiki/Modello_OSI)
