# Verifica 4CI sett-ott: soluzioni commentate

Ecco le risposte corrette a ogni esercizio, con una spiegazione del perché le alternative sbagliate non vanno bene. Leggi anche le alternative che non hai scelto: spesso è lì che si capisce il principio.

---

# Parte 1: I principi, perché esistono

**T1 ✅ (0,5)** La classe `Tavolo` memorizza il numero di posti nell'attributo `private int posti`. Che cosa implica? Cosa succede?

- [ ] **A.** Permette alle altre classi di leggere `posti`, ma non di modificarlo.
- [ ] **B.** Fa rifiutare ai metodi di `Tavolo` i valori negativi per `posti`.
- [ ] **C.** Permette solo al codice di `Tavolo` di accedere direttamente a `posti`.
- [ ] **D.** Permette anche alle sottoclassi di accedere direttamente a `posti`.

**Risposta: C.** Il resto del programma deve passare dai metodi accessibili della classe, ed è lì che si controllano le modifiche allo stato.

- **A** confonde accesso privato e sola lettura: da fuori non si può neppure leggere direttamente il campo.
- **B** attribuisce a `private` una validazione che va invece scritta nei metodi.
- **D** confonde `private` con l'accesso consentito alle sottoclassi.

**T2 ✅ (0,5)** Le classi `Pizza` e `Panino` hanno entrambe gli attributi `nome` e `prezzo`. `Pizza` ha anche il tipo di impasto; `Panino` ha anche il tipo di farcitura. Come possiamo usare l'ereditarietà per non ripetere la definizione di `nome` e `prezzo` nelle due classi?

- [ ] **A.** Mettere nome e prezzo nella classe padre `Prodotto`, da cui ereditano le due classi figlie.
- [ ] **B.** Mettere nome e prezzo nella classe padre `Pizza`, da cui eredita la classe figlia `Panino`.
- [ ] **C.** Mettere nome e prezzo nella classe padre `Panino`, da cui eredita la classe figlia `Pizza`.
- [ ] **D.** Mettere nome e prezzo in entrambe le classi, senza creare una classe padre comune.

**Risposta: A.** Pizza e panino sono tipi di prodotto: la classe padre raccoglie la parte comune e le classi figlie aggiungono quella specifica.

- **B** e **C** usano l'ereditarietà solo per riusare dati, ma un panino non è una pizza e viceversa.
- **D** ripete la parte comune e non usa l'ereditarietà.

**T3 ✅ (0,5)** Il programma della cassa deve sommare i prezzi di pizze, bibite e dolci. Ogni prodotto è rappresentato da un oggetto. Quale soluzione usa il polimorfismo?

