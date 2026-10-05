# 🧩 Anatomia di un'istruzione in linguaggio macchina

Un programma è una sequenza di **istruzioni**. Ogni istruzione dice alla CPU quale operazione eseguire e su quali dati lavorare.

## Un esempio

```text
ADD R3, R1, R2
```

Possiamo leggerla così:

> Somma i contenuti di `R1` e `R2`, poi metti il risultato in `R3`.

Questa istruzione contiene tre parti importanti:

```text
+---------+-------------------+----------------+
| opcode  | operando sorgente | destinazione   |
+---------+-------------------+----------------+
| ADD     | R1, R2            | R3             |
+---------+-------------------+----------------+
| cosa    | quali dati usare  | dove salvare   |
+---------+-------------------+----------------+
```

## Le parti principali

- **Opcode:** indica l'operazione, per esempio `ADD`, `SUB`, `LOAD`, `STORE` o `JUMP`.
- **Operandi:** indicano i dati, i registri o gli indirizzi coinvolti.
- **Destinazione:** indica dove mettere il risultato, quando l'operazione produce un risultato.

A volte un'istruzione non ha una destinazione esplicita:

```text
JUMP 250
```

Significa: “continua l'esecuzione a partire dall'indirizzo 250”.

## Dal testo ai bit

`ADD R3, R1, R2` è una forma leggibile dagli esseri umani, chiamata spesso **assembly** o linguaggio simbolico. La CPU, invece, riceve una codifica binaria:

```text
+----------+----------+----------+----------+
| opcode   | registro | registro | registro |
| ADD      | R3       | R1       | R2       |
+----------+----------+----------+----------+
```

I bit che rappresentano l'opcode e i registri dipendono dall'architettura del processore. La Control Unit legge questi campi, li decodifica e genera i segnali necessari per eseguire l'operazione.

## Non tutte le istruzioni usano registri

Un'istruzione può contenere anche:

```text
LOAD R1, 200       carica in R1 il dato che si trova all'indirizzo 200
ADD R2, R1, 5      somma a R1 il valore immediato 5 e salva in R2
STORE R2, 300      salva R2 all'indirizzo 300
```

Il numero `5` nell'istruzione `ADD R2, R1, 5` è un **valore immediato**: è scritto direttamente nell'istruzione, non deve essere cercato in un'altra posizione di memoria.

## Il collegamento con il ciclo macchina

Quando la CPU esegue un'istruzione:

```text
FETCH       legge l'istruzione dalla memoria
DECODE      separa e interpreta opcode e operandi
EXECUTE     esegue l'operazione
WRITE-BACK  salva il risultato, se necessario
```

Per esempio, con:

```text
ADD R3, R1, R2
```

la CPU deve capire:

1. che l'operazione è una somma (`ADD`);
2. che deve leggere `R1` e `R2`;
3. che deve attivare l'ALU per sommare;
4. che deve scrivere il risultato in `R3`.

> **In sintesi:** un'istruzione è un piccolo comando codificato. L'opcode dice “che cosa fare”; gli operandi dicono “su quali dati”; la destinazione dice “dove mettere il risultato”.
