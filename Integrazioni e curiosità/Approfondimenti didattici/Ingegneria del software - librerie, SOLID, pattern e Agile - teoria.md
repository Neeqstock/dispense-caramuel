# 🏗️ Ingegneria del software: dai componenti al lavoro di squadra

**4CI · Dispensa teorica · Librerie, SOLID, design pattern, Agile e caso Log4Shell · Una lezione di 60 minuti**

> **Domanda guida:** come possiamo costruire software che sia comprensibile, modificabile e affidabile, anche quando utilizza componenti esterni e viene sviluppato da più persone?

Questa dispensa non richiede programmazione, installazioni o computer. Gli esempi sono descrizioni di problemi e scelte di progetto, non esercizi di sintassi.

## 🧭 1. Perché esiste l'ingegneria del software?

Un programma può funzionare in una dimostrazione e diventare difficile da gestire quando aumentano utenti, funzionalità e persone che ci lavorano.

L'**ingegneria del software** affronta progettazione, sviluppo, verifica, rilascio e manutenzione del software. Non riguarda soltanto la scrittura delle istruzioni: riguarda anche le decisioni che permettono a un progetto di durare.

Le domande fondamentali sono:

- stiamo risolvendo il problema giusto?
- chi legge il progetto può comprenderlo?
- quanto costa aggiungere una funzionalità?
- come controlliamo che una modifica non rompa il resto?
- quali componenti esterni utilizziamo?
- come collaboriamo e raccogliamo feedback?
- che cosa facciamo quando emerge un errore o una vulnerabilità?

**Programmare non significa soltanto fare gestionali.** Queste domande riguardano anche videogiochi, strumenti musicali, simulatori, applicazioni scientifiche e software di comunicazione.

### Il ponte con l'OOP di settembre–ottobre

Classi, oggetti, incapsulamento, ereditarietà, interfacce e polimorfismo sono strumenti per organizzare il codice. Ora saliamo di livello:

- non soltanto «che cos'è un'interfaccia?», ma «quale contratto dovrebbe rappresentare?»;
- non soltanto «come si eredita?», ma «quando conviene ereditare e quando no?»;
- non soltanto «funziona?», ma «è facile da cambiare e verificare?».

**Esempio conduttore:** immaginiamo un videogioco nel quale personaggi diversi possono cambiare attacco, produrre suoni e generare eventi da registrare. Non costruiremo il gioco: useremo queste esigenze per ragionare sul progetto.

### La nostra storia: il drago e il potenziamento

Il gioco si chiama, per questa lezione, **La grotta del drago**. Il drago parte con 100 punti vita e un morso da 10 punti di danno. Quando raccoglie una gemma, può usare il fuoco, che infligge 20 punti.

Durante la lezione arrivano tre richieste:

1. «Aggiungiamo anche il ghiaccio, da 15 punti.»
2. «Quando il drago viene colpito, aggiorniamo la barra della vita e facciamo sentire un suono.»
3. «Se il server si blocca, vogliamo capire che cosa è successo.»

**Funzionante ma difficile da mantenere:** ogni richiesta obbliga a intervenire in un unico grande componente che gestisce tutto.

**Progettato per il cambiamento:** le regole del personaggio, i comportamenti di attacco, l'audio e la registrazione degli eventi hanno responsabilità riconoscibili e contratti chiari.

> **Domanda:** se il gioco oggi funziona, quale delle due soluzioni preferiremmo dovendo aggiungere venti nuovi attacchi?

## 📦 2. Librerie: non costruire ogni pezzo da zero

Una **libreria** è un insieme di funzionalità riutilizzabili, sviluppate per essere utilizzate da altri programmi.

Un videogioco potrebbe usare librerie per:

- riprodurre suoni;
- disegnare immagini;
- gestire comunicazioni di rete;
- leggere formati di dati;
- registrare eventi.

Il nostro programma non deve necessariamente inventare tutti questi meccanismi. Può concentrarsi sulle regole del gioco e affidare le funzionalità generali a componenti esistenti.

### Libreria, API e dipendenza

