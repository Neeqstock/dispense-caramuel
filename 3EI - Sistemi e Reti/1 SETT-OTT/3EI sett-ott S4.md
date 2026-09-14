# 3EI - Settimana 4: IL CICLO DELLA CPU E LE STRADE DEI DATI

Kit didattico completo. Il riferimento delle otto settimane e' il [quadro 3EI - SETT-OTT](3EI%20-%20SETT-OTT.md).

```text
SETTIMANA 4
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] Dal PC all'istruzione: il fetch
│   ├── [1.2] Decode, execute e write-back
│   ├── [1.3] Registri e segnali di controllo
│   ├── [1.4] CISC e RISC: due filosofie, molte implementazioni
│   └── [1.5] Prestazioni: istruzioni, CPI e clock
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] HDD: meccanica e latenza
│   ├── [2.2] SSD SATA e memoria NAND
│   ├── [2.3] SSD NVMe e bus PCIe
│   └── [2.4] Identificazione e confronto su postazioni reali
└── 📋 GUIDA DI REGIA PER IL DOCENTE
    ├── Cronoprogramma teorico
    ├── Schema del ciclo da disegnare
    └── Micro-task formativo per casa
```

## 🧠 MODULO TEORICO (2 Ore in Aula)

### ├── [1.1] Fetch: trovare l'istruzione

Il ciclo macchina e' la sequenza con cui la CPU trasforma un programma memorizzato in azioni. Nel **fetch** la CU usa il valore del PC come indirizzo; il MAR lo presenta alla memoria, la memoria restituisce l'istruzione nel MDR e l'IR la conserva per la fase successiva. Il PC viene incrementato in modo da puntare alla prossima istruzione, salvo che un salto lo modifichi.

```text
PC ──> MAR ── richiesta READ ──> MEMORIA
				      │
IR <── MDR <── istruzione <───────┘
PC <- PC + lunghezza istruzione
```

L'incremento non e' sempre di un byte fisso: dipende dal formato delle istruzioni. Nelle architetture con istruzioni a lunghezza variabile, la CU deve determinare la lunghezza durante la decodifica.

### ├── [1.2] Decode, execute e write-back

* **Decode (decodifica):** la CU separa opcode, registri sorgente, registro destinazione e dati immediati. Attiva i percorsi necessari all'interno della CPU.
* **Execute (esecuzione):** l'ALU calcola, confronta o sposta; una load/store prepara un accesso alla memoria; un salto calcola la nuova destinazione.
* **Write-back:** il risultato viene scritto nel registro destinazione oppure completato in memoria. In una store il valore passa verso la memoria invece di rientrare in un registro.

**Esempio d'aula:** per `ADD R3, R1, R2`, la CU legge R1 e R2, seleziona ADD nell'ALU e abilita la scrittura di R3. Per `LOAD R3, [R1+8]`, l'ALU calcola l'indirizzo effettivo e la CPU deve attendere il dato prima del write-back.

### ├── [1.3] Registri e segnali di controllo

Il diagramma del ciclo diventa concreto quando si associano segnali e registri:

| Fase | Registri coinvolti | Segnali o azioni |
|---|---|---|
| Fetch | PC, MAR, MDR, IR | `MemRead`, incremento PC, caricamento IR |
| Decode | IR, registri generali | lettura operandi, decodifica opcode |
| Execute | ALU, PSW | selezione operazione, aggiornamento flag |
| Memory | MAR, MDR | `MemRead` oppure `MemWrite` |
| Write-back | registro destinazione | `RegWrite` |

I segnali non sono messaggi software: sono livelli logici che abilitano multiplexer, porte di scrittura e linee di lettura. Questo collega la teoria della CU al cablaggio interno della CPU.

### ├── [1.4] CISC e RISC

**CISC (Complex Instruction Set Computer)** tende a offrire molte istruzioni, alcune capaci di svolgere operazioni articolate e con formati anche variabili. La famiglia x86-64 e' un esempio; internamente puo' tradurre istruzioni complesse in micro-operazioni piu' semplici.

**RISC (Reduced Instruction Set Computer)** privilegia istruzioni semplici e regolari, spesso di lunghezza uniforme, e un modello **load/store**: solo alcune istruzioni accedono alla memoria, mentre i calcoli lavorano sui registri. ARM e RISC-V rappresentano famiglie RISC diffuse.

