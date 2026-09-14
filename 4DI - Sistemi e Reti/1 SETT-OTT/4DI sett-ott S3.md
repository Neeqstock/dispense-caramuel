# 4DI - Settimana 3

> Riferimento: [4DI - SETT-OTT](4DI%20-%20SETT-OTT.md). Questa settimana introduce il problema pratico che il subnetting risolve: come organizzare una rete senza sprecare indirizzi e senza confondere rete, host e collegamento verso l'esterno.

# 🗺️ SETTIMANA 3: INDIRIZZI PUBBLICI, PRIVATI E PRIMO SUBNETTING FLSM

```text
SETTIMANA 3
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] Perché gli indirizzi IPv4 non bastano
│   ├── [1.2] Indirizzi pubblici, privati e RFC 1918
│   ├── [1.3] NAT: la frontiera tra rete locale e Internet
│   └── [1.4] Introduzione al subnetting FLSM e all'AND bit a bit
│
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] Collegare PC, switch e router
│   ├── [2.2] Configurare le interfacce Cisco
│   ├── [2.3] Leggere lo stato con i comandi show
│   └── [2.4] Esercitazione: una LAN con gateway funzionante
│
└── 📋 GUIDA DI REGIA PER IL DOCENTE
	├── Scaletta minuto per minuto
	├── Schema da disegnare alla lavagna
	└── Domande, errori tipici e compito breve
```

## 🎯 Obiettivi della settimana

Alla fine della settimana dovresti saper:

- distinguere un indirizzo pubblico da uno privato;
- elencare le tre famiglie di reti private definite da RFC 1918;
- spiegare perché il NAT e' diventato necessario, senza confonderlo con una misura di sicurezza completa;
- riconoscere rete, host, gateway e broadcast in una rete semplice;
- applicare una subnet mask con un AND bit a bit per ricavare il NetID;
- configurare un indirizzo su un'interfaccia router e verificare lo stato con `show ip interface brief`.

---

## 🧠 MODULO TEORICO (2 ORE IN AULA)

### [1.1] Perché gli indirizzi IPv4 non bastano

Un indirizzo IPv4 contiene 32 bit. Le combinazioni possibili sono:

$$2^{32} = 4.294.967.296$$

Sembra un numero enorme, ma non tutti gli indirizzi sono assegnabili a host, e Internet connette ormai miliardi di dispositivi. Inoltre ogni rete ha bisogno di indirizzi per identificare la rete stessa, il broadcast e spesso apparati, server e infrastrutture.

Il problema non e' soltanto quantitativo. Un indirizzo deve anche essere **organizzato**: un router deve poter capire rapidamente a quale rete appartiene una destinazione. Per questo un IPv4 non e' un numero civico isolato: e' formato da una parte di rete e da una parte di host, separate dalla subnet mask.

#### Un piccolo percorso storico

Quando Internet era ancora una rete di ricerca, assegnare grandi blocchi di indirizzi sembrava ragionevole. Con la diffusione di universita', aziende, modem e poi smartphone, la richiesta e' cresciuta molto piu' rapidamente delle previsioni. La risposta non e' stata una singola invenzione, ma una combinazione di idee:

1. classi e poi CIDR per assegnare blocchi in modo piu' ordinato;
2. indirizzi privati per le reti interne;
3. NAT per far uscire molte reti private usando pochi indirizzi pubblici;
4. IPv6, che amplia enormemente lo spazio degli indirizzi.

**Domanda guida:** se un'azienda ha 500 computer ma solo un indirizzo pubblico, come puo' collegarli tutti a Internet senza dare a ciascuno un IPv4 pubblico?

### [1.2] Indirizzi pubblici, privati e RFC 1918

Un **indirizzo pubblico** e' instradabile su Internet globale e deve essere assegnato in modo coordinato. Un **indirizzo privato** e' destinato alle reti interne: puo' essere riutilizzato in scuole, case e aziende diverse perche' non viene instradato direttamente su Internet.

Le tre famiglie private definite da [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) sono:

| Blocco | Prefisso | Intervallo | Uso tipico |
|---|---:|---|---|
| `10.0.0.0/8` | 8 | `10.0.0.0` - `10.255.255.255` | reti aziendali grandi |
| `172.16.0.0/12` | 12 | `172.16.0.0` - `172.31.255.255` | reti medie e segmentate |
| `192.168.0.0/16` | 16 | `192.168.0.0` - `192.168.255.255` | reti domestiche e piccoli laboratori |

Il prefisso `/8`, `/12` o `/16` indica quanti bit iniziali appartengono alla rete. La maschera equivalente e':

| Prefisso | Maschera decimale |
|---:|---|
| `/8` | `255.0.0.0` |
| `/12` | `255.240.0.0` |
| `/16` | `255.255.0.0` |

