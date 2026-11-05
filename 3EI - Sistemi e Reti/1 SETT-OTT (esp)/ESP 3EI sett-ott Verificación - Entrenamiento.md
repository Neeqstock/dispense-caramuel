# 🎯 Entrenamiento · 3EI sett-ott

**Entrenamiento**, para hacer juntos en clase. Misma estructura, mismos temas y mismas puntuaciones que la evaluación; sin embargo, las preguntas son **distintas**: hay que razonar, no memorizar.

**Total 10 puntos (+2 opcionales)** · ✅ base 7 · 🔍 más exigente 3 · ⭐ extra · **40 minutos** · sin calculadora.

| Parte | Tema | Nivel | Puntos |
|---|---|---|---|
| 1 | Conceptos de la máquina | ✅ | 2 |
| 2 | Seguir un programa | ✅ | 3 |
| 3 | Direcciones y capacidad | ✅ | 2 |
| 4 | Programa y caché | 🔍 | 3 |
| | **Total** | | **10** |
| ⭐ | Extra | opcional | +2 |

**Reglas de las casillas:** una sola respuesta correcta, 0,5 puntos. Si fallas, la justificación escrita («¿Por qué?») puede recuperar hasta 0,5.

**Espacio para el debate en grupo:** `______________________________________________`

## Parte 1 · Conceptos de la máquina ✅ (2 puntos)

💬 *Sugerencia: antes de mirar las opciones, intenta decir la respuesta en voz alta. Luego busca la que más se parece.*

### 1.1 ✅ (0,5 puntos)

**Una máquina de Von Neumann tiene que ejecutar un programa distinto al anterior. ¿Qué hace falta cambiar?**

- [ ] A) Las conexiones entre CPU y memoria, que hay que rehacer para el nuevo programa.
- [ ] B) Las instrucciones escritas en memoria: el hardware sigue siendo el mismo.
- [ ] C) Los circuitos de la ALU, construidos para ejecutar un solo programa.
- [ ] D) Los valores de los registros, porque son ellos los que contienen todo el programa.

¿Por qué? (opcional) `______________________________`

### 1.2 ✅ (0,5 puntos)

**El registro R1 contiene 5. La CPU ejecuta `STORE [30], R1`. ¿Qué pasa?**

- [ ] A) El número 30 se copia en la celda de dirección 5; R1 no cambia.
- [ ] B) El contenido de la celda 30 se copia en R1, que pasa de 5 a ese valor.
- [ ] C) El número 5 se traslada a la celda 30, y R1 queda por tanto vacío.
- [ ] D) El número 5 se copia en la celda 30; R1 sigue conteniendo 5.

¿Por qué? (opcional) `______________________________`

### 1.3 ✅ (0,5 puntos)

**Una CPU tiene el reloj a 2 GHz, otra a 4 GHz. ¿Qué se puede decir con seguridad?**

- [ ] A) La segunda tiene el doble de ciclos de reloj en cada segundo.
- [ ] B) La segunda completa el doble de instrucciones cada segundo.
- [ ] C) La segunda ejecuta cada instrucción en la mitad del tiempo.
- [ ] D) La segunda lee de la RAM con un ancho de banda doble que la primera.

¿Por qué? (opcional) `______________________________`

### 1.4 ✅ (0,5 puntos)

**Un usuario apaga el ordenador mientras escribe un documento que todavía no ha guardado. ¿Por qué pierde el texto?**

- [ ] A) Porque la CPU borra la memoria de masa en cada apagado.
- [ ] B) Porque la RAM es demasiado pequeña para contener un documento.
- [ ] C) Porque el texto estaba solo en la RAM, que sin corriente pierde los datos.
- [ ] D) Porque el PC olvida la dirección en la que había escrito el documento.

¿Por qué? (opcional) `______________________________`

<details>
<summary>🃏 <b>Parte 1 — Soluciones</b></summary>

