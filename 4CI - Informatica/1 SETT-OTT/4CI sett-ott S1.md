Ecco il kit didattico completo per la **Settimana 1**, strutturato come una **mappa concettuale espansa (mindmap ad albero)** con tutti i contenuti pronti per essere spiegati alla lavagna e svolti al PC.

> Nota: il quadro sinottico delle 8 settimane e il dettaglio sintetico settimana per settimana si trovano in [4CI - SETT-OTT.md](4CI%20-%20SETT-OTT.md).

---

# 🗺️ SETTIMANA 1: IL RITORNO ALLA PROGRAMMAZIONE — CLASSI E OGGETTI

```text
SETTIMANA 1
├── 🧠 LEZIONE 1: TEORIA (3 ORE IN AULA)
│   ├── [1.1] Presentazione del Corso e Patto Formativo
│   ├── [1.2] Classe vs Oggetto: il Progetto e l'Istanza
│   ├── [1.3] Stato e Comportamento: Attributi e Metodi
│   └── [1.4] Primo Esempio Guidato: la Classe Animale
│
├── 💻 LEZIONE 2: LABORATORIO (3 ORE CON ITP) — PARTE 1 DEL PROGETTO "LA STALLA"
│   ├── [2.1] Setup dell'Ambiente di Sviluppo (JDK + IDE)
│   ├── [2.2] Anatomia di un Progetto Java
│   ├── [2.3] Prima Classe Animale con Attributi Pubblici e Main di Test
│   └── [2.4] Esercitazione Pratica Guidata (Missione: "Il Primo Animale della Stalla")
│
├── 🐔 ESERCIZI PRATICI — LA STALLA (Settimana 1)
│
└── 📋 GUIDA DI REGIA PER IL DOCENTE
    ├── Scaletta Minuto per Minuto
    ├── Schema da Disegnare alla Lavagna
    └── Micro-Task di Consolidamento (Formative Assessment)
```

> 🐄 **Il progetto guida dell'anno: "La Stalla".** Da questa settimana in poi, gli esempi di laboratorio e gli esercizi pratici ruoteranno attorno a un unico progetto in crescita: una stalla con animali (`Animale`, poi `Pollo` e `Mucca`). Il progetto si arricchirà settimana dopo settimana — costruttori, incapsulamento, overloading, ereditarietà — fino al leggendario `KebabRadioattivo` della Settimana 6. Gli esempi teorici in aula (es. `Persona`, `ContoCorrenteBancario`) restano utili per illustrare i concetti in generale, ma il codice che scriverete voi al PC sarà sempre la Stalla.

---

## 🧠 MODULO TEORICO (3 Ore in Aula)

### ├── [1.1] Presentazione del Corso e Patto Formativo
*Obiettivo: dare un quadro chiaro dell'anno e ridurre l'ansia da rientro dopo l'estate.*

* 📌 **Il programma dell'anno in due blocchi:**
  * **Modulo 1 (Java):** completamento della Programmazione ad Oggetti — costruttori, incapsulamento, ereditarietà, polimorfismo, collezioni (`ArrayList`), persistenza su file.
  * **Modulo 2 (Python):** un linguaggio diverso, più agile, per consolidare la logica algoritmica senza l'impalcatura rigida di Java.
* 📌 **Il patto formativo:** come funzionano le verifiche (scritte + pratiche di laboratorio), il valore dell'errore come parte del processo di apprendimento, il libro di testo adottato.
* 🎯 **Perché ripartire da "Classi e Oggetti":** anche se già visti in 3° anno, l'OOP richiede solide fondamenta: senza di esse, ereditarietà e polimorfismo (a fine bimestre) risultano incomprensibili.

---

### ├── [1.1 bis] La Programmazione Orientata agli Oggetti: Cos'è, Perché Serve, Come Differisce dai Paradigmi
- [ ] Sanità mentale e progetti grandi
- [ ] Vedrete che l'IDE vi dirà vita, morte e miracoli del vostro programma
- [ ] Focus sul ==DESIGN== del codice. Diventeremo dei piccoli artisti dell'ordine

#### **COS'È L'OBJECT-ORIENTED PROGRAMMING (OOP)?**

* 🎯 **Definizione essenziale:**
  * La **Programmazione Orientata agli Oggetti** è un **paradigma di programmazione** (cioè un modo di pensare al codice) che organizza il software attorno a **"oggetti"** — entità che contengono sia dati (attributi) che comportamenti (metodi), proprio come le cose del mondo reale.
  * È nata negli anni '70-80 (linguaggi come Smalltalk, C++) per risolvere i problemi crescenti di complessità nella programmazione.

