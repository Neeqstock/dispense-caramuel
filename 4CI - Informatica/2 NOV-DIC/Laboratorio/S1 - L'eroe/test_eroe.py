"""Test della missione S1. Non modificare: dice che cosa deve funzionare."""

from eroe import (
    saluta,
    scheda,
    meta_forza,
    meta_forza_intera,
    leggi_vita,
    tipo,
)


def test_saluta_restituisce_il_benvenuto():
    assert saluta("Aria") == "Benvenuta, Aria!"


def test_scheda_mostra_nome_vita_e_forza():
    assert scheda("Aria", 100, 7) == "Aria: vita 100, forza 7"


def test_meta_forza_tiene_i_decimali():
    assert meta_forza(7) == 3.5
    assert meta_forza(8) == 4.0


def test_meta_forza_intera_tronca_i_decimali():
    assert meta_forza_intera(7) == 3
    assert meta_forza_intera(8) == 4


def test_leggi_vita_trasforma_il_testo_in_numero():
    assert leggi_vita("100") == 100
    assert isinstance(leggi_vita("100"), int)


def test_tipo_nomina_il_tipo_del_valore():
    assert tipo(7) == "int"
    assert tipo("7") == "str"
    assert tipo(7.5) == "float"
    assert tipo(True) == "bool"