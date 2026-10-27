# Progetto dummy S1 - l'eroe

Esempi per la settimana 1 (non è una dispensa: sono file da provare e leggere insieme alla teoria di [Primi passi con Python](../../%28STU%29%204CI%20nov-dic%20S1%20-%20Primi%20passi%20con%20Python.md)).

Requisito: Python 3.10 o superiore.

| File | Che cosa mostra |
| --- | --- |
| `eroe.py` | script con `input`, `print`, variabili, f-string, operatori |
| `tipi.py` | tipi dei valori con `type()`; una variabile che cambia tipo |
| `operatori.py` | `/`, `//`, `%`, `**`, testo ripetuto, confronti |
| `errore.py` | errore voluto: si legge il traceback |
| `tour.py` | forma tipica di uno script: `import`, funzioni, righe fuori da funzioni, `global`, `if __name__ == "__main__"` |
| `dado.py` | modulo importato da `tour.py`: il suo `print` gira all'import |
| `repl.md` | trascrizione di una sessione REPL, con output reale |

Esecuzione dal terminale, dentro la cartella del progetto:

```text
python eroe.py
python tipi.py
python operatori.py
python errore.py
python tour.py
```

Per vedere l'effetto di `import`:

```text
python -c "import tour"
```
