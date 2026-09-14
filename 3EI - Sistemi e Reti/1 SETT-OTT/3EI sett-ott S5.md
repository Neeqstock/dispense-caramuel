# 3EI - Settimana 5: LA SCALA DELLA MEMORIA E IL SEGRETO DELLA CACHE

Kit didattico completo. La settimana si collega al percorso generale nel [quadro 3EI - SETT-OTT](3EI%20-%20SETT-OTT.md).

```text
SETTIMANA 5
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] Perche' esiste una gerarchia delle memorie
│   ├── [1.2] Registri, cache L1/L2/L3, RAM e memoria di massa
│   ├── [1.3] SRAM, DRAM e organizzazione delle celle
│   ├── [1.4] Hit, miss, localita' e AMAT
│   └── [1.5] Lettura di un accesso a un array
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] Checklist di smontaggio
│   ├── [2.2] Catalogazione dei componenti
│   ├── [2.3] Rimontaggio guidato e controllo dei cavi
│   └── [2.4] Prova funzionale senza improvvisazioni
└── 📋 GUIDA DI REGIA PER IL DOCENTE
	├── Cronoprogramma teorico
	├── Disegno della gerarchia alla lavagna
	└── Micro-task formativo per casa
```

## 🧠 MODULO TEORICO (2 Ore in Aula)

### ├── [1.1] Perche' esiste una gerarchia

Una memoria ideale sarebbe enorme, velocissima, economica e non volatile. Nella pratica queste proprieta' sono in conflitto: la tecnologia piu' veloce costa di piu' per bit e ha capacita' inferiore. Il computer usa quindi piu' livelli e porta vicino alla CPU cio' che probabilmente servira' presto.

```text
piu' veloce, piccola, costosa per bit
				 ▲
REGISTRI -> CACHE L1 -> CACHE L2 -> CACHE L3 -> RAM -> SSD/HDD
				 ▼
piu' lenta, grande, economica per bit, persistente
```

Salendo la latenza diminuisce e la banda aumenta; scendendo aumentano capacita' e persistenza. Non e' una graduatoria assoluta per ogni dispositivo, ma un modello utile per prevedere il comportamento di un accesso.

### ├── [1.2] Dal registro alla memoria di massa

* **Registri:** sono nella CPU, hanno pochissimi bit e possono essere letti dall'ALU con latenza minima.
* **Cache L1/L2/L3:** sono piccole memorie vicine o integrate nella CPU. L1 e' generalmente la piu' rapida e piccola; L2 offre piu' spazio; L3 e' spesso condivisa tra core.
* **RAM:** contiene programmi e dati attivi. E' volatile: togliendo alimentazione il contenuto ordinario si perde.
* **SSD/HDD:** conservano i dati senza alimentazione, ma hanno latenze molto superiori rispetto alla RAM.

**Esempio d'aula:** quando un programma scorre un vettore, la CPU non chiede ogni byte direttamente al disco. Il sistema carica blocchi nella RAM; la cache trattiene le porzioni usate piu' spesso, mentre i registri custodiscono gli operandi immediati.

### ├── [1.3] SRAM e DRAM

La **SRAM** usa celle costituite tipicamente da piu' transistor, non richiede il refresh della carica come la DRAM ed e' rapida ma occupa piu' area. Per questo e' adatta alla cache.

La **DRAM** memorizza il bit in una cella con condensatore e transistor. Il condensatore perde carica, quindi la memoria deve essere periodicamente rinfrescata. Le celle sono piu' dense ed economiche, motivo per cui la DRAM e' usata come RAM principale.

Il refresh non significa che il programma “si aggiorna”: e' un'operazione elettrica interna che mantiene la carica delle celle. Anche la RAM piu' veloce resta molto piu' lenta dei registri.

### ├── [1.4] Hit, miss, localita' e AMAT

Quando la CPU cerca un dato in cache si verifica un **hit** se il dato e' presente. In caso contrario c'e' un **miss** e bisogna consultare il livello successivo, pagando una penalita'.

La cache funziona grazie a due forme di localita':

* **temporale:** un dato usato da poco potrebbe essere riutilizzato presto;
* **spaziale:** se si accede a un indirizzo, e' probabile accedere a indirizzi vicini, come nella scansione di un array.

