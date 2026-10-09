# 🧩 Von Neumann, CPU e registri: come pensa una macchina digitale

> Prima di studiare i dettagli di una CPU, serve una mappa: dove stanno il programma e i dati? Chi esegue le istruzioni? Dove vengono tenuti i numeri mentre vengono elaborati?

Questa dispensa è un'introduzione. Non pretende di descrivere ogni dettaglio di una CPU moderna: costruisce il modello mentale che useremo per capire memoria, bus, ciclo macchina e registri.

---

## 1. Il problema: come facciamo a costruire una macchina programmabile?

Immaginiamo due macchine:

- una calcolatrice costruita per fare soltanto somme;
- una macchina che oggi calcola una media, domani riproduce un'immagine e dopodomani gestisce una rete.

La seconda non deve essere ricostruita ogni volta. Deve poter cambiare **istruzioni** senza cambiare tutto l'hardware.

L'idea decisiva è questa:

> **Il programma può essere rappresentato come dati e conservato nella memoria, insieme ai dati su cui deve lavorare.**

Se il programma è in memoria, la macchina può leggerlo, eseguire un'istruzione, passare alla successiva e cambiare comportamento semplicemente caricando un programma diverso.

### Prima e dopo

```text
+------------------------------+
| MACCHINA SPECIALIZZATA       |
| circuiti costruiti per       |
| una sola funzione            |
+------------------------------+
              |
              | cambiare funzione = modificare la macchina
              v
+------------------------------+
| MACCHINA PROGRAMMABILE       |
| stesso hardware              |
| programmi diversi in memoria |
+------------------------------+
```

Questa è una delle idee alla base dell'architettura chiamata **von Neumann**, dal nome del matematico John von Neumann, che contribuì a formalizzarla nel contesto dei primi calcolatori elettronici del dopoguerra.

Non significa che von Neumann abbia inventato da solo tutto il computer moderno. Il modello raccoglie idee sviluppate da più persone e progetti, tra cui il lavoro di progettisti, matematici, ingegneri e programmatrici. È diventato un modo utile per descrivere come organizzare un calcolatore a programma memorizzato.

> 🕰️ **Aneddoto (con tanto di polemica vera):** il documento che rese celebre questo modello, il *First Draft of a Report on the EDVAC* (1945), circolò a lungo con la sola firma di von Neumann. Il problema è che gran parte di quelle idee erano state elaborate insieme a **J. Presper Eckert** e **John Mauchly**, gli ingegneri che avevano già costruito l'ENIAC. La bozza, pensata come appunto di lavoro interno, finì distribuita pubblicamente prima che Eckert e Mauchly potessero brevettare le loro soluzioni: ne nacque una disputa, anche legale, su chi avesse davvero "inventato" il calcolatore a programma memorizzato. Anche la storia dell'informatica è fatta di persone, ambizioni e battaglie per il credito, non solo di idee pulite calate dall'alto.

---

## 2. La macchina di von Neumann in cinque blocchi

A livello introduttivo possiamo rappresentare il computer con cinque elementi:

```text
                         +----------------+
                         |    MEMORIA     |
                         | programmi      |
                         | dati           |
                         +--------+-------+
                                  ^
                                  | dati e istruzioni
                                  v
+-------------+     +------------+-------------+     +-------------+
| INPUT       | --> |            CPU            | --> | OUTPUT      |
| tastiera    |     | controllo + elaborazione |     | schermo     |
| mouse       |     +------------+-------------+     | stampante   |
| sensori     |                  ^                  | altoparlante|
+-------------+                  |                  +-------------+
                                  |
                            +-----+-----+
                            |    BUS    |
                            | collegano |
                            | i blocchi |
                            +-----------+
```

### I blocchi, in parole semplici

| Blocco | Che cosa fa | Esempio |
| --- | --- | --- |
| **Memoria** | conserva programmi e dati | RAM |
| **CPU** | interpreta ed esegue le istruzioni | processore |
| **Input** | porta informazioni dentro il computer | tastiera, microfono, sensore |
| **Output** | porta risultati verso l'esterno | monitor, stampante, casse |
| **Bus** | trasporta dati, indirizzi e segnali | collegamenti elettrici/logici |

