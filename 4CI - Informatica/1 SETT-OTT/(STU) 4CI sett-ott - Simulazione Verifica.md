# Simulazione di verifica — capire e progettare con gli oggetti

**4CI · Informatica · 55 minuti · 10 punti**

Nome e cognome: ______________________________  Data: ____________

## Come funziona

- Niente computer o appunti, salvo gli strumenti previsti dal tuo piano personalizzato.
- ✅ indica una domanda di base; 🔍 una domanda più impegnativa.
- Nelle crocette c'è una sola risposta corretta. Sbagliare non toglie punti.
- Il «Perché?» è facoltativo: il ragionamento può aiutarti, ma non può penalizzarti.
- Non serve scrivere programmi completi. Nella parte 2 puoi usare un disegno generico, UML o una descrizione a parole. Per i metodi contano soprattutto dichiarazione e firma; per il comportamento basta anche pseudocodice.
- Nel disegno indica **C** per le classi concrete, **A** per le classi astratte e **I** per le interfacce. Distingui «estende», «implementa» e «contiene».

| Parte | Attività | Punti | Tempo indicativo |
| --- | --- | ---: | ---: |
| 1 | Teoria, lettura e ragionamento | 6,5 | 28 min |
| 2 | Progettazione | 3,5 | 27 min |

I tempi sono indicativi: puoi distribuirli come preferisci e lasciare qualche minuto per rileggere.

---

# Parte 1

## Teoria

**T1 ✅ (0,5)** Quale frase descrive meglio la differenza tra una classe e un oggetto?

- [ ] **A.** La classe è una variabile che contiene tutti gli oggetti.
- [ ] **B.** Gli oggetti di una classe hanno sempre lo stesso stato.
- [ ] **C.** La classe descrive caratteristiche e comportamenti; ogni oggetto ha il proprio stato.
- [ ] **D.** Un oggetto esiste solo mentre si scrive il programma.

*Perché? (facoltativo)* ______________________________________________

**T2 ✅ (0,5)** Una classe `Personaggio` ha `private int energia` e un metodo che permette di impostarla a qualsiasi valore. Qual è il problema rispetto all'incapsulamento?

- [ ] **A.** Il campo `private` non può essere usato nemmeno dalla classe `Personaggio`.
- [ ] **B.** Un metodo pubblico può consentire valori non ammessi se non controlla le modifiche allo stato.
- [ ] **C.** Ogni campo deve essere una costante.
- [ ] **D.** L'incapsulamento impedisce di modificare lo stato dopo la creazione dell'oggetto.

*Perché? (facoltativo)* ______________________________________________

**T3 ✅ (0,5)** Quale situazione è un buon motivo per usare l'ereditarietà?

- [ ] **A.** Una classe `Motore` contiene un oggetto `Auto`.
- [ ] **B.** Due classi hanno nomi simili.
- [ ] **C.** Una classe rappresenta un tipo specifico di un'altra, per esempio `AutoSportiva` è un tipo di `Auto`.
- [ ] **D.** Si vuole rendere pubblico ogni campo della classe base.

*Perché? (facoltativo)* ______________________________________________

**T4 ✅ (0,5)** Un programma gestisce diversi tipi di notifica attraverso la stessa operazione `invia()`. Qual è un vantaggio del polimorfismo?

- [ ] **A.** Il programma può usare un contratto (interfaccia) comune senza dover conoscere ogni volta la classe concreta.
- [ ] **B.** Tutti gli oggetti diventano istanze della stessa classe.
- [ ] **C.** Gli oggetti non hanno più attributi.
- [ ] **D.** Le classi concrete non devono definire il proprio comportamento.

*Perché? (facoltativo)* ______________________________________________

**T5 🔍 (0,5)** Una classe `Sensore` e una classe `ServizioWeb` devono entrambe offrire `inviaDati()`, ma non condividono né stato né codice. Quale soluzione rappresenta meglio questa capacità comune?

- [ ] **A.** Far ereditare `ServizioWeb` da `Sensore`.
- [ ] **B.** Creare un'interfaccia con il contratto `inviaDati()` e farla implementare da entrambe.
- [ ] **C.** Inserire tutti gli attributi di entrambe in una nuova classe concreta.
- [ ] **D.** Rinominare uno dei due metodi, così non c'è più una capacità comune.

*Perché? (facoltativo)* ______________________________________________

**T6 ✅ (0,5)** Qual è lo scopo dell'astrazione?

- [ ] **A.** Nascondere qualsiasi operazione agli altri oggetti.
- [ ] **B.** Descrivere ciò che è essenziale per usare un tipo, separandolo dai dettagli di realizzazione.
- [ ] **C.** Trasformare una variabile in un oggetto nuovo.
- [ ] **D.** Rendere pubblici gli attributi condivisi.

*Perché? (facoltativo)* ______________________________________________

## Leggere il codice

Per C1 e C2, considera questa classe:

```java
class Cartellino {
    private String colore;

    public Cartellino(String colore) {
        this.colore = colore;
    }

    public void setColore(String colore) {
        this.colore = colore;
    }

    public String getColore() {
        return colore;
    }
}
```

**C1 🔍 (0,5)** Che cosa stampa il codice?

```java
Cartellino primo = new Cartellino("Verde");
Cartellino secondo = primo;
secondo.setColore("Giallo");
System.out.println(primo.getColore());
```

- [ ] **A.** `Verde`
- [ ] **B.** `Giallo`
- [ ] **C.** `null`
- [ ] **D.** Non compila.

*Perché? (facoltativo)* ______________________________________________

**C2 ✅ (0,5)** Questo frammento è indipendente da C1. Che cosa stampa?

```java
Cartellino primo = new Cartellino("Verde");
Cartellino secondo = new Cartellino("Giallo");
secondo.setColore("Blu");
System.out.println(primo.getColore());
```

- [ ] **A.** `Blu`
- [ ] **B.** `Giallo`
- [ ] **C.** `Verde`
- [ ] **D.** `null`

*Perché? (facoltativo)* ______________________________________________

**C3 ✅ (0,5)** Sono già definite le classi concrete `Documento` e `EBook extends Documento`, entrambe con un costruttore senza parametri. Quale riga assegna un nuovo oggetto della sottoclasse a un riferimento della superclasse?

- [ ] **A.** `Documento d = new Documento();`
- [ ] **B.** `Documento d = new EBook();`
- [ ] **C.** `EBook e = new EBook();`
- [ ] **D.** `Documento d = null;`

*Perché? (facoltativo)* ______________________________________________

## Riconoscere un problema di progettazione

**E1 ✅ (0,5)** Il codice compila, ma dopo `new Profilo("Ada")` il campo `nome` resta `null`. Spiega il motivo e correggi il costruttore.

```java
class Profilo {
    private String nome;

    public Profilo(String nome) {
        nome = nome;
    }
}
```

________________________________________________________________________

________________________________________________________________________

**E2 ✅ (0,5)** Una delle due righe non è valida. Indica quale e spiega perché.

```java
abstract class Strumento {
    public abstract String suona();
}

class Flauto extends Strumento {
    @Override
    public String suona() {
        return "Fiu";
    }
}

// nel main:
Strumento s1 = new Strumento(); // riga 1
Strumento s2 = new Flauto();    // riga 2
```

________________________________________________________________________

________________________________________________________________________

**E3 🔍 (1)** Il codice è sintatticamente valido, ma il modello rappresenta male il rapporto tra gli oggetti. Spiega il problema e descrivi una relazione più adatta.

```java
class Libro {
}

class Biblioteca extends Libro {
}
```

________________________________________________________________________

________________________________________________________________________

________________________________________________________________________

---

# Parte 2 — progettare un catalogo di contenuti

Un'applicazione cataloga contenuti digitali.

- Ogni contenuto ha un **titolo**.
- Esistono contenuti di tipo **Articolo** e **Podcast**.
- Ogni contenuto deve saper restituire una breve descrizione tramite `descrivi()`, che restituisce un testo.
- Un articolo ha anche un autore.
- Un podcast ha una durata in minuti e può essere scaricato tramite `scarica()`, che restituisce un testo. Gli articoli non sono scaricabili.
- Il catalogo conserva tutti i contenuti in un'unica lista.
- Non esistono contenuti generici da creare direttamente: si creano articoli o podcast.

È già stata progettata questa parte:

```java
class Articolo extends Contenuto {
    // costruttore: Articolo(String titolo, String autore)
    // descrivi() restituisce un testo con titolo e autore
}
```

**D1 ✅ (1)** Rappresenta le classi e l'interfaccia necessarie, usando un disegno, UML o parole. Indica:

- quali elementi sono classi concrete, classe astratta e interfaccia;
- quali classi estendono `Contenuto`;
- quale classe implementa l'interfaccia per lo scaricamento;
- come il catalogo conserva la lista.

________________________________________________________________________

________________________________________________________________________

________________________________________________________________________

**D2 ✅ (0,5)** Descrivi o scrivi la parte essenziale di `Contenuto`: attributo, costruttore e metodo `descrivi()`. Non serve scrivere il corpo del metodo astratto.

________________________________________________________________________

________________________________________________________________________

**D3 🔍 (1)** Descrivi o scrivi la parte essenziale di `Podcast`, includendo il costruttore, la durata, `descrivi()` e il metodo `scarica()`. Indica anche quale relazione collega `Podcast` all'interfaccia.

________________________________________________________________________

________________________________________________________________________

________________________________________________________________________

**D4 🔍 (1)** Quale tipo useresti per la lista del catalogo? Spiega perché può contenere sia articoli sia podcast. Poi spiega in una frase perché il fatto che solo i podcast siano scaricabili è rappresentato meglio dall'interfaccia che da una caratteristica comune di tutti i contenuti.

________________________________________________________________________

________________________________________________________________________

________________________________________________________________________
