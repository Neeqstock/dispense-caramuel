# Dove siamo arrivati, cosa abbiamo fatto

## Settembre-Ottobre

### 🧭 Di che cosa parliamo

**Che cos'è una rete**

Gli esseri umani cooperano in milioni perché condividono accordi: lingue, leggi, denaro. Le macchine fanno lo stesso. Una rete è un insieme di accordi scritti così bene che i computer li rispettano senza discutere: chi fa che cosa, come ci si chiama, dove finisce un gruppo.

In questo bimestre seguiamo il viaggio di un messaggio, dalla busta ai segnali, e impariamo a **disegnare lo spazio** in cui viaggia: reti, sottoreti, confini. Alla fine saprai non solo fare un calcolo, ma **controllarlo**.

Lungo la strada incontreremo un primo messaggio che si ferma a «LO», un cavo coassiale chiamato come l'etere, indirizzi finiti nel 2011, piccioni viaggiatori e un esperto di reti che mangia un articolo frullato.

### 📅 Dispense Settembre-Ottobre

- [x] [S1 - Modelli e incapsulamento](1%20SETT-OTT/%28STU%29%204DI%20sett-ott%20S1%20-%20Modelli%20e%20incapsulamento.md) — Chi fa che cosa quando un messaggio parte, e come i dati si chiudono in buste.
- [x] [S2 - Il livello fisico e Ethernet](1%20SETT-OTT/%28STU%29%204DI%20sett-ott%20S2%20-%20Il%20livello%20fisico%20e%20Ethernet.md) — Come i bit diventano segnali, e come un frame arriva sul tratto locale.
- [x] [S3 - IPv4 e il pacchetto](1%20SETT-OTT/%28STU%29%204DI%20sett-ott%20S3%20-%20IPv4%20e%20il%20pacchetto.md) — Come si chiama un'interfaccia e che cosa dice il suo indirizzo.
- [x] [S4 - Reti private e FLSM](1%20SETT-OTT/%28STU%29%204DI%20sett-ott%20S4%20-%20Reti%20private%20e%20FLSM.md) — Come si riutilizzano i numeri e come si taglia una rete in parti uguali. ✅ 2026-10-21
- [x] [S5 - CIDR e intervalli](1%20SETT-OTT/%28STU%29%204DI%20sett-ott%20S5%20-%20CIDR%20e%20intervalli.md) — Come una barra e un numero dicono dove finisce una rete. ✅ 2026-10-21
- [x] [S6 - VLSM e progettazione](1%20SETT-OTT/%28STU%29%204DI%20sett-ott%20S6%20-%20VLSM%20e%20progettazione.md) — Come dare a ognuno lo spazio che gli serve, senza sovrapposizioni. ✅ 2026-10-29
- [x] [S7 - Ripasso e troubleshooting](1%20SETT-OTT/%28STU%29%204DI%20sett-ott%20S7%20-%20Ripasso%20e%20troubleshooting.md) — Come ricomporre quello che sai e trovare il passaggio che non torna. ✅ 2026-11-16

### ✏️ Esercizi

- [Eserciziario](1%20SETT-OTT/%28STU%29%204DI%20sett-ott%20-%20Eserciziario.md) — Otto dossier con casi reali di sicurezza informatica: un esercizio svolto per ogni argomento, gli altri da provare con la soluzione nascosta. Prima prova tu, poi apri la flashcard.

### 📝 Verifica di allenamento

- [Allenamento verifica — il tecnico di rete](1%20SETT-OTT/Verifica/4DI%20sett-ott%20Verifica%20-%20allenamento.md) — Cinque richieste con la stessa struttura della verifica vera, 35 minuti e 10 punti. Non conta per il voto: ogni soluzione è nascosta sotto il suo esercizio, aprila solo dopo aver provato.

## Novembre-Dicembre

### 🧭 Di che cosa parliamo

**IPv6: lo spazio nuovo**; **Router e tabelle di routing**; **Routing statico**; **Routing dinamico**

A settembre e ottobre abbiamo disegnato i confini delle reti IPv4 e scoperto che circa 4,3 miliardi di indirizzi non bastano più per un pianeta pieno di telefoni, computer e sensori. Ora facciamo due passi avanti: prima allarghiamo lo spazio degli indirizzi con **IPv6**, poi entriamo nella scatola che unisce reti diverse — il **router** — per capire come sceglie la strada giusta per ogni pacchetto, senza dover conoscere a memoria tutta Internet.

<details open>
<summary><b>🌐 Dallo spazio nuovo alle strade fra le reti</b></summary>

<details open>
<summary>🔢 <b>IPv6: lo spazio nuovo</b></summary>

