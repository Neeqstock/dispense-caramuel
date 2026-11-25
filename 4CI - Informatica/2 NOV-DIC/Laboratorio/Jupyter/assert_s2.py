"""Verifiche degli esercizi: usate dai notebook, non da modificare."""

def _test_2_1(danno_subito):
    assert danno_subito(7) == 5, "con armatura 2 predefinita"
    assert danno_subito(7, armatura=5) == 2
    assert danno_subito(3, armatura=10) == 0, "caso limite: l'armatura supera il colpo"
    assert danno_subito(0) == 0
    print("✅ 2.1 superato")


def _test_2_2(pozione):
    assert pozione(40) == 55, "pozione(40) deve restituire 55"
    assert pozione(0) == 15

    vita = 40
    vita = pozione(vita)           # è il chiamante a spostare la freccia
    assert vita == 55
    print("✅ 2.2 superato")


def _test_2_3(turni_necessari):
    assert turni_necessari(30, 8) == 4, "30 -> 22 -> 14 -> 6 -> -2: quattro colpi"
    assert turni_necessari(8, 8) == 1
    assert turni_necessari(1, 100) == 1
    assert turni_necessari(0, 8) == 0, "caso limite: già morto, zero colpi"
    print("✅ 2.3 superato")


def _test_2_4(risolvi_turno):
    assert risolvi_turno(100, 8, 8) == 100, "il goblin è morto: non morde"
    assert risolvi_turno(100, 30, 8) == 96, "il goblin sopravvive e morde"
    assert risolvi_turno(3, 30, 8) == 0, "la vita non scende sotto zero"
    assert risolvi_turno(100, 8, 0) == 96, "danno nullo: il goblin sopravvive"
    assert risolvi_turno(100, 1, 50) == 100, "danno enorme: il goblin cade"
    print("✅ 2.4 superato")


def _test_2_5(porta):
    assert porta(5) == [
        "La porta resiste al tentativo 1",
        "La porta resiste al tentativo 3",
        "La porta si apre.",
    ]
    assert porta(1) == ["La porta si apre."]
    assert porta(7)[-1] == "La porta si apre."
    # Con un numero pari il continue salta il controllo: la porta non si apre mai!
    assert "La porta si apre." not in porta(4), "i pari vengono saltati PRIMA del controllo"
    assert len(porta(4)) == 4
    print("✅ 2.5 superato")


def _test_2_6(conta_valori, tira_dado):
    # Dado truccato: restituisce i valori di una lista, uno alla volta (pop(0) toglie il primo)
    tiri_finti = [6, 2, 6, 6, 1]
    def dado_finto():
        return tiri_finti.pop(0)

    assert conta_valori(dado_finto, 6, 5) == 3, "nei tiri finti il 6 esce tre volte"

    # Dado vero: non prevediamo il numero esatto, ma l'intervallo sì
    for _ in range(500):
        assert 1 <= tira_dado() <= 6
        assert 1 <= tira_dado(20) <= 20
    assert tira_dado(1) == 1
    from unittest.mock import patch
    with patch("random.randint", return_value=1) as casuale:
        assert tira_dado() == 1
        casuale.assert_called_once_with(1, 6)
    with patch("random.randint", return_value=6) as casuale:
        assert tira_dado() == 6
        casuale.assert_called_once_with(1, 6)
    assert conta_valori(tira_dado, 7, 100) == 0, "un d6 non fa mai 7"
    print("✅ 2.6 superato")


def _test_2_7(cura):
    assert cura(100) == 120
    assert cura(0) == 20

    vita = 100
    cura(vita)                  # il risultato non viene salvato: la freccia esterna non si muove
    assert vita == 100, "una funzione con return non modifica la variabile esterna"
    vita = cura(vita)           # è il chiamante a spostare la freccia
    assert vita == 120
    print("✅ 2.7 superato")


def _test_2_8(aggiungi):
    assert aggiungi("spada") == ["spada"]
    assert aggiungi("pozione") == ["pozione"], "lo zaino non deve ricordare le chiamate precedenti"

    mio = ["pane"]
    risultato = aggiungi("corda", mio)
    assert risultato == ["pane", "corda"]
    assert risultato is mio, "deve modificare proprio lo zaino ricevuto, non una copia"
    print("✅ 2.8 superato")


_TEST = {
    "2.1": (_test_2_1, ('danno_subito',)),
    "2.2": (_test_2_2, ('pozione',)),
    "2.3": (_test_2_3, ('turni_necessari',)),
    "2.4": (_test_2_4, ('risolvi_turno',)),
    "2.5": (_test_2_5, ('porta',)),
    "2.6": (_test_2_6, ('conta_valori', 'tira_dado')),
    "2.7": (_test_2_7, ('cura',)),
    "2.8": (_test_2_8, ('aggiungi',)),
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
