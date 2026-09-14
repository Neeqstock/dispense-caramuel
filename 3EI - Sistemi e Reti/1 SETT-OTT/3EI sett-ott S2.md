# SETTIMANA 2: Il Modello di Von Neumann e i Bus di Sistema

Ecco il kit didattico completo per la **Settimana 2**, strutturato come una **mappa concettuale espansa (mindmap ad albero)** con tutti i contenuti pronti per essere spiegati alla lavagna e svolti al PC.

> Nota: il quadro sinottico delle 8 settimane e il dettaglio sintetico settimana per settimana si trovano in [3EI - SETT-OTT.md](3EI%20-%20SETT-OTT.md).

---

# 🗺️ SETTIMANA 2: VON NEUMANN, I BUS E LE AUTOSTRADE DEL COMPUTER

```text
SETTIMANA 2
├── 🧠 LEZIONE 1: TEORIA (2 ORE IN AULA)
│   ├── [1.1] Cos'è l'Architettura di Von Neumann
│   ├── [1.2] I 4 Blocchi Fondamentali (CPU, Memoria, I/O, Bus)
│   ├── [1.3] Il Collo di Bottiglia di Von Neumann
│   └── [1.4] Confronto breve: Von Neumann vs Harvard (cenno)
│
├── 💻 LEZIONE 2: LABORATORIO (2 ORE CON ITP)
│   ├── [2.1] Anatomia Esterna del Case (Form Factor, Connettori)
│   ├── [2.2] La Scatola Nera: Apertura Sicura e Regole
│   ├── [2.3] L'Alimentatore (PSU): Trasformazione AC → DC
│   ├── [2.4] Tensioni Standard e Connettori Ricorrenti
│   └── [2.5] Esercitazione Pratica (Missione: "Ispezione Sotto Controllo")
│
└── 📋 GUIDA DI REGIA PER IL DOCENTE
    ├── Scaletta Minuto per Minuto
    ├── Schema da Disegnare alla Lavagna
    └── Micro-Task di Consolidamento (Formative Assessment)
```

---

## 🧠 MODULO TEORICO (2 Ore in Aula)

### ├── [1.1] Cos'è l'Architettura di Von Neumann
*Obiettivo: presentare il modello architetturale "classico" che regge tutti i computer moderni.*

* 📌 **John von Neumann (1903–1957):** matematico ungherese che nel 1945–1950 propone un'architettura di riferimento per i calcolatori digitali basata su **5 componenti fondamentali:**
  1. **Unità di ingresso** (input devices)
  2. **Unità di elaborazione** (CPU / Processore)
  3. **Unità di memorizzazione** (Memory)
  4. **Unità di uscita** (output devices)
  5. **Un bus che connette il tutto** (sistema di comunicazione interna)

* 🎯 **Intuizione geniale:** anziché costruire computer monolitici ad hoc, Von Neumann propone un **paradigma modulare e generalista** che ha dimostrato di essere scalabile da 70 anni:
  * Puoi cambiare la CPU e il resto rimane uguale.
  * Puoi aggiungere una nuova periferica senza riprogettare l'intera architettura.
  * Tutto comunica attraverso il medesimo **sistema di bus**, come macchine su un'autostrada.

---

### ├── [1.2] I 4 Blocchi Fondamentali + Bus
*Obiettivo: visualizzare i blocchi e le loro relazioni, fondamento per le settimane a seguire.*

```text
                      L'ARCHITETTURA DI VON NEUMANN
                      
     ┌──────────────────────────────────────────────┐
     │            UNITÀ DI CONTROLLO               │
     │         (Coordina tutto il flusso)           │
     └──────────────────────────────────────────────┘
                    │                   
      ┌─────────────┼─────────────┐
      │             │             │
      ▼             ▼             ▼
 ┌─────────┐  ┌──────────┐  ┌──────────┐
 │   CPU   │  │ MEMORIA  │  │ PERIFERICHE│
 │(Calcoli)│  │(Dati+Cod)│  │(Input/Out)│
 └─────────┘  └──────────┘  └──────────┘
      │             │             │
      └─────────────┼─────────────┘
                    │
              ═══════════════════
              ║  SISTEMA DI BUS ║
              ║ (Data/Addr/Ctrl)║
              ═══════════════════
```