| Termine | Significato |
|---|---|
| **Libreria** | Il componente che offre funzionalità riutilizzabili |
| **API** | Le operazioni e i contratti attraverso cui possiamo utilizzare il componente |
| **Dipendenza** | Un componente esterno di cui il nostro programma ha bisogno |
| **Versione** | Una specifica edizione del componente, con determinate funzionalità e correzioni |

L'API è come il pannello dei comandi: possiamo utilizzare una funzione senza conoscere ogni dettaglio interno. **API** e **libreria** non sono sinonimi: anche un servizio remoto può esporre un'API.

Nel mondo Java le librerie sono spesso distribuite in archivi **JAR**, che contengono classi compilate e risorse. Il JAR è il contenitore, non una garanzia di qualità.

### Esempio: il ruggito del drago

Vogliamo riprodurre un ruggito quando il drago attacca.

| Senza riuso | Con una libreria audio |
|---|---|
| Dobbiamo occuparci di lettura del file, formato audio, riproduzione e gestione degli errori | Chiediamo alla libreria di riprodurre una risorsa usando le operazioni della sua API |
| Il lavoro riguarda sia il gioco sia il funzionamento dell'audio | Il nostro lavoro si concentra su quando e perché il drago deve ruggire |

Il gioco decide **quando riprodurre il suono**; la libreria gestisce **come riprodurlo**. Se il file non esiste, però, dobbiamo ancora decidere che cosa deve accadere: segnalare il problema, impedire l'avvio oppure proseguire esplicitamente senza audio.

**Un esempio Java reale:** JFugue offre funzionalità musicali; Log4j offre funzionalità di logging. Non sono intercambiabili soltanto perché entrambe sono librerie.

**Analogia quotidiana:** il telecomando espone comandi come volume e cambio canale; non mostra tutti i circuiti del televisore. Allo stesso modo, l'API espone operazioni, non ogni dettaglio della loro realizzazione.

### Dipendenze dirette e transitive

Una dipendenza è **diretta** quando la scegliamo per il nostro progetto.

È **transitiva** quando viene richiesta da un'altra dipendenza. Per esempio:

> Il gioco usa una libreria di rete; la libreria di rete usa un componente per registrare gli eventi.

Possiamo quindi utilizzare software che non abbiamo scelto personalmente. Strumenti come Maven e Gradle aiutano a gestire queste relazioni, ma non eliminano la responsabilità di conoscerle.

**Esempio inventato:** scegliamo il componente «ReteGioco», che a sua volta usa «RegistroEventi». Per noi ReteGioco è una dipendenza diretta e RegistroEventi è transitiva. Se emerge un problema in RegistroEventi, dobbiamo verificare anche il nostro gioco, pur non avendo scelto quel componente direttamente.

### Vantaggi e responsabilità

| Vantaggio | Responsabilità corrispondente |
|---|---|
| Risparmiare lavoro | Verificare che il componente sia adatto al problema |
| Riutilizzare competenze altrui | Leggere documentazione e limiti |
| Ricevere correzioni | Gestire aggiornamenti e compatibilità |
| Integrare funzionalità complesse | Conoscere dipendenze e rischi |
| Usare software open source | Rispettare la licenza e valutare la manutenzione |

**Open source** significa che il codice è disponibile secondo una licenza che ne disciplina uso, modifica e distribuzione. Non significa automaticamente sicuro, gratuito in ogni senso o privo di obblighi.

> **Da ricordare:** utilizzare una libreria significa riutilizzare funzionalità, ma anche assumersi responsabilità sui componenti inclusi.

## 🧱 3. SOLID: cinque criteri per discutere il progetto

SOLID raccoglie cinque principi di progettazione orientata agli oggetti. Sono **criteri**, non leggi: applicarli meccanicamente può produrre più complessità di quella che risolve.

### S — Single Responsibility: responsabilità coerenti

> Un componente dovrebbe avere un solo motivo principale per cambiare.

Immaginiamo una classe che gestisca contemporaneamente vita del personaggio, riproduzione audio, salvataggio e connessione al server. Potrebbe cambiare per ragioni completamente diverse.

