"""Missione S5 - Il gioco intero.

Qui non ci sono funzioni da riempire una per una: c'è un gioco da montare
con i pezzi delle settimane scorse. Scrivi tu le funzioni, usando i nomi
che i test si aspettano. Non toccare test_gioco.py.

Per sapere che cosa manca:   python -m pytest -q

Regole del gioco:
- il gioco chiede un comando con input("> ") e risponde;
- comandi: "1" scheda, "2" combatti, "3" bevi pozione, "0" esci;
- ogni comando diverso da questi stampa "Comando sconosciuto.";
- se vince contro l'ultimo mostro stampa "Hai vinto!" e si ferma;
- se perde stampa "Game over." e si ferma.
"""


VITA_MASSIMA = 100


def crea_eroe(nome="Aria"):
    """Dizionario con nome, vita (VITA_MASSIMA), forza 7, zaino con una pozione."""
    return {}


def crea_bestiario():
    """Lista con due mostri: Goblin (vita 10, attacco 1) e Drago (vita 20, attacco 2)."""
    return []


def subisci_danno(vita, danno):
    """Vita dopo il danno, mai sotto zero."""
    return 0


def cura(vita, punti):
    """Vita dopo la cura, mai sopra VITA_MASSIMA."""
    return 0


def mostra_scheda(eroe):
    """Restituisce il testo della scheda, per esempio:
    Aria: vita 100, forza 7, zaino ['pozione']
    """
    return ""


def scegli_mostro(bestiario):
    """Toglie e restituisce il primo mostro della lista."""
    return None


def combatti(eroe, mostro, dado):
    """Un turno di combattimento, con il tiro del dado già passato come numero.

    L'eroe colpisce con forza + dado; se il mostro resta vivo, risponde.
    Restituisce True se il mostro è caduto.
    """
    return False


def bevi_pozione(eroe):
    """Se c'è una pozione nello zaino, la toglie e cura di 30.

    Restituisce il messaggio da stampare.
    """
    return ""


def gioca(ingresso, uscita):
    """Il ciclo principale del gioco.

    ingresso è una funzione senza argomenti che restituisce una riga
    (nel gioco vero è input); uscita è una funzione che riceve un testo
    (nel gioco vero è print). Restituisce il punteggio: i mostri sconfitti.
    """
    return 0


if __name__ == "__main__":
    print("Punteggio:", gioca(input, print))