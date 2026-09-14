# 4DI - Settimana 4

> Riferimento: [4DI - SETT-OTT](4DI%20-%20SETT-OTT.md). Questa settimana trasforma il subnetting da intuizione a procedura ripetibile: dato un blocco e un numero di sottoreti, si calcolano prefisso, maschera, reti, host e broadcast, poi si verifica tutto in Packet Tracer.

# 🗺️ SETTIMANA 4: SUBNETTING FLSM AVANZATO E CIDR

```text
SETTIMANA 4
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] Il metodo completo per risolvere un esercizio FLSM
│   ├── [1.2] Potenze di 2, prefissi e maschere
│   ├── [1.3] Calcolo di rete, host e broadcast
│   └── [1.4] CIDR: dal mondo delle classi ai prefissi
│
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] Progettare una rete multi-subnet
│   ├── [2.2] Configurare router, switch e PC
│   ├── [2.3] Verificare con ping e comandi show
│   └── [2.4] Diagnosi di tre errori intenzionali
│
└── 📋 GUIDA DI REGIA PER IL DOCENTE
	├── Scaletta minuto per minuto
	├── Schema procedurale alla lavagna
	└── Esercizi graduati e domande di intuizione
```

## 🎯 Obiettivi della settimana

Alla fine della settimana dovresti saper:

- calcolare quanti bit prendere dalla parte host per ottenere un certo numero di sottoreti;
- ricavare il nuovo prefisso e la subnet mask decimale;
- elencare tutte le sottoreti di un blocco con il metodo del passo;
- trovare primo host, ultimo host e broadcast senza procedere per tentativi;
- spiegare che cosa cambia tra indirizzamento classful e CIDR;
- realizzare e verificare una rete con piu' sottoreti in Packet Tracer.

---

## 🧠 MODULO TEORICO (2 ORE IN AULA)

### [1.1] Il metodo completo per un esercizio FLSM

In un esercizio FLSM tutte le sottoreti hanno la stessa maschera. Il procedimento e' sempre lo stesso; la difficolta' consiste nel non saltare passaggi.

#### Procedura in sette passi

1. **Leggi il blocco di partenza**, per esempio `192.168.40.0/24`.
2. **Conta le sottoreti richieste**, per esempio 6.
3. **Trova i bit da prendere**: serve il minimo $n$ per cui $2^n$ sia almeno il numero di subnet. Per 6, $n=3$ perche' $2^2=4$ non basta e $2^3=8$ basta.
4. **Somma i bit al prefisso**: `/24 + 3 = /27`.
5. **Calcola gli host rimanenti**: $32 - 27 = 5$ bit, quindi $2^5 - 2 = 30$ host assegnabili per subnet.
6. **Calcola il passo** a partire dall'ottetto interessato: con `/27`, la maschera e' `255.255.255.224`, quindi passo `256 - 224 = 32`.
7. **Scrivi la tabella** di rete, host validi e broadcast.

Anche se servono solo 6 sottoreti, FLSM ne produce 8: le due eccedenti possono restare inutilizzate o essere riservate per crescita futura.

### [1.2] Potenze di 2, prefissi e maschere

| Bit presi | Sottoreti ottenibili | Bit host rimasti in una `/24` | Host assegnabili per subnet |
|---:|---:|---:|---:|
| 1 | 2 | 7 | 126 |
| 2 | 4 | 6 | 62 |
| 3 | 8 | 5 | 30 |
| 4 | 16 | 4 | 14 |
| 5 | 32 | 3 | 6 |
| 6 | 64 | 2 | 2 |
| 7 | 128 | 1 | 0, non utile per una LAN tradizionale |

Formula generale:

$$\text{sottoreti} = 2^{b}$$

$$\text{host assegnabili} = 2^{h} - 2$$

Il `-2` esclude l'indirizzo di rete e il broadcast. Per collegamenti punto-punto moderni esistono eccezioni e prefissi come `/31`, ma non sono il caso didattico di questa settimana.

#### Tabella rapida dell'ultimo ottetto