Separare responsabilità permette di modificare il sistema audio senza intervenire nelle regole della vita del personaggio.

**Non significa:** una classe deve avere un solo metodo. Significa raggruppare ciò che cambia per ragioni coerenti e separare ciò che cambia indipendentemente.

**Esempio prima/dopo:** il tecnico audio chiede di sostituire il ruggito; il game designer chiede di portare la vita da 100 a 120. Se entrambi devono modificare lo stesso grande componente, le responsabilità sono intrecciate. Separandole, il cambio del suono non richiede di toccare le regole della vita.

### O — Open/Closed: prevedere punti di estensione

> Un componente dovrebbe poter essere esteso senza dover riscrivere continuamente il suo nucleo.

Un personaggio usa un contratto generale di attacco. Possiamo introdurre l'attacco di ghiaccio aggiungendo una nuova implementazione, senza riscrivere il funzionamento generale del personaggio.

**Non significa:** nessun file deve mai essere modificato. Il nuovo comportamento dovrà essere creato e selezionato da qualche parte. Si cerca di proteggere i componenti stabili da modifiche ripetitive.

**Esempio prima/dopo:** inizialmente il personaggio contiene un elenco di casi: «se morso, 10; se fuoco, 20». Per il ghiaccio dobbiamo modificare quell'elenco. Con un contratto di attacco, aggiungiamo il comportamento ghiaccio da 15 punti e lo rendiamo selezionabile: il personaggio continua a chiedere soltanto «quanto danno produci?».

### L — Liskov Substitution: mantenere le promesse

> Un oggetto più specifico deve poter sostituire quello generale senza violarne il contratto.

Se ogni attacco promette di restituire una quantità di danno non negativa, un nuovo attacco deve mantenere questa promessa. Non dovrebbe, senza cambiare il contratto, restituire un danno negativo o modificare segretamente altri personaggi.

Il compilatore controlla tipi e firme, ma non tutte le aspettative sul comportamento.

**Collegamento con l'ereditarietà:** una relazione apparentemente corretta nei nomi non garantisce una sostituzione corretta nei comportamenti.

**Esempio con numeri:** il bersaglio ha 100 punti vita. Un attacco da 20 lo porta a 80; uno da 15 lo porta a 85. Se un «attacco curativo» restituisce −20, lo stesso calcolo porta la vita a 120: viola il contratto di danno non negativo. La cura è lecita nel gioco, ma va modellata con un contratto appropriato, non introdotta di nascosto.

**Analogia:** se prenotiamo un mezzo che promette di trasportare quattro persone, un modello più specifico con due soli posti non mantiene la promessa, anche se appartiene alla stessa marca.

### I — Interface Segregation: contratti mirati

> Non obbligare un componente a dipendere da operazioni che non gli servono.

Un contratto per gli attacchi non dovrebbe obbligare ogni implementazione anche a volare, riprodurre musica e salvare la partita.

Interfacce mirate aiutano chi usa e chi realizza il contratto a capire quali responsabilità sono effettivamente richieste.

**Non significa:** creare sempre un'interfaccia diversa per ciascun metodo. Il contratto deve restare coerente e utile.

**Esempio prima/dopo:** un contratto «Creatura» impone attaccare, volare e nuotare. Per il lupo siamo costretti a inventare un volo che non funziona o segnala un errore. Contratti distinti per combattimento, volo e nuoto permettono al lupo di offrire soltanto capacità reali e al drago di combinare quelle pertinenti.

### D — Dependency Inversion: dipendere dalle astrazioni

> La logica principale dovrebbe dipendere da contratti stabili, non essere legata a ogni dettaglio concreto.

Il personaggio conosce l'idea generale di attacco, non tutti gli attacchi possibili. Anche gli attacchi concreti rispettano quel contratto.

Questo permette di sostituire un comportamento e di usare un componente semplice durante le verifiche.

Passare una dipendenza dall'esterno può aiutare ad applicare il principio, ma **dependency injection** e **dependency inversion** non sono la stessa cosa: la prima è una tecnica, la seconda riguarda la direzione delle dipendenze nel progetto.

