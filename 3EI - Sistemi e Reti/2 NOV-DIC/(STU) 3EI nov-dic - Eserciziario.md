⬅️ [S5 - Ripasso e collegamenti](./%28STU%29%203EI%20nov-dic%20S5%20-%20Ripasso%20e%20collegamenti.md) · 🏠 [Indice](../README.md)

# 🛠️ Eserciziario · 3EI Novembre-Dicembre — Dischi, avvio, VM e parallelismo

**3EI · Novembre-Dicembre · Eserciziario · Sistemi e Reti · Unità S1–S4**

⏱️ **Tempo di studio dichiarato:** circa **1 ora e 20 minuti** in totale (**✅ circa 50 minuti**, **🔍 circa 30 minuti**). I 🤓 sono facoltativi. Non è un compito obbligatorio.

> **Legenda:** ✅ minimo per la sufficienza · 🔍 dettagli per il voto massimo · 🤓 approfondimento facoltativo · 🟢 esercizio svolto · 🎯 da provare · 📖 teoria · ✏️ pratica scritta · 📜 caso reale · 🧪 caso inventato (dati dichiarati) · 📌 controllo · ⚠️ errore comune · 🧠 da ricordare · 🃏 soluzione

**Filo rosso.** Sei alle prese con il tuo PC (e con quelli di alcuni amici) per risolvere problemi reali: un disco lento o quasi pieno, l'installazione di Linux accanto a Windows, una macchina virtuale che scatta, uno script Python che non accelera. Tutti i nomi (Marco, PC-Casa, Disco-A) e i valori degli scenari sono **inventati e dichiarati come tali**.

**Nota.** Questo eserciziario è allineato alle dispense **S1–S4** del bimestre. La verifica docente non è ancora stata redatta: quando sarà pronta, eventuali dettagli potranno essere aggiornati.

---

## 🧭 Come usare questo eserciziario

Ogni dossier corrisponde a una settimana di lezione e segue lo stesso ordine: 📜 un caso reale, poi 🟢 almeno un esercizio svolto passo passo, poi 🎯 esercizi da provare da solo. La soluzione di ogni 🎯 è nascosta dentro 🃏: **prova prima su carta o a voce, poi apri per controllare.**

| Livello | Che cosa trovi | Tempo stimato |
|---|---|---|
| ✅ | 🟢 svolti e 🎯 essenziali per la sufficienza | circa 50 minuti |
| 🔍 | 🎯 di approfondimento, calcoli e diagnosi | circa 30 minuti |
| 🤓 | riquadri facoltativi per curiosi | a piacere |

---

## 1 · 💾 Memorie di massa (S1)

📜 **Caso reale.** Dal 2013 l'azienda cloud **Backblaze** pubblica ogni trimestre statistiche pubbliche sullo stato di salute di oltre 280.000 dischi fissi nei suoi data center. I dati mostrano che i contatori **SMART** aiutano a prevedere molti guasti prima che il disco muoia del tutto, ma non tutti: una parte dei dischi si rompe all'improvviso senza nessun preavviso. Per questo i backup restano sempre indispensabili.

### 1.1 🟢 Svolto · ✅ (📖 + ✏️) — Disco lento e manutenzione sbagliata

**Consegna (scenario inventato).** Marco ha un vecchio portatile con Windows su un **HDD da 1 TB**. Negli ultimi mesi il PC impiega quasi due minuti ad aprire una cartella piena di video e documenti. Un amico gli consiglia: *«Lancia la deframmentazione!»*. Poi Marco compra un **SSD M.2 NVMe da 512 GB** e vuole fare la stessa operazione ogni settimana anche sul nuovo disco.
1. Perché la deframmentazione aiuta il vecchio HDD?
2. Perché sarebbe un errore deframmentare il nuovo SSD, e che cosa usa invece il sistema operativo?

