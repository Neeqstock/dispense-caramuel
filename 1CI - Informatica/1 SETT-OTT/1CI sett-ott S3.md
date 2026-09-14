# SETTIMANA 3: IL LINGUAGGIO DEGLI INTERRUTTORI

*Collegamento al quadro operativo: [[1CI - SETT-OTT]]. Questa settimana apre il modulo sui sistemi di numerazione e trasforma una domanda concreta - "quanto spazio occupa?" - in un modo per capire come ragiona un computer.*

```text
SETTIMANA 3
├── TEORIA (55 min)
│   ├── Bit: due stati, non due numeri misteriosi
│   ├── Byte e stati rappresentabili: 2^N
│   ├── Potenze di due e capacita di memoria
│   └── KB, MB, GB, TB: decimale e binario
├── LABORATORIO (120 min)
│   ├── Pagina, margini e digitazione professionale
│   ├── Stili: Titolo 1, Titolo 2, Corpo testo
│   └── Scheda "Bit e Byte" ordinata e salvata
└── REGIA DOCENTE
		├── Lavagna: stati di N bit e scala delle capacita
		└── Micro-task: leggere una memoria senza confondere le unita
```

## MODULO TEORICO (55 minuti)

### 1. Un computer non vede numeri: riconosce stati
Un transistor e un piccolo interruttore elettronico. In modo molto semplificato puo essere in due condizioni affidabili: passa corrente oppure non passa corrente. Per convenzione le indichiamo con `1` e `0`.

Un **bit** (*binary digit*) e quindi la piu piccola unita di informazione: puo assumere soltanto due stati. Non e ancora una lettera, una foto o un voto: e un posto in cui scegliere tra due possibilita.

```text
Interruttore spento       Interruttore acceso
				0                         1
	nessuna tensione            tensione rilevata
```

La domanda utile non e "quanto vale un bit?", ma: **quante combinazioni posso formare con piu bit?** Ogni nuovo bit raddoppia le possibilita.

### 2. Da un bit al byte: la regola del raddoppio
Con $N$ bit gli stati rappresentabili sono $2^N$.

| Bit disponibili | Calcolo | Stati possibili | Esempio di codici |
|---:|---:|---:|---|
| 1 | $2^1$ | 2 | `0`, `1` |
| 2 | $2^2$ | 4 | `00`, `01`, `10`, `11` |
| 3 | $2^3$ | 8 | da `000` a `111` |
| 4 | $2^4$ | 16 | da `0000` a `1111` |
| 8 | $2^8$ | 256 | da `00000000` a `11111111` |

Otto bit formano un **byte**. Poiche un byte ha 256 configurazioni, puo codificare un valore intero da $0$ a $255$: sono 256 valori, perche si conta anche lo zero.

Esempio: con due bit non possiamo inventare un quinto stato. Le combinazioni sono gia tutte qui: `00`, `01`, `10`, `11`. Questa finitezza e importante: anche testi, immagini e musica devono essere tradotti in gruppi limitati di bit.

### 3. Le potenze del due sono una scala
Memorizzare almeno questa sequenza evita molti errori nelle conversioni future:

```text
2^0=1   2^1=2   2^2=4   2^3=8   2^4=16   2^5=32
2^6=64  2^7=128 2^8=256 2^9=512 2^10=1024
```

Un byte non e "otto caratteri": puo contenere un carattere semplice oppure una piccola parte di un carattere, di un colore o di un'istruzione. L'unita misura spazio disponibile, non il significato umano del contenuto.

### 4. KB o KiB? Due convenzioni da riconoscere
I produttori di dischi usano di solito la scala decimale: $1\,\text{kB}=1000\,\text{B}$. I sistemi informatici hanno storicamente usato gruppi di potenze di due: $1\,\text{KiB}=2^{10}\,\text{B}=1024\,\text{B}$.

| Prefisso commerciale | Valore decimale | Prefisso binario | Valore binario |
|---|---:|---|---:|
| kB | $10^3$ B | KiB | $2^{10}$ B |
| MB | $10^6$ B | MiB | $2^{20}$ B |
| GB | $10^9$ B | GiB | $2^{30}$ B |
| TB | $10^{12}$ B | TiB | $2^{40}$ B |

Per questo un disco dichiarato da `500 GB` puo apparire con una capacita numerica piu bassa nel sistema operativo: non sono spariti file, sono cambiate le unita usate per visualizzarli.

## MODULO LABORATORIO (120 minuti)

### 1. Preparare un documento prima di scrivere
Aprire Word o LibreOffice Writer e creare `Cognome_Nome_BitByte.docx` oppure `.odt`. Impostare formato A4, margini di circa 2,5 cm, orientamento verticale e interlinea 1,15. Salvare subito nella cartella personale di Informatica: salvare e una parte del lavoro.

### 2. Usare gli stili, non il font "a caso"
Applicare **Titolo** al titolo principale, **Titolo 1** a `Bit e byte`, `Potenze di due`, `Multipli della memoria`, e **Corpo testo** ai paragrafi. Gli stili producono una gerarchia leggibile e, piu avanti, permetteranno di creare un sommario automatico.

