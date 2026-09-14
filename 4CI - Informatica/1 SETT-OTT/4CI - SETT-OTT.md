# SETT-OTT — 4ª CI (Informatica)

Piano operativo delle prime 8 settimane (Settembre–Ottobre) per la 4ª CI (Informatica: OOP in Java + fondamenti Python).

* **Monte ore:** 6 ore settimanali (3 ore di teoria in aula + 3 ore di laboratorio, in compresenza con l'ITP).
* **Obiettivo del bimestre:** Consolidare ed espandere i fondamenti della Programmazione ad Oggetti in Java (classi, costruttori, incapsulamento, overloading), per poi introdurre ereditarietà e polimorfismo, chiudendo con la prima verifica sommativa teorica e pratica.

---

## 🧭 Quadro Sinottico Settimana per Settimana (Settembre – Ottobre)

```
┌───────────┬──────────────────────────────────────┬────────────────────────────────────────┐
│ SETTIMANA │ TEORIA (3h - In aula)                 │ LABORATORIO (3h - Con ITP)              │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 1   │ Ripasso Classi/Oggetti;              │ Setup IDE e JDK, primo progetto Java,  │
│           │ Attributi e Metodi                   │ classe con attributi pubblici          │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 2   │ Costruttori: default, sovraccarichi, │ Refactoring con costruttori multipli,  │
│           │ costruttore di copia                 │ istanziazione con `new` e parola `this`│
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 3   │ Incapsulamento e Information Hiding; │ Getter/Setter, validazione dei dati    │
│           │ private/public/protected             │ in ingresso, classi "sicure"            │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 4   │ Overloading dei metodi;              │ Metodi con firme diverse (parametri    │
│           │ ripasso e consolidamento Modulo 1.1   │ diversi per numero/tipo), esercizi misti│
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 5   │ Ereditarietà: `extends`,              │ Creazione gerarchie di classi          │
│           │ superclasse/sottoclasse, riuso codice │ (superclasse/sottoclasse) in progetto  │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 6   │ Overriding dei metodi e `super`;      │ Override pratico, test del comportamento│
│           │ introduzione al Polimorfismo          │ polimorfico su gerarchie create        │
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 7   │ Ripasso attivo e simulazione          │ Consolidamento pratico, correzione     │
│           │ della prova scritta                   │ incrociata degli esercizi in laboratorio│
├───────────┼──────────────────────────────────────┼────────────────────────────────────────┤
│ Sett. 8   │ 📝 VERIFICA SCRITTA 1 (Fondamenti OOP)│ Verifica pratica di laboratorio /      │
│           │                                        │ recupero e approfondimento             │
└───────────┴──────────────────────────────────────┴────────────────────────────────────────┘
```

---

## 📝 Dettaglio Operativo dei Moduli

---

### SETTIMANA 1: Il Ritorno alla Programmazione: Classi e Oggetti
*Obiettivo: riallineare tutta la classe sui fondamenti di OOP visti (parzialmente) in 3° anno, prima di procedere spediti.*

* **Teoria (3h):**
  * Presentazione del programma annuale: Modulo 1 (OOP Java), Modulo 2 (Python), criteri di valutazione, libro di testo.
  * Ripasso: cos'è una **Classe** (il progetto/stampo) vs un **Oggetto** (l'istanza concreta).
  * **Stato** (attributi/campi) e **comportamento** (metodi) di un oggetto.
  * Esempio guidato alla lavagna: classe `Persona` con attributi `nome`, `cognome`, `età` e metodo `saluta()`.
* **Laboratorio (3h):**
  * Setup dell'ambiente di sviluppo (JDK, IDE adottato dall'istituto: Eclipse / IntelliJ / VS Code + estensioni Java).
  * Creazione del primo progetto Java: struttura cartelle `src/`, package, convenzioni di naming.
  * Scrittura ed esecuzione di una prima classe con attributi pubblici e un metodo `main` di test.
* 📚 **Cosa devi ripassare tu:**
  * Sintassi base Java: tipi primitivi, dichiarazione variabili, struttura minima di una classe (`public class X { ... }`).

---

### SETTIMANA 2: Costruttori e l'Arte di Nascere Bene
*Obiettivo: rendere operativa la creazione controllata di oggetti tramite costruttori.*

* **Teoria (3h):**
  * I **costruttori**: metodo speciale che inizializza lo stato dell'oggetto al momento della creazione.
  * Costruttore di default (implicito) vs costruttore esplicito con parametri.
  * **Costruttori sovraccaricati** (più costruttori con firme diverse nella stessa classe).
  * Cenno al **costruttore di copia** (creare un nuovo oggetto copiando i valori di un altro).
* **Laboratorio (3h):**
  * Refactoring della classe `Persona`: aggiunta di costruttori multipli.
  * Istanziazione di più oggetti con `new Persona(...)` usando costruttori diversi.
  * Esercizio: classe `Libro` (o `Prodotto`) con almeno due costruttori sovraccaricati.
* 📚 **Cosa devi ripassare tu:**
  * Differenza tra dichiarazione (`Persona p;`) e istanziazione (`p = new Persona();`); il ruolo della parola chiave `this`.

---

### SETTIMANA 3: Incapsulamento e Information Hiding
*Obiettivo: proteggere lo stato interno degli oggetti e introdurre l'accesso controllato tramite getter/setter.*