#### Attenzione a una distinzione importante

Privato non significa automaticamente sicuro. Un PC con IP privato non e' raggiungibile direttamente da Internet nello stesso modo di un host pubblico, ma puo' comunque essere vulnerabile da un dispositivo gia' presente nella LAN, da un port forwarding errato o da un malware. Il NAT nasconde indirizzi; non sostituisce firewall, autenticazione, aggiornamenti e segmentazione.

### [1.3] NAT: la frontiera tra rete locale e Internet

Il **NAT (Network Address Translation)** modifica gli indirizzi presenti nei pacchetti quando attraversano il router. Nel caso piu' comune, molti host privati condividono un indirizzo pubblico usando anche le porte: questa variante e' spesso chiamata **PAT (Port Address Translation)** o NAT overload.

```text
LAN privata                         Router/NAT             Internet
192.168.1.10:51500 ───────────────► 203.0.113.8:40001 ───► server web
192.168.1.11:51501 ───────────────► 203.0.113.8:40002 ───► server web
```

Il router mantiene una tabella di traduzione. Quando arrivano le risposte, usa la coppia indirizzo/porta per capire a quale host interno consegnarle.

| Prima del NAT | Dopo il NAT |
|---|---|
| sorgente `192.168.1.10:51500` | sorgente `203.0.113.8:40001` |
| destinazione `198.51.100.20:443` | destinazione `198.51.100.20:443` |

Gli intervalli `203.0.113.0/24` e `198.51.100.0/24` sono riservati alla documentazione e agli esempi, quindi non rappresentano indirizzi pubblici reali da configurare su Internet.

#### Un aneddoto dalla comunita' di rete

Molti problemi domestici descritti come “Internet non va” sono in realta' problemi di confine: il Wi-Fi funziona, il PC ha un IP privato, ma il gateway non risponde o il NAT non ha una traduzione valida. La prima diagnosi utile non e' riavviare tutto a caso: e' chiedersi **fino a quale confine arriva il traffico**. La mentalita' da tecnico nasce proprio da questa domanda.

### [1.4] Introduzione al subnetting FLSM

Il **subnetting** divide una rete piu' grande in sottoreti piu' piccole. In **FLSM (Fixed Length Subnet Masking)** tutte le sottoreti usano la stessa maschera e hanno quindi la stessa dimensione.

Esempio: da `192.168.10.0/24` vogliamo ottenere 4 sottoreti uguali.

1. 4 sottoreti richiedono $2^2 = 4$: prendiamo 2 bit dalla parte host.
2. Il prefisso passa da `/24` a `/26`.
3. Restano $32 - 26 = 6$ bit host.
4. Ogni sottorete contiene $2^6 = 64$ indirizzi, di cui 62 host normalmente assegnabili.

```text
/24: 11111111.11111111.11111111.00000000
/26: 11111111.11111111.11111111.11000000
									  ^^ bit presi per le subnet
```

| Sottorete | Network | Host validi | Broadcast |
|---:|---|---|---|
| 1 | `192.168.10.0/26` | `.1` - `.62` | `.63` |
| 2 | `192.168.10.64/26` | `.65` - `.126` | `.127` |
| 3 | `192.168.10.128/26` | `.129` - `.190` | `.191` |
| 4 | `192.168.10.192/26` | `.193` - `.254` | `.255` |

La regola rapida e' il **passo**:

$$256 - 192 = 64$$

Poiche' `255.255.255.192` e' la maschera `/26`, le reti iniziano ogni 64 nel quarto ottetto.

#### Ricavare il NetID con l'AND

Per ottenere l'indirizzo di rete si esegue un AND bit a bit tra IP e maschera:

```text
IP:       192.168.10.77  = 11000000.10101000.00001010.01001101
Maschera: 255.255.255.192= 11111111.11111111.11111111.11000000
AND:      192.168.10.64  = 11000000.10101000.00001010.01000000
```

Regola dell'AND: `1 AND 1 = 1`; in tutti gli altri casi il risultato e' `0`.

---

## 💻 MODULO LABORATORIO (2 ORE CON ITP)

### [2.1] Topologia e piano di indirizzamento

Costruire in Packet Tracer:

```text
PC-A ─────┐
		  ├── Switch0 ─── Router0 G0/0
PC-B ─────┘
```

Usare la rete `192.168.10.0/24` senza ancora fare subnetting operativo:

| Dispositivo | Interfaccia | IP | Maschera | Gateway |
|---|---|---|---|---|
| Router0 | G0/0 | `192.168.10.1` | `255.255.255.0` | - |
| PC-A | FastEthernet0 | `192.168.10.10` | `255.255.255.0` | `192.168.10.1` |
| PC-B | FastEthernet0 | `192.168.10.11` | `255.255.255.0` | `192.168.10.1` |