| ID | Respuesta | Notas para la corrección |
|---|---|---|
| 1.1 | B | Cambia el programa en memoria. A y C atribuyen la tarea a las conexiones o a la ALU; D confunde los registros (valores en uso) con la memoria de programas. |
| 1.2 | D | `STORE` copia del registro a la celda. B describe una `LOAD`; A intercambia dato y dirección; C olvida que la copia deja intacto el origen. |
| 1.3 | A | El reloj cuenta los ciclos por segundo. B y C son la idea errónea «más GHz = siempre más rápido»; D confunde reloj y ancho de banda de la memoria. |
| 1.4 | C | El texto no guardado estaba solo en la RAM, que es volátil. A y D son ideas erróneas sobre el apagado; B confunde capacidad y persistencia. |

**Criterios:** 0,5 por cada casilla correcta. Justificación incorrecta: 0 si falta o no tiene que ver, parcial si está incompleta, 0,5 si muestra la distinción correcta.

</details>

## Parte 2 · Seguir un programa ✅ (3 puntos)

💬 *Sugerencia: sigue las instrucciones una a una y reescribe todos los valores en cada línea. Fíjate en qué registro se modifica y en qué celda se lee o se escribe.*

En la memoria de la máquina hay estas instrucciones, una por celda. Al final de la hoja tienes un recordatorio de las instrucciones: no hace falta memorizarlo.

| Celda | Instrucción |
|---:|---|
| 25 | `LOAD R2, [90]` |
| 26 | `ADD R2, R2, R2` |
| 27 | `STORE [91], R2` |
| 28 | `LOAD R1, [91]` |
| 29 | `ADD R3, R1, R2` |
| 30 | `STORE [90], R3` |
| 31 | `HALT` |

**Estado inicial:** `PC = 25`; `R1 = 0`; `R2 = 0`; `R3 = 0`. En la memoria: `MEM[90] = 5`, `MEM[91] = 1`. Después del fetch, el PC avanza uno.

### 2.1 ✅ (3 puntos)

**Ejecuta las instrucciones de las celdas 25, 26 y 27, una a una. Después de cada una, escribe los nuevos valores en la fila de la tabla.** La primera fila muestra el estado inicial.

| Instrucción ejecutada | PC | R1 | R2 | R3 | MEM[90] | MEM[91] |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| (estado inicial) | 25 | 0 | 0 | 0 | 5 | 1 |
| `LOAD R2, [90]` | `____` | `____` | `____` | `____` | `____` | `____` |
| `ADD R2, R2, R2` | `____` | `____` | `____` | `____` | `____` | `____` |
| `STORE [91], R2` | `____` | `____` | `____` | `____` | `____` | `____` |

<details>
<summary>🃏 <b>2.1 — Solución</b></summary>

| Instrucción ejecutada | PC | R1 | R2 | R3 | MEM[90] | MEM[91] |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `LOAD R2, [90]` | 26 | 0 | 5 | 0 | 5 | 1 |
| `ADD R2, R2, R2` | 27 | 0 | 10 | 0 | 5 | 1 |
| `STORE [91], R2` | 28 | 0 | 10 | 0 | 5 | 10 |

**Criterios:** 1 punto por fila, si todos los valores son correctos; 0,5 si solo un valor es incorrecto. Error arrastrado: si la fila es coherente con valores incorrectos que venían de la fila anterior, puntuación completa.

**Errores frecuentes:** el PC no avanza; PC = 90 después de la `LOAD`; `ADD R2, R2, R2` leída como R2 + 0 o R2 = 1; MEM[90] puesta a cero tras la lectura; `STORE` cambiada por `LOAD` (R2 modificado en lugar de MEM[91]).

</details>

## Parte 3 · Direcciones y capacidad ✅ (2 puntos)

💬 *Sugerencia: cada bit más duplica el número de direcciones. Para saber cuántos bits hacen falta, duplica 1, 2, 4, ... hasta llegar al número de posiciones.*

