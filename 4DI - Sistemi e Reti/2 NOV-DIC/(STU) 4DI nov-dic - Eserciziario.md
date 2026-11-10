⬅️ [S7 - Ripasso e recupero](%28STU%29%204DI%20nov-dic%20S7%20-%20Ripasso%20e%20recupero.md) · 🏠 [Indice](../README.md)

# 🧮 Eserciziario · 4DI nov-dic

**4DI · Novembre-Dicembre · Eserciziario con casi reali · Teoria e pratica scritta**

⏱️ **Tempo: un dossier dura 10-25 minuti.** ✅ essenziale: circa 60 minuti in tutto. 🔍 per il voto alto: circa 75 minuti. 🤓 si può saltare. Non è un compito a casa: scegli i dossier che ti servono, anche uno al giorno.

> **Legenda:** ✅ da sapere · 🔍 per capire fino in fondo · 🤓 facoltativo · 📜 caso reale o inventato · 📖 teoria · ✏️ pratica scritta · 🟢 svolto: guarda come si fa · 🎯 da provare: soluzione nascosta · 🧠 da ricordare · ⚠️ errore comune · 📌 controllo · 🩹 recupero · 🔧 in laboratorio · 🃏 soluzione

In ufficio nessuno ti dà un esercizietto. Ti dicono: «la sede Monte non si collega, guardaci tu». Sei il nuovo tecnico di rete di **Ponte Srl** (azienda inventata), con tre sedi: Mare, Monte e Valle. Ogni dossier parte da un caso e ti chiede i conti che servono per capire il problema.

<u>Una rete è fatta di confini. Se un confine è sbagliato, il pacchetto non arriva dove deve.</u>

## Come si usa

- 🟢 **Svolto.** Leggi i passaggi, poi copri la mano e rifai l'esercizio sul quaderno.
- 🎯 **Da provare.** Prima prova tu, sul quaderno. Poi apri la soluzione 🃏 e confronta.
- Ogni dossier ha almeno un esercizio svolto, uno di teoria 📖 e uno di pratica scritta ✏️.
- **Valori.** Ponte Srl, le sue sedi, i nomi dei reparti e i numeri degli esercizi sono inventati. Gli indirizzi `172.18.x.x` sono privati (RFC 1918), `198.51.100.0/30` è riservato alla documentazione (RFC 5737), `2001:db8::/32` è il prefisso riservato alla documentazione IPv6. I casi reali sono segnalati con 📜 e hanno le fonti in fondo.
- **Strumenti.** Puoi usare il metodo del salto e il metodo binario di S1, e una calcolatrice. Scrivi i passaggi: un risultato senza passaggi non si può controllare.
- **Solo carta.** Nessun comando e nessuna configurazione: gli apparati si vedranno in laboratorio.

| Dossier | Tema                                | Settimana | Caso                                    |
| :-----: | ----------------------------------- | :-------: | --------------------------------------- |
|    1    | Il confine del prefisso             |    S1     | RFC 1519, 1993                          |
|    2    | VLSM e collegamenti /30             |    S2     | RFC 950, 1985; il piano di Ponte Srl    |
|    3    | IPv6: lo spazio nuovo               |    S3     | IANA 2011; World IPv6 Launch 2012       |
|    4    | Router e tabella                    |    S4     | YouTube, 2008                           |
|    5    | Rotte statiche e default route      |    S5     | La sede Valle non risponde              |
|    6    | Distance Vector e Link State        |    S6     | ARPANET, 1979                           |
|    7    | Livello finale: ripasso mescolato   |    S7     | Lunedì mattina a Ponte Srl              |

---

## 🔢 Dossier 1 · Il confine del prefisso

*Si usa S1: prefisso, rete, broadcast, salto.*

### 📜 Caso reale: il 1993 e il prefisso

Fino al 1993 la taglia di una rete la decideva la **classe**, cioè il primo numero dell'indirizzo. Una rete di classe C dava 254 host ordinari anche a chi ne serviva 40: il resto dello spazio andava perso. Nel settembre 1993 le RFC 1518 e 1519 introducono **CIDR**: il confine si scrive con un prefisso, come `/26`, e può cadere in qualunque punto.

🧠 <u>Il prefisso sostituisce la classe: il numero dopo la barra dice dove passa il confine.</u>

### 1.1 📖 Teoria · ✅ · 🟢 Svolto — Dove finisce il blocco

**Consegna.** Il PC di Dalia, nella sede Mare, ha `172.18.40.200/21`. Trova: maschera, bit host, rete, broadcast, primo e ultimo host, host ordinari. Poi dì se `172.18.47.9` sta nello stesso blocco.

**Svolgimento.**

1. **Maschera.** `/21` diventa `255.255.248.0`: il confine cade nel terzo ottetto.
2. **Bit host.** $32 - 21 = 11$. Indirizzi nel blocco: $2^{11} = 2048$.
3. **Salto.** $256 - 248 = 8$. I blocchi del terzo ottetto partono da 0, 8, 16, …, 40, 48.
4. **Rete.** 40 è multiplo di 8: la rete è `172.18.40.0/21`. Il `200` finale non conta.
5. **Broadcast.** $40 + 8 - 1 = 47$: `172.18.47.255`.
6. **Host.** Da `172.18.40.1` a `172.18.47.254`: $2048 - 2 = 2046$ host ordinari.
7. **Verifica.** `172.18.47.9` ha terzo ottetto 47, dentro 40-47: **sì**, stesso blocco. `172.18.48.1` no.

📌 **Controllo binario.** $40 = 00101000$, $248 = 11111000$, AND $= 00101000 = 40$. Il metodo binario conferma il salto.

⚠️ **Errore comune.** Cercare il salto nel quarto ottetto, cioè nel `200`. Il salto sta nell'ottetto dove la maschera smette di valere 255.

