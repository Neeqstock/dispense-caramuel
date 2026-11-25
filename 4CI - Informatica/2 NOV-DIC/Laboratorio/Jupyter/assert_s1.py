"""Verifiche degli esercizi: usate dai notebook, non da modificare."""

def _test_1_1(divisione_intera, divisione_vera, grido, incollati, potenza, resto, sommati):
    assert divisione_vera == 3.5
    assert divisione_intera == 3 and type(divisione_intera) is int, "serve una divisione INTERA"
    assert resto == 1
    assert potenza == 49
    assert incollati == "34"
    assert sommati == 7 and type(sommati) is int
    assert grido == "ciaociaociao"
    print("✅ 1.1 superato")


def _test_1_2(nuova_forza, scheda_breve):
    assert scheda_breve("Aria", 70) == "Aria ha 70 punti vita (70%)"
    assert scheda_breve("Kofi", 5) == "Kofi ha 5 punti vita (5%)"
    assert nuova_forza("7", 2) == 9
    assert type(nuova_forza("7", 2)) is int, "deve restituire un int, non un testo"
    assert nuova_forza("10", 0) == 10
    print("✅ 1.2 superato")


def _test_1_3(menu, piatto, previsione_y, y):
    assert previsione_y == y, "controlla: la freccia di y si è spostata insieme a x?"
    assert menu[0][1] == 8.0
    assert menu[1][1] == 6.0, "il secondo piatto non doveva cambiare prezzo!"
    assert menu[0] is not menu[1], "sono ancora la stessa lista"
    assert piatto[1] == 6.0, "nemmeno l'originale doveva cambiare"
    print("✅ 1.3 superato")


def _test_1_4(media):
    assert media(7, 3) == 5, "media(7, 3) deve valere 5"
    assert media(6, 8) == 7
    assert media(0, 0) == 0
    assert media(1, 2) == 1.5
    print("✅ 1.4 superato")


def _test_1_5(errore_1, errore_2, errore_3, errore_4, errore_5, errore_6):
    assert errore_1 == "TypeError", "1) un testo non si sottrae: che tipo di errore è?"
    assert errore_2 == "ValueError", "2) il tipo è giusto (str), il contenuto no"
    assert errore_3 == "NameError"
    assert errore_4 == "ZeroDivisionError"
    assert errore_5 == "SyntaxError"
    assert errore_6 == "nessuno", "6) moltiplicare un testo per un numero è lecito!"
    print("✅ 1.5 superato")


_TEST = {
    "1.1": (_test_1_1, ('divisione_intera', 'divisione_vera', 'grido', 'incollati', 'potenza', 'resto', 'sommati')),
    "1.2": (_test_1_2, ('nuova_forza', 'scheda_breve')),
    "1.3": (_test_1_3, ('menu', 'piatto', 'previsione_y', 'y')),
    "1.4": (_test_1_4, ('media',)),
    "1.5": (_test_1_5, ('errore_1', 'errore_2', 'errore_3', 'errore_4', 'errore_5', 'errore_6')),
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
