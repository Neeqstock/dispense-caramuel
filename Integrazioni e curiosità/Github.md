# Git e GitHub

*Scheda operativa: salvare e condividere il tuo lavoro, con VS Code e pochi clic.*

---

## Indice

1. A cosa serve, in 30 secondi
2. Le parole da conoscere
3. Da fare una volta sola
4. Il tuo primo progetto
5. Il ciclo di tutti i giorni
6. I conflitti: cosa sono e come si risolvono
7. Se qualcosa va storto
8. Esercizio
9. Livello 2: collaborare ai progetti degli altri (fork e pull request)

---

## 1. A cosa serve, in 30 secondi

Hai presente i file chiamati `tema_finale_v2_DEFINITIVO_ok.docx`? Git serve a non farli nascere mai.

**Git** funziona come i salvataggi di un videogioco: puoi salvare in punti precisi (i "checkpoint") e tornare indietro quando vuoi. **GitHub** è il posto online dove tieni una copia dei tuoi salvataggi: un po' come Google Drive, ma pensato per il codice e per lavorare in gruppo.

## 2. Le parole da conoscere

| Parola | Cosa significa davvero |
|---|---|
| **Repository (repo)** | La cartella del tuo progetto **più** la storia di tutti i suoi salvataggi. |
| **Repo locale** | Quella che sta sul tuo computer. |
| **Repo remoto** | La copia online, su GitHub. |
| **Commit** | Un salvataggio con etichetta: una "foto" del progetto in quel momento, con un messaggio che dice cosa hai fatto (es. "Aggiunta pagina contatti"). **Resta sul tuo computer.** |
| **Push** | "Spedisci": manda i tuoi commit da computer a GitHub. |
| **Pull** | "Scarica": porta sul computer i commit che ci sono su GitHub e tu non hai ancora. |
| **Clone** | La prima volta che scarichi da GitHub un progetto intero. |
| **Conflitto** | Due persone hanno cambiato la **stessa riga** dello stesso file. Git non sa chi ha ragione e lo chiede a te. |

> **Commit e push: la differenza.**
> Commit = scrivi la lettera e la chiudi nella busta. Push = la imbuchi.
> Un commit da solo non è ancora su GitHub. Finché non fai push, esiste solo sul tuo computer.

## 3. Da fare una volta sola

1. **Crea l'account.** Vai su github.com → **Sign up**. Scegli uno username che potresti mostrare a un futuro datore di lavoro. Conferma l'e-mail con il codice che ti arriva.
2. **Servono git e VS Code** installati (a scuola sono già pronti; a casa: git-scm.com e code.visualstudio.com).
3. **Dì a git chi sei.** È l'unico momento in cui serve il terminale, ed è solo copia-incolla. In VS Code: menu **Terminal → New Terminal**. Incolla queste due righe, una alla volta, premendo Invio (con i tuoi dati, la stessa e-mail di GitHub):

```
git config --global user.name "Nome Cognome"
git config --global user.email "la-tua-mail@esempio.it"
```

## 4. Il tuo primo progetto

1. **Crea una cartella** normale sul Desktop (es. `mio-primo-repo`). In VS Code: **File → Open Folder** e scegli quella cartella. Se chiede "Trust the authors", rispondi sì.
2. **Crea un file:** icona "New File" → chiamalo `README.md` → scrivi una riga qualsiasi → salva con `Ctrl+S`.
3. **Trasforma la cartella in repo:** clic sull'icona **Source Control** (a sinistra: tre pallini uniti da linee) → **Initialize Repository**. Da adesso git tiene d'occhio la cartella.
4. **Primo commit:** sotto "Changes" vedi il tuo file. Scrivi un messaggio nella casella (es. "Primo commit: aggiunto README") → **Commit**. Se chiede di includere tutti i file, rispondi **Yes**.
5. **Pubblica su GitHub:** clic su **Publish Branch** (o "Publish to GitHub"). La prima volta si apre il browser: accedi e premi **Authorize**. Poi scegli il nome del repo e **Private** o **Public**. Ricarica la pagina su GitHub: il tuo progetto è online.

> **Attenzione a cosa pubblichi.** **Public** = lo può vedere chiunque nel mondo. Non mettere mai password, dati personali o foto di altre persone nei file. Nel dubbio scegli **Private**.

