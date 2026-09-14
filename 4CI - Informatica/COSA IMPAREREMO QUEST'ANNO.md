# 📚 COSA IMPAREREMO A 4CI QUEST'ANNO (2025-2026)

Benvenuto al quarto anno di Informatica! 🎉

Ricordi il primo anno, quando "pensavi algoritmicamente"? Ricordi il secondo anno, quando hai fatto i primi programmi in Python?

**Bene, dimenticati tutto.** 😄

A 4CI, entrerai nel mondo **"serio"** della programmazione: **la Programmazione Orientata agli Oggetti (OOP)**. Questo è il paradigma che usa il 90% delle aziende software del mondo. Java, C++, C#, Python (anche) — tutti OOP.

Se impari OOP bene adesso, avrai una skill che le aziende cercano **disperatamente**.

---

## 🎯 Le Due Grandi Domande che Rispondemmo

### 1️⃣ **"Come organizzo il codice in progetti grandi?" (Programmazione Orientata agli Oggetti — OOP)**

Immagina: 10 programmatori, 100.000 righe di codice, 50 file sorgenti. Come eviti il caos?

**La risposta: Oggetti e Classi.**

Invece di scrivere codice "piatto" (una lista infinita di funzioni), pensi **agli oggetti del tuo dominio**:
- Se scrivi un'app bancaria → hai oggetti `ContoCorrenteBancario`, `Cliente`, `Transazione`
- Se scrivi un videogame → hai oggetti `Giocatore`, `Nemico`, `Arma`, `Mappa`
- Se scrivi un gestionale → hai oggetti `Prodotto`, `Ordine`, `Fornitore`

**Cosa vedrai in pratica:**
- Scrivere **classi in Java** — le definizioni di come deve essere un oggetto
- Capire **incapsulamento** — proteggere i dati di un oggetto in modo che non siano modificati sconsideratamente
- Imparare l'**ereditarietà** — creare una classe "padre" e tante classi "figlie" che ne ereditano le proprietà (riduce il codice duplicato)
- Scoprire il **polimorfismo** — lo stesso metodo si comporta diversamente a seconda dell'oggetto (magia!)
- Usare **collezioni** (`ArrayList`) — liste di oggetti che crescono e si restringono dinamicamente

**Esempio concreto:**

```java
// Definisci una classe "stampo"
class Auto {
    String marca;
    String colore;
    double velocitàAttuale;
    
    void accelera() {
        velocitàAttuale = velocitàAttuale + 10;
    }
    
    void frena() {
        velocitàAttuale = velocitàAttuale - 10;
    }
}

// Crei due oggetti (istanze) dalla classe
Auto miaAuto = new Auto();
miaAuto.marca = "Ferrari";
miaAuto.accelera();  // La Ferrari va più veloce

Auto tuaAuto = new Auto();
tuaAuto.marca = "Fiat";
tuaAuto.accelera();  // La Fiat accelera allo stesso modo (ma è una Fiat! 😄)
```

---

### 2️⃣ **"Come salvo i dati in modo permanente?" (File e Database)**

Un programma che non salva i dati è inutile. Se chiudi l'app, tutto scompare.