* **Teoria (3h):**
  * **Incapsulamento** e *information hiding*: perché nascondere lo stato interno di un oggetto.
  * Modificatori di visibilità: `private`, `public`, `protected` (cenno, in vista dell'ereditarietà).
  * Metodi di accesso e modifica: **getter** e **setter**, con validazione opzionale dei dati in ingresso.
* **Laboratorio (3h):**
  * Conversione degli attributi delle classi già create in `private`, con getter/setter espliciti.
  * Aggiunta di semplice validazione nei setter (es. età non negativa, stringhe non vuote).
  * Esercizio: classe `ContoBancario` con saldo privato e metodi `deposita()`/`preleva()` che validano l'importo.
* 📚 **Cosa devi ripassare tu:**
  * Perché un attributo pubblico modificabile liberamente è un rischio di robustezza del software (nessun controllo sui valori).

---

### SETTIMANA 4: Overloading dei Metodi e Consolidamento
*Obiettivo: introdurre l'overloading e fissare tutti i concetti del blocco "Fondamenti OOP" prima di passare all'ereditarietà.*

* **Teoria (3h):**
  * **Overloading (sovraccarico) dei metodi:** più metodi con lo stesso nome ma firma diversa (numero e/o tipo dei parametri).
  * Differenza tra overloading (stesso nome, firma diversa, stessa classe) e semplice ridefinizione di variabili.
  * Ripasso guidato di tutto il blocco: classi, oggetti, costruttori, incapsulamento.
* **Laboratorio (3h):**
  * Esercizio pratico: aggiungere metodi sovraccaricati (es. `stampa()` senza parametri e `stampa(String prefisso)` con parametro).
  * Batteria di esercizi misti di consolidamento su classi già sviluppate nelle settimane precedenti.
* 📚 **Cosa devi ripassare tu:**
  * Prepara 3-4 esempi di overloading "puliti" da mostrare alla lavagna (evitando ambiguità di firma che il compilatore rifiuterebbe).

---

### SETTIMANA 5: Ereditarietà: Riuso del Codice e Gerarchie di Classi
*Obiettivo: introdurre il secondo pilastro dell'OOP, mostrando come evitare duplicazione di codice.*

* **Teoria (3h):**
  * **Ereditarietà:** estensione di classi con `extends`, concetto di **superclasse** e **sottoclassi**.
  * Il **riuso del codice**: la sottoclasse eredita attributi e metodi della superclasse.
  * Costruzione di gerarchie di classi (es. `Veicolo` → `Auto`, `Moto`).
* **Laboratorio (3h):**
  * Creazione di un progetto con una superclasse e almeno due sottoclassi.
  * Verifica che le sottoclassi ereditino correttamente attributi/metodi della superclasse.
* 📚 **Cosa devi ripassare tu:**
  * La differenza semantica tra ereditarietà ("è un") e composizione ("ha un"), da usare come discriminante quando si progetta una gerarchia.

---

### SETTIMANA 6: Overriding, `super` e Introduzione al Polimorfismo
*Obiettivo: mostrare come una sottoclasse può specializzare il comportamento ereditato.*

* **Teoria (3h):**
  * **Overriding (sovrascrittura) dei metodi:** una sottoclasse ridefinisce un metodo della superclasse con la stessa firma.
  * Uso della parola chiave `super` per richiamare costruttore/metodo della superclasse.
  * Introduzione al **Polimorfismo**: *binding* dinamico, tipo statico vs tipo dinamico di un riferimento.
* **Laboratorio (3h):**
  * Override pratico di un metodo (es. `descrivi()`) nelle sottoclassi della gerarchia creata in Settimana 5.
  * Test del comportamento polimorfico: array/collezione di riferimenti al tipo superclasse, popolata con oggetti di sottoclassi diverse.
* 📚 **Cosa devi ripassare tu:**
  * Un esempio chiaro di *binding* dinamico da presentare alla lavagna (stesso metodo chiamato, comportamento diverso a runtime in base al tipo reale dell'oggetto).

---

### SETTIMANA 7: Ripasso Attivo e Preparazione alla Verifica
*Obiettivo: consolidare tutti i concetti del bimestre con esercizi di retrieval practice prima del test sommativo.*

* **Teoria (3h):**
  * **Simulazione di verifica (mock test):** esercizi identici per tipologia a quelli della prova, su classi, costruttori, incapsulamento, overloading, ereditarietà, overriding.
  * Correzione collettiva alla lavagna, con enfasi sugli errori tipici (es. dimenticare `private`, confondere overload/override).
* **Laboratorio (3h):**
  * Consolidamento pratico: completamento e rifinitura di tutti gli esercizi/progetti delle settimane precedenti.
  * Correzione incrociata (*peer review*) tra studenti sul codice prodotto.
* 📚 **Cosa devi ripassare tu:**
  * Prepara il testo della verifica scritta (due file bilanciati: Fila A e Fila B).

---

### SETTIMANA 8: La Prima Verifica Sommativa
*Obiettivo: misurare l'acquisizione dei fondamenti OOP del primo bimestre.*

* **Teoria (3h):**
  * 📝 **VERIFICA SCRITTA N. 1 (Fondamenti OOP: classi, costruttori, incapsulamento, overloading, ereditarietà base, overriding)**.
  * Struttura consigliata: quesiti teorici a risposta multipla/aperta + un breve esercizio di scrittura/lettura di codice Java.
* **Laboratorio (3h):**
  * Verifica pratica di laboratorio: scrittura autonoma di una piccola gerarchia di classi con i requisiti visti nel bimestre.
  * Sessione di recupero/approfondimento per chi necessita di consolidare ulteriormente.
* 📚 **Cosa devi fare tu:**
  * Correggi le verifiche entro pochi giorni: è il primo voto del quadrimestre e definisce il livello di serietà percepito dagli studenti.