## 5. Il ciclo di tutti i giorni

Impara questo e sai usare il 90% di git.

1. **Prima di iniziare:** clic su **Sync Changes** (le due frecce circolari) per scaricare le novità.
2. **Lavora** sui file e salva.
3. **Commit:** scrivi un messaggio chiaro e premi **Commit**.
4. **Sync Changes** di nuovo: spedisce i tuoi commit (push) e scarica quelli degli altri (pull), tutto in un clic.

> **Regole d'oro**
> - Commit **piccoli e frequenti**, non uno solo a fine progetto.
> - Messaggi che dicono cosa è cambiato: "Corretto calcolo della media", non "modifiche" o "asdf".
> - Il **+** accanto a un file serve a scegliere cosa includere nel commit. Per ora ignoralo: se non lo usi, VS Code include tutto.

## 6. I conflitti: cosa sono e come si risolvono

**L'idea.** Tu e un compagno correggete la stessa frase del tema su due copie diverse: tu scrivi "bello", lui scrive "brutto". Quando unite le copie, chi vince? Git non può saperlo, e ti chiede di scegliere.

**Come succede.** Marco cambia la riga 3 e fa Sync. Tu, senza aver fatto Sync prima, cambi anche tu la riga 3 e fai Sync: conflitto.

> **Un conflitto non è un errore e non hai rotto nulla.** Succede spesso, anche ai professionisti.

### Come lo risolvi (tutto a clic)

1. Nel pannello Source Control compare la sezione **Merge Changes** con i file in conflitto. Clicca il file.
2. Nel file vedi le due versioni evidenziate: **Current Change** (la tua) e **Incoming Change** (quella arrivata da GitHub).
3. Sopra il blocco clicca **Accept Current Change**, **Accept Incoming Change** o **Accept Both Changes**. Oppure cancella tutto e scrivi tu la versione finale.
4. Salva il file, clic sul **+** accanto ad esso, scrivi un messaggio, **Commit**, poi **Sync Changes**.

**Come li eviti:** Sync prima di iniziare a lavorare, commit piccoli, e mettetevi d'accordo su chi tocca quale file.

## 7. Se qualcosa va storto

| Problema | Cosa fare |
|---|---|
| Errore "Please tell me who you are" o "author identity unknown" | Non hai fatto il punto 3 della sezione 3: le due righe `git config`. |
| Non trovo "Publish Branch" | Hai fatto il primo commit? Se no, fallo prima. Controlla anche di avere aperto la cartella del progetto. |
| Il push viene rifiutato ("rejected") | Qualcuno ha spedito prima di te. Premi **Sync Changes** (scarica le novità) e riprova. |
| Il login con GitHub non funziona | Icona **Accounts** (omino, in basso a sinistra) → Sign out → Sign in with GitHub. |
| Ho modificato un file e voglio annullare | Se non hai ancora fatto commit: nel pannello Source Control, clic destro sul file → **Discard Changes**. |
| Non so cosa è successo | Non fare altri clic e chiama l'insegnante. Quasi tutto in git si può recuperare, se non si improvvisa. |

## 8. Esercizio

### Parte 1: da solo

1. Crea un repo con un file `presentazione.txt` (chi sei, cosa ti piace).
2. Fai **almeno tre commit** con messaggi chiari: creazione del file, una modifica, un secondo file.
3. Pubblica su GitHub (Sync Changes) e manda il link al prof.

### Parte 2: in coppia, con conflitto voluto

1. Uno dei due invita l'altro: su GitHub, nel repo → **Settings → Collaborators → Add people**.
2. L'altro clona il repo: **Source Control → Clone Repository** → incolla l'indirizzo del repo.
3. Entrambi modificano **la stessa riga** di `README.md`, salvano e fanno commit. Non fate Sync in mezzo!
4. Il primo fa **Sync Changes**. Poi lo fa il secondo: comparirà il conflitto. Risolvetelo insieme con la procedura della sezione 6.

### Autovalutazione

Ho capito se so spiegare a un compagno, con parole mie: la differenza tra **commit** e **push**, e cosa fare quando compare un **conflitto**.

---

