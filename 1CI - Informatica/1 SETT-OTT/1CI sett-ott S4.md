# SETTIMANA 4: CONTARE CON I PESI DEL BINARIO

*Collegamento al quadro operativo: [[1CI - SETT-OTT]]. Dopo bit e potenze di due, il binario diventa una tecnica concreta: leggere un codice e costruirne uno senza indovinare.*

```text
SETTIMANA 4
├── TEORIA (55 min)
│   ├── Notazione posizionale in base 10 e in base 2
│   ├── Binario -> decimale: somma dei pesi
│   └── Decimale -> binario: divisioni successive per 2
├── LABORATORIO (120 min)
│   ├── Tabelle, immagini, layout e formule
│   └── Scheda con conversioni commentate
└── REGIA DOCENTE
	├── Correggere il verso dei resti
	└── Preparare il ponte verso l'esadecimale
```

## MODULO TEORICO (55 minuti)

### 1. Il valore di una cifra dipende dalla posizione
Nel sistema decimale usiamo dieci simboli, da 0 a 9. In `345`, il `3` non vale tre unita: vale tre centinaia. In formula:

$$345_{10}=3\cdot10^2+4\cdot10^1+5\cdot10^0$$

Il binario usa solo `0` e `1`, ma segue la stessa idea. Cambia la base: le colonne pesano $1,2,4,8,16,\ldots$ invece di $1,10,100,1000,\ldots$.

```text
Binario:       1   1   0   1
Peso:          8   4   2   1
Contributo:     8 + 4 + 0 + 1 = 13
Quindi: (1101)2 = (13)10
```

Il pedice indica la base ed evita equivoci: `10` puo significare dieci in base 10 oppure due in base 2.

### 2. Da binario a decimale: metodo dei pesi
Per convertire $(101101)_2$, scrivere le potenze di due sotto ogni cifra, da destra verso sinistra, e sommare soltanto i pesi sotto gli `1`:

$$1\cdot2^5+0\cdot2^4+1\cdot2^3+1\cdot2^2+0\cdot2^1+1\cdot2^0=32+8+4+1=45$$

Gli zeri sono importanti: non aggiungono valore, ma mantengono le posizioni corrette. Un errore comune e leggere `101101` come "centounomilacentouno": va letto come una scelta di pesi.

### 3. Da decimale a binario: divisioni successive
Per convertire $45_{10}$, dividere per 2 fino a ottenere quoziente 0. Si registrano i resti e si legge **dal basso verso l'alto**.

```text
45 : 2 = 22 resto 1
22 : 2 = 11 resto 0
11 : 2 =  5 resto 1
 5 : 2 =  2 resto 1
 2 : 2 =  1 resto 0
 1 : 2 =  0 resto 1

resti dal basso verso l'alto: 101101
quindi (45)10 = (101101)2
```

Il controllo migliore e tornare indietro con il metodo dei pesi: se si ottiene ancora 45, il procedimento e coerente.

### 4. Strategia e errori utili
Prima di fare i conti, cercare la potenza di due piu grande che non supera il numero. Per $25$, la prima e $16$: rimangono 9, poi 8, poi 1. Otteniamo `11001`. Questa strategia e una verifica mentale delle divisioni.

Errori da rendere visibili: leggere i resti dall'alto, dimenticare gli zeri interni, assegnare il peso 1 a sinistra anziche a destra. Un errore scritto e un dato: va localizzato, non cancellato in silenzio.

## MODULO LABORATORIO (120 minuti)

### 1. Quattro strumenti per una scheda leggibile
La consegna e una pagina intitolata **Conversioni commentate**. Useremo:

- una **tabella** per allineare divisioni, quozienti e resti;
- una **immagine** piccola e pertinente, ad esempio una foto di un circuito o un QR del materiale fornito, impostata "in linea con il testo";
- un **layout** con titoli e spazio bianco: non tutto deve stare attaccato;
- l'editor **formula** per un calcolo con potenze, quando disponibile.

### 2. Procedura pratica
1. Creare `Cognome_Nome_Conversioni.docx` nella cartella `02_Relazioni_Laboratorio` o nella posizione indicata.
2. Impostare Titolo, Titolo 1 e Corpo testo usando gli stili gia sperimentati.
3. Inserire una tabella a tre colonne: `divisione`, `quoziente`, `resto`; usare bordi semplici e intestazione evidenziata con sobrietà.
4. Inserire un esempio binario-decimale con la riga dei pesi e un esempio decimale-binario con le divisioni.
5. Aggiungere un'immagine fornita dal docente con didascalia: "Il computer usa circuiti a due stati affidabili".
6. Controllare che l'immagine non copra il testo e che la tabella non esca dai margini.