🧠 <u>Il salto sta nell'ottetto dove la maschera smette di valere 255.</u>

### 1.2 ✏️ Pratica · ✅ · 🟢 Svolto — Sei reparti in una rete

**Consegna.** Ponte Srl ha il blocco `172.18.0.0/16` e vuole una sottorete uguale per ciascuno dei sei reparti. Quale prefisso? Scrivi i primi due blocchi.

**Svolgimento.**

1. **Sottoreti necessarie:** 6. Con 2 bit ne avresti $2^2 = 4$, non bastano; con 3 bit sono $2^3 = 8$.
2. **Prefisso:** $16 + 3 = 19$, cioè `/19`.
3. **Indirizzi per blocco:** $2^{13} = 8192$. Salto nel terzo ottetto: $256 - 224 = 32$.
4. **Primi due blocchi:** `172.18.0.0/19` (broadcast `172.18.31.255`) e `172.18.32.0/19` (broadcast `172.18.63.255`).

📌 **Controllo.** Gli 8 blocchi di `/19` sono $8 \times 8192 = 65536$, cioè tutto il `/16`. Ne usi 6; gli altri 2 restano liberi.

⚠️ **Errore comune.** Confondere le sottoreti con gli indirizzi: sei reparti non sono sei host.

### 1.3 📖 Teoria · 🔍 · 🎯 Da provare — Vero o falso?

**Consegna.** Per ciascuna frase scrivi **V** o **F**. Se è falsa, correggila in una frase.

1. Un `/26` ha 64 host ordinari.
2. Il primo indirizzo del blocco si può assegnare a un PC.
3. Più il prefisso è lungo, più il blocco è grande.
4. Un `/30` ha due host ordinari.
5. Il broadcast è l'ultimo indirizzo del blocco.

<details>
<summary>🃏 <b>1.3 — Soluzione</b></summary>

1. **F.** Un `/26` ha 64 indirizzi, ma host ordinari sono 62: si tolgono rete e broadcast.
2. **F.** Il primo indirizzo è quello di rete: non si assegna.
3. **F.** Più il prefisso è lungo, più bit sono di rete e meno bit restano per gli host: il blocco è più piccolo. Un `/30` ha 4 indirizzi; un `/24` ne ha 256.
4. **V.** $4 - 2 = 2$.
5. **V.**

⚠️ **Errore comune:** scrivere 64 al punto 1. Il conto giusto è $2^6 - 2 = 62$.

</details>

### 1.4 ✏️ Pratica · 🔍 · 🎯 Da provare — Il reparto Contabilità

**Consegna.** Un PC della Contabilità ha `172.18.100.130/26`. Scrivi rete, broadcast, primo e ultimo host. Poi dì se `172.18.100.191` può essere assegnato a un PC.

<details>
<summary>🃏 <b>1.4 — Soluzione</b></summary>

Salto nel quarto ottetto: $256 - 192 = 64$. Il `130` sta fra 128 e 191: la rete è `172.18.100.128/26`. Broadcast `172.18.100.191`; host da `172.18.100.129` a `172.18.100.190`.

Quindi `172.18.100.191` **non** si assegna: è il broadcast.

</details>

### 1.5 ✏️ Pratica · 🔍 · 🎯 Da provare — Trecento dispositivi

**Consegna.** Una sede ha 300 dispositivi. Quale prefisso scegli? Quanti host ordinari restano liberi nel blocco?

<details>
<summary>🃏 <b>1.5 — Soluzione</b></summary>

Una `/24` ha 254 host ordinari: non basta. Servono 9 bit host, perché $2^9 - 2 = 510 \ge 300$. Il prefisso è $32 - 9 = 23$: `/23`.

Host liberi nel blocco: $510 - 300 = 210$.

</details>

---

## 🧩 Dossier 2 · VLSM e collegamenti /30

*Si usa S2: dimensionare, ordinare, allineare, controllare. Il collegamento fra due router è una `/30`.*

### 📜 Caso reale: subnet tutte uguali

Nel 1985 la RFC 950 descrive come dividere una rete in sottoreti. Erano tutte della stessa misura: una sede piccola e una grande ricevevano lo stesso blocco, e lo spazio si sprecava. Dal 1993, con CIDR (RFC 1519), le misure possono cambiare.

Ponte Srl ha lo stesso problema, in versione inventata. Ha tre sedi: **Mare** (26 dispositivi), **Monte** (12) e **Valle** (5). Ogni sede ha un gateway, che conta come dispositivo. I collegamenti Mare–Monte e Monte–Valle sono `/30`. Il blocco disponibile è `172.18.20.0/24`.

### 2.1 📖 Teoria · ✅ · 🟢 Svolto — Dimensionare una sede

**Consegna.** La sede Monte ha 12 dispositivi. Quale prefisso minimo le serve? Il gateway conta.

**Svolgimento.**

1. **Conta:** $12 + 1 = 13$ dispositivi, gateway incluso.
2. **Bit host:** con 3 bit gli host utili sono $2^3 - 2 = 6$, troppi pochi. Con 4 bit sono $2^4 - 2 = 14 \ge 13$. Servono 4 bit.
3. **Prefisso:** $32 - 4 = 28$, cioè `/28`. Indirizzi nel blocco: 16. Host utili: 14.

📌 **Controllo.** $14 \ge 13$: ci sta, con un posto libero.

⚠️ **Errore comune.** Dimenticare il gateway. Una sede da 14 dispositivi sembra entrare in una `/28` (14 host utili), ma con il gateway sono 15: serve una `/27`.

### 2.2 ✏️ Pratica · ✅ · 🟢 Svolto — Il piano in quattro controlli