Regole di digitazione da applicare mentre si lavora:

- lo spazio viene dopo virgola, punto e due punti, mai prima;
- una sola spaziatura tra le parole; non usare spazi per allineare;
- `Shift` serve per una maiuscola singola; `Caps Lock` non e una decorazione;
- `Invio` chiude un paragrafo; per cambiare aspetto si usano gli stili.

### 3. Esercitazione: la scheda "Bit e Byte"

**Fase A - Avvio (15 min).** Creare il titolo, intestare nome, classe e data; applicare gli stili richiesti.

**Fase B - Tabella delle potenze (30 min).** Inserire una tabella con le potenze da $2^0$ a $2^{10}$, il risultato e una breve nota per `2^8` e `2^10`.

**Fase C - Spiegazione (35 min).** Scrivere tre brevi paragrafi: che cos'e un bit, perche 8 bit formano un byte, differenza tra `GB` e `GiB`. Inserire l'esempio $2^8=256$ con l'editor formule o in forma testuale corretta.

**Fase D - Controllo e consegna (25 min).** Correggere con il controllo ortografico, verificare che i titoli siano stili e non testo ingrandito, salvare e caricare il file dove indicato dal docente.

**Fase E - Uscita (15 min).** Rispondere in fondo al documento: "Con 5 bit quanti stati posso rappresentare?" e "Perche 1 KiB non coincide esattamente con 1000 B?".

## Spunti, domande e riferimenti

### Perche siamo arrivati qui
I prefissi `kilo`, `mega` e `giga` esistevano gia nelle misure decimali. Con le memorie elettroniche, pero, le capacita crescevano naturalmente per potenze di due: $2^{10}=1024$ era vicino a 1000. Per evitare ambiguita, gli standard hanno distinto `kB` da `KiB`, `MB` da `MiB` e cosi via.

### Aneddoto dalla cultura informatica
Negli anni 1990 molte discussioni tra tecnici riguardavano proprio il significato di "megabyte". La soluzione non fu cambiare i computer, ma introdurre i prefissi binari `kibi`, `mebi` e `gibi`: nomi insoliti, ma utili quando una capacita deve essere comunicata senza equivoci.

### Domande per ragionare insieme
1. Ripasso: con 7 bit, quanti stati diversi possiamo rappresentare?
2. Applicazione: un dispositivo dichiara `64 GB`; quale unita controlleresti nelle impostazioni per capire perche il valore visualizzato puo essere diverso?
3. Inferenza: se ogni bit aggiunto raddoppia gli stati, di quanti bit servirebbe aumentare una memoria per ottenere otto volte gli stati? Come lo deduci?

### Riferimenti e spunti visivi
- [Prefissi del Sistema Internazionale - BIPM](https://www.bipm.org/en/measurement-units/si-prefixes): per confrontare la scala decimale usata nelle misure.
- [Prefissi binari - NIST](https://physics.nist.gov/cuu/Units/binary.html): tabella affidabile da `KiB` a `YiB`.

## GUIDA DI REGIA PER IL DOCENTE

### Cronoprogramma teoria (55 min)
- **00-05:** mostrare una chiavetta e chiedere che cosa significhi `32 GB`.
- **05-15:** introdurre il transistor-interruttore e far votare alla classe uno stato `0` o `1`.
- **15-30:** costruire insieme la tabella da 1 a 4 bit; far pronunciare il raddoppio.
- **30-42:** definire byte e svolgere $2^8=256$; chiarire intervallo `0-255`.
- **42-50:** confrontare GB e GiB con un esempio di disco.
- **50-55:** ticket d'uscita: calcolare $2^6$ e spiegare un byte con una frase.

### Cronoprogramma laboratorio (120 min)
- **00-15:** accesso, cartella corretta, salvataggio iniziale e impostazione pagina.
- **15-35:** dimostrazione guidata degli stili; docente e ITP controllano due file campione.
- **35-70:** tabella potenze e formule; fermata tecnica dopo 20 minuti.
- **70-100:** paragrafi e revisione a coppie della leggibilita.
- **100-115:** controllo finale, salvataggio ed eventuale caricamento.
- **115-120:** domanda di uscita e chiusura delle postazioni.

### Disegni ASCII da lavagna
```text
N bit:       1       2        3          4
stati:       2  ->   4   ->   8    ->   16
						 2^1      2^2      2^3       2^4

bit:  [0] [1] [0] [1] [1] [0] [0] [1]
			 \____________ BYTE ____________/
```

### Consolidamento e ponte
Micro-task: fotografare o annotare tre capacita reali (telefono, chiavetta, disco/cloud), indicare l'unita e ordinarle dalla piu piccola alla piu grande. A fine settimana lo studente sa definire bit e byte, calcolare $2^N$ per piccoli valori, distinguere i prefissi e produrre un documento con pagina e stili coerenti. La settimana 4 usa proprio le potenze di due per convertire numeri tra decimale e binario.