* 📦 **La metafora centrale dell'OOP:**
  * Pensa alla realtà fisica: un'auto non è un insieme di operazioni ("accelera", "frena", "gira"), ma è un **oggetto** che **ha** componenti (motore, ruote, volante) e **sa fare** cose (accelerare, frenare, girar volante).
  * Un conto bancario non è una lista di istruzioni, ma un **oggetto** che **ha** un saldo, un titolare, una data di apertura, e **sa fare** operazioni (deposita, preleva, calcola interesse).
  * L'OOP rispecchia questo modo naturale di pensare: il codice diventa un specchio della realtà.

* 🏗️ **Tre pilastri fondamentali dell'OOP:**
  1. **Incapsulamento (Encapsulation):** racchiudere dati e metodi dentro una classe, nascondendo i dettagli interni. L'esterno vede solo l'interfaccia pubblica.
  2. **Ereditarietà (Inheritance):** una classe può "ereditare" attributi e metodi da un'altra classe, evitando la duplicazione di codice.
  3. **Polimorfismo (Polymorphism):** lo stesso metodo può comportarsi diversamente a seconda dell'oggetto che lo richiama.

---

#### **A COSA SERVE L'OOP? VANTAGGI CONCRETI**

* ✅ **Modularità:** il codice è organizzato in classi indipendenti, ognuna responsabile di una "cosa" specifica. Quando una classe ha un bug, sai esattamente dove cercarlo.
* ✅ **Riusabilità:** scrivi una classe `Persona` una volta; la usi 100 volte in progetti diversi. Scrivi una classe `ContoCorrenteBancario` e la personalizza tramite ereditarietà (`ContoRisparmio` estende `ContoCorrenteBancario`).
* ✅ **Manutenibilità:** se cambiano le regole di business (es. "il calcolo degli interessi ora è del 3% anziché 2%"), cambi il metodo `calcolaInteressi()` in una sola classe. Tutti gli oggetti usano istantaneamente la nuova logica.
* ✅ **Scalabilità:** in aziende grandi, venti programmatori lavorano su venti classi diverse in parallelo, senza che il codice di uno interferisca con quello dell'altro.
* ✅ **Closer to Reality:** quando un analista dice "il sistema gestisce Clienti e Ordini", il tuo codice avrà una classe `Cliente` e una classe `Ordine`. Il codice rispecchia il linguaggio del business → comunicazione più facile.

**Esempio pratico:**
```java
// CON OOP: il codice descrive la realtà
ContoCorrenteBancario mioCorso = new ContoCorrenteBancario("Mario Rossi", 1000.0);
mioCorso.deposita(500);
mioCorso.mostraaSaldo();  // "Saldo: 1500€"

// È intuitivo, leggibile, mantengbile per anni.
```

---

#### **OOP VS PROGRAMMAZIONE PROCEDURALE: IL GRANDE CONTRASTO**

Ora che hai studiato Flowgorithm, Python e pseudocodice in **1CI e 2CI**, hai usato la **programmazione procedurale** (o imperativa). È il momento di capire come l'OOP è completamente diversa.

| **Aspetto** | **PROGRAMMAZIONE PROCEDURALE** | **PROGRAMMAZIONE ORIENTATA AGLI OGGETTI (OOP)** |
|---|---|---|
| **Modo di pensare** | Focus sulle **azioni** ("che cosa deve fare il programma?") | Focus sugli **oggetti** ("che cose crea il programma?") |
| **Struttura** | Insieme di **funzioni/procedure** che operano su **dati globali** o **variabili locali** | Insieme di **classi**, ognuna contiene dati (attributi) + funzioni (metodi) correlati |
| **Dati** | Variabili libere, sparse nel codice, accessibili da ovunque (globali) | Dati **incapsulati** dentro le classi, controllati tramite metodi |
| **Riusabilità** | Bassa: se scrivi una funzione `calcolaStipendio()`, non è facile adattarla ad altri contesti | Alta: scrivi una classe `Stipendio`, la estendi tramite ereditarietà, la usi ovunque |
| **Manutenibilità** | Media: un bug in una funzione globale può avere effetti inaspettati in altre parti | Alta: un bug in una classe è **localizzato**, gli effetti collaterali sono minimi |
| **Parallelismo** | Difficile: se più programmatori modificano lo stesso file di funzioni, ci sono conflitti | Facile: ogni programmatore può lavorare su una classe diversa senza conflitti |
| **Esempio di codice** | `function trasferisci(importo, conto1, conto2) { ... }` (funzione generica) | `class ContoCorrenteBancario { ... trasferisci(importo, altroC) ... }` (il metodo conosce lo stato interno) |

