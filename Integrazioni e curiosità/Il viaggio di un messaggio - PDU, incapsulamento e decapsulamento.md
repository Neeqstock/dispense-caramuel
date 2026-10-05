# Il viaggio di un messaggio: PDU, incapsulamento e decapsulamento

> Quando inviamo un messaggio, il computer non spedisce semplicemente "del testo". Lo prepara in piu' buste, una dentro l'altra. Ogni busta aggiunge una piccola informazione indispensabile al suo pezzo di viaggio.

Questa dispensa segue un messaggio da un computer a un altro per capire tre idee:

- che cosa sono le **PDU**;
- che cosa significa **incapsulare**;
- che cosa significa **decapsulare**.

Non occorre imparare ogni campo di ogni protocollo. L'obiettivo e' capire chi aggiunge che cosa, chi la legge e perche' quella informazione serve.

---

## 1. Prima idea: una rete divide il lavoro

Immaginiamo di voler consegnare una lettera a una persona che vive in un'altra citta'. Per riuscirci servono informazioni diverse:

- il testo della lettera;
- il nome del destinatario;
- il suo indirizzo;
- l'ufficio o il mezzo che la portera' nel primo tratto;
- il modo fisico con cui viaggia: strada, treno, aereo.

Una sola informazione non basta a tutte le persone coinvolte. Il postino del quartiere non deve leggere la lettera; gli basta sapere dove consegnare nel suo tratto. Allo stesso modo, in una rete ogni livello riceve una responsabilita' precisa.

```text
TCP/IP

Applicazione     Che cosa vogliono comunicare i programmi?
Trasporto        A quale programma deve arrivare il messaggio?
Internet/ Accesso alla rete         In quale rete e verso quale computer deve andare?
Fisico           Come trasformo i bit in segnali?
```

Questi livelli non sono persone dentro il computer: sono un modo per organizzare protocolli e responsabilita'. Un livello usa il servizio di quello sottostante senza dover conoscere tutti i suoi dettagli.

## 2. Che cos'e' una PDU?

PDU significa **Protocol Data Unit**, cioe' *unita' di dati di un protocollo*. E' il nome del "pacchetto di lavoro" visto da un certo livello.

Lo stesso contenuto cambia nome mentre scende nella pila, perche' ogni livello aggiunge informazioni diverse.

| Livello TCP/IP    | PDU                           | In parole semplici                                         |
| ----------------- | ----------------------------- | ---------------------------------------------------------- |
| Applicazione      | dati                          | il messaggio che interessa al programma                    |
| Trasporto         | segmento TCP o datagramma UDP | dati piu' informazioni per consegnarli al programma giusto |
| Internet          | pacchetto IP                  | dati piu' indirizzo IP sorgente e destinazione             |
| Accesso alla rete | frame Ethernet o Wi-Fi        | dati piu' indirizzi MAC per il tratto locale               |
| Fisico            | bit e segnali                 | zero e uno trasformati in elettricita', luce o onde radio  |

Nella vita quotidiana spesso chiamiamo tutto "pacchetto". Nello studio delle reti conviene invece usare il nome giusto: un **frame** riguarda un collegamento locale; un **pacchetto IP** puo' attraversare molte reti; un **segmento TCP** serve alla comunicazione fra programmi.

---

## 3. Incapsulare: mettere una busta dentro un'altra

**Incapsulamento** significa che, mentre i dati scendono nella pila TCP/IP, ogni livello li prende come contenuto e aggiunge la propria intestazione, detta *header*. Ethernet aggiunge anche una parte finale di controllo, detta *trailer*.

```text
Messaggio dell'applicazione
        |
        v
[ header TCP | messaggio ]                         = segmento TCP
        |
        v
[ header IP | header TCP | messaggio ]             = pacchetto IP
        |
        v
[ header Ethernet | pacchetto IP | FCS ]           = frame Ethernet
        |
        v
010011010101...                                     = segnali sul mezzo fisico
```

Ogni header risponde a una domanda diversa:

| Livello | Informazione aggiunta, semplificata | Domanda a cui risponde |
| --- | --- | --- |
| Trasporto | porte sorgente e destinazione | quale programma sta parlando con quale programma? |
| Internet | IP sorgente e IP destinazione | quale computer/rete e' la destinazione finale? |
| Accesso alla rete | MAC sorgente e MAC destinazione | quale dispositivo vicino riceve questo frame? |

Il messaggio originale non viene cancellato. Viene custodito nel contenitore del livello precedente, come una lettera in una busta, a sua volta dentro un pacco.

### Un dettaglio utile: header non significa segreto

L'header non e' necessariamente cifrato e non contiene il contenuto completo del messaggio. E' una specie di etichetta tecnica, con le informazioni che quel livello deve poter leggere. La cifratura, quando presente, dipende dai protocolli usati dall'applicazione, per esempio HTTPS/TLS.