Questa tabella è una mappa funzionale. Nella realtà esistono molti altri componenti, livelli e collegamenti, ma questi cinque blocchi aiutano a non perdersi.

### Un esempio quotidiano

Quando digitiamo la lettera `A`:

1. la tastiera rileva la pressione del tasto (**input**);
2. il computer rappresenta quel carattere con un codice;
3. la CPU esegue le istruzioni necessarie;
4. il dato passa attraverso i collegamenti del sistema (**bus**);
5. il programma e i dati usati si trovano in memoria;
6. il carattere appare sullo schermo (**output**).

La CPU non “vede” la lettera A come la vede una persona. Lavora con rappresentazioni binarie e istruzioni codificate.

---

## 3. La memoria contiene sia istruzioni sia dati

Questa è la caratteristica da ricordare meglio:

```text
+--------------------------------------------------+
| MEMORIA                                          |
|                                                  |
| istruzione 1: carica un valore                   |
| istruzione 2: somma                              |
| dato: 7                                          |
| dato: 5                                          |
| istruzione 3: salva il risultato                  |
+--------------------------------------------------+
```

Per la macchina, istruzioni e dati sono sequenze di bit. È il contesto e il modo in cui vengono lette a dare loro un significato diverso.

Una sequenza può essere interpretata come:

- un numero;
- un carattere;
- un'immagine;
- un'istruzione per la CPU.

Per questo il computer ha bisogno di sapere **dove** si trova ogni informazione e **come** deve interpretarla.

### Un equivoco comune

Dire “la memoria contiene il programma” non significa che la CPU legga tutto il programma in una volta. Normalmente procede per passi:

```text
   memoria: [istruzione 1] [istruzione 2] [istruzione 3] [ ... ]
                ^
                |
             la CPU legge la prossima istruzione
```

Il registro che indica dove cercare la prossima istruzione è il **Program Counter**, abbreviato **PC**.

---

## 4. La CPU: non è un blocco magico

La CPU, o **Central Processing Unit**, è il componente che esegue le istruzioni del programma. Nel modello introduttivo possiamo dividerla in tre grandi parti:

```text
                    CPU
+------------------------------------------------+
|                                                |
|  +----------------+       +----------------+  |
|  | CONTROL UNIT   |       | REGISTRI       |  |
|  | CU             |<----->| piccoli        |  |
|  | coordina       |       | contenitori    |  |
|  +--------+-------+       +--------+-------+  |
|           |                         |          |
|           | segnali                 | dati     |
|           v                         v          |
|                 +----------------+             |
|                 | ALU            |             |
|                 | calcola e      |             |
|                 | confronta      |             |
|                 +----------------+             |
|                                                |
+------------------------------------------------+
```

### 4.1 Control Unit: organizza

La **Control Unit**, o **CU**, coordina l'esecuzione:

- legge la prossima istruzione;
- la interpreta;
- decide quali circuiti attivare;
- stabilisce in quale ordine eseguire i passaggi;
- coordina letture e scritture.

La CU non è una persona e non “pensa” come noi. È un insieme di circuiti progettati per produrre segnali di controllo.

### 4.2 ALU: esegue operazioni

L'**ALU**, cioè *Arithmetic Logic Unit*, esegue operazioni aritmetiche e logiche:

- somma e sottrazione;
- confronti;
- AND, OR, XOR e altre operazioni logiche;
- spostamenti di bit.

La ALU non decide da sola quale operazione fare. Riceve dati e segnali dalla parte di controllo.

```text
   dato A --------\
                   >---- ALU ----> risultato
   dato B --------/       ^
                          |
                   segnale: ADD
```

### 4.3 Registri: tengono a portata di mano

I **registri** sono piccolissime memorie interne alla CPU. Contengono temporaneamente:

- dati su cui lavorare;
- istruzioni;
- indirizzi di memoria;
- risultati intermedi;
- informazioni sullo stato dell'elaborazione.

Sono molto veloci, ma pochi e di capacità limitata. Non sono “la RAM in piccolo”: hanno uno scopo più immediato e si trovano dentro la CPU.

---

## 5. I registri con una metafora

Immaginiamo un banco da lavoro.

