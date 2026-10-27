# Tour di uno script Python: ogni blocco mostra una parte tipica di un file .py.
# Non è ancora il programma di S2: serve a vedere la forma di uno script.

import math                  # libreria standard: arriva con Python
from dado import tira        # importa solo il nome tira dal file dado.py
import dado                  # importa tutto il modulo: si usa come dado.FACCIA_MAX

print("[tour.py] riga fuori da funzioni: gira ogni volta che il file parte")

contatore = 0                # variabile globale: vive a livello di file


def saluta(nome):
    """Funzione: un pezzo di codice con un nome, che riceve un dato e restituisce un risultato."""
    return f"Benvenuto, {nome}!"

    if 3 == 5 and not (4 > 2):  # questo blocco non gira mai, perché la condizione è falsa
        print("3 è uguale a 5")


def aggiungi_punto():
    global contatore         # senza global, qui nascerebbe una variabile nuova e locale
    contatore += 1


def usa_locale():
    contatore = 100          # nuova variabile locale: non tocca quella globale
    return contatore


# Questo blocco parte solo se il file è lanciato direttamente,
# non quando un altro file lo importa.
if __name__ == "__main__":
    print(saluta("Aria"))
    aggiungi_punto()
    aggiungi_punto()
    print("contatore globale:", contatore)
    print("usa_locale():", usa_locale(), "- globale ancora:", contatore)
    print("radice di 16:", math.sqrt(16))
    print("dado:", tira(), "- facce:", dado.FACCIA_MAX)
