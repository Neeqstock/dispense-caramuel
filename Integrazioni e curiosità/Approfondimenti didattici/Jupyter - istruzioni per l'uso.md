# Jupyter: istruzioni per l'uso

Un **notebook Jupyter** (file `.ipynb`) è un quaderno digitale diviso in **celle**: alcune contengono testo formattato (Markdown), altre contengono codice Python che puoi eseguire una cella alla volta, vedendo subito il risultato sotto.

---

## 1. Come iniziare in VS Code (consigliato)

È il modo più comodo per lavorare nella stessa cartella dei tuoi file `.py`.

1. Apri la cartella del progetto in VS Code e installa l'estensione **Jupyter** (pubblicata da Microsoft), oltre all'estensione **Python**.
2. Crea un nuovo file che finisce con `.ipynb` (es. `prove.ipynb`) oppure apri un notebook già esistente.
3. Aggiungi una cella di codice (`+ Code`), scrivi una riga di Python (es. `print("Ciao!")`) ed eseguila premendo `Shift + Invio` (oppure il pulsante ▶️ a sinistra della cella).
4. **La prima volta**, VS Code ti chiederà in alto a destra **Select Kernel**: scegli il tuo interprete Python. Se ti propone di installare il pacchetto `ipykernel`, accetta (in alternativa, dal terminale lancia `python -m pip install ipykernel`).

---

## 2. Alternative nel browser (senza installare nulla)

Se vuoi fare una prova veloce da casa o sei su un computer senza Python configurato:

- **[Google Colab](https://colab.research.google.com/):** funziona direttamente nel browser, è gratuito e salva i notebook su Google Drive (richiede un account Google).
- **[JupyterLite](https://jupyter.org/try):** gira tutto dentro il browser senza installazioni e senza login. È ottimo per esperimenti rapidi, ma non vede i file salvati sul tuo PC.

---

## 3. Lavorare con le celle

Un notebook alterna due tipi di celle:
- **Code:** codice Python eseguibile. L'ultima espressione di una cella viene mostrata automaticamente anche senza `print()`, ma per stampare più valori conviene usare `print()`.
- **Markdown:** testo per appunti, titoli (`# Titolo`), elenchi e spiegazioni. Quando esegui una cella Markdown, il testo viene formattato; con un doppio click torni a modificarlo.

| Azione | Come si fa in VS Code |
| --- | --- |
| Eseguire la cella e passare alla successiva | `Shift + Invio` (o ▶️) |
| Eseguire la cella e restare lì | `Ctrl + Invio` |
| Aggiungere una cella di codice o testo | Pulsanti `+ Code` / `+ Markdown` |
| Azzerare tutte le variabili | **Restart** (nella barra in alto) |
| Rieseguire tutto da capo in ordine | **Run All** (o **Restart** e poi **Run All**) |

---

## 4. La regola d'oro: attenzione allo stato nascosto

Tutte le celle di un notebook condividono la stessa memoria finché il kernel è acceso. Se esegui le celle in ordine sparso, o esegui più volte una cella che modifica una variabile, il risultato può dipendere da una storia che non si vede più nel codice.

- Se una variabile ha un valore strano o un errore non torna, clicca **Restart** per ripulire la memoria.
- Prima di salvare, condividere o consegnare un notebook, usa sempre **Restart** seguito da **Run All**: se funziona dall'inizio alla fine senza errori, allora funziona davvero.

---

## 5. Problemi comuni e soluzioni rapide

- **VS Code chiede "Select Kernel" e non parte nulla:** clicca su *Select Kernel* in alto a destra e seleziona l'interprete Python installato sul PC.
- **Errore `Running cells requires the 'ipykernel' package`:** apri il terminale in VS Code ed esegui `python -m pip install ipykernel`.
- **Non trova un file `.py` o un modulo della cartella:** assicurati di aver aperto in VS Code la cartella giusta del progetto (non solo il singolo file).
