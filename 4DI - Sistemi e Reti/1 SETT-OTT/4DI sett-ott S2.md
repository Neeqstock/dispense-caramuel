Ecco il kit didattico completo per la **Settimana 2**, strutturato come una **mappa concettuale espansa (mindmap ad albero)** con tutti i contenuti pronti per essere spiegati alla lavagna e svolti al PC.

> Nota: il quadro sinottico delle 8 settimane e il dettaglio sintetico settimana per settimana si trovano in [4DI - SETT-OTT.md](4DI%20-%20SETT-OTT.md).

---

# 🗺️ SETTIMANA 2: IL PROTOCOLLO IP E L'INDIRIZZAMENTO IPv4

```text
SETTIMANA 2
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] Il Protocollo IP: Ruolo e Funzioni
│   ├── [1.2] L'Header IP Sotto la Lente
│   ├── [1.3] Indirizzamento IPv4: le Classi Storiche A/B/C
│   └── [1.4] NetID e HostID: Separare Rete e Host
│
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] Il Cavo Console e le Modalità CLI
│   ├── [2.2] Navigazione tra User EXEC, Privileged EXEC, Global Config
│   ├── [2.3] Configurazione di IP Statico su PC in Packet Tracer
│   └── [2.4] Esercitazione Pratica Guidata (Missione: "Riconosci l'Indirizzo")
│
└── 📋 GUIDA DI REGIA PER IL DOCENTE
    ├── Scaletta Minuto per Minuto
    ├── Schema da Disegnare alla Lavagna
    └── Micro-Task di Consolidamento (Formative Assessment)
```

---

## 🧠 MODULO TEORICO (2 Ore in Aula)

### ├── [1.1] Il Protocollo IP: Ruolo e Funzioni
*Obiettivo: collocare con precisione il protocollo IP nel livello Network, dopo il ripasso generale della scorsa settimana.*

