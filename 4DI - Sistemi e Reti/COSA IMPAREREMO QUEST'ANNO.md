# 📚 COSA IMPAREREMO A 4DI QUEST'ANNO (2025-2026)

Benvenuto al quarto anno di Sistemi e Reti! 🎉

Ricordi a 3EI quando hai imparato il **"come funziona una rete"**? Quando hai smontato il PC e crimped il cavo Ethernet?

**Bene, adesso vai a fondo.** 🏊‍♂️

A 4DI non basta sapere che il PC è connesso — devi capire **OGNI PACCHETTO** che viaggia nella rete:
- Da quale IP parte?
- Verso quale IP va?
- Quale porta usa?
- Quale protocollo? (TCP? UDP?)
- Come lo "tracki" se non arriva?
- Come lo proteggi da attacchi?

Questo è il livello dove i **veri network engineer** giocano. E i **veri network engineer** guadagnano bene** — 2.500-4.500€/mese in Italia, di più all'estero.

---

## 🎯 Le Tre Grandi Domande che Rispondemmo

### 1️⃣ **"Come navigano i pacchetti dentro la rete?" (Stack TCP/IP Profondo)**

A 3EI hai imparato i **7 livelli ISO/OSI**. Ora zoomi su 4 livelli specifici dello stack TCP/IP che usano **veramente** tutti i giorni gli ingegneri di rete:

#### **Livello 1 (Physical):** Il filo
- Come il segnale viaggia nel rame (voltaggio), nella fibra (luce), nell'aria (onde radio)
- Velocità di trasmissione, latenza, distanza
- Per i tecnici che installano i cavi (raramente li configuri, ma devi sapere i limiti)

#### **Livello 2 (Data Link - MAC):** La "bolla" locale
- Come due computer **sulla stessa rete fisica** si trovano a vicenda (indirizzo MAC)
- Protocollo **Ethernet** — il sistema che tutti usiamo
- Switch (Layer 2) — come decide dove mandare un pacchetto basandosi sull'indirizzo MAC

