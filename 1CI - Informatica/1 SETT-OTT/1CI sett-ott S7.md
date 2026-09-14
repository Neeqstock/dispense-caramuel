# SETTIMANA 7: RECUPERARE, SPIEGARE, MIGLIORARE

*Collegamento al quadro operativo: [[1CI - SETT-OTT]]. Prima della verifica, gli studenti richiamano le procedure dalla memoria, migliorano una relazione con feedback concreto e imparano a trattare il Drive come uno spazio di lavoro, non come un cassetto senza etichette.*

```text
SETTIMANA 7
├── TEORIA (55 min)
│   ├── Ripasso attivo: richiamare senza appunti
│   ├── Simulazione test su basi e conversioni
│   └── Errori tipici trasformati in correzioni
├── LABORATORIO (120 min)
│   ├── Peer review della relazione hardware
│   ├── Google Drive: condivisione e permessi
│   └── Backup e organizzazione delle cartelle
└── REGIA DOCENTE
	├── Due versioni della simulazione
	└── Feedback descrittivo, non giudizi generici
```

## MODULO TEORICO (55 minuti)

### 1. Ripassare non significa rileggere
Rileggere gli appunti da una sensazione di familiarita; una verifica chiede invece di recuperare una procedura senza suggerimenti. Il ripasso attivo consiste nel chiudere il quaderno, provare, controllare e correggere.

Questa settimana si riprendono quattro nuclei: bit/byte e $2^N$, multipli di memoria, conversioni decimale-binario, conversioni binario-esadecimale. Ogni esercizio deve mostrare passaggi: una risposta corretta senza procedimento non permette di capire se e stata ragionata o indovinata.

### 2. Simulazione: struttura e metodo
La simulazione contiene quattro esercizi brevi e una domanda di spiegazione:

1. Con 6 bit, quanti stati sono rappresentabili?
2. Convertire $(37)_{10}$ in binario con divisioni successive.
3. Convertire $(101101)_2$ in decimale con i pesi.
4. Convertire $(11001110)_2$ in esadecimale a nibble.
5. Spiegare in due frasi perche un byte ha 256 combinazioni.

Distribuire eventualmente fila A e fila B cambiando i numeri ma mantenendo la stessa difficolta. Il tempo non misura la velocita di calcolo: misura la capacita di applicare un metodo ordinato.

### 3. Correggere gli errori, non solo il risultato
```text
Errore: 25 : 2 -> resti letti dall'alto = 10011
Diagnosi: i resti descrivono prima il bit meno significativo.
Correzione: leggere dal basso verso l'alto = 11001.
```

Altri errori ricorrenti: confondere bit e byte, usare `Giga` come se fosse sempre $1024$, dimenticare uno zero nel gruppo hex e usare pesi al contrario. Durante la correzione chiedere: "Quale regola hai violato?"; questa domanda e piu utile di "Quanto fa?".

### 4. Prepararsi senza trucchi
La procedura minima per ogni conversione e: scrivere base iniziale e finale; usare il metodo richiesto; rileggere verso e zeri; fare un controllo inverso quando possibile. Calcolatrice e ricerca web non sostituiscono il quaderno: durante la prova la risorsa affidabile e il procedimento imparato.

## MODULO LABORATORIO (120 minuti)

### 1. Peer review: un compagno aiuta a vedere meglio
Scambiare il PDF della relazione con un compagno. Chi revisiona non riscrive il lavoro altrui e non assegna un voto: offre due osservazioni specifiche positive e un suggerimento migliorabile. Esempi: "La tabella ha intestazioni chiare" e "Nel sommario manca la sezione Fonti". Non sono utili commenti come "bello" o "brutto".

Checklist del revisore:

- frontespizio, titoli e sommario sono presenti e coerenti;
- CPU, RAM, archiviazione e scheda madre hanno funzioni corrette;
- tabella e immagini sono leggibili e dentro i margini;
- PDF e file hanno un nome riconoscibile;
- il suggerimento e concreto, rispettoso e realizzabile.

### 2. Drive: condividere non significa aprire tutto a tutti
In Google Drive selezionare cartella o file, scegliere **Condividi** e controllare il ruolo assegnato. **Visualizzatore** puo leggere; **Commentatore** puo lasciare note; **Editor** puo modificare e deve essere concesso solo quando serve. Verificare sempre destinatario, ruolo e impostazione del link prima di inviare.

Una cartella condivisa e utile per consegne di gruppo; un documento personale non deve diventare modificabile da chiunque possieda il collegamento. I permessi sono una scelta di responsabilita, non un dettaglio del menu.

