# 🎯 Allenamento · 3EI sett-ott

**Allenamento**, da svolgere insieme in classe. Stessa struttura, stessi argomenti e stessi punteggi della verifica; le domande sono però **diverse**: serve ragionare, non ricordare.

**Totale 10 punti (+2 facoltativi)** · ✅ base 7 · 🔍 più impegnativa 3 · ⭐ extra · **40 minuti** · nessuna calcolatrice.

| Parte | Argomento | Livello | Punti |
|---|---|---|---|
| 1 | Concetti della macchina | ✅ | 2 |
| 2 | Seguire un programma | ✅ | 3 |
| 3 | Indirizzi e capacità | ✅ | 2 |
| 4 | Programma e cache | 🔍 | 3 |
| | **Totale** | | **10** |
| ⭐ | Extra | facoltativa | +2 |

**Regole delle crocette:** una sola risposta corretta, 0,5 punti. Se sbagli, la motivazione scritta («Perché?») può recuperare fino a 0,5.

**Spazio per la discussione di gruppo:** `______________________________________________`

## Parte 1 · Concetti della macchina ✅ (2 punti)

💬 *Suggerimento: prima di guardare le opzioni, prova a dire la risposta a voce. Poi cerca quella che somiglia di più.*

### 1.1 ✅ (0,5 punti)

**Una macchina di Von Neumann deve eseguire un programma diverso da quello di prima. Che cosa serve cambiare?**

- [ ] A) I collegamenti fra CPU e memoria, che vanno rifatti per il nuovo programma.
- [ ] B) Le istruzioni scritte in memoria: l'hardware resta lo stesso.
- [ ] C) I circuiti dell'ALU, costruiti per eseguire un solo programma.
- [ ] D) I valori dei registri, perché sono loro a contenere tutto il programma.

Perché? (facoltativo) `______________________________`

### 1.2 ✅ (0,5 punti)

**Il registro R1 contiene 5. La CPU esegue `STORE [30], R1`. Che cosa succede?**

- [ ] A) Il numero 30 viene copiato nella cella di indirizzo 5; R1 non cambia.
- [ ] B) Il contenuto della cella 30 viene copiato in R1, che passa da 5 a quel valore.
- [ ] C) Il numero 5 viene spostato nella cella 30, e R1 resta quindi vuoto.
- [ ] D) Il numero 5 viene copiato nella cella 30; R1 continua a contenere 5.

Perché? (facoltativo) `______________________________`

### 1.3 ✅ (0,5 punti)

**Una CPU ha il clock a 2 GHz, un'altra a 4 GHz. Che cosa si può dire con certezza?**

- [ ] A) La seconda ha il doppio dei cicli di clock in ogni secondo.
- [ ] B) La seconda completa il doppio delle istruzioni ogni secondo.
- [ ] C) La seconda esegue ogni istruzione in metà del tempo.
- [ ] D) La seconda legge dalla RAM con una banda doppia della prima.

Perché? (facoltativo) `______________________________`

### 1.4 ✅ (0,5 punti)

**Un utente spegne il computer mentre scrive un documento che non ha ancora salvato. Perché perde il testo?**

- [ ] A) Perché la CPU cancella la memoria di massa a ogni spegnimento.
- [ ] B) Perché la RAM è troppo piccola per contenere un documento.
- [ ] C) Perché il testo era soltanto in RAM, che senza corrente perde i dati.
- [ ] D) Perché il PC dimentica l'indirizzo in cui aveva scritto il documento.

Perché? (facoltativo) `______________________________`

<details>
<summary>🃏 <b>Parte 1 — Soluzioni</b></summary>

| ID | Risposta | Note per la correzione |
|---|---|---|
| 1.1 | B | Cambia il programma in memoria. A e C attribuiscono il compito a collegamenti o ALU; D scambia i registri (valori in uso) con la memoria dei programmi. |
| 1.2 | D | `STORE` copia dal registro alla cella. B descrive una `LOAD`; A scambia dato e indirizzo; C dimentica che la copia lascia intatta la sorgente. |
| 1.3 | A | Il clock conta i cicli al secondo. B e C sono la misconcezione «più GHz = sempre più veloce»; D confonde clock e banda della memoria. |
| 1.4 | C | Il testo non salvato era solo in RAM, volatile. A e D sono idee sbagliate sullo spegnimento; B confonde capacità e persistenza. |