- **Indirizzi a 128 bit**: un numero di targa molto più lungo di IPv4, scritto in otto gruppi esadecimali, così grande da non finire più.
- **Compressione con `::`**: una scorciatoia di scrittura per saltare una fila di zeri senza cambiare il significato dell'indirizzo, come scrivere «ecc.» una volta sola.
- **Prefisso `/64` e tipi di indirizzo**: i primi bit dicono ancora in quale rete ti trovi, e dalle prime cifre capisci subito se un indirizzo vale su tutta Internet (`2000::/3`), solo sul cavo di casa (`fe80::/10`) o per un gruppo (`ff00::/8`).

</details>

<details open>
<summary>🚪 <b>Router e tabelle di routing</b></summary>

- **Router e gateway**: l'apparecchio sul confine fra due reti diverse (come il modem-router di casa fra il tuo Wi-Fi e il provider); per il tuo PC è la porta d'uscita, chiamata gateway.
- **Tabella di instradamento**: un piccolo elenco di righe «confine → direzione», come i cartelli stradali a un incrocio che indicano solo la prossima svolta e non l'intero Paese.
- **Scelta della riga più specifica**: se due cartelli vanno bene per la stessa destinazione, il router sceglie quello più preciso (il prefisso più lungo).

</details>

<details open>
<summary>🛣️ <b>Routing statico</b></summary>

- **Rotta statica e prossimo passo**: una riga scritta a mano dal tecnico che dice a quale router vicino consegnare il pacchetto per il tratto successivo.
- **Rotta predefinita (`0.0.0.0/0` e `::/0`)**: la strada di ultima risorsa («tutto il resto mandalo lì»), usata solo quando nessun'altra riga della tabella corrisponde.
- **`ping` e `traceroute`**: due strumenti di controllo per sapere se un messaggio riesce a fare andata e ritorno, oppure a quale incrocio si interrompe la strada.

</details>

<details open>
<summary>🔄 <b>Routing dinamico</b></summary>

- **Distance Vector (passaparola)**: i router si confidano le distanze solo con i vicini diretti, come chiedere indicazioni al passante dell'incrocio accanto.
- **Link State (mappa completa)**: tutti i router si scambiano l'elenco dei collegamenti attivi, costruiscono la stessa mappa stradale e calcolano da soli il percorso meno costoso.
- **Convergenza**: il breve tempo che serve a tutti i router per rimettersi d'accordo dopo che un cavo si rompe.

</details>

</details>

### 📅 Dispense Novembre-Dicembre

- [x] [S1 - IPv6](2%20NOV-DIC/%28STU%29%204DI%20nov-dic%20S1%20-%20IPv6.md) — Perché 32 bit non bastavano più, come si comprimono gli indirizzi a 128 bit e come riconoscere i tre tipi principali. ✅ 2026-11-25
- [ ] [S2 - Router e tabelle di routing](2%20NOV-DIC/%28STU%29%204DI%20nov-dic%20S2%20-%20Router%20e%20tabelle%20di%20routing.md) — Chi lavora sul confine fra due reti, com'è fatta la tabella di un router e come si sceglie la riga giusta.
- [ ] [S3 - Routing statico](2%20NOV-DIC/%28STU%29%204DI%20nov-dic%20S3%20-%20Routing%20statico.md) — Scrivere le strade a mano su più sedi, controllare il prossimo passo, usare la rotta predefinita e leggere `ping` e `traceroute`.
- [ ] [S4 - Introduzione al routing dinamico](2%20NOV-DIC/%28STU%29%204DI%20nov-dic%20S4%20-%20Introduzione%20al%20routing%20dinamico.md) — Come i router imparano da soli una strada nuova quando cade un collegamento: passaparola (*Distance Vector*) contro mappa completa (*Link State*).
- [ ] [S5 - Ripasso e recupero](2%20NOV-DIC/%28STU%29%204DI%20nov-dic%20S5%20-%20Ripasso%20e%20recupero.md) — Mazzo di flashcard mescolate su tutto il bimestre, casi graduati e bussola per il recupero.
- [ ] **S6 - Verifica e recupero** — Verifica su IPv6, lettura e scrittura di tabelle di routing e confronto fra routing statico e dinamico.

### ✏️ Esercizi

- [Eserciziario](2%20NOV-DIC/%28STU%29%204DI%20nov-dic%20-%20Eserciziario.md) — Cinque dossier mirati con casi reali di rete e sicurezza: flashcard di riscaldamento, un esercizio svolto per argomento, prove con soluzione nascosta e Capture The Flag finale.

## Extra facoltativo

- [Giochiamo con le reti](1%20SETT-OTT/%28STU%29%204DI%20sett-ott%20SX%20-%20Extra%20-%20Giochiamo%20e%20smancciamo%20con%20le%20reti.md) — Comandi di sola osservazione, una sfida CIDR e wargame facoltativi da usare esclusivamente nei loro ambienti autorizzati. `tracert` è solo un assaggio.