### 3. Backup e ordine
Creare nel Drive una struttura essenziale, senza duplicare file a caso:

```text
Informatica_1CI/
├── 01_Appunti/
├── 02_Relazioni/
│   ├── Bozze/
│   └── Consegne_PDF/
├── 03_Esercizi/
└── 99_Backup/
```

Un backup e una copia verificabile in una posizione diversa: non e rinominare il file in `finale_definitivo_vero.docx`. Caricare una copia datata e controllare che si apra. Il nome consigliato e `Cognome_Nome_RelazioneHardware_v1.docx`; la consegna definitiva evita sigle confuse.

### 4. Esercitazione a fasi temporizzate
**Fase A - Scambio guidato (15 min).** Aprire due PDF, assegnare coppie e ripetere le regole del feedback.

**Fase B - Revisione (25 min).** Compilare checklist e scrivere due punti di forza, un miglioramento.

**Fase C - Revisione autore (20 min).** Applicare almeno un miglioramento e annotare quale.

**Fase D - Drive e permessi (25 min).** Creare cartelle, condividere una cartella-test con il docente come visualizzatore e controllare il ruolo.

**Fase E - Backup (20 min).** Caricare la copia datata nella cartella `99_Backup`, aprirla dal cloud e verificare.

**Fase F - Chiusura (15 min).** Rimuovere condivisioni-test non necessarie e ordinare i file della settimana.

## Spunti, domande e riferimenti

### Perche siamo arrivati qui
Il ripasso attivo si basa sul recuperare un'informazione, non solo sul rileggerla: e lo stesso principio con cui una prova chiede di usare un metodo senza suggerimenti. Nei documenti condivisi, ruoli e backup sono nati per rendere possibile la collaborazione senza perdere il controllo su chi modifica e senza affidare l'unica copia a un solo luogo.

### Aneddoto dalla cultura informatica
La regola di backup "3-2-1" e celebre nella comunita informatica: tre copie dei dati, su due tipi di supporto, con una copia in un luogo diverso. Non e una formula magica, ma ricorda che una sincronizzazione cloud puo propagare anche una cancellazione: una copia precedente verificata resta preziosa.

### Domande per ragionare insieme
1. Ripasso: quale differenza pratica c'e tra il ruolo di commentatore e quello di editor in Drive?
2. Applicazione: devi far leggere la tua relazione a un compagno senza permettergli di modificarla. Quale ruolo e quale impostazione del link sceglieresti?
3. Inferenza: perche una cartella condivisa con permesso di editor puo creare un problema anche se tutti i membri sono persone fidate?

### Riferimenti e spunti visivi
- [Formazione su Google Drive](https://support.google.com/a/users/answer/9282958?hl=it): materiali introduttivi per organizzare e usare i file.
- [Condividere file e cartelle in Google Drive](https://support.google.com/drive/answer/2494822?hl=it): ruoli, destinatari e impostazioni dei link.

## GUIDA DI REGIA PER IL DOCENTE

### Cronoprogramma teoria (55 min)
- **00-05:** consegnare la simulazione e ricordare che prima si prova senza appunti.
- **05-20:** lavoro individuale silenzioso; osservare procedimenti, non suggerire risultati.
- **20-38:** correzione partecipata: studenti alla lavagna per un esercizio ciascuno.
- **38-48:** analisi degli errori tipici con un esempio sbagliato.
- **48-55:** autosegnalazione anonima: argomento sicuro e argomento da ripassare.

### Cronoprogramma laboratorio (120 min)
- **00-15:** accordo su regole del feedback e scambio dei PDF.
- **15-40:** peer review con checklist; docente monitora la qualita dei commenti.
- **40-60:** miglioramento individuale della relazione.
- **60-85:** dimostrazione Drive: cartella, condivisione, ruoli, rimozione accesso.
- **85-105:** struttura personale e backup verificato.
- **105-120:** pulizia, controllo dei nomi e domanda di uscita.

### Disegni ASCII da lavagna
```text
CREATORE ---- Editor ------> puo modificare
	 |------ Commentatore -> puo suggerire
	 \----- Visualizzatore -> puo leggere

Provo -> controllo -> individuo l'errore -> correggo -> riprovo
```

### Consolidamento e ponte
Micro-task: preparare sul quaderno una "carta procedura" di quattro righe per una conversione decimale-binario e una binario-esadecimale, senza esempi risolti. A fine settimana lo studente affronta una simulazione con metodo, formula feedback utile e gestisce file, permessi e backup in Drive. La settimana 8 porta alla verifica sommativa e apre il linguaggio visivo delle presentazioni.
