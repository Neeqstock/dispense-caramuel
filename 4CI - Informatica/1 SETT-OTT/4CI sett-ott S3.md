# SETTIMANA 3 — INCAPSULAMENTO: LA STALLA HA DELLE REGOLE

> **Progetto guida:** `LaStalla`.
>
> Questa settimana gli animali smettono di essere oggetti completamente esposti. Gli attributi non saranno piu modificabili da chiunque: la classe proteggera il proprio stato e offrira operazioni controllate.

## Obiettivi

Al termine dovresti saper:

- spiegare l'incapsulamento e l'information hiding;
- distinguere `public`, `private` e `protected`;
- dichiarare attributi privati;
- scrivere getter e setter;
- validare i dati prima di modificarli;
- distinguere un metodo di accesso da un'operazione del dominio;
- testare sia input validi sia input non validi.

---

## 1. Il problema: chiunque puo rompere la stalla

Nelle settimane precedenti abbiamo scritto una classe simile:

```java
public class Animale {
	String nome;
	String verso;
	int numeroZampe;
	double peso;

	public Animale(String nome, String verso, int numeroZampe, double peso) {
		this.nome = nome;
		this.verso = verso;
		this.numeroZampe = numeroZampe;
		this.peso = peso;
	}
}
```

Dal `main` potevamo scrivere:

```java
Animale pollo = new Animale("Coccodè", "Coccodè!", 2, 1.8);
pollo.numeroZampe = -12;
pollo.peso = -40.0;
pollo.nome = "";
```

Il compilatore non protesta: i tipi sono corretti. Ma il programma contiene un animale impossibile. Questo e un punto fondamentale:

> **Un programma puo essere sintatticamente corretto e concettualmente sbagliato.**

Il tipo `int` impedisce di scrivere una parola al posto di un numero, ma non impedisce di scrivere un numero senza senso. La classe deve quindi difendere le proprie regole.

---

## 2. Incapsulamento e information hiding

L'**incapsulamento** consiste nel racchiudere dati e operazioni dentro una classe, controllando come il resto del programma puo accedervi.

Un oggetto ben progettato non espone ogni dettaglio interno. Espone una piccola interfaccia pubblica, cioe un insieme di operazioni che gli altri oggetti possono usare.

```text
ESTERNO DEL PROGRAMMA
		│ usa operazioni pubbliche
		▼
┌────────────────────────────┐
│          Animale            │
│ stato privato:              │
│ nome, verso, zampe, peso    │
│ operazioni pubbliche:       │
│ getNome(), setNome(),       │
│ faiVerso(), aumentaPeso()   │
└────────────────────────────┘
```

La classe decide che cosa puo essere letto, che cosa puo essere modificato e con quali regole. Non e sempre necessario fornire un setter per ogni campo: un identificativo assegnato alla nascita potrebbe essere leggibile, ma non modificabile.

---

## 3. I modificatori di visibilita

| Modificatore | Significato operativo | Uso nel progetto |
|---|---|---|
| `public` | accessibile dall'esterno | metodi dell'interfaccia |
| `private` | accessibile solo nella stessa classe | stato interno |
| `protected` | accessibile nella classe e nelle sottoclassi | utile con `Pollo` e `Mucca` |
| nessun modificatore | visibilita limitata al package | da conoscere, senza insistere |

Regola pratica per `LaStalla`: **attributi `private`, metodi necessari all'esterno `public`.**

```java
public class Animale {
	private String nome;
	private String verso;
	private int numeroZampe;
	private double peso;

	public void faiVerso() {
		System.out.println(nome + " fa: " + verso);
	}
}
```

Ora `pollo.numeroZampe = -12` non compila. L'errore e utile: costringe il programma a usare l'interfaccia progettata dalla classe.

---

## 4. Getter, setter e validazione

Un **getter** restituisce il valore di un attributo. Un **setter** prova a modificarlo.

```java
public String getNome() {
	return nome;
}

public void setNome(String nome) {
	this.nome = nome;
}
```

Un setter puo controllare il dato:

```java
public void setPeso(double peso) {
	if (peso > 0) {
		this.peso = peso;
	} else {
		System.out.println("Errore: il peso deve essere positivo.");
	}
}
```

La differenza e decisiva:

```java
// Accesso diretto: nessun controllo
pollo.peso = -4;

// Setter: la classe puo rifiutare il dato
pollo.setPeso(-4);
```

### Invarianti della classe `Animale`

Un'invariante e una regola che dovrebbe restare vera per tutta la vita dell'oggetto. In questa versione scegliamo:

- `nome` non nullo e non vuoto;
- `verso` non nullo e non vuoto;
- `numeroZampe >= 0`;
- `peso > 0`.

La regola generale sulle zampe non va confusa con le regole dei sottotipi: un `Pollo` normalmente ha due zampe, mentre un animale generico potrebbe averne zero.

---

## 5. Codice guidato: `Animale` incapsulato