---

## 4. Un esempio completo: "Ciao!" da Anna a Bruno

Anna invia il messaggio `Ciao!` dal suo computer al computer di Bruno. I due computer sono in reti diverse e in mezzo c'e' un router.

```text
Computer di Anna       Router             Computer di Bruno
192.168.1.10  ------  192.168.1.1
                              |
                         10.0.0.1  ------  10.0.0.20
                                           
```

Per semplificare immaginiamo che l'app di messaggistica usi TCP e che conosca gia' l'indirizzo IP di Bruno. In una rete reale possono comparire anche DNS e ARP: li lasciamo sullo sfondo per concentrarci sulle PDU.

### Passo 1: l'applicazione crea i dati

L'applicazione di Anna produce i dati:

```text
DATI
"Ciao!"
```

Per l'applicazione, cio' che conta e' il significato del messaggio. Non deve sapere se il primo tratto usera' un cavo, il Wi-Fi o una fibra lontana.

### Passo 2: TCP aggiunge le porte

Il livello di trasporto incapsula i dati in un segmento TCP. Aggiunge, fra le altre cose, una porta sorgente temporanea e una porta di destinazione. Le porte distinguono i programmi: sullo stesso computer possono comunicare contemporaneamente browser, chat, videogioco e posta.

```text
SEGMENTO TCP
[ porta sorgente: 51000 | porta destinazione: 4000 | "Ciao!" ]
```

`51000` e `4000` sono numeri inventati per l'esempio. Non sono indirizzi di computer: sono come interni di un centralino. L'IP porta alla macchina giusta; la porta porta al programma giusto su quella macchina.

### Passo 3: IP aggiunge gli indirizzi logici

Il livello Internet inserisce il segmento TCP dentro un pacchetto IP:

```text
PACCHETTO IP
[ IP sorgente: 192.168.1.10 | IP destinazione: 10.0.0.20 |
  segmento TCP ]
```

Ora il pacchetto contiene il vero obiettivo del viaggio: Bruno, `10.0.0.20`. Anna controlla la propria maschera e capisce che quell'indirizzo non e' nella sua rete `192.168.1.0/24`. Quindi consegnera' il primo frame al suo **gateway**, il router `192.168.1.1`.

### Passo 4: Ethernet prepara il primo tratto

Anna non puo' spedire direttamente sulla LAN un frame al MAC di Bruno: Bruno e' in un'altra rete. Il primo destinatario locale e' il router. Il livello di accesso alla rete crea quindi questo frame:

```text
FRAME SULLA RETE DI ANNA
[ MAC Anna | MAC del router, lato 192.168.1.1 |
  pacchetto IP: 192.168.1.10 -> 10.0.0.20 |
  FCS ]
```

L'indirizzo MAC e l'indirizzo IP non sono concorrenti:

- il **MAC** serve per la consegna sul tratto locale;
- l'**IP** serve per indicare il mittente e la destinazione fra reti.

Infine il frame diventa una sequenza di bit e attraversa il mezzo fisico: un cavo, il Wi-Fi o altro.

---

## 5. Il router: apre una busta e ne prepara un'altra

Il router riceve il frame destinato al proprio MAC. Controlla che il frame sia valido e rimuove l'involucro Ethernet. Questa prima parte e' **decapsulamento fino al livello IP**.

```text
FRAME RICEVUTO
[ MAC Anna | MAC router | PACCHETTO IP | FCS ]
                      |
                      v
PACCHETTO CHE IL ROUTER DEVE INOLTRARE
[ IP Anna: 192.168.1.10 | IP Bruno: 10.0.0.20 | segmento TCP ]
```

Il router legge l'IP di destinazione e consulta le informazioni di instradamento per scegliere l'uscita verso la rete `10.0.0.0/24`. Non deve consegnare il segmento TCP a un'applicazione propria: il messaggio non e' per lui. Deve solo preparare il pacchetto per il prossimo tratto.

Percio' il router lo **re-incapsula** in un nuovo frame:

```text
NUOVO FRAME, SULLA RETE DI BRUNO
[ MAC router, lato 10.0.0.1 | MAC Bruno |
  pacchetto IP: 192.168.1.10 -> 10.0.0.20 |
  FCS ]
```

### La frase da ricordare

> **Il frame cambia a ogni collegamento; il pacchetto IP conserva la destinazione finale.**

In una vera rete il router riduce anche il TTL del pacchetto IP di uno, per impedire che un pacchetto con un percorso sbagliato giri senza fine. Il principio importante qui resta: il router toglie il frame del tratto appena concluso e ne crea uno per quello successivo.

---

## 6. Decapsulare: togliere le buste nell'ordine corretto