#### **Livello 3 (Network - IP):** La "bolla" globale
- **Indirizzamento IPv4:** come passiamo dai "nomi postali" ai computer (192.168.1.100)
- **Subnetting:** come dividi una rete grande in sottoreti (l'arte di tagliare gli indirizzi IP)
- **Routing:** come un pacchetto attraversa 10 router per arrivare dall'Italia al Giappone
- **Diagnostica:** ping (test se arriva), traceroute (vedi il percorso), ARP (trovo il MAC di un IP)

- [ ] #dubbio chi riceve l'indirizzo IP dal provider? Lo switch? Il router? La singola macchina?

#### **Livello 4 (Transport - TCP/UDP):** La "consegna affidabile vs veloce"
- **TCP:** "garantisco che il pacchetto arriva intero e nell'ordine giusto" (web, email, file transfer) — **affidabile**
- **UDP:** "spaccio il pacchetto il più veloce possibile, se qualcuno si perde, pazienza" (video streaming, gaming, VoIP) — **veloce ma rischia**

**Concretamente:**
```
Firefox richiede www.google.com

1. (Livello 7 - Applicazione) Browser: "Dimmi l'IP di google.com"
2. (Livello 3 - Network - DNS) Sistema: "google.com = 142.251.32.14"
3. (Livello 4 - Transport - TCP) Browser: "OK, connetto a 142.251.32.14 porta 80 (HTTP)"
4. (Livello 3 - Network - IP) Router: "142.251.32.14 è in Giappone, mando il pacchetto via router 1, 2, 3, ..."
5. (Livello 2 - Ethernet) Switch: "L'indirizzo MAC del prossimo router è XX:XX:XX, glelo mando"
6. (Livello 1 - Physical) Cavo: "Spedisco voltaggio lungo il rame"
7. [Viaggio attraverso il mondo] 
8. (Livello 2 - Ethernet) Switch di Google: "È per la porta 6, glelo mando"
9. (Livello 1 - Physical) Luce nella fibra: "Arrivati!"
10. (Livello 3 - Network) Router di Google: "OK, questo è un pacchetto per me"
11. (Livello 4 - Transport) Port 80: "HTTP server, ricevi il pacchetto"
12. (Livello 7 - Applicazione) Browser Google: "Ricevo la pagina HTML, la disegno sullo schermo"
```

---

### 2️⃣ **"Come configuro e configuro un router/switch via linea di comando?" (CLI Cisco & Configurazione)**

A 3EI hai visto Packet Tracer (la **simulazione**). Adesso **tocchi un vero router Cisco** e lo configuri da linea di comando (CLI — Command Line Interface).

**Cosa vedrai in pratica:**
- Connetterti via **console cable** (il cordone ombelicale del router)
- Accedere ai vari **livelli di privilegio** Cisco:
  - `Router>` — utente (limitato)
  - `Router#` — privilegio elevato
  - `Router(config)#` — configurazione globale
- Comandiz essenziali:
  ```
  Router(config)# hostname MioRouter  ← rinomina il router
  Router(config)# interface g0/0     ← entra nell'interfaccia Gigabit 0/0
  Router(config-if)# ip address 192.168.1.1 255.255.255.0  ← assegna IP
  Router(config-if)# no shutdown     ← accendi l'interfaccia
  ```
- **VLAN:** come dividi uno switch fisico in tante reti "virtuali"
- **Trunking:** come fai comunicare VLAN diverse attraverso un singolo cavo (802.1Q)
- **Routing dinamico:** come configuri un router per imparare automaticamente le rotte (OSPF, RIP, EIGRP)

**Il primo progetto vero:**
Configurerai una rete con 2-3 router reali via CLI Cisco. Assegnerai IP, configurerai VLAN, farai un ping end-to-end. Vedrai davvero il pacchetto viaggiare da un router all'altro.

---

### 3️⃣ **"Come intercetto e analizzo i pacchetti?" (Wireshark — Packet Sniffing)**

**Wireshark** è il "microscopio digitale" della rete. Ti permette di "catturare" ogni singolo pacchetto che passa dal tuo PC e vederlo in dettaglio.

**Cosa vedrai in pratica:**
- Avvii Wireshark, fai partire una cattura
- Fai qualcosa sul PC (visiti Google, apri YouTube)
- Wireshark cattura **migliaia di pacchetti** in tempo reale
- Zoomi su uno e vedi:
  - Il MAC address source e destination
  - L'IP address source e destination
  - La porta source e destination
  - Il protocollo (TCP/UDP/ICMP)
  - Il payload (i dati veri e propri)

**Importanza didattica:**
Non è solo "figo". È essenziale per **diagnosticare problemi di rete**:
- Il server non risponde? → guarda i pacchetti TCP
- YouTube non buffering? → guarda i pacchetti UDP
- Il DNS non funziona? → cattura e analizza le query DNS

**Bonus sicurezza:**
Con Wireshark vedi che se qualcuno invia la password in chiaro (plain text) su HTTP, vedrai la password nel payload. Ecco perché HTTPS (con crittografia) è obbligatorio oggi.

---

## 📋 I Contenuti Specifici

### 🌐 Primo Semestre: Stack TCP/IP Profondo (Settembre - Gennaio)

| **Periodo** | **Cosa Imparemmo in Aula** | **In Laboratorio (Packet Tracer + Hardware vero)** |
|---|---|---|
| **Settembre - Ottobre** | Modelli ISO/OSI vs TCP/IP, Livello Physical e Data Link (MAC, Ethernet, CSMA/CD) | Cisco CCNA 1 (NetAcad): prime lezioni, Packet Tracer base, configurazione IP statico su switch |
| **Novembre - Dicembre** | Livello Network (IPv4, IPv6, Subnet, CIDR, DNS, ICMP, ARP), Indirizzamento | Packet Tracer: calcoli di subnetting, assegnazione IP, test ping/traceroute, configurazione DNS |
| **Gennaio** | Livello Transport (TCP vs UDP), Porte e Socket, stateful vs stateless | Packet Tracer: configurazione DHCP server, monitoraggio TCP/UDP, analisi del 3-way handshake |

### 🛠️ Secondo Semestre: Configurazione e Diagnostica (Febbraio - Giugno)

| **Periodo** | **Cosa Imparemmo in Aula** | **In Laboratorio (CLI Cisco + Wireshark)** |
|---|---|---|
| **Febbraio - Marzo** | Router e Switch base, gerarchie di accesso Cisco, VLAN (concetti), Trunking (802.1Q) | Connessione via console a router vero, configurazione hostname/password, interfacce IP |
| **Aprile - Maggio** | Routing (statico vs dinamico), OSPF base, ACL (Access Control List), Wireshark | CLI Cisco avanzato: configurare VLAN, trunking, routing, catturare e analizzare pacchetti con Wireshark |
| **Giugno** | Routing dinamico (OSPF), Basi di cybersecurity (firewall, IDS), Intro VPN | Progetto integrato: una rete multi-VLAN con routing, test end-to-end, analisi con Wireshark, recupero |

---

## 💡 Perché Tutto Questo Serve?

✅ **Per il lavoro (short term):**
- Un **network engineer junior** in Italia guadagna 1.800-2.800€/mese
- In aziende grandi (banche, telecom, tech) facilmente 3.000-4.000€/mese
- **CCNA (Cisco Certified Network Associate)** — la certificazione che farai l'anno prossimo — è riconosciuta **mondialmente**
- Le aziende pagano per gente che sa configura reti in production (il "vero mondo")

✅ **Per la specializzazione (medio term):**
- Network Security Engineer (aggiunge crittografia e firewall)
- DevOps + Network (deploy su cloud AWS/Azure, orchestrazione)
- Cloud Infrastructure Engineer (reti virtuali sul cloud)
- Penetration Tester (eticamente "hackerare" per trovare buchi di sicurezza)

✅ **Per il presente:**
- Capirai come funziona **veramente** Internet — non il "marketing" che vedi sui media
- Diventerai capace di **diagnosticare qualsiasi problema di rete** (il WiFi non funziona? Io so risolvere!)
- Avrai competenze **dirette commerciabili** — puoi già lavorare come junior network admin se sei bravo
- La mentalità "sistemica e globale" che impari qui vale anche fuori dall'IT

---

## 🎯 I Progetti che Farai

1. **Settembre-Ottobre:** Packet Tracer beginner — topologie semplici, IP statico
2. **Novembre-Dicembre:** Calcoli di subnetting e progetti avanzati di Packet Tracer
3. **Gennaio:** Hardware vero — connessione console, primo router configurato
4. **Febbraio-Marzo:** VLAN e trunking, rete multi-VLAN
5. **Aprile-Maggio:** Wireshark — analisi di pacchetti, traccia di problemi di rete
6. **Giugno:** Progetto finale integrativo (rete con router, switch, VLAN, routing, documentazione completa)

**Bonus Cisco CCNA 1:**
Completerai il corso ufficiale Cisco **CCNA 1 - Introduction to Networks** e avrai il certificato di NetAcad.

---

## 🚀 Aspettative e Regole del Gioco

### ✨ Quello che Ci Aspettiamo da Te:

1. **Precisione:** Un errore nella configurazione e la rete non funziona — abituati al rigore
2. **Diagnostica:** Non è "il router non funziona". È "ho controllato con ping, traceroute, Wireshark e il problema è qui"
3. **Documentazione:** Disegna la tua rete prima. Documenta ogni passo. Un tecnico che sa spiegare il suo lavoro vale il doppio
4. **Sicurezza:** Quando lavori con veri router/switch, sai che una configurazione sbagliata potrebbe impattare la rete reale
5. **Curiosità:** "Perché il protocollo X funziona così?" — questa è la domanda giusta

### 📋 Come Funzionerà l'Anno:

- **Lezione in aula (2 ore/settimana):** stack TCP/IP, protocolli, architetture
- **Laboratorio con ITP (2 ore/settimana):**
  - Primo semestre: Packet Tracer (simulazione)
  - Secondo semestre: Router/Switch veri (CLI) + Wireshark (sniffing)
- **Iscrizione a NetAcad (Cisco):** corso CCNA 1 integrato (seguirai lezioni video, farai quiz, progetti pratici)

### 🎓 Voto:
- Teoria: 35% (conosci TCP/IP? Sai la differenza tra TCP e UDP? Cos'è il subnetting?)
- Pratica/Laboratorio: 50% (sai configurare un router? Sai leggere Wireshark?)
- Documentazione e Relazioni: 15% (comunichi bene quello che hai fatto?)

---

## 🎬 TL;DR (Troppo Lungo; Non Ho Letto)

**4DI = diventare un network engineer (per davvero)**

- **Stack TCP/IP profondo** — come funziona veramente Internet
- **IPv4/IPv6, Subnetting, Routing** — come naviga il traffico
- **CLI Cisco** — comandi per configurare router/switch reali
- **VLAN, Trunking** — come segmenti la rete
- **Wireshark** — come analizzi i pacchetti
- **Certificazione CCNA 1** — primo passo verso la certificazione riconosciuta mondialmente

**Bonus:** Se sei bravo, puoi fare **penetration testing** (hacking etico) come secondaria — uno skill ancora più raro 🏆

---

**Pronto a imparare come funziona veramente il mondo digitale? Let's network! 🚀**
