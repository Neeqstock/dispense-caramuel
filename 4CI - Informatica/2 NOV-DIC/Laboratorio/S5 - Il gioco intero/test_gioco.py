"""Test della missione S5. Non modificare: dice che cosa deve funzionare."""

import random

from gioco import (
    VITA_MASSIMA,
    crea_eroe,
    crea_bestiario,
    subisci_danno,
    cura,
    mostra_scheda,
    scegli_mostro,
    combatti,
    bevi_pozione,
    gioca,
)


class FintoIngresso:
    """Restituisce le righe della lista, una alla volta."""

    def __init__(self, righe):
        self.righe = list(righe)

    def __call__(self):
        return self.righe.pop(0)


class FintaUscita:
    """Raccoglie quello che il gioco stampa."""

    def __init__(self):
        self.righe = []

    def __call__(self, testo):
        self.righe.append(str(testo))

    def testo(self):
        return "\n".join(self.righe)


def test_crea_eroe():
    eroe = crea_eroe()
    assert eroe["nome"] == "Aria"
    assert eroe["vita"] == VITA_MASSIMA
    assert eroe["forza"] == 7
    assert eroe["zaino"] == ["pozione"]


def test_crea_bestiario():
    bestiario = crea_bestiario()
    assert [m["nome"] for m in bestiario] == ["Goblin", "Drago"]
    assert bestiario[0]["vita"] == 10
    assert bestiario[1]["attacco"] == 2


def test_danno_e_cura():
    assert subisci_danno(30, 8) == 22
    assert subisci_danno(5, 8) == 0
    assert cura(70, 30) == 100
    assert cura(90, 30) == 100


def test_mostra_scheda():
    eroe = crea_eroe()
    assert mostra_scheda(eroe) == "Aria: vita 100, forza 7, zaino ['pozione']"


def test_scegli_mostro_toglie_il_primo():
    bestiario = crea_bestiario()
    mostro = scegli_mostro(bestiario)
    assert mostro["nome"] == "Goblin"
    assert len(bestiario) == 1


def test_combatti_un_colpo_basta():
    eroe = crea_eroe()
    mostro = {"nome": "Goblin", "vita": 10, "attacco": 1}
    assert combatti(eroe, mostro, 6) is True
    assert mostro["vita"] == 0


def test_combatti_il_mostro_risponde():
    eroe = crea_eroe()
    mostro = {"nome": "Drago", "vita": 20, "attacco": 2}
    combatti(eroe, mostro, 1)
    assert eroe["vita"] == VITA_MASSIMA - 2


def test_bevi_pozione():
    eroe = crea_eroe()
    eroe["vita"] = 50
    assert bevi_pozione(eroe) == "Glu glu. Vita: 80"
    assert eroe["zaino"] == []
    assert bevi_pozione(eroe) == "Lo zaino non ha pozioni."


def test_gioca_comando_sconosciuto_ed_esci():
    random.seed(1)
    ingresso = FintoIngresso(["x", "0"])
    uscita = FintaUscita()
    assert gioca(ingresso, uscita) == 0
    assert "Comando sconosciuto." in uscita.testo()


def test_gioca_fino_alla_vittoria():
    random.seed(1)
    righe = ["1", "3", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "0"]
    uscita = FintaUscita()
    punteggio = gioca(FintoIngresso(righe), uscita)
    testo = uscita.testo()
    assert punteggio == 2
    assert "Hai vinto!" in testo
    assert "Aria: vita 100" in testo
    assert "Glu glu." in testo