**Criteri:** 0,5 per ogni crocetta corretta. Motivazione sbagliata: 0 se manca o non c'entra, parziale se incompleta, 0,5 se mostra la distinzione giusta.

</details>

<details>
<summary>✅ <b>Parte 1 — Soluzioni</b></summary>

| ID | Risposta | Spiegazione |
|---|:-:|---|
| 1.1 | B | In una macchina di Von Neumann il programma è fatto di istruzioni scritte in memoria: per cambiare programma si cambia la memoria, l'hardware resta uguale. |
| 1.2 | D | `STORE` **copia** dal registro alla cella: la cella 30 diventa 5 e `R1` resta 5. B descriverebbe una `LOAD`. |
| 1.3 | A | Il clock dà il ritmo: 4 GHz sono il doppio dei cicli al secondo. Ma quante istruzioni si completano dipende da quanti cicli ne servono ciascuna: più GHz non vuol dire per forza più veloce. |
| 1.4 | C | La RAM è **volatile**: senza corrente perde i dati. Il testo non salvato era solo lì. |

</details>

## Parte 2 · Seguire un programma ✅ (3 punti)

💬 *Suggerimento: segui le istruzioni una alla volta e riscrivi tutti i valori a ogni riga. Attenzione a quale registro viene modificato e a quale cella viene letta o scritta.*

Nella memoria della macchina ci sono queste istruzioni, una per cella. In fondo al foglio trovi un promemoria delle istruzioni: non serve impararlo a memoria.

| Cella | Istruzione |
|---:|---|
| 25 | `LOAD R2, [90]` |
| 26 | `ADD R2, R2, R2` |
| 27 | `STORE [91], R2` |
| 28 | `LOAD R1, [91]` |
| 29 | `ADD R3, R1, R2` |
| 30 | `STORE [90], R3` |
| 31 | `HALT` |

**Stato iniziale:** `PC = 25`; `R1 = 0`; `R2 = 0`; `R3 = 0`. Nella memoria: `MEM[90] = 5`, `MEM[91] = 1`. Dopo il fetch il PC avanza di uno.

### 2.1 ✅ (3 punti)

**Esegui le istruzioni delle celle 25, 26 e 27, una alla volta. Dopo ciascuna scrivi i nuovi valori nella riga della tabella.** La prima riga mostra lo stato iniziale.

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[90] | MEM[91] |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| (stato iniziale) | 25 | 0 | 0 | 0 | 5 | 1 |
| `LOAD R2, [90]` | `____` | `____` | `____` | `____` | `____` | `____` |
| `ADD R2, R2, R2` | `____` | `____` | `____` | `____` | `____` | `____` |
| `STORE [91], R2` | `____` | `____` | `____` | `____` | `____` | `____` |

<details>
<summary>🃏 <b>2.1 — Soluzione</b></summary>

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[90] | MEM[91] |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `LOAD R2, [90]` | 26 | 0 | 5 | 0 | 5 | 1 |
| `ADD R2, R2, R2` | 27 | 0 | 10 | 0 | 5 | 1 |
| `STORE [91], R2` | 28 | 0 | 10 | 0 | 5 | 10 |

**Criteri:** 1 punto per riga, se tutti i valori sono giusti; 0,5 se un solo valore è sbagliato. Errore propagato: se la riga è coerente con valori sbagliati venuti dalla riga prima, punteggio pieno.

**Errori frequenti:** PC non avanzato; PC = 90 dopo la `LOAD`; `ADD R2, R2, R2` letta come R2 + 0 o R2 = 1; MEM[90] azzerata dopo la lettura; `STORE` scambiata con `LOAD` (R2 modificato invece di MEM[91]).

</details>

<details>
<summary>✅ <b>2.1 — Soluzione</b></summary>

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[90] | MEM[91] |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `LOAD R2, [90]` | 26 | 0 | 5 | 0 | 5 | 1 |
| `ADD R2, R2, R2` | 27 | 0 | 10 | 0 | 5 | 1 |
| `STORE [91], R2` | 28 | 0 | 10 | 0 | 5 | 10 |