Una memoria tiene **32 posiciones de memoria**, numeradas desde 0. Cada posición contiene **2 bytes**.

### 3.1 ✅ (1 punto)

**¿Cuántos bits hacen falta para escribir la dirección de cada posición?**

Respuesta: `______________________`

### 3.2 ✅ (0,5 puntos)

**¿Qué capacidad total tiene la memoria, en bytes?**

Respuesta: `______________________`

### 3.3 ✅ (0,5 puntos)

**Se añade un bit a la dirección, sin cambiar el tamaño de las posiciones. ¿Cuántas posiciones tiene ahora la memoria, y cuántos bytes?**

Respuesta: `______________________`

<details>
<summary>🃏 <b>Parte 3 — Soluciones</b></summary>

**3.1 — 5 bits**, porque 2⁵ = 32 (1, 2, 4, 8, 16, 32 duplicando). Criterios: 1 punto por 5; medio punto si la idea es correcta pero el número es incorrecto por un solo duplicado (4 o 6). Error frecuente: 32 (el número de posiciones, no de bits) o 31 (última dirección).

**3.2 — 64 bytes**, es decir, 32 posiciones × 2 bytes. Criterios: 0,5 solo si el cálculo muestra la multiplicación; el número sin unidad no vale el punto.

**3.3 — 64 posiciones y 128 bytes**, porque un bit más duplica las posiciones (2⁶) y cada una sigue siendo de 2 bytes. Criterios: 0,25 por las posiciones, 0,25 por los bytes. Error frecuente: sumar 1 en lugar de duplicar.

</details>

## Parte 4 · Programa y caché 🔍 (3 puntos)

💬 *Sugerencia: para 4.1 parte de la línea dada, aunque no hayas terminado la parte 2. Para 4.2 escribe los límites de los bloques antes de responder y marca, en cada lectura, qué bloque se necesita.*

### 4.1 🔍 (1,5 puntos)

**a) Continúa el programa de la parte 2 desde la celda 28 *(1)*.** Parte del estado dado en la primera fila de la tabla. Ejecuta las instrucciones de las celdas 28, 29 y 30, una a una.

| Instrucción ejecutada | PC | R1 | R2 | R3 | MEM[90] | MEM[91] |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| (estado de partida) | 28 | 0 | 10 | 0 | 5 | 10 |
| `LOAD R1, [91]` | `____` | `____` | `____` | `____` | `____` | `____` |
| `ADD R3, R1, R2` | `____` | `____` | `____` | `____` | `____` | `____` |
| `STORE [90], R3` | `____` | `____` | `____` | `____` | `____` | `____` |

**b) Fíjate en la `LOAD R1, [91]` de la celda 28 *(0,5)*.** En el *fetch* de la `LOAD`, ¿qué valor tiene el MAR? Luego, en el *execute*, ¿qué valores tienen el MAR y el MDR cuando el dato llega desde la memoria? ¿Qué contiene el IR en ese momento?

Respuesta: `______________________________________________`

<details>
<summary>🃏 <b>4.1 — Solución</b></summary>

**a)**

| Instrucción ejecutada | PC | R1 | R2 | R3 | MEM[90] | MEM[91] |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `LOAD R1, [91]` | 29 | 10 | 10 | 0 | 5 | 10 |
| `ADD R3, R1, R2` | 30 | 10 | 10 | 20 | 5 | 10 |
| `STORE [90], R3` | 31 | 10 | 10 | 20 | 20 | 10 |

Criterios: 0,5 por fila, si todos los valores son correctos; 0,25 si solo un valor es incorrecto. Error arrastrado: puntuación completa si es coherente con los valores del estudiante. Puntos delicados: R1 y R2 valen ambos 10 (la `LOAD` vuelve a leer lo que la `STORE` ha escrito); la suma es 20. La última `STORE` sobrescribe MEM[90] (5 → 20); MEM[91] no cambia.

