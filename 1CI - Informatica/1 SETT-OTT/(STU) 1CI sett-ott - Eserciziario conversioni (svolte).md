⬅️ [S6 - Convertire a gruppi](%28STU%29%201CI%20sett-ott%20S6%20-%20Convertire%20a%20gruppi.md) · 🏠 [Indice](../README.md)

# Eserciziario conversioni (svolte) · 1CI sett-ott

**1CI · Settembre-Ottobre · Eserciziario conversioni (svolte) · Teoria**
⏱️ **Tempo di studio: circa 15 minuti.** Leggi ogni esempio, poi coprilo e rifallo sul quaderno.

> **Legenda:** ✅ da sapere · 🔍 per capire fino in fondo · 🧠 da ricordare · ⚠️ errore comune · 📌 controllo

Qui trovi esempi già svolti dei tre tipi di conversione: decimale → binario, binario → decimale, binario ↔ esadecimale. Ogni esempio mostra **tutti i passaggi**. Le conversioni si fanno **a mano**: il convertitore online serve solo per controllare dopo.

## ✅ Decimale → binario

### ✅ Esempio: 29

Dividi per 2 e annota ogni resto. Continua finché il quoziente è 0.

```text
29 : 2 = 14  resto 1   ^
14 : 2 =  7  resto 0   |
 7 : 2 =  3  resto 1   |   leggi dal basso
 3 : 2 =  1  resto 1   |
 1 : 2 =  0  resto 1   |

risultato: 11101
```

📌 **Controllo:** 16 + 8 + 4 + 1 = 29. Il metodo è giusto.

🧠 <u>I resti si leggono dal basso verso l'alto: l'ultimo resto è la cifra più a sinistra.</u>

### 🔍 Esempio: 100

```text
100 : 2 = 50  resto 0   ^
 50 : 2 = 25  resto 0   |
 25 : 2 = 12  resto 1   |   leggi dal basso
 12 : 2 =  6  resto 0   |
  6 : 2 =  3  resto 0   |
  3 : 2 =  1  resto 1   |
  1 : 2 =  0  resto 1   |

risultato: 1100100
```

📌 **Controllo:** 64 + 32 + 4 = 100.

⚠️ **Errore comune:** leggere i resti dall'alto. Il risultato esce rovesciato: 0010011 invece di 1100100.

## ✅ Binario → decimale

### ✅ Esempio: (101001)₂

Scrivi i pesi da destra: 1, 2, 4, 8, 16, 32. Sotto ogni cifra scrivi il peso, poi somma solo i pesi che stanno sotto un 1.

```text
peso:    32  16   8   4   2   1
cifra:    1   0   1   0   0   1
valore:  32 +  0 + 8 + 0 + 0 + 1 = 41
```

📌 **Risultato:** (101001)₂ = (41)₁₀.

🧠 <u>I pesi partono da destra con 1, e raddoppiano verso sinistra.</u>

### ✅ Esempio: (1000000)₂

```text
peso:    64  32  16   8   4   2   1
cifra:    1   0   0   0   0   0   0
valore:  64
```

📌 **Risultato:** (1000000)₂ = (64)₁₀. Un 1 seguito da sei zeri è una potenza di 2: $2^6 = 64$.

⚠️ **Errore comune:** contare i pesi da sinistra. Per questo esempio si ottiene 1, mentre il valore vero è 64.

## ✅ Binario → esadecimale

### ✅ Esempio: (10010110)₂

Raggruppa i bit a **quattro, da destra**. Poi traduci ogni gruppo con la tabella dei nibble.

```text
1001 | 0110
  9  |  6     →  96
```

📌 **Controllo:** 9 · 16 + 6 = 150; e 128 + 16 + 4 + 2 = 150.

### 🔍 Esempio: (1111001)₂ (7 bit)

Il primo gruppo a sinistra è incompleto: aggiungi **zeri a sinistra** fino a 4 bit.

```text
111 1001   →   0111 | 1001
                7   |  9     →  79
```

📌 **Controllo:** 7 · 16 + 9 = 121; e 64 + 32 + 16 + 8 + 1 = 121.

⚠️ **Errore comune:** partire da sinistra. Con `111 1001` i gruppi diventano `1111 | 001`, e il risultato è sbagliato.

## ✅ Esadecimale → binario

### ✅ Esempio: (B4)₁₆

Sostituisci ogni cifra con il suo nibble di quattro bit, **senza saltare gli zeri**.

```text
B  →  1011
4  →  0100

risultato: 10110100
```

📌 **Controllo:** ogni cifra esadecimale diventa sempre quattro bit.

### 🔍 Esempio: (05)₁₆

```text
0  →  0000
5  →  0101

risultato: 00000101
```

⚠️ **Errore comune:** scrivere 5 come `101` e perdere lo zero iniziale del nibble. Il risultato corretto è `00000101`, con otto bit.

## ✅ Esadecimale → decimale

### ✅ Esempio: (2A)₁₆

Usa i pesi di 16: 1, 16, 256…

```text
peso:    16    1
cifra:    2    A (= 10)
valore:  2·16 + 10·1 = 32 + 10 = 42
```

📌 **Risultato:** (2A)₁₆ = (42)₁₀.

🧠 <u>In esadecimale A vale 10, B vale 11, F vale 15: sono cifre, non lettere.</u>

## 🧠 Il metodo in quattro mosse

1. **Scrivi la base di partenza e quella di arrivo.** Così sai che cosa stai convertendo.
2. **Scegli il percorso:** pesi o divisioni per il decimale; gruppi da 4 o da 3 per binario e hex/ottale.
3. **Controlla il verso:** resti dal basso, pesi e gruppi da destra.
4. **Controlla il risultato:** torna al decimale con un secondo metodo.

📌 Se i due metodi danno lo stesso numero, la conversione è probabilmente giusta.

## 📚 Dove esercitarti

- Gli esempi delle dispense [S4](%28STU%29%201CI%20sett-ott%20S4%20-%20Binario%20e%20decimale.md), [S5](%28STU%29%201CI%20sett-ott%20S5%20-%20Esadecimale%20e%20ottale.md) e [S6](%28STU%29%201CI%20sett-ott%20S6%20-%20Convertire%20a%20gruppi.md) contengono altri esercizi.
- Il ripasso di [S7](%28STU%29%201CI%20sett-ott%20S7%20-%20Ripasso%20attivo.md) ti propone un metodo da seguire passo per passo.

---

⬅️ [S6 - Convertire a gruppi](%28STU%29%201CI%20sett-ott%20S6%20-%20Convertire%20a%20gruppi.md) · 🏠 [Indice](../README.md)
