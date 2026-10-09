# 🎮 Ingegneria del software in un'ora

**4CI · Collegamento al percorso settembre–ottobre · Videogiochi, Log4Shell e razzi**

> **Domanda guida:** come costruiamo un programma che non soltanto funziona oggi, ma può essere capito, modificato e verificato domani?

Programmare non significa soltanto costruire gestionali. Significa anche creare videogiochi, strumenti musicali, simulatori, software scientifico, sistemi di comunicazione e programmi che guidano veicoli spaziali.

In questa lezione useremo un **piccolo videogioco**, poi incontreremo due casi storici reali: **Log4Shell** e **Ariane 5**. Il videogioco è un esempio didattico inventato: non rappresenta il codice interno di Minecraft.

## ⏱️ La rotta: sessanta minuti, non sei lezioni

| Minuti | Tappa | Attività |
|---:|---|---|
| 0–5 | Ingegneria del software | Domanda iniziale e crisi del software |
| 5–13 | OOP nel videogioco | Ripasso di settembre–ottobre; prevedere l'output |
| 13–20 | Contratti e UML | Disegnare classi e relazioni; cambiare comportamento |
| 20–28 | SOLID e design pattern | Applicare S, O e D; riconoscere Strategy |
| 28–35 | Librerie e logging | Scaricare una libreria Java; mostrare un log |
| 35–43 | Log4Shell | Ricostruire il problema e la gestione delle dipendenze |
| 43–48 | Ariane 5 | Discutere riuso, ipotesi e test di integrazione |
| 48–56 | XP e Agile | Un test, un piccolo incremento, una board |
| 56–60 | Riepilogo | Tre domande d'uscita |

**Obiettivo realistico:** riconoscere il ruolo di ciascuno strumento e collegarlo agli altri. Non imparare in un'ora l'intera notazione UML, cinque principi in profondità, un catalogo di pattern e tutti gli eventi Scrum.

**Modalità:** dimostrazione partecipata, adatta anche a una classe in cui non tutti hanno il computer. Il docente scrive; gli studenti prevedono risultati, individuano responsabilità e propongono cambiamenti.

## 🏗️ 1. Che cos'è l'ingegneria del software?

Nel 1968, a Garmisch, una conferenza NATO contribuì a diffondere l'espressione **ingegneria del software**. Il problema era la cosiddetta crisi del software: programmi difficili da completare, costosi da mantenere e poco affidabili.

L'ingegneria del software affronta il ciclo di vita del programma:

```text
Bisogni → requisiti → progetto → codice → test → rilascio → manutenzione
```

Le attività possono essere ripetute e sovrapposte: la freccia non obbliga a un processo rigidamente sequenziale.

Oltre a chiedere «funziona?», dobbiamo chiedere:

- risolve il problema giusto?
- possiamo capire e modificare il codice?
- possiamo lavorarci in più persone?
- come riconosciamo una regressione?
- quali componenti esterni utilizza?
- come lo aggiorniamo dopo il rilascio?

**Requisito funzionale:** il mostro può attaccare. **Requisito non funzionale:** il gioco deve rispondere rapidamente, essere mantenibile e gestire correttamente input non fidati.

> Una bella gerarchia di classi non basta: contano anche requisiti, test, collaborazione, sicurezza e manutenzione.

## 👾 2. Il caso: un mostro che cambia attacco

Prima richiesta:

> Come giocatore, voglio affrontare un mostro che infligge 10 punti di danno.

Poi il game designer cambia idea:

> «Un mostro di fuoco deve infliggere 20 punti. Inoltre voglio poter cambiare il suo attacco durante la partita, quando raccoglie un potenziamento.»

Potremmo aggiungere condizioni a un metodo:

```java
int danno(String tipo) {
    if (tipo.equals("base")) {
        return 10;
    }
    if (tipo.equals("fuoco")) {
        return 20;
    }
    throw new IllegalArgumentException("Attacco sconosciuto");
}
```