```text
+------------------------------------------------+
| BANCO DI LAVORO DEL TECNICO                    |
|                                                |
| [PC]  prossima pagina da consultare            |
| [IR]  istruzione aperta davanti a me          |
| [R1]  primo valore                             |
| [R2]  secondo valore                           |
| [ACC] risultato temporaneo                     |
| [FLAG] piccoli segnali sul risultato           |
+------------------------------------------------+
```

La RAM è come un archivio più grande nella stanza: contiene molte cose, ma per usare un oggetto bisogna prenderlo e portarlo sul banco. I registri sono il banco: poco spazio, accesso rapidissimo.

```text
   grande capacità                                  grande velocità
   <-------------------------------------------------------->
   SSD/HDD       RAM              cache       REGISTRI
   archivio      tavolo           cassetto    banco della CPU
```

La gerarchia è più complessa di questa immagine, ma l'idea è corretta: più una memoria è vicina alla CPU e veloce, più tende a essere piccola e costosa per bit.

---

## 6. I registri principali

I nomi precisi cambiano a seconda dell'architettura del processore. Questi sono ruoli tipici che useremo per ragionare.

### Program Counter: PC

Il **PC** contiene l'indirizzo della prossima istruzione da leggere.

```text
   PC = 1200
   significa: la prossima istruzione si trova all'indirizzo 1200
```

Dopo aver letto l'istruzione, il PC viene normalmente aggiornato per puntare alla successiva. Un salto, una chiamata o una condizione possono cambiare il suo valore.

### Instruction Register: IR

L'**IR** contiene l'istruzione che la CPU sta esaminando o eseguendo in quel momento.

```text
   memoria: [LOAD] [ADD] [STORE]
                       ^
                       |
                      IR
```

Il PC dice **dove cercare dopo**; l'IR contiene **che cosa si sta esaminando ora**.

### Memory Address Register: MAR

Il **MAR** contiene l'indirizzo della cella di memoria con cui la CPU vuole comunicare.

```text
   MAR = 2400
   significa: voglio leggere o scrivere la memoria all'indirizzo 2400
```

Il MAR trasporta un indirizzo, non il contenuto della cella.

### Memory Data Register: MDR

Il **MDR** contiene temporaneamente il dato trasferito fra CPU e memoria.

```text
   MAR = 2400       quale cella?
   MDR = 00000101   quale contenuto?
```

Una coppia utile da ricordare:

- **MAR = dove**;
- **MDR = che cosa**.

### Registri generali

I registri generali, indicati per esempio come `R1`, `R2`, `R3` oppure `X0`, `X1`, contengono operandi e risultati temporanei.

```text
   R1 = 7
   R2 = 5
   ALU: R1 + R2
   R3 = 12
```

### Registro di stato e flag

Dopo un'operazione, la CPU può dover ricordare alcune condizioni:

- il risultato è zero;
- c'è stato un riporto (*carry*);
- il risultato è negativo;
- è avvenuto un overflow.

Queste informazioni possono essere rappresentate da bit chiamati **flag**. Servono, per esempio, a decidere se una condizione è vera e se un salto deve essere eseguito.

---

## 7. Un'istruzione vista da vicino

Supponiamo di voler eseguire:

```text
R3 = R1 + R2
```

con `R1 = 7` e `R2 = 5`.

### Passo 1: il PC indica la prossima istruzione

```text
PC = 100
```

La CU usa questo indirizzo per chiedere alla memoria l'istruzione che si trova in posizione 100.

### Passo 2: l'istruzione entra nell'IR

La memoria restituisce un codice che significa, per esempio:

```text
ADD R3, R1, R2
```

La CPU lo conserva temporaneamente nell'**IR**.

### Passo 3: la CU decodifica

La CU riconosce:

- operazione: `ADD`;
- sorgenti: `R1` e `R2`;
- destinazione: `R3`.

### Passo 4: i registri forniscono i dati

```text
R1 = 7  ----\
             >---- ALU: ADD ----> 12
R2 = 5  ----/                         |
                                      v
                                    R3 = 12
```

### Passo 5: il PC prosegue

Il PC viene aggiornato per indicare l'istruzione successiva, salvo che l'istruzione corrente imponga un salto.

La sequenza generale è:

```text
FETCH       prendi l'istruzione dalla memoria
   |
DECODE      capisci che cosa significa
   |
EXECUTE     esegui l'operazione
   |
WRITE-BACK  conserva il risultato
```