**Consegna.** Dimensiona le tre sedi (Mare 26, Monte 12, Valle 5 dispositivi, gateway inclusi) e i due collegamenti `/30` dentro `172.18.20.0/24`. Ordina dal più grande, assegna dall'inizio senza buchi, poi controlla il piano con i quattro controlli.

**Svolgimento.**

1. **Dimensiona.** Mare: $26 + 1 = 27$ → `/27` (30 utili). Monte: $12 + 1 = 13$ → `/28` (14 utili). Valle: $5 + 1 = 6$ → `/29` (6 utili, esattamente). Collegamenti: due `/30`.
2. **Ordina.** `/27` (32), `/28` (16), `/29` (8), `/30` (4), `/30` (4): in tutto 64 indirizzi.
3. **Assegna.** Dall'inizio dello spazio, senza buchi:

| Rete | Prefisso | Host utili | Broadcast | Gateway o router |
| --- | --- | --- | --- | --- |
| `172.18.20.0` (Mare) | `/27` | da `.1` a `.30` | `.31` | gateway Mare `.1` |
| `172.18.20.32` (Monte) | `/28` | da `.33` a `.46` | `.47` | gateway Monte `.33` |
| `172.18.20.48` (Valle) | `/29` | da `.49` a `.54` | `.55` | gateway Valle `.49` |
| `172.18.20.56` (Mare–Monte) | `/30` | `.57` e `.58` | `.59` | Mare `.57`, Monte `.58` |
| `172.18.20.60` (Monte–Valle) | `/30` | `.61` e `.62` | `.63` | Monte `.61`, Valle `.62` |

4. **Controlli.**
   - **Capienza:** 26 ≤ 30, 12 ≤ 14, 5 ≤ 6, 2 ≤ 2 per ogni collegamento.
   - **Allineamento:** 0 è multiplo di 32; 32 di 16; 48 di 8; 56 e 60 di 4.
   - **Non sovrapposizione:** 0-31, 32-47, 48-55, 56-59, 60-63: nessun intervallo entra in un altro.
   - **Tracciabilità:** ogni riga ha rete, prefisso, intervallo, broadcast e gateway.

📌 **Spazio libero.** Restano `172.18.20.64` - `172.18.20.255`.

⚠️ **Errore comune.** Sommare le dimensioni e pensare che il piano sia giusto. Un blocco non allineato lascia buchi che nessuno può usare.

🧠 <u>Prima si dimensiona ogni rete; poi si assegnano gli indirizzi, dal più grande.</u>

### 2.3 ✏️ Pratica · 🔍 · 🎯 Da provare — Il collegamento sbagliato

**Consegna.** Il collegamento Mare–Monte dovrebbe stare in `172.18.20.56/30`. Un tecnico propone `172.18.20.58/30`, con router Mare a `.59` e router Monte a `.60`. Trova gli errori: rete, host e broadcast del blocco, e chi occupa quali indirizzi.

<details>
<summary>🃏 <b>2.3 — Soluzione</b></summary>

Il `58` sta nel blocco 56-59: la rete corretta è `172.18.20.56/30`, con host `.57` e `.58` e broadcast `.59`.

- **Errore 1:** `.59` è il broadcast, non si assegna a un router.
- **Errore 2:** `.60` è la rete del collegamento Monte–Valle, cioè un altro blocco.

Il piano giusto: Mare `.57`, Monte `.58`.

</details>

### 2.4 📖 Teoria · 🔍 · 🎯 Da provare — Perché un /30

**Consegna.** In una frase per ciascuna domanda:

- (a) Perché un collegamento fra due router ha una `/30`?
- (b) Quanti indirizzi si sprecherebbero se per il collegamento Mare–Monte usassi una `/27`?
- (c) Perché il gateway si conta fra i dispositivi di una sede?

<details>
<summary>🃏 <b>2.4 — Soluzione</b></summary>

- (a) Perché i due apparati sono due: servono due host, più la rete e il broadcast, cioè quattro indirizzi.
- (b) Una `/27` ha 32 indirizzi; ne servono 2. Se ne sprecano 30.
- (c) Il gateway è un dispositivo della sede: occupa un indirizzo host della sua rete.

🧠 <u>Un collegamento fra router occupa spazio come una rete: 4 indirizzi, 2 usabili.</u>

</details>

---

## 🌐 Dossier 3 · IPv6: lo spazio nuovo

*Si usa S3: notazione, compressione, prefisso `/64`, tipi di indirizzo.*

### 📜 Caso reale: lo spazio che finisce

Il 3 febbraio 2011 la IANA, l'ente che distribuisce i grandi blocchi di indirizzi, assegna gli ultimi blocchi liberi di IPv4 ai registri regionali. Il 6 giugno 2012 il *World IPv6 Launch* porta IPv6 in modo permanente su grandi fornitori e siti. Il NAT ha tamponato per anni: IPv6 è la soluzione strutturale, ma IPv4 non è ancora sparito.

### 3.1 📖 Teoria · ✅ · 🟢 Svolto — Comprimere un indirizzo

**Consegna.** Comprimi `2001:0db8:0000:0000:0000:0a00:0005:0010`.

**Svolgimento.**

1. **Gruppi.** `2001` · `0db8` · `0000` · `0000` · `0000` · `0a00` · `0005` · `0010`: sono 8.
2. **Zeri iniziali.** Tolti da ogni gruppo: `2001` · `db8` · `0` · `0` · `0` · `a00` · `5` · `10`.
3. **Sequenza di zeri.** I tre gruppi `0` consecutivi diventano `::`.
4. **Risultato.** `2001:db8::a00:5:10`.

📌 **Controllo.** Restano 5 gruppi visibili (`2001`, `db8`, `a00`, `5`, `10`) più i tre zeri: 8 in tutto.

