# 🧭 Python: scope, cioè dove vive una variabile

⏱️ **Tempo di studio:** ✅ 10 minuti · 🔍 5 minuti in più · 🤓 facoltativo

**Legenda:** ✅ minimo da sapere · 🔍 per il voto alto · 🤓 curiosità · ✏️ esercizio · 🃏 flashcard · ⚠️ errore comune

> Un castello ha stanze, corridoi, un cortile e le regole del regno. Quando l'eroe cerca un oggetto, guarda prima nella stanza, poi nel corridoio, poi nel castello, poi nel regno. Python fa lo stesso con le variabili.

## Che cos'è lo scope

Lo **scope** (in italiano **ambito**) è la parte del programma in cui una variabile esiste e si può usare. Una variabile vive in un posto preciso. Non sempre si vede dagli altri posti.

### ✅ La regola LEGB

<u>Quando usi un nome, Python lo cerca in quattro posti, in quest'ordine: **L**ocal, **E**nclosing, **G**lobal, **B**uilt-in. Si ferma al primo posto in cui lo trova.</u>

- **Local** (locale): dentro la funzione in cui ti trovi.
- **Enclosing** (racchiudente): nella funzione che contiene quella in cui ti trovi. Succede solo con una **funzione annidata**, cioè una funzione dentro un'altra.
- **Global** (globale): nel file, fuori da ogni funzione.
- **Built-in** (predefinito): le funzioni e i nomi già pronti in Python, come `print` e `len`.

Esempio: quale `x` vince?

```python
x = "globale"

def f():
    x = "locale"
    print(x)

f()
print(x)
```

→ stampa `locale`, poi `globale`. Dentro `f` il nome `x` si trova subito nella funzione, quindi Python non sale fino al globale.

<details><summary>🃏 <b>Che cosa significa LEGB?</b></summary>
Sono le quattro aree in cui Python cerca un nome, nell'ordine Local, Enclosing, Global, Built-in.
</details>

<details><summary>🃏 <b>Dove cerca Python per primo?</b></summary>
Nella funzione in cui si trova il codice: è lo scope Local.
</details>

### ✅ Le quattro stanze

**Local.** La variabile `a` nasce e muore dentro la funzione.

```python
def mia_funzione():
    a = 5
    print(a)

mia_funzione()
```

→ stampa `5`.

⚠️ Fuori dalla funzione `a` non esiste. Scrivere `print(a)` dopo la chiamata dà `NameError: name 'a' is not defined`.

**Enclosing.** La funzione interna non ha `x`: lo cerca nella funzione che la contiene.

```python
def esterna():
    x = "esterno"

    def interna():
        print(x)

    interna()

esterna()
```

→ stampa `esterno`.

**Global.** La variabile `y` vive nel file e si vede da ogni funzione.

```python
y = 10

def un_altra_funzione():
    print(y)

un_altra_funzione()
```

→ stampa `10`.

**Built-in.** Non hai definito `len`: è già pronta in Python.

```python
print(len("ciao"))
```

→ stampa `4`.

<details><summary>🃏 <b>Che cosa indica Built-in?</b></summary>
Le funzioni e i nomi già pronti in Python, come `print` e `len`, che non devi definire tu.
</details>

<details><summary>🃏 <b>Dove vive una variabile creata dentro una funzione?</b></summary>
Nello scope Local della funzione: fuori dalla funzione non esiste.
</details>

## Cambiare una variabile da dentro una funzione

Leggere una variabile del file è facile. Modificarla non lo è.

### 🔍 La parola chiave `global`

Il contatore di monete dell'eroe deve crescere a ogni moneta raccolta. Prova a scrivere così:

```python
contatore = 0

def incrementa():
    contatore += 1

incrementa()
```

⚠️ Python dà `UnboundLocalError: cannot access local variable 'contatore' where it is not associated with a value`. Un **UnboundLocalError** è un errore che dice: una variabile locale è usata prima di avere un valore. Il testo preciso del messaggio cambia fra versioni di Python; la parte importante è il nome dell'errore.

Il motivo: <u>se assegni un valore a un nome dentro una funzione, Python lo considera locale.</u> Per dire «parlo della variabile del file» serve `global`:

```python
contatore = 0

def incrementa():
    global contatore
    contatore += 1

incrementa()
incrementa()
print(contatore)
```

→ stampa `2`.

<details><summary>🃏 <b>A che cosa serve `global`?</b></summary>
A dire alla funzione che il nome è quello della variabile del file, così la funzione può modificarla.
</details>

### 🔍 La parola chiave `nonlocal`

`nonlocal` funziona come `global`, ma per le funzioni annidate. Dice: «la variabile non è mia, è della funzione che mi contiene».

```python
def contatore_esterno():
    c = 0

    def incremento_interno():
        nonlocal c
        c += 1
        print(c)

    incremento_interno()
    incremento_interno()

contatore_esterno()
```

→ stampa `1`, poi `2`.

<details><summary>🃏 <b>In quale caso si usa `nonlocal`?</b></summary>
In una funzione annidata, per modificare una variabile della funzione che la contiene.
</details>

## Un tranello: `if`, `for` e `while`

### ⚠️ I blocchi non cambiano stanza

In Java e in C++ una variabile creata dentro un `if` muore alla fine del blocco. In Python **<u>`if`, `for` e `while` non creano un nuovo scope</u>**: la variabile resta anche dopo.

```python
if True:
    messaggio = "Ciao"

print(messaggio)
```

→ stampa `Ciao`.

🔍 Lo stesso vale per la variabile del ciclo:

```python
for i in range(3):
    pass

print(i)
```

→ stampa `2`, l'ultimo valore del ciclo.

<details><summary>🃏 <b>Un `if` crea un nuovo scope in Python?</b></summary>
No: una variabile creata dentro un `if` esiste anche dopo il blocco.
</details>

## 🤓 Curiosità: un nome può coprire una funzione

```python
print(len("ciao"))
len = 5
print(len("ciao"))
```

→ stampa `4`, poi si ferma con `TypeError: 'int' object is not callable`.

L'assegnazione `len = 5` crea una variabile globale che copre la funzione predefinita `len`. Per questo non è una buona idea dare a una variabile il nome di una funzione predefinita.

## ✏️ Esercizi

1. **Prevedi prima di eseguire.** Che cosa stampa questo codice? Scrivi la risposta prima di eseguirlo.

```python
nome = "Aria"

def saluta():
    print(nome)
    nome = "Bran"

saluta()
```

2. **Trova la stanza.** Nel primo esempio della dispensa, dove trova Python il nome `print`? E il nome `f`? Scrivi la lettera LEGB per ciascuno.

3. **Spiega in una frase.** Perché `contatore += 1`, senza `global`, dà errore? Usa le parole «scope» e «locale».

## Fonti

- *Python Docs, Naming and binding* (riferimento ufficiale su come Python associa i nomi): <https://docs.python.org/3/reference/executionmodel.html>. Leggi il paragrafo su `global` e `nonlocal`.
