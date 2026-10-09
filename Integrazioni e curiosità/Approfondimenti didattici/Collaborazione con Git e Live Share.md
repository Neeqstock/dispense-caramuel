# Collaborazione con Git e Live Share

> Collaborare su un programma non significa soltanto stare davanti allo stesso schermo. Significa rendere visibile il lavoro, poter tornare a una versione precedente e lasciare agli altri un progetto che riescano a capire.

Questa integrazione introduce Git e GitHub come strumenti per conservare e condividere il lavoro, poi usa Visual Studio Live Share per provare la collaborazione in tempo reale.

## Obiettivi

Al termine, lo studente dovrebbe saper:

- distinguere Git, GitHub e Live Share;
- creare un repository locale, registrare una modifica e pubblicarlo su GitHub;
- invitare un collaboratore e recuperare il suo contributo;
- avviare e chiudere una sessione Live Share in modo consapevole.

## 1. Tre strumenti, tre ruoli

### Git: la cronologia del progetto

Git è un sistema di controllo delle versioni. Registra fotografie successive dei file, chiamate **commit**, ciascuna accompagnata da una descrizione. Se una modifica rompe qualcosa, la cronologia aiuta a capire che cosa è cambiato e a tornare a una versione precedente.

Un commit non viene creato ogni volta che si salva un file: prima si scelgono le modifiche da includere, poi si registra la fotografia con un messaggio chiaro.

Il ciclo essenziale è:

```text
modifico i file -> controllo le modifiche -> preparo quelle da salvare -> creo un commit
```

### GitHub: una copia online condivisa

GitHub ospita repository Git online. Il repository sul computer è **locale**; quello su GitHub è **remoto**. GitHub permette di conservare una copia online, invitare collaboratori e coordinare il lavoro.

- **push:** invia a GitHub i commit locali;
- **pull:** scarica e integra nel repository locale i commit presenti su GitHub;
- **clone:** crea sul proprio computer una copia locale di un repository remoto.

Salvare un file non equivale a fare un commit; fare un commit non equivale a inviarlo su GitHub. Sono tre azioni diverse.

### Live Share: lavorare insieme nello stesso momento

Visual Studio Live Share è un'estensione di VS Code che permette a una persona di condividere una cartella di progetto con altre persone durante una sessione. Chi ospita è l'**host**; chi si collega è un **guest**. I partecipanti possono seguire lo stesso codice e, se l'host lo permette, modificarlo insieme.

Live Share non crea da solo una cronologia Git e non pubblica il progetto su GitHub. Le modifiche dei guest avvengono nella cartella condivisa dell'host: alla fine, l'host può controllarle e registrarle con un commit.

> **Nota sullo strumento:** la documentazione Microsoft indica che Live Share è in modalità manutenzione: le funzioni esistenti restano disponibili, ma non sono previste nuove funzioni. È comunque utile per provare una sessione collaborativa; Git e GitHub restano la base per conservare e condividere le versioni.

## 2. Regole di collaborazione

Prima di condividere un progetto:

- usate un repository **privato** per il laboratorio e invitate solo le persone del gruppo;
- non inserite password, token, dati personali o altri segreti nei file;
- non condividete in pubblico un link Live Share: chi lo riceve può ottenere accesso alla sessione;
- controllate che cosa state condividendo. In Live Share l'host può dare accesso in scrittura, condividere un terminale o una porta di rete: autorizzate solo ciò che serve e non mostrate nel terminale dati riservati;
- usate account personali autorizzati dalla scuola. Non scambiatevi password e non usate un unico account condiviso.

Un repository privato limita l'accesso alle persone invitate, ma non rende opportuno inserirvi informazioni riservate. Le regole della scuola e l'idoneità degli studenti a creare account hanno la precedenza.

## 3. Laboratorio: creare e condividere un repository

**Durata indicativa:** 60-75 minuti  
**Gruppi:** coppie  
**Occorrente:** VS Code, Git installato, accesso a GitHub secondo le regole della scuola. Per la parte finale, estensione Live Share installata su entrambi i computer.

### A. Preparare il repository locale

1. Aprite VS Code e create una cartella nuova chiamata `laboratorio-git-gruppo-nome`.
2. Aprite la cartella con **File > Apri cartella**. Non iniziate dentro un altro repository già esistente.
3. Aprite **Controllo del codice sorgente** dalla barra laterale, oppure premete `Ctrl+Shift+G`.
4. Selezionate **Inizializza repository**. La cartella è ora un repository Git locale; per il momento non è stato caricato nulla online.
5. Create `README.md` e inserite una breve descrizione del progetto, i nomi o gli pseudonimi concordati dal gruppo e un elenco di due idee da sviluppare. Salvate il file.

### B. Registrare il primo commit

1. Tornate a **Controllo del codice sorgente**. `README.md` appare tra le modifiche non ancora tracciate.
2. Selezionate il file per controllare le modifiche. Lo spazio di lavoro mostra ciò che avete fatto, ma il file non è ancora nella cronologia.
3. Premete **+** accanto al file per prepararlo al commit. Questa operazione si chiama **stage**.
4. Scrivete un messaggio breve che descriva la modifica, per esempio `Aggiunge la descrizione iniziale`.
5. Selezionate **Commit**. Ora esiste una prima versione nella cronologia locale.

