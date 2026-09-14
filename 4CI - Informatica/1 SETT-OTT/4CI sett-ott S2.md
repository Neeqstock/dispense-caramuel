Ecco il kit didattico completo per la **Settimana 2**, strutturato come una **mappa concettuale espansa (mindmap ad albero)** con tutti i contenuti pronti per essere spiegati alla lavagna e svolti al PC.

> Nota: il quadro sinottico delle 8 settimane e il dettaglio sintetico settimana per settimana si trovano in [4CI - SETT-OTT.md](4CI%20-%20SETT-OTT.md).

---

# 🗺️ SETTIMANA 2: COSTRUTTORI E L'ARTE DI NASCERE BENE

```text
SETTIMANA 2
├── 🧠 LEZIONE 1: TEORIA (3 ORE IN AULA)
│   ├── [1.1] Il Problema: Animali "Nudi" Appena Creati
│   ├── [1.2] Il Costruttore: Nascere Già Pronti
│   ├── [1.3] Costruttori Sovraccaricati
│   └── [1.4] Cenno al Costruttore di Copia
│
├── 💻 LEZIONE 2: LABORATORIO (3 ORE CON ITP) — PARTE 2 DEL PROGETTO "LA STALLA"
│   ├── [2.1] Refactoring: Dalla Classe Nuda ai Costruttori
│   ├── [2.2] Istanziazione con Costruttori Diversi
│   ├── [2.3] La Parola Chiave `this`
│   └── [2.4] Esercitazione Pratica Guidata (Missione: "La Stalla Nasce Già Pronta")
│
├── 🐔 ESERCIZI PRATICI — LA STALLA (Settimana 2)
│
└── 📋 GUIDA DI REGIA PER IL DOCENTE
    ├── Scaletta Minuto per Minuto
    ├── Schema da Disegnare alla Lavagna
    └── Micro-Task di Consolidamento (Formative Assessment)
```

---

## 🧠 MODULO TEORICO (3 Ore in Aula)

### ├── [1.1] Il Problema: Animali "Nudi" Appena Creati
*Obiettivo: creare la necessità pedagogica del costruttore, partendo da un problema concreto vissuto in Settimana 1.*

* ⚠️ **Il problema visto la scorsa settimana:** quando scriviamo `new Animale()`, l'oggetto nasce con attributi vuoti/a zero (`null` per le stringhe, `0` per i numeri) e dobbiamo assegnarli **riga per riga** dopo la creazione.
* 🐌 **Perché è scomodo e rischioso:**
  * Codice ripetitivo: ogni volta 3-4 righe per popolare un oggetto.
  * Rischio di dimenticare un'assegnazione, lasciando l'oggetto in uno stato incompleto/inconsistente (un pollo con `numeroZampe = 0` per dimenticanza è un problema serio!).
* 🎯 **La soluzione che introduciamo oggi:** un meccanismo che permetta di **nascere già con i valori giusti**, in un'unica riga di codice.

---

### ├── [1.2] Il Costruttore: Nascere Già Pronti
*Obiettivo: definire formalmente il costruttore, distinguendo quello di default da quello esplicito.*

```text
              SENZA COSTRUTTORE ESPLICITO           CON COSTRUTTORE ESPLICITO
        ┌───────────────────────────────┐    ┌───────────────────────────────┐
        │ Animale a = new Animale();    │    │ Animale a = new Animale(      │
        │ a.nome = "Coccodè";           │    │     "Coccodè", "Coccodè!",     │
        │ a.verso = "Coccodè!";         │    │     2, 1.8);                   │
        │ a.numeroZampe = 2;            │    │                               │
        │ a.peso = 1.8;                 │    │ (già tutto pronto in 1 riga!) │
        └───────────────────────────────┘    └───────────────────────────────┘
```

* 🏗️ **Costruttore di default (implicito):** se non scriviamo nessun costruttore, Java ne fornisce uno vuoto automaticamente (`Animale() {}`), che non inizializza nulla di significativo.
* ✍️ **Costruttore esplicito con parametri:**
  ```java
  public class Animale {
      String nome, verso;
      int numeroZampe;
      double peso;

      Animale(String n, String v, int z, double p) {
          nome = n;
          verso = v;
          numeroZampe = z;
          peso = p;
      }
  }
  ```
* 📐 **Regole sintattiche fondamentali:**
  * Il costruttore ha **lo stesso nome della classe**.
  * **Non ha tipo di ritorno** (nemmeno `void`).
  * Viene invocato automaticamente con `new NomeClasse(argomenti)`.

---