### 3. Esercitazione a fasi temporizzate
**Fase A - Modello (15 min).** Ricostruire insieme il documento-prototipo e salvare.

**Fase B - Conversioni guidate (25 min).** Svolgere $(13)_{10}$ e $(11010)_2$ con il docente; commentare una scelta di peso e il verso di lettura dei resti.

**Fase C - Lavoro individuale (35 min).** Completare quattro conversioni: $25_{10}$, $42_{10}$, $(100111)_2$, $(111111)_2$.

**Fase D - Qualita del documento (25 min).** Inserire immagine, didascalia e almeno una formula; revisione a coppie con tre controlli: titoli, tabelle, passaggi leggibili.

**Fase E - Correzione e consegna (20 min).** Correggere un esercizio alla lavagna, salvare, esportare se richiesto e consegnare.

## Spunti, domande e riferimenti

### Perche siamo arrivati qui
La notazione posizionale e nata per rendere i calcoli piu pratici: una cifra cambia valore secondo la colonna in cui si trova. Il sistema binario applica la stessa idea alla base 2, adatta a circuiti che distinguono in modo affidabile due stati. Le conversioni servono quindi a leggere lo stesso valore con due alfabeti diversi.

### Aneddoto dalla cultura informatica
Il termine inglese *bug* esisteva prima dei computer, ma nel 1947 il team dell'Harvard Mark II trovo una falena in un rele e la incollò nel registro di bordo. Il caso rese celebre l'idea di "debugging": controllare con metodo dove un procedimento o una macchina smette di fare cio che dovrebbe.

### Domande per ragionare insieme
1. Ripasso: quale valore decimale rappresenta $(10110)_2$ usando la riga dei pesi?
2. Applicazione: converti $(26)_{10}$ in binario e verifica il risultato tornando ai pesi.
3. Inferenza: perche aggiungere uno zero a sinistra di un numero binario non ne cambia il valore, mentre aggiungerlo a destra lo cambia?

### Riferimenti e spunti visivi
- [Numeri binari - Khan Academy in italiano](https://it.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/a/binary-numbers): spiegazione visuale di base 2 e pesi.
- [CS Unplugged in italiano](https://www.csunplugged.org/it/): attivita senza computer, utili per vedere il binario con carte e movimenti.

## GUIDA DI REGIA PER IL DOCENTE

### Cronoprogramma teoria (55 min)
- **00-08:** scrivere `345` e chiedere quanto vale il `4`; trasferire l'idea al binario.
- **08-20:** costruire la riga dei pesi da 32 a 1 e convertire `1101` insieme.
- **20-35:** modellare le divisioni successive di 25, insistendo sul basso verso l'alto.
- **35-45:** far svolgere un numero pari e uno dispari sul quaderno.
- **45-52:** confronto a coppie e correzione di un errore volutamente preparato.
- **52-55:** exit ticket: $(10110)_2=?_{10}$.

### Cronoprogramma laboratorio (120 min)
- **00-15:** apertura file e richiamo di stili, margini e salvataggio.
- **15-35:** tabella delle divisioni e primo esempio guidato.
- **35-70:** quattro conversioni individuali; docente e ITP dividono le file.
- **70-90:** immagini, didascalie, formule e layout.
- **90-110:** revisione incrociata e correzione dei passaggi mancanti.
- **110-120:** consegna e verifica rapida delle cartelle.

### Disegni ASCII da lavagna
```text
		 32  16   8   4   2   1
(101101)2  1   0   1   1   0   1
		   32+ 0 + 8 + 4 + 0 + 1 = 45

45 -> /2 -> resti: 1,0,1,1,0,1
					 leggi questo verso: <---
```

### Consolidamento e ponte
Micro-task: svolgere $18_{10}$ e $(100100)_2$ su quaderno, cerchiando il controllo inverso. A fine settimana lo studente usa correttamente i pesi e le divisioni, sa spiegare un passaggio e produce una scheda impaginata con tabelle e formule. La settimana 5 introduce l'esadecimale: una scorciatoia visiva costruita su gruppi di quattro bit.
