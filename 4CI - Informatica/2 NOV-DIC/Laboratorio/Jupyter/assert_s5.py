"""Verifiche degli esercizi: usate dai notebook, non da modificare."""

def _test_5_1(VITA_MASSIMA, cura, subisci_danno):
    assert VITA_MASSIMA == 100
    assert subisci_danno(100, 30) == 70
    assert subisci_danno(10, 30) == 0, "caso limite: mai sotto zero"
    assert subisci_danno(50, 0) == 50, "caso limite: danno nullo"
    assert subisci_danno(30, 30) == 0, "caso limite: danno uguale alla vita"
    assert cura(50, 30) == 80
    assert cura(90, 30) == 100, "caso limite: mai sopra il massimo"
    assert cura(100, 30) == 100, "caso limite: già al massimo"
    assert cura(40, 0) == 40
    assert subisci_danno.__doc__ and cura.__doc__, "manca una docstring"
    print("✅ 5.1 superato")


def _test_5_2(bonus_critico, collauda, mutante_1, mutante_2, mutante_3):
    # --- Controllore (non modificare): usa try/except, che vedremo più avanti ---
    collauda(bonus_critico)         # la versione corretta DEVE passare tutti i tuoi assert

    sopravvissuti = []
    for nome, mutante in [("mutante_1", mutante_1), ("mutante_2", mutante_2), ("mutante_3", mutante_3)]:
        try:
            collauda(mutante)
            sopravvissuti.append(nome)      # nessun assert è fallito: il bug è sfuggito!
        except AssertionError:
            pass                            # bug scoperto

    assert not sopravvissuti, f"Questi mutanti sono sopravvissuti ai tuoi test: {sopravvissuti}"
    print("✅ 5.2 superato: tutti i mutanti eliminati 🧟🗡️")


def _test_5_3(combatti):
    def dado_tre():
        return 3

    def dado_uno():
        return 1

    # Aria (forza 7, dado 3 -> danno 10) contro un Goblin da 30 vita, attacco 4:
    # t1 goblin 20, Aria 96 | t2 goblin 10, Aria 92 | t3 goblin 0 (non contrattacca)
    aria = {"nome": "Aria", "vita": 100, "forza": 7}
    goblin = {"nome": "Goblin", "vita": 30, "attacco": 4}
    assert combatti(aria, goblin, dado_tre) is True
    assert goblin["vita"] == 0, "il goblin non deve scendere sotto zero"
    assert aria["vita"] == 92, "il goblin morto non contrattacca"

    # Un eroe debole (forza 1, dado 1 -> danno 2) con 5 di vita perde:
    # t1 goblin 28, eroe 1 | t2 goblin 26, eroe 0
    debole = {"nome": "Pip", "vita": 5, "forza": 1}
    goblin = {"nome": "Goblin", "vita": 30, "attacco": 4}
    assert combatti(debole, goblin, dado_uno) is False
    assert debole["vita"] == 0, "la vita dell'eroe non scende sotto zero"
    assert goblin["vita"] == 26

    # Mostro già morto: nessun giro di combattimento
    aria = {"nome": "Aria", "vita": 100, "forza": 7}
    cadavere = {"nome": "Ossa", "vita": 0, "attacco": 99}
    assert combatti(aria, cadavere, dado_tre) is True
    assert aria["vita"] == 100

    # Con il dado vero (parametro predefinito) non prevediamo il numero, ma l'esito sì:
    eroe_forte = {"nome": "Eracle", "vita": 100, "forza": 50}
    assert combatti(eroe_forte, {"nome": "Topo", "vita": 10, "attacco": 1}) is True
    print("✅ 5.3 superato")


def _test_5_4(esegui_comandi):
    def dado_tre():
        return 3


    def dado_uno():
        return 1


    def nuova_partita():
        eroe = {"nome": "Aria", "vita": 100, "forza": 7, "zaino": ["pozione"]}
        bestiario = [
            {"nome": "Goblin", "vita": 30, "attacco": 4},
            {"nome": "Scheletro", "vita": 45, "attacco": 6},
        ]
        return eroe, bestiario

    # --- Una partita intera (dado sempre 3: danno 10 a ogni colpo) ---
    eroe, bestiario = nuova_partita()
    registro = esegui_comandi(eroe, bestiario, ["1", "2", "3", "2", "2", "0"], tira=dado_tre)
    assert registro == [
        "Aria: vita 100, zaino ['pozione']",
        "Goblin sconfitto! Vita di Aria: 92",
        "Glu glu. Vita: 100",
        "Scheletro sconfitto! Vita di Aria: 76",
        "Il dungeon è vuoto: hai vinto!",       # qui il gioco finisce: lo "0" finale non viene eseguito
    ], registro
    assert bestiario == [], "i mostri sconfitti vengono tolti dal bestiario"

    # --- Scelte strane e zaino vuoto ---
    eroe, bestiario = nuova_partita()
    registro = esegui_comandi(eroe, bestiario, ["9", "3", "3", "uno", "0", "1"], tira=dado_tre)
    assert registro == [
        "Scelta non valida.",
        "Glu glu. Vita: 100",                  # a 100 di vita la cura non supera il massimo
        "Lo zaino non ha pozioni.",
        "Scelta non valida.",                  # "uno" è un testo diverso da "1"
        "Alla prossima!",
    ], registro
    assert eroe["zaino"] == []
    assert len(bestiario) == 2, "nessun combattimento: il bestiario è intatto"

    # --- Game over: il gioco si ferma e il resto dei comandi viene ignorato ---
    debole = {"nome": "Pip", "vita": 5, "forza": 1, "zaino": []}
    bestiario = [{"nome": "Goblin", "vita": 30, "attacco": 4}]
    registro = esegui_comandi(debole, bestiario, ["2", "1", "1"], tira=dado_uno)
    assert registro == ["Goblin ha vinto. Game over."], registro
    assert debole["vita"] == 0

    # --- Nessun comando, nessun messaggio ---
    eroe, bestiario = nuova_partita()
    assert esegui_comandi(eroe, bestiario, []) == []
    print("✅ 5.4 superato")


_TEST = {
    "5.1": (_test_5_1, ('VITA_MASSIMA', 'cura', 'subisci_danno')),
    "5.2": (_test_5_2, ('bonus_critico', 'collauda', 'mutante_1', 'mutante_2', 'mutante_3')),
    "5.3": (_test_5_3, ('combatti',)),
    "5.4": (_test_5_4, ('esegui_comandi',)),
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
