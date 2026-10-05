# 🗺️ Mappa delle astrazioni: come si istruisce un computer

Programmare significa trovare un modo per dire a una macchina che cosa deve fare. Nel corso della storia è cambiato il linguaggio dell'istruzione: siamo passati dal modificare fisicamente la macchina al descrivere un'intenzione con parole quasi naturali.

> Più saliamo, meno dettagli dobbiamo specificare. Più scendiamo, più siamo vicini ai segnali elettrici che la macchina esegue davvero.

## La mappa

```text
      più vicino al modo umano di esprimere un'intenzione
                             ^
                             |
+---------------------------------------------------------+
| LINGUAGGIO NATURALE + RETI NEURALI                     |
| "Ordina questi dati e mostrami i più frequenti"        |
| intenzione interpretata da un modello                  |
+----------------------------+----------------------------+
                             | prompt, esempi, vincoli
+----------------------------v----------------------------+
| PROGRAMMAZIONE DICHIARATIVA / VISUALE                  |
| descrivo che cosa voglio, non ogni passaggio           |
| SQL, regole, fogli di calcolo, blocchi visuali         |
+----------------------------+----------------------------+
                             | compilatore / interprete
+----------------------------v----------------------------+
| LINGUAGGI DI ALTO LIVELLO                              |
| Python, Java, C, JavaScript                            |
| variabili, funzioni, cicli, classi, strutture dati     |
+----------------------------+----------------------------+
                             | compilazione / assemblaggio
+----------------------------v----------------------------+
| ASSEMBLY                                               |
| nomi leggibili per le istruzioni della CPU             |
| LOAD, ADD, STORE, JUMP; registri e indirizzi           |
+----------------------------+----------------------------+
                             | traduzione in codici binari
+----------------------------v----------------------------+
| LINGUAGGIO MACCHINA                                   |
| opcode, operandi e indirizzi rappresentati come bit   |
| 0101 0010 1100 ...                                    |
+----------------------------+----------------------------+
                             | istruzioni interpretate dalla CPU
+----------------------------v----------------------------+
| CIRCUITI DIGITALI                                     |
| porte logiche, registri, ALU, Control Unit            |
| AND, OR, NOT, XOR                                     |
+----------------------------+----------------------------+
                             | transistor come interruttori
+----------------------------v----------------------------+
| LIVELLO FISICO/ELETTRICO                              |
| tensioni, correnti, cariche e transistor              |
+---------------------------------------------------------+
      più vicino a ciò che accade fisicamente nella macchina
```

La programmazione ad alto livello non elimina gli strati inferiori: li usa e li nasconde. Una riga Python deve comunque diventare istruzioni, bit, segnali e infine cambiamenti fisici nei transistor.

---

## 1. Istruire modificando la macchina

I primi calcolatori non erano programmati scrivendo righe su uno schermo. Per cambiare il comportamento si potevano:

- ricablare collegamenti elettrici;
- impostare interruttori;
- inserire schede perforate;
- configurare pannelli e sequenze fisiche.

L'istruzione era quindi molto vicina all'hardware. Cambiare programma poteva significare cambiare fisicamente la configurazione della macchina.

```text
programma = collegamenti, interruttori o schede
```

Il vantaggio era il controllo diretto. Il difetto era enorme: programmare era lento, fragile e difficile da modificare.

## 2. Istruire con il linguaggio macchina

Con il modello a programma memorizzato, le istruzioni possono stare nella memoria insieme ai dati.

Una CPU riconosce codici binari che indicano operazioni come:

```text
carica un dato
somma
salva un risultato
salta a un altro indirizzo
```

Un'istruzione macchina contiene campi codificati in bit, per esempio:

```text
+--------+----------+----------+----------+
| opcode | sorgente | sorgente | destinaz.|
|  ADD   |    R1    |    R2    |    R3    |
+--------+----------+----------+----------+
```

È già possibile cambiare programma senza ricablare la macchina, ma il programmatore deve ragionare in termini di registri, indirizzi e istruzioni elementari.

## 3. Istruire con l'assembly

L'assembly sostituisce i codici binari con abbreviazioni leggibili:

```text
LOAD  R1, 200
LOAD  R2, 201
ADD   R3, R1, R2
STORE R3, 202
```