**Spiegazione:**
- `LOAD R2, [90]`: copia in `R2` il contenuto della cella 90 (5). La cella resta 5. Il PC avanza di uno: 26.
- `ADD R2, R2, R2`: `R2 = 5 + 5 = 10`. La destinazione è il primo registro.
- `STORE [91], R2`: copia `R2` (10) nella cella 91, che passa da 1 a 10. `R2` resta 10.

Gli altri valori non cambiano. In ogni riga il PC avanza di uno, perché non ci sono salti.

</details>

## Parte 3 · Indirizzi e capacità ✅ (2 punti)

💬 *Suggerimento: ogni bit in più raddoppia il numero di indirizzi. Per trovare quanti bit servono, raddoppia 1, 2, 4, ... finché arrivi al numero di locazioni.*

Una memoria ha **32 locazioni**, numerate a partire da 0. Ogni locazione contiene **2 byte**.

### 3.1 ✅ (1 punto)

**Quanti bit servono per scrivere l'indirizzo di ogni locazione?**

Risposta: `______________________`

### 3.2 ✅ (0,5 punti)

**Quale capacità totale ha la memoria, in byte?**

Risposta: `______________________`

### 3.3 ✅ (0,5 punti)

**Si aggiunge un bit all'indirizzo, senza cambiare la dimensione delle locazioni. Quante locazioni ha ora la memoria, e quanti byte?**

Risposta: `______________________`

<details>
<summary>🃏 <b>Parte 3 — Soluzioni</b></summary>

**3.1 — 5 bit**, perché 2⁵ = 32 (1, 2, 4, 8, 16, 32 raddoppiando). Criteri: 1 punto per 5; mezzo punto se l'idea è giusta ma il numero è sbagliato per un solo raddoppio (4 o 6). Errore frequente: 32 (il numero di locazioni, non i bit) o 31 (ultimo indirizzo).

**3.2 — 64 byte**, cioè 32 locazioni × 2 byte. Criteri: 0,5 solo se il calcolo mostra la moltiplicazione; il numero senza unità non vale il punto.

**3.3 — 64 locazioni e 128 byte**, perché un bit in più raddoppia le locazioni (2⁶) e ognuna resta da 2 byte. Criteri: 0,25 per le locazioni, 0,25 per i byte. Errore frequente: aggiungere 1 invece di raddoppiare.

</details>

<details>
<summary>✅ <b>Parte 3 — Soluzioni</b></summary>

**3.1 — 5 bit.** Con n bit si scrivono 2ⁿ indirizzi. Raddoppiando: 1, 2, 4, 8, 16, **32** → servono 5 raddoppi, quindi 2⁵ = 32. (Attenzione: 32 è il numero di locazioni, non di bit; 31 è solo l'ultimo indirizzo.)

**3.2 — 64 byte.** 32 locazioni × 2 byte = 64 byte.

**3.3 — 64 locazioni e 128 byte.** Un bit in più **raddoppia** le locazioni (2⁶ = 64, non 33). Ognuna resta da 2 byte: 64 × 2 = 128 byte.

</details>

## Parte 4 · Programma e cache 🔍 (3 punti)

💬 *Suggerimento: per 4.1 riparti dalla riga data, anche se non hai finito la parte 2. Per 4.2 scrivi i confini dei blocchi prima di rispondere e segna, a ogni lettura, quale blocco serve.*

### 4.1 🔍 (1,5 punti)

**a) Continua il programma della parte 2 dalla cella 28 *(1)*.** Riparti dallo stato dato nella prima riga della tabella. Esegui le istruzioni delle celle 28, 29 e 30, una alla volta.

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[90] | MEM[91] |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| (stato di partenza) | 28 | 0 | 10 | 0 | 5 | 10 |
| `LOAD R1, [91]` | `____` | `____` | `____` | `____` | `____` | `____` |
| `ADD R3, R1, R2` | `____` | `____` | `____` | `____` | `____` | `____` |
| `STORE [90], R3` | `____` | `____` | `____` | `____` | `____` | `____` |

**b) Guarda dentro la `LOAD R1, [91]` della cella 28 *(0,5)*.** Nel *fetch* della `LOAD`, quale valore ha il MAR? Poi, nell'*execute*, quali valori hanno il MAR e l'MDR quando il dato arriva dalla memoria? Che cosa contiene l'IR in quel momento?

Risposta: `______________________________________________`

<details>
<summary>🃏 <b>4.1 — Soluzione</b></summary>