**Svolgimento.**
1. **Sul vecchio HDD:** salvando e cancellando file nel tempo, i dati si sono spezzati in blocchi sparsi (**frammentazione**). La testina meccanica deve spostarsi in più punti del piatto rotante per leggere un solo file. La **deframmentazione** rimette i pezzi vicini, riducendo gli spostamenti della testina.
2. **Sul nuovo SSD:** non ci sono testine né piatti che girano, quindi leggere celle sparse non rallenta quasi per nulla. Inoltre, spostare gigabyte di file consuma inutilmente le celle flash, che reggono un numero finito di scritture. Al posto della deframmentazione, il sistema usa il comando **TRIM** per avvisare l'SSD di quali blocchi cancellati può ripulire.

📌 **Controllo.** Controlla la tecnologia del disco prima di scegliere l'operazione: HDD → deframmentazione; SSD → niente deframmentazione, sì TRIM (*Ottimizza unità*).

⚠️ **Errore comune:** pensare che «ottimizzare» un SSD voglia dire deframmentarlo. In Windows il pulsante *Ottimizza* riconosce il tipo di disco: sull'HDD deframmenta, sull'SSD manda il comando TRIM.

> 🧠 <u>Su HDD i pezzi lontani rallentano la testina; su SSD spostare i file non accelera la lettura e consuma le celle.</u>

### 1.2 🎯 Da provare (📖) · ✅ — Volatile, persistente e TRIM

**Consegna.** Rispondi alle due domande brevi.
1. Classifica ciascun componente come **volatile (V)** o **persistente (P)**: RAM, SSD, cache L1 della CPU, chiavetta USB, HDD.
2. Perché quando un programma parte viene copiato dal disco alla RAM invece di essere eseguito direttamente dal disco?

<details>
<summary>🃏 <b>1.2 — Soluzione</b></summary>

1. RAM (**V**), SSD (**P**), cache L1 (**V**), chiavetta USB (**P**), HDD (**P**).
2. Perché la CPU lavora sulla RAM, che ha tempi di accesso ordini di grandezza più rapidi rispetto a qualsiasi memoria di massa.

</details>

### 1.3 🎯 Da provare (✏️) · ✅ — Formato, interfaccia e guasti

**Consegna.** Risolvi i due punti su casi inventati.
1. Un compagno legge sulla scatola di un disco: *«SSD M.2 SATA 256 GB»* e ti dice: *«Siccome è M.2, allora è NVMe!»*. Correggilo distinguendo **formato** e **interfaccia/protocollo**.
2. Associa ciascun sintomo alla causa più probabile scegliendo tra: *danno logico (soft bad sector)*, *guasto meccanico HDD (click of death)*, *SSD a fine vita*.
   - (a) L'HDD fa un ticchettio ritmico continuo e il PC non parte.
   - (b) L'SSD lascia ancora aprire e copiare i file, ma rifiuta qualunque salvataggio.
   - (c) Un solo file corrotto dopo uno sbalzo di corrente torna leggibile dopo una riscrittura del settore.

<details>
<summary>🃏 <b>1.3 — Soluzione</b></summary>

1. **M.2** indica il **formato fisico** (la schedina rettangolare che si avvita sulla scheda madre), mentre **SATA** indica l'**interfaccia/protocollo** con cui comunica (fino a ~550 MB/s). Esistono M.2 che usano SATA e M.2 che usano PCIe/NVMe: la forma non garantisce il protocollo NVMe.
2. (a) **Guasto meccanico HDD (click of death)**; (b) **SSD a fine vita** (passa in sola lettura); (c) **Danno logico (soft bad sector)**.

</details>

### 1.4 🎯 Da provare (✏️) · 🔍 — GB contro GiB e cancellazione

**Consegna (dati inventati).** Compri un disco esterno da **1 TB** dichiarato sulla confezione ($1\,000\,000\,000\,000$ byte).
1. Quando lo colleghi a Windows, quanti **GiB** (che Windows chiama spesso "GB") ti aspetti di vedere? ($1\text{ GiB} = 2^{30} = 1\,073\,741\,824\text{ byte}$).
2. Dopo averci copiato una cartella di foto, la elimini e svuoti il Cestino. Se il disco è un **HDD**, perché un programma di recupero riesce spesso a ritrovare le foto? E perché su un **SSD con TRIM** è molto più difficile?