* 🧠 **CPU (Unità Centrale di Elaborazione):**
  * Contiene l'ALU (Arithmetic Logic Unit) che fa calcoli e confronti.
  * Contiene i registri (memorie microscopiche molto veloci).
  * Contiene la Control Unit (direttore d'orchestra) che decodifica i comandi.
  * Tipicamente frequenza moderna: 2–5 GHz (miliardi di operazioni al secondo).

* 💾 **Memoria (RAM, ROM, e di massa):**
  * Dove risiedono i dati e il programma che la CPU dovrà eseguire.
  * Separata dalla CPU (a differenza dell'architettura Harvard dei microcontrollori).
  * Accesso tramite il bus indirizzi: la CPU dice "voglio il dato all'indirizzo 1000" e la memoria lo fornisce via bus dati.

* 📤 **Periferiche (Input / Output):**
  * Tastiera, mouse, monitor, stampante, scheda di rete, ecc.
  * Comunicano col resto della macchina tramite il bus di controllo e handshaking protocol.
  * Possono essere molto lente rispetto alla CPU (un monitor aggiorna 60 volte al secondo, la CPU bilioni).

* 🛣️ **Il Bus di Sistema:**
  * L'infrastruttura che connette tutto.
  * Fisicamente: piste di rame sulla scheda madre, che trasportano segnali in parallelo.
  * Logicamente: tre componenti (Data Bus, Address Bus, Control Bus) che vedremo nel prossimo paragrafo.

---

### ├── [1.3] Il Collo di Bottiglia di Von Neumann
*Obiettivo: mostrare il compromesso architetturale che ancora oggi limita le prestazioni.*

* ⚠️ **Il Problema:** CPU, Memoria e Periferiche comunicano tramite un **unico bus condiviso**. Se il bus è saturo, tutto rallenta — proprio come un'autostrada a una corsia che collega tre città: se tutte le auto cercano di passare contemporaneamente, il traffico crolla.

```text
        Velocità della CPU: ~GHz (miliardi op/sec)
                    ▼
            ══════════════════ ← Bottleneck (solo qualche GB/sec)
                    ▲
    Velocità della Memoria: ~GB/sec
```

* 📊 **Esempio numerico (ordini di grandezza):**
  * CPU moderna: 10 miliardi di istruzioni per secondo ($10^{10}$ op/s).
  * Se ogni istruzione richiede di andare in memoria, e la memoria può fornire 10 miliardi di byte al secondo ($10^{10}$ bytes/s)...
  * ... in teoria vanno a pari. **Ma nella pratica:** non tutte le istruzioni accedono alla memoria; alcune operano sui registri (velocissimi). È qui che la memoria cache (Settimana 5) risolve il problema sfruttando la **località**.

* 🔧 **Soluzioni architetturali (cenni):**
  * **Bus ad alta velocità:** nuovi standard (PCIe, Thunderbolt) a decine di GB/s.
  * **Multipath:** in chip moderni, ci sono più vie di comunicazione interna, non un unico bus.
  * **Memoria Cache:** metti piccole quantità di memoria velocissima vicino alla CPU, in modo da ridurre gli accessi lenti alla RAM.

---

### ├── [1.4] Confronto breve: Von Neumann vs Harvard
*Obiettivo: dare contesto storico, mostrare che esistono alternative (anche se meno comuni).*

```text
┌───────────────────────────────┬────────────────────────────────┐
│      VON NEUMANN              │         HARVARD                │
├───────────────────────────────┼────────────────────────────────┤
│ Una sola memoria              │ Due memorie separate           │
│ (dati e istruzioni            │ (una per istruzioni,           │
│  mescolati)                   │  una per dati)                 │
│                               │                                │
│ ✓ Progettazione semplice      │ ✓ Fetch istruzione parallelo   │
│ ✓ Memoria flessibile          │   a lettura dati               │
│ ✗ Collo di bottiglia          │ ✓ Potenzialmente più veloce    │
│                               │ ✗ Progettazione complessa      │
├───────────────────────────────┼────────────────────────────────┤
│ Usato in: PC, server,         │ Usato in: microcontrollori     │
│ workstation (macchine         │ (Arduino), DSP, processori     │
│ "generiche")                  │ specializzati (segnali)        │
└───────────────────────────────┴────────────────────────────────┘
```

* 📌 **Per il resto di Sistemi e Reti (tutto il primo bimestre), lavoriamo su architettura von Neumann,** perché è quella di qualsiasi PC / server che smontate in laboratorio.

---

## 💻 MODULO LABORATORIO (2 Ore con ITP)

### ├── [2.1] Anatomia Esterna del Case: Form Factor e Standard
*Obiettivo: riconoscere gli standard costruttivi dei case, fondamentali per il cablaggio e l'upgrade.*

* 📦 **Fattori di forma (Form Factor) comuni:**
  * **ATX (Advanced Technology eXtended):** lo standard "full-size", case grande, scheda madre 305 × 244 mm. Quello più diffuso nei PC desktop e negli ambienti scolastici/aziendali.
  * **Micro-ATX (M-ATX):** versione ridotta, scheda madre 244 × 244 mm, footprint più piccolo. Ideale per HTPC (home theater PC) o postazioni compatte.
  * **Mini-ITX:** ancora più piccolo, scheda madre 170 × 170 mm, per PC ultra-compatti (media center, embedded systems).

* 🔌 **Connettori esterni ricorrenti sul retro del case:**
  * **Presa di alimentazione (IEC 60320):** connettore a tre buchi dove si collega il cavo di rete (230V AC, EU) o (110V AC, USA).
  * **Porte USB:** Type-A (rettangolari, le classiche), Type-C (reversibili, nuove), Mini/Micro (periferiche).
  * **Jack audio (3.5 mm):** mic, speaker, line-in, line-out (colori codificati: rosa = mic, azzurro = line-in, verde = speaker).
  * **Porta di rete (Ethernet RJ-45):** connettore dalla scheda di rete.
  * **Porte Legacy (sempre meno comuni):** parallela (stampante vecchia), seriale (DB-9), S-Video (TV analogica).

* 🌡️ **Aperture di ventilazione:**
  * Il case ha fori o griglie per il passaggio dell'aria.
  * Regola d'oro in laboratorio: **mai bloccare le prese d'aria** (es. con giornali, polvere, cavi arrotolati) — il computer rischia il surriscaldamento.

---

### ├── [2.2] La Scatola Nera: Apertura Sicura e Regole di Laboratorio
*Obiettivo: standardizzare la procedura di apertura del case, minimizzando i rischi ESD e di danni meccanici.*

* 🔓 **Procedura di apertura sicura (checklist):**
  1. **Spegnere completamente il computer** (power button → arresto → attendere 5 secondi).
  2. **Staccare il cavo di alimentazione** dalla presa a muro (non solo dal computer).
  3. **Indossare il braccialetto antistatico** e collegarlo a terra / al telaio del case.
  4. **Attendere 10–15 secondi** perché l'energia residua nei condensatori si discarichi (importante!).
  5. **Individuare le viti di chiusura** del pannello laterale (di solito 2–4 viti, talvolta anche leve a pulsante).
  6. **Svitare lentamente** senza forzare; se una vite è incastrata, usa un cacciavite a croce della giusta misura (non troppo grande che scivoli, non troppo piccolo che non abbia grip).
  7. **Togliere il pannello laterale** scivolando verso dietro (non tirando verso l'alto, che potrebbe danneggiare i cavi interni).
  8. **Posare il pannello in un'area designata**, non in mezzo al tavolo dove potrebbe cadere.

* ⚠️ **Regole d'oro:**
  * **Non toccare i componenti se non è necessario.** Lo scopo della prima ispezione è osservare, non manipolare.
  * **Tocca sempre il telaio metallico del case prima di toccare un componente** (mantenendo il braccialetto allacciato).
  * **Lavora su un tappetino antistatico** con il case poggiato su di esso.
  * **Se devi estrarre un modulo RAM per ispezione,** tieni il braccialetto allacciato, afferra il modulo dai bordi (non dai pin dorati), estrai sollevando leggermente e scorrendo.

---

### ├── [2.3] L'Alimentatore (PSU): Trasformazione AC → DC
*Obiettivo: smontare il "black box" dell'alimentatore, capire come converte la corrente alternata in corrente continua stabilizzata.*

* ⚡ **Quello che entra: AC (Corrente Alternata)**
  * Dalla presa a muro: 230V AC (Europa) o 110V AC (USA/Giappone), 50/60 Hz.
  * "AC" significa che la tensione oscilla sinusoidalmente tra +V e −V cento volte al secondo (50 Hz).

* 🔄 **Quello che deve uscire: DC (Corrente Continua) a tensioni multiple e stabili**
  * **+3.3V** (per logica digitale moderna, bus I/O veloci).
  * **+5V** (per logica tradizionale, alcuni sensori, ventole low-power).
  * **+12V** (per motori, ventole ad alta corrente, schede di espansione).
  * **−12V** (raramente usato, per alcune interfacce di controllo legacy).
  * (Meno frequente: **+5V Standby**, per wake-on-LAN).

* 🔧 **Come avviene la conversione (semplificato):**
  1. **Trasformatore:** riduce (step-down) i 230V AC a ~30V AC.
  2. **Raddrizzatore (diodi/ponte di Graetz):** converte AC in DC "grezzo" (ondulato).
  3. **Filtro (condensatori):** livella l'ondulazione del DC grezzo.
  4. **Regolatore (IC switching):** stabilizza la tensione alle soglie nominali (3.3V, 5V, 12V, −12V).

* 💡 **Perché è "switchato" (switching PSU)?**
  * I vecchi alimentatori lineari erano huge e caldi.
  * Gli alimentatori switching moderni usano transistor che si accendono/spengono milioni di volte al secondo, per uno switching veloce e efficionzia energetica (80–95% vs 60% dei lineari).

---

### ├── [2.4] Tensioni Standard e Connettori Ricorrenti
*Obiettivo: riconoscere al volo i connettori e le tensioni, essenziale per troubleshooting e upgrade.*

```text
CONNETTORI RICORRENTI DELL'ALIMENTATORE

Connettore                Tensioni           Dispositivi tipici
────────────────────────────────────────────────────────────────
Molex (4-pin)          +12V (2), +5V, GND    Ventole, schede IDE legacy
SATA Power (L-shape)   +3.3V, +5V, +12V     Dischi SSD/HDD, schede espansione
24-pin ATX (rettang.)  Tutti (+3.3, +5,     Scheda madre (connessione primaria)
                        +12V, −12V, GND)
4-pin/8-pin CPU        +12V (multiple)      Processore (alimentazione dedicata)
6-pin/8-pin PCIe       +12V (multiple)      Schede video discrete (GPU)
3-pin Fan (jasper)     +12V, GND, Tach      Ventole (sensore velocità)
```

* 🔍 **Come si riconoscono:** ogni connettore ha **forme geometriche diverse**, per evitare inserimenti errati (specie gli 8-pin CPU e PCIe, che somigliano ma sono di fatto incompatibili, protetti da piccole sporgenze).

* ⚠️ **Errore comune:** inserire il connettore al contrario o parzialmente. La regola: **deve entrare facile, senza forzare**. Se devi spingere forte, stai sbagliando direzione o allineamento.

---

### ├── [2.5] Esercitazione Pratica Guidata al PC (Durata: 70–80 minuti)

#### FASE A: Ricognizione esterna (10 min)
1. Ogni studente (o coppia) riceve un case di un PC da laboratorio (spento, cavo staccato).
2. **Missione:** trovare e nominare:
   * Il form factor (ATX, M-ATX, Mini-ITX?).
   * Tre connettori esterni sul retro.
   * Le aperture di ventilazione.
   * Il punto di chiusura del pannello laterale.

#### FASE B: Preparazione e apertura sicura (15 min)
1. Indossare braccialetto antistatico e collegarlo al telaio.
2. Aprire il case seguendo la procedura della scaletta (viti, pannello, attesa pre-apertura).
3. Osservare l'interno senza toccare nulla.

#### FASE C: Identificazione dell'alimentatore (20 min)
1. Localizzare la PSU (solitamente in basso a destra nel case ATX).
2. **Senza estrarre la PSU**, osservarne:
   * Il ventilatore di raffreddamento (qualche mm di diametro, ventilazione verso il basso per aspirare aria fredda dal fondo).
   * I 4–5 fasci di cavi che escono (colori: rossi +12V, gialli +12V legacy, bianchi −12V, neri GND, arancioni +3.3V).
   * L'etichetta posteriore con specifiche di potenza (es. "650W", efficienza "80+ Gold").
3. Tracciare un collegamento cavi: partendo da un connettore Molex, dire a voce alta quale tensione ha e dove andrà tipicamente (ventola, disco, scheda expansion).

#### FASE D: Esame della scheda madre (15 min)
1. Puntare col dito i connettori principali della scheda madre:
   * **Slot di alimentazione 24-pin ATX** (dove arriva la corrente).
   * **Slot 4-pin/8-pin CPU** (alimentazione dedicata del processore).
   * **Slot 6-pin/8-pin PCIe** (se presente, per GPU).
2. Contare i fasci di cavi rossi/gialli/neri che arrivano da quelle zone.
3. Discutere: *«Se uno di questi connettori si allentasse, cosa succederebbe al computer?»*

#### FASE E: Chiusura ordinata e riflessione (10 min)
1. Chiudere il case seguendo la procedura inversa (pannello, viti, braccialetto).
2. **Mini-test formativo orale (in plenaria):**
   * *«Quante tensioni fornisce un alimentatore moderno? Quali?»*
   * *«Se il computer non si accende, cosa potrebbe essere scollato?»*
   * *«Perché il braccialetto antistatico è importante?»*

---

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma Lezione Teorica (110 min, 2h)
* **00-10 min | Accoglienza e recap Settimana 1:** breve ripasso della scorsa lezione (transistor → microprocessore, parte operativa/controllo).
* **10-25 min | L'Hook di apertura:** chiedi *«Se dovessero disegnare all'improvviso il computer, cosa disegnereste?»*. Aspettati risposte caotiche (monitor, tastiera, scatola), poi arriva a "esistono blocchi interni collegati tra loro".
* **25-50 min | Lezione frontale con disegni:** introduce la struttura di Von Neumann (4 blocchi + bus), disegna lo schema alla lavagna step-by-step.
* **50-70 min | Il collo di bottiglia:** spiega il concetto di bandwidth, facendo esempi di traffico stradale. Mostra numericamente come la CPU sia più veloce della memoria.
* **70-90 min | Breve confronto Von Neumann vs Harvard:** disegna i due schemi a confronto, sottolinea che il nostro corso riguarda Von Neumann.
* **90-110 min | Chiusura e domande:** 4 domande rapide di verifica (*«Quali sono i 4 blocchi?»*, *«Cosa connette tutto?»*, *«Perché c'è un collo di bottiglia?»*, *«Mi fate un esempio di una periferica»*).

### ✍️ Disegni Guida da fare alla Lavagna (Lezione 1)

```text
DISEGNO 1: I 4 BLOCCHI + BUS
    
         CPU              MEMORIA           PERIFERICHE
        (Calcoli)        (Dati/Codice)     (Input/Output)
         │                  │                   │
         └──────────────────┼───────────────────┘
                            │
                    ══════════════════
                    ║  SISTEMA BUS  ║
                    ══════════════════

DISEGNO 2: IL COLLO DI BOTTIGLIA
    
    CPU (veloce: GHz)  ──►  ═══════════════════════  ──►  MEMORIA (lenta: ns)
                          (throughput limitato = bottleneck)
```

### 🎯 Micro-Task Formativa per Casa (Spaced Retrieval - 5 minuti)
Carica su Google Classroom questo compito (senza voto punitivo):
> *"Disegna i 4 blocchi di Von Neumann in una pagina e descrivili in 1-2 righe cada. Bonus: disegna le frecce che mostrano come comunicano via bus."*

Da completare inoltre entro la lezione successiva: **primo quiz del Capitolo 2 di IT Essentials su NetAcad (Hardware del PC)**.
