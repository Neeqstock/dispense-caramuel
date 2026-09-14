# SETTIMANA 6 — OVERRIDING E POLIMORFISMO: LA STALLA PARLA

> Questa e la settimana del pollo che mangia sia una quantita di cibo sia un `KebabRadioattivo`. Il kebab serve a separare due idee: **overloading** dei metodi `mangia` e **polimorfismo** dei comportamenti ereditati.

## Obiettivi

- distinguere overriding e overloading;
- ridefinire un metodo con `@Override`;
- usare `super.metodo()`;
- capire tipo statico e tipo dinamico;
- usare un riferimento `Animale` per contenere un `Pollo` o una `Mucca`;
- osservare il binding dinamico durante l'esecuzione.

---

## 1. Overriding: stesso contratto, comportamento diverso

La classe `Animale` puo avere:

```java
public void faiVerso() {
	System.out.println(getNome() + " fa un verso.");
}
```

Il pollo puo specializzarlo:

```java
@Override
public void faiVerso() {
	System.out.println(getNome() + " fa: Coccodè!");
}
```

La firma resta la stessa. Non stiamo aggiungendo un nuovo metodo: stiamo sostituendo il comportamento ereditato quando l'oggetto reale e un `Pollo`.

L'annotazione `@Override` chiede al compilatore di verificare che stiamo davvero ridefinendo un metodo esistente.

---

## 2. `super` nel metodo

Possiamo usare il comportamento generale e poi aggiungere dettagli:

```java
@Override
public void faiVerso() {
	super.faiVerso();
	System.out.println("Il pollo agita le ali.");
}
```

`super.faiVerso()` richiama l'implementazione della superclasse. `this` indica l'oggetto corrente; `super` indica la parte della superclasse.

---

## 3. Tipo statico e tipo dinamico

```java
Animale animale = new Pollo("Coccodè", "Coccodè!", 1.8, "bianco");
```

Qui ci sono due punti di vista:

- **tipo statico:** `Animale`, dichiarato a sinistra;
- **tipo dinamico:** `Pollo`, oggetto creato a destra.

Il riferimento puo usare solo i metodi visibili nel tipo statico:

```java
animale.faiVerso(); // consentito
animale.razzola();  // non consentito se Animale non dichiara razzola()
```

Per un metodo sottoposto a overriding Java sceglie pero l'implementazione del tipo dinamico:

```java
animale.faiVerso(); // esegue la versione di Pollo
```

Questo e il **binding dinamico**.

---

## 4. Una stalla polimorfica

```java
Animale[] stalla = {
	new Pollo("Coccodè", "Coccodè!", 1.8, "bianco"),
	new Mucca("Muucca", 540, "Pezzata"),
	new Animale("Animale misterioso", "...", 4, 10)
};

for (Animale animale : stalla) {
	animale.faiVerso();
}
```

Il ciclo conosce solo `Animale`, ma ogni elemento risponde secondo la propria classe concreta. Lo stesso messaggio produce comportamenti diversi.

---

## 5. Il kebab e l'overloading

Questi metodi sono **overload**, non override:

```java
public void mangia(int quantitaCibo) {
	System.out.println(getNome() + " mangia " + quantitaCibo + " grammi.");
}

public void mangia(KebabRadioattivo kebab) {
	System.out.println(getNome() + " affronta il kebab: " + kebab.getGusto());
}
```

Se il pollo ridefinisce `mangia(int)`, quello e overriding della versione ereditata, mentre `mangia(KebabRadioattivo)` resta un overload distinto.

---

## 6. Laboratorio — tre ore

### Fase A — Override dei versi (50 minuti)

Implementare versioni diverse di `faiVerso()` in `Pollo` e `Mucca`. Usare `@Override` e provare deliberatamente a sbagliare il nome del metodo.

### Fase B — Array polimorfico (50 minuti)

Creare un array `Animale[]`, inserire almeno quattro animali e richiamare `faiVerso()` in un ciclo.

### Fase C — Cibo e kebab (50 minuti)

Creare un `KebabRadioattivo`, chiamare entrambe le versioni di `mangia` e spiegare quale concetto e coinvolto in ciascuna chiamata.

### Fase D — Debug orale (30 minuti)

Per ogni riga dire se compila e perche:

```java
Animale a = new Pollo(...);
a.faiVerso();
a.razzola();
((Pollo) a).razzola();
```

---

## 7. Esercizi pratici

1. Aggiungere `Asino` con un verso personalizzato.
2. Creare `Animale[]` e contare quanti elementi sono `Pollo` usando `instanceof`.
3. Scrivere `faiCantare(Animale animale)` che chiami solo `faiVerso()`.
4. Spiegare perche `faiCantare` funziona con animali diversi senza conoscere la classe concreta.
5. Aggiungere `mangia(KebabRadioattivo)` e verificare l'overloading su un riferimento `Animale`.
6. Correggere un metodo con `@Override` scritto con parametri diversi e spiegare perche quello e overloading.

## Verifica formativa

Prevedere l'output di un programma con tre animali, due metodi overridden e due overload di `mangia`. Poi implementare una piccola gerarchia funzionante.
