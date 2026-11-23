# Dove siamo arrivati, cosa abbiamo fatto

## Settembre-Ottobre

### 🧭 Di che cosa parliamo

**Modello di Von Neumann**; **Istruzioni e attese del processore**

Come si passa da una macchina costruita per un solo compito a una macchina che cambia comportamento quando cambia il programma? Abbiamo già seguito la storia fino al modello di Von Neumann. Ora apriamo quella mappa: seguiamo un'istruzione per capire perché servono memoria, registri, calcolo, controllo e collegamenti. E scopriamo perché un processore velocissimo, a volte, resta ad aspettare. ⏳

### 📅 Dispense Settembre-Ottobre

- [x] [S1 - Dalle macchine alla CPU](1%20SETT-OTT/%28STU%29%203EI%20sett-ott%20S1%20-%20Dalle%20macchine%20alla%20CPU.md) — Come si passa da macchine con un solo lavoro a una CPU fatta di parti che conservano, calcolano e coordinano; dal relè al microprocessore e ai livelli di astrazione.
- [x] [S2 - La macchina di Von Neumann](1%20SETT-OTT/%28STU%29%203EI%20sett-ott%20S2%20-%20La%20macchina%20di%20Von%20Neumann.md) — Una macchina, tanti programmi: istruzioni e dati stanno nella stessa memoria.
- [x] [S3 - Registri e percorsi dei dati](1%20SETT-OTT/%28STU%29%203EI%20sett-ott%20S3%20-%20Registri%20e%20percorsi%20dei%20dati.md) — I piccoli «posti di lavoro» della CPU: chi tiene l'indirizzo, chi il dato, chi l'istruzione.
- [x] [S4 - Il ciclo macchina](1%20SETT-OTT/%28STU%29%203EI%20sett-ott%20S4%20-%20Il%20ciclo%20macchina.md) — Prelevare, interpretare, eseguire: seguiamo un programma passo dopo passo. ✅ 2026-10-29
- [x] [S5 - Indirizzi e gerarchia delle memorie](1%20SETT-OTT/%28STU%29%203EI%20sett-ott%20S5%20-%20Indirizzi%20e%20gerarchia%20delle%20memorie.md) — Quante celle si possono raggiungere con n bit, e perché nessuna memoria è insieme grande, veloce ed economica. ✅ 2026-10-29
- [/] [S6 - Cache, località e clock](1%20SETT-OTT/%28STU%29%203EI%20sett-ott%20S6%20-%20Cache%20localita%20e%20clock.md) — Tenere vicino ciò che servirà presto; il clock come ritmo, non come misura di tutto.
- [ ] [S7 - Ricostruire la macchina](1%20SETT-OTT/%28STU%29%203EI%20sett-ott%20S7%20-%20Ricostruire%20la%20macchina.md) — Ripasso: colleghiamo i pezzi e facciamo una prova di allenamento.
- **S8 - Verifica e recupero** — Verifica di teoria, lettura degli errori e recupero.

### ✏️ Esercizi

- [Eserciziario](1%20SETT-OTT/%28STU%29%203EI%20sett-ott%20-%20Eserciziario.md) — Sei dossier e un collaudo finale: un esercizio svolto per ogni argomento, gli altri da provare con la soluzione nascosta. Prima prova tu, poi apri la flashcard.

## Integrazioni

- [Linguaggio assembly: le basi](1%20SETT-OTT/%28STU%29%203EI%20-%20Linguaggio%20assembly%20base.md) — Completa le istruzioni usate negli esempi.

## Novembre-Dicembre

### 🧭 Di che cosa parliamo

**Memorie di massa**; **Boot e partizioni**; **Virtualizzazione**; **Pipelining e parallelismo**

Come rendiamo il computer capace di conservare i file da spento, di avviarsi da zero e di ospitare o eseguire più cose insieme? Seguiamo un filo pratico: *come si prepara un PC per installare un secondo sistema operativo come Linux, e come la CPU lavora su più compiti in parallelo*. 🧭