<details>
<summary>🃏 <b>1.4 — Soluzione</b></summary>

1. $1\,000\,000\,000\,000 \div 1\,073\,741\,824 \approx \mathbf{931{,}32\text{ GiB}}$ (circa **931 GiB**). Lo spazio fisico è lo stesso, cambia solo la base di conteggio (1000 contro 1024).
2. Svuotando il Cestino il file system toglie solo la voce dal catalogo, lasciando i byte sul disco finché non vengono sovrascritti: su un HDD restano lì recuperabili. Su un SSD con **TRIM**, il sistema avvisa subito il controllore che quei blocchi sono liberi, e il controllore li azzera in fretta per preparare nuove scritture.

</details>

---

## 2 · 🚀 Dall'accensione al sistema operativo (S2)

📜 **Caso reale.** Sui PC con Windows e Linux in dual boot accade spesso un episodio noto dopo grandi aggiornamenti di Windows: al riavvio successivo il menu di **GRUB** sembra sparito e parte solo Windows. In realtà Linux e le sue partizioni sono ancora intatti sull'SSD: l'aggiornamento ha semplicemente rimesso il bootloader di Windows in cima all'**ordine di avvio UEFI**, e basta riportare GRUB al primo posto dalle impostazioni del firmware.

### 2.1 🟢 Svolto · ✅ (📖 + ✏️) — Staffetta di avvio e disco da 4 TB

**Consegna (scenario inventato).** Stai preparando un PC fisso nuovo con un **SSD da 4 TB** per installarci Windows e, in seguito, Linux.
1. Metti in ordine le sei tappe dall'accensione al sistema operativo: *Bootloader · Kernel e servizi · Accensione · POST · Firmware (UEFI) · Caricamento del SO*. Per il **firmware** e il **kernel**, indica dove risiedono all'inizio e dove lavorano.
2. Quale tabella delle partizioni devi scegliere sull'SSD da 4 TB tra **MBR** e **GPT**, e perché?

**Svolgimento.**
1. Ordine esatto: **1. Accensione → 2. Firmware (UEFI) → 3. POST → 4. Bootloader → 5. Caricamento del SO → 6. Kernel e servizi**.
   - Il **firmware** sta già in una memoria non volatile saldata sulla **scheda madre**.
   - Il **kernel** sta sul **disco** (SSD) e viene copiato in **RAM** dal bootloader per essere eseguito.
2. Devi scegliere **GPT**: lo schema **MBR** usa indirizzi a 32 bit per i settori da 512 byte ($2^{32} \times 512\text{ byte} \approx 2{,}2\text{ TB}$, cioè 2 TiB) e si ferma a **4 partizioni primarie**. Con MBR perderesti quasi metà dell'SSD da 4 TB; **GPT** invece supera il limite dei 2 TB, gestisce fino a 128 partizioni standard e mantiene una copia di sicurezza della mappa.

📌 **Controllo.** Controlla sempre che il PC usi **UEFI + GPT** quando il disco supera i 2 TB o installi sistemi moderni.

⚠️ **Errore comune:** credere che all'accensione la CPU carichi subito il sistema operativo dall'SSD. A PC appena acceso la RAM è vuota e la CPU non sa leggere né file system né dischi: serve prima il firmware dalla scheda madre.

> 🧠 <u>Il boot è una staffetta: il firmware sulla scheda madre controlla l'hardware (POST) e passa il testimone al bootloader sul disco, che carica il kernel in RAM.</u>

### 2.2 🎯 Da provare (📖) · ✅ — Partizioni di avvio e POST

**Consegna.** Rispondi in modo breve e preciso.
1. Quando accendi il PC, uno dei due banchi di RAM è staccato e senti una sequenza di bip senza nulla a schermo. Quale tappa della sequenza di avvio ha bloccato il PC e perché?
2. Apri *Gestione disco* su un PC Windows UEFI e vedi tre partizioni principali: una piccola **EFI (ESP)** da 260 MB in FAT32, la partizione `C:` in NTFS e una **partizione di ripristino**. A che cosa servono la prima e la terza?

