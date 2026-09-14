# 3EI - Settimana 3: IL CUORE DELLA MACCHINA, CPU E SPAZIO DEGLI INDIRIZZI

Kit didattico completo per la terza settimana. Il percorso delle otto settimane e' nel [quadro 3EI - SETT-OTT](3EI%20-%20SETT-OTT.md).

```text
SETTIMANA 3
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] CPU, ALU e Control Unit: chi calcola e chi coordina
│   ├── [1.2] I registri visibili nel ciclo di istruzione
│   ├── [1.3] Clock, periodo e prestazioni
│   └── [1.4] Bus degli indirizzi e spazio indirizzabile 2^n
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] Motherboard, socket e orientamento della CPU
│   ├── [2.2] Pasta termica e dissipatore
│   ├── [2.3] RAM, DIMM e dual channel
│   └── [2.4] Scheda di osservazione e controllo ESD
└── 📋 GUIDA DI REGIA PER IL DOCENTE
    ├── Cronoprogramma di circa 110 minuti
    ├── Disegno CPU da costruire alla lavagna
    └── Micro-task formativo per casa
```

> **Obiettivo della settimana:** passare dall'idea astratta di CPU alla lettura fisica della scheda madre. Ogni studente deve saper descrivere il percorso di un indirizzo e di un dato, riconoscere i principali registri e motivare una scelta di montaggio senza forzare componenti.

---

## 🧠 MODULO TEORICO (2 Ore in Aula)

### ├── [1.1] CPU, ALU e Control Unit: due funzioni nella stessa macchina

La **CPU (Central Processing Unit)** e' il componente che interpreta ed esegue le istruzioni di un programma. Non e' una scatola magica che “fa tutto”: contiene un insieme di blocchi specializzati che collaborano sotto il coordinamento del clock.

* **ALU (Arithmetic Logic Unit):** esegue somme, sottrazioni, confronti, AND, OR, XOR, shift e test sui bit. Riceve operandi dai registri e produce un risultato, oltre ad aggiornare alcuni flag.
* **CU (Control Unit):** legge l'istruzione, la decodifica e genera segnali come lettura memoria, scrittura registro, selezione dell'operazione ALU e aggiornamento del PC. La CU decide la sequenza, ma non “somma” al posto dell'ALU.
* **Registri:** memoria interna piccola e velocissima. Conservano indirizzi, istruzioni, operandi, risultati temporanei e stato.

```text
			    CPU
	 ┌──────────────────────────────────────┐
	 │  ┌──────────────┐   ┌──────────────┐ │
	 │  │ CONTROL UNIT │──>│ segnali      │ │
	 │  │ decodifica   │   │ di controllo │ │
	 │  └──────┬───────┘   └──────┬───────┘ │
	 │         │                  │         │
	 │  ┌──────▼───────┐   ┌──────▼───────┐ │
	 │  │ REGISTRI     │<->│ ALU          │ │
	 │  │ PC IR MAR... │   │ calcoli      │ │
	 │  └──────────────┘   └──────────────┘ │
	 └───────────────┬──────────────────────┘
			   │ bus
		     ┌────▼────┐
		     │ memoria │
		     └─────────┘
```

**Esempio d'aula.** Per l'istruzione “somma il valore in R1 con quello in R2 e scrivi in R3”, la CU seleziona R1 e R2, ordina all'ALU l'operazione ADD e abilita la scrittura in R3. Se si scambiano i ruoli, la spiegazione non torna: l'ALU esegue, la CU orchestra.

### ├── [1.2] PC, IR, MAR, MDR e PSW: la memoria di lavoro della CPU

I registri hanno nomi diversi perche' conservano informazioni diverse.

1. **PC (Program Counter):** indirizzo della prossima istruzione da prelevare. Dopo il fetch viene incrementato oppure sostituito dalla destinazione di un salto.
2. **IR (Instruction Register):** istruzione appena prelevata e in fase di decodifica/esecuzione.
3. **MAR (Memory Address Register):** indirizzo della cella di memoria con cui la CPU sta comunicando.
4. **MDR (Memory Data Register):** dato letto dalla memoria o dato pronto per una scrittura.
5. **PSW (Program Status Word):** parola di stato con flag e informazioni di controllo. Flag tipici sono Zero (Z), Carry (C), Negative/Sign (N/S) e Overflow (V/O). Un confronto o una somma puo' modificarli; un salto condizionato li consulta.

Durante una lettura semplificata la sequenza e': `MAR <- PC`, richiesta `READ`, `MDR <- MEM[MAR]`, `IR <- MDR`, `PC <- PC + lunghezza_istruzione`. Per un dato si ripete una sequenza analoga, ma l'indirizzo puo' provenire dall'istruzione o da un registro di indirizzo.

**Esempio d'aula sui flag.** Se una ALU calcola $7-7$, il risultato e' zero e il flag Z viene impostato. La CU puo' poi eseguire un salto “se Z=1”. Il PSW non contiene il risultato completo: contiene segnali sintetici utili alle decisioni successive.

### ├── [1.3] Clock, periodo e prestazioni

Il **clock** e' un segnale periodico che fornisce un riferimento temporale ai circuiti sincroni. La frequenza $f$ e' il numero di cicli al secondo, misurata in hertz; il periodo $T$ e' la durata di un ciclo:

$$T = \frac{1}{f}$$

Un clock da $3\,\text{GHz}$ ha periodo teorico di circa $0{,}333\,\text{ns}$. Questo non significa che ogni istruzione finisca in un ciclo: possono servire piu' cicli e possono intervenire cache, pipeline e attese.