**Esempio concreto — Programmazione PROCEDURALE (quello che hai fatto a 2CI):**
```python
# Variabili globali — sparse, accessibili ovunque, pericolose
saldo = 1000
nome_cliente = "Mario"

def deposita(importo):
    global saldo
    saldo = saldo + importo
    print(f"Depositato {importo}€. Nuovo saldo: {saldo}€")

def preleva(importo):
    global saldo
    saldo = saldo - importo
    print(f"Prelevato {importo}€. Nuovo saldo: {saldo}€")

# Problema: se accidentalmente scrivo `saldo = -99999`, tutto il programma è corrotto
```

**Stesso codice — Programmazione ORIENTATA AGLI OGGETTI (quello che fai a 4CI):**
```java
class ContoCorrenteBancario {
    private double saldo;  // PRIVATO: nessuno può toccarlo direttamente
    private String nomeCliente;

    public ContoCorrenteBancario(String nome, double saldoIniziale) {
        this.nomeCliente = nome;
        this.saldo = saldoIniziale;
    }

    public void deposita(double importo) {
        if (importo > 0) {  // CONTROLLO: il metodo valida l'input
            saldo = saldo + importo;
            System.out.println("Depositato " + importo + "€. Nuovo saldo: " + saldo + "€");
        } else {
            System.out.println("Errore: importo negativo!");
        }
    }

    public void preleva(double importo) {
        if (importo > 0 && importo <= saldo) {
            saldo = saldo - importo;
            System.out.println("Prelevato " + importo + "€. Nuovo saldo: " + saldo + "€");
        } else {
            System.out.println("Errore: importo non valido o saldo insufficiente!");
        }
    }

    public double ottieniSaldo() {
        return saldo;
    }
}

// Uso:
ContoCorrenteBancario conto1 = new ContoCorrenteBancario("Mario", 1000);
conto1.deposita(500);     // OK: +500€
conto1.deposita(-50);     // ERRORE BLOCCATO dal metodo
conto1.saldo = -99999;    // ERRORE DI COMPILAZIONE! saldo è private, non è accessibile
```

**La differenza è profonda:**
- Programmazione procedurale: il programma **non si protegge** dall'uso sconsiderato
- Programmazione OOP: il programma **si difende** con l'incapsulamento

---

#### **BREVE ACCENNO AD ALTRI PARADIGMI (PER COMPLETEZZA)**

Esitono altri paradigmi di programmazione oltre a Procedurale e OOP. Non li studierai quest'anno, ma è bene sapere che esistono:

| **Paradigma**    | **Filosofia**                                | **Linguaggi tipici**                    | **Quando lo usi**                                        |
| ---------------- | -------------------------------------------- | --------------------------------------- | -------------------------------------------------------- |
| **Procedurale**  | Sequenza di comandi                          | Python, C, Pascal                       | Scripting, calcoli semplici, algoritmi                   |
| **OOP**          | Oggetti che interagiscono                    | Java, C++, C#, Python (multi-paradigma) | Applicazioni grandi, sistemi complessi                   |
| **Funzionale**   | Trasformazioni di dati tramite funzioni pure | Lisp, Haskell, Scheme                   | Data processing, trasformazioni matematiche, concorrenza |
| **Logico**       | Regole logiche e inferenza                   | Prolog                                  | Sistemi esperti, puzzle solving                          |
| **Dichiarativo** | Descrivi il "cosa" non il "come"             | SQL, HTML                               | Database, markup, configuration                          |

**Nota importante:** Python, JavaScript, C++ supportano **più paradigmi** (sono multi-paradigma). Java è nato come **OOP puro**, anche se versioni moderne (Java 8+) hanno aggiunto elementi funzionali (lambda, stream).

---

#### **PERCHÉ JAVA È OOP PURO (E COSA SIGNIFICA)**