**Esempio prima/dopo:** se il personaggio costruisce sempre un attacco di fuoco al proprio interno, scegliere il ghiaccio richiede di modificarlo. Se riceve un oggetto che rispetta il contratto di attacco, può lavorare con entrambi. Durante una verifica possiamo fornirgli un attacco di prova che restituisce sempre 10, senza attivare animazioni o audio.

**Analogia:** una lampada dipende da uno standard di alimentazione, non dall'identità della centrale elettrica. Lo standard consente di cambiare dettagli senza riprogettare la lampada.

### Le cinque domande, senza acronimi

1. Questo componente contiene responsabilità che cambiano per motivi diversi?
2. Ogni nuova variante ci obbliga a riscrivere il nucleo?
3. Le implementazioni mantengono le promesse del tipo generale?
4. I contratti chiedono operazioni inutili?
5. La logica principale è troppo legata ai dettagli?

> **Limite importante:** SOLID può aiutare la modificabilità e la testabilità. Non garantisce automaticamente sicurezza, prestazioni o correttezza.

## 🧩 4. Design pattern: soluzioni ricorrenti con un nome

Un **design pattern** descrive una soluzione riconoscibile a un problema che si presenta spesso. Specifica il contesto, i ruoli e i compromessi della soluzione.

Non è:

- una libreria da scaricare;
- un algoritmo pronto da copiare;
- una regola da applicare a ogni programma.

Il suo nome offre un vocabolario condiviso: «usiamo Strategy» può comunicare un'idea di progetto senza spiegare subito ogni dettaglio.

### Strategy: comportamenti intercambiabili

**Problema:** un personaggio può cambiare modo di attaccare.

**Soluzione:** rappresentare i diversi comportamenti con componenti che rispettano lo stesso contratto. Il personaggio usa il comportamento scelto senza conoscere ogni variante.

Il personaggio rimane lo stesso mentre cambia l'attacco. È un esempio di **composizione**: il personaggio *ha un* comportamento.

**Costo:** introdurre componenti separati può essere inutile se il comportamento è unico e stabile.

**Scena concreta:** il drago ha 100 punti vita e usa il morso da 10. Raccoglie la gemma: sostituiamo il comportamento con il fuoco da 20. Non creiamo un altro drago e non perdiamo la sua vita corrente. Il **contesto** è il drago, la **strategia** è il contratto di attacco e le **strategie concrete** sono morso e fuoco.

**Altro contesto:** un navigatore può scegliere percorso più veloce o percorso senza pedaggi. Cambia la politica di calcolo, non l'identità del navigatore.

### Observer: avvisare chi è interessato

**Problema:** quando il personaggio perde vita, devono aggiornarsi la barra della salute, il suono e il sistema degli obiettivi.

**Soluzione:** gli interessati si iscrivono a un evento; quando l'evento avviene, ricevono una notifica.

**Costo:** il flusso delle notifiche può diventare difficile da seguire; bisogna gestire iscrizioni, ordine ed eventuali effetti a catena.

**Scena concreta:** il drago passa da 100 a 80 punti vita e viene emesso l'evento «vita cambiata». La barra mostra 80, l'audio riproduce un gemito e il registro annota il colpo. In seguito aggiungiamo un indicatore lampeggiante: lo iscriviamo all'evento, invece di inserire un'altra chiamata nelle regole della vita.

**Analogia:** gli iscritti a una newsletter ricevono una notizia; chi non è iscritto non viene avvisato. L'iscrizione non implica che tutti i destinatari reagiscano allo stesso modo.

### Factory: organizzare la creazione

**Problema:** creare un personaggio può richiedere di scegliere attacco, aspetto e altri componenti.

**Soluzione:** affidare la creazione a un punto dedicato, invece di distribuire le stesse decisioni in molti punti.

“Factory” è un termine generale: Factory Method e Abstract Factory sono pattern specifici, non nomi equivalenti per qualsiasi funzione che crea oggetti.

**Costo:** aggiungere un livello di creazione può essere superfluo per oggetti semplicissimi.

