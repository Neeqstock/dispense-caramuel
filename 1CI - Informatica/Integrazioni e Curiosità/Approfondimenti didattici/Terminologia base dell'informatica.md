# Terminologia base dell'informatica

## Hardware vs Software

- Definizione: La distinzione fondamentale tra i componenti fisici, tangibili e strutturali di un sistema informatico (hardware) e l'insieme dei programmi, dei dati e delle istruzioni digitali che ne governano il funzionamento (software).
- Cosa è: L'hardware è la componente fisica (i chip, lo schermo, la tastiera, i cavi); il software sono le istruzioni digitali invisibili che dicono all'hardware cosa fare. Una celebre battuta dell'informatica dice: _"L'hardware è la parte che puoi prendere a calci quando il software non funziona"_.
- Cosa non è: Non sono indipendenti l'uno dall'altro. Non puoi far girare un software moderno su un hardware obsoleto (mancanza di potenza), e un hardware potentissimo senza software è solo un costoso fermacarte.

## Dato vs Informazione

- Definizione: La differenza qualitativa tra un singolo elemento grezzo, isolato e non interpretato (dato) e il risultato della sua elaborazione, strutturazione e contestualizzazione all'interno di un quadro dotato di significato utile (informazione).
- Cosa è: Il dato è un elemento grezzo, privo di contesto (es. il numero `39`). L'informazione è il dato elaborato e inserito in un contesto che gli dà un significato utile (es. _"La temperatura corporea del paziente è 39°C, quindi ha la febbre"_).
- Cosa non è: Non sono sinonimi. Un computer può memorizzare miliardi di dati (numeri, stringhe, byte), ma se non vengono organizzati e interpretati, restano del tutto inutili per gli esseri umani.

## Determinismo

- Definizione: La proprietà di un sistema di calcolo o di un algoritmo per cui, a parità di condizioni iniziali e di dati in ingresso, il processo evolutivo e il risultato finale rimangono sempre identici e perfettamente prevedibili.
- Cosa è: La proprietà per cui, dato un preciso stato iniziale e gli stessi identici input, un sistema produrrà sempre lo stesso identico risultato. Se premi il tasto `A` sulla tastiera in un documento di testo, uscirà sempre una `A`. I computer tradizionali sono macchine matematicamente deterministiche.
- Cosa non è: Casualità o libero arbitrio. Anche quando un videogioco sembra generare un livello "casuale", in realtà sta usando un algoritmo matematico ben preciso (chiamato pseudo-casuale) partendo da un numero di base. Se conosci quel numero, il risultato è prevedibile al 100%.

## Astrazione

- Definizione: Il principio metodologico che consiste nell'isolare le caratteristiche essenziali di un'entità o di un sistema, nascondendone i dettagli implementativi o i livelli di complessità inferiori per facilitarne la gestione e l'utilizzo.
- Cosa è: La creazione di un modello semplificato che nasconde i dettagli complessi. Ti mostra i pulsanti per salvare un file (`Ctrl+S`), ma nasconde il modo in cui i magneti o i transistor del disco rigido modificano la loro carica elettrica per conservare quel dato.
- Cosa non è: Cancellazione dei dettagli. I dettagli tecnici esistono ancora sotto la superficie e continuano a funzionare; sono semplicemente stati "coperti" da uno strato più comodo per non sovraccaricare la mente di chi usa il sistema.

## Metafora

- Definizione: L'adozione visiva o concettuale di elementi ed esperienze derivati dal mondo reale all'interno delle interfacce digitali, concepita per rendere intuitiva l'interazione dell'utente con strutture logiche astratte.
- Cosa è: L'uso di concetti del mondo reale per rendere comprensibili concetti digitali astratti. Pensa alla "Scrivania" (Desktop) del computer, al "Cestino" per buttare i file, alle "Cartelle" per organizzarli o alla "Finestra" per guardare dentro un programma.
- Cosa non è: La realtà fisica del computer. Dentro il tuo computer non ci sono vere cartelle di plastica o scrivanie di legno; ci sono solo indirizzi di memoria RAM e settori di memoria flash. La metafora serve solo al nostro cervello per non impazzire davanti alla pura astrazione matematica.

## Algoritmo

