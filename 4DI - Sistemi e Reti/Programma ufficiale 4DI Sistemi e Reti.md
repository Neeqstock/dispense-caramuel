Ecco la programmazione annuale ricavata dal documento per la classe **4ª DI** (disciplina **Sistemi e Reti**, A.S. 2025/2026), organizzata in sezioni logiche e strutturata con **checkbox operative** per monitorare l'avanzamento didattico.

---

# 📋 Programmazione Annuale: Sistemi e Reti (Classe 4ª DI)
**Istituto:** I.I.S. "Caramuel – Roncalli" – Vigevano  
**Anno Scolastico:** 2025/2026  
**Docenti di riferimento:** Calarco Carmelo, Salterio Roberto  
**Libro di testo in adozione:**  
> *Internetworking Sistemi e Reti* – Baldino, Rondano, Spano, Iacobelli (Juvenilia Scuola – Volume 4° Anno)

---

## 🌐 MODULO TEORICO: Lo Stack di Rete e i Protocolli

### 1. Modelli Architetturali e Livello Fisico (Physical Layer)
- [ ] **Modelli di riferimento a confronto:** architettura ISO/OSI vs architettura TCP/IP
- [ ] **Concetto di PDU (Protocol Data Unit)** e processi di incapsulamento/decapsulamento
- [ ] **Il livello Physical TCP/IP:** sottolivelli, funzioni e standard trasmissivi principali

---

### 2. Livello Network (IP, Indirizzamento e Diagnostica)
- [ ] **Il protocollo IP (Internet Protocol):** funzioni e struttura del pacchetto (Header IP)
- [ ] **Indirizzamento IPv4:** classi di indirizzi, parte NetID e HostID, indirizzi privati vs pubblici
- [!] **Tecniche di suddivisione in sottoreti:**
  - [ ] **Subnetting** con maschera fissa (FLSM)
  - [ ] **CIDR** (*Classless Inter-Domain Routing*) e notazione `/prefix`
  - [ ] **VLSM** (*Variable Length Subnet Masking*)
- [!] **Risoluzione degli indirizzi:**
  - [ ] Mappatura IP-MAC tramite protocollo **ARP** e cenni su **RARP**
- [ ] **Diagnostica e monitoraggio:** protocollo **ICMP** (meccanismo del ping e traceroute)
- [ ] **Risoluzione dei nomi:** gerarchia e funzionamento del servizio **DNS**
- [ ] **Introduzione a IPv6:** limiti di IPv4, struttura e notazione degli indirizzi IPv6

---

### 3. Instradamento (Routing) e Reti Geografiche
- [ ] **Interconnessione di reti e router:** tabelle di instradamento (*routing table*)
- [ ] **Scenari e problematiche di routing:** instradamento statico vs dinamico
- [ ] **Algoritmi e protocolli di routing:** principi di funzionamento (*Distance Vector* e *Link State*)

---

### 4. Livello di Trasporto (Transport Layer)
- [ ] **Ruolo del livello Transport:** comunicazione *end-to-end*, porte e socket
- [ ] **Funzionalità di Multiplexing e Demultiplexing** del traffico
- [ ] **Protocollo TCP (Transmission Control Protocol):**
  - [ ] Segmento TCP, affidabilità, controllo di flusso e di congestione
  - [ ] Fasi della connessione: instaurazione (*Three-way Handshake*), trasmissione dati e chiusura