### ├── [1.3] Costruttori Sovraccaricati
*Obiettivo: mostrare che una classe può offrire più "modalità di nascita" a seconda delle informazioni disponibili.*

* 🔀 **Costruttori sovraccaricati:** più costruttori nella stessa classe, con **firme diverse** (numero e/o tipo di parametri differenti).
  ```java
  Animale(String n, String v, int z, double p) { ... }  // costruttore completo
  Animale(String n, String v) {                          // costruttore parziale
      nome = n; verso = v;
      numeroZampe = 4;   // valore di default ragionevole
      peso = 1.0;        // valore di default ragionevole
  }
  Animale() { ... }                                      // costruttore vuoto
  ```
* 🎯 **Perché è utile:** in situazioni diverse abbiamo informazioni diverse a disposizione (a volte conosciamo già peso e zampe, a volte no) e vogliamo comunque poter creare l'oggetto.
* ⚠️ **Attenzione alla firma:** Java distingue i costruttori in base a **numero e tipo** dei parametri, non ai nomi delle variabili.

---

### ├── [1.4] Cenno al Costruttore di Copia
*Obiettivo: introdurre un pattern avanzato (facoltativo, da consolidare più avanti) senza appesantire la lezione.*

* 📑 **Costruttore di copia:** un costruttore che riceve **un oggetto della stessa classe** e ne copia i valori in un nuovo oggetto.
  ```java
  Animale(Animale altro) {
      nome = altro.nome;
      verso = altro.verso;
      numeroZampe = altro.numeroZampe;
      peso = altro.peso;
  }
  ```