<details>
<summary>🃏 <b>2.2 — Soluzione</b></summary>

1. Si è fermato al **POST** (*Power-On Self-Test*): il firmware controlla CPU e RAM prima di cercare il disco, perché senza RAM funzionante non c'è posto dove caricare bootloader e sistema operativo.
2. La **partizione EFI (ESP)** contiene i file dei **bootloader** (di Windows ed eventualmente di Linux) letti dalla UEFI; la **partizione di ripristino** contiene gli strumenti di emergenza per riparare il sistema se Windows non parte più.

</details>

### 2.3 🎯 Da provare (✏️) · ✅ — Piano per il dual boot Linux + Windows

**Consegna (scenario inventato).** La tua compagna Giulia vuole installare Ubuntu accanto a Windows 11 sullo stesso SSD da 512 GB (schema GPT, UEFI attivo). Prima di toccare il disco vuole verificare se Wi-Fi e audio funzionano.
Scrivi in ordine i passi corretti spiegando:
1. Come provare Ubuntu senza modificare l'SSD (quale strumento si usa e come si avvia dalla UEFI).
2. Le tre decisioni/operazioni del dual boot vero e proprio sullo spazio disco, sulla partizione EFI e su GRUB.
3. Quale precauzione va presa **prima** di ridurre la partizione di Windows.

<details>
<summary>🃏 <b>2.3 — Soluzione</b></summary>

1. Si prepara una **live USB** con Ubuntu e si entra nel setup **UEFI** (o nel menu di boot con tasti come F2/F12/Canc) per mettere la chiavetta al primo posto nell'**ordine di avvio**: Ubuntu gira in RAM senza scrivere sull'SSD.
2. Per il dual boot: (a) si riduce la partizione di Windows (`C:`) per creare spazio libero per le partizioni Linux (es. `ext4`); (b) si **condivide la stessa partizione EFI** già presente, aggiungendovi il bootloader di Linux senza crearne una seconda; (c) si installa **GRUB**, che all'accensione mostra il menu per scegliere tra Ubuntu e Windows.
3. Fare **sempre un backup** dei dati importanti su un disco esterno prima di toccare le partizioni.

</details>

### 2.4 🎯 Da provare (✏️) · 🔍 — Secure Boot, CSM e sicurezza GPT

**Consegna.** Risolvi i due quesiti.
1. Nel menu UEFI di un PC trovi attive le voci **Secure Boot** e disattivata la voce **CSM (Legacy)**. Spiega a che cosa serve ciascuna delle due voci e se devi disattivare Secure Boot per installare una distribuzione moderna come Ubuntu.
2. Perché uno sbalzo di corrente che danneggia i primi byte del disco è quasi sempre fatale su un disco **MBR**, mentre su un disco **GPT** il sistema ha molte più probabilità di recuperare la mappa delle partizioni?

<details>
<summary>🃏 <b>2.4 — Soluzione</b></summary>

1. **Secure Boot** controlla la firma digitale del bootloader per bloccare codice non riconosciuto prima dell'avvio del SO; le distribuzioni diffuse come Ubuntu hanno firma riconosciuta, quindi di norma non serve disattivarlo. **CSM** è la modalità di compatibilità che imita il vecchio BIOS per dischi MBR datati, e sui PC recenti resta disattivata.
2. Perché **GPT** salva una **copia di sicurezza** della tabella delle partizioni alla fine del disco e usa un controllo di integrità (CRC), mentre MBR ha una sola tabella nei primi 512 byte.

</details>

---

## 3 · 🖥️ Virtualizzazione (S3)

📜 **Caso reale.** Nel 1967 IBM sviluppò **CP-67** sul mainframe System/360 Model 67: un solo calcolatore grande quanto una stanza serviva decine di utenti nello stesso momento facendo credere a ciascuno di avere una macchina completa tutta per sé. La stessa idea regge oggi sia gli strumenti di prova sui nostri portatili (come VirtualBox) sia i server del cloud.

### 3.1 🟢 Svolto · ✅ (📖 + ✏️) — Quante VM regge il mio portatile?