Un `if` non è un errore di progettazione. Ma se i comportamenti crescono, cambiano spesso e devono essere intercambiabili, possiamo scegliere un'altra struttura.

### Il ponte con settembre–ottobre

| Concetto già incontrato | Nel videogioco |
|---|---|
| Classe e oggetto | `Mostro` è un modello; `new Mostro(...)` crea un oggetto |
| Stato e comportamento | Nome, vita e attacco corrente; subire danni e attaccare |
| Riferimenti | La variabile `boss` indica un oggetto, non contiene il mostro intero |
| Costruttore e `this` | Preparano un oggetto con uno stato iniziale valido |
| Incapsulamento | La vita è privata; non si può assegnare dall'esterno `vita = -100` |
| Overloading | Si possono offrire costruttori con parametri diversi; qui ne basta uno |
| Ereditarietà e `super` | Un'eventuale sottoclasse riusa il costruttore della superclasse |
| Overriding | Ogni attacco fornisce la propria versione di `danno()` |
| Astrazione e interfaccia | `Attacco` specifica ciò che il mostro può chiedere |
| Polimorfismo | La stessa chiamata produce risultati diversi secondo l'oggetto concreto |
| `ArrayList` | Può contenere più mostri e permettere di scorrerli |

Il caso non forza tutti i concetti nel codice: **usare l'ereditarietà ovunque non è l'obiettivo dell'OOP**. Qui un mostro *ha un* attacco, non *è un* attacco: è composizione.

## 🤝 3. Interfacce: accordarsi per collaborare

Un'interfaccia è un **contratto** tra chi usa una funzionalità e chi la realizza:

```java
interface Attacco {
    int danno();
}
```

Decidiamo anche il significato: `danno()` restituisce un valore non negativo, espresso in punti vita, senza modificare il bersaglio.

Il compilatore controlla firma e tipi. Non verifica da solo che il valore sia non negativo o che il metodo rispetti il significato concordato.

Due persone possono lavorare in parallelo:

- una costruisce `Mostro`, usando `Attacco`;
- l'altra realizza `AttaccoFuoco`, rispettando lo stesso contratto.

Uno **stub** può restituire temporaneamente un danno fisso per consentire di provare il resto. Va riconosciuto come componente provvisorio, non presentato come funzionalità completa.

## 📐 4. UML: discutere il progetto prima del dettaglio

**UML**, *Unified Modeling Language*, è un linguaggio grafico per descrivere sistemi software. Non è Java e non si esegue.

Alla lavagna rappresentiamo:

```text
Mostro
  - nome: String
  - vita: int
  - attacco: Attacco
  + attacca(): int
  + cambiaAttacco(nuovo: Attacco): void

Attacco «interface»
  + danno(): int

AttaccoBase realizza Attacco
AttaccoFuoco realizza Attacco
Mostro contiene un riferimento ad Attacco
```

Questo è un promemoria testuale per il disegno, non un diagramma UML formale.

Nel diagramma delle classi:

- rettangolo con nome, attributi e metodi;
- `+` per pubblico, `-` per privato;
- realizzazione dell'interfaccia: linea tratteggiata e triangolo vuoto verso l'interfaccia;
- ereditarietà: linea continua e triangolo vuoto verso la superclasse;
- associazione: relazione fra oggetti, qui il riferimento del mostro al suo attacco.

**Aggregazione** e **composizione** precisano relazioni tutto–parte; la composizione UML implica un vincolo forte di appartenenza e ciclo di vita. Non mettiamo un rombo pieno soltanto perché esiste un campo Java.

Altri diagrammi: **sequenza** per gli scambi nel tempo, **casi d'uso** per gli obiettivi degli attori. Nell'ora basta il diagramma delle classi.

## 🧱 5. SOLID: cinque domande sul design