| Prefisso | Maschera | Passo | Host assegnabili |
|---:|---|---:|---:|
| `/25` | `255.255.255.128` | 128 | 126 |
| `/26` | `255.255.255.192` | 64 | 62 |
| `/27` | `255.255.255.224` | 32 | 30 |
| `/28` | `255.255.255.240` | 16 | 14 |
| `/29` | `255.255.255.248` | 8 | 6 |
| `/30` | `255.255.255.252` | 4 | 2 |

### [1.3] Calcolo di rete, host e broadcast

Esempio: `192.168.40.173/27`.

1. `/27` significa maschera `255.255.255.224`.
2. Il passo e' `32`.
3. I confini sono `.0`, `.32`, `.64`, `.96`, `.128`, `.160`, `.192`, `.224`.
4. `173` cade nel blocco `160-191`.
5. Network: `192.168.40.160`.
6. Primo host: `192.168.40.161`.
7. Ultimo host: `192.168.40.190`.
8. Broadcast: `192.168.40.191`.

```text
192.168.40.160/27
├── network:   192.168.40.160
├── host:      192.168.40.161 - 192.168.40.190
└── broadcast: 192.168.40.191
```

#### Perche' il broadcast e' il numero prima del blocco successivo?

La parte host e' tutta a 1. In una `/27` restano 5 bit host: `11111` vale 31. Se la rete parte da 160, `160 + 31 = 191`. Il blocco successivo parte da 192, quindi il broadcast e' sempre il valore immediatamente precedente.

### [1.4] CIDR: dal mondo delle classi ai prefissi

Il metodo classful divideva le reti in A, B e C con confini rigidi: una classe C aveva sempre `/24`, anche quando un'organizzazione aveva bisogno di soli 10 indirizzi. Il **CIDR (Classless Inter-Domain Routing)**, descritto in [RFC 4632](https://www.rfc-editor.org/rfc/rfc4632), usa invece un prefisso esplicito.

```text
Classful: 192.168.40.0  -> implicitamente classe C -> /24
CIDR:     192.168.40.0/27 -> il confine e' dichiarato esplicitamente
```

Il prefisso `/27` dice che i primi 27 bit sono rete e i rimanenti 5 sono host. Non dobbiamo piu' indovinare il confine dalla prima cifra dell'indirizzo.

#### Aggregazione e riepilogo

CIDR permette anche di aggregare reti contigue. Quattro reti `/24` consecutive possono essere rappresentate, quando l'allineamento lo consente, con un prefisso piu' corto:

```text
192.168.0.0/24
192.168.1.0/24  ──► 192.168.0.0/22
192.168.2.0/24
192.168.3.0/24
```

Questo riduce le righe nelle tabelle di routing. E' uno dei motivi per cui Internet non memorizza una regola separata per ogni singolo host.

#### Un pezzo di cultura della rete

Il CIDR e' un esempio di una scelta poco appariscente ma decisiva: invece di aumentare subito la potenza delle macchine, si migliora il modo di descrivere il problema. Una tabella di routing piu' compatta significa meno memoria occupata, ricerche piu' rapide e amministrazione piu' sostenibile. Nelle reti, l'eleganza spesso assomiglia a una tabella piu' corta.

---

## 💻 MODULO LABORATORIO (2 ORE CON ITP)

### [2.1] Progettare una rete multi-subnet

Progettare quattro LAN a partire da `192.168.50.0/24`, una per ogni laboratorio. FLSM richiede quattro sottoreti uguali:

- 4 subnet -> 2 bit presi;
- nuovo prefisso `/26`;
- maschera `255.255.255.192`;
- 62 host assegnabili per subnet.

| LAN | Network | Gateway | Host suggeriti | Broadcast |
|---|---|---|---|---|
| Laboratorio A | `192.168.50.0/26` | `192.168.50.1` | `.10`, `.11` | `.63` |
| Laboratorio B | `192.168.50.64/26` | `192.168.50.65` | `.70`, `.71` | `.127` |
| Laboratorio C | `192.168.50.128/26` | `192.168.50.129` | `.140`, `.141` | `.191` |
| Laboratorio D | `192.168.50.192/26` | `192.168.50.193` | `.200`, `.201` | `.255` |