Il computer di Bruno riceve il frame il cui MAC di destinazione e' il suo. A differenza del router, Bruno e' il destinatario finale: puo' procedere fino all'applicazione.

```text
BIT ricevuti
    |
    v
FRAME Ethernet: riconosce il proprio MAC, verifica il frame, rimuove header e FCS
    |
    v
PACCHETTO IP: riconosce il proprio IP, rimuove header IP
    |
    v
SEGMENTO TCP: legge la porta 4000 e lo consegna all'app giusta
    |
    v
DATI: l'app mostra "Ciao!"
```

Questo processo si chiama **decapsulamento**: ogni livello legge e usa l'informazione che gli compete, rimuove il proprio involucro e passa il contenuto al livello superiore.

La porta e' decisiva nell'ultimo passaggio. Anche se il pacchetto arriva al computer corretto, senza la porta il sistema operativo non saprebbe con quale programma associare quella comunicazione.

---

## 7. La mappa completa in una sola figura

```text
ANNA, mittente                                      BRUNO, destinatario

app:       "Ciao!"                         ->      "Ciao!"
TCP:       [porte | dati]                   ->      legge la porta, consegna all'app
IP:        [IP Anna | IP Bruno | TCP]       ->      legge l'IP, passa a TCP
Ethernet:  [MAC Anna | MAC router | IP]     ->      [MAC router | MAC Bruno | IP]
fisico:    bit e segnali                    ->      bit e segnali
                     \                     /
                      \--- router ---/
                          toglie il primo frame,
                          mantiene il pacchetto IP,
                          crea il secondo frame
```

Lo schema semplifica alcuni dettagli, ma conserva l'idea fondamentale: non esiste una sola busta valida per l'intero viaggio. Il messaggio attraversa piu' tratte locali; per ciascuna serve un frame adatto. IP invece conserva una visione piu' ampia, da un estremo all'altro.

---

## 8. Domande per ragionare insieme

1. Perche' una porta TCP non puo' sostituire un indirizzo IP?
2. Il router deve leggere il testo `Ciao!` per decidere dove inoltrare il pacchetto? Perche'?
3. Se Anna usa il Wi-Fi invece del cavo Ethernet, quali informazioni cambiano soprattutto: TCP, IP o il frame del collegamento?
4. Perche' il MAC di destinazione del primo frame e' quello del router e non quello di Bruno?
5. Se un computer riceve un pacchetto con il proprio IP ma una porta che nessun programma sta usando, il messaggio e' arrivato "del tutto"? Discutere la differenza fra computer raggiunto e applicazione raggiunta.

### Soluzioni e piste per il docente

1. L'IP identifica una destinazione nella rete; la porta identifica un programma su quel computer. Servono entrambi.
2. No. Il router usa soprattutto l'IP di destinazione e le sue informazioni di instradamento; il contenuto appartiene a livelli superiori.
3. Cambia soprattutto il livello di accesso alla rete: il frame e i segnali. TCP e IP possono restare uguali.
4. Perche' il frame consegna solo al prossimo dispositivo locale. Bruno non e' collegato direttamente alla LAN di Anna.
5. Il computer e' stato raggiunto, ma il sistema operativo non puo' consegnare i dati all'applicazione prevista. Il livello di trasporto completa un compito diverso dal livello IP.

## Piccolo compito facoltativo

Disegnare cinque scatole annidate per un messaggio diverso da `Ciao!`, usando un'applicazione a scelta. Scrivere per ogni scatola una sola domanda a cui risponde: programma, destinazione IP, prossimo dispositivo locale oppure segnale fisico.

## Riferimenti

