# SETTIMANA 5: L'ESDECIMALE, LA SCORCIATOIA DEI TECNICI

*Collegamento al quadro operativo: [[1CI - SETT-OTT]]. L'esadecimale non sostituisce il binario: lo rende piu compatto e leggibile, dai colori del web agli indirizzi delle schede di rete.*

```text
SETTIMANA 5
├── TEORIA (55 min)
│   ├── Base 16 e cifre da 0 a F
│   ├── Nibble: quattro bit, sedici possibilita
│   ├── Cenno all'ottale: gruppi di tre bit
│   └── RGB e indirizzi MAC
├── LABORATORIO (120 min)
│   ├── Avvio relazione tecnica hardware
│   ├── Frontespizio, stili e sommario automatico
│   └── Componenti e tabella delle grandezze
└── REGIA DOCENTE
		├── Colori reali per rendere concreto #RRGGBB
		└── Prima revisione della relazione
```

## MODULO TEORICO (55 minuti)

### 1. Perche servono sedici simboli
Il binario e perfetto per i circuiti ma una sequenza lunga, come `1111000010100011`, e scomoda da leggere. In base 16 una cifra vale da 0 a 15. Dopo il 9 servono sei simboli aggiuntivi:

```text
decimale:       0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
esadecimale:    0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
```

Quindi `A` non e una parola e non e una variabile: in esadecimale rappresenta il valore dieci. Ad esempio $(2F)_{16}=2\cdot16+15=47_{10}$.

### 2. Il nibble spiega il legame con il binario
Quattro bit producono $2^4=16$ combinazioni. Per questo una cifra esadecimale corrisponde esattamente a un gruppo di quattro bit, chiamato **nibble**. Un byte contiene due nibble.

```text
byte:     1101 0110
nibble:   1101 | 0110
hex:        D  |   6       quindi D6
```

Non e necessario imparare una tabella infinita: bastano i sedici casi da `0000=0` fino a `1111=F`. La conversione diretta sara l'obiettivo della settimana 6.

### 3. Un cenno all'ottale
Il sistema ottale usa otto cifre, da 0 a 7. Poiche $2^3=8$, una cifra ottale corrisponde a tre bit. Oggi l'esadecimale e piu frequente perche quattro bit si collegano bene a byte e nibble, ma l'ottale serve per riconoscere che la base e una scelta di rappresentazione.

### 4. Due esempi fuori dal quaderno
Un colore web come `#FF0000` contiene tre componenti: rosso, verde e blu. `FF` significa 255, il massimo valore di un byte; quindi rosso al massimo, verde e blu a zero producono rosso puro. `#00FF00` e verde, `#0000FF` e blu.

Un indirizzo MAC identifica una scheda di rete a livello hardware ed e spesso scritto in sei coppie esadecimali: `A4:5E:60:1B:2C:90`. Non occorre memorizzarlo: riconoscere le cifre `A-F` e la struttura a coppie e gia una competenza tecnica utile.

## MODULO LABORATORIO (120 minuti)

### 1. Compito autentico: relazione tecnica sull'hardware
Ogni studente avvia una relazione dal titolo **Architettura interna del computer**. Il documento deve descrivere CPU, RAM, SSD o hard disk e scheda madre usando parole proprie, fonti indicate dal docente e immagini pertinenti. Non e una raccolta di frasi copiate: ogni paragrafo deve rispondere alla domanda "che cosa fa questo componente?".

### 2. Struttura obbligatoria
```text
Frontespizio
Sommario automatico
1. Che cos'e un computer
2. Componenti principali
	 2.1 CPU
	 2.2 RAM
	 2.3 Archiviazione
	 2.4 Scheda madre
3. Tabella: componente, funzione, unita di misura
4. Fonti / immagini utilizzate
```

Il frontespizio riporta titolo, studente, classe, disciplina, docente e data. Applicare Titolo 1 e Titolo 2 ai capitoli prima di inserire il sommario: il sommario non si scrive a mano, si genera dal menu Riferimenti o Inserisci.

