"""Test della missione S4. Non modificare: dice che cosa deve funzionare."""

from bestiario import (
    scheda_nuova,
    leggi,
    scrivi,
    aumenta,
    chiavi,
    cerca_per_nome,
    il_piu_forte,
    per_nome,
)


def test_scheda_nuova_ha_le_quattro_chiavi():
    scheda = scheda_nuova("Aria")
    assert scheda["nome"] == "Aria"
    assert scheda["vita"] == 100
    assert scheda["forza"] == 7
    assert scheda["zaino"] == []


def test_scheda_nuova_accetta_valori_diversi():
    scheda = scheda_nuova("Borin", vita=60, forza=12)
    assert scheda["vita"] == 60
    assert scheda["forza"] == 12


def test_leggi_chiave_presente_e_assente():
    scheda = {"nome": "Aria", "vita": 100}
    assert leggi(scheda, "vita") == 100
    assert leggi(scheda, "mana") is None


def test_scrivi_crea_e_sovrascrive():
    scheda = {"nome": "Aria"}
    scrivi(scheda, "vita", 90)
    scrivi(scheda, "mana", 5)
    assert scheda["vita"] == 90
    assert scheda["mana"] == 5


def test_aumenta_modifica_in_place():
    scheda = {"forza": 7}
    aumenta(scheda, "forza", 3)
    assert scheda["forza"] == 10


def test_chiavi_contiene_tutte_le_chiavi():
    scheda = scheda_nuova("Aria")
    assert sorted(chiavi(scheda)) == ["forza", "nome", "vita", "zaino"]


def test_cerca_per_nome_trova_e_non_trova():
    bestiario = [
        {"nome": "Goblin", "attacco": 4},
        {"nome": "Drago", "attacco": 30},
    ]
    assert cerca_per_nome(bestiario, "Drago")["attacco"] == 30
    assert cerca_per_nome(bestiario, "Orco") is None


def test_il_piu_forte():
    bestiario = [
        {"nome": "Goblin", "attacco": 4},
        {"nome": "Drago", "attacco": 30},
        {"nome": "Scheletro", "attacco": 6},
    ]
    assert il_piu_forte(bestiario) == "Drago"


def test_per_nome_costruisce_la_rubrica():
    bestiario = [
        {"nome": "Goblin", "attacco": 4},
        {"nome": "Drago", "attacco": 30},
    ]
    rubrica = per_nome(bestiario)
    assert set(rubrica) == {"Goblin", "Drago"}
    assert rubrica["Goblin"]["attacco"] == 4