- [ ] **Protocollo UDP (User Datagram Protocol):** caratteristiche di velocità e assenza di connessione (*connectionless*)
- [ ] **Confronto analitico TCP vs UDP** (scenari d'uso tipici: streaming, web, DNS, VoIP)

---

### 5. Livello Applicativo (Application Layer) e Sicurezza
- [ ] **Panoramica dei principali protocolli applicativi:**
  - [ ] Trasferimento file: **FTP**
  - [ ] Accesso remoto: **Telnet**
  - [ ] Navigazione web: **HTTP / HTTPS**
  - [ ] Posta elettronica: **SMTP, POP3, IMAP4**
- [ ] **Sicurezza e vulnerabilità:** analisi delle debolezze intrinseche dei protocolli in chiaro e relative contromisure

---

## 🛠️ MODULO PRATICO E LABORATORIO

### 1. Certificazione Cisco e Configurazione Apparati
- [ ] **Integrazione curricolare:** svolgimento dei moduli del corso **Cisco CCNA 1** (*Introduction to Networks*)
- [ ] **Configurazione switch e router da Console:**
  - [ ] Connessione tramite cavo console / adattatore seriale
  - [ ] Comandi CLI base di navigazione nei vari livelli di privilegio
- [ ] **Messa in sicurezza degli apparati:**
  - [ ] Configurazione e cifratura delle password (`enable secret`, `service password-encryption`)
  - [ ] Configurazione dell'accesso remoto (**TELNET**) e linee VTY
  - [ ] Comandi CLI Cisco per il controllo accessi e la sicurezza

---

### 2. Simulazione Avanzata con Cisco Packet Tracer
- [ ] **Calcolo e applicazione pratica del Subnetting:** progettazione e assegnazione di schemi di indirizzamento IPv4
- [ ] **Configurazione di interfacce IPv4 e IPv6** su host e router
- [ ] **Segmentazione del traffico tramite VLAN:**
  - [ ] Creazione e configurazione di una singola VLAN tramite CLI
  - [ ] Assegnazione delle porte dello switch in modalità *Access*
- [ ] **Trunking e VLAN multiple:**
  - [ ] Configurazione delle porte in modalità *Trunk*
  - [ ] Incapsulamento con protocollo standard **IEEE 802.1Q (`dot1q`)**
  - [ ] Cenni di routing inter-VLAN (*Router-on-a-Stick*)

---

## 🎯 OBIETTIVI MINIMI DI DISCIPLINA (Soglia Sufficienza / Voto 6)

| Area | Conoscenze Minime Richieste | Abilità Minime Richieste |
| :--- | :--- | :--- |
| **Teoria delle Reti** | Modello ISO/OSI e TCP/IP, Livello Fisico, Livello Network (indirizzi IP, subnetting base, DNS, ICMP, IPv6), nozioni base sul Routing, confronto essenziale TCP/UDP, protocolli applicativi standard e relative nozioni di sicurezza. | Saper illustrare il funzionamento dei protocolli principali e spiegare il flusso di un pacchetto attraverso i livelli dello stack. |
| **Laboratorio & Pratica** | Corso Cisco CCNA1, comandi CLI base di configurazione router/switch, gestione password, subnetting, configurazione VLAN e trunking dot1q. | Saper configurare via riga di comando (CLI) una rete locale comprendente sottoreti IPv4 e VLAN virtuali su Packet Tracer. |

---

## 📌 METODOLOGIE, STRUMENTI E VALUTAZIONE

* **Metodologie didattiche:** Attività laboratoriali con simulatore e apparati fisici, lezioni frontali e dialogate, esercitazioni a gruppi (*cooperative learning*), *flipped classroom*.
* **Strumenti:** Piattaforma didattica Cisco NetAcad (CCNA1), software di simulazione *Cisco Packet Tracer*, aule multimediali/laboratorio reti, G-Suite, Registro Elettronico.
* **Educazione Civica:** Svolta secondo la Scheda n.1 approvata dal Consiglio di Classe (sicurezza dei dati, tracciabilità, privacy).
* **Griglia di Valutazione Laboratorio (Max 10 pt):**
  1. **Conoscenze (Max 3 pt):** padronanza dell'architettura e delle nozioni.
  2. **Abilità operative (Max 2.5 pt):** sintassi corretta dei comandi CLI, configurazione senza errori bloccanti.
  3. **Competenze (Max 2.5 pt):** capacità di troubleshooting e risoluzione del problema di rete.
  4. **Tempi e Autonomia (Max 2 pt):** rispetto delle consegne e puntualità.


![[2025_2026_Quarte_ITIS_Sistemi_e_reti.docx.pdf]]