⚠️ **Errore comune.** Togliere zeri in mezzo a un gruppo: `0a00` diventa `a00`, non `a0`.

🧠 <u>Si tolgono gli zeri iniziali di ogni gruppo; una sola sequenza di zeri diventa `::`.</u>

### 3.2 ✏️ Pratica · ✅ · 🟢 Svolto — Rete di un indirizzo

**Consegna.** Per `2001:db8:4f2a:17:5c1e:9d3b:7a20:4e81/64` scrivi: (a) la rete, nella forma `prefisso::/64`; (b) quanti gruppi appartengono alla rete; (c) quanti indirizzi contiene una rete così.

**Svolgimento.**

1. **Rete.** I primi 64 bit sono i primi 4 gruppi: `2001:db8:4f2a:17::/64`.
2. **Gruppi di rete.** 4, cioè $4 \times 16 = 64$ bit.
3. **Indirizzi.** $2^{64}$, circa 18 miliardi di miliardi.

📌 **Controllo.** Il `/64` non vuol dire 64 host: vuol dire 64 bit di rete.

### 3.3 ✏️ Pratica · 🔍 · 🎯 Da provare — Trova l'errore

**Consegna.** Un collega scrive tre indirizzi. Per ognuno dì se è valido; se non lo è, quale regola viola.

a) `2001:db8::1::5`
b) `2001:db8:0:0:0:0:0:0:1`
c) `2001:db8::a00:5:10`

<details>
<summary>🃏 <b>3.3 — Soluzione</b></summary>

- a) **Non valido.** Il `::` compare due volte: non si capisce quanti zeri stanno in ciascun punto.
- b) **Non valido.** Contando i gruppi sono 9 (`2001`, `db8`, sei zeri, `1`): gli indirizzi IPv6 hanno 8 gruppi.
- c) **Valido.** Un solo `::`, otto gruppi in tutto.

</details>

### 3.4 📖 Teoria · 🔍 · 🎯 Da provare — Vero o falso?

1. Con 128 bit il prefisso non serve più. 
2. Un `/64` significa 64 host.
3. IPv4 ha circa 4,3 miliardi di indirizzi.
4. In IPv6 il `::` si può usare più volte.
5. Una rete locale tipica usa un `/64`.

<details>
<summary>🃏 <b>3.4 — Soluzione</b></summary>

1. **F.** Il prefisso resta: dice dove finisce la rete. Cambia la lunghezza dell'indirizzo.
2. **F.** `/64` sono 64 bit di rete; gli indirizzi possibili sono $2^{64}$.
3. **V.** $2^{32} = 4\,294\,967\,296$.
4. **F.** Una sola volta, per non creare ambiguità.
5. **V.** È la prassi comune, non un obbligo del protocollo.

</details>

### 3.5 ✏️ Pratica · ✅ · 🎯 Da provare — Che tipo è?

**Consegna.** Scrivi il tipo di ciascun indirizzo: globale, link-local o multicast.

a) `2001:db8:a::7`
b) `fe80::a1`
c) `ff02::2`

<details>
<summary>🃏 <b>3.5 — Soluzione</b></summary>

- a) **Globale.** Il prefisso `2001:db8::/32` è quello della documentazione: nel quaderno lo leggi come un indirizzo pubblico, che nelle reti reali sarebbe globale.
- b) **Link-local.** Il prefisso `fe80::/10` vale solo sul tratto di rete locale.
- c) **Multicast.** `ff02::2` è il gruppo di tutti i router del collegamento locale.

</details>

---

## 🧭 Dossier 4 · Router e tabella

*Si usa S4: router, gateway, tabella, prossimo passo, rotta predefinita, prefisso più lungo.*

### 📜 Caso reale: il prefisso più lungo vince

Il 24 febbraio 2008, secondo la ricostruzione del RIPE NCC, un provider pakistano annuncia nel mondo un prefisso `/24` (208.65.153.0/24) più specifico di quello legittimo di YouTube (208.65.152.0/22). Per la regola del prefisso più lungo, il traffico verso YouTube viene attirato dal provider sbagliato, per un tempo limitato.

Il meccanismo è quello di S4: <u>il prefisso più lungo vince, anche quando è sbagliato.</u>

### Scenario: il router R della sede centrale

Il router R della sede centrale di Ponte Srl (inventato; diverso dalla topologia dei dossier 2 e 5) ha questa tabella:

| Rete di destinazione | Prefisso | Prossimo passo | Uscita |
| --- | --- | --- | --- |
| `172.18.100.0` | `/24` | collegata | Amministrazione |
| `172.18.101.0` | `/24` | collegata | Server |
| `172.18.102.0` | `/24` | collegata | Magazzino |
| `198.51.100.0` | `/30` | collegata | verso il provider (`198.51.100.2`) |
| `0.0.0.0` | `/0` | `198.51.100.1` | verso il provider |

### 4.1 📖 Teoria · ✅ · 🟢 Svolto — Quale riga, quale direzione

**Consegna.** Per ciascun pacchetto scrivi la riga scelta e il prossimo passo:

- (a) destinazione `172.18.101.9` (Server);
- (b) destinazione `172.18.103.5`;
- (c) destinazione `8.8.8.8` (indirizzo pubblico reale, usato come destinazione esterna).

**Svolgimento.**

- (a) Corrisponde `172.18.101.0/24`: la rete Server è collegata direttamente. Nessun vicino.
- (b) Nessuna riga più stretta contiene `172.18.103.5`. Resta solo `0.0.0.0/0`: prossimo passo `198.51.100.1`.
- (c) Solo `0.0.0.0/0`: prossimo passo `198.51.100.1`.

📌 **Controllo.** Un `/24` contiene 256 indirizzi: da `172.18.101.0` a `172.18.101.255`. Il `.9` ci sta.

