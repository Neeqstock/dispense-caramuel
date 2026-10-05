# Extreme Programming nei laboratori

> Extreme Programming (XP) non significa lavorare più velocemente o sotto pressione. Significa rendere frequenti, visibili e correggibili i passaggi con cui si costruisce software.

XP è una metodologia nata nel mondo dello sviluppo software alla fine degli anni Novanta, associata soprattutto a Kent Beck. Le sue pratiche sono state pensate per team professionali, ma alcune possono diventare strumenti didattici molto efficaci: aiutano gli studenti a collaborare, ricevere feedback e imparare dal codice reale.

A scuola non dobbiamo imitare un'azienda. Dobbiamo prendere le pratiche che rendono l'apprendimento più osservabile e adattarle a tempi, età, valutazione e sicurezza del laboratorio.

---

## 1. I valori di XP

XP si fonda tradizionalmente su cinque valori.

### Comunicazione

Il codice non è l'unico modo per comunicare. Prima di programmare bisogna saper descrivere:

- quale problema si sta affrontando;
- quale comportamento ci si aspetta;
- che cosa è già stato provato;
- dove si trova l'errore.

**A scuola:** ogni gruppo mantiene una scheda breve con obiettivo, stato del lavoro e ostacolo attuale.

### Semplicità

Si costruisce ciò che serve adesso, evitando di aggiungere funzionalità immaginarie che nessuno ha richiesto.

**A scuola:** prima una versione minima che funziona, poi eventuali estensioni. Un programma piccolo e comprensibile vale più di un progetto enorme copiato o incompleto.

### Feedback

Un feedback utile arriva presto: un test, una revisione, una demo o una domanda del docente possono mostrare che una scelta non funziona prima che diventi difficile correggerla.

**A scuola:** gli studenti mostrano una versione funzionante più volte, non soltanto alla consegna finale.

### Coraggio

Serve coraggio per chiedere aiuto, cancellare una soluzione sbagliata, ammettere di non aver capito o modificare codice già scritto.

**A scuola:** l'errore documentato è una prova di lavoro, non automaticamente una colpa.

### Rispetto

Il rispetto riguarda compagni, tempi, codice e responsabilità condivise. Una revisione critica deve parlare del programma e delle scelte, non svalutare la persona.

---

## 2. Le pratiche XP più utili a scuola

Non tutte le pratiche XP hanno lo stesso valore didattico. Per una classe sceglierei queste.

### User story

Una user story descrive una necessità dal punto di vista di chi userà il programma:

> Come docente, voglio cercare uno studente per nome, così posso vedere rapidamente i suoi dati.

Una buona user story è breve e verificabile. Non descrive già la soluzione tecnica.

Formato:

```text
Come [tipo di utente]
vorrei [azione o risultato]
per [motivo].
```

A ogni storia si aggiungono **criteri di accettazione**:

```text
- se il nome esiste, vengono mostrati i dati;
- se il nome non esiste, compare un messaggio comprensibile;
- una ricerca vuota non manda in errore il programma.
```

### Planning game

La classe decide che cosa fare prima, stimando la difficoltà. Non si pretende una previsione professionale: l'obiettivo è imparare a dividere un problema.

Ogni gruppo assegna una stima semplice:

- 1 punto: compito breve e noto;
- 2 punti: compito con una difficoltà;
- 3 punti: compito da dividere o chiarire.

Se una storia vale 8 o 13 punti, probabilmente è troppo grande e va scomposta.

### Piccoli rilasci

Un piccolo rilascio è una versione utilizzabile, anche minima:

```text
Rilascio 1: creare e stampare un animale
Rilascio 2: cercare un animale
Rilascio 3: modificarlo e rimuoverlo
Rilascio 4: salvare i dati
```

Ogni rilascio deve essere eseguibile e dimostrabile. Questo riduce il rischio della “grande consegna finale che non parte”.

### Pair programming

Due studenti lavorano allo stesso computer con ruoli alternati:

- **driver:** scrive il codice;
- **navigator:** osserva, fa domande, controlla il ragionamento e propone il prossimo passo.

I ruoli cambiano ogni 15-20 minuti. Il navigator non è un supervisore e il driver non è uno stenografo: entrambi devono capire il codice.

Regole pratiche:

1. chi guida spiega che cosa sta per scrivere;
2. chi osserva non prende il mouse di nascosto;
3. ogni cambio di ruolo viene annotato;
4. alla fine entrambi spiegano una parte del lavoro.

Il pair programming non deve diventare una punizione per chi è più lento. Le coppie vanno cambiate e il docente deve osservare che la collaborazione sia reale.

### Test-first e TDD, in versione scolastica

Nel TDD professionale si scrive prima un test che fallisce, poi il codice minimo per farlo passare, infine si migliora il codice.