### [2.2] Topologia Packet Tracer

Per mantenere l'attivita' gestibile, usare un router con quattro interfacce oppure un router-on-a-stick solo se la classe ha gia' affrontato VLAN. In questa prima versione, ogni LAN e' collegata a una porta diversa del router:

```text
PC-A1 ─ Switch-A ─ G0/0  R1  G0/1 ─ Switch-B ─ PC-B1
PC-A2 ────────────────┘       └─────────────── PC-B2

						 G0/2 ─ Switch-C ─ PC-C1
						 G0/3 ─ Switch-D ─ PC-D1
```

Configurare le interfacce di R1:

```text
R1> enable
R1# configure terminal
R1(config)# hostname R1
R1(config)# interface g0/0
R1(config-if)# description LAB_A
R1(config-if)# ip address 192.168.50.1 255.255.255.192
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# interface g0/1
R1(config-if)# description LAB_B
R1(config-if)# ip address 192.168.50.65 255.255.255.192
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# interface g0/2
R1(config-if)# description LAB_C
R1(config-if)# ip address 192.168.50.129 255.255.255.192
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# interface g0/3
R1(config-if)# description LAB_D
R1(config-if)# ip address 192.168.50.193 255.255.255.192
R1(config-if)# no shutdown
R1(config-if)# end
R1# copy running-config startup-config
```

Configurare, per esempio, PC-A1 con IP `192.168.50.10`, maschera `255.255.255.192` e gateway `192.168.50.1`; PC-B1 con `192.168.50.70`, stessa maschera e gateway `192.168.50.65`.

### [2.3] Verificare la connettivita'

Eseguire in quest'ordine:

1. ping dal PC al proprio gateway;
2. ping tra due PC della stessa LAN;
3. ping tra PC di LAN diverse;
4. `ipconfig` sul PC per controllare i dati inseriti;
5. `show ip interface brief` sul router;
6. `show ip route connected` per leggere le reti direttamente connesse.

Il router conosce automaticamente le quattro reti perche' sono direttamente collegate alle sue interfacce. Non serve ancora una rotta statica tra loro.

### [2.4] Tre errori intenzionali da diagnosticare

Preparare tre copie della topologia o introdurre un errore alla volta:

| Errore | Sintomo | Indizio da cercare |
|---|---|---|
| PC-B1 ha gateway `192.168.50.1` | ping locale possibile, ping esterno fallisce | gateway non appartiene alla sua subnet |
| G0/2 senza `no shutdown` | tutti i PC della LAN C sono isolati | `administratively down` |
| PC-D1 ha IP `192.168.50.190` | PC-D1 finisce nella LAN C | indirizzo e gateway non condividono il NetID |

L'obiettivo non e' correggere a tentativi, ma scrivere prima una **ipotesi**, poi un comando o una prova che possa confermarla.

#### Consegna di laboratorio

Consegnare:

- la tabella delle quattro subnet;
- uno screenshot di `show ip interface brief`;
- la configurazione IP di un PC per ogni LAN;
- una tabella dei ping con esito atteso e osservato;
- la diagnosi di uno dei tre errori intenzionali.

---

## 🧩 ESERCIZI GUIDATI

### Esercizio 1 - Quattro subnet da una `/24`

Dividere `10.10.0.0/24` in 4 sottoreti. Calcolare prefisso, maschera, passo, network e broadcast di ogni blocco.

**Soluzione da costruire insieme:** `/26`, `255.255.255.192`, passo 64; reti `.0`, `.64`, `.128`, `.192`.

### Esercizio 2 - Otto subnet da una `/24`

Dividere `172.20.5.0/24` in 8 sottoreti. Per la quinta subnet indicare primo e ultimo host.

**Soluzione:** `/27`, passo 32; quinta rete `.128`, host `.129-.158`, broadcast `.159`.

