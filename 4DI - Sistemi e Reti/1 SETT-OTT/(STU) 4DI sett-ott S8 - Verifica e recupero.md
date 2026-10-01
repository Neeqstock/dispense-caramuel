# 🎯 Verifica e recupero

**4DI · Settembre-Ottobre · S8 · Ripasso personale**

> **Legenda:** ✅ da sapere · 🔍 per capire fino in fondo · 🤓 facoltativo, per curiosi · 🃏 flashcard: rispondi a voce, poi apri per controllare

```mermaid
mindmap
  root((🎯 Verifica e recupero))
    🧭 Prepararsi con metodo
      ✅ Ripassare i concetti fondamentali
      ✅ Mostrare i passaggi dei calcoli
    🔁 Imparare dalla verifica
      🔍 Usare gli errori per individuare un passaggio
      🔍 Dimostrare il recupero con un nuovo esempio
      🤓 Una verifica misura obiettivi circoscritti
    🧩 Metti alla prova il modello
```

## 🧭 Prepararsi con metodo

### ✅ Ripassare i concetti fondamentali

La verifica del bimestre riguarda i contenuti studiati da S1 a S6. Per ripassare, prova a spiegare senza appunti:

- come ISO/OSI e TCP/IP dividono le responsabilità;
- come dati, segmento, pacchetto, frame e segnali si collegano;
- che cosa fanno il livello fisico e il collegamento dati;
- come prefisso e maschera separano rete e host;
- che cosa distinguono indirizzi privati, NAT e firewall;
- come si dimensionano sottoreti FLSM, CIDR e VLSM.

ARP/RARP, routing, ICMP, `ping`, `traceroute`, DNS e configurazione degli apparati appartengono a un percorso successivo.

<details>
<summary>🃏 Quali settimane costituiscono il programma della verifica?</summary>
S1-S6: modelli, incapsulamento, livello fisico ed Ethernet, IPv4, reti private, FLSM, CIDR e VLSM.
</details>
<details>
<summary>🃏 Quale PDU è associata al livello di rete Internet?</summary>
Il pacchetto IP.
</details>
<details>
<summary>🃏 Quali argomenti sono successivi al bimestre?</summary>
ARP/RARP, routing, ICMP, ping, traceroute e DNS, oltre alla configurazione degli apparati.
</details>

### ✅ Mostrare i passaggi dei calcoli

Quando risolvi un esercizio, scrivi i passaggi in ordine:

1. prefisso e maschera;
2. bit host e dimensione del blocco;
3. Network ID e intervallo;
4. host ordinari e broadcast;
5. per VLSM, verifica di capienza, allineamento e sovrapposizioni.

Una risposta leggibile permette di capire il ragionamento anche se un calcolo intermedio va corretto. Non limitarti a riportare un numero senza spiegare da dove viene.

<details>
<summary>🃏 Che cosa conviene scrivere prima di trovare l'intervallo di una rete?</summary>
Prefisso, maschera, bit host e dimensione del blocco.
</details>
<details>
<summary>🃏 Quali informazioni principali mostra una soluzione completa di subnetting?</summary>
Network ID, intervallo host ordinari e broadcast, con prefisso e passaggi coerenti.
</details>
<details>
<summary>🃏 Quali controlli aggiungi in un progetto VLSM?</summary>
Capienza, allineamento e assenza di sovrapposizioni.
</details>

## 🔁 Imparare dalla verifica

### 🔍 Usare gli errori per individuare un passaggio

Un errore è più utile quando sai dire in quale passaggio è comparso. Se confondi rete e host, ricontrolla il confine del blocco. Se il numero di host non basta, rivedi i bit host. Se due sottoreti si sovrappongono, confronta gli intervalli sulla linea degli indirizzi.

Dopo una correzione, prova un esercizio con numeri diversi: così verifichi di aver capito il metodo e non soltanto memorizzato la risposta.

<details>
<summary>🃏 Che cosa fai quando una rete non parte su un confine valido?</summary>
Ricontrollo la dimensione del blocco e individuo il confine corretto che contiene l'indirizzo.
</details>
<details>
<summary>🃏 Come puoi verificare di aver capito una correzione?</summary>
Risolvo un nuovo esempio con dati diversi e mostro i passaggi.
</details>
<details>
<summary>🃏 Perché è utile individuare il passaggio in cui nasce un errore?</summary>
Per scegliere quale regola ripassare e correggere il procedimento, non solo il risultato.
</details>

### 🔍 Dimostrare il recupero con un nuovo esempio

Per rendere visibile il progresso, usa una traccia breve:

| Che cosa scrivo | Esempio |
|---|---|
| Il passaggio che confondevo | Rete e broadcast |
| La regola che applico ora | Il blocco `/27` contiene 32 indirizzi |
| Il nuovo esempio | Un indirizzo diverso con prefisso `/27` |
| Il controllo finale | Verifico rete, host e broadcast |

Adatta la traccia al tuo errore: modello, livelli, prefisso, conteggio degli host o confini.

<details>
<summary>🃏 Che cosa deve contenere un esempio di recupero?</summary>
Il passaggio da correggere, la regola applicata, un nuovo esempio e un controllo del risultato.
</details>
<details>
<summary>🃏 Perché usare numeri diversi nel nuovo esempio?</summary>
Per mostrare che si sa applicare la regola e non si sta ripetendo a memoria una soluzione.
</details>

### 🤓 Una verifica misura obiettivi circoscritti

> Una verifica teorica raccoglie evidenze su obiettivi definiti. Non dimostra da sola ogni capacità necessaria per configurare o diagnosticare una rete reale. Altri aspetti si affrontano nelle attività previste dal percorso.
>
> Per studiare bene, concentrati sulle richieste e sui metodi che avete esercitato.

<details>
<summary>🃏 Una verifica teorica dimostra automaticamente ogni capacità pratica?</summary>
No. Misura obiettivi teorici circoscritti; altre capacità richiedono attività specifiche.
</details>

## 🧩 Metti alla prova il modello

1. Spiega a voce la differenza fra pacchetto IP e frame.
2. Se restano 6 bit host, quanti indirizzi contiene il blocco? Quanti sono gli host ordinari?
3. Quali controlli fai per un piano VLSM?
4. Scegli un errore corretto e prepara un nuovo esempio per mostrare il metodo.

**Uscita:** «Il passaggio che ora so controllare è ..., perché ...».

## 📚 Fonti e risorse

- [CIDR e intervalli](%28STU%29%204DI%20sett-ott%20S5%20-%20CIDR%20e%20intervalli.md): prefissi e dimensione dei blocchi.
- [VLSM e progettazione](%28STU%29%204DI%20sett-ott%20S6%20-%20VLSM%20e%20progettazione.md): metodo e verifiche.
- [RFC 1918 - Private Address Space](https://www.rfc-editor.org/rfc/rfc1918): riferimento sugli indirizzi IPv4 privati.

---

[⬅️ S7 - Ripasso e troubleshooting](%28STU%29%204DI%20sett-ott%20S7%20-%20Ripasso%20e%20troubleshooting.md) · [🗺️ Indice](%28STU%29%204DI%20-%20SETT-OTT.md)