<details>
<summary><b>Novembre-Dicembre: una macchina efficiente e utilizzabile</b> — cosa vediamo in queste settimane</summary>
<details>
<summary><b>Memorie di massa</b> — dove restano i dati quando spegni il PC</summary>
<ul>
<li>Volatile e persistente: la RAM dimentica allo spegnimento, dischi e chiavette no.</li>
<li>HDD e SSD: dischi meccanici con testina contro celle flash senza parti mobili.</li>
<li>Formato e interfaccia: forma fisica (M.2, 2,5") contro collegamento (SATA, PCIe/NVMe, USB).</li>
<li>Frammentazione, deframmentazione e TRIM: perché un HDD rallenta e perché su SSD non si deframmenta.</li>
<li>Danneggiamento e SMART: settori danneggiati, settori riallocati e segnali prima di un guasto.</li>
</ul>
</details>
<details>
<summary><b>Dall'accensione al sistema operativo</b> — chi parte per primo e come si mappa il disco</summary>
<ul>
<li>Firmware (BIOS/UEFI), POST, bootloader e kernel: la staffetta dall'interruttore alla schermata di accesso.</li>
<li>MBR e GPT: le due mappe del disco, il limite dei 2 TB e le partizioni EFI e di ripristino.</li>
<li>Ordine di avvio UEFI: come far partire una chiavetta USB, Secure Boot e CSM.</li>
<li>Installare Linux accanto a Windows: live USB, scelte del dual boot e menu di GRUB.</li>
</ul>
</details>
<details>
<summary><b>Virtualizzazione</b> — provare un secondo sistema operativo senza toccare il disco</summary>
<ul>
<li>Host, guest e hypervisor: un computer simulato dentro un computer vero.</li>
<li>Condivisione, isolamento e limiti: CPU a turni, RAM a fette, disco virtuale come file.</li>
<li>Linux in VM contro dual boot: sicurezza contro prestazioni piene.</li>
</ul>
</details>
<details>
<summary><b>Pipelining, parallelismo e set di istruzioni</b> — fare più cose nello stesso tempo</summary>
<ul>
<li>CISC e RISC: istruzioni potenti contro istruzioni semplici a lunghezza fissa, porta verso il parallelismo.</li>
<li>Pipelining: catena a cinque stadi, latenza contro throughput e i tre hazard.</li>
<li>Basi di parallelismo: concorrenza contro parallelismo, multi-core, thread e legge di Amdahl.</li>
<li>Parallelismo in Python: il GIL, thread per le attese e processi separati per il calcolo.</li>
</ul>
</details>
</details>

### 📅 Dispense Novembre-Dicembre

- [ ] [S1 - Memorie di massa](2%20NOV-DIC/%28STU%29%203EI%20nov-dic%20S1%20-%20Memorie%20di%20massa.md) — Volatile e persistente, HDD e SSD, formato e interfaccia, frammentazione, TRIM, settori danneggiati e SMART.
- [ ] [S2 - Dall'accensione al sistema operativo](2%20NOV-DIC/%28STU%29%203EI%20nov-dic%20S2%20-%20Dall%27accensione%20al%20sistema%20operativo.md) — Sequenza di boot, BIOS/UEFI, MBR e GPT, partizione EFI, ordine di avvio, live USB e dual boot con Linux.
- [ ] [S3 - Virtualizzazione](2%20NOV-DIC/%28STU%29%203EI%20nov-dic%20S3%20-%20Virtualizzazione.md) — Host, guest, hypervisor, condivisione e isolamento delle risorse, confronto con il dual boot.
- [ ] [S4 - Pipelining, parallelismo e set di istruzioni](2%20NOV-DIC/%28STU%29%203EI%20nov-dic%20S4%20-%20Pipelining%2C%20parallelismo%20e%20set%20di%20istruzioni.md) — CISC/RISC e legame col parallelismo, pipeline a cinque stadi e hazard, basi di parallelismo, GIL e `concurrent.futures` in Python.
- [ ] [S5 - Ripasso e collegamenti](2%20NOV-DIC/%28STU%29%203EI%20nov-dic%20S5%20-%20Ripasso%20e%20collegamenti.md) — Riepilogo del bimestre, tre strade per Linux a confronto, esercizi graduati e mazzo misto di flashcard.
- **S6 - Verifica** — Verifica di teoria e recupero.

### ✏️ Esercizi

- [Eserciziario](2%20NOV-DIC/%28STU%29%203EI%20nov-dic%20-%20Eserciziario.md) — Quattro dossier (S1–S4) con casi reali, un esercizio svolto per argomento e esercizi da provare con soluzione nascosta. Prima prova tu, poi apri la flashcard.