### [2.2] Configurare l'interfaccia del router

```text
Router> enable
Router# configure terminal
Router(config)# hostname R1
R1(config)# interface gigabitEthernet 0/0
R1(config-if)# ip address 192.168.10.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# description LAN_4DI
R1(config-if)# end
R1# copy running-config startup-config
```

`no shutdown` e' fondamentale: un'interfaccia puo' avere un indirizzo corretto ma restare amministrativamente disattivata. Il comando `copy running-config startup-config` salva la configurazione nella memoria di avvio; senza questo passaggio la configurazione puo' sparire al riavvio.

### [2.3] Leggere lo stato con i comandi `show`

```text
R1# show ip interface brief
R1# show running-config
R1# show interfaces gigabitEthernet 0/0
R1# show arp
```

Interpretare almeno questi stati:

| Stato | Significato probabile |
|---|---|
| `up/up` | interfaccia attiva e collegamento fisico presente |
| `administratively down/down` | manca `no shutdown` |
| `down/down` | cavo, porta o dispositivo dall'altra parte non attivo |
| `up/down` | livello fisico presente, ma problema di protocollo/configurazione |

### [2.4] Esercitazione guidata: dal piano al ping

1. Posizionare due PC, uno switch e un router.
2. Collegare i dispositivi con i cavi corretti.
3. Configurare IP, maschera e gateway sui due PC.
4. Configurare l'interfaccia del router e attivarla.
5. Da PC-A eseguire `ping 192.168.10.11` e poi `ping 192.168.10.1`.
6. Spegnere l'interfaccia con `shutdown`, ripetere il ping e osservare il fallimento.
7. Riattivare con `no shutdown` e verificare nuovamente.
8. Cambiare per errore la maschera di PC-B in `255.255.0.0`: discutere perché il problema puo' essere difficile da notare in una rete semplice.

#### Consegna

Consegnare una tabella con IP, maschera e gateway di ogni dispositivo, uno screenshot di `show ip interface brief` e una breve diagnosi di un ping fallito.

---

## 🧩 DOMANDE DI RIPASSO E INTUIZIONE

1. Perche' due case diverse possono usare entrambe `192.168.1.10` senza conflitto diretto?
2. Un indirizzo privato puo' essere raggiunto da Internet? In quali condizioni un dispositivo interno potrebbe essere esposto?
3. Quanti host assegnabili offre normalmente una `/26`? Perche' non si usano network e broadcast?
4. Qual e' il NetID di `192.168.10.201/26`? Qual e' il broadcast?
5. Se tutti i PC della LAN fanno ping tra loro ma nessuno raggiunge un sito, quale confine controlleresti per primo: switch, router o DNS? Motiva.
6. **Intuizione:** se una rete `/24` viene divisa in 8 sottoreti uguali, quanti bit vengono presi dalla parte host e quale sara' il nuovo prefisso?
7. **Intuizione:** perché un router deve conoscere la maschera oltre all'indirizzo IP? Prova a descrivere un caso in cui lo stesso IP produce un NetID diverso con due maschere diverse.

### Mini-esercizi svolti insieme

Per `172.16.40.130/26` calcolare:

- maschera decimale: `255.255.255.192`;
- passo: `64`;
- rete: `172.16.40.128`;
- primo host: `172.16.40.129`;
- ultimo host: `172.16.40.190`;
- broadcast: `172.16.40.191`.

Per casa, svolgere lo stesso procedimento per `10.20.7.66/27` e `192.168.50.199/28`.

---

## 📋 GUIDA DI REGIA PER IL DOCENTE

### Scaletta della teoria (110 minuti)

- **00-10:** recupero attivo: IP, maschera, gateway e differenza tra switch/router.
- **10-25:** il problema storico dello spazio IPv4; raccogliere ipotesi degli studenti.
- **25-45:** RFC 1918 e tabella degli intervalli privati.
- **45-60:** NAT/PAT con due PC e una tabella di traduzione disegnata alla lavagna.
- **60-85:** FLSM da `/24` a `/26`; costruire la tabella delle quattro sottoreti.
- **85-102:** AND bit a bit su un esempio scelto dalla classe.
- **102-110:** exit ticket con tre domande: privato/pubblico, NetID, significato di `no shutdown`.

### Schema alla lavagna

```text
IP = rete + host
mask = decide il confine
AND(IP, mask) = rete

192.168.10.77/26
rete .64 | host .65-.126 | broadcast .127

LAN privata -- NAT/PAT -- IP pubblico -- Internet
```