Per collegare frequenza e lavoro si usa il tempo CPU:

$$T_{CPU} = N_{istruzioni} \times CPI \times T_{clock}$$

dove $CPI$ e' il numero medio di cicli per istruzione. **Esempio:** una CPU a $2\,\text{GHz}$ con $CPI=2$ impiega circa $1\,\text{ns}$ per istruzione media, prima di considerare altre attese. Il confronto corretto tra due processori deve quindi includere programma, numero di istruzioni e CPI, non solo i GHz.

### ├── [1.4] Spazio indirizzabile: perche' compare $2^n$

Se il bus degli indirizzi ha $n$ linee, ogni linea puo' assumere 0 oppure 1. Le combinazioni possibili sono:

$$2^n$$

Se ogni indirizzo identifica un byte, la capacita' massima indirizzabile e' $2^n$ byte. Con 16 linee si hanno $2^{16}=65.536$ indirizzi, cioe' $64\,\text{KiB}$; con 32 linee si arriva a $2^{32}$ byte, circa $4\,\text{GiB}$. La formula non dice quanta RAM e' fisicamente installata: indica quanti indirizzi il processore puo' rappresentare.

**Esercizio guidato:** per 12 linee, $2^{12}=4096$ byte = $4\,\text{KiB}$; per 20 linee, $2^{20}=1.048.576$ byte = $1\,\text{MiB}$. Chiedere sempre se l'indirizzamento e' a byte o a parola e non confondere bit con byte.

## 💻 MODULO LABORATORIO (2 Ore con ITP)

### ├── [2.1] Motherboard, socket e preparazione

Prima di intervenire, il gruppo deve spegnere il PC, togliere alimentazione, attendere la scarica residua e indossare il braccialetto antistatico. Sulla motherboard individuare chipset, socket CPU, slot DIMM, connettore ATX 24-pin, alimentazione CPU 4/8-pin, slot PCIe e connettori delle ventole.

### ├── [2.2] CPU, pasta termica e dissipatore

Osservare il triangolo di riferimento sulla CPU e quello sul socket. Sollevare la leva solo con la scheda scollegata e senza esercitare pressione laterale. La pasta termica non “incolla” il dissipatore: riempie microscopiche irregolarita' tra metallo del processore e base del dissipatore, riducendo la resistenza termica. Applicare una quantita' minima secondo le indicazioni dell'ITP, posare il dissipatore in asse e collegare la ventola a `CPU_FAN`.

Non avviare mai il sistema senza dissipatore correttamente montato. La pasta in eccesso puo' sporcare il socket e non migliora il raffreddamento.

### ├── [2.3] RAM e dual channel

Identificare il tipo di DIMM, la tacca di orientamento e i fermi laterali. Il modulo entra in una sola direzione: se la tacca non coincide, non si forza. Con due moduli compatibili inseriti negli slot indicati dal manuale, il **dual channel** permette al controller di usare due canali di memoria in parallelo, aumentando la larghezza di banda teorica. Non raddoppia automaticamente ogni prestazione: dipende dal carico e dalla configurazione.

### ├── [2.4] Procedura a fasi e scheda di osservazione (110 min)

* **FASE A - Sicurezza e inventario (15 min):** controllare alimentazione scollegata, ESD, attrezzi e numero della postazione. Fotografare o disegnare la configurazione iniziale.
* **FASE B - Mappa della motherboard (20 min):** ogni coppia etichetta socket, DIMM, ATX, CPU_FAN e PCIe. L'ITP verifica prima di procedere.
* **FASE C - CPU e raffreddamento (30 min):** simulare apertura socket, orientamento, pasta termica, dissipatore e collegamento ventola su banco didattico o PC non alimentato.
* **FASE D - RAM singolo/dual channel (25 min):** confrontare gli slot raccomandati, annotare tacca, fermi e capacita'. Motivare perche' si usano quegli slot.
* **FASE E - Riordino e restituzione (20 min):** ripristinare la postazione, completare la scheda e spiegare oralmente una scelta sicura.

La scheda deve contenere: modello della motherboard, socket, tipo e numero di moduli RAM, posizione di `CPU_FAN`, tre rischi prevenuti e una conversione svolta su $2^n$.

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma teorico (110 minuti)
* **00-10:** mostrare CPU e modulo RAM; domanda d'apertura: “Quale informazione deve conoscere la CPU per trovare la prossima istruzione?”.
* **10-30:** costruire la distinzione ALU/CU con l'esempio della somma.
* **30-55:** simulare PC, MAR, MDR e IR con quattro studenti che impersonano i registri.
* **55-75:** clock, periodo e formula del tempo CPU; calcolo collettivo di $T=1/f$.
* **75-98:** esercizi progressivi su $2^n$, indirizzamento a byte e KiB/MiB.
* **98-110:** correzione lampo, domande a bruciapelo e consegna della checklist al laboratorio.

### ✍️ Disegno alla lavagna
```text
PC -> MAR -> [BUS INDIRIZZI] -> MEMORIA
				  MEMORIA -> MDR -> IR
						   |
					   CU decodifica
						   |
					   ALU <-> registri
					   risultato + PSW
```

### 🎯 Micro-task formativo per casa
Disegnare il percorso `PC -> MAR -> memoria -> MDR -> IR` e risolvere: “Con 18 linee di indirizzo a byte, quanti KiB sono indirizzabili?”. Aggiungere una frase sulla differenza tra frequenza del clock e prestazione complessiva. Portare lo schema all'inizio della settimana 4.
