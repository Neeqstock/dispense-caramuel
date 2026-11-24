⬅️ [Eserciziario](./%28STU%29%204DI%20nov-dic%20-%20Eserciziario.md) · 📖 [S1 - IPv6](./%28STU%29%204DI%20nov-dic%20S1%20-%20IPv6.md) · 🏠 [Indice](../README.md)

# 🌐 Esercizi extra · Dossier 1 (IPv6)

**4DI · Novembre-Dicembre · S1 · Pratica e teoria aggiuntiva**

Questi esercizi integrano il **Dossier 1** dell'[Eserciziario](./%28STU%29%204DI%20nov-dic%20-%20Eserciziario.md) usando esclusivamente gli argomenti di [S1 - IPv6](./%28STU%29%204DI%20nov-dic%20S1%20-%20IPv6.md). Tutti gli indirizzi «pubblici» usano il blocco riservato alla documentazione `2001:db8::/32` (RFC 3849).

> **Legenda:** ✅ da sapere · 🔍 per capire fino in fondo · 🤓 facoltativo · ✏️ pratica scritta · 📖 teoria · 🕵️ scenario · 🎯 da provare · 🃏 soluzione nascosta

---

### 1.4 ✏️ Pratica · ✅ · 🎯 Da provare — Comprimere quattro indirizzi (occhio agli zeri!)

**Consegna.** Riscrivi ciascun indirizzo IPv6 nella forma **compressa più corta possibile**. Ricorda che gli zeri a destra dentro un gruppo non si cancellano mai, e che `::` può apparire una sola volta.

- **A)** `2001:0db8:1200:0000:0000:0000:0000:0b00`
- **B)** `fe80:0000:0000:0000:0200:5eff:fe00:0050`
- **C)** `2001:0db8:00a0:0000:0000:0004:0000:0010`
- **D)** `0000:0000:0000:0000:0000:0000:0000:0001`

<details>
<summary>🃏 <b>1.4 — Soluzione</b></summary>

- **A)** **`2001:db8:1200::b00`** — Si tolgono gli zeri iniziali (`0db8` → `db8`, `0b00` → `b00`, ma `1200` e `b00` conservano gli zeri finali) e i quattro gruppi `0` centrali diventano `::`. Controllo: 4 gruppi scritti + 4 in `::` = 8.
- **B)** **`fe80::200:5eff:fe00:50`** — `0200` diventa `200`, `0050` diventa `50`, mentre `fe00` resta `fe00`. I tre `0` dopo `fe80` diventano `::`. Controllo: 5 gruppi scritti + 3 in `::` = 8.
- **C)** **`2001:db8:a0::4:0:10`** — Ci sono due sequenze di zeri separate (`0:0` e un singolo `0`): si sostituisce con `::` la fila più lunga (i due `0` centrali), lasciando l'altro `0` scritto. Controllo: 6 gruppi scritti + 2 in `::` = 8.
- **D)** **`::1`** — È l'indirizzo di *loopback*: sette gruppi a zero a sinistra diventano `::` e resta `1`. Controllo: 1 gruppo scritto + 7 in `::` = 8.

</details>

---

### 1.5 ✏️ Pratica · ✅ · 🎯 Da provare — Espandere per esteso (32 cifre esadecimali)

**Consegna.** Fai l'operazione inversa: espandi ciascun indirizzo nella forma completa con **tutti gli 8 gruppi da 4 cifre esadecimali**.

- **A)** `2001:db8:5::1a`
- **B)** `fe80::1:20`
- **C)** `ff02::2`
- **D)** `2001:db8:0:30::/64` *(scrivi per esteso l'indirizzo di rete, mantenendo `/64` alla fine)*

<details>
<summary>🃏 <b>1.5 — Soluzione</b></summary>

- **A)** **`2001:0db8:0005:0000:0000:0000:0000:001a`** (4 gruppi visibili → `::` vale 4 gruppi di `0000`).
- **B)** **`fe80:0000:0000:0000:0000:0000:0001:0020`** (3 gruppi visibili → `::` vale 5 gruppi di `0000`).
- **C)** **`ff02:0000:0000:0000:0000:0000:0000:0002`** (2 gruppi visibili → `::` vale 6 gruppi di `0000`).
- **D)** **`2001:0db8:0000:0030:0000:0000:0000:0000/64`** (4 gruppi visibili → `::` vale 4 gruppi di `0000`).

</details>

---

### 1.6 ✏️ Pratica · 🔍 · 🎯 Da provare — Stessa rete `/64` o reti diverse?

**Consegna.** Un server di laboratorio si trova nella rete **`2001:db8:a0:4::/64`**. Per ciascuno dei quattro indirizzi qui sotto, stabilisci se appartiene alla **stessa rete `/64`** del server oppure a una **rete diversa**, motivando la risposta in una riga.

- **A)** `2001:db8:a0:4::99`
- **B)** `2001:db8:a0:4:1::5`
- **C)** `2001:db8:a0::4:5`
- **D)** `2001:db8:a0:40::1`

<details>
<summary>🃏 <b>1.6 — Soluzione</b></summary>

In una `/64` contano i **primi 4 gruppi** (`2001:0db8:00a0:0004`).

- **A) Stessa rete.** I primi 4 gruppi sono esattamente `2001:db8:a0:4`.
- **B) Stessa rete.** I primi 4 gruppi sono `2001:db8:a0:4`; il `:1::5` che segue fa parte dei 64 bit dell'interfaccia.
- **C) Rete diversa.** Espandendolo diventa `2001:0db8:00a0:0000:0000:0000:0004:0005`: il 4° gruppo è `0000`, non `0004`! Appartiene alla rete `2001:db8:a0:0::/64`.
- **D) Rete diversa.** Il 4° gruppo è `0040`, non `0004` (gli zeri a destra cambiano il valore del gruppo).