**a)**

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[90] | MEM[91] |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `LOAD R1, [91]` | 29 | 10 | 10 | 0 | 5 | 10 |
| `ADD R3, R1, R2` | 30 | 10 | 10 | 20 | 5 | 10 |
| `STORE [90], R3` | 31 | 10 | 10 | 20 | 20 | 10 |

Criteri: 0,5 per riga, se tutti i valori sono giusti; 0,25 se un solo valore è sbagliato. Errore propagato: punteggio pieno se coerente con i valori dello studente. Punti delicati: R1 e R2 valgono entrambi 10 (la `LOAD` rilegge ciò che la `STORE` ha scritto); la somma è 20. L'ultima `STORE` sovrascrive MEM[90] (5 → 20); MEM[91] non cambia.

**b)** Nel fetch il MAR vale **28** (copia del PC prima dell'avanzamento). Nell'execute il MAR vale **91** (indirizzo del dato) e l'MDR vale **10** (il contenuto di MEM[91]); l'IR contiene ancora **`LOAD R1, [91]`**, perché il dato passa dall'MDR e arriva in R1 senza sovrascrivere l'istruzione. Criteri: 0,25 per MAR = 28 nel fetch e MAR = 91 nell'execute; 0,25 per MDR = 10 e IR = `LOAD R1, [91]`. Errori frequenti: MAR = 10 (scambio fra indirizzo e contenuto), IR = 10 (il dato sovrascrive l'istruzione), MAR = 29 (PC già avanzato).

</details>

<details>
<summary>🔍 <b>4.1 — Soluzione</b></summary>

**a)**

| Istruzione eseguita | PC | R1 | R2 | R3 | MEM[90] | MEM[91] |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `LOAD R1, [91]` | 29 | 10 | 10 | 0 | 5 | 10 |
| `ADD R3, R1, R2` | 30 | 10 | 10 | 20 | 5 | 10 |
| `STORE [90], R3` | 31 | 10 | 10 | 20 | 20 | 10 |

**Spiegazione:**
- `LOAD R1, [91]`: `R1` riceve il contenuto della cella 91, che è 10 (scritto dalla `STORE` di prima).
- `ADD R3, R1, R2`: `R3 = 10 + 10 = 20`.
- `STORE [90], R3`: la cella 90 passa da 5 a 20 (sovrascritta). La cella 91 non cambia.

**b)** Nel *fetch* il MAR vale **28**: è il PC, copiato nel MAR prima che il PC avanzi a 29. Nell'*execute* il MAR vale **91** (l'indirizzo del dato) e l'MDR vale **10** (il contenuto di `MEM[91]`). L'IR contiene ancora **`LOAD R1, [91]`**: il dato passa dall'MDR a `R1` senza toccare l'IR.

Regola: il MAR contiene sempre un **indirizzo**, l'MDR un **contenuto**.

</details>

### 4.2 🔍 (1,5 punti)

**Un programma elabora i valori di un vettore memorizzato in posizioni consecutive.** La cache conserva blocchi di **8 posizioni consecutive**: 0-7, 8-15, 16-23, ... Rispondi ai tre casi, spiegando il ragionamento.

a) La cache è vuota. Il programma legge l'indirizzo **35** e poi, subito dopo, **38** e **40**. Per ciascuna delle tre letture indica HIT o MISS e quale blocco serve. Supponi che il blocco caricato resti in cache. *(0,5)*

Risposta: `______________________________________________`

b) Il programma somma gli elementi agli indirizzi **100, 101, 102, 103, 104, 105** (cache vuota all'inizio) e poi ripete la stessa somma una seconda volta. Quanti MISS ci sono nella prima passata, se nessun blocco viene sostituito? Quale tipo di località rende più veloce la seconda passata? *(0,5)*

Risposta: `______________________________________________`

c) La cache ha **una sola linea** da **4 posizioni** (blocchi 0-3, 4-7, 8-11, 12-15); ogni MISS sostituisce la linea. Due programmi leggono tutti i 16 indirizzi da 0 a 15. Il primo li legge in ordine: 0, 1, 2, ..., 15. Il secondo salta di quattro in quattro: 0, 4, 8, 12, poi 1, 5, 9, 13, poi 2, 6, 10, 14, poi 3, 7, 11, 15. Quanti MISS fa ciascuno? Spiega perché. *(0,5)*