* 🎯 **"OOP Puro" = tutto è un oggetto (o quasi):**
  * In Java, quando scrivi `int x = 5;`, la variabile `x` è una **primitiva** (non è un oggetto).
  * Ma quando scrivi `String s = "Ciao";`, `s` è un **oggetto** istanza della classe `String`.
  * Nel 99% dei casi, lavori con oggetti, classi, metodi.

---

##### **I Tipi Fondamentali (Primitivi) — L'Eccezione che Conferma la Regola**

* 📌 **Cosa sono i tipi primitivi:**
  * Sono i pochi tipi di dato **non orientati agli oggetti** che Java conserva dalla programmazione procedurale per motivi di efficienza.
  * Sono memorizzati direttamente in memoria (nello stack), non come riferimenti ad oggetti (come nel heap).
  * **Lista completa dei tipi primitivi in Java:**
    * **Numeri interi:** `byte` (8 bit), `short` (16 bit), `int` (32 bit), `long` (64 bit)
    * **Numeri decimali:** `float` (32 bit), `double` (64 bit)
    * **Booleani:** `boolean` (true / false)
    * **Caratteri:** `char` (16 bit, un singolo carattere Unicode)

  ```java
  int età = 17;              // primitivo: il valore 17 è memorizzato direttamente
  double voto = 8.5;         // primitivo: il valore 8.5 è memorizzato direttamente
  boolean promozione = true; // primitivo: il valore true è memorizzato direttamente
  ```

* 📌 **Perché Java ha i primitivi (e perché importa):**
  * **Efficienza:** un `int` è velocissimo perché è puro dato binario, senza l'overhead di un oggetto.
  * **Tradizione:** Java eredita i tipi primitivi dal C/C++ per compatibilità e performance.
  * **Uso quotidiano:** quando scrivi un ciclo `for (int i = 0; i < 10; i++)`, `i` è un primitivo, non un oggetto.

* 📌 **Tutto il resto è un oggetto:**
  * Se non è uno dei 8 tipi primitivi elencati sopra, è un **oggetto**.
  * `String` è una classe (oggetto) — anche se sembra una cosa semplice, è un oggetto.
  * `ArrayList<Integer>` è una classe (oggetto) — una collezione di oggetti `Integer`.
  * Le tue classi `Persona`, `Auto`, `ContoCorrenteBancario` sono oggetti.

  ```java
  String nome = "Mario";           // oggetto: istanza della classe String
  ArrayList<Integer> voti = new ArrayList<>();  // oggetto: istanza della classe ArrayList
  Persona p1 = new Persona();      // oggetto: istanza della tua classe Persona
  ```

---

##### **Wrapper Classes: "Oggetti che avvolgono i primitivi"**

* 🔄 **Cosa succede quando un primitivo deve diventare un oggetto:**
  * A volte Java ha bisogno di trattare un primitivo come un oggetto (es. metterlo dentro un `ArrayList`).
  * Per questo, Java fornisce delle **wrapper classes** — classi che "avvolgono" i primitivi.

  | **Tipo Primitivo** | **Wrapper Class** |
  |---|---|
  
  | `byte` | `Byte` |
  | `short` | `Short` |
  | `int` | `Integer` |
  | `long` | `Long` |
  
  | `float` | `Float` |
  | `double` | `Double` |
  | `boolean` | `Boolean` |
  
  | `char` | `Character` |

  ```java
  // Primitivo: non è un oggetto
  int x = 5;

  // Wrapper: è un oggetto che contiene il valore primitivo 5
  Integer xOggetto = new Integer(5);  // o semplicemente: Integer xOggetto = 5; (autoboxing)

  // Adesso puoi mettere xOggetto dentro un ArrayList
  ArrayList<Integer> numeri = new ArrayList<>();
  numeri.add(5);  // Java converte automaticamente il 5 in Integer (autoboxing)
  ```

* 🎯 **Regola pratica:** 
  - Quando scrivi cicli, calcoli veloci, operazioni semplici → usa i **primitivi** (`int`, `double`, `boolean`).
  - Quando usi collezioni (`ArrayList`, `HashMap`) → Java userà automaticamente i **wrapper** (`Integer`, `Double`, `Boolean`).
  - Non devi preoccuparti troppo della differenza — Java converte automaticamente (autoboxing/unboxing).

---

* 🎯 **Implicazioni per il tuo apprendimento:**
  * A 4CI, praticamente **tutto** quello che farai sarà OOP. Non c'è modo di aggirarlo.
  * Ogni programma che scrivi sarà una o più classi, mai una lista di funzioni globali.
  * Questo è sia un vantaggio (forza buone abitudini) sia una sfida (richiede un cambio mentale).