Se Git chiede nome e indirizzo e-mail, configurateli secondo le indicazioni del docente. Questi dati identificano l'autore nella cronologia dei commit e possono essere visibili quando il progetto viene pubblicato; non sono la password dell'account.

### C. Pubblicare su GitHub

1. Aprite la **Tavolozza comandi** con `Ctrl+Shift+P` e cercate `Publish to GitHub`.
2. Accedete a GitHub quando VS Code lo richiede.
3. Scegliete un nome per il repository e selezionate **Private**.
4. Al termine, aprite il repository su GitHub e controllate che ci siano `README.md` e il commit appena creato.

Da questo momento, i commit successivi restano sul computer finché non vengono inviati con **Push** o **Sincronizza modifiche**.

### D. Invitare il compagno e scambiare una modifica

1. La persona che ha creato il repository lo apre su GitHub e seleziona **Settings > Collaborators** (la voce può apparire sotto **Access**). Seleziona **Add people** e invita il compagno come collaboratore.
2. Il compagno accetta l'invito e copia l'indirizzo del repository.
3. In VS Code apre la Tavolozza comandi, sceglie `Git: Clone`, incolla l'indirizzo e seleziona una cartella in cui salvare la copia.
4. Il compagno crea un file distinto, per esempio `idea-compagno.md`, scrive una proposta, poi fa stage, commit e push.
5. La persona che ha creato il repository seleziona **Pull** o **Sincronizza modifiche** in VS Code. Controlla che il nuovo file sia arrivato sia nella cartella locale sia su GitHub.

Per il primo esercizio, modificate file diversi: riduce la possibilità di sovrapporre il lavoro. In un progetto reale, due persone possono modificare le stesse righe; Git segnala il conflitto e il gruppo deve decidere quale versione mantenere.

### E. Provare Live Share

1. Entrambi installano l'estensione **Visual Studio Live Share** e accedono con un account supportato.
2. L'host apre in VS Code la cartella del progetto e seleziona **Live Share** nella barra di stato. In alternativa, dalla Tavolozza comandi esegue `Live Share: Start collaboration session (Share)`.
3. L'host invia il link d'invito solo al compagno. Il guest apre il link e sceglie di entrare in VS Code. Se richiesto, l'host approva l'accesso.
4. Provate a seguire il cursore dell'altro e a modificare insieme una riga di `README.md`. Prima di digitare, accordatevi su chi guida e chi osserva; poi scambiate i ruoli.
5. L'host controlla le modifiche in **Controllo del codice sorgente**, crea un commit e conclude la sessione con **Stop collaboration session**.

Per una semplice revisione, l'host può avviare una sessione in sola lettura. VS Code può condividere automaticamente il terminale in sola lettura: controllate le impostazioni di Live Share o disattivate la condivisione automatica dei terminali se non serve. Non condividete porte di rete se non servono all'attività.

## 4. Comandi da ricordare

È possibile svolgere il laboratorio dai pulsanti di VS Code. Questi comandi mostrano le operazioni equivalenti:

```bash
git status                  # controlla lo stato dei file
git add README.md            # prepara un file
git commit -m "Descrizione"  # registra una versione locale
git push                    # invia i commit al repository remoto
git pull                    # recupera i commit dal repository remoto
git clone INDIRIZZO          # crea una copia locale
```

## 5. Verifica e riflessione

Ogni coppia mostra al docente:

- il repository privato su GitHub;
- almeno due commit con messaggi comprensibili;
- la modifica inviata dal compagno e recuperata con pull;
- una breve sessione Live Share avviata e poi chiusa.

Domande finali:

1. Qual è la differenza tra salvare, fare commit e fare push?
2. Se il compagno spegne il computer, che cosa resta su GitHub? Che cosa invece non resta automaticamente nella cronologia?
3. In quale momento usereste Live Share? In quale momento vi basta Git e GitHub?
4. Quale rischio si corre se si condivide una cartella o un link con la persona sbagliata?

## Collegamento didattico

Questa integrazione rende visibili alcune pratiche di [Extreme Programming nei laboratori](Extreme%20Programming%20nei%20laboratori.md): pair programming, piccoli rilasci, feedback frequente e responsabilità condivisa. La cronologia dei commit aiuta anche a spiegare che collaborare non significa soltanto dividere il lavoro: significa poter ricostruire chi ha fatto che cosa e perché.

## Fonti e guide

- [GitHub: Quickstart for repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories)
- [VS Code: Quickstart per il controllo del codice sorgente](https://code.visualstudio.com/docs/sourcecontrol/quickstart)
- [Microsoft Learn: installare e accedere a Live Share](https://learn.microsoft.com/en-us/visualstudio/liveshare/use/install-live-share-visual-studio-code)
- [Microsoft Learn: condividere un progetto e unirsi a una sessione](https://learn.microsoft.com/en-us/visualstudio/liveshare/use/share-project-join-session-visual-studio-code)
- [Microsoft Learn: sicurezza di Live Share](https://learn.microsoft.com/en-us/visualstudio/liveshare/reference/security)
