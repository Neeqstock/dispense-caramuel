# Macchine di Turing e completezza

## Che cos'è una macchina di Turing?

Una **macchina di Turing** è un modello teorico, immaginato dal matematico Alan Turing nel 1936, per descrivere che cosa significa “eseguire un calcolo”. Non è un computer da costruire: è una macchina molto semplice con cui ragionare sui limiti e sulle possibilità degli algoritmi.

Possiamo immaginarla così:

```text
Nastro infinito:  ... | 0 | 1 | 1 | 0 | 0 | 1 | ...
                         ^
                         |
                 testina di lettura/scrittura
                         |
                    stato interno
```

La macchina possiede:

- un **nastro** diviso in celle, che contiene simboli;
- una **testina** che legge e può modificare una cella;
- un insieme finito di **stati interni**;
- una serie di regole che dicono: “se leggi questo simbolo mentre sei in questo stato, scrivi questo, spostati a destra o a sinistra e cambia stato”.

La macchina procede un passo alla volta. Anche se è semplicissima, può rappresentare algoritmi molto complessi, se dispone di abbastanza tempo e spazio.

## Che cosa significa “Turing completo”?

Un sistema è **Turing completo** quando, in linea di principio, può eseguire qualunque calcolo eseguibile da una macchina di Turing.

In pratica deve poter:

1. conservare e modificare informazioni;
2. eseguire istruzioni condizionali, come `se... allora...`;
3. ripetere istruzioni, per esempio con cicli;
4. usare una quantità di memoria che possa crescere, almeno nel modello teorico.

Essere Turing completi non significa essere veloci, comodi o adatti a ogni problema. Significa avere una potenza di calcolo generale: con abbastanza risorse, il sistema può simulare altri sistemi computazionali.

## Esempi

Sono Turing completi, o progettati per esserlo:

- i comuni linguaggi di programmazione, come Python, Java e C;
- i computer moderni;
- molti linguaggi esoterici, anche se difficilissimi da usare;
- alcuni giochi o dispositivi programmabili, se offrono memoria, condizioni e ripetizioni sufficienti.

Una calcolatrice tascabile molto semplice, invece, potrebbe non essere Turing completa se può eseguire soltanto un insieme fisso di operazioni e non dispone di memoria o controllo abbastanza generale.

## L'idea da ricordare

> **Una macchina di Turing è un modello minimo di calcolatore. Un sistema Turing completo è abbastanza generale da poter simulare quel modello.**

La completezza di Turing parla quindi di **possibilità teorica**, non di qualità del programma, velocità del computer o utilità pratica.

## Una conseguenza importante

Turing mostrò anche che esistono problemi che nessun programma può risolvere sempre. Il più famoso è il **problema dell'arresto**: non esiste un algoritmo generale capace di ricevere qualunque programma e qualunque input e stabilire sempre, in anticipo, se quel programma finirà oppure continuerà per sempre.

Quindi:

```text
Turing completo ≠ può fare ogni cosa

Turing completo = può esprimere ogni calcolo esprimibile,
                  ma esistono domande che nessun algoritmo
                  può risolvere in tutti i casi.
```

## Domanda per la classe

Un sistema può essere Turing completo ma praticamente inutilizzabile? Pensate a un linguaggio con memoria sufficiente e tutte le istruzioni necessarie, ma così lento o scomodo da rendere impossibile scrivere programmi reali.
