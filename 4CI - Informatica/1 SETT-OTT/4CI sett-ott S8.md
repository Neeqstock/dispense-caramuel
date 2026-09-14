# SETTIMANA 8 — VERIFICA E CHIUSURA DEL PRIMO BLOCCO

## Scopo della settimana

La verifica misura se sai costruire e spiegare una piccola soluzione a oggetti. Non basta che il programma parta: devono essere leggibili anche la progettazione, i nomi e le scelte.

---

## 1. Prova teorica suggerita

### Parte A — Conoscenze (3 punti)

1. Definire classe e oggetto.
2. Spiegare costruttore e `this`.
3. Distinguere `private`, `public` e `protected`.
4. Definire overloading e overriding.
5. Spiegare tipo statico, tipo dinamico e binding dinamico.

### Parte B — Lettura di codice (3 punti)

Individuare errori e prevedere l'output di frammenti con:

- costruttori sovraccaricati;
- getter e setter;
- `extends` e `super`;
- `@Override`;
- riferimento `Animale` a oggetto `Pollo`.

### Parte C — Progettazione (2 punti)

Dato il testo "una stalla gestisce polli e mucche", disegnare una gerarchia e indicare due attributi comuni e uno specifico per ogni sottoclasse.

### Parte D — Correzione (2 punti)

Correggere una classe con attributi pubblici, setter senza validazione e metodo erroneamente annotato `@Override`.

---

## 2. Prova pratica suggerita — La Stalla

Realizzare un progetto con almeno questi file:

```text
Animale.java
Pollo.java
Mucca.java
KebabRadioattivo.java
TestStalla.java
```

### Requisiti minimi

1. `Animale` deve avere almeno tre attributi privati.
2. Deve avere un costruttore completo.
3. Deve avere almeno due getter e due setter, con una validazione.
4. Deve avere `faiVerso()` e almeno due overload di `mangia`.
5. `Pollo` e `Mucca` devono usare `extends` e `super(...)`.
6. Almeno una sottoclasse deve fare overriding di `faiVerso()`.
7. Il `main` deve usare un array o una lista di riferimenti `Animale`.
8. Deve essere creato almeno un `KebabRadioattivo`.
9. Il programma deve mostrare almeno un input rifiutato.
10. Il progetto deve includere un breve `README.md`.

---

## 3. Traccia operativa per gli studenti

1. Disegnare la gerarchia prima di scrivere il codice.
2. Scrivere prima `Animale` e testarla.
3. Creare `Pollo` e `Mucca` usando `super`.
4. Aggiungere l'override dei versi.
5. Aggiungere i due overload di `mangia`.
6. Creare il test polimorfico.
7. Provare dati validi e non validi.
8. Sistemare nomi, formattazione e README.

Non copiare codice da un file all'altro senza capire dove appartiene. Se un comportamento vale per ogni animale, probabilmente appartiene ad `Animale`; se vale solo per un sottotipo, appartiene alla sottoclasse.

---

## 4. Esempio di test minimo

```java
public class TestStalla {
	public static void main(String[] args) {
		Animale[] stalla = {
			new Pollo("Coccodè", "Coccodè!", 1.8, "bianco"),
			new Mucca("Muucca", 540, "Pezzata")
		};

		for (Animale animale : stalla) {
			animale.faiVerso();
			animale.mangia(100);
		}

		KebabRadioattivo kebab = new KebabRadioattivo("piccante", 3);
		stalla[0].mangia(kebab);
		stalla[0].setNumeroZampe(-1);
	}
}
```

Durante la discussione finale chiedere:

- quale versione di `faiVerso()` viene eseguita;
- quale overload di `mangia` viene scelto;
- perche il setter rifiuta `-1`;
- quale tipo statico ha `stalla[0]` e quale tipo dinamico ha l'oggetto.

---

## 5. Griglia di valutazione possibile

| Area | Punti |
|---|---:|
| Comprensione dei concetti | 2 |
| Classi, costruttori e `this` | 2 |
| Incapsulamento e validazione | 2 |
| Ereditarieta e `super` | 1.5 |
| Overloading, overriding e polimorfismo | 1.5 |
| Test, ordine e spiegazione | 1 |
| **Totale** | **10** |

La correttezza sintattica e importante, ma non deve cancellare la valutazione del ragionamento. Un errore di parentesi e diverso dal non sapere dove collocare una responsabilita.

---

## 6. Recupero

Per chi non completa il progetto, proporre una versione ridotta con:

- `Animale`;
- una sottoclasse `Pollo`;
- un costruttore;
- due attributi privati;
- un getter;
- un setter validato;
- un override di `faiVerso()`;
- un `main` con due oggetti.

La prova di recupero deve includere anche una spiegazione orale di classe, oggetto e overriding.

## 7. Approfondimento

Per chi termina prima:

- aggiungere `Capra` e `Asino`;
- usare `ArrayList<Animale>`;
- contare le zampe complessive;
- cercare l'animale piu pesante;
- aggiungere un metodo `nutriCon(Mangime mangime)`;
- scrivere test separati per input validi e non validi.

## Chiusura del bimestre

Il risultato atteso non e una stalla perfetta. E una prima architettura coerente, capace di rappresentare oggetti, proteggere il proprio stato, riusare codice e scegliere comportamenti diversi in base al tipo reale dell'animale.

Il progetto proseguira con collezioni, file e persistenza: la stalla dovra crescere oltre i pochi oggetti scritti a mano nel `main`.
