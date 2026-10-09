[⬅️ S3 - Registri e percorsi dei dati](%28STU%29%203EI%20sett-ott%20S3%20-%20Registri%20e%20percorsi%20dei%20dati.md) · 🏠 [Indice](%28STU%29%203EI%20-%20SETT-OTT.md) · [S4 - Il ciclo macchina](%28STU%29%203EI%20sett-ott%20S4%20-%20Il%20ciclo%20macchina.md) ➡️

# 💻 Linguaggio assembly: le basi

**3EI · Settembre-Ottobre · Integrazione**

## 🧭 Prima distinzione

Il **linguaggio macchina** è fatto di bit. L'**assembly** usa nomi brevi, come `ADD` e `LOAD`, per rappresentare le istruzioni. La CPU non esegue direttamente queste parole: un assemblatore le traduce in codici macchina.

**MIPS** è una famiglia di architetture per processori, basata su un insieme di istruzioni RISC: un repertorio di istruzioni relativamente semplici e regolari. Si studia spesso perché rende visibili i passaggi tra registri, calcoli e memoria. Il suo assembly usa registri con nomi come `$t0` e `$s0`; le regole precise dipendono dalla variante MIPS.

Negli esempi delle dispense S2-S4 usiamo un assembly didattico, molto semplificato, non vero MIPS. La tabella qui sotto lo completa e mostra, quando possibile, l'istruzione MIPS simile. Le due colonne non sono sempre intercambiabili: MIPS ha regole e registri propri.

## 🧰 Le istruzioni che ci servono

| Istruzione didattica | Che cosa fa | Istruzione MIPS simile |
|---|---|---|
| `LOAD R1, [40]` | Copia in `R1` il contenuto della cella di memoria 40. | `lw $t0, 0($s0)` legge una parola dall'indirizzo contenuto in `$s0` più l'offset. |
| `STORE [41], R3` | Copia il contenuto di `R3` nella cella di memoria 41. | `sw $t2, 4($s0)` scrive una parola all'indirizzo `$s0 + 4`. |
| `ADD R3, R1, R2` | Somma `R1` e `R2`; mette il risultato in `R3`. | `add $t2, $t0, $t1` |
| `SUB R3, R1, R2` | Sottrae `R2` da `R1`; mette il risultato in `R3`. | `sub $t2, $t0, $t1` |
| `ADDI R1, R1, 1` | Aggiunge il numero costante 1 a `R1`. | `addi $t0, $t0, 1` |
| `BEQ R1, R2, uguali` | Se `R1` e `R2` sono uguali, continua dall'etichetta `uguali`. | `beq $t0, $t1, uguali` |
| `J inizio` | Continua dall'etichetta `inizio`. | `j inizio` |
| `HALT` | Ferma la macchina didattica. | Non è un'istruzione MIPS standard: i simulatori usano convenzioni specifiche per terminare. |

📌 `lw` e `sw` trasferiscono una **parola** fra un registro e la memoria. Nell'esempio, `0($s0)` significa «indirizzo contenuto in `$s0`, più 0 byte»; `4($s0)` significa «quattro byte dopo». L'offset non è il contenuto della cella.

## ➕ Un programma piccolo

Vogliamo sommare i valori nelle celle 40 e 41 e scrivere il risultato nella cella 42:

```text
LOAD R1, [40]
LOAD R2, [41]
ADD R3, R1, R2
STORE [42], R3
HALT
```

La CPU legge due valori, li somma e scrive il risultato. `R1`, `R2` e `R3` sono registri: gli indirizzi tra parentesi quadre indicano invece celle di memoria.

## ⚠️ Da non confondere

- `ADD destinazione, sorgente1, sorgente2`: il primo registro riceve il risultato.
- `LOAD` porta un dato dalla memoria a un registro; `STORE` fa il percorso opposto.
- `HALT` appartiene al nostro modello didattico: non copiarlo come se fosse un comando MIPS universale.
- MIPS usa registri con nomi come `$t0` e `$s0`, e gli indirizzi di memoria seguono regole proprie. Qui basta riconoscere l'idea, non imparare la codifica binaria delle istruzioni.

---

[⬅️ S3 - Registri e percorsi dei dati](%28STU%29%203EI%20sett-ott%20S3%20-%20Registri%20e%20percorsi%20dei%20dati.md) · 🏠 [Indice](%28STU%29%203EI%20-%20SETT-OTT.md) · [S4 - Il ciclo macchina](%28STU%29%203EI%20sett-ott%20S4%20-%20Il%20ciclo%20macchina.md) ➡️