### Errori tipici da rendere visibili

- confondere `192.168.x.x` con “indirizzo sempre sicuro”;
- considerare il gateway come DNS;
- usare il primo o l'ultimo indirizzo di una subnet come host normale;
- dimenticare `no shutdown`;
- contare 64 host in una `/26` invece di 62 host assegnabili;
- calcolare il broadcast come “ultimo numero possibile” senza prima individuare il passo.

### Riferimenti utili

- [RFC 1918 - Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918)
- [RFC 4632 - CIDR](https://www.rfc-editor.org/rfc/rfc4632)
- [Cisco - IP addressing and subnetting](https://www.cisco.com/c/en/us/support/docs/ip/routing-information-protocol-rip/13788-3.html)
- [IANA - IPv4 Special-Purpose Address Space](https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml)

---

## 🧮 UN ESEMPIO FLSM SVOLTO LENTAMENTE

Una scuola ha la rete `192.168.100.0/24` e vuole quattro reti uguali: docenti, studenti, laboratorio e ospiti.

### 1. Quante reti e quanti bit?

Servono 4 subnet. Poiche' $2^2=4$, prendiamo 2 bit dalla parte host. Il prefisso diventa `/26`.

### 2. Quanti indirizzi restano?

Con `/26` restano 6 bit host:

$$2^6 = 64\text{ indirizzi per subnet}$$

Normalmente 62 sono assegnabili: il primo identifica la rete e l'ultimo e' il broadcast.

### 3. Qual e' il passo?

La maschera `/26` e' `255.255.255.192`. Il passo e':

$$256 - 192 = 64$$

Quindi i confini sono `.0`, `.64`, `.128`, `.192`.

| Scopo | Rete | Gateway suggerito | Host utilizzabili | Broadcast |
|---|---|---|---|---|
| Docenti | `192.168.100.0/26` | `.1` | `.1-.62` | `.63` |
| Studenti | `192.168.100.64/26` | `.65` | `.65-.126` | `.127` |
| Laboratorio | `192.168.100.128/26` | `.129` | `.129-.190` | `.191` |
| Ospiti | `192.168.100.192/26` | `.193` | `.193-.254` | `.255` |

La scelta del primo host come gateway non e' una legge: e' una convenzione leggibile. L'importante e' documentarla e usarla in modo coerente.

### Perche' FLSM puo' sprecare indirizzi

Se la rete ospiti contiene solo 8 dispositivi, una `/26` le assegna 62 host possibili. FLSM e' semplice da calcolare e da insegnare, ma non ottimizza dimensioni diverse. La settimana 5 introdurra' VLSM proprio per assegnare blocchi piu' piccoli alle reti piccole.

### Dal numero decimale alla maschera

Il valore `192` dell'ultimo ottetto e':

```text
192 = 128 + 64
	= 11000000
```

Per `/26`, i primi 26 bit sono rete (`24 + 2`) e gli ultimi 6 sono host:

```text
11111111.11111111.11111111.11000000
```

Questo rende visibile il motivo per cui il passo e' 64: con 6 bit host, ogni blocco contiene 64 combinazioni.

## 🧪 MICRO-LAB: CAPISCI SE IL PROBLEMA E' LOCALE O DI GATEWAY

Usare la LAN `192.168.10.0/26`:

| Dispositivo | IP | Maschera | Gateway |
|---|---|---|---|
| R1 G0/0 | `192.168.10.1` | `255.255.255.192` | - |
| PC-A | `192.168.10.10` | `255.255.255.192` | `.1` |
| PC-B | `192.168.10.11` | `255.255.255.192` | `.1` |

Eseguire:

1. `ping 192.168.10.1` da PC-A: verifica il gateway.
2. `ping 192.168.10.11` da PC-A: verifica l'altro host.
3. Su R1 eseguire `show ip interface brief`.
4. Usare `shutdown` su G0/0 e ripetere i test.
5. Riattivare con `no shutdown`.

La sequenza insegna una regola diagnostica: provare prima il vicino, poi il gateway, poi la destinazione remota. Un test alla volta riduce il numero di ipotesi.

### Domande di comprensione

1. Perche' `192.168.10.63` non e' un host ordinario nella prima subnet `/26`?
2. Quale indirizzo useresti come gateway della terza subnet e perche'?
3. Se il ping tra PC-A e PC-B funziona ma il ping al gateway fallisce, quale configurazione controlleresti?
4. **Intuizione:** una scuola aggiunge 70 dispositivi alla rete studenti. Perche' la progettazione FLSM attuale potrebbe non bastare?
5. **Intuizione:** se due classi usano entrambe `192.168.10.0/26`, quando questo e' innocuo e quando diventa un problema?