| Principio | Domanda | Nel caso |
|---|---|---|
| **S — Single Responsibility** | Quali ragioni diverse possono far cambiare questa classe? | Stato del mostro, formula del danno e registrazione degli eventi non vanno mescolati indiscriminatamente |
| **O — Open/Closed** | Possiamo introdurre una variante senza riscrivere il componente che la usa? | Aggiungiamo `AttaccoGhiaccio` senza modificare `Mostro.attacca()` |
| **L — Liskov Substitution** | Ogni implementazione mantiene le promesse del tipo generale? | Tutti gli attacchi restituiscono un danno non negativo, senza effetti nascosti incompatibili |
| **I — Interface Segregation** | Obblighiamo chi implementa un contratto a fare cose inutili? | `Attacco` non impone anche `vola()` e `salvaPartita()` |
| **D — Dependency Inversion** | Il componente principale dipende dal contratto o da un dettaglio specifico? | `Mostro` dipende da `Attacco`, non direttamente da `AttaccoFuoco` |

**Approfondire nell'ora S, O e D; presentare L e I come controlli sul contratto.**

Open/Closed non significa «non modificare mai nessun file»: qualcuno dovrà scegliere o creare il nuovo attacco. Si evita di modificare il componente stabile per ogni variante.

## 🧩 6. Design pattern: dare un nome alle soluzioni

Un **design pattern** descrive una soluzione ricorrente, i suoi ruoli e i suoi compromessi. Non è una libreria da scaricare.

Il nostro progetto usa **Strategy**:

- contesto: `Mostro`;
- strategia: `Attacco`;
- strategie concrete: `AttaccoBase`, `AttaccoFuoco`.

Il mostro delega un comportamento a un oggetto sostituibile. Separiamo così l'identità del personaggio dalla politica di attacco.

### Codice completo per la dimostrazione

Salvare il blocco in `Main.java`. Non richiede librerie esterne.

```java
public class Main {
    interface Attacco {
        int danno();
    }

    static class AttaccoBase implements Attacco {
        @Override
        public int danno() {
            return 10;
        }
    }

    static class AttaccoFuoco implements Attacco {
        @Override
        public int danno() {
            return 20;
        }
    }

    static class Mostro {
        private final String nome;
        private int vita;
        private Attacco attacco;

        Mostro(String nome, int vita, Attacco attacco) {
            if (nome == null || nome.isBlank()) {
                throw new IllegalArgumentException("Nome obbligatorio");
            }
            if (vita <= 0) {
                throw new IllegalArgumentException("Vita iniziale positiva");
            }
            this.nome = nome;
            this.vita = vita;
            cambiaAttacco(attacco);
        }

        String getNome() {
            return nome;
        }

        int getVita() {
            return vita;
        }

        void subisciDanno(int danno) {
            if (danno < 0) {
                throw new IllegalArgumentException("Danno non negativo");
            }
            vita = Math.max(0, vita - danno);
        }

        void cambiaAttacco(Attacco nuovo) {
            if (nuovo == null) {
                throw new IllegalArgumentException("Attacco obbligatorio");
            }
            attacco = nuovo;
        }

        int attacca() {
            return attacco.danno();
        }
    }

    public static void main(String[] args) {
        Mostro boss = new Mostro("Drago", 100, new AttaccoBase());
        System.out.println(boss.getNome() + ": " + boss.attacca());
        boss.cambiaAttacco(new AttaccoFuoco());
        System.out.println(boss.getNome() + ": " + boss.attacca());
        boss.subisciDanno(200);
        System.out.println("Vita: " + boss.getVita());
    }
}
```

**Prima di eseguire:** il mostro viene ricreato quando cambia attacco?

Output:

```text
Drago: 10
Drago: 20
Vita: 0
```

È lo stesso mostro. Cambia il riferimento al comportamento usato.

### Gli altri pattern, in un minuto

| Pattern | Idea nel videogioco | Famiglia |
|---|---|---|
| Strategy | Cambiare politica di attacco | Comportamentale |
| Observer | Avvisare interfaccia, audio e obiettivi quando accade un evento | Comportamentale |
| Factory | Centralizzare la creazione di personaggi | Creazionale |
| Adapter | Collegare un'API esterna al contratto del nostro gioco | Strutturale |

