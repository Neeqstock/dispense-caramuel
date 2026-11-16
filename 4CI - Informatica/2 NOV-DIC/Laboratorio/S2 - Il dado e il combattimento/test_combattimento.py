"""Test della missione S2. Non modificare: dice che cosa deve funzionare."""

import random

from combattimento import (
    tira_dado,
    subisci_danno,
    cura,
    e_vivo,
    combatti,
    conta_vittorie,
)


def test_tira_dado_resta_nell_intervallo():
    for _ in range(300):
        assert 1 <= tira_dado() <= 6
        assert 1 <= tira_dado(20) <= 20


def test_tira_dado_usa_la_casualita():
    random.seed(1)
    tiri = {tira_dado() for _ in range(200)}
    assert tiri == {1, 2, 3, 4, 5, 6}


def test_subisci_danno_non_scende_sotto_zero():
    assert subisci_danno(30, 8) == 22
    assert subisci_danno(5, 8) == 0


def test_cura_non_supera_il_massimo():
    assert cura(70, 30) == 100
    assert cura(90, 30) == 100
    assert cura(40, 10) == 50


def test_e_vivo():
    assert e_vivo(1) is True
    assert e_vivo(0) is False
    assert e_vivo(-2) is False


def test_combatti_mostro_debole():
    random.seed(7)
    eroe = {"nome": "Aria", "vita": 100, "forza": 50}
    mostro = {"nome": "Goblin", "vita": 10, "attacco": 1}
    assert combatti(eroe, mostro) is True
    assert mostro["vita"] == 0


def test_combatti_eroe_debole_perde():
    random.seed(7)
    eroe = {"nome": "Aria", "vita": 5, "forza": 1}
    mostro = {"nome": "Drago", "vita": 500, "attacco": 50}
    assert combatti(eroe, mostro) is False
    assert eroe["vita"] == 0


def test_combatti_aggiorna_i_dizionari():
    random.seed(3)
    eroe = {"nome": "Aria", "vita": 100, "forza": 10}
    mostro = {"nome": "Scheletro", "vita": 20, "attacco": 3}
    vita_prima = eroe["vita"]
    combatti(eroe, mostro)
    assert eroe["vita"] < vita_prima


def test_conta_vittorie():
    random.seed(11)
    eroe = {"nome": "Aria", "vita": 100, "forza": 20}
    mostri = [
        {"nome": "Goblin", "vita": 10, "attacco": 1},
        {"nome": "Goblin", "vita": 10, "attacco": 1},
        {"nome": "Goblin", "vita": 10, "attacco": 1},
    ]
    assert conta_vittorie(eroe, mostri) == 3