* 🎯 **Caso d'uso tipico:** creare un "duplicato indipendente" di un oggetto, per poterlo modificare senza alterare l'originale (es. clonare un animale per simulare una nascita gemellare, poi modificarne il peso senza toccare l'originale).
* 💡 **Nota didattica:** non insistere troppo in questa prima presentazione; è un concetto che tornerà utile più avanti (es. con le collezioni di oggetti).

---

## 💻 MODULO LABORATORIO (3 Ore con ITP)

### ├── [2.1] Refactoring: Dalla Classe Nuda ai Costruttori
*Obiettivo: trasformare il codice della Settimana 1 applicando concretamente quanto appreso in teoria.*

* 🔧 **Refactoring guidato della classe `Animale`:** aggiunta di un costruttore completo con tutti gli attributi come parametri.
* 🔍 **Confronto diretto:** riscrivere il codice del `main` di Settimana 1 usando il nuovo costruttore, e far notare quante righe si risparmiano.

---

### ├── [2.2] Istanziazione con Costruttori Diversi
*Obiettivo: rendere operativa la sovraccarico dei costruttori su un caso pratico nuovo, sempre dentro il progetto "La Stalla".*

* 🐎 **Esercizio:** classe `Recinto` (il recinto/box che ospita gli animali) con attributi `nome` (es. "Pollaio", "Stalla dei bovini"), `capienzaMax` e `numeroAnimaliOspitati`.
* 🏗️ **Da implementare:**
  * Un costruttore completo (tutti i parametri).
  * Un costruttore parziale (solo `nome` e `capienzaMax`, con `numeroAnimaliOspitati` impostato a `0` di default — il recinto nasce vuoto).
* ▶️ **Nel `main`:** istanziare almeno 2 recinti usando entrambi i costruttori, e stampare le loro informazioni.

---

### ├── [2.3] La Parola Chiave `this`
*Obiettivo: risolvere il conflitto di nomi tra parametri del costruttore e attributi della classe.*

* ❓ **Il problema:** cosa succede se chiamo il parametro del costruttore con lo stesso nome dell'attributo?
  ```java
  Animale(String nome, String verso, int numeroZampe, double peso) {
      this.nome = nome;               // this.nome = attributo, nome = parametro
      this.verso = verso;
      this.numeroZampe = numeroZampe;
      this.peso = peso;
  }
  ```
* 🎯 **`this`** si riferisce **all'oggetto che si sta costruendo/utilizzando**, permettendo di distinguere l'attributo dal parametro omonimo.
* 💡 **Vantaggio didattico:** usare nomi di parametri identici agli attributi (invece di abbreviazioni tipo `n`, `v`, `z`) rende il codice molto più leggibile, a patto di usare `this` correttamente.

---

### ├── [2.4] Esercitazione Pratica Guidata al PC (Durata: 90 minuti)

#### FASE A: Refactoring guidato (25 min)
1. Aggiungere alla classe `Animale` un costruttore completo con `this`.
2. Riscrivere il `main` di Settimana 1 usando `new Animale(...)` invece delle assegnazioni riga per riga.

#### FASE B: Classe Recinto con costruttori sovraccaricati (35 min)
1. Creare la classe `Recinto` con almeno 2 costruttori (completo e parziale).
2. Istanziare almeno 2 oggetti `Recinto` usando entrambi i costruttori.
3. Aggiungere un metodo `stampaScheda()` che mostri tutte le informazioni del recinto.

#### FASE C: Estensione autonoma (20 min)
1. Aggiungere alla classe `Recinto` un terzo costruttore a scelta (es. solo `nome`, con `capienzaMax` di default a `10`).
2. Discutere in coppia: quali valori di default ha senso assegnare agli attributi non specificati?

#### FASE D: Consegna e riflessione (10 min)
1. Salvataggio e consegna su Google Classroom.
2. Domanda di chiusura: *«Perché non possiamo avere due costruttori con esattamente gli stessi parametri (stesso tipo e stesso numero)?»*

---

## 🐔 ESERCIZI PRATICI — LA STALLA (Settimana 2)

1. **Nascita guidata.** Usando il costruttore completo, crea 4 animali diversi in una sola riga di codice ciascuno (niente più assegnazioni riga per riga).
2. **Il recinto che si riempie.** Nella classe `Recinto`, scrivi un metodo `aggiungiAnimale()` che incrementi `numeroAnimaliOspitati` di 1 ogni volta che viene chiamato. Chiamalo 3 volte e stampa il totale.
3. **Costruttore intelligente.** Aggiungi ad `Animale` un terzo costruttore che riceve solo `nome` e `verso`, assegnando `numeroZampe = 4` e `peso = 1.0` come valori di default. Verifica che funzioni creando un oggetto con questo costruttore.
4. **Il costruttore di copia in azione.** Usa il costruttore di copia per creare un "gemello" di un animale esistente. Modifica il peso del gemello e verifica che l'originale non sia cambiato.
5. **Sfida bonus — Trova l'errore.** Un compagno immaginario ha scritto due costruttori: `Animale(String nome, String verso)` e `Animale(String verso, String nome)`. Perché Java non li accetta entrambi nella stessa classe? (Suggerimento: pensa alla firma, non ai nomi dei parametri.)
6. **Domanda di riflessione:** perché il costruttore di copia è utile quando lavoriamo con gli animali della stalla? Fai un esempio concreto in cui "clonare" un animale e poi modificarlo separatamente ha senso.

---

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma Lezione Teorica (165 min, 3h)
* **00-10 min | Accoglienza e recap Settimana 1:** ripasso veloce di Classe/Oggetto/Attributi/Metodi sulla classe `Animale`.
* **10-30 min | L'Hook d'apertura:** mostra alla lavagna il codice "nudo" (`new Animale()` + assegnazioni riga per riga) e chiedi *«Vi sembra comodo? Cosa cambiereste?»*.
* **30-60 min | Il Costruttore:** introduci la sintassi, disegna il confronto "senza/con costruttore" alla lavagna usando `Animale`.
* **60-90 min | Costruttori sovraccaricati:** presenta 2-3 costruttori della stessa classe, fai distinguere le firme diverse.
* **90-110 min | La parola chiave `this`:** spiega il conflitto di nomi con un esempio scritto interamente alla lavagna, riga per riga.
* **110-130 min | Cenno al costruttore di copia:** presentazione leggera, senza approfondire troppo.
* **130-165 min | Esercizi collettivi alla lavagna:** scrivi insieme alla classe 2-3 costruttori per un nuovo animale proposto dagli studenti stessi.

### ✍️ Disegno Guida da fare alla Lavagna (Lezione 1)

```text
    ┌─────────────────────────────────────────────────────────┐
    │        COSTRUTTORE: NASCERE GIÀ CON I VALORI GIUSTI       │
    │                                                         │
    │   Animale(String nome, String verso,                    │
    │           int numeroZampe, double peso) {                │
    │       this.nome = nome;                                │
    │       this.verso = verso;                              │
    │       this.numeroZampe = numeroZampe;                   │
    │       this.peso = peso;                                │
    │   }                                                    │
    │                                                         │
    │   new Animale("Coccodè", "Coccodè!", 2, 1.8) → pronto! │
    └─────────────────────────────────────────────────────────┘
```

### 🎯 Micro-Task Formativa per Casa (Spaced Retrieval - 5 minuti)
Carica su Google Classroom questo compito (senza voto punitivo, solo spunta di completamento):
> *"Scrivi su carta (senza IDE) due costruttori sovraccaricati per una classe 'Recinto' (attributi: nome, capienzaMax, numeroAnimaliOspitati). Uno completo, uno che assume il recinto vuoto come default."*