Le famiglie sono **creazionali**, **strutturali**, **comportamentali**. Singleton controlla l'esistenza di un'unica istanza, ma può introdurre stato globale e rendere difficili i test: non è un ingrediente obbligatorio.

**Anti-pattern:** applicare sempre la stessa soluzione anche quando non serve. Tre classi nuove per eliminare un singolo `if` stabile possono peggiorare il progetto.

## 📦 7. Librerie Java e logging

Un gioco deve permettere di capire che cosa accade anche quando nessuno guarda lo schermo. Un **log** è una registrazione di eventi: avvio, ingresso di un giocatore, errore, operazione importante.

Una libreria di logging offre livelli, formati e destinazioni:

- `DEBUG`: dettagli utili alla diagnosi;
- `INFO`: eventi ordinari significativi;
- `WARN`: situazione anomala da controllare;
- `ERROR`: errore che richiede attenzione.

**Log4j 2** è una libreria Java per il logging. Non è il linguaggio Java, non è un videogioco e non coincide con la vulnerabilità Log4Shell.

### Scaricare e utilizzare una libreria

Per una dimostrazione senza Maven:

1. partire dal [sito ufficiale di Log4j](https://logging.apache.org/log4j/2.x/);
2. scegliere una versione stabile attualmente supportata e compatibile con il JDK;
3. controllare la pagina di sicurezza, non scegliere una versione vecchia perché compare in un tutorial;
4. scaricare i JAR `log4j-api` e `log4j-core` della stessa versione da una fonte ufficiale o da Maven Central;
5. copiarli nella cartella `lib` e aggiungerli a **Referenced Libraries** in VS Code;
6. importare le classi e provare una chiamata.

L'API espone il contratto; `log4j-core` fornisce un'implementazione. Un JAR è un archivio di classi e risorse: importare un nome nel sorgente non scarica la libreria.

Esempio separato, da salvare in `DemoLog.java`:

```java
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class DemoLog {
    private static final Logger LOG = LogManager.getLogger(DemoLog.class);

    public static void main(String[] args) {
        LOG.error("Dimostrazione del livello ERROR: nessun guasto reale.");
    }
}
```

Il messaggio usa `ERROR` perché la configurazione predefinita lo rende visibile; in un'applicazione vera l'avvio normale sarebbe `INFO`, abilitato nella configurazione. Il formato preciso dipende dalla configurazione.

Da PowerShell, nel progetto:

```powershell
javac -cp "lib\*" DemoLog.java
java -cp ".;lib\*" DemoLog
```

Maven e Gradle automatizzano la gestione delle **dipendenze**, comprese quelle **transitive**: librerie richieste da altre librerie. Anche un componente che non abbiamo scelto direttamente può diventare parte del programma.

Non registrare password, token o dati personali non necessari. Un log può aiutare a diagnosticare un problema e contemporaneamente creare un problema di riservatezza.

## 🌍 8. Caso storico: Log4Shell, dicembre 2021

**Fatto:** nel dicembre 2021 fu divulgata una grave vulnerabilità di Log4j 2, identificata come **CVE-2021-44228**, nota come **Log4Shell**.

La funzione di logging, che sembrava un dettaglio secondario, diventò un punto critico per numerosi sistemi. Anche l'ecosistema Minecraft Java Edition fu coinvolto nell'emergenza.

### La catena, senza eseguire un attacco

```text
Input controllato da un utente
        ↓
L'applicazione registra l'input
        ↓
Una versione vulnerabile interpreta particolari espressioni nel messaggio
        ↓
Può essere avviata una ricerca tramite JNDI verso servizi esterni
        ↓
In condizioni sfruttabili, esecuzione di codice sul sistema
```

Il problema non era «un messaggio molto lungo» o «la chat rompe Java». Alcune funzionalità di lookup oltrepassavano il confine fra **registrare dati** e **interpretare dati con effetti esterni**.

La vulnerabilità riguardava `log4j-core` nelle versioni interessate. Avere soltanto `log4j-api` non significa automaticamente essere vulnerabili a questa CVE. Il rischio concreto dipende da componenti, versioni, configurazione e ambiente.

Nel 2021 arrivarono più correzioni e furono individuati problemi ulteriori: **non usiamo oggi “installa 2.15.0” come prescrizione universale**. Occorre seguire gli avvisi aggiornati e usare una versione supportata adeguata all'ambiente.

### Perché è ingegneria del software?

Non basta cambiare una riga. Il gruppo deve:

1. inventariare dove la libreria è usata, anche indirettamente;
2. identificare versioni e componenti realmente distribuiti;
3. applicare gli aggiornamenti appropriati;
4. verificare compatibilità e comportamenti;
5. distribuire il software corretto;
6. controllare i sistemi e indagare eventuali compromissioni pregresse.

Una patch non annulla automaticamente un'intrusione già avvenuta.

**Collegamenti:** dipendenze, confini di fiducia, test di regressione, rilascio, manutenzione e comunicazione. SOLID non è una protezione automatica da questa vulnerabilità; Agile non sostituisce la gestione della sicurezza.

> **Domanda alla classe:** se non abbiamo mai scritto `import Log4j`, come può comunque trovarsi nel nostro programma?

Non scarichiamo versioni vulnerabili e non proviamo payload: per comprendere il caso bastano la catena e gli avvisi pubblici.

## 🚀 9. Caso storico: Ariane 5, 4 giugno 1996

Il primo volo di Ariane 5 fallì circa quaranta secondi dopo l'inizio della sequenza di volo.

L'inchiesta individuò una conversione da un valore in virgola mobile a 64 bit a un intero con segno a 16 bit nel software del sistema di riferimento inerziale. Il valore superò l'intervallo rappresentabile; la conversione non era protetta e il sistema si arrestò.

Il software riusava elementi sviluppati per Ariane 4, ma le condizioni di volo di Ariane 5 erano diverse. Anche il sistema di riserva eseguiva lo stesso software e fallì per lo stesso motivo.

**Lezioni:**

- riusare codice significa verificare anche le sue ipotesi;
- i tipi non sostituiscono la conoscenza degli intervalli ammessi;
- un componente corretto in un contesto può essere inadatto in un altro;
- due copie dello stesso software non eliminano un difetto comune;
- i test devono rappresentare le condizioni del sistema integrato.

**Ponte con 4CI:** come il costruttore deve rifiutare una vita iniziale impossibile, un componente deve dichiarare e controllare le condizioni in cui opera. L'analogia non significa che un setter o SOLID avrebbero, da soli, risolto il caso Ariane.

> **Domanda alla classe:** «Ha funzionato per anni» è una prova sufficiente quando cambiano ambiente e requisiti?

## 🛠️ 10. XP: cambiare il codice in piccoli passi

**Extreme Programming** è una metodologia agile che combina feedback frequente e pratiche tecniche.

| Pratica | Applicazione al gioco |
|---|---|
| User story e piccoli rilasci | Prima il mostro base, poi il potenziamento |
| Pair programming | Driver alla tastiera; navigator controlla e ragiona sul passo successivo |
| TDD | Un test guida il nuovo comportamento |
| Refactoring | Migliorare la struttura conservando il comportamento |
| Integrazione continua | Integrare spesso e verificare automaticamente le modifiche |
| Proprietà collettiva | Il codice è responsabilità del gruppo |
| Ritmo sostenibile | Qualità e concentrazione non richiedono emergenze permanenti |

I valori XP sono **comunicazione, semplicità, feedback, coraggio e rispetto**.

### Un test concreto senza installare altri strumenti

Per l'ora basta questo metodo, aggiunto dentro `Main` e chiamato all'inizio di `main`:

```java
static void verificaPotenziamento() {
    Mostro boss = new Mostro("Drago", 100, new AttaccoBase());
    if (boss.attacca() != 10) {
        throw new AssertionError("Attacco iniziale errato");
    }
    boss.cambiaAttacco(new AttaccoFuoco());
    if (boss.attacca() != 20) {
        throw new AssertionError("Potenziamento errato");
    }
    if (boss.getVita() != 100) {
        throw new AssertionError("Il potenziamento ha cambiato la vita");
    }
}
```

È una verifica automatica minimale, non un sostituto di un framework come JUnit. Un errore interrompe esplicitamente l'esecuzione.

Per mostrare **TDD**, preparare prima la versione senza `AttaccoFuoco`: scrivere la verifica, osservare il fallimento, implementare il comportamento, rieseguire e infine migliorare il codice. Mostrare soltanto il test dopo il codice non dimostra il ciclo test-first.

```text
ROSSO: test che fallisce
VERDE: minimo comportamento corretto
REFACTOR: miglioramento senza cambiare i risultati
```

Il passaggio dagli `if` a Strategy è refactoring soltanto se conserva i comportamenti precedenti. Aggiungere un nuovo attacco è invece un incremento funzionale.

## 🔁 11. Agile: organizzare feedback e lavoro

Il Manifesto Agile, del 2001, valorizza:

- persone e interazioni più di processi e strumenti;
- software funzionante più di documentazione esaustiva;
- collaborazione con il cliente più di negoziazione dei contratti;
- risposta al cambiamento più di adesione al piano.

Gli elementi a destra conservano valore: Agile non significa niente documentazione, niente progetto o niente regole.

**Iterativo:** si riesamina e migliora attraverso cicli. **Incrementale:** si aggiungono parti utilizzabili.

Nel gioco: mostro base → prova con i giocatori → potenziamento → nuova prova. Ogni incremento deve essere verificato; chiedere feedback su qualcosa che funziona è più utile che discutere soltanto una promessa.

### Tre approcci da distinguere

| Approccio | Focus | Parole chiave |
|---|---|---|
| XP | Pratiche di sviluppo e feedback | Pair programming, TDD, refactoring |
| Scrum | Organizzazione empirica del lavoro | Product Owner, Scrum Master, Developers; sprint, planning, daily, review, retrospettiva |
| Kanban | Gestione del flusso | Visualizzare il lavoro, limitare il WIP, migliorare il flusso |

Uno sprint Scrum dura al massimo un mese. Il daily non è un interrogatorio del capo. Una lavagna da sola non equivale all'intero metodo Kanban.

Esempio: limite di **una attività in corso**.

| Da fare | In corso — massimo 1 | Da verificare | Fatto |
|---|---|---|---|
| Attacco ghiaccio | Potenziamento fuoco | Logging | Mostro base |

Una vulnerabilità urgente può cambiare le priorità: si coordina aggiornamento, verifica e rilascio. Non si elimina il collaudo perché «siamo Agile».

## 🧠 12. Tutto insieme

| Livello | Strumenti | Che cosa ci permettono di fare |
|---|---|---|
| Fondamenti | OOP di settembre–ottobre | Modellare stato, comportamento e contratti |
| Comunicazione | Interfacce e UML | Dividere il lavoro e comprendere il progetto |
| Design | SOLID e pattern | Gestire responsabilità e variazioni |
| Implementazione | Java e librerie | Riutilizzare componenti attraverso API |
| Qualità | Test, refactoring, integrazione continua | Scoprire errori e regressioni |
| Processo | XP, Scrum, Kanban, valori Agile | Organizzare collaborazione e feedback |
| Manutenzione | Inventario dipendenze, aggiornamenti, rilascio | Mantenere affidabile il sistema nel tempo |

**Log4Shell:** dobbiamo conoscere ciò che includiamo. **Ariane 5:** dobbiamo conoscere le ipotesi di ciò che riusiamo.

Nessun diagramma, principio o processo garantisce da solo un buon software. Sono strumenti da usare con giudizio.

### Biglietto d'uscita — quattro minuti

1. Il mostro riceve un attacco nuovo: quale classe aggiungiamo e quale metodo non dobbiamo riscrivere?
2. Che cosa insegna Log4Shell sulle librerie indirette?
3. Qual è la differenza fra un principio SOLID, un pattern e una pratica XP?

**Risposte attese:** nuova implementazione di `Attacco`, senza riscrivere `Mostro.attacca()`; le dipendenze transitive vanno inventariate e aggiornate; un principio orienta il design, un pattern descrive una soluzione ricorrente, una pratica XP guida il lavoro quotidiano.

## 📚 Dove approfondire

Le sei dispense di questa cartella sono il dettaglio; questa è la mappa introduttiva:

1. [INT1 — Interfacce Java per collaborare](%28DOC%29%204CI%20INT1%20-%20Interfacce%20Java%20per%20collaborare.md)
2. [INT2 — UML e diagramma delle classi](%28DOC%29%204CI%20INT2%20-%20UML%20e%20diagramma%20delle%20classi.md)
3. [INT3 — Principi SOLID](%28DOC%29%204CI%20INT3%20-%20Principi%20SOLID.md)
4. [INT4 — Design Pattern](%28DOC%29%204CI%20INT4%20-%20Design%20Pattern.md)
5. [INT5 — Extreme Programming](%28DOC%29%204CI%20INT5%20-%20Extreme%20Programming.md)
6. [INT6 — Metodologie di sviluppo Agile](%28DOC%29%204CI%20INT6%20-%20Metodologie%20di%20sviluppo%20Agile.md)

La dispensa [Ingegneria del software e casi di studio](../Approfondimenti%20didattici/Ingegneria%20del%20software%20e%20casi%20di%20studio.md) usa un improvvisatore musicale ed è un percorso alternativo, non un'aggiunta da svolgere nella stessa ora.

### Fonti dei casi e dei concetti

- [Rapporti delle conferenze NATO sul software, 1968 e 1969](https://homepages.cs.ncl.ac.uk/brian.randell/NATO/): contesto storico dell'ingegneria del software.
- [Apache Log4j](https://logging.apache.org/log4j/2.x/) e [Apache Logging — sicurezza](https://logging.apache.org/security.html): documentazione e avvisi da consultare prima della dimostrazione.
- [GitHub Advisory — CVE-2021-44228](https://github.com/advisories/GHSA-jfh8-c2jp-5v3q): componente coinvolto, condizioni e cronologia delle prime correzioni. Le raccomandazioni storiche non sostituiscono gli avvisi attuali.
- [Minecraft — comunicazione sulla vulnerabilità Java Edition](https://www.minecraft.net/en-us/article/important-message--security-vulnerability-java-edition): comunicazione storica del dicembre 2021.
- [Ariane 5 Flight 501 — rapporto della commissione d'inchiesta](https://www-users.cse.umn.edu/~arnold/disasters/ariane5rep.html): copia del rapporto ESA/CNES, in particolare sezioni 2 e 3.
- [Manifesto Agile, versione italiana](https://agilemanifesto.org/iso/it/manifesto.html) e [principi](https://agilemanifesto.org/iso/it/principles.html).
- [Scrum Guide](https://scrumguides.org/): definizione di Scrum e dei suoi elementi.

## Note per il docente: preparazione e tagli

- Preparare `Main.java`, i JAR aggiornati e `DemoLog.java` prima della lezione. Il download è una dimostrazione, non una scommessa sulla rete.
- Usare un JDK compatibile con la versione di Log4j scelta; il codice del gioco richiede almeno Java 11 per `isBlank()`.
- Fare prima la prova audio-visiva del terminale: font grande, log leggibile, output prevedibile.
- Non installare JUnit o configurare Maven da zero nell'ora: citarli e rimandare al laboratorio.
- Proiettare il codice, ma far prevedere l'output prima di avviarlo. Per UML bastano lavagna e pennarello.
- Se manca tempo, tagliare il catalogo dei pattern e i dettagli Scrum, non le domande sui due casi.
- L'attacco ghiaccio, la lista di mostri e l'Observer per l'audio sono sviluppi per una lezione successiva.
- I concetti avanzati sono una panoramica: non trasformarli automaticamente in nuovi requisiti della verifica OOP.