Risposta: `______________________________________________`

<details>
<summary>🃏 <b>4.2 — Soluzione</b></summary>

**a)** 35 è MISS (blocco 32-39, cache vuota); 38 è HIT (stesso blocco, già caricato); 40 è MISS (blocco 40-47, mai caricato). Criteri: 0,5 se i tre esiti sono giusti con il blocco indicato; 0,25 se due su tre. Errore frequente: considerare 38 un MISS perché «mai letto prima», o 40 un HIT perché «vicino».

**b)** 2 MISS nella prima passata. Gli indirizzi 100-103 stanno nel blocco 96-103 (un MISS, poi tre HIT); 104 e 105 nel blocco 104-111 (un MISS, poi un HIT). La seconda passata è più veloce per la località temporale (gli stessi dati sono riusati) e, nella prima, la spaziale ha già evitato quattro MISS. Criteri: 0,25 per 2 MISS con i blocchi giusti; 0,25 per località temporale. Errore frequente: 6 MISS (ogni lettura trattata come nuova) o 1 MISS (blocchi di 8 allineati a 100).

**c)** Il primo fa **4 MISS** (uno per ogni blocco: leggendo 0-3 il blocco resta caricato, poi si passa a 4-7, ...). Il secondo fa **16 MISS**: a ogni lettura serve un blocco diverso da quello presente e, tornando a 1, 2, 3, il blocco 0-3 è già stato sostituito. Criteri: 0,25 per i due numeri (4 e 16); 0,25 per la spiegazione che lega MISS, località spaziale e sostituzione della linea. Errore frequente: dire che i due fanno lo stesso numero di MISS perché leggono gli stessi 16 indirizzi.

</details>

<details>
<summary>🔍 <b>4.2 — Soluzione</b></summary>

**a)** I blocchi sono 32-39 e 40-47.
- 35 → **MISS** (cache vuota): si carica tutto il blocco 32-39.
- 38 → **HIT**: sta nel blocco 32-39, già in cache, anche se non era mai stato letto.
- 40 → **MISS**: appartiene al blocco 40-47, mai caricato. Essere «vicino» al 38 non basta: conta il blocco.

**b)** **2 MISS.** Il blocco di 100 è 96-103: un MISS per il 100, poi 101, 102, 103 sono HIT. Il 104 è nel blocco 104-111: un altro MISS, poi il 105 è HIT. Nella seconda passata gli stessi dati sono già in cache: è la **località temporale** (riuso degli stessi dati). La **località spaziale** (dati vicini nello stesso blocco) ha già evitato 4 MISS nella prima passata.

**c)** Il primo fa **4 MISS**, il secondo **16 MISS**.
- In ordine (0, 1, 2, 3, 4, ...): il MISS sullo 0 carica 0-3, quindi 1, 2, 3 sono HIT; poi si passa al blocco 4-7, e così via: 1 MISS per blocco, 4 blocchi.
- A salti di quattro (0, 4, 8, 12, 1, ...): ogni lettura richiede un blocco diverso da quello nella linea, che è una sola e viene sostituita. Quando si torna a 1 il blocco 0-3 non c'è più: tutte le 16 letture sono MISS.

Stessi indirizzi, ordine diverso, risultati molto diversi: leggere in modo consecutivo sfrutta la località spaziale.

</details>

## ⭐ Extra (+2 punti, facoltativo)

Non serve per arrivare a 10. Il voto finale non supera 10. L'istruzione `BEQ` non è stata svolta come obiettivo della verifica: se vuoi provarla, la regola è qui.

`BEQ R1, R2, fine`: se `R1` e `R2` hanno lo stesso valore, il programma continua dalla cella con l'etichetta `fine`; altrimenti passa alla cella successiva.

| Cella | Istruzione |
|---:|---|
| 50 | `LOAD R1, [40]` |
| 51 | `LOAD R2, [41]` |
| 52 | `BEQ R1, R2, fine` |
| 53 | `STORE [42], R1` |
| 54 | `fine: HALT` |

Stato iniziale: `MEM[40] = 4`; `MEM[42] = 0`.

**⭐a (0,5)** Se `MEM[41] = 4`, la `STORE` della cella 53 viene eseguita? Quanto vale `MEM[42]` alla fine? `______________________`