</details>

---

### 1.7 ✏️ Pratica · 🔍 · 🎯 Da provare — Caccia all'errore nei log del firewall

**Consegna.** Durante l'analisi di un file di configurazione trovi quattro indirizzi IPv6. Per ciascuno indica se è **valido** o **non valido**:
- se **non è valido**, spiega quale regola viola;
- se **è valido**, scrivilo nella forma compressa più corta.

- **A)** `fe80::12345`
- **B)** `2001:db8:cafe:babe:1:2:3`
- **C)** `2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- **D)** `2001:db8:0:0::0::1`

<details>
<summary>🃏 <b>1.7 — Soluzione</b></summary>

- **A) Non valido.** L'ultimo gruppo `12345` ha **5 cifre esadecimali** (20 bit), mentre ogni gruppo IPv6 ha al massimo 4 cifre (16 bit).
- **B) Non valido.** Ha soltanto **7 gruppi** separati da `:` e non usa `::` per compensare il gruppo mancante.
- **C) Valido.** Ha tutti gli 8 gruppi con cifre esadecimali corrette. Compresso diventa **`2001:db8:85a3::8a2e:370:7334`**.
- **D) Non valido.** Contiene due volte `::`, rendendo ambiguo quanti gruppi a zero siano stati compressi in ciascun punto.

</details>

---

### 1.8 📖 Teoria · ✅ · 🎯 Da provare — Riconosci l'indirizzo dal prefisso

**Consegna.** Associa ciascuno di questi sei indirizzi al proprio tipo (**globale unicast**, **link-local**, **multicast**, **loopback**, **unique local**):

1. `fe80::4a2b`
2. `ff02::2`
3. `2001:db8:10::5`
4. `::1`
5. `febf::abcd`
6. `fd12:3456:789a::1` *(argomento 🤓)*

Poi rispondi a queste due domande:
- **a)** Perché su un PC Windows, lanciando `ipconfig`, il **Gateway predefinito** IPv6 inizia quasi sempre con `fe80::`?
- **b)** Perché `fe80::4a2b` non è equivalente a un indirizzo privato IPv4 come `192.168.1.10`?

<details>
<summary>🃏 <b>1.8 — Soluzione</b></summary>

1. `fe80::4a2b` → **link-local** (`fe80::/10`)
2. `ff02::2` → **multicast** (`ff00::/8`, in particolare tutti i router sul collegamento locale)
3. `2001:db8:10::5` → **globale unicast** (`2000::/3`, qui nel blocco di documentazione)
4. `::1` → **loopback**
5. `febf::abcd` → **link-local** (il blocco `fe80::/10` va da `fe80` fino a `febf`)
6. `fd12:3456:789a::1` → **unique local** (`fd00::/8`, l'equivalente IPv6 degli indirizzi privati aziendali)

- **a)** Perché il router di casa usa il proprio indirizzo *link-local* sul cavo o Wi-Fi locale per parlare con i dispositivi della stessa LAN, prima ancora (o indipendentemente) che abbiano un indirizzo globale.
- **b)** Un indirizzo privato IPv4 (`192.168.x.x`) può attraversare più router interni all'interno di un'azienda; un indirizzo *link-local* `fe80::/10` invece non supera **nemmeno il primo router**.

</details>

---

### 1.9 🕵️ Scenario · 🔍 · 🎯 Da provare — Due PC, un cavo e un collega troppo sicuro

**Consegna.** Leggi i due mini-scenari e rispondi sul quaderno:

1. **Solo cavo:** colleghi direttamente **PC-A** e **PC-B** con un cavo Ethernet, senza switch, senza router e senza configurare indirizzi a mano. Entrambi generano automaticamente un `fe80::...`. Riescono a fare `ping` tra loro usando quegli indirizzi? E se provassero a raggiungersi su `2001:db8:1::10` senza aver configurato nulla?
2. **Il collega ottimista:** in un'aula scolastica nessuno ha configurato un router IPv6, quindi un collega dice: *«Possiamo ignorare IPv6 sul firewall dei PC: senza router IPv6, due computer della stessa aula non possono proprio parlarsi in IPv6»*. Ha ragione? Spiega perché.
3. **🤓 Bonus rapido:** un compagno legge `2001:db8:1::/64` e dice che in quella rete ci stanno al massimo 64 computer. Correggilo indicando quanti indirizzi totali contiene davvero una `/64`.

<details>
<summary>🃏 <b>1.9 — Soluzione</b></summary>

1. **Con `fe80::...` sì**, perché i dispositivi moderni creano da soli l'indirizzo *link-local* appena il cavo è collegato e sul collegamento diretto non serve alcun router. **Con `2001:db8:1::10` no**, perché nessuno ha assegnato loro un prefisso globale né c'è un router che lo distribuisca.
2. **Ha torto.** I dispositivi nella stessa LAN (stesso switch o Wi-Fi) comunicano direttamente tramite i propri indirizzi *link-local* (`fe80::/10`) e *multicast* (`ff02::1`), senza aver bisogno di alcun router.
3. **`/64` indica 64 bit di rete**, non 64 host. Restano $128 - 64 = 64$ bit per le interfacce, quindi **$2^{64}$ indirizzi** (circa 18 miliardi di miliardi).

</details>

---

⬅️ [Eserciziario](./%28STU%29%204DI%20nov-dic%20-%20Eserciziario.md) · 📖 [S1 - IPv6](./%28STU%29%204DI%20nov-dic%20S1%20-%20IPv6.md) · 🏠 [Indice](../README.md)