**b)** En el fetch, el MAR vale **28** (copia del PC antes de avanzar). En el execute, el MAR vale **91** (dirección del dato) y el MDR vale **10** (el contenido de MEM[91]); el IR todavía contiene **`LOAD R1, [91]`**, porque el dato pasa por el MDR y llega a R1 sin sobrescribir la instrucción. Criterios: 0,25 por MAR = 28 en el fetch y MAR = 91 en el execute; 0,25 por MDR = 10 e IR = `LOAD R1, [91]`. Errores frecuentes: MAR = 10 (intercambio entre dirección y contenido), IR = 10 (el dato sobrescribe la instrucción), MAR = 29 (PC ya avanzado).

</details>

### 4.2 🔍 (1,5 puntos)

**Un programa procesa los valores de un vector guardado en posiciones consecutivas.** La caché guarda bloques de **8 posiciones consecutivas**: 0-7, 8-15, 16-23, ... Responde a los tres casos, explicando el razonamiento.

a) La caché está vacía. El programa lee la dirección **35** y luego, enseguida, **38** y **40**. Para cada una de las tres lecturas indica HIT o MISS y qué bloque se necesita. Supón que el bloque cargado se queda en la caché. *(0,5)*

Respuesta: `______________________________________________`

b) El programa suma los elementos de las direcciones **100, 101, 102, 103, 104, 105** (caché vacía al principio) y luego repite la misma suma una segunda vez. ¿Cuántos MISS hay en la primera pasada, si ningún bloque se sustituye? ¿Qué tipo de localidad hace más rápida la segunda pasada? *(0,5)*

Respuesta: `______________________________________________`

c) La caché tiene **una sola línea** de **4 posiciones** (bloques 0-3, 4-7, 8-11, 12-15); cada MISS sustituye la línea. Dos programas leen las 16 direcciones de 0 a 15. El primero las lee en orden: 0, 1, 2, ..., 15. El segundo salta de cuatro en cuatro: 0, 4, 8, 12, luego 1, 5, 9, 13, luego 2, 6, 10, 14, luego 3, 7, 11, 15. ¿Cuántos MISS hace cada uno? Explica por qué. *(0,5)*

Respuesta: `______________________________________________`

<details>
<summary>🃏 <b>4.2 — Solución</b></summary>

**a)** 35 es MISS (bloque 32-39, caché vacía); 38 es HIT (mismo bloque, ya cargado); 40 es MISS (bloque 40-47, nunca cargado). Criterios: 0,5 si los tres resultados son correctos con el bloque indicado; 0,25 si dos de tres. Error frecuente: considerar 38 un MISS porque «nunca leído antes», o 40 un HIT porque «está cerca».

**b)** 2 MISS en la primera pasada. Las direcciones 100-103 están en el bloque 96-103 (un MISS, luego tres HIT); 104 y 105 en el bloque 104-111 (un MISS, luego un HIT). La segunda pasada es más rápida por la localidad temporal (se reutilizan los mismos datos) y, en la primera, la espacial ya evitó cuatro MISS. Criterios: 0,25 por 2 MISS con los bloques correctos; 0,25 por localidad temporal. Error frecuente: 6 MISS (cada lectura tratada como nueva) o 1 MISS (bloques de 8 alineados a 100).

**c)** El primero hace **4 MISS** (uno por cada bloque: al leer 0-3 el bloque se queda cargado, luego se pasa a 4-7, ...). El segundo hace **16 MISS**: en cada lectura hace falta un bloque distinto del presente y, al volver a 1, 2, 3, el bloque 0-3 ya ha sido sustituido. Criterios: 0,25 por los dos números (4 y 16); 0,25 por la explicación que relaciona MISS, localidad espacial y sustitución de la línea. Error frecuente: decir que los dos hacen el mismo número de MISS porque leen las mismas 16 direcciones.

</details>

## ⭐ Extra (+2 puntos, opcional)

No hace falta para llegar a 10. La nota final no supera 10. La instrucción `BEQ` no se ha trabajado como objetivo de la evaluación: si quieres probarla, la regla está aquí.