Un **assembler** traduce queste parole nei codici macchina corrispondenti.

L'assembly è più leggibile del binario, ma resta vicino alla CPU: bisogna decidere quali registri usare, come spostare i dati e quali salti eseguire.

## 4. I linguaggi di alto livello

Nei linguaggi di alto livello possiamo esprimere un algoritmo senza descrivere ogni movimento fra registri:

```python
risultato = valore1 + valore2
```

Il compilatore o l'interprete si occupa di trasformare questa istruzione in molte operazioni più vicine alla macchina.

Compaiono concetti più ricchi:

- variabili e tipi;
- funzioni;
- cicli e condizioni;
- strutture dati;
- classi e oggetti;
- gestione degli errori.

Il programmatore guadagna chiarezza e velocità di sviluppo, ma perde il controllo diretto su molti dettagli dell'hardware.

## 5. Descrivere invece di comandare: dichiarativo e visuale

In alcuni linguaggi non descriviamo tutti i passaggi. Descriviamo il risultato o le regole che vogliamo ottenere.

Esempio SQL:

```sql
SELECT nome
FROM studenti
WHERE voto >= 8;
```

Qui non diciamo come scorrere fisicamente ogni riga del database. Diciamo quale insieme di risultati ci interessa; il sistema sceglie una strategia per trovarli.

Ne fanno parte, con modalità diverse:

- SQL e altri linguaggi dichiarativi;
- linguaggi basati su regole;
- fogli di calcolo;
- ambienti a blocchi visuali;
- configurazioni e descrizioni di infrastrutture.

Questo è un ulteriore salto: dall'istruire passo-passo al dichiarare che cosa deve essere vero o prodotto.

## 6. Parlare a un computer in linguaggio naturale

Con una rete neurale o un modello linguistico possiamo formulare una richiesta come:

> “Prendi questi dati, raggruppali per mese e spiegami le anomalie.”

Questa non è una normale istruzione macchina. È una richiesta ambigua e ricca, che un modello prova a interpretare usando il contesto e gli esempi appresi.

```text
intenzione in linguaggio naturale
              |
              v
rete neurale / modello linguistico
              |
              v
codice, chiamate a strumenti o testo prodotto
              |
              v
linguaggi e istruzioni eseguite dal computer
```

Le reti neurali sono quindi un **nuovo strato di interazione**, non un sostituto della CPU o dei linguaggi. Il sistema deve comunque trasformare la richiesta in operazioni concrete e può interpretarla male.

Il vantaggio è l'accessibilità: possiamo descrivere un obiettivo senza conoscere tutta la sintassi. Il rischio è l'ambiguità: il computer può produrre qualcosa di plausibile ma sbagliato.

---

## Lo stesso compito a livelli diversi

Compito: sommare i valori contenuti in due celle.

```text
LINGUAGGIO NATURALE
"Somma i due valori e mostrami il risultato."

SQL / DICHIARATIVO
SELECT valore1 + valore2;

ALTO LIVELLO
risultato = valore1 + valore2

ASSEMBLY
ADD R3, R1, R2

MACCHINA
codice binario dell'istruzione ADD

CIRCUITI
porte logiche che calcolano la somma dei bit

FISICA
transistor che cambiano stato in risposta a tensioni elettriche
```

È lo stesso obiettivo, ma espresso con quantità diverse di dettagli.

## Come è cambiato il modo di programmare?

```text
ricablare la macchina
        ↓
impostare bit e istruzioni
        ↓
usare nomi assembly
        ↓
scrivere algoritmi in linguaggi di alto livello
        ↓
descrivere regole e risultati
        ↓
formulare intenzioni in linguaggio naturale
```

Ogni passaggio ha aumentato l'astrazione e ridotto il lavoro meccanico. Ma ogni passaggio ha anche aggiunto traduttori, interpretazioni e possibili errori.

> **Più astrazione significa più comodità, non necessariamente più comprensione.**

## Tre cose da ricordare

1. Un computer esegue sempre, alla fine, cambiamenti fisici nei circuiti.
2. Un linguaggio superiore è un modo più comodo per descrivere istruzioni che verranno tradotte verso il basso.
3. Il linguaggio naturale e le reti neurali rendono l'interazione più vicina alle persone, ma introducono interpretazione e quindi richiedono verifica.
