# SETTIMANA 6: QUATTRO BIT ALLA VOLTA

*Collegamento al quadro operativo: [[1CI - SETT-OTT]]. La relazione tecnica entra nella fase professionale di revisione e consegna, mentre la teoria rende rapida la traduzione tra binario ed esadecimale.*

```text
SETTIMANA 6
├── TEORIA (55 min)
│   ├── Binario -> esadecimale: gruppi di quattro da destra
│   ├── Esadecimale -> binario: espandere ogni cifra
│   └── Zeri iniziali e controllo del risultato
├── LABORATORIO (120 min)
│   ├── Revisione contenuto e impaginazione
│   ├── Numeri pagina, PDF e consegna
│   └── Griglia valutativa esplicita
└── REGIA DOCENTE
	├── Verificare prima il file sorgente, poi il PDF
	└── Preparare la peer review della settimana 7
```

## MODULO TEORICO (55 minuti)

### 1. Da binario a esadecimale: separare, tradurre, ricomporre
Si raggruppano i bit in blocchi di quattro **partendo da destra**, perche a destra c'e il bit meno significativo. Se il primo gruppo e incompleto si aggiungono zeri a sinistra: il valore non cambia.

```text
11010110  ->  1101 | 0110  ->  D | 6  ->  (D6)16
101101     ->  0010 | 1101  ->  2 | D  ->  (2D)16
```

Nel secondo esempio gli zeri aggiunti non sono "barare": `00101101` e lo stesso numero di `101101`, proprio come `025` e `25` rappresentano lo stesso valore decimale.

### 2. Da esadecimale a binario: ogni cifra esplode in quattro bit
Il percorso inverso e meccanico: sostituire ogni cifra hex con la sua forma a quattro bit, senza saltare gli zeri.

```text
(3A)16 -> 3 = 0011, A = 1010 -> (00111010)2
(F0)16 -> F = 1111, 0 = 0000 -> (11110000)2
```

Scrivere `3A -> 111010` sarebbe scorretto come rappresentazione a nibble: manca uno zero nel gruppo del 3. Il numero puo avere lo stesso valore, ma si perde la corrispondenza uno-a-uno con le cifre esadecimali.

### 3. La mini-tabella indispensabile
```text
0=0000  1=0001  2=0010  3=0011  4=0100  5=0101  6=0110  7=0111
8=1000  9=1001  A=1010  B=1011  C=1100  D=1101  E=1110  F=1111
```
La tabella e uno strumento, non un test di memoria pura. L'obiettivo e saper scegliere il gruppo corretto, mantenere l'ordine e controllare il risultato.

### 4. Controllo incrociato
Per verificare `D6`, possiamo fare un controllo in decimale: $D\cdot16+6=13\cdot16+6=214$. Anche `11010110` vale $128+64+16+4+2=214$. Due strade diverse che arrivano allo stesso risultato sono un ottimo segnale.

## MODULO LABORATORIO (120 minuti)

### 1. Revisione della relazione: prima il contenuto
Aprire la relazione hardware e usare questa lista prima di curare l'aspetto:

- CPU, RAM, archiviazione e scheda madre sono descritti con una funzione corretta;
- i titoli seguono una gerarchia di stili, senza salti casuali;
- la tabella ha intestazioni chiare e non supera il margine;
- immagini e testo hanno fonte o didascalia quando necessario;
- il sommario si aggiorna dopo le modifiche.

### 2. Numeri di pagina e PDF
Inserire il numero pagina nel piè di pagina. Il frontespizio resta senza numero visibile: usare "prima pagina diversa" oppure una sezione separata secondo il programma disponibile. Aggiornare il sommario, poi esportare in PDF. Il PDF conserva il layout e riduce il rischio che un font o una versione diversa del programma sposti tutto.

Procedura: **File -> Esporta / Salva con nome -> PDF**, controllare cartella e nome, aprire il PDF appena creato e sfogliare almeno frontespizio, sommario, tabella e ultima pagina.

### 3. Esercitazione a fasi temporizzate
**Fase A - Conversioni lampo (15 min).** Completare cinque conversioni su scheda: `1010`, `11110000`, `2D`, `A4`, `101101`.

