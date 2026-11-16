"""Missione S1 - L'eroe.

Completa le funzioni qui sotto. Non toccare test_eroe.py.
Per sapere che cosa manca:   python -m pytest -q
"""


def saluta(nome):
    """Restituisce il saluto per l'eroe:   Benvenuta, Aria!"""
    return ""


def scheda(nome, vita, forza):
    """Restituisce una riga sola:   Aria: vita 100, forza 7"""
    return ""


def meta_forza(forza):
    """Restituisce la metà della forza, con i decimali (usa /)."""
    return 0


def meta_forza_intera(forza):
    """Restituisce la metà della forza, senza decimali (usa //)."""
    return 0


def leggi_vita(testo):
    """Trasforma in numero il testo letto da input: "100" diventa 100."""
    return 0


def tipo(valore):
    """Restituisce il nome del tipo del valore: "int", "str", "float", "bool"."""
    return ""


def main():
    """Il programma vero: chiede i dati e stampa la scheda. Non è testato."""
    nome = input("Come si chiama l'eroe? ")
    vita = leggi_vita(input("Quanti punti vita ha? "))
    forza = leggi_vita(input("Quanta forza ha? "))
    print(saluta(nome))
    print(scheda(nome, vita, forza))
    print("Meta forza:", meta_forza(forza))


if __name__ == "__main__":
    main()