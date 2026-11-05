# Allenamento verifica — il tecnico di rete

**4DI · Sistemi e Reti · Allenamento · 35 minuti · 10 punti (+2 facoltativi)**

> 🎯 **Questo è un allenamento: serve per prepararsi alla verifica, non conta per il voto.** Ha la stessa struttura della verifica vera (stesse richieste, stessi livelli ✅/🔍, stessi punti), ma **storie e numeri sono diversi**. Ogni soluzione è nascosta sotto il suo esercizio: aprila 🃏 solo dopo aver provato.

Nome e cognome: ______________________________  Data: ____________

## Come allenarsi

1. **Leggi la richiesta** e dì a voce che cosa ti chiede il «cliente».
2. **Prevedi** una risposta prima di calcolare («secondo me finisce intorno a…»).
3. **Risolvi** con calcolatrice e tabella delle potenze del 2 (in fondo).
4. **Apri la 🃏 soluzione** e confrontala con la tua. Se è diversa, cerca il passaggio in cui ti sei separato dalla soluzione. È la parte più utile.
5. Ogni richiesta ha un **suggerimento** su come ragionare e uno spazio per la **discussione**.

## Come funziona (come nella verifica vera)

- Calcolatrice e tabella delle potenze del 2 sono permesse. Non servono altri appunti.
- ✅ domanda di base; 🔍 domanda più impegnativa; ⭐ attività facoltativa (bonus).
- Nelle crocette c'è una sola risposta corretta. Sbagliare non toglie punti.
- Il «Perché?» è facoltativo: può aiutarti, non può penalizzarti.
- Scrivi i passaggi: una risposta con il ragionamento vale anche se un numero è sbagliato.
- Gli indirizzi «pubblici» che trovi nelle richieste sono indirizzi di esempio.
- Se una domanda ti blocca, passa alla successiva e torna indietro dopo.
- Il bonus ⭐ vale +2. Il voto finale non supera 10.

| Richiesta | Attività | Punti | Tempo indicativo |
| --- | --- | ---: | ---: |
| 1 | Il viaggio di un documento | 1 | 3 min |
| 2 | La rete delle telecamere di Sofia | 2,5 | 6 min |
| 3 | Il log dello studio veterinario | 2 | 6 min |
| 4 | Il PC esce su Internet | 1,5 | 4 min |
| 5 | L'agenzia cresce | 3 | 9 min |
| | **Totale** | **10** | **28 min** |
| ⭐ | Facoltative (⭐a–⭐d) | +2 | 8 min |

Allenandoti da solo, prova a rispettare i tempi: nella verifica vera avrai circa 35 minuti.

---

# Richiesta 1 — Il viaggio di un documento

Sara è in biblioteca e stampa un documento. Il suo PC e la **stampante** sono collegati con un cavo Ethernet allo stesso **switch**.

> 💡 **Suggerimento.** Chiediti sempre «in quale livello siamo?». Lo switch lavora sul tratto locale; i dati scendono verso il cavo quando partono e risalgono quando arrivano.

**1a ✅ (0,5)** Il frame di Sara arriva allo switch, ma lo switch non ha ancora in tabella il MAC della stampante. Che cosa fa?

- [ ] **A.** Scarta il frame, perché non sa a chi consegnarlo.
- [ ] **B.** Lo manda solo al router, che decide dove farlo arrivare.
- [ ] **C.** Lo manda a tutte le porte tranne quella di arrivo.
- [ ] **D.** Lo manda solo alla porta usata più di recente.

*Perché? (facoltativo)* ______________________________________________

<details>
<summary>🃏 <b>1a — Soluzione</b></summary>
<p><b>C.</b> Con la tabella senza il MAC di destinazione, lo switch non sa quale porta scegliere e copia il frame su tutte le porte tranne quella di arrivo (S2). Il primo dispositivo che risponde si fa conoscere e la tabella si aggiorna.</p>
<p><b>Distrattori.</b> <em>A</em>: scartare è tipico del firewall, non dello switch. <em>B</em>: il router non c'entra nella consegna locale. <em>D</em>: la porta più recente non ha senso se il MAC non è in tabella.</p>
<p><b>Punteggio.</b> 0,5.</p>
</details>