**Consegna (scenario inventato).** Il tuo PC host ha **16 GB di RAM** e una CPU da **4 core**, con Windows 11 installato. Usi **VirtualBox** (hypervisor) per esercitarti con Linux.
1. Identifica **host**, **guest** e **hypervisor** nel tuo scenario, e specifica se l'hypervisor è di **Tipo 1** o **Tipo 2**.
2. Accendi **due** VM Linux assegnando **5 GB di RAM** a ciascuna. Quanta RAM rimane disponibile per Windows?
3. Se provi ad accendere una **terza** VM da **4 GB** nello stesso momento, che cosa succede al PC host?

**Svolgimento.**
1. **Host:** il tuo PC fisico (16 GB RAM, 4 core, Windows 11). **Hypervisor:** VirtualBox, che è di **Tipo 2 (*hosted*)** perché gira come applicazione sopra il sistema operativo dell'host. **Guest:** ciascuna VM Linux con il proprio sistema operativo.
2. Le due VM prendono $5 + 5 = 10\text{ GB}$ di RAM. All'host Windows restano $16 - 10 = \mathbf{6\text{ GB}}$ finché entrambe le VM restano accese.
3. Tre VM occuperebbero $5 + 5 + 4 = 14\text{ GB}$, lasciando solo **2 GB** a tutto Windows 11. O VirtualBox rifiuta di avviare la terza VM, oppure il sistema finisce la RAM libera, usa il disco come appoggio e rallenta tutto in modo evidente.

📌 **Controllo.** Somma della RAM assegnata alle VM accese + RAM minima per l'host $\le$ RAM fisica totale (16 GB).

⚠️ **Errore comune:** credere che una VM da 8 GB su un PC da 8 GB vada alla stessa velocità del PC fisico, oppure che più VM «creino» nuova RAM. Ogni risorsa viene tolta all'host.

> 🧠 <u>La RAM è quasi sempre il primo limite della virtualizzazione: ogni VM accesa sottrae una fetta reale di memoria all'host.</u>

### 3.2 🎯 Da provare (📖) · ✅ — Isolamento contro limite