A scuola si può usare una versione più leggera:

```text
1. descrivi il comportamento atteso;
2. prepara un esempio concreto;
3. scrivi o esegui il test;
4. implementa la soluzione;
5. ripeti il test;
6. migliora il codice senza cambiare il comportamento.
```

Esempio:

```text
Test: Animale("Pio", 1.8).descrizione()
Atteso: contiene "Pio" e "1.8"
```

Non è necessario trasformare ogni esercizio in una lezione formale su JUnit o pytest. Il principio importante è separare “che cosa deve succedere” da “come l'ho programmato”.

### Refactoring

Il refactoring modifica la struttura interna senza cambiare il comportamento osservabile.

Esempi:

- rinominare `x` in `pesoIniziale`;
- estrarre un metodo troppo lungo;
- eliminare codice duplicato;
- spostare una responsabilità nella classe corretta;
- dividere una funzione in parti testabili.

Prima e dopo il refactoring bisogna eseguire gli stessi test. Altrimenti non sappiamo se abbiamo migliorato il codice o cambiato accidentalmente il programma.

### Collective ownership

Il codice del progetto appartiene al gruppo, non alla persona che lo ha scritto per prima. Tutti devono poter leggere, eseguire e migliorare ogni parte.

A scuola questo significa:

- niente file conosciuti da una sola persona;
- niente “non toccare questa parte, l'ho fatta io”;
- commit o note con descrizioni comprensibili;
- spiegazione reciproca delle scelte.

La responsabilità resta valutabile individualmente: proprietà collettiva non significa assenza di responsabilità.

### Continuous integration, in forma scolastica

Ogni volta che un gruppo completa una modifica importante:

1. salva una versione identificabile;
2. esegue il programma;
3. esegue i test disponibili;
4. controlla che il progetto sia ancora condivisibile.

Se si usa Git, il gruppo può fare piccoli commit. Se Git non è ancora parte del corso, si può usare una convenzione semplice:

```text
stalla-v01
stalla-v02-ricerca
stalla-v03-rimozione
```

L'idea essenziale è integrare spesso, non accumulare modifiche invisibili fino all'ultimo giorno.

### Retrospective

Alla fine di una sessione il gruppo risponde a tre domande:

- che cosa ha funzionato?
- che cosa ci ha bloccato?
- che cosa cambiamo nella prossima sessione?

La retrospettiva non è una gara a trovare colpe. Deve produrre almeno una decisione concreta.

### Sustainable pace

XP rifiuta l'idea che una squadra debba lavorare sempre al limite. In laboratorio significa proteggere:

- pause;
- tempi realistici;
- sonno e recupero;
- richiesta di aiuto;
- conclusione ordinata della sessione.

Un progetto che funziona solo dopo una notte insonne non è un buon progetto didattico.

---

## 3. Come usarle in una sessione da tre ore

### Prima fase: pianificazione (20 minuti)

Il docente presenta il problema e chiarisce i criteri di accettazione. Gli studenti:

1. leggono le user story;
2. fanno domande;
3. dividono le storie troppo grandi;
4. scelgono il primo compito;
5. assegnano i ruoli nella coppia.

### Seconda fase: ciclo di lavoro (70 minuti)

Le coppie alternano driver e navigator. Ogni 20 minuti fanno un controllo:

```text
Che cosa dovrebbe funzionare ora?
Quale test lo dimostra?
Qual è il prossimo passo piccolo?
```

Il docente non aspetta la fine per intervenire: osserva le domande, il debugging, la divisione dei ruoli e la qualità delle spiegazioni.

### Terza fase: integrazione e demo (35 minuti)

Ogni gruppo:

- integra il lavoro;
- esegue i test;
- mostra una funzionalità;
- dichiara un limite o un bug ancora aperto.

Dire “questa parte non è ancora pronta” è preferibile a nascondere il problema.

### Quarta fase: retrospettiva (15 minuti)

Ogni gruppo completa:

```text
Ha funzionato:
Ci ha bloccato:
La prossima volta cambiamo:
```

### Quinta fase: chiusura (20 minuti)

Il docente raccoglie evidenze individuali: una spiegazione orale, un test scritto, una nota di debug o una breve revisione del codice.

---

## 4. Esempio per la 4CI alternativa: archivio della stalla

### User stories

```text
US1 — Come utente, voglio aggiungere un animale, così posso inserirlo nell'archivio.
US2 — Come utente, voglio vedere tutti gli animali, così posso controllare la stalla.
US3 — Come utente, voglio cercare per nome, così trovo rapidamente un animale.
US4 — Come utente, voglio rimuovere un animale, così l'archivio resta aggiornato.
US5 — Come utente, voglio salvare l'archivio, così non perdo i dati.
```

### Scomposizione di US1