**1b ✅ (0,5) — Riordina le carte.** Sulla stampante le PDU si «aprono» una dopo l'altra, dal cavo verso l'applicazione. Scrivi un numero da **1** (la prima a comparire) a **5** (l'ultima) accanto a ciascuna carta.

| Carta                  | Numero (1–5) |
| ---------------------- | :----------: |
| 📦 Pacchetto           |      3       |
| ⚡ Segnali dal cavo     |      1       |
| 🧩 Segmento            |      4       |
| ✉️ Frame               |      2       |
| 💬 Dati (il documento) |      5       |

<details>
<summary>🃏 <b>1b — Soluzione</b></summary>
<p><b>Ordine corretto:</b> 1 Segnali · 2 Frame · 3 Pacchetto · 4 Segmento · 5 Dati.</p>
<p><b>Punteggio.</b> 0,1 per ogni carta al posto giusto.</p>
</details>

🗣️ **Discussione di gruppo.** Perché, secondo voi, si aprono in questo ordine e non in un altro? Che cosa cambia rispetto a quando il documento parte?

______________________________________________________________

---

# Richiesta 2 — La rete delle telecamere di Sofia

Sofia ha creato nel router di casa una rete separata per le telecamere, con prefisso **/29**. La telecamera del cortile ha l'indirizzo **192.168.50.13/29**.

> 💡 **Suggerimento.** Dimensiona il blocco (quanti bit host? quanti indirizzi?), poi trova dove inizia: i blocchi partono da multipli della loro dimensione. Controlla con un secondo metodo.

**2a ✅ (2) — Compila la scheda.** Completa la tabella con i dati della rete delle telecamere.

| Dato                                   | Il tuo valore                |
| -------------------------------------- | ---------------------------- |
| Maschera in notazione decimale         | 255.255.255.248              |
| Bit host                               | 3                            |
| Indirizzo di rete                      | 192.168.50.8                 |
| Indirizzo di broadcast                 | 192.168.50.15                |
| Intervallo degli host (primo – ultimo) | 192.168.50.9 - 192.168.50.14 |

<details>
<summary>🃏 <b>2a — Soluzione</b></summary>
<p><b>Risposte.</b> Maschera <code>255.255.255.248</code> · 3 bit host (32 − 29) · rete <code>192.168.50.8</code> · broadcast <code>192.168.50.15</code> · host da <code>192.168.50.9</code> a <code>192.168.50.14</code> (6 host).</p>
<p><b>Controllo.</b> AND di 13 (<code>00001101</code>) con 248 (<code>11111000</code>) dà <code>00001000</code> = 8. Il blocco ha 8 indirizzi (2³).</p>
<p><b>Punteggio.</b> 0,4 per ciascuna riga.</p>
</details>

**2b ✅ (0,5)** Sofia vuole collegare altre telecamere alla stessa rete. Quanti dispositivi, in tutto, possono ricevere un indirizzo in questa rete?

- [x] **A.** 6 ✅ 2026-11-04
- [ ] **B.** 8
- [ ] **C.** 7
- [ ] **D.** 4

*Perché? (facoltativo)* ______________________________________________

<details>
<summary>🃏 <b>2b — Soluzione</b></summary>
<p><b>A.</b> Un <code>/29</code> ha 8 indirizzi: tolti rete e broadcast restano 6 host.</p>
<p><b>Distrattori.</b> <em>B</em>: 8 conta anche rete e broadcast. <em>C</em>: 7 toglie solo il broadcast, dimenticando la rete. <em>D</em>: 4 è 2², non 2³.</p>
<p><b>Punteggio.</b> 0,5.</p>
</details>

🗣️ **Discussione di gruppo.** Il vicino di Sofia ha la stessa rete `192.168.50.8/29` nel suo router. Perché i due router non si disturbano? E se le due reti venissero collegate, che cosa andrebbe storto? (Ci torniamo nel bonus.)

<details>
<summary>🃏 <b>Discussione — Traccia</b></summary>
<p>Gli intervalli <code>192.168.x.x</code> sono <b>privati</b> e non vengono instradati in Internet: ogni casa può riusarli. Il <b>NAT</b> del router traduce l'indirizzo privato in quello pubblico ricevuto dal provider. Collegando le due reti, due dispositivi potrebbero avere lo stesso indirizzo.</p>
</details>

______________________________________________________________

---

# Richiesta 3 — Allarme nel log

Sei il tecnico dello studio veterinario «Il Gatto Blu». Il router ha segnato sei tentativi falliti di accesso al pannello del gestionale. Gli indirizzi che iniziano con `192.0.2` sono **pubblici** (indirizzi di esempio). Sono **tentativi sospetti**: il titolare pensa che qualcuno abbia provato ad entrare da fuori.

| Riga | Ora | Indirizzo sorgente |
| :---: | :---: | --- |
| 1 | 08:10 | `192.0.2.44` |
| 2 | 08:11 | `192.0.2.7` |
| 3 | 08:13 | `192.0.2.44` |
| 4 | 08:15 | `10.0.0.23` |
| 5 | 08:16 | `192.0.2.70` |
| 6 | 08:19 | `192.0.2.96` |

> 💡 **Suggerimento.** Un numero da solo non basta: conta in quale **intervallo** cade. Per una regola con prefisso, scrivi prima la dimensione del blocco, poi dove inizia e dove finisce.

**3a ✅ (0,5)** Le righe 1 e 3 hanno lo stesso indirizzo sorgente, `192.0.2.44`. Scrivi in due frasi una spiegazione plausibile.

______________________________________________________________

<details>
<summary>🃏 <b>3a — Soluzione</b></summary>
<p><b>Risposta.</b> Le righe 1 e 3 hanno lo stesso IP, <code>192.0.2.44</code>. Spiegazioni plausibili: (a) lo stesso dispositivo che riprova la password dopo un errore; (b) un altro dispositivo dietro lo stesso router, che condivide l'IP pubblico (NAT/PAT, S4). Basta una spiegazione motivata.</p>
<p><b>Punteggio.</b> 0,5.</p>
</details>

**3b ✅ (0,5)** Il PC della segreteria, con indirizzo privato `10.0.0.23`, apre una pagina su un server in Internet. Quale indirizzo IP vede il server come sorgente?

- [ ] **A.** `10.0.0.23`, l'indirizzo che il PC conosce.
- [ ] **B.** `192.0.2.44`, l'indirizzo pubblico del router.
- [ ] **C.** `192.0.2.7`, l'indirizzo del server stesso.
- [ ] **D.** Nessun indirizzo: il NAT nasconde il PC.

*Perché? (facoltativo)* ______________________________________________

<details>
<summary>🃏 <b>3b — Soluzione</b></summary>
<p><b>B.</b> Il server vede l'IP pubblico del router, non quello privato del PC: il NAT sostituisce l'indirizzo in uscita.</p>
<p><b>Distrattori.</b> <em>A</em>: l'IP privato non esce dalla rete. <em>C</em>: confonde la sorgente con l'indirizzo del server. <em>D</em>: il NAT non nasconde il PC, cambia solo l'indirizzo.</p>
<p><b>Punteggio.</b> 0,5.</p>
</details>

**3c 🔍 (1)** Imposti nel firewall la regola: **blocca `192.0.2.64/27`**.

1. Scrivi il **primo** e l'**ultimo** indirizzo coperti dalla regola. *(0,5)*

   Primo: ______________  Ultimo: ______________

2. Quali **righe** del log sono bloccate dalla regola? *(0,5)*

   Righe: ______________

<details>
<summary>🃏 <b>3c — Soluzione</b></summary>
<p><b>1.</b> Una <code>/27</code> ha 32 indirizzi: la regola copre da <code>192.0.2.64</code> a <code>192.0.2.95</code>. Punteggio: 0,25 per estremo.</p>
<p><b>2.</b> Riga <b>5</b> (<code>.70</code>). Non bloccate: 6 (<code>.96</code>, appena oltre il .95), 1 e 3 (<code>.44</code>), 2 (<code>.7</code>), 4 (privato). Punteggio: 0,5.</p>
</details>

🗣️ **Discussione di gruppo.** Il titolare dice: «basta bloccare l'indirizzo che attacca». Perché potrebbe non bastare?

______________________________________________________________

---

# Richiesta 4 — Il PC esce su Internet

Lo studio ha una rete interna con indirizzi privati. Il router ha un solo indirizzo pubblico, `192.0.2.44`: tutti i PC passano da lì per navigare.

> 💡 **Suggerimento.** Chiediti quali indirizzi cambiano quando il pacchetto esce dalla rete locale, e quali restano uguali.

**4a ✅ (0,5)** Quale affermazione descrive correttamente i due apparati?

- [ ] **A.** Il firewall cambia l'indirizzo sorgente dei pacchetti in uscita.
- [ ] **B.** Il NAT decide quali pacchetti possono entrare nella rete.
- [ ] **C.** Il PAT cifra il contenuto dei pacchetti prima di inviarli.
- [ ] **D.** Il NAT traduce gli indirizzi; il firewall applica regole su chi può passare.

*Perché? (facoltativo)* ______________________________________________

<details>
<summary>🃏 <b>4a — Soluzione</b></summary>
<p><b>D.</b> Il NAT traduce gli indirizzi (l'IP privato in quello pubblico), il firewall decide chi può passare.</p>
<p><b>Distrattori.</b> <em>A</em>: il firewall non cambia gli indirizzi. <em>B</em>: decidere chi entra è compito del firewall, non del NAT. <em>C</em>: il PAT condivide un IP usando le porte, non cifra nulla.</p>
<p><b>Punteggio.</b> 0,5.</p>
</details>

**4b ✅ (0,5)** Quale campo dell'header IP permette di scoprire se l'header è stato alterato durante il viaggio?

- [ ] **A.** Indirizzo IP di destinazione, che stabilisce se il pacchetto è arrivato al destinatario giusto.
- [ ] **B.** Header Checksum, che verifica solo l'header e non il contenuto.
- [ ] **C.** Lunghezza totale, che conta quanti byte contiene il pacchetto.
- [ ] **D.** Indirizzo MAC sorgente, che stabilisce chi ha spedito il frame.

*Perché? (facoltativo)* ______________________________________________

<details>
<summary>🃏 <b>4b — Soluzione</b></summary>
<p><b>B.</b> Il checksum (S3) controlla solo l'header, non il contenuto.</p>
<p><b>Distrattori.</b> <em>A</em>: l'IP di destinazione dice dove andare, non se l'header è intatto. <em>C</em>: la lunghezza dice quanti byte pesa il pacchetto. <em>D</em>: il MAC sorgente sta nel frame Ethernet, non nell'header IP.</p>
<p><b>Punteggio.</b> 0,5.</p>
</details>

**4c ✅ (0,5)** Nel frame Ethernet che porta un pacchetto IP, quale campo dichiara il tipo di dati trasportati?

- [ ] **A.** EtherType, che indica che cosa c'è dentro il frame.
- [ ] **B.** MAC sorgente, che indica quale scheda di rete ha spedito il frame.
- [ ] **C.** CRC, che serve a rilevare alcuni errori nel frame.
- [ ] **D.** MAC di destinazione, che indica quale scheda deve riceverlo.

*Perché? (facoltativo)* ______________________________________________

<details>
<summary>🃏 <b>4c — Soluzione</b></summary>
<p><b>A.</b> L'EtherType dice che cosa c'è dentro il frame (<code>0x0800</code> = IPv4) e permette alla scheda di rete di consegnare i dati al software giusto.</p>
<p><b>Distrattori.</b> <em>B</em>: il MAC sorgente dice chi ha spedito il frame. <em>C</em>: il CRC serve a scoprire errori, non il tipo. <em>D</em>: il MAC di destinazione dice chi deve riceverlo.</p>
<p><b>Punteggio.</b> 0,5.</p>
</details>

🗣️ **Discussione di gruppo.** Con un solo indirizzo su Internet, come fa il router a rimandare ogni risposta al PC giusto dello studio? Provate a dirlo con parole vostre.

<details>
<summary>🃏 <b>Discussione — Traccia</b></summary>
<p>Il router ricorda quale PC interno ha aperto ogni connessione e usa le porte per distinguerle (PAT, S4): così ogni risposta torna al PC giusto.</p>
</details>

______________________________________________________________

---

# Richiesta 5 — L'agenzia cresce

L'agenzia di viaggi «Viaggi Nord» ha una sede con la rete interna **`10.60.4.0/24`** (indirizzi privati). Il titolare ti chiede di dare una sottorete a ciascun reparto, sprecando il meno possibile. Nei numeri richiesti è **già compreso** il gateway.

| Reparto | Dispositivi richiesti |
| --- | ---: |
| Prenotazioni | 58 |
| Biglietteria | 25 |
| Direzione | 6 |

> 💡 **Suggerimento.** Dimensiona, ordina dal più grande, alloca, controlla. Dopo ogni blocco chiediti: «dove finisce? dove inizia il prossimo?».

**5a ✅ (1) — Dimensiona.** Per ogni reparto trova il blocco più piccolo che basta.

| Reparto | Bit host | Prefisso | Indirizzi nel blocco |
| --- | :---: | :---: | :---: |
| Prenotazioni | | `/` | |
| Biglietteria | | `/` | |
| Direzione | | `/` | |

<details>
<summary>🃏 <b>5a — Soluzione</b></summary>
<table>
<tr><th>Reparto</th><th>Bit host</th><th>Prefisso</th><th>Indirizzi nel blocco</th></tr>
<tr><td>Prenotazioni (58)</td><td>6</td><td><code>/26</code></td><td>64</td></tr>
<tr><td>Biglietteria (25)</td><td>5</td><td><code>/27</code></td><td>32</td></tr>
<tr><td>Direzione (6)</td><td>3</td><td><code>/29</code></td><td>8</td></tr>
</table>
<p><b>Controlli.</b> 58 → 5 bit danno 30 (no), 6 bit danno 62 (sì). 25 → 4 bit danno 14 (no), 5 bit danno 30 (sì). 6 → 2 bit danno 2 (no), 3 bit danno 6 (sì: 2³ − 2 = 6).</p>
<p><b>Punteggio.</b> 0,3 Prenotazioni, 0,3 Biglietteria, 0,4 Direzione: è la riga con il trabocchetto del 6, che entra esatto in un <code>/29</code>.</p>
</details>

**5b 🔍 (2) — Assegna.** Parti da `10.60.4.0`. Assegna i blocchi nell'**ordine** che ritieni giusto: scrivi nella colonna 1 l'ordine di assegnazione (1, 2, 3) e completa il resto.

| Ordine | Reparto | Rete e prefisso | Broadcast | Host (primo – ultimo) |
| :---: | --- | --- | --- | --- |
| | | | | |
| | | | | |
| | | | | |

<details>
<summary>🃏 <b>5b — Soluzione</b></summary>
<pre><code>1  Prenotazioni  10.60.4.0/26    10.60.4.63    .1  – .62
2  Biglietteria  10.60.4.64/27   10.60.4.95    .65 – .94
3  Direzione     10.60.4.96/29   10.60.4.103   .97 – .102</code></pre>
<p><b>Metodo.</b> Dimensiona (5a), ordina dal più grande, alloca in sequenza a partire da <code>.0</code> su confini allineati, controlla. Spazio libero: da <code>.104</code> a <code>.255</code>.</p>
<p><b>Un altro ordine.</b> Per esempio Direzione a <code>.0/29</code>, Biglietteria a <code>.32/27</code>, Prenotazioni a <code>.64/26</code>: il piano è valido, ma lascia un buco da <code>.8</code> a <code>.31</code> e spreca spazio.</p>
<p><b>Punteggio.</b> Prenotazioni 0,5 · Biglietteria 0,75 · Direzione 0,75.</p>
</details>

🗣️ **Discussione di gruppo.** Se aveste lasciato un po' di spazio libero a ogni reparto, il piano sarebbe stato più comodo da estendere? Che cosa si perde?

______________________________________________________________

---

# ⭐ Facoltative (+2)

**Non servono per arrivare a 10.** Se le svolgi, i punti si sommano; il voto finale non supera 10.

## ⭐a–b — Riuso e sovrapposizione

**⭐a (0,5)** Milioni di case usano la stessa rete `192.168.1.0/24`, ma due siti su Internet non possono avere lo stesso IP pubblico. Perché? Spiega in due frasi.

______________________________________________________________

______________________________________________________________

**⭐b (0,5)** Le reti `172.20.0.0/16` e `172.20.4.0/24` si sovrappongono? Scrivi **sì** o **no** e spiega in una frase.

______________________________________________________________

<details>
<summary>🃏 <b>⭐a–b — Soluzione</b></summary>
<p><b>⭐a.</b> Gli indirizzi privati (<code>192.168.x.x</code>, <code>10.x.x.x</code>, <code>172.16–31.x.x</code>) non vengono instradati su Internet, quindi ogni casa può riusarli. Un IP pubblico deve essere unico nel mondo, perché deve raggiungere un solo destinatario. Punteggio: 0,25 per ciascuna frase.</p>
<p><b>⭐b.</b> <b>Sì</b>: <code>172.20.4.0/24</code> sta tutta dentro <code>172.20.0.0/16</code> (da <code>.0.0</code> a <code>.255.255</code>). Una rete più piccola contenuta in una più grande si sovrappone. Punteggio: 0,25 per sì/no, 0,25 per la motivazione.</p>
</details>

## ⭐c — Chi fa che cosa

**⭐c (0,5)** Abbina ogni funzione a chi la svolge, scegliendo fra **NAT**, **firewall**, **PAT**, **IANA**. Ognuno si usa una sola volta.

| Funzione | Chi la svolge |
| --- | :---: |
| Decide quali pacchetti possono attraversare il router | |
| Assegna i grandi blocchi di indirizzi a livello mondiale | |
| Fa condividere un solo IP pubblico a più dispositivi usando le porte | |
| Traduce indirizzi privati in indirizzi pubblici | |

<details>
<summary>🃏 <b>⭐c — Soluzione</b></summary>
<p>Firewall: decide quali pacchetti passano · IANA: blocchi mondiali · PAT: condivide un IP con le porte · NAT: traduce indirizzi privati in pubblici.</p>
<p><b>Punteggio.</b> 0,125 per ogni riga.</p>
</details>

## ⭐d — Quanto tempo tenere i log

**⭐d (0,5)** Il titolare vuole conservare per sempre gli indirizzi IP dei visitatori del sito. Scrivi un motivo a favore e uno contro, in una frase ciascuno.

______________________________________________________________

______________________________________________________________

<details>
<summary>🃏 <b>⭐d — Soluzione</b></summary>
<p><b>A favore:</b> conservare gli IP aiuta a capire un attacco e a difendersi. <b>Contro:</b> sono dati personali; più si conservano, più c'è da proteggere, e le regole sulla privacy chiedono tempi limitati e motivati. Basta una ragione per lato.</p>
<p><b>Punteggio.</b> 0,25 + 0,25.</p>
</details>

---

# Aiuto: potenze del 2

| Potenza | Valore | Potenza | Valore |
| --- | ---: | --- | ---: |
| 2⁰ | 1 | 2⁵ | 32 |
| 2¹ | 2 | 2⁶ | 64 |
| 2² | 4 | 2⁷ | 128 |
| 2³ | 8 | 2⁸ | 256 |
| 2⁴ | 16 | 2⁹ | 512 |