**Consegna.** Rispondi in due frasi per ciascun punto.
1. Dentro una VM Linux apri un programma sperimentale difettoso che manda in crash il sistema guest. Perché Windows (l'host) e un'altra VM accesa continuano a funzionare? Come si chiama questa proprietà?
2. Un amico ti dice: *«Ho messo Linux in una VM su VirtualBox: ora gira più veloce del mio Windows perché è un sistema più leggero!»*. Perché questa affermazione è falsa dal punto di vista dell'hardware?

<details>
<summary>🃏 <b>3.2 — Soluzione</b></summary>

1. Si chiama **isolamento**: ogni guest gira in un ambiente separato e non può toccare la RAM né i file dell'host o delle altre VM (salvo cartelle condivise configurate apposta).
2. Perché una VM non è un secondo computer fisico: usa solo una fetta delle risorse dell'host (CPU condivisa a turni, meno RAM) e passa attraverso l'hypervisor, quindi non può superare le prestazioni dell'hardware reale.

</details>

### 3.3 🎯 Da provare (✏️) · ✅ — VM o dual boot?

**Consegna (scenario inventato).** Devi consigliare **macchina virtuale (S3)** oppure **dual boot (S2)** a due persone diverse:
- **Caso A:** Luca vuole solo provare i comandi base di Linux per due settimane, ma ha sul disco le tesine dell'anno e non vuole correre alcun rischio di toccare le partizioni.
- **Caso B:** Sara userà Linux tutti i giorni per montare video e compilare progetti grandi, sfruttando tutta la RAM e tutta la CPU del portatile.

Indica la scelta migliore per ciascuno motivando in base a **rischio**, **prestazioni** e **avvio/rimozione**.

<details>
<summary>🃏 <b>3.3 — Soluzione</b></summary>

- **Caso A (Luca) → Macchina virtuale:** zero rischi per le partizioni di Windows (il disco della VM è un singolo file), si avvia in una finestra e si cancella in un attimo quando non serve più.
- **Caso B (Sara) → Dual boot:** usa direttamente tutto l'hardware (CPU e RAM piene, senza l'intermediazione dell'hypervisor), anche se richiede più attenzione alle partizioni, backup iniziale e riavvio per cambiare sistema tramite GRUB.

</details>

### 3.4 🎯 Da provare (✏️) · 🔍 — Hypervisor di Tipo 1 vs Tipo 2 e disco virtuale

**Consegna.** Completa i due punti.
1. Un'azienda ha un server potente su cui deve far girare 12 VM diverse con il minor spreco possibile di risorse. Sceglie un hypervisor di **Tipo 1 (*bare-metal*)** o di **Tipo 2 (*hosted*)**? Spiega la differenza architetturale tra i due tipi e fai almeno un esempio reale per ciascuno.
2. Che cosa vede il sistema guest al posto del disco, e che cos'è invece in realtà quel disco sul PC host? Che cosa implica questo per i backup della VM?

<details>
<summary>🃏 <b>3.4 — Soluzione</b></summary>

1. Sceglie il **Tipo 1 (*bare-metal*)**, come VMware ESXi, Proxmox VE o Microsoft Hyper-V, perché gira direttamente sull'hardware senza un sistema operativo ospite sotto che consuma risorse. Il **Tipo 2 (*hosted*)**, come VirtualBox o VMware Workstation, è un programma installato sopra il SO dell'host (adatto per uso personale e didattico).
2. Il guest vede un normale disco con le sue partizioni (es. EFI ed `ext4`), ma sull'host quel disco è un **singolo file** (es. `.vdi`): per questo è facilissimo copiarlo per farne un backup prima di un esperimento.

</details>

---

## 4 · 🏭 Pipelining, parallelismo e set di istruzioni (S4)

📜 **Caso reale.** Intorno al **2004–2005** la corsa alla frequenza di clock si fermò contro il **muro dei GHz** (e del calore): i Pentium 4 (*Prescott*) superarono i 3,8 GHz scaldando moltissimo. Nel 2005 Intel e AMD portarono sul mercato di massa i primi **dual core** (Pentium D e Athlon 64 X2): invece di spingere un solo core sempre più veloce, si affiancarono più core e si sfruttò il parallelismo a più livelli.

### 4.1 🟢 Svolto · ✅ (📖 + ✏️) — Da CISC a RISC, pipeline e hazard

**Consegna (notazione di ottobre, valori inventati).** Considera l'operazione CISC `ADD [40], R2` (aggiungi `R2` al valore in memoria alla cella `40` e riscrivi nella cella `40`).
1. Riscrivi questa operazione in stile **RISC** usando `LOAD`, `ADD`, `STORE` e il registro `R1`. Quante istruzioni servono?
2. Supponi ora di avere **6 istruzioni** indipendenti su una pipeline ideale a **5 stadi** (`IF, ID, EX, MEM, WB`), dove ogni stadio dura **1 ciclo**. Calcola i cicli totali **con** la pipeline e **senza** pipeline.
3. Nella tua sequenza RISC del punto 1 (`LOAD R1, [40]` seguita subito da `ADD R1, R1, R2`), quale **hazard** nasce e perché?

**Svolgimento.**
1. In stile RISC la memoria si tocca solo con `LOAD` e `STORE`, quindi servono **3 istruzioni**:
   - `LOAD R1, [40]`
   - `ADD R1, R1, R2`
   - `STORE [40], R1`
2. **Con pipeline (modello ideale):** $\text{cicli} = \text{stadi} + (\text{istruzioni} - 1) = 5 + (6 - 1) = \mathbf{10\text{ cicli}}$.
   **Senza pipeline:** $\text{cicli} = 5 \times 6 = \mathbf{30\text{ cicli}}$. La pipeline completa lo stesso blocco di 6 istruzioni in un terzo del tempo.
3. Nasce un **hazard di dati**: la `ADD` vuole usare subito `R1`, ma `LOAD` legge il dato dalla memoria solo nello stadio `MEM` e lo scrive in `R1` nello stadio `WB`.

📌 **Controllo.** $5 + (6 - 1) = 10$: il primo risultato esce al ciclo 5 (`IF, ID, EX, MEM, WB`), poi esce un'istruzione nuova a ogni ciclo dal 6 al 10.

⚠️ **Errore comune:** scrivere `cicli = stadi × istruzioni` anche con la pipeline, oppure dire che la pipeline dimezza la durata della singola istruzione (la latenza di una singola istruzione resta **5 cicli**; aumenta il **throughput**).

> 🧠 <u>Le istruzioni RISC a lunghezza fissa facilitano la pipeline; la pipeline non accorcia la singola istruzione, ma aumenta il throughput.</u>

### 4.2 🎯 Da provare (📖) · ✅ — CISC, RISC e latenza contro throughput

**Consegna.** Rispondi in modo breve.
1. Perché la **lunghezza fissa** delle istruzioni RISC aiuta il processore a lavorare in parallelo rispetto alle istruzioni a lunghezza variabile tipiche dei CISC?
2. Un compagno afferma: *«Con una pipeline a 5 stadi, una singola istruzione diventa 5 volte più veloce»*. Correggilo usando i termini **latenza** e **throughput**.

<details>
<summary>🃏 <b>4.2 — Soluzione</b></summary>

1. Con lunghezza fissa la CPU sa già dove inizia l'istruzione successiva ancora prima di aver finito di decifrare quella precedente, quindi può caricare e mettere in catena le istruzioni subito.
2. È falso: la **latenza** di una singola istruzione (tempo dall'ingresso all'uscita) resta 5 cicli; la pipeline aumenta invece il **throughput**, cioè il numero di istruzioni completate nell'unità di tempo (a regime, 1 al ciclo).

</details>

### 4.3 🎯 Da provare (✏️) · ✅ — Concorrenza, Amdahl e Python

**Consegna (dati inventati).** Risolvi i tre punti.
1. Distingui con un esempio **concorrenza** e **parallelismo** (e nomina la differenza tra **core** e **thread**).
2. Un programma su **1 core** dura **100 secondi**: **70 secondi** sono una parte obbligatoriamente sequenziale (lettura e unione dei file) e **30 secondi** possono essere divisi su più core. Se lo esegui su un PC con **3 core**, il tempo totale può scendere sotto i 70 secondi? Perché?
3. Devi scrivere due script in Python (CPython) su un PC con 8 core:
   - **Script A:** scarica i titoli di 40 pagine web (attesa di rete).
   - **Script B:** calcola migliaia di numeri primi pesanti (calcolo puro).
   Quale libreria usi in A e quale in B fra `threading` e `multiprocessing`, e che ruolo ha il **GIL**?

<details>
<summary>🃏 <b>4.3 — Soluzione</b></summary>

1. Nella **concorrenza** più lavori avanzano nello stesso periodo alternandosi a turno su una sola risorsa (es. un cuoco che cambia pentola); nel **parallelismo** vengono eseguiti davvero nello stesso istante fisico su più unità (es. più cuochi su più fornelli). Il **core** è l'unità hardware fisica; il **thread** è un flusso di esecuzione software assegnato dal SO a un core.
2. **No**, resterà sempre sopra i **70 secondi** (circa $70 + 30 \div 3 = 80$ s nel caso ideale): per la **legge di Amdahl**, la parte sequenziale che non si può dividere fa da collo di bottiglia.
3. In **Script A** (*I/O-bound*) va bene `threading` (o `asyncio`): mentre un thread aspetta la rete rilascia il **GIL** e un altro lavora. In **Script B** (*CPU-bound*) serve `multiprocessing`: in CPython il **GIL** lascia eseguire codice Python a un solo thread alla volta nello stesso processo, quindi per usare davvero più core servono processi separati, ognuno con il proprio interprete e il proprio GIL.

</details>

### 4.4 🎯 Da provare (✏️) · 🔍 — Griglia a 5 stadi, hazard e race condition

**Consegna.** Risolvi i due punti.
1. Disegna su carta (o in tabella) la griglia dei cicli per **4 istruzioni indipendenti** (`I1..I4`) su una pipeline ideale a **5 stadi** (`IF, ID, EX, MEM, WB`) e verifica quanti cicli servono in tutto. Poi indica che tipo di hazard (tra *strutturale*, *di dati* e *di controllo*) si verifica in ciascuno di questi casi:
   - (a) Un `if` cambia strada dopo che la CPU ha già caricato l'istruzione seguente.
   - (b) Due stadi vogliono accedere nello stesso ciclo all'unica memoria disponibile.
   - (c) `LOAD R1, [10]` seguito subito da `ADD R3, R1, R2`.
2. Nel tuo script Python multithread due thread aggiornano la stessa variabile `saldo = 100` aggiungendo `10` nello stesso momento, e alla fine trovi `110` invece di `120`. Come si chiama questo problema e quale strumento si usa per evitarlo?

<details>
<summary>🃏 <b>4.4 — Soluzione</b></summary>

1. Con 4 istruzioni su 5 stadi servono $5 + (4 - 1) = \mathbf{8\text{ cicli}}$:
   - `I1`: `IF` (1), `ID` (2), `EX` (3), `MEM` (4), `WB` (5)
   - `I2`: `IF` (2), `ID` (3), `EX` (4), `MEM` (5), `WB` (6)
   - `I3`: `IF` (3), `ID` (4), `EX` (5), `MEM` (6), `WB` (7)
   - `I4`: `IF` (4), `ID` (5), `EX` (6), `MEM` (7), `WB` (8)
   Hazard: (a) **di controllo**; (b) **strutturale**; (c) **di dati**.
2. È una **race condition** (*corsa critica*). Si evita proteggendo la risorsa condivisa con un **lock** (o *mutex*), in modo che un solo thread alla volta possa leggere e aggiornare il dato.

</details>

### 🤓 Oltre la CPU: OpenMP e GPU

In C/C++ (a differenza di Python con il GIL) basta una direttiva **OpenMP** come `#pragma omp parallel for` per far dividere un ciclo `for` dal compilatore fra i core della CPU. Quando invece il lavoro è fare la stessa operazione matematica su milioni di numeri nello stesso istante (parallelismo puro sui dati), entra in gioco la **GPU** con migliaia di core piccoli e semplici, usata per grafica e intelligenza artificiale (con **CUDA** o **OpenCL**).

---

## 📚 Fonti e risorse

- [Backblaze Hard Drive Test Data](https://www.backblaze.com/cloud-storage/resources/hard-drive-test-data) (in inglese): utile per vedere statistiche reali su guasti e limiti di SMART nei data center.
- [TRIM — Wikipedia IT](https://it.wikipedia.org/wiki/TRIM) e [S.M.A.R.T. — Wikipedia IT](https://it.wikipedia.org/wiki/S.M.A.R.T.): approfondimento su pulizia blocchi SSD e autodiagnosi.
- [GUID Partition Table — Wikipedia IT](https://it.wikipedia.org/wiki/GUID_Partition_Table) e [GRUB — Wikipedia IT](https://it.wikipedia.org/wiki/GRUB): dettagli su GPT, copia di sicurezza e menu di avvio dual boot.
- [CP-67 — Wikipedia EN](https://en.wikipedia.org/wiki/CP-67) e [Hypervisor — Wikipedia EN](https://en.wikipedia.org/wiki/Hypervisor): storia delle prime VM e confronto tra hypervisor di Tipo 1 e Tipo 2.
- [Instruction pipelining — Wikipedia EN](https://en.wikipedia.org/wiki/Instruction_pipelining) e [Legge di Amdahl — Wikipedia IT](https://it.wikipedia.org/wiki/Legge_di_Amdahl): stadi della pipeline, hazard e limite sequenziale.
- [concurrent.futures — Python Docs](https://docs.python.org/3/library/concurrent.futures.html): documentazione ufficiale per provare `ThreadPoolExecutor` e `ProcessPoolExecutor`.

---

⬅️ [S5 - Ripasso e collegamenti](./%28STU%29%203EI%20nov-dic%20S5%20-%20Ripasso%20e%20collegamenti.md) · 🏠 [Indice](../README.md)
