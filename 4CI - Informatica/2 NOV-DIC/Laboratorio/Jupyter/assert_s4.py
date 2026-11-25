"""Verifiche degli esercizi: usate dai notebook, non da modificare."""

def _test_4_1(goblin):
    assert goblin == {"nome": "Goblin", "vita": 20, "oro": 5}, f"il goblin è {goblin}"
    assert len(goblin) == 3
    assert "attacco" not in goblin
    print("✅ 4.1 superato")


def _test_4_2(ha_zaino, oro_di):
    assert oro_di({"nome": "Aria", "oro": 12}) == 12
    assert oro_di({"nome": "Aria"}) == 0, "chiave mancante: 0, non KeyError"
    assert oro_di({}) == 0
    assert ha_zaino({"zaino": []}) is True, "anche uno zaino vuoto esiste come chiave"
    assert ha_zaino({"nome": "Kofi"}) is False
    print("✅ 4.2 superato")


def _test_4_3(conta_mostri):
    assert conta_mostri(["goblin", "ragno", "goblin"]) == {"goblin": 2, "ragno": 1}
    assert conta_mostri([]) == {}, "caso limite: lista vuota"
    assert conta_mostri(["drago"]) == {"drago": 1}
    assert conta_mostri(["a", "b", "a", "b", "a"]) == {"a": 3, "b": 2}
    assert conta_mostri(list("abracadabra")) == {"a": 5, "b": 2, "r": 2, "c": 1, "d": 1}
    print("✅ 4.3 superato")


def _test_4_4(aggiungi_oggetto, totale_oggetti, usa_oggetto):
    inv = {"pozione": 3, "freccia": 20}
    aggiungi_oggetto(inv, "chiave")
    aggiungi_oggetto(inv, "freccia", 5)
    assert inv == {"pozione": 3, "freccia": 25, "chiave": 1}
    assert totale_oggetti(inv) == 29

    assert usa_oggetto(inv, "pozione") is True
    assert inv["pozione"] == 2
    assert usa_oggetto(inv, "chiave") is True
    assert "chiave" not in inv, "a quantità 0 la chiave deve sparire"
    assert usa_oggetto(inv, "chiave") is False, "non ce n'è più"
    assert usa_oggetto(inv, "drago in scatola") is False
    assert totale_oggetti(inv) == 27
    assert totale_oggetti({}) == 0
    print("✅ 4.4 superato")


def _test_4_5(cerca, deboli, nuovo_bestiario, piu_pericoloso, vita_totale):
    b = nuovo_bestiario()
    assert vita_totale(b) == 375
    assert vita_totale([]) == 0
    assert cerca(b, "Scheletro") == {"nome": "Scheletro", "vita": 45, "attacco": 6}
    assert cerca(b, "Beholder") is None
    assert piu_pericoloso(b)["nome"] == "Drago"
    assert deboli(b, 46) == ["Goblin", "Scheletro"]
    assert deboli(b, 30) == [], "soglia esclusa: 'minore di', non 'minore o uguale'"

    # Frecce: cerca() restituisce proprio il dizionario del bestiario, non una copia
    goblin = cerca(b, "Goblin")
    goblin["vita"] -= 10
    assert b[0]["vita"] == 20, "il goblin ferito resta ferito nel bestiario"
    assert vita_totale(b) == 365
    print("✅ 4.5 superato")


def _test_4_6(schedario):
    assert schedario(["albero", "Ape", "barca"]) == {"a": ["albero", "Ape"], "b": ["barca"]}
    assert schedario([]) == {}
    s = schedario(["drago", "dado", "Dungeon", "elfo"])
    assert s["d"] == ["drago", "dado", "Dungeon"]
    assert list(s.keys()) == ["d", "e"], "le chiavi seguono l'ordine di inserimento"
    assert len(schedario(["x", "x", "x"])["x"]) == 3, "i doppioni restano"
    print("✅ 4.6 superato")


def _test_4_7(ha_oggetto, raccogli, riga_dell_eroe):
    eroe = {"nome": "Aria", "vita": 100, "zaino": ["spada", "torcia"], "posizione": (1, 1)}
    assert ha_oggetto(eroe, "spada") is True
    assert ha_oggetto(eroe, "pozione") is False
    raccogli(eroe, "pozione")
    assert eroe["zaino"] == ["spada", "torcia", "pozione"]
    assert ha_oggetto(eroe, "pozione") is True
    assert riga_dell_eroe(eroe) == 1
    eroe["posizione"] = (3, 2)         # la tupla non si modifica: si sostituisce
    assert riga_dell_eroe(eroe) == 3
    print("✅ 4.7 superato")


def _test_4_8(scelta_a, scelta_b, scelta_c, scelta_d, scelta_e):
    assert scelta_a == "dizionario", "a) si cerca per nome, non per posizione"
    assert scelta_b == "lista di liste", "b) una griglia"
    assert scelta_c == "lista di dizionari", "c) tante cose con gli stessi campi"
    assert scelta_d == "lista", "d) conta l'ordine"
    assert scelta_e == "dizionario", "e) la chiave è il giocatore, il valore le vittorie"
    print("✅ 4.8 superato")


def _test_4_9(err_a, err_b, err_c, err_d, err_e, err_f):
    assert err_a == "IndexError", "a) lo zaino ha caselle 0, 1, 2"
    assert err_b == "KeyError", "b) maiuscole e minuscole sono chiavi diverse"
    assert err_c == "nessuno", "c) get restituisce None"
    assert err_d == "TypeError", "d) i testi sono immutabili"
    assert err_e == "UnboundLocalError"
    assert err_f == "TypeError", "f) unhashable type: 'list'"
    print("✅ 4.9 superato")


_TEST = {
    "4.1": (_test_4_1, ('goblin',)),
    "4.2": (_test_4_2, ('ha_zaino', 'oro_di')),
    "4.3": (_test_4_3, ('conta_mostri',)),
    "4.4": (_test_4_4, ('aggiungi_oggetto', 'totale_oggetti', 'usa_oggetto')),
    "4.5": (_test_4_5, ('cerca', 'deboli', 'nuovo_bestiario', 'piu_pericoloso', 'vita_totale')),
    "4.6": (_test_4_6, ('schedario',)),
    "4.7": (_test_4_7, ('ha_oggetto', 'raccogli', 'riga_dell_eroe')),
    "4.8": (_test_4_8, ('scelta_a', 'scelta_b', 'scelta_c', 'scelta_d', 'scelta_e')),
    "4.9": (_test_4_9, ('err_a', 'err_b', 'err_c', 'err_d', 'err_e', 'err_f')),
}


def verifica(numero, namespace):
    """Esegue i test dell'esercizio usando i valori della cella dello studente."""
    controllo, nomi = _TEST[numero]
    mancanti = [nome for nome in nomi if nome not in namespace]
    if mancanti:
        raise NameError(
            "Mancano: " + ", ".join(mancanti) + ". Esegui prima la cella dell'esercizio."
        )
    try:
        controllo(*(namespace[nome] for nome in nomi))
    except AssertionError:
        raise AssertionError(
            f"❌ {numero}: almeno un controllo non è passato. Rivedi la consegna e i casi limite."
        ) from None