**Scena concreta:** tre livelli del gioco creano draghi. Ogni drago deve ricevere 100 punti vita, un attacco iniziale e una risorsa audio. Se ciascun livello ripete queste decisioni, uno potrebbe dimenticare l'audio. Un punto di creazione dedicato prepara il personaggio con i componenti richiesti. Questa è l'idea generale di factory, non necessariamente l'applicazione di uno specifico pattern del catalogo.

### Le famiglie

| Famiglia | Tema | Esempi |
|---|---|---|
| Creazionali | Creazione degli oggetti | Factory Method, Abstract Factory |
| Strutturali | Collegamento e organizzazione dei componenti | Adapter, Decorator |
| Comportamentali | Collaborazione e distribuzione dei comportamenti | Strategy, Observer |

**Principio e pattern sono diversi:** Open/Closed indica un obiettivo di progettazione; Strategy è una possibile struttura che può aiutarci a raggiungerlo.

Quando usiamo una soluzione soltanto perché la conosciamo, anche se il problema non la richiede, rischiamo un **anti-pattern**: un'abitudine ricorrente che peggiora il progetto.

## 🔁 5. Agile: imparare mentre si costruisce

Spesso gli utenti capiscono meglio ciò che desiderano dopo aver provato una prima versione.

Nel gioco, il progettista può chiedere un attacco potente e poi scoprire che rende la partita noiosa. Il requisito non cambia necessariamente per disorganizzazione: cambia anche perché abbiamo imparato qualcosa.

**Agile** indica un insieme di valori e principi per sviluppare software attraverso collaborazione, feedback e adattamento. Non è un singolo procedimento.

### Il Manifesto Agile

Nel 2001 diciassette sviluppatori formularono il Manifesto per lo sviluppo Agile del software. Esso dà maggiore importanza a:

- individui e interazioni rispetto a processi e strumenti;
- software funzionante rispetto a documentazione esaustiva;
- collaborazione con il cliente rispetto a negoziazione dei contratti;
- risposta al cambiamento rispetto ad adesione al piano.

Gli elementi a destra conservano valore. Agile **non** significa niente documentazione, niente contratti o niente pianificazione.

### Iterativo e incrementale

**Iterativo:** lavoriamo per cicli, riesaminando e migliorando la soluzione.

**Incrementale:** aggiungiamo parti utilizzabili del prodotto.

Nel gioco:

1. rendiamo giocabile un personaggio;
2. osserviamo una prova;
3. introduciamo un attacco alternativo;
4. raccogliamo feedback sul bilanciamento;
5. scegliamo la modifica successiva.

È diverso dal costruire tutto prima di mostrare qualunque risultato.

### Esempio: il fuoco funziona, ma il gioco è noioso

**Richiesta iniziale:** «Come giocatore, voglio un attacco di fuoco per affrontare nemici più resistenti.»

| Passo | Risultato e apprendimento |
|---|---|
| Primo incremento | Morso da 10 e un nemico: una piccola scena già giocabile |
| Secondo incremento | Fuoco da 20: nuova funzionalità utilizzabile |
| Prova con i giocatori | Tutti scelgono sempre il fuoco; il morso è diventato inutile |
| Iterazione | Il fuoco continua a infliggere 20, ma richiede una risorsa limitata |
| Nuova prova | Osserviamo se ora esiste una scelta interessante |

**Incrementare** significa aggiungere il fuoco. **Iterare** significa rivederne il funzionamento dopo averlo provato. Dire «abbiamo rispettato la richiesta iniziale» non basta se il risultato non risolve il bisogno.

I valori Agile diventano concreti: parliamo con i giocatori, mostriamo una versione funzionante, aggiorniamo il piano e documentiamo la nuova regola.

### XP, Scrum e Kanban

| Approccio | Accento principale | Concetti da riconoscere |
|---|---|---|
| **Extreme Programming — XP** | Pratiche di sviluppo e feedback | Pair programming, test-first, refactoring, integrazione continua |
| **Scrum** | Organizzazione empirica del lavoro | Sprint, Product Owner, Scrum Master, Developers; planning, daily, review, retrospettiva |
| **Kanban** | Gestione del flusso di lavoro | Visualizzare il lavoro, limitare attività in corso, migliorare il flusso |