⚠️ **Errore comune.** Scrivere `8.8.8.8` come prossimo passo. Il prossimo passo è il vicino: per `8.8.8.8` è `198.51.100.1`.

🧠 <u>Il router decide solo il passo successivo; il resto lo decidono i router vicini.</u>

### 4.2 ✏️ Pratica · ✅ · 🟢 Svolto — La riga più stretta

**Consegna.** Alla tabella di R viene aggiunta una riga inventata, `172.18.0.0/16` verso `198.51.100.1`. Per `172.18.101.9` e per `172.18.103.5` scrivi quali righe contengono l'indirizzo e quale vince.

**Svolgimento.**

| Riga | Prefisso | Contiene `172.18.101.9`? | Contiene `172.18.103.5`? |
| --- | --- | --- | --- |
| `172.18.101.0` | `/24` | sì | no |
| `172.18.0.0` | `/16` | sì | sì |
| `0.0.0.0` | `/0` | sì | sì |

1. Per `172.18.101.9` vince `/24`: è la riga con il prefisso più lungo.
2. Per `172.18.103.5` vince `/16`, più stretta di `/0`.
3. Il prossimo passo di `/16` è `198.51.100.1`, lo stesso della predefinita: la direzione non cambia.

📌 **Controllo.** Più il prefisso è lungo, più la riga è stretta e vince.

🧠 <u>Vince la riga più stretta; se due righe portano allo stesso vicino, la scelta non cambia la strada.</u>

### 4.3 ✏️ Pratica · 🔍 · 🎯 Da provare — Disegna il percorso

**Consegna.** Un PC del Magazzino (`172.18.102.20`, gateway `172.18.102.1`) scrive a un PC dell'Amministrazione (`172.18.100.5`). Scrivi: (1) la riga che R sceglie per la destinazione; (2) il prossimo passo; (3) se il pacchetto esce verso il provider.

<details>
<summary>🃏 <b>4.3 — Soluzione</b></summary>

1. La riga `172.18.100.0/24`, collegata direttamente.
2. Nessun vicino: R consegna il pacchetto sulla rete Amministrazione.
3. **No.** Il pacchetto passa da R, che è il gateway del Magazzino, ma non esce verso il provider.

</details>

### 4.4 📖 Teoria · 🔍 · 🎯 Da provare — Vero o falso?

1. Lo switch sceglie la strada fra reti diverse.
2. Il prossimo passo è sempre la destinazione finale.
3. La rotta predefinita contiene tutta Internet.
4. Un router conosce solo le righe della sua tabella.
5. Se due righe corrispondono, vince quella con il prefisso più lungo.

<details>
<summary>🃏 <b>4.4 — Soluzione</b></summary>

1. **F.** Lo switch lavora dentro una sola rete. Fra reti diverse decide il router.
2. **F.** È il vicino a cui consegnare il pacchetto.
3. **F.** La rotta predefinita è usata solo quando nessun'altra riga corrisponde.
4. **V.**
5. **V.**

</details>

### 4.5 ✏️ Pratica · 🔍 · 🎯 Da provare — La riga che manca

**Consegna.** Il router Q della sede Valle ha solo due righe: `172.18.100.0/24` e `172.18.101.0/24`, e nessuna rotta predefinita. Q è collegato a R sulla rete `172.18.103.0/30` (Q ha `172.18.103.2`, R ha `172.18.103.1`). Un pacchetto per `8.8.8.8` non trova riga. Scrivi la riga che lo manda verso R, con prefisso e prossimo passo, poi fai il controllo.

<details>
<summary>🃏 <b>4.5 — Soluzione</b></summary>

Riga: `0.0.0.0/0`, prossimo passo `172.18.103.1`.

Controllo: `172.18.103.1` sta in `172.18.103.0/30`, rete collegata direttamente a Q. Il prossimo passo è raggiungibile.

⚠️ **Errore comune:** scrivere `8.8.8.8/32`. Vale solo per quella destinazione: per tutto il resto il pacchetto si fermerebbe di nuovo.

</details>

---

## 🛣️ Dossier 5 · Rotte statiche e default route

*Si usa S5: rotta = rete + prefisso + prossimo passo; controllo a due passi; rotta predefinita.*

Ponte Srl usa la topologia del dossier 2, con i valori del piano:

- sede Mare `172.18.20.0/27`, router M con LAN `.1` e collegamento `.57`;
- sede Monte `172.18.20.32/28`, router N con LAN `.33`, collegamento verso M `.58` e verso V `.61`;
- sede Valle `172.18.20.48/29`, router V con LAN `.49` e collegamento verso N `.62`;
- collegamenti `172.18.20.56/30` (M–N) e `172.18.20.60/30` (N–V).

### 📜 Caso inventato: la sede Valle non risponde

Lunedì mattina il PC di Valle, `172.18.20.50`, non raggiunge il server di Mare. Le tabelle sono scritte a mano: nessuno le ha aggiornate dopo l'ultima modifica. Valori inventati.

### 5.1 📖 Teoria · ✅ · 🟢 Svolto — Scrivere una rotta

**Consegna.** Sul router M scrivi la rotta verso la sede Valle (`172.18.20.48/29`). Il pacchetto passa per N. Scrivi rete, prefisso e prossimo passo, poi fai il controllo a due passi.

**Svolgimento.**

1. **Rete e prefisso:** `172.18.20.48/29`.
2. **Prossimo passo:** l'indirizzo di N sul collegamento che M vede, cioè `172.18.20.58`.
3. **Controllo 1:** `172.18.20.58` sta in `172.18.20.56/30`, collegato a M. È raggiungibile.
4. **Controllo 2:** la riga è scritta sul router che vede quel collegamento, cioè M.

Rotta: `172.18.20.48/29` → `172.18.20.58`.

