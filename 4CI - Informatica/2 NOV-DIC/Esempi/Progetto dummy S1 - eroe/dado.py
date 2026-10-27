import random

# Gira appena un altro file fa «import dado»: non dentro una funzione.
print("[dado.py] modulo caricato")

FACCIA_MAX = 6               # costante a livello di modulo

def tira():
    """Cacca cacca pipi cacca pipi"""
    return random.randint(1, FACCIA_MAX)