XP è una metodologia agile. Scrum è un framework; Kanban gestisce il flusso. Possono essere combinati con attenzione: non sono sinonimi di Agile.

In XP:

- **pair programming:** due persone collaborano, alternando chi scrive e chi osserva il quadro generale;
- **test-first e TDD:** una verifica guida il comportamento da realizzare;
- **refactoring:** si migliora la struttura senza cambiare il comportamento osservabile;
- **integrazione continua:** le modifiche vengono integrate e verificate frequentemente.

Scrum organizza il lavoro in sprint di durata fissa, al massimo un mese. Kanban aiuta a evitare che troppe attività vengano iniziate contemporaneamente; una semplice lavagna non esaurisce l'intero metodo.

### Lo stesso cambiamento visto con XP, Scrum e Kanban

- **XP — come sviluppiamo:** prima concordiamo una verifica: «con una carica disponibile il fuoco infligge 20 e consuma la carica». Due persone collaborano alla modifica; le verifiche controllano anche che il morso continui a infliggere 10. Poi migliorano la struttura senza cambiare i risultati.
- **Scrum — come organizziamo il ciclo:** in uno sprint di una settimana il gruppo concorda l'obiettivo di rendere significativa la scelta fra gli attacchi. Alla review mostra il risultato e raccoglie feedback; alla retrospettiva esamina come ha lavorato.
- **Kanban — come gestiamo il flusso:** le attività passano da «da fare» a «in corso», «da verificare» e «fatto». Se il limite della colonna «in corso» è due e ci sono già due attività, aiutiamo a finirle prima di iniziarne una terza.

> **Domanda:** una riunione quotidiana, da sola, dimostra che il gruppo lavora in modo Agile? No: contano anche prodotto utilizzabile, feedback e adattamento.

### Che cosa Agile non può fare

Agile non rende automaticamente sicuro il software, non elimina gli errori e non giustifica rilasci senza verifica.

Un cambiamento urgente richiede ancora valutazione del rischio, test e coordinamento. «Dobbiamo essere veloci» non significa «possiamo ignorare la qualità».

## ☕ 6. Caso reale: Log4j e Log4Shell

### Prima distinzione: libreria e vulnerabilità

**Log4j 2** è una libreria Java di **logging**. Registra eventi del programma: avvii, operazioni significative, avvisi ed errori.

**Log4Shell** è il nome di una vulnerabilità divulgata nel dicembre 2021, identificata come **CVE-2021-44228**, che riguardava determinate versioni di Log4j 2.

Non sono la stessa cosa. Utilizzare Java non significa automaticamente utilizzare Log4j; utilizzare Log4j non significa automaticamente essere vulnerabili a questa CVE.

### Perché registrare eventi?

Se un server si blocca alle tre di notte, lo sviluppatore non può osservare ciò che è successo direttamente. I log aiutano a ricostruire gli eventi.

Una libreria di logging può offrire:

- livelli di gravità;
- formati uniformi;
- destinazioni diverse;
- regole per selezionare quali messaggi registrare.

Anche i log richiedono attenzione: registrare password o dati personali non necessari può creare un problema di riservatezza.

**Esempio di lettura, non di programmazione:** nel registro troviamo «09:12 — server avviato», «09:14 — giocatore entrato», «09:16 — errore nel caricamento della mappa». Questo non prova da solo la causa del guasto, ma aiuta a ricostruire la sequenza e a individuare che cosa investigare.

### Che cosa accadde?

In versioni vulnerabili, particolari espressioni contenute nei messaggi potevano attivare funzionalità di ricerca esterna attraverso **JNDI**, un meccanismo Java per accedere a servizi di nomi e directory.

In condizioni sfruttabili, un attaccante capace di controllare dati registrati poteva arrivare a far eseguire codice sul sistema.

Il passaggio decisivo era questo:

> Un testo che doveva essere registrato come dato poteva essere interpretato in modo da produrre effetti esterni.

Non era semplicemente un messaggio lungo o un errore della chat. Il rischio dipendeva dal comportamento della libreria e dall'ambiente.