Questi nomi descrivono fasi logiche. Nelle CPU moderne più istruzioni possono trovarsi contemporaneamente in fasi diverse, come in una catena di montaggio; lo studieremo più avanti.

---

## 8. Come comunicano CPU e memoria?

I bus sono percorsi di comunicazione. A livello didattico distinguiamo:

```text
+--------+       +-----+       +---------+
|  CPU   |=======| BUS |=======| MEMORIA |
+--------+       +-----+       +---------+
              /    |    \
             /     |     \
      indirizzi   dati   controllo
```

- **Bus degli indirizzi:** indica quale posizione si vuole raggiungere;
- **Bus dei dati:** trasporta il contenuto;
- **Bus di controllo:** trasporta segnali come lettura, scrittura e sincronizzazione.

Esempio di lettura:

```text
1. PC contiene l'indirizzo della prossima istruzione.
2. L'indirizzo passa verso la memoria.
3. La memoria restituisce l'istruzione.
4. L'istruzione entra nell'IR.
5. La CU la decodifica.
```

Questa è una semplificazione utile per cominciare. I processori reali usano cache, prefetch, pipeline, più core e meccanismi molto più complessi.

---

## 9. La distinzione più importante

```text
+----------------------+-----------------------------+
| COMPONENTE           | DOMANDA A CUI RISPONDE      |
+----------------------+-----------------------------+
| Memoria              | Dove sono programma e dati? |
| PC                   | Quale istruzione viene dopo?|
| IR                   | Quale istruzione sto usando?|
| CU                   | Che segnali devo generare?  |
| Registri             | Quali valori uso subito?    |
| ALU                  | Quale operazione eseguo?    |
| Bus                  | Come viaggiano le info?     |
+----------------------+-----------------------------+
```

Da ricordare:

> **La memoria conserva. Il PC indica. L'IR trattiene l'istruzione corrente. La CU coordina. I registri tengono i valori vicini. L'ALU calcola. I bus collegano.**

---

## 10. Confusioni frequenti

### “I registri sono la RAM?”

No. Entrambi conservano informazioni, ma i registri sono dentro la CPU, pochissimi e molto veloci. La RAM è più grande, più lontana dalla parte operativa e contiene programmi e dati in uso dal sistema.

### “Il PC contiene il programma?”

No. Il **Program Counter** contiene un indirizzo, cioè indica dove si trova la prossima istruzione. Il programma è nella memoria.

### “L'IR indica la prossima istruzione?”

Non esattamente. L'IR conserva l'istruzione corrente. Il PC indica il prossimo punto da leggere.

### “La CU fa i calcoli?”

No. La CU coordina. I calcoli aritmetici e logici vengono eseguiti dall'ALU.

### “Von Neumann è il nome di una CPU?”

No. È il nome associato a un modello di organizzazione del calcolatore: CPU, memoria, input/output e collegamenti, con istruzioni e dati conservati in memoria.

### “Le CPU moderne sono identiche al modello originale?”

No. Il modello di von Neumann è una mappa concettuale. Le CPU moderne aggiungono cache, pipeline, più unità di esecuzione, più core e altre ottimizzazioni. La mappa resta utile, ma non descrive ogni strada e ogni dettaglio della città.

---

## 🧪 Attività: impersoniamo una CPU

**Durata:** 20-25 minuti  
**Materiale:** cartelli con `PC`, `IR`, `MAR`, `MDR`, `R1`, `R2`, `R3`, `CU`, `ALU`, `MEMORIA`.

### Preparazione

Scegliere alcuni studenti per impersonare i componenti. Scrivere alla lavagna:

```text
100: LOAD R1, 200
101: LOAD R2, 201
102: ADD R3, R1, R2
103: STORE R3, 202
200: 7
201: 5
202: vuoto
```

### Esecuzione guidata

La classe deve rappresentare i passaggi:

1. il PC indica `100`;
2. il MAR riceve l'indirizzo `100`;
3. il MDR riceve l'istruzione `LOAD R1, 200`;
4. l'IR conserva l'istruzione;
5. la CU la interpreta;
6. la memoria restituisce il valore `7` dalla posizione `200`;
7. il valore entra in `R1`;
8. si ripete con `R2`;
9. l'ALU somma `R1` e `R2`;
10. il risultato va in `R3` e poi nella posizione `202`.