- [ ] **A.** La cassa legge il tipo e sceglie il prezzo con un `if`.
- [ ] **B.** La cassa legge gli attributi e calcola da sé ciascun prezzo.
- [ ] **C.** La cassa chiama metodi distinti: `prezzoPizza()`, `prezzoBibita()`, `prezzoDolce()`.
- [ ] **D.** La cassa chiama `prezzo()` (ad esempio su un'`ArrayList`) e ciascun prodotto calcola il proprio prezzo.

**Risposta: D.** Si usa la stessa operazione del tipo comune, e ciascun prodotto realizza il proprio calcolo. Per aggiungere un tipo non serve aggiungere un caso alla cassa.

- **A** lascia alla cassa la scelta in base al tipo: è proprio ciò che il polimorfismo evita.
- **B** sposta nella cassa le regole dei singoli prodotti.
- **C** richiede un nome diverso per ogni tipo, quindi la cassa deve conoscere tutti i tipi. Le alternative A, B e C possono funzionare, ma non sfruttano il polimorfismo.

**T4 ✅ (0,5)** Nel programma, `Pizza` e `Bibita` sono sottoclassi della classe astratta `Prodotto`. Quale frase descrive correttamente la classe `Prodotto`?

- [ ] **A.** Non può contenere metodi con un corpo, solo dichiarazioni astratte.
- [ ] **B.** Può contenere dati e metodi, ma non permette di creare oggetti con `new Prodotto()`.
- [ ] **C.** Permette di creare oggetti con `new Prodotto()` se le sottoclassi implementano tutti i metodi.
- [ ] **D.** Le sottoclassi concrete possono lasciare senza corpo i metodi astratti.

*Suggerimento: il corpo di un metodo è ciò che sta tra le parentesi graffe `{}`.*

**Risposta: B.** La classe raccoglie gli elementi comuni senza permettere di creare un prodotto generico. Le sottoclassi concrete completano i metodi astratti.

- **A** esclude i metodi già realizzati, che una classe astratta può avere.
- **C** confonde la possibilità di creare un oggetto con la realizzazione dei metodi: una classe astratta non si istanzia mai, anche se tutti i metodi sono completi.
- **D** è sbagliata: una sottoclasse concreta deve realizzare (scrivere il corpo di) ogni metodo astratto ereditato.

**T5 🔍 (0,5)** `Pizza` estende `Prodotto`, `Torta` estende `Dolce` e `Arrosto` estende `Piatto`. Il programma del forno deve chiamare `cuoci()` su oggetti delle tre classi, usando un unico tipo `Cuocibile`. Le tre classi devono mantenere le superclassi attuali. Come definiamo `Cuocibile`?

- [ ] **A.** Aggiungere `Cuocibile` come interfaccia implementata dalle tre classi.
- [ ] **B.** Aggiungere `Cuocibile` come seconda superclasse delle tre classi.
- [ ] **C.** Usare `Cuocibile` come nuova superclasse, sostituendo quelle attuali.
- [ ] **D.** Aggiungere `cuoci()` alle tre classi, senza un tipo comune.

*Suggerimento: superclasse e classe padre sono la stessa cosa.*

**Risposta: A.** L'interfaccia descrive la capacità comune e si aggiunge senza sostituire le superclassi esistenti.

- **B** non è ammessa in Java: una classe può estendere una sola superclasse.
- **C** cambia le gerarchie, mentre la consegna chiedeva di mantenerle.
- **D** dà ai metodi lo stesso nome, ma non crea un tipo comune: il forno non potrebbe usare un unico riferimento `Cuocibile`.

**T6 🔍 (0,5)** La classe `Cassa` memorizza il totale delle vendite nell'attributo `private double incasso`. Questo totale può aumentare, ma non deve diminuire. Quale metodo pubblico rispetta questa regola?

- [ ] **A.** Un setter che sostituisce l'incasso con qualsiasi totale maggiore o uguale a zero.
- [ ] **B.** Un metodo che aggiunge all'incasso qualsiasi importo diverso da zero.
- [ ] **C.** Un metodo che aggiunge all'incasso l'importo ricevuto solo se è positivo.
- [ ] **D.** Un setter che sostituisce l'incasso con qualsiasi importo positivo.

**Risposta: C.** Aggiungere un importo positivo fa aumentare l'incasso; gli altri valori sono rifiutati e il totale resta invariato.

- **A** e **D** controllano il nuovo totale, ma permettono di sostituirne uno alto con uno più basso, cioè di far diminuire l'incasso.
- **B** ammette anche importi negativi: essere diverso da zero non significa essere positivo.

---

# Parte 2: Leggere il codice

**C1 ✅ (0,75)** La classe `Pizza` ha un attributo `prezzo`. Il costruttore `Pizza(String nome, double prezzo)` assegna il prezzo iniziale. `setPrezzo(double)` sostituisce il prezzo e `getPrezzo()` lo restituisce. Che cosa stampa il codice?

```java
Pizza[] menu = new Pizza[2];
Pizza p = new Pizza("Margherita", 6.0);
menu[0] = p;
menu[1] = p;
menu[0].setPrezzo(8.0);
System.out.println(menu[1].getPrezzo());
```

- [ ] **A.** `0.0`
- [ ] **B.** `6.0`
- [ ] **C.** `14.0`
- [ ] **D.** `8.0`

**Risposta: D.** Le due caselle contengono lo stesso riferimento: c'è **un solo** oggetto `Pizza`, e il suo prezzo diventa `8.0`.

- **A** trascura il valore assegnato dal costruttore.
- **B** tratta l'assegnazione come una copia indipendente dell'oggetto: non lo è.
- **C** somma il vecchio prezzo al nuovo, mentre `setPrezzo` lo sostituisce.

**C2 ✅ (0,75)** La classe `Bibita` ha due costruttori. Che cosa stampa il codice?

```java
class Bibita {
    private String nome;
    private int cl;

    public Bibita() {
        nome = "Acqua";
        cl = 50;
    }

    public Bibita(String nome, int cl) {
        this.nome = nome;
        this.cl = cl;
    }

    public String descrizione() {
        return nome + " " + cl + "cl";
    }
}

Bibita x = new Bibita();
Bibita y = new Bibita("Cola", 33);
System.out.println(x.descrizione() + " / " + y.descrizione());
```

- [ ] **A.** `Acqua 50cl / Cola 33cl`
- [ ] **B.** `Cola 33cl / Cola 33cl`
- [ ] **C.** `Acqua 50cl / Acqua 50cl`
- [ ] **D.** `Cola 33cl / Acqua 50cl`

**Risposta: A.** Il costruttore senza parametri inizializza `x` con Acqua e 50; quello con parametri inizializza `y` con Cola e 33. I due oggetti hanno stati indipendenti.

- **B** fa dipendere `x` dallo stato di `y`: non succede.
- **C** usa per entrambi il costruttore senza parametri.
- **D** scambia l'ordine dei risultati, ma i valori dei due oggetti sono quelli giusti in A.

**Per C3, C4 e C5 considera queste classi:**

```java
class Prodotto {
    public String descrivi() {
        return "Prodotto generico";
    }
}

class Panino extends Prodotto {
    public String getFarcitura() {
        return "prosciutto";
    }

    @Override
    public String descrivi() {
        return "Panino con " + getFarcitura();
    }
}

class Gelato extends Prodotto {
}
```

**C3 ✅ (0,75)** Che cosa stampa il codice?

```java
Panino a = new Panino();
Gelato b = new Gelato();
System.out.println(a.descrivi());
System.out.println(b.descrivi());
```

- [ ] **A.** `Prodotto generico` e poi `Prodotto generico`
- [ ] **B.** `Panino con prosciutto` e poi `Panino con prosciutto`
- [ ] **C.** `Panino con prosciutto` e poi `Prodotto generico`
- [ ] **D.** `Prodotto generico` e poi `Panino con prosciutto`

**Risposta: C.** `Panino` ridefinisce `descrivi()`; `Gelato` usa il metodo ereditato da `Prodotto`.

- **A** ignora la ridefinizione fatta in `Panino`.
- **B** applica la ridefinizione anche a `Gelato`, che è una classe sorella e non la eredita.
- **D** scambia i comportamenti dei due oggetti.

**C4 ✅ (0,75)** Quale riga compila?

- [ ] **A.** `Panino p = new Prodotto();`
- [ ] **B.** `Prodotto p = new Panino();`
- [ ] **C.** `Gelato g = new Panino();`
- [ ] **D.** `Panino p = new Gelato();`

**Risposta: B.** Un `Panino` **è un** `Prodotto`, quindi può essere assegnato a un riferimento di tipo `Prodotto` (upcasting automatico).

- **A** non compila: un prodotto generico non è per forza un panino.
- **C** non compila: un panino non è un gelato.
- **D** non compila: un gelato non è un panino.

**C5 🔍 (1)** L'ultima riga non compila. Qual è il motivo?

```java
Prodotto p = new Panino();
System.out.println(p.getFarcitura());
```

- [ ] **A.** `Panino` non può essere assegnato a un riferimento `Prodotto`.
- [ ] **B.** `getFarcitura()` richiede `@Override` perché appartiene a una sottoclasse.
- [ ] **C.** `Prodotto` deve essere astratto per riferirsi a una sua sottoclasse.
- [ ] **D.** `getFarcitura()` non è dichiarato nel tipo del riferimento `p`.

**Risposta: D.** Il tipo del riferimento `p` è `Prodotto`, che non espone `getFarcitura()`. Il fatto che l'oggetto sia un `Panino` non rende quel metodo accessibile attraverso questo riferimento.

- **A** nega un upcasting che è valido.
- **B** confonde un metodo nuovo con una ridefinizione: `getFarcitura()` non ridefinisce nulla della superclasse, quindi `@Override` non c'entra.
- **C** confonde astrazione e polimorfismo: anche un riferimento a una classe concreta può indicare un oggetto di una sottoclasse.

---

# Parte 3: Riconoscere e correggere

**E1 ✅ (1)** Nella classe `Tavolo`, l'attributo `private int posti` indica il numero di posti del tavolo. Completa `setPosti`: il metodo deve assegnare a questo attributo soltanto valori **da 1 a 12, compresi 1 e 12**. Spiega anche che cosa fa il metodo se riceve un valore non valido.

```java
public void setPosti(int posti) {
    // completa
}
```

**Soluzione:**

```java
public void setPosti(int posti) {
    if (posti >= 1 && posti <= 12) {
        this.posti = posti;
    }   // altrimenti la richiesta viene ignorata
}
```

Il metodo controlla la condizione prima di assegnare il valore, così `posti` non può mai contenere un numero impossibile. Se il valore non è valido, la soluzione lo ignora: in alternativa andava bene mostrare un avviso o lanciare un errore, purché lo si dicesse.

Errori comuni: scrivere `<` invece di `<=` esclude gli estremi 1 e 12. Scrivere la condizione ma assegnare il valore fuori dall'`if` vanifica il controllo.

**E2 ✅ (1)** Il compilatore segnala un errore nella classe `Torta`. Spiega perché e come lo correggi.

```java
interface Cuocibile {
    void cuoci();
}

class Torta implements Cuocibile {
    private String gusto;
}
```

**Soluzione:** `Torta` dichiara di **implementare** `Cuocibile`, cioè accetta il contratto, ma non scrive il metodo `cuoci()`. Il compilatore pretende che ogni metodo dell'interfaccia sia realizzato in una classe concreta.

Correzione: aggiungere in `Torta` il metodo

```java
public void cuoci() {
    // ...
}
```

Rendere `Torta` astratta sarebbe una correzione formalmente possibile, ma non adatta qui: una torta da usare nel forno deve essere concreta.

**E3 🔍 (1)** La classe `Pizza` eredita dalla classe padre `Prodotto`. La classe `Prodotto` ha **un solo** costruttore, che riceve `nome` e `prezzo`. Il compilatore segnala un errore nel costruttore di `Pizza` e non riesce a inizializzare `nome` e `prezzo`. Spiega qual è il problema e correggi il costruttore di `Pizza`.

```java
class Prodotto {
    private String nome;
    private double prezzo;

    public Prodotto(String nome, double prezzo) {
        this.nome = nome;
        this.prezzo = prezzo;
    }
}

class Pizza extends Prodotto {
    private String impasto;

    public Pizza(String nome, double prezzo, String impasto) {
        this.impasto = impasto;
    }
}
```

**Soluzione:** il costruttore di `Pizza` non chiama il costruttore della classe padre. `Prodotto` non ha un costruttore senza parametri, e i suoi attributi sono `private`: solo il suo costruttore può inizializzarli. Va quindi chiamato `super(...)` come prima istruzione:

```java
public Pizza(String nome, double prezzo, String impasto) {
    super(nome, prezzo);
    this.impasto = impasto;
}
```

---

# Parte 4: Facoltativa, progettare un parco avventura (+2)

Un parco avventura gestisce le sue attività.

- Ogni attività ha un **nome** e un **prezzo**.
- Esistono attività di tipo **Percorso**, **Zipline** e **Parete** (arrampicata).
- Ogni attività deve saper restituire una breve descrizione con `descrivi()`, che restituisce un testo. Non esistono attività «generiche» da creare direttamente.
- Un percorso ha un'**altezza minima**; una zipline ha una **lunghezza in metri**; una parete ha una **difficoltà** (numero).
- **Solo** la zipline e la parete si possono prenotare, con `prenota(String cognome)`, che restituisce un testo di conferma. I percorsi non si prenotano.
- Il parco conserva tutte le attività in un **array**.

**P1 ⭐ (1)** Disegna o descrivi le classi e l'interfaccia che useresti per il programma del parco. Indica **C**, **A** o **I** accanto a ogni nome. Specifica quali classi ne estendono altre, quali implementano l'interfaccia e quale classe contiene l'array delle attività.

**Soluzione di riferimento:**

<table>
<thead>
<tr><th>Classe</th><th>Tipo</th><th>Membri</th></tr>
</thead>
<tbody>
<tr><td>Attivita</td><td>astratta (<code>abstract</code>)</td><td>-nome: String; -prezzo: double; +descrivi() String</td></tr>
<tr><td>Prenotabile</td><td>interfaccia (<code>interface</code>)</td><td>+prenota(cognome: String) String</td></tr>
<tr><td>Percorso</td><td>classe</td><td>—</td></tr>
<tr><td>Zipline</td><td>classe</td><td>—</td></tr>
<tr><td>Parete</td><td>classe</td><td>—</td></tr>
<tr><td>Parco</td><td>classe</td><td>-attivita: Attivita[]</td></tr>
</tbody>
</table>

<table>
<thead>
<tr><th>Da</th><th>A</th><th>Relazione</th></tr>
</thead>
<tbody>
<tr><td>Percorso</td><td>Attivita</td><td>estende</td></tr>
<tr><td>Zipline</td><td>Attivita</td><td>estende</td></tr>
<tr><td>Parete</td><td>Attivita</td><td>estende</td></tr>
<tr><td>Zipline</td><td>Prenotabile</td><td>implementa</td></tr>
<tr><td>Parete</td><td>Prenotabile</td><td>implementa</td></tr>
<tr><td>Parco</td><td>Attivita</td><td>contiene un array</td></tr>
</tbody>
</table>

- `Attivita` è **A** (astratta), e `Percorso`, `Zipline`, `Parete` sono **C** (concrete) che la estendono.
- `Prenotabile` è **I** (interfaccia), implementata da `Zipline` e `Parete`, ma non da `Percorso`.
- `Parco` contiene l'array di `Attivita`.

**P2 ⭐ (0,5)** Descrivi a parole oppure scrivi in Java queste parti. Non serve scrivere il codice dentro i costruttori e i metodi.

- Per `Attivita`: attributi, costruttore e dichiarazione del metodo `descrivi()`.
- Per `Zipline`: superclasse, interfaccia, attributo specifico, costruttore e dichiarazioni di `descrivi()` e `prenota`.

**Soluzione di riferimento:**

```java
abstract class Attivita {
    private String nome;
    private double prezzo;

    public Attivita(String nome, double prezzo) { ... }

    public abstract String descrivi();
}

class Zipline extends Attivita implements Prenotabile {
    private int lunghezza;

    public Zipline(String nome, double prezzo, int lunghezza) { ... } // chiama super(nome, prezzo)

    public String descrivi() { ... }

    public String prenota(String cognome) { ... }
}
```

**P3 ⭐ (0,5)** Il parco deve raccogliere oggetti `Percorso`, `Zipline` e `Parete` nello stesso array. Scrivi il tipo dell'array e spiega perché può contenere oggetti di tutte e tre le classi. Poi spiega perché dichiareresti `prenota` nell'interfaccia anziché in `Attivita`.

**Soluzione:** il tipo è `Attivita[]`. Ogni percorso, zipline e parete **è un** `Attivita`, quindi può essere messo in una casella di quel tipo (upcasting).

`prenota` sta nell'interfaccia perché è una capacità di **alcune** attività, non di tutte. Se fosse in `Attivita`, anche i percorsi dovrebbero averla, anche se non si prenotano.