L'episodio interessò numerosi sistemi; anche Minecraft Java Edition fu coinvolto nell'emergenza. Una funzionalità apparentemente secondaria poteva quindi compromettere un'applicazione molto più grande.

### Una scena per capire il confine fra dati e istruzioni

Immaginiamo un server che registra i messaggi inviati dagli utenti. Questa scena illustra il meccanismo generale, non ricostruisce il codice di uno specifico prodotto.

1. Un utente invia «ciao».
2. Il server chiede alla libreria di registrarlo: il testo dovrebbe rimanere un dato.
3. Un utente invia invece un testo contenente una particolare espressione, qui non riportata.
4. In una configurazione vulnerabile, la libreria può interpretare l'espressione come richiesta di lookup esterno, invece di trattarla come semplice testo.
5. In condizioni sfruttabili, questa catena può consentire esecuzione di codice.

**Analogia:** chiediamo a un archivista di conservare un foglio. Il foglio contiene «telefona a questo numero e segui le istruzioni». Archiviare quella frase è diverso dall'obbedirle. L'analogia chiarisce il confine di fiducia; non descrive i dettagli tecnici di JNDI.

> **Domanda:** il testo di un utente dovrebbe poter decidere quali servizi esterni contatta una funzione di logging?

### Quali componenti erano coinvolti?

La vulnerabilità riguardava **log4j-core** nelle versioni interessate. La sola presenza di **log4j-api** non implica automaticamente vulnerabilità a Log4Shell.

Servono informazioni su versioni, configurazione e componenti effettivamente distribuiti. Il nome generico della libreria non basta a valutare il rischio.

Nel 2021 furono pubblicate più correzioni e individuati problemi ulteriori. Un numero di versione citato in una notizia storica non è una raccomandazione valida per sempre: oggi vanno consultati gli avvisi aggiornati e le versioni supportate.

### Perché questo è un caso di ingegneria del software?

La risposta non consisteva soltanto nel cambiare una riga:

1. **Inventario:** dove è presente il componente, anche come dipendenza transitiva?
2. **Valutazione:** quali sistemi e versioni sono interessati?
3. **Correzione:** quali aggiornamenti o misure sono appropriati?
4. **Verifica:** il programma continua a funzionare dopo la modifica?
5. **Rilascio:** la correzione è arrivata ai sistemi realmente in uso?
6. **Controllo:** ci sono segnali di compromissione da investigare?

Una correzione non annulla automaticamente un'intrusione già avvenuta.

**Esempio di gestione:** il gruppo aggiorna la libreria nel progetto, ma un vecchio server continua a eseguire il pacchetto precedente. Il sorgente è stato corretto; quel server no. Bisogna verificare ciò che è realmente distribuito, non soltanto ciò che compare sul computer degli sviluppatori.

### Il collegamento con gli altri argomenti

| Argomento | Che cosa ci insegna il caso |
|---|---|
| Librerie | Il riuso richiede conoscenza dei componenti e delle dipendenze |
| SOLID | Separare responsabilità può facilitare modifiche, ma non impedisce automaticamente una vulnerabilità |
| Design pattern | Un buon schema di progetto non sostituisce la verifica dei componenti |
| XP e test | Le verifiche aiutano a evitare regressioni durante gli aggiornamenti, ma i test funzionali non coprono ogni attacco |
| Agile | Si possono cambiare priorità e coordinare incrementi urgenti, senza rinunciare alla qualità |
| Manutenzione | La responsabilità continua dopo la prima consegna |

> **Lezione centrale:** non basta conoscere il codice che abbiamo scritto. Dobbiamo conoscere anche il software che abbiamo incluso.

Per raccontare il caso non occorre installare versioni vulnerabili né eseguire un attacco.

## 🧠 7. La mappa finale

| Concetto | Domanda |
|---|---|
| Ingegneria del software | Come governiamo l'intero ciclo di vita? |
| Libreria | Quali funzionalità possiamo riutilizzare? |
| API | Quale contratto offre il componente? |
| SOLID | Come valutiamo responsabilità e dipendenze? |
| Design pattern | Esiste una soluzione ricorrente adatta al problema? |
| Agile | Come collaboriamo e impariamo dal feedback? |
| Log4Shell | Conosciamo e manteniamo i componenti esterni? |

