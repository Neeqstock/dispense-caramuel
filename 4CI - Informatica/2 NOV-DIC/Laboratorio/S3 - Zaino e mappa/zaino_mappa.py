"""Missione S3 - Zaino e mappa.

Completa le funzioni. Non toccare test_zaino_mappa.py.
Per sapere che cosa manca:   python -m pytest -q
"""


def zaino_nuovo():
    """Restituisce una lista vuota. Sembra banale: serve a mostrare che
    una lista si può creare dentro una funzione e restituire."""
    return []


def aggiungi(zaino, oggetto):
    """Aggiunge l'oggetto in fondo allo zaino e restituisce la lista."""
    return []


def togli(zaino, oggetto):
    """Toglie la prima occorrenza dell'oggetto. Se non c'è, non fa nulla."""
    return []


def conta_oggetti(zaino):
    """Restituisce quanti oggetti ci sono nello zaino."""
    return 0


def c_e(zaino, oggetto):
    """Restituisce True se l'oggetto è nello zaino."""
    return False


def valore_totale(prezzi):
    """Somma i prezzi; se la lista è vuota restituisce 0."""
    return 0


def copia(zaino):
    """Restituisce una copia indipendente dello zaino."""
    return []


def mappa_vuota(righe=3, colonne=3):
    """Crea una matrice righe x colonne piena di "." (punto).

    Deve essere una vera matrice: cambiare una cella non deve cambiare
    le altre righe.
    """
    return []


def metti(mappa, riga, colonna, simbolo):
    """Mette il simbolo nella cella indicata e restituisce la mappa."""
    return []


def trova(mappa, simbolo):
    """Restituisce (riga, colonna) del simbolo, oppure None se non c'è."""
    return None


def conta_simboli(mappa, simbolo):
    """Restituisce quante celle contengono il simbolo."""
    return 0


def main():
    zaino = zaino_nuovo()
    aggiungi(zaino, "pozione")
    aggiungi(zaino, "spada")
    print(zaino, conta_oggetti(zaino), c_e(zaino, "spada"))

    mappa = mappa_vuota(5, 5)
    metti(mappa, 0, 0, "E")
    metti(mappa, 4, 4, "U")
    for riga in mappa:
        print("".join(riga))
    print("Eroe in", trova(mappa, "E"))


if __name__ == "__main__":
    main()