* 📌 **Cos'è il protocollo IP (*Internet Protocol*):** il protocollo che si occupa dell'**indirizzamento logico** e dell'**instradamento** (routing) dei pacchetti tra reti diverse.
* 🎯 **Le due funzioni chiave:**
  * **Indirizzamento:** assegnare un identificativo univoco (l'indirizzo IP) a ogni dispositivo di rete.
  * **Instradamento (routing):** determinare il percorso migliore per far arrivare un pacchetto da mittente a destinatario, anche attraverso reti intermedie.
* ⚠️ **Un servizio "best-effort":** IP non garantisce che i pacchetti arrivino, arrivino in ordine o senza errori — questi compiti sono demandati ad altri protocolli (es. TCP, livello Transport).

---

### ├── [1.2] L'Header IP Sotto la Lente
*Obiettivo: analizzare la struttura del pacchetto IP, campo per campo (i più rilevanti per un tecnico).*

```text
                    HEADER DEL PACCHETTO IPv4 (semplificato)
┌────────────┬────────────┬─────────────────────────────────┐
│  Versione  │    TTL     │   Protocollo (TCP=6, UDP=17,...) │
├────────────┴────────────┴─────────────────────────────────┤
│                  Indirizzo IP Sorgente                     │
├─────────────────────────────────────────────────────────────┤
│                Indirizzo IP Destinazione                   │
├─────────────────────────────────────────────────────────────┤
│                       Checksum Header                       │
└─────────────────────────────────────────────────────────────┘
```

* 🔢 **Versione:** `4` per IPv4 (vedremo IPv6 più avanti nel bimestre successivo).
* ⏳ **TTL (*Time To Live*):** contatore che si decrementa a ogni router attraversato; se arriva a 0, il pacchetto viene scartato (evita loop infiniti di routing).
* 🏷️ **Campo Protocollo:** indica quale protocollo di livello Transport è incapsulato nei dati (es. `6` = TCP, `17` = UDP) — fondamentale per il decapsulamento corretto.
* ✅ **Checksum:** permette di verificare che l'header non sia stato corrotto durante il trasporto.
* 📍 **Indirizzi IP sorgente/destinazione:** i due campi più importanti per un tecnico di rete, oggetto del resto della lezione.

---

### ├── [1.3] Indirizzamento IPv4: le Classi Storiche A/B/C
*Obiettivo: introdurre lo schema di classificazione storico degli indirizzi IPv4, base di partenza per il subnetting.*

```text
CLASSE   PRIMO OTTETTO     BIT INIZIALI    USO TIPICO
──────────────────────────────────────────────────────────────
  A         1 - 126            0            Reti enormi (poche reti,
                                             milioni di host ciascuna)
  B        128 - 191           10           Reti medie (aziende, univ.)
  C        192 - 223          110           Reti piccole (LAN comuni)
  D        224 - 239          1110          Multicast (non per host)
  E        240 - 255          1111          Sperimentale/riservata
```

* 🔢 **Indirizzo IPv4:** 32 bit, scritto in **notazione decimale puntata** (es. `192.168.1.10`), 4 ottetti da 8 bit ciascuno.
* ⚠️ **Indirizzi speciali da ricordare:**
  * `127.0.0.0/8` → *loopback* (es. `127.0.0.1`, il proprio PC).
  * `0.0.0.0` → indirizzo "sconosciuto"/di default.
  * L'ultimo indirizzo di ogni rete è riservato al **broadcast**.
* 💡 **Nota storica:** oggi si usa quasi ovunque il **CIDR** (Settimana 3-4) al posto delle classi rigide, ma conoscere le classi resta utile per orientarsi velocemente su un indirizzo IP.

---

### ├── [1.4] NetID e HostID: Separare Rete e Host
*Obiettivo: introdurre il concetto chiave che verrà usato per tutto il resto del bimestre (subnetting incluso).*

```text
        Indirizzo IP: 192 . 168 .  1  . 10
                      └──────┬──────┘└─┬─┘
                         NetID        HostID
                    (identifica       (identifica
                     la RETE)         l'HOST nella rete)
```

* 🏘️ **NetID:** la parte dell'indirizzo che identifica la **rete** a cui appartiene il dispositivo.
* 🏠 **HostID:** la parte dell'indirizzo che identifica il **singolo dispositivo** all'interno di quella rete.
* 🎭 **Metafora d'aula:** un indirizzo postale ha una via/città (NetID, la "zona") e un numero civico (HostID, la "casa specifica" in quella zona).
* 🎯 **Perché è cruciale:** due dispositivi possono comunicare direttamente solo se hanno **lo stesso NetID** (stessa rete); altrimenti serve un router che li colleghi.

---

## 💻 MODULO LABORATORIO (2 Ore con ITP)

### ├── [2.1] Il Cavo Console e le Modalità CLI
*Obiettivo: ripassare come ci si collega fisicamente e logicamente a un apparato Cisco, prima di configurarlo.*

* 🔌 **Il cavo console (o adattatore USB-seriale):** collega il PC direttamente alla porta di gestione di router/switch, permettendo la configurazione anche quando l'apparato non ha ancora una rete funzionante.
* 💻 **Software terminale:** utilizzo di un emulatore di terminale (es. quello integrato in Packet Tracer, o PuTTY/Tera Term nella realtà) per aprire una sessione CLI.

---

### ├── [2.2] Navigazione tra User EXEC, Privileged EXEC, Global Config
*Obiettivo: ripassare la gerarchia dei "livelli di potere" della CLI Cisco, indispensabile per ogni configurazione futura.*

```text
     User EXEC          Privileged EXEC         Global Configuration
   Switch>            Switch#                 Switch(config)#
   (comandi limitati,   (comandi completi,      (modifica la
    solo consultazione)  incluso `configure`)    configurazione attiva)

        comando "enable"  ───────►
        comando "disable" ◄───────
                              comando "configure terminal" ───────►
                              comando "exit"                ◄───────
```

* 🔑 **User EXEC (`>`):** modalità di ingresso, comandi di sola consultazione (es. `ping`, `show` limitati).
* 🔓 **Privileged EXEC (`#`):** si accede con `enable`; permette comandi completi di diagnostica (`show running-config`, `show ip interface brief`).
* ⚙️ **Global Configuration (`(config)#`):** si accede con `configure terminal`; qui si modificano effettivamente le impostazioni dell'apparato (hostname, interfacce, password, ...).
* 🎯 **Regola pratica:** più si scende nella gerarchia, più i comandi diventano "potenti" e potenzialmente pericolosi (si può disattivare un'interfaccia, cambiare una password, ecc.).

---

### ├── [2.3] Configurazione di IP Statico su PC in Packet Tracer
*Obiettivo: mettere in pratica NetID/HostID assegnando indirizzi coerenti a dispositivi reali (simulati).*

* 🖥️ **Interfaccia di configurazione IP su un PC (in Packet Tracer):** scheda "Desktop" → "IP Configuration".
* 📝 **Campi da compilare:** indirizzo IP, subnet mask, gateway predefinito (facoltativo per ora, approfondito quando si parlerà di routing).
* ✅ **Verifica:** uso del comando `ping` da un PC all'altro per controllare la connettività, osservando cosa succede se i due PC hanno NetID diversi senza un router di mezzo.

---

### ├── [2.4] Esercitazione Pratica Guidata al PC (Durata: 70-80 minuti)

#### FASE A: Accesso CLI e navigazione tra modalità (20 min)
1. Aprire la CLI di uno switch/router in Packet Tracer (tramite tab "CLI" del dispositivo).
2. Praticare il passaggio `> enable` → `#`, poi `# configure terminal` → `(config)#`, e il ritorno con `exit`/`end`.
3. Provare un comando di ciascuna modalità (es. `show version` in Privileged EXEC).

#### FASE B: Configurazione IP sui PC (25 min)
1. Sulla topologia PC–Switch–Router della scorsa settimana, assegnare indirizzi IP nella stessa subnet ai due PC (es. `192.168.1.1` e `192.168.1.2`, maschera `255.255.255.0`).
2. Verificare la connettività con `ping` tra i due PC.

#### FASE C: Riconoscimento di classi e NetID/HostID (20 min)
1. Fornire agli studenti una lista di 6-8 indirizzi IP misti (classe A, B, C).
2. Per ciascuno: individuare la classe di appartenenza e separare NetID da HostID (assumendo maschera di default della classe).

#### FASE D: Consegna e riflessione (10 min)
1. Screenshot della configurazione IP e del `ping` riuscito, da consegnare su Google Classroom.
2. Domanda di chiusura: *«Se cambio l'ultimo numero dell'indirizzo IP di un PC, cambia il NetID o l'HostID?»*

---

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma Lezione Teorica (110 min, 2h)
* **00-10 min | Accoglienza e recap Settimana 1:** ripasso veloce di ISO/OSI, TCP/IP, incapsulamento.
* **10-25 min | L'Hook d'apertura:** mostra un indirizzo postale reale (via, città, numero civico) e chiedi *«Cosa cambia se cambio solo il numero civico? E se cambio la città?»*, introducendo NetID/HostID in anteprima.
* **25-50 min | Il protocollo IP e il suo header:** disegna la struttura semplificata dell'header, spiega TTL e campo Protocollo con esempi concreti.
* **50-75 min | Le classi A/B/C:** disegna la tabella delle classi alla lavagna, fai calcolare in coro la classe di 3-4 indirizzi proposti a voce.
* **75-100 min | NetID e HostID:** disegna lo schema di separazione dell'indirizzo, collega alla metafora dell'indirizzo postale.
* **100-110 min | Chiusura e domande a bruciapelo:** 3 domande rapide (*«Cos'è il TTL? A quale classe appartiene 172.20.5.1? Cos'è il NetID?»*).

### ✍️ Disegno Guida da fare alla Lavagna (Lezione 1)

```text
    ┌─────────────────────────────────────────────────────────┐
    │       NetID vs HostID: L'INDIRIZZO POSTALE DIGITALE       │
    │                                                         │
    │   Via Roma 10, Vigevano   ↔   192.168.1.10              │
    │   └──────┬──────┘└┬┘          └────┬────┘└┬┘            │
    │        Via/Città  civico        NetID   HostID          │
    └─────────────────────────────────────────────────────────┘
```

### 🎯 Micro-Task Formativa per Casa (Spaced Retrieval - 5 minuti)
Carica su Google Classroom questo compito (senza voto punitivo, solo spunta di completamento):
> *"Prendi 3 indirizzi IP a scelta (inventali) di classi diverse (A, B, C). Per ciascuno indica: classe, NetID e HostID (assumendo la maschera di default della classe)."*

Da completare inoltre entro la lezione successiva: **primo quiz del Capitolo 2 di Cisco CCNA1 su NetAcad (livello Network)**.

---

## 🧭 DALL'IP ALLA DECISIONE: COME RAGIONA UN HOST

Un indirizzo IPv4 non e' completo senza la maschera. La maschera dice al dispositivo dove finisce il prefisso di rete e dove comincia la parte host.

### Notazione binaria e AND: un esempio completo

Consideriamo `192.168.1.35` con maschera `255.255.255.0`:

```text
IP:       11000000.10101000.00000001.00100011
Maschera: 11111111.11111111.11111111.00000000
Risultato:11000000.10101000.00000001.00000000 = 192.168.1.0
```

Il risultato e' la rete. Per una maschera `/24`, gli ultimi 8 bit sono host: `.0` identifica la rete, `.255` il broadcast e `.1-.254` gli host normalmente assegnabili.

Ora confrontiamo `192.168.1.35/24` con `192.168.2.35/24`: la parte di rete e' diversa, quindi i due host non sono nella stessa LAN logica anche se hanno lo stesso ultimo ottetto.

### Come decide se usare il gateway

```text
            stessa rete?
PC mittente ────────────────┬──────────────► host locale
                   │ no
                   ▼
                 gateway
```

L'host calcola la propria rete e quella della destinazione. Se coincidono, cerca il destinatario sulla LAN; se non coincidono, invia il frame al gateway predefinito. Il gateway non e' “Internet”: e' il router locale a cui l'host consegna il traffico destinato fuori rete.

### Esercizio guidato: classificare senza indovinare

Per ciascun indirizzo indicare classe storica, indirizzo speciale eventuale, NetID e HostID usando la maschera classful:

| Indirizzo | Classe attesa | Maschera storica | Osservazione |
|---|---|---|---|
| `10.4.7.9` | A | `255.0.0.0` | privato RFC 1918 |
| `172.20.5.12` | B | `255.255.0.0` | privato RFC 1918 |
| `192.168.4.25` | C | `255.255.255.0` | privato RFC 1918 |
| `127.0.0.1` | A come classe storica | `/8` | loopback, non host di rete |
| `224.0.0.1` | D | non classful per host | multicast |

La classificazione storica e la validita' pratica sono due domande diverse: `127.0.0.1` ricade nell'intervallo numerico della classe A, ma non e' assegnabile a una scheda per comunicare con un altro host.

### L'header IPv4: che cosa cambia attraversando un router?

| Campo | Tra PC e gateway | Tra gateway e rete successiva |
|---|---|---|
| IP sorgente/destinazione | normalmente invariati | normalmente invariati |
| TTL | valore iniziale | diminuito di 1 |
| Protocollo | indica ICMP/TCP/UDP | resta lo stesso |
| MAC del frame | cambia a ogni tratto | viene ricostruito |

Questa tabella prepara la distinzione tra pacchetto e frame: il router legge il pacchetto IP per decidere, ma trasmette quel pacchetto dentro un nuovo frame adatto al collegamento successivo.

### Laboratorio: prove di falsificazione

Non correggere subito una configurazione sbagliata. Formulare prima una previsione:

1. Mettere PC-A `192.168.1.10/24` e PC-B `192.168.1.20/24`: il ping deve riuscire.
2. Cambiare PC-B in `192.168.2.20/24` senza aggiungere un router: prevedere il fallimento.
3. Ripristinare la rete e cambiare solo la maschera di PC-B in `/16`: prevedere che il risultato possa sembrare controintuitivo.
4. Aprire il prompt e usare `ipconfig`, poi verificare con `ping`.
5. Scrivere la causa ipotizzata prima di correggere.

### Domande di ripasso e intuizione

1. Perche' la maschera deve essere uguale sui due host di una LAN?
2. Qual e' la differenza tra indirizzo di rete, indirizzo host e broadcast?
3. Che cosa indica il campo `Protocol` dell'header IP? Perche' non contiene la porta?
4. **Intuizione:** due PC possono avere lo stesso IP se si trovano su reti private isolate? Quale problema nasce quando le reti vengono collegate?
5. **Intuizione:** perche' il MAC cambia a ogni tratto ma l'IP di destinazione resta quello finale?

### Riferimenti utili

- [RFC 791 - Internet Protocol](https://www.rfc-editor.org/rfc/rfc791)
- [RFC 950 - Internet Standard Subnetting Procedure](https://www.rfc-editor.org/rfc/rfc950)
- [Wikipedia italiana - Indirizzo IP](https://it.wikipedia.org/wiki/Indirizzo_IP)