Gli studenti che osservano devono rispondere:

- chi sta indicando un indirizzo?
- chi sta trasportando un dato?
- chi sta conservando l'istruzione?
- chi sta coordinando?
- chi sta calcolando?

### Variante con errore

Il docente dà volutamente al MAR il valore `201` quando la CU ha chiesto la posizione `200`. La classe deve individuare l'errore e dire perché il risultato finale sarebbe sbagliato.

---

## 🎯 Domande di verifica

1. Perché è utile conservare il programma in memoria?
2. Quali sono i cinque blocchi del modello introduttivo di von Neumann?
3. Qual è la differenza fra CU e ALU?
4. Perché i registri sono veloci ma pochi?
5. Che cosa contiene il PC?
6. Qual è la differenza fra MAR e MDR?
7. Che cosa succede durante fetch, decode ed execute?
8. Se il PC contiene 500, che cosa possiamo sapere? Che cosa non possiamo ancora sapere?
9. Perché la metafora del banco di lavoro aiuta a capire i registri?
10. In quale punto del modello collocheresti tastiera, RAM, CPU e monitor?

### Domande che fanno lavorare l'intuizione

- Se aumentassimo molto la capacità dei registri, perché non elimineremmo automaticamente la RAM?
- Se il PC si corrompesse, quale tipo di comportamento osserveremmo?
- Se l'ALU funzionasse ma i registri ricevessero valori sbagliati, perché il risultato sarebbe comunque errato?
- Perché un programma diverso può cambiare il comportamento dello stesso hardware?
- Se dati e istruzioni sono entrambi sequenze di bit, che cosa impedisce di interpretarli nel modo sbagliato?

---

## 🌍 Scenari reali (e uno plausibile) da analizzare

Le domande sopra fanno ragionare sul modello. Questi tre casi fanno vedere che cosa succede quando qualcosa, in un pezzo di quel modello, va davvero storto — o potrebbe andare storto.

### Caso 1 — Il processore che divideva male (1994, reale)

Nel 1994 un matematico, Thomas Nicely, si accorse che il suo nuovo processore Intel Pentium sbagliava alcune divisioni in virgola mobile: non tutte, solo combinazioni particolari di numeri (esempio storico: 4.195.835 diviso 3.145.727). La causa era un errore in una tabella usata dall'unità che eseguiva le divisioni: alcune celle che avrebbero dovuto contenere un valore contenevano zero per un difetto di fabbricazione. Intel dovette sostituire i processori difettosi: costo dichiarato, 475 milioni di dollari.

**Domande:** Quale "pezzo" del nostro modello (CU, ALU, registri, memoria) è coinvolto in un errore di calcolo come questo? Perché un errore così piccolo poteva restare nascosto per mesi prima di essere scoperto? Che cosa avrebbe potuto aiutare a scoprirlo prima?

### Caso 2 — Il razzo che si autodistrusse per un numero troppo grande (1996, reale)

Il volo inaugurale del razzo europeo Ariane 5 si autodistrusse 37 secondi dopo il decollo. La causa: un valore interno, calcolato come numero molto grande (a 64 bit), veniva convertito in un formato più piccolo (16 bit) da un pezzo di software riciclato dal razzo precedente (Ariane 4), che volava più lentamente e non generava mai numeri così grandi. Il valore non ci stava: overflow, eccezione, il sistema di guida si è spento da solo, il razzo ha perso il controllo ed è stato autodistrutto. Danno: oltre 370 milioni di dollari, persi in meno di un minuto.

**Domande:** con quale concetto già visto (a proposito di ALU e registri di stato) collegate la parola "overflow"? Il software non si è "rotto per caso": ha funzionato esattamente come previsto. Perché questo rende il caso più inquietante, non meno? Che cosa insegna questo caso sul riutilizzare codice vecchio in un contesto nuovo?

### Caso 3 — "Ha scritto nel posto sbagliato" (plausibile, non un fatto realmente accaduto)