**Fase B - Revisione contenuto (25 min).** Correggere termini imprecisi e rendere ogni paragrafo leggibile a un compagno.

**Fase C - Impaginazione (25 min).** Aggiornare stili, sommario, immagini, tabella e inserire i numeri di pagina.

**Fase D - Esportazione controllata (20 min).** Creare il PDF e confrontarlo con il file modificabile in quattro punti.

**Fase E - Consegna (20 min).** Caricare sia il file sorgente sia il PDF solo se richiesto; nominare i file in modo uniforme e verificare il caricamento.

**Fase F - Autovalutazione (15 min).** Compilare la griglia e indicare una modifica concreta fatta dopo la revisione.

### 4. Griglia valutativa della relazione (10 punti)
| Criterio | Punti | Evidenze |
|---|---:|---|
| Struttura, frontespizio, stili e sommario | 3 | gerarchia riconoscibile e completa |
| Correttezza delle nozioni hardware | 3 | funzioni di componenti spiegate bene |
| Tabella, immagini e leggibilita | 2 | elementi ordinati e pertinenti |
| PDF, nome file, puntualita e consegna | 2 | file richiesti corretti e presenti |

## Spunti, domande e riferimenti

### Perche siamo arrivati qui
Raggruppare quattro bit in un nibble permette di passare dal binario all'esadecimale senza rifare ogni volta tutti i calcoli in decimale. Allo stesso modo, esportare in PDF separa il contenuto dal programma con cui e stato scritto: chi riceve il file puo vederne un layout molto piu stabile.

```text
codice:   1101 0110  ->  D6
documento: sorgente  ->  PDF da controllare
```

### Aneddoto dalla cultura informatica
Il PDF fu creato da Adobe nei primi anni 1990 per far apparire un documento nello stesso modo su computer diversi. Da allora l'espressione "ma sul mio computer si vede bene" e diventata quasi una battuta ricorrente: aprire il PDF appena esportato e la risposta tecnica piu semplice.

### Domande per ragionare insieme
1. Ripasso: converti `101101` in esadecimale, mostrando gli zeri aggiunti a sinistra.
2. Applicazione: quali quattro punti controlleresti confrontando il file sorgente con il PDF della relazione?
3. Inferenza: perche lo zero iniziale e importante in `0011` quando rappresenta la cifra hex `3`, anche se il valore numerico resta uguale a `11`?

### Riferimenti e spunti visivi
- [Numeri binari - Khan Academy in italiano](https://it.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/a/binary-numbers): richiamo visuale della base 2 e delle posizioni.
- [Valori di colore CSS - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value): esempi concreti di coppie esadecimali nei colori digitali.

## GUIDA DI REGIA PER IL DOCENTE

### Cronoprogramma teoria (55 min)
- **00-10:** richiamo di nibble e tabella 0-F con due domande orali.
- **10-22:** conversione guidata `11010110 -> D6`.
- **22-32:** esempio con gruppo incompleto e zeri iniziali.
- **32-42:** conversione `3A -> 00111010` e discussione dello zero mancante.
- **42-50:** due esercizi a coppie e controllo incrociato in decimale.
- **50-55:** ticket: convertire `B7` in binario.

### Cronoprogramma laboratorio (120 min)
- **00-15:** conversioni lampo e apertura relazione.
- **15-40:** revisione di contenuto con checklist proiettata.
- **40-65:** stili, sommario, numeri pagina e tabella.
- **65-85:** esportazione PDF e controllo visivo del file prodotto.
- **85-105:** consegna assistita e risoluzione dei problemi di caricamento.
- **105-120:** autovalutazione con griglia e chiusura ordinata.

### Disegni ASCII da lavagna
```text
da destra:  101101 -> 0010 | 1101 -> 2D
						^ zeri aggiunti, valore invariato

hex:        B        7
bin:      1011     0111
		  \__________/  -> 10110111
```

### Consolidamento e ponte
Micro-task: convertire `7C` in binario e `11101001` in esadecimale, indicando i gruppi. A fine settimana lo studente converte per nibble, controlla un documento professionale, esporta un PDF e comprende la griglia di valutazione. La settimana 7 usera i risultati per un ripasso attivo e una peer review ragionata.