```text
CISC:  LOAD+CALCOLO+STORE in una istruzione complessa
	-> decoder piu' ricco, formato variabile

RISC:  LOAD -> ADD -> STORE in istruzioni regolari
	-> pipeline piu' prevedibile, piu' istruzioni possibili
```

Non e' corretto dichiarare un vincitore assoluto. Contano microarchitettura, compilatore, cache, pipeline, consumo e programma eseguito. Anche un processore CISC moderno usa molte tecniche tipiche del mondo RISC.

### ├── [1.5] Prestazioni: dal clock al tempo effettivo

La relazione utile e':

$$T_{CPU} = N_{istruzioni} \times CPI \times T_{clock}$$

Due processori possono avere frequenze diverse ma tempi simili se cambiano numero di istruzioni o CPI. **Esempio:** macchina A: $10^9$ istruzioni, $CPI=2$, $f=2\,\text{GHz}$; macchina B: $1{,}2\cdot10^9$ istruzioni, $CPI=1{,}2$, $f=1{,}5\,\text{GHz}$. Si calcolano i tre fattori prima di dire quale sia piu' rapida. Le attese della memoria non sono un dettaglio: saranno centrali nella settimana 5.

## 💻 MODULO LABORATORIO (2 Ore con ITP)

### ├── [2.1] HDD: piatti, testine e latenza

Un HDD registra dati su piatti magnetici rotanti. Il tempo di accesso comprende seek della testina, latenza di rotazione e trasferimento. Individuare su un disco didattico piatti, motore, attuatore e connettori SATA data/power. Non aprire un HDD funzionante: il gruppo osserva immagini o un campione dismesso, perche' polvere e urti possono danneggiarlo.

### ├── [2.2] SSD SATA e NAND

Un SSD usa celle di memoria NAND e un controller; non possiede parti meccaniche mobili. L'interfaccia SATA limita il collegamento rispetto a un NVMe moderno, ma il formato da 2,5 pollici e i cavi SATA lo rendono semplice da installare. Distinguere **protocollo/interfaccia SATA** da **forma fisica**: 2,5 pollici descrive il contenitore, non la tecnologia interna.

### ├── [2.3] SSD NVMe e PCIe

NVMe e' un protocollo progettato per la memoria non volatile su PCIe. Un modulo M.2 puo' essere SATA oppure NVMe: la tacca, la serigrafia della motherboard e la documentazione chiariscono il caso. PCIe usa lane (x1, x4, x8, x16); piu' lane aumentano la banda teorica, ma slot e dispositivo devono essere compatibili.

### ├── [2.4] Procedura concreta (110 min)

* **FASE A - Sicurezza e previsione (10 min):** PC spento, cavo staccato, braccialetto; leggere l'etichetta senza rimuovere il disco.
* **FASE B - HDD (20 min):** riconoscere parti meccaniche su campione o schema, collegare mentalmente latenza e sintomo “rumore/attesa”.
* **FASE C - SATA (25 min):** distinguere cavo dati e alimentazione, individuare porte SATA e compilare modello, capacita' e velocita' dichiarata.
* **FASE D - NVMe/PCIe (25 min):** individuare slot M.2 e PCIe, leggere il manuale della scheda e verificare il numero di lane.
* **FASE E - Tabella diagnostica (20 min):** per tre scenari scegliere HDD, SSD SATA o NVMe motivando costo, capacita', latenza e uso.
* **FASE F - Riordino (10 min):** riposizionare pannelli e cavi e consegnare la scheda.

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma teorico (110 minuti)
* **00-12:** ripresa della settimana 3: “dove va l'istruzione dopo il PC?”.
* **12-35:** simulazione fisica di fetch con PC, MAR, MDR e IR.
* **35-58:** decode, execute, write-back su `ADD` e `LOAD`.
* **58-78:** segnali della CU e tabella alla lavagna.
* **78-98:** CISC/RISC con trasformazione di una istruzione complessa in tre semplici.
* **98-110:** esercizio numerico sul tempo CPU e ticket d'uscita.

### ✍️ Disegno alla lavagna
```text
[FETCH] -> [DECODE] -> [EXECUTE] -> [MEMORY] -> [WRITE-BACK]
 PC         IR/CU        ALU          MAR/MDR       REG
```

### 🎯 Micro-task formativo per casa
Preparare una tabella a tre righe per HDD, SSD SATA e SSD NVMe con: parti mobili, interfaccia, latenza relativa, vantaggio e limite. Scrivere inoltre in quattro frasi il ciclo di `LOAD R1,[R2+4]`.