---

#### **COME RICONOSCERAI L'OOP NEL CODICE (ANTICIPAZIONE)**

Quando leggi il codice Java, vedrai schemi ricorrenti che indicano OOP:

1. **Keyword `class`:** ogni file contiene una classe
   ```java
   public class Persona { ... }  // ← questo è OOP
   ```

2. **Variabili dentro la classe** (attributi):
   ```java
   public class Auto {
       String marca;       // ← attributo (dato che ogni Auto ha)
       double velocità;    // ← attributo
   }
   ```

3. **Metodi dentro la classe** (comportamenti):
   ```java
   public class Auto {
       void accelera() { ... }   // ← metodo (azione che Auto sa fare)
       void frena() { ... }      // ← metodo
   }
   ```

4. **Istanziazione con `new`:**
   ```java
   Auto miaAuto = new Auto();    // ← creo un oggetto (istanza) della classe Auto
   ```

5. **Accesso tramite `.` (dot notation):**
   ```java
   miaAuto.accelera();          // ← chiamo un metodo dell'oggetto
   System.out.println(miaAuto.velocità);  // ← accedo a un attributo
   ```

---

### ├── [1.2] Classe vs Oggetto: il Progetto e l'Istanza
*Obiettivo: fissare la distinzione concettuale più importante di tutta la programmazione ad oggetti.*

```text
                    CLASSE (Il progetto/stampo)
        ┌─────────────────────────────────────────┐
        │   class Animale {                       │
        │       String nome;                      │
        │       String verso;                     │
        │       int numeroZampe;                  │
        │       void faiVerso() { ... }            │
        │   }                                     │
        └─────────────────────────────────────────┘
                          │
                 (new Animale(...))
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   OGGETTO 1          OGGETTO 2         OGGETTO 3
 nome="Coccodè"     nome="Mucca"        nome="Cane"
 verso="Coccodè!"   verso="Muuu!"     verso="Bau!"
 zampe=2             zampe=4           zampe=4
```

* 🏗️ **Classe:** definisce **la struttura** (quali attributi e metodi avrà ogni oggetto), ma non esiste fisicamente in memoria come dato.
* 📦 **Oggetto (istanza):** un'entità concreta creata a partire dalla classe, con i **propri valori** per ogni attributo.
* **Metafora d'aula:** la classe `Animale` è lo "stampo" per qualsiasi bestia della stalla; ogni animale creato (oggetto) condivide la stessa struttura (ha un nome, un verso, delle zampe) ma con valori propri. Non esiste ancora differenza tra un pollo e una mucca: per ora sono tutti semplicemente `Animale` — la specializzazione (Pollo, Mucca) arriverà con l'ereditarietà in Settimana 5.

---

### ├── [1.3] Stato e Comportamento: Attributi e Metodi
*Obiettivo: collegare i concetti teorici alla sintassi Java che verrà scritta in laboratorio.*