### 3. Esercitazione a fasi temporizzate
**Fase A - Frontespizio (20 min).** Creare una prima pagina essenziale, centrata ma leggibile; non usare immagini decorative enormi.

**Fase B - Gerarchia (25 min).** Inserire tutti i titoli della struttura e applicare gli stili corretti; verificare dal riquadro di navigazione che la gerarchia sia visibile.

**Fase C - Contenuto tecnico (35 min).** Scrivere almeno due sezioni: CPU e RAM, con una definizione, una funzione e un esempio concreto.

**Fase D - Tabella (25 min).** Inserire quattro righe per CPU, RAM, SSD/HDD, scheda madre; colonne: componente, funzione, esempio di caratteristica, unita.

**Fase E - Sommario e salvataggio (15 min).** Generare il sommario, controllare i titoli, salvare con nome `Cognome_Nome_RelazioneHardware`.

## Spunti, domande e riferimenti

### Perche siamo arrivati qui
L'esadecimale e diventato comune perche una sua cifra raccoglie esattamente quattro bit: rende piu corti i codici binari senza perdere la struttura. Per questo compare sia nei colori RGB, dove ogni coppia va da `00` a `FF`, sia negli indirizzi MAC, scritti in sei coppie per renderli leggibili.

### Aneddoto dalla cultura informatica
Il colore web `#FF00FF` e chiamato spesso *fuchsia* o *magenta* ed e uno dei colori piu riconoscibili dei primi schermi e del web. La notazione `#RRGGBB` non e un codice segreto: sono tre byte scritti in esadecimale, uno per rosso, verde e blu.

### Domande per ragionare insieme
1. Ripasso: quale valore decimale rappresenta `F` in base 16?
2. Applicazione: quale colore prevedi per `#FFFF00`? Motiva guardando le tre coppie RGB.
3. Inferenza: un MAC ha sei coppie esadecimali. Quanti byte contiene e perche puoi dedurlo dai separatori?

### Riferimenti e spunti visivi
- [Valori di colore CSS - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value): esempi dei formati di colore usati sul web.
- [Introduzione agli indirizzi MAC - IEEE](https://standards.ieee.org/products-programs/regauth/tut/mac/): spiegazione dell'identificatore delle interfacce di rete.

## GUIDA DI REGIA PER IL DOCENTE

### Cronoprogramma teoria (55 min)
- **00-08:** mostrare i codici `#FF0000`, `#00FF00`, `#0000FF` e chiedere quale colore prevedono.
- **08-20:** presentare la tabella 0-F; far leggere `A`, `C`, `F` come 10, 12, 15.
- **20-32:** ricavare $2^4=16$ e definire nibble e byte.
- **32-42:** cenno comparativo a ottale e gruppi di tre bit.
- **42-50:** leggere un MAC a coppie e riconoscere le lettere ammesse.
- **50-55:** domanda d'uscita: perche `F` e una cifra valida in base 16 ma non in base 10?

### Cronoprogramma laboratorio (120 min)
- **00-15:** consegna della traccia e creazione del file nella cartella corretta.
- **15-35:** frontespizio; controllo rapido di nome, classe, titolo e data.
- **35-55:** titoli e stili; dimostrazione del sommario automatico.
- **55-90:** scrittura delle due prime componenti, con supporto docente-ITP.
- **90-110:** tabella tecnica e prima revisione della leggibilita.
- **110-120:** salvataggio, caricamento provvisorio o controllo sul Drive.

### Disegni ASCII da lavagna
```text
							4 bit = 1 nibble = 1 cifra hex
0000 0001 0010 ... 1001 1010 ... 1111
 0    1    2        9    A        F

# FF 00 00
	R  G  B       FF = 15*16 + 15 = 255
```

### Consolidamento e ponte
Micro-task: associare `#000000`, `#FFFFFF`, `#FF0000` a nero, bianco e rosso e scrivere un esempio di cifra esadecimale con il suo valore decimale. A fine settimana lo studente riconosce la base 16, spiega nibble e RGB e ha una relazione impostata con stili, sommario e tabella. La settimana 6 chiude il cerchio con conversioni dirette binario-esadecimale e finalizzazione del PDF.
