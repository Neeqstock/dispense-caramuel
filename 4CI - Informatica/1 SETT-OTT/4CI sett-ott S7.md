# SETTIMANA 7 — RIPASSO ATTIVO E SIMULAZIONE

Questa settimana non introduce un nuovo pilastro. Serve a collegare i concetti e a capire dove il progetto e solido e dove invece ci sono buchi.

## Mappa completa della Stalla

```text
Animale
├── attributi privati: nome, verso, zampe, peso
├── costruttori sovraccaricati
├── getter/setter e validazione
├── faiVerso(), mangia(int), mangia(KebabRadioattivo)
├── Pollo extends Animale: colorePiume, razzola(), override di faiVerso()
└── Mucca extends Animale: razza, produciLatte(), override di faiVerso()
```

## Le cinque domande fondamentali

1. **Che cosa descrive una classe?** Struttura e comportamento degli oggetti: attributi, costruttori e metodi.
2. **Che cos'e un oggetto?** Un'istanza concreta di una classe, con uno stato proprio.
3. **Perche `private`?** Per proteggere lo stato e imporre controlli attraverso l'interfaccia pubblica.
4. **Quando uso `extends`?** Quando esiste una relazione "e un" e la sottoclasse specializza la superclasse.
5. **Overloading o overriding?** Parametri diversi nella stessa classe significa overloading; stessa firma ridefinita nella sottoclasse significa overriding.

## Laboratorio di ripasso — tre ore

### Stazione A — Costruttori (35 minuti)

Scrivere tre modi validi per creare un `Animale` e individuare una chiamata impossibile.

### Stazione B — Incapsulamento (35 minuti)

Correggere una classe con campi pubblici, aggiungendo setter e controlli.

### Stazione C — Gerarchia (35 minuti)

Disegnare la gerarchia e implementare una nuova sottoclasse.

### Stazione D — Polimorfismo (35 minuti)

Scrivere un array di `Animale` e prevedere l'output di `faiVerso()`.

### Stazione E — KebabRadioattivo (25 minuti)

Dimostrare le due versioni di `mangia` e spiegare perche sono overload.

### Stazione F — Refactoring (15 minuti)

Rinominare variabili poco chiare, aggiungere metodi di stampa e ordinare il progetto.

## Simulazione scritta

### Parte A — Terminologia

Definire classe, oggetto, costruttore, incapsulamento, ereditarieta, overriding e polimorfismo.

### Parte B — Firma

Stabilire quali chiamate a `mangia` usano overload validi e quali firme sono duplicate: `mangia(int)`, `mangia(double)`, `mangia(String)`, una seconda `mangia(int)` e `mangia(int, int)`.

### Parte C — Codice

Completare `Animale`, `Pollo` e `Mucca` con costruttori, un metodo overridden e un array polimorfico.

### Parte D — Output

Spiegare l'output di un programma con riferimento `Animale` e oggetto `Pollo`.

## Checklist di autovalutazione

- [ ] So distinguere classe e oggetto.
- [ ] So scrivere un costruttore senza `void`.
- [ ] So usare `this`.
- [ ] So proteggere un attributo con `private`.
- [ ] So scrivere e chiamare getter e setter.
- [ ] So usare `extends` e `super`.
- [ ] So riconoscere `@Override`.
- [ ] So distinguere overloading e overriding.
- [ ] So spiegare il tipo statico e dinamico.
- [ ] So descrivere perche il pollo puo mangiare anche un `KebabRadioattivo`.

## Consegna

Consegnare una versione funzionante del progetto `LaStalla`, un diagramma della gerarchia e una pagina di spiegazione degli errori corretti durante il ripasso.