## 9. Livello 2: collaborare ai progetti degli altri (fork e pull request)

### Il problema

Sui repo degli altri **non puoi scrivere**: solo il proprietario (e chi lui invita) può fare push. È normale: altrimenti chiunque potrebbe rovinare il progetto di chiunque.

Ma allora come fanno migliaia di persone a contribuire a progetti come Linux o Firefox? Con **fork** e **pull request**.

### Le parole nuove

| Parola | Cosa significa davvero |
|---|---|
| **Fork** | Una **tua copia personale** del repo di un altro, che vive sul tuo account GitHub. Lì puoi scrivere liberamente. L'originale non viene toccato. |
| **Branch** (ramo) | Una "linea parallela" di salvataggi dentro lo stesso repo. Ci lavori sulla tua modifica senza toccare la versione principale (`main`). |
| **Pull request (PR)** | Una proposta: "Ho fatto questa modifica nella mia copia. Ti va di prenderla nel tuo progetto?". Il proprietario la guarda e decide se accettarla. |

**L'analogia.** Il fork è come fotocopiare un libro della biblioteca: sulla tua copia scrivi quello che vuoi. La pull request è mandare all'autore un biglietto: "Ho corretto un errore a pagina 12, guarda!". Sarà lui a decidere se aggiornare il libro originale.

### Il percorso, passo per passo (tutto a clic)

1. **Fork.** Apri il repo su GitHub. In alto a destra clicca **Fork** → **Create fork**. Ti ritrovi su una pagina identica, ma con il tuo username nell'indirizzo: quella è la tua copia.
2. **Clone.** In VS Code: **Source Control → Clone Repository** → incolla l'indirizzo **del tuo fork** (non dell'originale!) → scegli dove salvarlo → **Open**.
3. **Crea un branch.** In basso a sinistra, nella barra blu, vedi la scritta `main`. Cliccala → **Create new branch...** → dai un nome che dica cosa fai (es. `aggiungi-mio-nome`).
4. **Fai la modifica.** Cambia o aggiungi file, salva, poi **Commit** con un messaggio chiaro come sempre.
5. **Pubblica il branch.** Clicca **Publish Branch**. Ora la tua modifica è sul tuo fork su GitHub.
6. **Apri la pull request.** Vai su GitHub, sulla pagina del tuo fork: compare un banner giallo **Compare & pull request**. Cliccalo, scrivi un titolo e due righe su cosa hai cambiato e perché → **Create pull request**.
7. **Aspetta.** Il proprietario può accettare (**merge**), chiederti modifiche o rifiutare. Se ti chiede modifiche, basta fare altri commit sullo stesso branch e **Sync Changes**: la PR si aggiorna da sola.

> **Un rifiuto non è un fallimento.** Succede spesso e di solito arriva con un commento utile. Anche i professionisti ricevono richieste di modifica sulle loro PR.

### Tenere il tuo fork aggiornato

Se l'originale va avanti, il tuo fork resta indietro. Per allinearlo, senza terminale:

1. Su GitHub, nella pagina del tuo fork, clicca **Sync fork** → **Update branch**.
2. In VS Code, clicca **Sync Changes** per scaricare l'aggiornamento sul tuo computer.

### Regole di buona educazione

- **Leggi il file `README` (e `CONTRIBUTING`, se c'è)** prima di proporre modifiche: spesso il progetto spiega come vuole essere aiutato.
- **Una PR = una cosa sola.** Piccole e chiare vengono accettate più in fretta.
- **Sii gentile nei commenti.** Dall'altra parte c'è una persona, spesso un volontario.

### Esercizio

Il prof crea un repo pubblico con una cartella `partecipanti/`. Tu devi:

1. Fare il **fork** del repo del prof.
2. Clonarlo e creare un **branch** col tuo nome.
3. Aggiungere nella cartella `partecipanti/` un file `cognome.md` con due righe di presentazione.
4. Fare commit, pubblicare il branch e aprire una **pull request**.

Il prof accetterà le PR una alla volta, come farebbe il responsabile di un vero progetto.

### Autovalutazione

So spiegare a un compagno, con parole mie: che differenza c'è tra **fork** e **clone**, e perché per contribuire a un progetto altrui serve una **pull request**.