### Esercizio 3 - Partenza non allineata a zero

Per `192.168.12.214/28`, trovare network, broadcast e intervallo host.

**Soluzione:** passo 16; il blocco e' `208-223`; network `192.168.12.208`, host `.209-.222`, broadcast `.223`.

### Esercizio 4 - Ragionare al contrario

Una sottorete deve contenere almeno 50 host assegnabili. Qual e' il prefisso piu' specifico possibile?

**Soluzione:** servono 6 bit host perche' $2^5-2=30$ non basta e $2^6-2=62$ basta; il prefisso e' `/26`.

### Domande di ripasso e intuizione

1. Perche' una `/27` produce 8 blocchi quando si parte da una `/24`?
2. Due host con IP in sottoreti diverse possono comunicare senza router? Motiva a livello di rete.
3. Perche' il gateway della LAN B dell'esempio non puo' essere `192.168.50.1`?
4. In CIDR, che differenza c'e' tra `192.168.50.0/24` e `192.168.50.0/26`?
5. **Intuizione:** se il numero di host richiesti raddoppia, che cosa accade al numero di bit host e al prefisso?
6. **Intuizione:** perche' una subnet inutilizzata non e' necessariamente spazio sprecato? Pensa alla crescita di una scuola o di un'azienda.
7. Un PC ha IP corretto e ping verso il gateway riuscito, ma non raggiunge un'altra subnet: quale informazione controlleresti subito dopo?

---

## 📋 GUIDA DI REGIA PER IL DOCENTE

### Scaletta della teoria (110 minuti)

- **00-10:** quiz orale sui risultati della Settimana 3: `/26`, network, broadcast e host.
- **10-30:** problema-guida: “sei laboratori, una rete `/24`, quante sottoreti?”
- **30-50:** potenze di 2 e tabella rapida delle maschere.
- **50-75:** algoritmo dei sette passi su `192.168.40.173/27`.
- **75-92:** esercizio al contrario: dato il numero di host, trovare il prefisso.
- **92-105:** CIDR, differenza con le classi storiche e aggregazione.
- **105-110:** exit ticket: ogni studente scrive rete e broadcast dell'IP assegnato.

### Procedura da lasciare alla lavagna

```text
1. subnet richieste -> bit da prendere
2. prefisso nuovo
3. bit host rimasti -> 2^h - 2
4. maschera decimale
5. passo = 256 - ottetto maschera
6. elenco dei confini
7. network | host | broadcast
```

### Criteri di osservazione formativa

- **Procedura:** lo studente segue i passaggi senza saltare direttamente al risultato.
- **Precisione:** network e broadcast non vengono assegnati agli host.
- **Linguaggio:** usa correttamente prefisso, maschera, gateway e subnet.
- **Diagnosi:** prima osserva un comando o un ping, poi formula una correzione.

### Riferimenti utili

