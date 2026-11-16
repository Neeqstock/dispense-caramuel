"""Missione S2 - Il dado e il combattimento.

Completa le funzioni. Non toccare test_combattimento.py.
Per sapere che cosa manca:   python -m pytest -q
"""

import random


def tira_dado(facce=6):
    """Restituisce un numero intero da 1 a facce, estremi compresi."""
    return 0


def subisci_danno(vita, danno):
    """Restituisce la vita dopo il danno, mai sotto zero."""
    return 0


def cura(vita, punti, vita_massima=100):
    """Restituisce la vita dopo la cura, mai sopra vita_massima."""
    return 0


def e_vivo(vita):
    """Restituisce True se la vita è maggiore di zero."""
    return False


def combatti(eroe, mostro):
    """Fa combattere eroe e mostro finché uno cade.

    eroe e mostro sono dizionari con le chiavi "vita", "forza"/"attacco".
    A ogni turno: l'eroe colpisce con forza + dado; se il mostro è ancora
    vivo, risponde con il suo attacco.
    Restituisce True se vince l'eroe, False altrimenti.
    ATTENZIONE: modifica i dizionari che riceve.
    """
    return False


def conta_vittorie(eroe, mostri):
    """Simula il combattimento contro ogni mostro della lista, uno alla volta.

    Restituisce quanti mostri l'eroe ha sconfitto senza mai morire.
    """
    return 0


def main():
    eroe = {"nome": "Aria", "vita": 100, "forza": 7}
    mostro = {"nome": "Goblin", "vita": 30, "attacco": 4}
    print(f"Tiro: {tira_dado()}")
    print("Vince l'eroe:", combatti(eroe, mostro))
    print(f"Vita rimasta ad Aria: {eroe['vita']}")


if __name__ == "__main__":
    main()