`BEQ R1, R2, fine`: si `R1` y `R2` tienen el mismo valor, el programa continúa en la celda con la etiqueta `fine`; si no, pasa a la celda siguiente.

| Celda | Instrucción |
|---:|---|
| 50 | `LOAD R1, [40]` |
| 51 | `LOAD R2, [41]` |
| 52 | `BEQ R1, R2, fine` |
| 53 | `STORE [42], R1` |
| 54 | `fine: HALT` |

Estado inicial: `MEM[40] = 4`; `MEM[42] = 0`.

**⭐a (0,5)** Si `MEM[41] = 4`, ¿se ejecuta la `STORE` de la celda 53? ¿Cuánto vale `MEM[42]` al final? `______________________`

**⭐b (0,5)** Si `MEM[41] = 9`, ¿se ejecuta la `STORE`? ¿Cuánto vale `MEM[42]` al final? `______________________`

**⭐c (1) Escribe un programa.** Usando solo `LOAD`, `ADD`, `STORE` y `HALT`, escribe un programa que lea los números de las celdas `MEM[70]` y `MEM[71]`, los sume y escriba el resultado en `MEM[72]`. Una instrucción por celda, empezando en la celda 60.

| Celda | Instrucción |
|---:|---|
| 60 | `______________________` |
| 61 | `______________________` |
| 62 | `______________________` |
| 63 | `______________________` |
| 64 | `______________________` |

<details>
<summary>🃏 <b>⭐ — Solución</b></summary>

**⭐a.** No. R1 y R2 valen ambos 4, el `BEQ` salta a `fine`, la `STORE` se salta y MEM[42] sigue en 0.

**⭐b.** Sí. R1 = 4 y R2 = 9 son distintos: el `BEQ` no salta, la `STORE` se ejecuta y MEM[42] pasa a 4.

Criterios ⭐a y ⭐b: 0,25 por «ejecutada sí/no» y 0,25 por el valor de MEM[42], en cada caso.

**⭐c.**

| Celda | Instrucción |
|---:|---|
| 60 | `LOAD R1, [70]` |
| 61 | `LOAD R2, [71]` |
| 62 | `ADD R3, R1, R2` |
| 63 | `STORE [72], R3` |
| 64 | `HALT` |

Criterios (1 punto): 0,25 por las dos `LOAD` (registro primero, dirección entre corchetes, registros distintos); 0,25 por el `ADD` con el destino primero y los dos registros ya cargados; 0,25 por la `STORE` con la dirección primero y un registro que contiene la suma; 0,25 por el orden correcto y por el `HALT` final. Se aceptan registros distintos o un orden distinto de las dos `LOAD`.

Errores frecuentes: `STORE R3, [72]` (argumentos intercambiados); `ADD` antes de las `LOAD`; `LOAD R1, 70` sin corchetes (número en lugar del contenido); olvidar el `HALT`.

</details>

## Espacio para el debate en grupo

Después de la prueba, comparad las filas de las dos tablas y las respuestas de las casillas. ¿Dónde no estáis de acuerdo? Intentad explicar el error a quien ha respondido de otra manera, sin decir enseguida el resultado.

## Recordatorio · las instrucciones de nuestra máquina

Esta tabla solo sirve de ayuda: no hace falta memorizarla.

| Instrucción | Qué hace |
|---|---|
| `LOAD R1, [50]` | Copia en `R1` el contenido de la celda 50. La celda no cambia. |
| `STORE [52], R3` | Copia el contenido de `R3` en la celda 52. `R3` no cambia. |
| `ADD R3, R1, R2` | Suma `R1` y `R2` y escribe el resultado en `R3` (el destino es el primero). |
| `HALT` | Detiene el programa. |
| `BEQ R1, R2, fine` | (solo extra ⭐) Si `R1` y `R2` son iguales, salta a la etiqueta `fine`. |

Después del fetch de cada instrucción, el PC avanza uno.
