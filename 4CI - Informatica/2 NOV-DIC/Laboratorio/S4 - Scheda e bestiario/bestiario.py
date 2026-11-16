"""Missione S4 - Scheda e bestiario.

Completa le funzioni. Non toccare test_bestiario.py.
Per sapere che cosa manca:   python -m pytest -q
"""


def scheda_nuova(nome, vita=100, forza=7):
    """Restituisce un dizionario con le chiavi "nome", "vita", "forza", "zaino"."""
    return {}


def leggi(scheda, chiave):
    """Restituisce il valore della chiave. Se la chiave non c'è, restituisce None."""
    return None


def scrivi(scheda, chiave, valore):
    """Mette il valore nella chiave, creandola se non esiste."""
    return {}


def aumenta(scheda, chiave, quanto):
    """Aumenta di quanto il valore numerico della chiave."""
    return {}


def chiavi(scheda):
    """Restituisce la lista delle chiavi."""
    return []


def cerca_per_nome(bestiario, nome):
    """Restituisce il dizionario del mostro con quel nome, oppure None."""
    return None


def il_piu_forte(bestiario):
    """Restituisce il nome del mostro con la forza più alta (usa l'attacco)."""
    return ""


def per_nome(bestiario):
    """Trasforma una lista di mostri in un dizionario nome -> mostro."""
    return {}


def main():
    eroe = scheda_nuova("Aria")
    scrivi(eroe, "zaino", ["pozione"])
    aumenta(eroe, "forza", 2)
    print(eroe)
    print(chiavi(eroe))

    bestiario = [
        {"nome": "Goblin", "attacco": 4},
        {"nome": "Drago", "attacco": 30},
    ]
    print(cerca_per_nome(bestiario, "Drago"))
    print(il_piu_forte(bestiario))
    print(per_nome(bestiario))


if __name__ == "__main__":
    main()