Una **libreria** è un componente concreto. Un **principio** orienta le decisioni. Un **pattern** descrive una struttura ricorrente. Un **approccio Agile** organizza collaborazione e adattamento.

Sono strumenti diversi che possono lavorare insieme. Nessuno è una garanzia automatica di buon software.

## 🗣️ 8. Domande per la discussione

1. Perché usare una libreria non significa liberarsi di ogni responsabilità?
2. Che differenza c'è fra API e implementazione?
3. Una libreria può essere presente anche se non l'abbiamo scelta direttamente?
4. Single Responsibility significa «un solo metodo per classe»?
5. Qual è la differenza fra Open/Closed e Strategy?
6. Perché rispettare una firma non basta a rispettare un contratto?
7. Quando un design pattern può diventare complessità inutile?
8. Agile significa non pianificare?
9. Qual è la differenza fra Log4j e Log4Shell?
10. Un programma che supera tutti i test funzionali è necessariamente sicuro?

### Biglietto d'uscita

In tre brevi frasi:

- spiega una responsabilità di chi usa librerie;
- distingui principio SOLID e design pattern;
- indica che cosa insegna Log4Shell sul software già distribuito.

## ⏱️ Regia per una lezione di sessanta minuti

| Minuti | Argomento | Coinvolgimento della classe |
|---:|---|---|
| 0–5 | Ingegneria del software e ponte con l'OOP | «Un programma funzionante può essere progettato male?» |
| 5–15 | Librerie, API e dipendenze | Individuare componenti esterni in un videogioco |
| 15–29 | SOLID | Discutere le cinque domande sul personaggio |
| 29–39 | Design pattern | Riconoscere Strategy, Observer e creazione centralizzata |
| 39–49 | Agile, XP, Scrum e Kanban | Ragionare sul feedback dei giocatori |
| 49–57 | Caso Log4Shell | Distinguere dato, interpretazione e responsabilità delle dipendenze |
| 57–60 | Riepilogo | Biglietto d'uscita |

**Priorità:** approfondire S, O e D; presentare L e I in modo essenziale. Per i pattern sviluppare Strategy e raccontare brevemente gli altri. Su Scrum e Kanban limitarsi alle differenze di scopo.

La dispensa è anche materiale di consultazione: non è necessario leggere ogni paragrafo durante l'ora.

Per ogni concetto scegliere un solo esempio e chiedere alla classe di prevedere il problema prima di mostrare la soluzione. Le analogie e gli esempi alternativi sono riserve per chiarire, non contenuti aggiuntivi da leggere tutti.

## 📚 Fonti e approfondimenti

- [Apache Log4j](https://logging.apache.org/log4j/2.x/): documentazione della libreria.
- [Apache Logging — sicurezza](https://logging.apache.org/security.html): avvisi e indicazioni aggiornate.
- [GitHub Advisory — CVE-2021-44228](https://github.com/advisories/GHSA-jfh8-c2jp-5v3q): dettagli del componente coinvolto e cronologia delle prime correzioni; le indicazioni storiche non sostituiscono quelle attuali.
- [Minecraft — comunicazione sulla vulnerabilità Java Edition](https://www.minecraft.net/en-us/article/important-message--security-vulnerability-java-edition): comunicazione storica del dicembre 2021.
- [Manifesto Agile in italiano](https://agilemanifesto.org/iso/it/manifesto.html) e [dodici principi](https://agilemanifesto.org/iso/it/principles.html).
- [Scrum Guide](https://scrumguides.org/): definizione del framework.
- [Dispense di ingegneria del software](../Ingegneria%20del%20software/): approfondimenti su interfacce, UML, SOLID, pattern, XP e Agile.
- [Ingegneria del software e casi di studio](Ingegneria%20del%20software%20e%20casi%20di%20studio.md): percorso alternativo con codice e improvvisatore musicale.