- [RFC 4632 - Classless Inter-Domain Routing](https://www.rfc-editor.org/rfc/rfc4632)
- [Cisco - Subnetting overview](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [IANA - IPv4 Special-Purpose Address Registry](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml)
- [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer)

---

## 🧮 PROCEDURA COMPLETA SU UN CASO NUOVO

Progettiamo una rete per 5 laboratori partendo da `172.16.8.0/24`. FLSM deve creare almeno 5 sottoreti uguali.

### Passo 1: arrotondare con le potenze di 2

`2^2 = 4` non basta; `2^3 = 8` basta. Prendiamo quindi 3 bit dalla parte host.

```text
Prefisso iniziale: /24
Bit presi:          3
Prefisso nuovo:    /27
```

Restano 5 bit host, quindi ogni subnet ha 30 host assegnabili. Otteniamo 8 blocchi: ne usiamo 5 e ne riserviamo 3 per crescita futura.

### Passo 2: costruire la tabella senza saltare righe

`/27` equivale a `255.255.255.224`; il passo e' `256 - 224 = 32`.

| Subnet | Network | Primo host | Ultimo host | Broadcast | Uso |
|---:|---|---|---|---|---|
| 1 | `172.16.8.0/27` | `.1` | `.30` | `.31` | Lab 1 |
| 2 | `172.16.8.32/27` | `.33` | `.62` | `.63` | Lab 2 |
| 3 | `172.16.8.64/27` | `.65` | `.94` | `.95` | Lab 3 |
| 4 | `172.16.8.96/27` | `.97` | `.126` | `.127` | Lab 4 |
| 5 | `172.16.8.128/27` | `.129` | `.158` | `.159` | Lab 5 |
| 6 | `172.16.8.160/27` | `.161` | `.190` | `.191` | riserva |
| 7 | `172.16.8.192/27` | `.193` | `.222` | `.223` | riserva |
| 8 | `172.16.8.224/27` | `.225` | `.254` | `.255` | riserva |

### Controllo inverso

Un buon tecnico non si fida di un solo calcolo. Per la subnet 4, `172.16.8.110/27` deve risultare nella rete `172.16.8.96/27`, perche' 110 e' compreso tra 96 e 127. Il broadcast e' 127, il blocco seguente parte da 128.

## 🧭 CIDR E AGGREGAZIONE: QUANDO IL PREFISSO DEVE ESSERE ALLINEATO

L'esempio `192.168.0.0/22` rappresenta quattro reti `/24` da `.0` a `.3`. Non basta pero' sommare quattro reti qualsiasi: per aggregare correttamente bisogna partire da un confine compatibile con il nuovo prefisso. Quattro `/24` a partire da `192.168.1.0` non possono essere riassunte semplicemente come `192.168.1.0/22`, perche' `/22` ha blocchi allineati su multipli di 4 nel terzo ottetto.

```text
/22 nel terzo ottetto: 0-3, 4-7, 8-11, ...
192.168.0.0/22  -> valido
192.168.4.0/22  -> valido
192.168.1.0/22  -> non e' un confine di rete /22
```

Questa e' una buona occasione per mostrare che una notazione breve non e' una scorciatoia arbitraria: descrive bit precisi e confini precisi.

## 🧪 LABORATORIO: PROGETTARE, CONFIGURARE, DIMOSTRARE

Per ogni LAN della topologia, lo studente deve consegnare quattro evidenze:

1. calcolo scritto della subnet e del broadcast;
2. configurazione del gateway sull'interfaccia del router;
3. `show ip interface brief` con stato `up/up`;
4. ping dal PC al gateway e verso un PC di un'altra subnet.

Quando un test fallisce, compilare questa scheda:

| Domanda | Osservazione |
|---|---|
| Il cavo e' attivo? | colore del link / stato interfaccia |
| Il PC appartiene alla subnet corretta? | IP, maschera, gateway |
| Il gateway risponde? | ping locale |
| Il router conosce la rete? | `show ip route connected` |
| Il secondo host e' configurato? | indirizzo e maschera |

### Esercizi di intuizione

1. Perche' una `/27` offre piu' subnet ma meno host per subnet rispetto a una `/26`?
2. Se servono 17 host, quale prefisso scegli tra `/27` e `/28`? Motiva con la formula.
3. Un IP appartiene alla rete `10.0.4.64/28` e ha broadcast `.79`. Quali sono gli host validi?
4. **Intuizione:** perche' riservare subnet non ancora usate puo' semplificare la crescita di una rete?
5. **Intuizione:** una rete con pochi host ma molti reparti trarrebbe piu' vantaggio da FLSM o VLSM? Anticipa la risposta e collegala alla settimana successiva.

### Riferimenti in italiano

- [Wikipedia italiana - CIDR](https://it.wikipedia.org/wiki/Classless_Inter-Domain_Routing)
- [Wikipedia italiana - Subnet mask](https://it.wikipedia.org/wiki/Subnet_mask)
- [Cisco - IPv4 addressing](https://www.cisco.com/c/it_it/support/docs/ip/routing-information-protocol-rip/13788-3.html)