- Definizione: Una sequenza finita, ordinata, univoca e non ambigua di passi logici e istruzioni che definisce con precisione le operazioni necessarie per risolvere un determinato problema o raggiungere un obiettivo.
- Cosa è: Una ricetta di cucina passo-passo. È una sequenza finita, rigida e precisa di istruzioni per ottenere un risultato (es. "Se l'acqua bolle, butta la pasta, aspetta 10 minuti, scolati").
- Cosa non è: Un'intelligenza artificiale magica che pensa da sola. Un algoritmo non ha intuito; se c'è un errore logico nei passi, eseguirà l'errore perfettamente.

## Complessità Computazionale

- Definizione: La branca della teoria della computazione che quantifica lo scalability di un algoritmo, determinando la quantità di risorse hardware (tempo di calcolo ed estensione di memoria) richieste in funzione della dimensione dei dati in ingresso.
- Cosa è: La misura di quanta "fatica" fa un computer all'aumentare dei dati. Ad esempio, cercare un nome in un elenco telefonico ordinato (pagine gialle) richiede pochissimi passaggi rispetto a cercarlo in un elenco totalmente disordinato.
- Cosa non è: La difficoltà del programmatore nello scrivere il codice. Non indica quanto il codice sia "difficile da capire" per un essere umano, ma quante risorse hardware (tempo e memoria) consuma la macchina.

## Automa

- Definizione: Un modello matematico astratto di un sistema formale sequenziale che risiede in un numero finito di stati interni e che transita da uno stato all'altro in risposta a specifici input esterni.
- Cosa è: Un distributore automatico di merendine o un semaforo. È un sistema che si trova in un certo "stato" (es. Luce Rossa) e passa a un altro stato (es. Luce Verde) solo quando riceve un input preciso (es. scade il timer).
- Cosa non è: Un robot umanoide senziente con le sembianze di Terminator. È un modello matematico puro e privo di coscienza.

## Variabile

- Definizione: Un'area di memoria allocata e identificata da un nome simbolico (identificatore), il cui contenuto informativo può essere dinamicamente modificato, sovrascritto o riletto durante l'esecuzione di un programma.
- Cosa è: Una scatola di cartone con un'etichetta sopra (es. scritta "Età"). Dentro la scatola metti un foglietto con il numero `25`. Se l'anno prossimo compi gli anni, cancelli `25` e ci scrivi `26`. La scatola (il nome) resta uguale, il contenuto cambia.
- Cosa non è: Un'equazione matematica da risolvere (come la $x$ in $2x + 5 = 11$). In informatica non devi "trovare" il valore della variabile, sei tu che glielo assegni direttamente.

## Protocollo

- Definizione: Un insieme formalizzato di regole standard, convenzioni e formati di messaggi che stabilisce i criteri e le modalità di sincronizzazione, comunicazione e scambio di informazioni tra sistemi informatici interconnessi.
- Cosa è: Il galateo o il codice diplomatico. È un accordo su come stringersi la mano: ad esempio, nel protocollo del telefono, chi riceve la chiamata dice "Pronto?" e chi chiama risponde, stabilendo la connessione.
- Cosa non è: Un cavo fisico o un programma software. È semplicemente una regola astratta di comportamento a cui i dispositivi scelgono di obbedire per capirsi.

## Sistema Operativo

- Definizione: Il software di sistema di livello base che si interfaccia direttamente con l'hardware del computer, coordinando l'allocazione delle risorse fisiche (CPU, memoria, periferiche) e fornendo un ambiente astratto per l'esecuzione dei software applicativi.
- Cosa è: Il direttore di un albergo (es. Windows, macOS, Linux). Gestisce le stanze (la memoria RAM), decide chi può usare l'ascensore (il processore) e distribuisce le risorse ai clienti (le app come Chrome o Spotify).
- Cosa non è: Il computer fisico (l'hardware) e nemmeno il browser con cui navighi su internet. È lo strato invisibile nel mezzo che fa funzionare tutto.

## Crittografia

- Definizione: La disciplina matematica e ingegneristica volta all'offuscamento intenzionale e reversibile delle informazioni, al fine di garantirne la riservatezza, l'integrità e l'autenticità durante lo storage o il transito su canali insicuri.
- Cosa è: Un linguaggio segreto o un lucchetto digitale. Prende il tuo messaggio (es. "Ciao") e lo mescola usando una formula matematica complessa (es. diventa "Xy9%m") in modo che solo chi possiede la chiave giusta possa leggerlo.
- Cosa non è: Un antivirus. La crittografia protegge la privacy dei tuoi dati mentre viaggiano o sono memorizzati, ma non impedisce a un malware di infettare il tuo sistema.