📌 **Controllo.** Il prossimo passo è il vicino (N), non il PC di Valle.

⚠️ **Errore comune.** Scrivere come prossimo passo l'indirizzo del proprio router (`172.18.20.57` per M).

### 5.2 ✏️ Pratica · ✅ · 🟢 Svolto — Completare la tabella di N

**Consegna.** La tabella di N ha tre righe già scritte: sede Monte e i due collegamenti (tutte collegate direttamente). Completa le due righe mancanti: sede Mare `172.18.20.0/27` e sede Valle `172.18.20.48/29`. Per ciascuna scrivi il prossimo passo e il controllo.

**Svolgimento.**

- `172.18.20.0/27` (Mare) → `172.18.20.57`, il router M. Controllo: `.57` sta in `172.18.20.56/30`, collegato a N.
- `172.18.20.48/29` (Valle) → `172.18.20.62`, il router V. Controllo: `.62` sta in `172.18.20.60/30`, collegato a N.

| Rete | Prefisso | Prossimo passo |
| --- | --- | --- |
| `172.18.20.32` (Monte) | `/28` | collegata |
| `172.18.20.56` (M–N) | `/30` | collegata |
| `172.18.20.60` (N–V) | `/30` | collegata |
| `172.18.20.0` (Mare) | `/27` | `172.18.20.57` |
| `172.18.20.48` (Valle) | `/29` | `172.18.20.62` |

📌 **Controllo.** Il prossimo passo di ogni riga è raggiungibile da N.

🧠 <u>Il prossimo passo sta sempre su una rete che il router vede già.</u>

### 5.3 ✏️ Pratica · 🔍 · 🎯 Da provare — Trova l'errore

**Consegna.** Sul router M il tecnico scrive: rete `172.18.20.48`, prefisso `/29`, prossimo passo `172.18.20.62`. Quale controllo fallisce, e perché?

<details>
<summary>🃏 <b>5.3 — Soluzione</b></summary>

Fallisce il **controllo 1**. `172.18.20.62` sta in `172.18.20.60/30`, che M non vede: M conosce solo `172.18.20.0/27` e `172.18.20.56/30`.

Correzione: prossimo passo `172.18.20.58`, il vicino N sul collegamento che M vede.

</details>

### 5.4 ✏️ Pratica · 🔍 · 🎯 Da provare — Prevedi la riga

**Consegna.** Il router N ha, oltre alle sue righe, la rotta predefinita `0.0.0.0/0` verso `172.18.20.57` (M, che esce verso il provider). Per ciascun indirizzo scrivi prima la riga scelta da N e il prossimo passo: `172.18.20.40`, `172.18.20.50`, `8.8.8.8`.

<details>
<summary>🃏 <b>5.4 — Soluzione</b></summary>

- `172.18.20.40` → `172.18.20.32/28`, collegata: consegna diretta sulla LAN di Monte.
- `172.18.20.50` → `172.18.20.48/29`, prossimo passo `172.18.20.62`. È la riga più stretta: vince su `/0`.
- `8.8.8.8` → solo `0.0.0.0/0`, prossimo passo `172.18.20.57`.

⚠️ **Errore comune.** Scegliere la predefinita per `172.18.20.50` perché «è la riga generale». La rotta predefinita vince solo quando nessun'altra riga corrisponde.

</details>

### 5.5 📖 Teoria · 🔍 · 🎯 Da provare — Perché una default route su Valle

**Consegna.** In una frase: perché il router V può avere una sola rotta predefinita, `0.0.0.0/0` verso `172.18.20.61`, invece di una riga per ogni sede?

<details>
<summary>🃏 <b>5.5 — Soluzione</b></summary>

V ha un solo collegamento verso il resto della rete, quello con N. Tutto ciò che non sta nella sua LAN va a N, che sa come proseguire: una riga sola basta. Il prossimo passo `172.18.20.61` sta in `172.18.20.60/30`, collegato a V.

</details>

---

## 🔁 Dossier 6 · Distance Vector e Link State

*Si usa S6: passaparola contro mappa, costo, convergenza. Nessuna configurazione.*

### 📜 Caso reale: la ARPANET cambia metodo

Nei primi anni la ARPANET usa un metodo di tipo passaparola (**Distance Vector**): ogni nodo dice ai vicini quanto costa arrivare a ogni destinazione. Il metodo reagisce lentamente ai guasti e può far girare i messaggi per un po' in tondo. Nel 1979 la rete passa a un algoritmo basato sulla mappa dei collegamenti (**Link State**), descritto nel 1980 da McQuillan, Richer e Rosen.

Per i dossier 6 usiamo un triangolo inventato con costi inventati: **A–B costa 2**, **B–C costa 3**, **A–C costa 7**. Il costo è un numero che misura quanto conviene un percorso, non una velocità.

### 6.1 📖 Teoria · ✅ · 🟢 Svolto — Il passaparola di A

**Consegna.** A riceve da B la frase «so andare a C con costo 3». Il collegamento A–B costa 2. A ha anche il collegamento diretto A–C, che costa 7. Quale strada sceglie A per C, e con quale costo?

**Svolgimento.**

1. **Via B:** costo di A–B più quello annunciato da B: $2 + 3 = 5$.
2. **Diretta:** 7.
3. **Scelta:** il costo minore, 5, passando da B.

📌 **Controllo.** Il costo di un percorso è la somma dei costi dei collegamenti attraversati.

⚠️ **Errore comune.** Sommare solo il costo di B–C, dimenticando quello di A–B.

🧠 <u>Distance Vector: A non conosce la strada, conosce ciò che gli dicono i vicini.</u>

### 6.2 ✏️ Pratica · ✅ · 🟢 Svolto — La mappa di A

