# SETTIMANA 5 — EREDITARIETA: NASCONO `POLLO` E `MUCCA`

> **Progetto guida:** trasformiamo l'`Animale` generico in una famiglia di classi specializzate.

## Obiettivi

- spiegare superclasse e sottoclasse;
- usare `extends`;
- distinguere relazione "e un" da relazione "ha un";
- richiamare il costruttore della superclasse con `super(...)`;
- riutilizzare attributi e metodi senza copiare codice;
- progettare una gerarchia semplice e leggibile.

---

## 1. Perche serve l'ereditarieta?

Se scrivessimo da zero `Pollo` e `Mucca`, duplicheremmo nome, verso, peso, zampe e tutti i metodi comuni. La duplicazione aumenta gli errori: se correggiamo `faiVerso()` in una classe, dobbiamo ricordarci di correggerlo anche nelle altre.

L'ereditarieta permette di definire una classe generale e specializzarla:

```text
						 Animale
					   /         \
				  Pollo           Mucca
```

Un `Pollo` **e un** `Animale`. Una `Mucca` **e un** `Animale`. Questo e il criterio "e un".

Non vale invece per:

```text
Pollo ha un Recinto
Mucca ha un Proprietario
```

Queste sono relazioni di composizione o associazione, non ereditarieta.

---

## 2. Sintassi di `extends`

```java
public class Pollo extends Animale {
	private String colorePiume;
}

public class Mucca extends Animale {
	private boolean produceLatte;
}
```

La sottoclasse riceve dalla superclasse i membri accessibili secondo le regole di visibilita. Un attributo `private` della superclasse non diventa direttamente accessibile nella sottoclasse: si usano getter, setter o operazioni della superclasse.

---

## 3. Il costruttore e `super(...)`

Quando creiamo un `Pollo`, prima deve essere inizializzata la parte `Animale`. Usiamo `super(...)`:

```java
public class Pollo extends Animale {
	private String colorePiume;

	public Pollo(String nome, String verso, double peso, String colorePiume) {
		super(nome, verso, 2, peso);
		this.colorePiume = colorePiume;
	}
}
```

`super(...)` deve essere la prima istruzione del costruttore. Se la superclasse non ha un costruttore vuoto accessibile, la sottoclasse deve chiamare esplicitamente uno dei suoi costruttori.

La mucca:

```java
public class Mucca extends Animale {
	private String razza;

	public Mucca(String nome, double peso, String razza) {
		super(nome, "Muuu!", 4, peso);
		this.razza = razza;
	}
}
```

---

## 4. Riuso e specializzazione

Il codice comune resta in `Animale`:

```java
Animale animale = new Animale("Generico", "...", 4, 10);
animale.aumentaPeso(1.0);
System.out.println(animale.descrizioneBreve());
```

`Pollo` e `Mucca` possono aggiungere comportamenti specifici:

```java
public void razzola() {
	System.out.println(getNome() + " razzola nel terreno.");
}
```

```java
public void produciLatte() {
	System.out.println(getNome() + " produce latte.");
}
```

La sottoclasse non deve duplicare cio che ha gia senso per ogni animale.

---

## 5. Laboratorio — tre ore

### Fase A — Diagramma della gerarchia (30 minuti)

Disegnare `Animale`, `Pollo` e `Mucca`, indicando attributi e metodi propri o ereditati.

### Fase B — Creazione delle sottoclassi (60 minuti)

Implementare le classi con costruttori corretti e almeno un attributo specifico per ciascun sottotipo.

### Fase C — Test della costruzione (45 minuti)

Nel `main` creare:

```java
Pollo pollo = new Pollo("Coccodè", "Coccodè!", 1.8, "bianco");
Mucca mucca = new Mucca("Muucca", 540, "Pezzata");
```

Richiamare metodi comuni e specifici. Annotare quali chiamate sono possibili attraverso ogni riferimento.

### Fase D — Errori intenzionali (45 minuti)

Provare ad accedere direttamente a un campo `private` di `Animale` dalla sottoclasse. Leggere l'errore e correggere usando getter, setter o un metodo della superclasse.

---

## 6. Esercizi pratici graduati

1. Creare `Capra extends Animale` con il metodo `arrampicati()`.
2. Aggiungere alla gerarchia `Cane` con un attributo `razza`.
3. Scrivere una classe `Recinto` che **ha** una descrizione e una capienza: spiegare perche non deve estendere `Animale`.
4. Modificare la gerarchia perche `Pollo` abbia sempre due zampe e `Mucca` quattro.
5. Disegnare un diagramma con almeno due membri ereditati e due membri specifici.
6. Scrivere cosa si rompe se copiamo in ogni sottoclasse il codice di `aumentaPeso()`.

## Verifica formativa

Creare una superclasse `Animale` e due sottoclassi. La consegna deve contenere diagramma, codice, tre oggetti nel `main` e una breve spiegazione della chiamata `super(...)`.