Immaginate un tecnico che, per un errore di battitura, invia alla CPU l'indirizzo `202` invece di `200` — esattamente come nella "Variante con errore" dell'attività di prima. Il MAR riceve l'indirizzo sbagliato, il MDR riporta indietro un dato che si trovava lì per un altro motivo, e quel dato — che magari doveva restare vuoto — viene usato come se fosse un operando valido.

**Domande:** in questo modello semplificato, chi avrebbe dovuto "accorgersi" che l'indirizzo non aveva senso? Perché i computer moderni hanno meccanismi (che vedremo più avanti, parlando di sistemi operativi) per impedire a un programma di leggere o scrivere ovunque in memoria? Che differenza c'è tra questo errore e quelli dei Casi 1 e 2 (chi lo causa: hardware, software, persona)?

> 💡 Consiglio di regia: dividi la classe in tre gruppi, uno per caso, 5 minuti di discussione, poi un portavoce per gruppo riassume alla lavagna. Il Caso 3 apre bene un collegamento a un tema più ampio: molte falle di sicurezza informatica nascono proprio da un programma che legge o scrive in un indirizzo di memoria che non avrebbe dovuto toccare — ne riparleremo quando affronteremo la sicurezza.

---

## ✅ Soluzioni e spunti per il docente

**Domande di verifica:**

1. Perché conservare il programma in memoria: permette di cambiare il comportamento della macchina caricando un programma diverso, senza modificare l'hardware.
2. I cinque blocchi: memoria, CPU, input, output, bus.
3. CU contro ALU: la CU coordina e decodifica, genera segnali di controllo; l'ALU esegue davvero i calcoli aritmetici e logici.
4. Registri veloci ma pochi: sono circuiti dentro la CPU, fisicamente vicinissimi alle unità di calcolo; questa vicinanza li rende velocissimi, ma anche costosi e quindi limitati di numero.
5. Il PC contiene: l'indirizzo di memoria della prossima istruzione da eseguire.
6. MAR contro MDR: il MAR contiene l'indirizzo (il "dove"), il MDR contiene il dato trasferito (il "che cosa").
7. Fetch/decode/execute: si preleva l'istruzione indicata dal PC (fetch), la CU la interpreta (decode), l'operazione viene eseguita, per esempio dall'ALU (execute), il risultato viene eventualmente salvato (write-back).
8. Se PC = 500: sappiamo dove si trova la prossima istruzione, non sappiamo ancora quale istruzione sia né che cosa farà — serve leggerla e decodificarla.
9. La metafora del banco aiuta perché rende tangibile la differenza fra "conservare molto, lontano, lento" (l'archivio/RAM) e "poco, vicino, velocissimo" (il banco/i registri).
10. Tastiera: input. RAM: memoria. CPU: elaborazione (CU + ALU + registri). Monitor: output.

**Domande che fanno lavorare l'intuizione:**

- Più registri non eliminano la RAM: i registri restano legati alla CPU per costo e spazio fisico; servono comunque grandi quantità di memoria per tutto ciò che non sta "sul banco" in quel momento.
- PC corrotto: la CPU leggerebbe/eseguirebbe istruzioni a un indirizzo sbagliato, con comportamento imprevedibile (blocco, crash, o un "salto" nel punto sbagliato del programma).
- ALU giusta, registri sbagliati: il calcolo sarebbe eseguito correttamente ma sugli operandi sbagliati — tecnicamente corretto, ma inutile ("garbage in, garbage out").
- Un programma diverso cambia il comportamento perché è la sequenza di istruzioni in memoria a dettare, passo passo, che segnali genera la CU: l'hardware resta lo stesso, cambia solo che cosa gli viene chiesto di fare.
- Che cosa impedisce di interpretare male i bit: il contesto — l'indirizzo/il registro in cui si trovano, e nel ciclo fetch-decode la CU sa (dal PC) che sta leggendo un'istruzione e non un dato. È la disciplina con cui il programma è scritto ed eseguito a garantire l'interpretazione corretta, non una proprietà dei bit in sé.

**Scenari reali:** Caso 1 (Pentium) è un errore nell'ALU/unità di calcolo, difficile da scoprire perché capitava solo con rarissime combinazioni di numeri (un test esaustivo era impensabile all'epoca). Caso 2 (Ariane 5) è un errore di registro di stato/overflow non gestito: il software ha fatto esattamente quello per cui era stato scritto, il problema è che quel codice non andava eseguito in quel contesto — inquietante perché niente si è "rotto" per caso. Caso 3: nel modello base nessuno si accorge dell'indirizzo sbagliato (è un modello semplificato); nella realtà è il sistema operativo, insieme a meccanismi hardware di protezione della memoria, a impedirlo.