```text
- definire la classe Animale;
- creare un costruttore;
- validare il nome;
- aggiungere l'oggetto alla lista;
- aggiornare la stampa;
- testare input valido e vuoto.
```

### Criteri di accettazione di US3

- la ricerca non distingue maiuscole e minuscole;
- se trova un animale, mostra la descrizione;
- se non trova nulla, mostra un messaggio;
- la ricerca vuota non provoca un crash.

### Ruoli durante il laboratorio

- **cliente simulato:** chiarisce i criteri e prova la funzione;
- **driver:** scrive;
- **navigator:** controlla ragionamento e test;
- **responsabile integrazione:** verifica che il progetto completo continui a funzionare.

Il ruolo di cliente non è sempre separato: può essere svolto a turno dal docente o da un'altra coppia.

---

## 5. Regia docente

Il docente non è soltanto il programmatore più esperto del laboratorio. In un'attività ispirata a XP svolge soprattutto queste funzioni:

### Preparare il terreno

- scrivere user story comprensibili;
- definire criteri di accettazione;
- preparare un primo esempio funzionante;
- proporre compiti abbastanza piccoli;
- rendere disponibili test e dati di prova.

### Osservare il processo

Durante il lavoro, guardare:

- chi prende sempre la tastiera;
- chi sa spiegare il codice;
- se le coppie eseguono test o procedono per tentativi casuali;
- se il gruppo integra spesso;
- se una persona diventa l'unico punto di conoscenza.

### Intervenire con domande

Invece di correggere subito tutto, chiedere:

- quale risultato ti aspettavi?
- quale risultato hai ottenuto?
- qual è il test più piccolo che può distinguere le due ipotesi?
- quale parte del codice ha questa responsabilità?
- come lo spiegheresti al compagno?

### Valutare senza premiare solo la velocità

Una valutazione equilibrata considera:

- comportamento corretto del programma;
- qualità della progettazione;
- test e debugging;
- collaborazione osservabile;
- capacità di spiegare il proprio lavoro;
- miglioramento fra una versione e la successiva.

XP non deve diventare una nuova gara a chi consegna prima.

---

## 6. Adattamenti e limiti

Non tutte le pratiche vanno applicate alla lettera.

- **Stand-up quotidiano:** in una classe può bastare un check-in di cinque minuti a inizio laboratorio.
- **Pair programming:** non tutte le attività devono essere a coppie; alternare lavoro individuale, coppie e gruppi.
- **TDD formale:** introdurre prima test manuali e criteri di accettazione, poi eventualmente JUnit o pytest.
- **Continuous integration:** piccoli salvataggi o commit sono già un buon inizio.
- **Cliente:** il docente può simulare il cliente, ma deve lasciare spazio agli studenti per chiarire requisiti.
- **Velocity:** non usare i punti per confrontare studenti o gruppi. Servono a stimare e dividere il lavoro, non a creare classifiche.

Il rischio principale è trasformare XP in una collezione di rituali vuoti. Se gli studenti fanno stand-up ma non imparano a formulare problemi, o compilano una scheda senza leggere i test, abbiamo copiato la forma e perso il senso.

---

## 7. Checklist per gli studenti

Prima della consegna, il gruppo controlla:

- [ ] Abbiamo scritto che cosa deve fare ogni funzionalità.
- [ ] Abbiamo diviso i compiti troppo grandi.
- [ ] Tutti hanno scritto e spiegato una parte del codice.
- [ ] Abbiamo alternato driver e navigator.
- [ ] Abbiamo testato casi normali e casi limite.
- [ ] Abbiamo integrato spesso il lavoro.
- [ ] Sappiamo dichiarare almeno un limite del programma.
- [ ] Il progetto può essere eseguito da un compagno che non lo ha scritto.
- [ ] Abbiamo registrato una decisione dalla retrospettiva.

## Domande di ripasso

1. Perché una user story non dovrebbe iniziare già con la soluzione tecnica?
2. Qual è la differenza fra test e criterio di accettazione?
3. Perché il navigator deve parlare e non limitarsi a guardare?
4. In che senso il refactoring può migliorare il codice senza aggiungere funzionalità?
5. Perché integrare spesso riduce il rischio del progetto?
6. Che cosa può andare storto se il docente valuta solo il prodotto finale?
7. Quale pratica XP si adatta meglio alla vostra classe? Quale richiede più cautela?

## Riferimenti

- Kent Beck, **Extreme Programming Explained: Embrace Change**, Addison-Wesley.
- Agile Alliance, [Extreme Programming](https://www.agilealliance.org/glossary/xp/).
- Agile Alliance, [User Stories](https://www.agilealliance.org/glossary/user-stories/).
- Martin Fowler, [Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html).
- Martin Fowler, [Pair Programming](https://martinfowler.com/articles/on-pair-programming.html).