**Consegna.** Con Link State, A conosce la mappa: tre router e tre collegamenti (A–B 2, B–C 3, A–C 7). Calcola il percorso migliore da A a C.

**Svolgimento.**

1. **Percorsi possibili:** A → C diretto (7); A → B → C (5).
2. **Migliore:** A → B → C, costo 5.

📌 **Controllo.** Lo stesso calcolo, fatto da C verso A, dà C → B → A con costo 5: le strade sono coerenti perché la mappa è la stessa per tutti.

🧠 <u>Link State: tutti hanno la stessa mappa; ognuno calcola da sé la propria strada.</u>

### 6.3 ✏️ Pratica · 🔍 · 🎯 Da provare — Prevedi il guasto

**Consegna.** Cade il collegamento A–B. Per ciascun principio scrivi quale percorso usa A per arrivare a C e con quale costo.

<details>
<summary>🃏 <b>6.3 — Soluzione</b></summary>

- **Link State:** A riceve l'annuncio della caduta, toglie A–B dalla mappa e ricalcola. Resta solo il diretto A–C: costo 7.
- **Distance Vector:** A non ha più la riga «C via B, costo 5». Usa quella diretta, che conosce dal proprio collegamento: costo 7.

Il risultato finale coincide. Cambia il tempo: il Distance Vector può usare per un po' la notizia vecchia prima di correggerla.

</details>

### 6.4 📖 Teoria · 🔍 · 🎯 Da provare — Notizie vecchie

**Consegna.** In due frasi: perché un router Distance Vector può usare una notizia vecchia? Perché un Link State ha meno questo problema?

<details>
<summary>🃏 <b>6.4 — Soluzione</b></summary>

Il Distance Vector sa solo ciò che dicono i vicini: ogni notizia fa tappe di vicino in vicino, e nel frattempo qualcuno può non essere aggiornato.

Il Link State riceve l'annuncio del collegamento caduto, che arriva a tutti, e ognuno ricalcola sulla mappa. Non elimina il ritardo: serve tempo per la convergenza.

</details>

### 6.5 📖 Teoria · ✅ · 🎯 Da provare — Vero o falso?

1. Un Link State conosce solo i propri vicini.
2. Un Distance Vector conosce la mappa completa.
3. Nel routing la «distanza» è un costo, non una velocità.
4. La convergenza è il momento in cui tutti i router hanno la stessa informazione aggiornata.

<details>
<summary>🃏 <b>6.5 — Soluzione</b></summary>

1. **F.** Il Link State conosce la mappa completa.
2. **F.** Il Distance Vector sa solo ciò che gli dicono i vicini.
3. **V.** Un collegamento a costo basso non è necessariamente veloce.
4. **V.**

</details>

---

## 🧠 Dossier 7 · Livello finale: ripasso mescolato

*Si usa S7: tutti i temi insieme, senza indicare il metodo. Nessun argomento nuovo: è un ripasso, non una verifica.*

### 📜 Caso inventato: lunedì a Ponte Srl

Lunedì alle 8:00 la segreteria chiama. Ti trovi tre ticket sul tavolo. Nessuno ti dice quale metodo usare: prima guarda i dati, poi scegli. Valori inventati.

### 7.1 ✏️ Base · ✅ · 🎯 Da provare — Ticket 1: l'indirizzo del PC

**Consegna.** Un PC ha `172.18.122.77/23`. Scrivi rete, broadcast, primo e ultimo host, host ordinari.

<details>
<summary>🃏 <b>7.1 — Soluzione</b></summary>

Salto nel terzo ottetto: $256 - 254 = 2$. Il `122` è multiplo di 2: rete `172.18.122.0/23`. Broadcast `172.18.123.255`. Host da `172.18.122.1` a `172.18.123.254`. Host ordinari: $2^9 - 2 = 510$.

</details>

### 7.2 ✏️ Medio · 🔍 · 🎯 Da provare — Ticket 2: la sede nuova

**Consegna.** Ponte Srl apre una sede **Nuova** con 100 dispositivi, una sede con 50 e una con 20, gateway inclusi nel conteggio (quindi 101, 51 e 21). Dentro `172.18.60.0/24` assegna i blocchi, dal più grande. Aggiungi anche un collegamento `/30` fra la sede da 50 e quella da 20. Scrivi la tabella con rete, prefisso, intervallo, broadcast e gateway.

<details>
<summary>🃏 <b>7.2 — Soluzione</b></summary>

- **Dimensiona:** 101 → `/25` (126 utili); 51 → `/26` (62 utili); 21 → `/27` (30 utili); collegamento → `/30`.
- **Ordina:** 128, 64, 32, 4: in tutto 228 indirizzi, meno di 256.
- **Assegna:**

| Rete | Prefisso | Host utili | Broadcast | Gateway |
| --- | --- | --- | --- | --- |
| `172.18.60.0` (Nuova) | `/25` | da `.1` a `.126` | `.127` | `.1` |
| `172.18.60.128` (sede da 50) | `/26` | da `.129` a `.190` | `.191` | `.129` |
| `172.18.60.192` (sede da 20) | `/27` | da `.193` a `.222` | `.223` | `.193` |
| `172.18.60.224` (collegamento) | `/30` | `.225` e `.226` | `.227` | sede da 50 `.225`, sede da 20 `.226` |

📌 **Controllo.** Ogni blocco parte da un multiplo della sua dimensione (0, 128, 192, 224). Spazio libero: `172.18.60.228` - `172.18.60.255`.

</details>

### 7.3 ✏️ Avanzato · 🔍 · 🎯 Da provare — Ticket 3: il pacchetto che non arriva

**Consegna.** Il router V (Valle) della topologia del dossier 5 ha queste righe: `172.18.20.48/29` collegata e `172.18.20.60/30` collegata. Nessuna rotta predefinita. Un PC di Valle (`172.18.20.50`) scrive a un PC di Mare (`172.18.20.20`).