**Cosa vedrai in pratica:**
- Leggere e scrivere **file di testo** (CSV, file log, ecc.)
- Salvare lo "stato" dei tuoi oggetti su disco (uno `ArrayList<Auto>` che persiste tra una sessione e l'altra)
- Concetti base di **database** — come organizzare i dati in tabelle (si approfondisce negli anni successivi)
	- **Gestione delle eccezioni** — quando qualcosa va storto (il file non esiste, il disco è pieno), il programma non muore, ma gestisce l'errore con grazia

**Esempio:**
```java
// Leggi un file CSV di auto
ArrayList<Auto> auto = new ArrayList<>();
Scanner file = new Scanner(new File("auto.csv"));
while (file.hasNextLine()) {
    String linea = file.nextLine();
    // Parsing della linea: "Ferrari,rosso,250"
    Auto a = new Auto(...);
    auto.add(a);
}
// Ora hai una collezione di Auto caricate dal disco
```

---

## 📖 Bonus: Python (Il Linguaggio "Più Agile")

Nel secondo semestre, vedrai anche **Python**. Non perché sia il "migliore", ma perché:
- È **più semplice di Java** — meno punteggiatura, meno boilerplate
- È usato per **machine learning, data science, scripting** — settori in crescita
- Imparerai che il concetto di **funzioni** e **modularità** è **universale** — cambia il linguaggio, ma il ragionamento rimane

Visto che hai già visto Python a 2CI, questa volta vai più in profondità (liste, dizionari, funzioni).

---

## 📋 I Contenuti Specifici

### ☕ Primo Semestre: JAVA e OOP (Settembre - Gennaio)

| **Periodo** | **Cosa Imparemmo in Aula** | **In Laboratorio (al PC)** |
|---|---|---|
| **Settembre - Ottobre** | Classe vs Oggetto, Attributi e Metodi, Costruttori, Incapsulamento (public/private) | Setup IDE (IntelliJ IDEA), scrivere la classe `Persona`, creare istanze, test nel `main` |
| **Novembre - Dicembre** | Getter e Setter, Ereditarietà (`extends`), Superclasse e Sottoclassi, Overriding | Creare gerarchie di classi (es: `Persona` → `Dipendente` → `Manager`), riuso di codice |
| **Gennaio** | Polimorfismo, Astrattezza, Interfacce (cenni), Colleghi Dinamiche | Projeto integrato: una gerarchia di classi + un ArrayList che raccogli istanze diverse |

### 🐍 Secondo Semestre: Python + Persistenza (Febbraio - Giugno)

| **Periodo** | **Cosa Imparemmo in Aula** | **In Laboratorio (al PC)** |
|---|---|---|
| **Febbraio - Marzo** | Ripasso Java + Introduzione ArrayList, Algoritmi su collezioni | Gestire liste di oggetti: ricerca, ordinamento, filtro |
| **Aprile - Maggio** | File I/O (lettura/scrittura di file), Parsing CSV, Gestione eccezioni (`try-catch`) | Salvare dati su file, ricaricarli, verificare che persistono tra le sessioni |
| **Giugno** | Python base: sintassi, liste, dizionari, funzioni | Mini-progetto finale: un programma che carica dati da file, li elabora, li salva di nuovo |

---

## 💡 Perché Tutto Questo Serve?

✅ **Per il lavoro (short term - prossimi 1-2 anni):**
- Uno **programmatore Java junior** in Italia guadagna 1.500-2.500€/mese (base, può salire)
- Le aziende cercano programmatori che conoscono OOP — è una **skill non negoziabile**
- Se impari bene OOP, puoi imparare C++, C#, TypeScript con facilità (tutti usano gli stessi concetti)

✅ **Per la specializzazione (medio term - anni 3-5):**
- Se sei bravo, puoi specializzarti in **backend** (server-side programming)
- O in **full-stack** (frontend + backend)
- O in **DevOps** (deploying e mantenendo applicazioni)
- O in **microservizi, cloud (AWS/Azure), containerizzazione** — tutto parte da OOP

✅ **Per il presente:**
- Capirai che il codice **non è magia**, è **logica**
- Non avrai più paura dei bug — saprai come debuggare
- Vedrai il valore della **documentazione e dello stile** di codice
- Imparerai a usare **Git** per il versionamento (skill fondamentale in team)

---

## 🎯 I Progetti che Farai

Tutto l'anno ruota attorno a **progetti pratici**, non solo teoria:

1. **Settembre-Ottobre:** La classe `Persona` — primo contatto con OOP
2. **Novembre-Dicembre:** Gerarchia di classi (es: `Persona` → `Studente` → `Liceale` + `Tecnico`)
3. **Gennaio:** ArrayList di oggetti + ricerca/ordinamento
4. **Febbraio-Marzo:** File I/O — carica dati da CSV, salvali su file
5. **Aprile-Maggio:** Progetto integrato Java (scelta vostra: gestionale pizzeria, biblioteca, ecommerce)
6. **Giugno:** Mini-progetto Python (script per analizzare dati o risolvere un problema)

Ogni progetto ha una **relazione tecnica** che documenti il design, il codice e i test.

---

## 🚀 Aspettative e Regole del Gioco

### ✨ Quello che Ci Aspettiamo da Te:

1. **Cambia mentalità:** Da "scrivere linee di codice" a "disegnare un'architettura"
2. **Progetta prima, coda dopo:** Disegna le tue classi sulla carta prima di scrivere il codice
3. **Testa il tuo codice:** Un professionista scrive test prima ancora di finire il feature
4. **Comunica con il codice:** Nomi di variabili chiari, commenti dove serve, codice leggibile
5. **Impara da chi è bravo:** Leggi codice open-source su GitHub, rubati i pattern

### 📋 Come Funzionerà l'Anno:

- **Lezione in aula (3 ore/settimana):** teoria OOP, design patterns, best practices
- **Laboratorio con ITP (3 ore/settimana):** **tu al PC**, che scrivi, che debuggi, che testi
- **Piattaforma:** IntelliJ IDEA (IDE professionale, gratuito per studenti), GitHub (versionamento)

### 🎓 Voto:
- Teoria: 30% (conosci OOP? Sai la differenza tra classe e oggetto?)
- Pratica/Progetti: 55% (il codice funziona? È ben scritto? È leggibile?)
- Documentazione e comunicazione: 15% (sai spiegare quello che hai fatto?)

---

## 🎬 TL;DR (Troppo Lungo; Non Ho Letto)

**4CI = diventare un programmatore "per davvero"**

- **Java + OOP** — il paradigma che usa il 90% delle aziende software
- **Incapsulamento, Ereditarietà, Polimorfismo** — i tre pilastri dell'OOP
- **File I/O** — come salvi i dati in modo permanente
- **Python** — secondo linguaggio, sintassi semplice
- **Progetti reali** — non solo compiti, ma veri mini-progetti software

**Bonus:** Se sei **veramente bravo**, puoi contribuire a progetti open-source su GitHub (che i recruiter adorano vedere nel CV) 🏆

---

**Pronto a diventare un vero programmatore? Let's code! 💻🚀**
