"""Test della missione S3. Non modificare: dice che cosa deve funzionare."""

from zaino_mappa import (
    zaino_nuovo,
    aggiungi,
    togli,
    conta_oggetti,
    c_e,
    valore_totale,
    copia,
    mappa_vuota,
    metti,
    trova,
    conta_simboli,
)


def test_aggiungi_in_fondo_e_restituisce_la_lista():
    zaino = zaino_nuovo()
    assert aggiungi(zaino, "pozione") == ["pozione"]
    assert aggiungi(zaino, "spada") == ["pozione", "spada"]


def test_zaino_nuovo_e_ogni_volta_una_lista_diversa():
    a = zaino_nuovo()
    b = zaino_nuovo()
    a.append("x")
    assert b == []


def test_togli_la_prima_occorrenza():
    zaino = ["pozione", "spada", "pozione"]
    assert togli(zaino, "pozione") == ["spada", "pozione"]


def test_togli_un_oggetto_assente_non_fa_nulla():
    zaino = ["spada"]
    assert togli(zaino, "scudo") == ["spada"]


def test_conta_e_c_e():
    zaino = ["pozione", "spada"]
    assert conta_oggetti(zaino) == 2
    assert c_e(zaino, "spada") is True
    assert c_e(zaino, "scudo") is False


def test_valore_totale_anche_vuoto():
    assert valore_totale([2.5, 1.5]) == 4.0
    assert valore_totale([]) == 0


def test_copia_e_indipendente():
    originale = ["pozione"]
    altra = copia(originale)
    altra.append("spada")
    assert originale == ["pozione"]
    assert altra == ["pozione", "spada"]
    assert altra is not originale


def test_mappa_vuota_ha_le_dimensioni_chieste():
    mappa = mappa_vuota(4, 6)
    assert len(mappa) == 4
    assert len(mappa[0]) == 6
    assert mappa[0] == ["."] * 6


def test_le_righe_della_mappa_sono_indipendenti():
    mappa = mappa_vuota(3, 3)
    mappa[0][0] = "X"
    assert mappa[1][0] == "."
    assert mappa[2][0] == "."
    assert len({id(riga) for riga in mappa}) == 3


def test_metti_e_trova():
    mappa = mappa_vuota(3, 3)
    metti(mappa, 1, 2, "E")
    assert mappa[1][2] == "E"
    assert trova(mappa, "E") == (1, 2)


def test_trova_restituisce_none_se_non_c_e():
    assert trova(mappa_vuota(3, 3), "E") is None


def test_conta_simboli():
    mappa = mappa_vuota(3, 3)
    metti(mappa, 0, 0, "#")
    metti(mappa, 2, 1, "#")
    assert conta_simboli(mappa, "#") == 2
    assert conta_simboli(mappa, ".") == 7