---

## 📝 Compito a casa (facoltativo, breve)

Cerca online un bug storico famoso legato all'hardware o alla memoria (per esempio uno dei due raccontati sopra, oppure un altro che trovi) e scrivi 4-5 righe: che cosa è andato storto, e a quale "pezzo" del modello di von Neumann (memoria, registro, ALU, bus) è più collegato.

---

## 🌱 Un pensiero scomodo (breve)

I registri e la CPU di cui abbiamo parlato non sono solo schemi su una lavagna: sono circuiti stampati su silicio, prodotti in fabbriche che consumano acqua ed energia in grandi quantità e che dipendono da minerali estratti in condizioni spesso difficili. Non approfondiamo qui (ci torneremo parlando di hardware e sostenibilità), ma vale la pena chiedersi: *quando compriamo un computer nuovo, che cosa "paghiamo" davvero, oltre al prezzo in negozio?*

---

## Collegamento con il programma

Questa integrazione prepara:

- **Settimana 1:** parte operativa, parte di controllo e ruolo dei registri;
- **Settimana 2:** macchina di von Neumann e bus di sistema;
- **Settimana 3:** struttura interna della CPU e registri;
- **Settimana 4:** ciclo fetch-decode-execute;
- **Settimana 5:** gerarchia della memoria, cache e RAM.

Il filo logico è:

```text
Von Neumann
     |
     v
CPU + memoria + I/O + bus
     |
     v
CU + registri + ALU
     |
     v
fetch -> decode -> execute -> write-back
     |
     v
gerarchia delle memorie e prestazioni
```

---

## 🎮 Materiali consigliati (video, simulatori, giochi)

Non serve reinventare tutto: per questo argomento esistono risorse gratuite fatte molto bene.

- **[Ben Eater — canale YouTube (@BenEater)](https://www.youtube.com/@BenEater):** costruisce un computer a 8 bit su breadboard, registro per registro, bus per bus. Vederne anche solo pochi minuti rende "fisici" concetti come registri e bus che altrimenti restano astratti. Ottimo da guardare a casa dopo questa lezione.
- **[Nand2Tetris](https://www.nand2tetris.org/):** corso gratuito e open source che parte dalle porte logiche e arriva a costruire un computer intero. Impegnativo, ma perfetto per chi vuole andare oltre il programma.
- **[Simple 8-bit Assembler Simulator](https://schweigi.github.io/assembler-simulator/):** simulatore nel browser, gratuito, che mostra registri e memoria mentre un programmino in assembly gira davvero. Usalo in laboratorio subito dopo l'attività "Impersoniamo una CPU", per far vedere la stessa cosa fatta da una macchina vera invece che dai ragazzi.
- **[Human Resource Machine](https://tomorrowcorporation.com/humanresourcemachine)** (gioco a pagamento, Tomorrow Corporation): il giocatore *è* letteralmente una piccola CPU con un solo registro (le mani dell'impiegato), un inbox e un outbox. Ottimo suggerimento come attività a casa per chi preferisce giocare piuttosto che ripassare in modo tradizionale.

---

## Riferimenti per approfondire

- John von Neumann et al., **First Draft of a Report on the EDVAC** (1945), documento storico sul concetto di programma memorizzato: [computer-history.info](https://www.computer-history.info/Page4.dir/pages/FirstDraft.html).
- Computer History Museum, **The Stored Program Concept**: [computerhistory.org](https://www.computerhistory.org/revolution/birth-of-the-computer/4/78).
- Encyclopaedia Britannica, **John von Neumann**: [britannica.com](https://www.britannica.com/biography/John-von-Neumann).
- Patterson e Hennessy, **Computer Organization and Design**, testo di riferimento sull'organizzazione dei calcolatori.
- David A. Patterson e John L. Hennessy, **Computer Architecture: A Quantitative Approach**, per il rapporto fra architettura, prestazioni e gerarchia della memoria.