1. Quale riga sceglie V per `172.18.20.20`?
2. Quale riga manca? Scrivila con prefisso e prossimo passo.
3. Che cosa succede al pacchetto se la riga non c'è?

<details>
<summary>🃏 <b>7.3 — Soluzione</b></summary>

1. Nessuna: `172.18.20.20` non sta né in `/29` (da `.48` a `.55`) né in `/30` (da `.60` a `.63`). V non sa dove mandarlo.
2. Riga mancante: `172.18.20.0/27` con prossimo passo `172.18.20.61`, il router N. Controllo: `.61` sta in `172.18.20.60/30`, collegato a V.
3. Il pacchetto viene scartato sul router V. Anche una rotta predefinita verso `172.18.20.61` sarebbe andata bene, come nel dossier 5.5.

</details>

### 🩹 Recupero: dove riprendere

Il recupero non è un voto: è tornare al punto giusto. Quando un esercizio non torna, parti dall'errore.

| Se ti trovi in questo punto | Riprendi |
| --- | --- |
| non sai quanti indirizzi ha un prefisso | [S1 nov-dic](%28STU%29%204DI%20nov-dic%20S1%20-%20CIDR%20e%20subnetting.md) e [S5 sett-ott](../1%20SETT-OTT/%28STU%29%204DI%20sett-ott%20S5%20-%20CIDR%20e%20intervalli.md) |
| due blocchi si sovrappongono, o un broadcast è sbagliato | [S2 nov-dic](%28STU%29%204DI%20nov-dic%20S2%20-%20VLSM.md) e [S6 sett-ott](../1%20SETT-OTT/%28STU%29%204DI%20sett-ott%20S6%20-%20VLSM%20e%20progettazione.md) |
| un IPv6 che non si comprime | [S3 nov-dic](%28STU%29%204DI%20nov-dic%20S3%20-%20IPv6.md) |
| il router sceglie la riga sbagliata | [S4 nov-dic](%28STU%29%204DI%20nov-dic%20S4%20-%20Router%20e%20tabelle%20di%20routing.md) |
| il prossimo passo non sta nella rete collegata | [S5 nov-dic](%28STU%29%204DI%20nov-dic%20S5%20-%20Routing%20statico.md) |
| confondi passaparola e mappa | [S6 nov-dic](%28STU%29%204DI%20nov-dic%20S6%20-%20Introduzione%20al%20routing%20dinamico.md) |

🔧 **In laboratorio:** la topologia di Ponte Srl si ricostruisce sugli apparati. Qui solo carta e matita.

---

## 📚 Fonti e risorse

- [RFC 950 - Internet Standard Subnetting Procedure](https://www.rfc-editor.org/rfc/rfc950) (1985): come dividere una rete in sottoreti. Basta l'introduzione.
- [RFC 1519 - Classless Inter-Domain Routing (CIDR)](https://www.rfc-editor.org/rfc/rfc1519) (1993): la base del prefisso `/n`. Per il caso del dossier 1, leggi l'introduzione.
- [RFC 1918 - Address Allocation for Private Internets](https://www.rfc-editor.org/rfc/rfc1918) e [RFC 5737 - IPv4 Address Blocks Reserved for Documentation](https://www.rfc-editor.org/rfc/rfc5737): perché `172.18.x.x` è privato e `198.51.100.0/30` è di documentazione.
- [RFC 4291 - IPv6 Addressing Architecture](https://www.rfc-editor.org/rfc/rfc4291) e [RFC 5952 - Text Representation of IPv6 Addresses](https://www.rfc-editor.org/rfc/rfc5952): tipi di indirizzo e regole di compressione con `::`. La seconda si legge in pochi minuti.
- [RFC 3849 - Documentation Prefix 2001:db8::/32](https://www.rfc-editor.org/rfc/rfc3849): perché gli esempi IPv6 usano `2001:db8`.
- [IPv4 address exhaustion (Wikipedia)](https://en.wikipedia.org/wiki/IPv4_address_exhaustion): la storia degli ultimi blocchi IPv4 assegnati nel 2011, in inglese.
- [World IPv6 Launch](https://www.worldipv6launch.org/): il lancio del 6 giugno 2012, con gli aggiornamenti dei fornitori.
- [RIPE NCC - YouTube Hijacking: A RIPE NCC RIS case study](https://www.ripe.net/about-us/news/youtube-hijacking-a-ripe-ncc-ris-case-study/): il caso del 2008 raccontato dal registro europeo, con i prefissi veri. Per il dossier 4, leggi la parte sul prefisso più specifico.
- [ARPANET (Wikipedia)](https://en.wikipedia.org/wiki/ARPANET): il messaggio del 1969 e il passaggio al nuovo algoritmo di routing alla fine degli anni Settanta.
- McQuillan, Richer, Rosen, *The New Routing Algorithm for the ARPANET*, IEEE Transactions on Communications, 1980: l'articolo originale sul passaggio al Link State. Per consultazione.
- [RFC 1058 - RIP](https://www.rfc-editor.org/rfc/rfc1058) e [RFC 2328 - OSPF](https://www.rfc-editor.org/rfc/rfc2328): solo per i nomi dei protocolli, in 🤓.

**Come usarle.** Per i casi reali leggi solo la parte che riguarda il prefisso o il metodo. Le RFC si consultano: non serve leggerle per intero.

**Valori.** Ponte Srl, le sue sedi e tutti i numeri degli esercizi sono inventati. I casi reali sono descritti con le date e i fatti delle fonti.

---

⬅️ [S7 - Ripasso e recupero](%28STU%29%204DI%20nov-dic%20S7%20-%20Ripasso%20e%20recupero.md) · 🏠 [Indice](../README.md)
