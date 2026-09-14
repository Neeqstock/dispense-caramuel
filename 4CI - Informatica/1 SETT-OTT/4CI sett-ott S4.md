# SETTIMANA 4 — OVERLOADING: PIU MODI PER FARE LA STESSA COSA

> **Progetto guida:** `LaStalla`.
>
> Un animale puo mangiare una quantita di cibo misurata in grammi, oppure un oggetto `KebabRadioattivo`. Il metodo si chiama sempre `mangia`, ma la firma cambia: e il nostro primo incontro serio con l'overloading.

## Obiettivi

- definire la firma di un metodo;
- distinguere overloading e overriding;
- riconoscere il ruolo di nome, numero e tipo dei parametri;
- scrivere metodi e costruttori sovraccaricati;
- evitare firme ambigue;
- progettare un'interfaccia comoda ma non confusa.

---

## 1. Che cos'e l'overloading?

L'**overloading** permette di avere piu metodi con lo stesso nome nella stessa classe, purche abbiano parametri diversi.

```java
public void mangia(int quantitaCibo) { ... }
public void mangia(String alimento) { ... }
```

Quando il programma incontra una chiamata, Java sceglie il metodo compatibile con gli argomenti:

```java
pollo.mangia(150);       // versione int
pollo.mangia("mais");   // versione String
```

La firma considera il nome del metodo, il numero, il tipo e l'ordine dei parametri. Il tipo restituito non basta a distinguere due metodi.

```java
// Non valido: stessa firma, cambia solo il ritorno
int calcola(int x) { return x; }
double calcola(int x) { return x; }
```

---

## 2. La classe `KebabRadioattivo`

```java
public class KebabRadioattivo {
	private String gusto;
	private int livelloRadioattivita;

	public KebabRadioattivo(String gusto, int livelloRadioattivita) {
		this.gusto = gusto;
		this.livelloRadioattivita = livelloRadioattivita;
	}

	public String getGusto() {
		return gusto;
	}

	public int getLivelloRadioattivita() {
		return livelloRadioattivita;
	}
}
```

Nella classe `Animale` aggiungiamo due versioni di `mangia`:

```java
public void mangia(int quantitaCibo) {
	if (quantitaCibo > 0) {
		System.out.println(getNome() + " mangia " + quantitaCibo + " grammi.");
	}
}

public void mangia(KebabRadioattivo kebab) {
	System.out.println(getNome() + " guarda il kebab radioattivo con prudenza.");
}
```

Queste due versioni hanno lo stesso nome, ma firme diverse. La scelta avviene in base al tipo degli argomenti.

---

## 3. Costruttori sovraccaricati

Anche i costruttori possono essere sovraccaricati:

```java
public Animale(String nome, String verso, int numeroZampe, double peso) { ... }

public Animale(String nome, String verso) {
	this(nome, verso, 4, 1.0);
}

public Animale() {
	this("Senza nome", "...", 0, 1.0);
}
```

La chiamata `this(...)` deve essere la prima istruzione e richiama un altro costruttore della stessa classe. Cosi evitiamo di duplicare le assegnazioni.

---

## 4. Overloading e overriding

| Concetto | Dove avviene | Come cambia |
|---|---|---|
| overloading | stessa classe | cambia la firma dei parametri |
| overriding | sottoclasse | stessa firma, comportamento specializzato |

Overloading:

```java
pollo.mangia(100);
pollo.mangia(kebab);
```

Overriding, che useremo dalla Settimana 5:

```java
class Pollo extends Animale {
	@Override
	public void faiVerso() {
		System.out.println("Coccodè!");
	}
}
```

---

## 5. Laboratorio — tre ore

### Fase A — Metodi di stampa (40 minuti)

Scrivere nella classe `Animale`:

```java
public void stampa() { ... }
public void stampa(String prefisso) { ... }
```

Provare entrambe le chiamate e osservare quale firma viene scelta.

### Fase B — Cibo normale (40 minuti)

Implementare `mangia(int quantitaCibo)`, rifiutando quantita nulle o negative.

### Fase C — KebabRadioattivo (60 minuti)

Creare la classe, istanziarla nel `main` e implementare `mangia(KebabRadioattivo kebab)`. La versione radioattiva deve produrre un messaggio diverso.

### Fase D — Test dell'overload (40 minuti)

Scrivere almeno sei chiamate e annotare la versione scelta. Provare anche una chiamata ambigua e spiegare l'errore del compilatore.

---

## 6. Esercizi pratici graduati

1. Aggiungere `mangia(double quantitaCibo)` e spiegare la differenza rispetto a `mangia(int)`.
2. Scrivere tre costruttori per `KebabRadioattivo`: vuoto, con gusto, completo.
3. Progettare `beve(int millilitri)` e `beve(String bevanda)`.
4. Trovare perche `mangia(int)` e `mangia(Integer)` possono produrre chiamate poco chiare.
5. Scrivere una tabella con chiamata, tipo degli argomenti e metodo selezionato.
6. Spiegare perche `int mangia(int)` e `void mangia(int)` non possono coesistere.
7. Creare `Mangime` con `tipo`, `quantita` e `biologico`, poi aggiungere `mangia(Mangime mangime)`.

## 7. Verifica formativa

- definizione di firma;
- tre esempi di overloading;
- confronto overloading/overriding;
- completamento di un metodo `mangia`;
- previsione dell'output di un programma con costruttori sovraccaricati;
- correzione di una firma duplicata.

## Compito per casa

Documentare in una pagina perche il metodo si chiama `mangia` sia quando riceve un `int` sia quando riceve un `KebabRadioattivo`. Includere due esempi di chiamata e una frase sulla firma.