**⭐b (0,5)** Se `MEM[41] = 9`, la `STORE` viene eseguita? Quanto vale `MEM[42]` alla fine? `______________________`

**⭐c (1) Scrivi un programma.** Usando solo `LOAD`, `ADD`, `STORE` e `HALT`, scrivi un programma che legge i numeri nelle celle `MEM[70]` e `MEM[71]`, li somma e scrive il risultato in `MEM[72]`. Una istruzione per cella, a partire dalla cella 60.

| Cella | Istruzione |
|---:|---|
| 60 | `______________________` |
| 61 | `______________________` |
| 62 | `______________________` |
| 63 | `______________________` |
| 64 | `______________________` |

<details>
<summary>🃏 <b>⭐ — Soluzione</b></summary>

**⭐a.** No. R1 e R2 valgono entrambi 4, il `BEQ` salta a `fine`, la `STORE` viene saltata e MEM[42] resta 0.

**⭐b.** Sì. R1 = 4 e R2 = 9 sono diversi: il `BEQ` non salta, la `STORE` viene eseguita e MEM[42] diventa 4.

Criteri ⭐a e ⭐b: 0,25 per «eseguita sì/no» e 0,25 per il valore di MEM[42], in ciascun caso.

**⭐c.**

| Cella | Istruzione |
|---:|---|
| 60 | `LOAD R1, [70]` |
| 61 | `LOAD R2, [71]` |
| 62 | `ADD R3, R1, R2` |
| 63 | `STORE [72], R3` |
| 64 | `HALT` |

Criteri (1 punto): 0,25 per le due `LOAD` (registro prima, indirizzo fra parentesi quadre, registri diversi); 0,25 per l'`ADD` con la destinazione per prima e i due registri già caricati; 0,25 per la `STORE` con l'indirizzo per primo e un registro che contiene la somma; 0,25 per l'ordine corretto e per l'`HALT` finale. Si accettano registri diversi o un ordine diverso delle due `LOAD`.

Errori frequenti: `STORE R3, [72]` (argomenti scambiati); `ADD` prima delle `LOAD`; `LOAD R1, 70` senza parentesi (numero al posto del contenuto); dimenticare l'`HALT`.

</details>

<details>
<summary>⭐ <b>Extra — Soluzione</b></summary>

**⭐a.** No, la `STORE` viene saltata. `R1 = R2 = 4`, quindi il `BEQ` salta a `fine` e `MEM[42]` resta **0**.

**⭐b.** Sì, la `STORE` viene eseguita. `R1 = 4` e `R2 = 9` sono diversi: il `BEQ` non salta, si passa alla cella 53 e `MEM[42]` diventa **4** (il valore di `R1`).

**⭐c.**

| Cella | Istruzione |
|---:|---|
| 60 | `LOAD R1, [70]` |
| 61 | `LOAD R2, [71]` |
| 62 | `ADD R3, R1, R2` |
| 63 | `STORE [72], R3` |
| 64 | `HALT` |

Prima si portano i due numeri nei registri (`LOAD`, registro per primo e indirizzo tra parentesi quadre), poi si somma (`ADD`, destinazione per prima), poi si scrive il risultato in memoria (`STORE`, indirizzo per primo), infine `HALT`. Sono valide anche soluzioni con altri registri o con le due `LOAD` scambiate, purché la somma avvenga dopo entrambe.

</details>

## Spazio per la discussione di gruppo

Dopo la prova, confrontate le righe delle due tabelle e le risposte alle crocette. Dove non siete d'accordo? Provate a spiegare l'errore a chi ha risposto diversamente, senza dire subito il risultato.

## Promemoria · le istruzioni della nostra macchina

Questa tabella serve solo da aiuto: non va imparata a memoria.

| Istruzione | Che cosa fa |
|---|---|
| `LOAD R1, [50]` | Copia in `R1` il contenuto della cella 50. La cella non cambia. |
| `STORE [52], R3` | Copia il contenuto di `R3` nella cella 52. `R3` non cambia. |
| `ADD R3, R1, R2` | Somma `R1` e `R2` e scrive il risultato in `R3` (la destinazione è la prima). |
| `HALT` | Ferma il programma. |
| `BEQ R1, R2, fine` | (solo extra ⭐) Se `R1` e `R2` sono uguali, salta all'etichetta `fine`. |

Dopo il fetch di ogni istruzione il PC avanza di uno.