```java
public class Animale {
	private String nome;
	private String verso;
	private int numeroZampe;
	private double peso;

	public Animale(String nome, String verso, int numeroZampe, double peso) {
		setNome(nome);
		setVerso(verso);
		setNumeroZampe(numeroZampe);
		setPeso(peso);
	}

	public String getNome() { return nome; }

	public void setNome(String nome) {
		if (nome != null && !nome.trim().isEmpty()) {
			this.nome = nome;
		} else {
			System.out.println("Errore: il nome non puo essere vuoto.");
		}
	}

	public String getVerso() { return verso; }

	public void setVerso(String verso) {
		if (verso != null && !verso.trim().isEmpty()) {
			this.verso = verso;
		} else {
			System.out.println("Errore: il verso non puo essere vuoto.");
		}
	}

	public int getNumeroZampe() { return numeroZampe; }

	public void setNumeroZampe(int numeroZampe) {
		if (numeroZampe >= 0) {
			this.numeroZampe = numeroZampe;
		} else {
			System.out.println("Errore: le zampe non possono essere negative.");
		}
	}

	public double getPeso() { return peso; }

	public void setPeso(double peso) {
		if (peso > 0) {
			this.peso = peso;
		} else {
			System.out.println("Errore: il peso deve essere positivo.");
		}
	}

	public void faiVerso() {
		System.out.println(nome + " fa: " + verso);
	}

	public void aumentaPeso(double quantita) {
		if (quantita > 0) {
			peso += quantita;
		}
	}

	public String descrizioneBreve() {
		return nome + " ha " + numeroZampe + " zampe e pesa " + peso + " kg.";
	}
}
```

### Perche il costruttore usa i setter?

Cosi la validazione e concentrata in un solo punto. Se il costruttore assegnasse direttamente i campi, potrebbe accettare dati che i setter invece rifiutano.

---

## 6. Laboratorio — 3 ore

### Fase A — Rendere privati gli attributi (30 minuti)

1. Partire dalla versione della Settimana 2.
2. Aggiungere `private` a tutti gli attributi.
3. Provare a compilare il vecchio `main`.
4. Leggere gli errori dell'IDE.
5. Eliminare gli accessi diretti ai campi.

### Fase B — Getter e setter (45 minuti)

Scrivere getter e setter per `nome`, `verso`, `numeroZampe` e `peso`. Prima usare setter semplici, poi aggiungere i controlli.

### Fase C — Operazioni della stalla (45 minuti)

Aggiungere e provare:

```java
public void mangia() {
	System.out.println(nome + " sta mangiando.");
}

public void aumentaPeso(double quantita) {
	if (quantita > 0) {
		peso += quantita;
	}
}
```

Discutere la differenza tra `setPeso(5.0)`, che imposta un valore, e `aumentaPeso(0.2)`, che rappresenta un'operazione del dominio.

### Fase D — Test e consegna (60 minuti)

Creare `TestStalla.java` con un animale valido, tentativi non validi, una modifica corretta, `aumentaPeso()` e una stampa finale dello stato.

---

## 7. Esercizi pratici graduati

### Esercizio 1 — Accesso vietato

Spiegare perche questa riga non compila dopo l'incapsulamento e riscriverla con il metodo pubblico corretto:

```java
pollo.nome = "Pollo nuovo";
```

### Esercizio 2 — Setter sicuro

Scrivere `setNumeroZampe(int numeroZampe)` in modo che accetti zero o numeri positivi, rifiuti i negativi e conservi il vecchio valore quando il nuovo e invalido.

### Esercizio 3 — Getter booleano

Aggiungere `private boolean affamato`, poi scrivere `isAffamato()` e `setAffamato(boolean affamato)`.

### Esercizio 4 — Recinto protetto

Creare `Recinto` con `nome`, `capienzaMax` e `numeroAnimaliOspitati` privati. Scrivere `aggiungiAnimale()` senza superare la capienza.

### Esercizio 5 — Trova l'errore

Correggere questo setter e spiegare l'errore:

```java
public void setPeso(double peso) {
	if (peso < 0) {
		this.peso = peso;
	}
}
```

### Esercizio 6 — Relazione

Scrivere dieci righe rispondendo: perche un setter e piu utile di un attributo pubblico? In quale situazione della Stalla si vede chiaramente la differenza?

---

## 8. Verifica formativa

### Teoria

1. Definisci l'incapsulamento.
2. Qual e la differenza tra `public` e `private`?
3. Che cosa restituisce un getter?
4. Perche un setter puo contenere una condizione?
5. Che cos'e un'invariante?

### Lettura di codice

Dato:

```java
Animale a = new Animale("Muu", "Muuu!", 4, 500);
a.setPeso(-10);
System.out.println(a.getPeso());
```

Indicare quale valore dovrebbe essere stampato e motivare la risposta.

### Programmazione

Scrivere una classe `Animale` incapsulata con due attributi privati, un costruttore, getter, setter con controllo e un metodo di stampa.

## Compito per casa

Aggiungere a `Animale` il metodo `public String descrizioneBreve()`. Deve restituire una frase, non stamparla direttamente. Preparare anche due chiamate: una con input valido e una con input rifiutato.

## Domande guida per la lezione

- Chi deve sapere che un peso negativo non e valido: il `main` o `Animale`?
- Se domani cambia la regola sul peso, quanti file dobbiamo modificare?
- E sempre giusto fornire un setter per ogni attributo?
- Perche `aumentaPeso()` puo essere piu significativo di `setPeso()`?
