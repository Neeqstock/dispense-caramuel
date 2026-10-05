# VS Code: trucchi, debug e Live Share

Visual Studio Code è un editor che può diventare un ambiente di sviluppo grazie alle estensioni. Non serve conoscere ogni pulsante: bastano pochi strumenti per orientarsi nel progetto, capire gli errori e osservare il programma mentre gira.

## Prima di iniziare con Java

Apri in VS Code **la cartella del progetto**, non soltanto un file `.java`. In questo modo l'editor vede insieme sorgenti e cartelle collegate. Per lavorare con Java servono un JDK e l'estensione **Extension Pack for Java**. Se VS Code mostra un invito a installare strumenti mancanti, controlla che si tratti dell'estensione ufficiale e segui le istruzioni.

La barra laterale **Explorer** mostra i file del progetto. Clicca un file per aprirlo; il nome appare in una scheda in alto. Chiudere una scheda non cancella il file: lo puoi riaprire dall'Explorer o cercandolo per nome.

## Comandi e scorciatoie utili

La Tavolozza comandi è una ricerca per azioni: premi `Ctrl+Shift+P` e scrivi che cosa vuoi fare. È spesso più veloce che cercare il comando nei menu. I nomi dei comandi possono essere in inglese anche quando l'interfaccia è tradotta.

| Tasti su Windows | Uso pratico |
|---|---|
| `Ctrl+P` | Trovare e aprire un file per nome |
| `Ctrl+Shift+P` | Cercare e avviare un comando |
| `Ctrl+Shift+F` | Cercare testo in tutti i file del progetto |
| `Ctrl+S` | Salvare il file corrente |
| `Ctrl` + tasto backtick (`) | Aprire o chiudere il terminale integrato |
| `F2` su un nome Java riconosciuto | Rinominare il simbolo e i suoi usi collegati |
| `Shift+Alt+F` | Formattare il file, se è disponibile un formatter |
| `F9` | Aggiungere o rimuovere un breakpoint sulla riga corrente |
| `F5` | Avviare o continuare il debug |

Un **simbolo** è un elemento del programma riconosciuto dall'editor, per esempio il nome di una classe o di un metodo. La rinomina con `F2` aggiorna i riferimenti collegati; una ricerca e sostituzione testuale, invece, può cambiare anche parole che non c'entrano.

## Leggere gli indizi dell'editor

La scheda **Problems** raccoglie errori e avvisi rilevati nei file. Se qualcosa è sottolineato, passa il puntatore sul testo o apri Problems: il messaggio e il numero di riga sono indizi da verificare. Una sottolineatura rossa non spiega sempre da sola la causa; a volte il problema è in un altro file o nella configurazione del progetto.

Se una classe Java non viene riconosciuta o non compare il comando per eseguire il programma, controlla nell'ordine:

1. di aver aperto la cartella del progetto;
2. che il JDK sia installato e individuato dall'estensione Java;
3. che l'Extension Pack for Java sia installato e attivo;
4. che il file contenga una classe avviabile, per esempio con un metodo `main`.

## Debug: fermare il programma per capire

Stampare valori con `System.out.println` è utile, ma quando il programma fa qualcosa di inatteso puoi fermarlo in un punto preciso. Questo è il **debug**.

1. Clicca accanto al numero di una riga eseguibile, oppure posizionati sulla riga e premi `F9`: compare un breakpoint.
2. Avvia il debug con `F5` e scegli la configurazione proposta, se viene richiesta.
3. Quando il programma raggiunge il breakpoint, si ferma. Osserva le variabili nel pannello **Run and Debug** o passando il puntatore sui nomi.
4. Avanza un'istruzione alla volta con i controlli di debug. Puoi così vedere come cambiano i valori e in quale ordine vengono chiamati i metodi.
5. Premi `F5` per continuare oppure arresta il debug con il pulsante di stop.

Un breakpoint è particolarmente utile per seguire un riferimento: fermati dopo `Animale b = a;` e confronta i valori osservati; poi modifica un attributo attraverso `b` e verifica che cosa vedi tramite `a`.

## Live Share: lavorare insieme in tempo reale

**Visual Studio Live Share** è un'estensione per collaborare in una sessione. Chi la avvia è l'**host**; chi entra tramite invito è il **guest**. Il guest può seguire il cursore dell'host e, se riceve il permesso di scrittura, modificare i file condivisi.

1. Entrambi installano l'estensione Visual Studio Live Share e accedono con un account supportato.
2. L'host apre il progetto e, dalla Tavolozza comandi (`Ctrl+Shift+P`), esegue `Live Share: Start collaboration session (Share)`.
3. L'host invia il link d'invito soltanto alla persona che deve partecipare.
4. Provate a seguire insieme una riga di codice. Decidete chi guida e chi osserva, poi scambiate i ruoli.
5. Alla fine l'host termina la sessione con `Live Share: Stop collaboration session`.

Live Share non equivale a Git o GitHub:

| Strumento o azione | Che cosa fa |
|---|---|
| Salvare | Aggiorna il file nella cartella del progetto |
| Git commit | Registra una versione nella cronologia locale |
| Git push | Invia commit a un repository remoto |
| Live Share | Permette di collaborare sul progetto durante una sessione |

Durante una sessione, le modifiche dei partecipanti agiscono sui file condivisi dall'host. Live Share non crea da solo una cronologia né pubblica una copia online: prima di chiudere, l'host controlla le modifiche e decide come conservarle.

Condividi il link solo con i partecipanti previsti. L'host deve controllare i permessi e che cosa viene condiviso, inclusi terminali e porte di rete; non mostrare password, token o dati riservati. Se ti basta una revisione, scegli l'accesso in sola lettura quando disponibile.

Per una guida più ampia su commit, repository remoti e lavoro di gruppo, vedi [Collaborazione con Git e Live Share](Collaborazione%20con%20Git%20e%20Live%20Share.md).

## Fonti e guide

- [VS Code: Java in Visual Studio Code](https://code.visualstudio.com/docs/languages/java): configurare il supporto Java e avviare o fare debug di un programma.
- [VS Code: scorciatoie da tastiera per Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf): consultare e cercare le scorciatoie.
- [Microsoft Learn: installare e accedere a Live Share](https://learn.microsoft.com/en-us/visualstudio/liveshare/use/install-live-share-visual-studio-code): preparare Live Share.
- [Microsoft Learn: condividere un progetto e unirsi a una sessione](https://learn.microsoft.com/en-us/visualstudio/liveshare/use/share-project-join-session-visual-studio-code): avviare e raggiungere una sessione.
- [Microsoft Learn: sicurezza di Live Share](https://learn.microsoft.com/en-us/visualstudio/liveshare/reference/security): capire permessi e contenuti condivisi.