* 🧬 **Stato (attributi/campi):** le variabili dichiarate dentro la classe, che rappresentano le caratteristiche di un oggetto (es. `nome`, `numeroZampe`).
* ⚙️ **Comportamento (metodi):** le funzioni dichiarate dentro la classe, che rappresentano le azioni che un oggetto può compiere (es. `faiVerso()`, `mangia()` — quest'ultimo arriverà in Settimana 4).
* 📐 **Sintassi minima di una classe Java:**
  ```java
  public class Animale {
      String nome;        // attributo
      String verso;       // attributo
      int numeroZampe;    // attributo

      void faiVerso() {              // metodo
          System.out.println(nome + " fa: " + verso);
      }
  }
  ```
* 🎯 **Regola pratica:** se una parola risponde alla domanda *"che cos'ha?"* è un attributo (`nome`, `numeroZampe`); se risponde a *"che cosa fa?"* è un metodo (`faiVerso()`).

---

### ├── [1.4] Primo Esempio Guidato: la Classe Animale
*Obiettivo: vedere l'intero ciclo di vita di un oggetto, dalla definizione della classe all'uso concreto — è il primo mattone del progetto "La Stalla".*

* 🐔 **Definizione della classe** `Animale` con attributi `nome`, `verso`, `numeroZampe` e metodo `faiVerso()`.
* 🏭 **Creazione di oggetti** nel metodo `main`:
  ```java
  Animale a1 = new Animale();
  a1.nome = "Coccodè";
  a1.verso = "Coccodè!";
  a1.numeroZampe = 2;
  a1.faiVerso();   // stampa: "Coccodè fa: Coccodè!"
  ```
* 🔍 **Osservazione guidata:** ogni oggetto (`a1`, `a2`, ...) occupa uno spazio di memoria distinto, con valori propri, pur condividendo la stessa struttura definita dalla classe. Se cambio `a1.nome`, `a2.nome` non viene toccato: sono due "stanze" separate nella stalla di memoria del programma.
* 💡 **Perché proprio gli animali?** Perché nelle prossime settimane costruiremo gerarchie (`Pollo`, `Mucca` che ereditano da `Animale`), useremo l'incapsulamento per evitare che qualcuno assegni `numeroZampe = -3`, e arriveremo a un esempio memorabile di overloading e polimorfismo con un ingrediente... particolare. Pazienza fino alla Settimana 6. 😉

---

## 💻 MODULO LABORATORIO (3 Ore con ITP)

### ├── [2.1] Setup dell'Ambiente di Sviluppo (JDK + IDE)
*Obiettivo: garantire che ogni postazione abbia un ambiente Java funzionante e uniforme.*

* ☕ **Il JDK (Java Development Kit):** verifica dell'installazione e della versione (`java -version`, `javac -version` da terminale).
* 🖥️ **L'IDE adottato dall'istituto** (Eclipse / IntelliJ IDEA / VS Code con estensione Java): apertura, creazione di un nuovo progetto/workspace.
* 🔧 **Configurazione minima:** impostazione del JDK di progetto, verifica che la compilazione di un file di prova (`Hello World`) funzioni correttamente.

---

### ├── [2.2] Anatomia di un Progetto Java
*Obiettivo: dare ordine mentale alla struttura di cartelle e file che gli studenti vedranno tutto l'anno.*

```text
LaStalla/
├── src/                     <- cartella dei sorgenti
│   └── it.scuola.stalla/    <- package (facoltativo ma consigliato)
│       └── Animale.java     <- il file della classe
├── bin/ (o out/, target/)   <- file .class compilati (generati automaticamente)
└── README.md (facoltativo)  <- descrizione del progetto
```

* 📦 **Il concetto di package:** un "raccoglitore" logico di classi correlate, utile fin da ora per abituarsi all'organizzazione del codice. Chiameremo il nostro pacchetto `it.scuola.stalla`, e ci vivranno tutte le classi del progetto guida dell'anno.
* 📄 **Convenzione di naming:** nome del file = nome della classe pubblica al suo interno (`Animale.java` contiene `public class Animale`).

---

### ├── [2.3] Prima Classe Animale con Attributi Pubblici e Main di Test
*Obiettivo: scrivere ed eseguire codice reale, chiudendo il cerchio teoria-pratica della lezione — nasce ufficialmente il progetto "La Stalla".*

* ✍️ **Scrittura guidata** della classe `Animale` (attributi pubblici per semplicità, verranno resi privati in Settimana 3).
* ▶️ **Scrittura del metodo `main`** in una classe separata (es. `TestStalla`) che crea oggetti e ne richiama i metodi.
* 🐞 **Prima sessione di debug guidato:** errori tipici (dimenticare il punto e virgola, `public class` non corrispondente al nome file, `main` scritto male).

---

### ├── [2.4] Esercitazione Pratica Guidata al PC (Durata: 90 minuti)

#### FASE A: Verifica ambiente (15 min)
1. Ogni studente verifica che JDK e IDE funzionino correttamente compilando ed eseguendo un `Hello World`.

#### FASE B: Creazione della classe Animale (30 min)
1. Creare il file `Animale.java` con attributi `nome`, `verso`, `numeroZampe` e metodo `faiVerso()`.
2. Creare il file `TestStalla.java` con il metodo `main`.
3. Istanziare almeno 2 oggetti `Animale` con valori diversi (es. un pollo con 2 zampe e una mucca con 4) e richiamarne il metodo `faiVerso()`.

#### FASE C: Estensione autonoma (30 min)
1. Aggiungere un nuovo attributo `double peso` e un nuovo metodo `presentati()` che stampi tutti i dati dell'animale in una frase leggibile.
2. Creare almeno 3 oggetti diversi (con nomi, versi, zampe e pesi differenti) e stampare le loro presentazioni.

#### FASE D: Consegna e riflessione (15 min)
1. Salvataggio del progetto e consegna su Google Classroom (screenshot dell'output in console).
2. Domanda di chiusura in plenaria: *«Se cambio il valore di `nome` in un oggetto, cosa succede agli altri oggetti?»*

---

## 🐔 ESERCIZI PRATICI — LA STALLA (Settimana 1)

*Ogni settimana troverai qui una batteria di esercizi graduati sul progetto "La Stalla", da svolgere dopo (o durante) il laboratorio guidato.*

1. **Riscaldamento — Il primo pollo.** Crea un oggetto `Animale` che rappresenti un pollo (`nome = "Coccodè"`, `verso = "Coccodè!"`, `numeroZampe = 2`, `peso = 1.8`). Stampane la presentazione con `presentati()`.
2. **La mandria.** Crea un array (o semplicemente 5 variabili) di oggetti `Animale` diversi. Scrivi un ciclo `for` che li stampi tutti in sequenza usando `presentati()`.
3. **Conta zampe.** Usando lo stesso array, scrivi un ciclo che sommi il `numeroZampe` di tutti gli animali e stampi il totale ("In stalla ci sono in tutto N zampe").
4. **Il più pesante.** Scrivi un ciclo che trovi e stampi il nome dell'animale con il `peso` maggiore.
5. **Sfida bonus — Zampe di default.** Crea un `Animale` senza assegnare `numeroZampe`. Stampa il suo valore: cosa succede? Perché Java assegna `0` di default a un attributo `int` mai inizializzato? (Risposta attesa: ogni tipo primitivo ha un valore di default — `0` per i numeri, `false` per i booleani, `null` per gli oggetti/stringhe — finché non lo sovrascriviamo esplicitamente.)
6. **Domanda di riflessione (da scrivere a parole, non in codice):** perché conviene scrivere un metodo `presentati()` invece di ripetere sempre le stesse 4 righe di `System.out.println` per ogni animale?

---

## 📋 GUIDA DI REGIA PER IL DOCENTE

### ⏱️ Cronoprogramma Lezione Teorica (165 min, 3h)
* **00-15 min | Accoglienza e presentazione del corso:** saluto, presentazione del programma annuale e dei criteri di valutazione.
* **15-40 min | L'Hook d'apertura:** disegna alla lavagna uno stampo per biscotti e chiedi *«Cosa rappresenta lo stampo? E i biscotti?»*, arrivando alla metafora Classe/Oggetto.
* **40-75 min | Lavagna partecipata su Classe vs Oggetto:** disegna lo schema classe→istanze multiple, fai costruire alla classe altri esempi (es. classe `Automobile` → oggetti `auto1`, `auto2`).
* **75-110 min | Attributi e Metodi:** scrivi alla lavagna la sintassi minima di una classe Java, fai distinguere collettivamente attributi da metodi in esempi proposti dagli studenti.
* **110-150 min | Esempio guidato completo:** sviluppa insieme alla classe (a voce, senza PC) l'intero esempio `Animale`, dalla definizione all'uso — annuncia che sarà il progetto guida di tutto il bimestre.
* **150-165 min | Chiusura e domande a bruciapelo:** 3 domande rapide (*«Cos'è un attributo? Fammi un esempio di metodo. Quanti oggetti posso creare da una classe?»*).

### ✍️ Disegno Guida da fare alla Lavagna (Lezione 1)

```text
    ┌─────────────────────────────────────────────────────────┐
    │           CLASSE "STAMPO" → OGGETTI "ANIMALI"            │
    │                                                         │
    │   class Animale { nome, verso, numeroZampe, faiVerso() } │
    │                        │                                │
    │        ┌───────────────┼───────────────┐                │
    │        ▼               ▼               ▼                │
    │   Coccodè, 2 zampe   Muu, 4 zampe    Bau, 4 zampe        │
    └─────────────────────────────────────────────────────────┘
```

### 🎯 Micro-Task Formativa per Casa (Spaced Retrieval - 5 minuti)
Carica su Google Classroom questo compito (senza voto punitivo, solo spunta di completamento):
> *"Pensa a un altro animale della stalla che non abbiamo ancora usato in classe (es. un'oca, una capra, un asino). Scrivi su carta: quali valori avrebbero i suoi attributi nome, verso, numeroZampe, peso — senza scrivere codice Java, solo in italiano."*