Il tempo medio di accesso e' stimabile con:

$$AMAT = Hit\ Time + Miss\ Rate \times Miss\ Penalty$$

**Esempio:** hit time $2\,ns$, miss rate $5\%$, miss penalty $50\,ns$ danno $AMAT=2+0{,}05\times50=4{,}5\,ns$. Ridurre il miss rate puo' essere piu' efficace che rendere appena piu' rapida la cache.

### ├── [1.5] Un programma e la localita'

Consideriamo due cicli che sommano gli elementi di una matrice. Il ciclo che percorre elementi contigui sfrutta meglio la localita' spaziale; un accesso casuale puo' provocare piu' miss. La cache trasferisce spesso una **linea** contenente piu' parole, non una singola parola isolata.

Questo non significa che la cache “indovini” sempre: se la struttura dati e' piu' grande, se il programma salta continuamente tra aree lontane o se piu' dati competono nello stesso insieme, i miss aumentano. La misura reale dipende dal programma e dal sistema.

## 💻 MODULO LABORATORIO (2 Ore con ITP)

### ├── [2.1] Preparazione e inventario iniziale

Il gruppo prepara tappetino ESD, braccialetto, cacciaviti, vaschetta per viti, etichette e scheda di lavoro. Prima di scollegare alcun cavo, fotografa il PC aperto e disegna una mappa: posizione della motherboard, RAM, dischi, PSU, ventole e schede.

### ├── [2.2] Smontaggio guidato

1. Spegnere, scollegare e attendere; verificare la checklist con l'ITP.
2. Scollegare i cavi afferrando il connettore, non tirando il filo.
3. Rimuovere RAM e schede di espansione dai bordi, poi dischi e alimentatore secondo l'ordine indicato.
4. Conservare ogni vite in un contenitore etichettato e non mescolare distanziali e viti del case.
5. Per ogni elemento annotare tecnologia, connettori, funzione, posizione e rischio principale.

### ├── [2.3] Rimontaggio e controllo

Il rimontaggio segue l'ordine inverso solo quando la struttura lo consente. Controllare distanziali della motherboard, allineamento delle porte posteriori, fissaggio dei dischi, collegamento ATX/CPU, RAM inserita fino allo scatto e cavi lontani dalle ventole. Prima dell'accensione, l'ITP firma il controllo incrociato del gruppo.

### ├── [2.4] Attivita' a fasi (110 min)

* **FASE A - Briefing e sicurezza (15 min):** ruoli nel gruppo, inventario e foto iniziale.
* **FASE B - Smontaggio (35 min):** un componente alla volta, con verifica dell'ITP prima del successivo.
* **FASE C - Catalogazione (20 min):** tabella con livello di memoria, tecnologia, connettore e funzione.
* **FASE D - Rimontaggio (30 min):** seguire la checklist, senza accendere fino alla firma.
* **FASE E - Debrief (10 min):** spiegare quale componente appartiene alla gerarchia piu' vicina alla CPU e perche'.

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma teorico (110 minuti)
* **00-10:** mostrare tre oggetti: registro simulato, modulo RAM e SSD; raccogliere ipotesi sull'ordine.
* **10-30:** costruire la gerarchia e discutere velocita', costo e capacita'.
* **30-50:** SRAM/DRAM con disegno di cella semplificato.
* **50-75:** hit, miss e localita' usando una scatola di carte numerate.
* **75-98:** calcolo guidato dell'AMAT e confronto tra due cache.
* **98-110:** verifica flash e consegna della scheda di smontaggio.

### ✍️ Disegno alla lavagna
```text
CPU
 |  registri: minimo tempo
 v
L1 -> L2 -> L3 -> RAM -> SSD/HDD
	   ogni miss porta al livello successivo
	   AMAT = hit time + miss rate * miss penalty
```

### 🎯 Micro-task formativo per casa
Inventare una sequenza di sei accessi a indirizzi e indicare quali sfruttano localita' temporale o spaziale. Calcolare l'AMAT per hit time $1\,ns$, miss rate $10\%$ e penalty $40\,ns$. Portare anche una domanda da porre al gruppo durante lo smontaggio.
