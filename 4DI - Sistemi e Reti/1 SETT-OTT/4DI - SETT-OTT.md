# SETT-OTT — 4ª DI (Sistemi e Reti)

Piano operativo delle prime 8 settimane (Settembre–Ottobre) per la 4ª DI (Sistemi e Reti: stack TCP/IP, indirizzamento, Cisco CCNA1).

* **Monte ore:** 4 ore settimanali (2 ore di teoria in aula + 2 ore di laboratorio, in compresenza con l'ITP).
* **Obiettivo del bimestre:** Ripartire dal modello ISO/OSI e TCP/IP con il concetto di incapsulamento, per poi affrontare in profondità il protocollo IP e l'indirizzamento IPv4 (classi, subnetting, ARP, ICMP, DNS), avviando in parallelo il corso Cisco CCNA1 e le prime configurazioni via CLI.

---

## 🧭 Quadro Sinottico Settimana per Settimana (Settembre – Ottobre)

```
┌───────────┬──────────────────────────────────────┬────────────────────────────────────────┐
│ SETTIMANA │ TEORIA (2h - In aula)                 │ LABORATORIO (2h - Con ITP)              │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 1   │ ISO/OSI vs TCP/IP; PDU e              │ Iscrizione Cisco NetAcad (CCNA1),      │
│           │ incapsulamento/decapsulamento         │ ripasso Packet Tracer, prima topologia │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 2   │ Protocollo IP: header, funzioni;      │ Cavo console e CLI (User/Privileged/   │
│           │ Indirizzamento IPv4 (classi, Net/Host)│ Global Config), IP statico su PC in PT │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 3   │ Indirizzi pubblici vs privati (RFC    │ Configurazione IP su interfacce router │
│           │ 1918); introduzione al Subnetting FLSM│ e switch, primi comandi `show`          │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 4   │ Subnetting FLSM (esercizi numerici);  │ Progettazione schema di indirizzamento │
│           │ cenni a CIDR e notazione `/prefix`    │ IPv4 di una piccola rete in Packet Tracer│
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 5   │ VLSM (Variable Length Subnet Masking);│ Applicazione pratica VLSM su topologia │
│           │ risoluzione indirizzi: ARP e RARP     │ multi-rete, cattura frame ARP           │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 6   │ Diagnostica: protocollo ICMP           │ Prove pratiche `ping`/`traceroute`,    │
│           │ (ping, traceroute); risoluzione DNS    │ configurazione server DNS in Packet Tracer│
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 7   │ Ripasso attivo e simulazione           │ Consolidamento pratico: subnetting +   │
│           │ della prova scritta                    │ configurazione completa fine-to-fine    │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 8   │ 📝 VERIFICA SCRITTA 1 (IP e            │ Capitoli Cisco NetAcad CCNA1 e verifica│
│           │ Indirizzamento)                        │ pratica di configurazione               │
└───────────┴──────────────────────────────────────┴────────────────────────────────────────┘
```

---

## 📝 Dettaglio Operativo dei Moduli

---

### SETTIMANA 1: Ripartenza dallo Stack: ISO/OSI, TCP/IP e Incapsulamento
*Obiettivo: riallineare la classe sui modelli di riferimento visti in 3° anno, ponendo le basi per il resto del bimestre.*

* **Teoria (2h):**
  * Presentazione del programma annuale: stack TCP/IP a fondo (Network, Transport, Application) + certificazione Cisco CCNA1.
  * Ripasso comparato: modello **ISO/OSI** a 7 livelli vs modello **TCP/IP** a 4/5 livelli, mappatura tra i due.
  * Concetto di **PDU** (*Protocol Data Unit*) e processo di **incapsulamento/decapsulamento** lungo la pila di protocolli.
* **Laboratorio (2h):**
  * Iscrizione alla piattaforma **Cisco Networking Academy** per il corso **CCNA1 (Introduction to Networks)**.
  * Ripasso rapido dell'interfaccia di **Cisco Packet Tracer** (già usato in 3° anno).
  * Attività: costruire una topologia semplice PC–Switch–Router e osservare l'incapsulamento pacchetto per pacchetto in modalità simulazione.
* 📚 **Cosa devi ripassare tu:**
  * I nomi delle PDU a ogni livello (bit, frame, pacchetto, segmento, dato) per non confonderti durante la spiegazione dell'incapsulamento.

---

### SETTIMANA 2: Il Protocollo IP e l'Indirizzamento IPv4
*Obiettivo: entrare nel dettaglio del livello Network, a partire dalla struttura del pacchetto IP.*

* **Teoria (2h):**
  * Il **protocollo IP**: funzioni principali e struttura dell'header (versione, TTL, protocollo, checksum, IP sorgente/destinazione).
  * **Indirizzamento IPv4:** le classi storiche A/B/C, concetto di **NetID** e **HostID**.
  * Introduzione alla distinzione tra indirizzi validi e non validi in una rete (cenno, approfondito in Settimana 3).
* **Laboratorio (2h):**
  * Connessione a router/switch tramite cavo console: ripasso delle modalità CLI (**User EXEC → Privileged EXEC → Global Configuration**).
  * Configurazione di indirizzi IP statici su PC host in Packet Tracer.
  * Esercizio di riconoscimento: dato un indirizzo IP, individuare classe di appartenenza e separazione NetID/HostID.
* 📚 **Cosa devi ripassare tu:**
  * Le soglie numeriche delle classi A/B/C (`1-126`, `128-191`, `192-223`) e i relativi indirizzi riservati/speciali (`127.x`, `0.0.0.0`, broadcast).

---

### SETTIMANA 3: Indirizzi Pubblici, Privati e Subnetting FLSM
*Obiettivo: introdurre la necessità pratica di suddividere le reti in sottoreti.*

* **Teoria (2h):**
  * **Indirizzi privati** (RFC 1918: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) vs **indirizzi pubblici**; cenno al ruolo del **NAT**.
  * Perché non basta assegnare indirizzi di classe: introduzione al **Subnetting** con maschera fissa (**FLSM**).
* **Laboratorio (2h):**
  * Configurazione di indirizzi IP su interfacce di router e switch in Packet Tracer.
  * Primi comandi diagnostici `show ip interface brief`, `show running-config`.
* 📚 **Cosa devi ripassare tu:**
  * Il meccanismo dell'AND bit a bit tra indirizzo IP e maschera di sottorete per ricavare il NetID.

---

### SETTIMANA 4: Subnetting FLSM Avanzato e Notazione CIDR
*Obiettivo: rendere gli studenti autonomi nel calcolo di sottoreti a maschera fissa.*

* **Teoria (2h):**
  * Esercizi numerici guidati di **Subnetting FLSM**: calcolo di NetID, primo/ultimo host validi, indirizzo di broadcast.
  * Cenni a **CIDR** (*Classless Inter-Domain Routing*) e alla notazione `/prefix`.
* **Laboratorio (2h):**
  * Progettazione dello schema di indirizzamento IPv4 di una piccola rete multi-subnet in Packet Tracer.
  * Assegnazione degli indirizzi calcolati alle interfacce di router/PC e verifica di connettività.
* 📚 **Cosa devi ripassare tu:**
  * La tabella delle potenze di 2 (per ricavare rapidamente il numero di host per sottorete in base ai bit di host rimanenti).

---

### SETTIMANA 5: VLSM e Risoluzione degli Indirizzi (ARP/RARP)
*Obiettivo: ottimizzare l'uso dello spazio di indirizzamento e introdurre la mappatura IP↔MAC.*

* **Teoria (2h):**
  * **VLSM** (*Variable Length Subnet Masking*): suddivisione in sottoreti di dimensione diversa a seconda del numero di host richiesti.
  * **Risoluzione degli indirizzi:** il protocollo **ARP** (mappatura IP→MAC) e cenno al **RARP**.
* **Laboratorio (2h):**
  * Applicazione pratica di VLSM su una topologia multi-rete in Packet Tracer.
  * Cattura e analisi di un frame ARP in modalità simulazione (Packet Tracer Simulation Mode).
* 📚 **Cosa devi ripassare tu:**
  * Il funzionamento della richiesta ARP in broadcast e della risposta in unicast, da disegnare passo-passo alla lavagna.

---

### SETTIMANA 6: Diagnostica di Rete (ICMP) e Risoluzione dei Nomi (DNS)
*Obiettivo: fornire gli strumenti diagnostici di base e introdurre il servizio DNS.*

* **Teoria (2h):**
  * Il protocollo **ICMP**: meccanismo di `ping` (echo request/reply) e di `traceroute` (TTL decrescente).
  * Il servizio **DNS**: gerarchia dei nomi a dominio e funzionamento essenziale della risoluzione nome→IP.
* **Laboratorio (2h):**
  * Prove pratiche di `ping` e `traceroute` tra dispositivi in Packet Tracer, analisi dei messaggi ICMP generati.
  * Configurazione di un server DNS di base in Packet Tracer e verifica della risoluzione dei nomi da un client.
* 📚 **Cosa devi ripassare tu:**
  * La differenza tra i codici ICMP più comuni (*Destination Unreachable*, *Time Exceeded*) da mostrare con un esempio pratico di `traceroute` fallito.

---

### SETTIMANA 7: Ripasso Attivo e Preparazione alla Verifica
*Obiettivo: consolidare tutto il modulo di indirizzamento IP con esercizi di retrieval practice.*

* **Teoria (2h):**
  * **Simulazione di verifica (mock test):** esercizi di subnetting FLSM/VLSM, domande teoriche su ICMP/ARP/DNS.
  * Correzione collettiva alla lavagna, enfasi sugli errori tipici di calcolo (maschera, broadcast, range host).
* **Laboratorio (2h):**
  * Consolidamento pratico: configurazione end-to-end di una rete con subnetting, verifica di connettività completa (`ping` tra tutte le sottoreti).
* 📚 **Cosa devi ripassare tu:**
  * Prepara il testo della verifica scritta (due file bilanciati: Fila A e Fila B, con esercizi di subnetting diversi ma di pari difficoltà).

---

### SETTIMANA 8: La Prima Verifica Sommativa
*Obiettivo: misurare l'acquisizione delle competenze sul protocollo IP e l'indirizzamento.*

* **Teoria (2h):**
  * 📝 **VERIFICA SCRITTA N. 1 (Protocollo IP, Indirizzamento IPv4, Subnetting FLSM/VLSM, ARP, ICMP, DNS)**.
  * Struttura consigliata: esercizio di subnetting guidato + quesiti teorici a risposta multipla/aperta.
* **Laboratorio (2h):**
  * Sessione Cisco NetAcad (capitoli CCNA1 relativi a indirizzamento e livello Network) con quiz di autovalutazione.
  * Verifica pratica di configurazione di una piccola rete indirizzata in Packet Tracer.
* 📚 **Cosa devi fare tu:**
  * Correggi le verifiche scritte entro pochi giorni, annotando gli errori di calcolo più frequenti per impostare il ripasso del bimestre successivo.