- [RFC 1122 — Requirements for Internet Hosts](https://www.rfc-editor.org/rfc/rfc1122)
- [RFC 9293 — Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 8200 — Internet Protocol, Version 6](https://www.rfc-editor.org/rfc/rfc8200)
- [Cisco Networking Academy — Introduction to Networks](https://www.netacad.com/courses/networking)

---

## Quizzettone aneddotico: Operazione "Ciao!" sotto copertura

Una comunicazione urgente deve arrivare da **Anna** a **Bruno**:

```text
"Ciao! Il router non deve leggere questo messaggio."
```

Anna si trova nella rete `192.168.1.0/24`, Bruno nella rete `10.0.0.0/24`. In mezzo c'e' il router R1.

Dividiamoci in squadre: Applicazione, TCP, IP, Ethernet di Anna, Router R1, Ethernet di Bruno e Bruno. Ogni squadra difende il proprio livello: puo' leggere soltanto le informazioni che le servono.

### Livello 1: le buste

1. Qual e' la PDU quando il messaggio e' ancora nelle mani dell'applicazione?
2. TCP aggiunge le porte `51000 -> 4000`. Che cosa rappresentano? Perche' non basta l'IP?
3. IP aggiunge `192.168.1.10 -> 10.0.0.20`. A quale domanda risponde questa informazione?
4. Anna deve costruire il primo frame: come MAC di destinazione mette quello di Bruno o quello del router? Perche'?
5. Mettete nel giusto ordine: frame Ethernet, dati dell'applicazione, pacchetto IP, segmento TCP, bit e segnali.

### Livello 2: il dramma del router

R1 riceve:

```text
[ MAC Anna | MAC R1 | IP Anna -> IP Bruno | TCP 51000 -> 4000 | "Ciao!" | FCS ]
```

6. R1 puo' leggere il frame? Fino a quale livello deve decapsulare per prendere la decisione di inoltro?
7. Per inoltrare verso Bruno, quali informazioni devono restare uguali fra il primo e il secondo tratto?
8. Quali informazioni cambiano certamente quando R1 crea il nuovo frame?
9. Il router dovrebbe leggere il testo del messaggio per scegliere la strada? Cosa succederebbe alla privacy e all'efficienza della rete se ogni router lo facesse?
10. Il TTL diminuisce di uno: quale problema evita? Inventate un piccolo disastro di rete che succederebbe senza TTL.

### Livello 3: arrivo a destinazione

11. Bruno riceve un frame con il proprio MAC, ma il pacchetto IP contiene l'indirizzo di un altro computer. Che cosa dovrebbe fare?
12. Bruno riceve un pacchetto con il proprio IP, ma nessuna applicazione ascolta sulla porta `4000`. Il messaggio e' arrivato? Rispondete distinguendo fra computer raggiunto e applicazione raggiunta.
13. Perche' le porte assomigliano agli interni di un centralino, mentre gli IP assomigliano all'indirizzo dell'edificio?
14. Se Anna passa dal cavo al Wi-Fi, cosa cambia soprattutto: dati dell'app, TCP, IP o livello di accesso alla rete?
15. Vera o falsa, poi motivate: "Un MAC identifica un computer su Internet".

### Boss finale: il messaggio misterioso

Un pacchetto parte da Anna verso Bruno e attraversa **cinque router**.

16. Quanti frame diversi possono essere creati lungo il percorso?
17. Quante volte il pacchetto IP viene inserito in un nuovo frame?
18. IP sorgente, IP destinazione e porte TCP restano normalmente gli stessi? Quale eccezione reale conoscete o potete intuire?
19. Disegnate il viaggio come una serie di buste: segnate in rosso cio' che cambia a ogni tratto e in blu cio' che identifica la conversazione fra Anna e Bruno.
20. Una squadra propone: "Usiamo solo MAC, cosi' eliminiamo IP e semplifichiamo tutto". L'altra deve trovare almeno due ragioni per cui l'idea non scala a Internet.

### Soluzioni per il docente

1. Dati dell'applicazione.
2. Identificano processo o applicazione sorgente e destinazione; l'IP identifica il computer, non il programma.
3. A quale computer o rete deve arrivare il messaggio finale.
4. Il MAC del router: Bruno e' in un'altra rete, quindi il router e' il prossimo dispositivo locale.
5. Dati dell'applicazione, segmento TCP, pacchetto IP, frame Ethernet, bit e segnali.
6. Si'; rimuove il frame e lavora fino a IP. Non deve consegnare il segmento a TCP o a un'applicazione.
7. In generale il pacchetto IP e il segmento TCP: IP finali, porte e dati.
8. MAC sorgente, MAC destinazione, trailer FCS e frame intero; inoltre il TTL del pacchetto IP diminuisce.
9. No: il router usa l'IP di destinazione e le informazioni di instradamento. Leggere il contenuto danneggerebbe privacy, efficienza e separazione dei compiti.
10. Evita cicli infiniti di pacchetti causati da errori di routing.
11. Scarta il pacchetto: il frame era per lui, ma il pacchetto IP no.
12. Il computer e' stato raggiunto, ma non l'applicazione.
13. L'IP porta all'host; la porta al servizio o processo dentro quell'host.
14. Il livello di accesso alla rete e i segnali fisici; TCP e IP possono restare invariati.
15. Falsa: il MAC serve sul collegamento locale e il MAC di destinazione cambia a ogni tratto.
16. Con cinque router ci sono sei tratte, quindi almeno sei frame successivi.
17. Sei volte.
18. Normalmente restano gli stessi; il NAT puo' modificare IP e/o porte.
19. Cambiano frame, MAC e FCS; restano dati, porte e IP end-to-end, mentre il TTL diminuisce.
20. I MAC non forniscono una gerarchia adatta all'instradamento globale; ogni rete locale dovrebbe conoscere un numero enorme di dispositivi lontani.
