"""Verifiche degli esercizi: usate dai notebook, non da modificare."""

def _test_3_1(tolto, zaino):
    assert tolto == "corda", "pop() restituisce l'elemento tolto: salvalo in 'tolto'"
    assert zaino == ["pagnotta", "mappa", "torcia"], f"zaino è {zaino}"
    assert "corda" not in zaino
    print("✅ 3.1 superato")


def _test_3_2(al_contrario, alfabeto, centro, iniziale_e_fine, primi_tre, senza_ultimo, ultimi_due, uno_su_due):
    assert primi_tre == ["a", "b", "c"]
    assert ultimi_due == ["f", "g"]
    assert centro == ["c", "d", "e"]
    assert al_contrario == ["g", "f", "e", "d", "c", "b", "a"]
    assert uno_su_due == ["a", "c", "e", "g"]
    assert senza_ultimo == ["a", "b", "c", "d", "e", "f"]
    assert iniziale_e_fine == "don"
    assert alfabeto == ["a", "b", "c", "d", "e", "f", "g"], "lo slicing non modifica la lista originale"
    print("✅ 3.2 superato")


def _test_3_3(ordina_decrescente, piu_forte):
    assert piu_forte([8, 12, 5, 9]) == 12
    assert piu_forte([5]) == 5, "caso limite: un solo elemento"
    assert piu_forte([-3, -1, -7]) == -1, "caso limite: tutti negativi"

    d = [3, 1, 2]
    assert ordina_decrescente(d) == [3, 2, 1]
    assert d == [3, 1, 2], "la lista originale non va modificata (sorted, non sort)"
    assert ordina_decrescente([]) == []
    print("✅ 3.3 superato")


def _test_3_4(copia_con):
    zaino_aria = ["spada", "pozione"]
    zaino_kofi = copia_con(zaino_aria, "torcia")
    assert zaino_kofi == ["spada", "pozione", "torcia"]
    assert zaino_aria == ["spada", "pozione"], "lo zaino di Aria non doveva cambiare!"
    assert zaino_kofi is not zaino_aria
    assert copia_con([], "pane") == ["pane"]
    print("✅ 3.4 superato")


def _test_3_5(conta_simbolo, mappa_in_testo, nuova_mappa, trova):
    m = nuova_mappa()
    assert conta_simbolo(m, "#") == 17
    assert conta_simbolo(m, "$") == 1
    assert conta_simbolo(m, "X") == 0
    assert trova(m, "@") == (1, 1)
    assert trova(m, "$") == (2, 4)
    assert trova(m, "X") is None, "se il simbolo non c'è: None"
    assert mappa_in_testo(m) == "######\n#@..M#\n#.#.$#\n######"
    print("✅ 3.5 superato")


def _test_3_6(conta_simbolo, muovi, nuova_mappa, trova):
    m = nuova_mappa()
    assert muovi(m, "destra") is True
    assert m[1] == ["#", ".", "@", ".", "M", "#"], "la @ deve aver fatto un passo a destra"

    m = nuova_mappa()
    assert muovi(m, "su") is False, "sopra l'eroe c'è un muro"
    assert m == nuova_mappa(), "contro un muro la mappa non cambia"

    # Un percorso intero verso il tesoro: giù, poi blocco a destra (muro), poi la strada lunga
    m = nuova_mappa()
    assert muovi(m, "giu") is True and trova(m, "@") == (2, 1)
    assert muovi(m, "destra") is False, "in (2, 2) c'è un muro"
    assert muovi(m, "su") is True and muovi(m, "destra") is True and muovi(m, "destra") is True
    assert trova(m, "@") == (1, 3)
    assert muovi(m, "giu") is True and muovi(m, "destra") is True
    assert trova(m, "@") == (2, 4), "l'eroe è sul tesoro"
    assert conta_simbolo(m, "$") == 0, "camminare sul tesoro lo raccoglie (lo sovrascrive)"
    assert conta_simbolo(m, "@") == 1, "deve esistere una sola @"
    print("✅ 3.6 superato")


def _test_3_7(crea_griglia):
    g = crea_griglia(3, 4, ".")
    assert len(g) == 3 and len(g[0]) == 4
    assert g == [[".", ".", ".", "."]] * 3
    g[0][0] = "@"
    assert g[1][0] == ".", "se fallisce: le righe sono tre frecce verso la stessa lista"
    assert g[2][0] == "."
    assert g[0] is not g[1]
    assert crea_griglia(0, 5, "x") == [], "caso limite: nessuna riga"
    print("✅ 3.7 superato")


_TEST = {
    "3.1": (_test_3_1, ('tolto', 'zaino')),
    "3.2": (_test_3_2, ('al_contrario', 'alfabeto', 'centro', 'iniziale_e_fine', 'primi_tre', 'senza_ultimo', 'ultimi_due', 'uno_su_due')),
    "3.3": (_test_3_3, ('ordina_decrescente', 'piu_forte')),
    "3.4": (_test_3_4, ('copia_con',)),
    "3.5": (_test_3_5, ('conta_simbolo', 'mappa_in_testo', 'nuova_mappa', 'trova')),
    "3.6": (_test_3_6, ('conta_simbolo', 'muovi', 'nuova_mappa', 'trova')),
    "3.7": (_test_3_7, ('crea_griglia',)),
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
