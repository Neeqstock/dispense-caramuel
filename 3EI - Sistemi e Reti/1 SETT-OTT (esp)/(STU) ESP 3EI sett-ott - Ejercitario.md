⬅️ [S7 - Reconstruir la máquina](%28STU%29%20ESP%203EI%20sett-ott%20S7%20-%20Reconstruir%20la%20m%C3%A1quina.md) · 🏠 [Índice](%28STU%29%20ESP%203EI%20-%20SETT-OTT.md)

# 🛠️ Ejercitario · 3EI sett-ott

**3EI · Septiembre-Octubre · Ejercitario con casos reales · Teoría y práctica escrita**

⏱️ **Tiempo: un dossier dura 10-20 minutos.** ✅ esencial: unos 75 minutos en total. 🔍 para la nota alta: unos 45 minutos. 🤓 se puede saltar. No es un deber para casa: elige los dossiers que necesites, aunque sea uno al día.

> **Leyenda:** ✅ hay que saber · 🔍 para entender a fondo · 🤓 opcional, para curiosos · 📜 caso real o verosímil · 🛠️ restauración · 📖 teoría · ✏️ práctica escrita · 🟢 resuelto: mira cómo se hace · 🎯 para probar: solución oculta · 🧠 para recordar · ⚠️ error común · 📌 control · 🃏 solución

Un museo de informática recibe como donación una sala llena de máquinas apagadas: un computador de los años cuarenta, una placa de a bordo, un viejo PC. Nadie sabe ya cómo funcionan. Tu grupo es el equipo técnico del **laboratorio de restauración** (el museo es inventado). Para ponerlas en marcha no hacen falta martillos: hace falta entender **qué guarda cada pieza, quién manda sobre quién y cuánto espera**.

Cada dossier parte de una máquina real o verosímil, de una avería que hay que encontrar o de una ficha técnica que hay que leer. Al final tienes que «reconstruir la máquina».

<u>Un computador no es un misterio: es una cadena de pequeñas reglas.</u> Conocerlas es la forma de saber dónde mirar cuando algo no va bien.

## Cómo se usa

- 🟢 **Resuelto.** Lee los pasos, luego tapa la solución con la mano y repite el ejercicio en tu cuaderno.
- 🎯 **Para probar.** Primero intenta resolverlo tú, en el cuaderno. Luego abre la tarjeta de estudio (flashcard) 🃏 y compara.
- Cada dossier tiene al menos un ejercicio resuelto, uno de teoría 📖 y uno de práctica escrita ✏️.
- **Las reglas del juego.** Las instrucciones son las de nuestra máquina: `LOAD`, `ADD`, `STORE`, `HALT`, con una instrucción por celda. Después del fetch, el PC avanza una posición. Si necesitas repasar la notación, mira la [hoja sobre el lenguaje ensamblador](%28STU%29%20ESP%203EI%20-%20Lenguaje%20ensamblador%20b%C3%A1sico.md).
- **Valores.** Nombres, celdas y números de los ejercicios son inventados. Los datos de los casos 📜 son reales y tienen la fuente al final.

| Dossier | Tema | Semana | Caso |
| :-----: | ------------------------------- | :-------: | ------------------------------------ |
| 1 | El programa entra en memoria | S1–S2 | ENIAC y EDSAC |
| 2 | Dentro de la CPU | S1, S3 | Shannon y los relés; el depurador |
| 3 | El ciclo de máquina | S4 | La centralita de un invernadero |
| 4 | Direcciones, buses y capacidad | S5 | IBM PC, Apolo, EDSAC |
| 5 | Jerarquía y caché | S5–S6 | La ficha técnica de un portátil |
| 6 | El reloj | S6 | La carrera de los GHz de los Pentium 4 |
| 7 | Reconstruye la máquina | S1–S6 | La prueba final del museo |

---

## 🛠️ Dossier 1 · El programa entra en memoria

*Se usa S1–S2: Von Neumann, dirección y contenido, los cinco bloques.*

### 📜 Caso real: de ENIAC a EDSAC

En 1946 el ENIAC, una de las primeras computadoras electrónicas, se «programa» a mano: hay que volver a conectar cables y girar interruptores. Para cambiar de cálculo hacen falta días. El trabajo lo hace un grupo de mujeres matemáticas, entre ellas Kay McNulty, Jean Jennings y Betty Snyder.

El 6 de mayo de 1949, en Cambridge, entra en funcionamiento el EDSAC. Tiene **512 palabras** de memoria, hechas de ondas sonoras que viajan dentro de tubos de mercurio. Su truco no está en el metal: está en la idea de guardar **también el programa en memoria**. Para cambiar de tarea ya no se toca ningún cable. Se cambian los números que están en las celdas.

🧠 <u>La máquina sigue siendo la misma. Cambia lo que hay en memoria.</u>

### 1.1 📖 Teoría · ✅ · 🟢 Resuelto — Qué hay en las celdas

**Enunciado.** En el laboratorio hay un computador con estas celdas (valores inventados):

```text
dirección:  60                61                 62      63    64
contenido:  LOAD R1, [63]     STORE [64], R1     HALT    9     0
```

1. ¿Qué celdas contienen instrucciones y cuáles datos?
2. ¿Qué diferencia hay entre `63` y `MEM[63]`?
3. ¿Qué cambia en la memoria después de ejecutar el programa?
4. Para que la máquina haga otro trabajo, ¿qué tienes que cambiar?

**Desarrollo.**

1. Las instrucciones están en las celdas **60, 61 y 62**. Los datos están en las celdas **63 y 64**.
2. `63` es la **dirección**: dice dónde está la celda. `MEM[63]` es su **contenido**: aquí vale 9.
3. La `LOAD` copia 9 en R1. La `STORE` copia R1 en la celda 64. Al final `MEM[64] = 9`. La celda 63 sigue valiendo 9, porque una copia no vacía el origen.
4. Cambias las **instrucciones escritas en memoria**. Las conexiones y los circuitos siguen igual.

📌 **Control.** Instrucciones y datos están en la misma memoria, en celdas distintas. Mirando solo los números nadie los distingue: los distingue la forma en que los usa el PC.

🧠 <u>La dirección dice dónde. El contenido dice qué hay.</u>

### 1.2 ✏️ Práctica · ✅ · 🎯 Para probar — Lee la memoria

**Enunciado.** Esta es la memoria de una máquina (valores inventados). El PC empieza en 200 y los registros valen 0.

| Dirección | 200 | 201 | 202 | 203 | 204 | 205 | 206 | 207 |
|---|---|---|---|---|---|---|---|---|
| Contenido | `LOAD R1, [205]` | `LOAD R2, [206]` | `ADD R3, R1, R2` | `STORE [207], R3` | `HALT` | 14 | 6 | 0 |

En tu cuaderno, responde:

a) ¿Cuánto vale `MEM[205]`?
b) ¿En qué dirección está la instrucción `HALT`?
c) ¿Cuáles son las celdas que contienen datos?
d) ¿Cuánto vale `MEM[207]` al final del programa?
e) Después de la `LOAD R1, [205]`, ¿la celda 205 sigue valiendo 14?

<details>
<summary>🃏 <b>1.2 — Solución</b></summary>

a) 14. b) 204. c) 205, 206 y 207. d) 20, porque R3 = 14 + 6 y la `STORE` lo copia en la celda 207. e) Sí: la `LOAD` copia, no mueve.

⚠️ **Error común:** decir que `MEM[205]` vale 205. El número 205 es la dirección; el contenido es 14.

</details>

### 1.3 📖 Teoría · 🔍 · 🎯 Para probar — Las frases del restaurador

**Enunciado.** Para cada frase escribe **verdadero** o **falso**. Si es falsa, corrígela en una frase.

A. «Para hacer otro trabajo con un computador de programa almacenado hay que volver a conectar los cables, como con el ENIAC.»
B. «Si en una celda hay escrito 70, ese 70 es necesariamente una dirección.»
C. «En una máquina de programa almacenado, las instrucciones son información como los datos: se pueden cargar y reemplazar en memoria.»
D. «En el modelo de Von Neumann, los datos y las instrucciones están en la misma memoria.»

<details>
<summary>🃏 <b>1.3 — Solución</b></summary>

A. **Falso.** Basta con cambiar lo que hay en memoria: instrucciones y datos. Los cables se quedan donde están.
B. **Falso.** Un número en una celda puede ser un dato, o la parte de una instrucción que indica una dirección. Depende de cómo lo use la máquina.
C. **Verdadero.**
D. **Verdadero.**

</details>

### 1.4 ✏️ Práctica · ✅ · 🎯 Para probar — Los cinco bloques de un computador

**Enunciado.** Un viejo computador del museo tiene un teclado, una RAM que contiene el programa, un altavoz, el procesador que ejecuta las instrucciones y las conexiones entre las piezas. En tu cuaderno, asigna cada elemento a uno de los **cinco bloques** del modelo (CPU, memoria principal, entrada, salida, conexiones). Luego responde: ¿una tarjeta de red es de entrada o de salida?

<details>
<summary>🃏 <b>1.4 — Solución</b></summary>

Teclado → **entrada**. RAM con el programa → **memoria principal**. Altavoz → **salida**. Procesador → **CPU**. Cables y pistas de conexión → **conexiones**. Una tarjeta de red es **ambas cosas**: lleva datos al sistema y los saca de él.

</details>

---

## 🛠️ Dossier 2 · Dentro de la CPU

*Se usa S1 y S3: interruptores, parte operativa y de control, registros y notación.*

### 📜 Caso real: Shannon y los relés, 1937

En 1937 un joven investigador del MIT, Claude Shannon, escribe su tesis con una idea que parece un juego. Los circuitos hechos de **relés**, es decir, interruptores controlados por una señal eléctrica, pueden realizar el álgebra de Boole. Dos interruptores en serie dejan pasar la corriente solo si están los dos cerrados: es un **AND**. Dos interruptores en paralelo la dejan pasar si basta con uno: es un **OR**. Un interruptor que se abre cuando recibe corriente da un **NOT**.

Desde ese momento los circuitos ya no se dibujan a prueba y error: se **diseñan** con la lógica. Relés, válvulas y transistores serán solo formas cada vez más pequeñas y rápidas de construir el mismo interruptor.

🧠 <u>Cada cálculo de la CPU está hecho de interruptores que se controlan unos a otros.</u>

### 2.1 📖 Teoría · ✅ · 🟢 Resuelto — La puerta del laboratorio

**Enunciado.** La puerta del laboratorio se abre en estos casos (escena inventada): si se presentan **la credencial y el código correcto**, o bien si hay **la llave de emergencia**. Escribe la condición con AND y OR y dibuja los interruptores.

**Desarrollo.**

1. La credencial y el código hacen falta **juntos**: son dos interruptores **en serie**. Es un AND.
2. La llave basta **sola**: es una rama **en paralelo**. Es un OR.
3. Condición: `(credencial AND código) OR llave`.

```text
          credencial    código
      +-----/ -------/ ----------+
 ----+                           +----- cerradura
      +----------/ --------------+
                llave
```

| Credencial | Código | Llave | ¿Se abre la puerta? |
|:-:|:-:|:-:|:-:|
| sí | sí | no | sí |
| sí | no | no | no |
| no | no | sí | sí |
| sí | no | sí | sí |

📌 **Control.** Un solo interruptor cerrado en la serie no basta. Una rama en paralelo cerrada sí basta.

⚠️ **Error común:** confundir serie y paralelo. Serie = «todos», AND. Paralelo = «al menos uno», OR.

### 2.2 ✏️ Práctica · ✅ · 🎯 Para probar — ¿Operativa o de control?

**Enunciado.** Para cada uno de estos elementos de una CPU, escribe si pertenece a la **parte operativa** o a la **parte de control**. La pregunta guía: *¿este circuito toca los datos o manda sobre quien los toca?*

1. El registro R1, que contiene 7.
2. La ALU, que transforma 7 y 5 en 12.
3. La CU, que decide «aquí se hace una suma, no una resta».
4. La conexión que lleva el contenido de R1 hacia la ALU.
5. La señal «abre la conexión desde R2».
6. El registro que conserva el resultado 12.

<details>
<summary>🃏 <b>2.2 — Solución</b></summary>

1. **Operativa**: guarda un dato.
2. **Operativa**: transforma los datos.
3. **Control**: decide, no toca los datos.
4. **Operativa**: mueve los datos; lo abre una señal de control.
5. **Control**: es una orden, no un dato.
6. **Operativa**: guarda un dato.

🧠 La CU **no calcula** ni **guarda** datos: los dirige.

</details>

### 2.3 ✏️ Práctica · ✅ · 🎯 Para probar — La notación de los registros

**Enunciado.** Estado inicial: `R1 = 3`, `R2 = 0`, `MAR = 0`, `MDR = 0`, `MEM[95] = 11`. Ejecuta los cuatro pasos **uno a uno** y completa la tabla después de cada uno.

| Paso | R1 | R2 | MAR | MDR | MEM[95] |
|---|:-:|:-:|:-:|:-:|:-:|
| `R2 <- 5` | `__` | `__` | `__` | `__` | `__` |
| `MAR <- 95` | `__` | `__` | `__` | `__` | `__` |
| `MDR <- MEM[95]` | `__` | `__` | `__` | `__` | `__` |
| `R1 <- MDR` | `__` | `__` | `__` | `__` | `__` |

<details>
<summary>🃏 <b>2.3 — Solución</b></summary>

| Paso | R1 | R2 | MAR | MDR | MEM[95] |
|---|:-:|:-:|:-:|:-:|:-:|
| `R2 <- 5` | 3 | 5 | 0 | 0 | 11 |
| `MAR <- 95` | 3 | 5 | 95 | 0 | 11 |
| `MDR <- MEM[95]` | 3 | 5 | 95 | 11 | 11 |
| `R1 <- MDR` | 11 | 5 | 95 | 11 | 11 |

📌 La flecha **copia**: el origen no cambia. `MEM[95]` vale 11 desde el principio hasta el final.

⚠️ **Error común:** escribir `MAR = 11`. El MAR guarda la **dirección** (95), el MDR guarda el **contenido** (11).

</details>

### 2.4 📖 Teoría · 🔍 · 🎯 Para probar — El panel del depurador

**Enunciado.** Un depurador (debugger) es un programa que te deja ver los registros mientras otro programa se ejecuta. El restaurador mira este panel (valores inventados). En la celda 150 hay `LOAD R2, [260]` y `MEM[260] = 18`.

| | PC | MAR | MDR | IR | R2 |
|---|:-:|:-:|:-:|:-:|:-:|
| **Panel A** · fetch terminado | 151 | 150 | `LOAD R2, [260]` | `LOAD R2, [260]` | 0 |
| **Panel B** · dato llegado | 151 | 260 | 18 | `LOAD R2, [260]` | 0 |

a) ¿Qué registro dice dónde buscar la **siguiente instrucción**?
b) ¿Por qué en el panel A el MAR vale 150 y no 151?
c) ¿Por qué en el panel B el MAR vale 260 y el IR sigue igual?
d) ¿Cuánto vale R2 al final de la instrucción?

<details>
<summary>🃏 <b>2.4 — Solución</b></summary>

a) El **PC**.
b) El MAR recibe el valor del PC **antes** de que el PC avance: para buscar la instrucción ha usado 150. Después el PC pasa a 151.
c) En el segundo acceso, el MAR guarda la dirección del **dato** (260). El IR sigue guardando la orden hasta que la instrucción termina: el dato llega al MDR, no al IR.
d) 18, porque el contenido del MDR se copia en R2.

⚠️ **Error común:** pensar que, después de la `LOAD`, el PC salta a 260. El PC sigue con la instrucción siguiente; 260 es la dirección de un dato.

</details>

---

## 🛠️ Dossier 3 · El ciclo de máquina

*Se usa S4: fetch, decode, execute, trazas de programa, buses.*

### 📜 Escena verosímil: la centralita del invernadero (inventada)

En el museo hay la centralita de un viejo invernadero: un pequeño computador que vigila la temperatura. Cada día hace el mismo recorrido. Toma la siguiente instrucción. Entiende qué pide. La ejecuta. Luego pasa a la siguiente.

Buscar (**fetch**), interpretar (**decode**), ejecutar (**execute**). Si la centralita se bloquea, el restaurador no puede «oír» qué va mal. Tiene que seguir el programa paso a paso, igual que hace la CPU.

🧠 <u>Una máquina de programa almacenado siempre hace el mismo recorrido: lee, entiende, ejecuta y pasa a la siguiente.</u>

### 3.1 ✏️ Práctica · ✅ · 🟢 Resuelto — Sube la temperatura objetivo

**Enunciado.** En memoria hay este programa (valores inventados). La temperatura objetivo del invernadero está en `MEM[300]` y el paso de aumento en `MEM[301]`.

| Celda | Instrucción |
|---:|---|
| 120 | `LOAD R1, [300]` |
| 121 | `LOAD R2, [301]` |
| 122 | `ADD R1, R1, R2` |
| 123 | `STORE [300], R1` |
| 124 | `HALT` |

**Estado inicial:** `PC = 120`, `R1 = 0`, `R2 = 0`, `MEM[300] = 20`, `MEM[301] = 5`. Después del fetch, el PC avanza una posición. Ejecuta las primeras cuatro instrucciones.

**Desarrollo.**

| Instrucción ejecutada | PC | R1 | R2 | MEM[300] |
|---|:-:|:-:|:-:|:-:|
| (estado inicial) | 120 | 0 | 0 | 20 |
| `LOAD R1, [300]` | 121 | 20 | 0 | 20 |
| `LOAD R2, [301]` | 122 | 20 | 5 | 20 |
| `ADD R1, R1, R2` | 123 | 25 | 5 | 20 |
| `STORE [300], R1` | 124 | 25 | 5 | 25 |

📌 **Control.** En cada fila cambia **una sola** cosa entre registros y memoria. El PC siempre avanza una posición y nunca vale 300: 300 es la dirección de un dato.

⚠️ **Error común:** escribir `MEM[300] = 25` ya después del `ADD`. El `ADD` cambia solo R1: la memoria cambia únicamente con la `STORE`.

🧠 <u>Una instrucción a la vez, un cambio a la vez.</u>

### 3.2 ✏️ Práctica · ✅ · 🎯 Para probar — Tres veces la dosis

**Enunciado.** Aquí tienes otro programa (valores inventados).

| Celda | Instrucción |
|---:|---|
| 140 | `LOAD R1, [310]` |
| 141 | `ADD R2, R1, R1` |
| 142 | `ADD R3, R2, R1` |
| 143 | `STORE [311], R3` |
| 144 | `STORE [310], R2` |
| 145 | `HALT` |

**Estado inicial:** `PC = 140`, `R1 = R2 = R3 = 0`, `MEM[310] = 6`, `MEM[311] = 0`. Ejecuta las primeras cinco instrucciones, una a una, y completa la tabla.

| Instrucción ejecutada | PC | R1 | R2 | R3 | MEM[310] | MEM[311] |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| `LOAD R1, [310]` | `__` | `__` | `__` | `__` | `__` | `__` |
| `ADD R2, R1, R1` | `__` | `__` | `__` | `__` | `__` | `__` |
| `ADD R3, R2, R1` | `__` | `__` | `__` | `__` | `__` | `__` |
| `STORE [311], R3` | `__` | `__` | `__` | `__` | `__` | `__` |
| `STORE [310], R2` | `__` | `__` | `__` | `__` | `__` | `__` |

<details>
<summary>🃏 <b>3.2 — Solución</b></summary>

| Instrucción ejecutada | PC | R1 | R2 | R3 | MEM[310] | MEM[311] |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| `LOAD R1, [310]` | 141 | 6 | 0 | 0 | 6 | 0 |
| `ADD R2, R1, R1` | 142 | 6 | 12 | 0 | 6 | 0 |
| `ADD R3, R2, R1` | 143 | 6 | 12 | 18 | 6 | 0 |
| `STORE [311], R3` | 144 | 6 | 12 | 18 | 6 | 18 |
| `STORE [310], R2` | 145 | 6 | 12 | 18 | 12 | 18 |

⚠️ **Errores comunes:** leer `ADD R2, R1, R1` como R2 = 1 o R2 = 6 (suma R1 consigo mismo: 12). Confundir `STORE [310], R2` con una `LOAD` (R2 no cambia) en lugar de modificar `MEM[310]`.

📌 R3 = R2 + R1 = 12 + 6 = 18. El destino es siempre el **primer** registro del `ADD`.

</details>

### 3.3 📖 Teoría · ✅ · 🎯 Para probar — Qué pasa por los buses

**Enunciado.** Para el programa del 3.2, completa la tabla de los tres buses (direcciones, control, datos). En la tercera fila, R3 vale 18.

| Qué ocurre | Bus de direcciones | Bus de control | Bus de datos |
|---|---|---|---|
| Fetch de la instrucción de la celda 140 | `__` | `__` | `__` |
| Lectura del dato pedido por la `LOAD R1, [310]` | `__` | `__` | `__` |
| Escritura de la `STORE [311], R3` | `__` | `__` | `__` |

<details>
<summary>🃏 <b>3.3 — Solución</b></summary>

| Qué ocurre | Bus de direcciones | Bus de control | Bus de datos |
|---|---|---|---|
| Fetch de la celda 140 | 140 | READ | `LOAD R1, [310]`, de la memoria a la CPU |
| Lectura del dato | 310 | READ | 6, de la memoria a la CPU |
| Escritura de la `STORE` | 311 | WRITE | 18, de la CPU a la memoria |

🧠 <u>Direcciones: dónde. Datos: qué. Control: qué acción.</u> El bus de direcciones siempre va de la CPU a la memoria.

</details>

### 3.4 📖 Teoría · 🔍 · 🎯 Para probar — El fetch con MAR y MDR

**Enunciado.** Antes del fetch de la instrucción de la celda 142, `ADD R3, R2, R1`, el PC vale 142, `MAR = 0`, `MDR = 0` y el IR está vacío. Escribe los valores de MAR, MDR, IR y PC **después de cada paso**. Luego responde: ¿la `ADD` necesita leer la memoria en la fase de execute? ¿Y la `LOAD` de la celda 140?

| Paso | Qué ocurre | MAR | MDR | IR | PC |
|---:|---|:-:|:-:|:-:|:-:|
| 1 | El MAR recibe el valor del PC. | `__` | `__` | `__` | `__` |
| 2 | La CU pide **READ**. | `__` | `__` | `__` | `__` |
| 3 | La instrucción pasa de la memoria al MDR. | `__` | `__` | `__` | `__` |
| 4 | La instrucción pasa del MDR al IR. | `__` | `__` | `__` | `__` |
| 5 | El PC avanza. | `__` | `__` | `__` | `__` |

<details>
<summary>🃏 <b>3.4 — Solución</b></summary>

| Paso | MAR | MDR | IR | PC |
|---:|:-:|:-:|:-:|:-:|
| 1 | 142 | 0 | vacío | 142 |
| 2 | 142 | 0 | vacío | 142 |
| 3 | 142 | `ADD R3, R2, R1` | vacío | 142 |
| 4 | 142 | `ADD R3, R2, R1` | `ADD R3, R2, R1` | 142 |
| 5 | 142 | `ADD R3, R2, R1` | `ADD R3, R2, R1` | 143 |

En el paso 2 no cambia ningún registro: la memoria está buscando la celda.

La **`ADD`** usa solo registros: la memoria no se lee de nuevo. En cambio, la **`LOAD R1, [310]`** lee la memoria **dos veces**: primero con MAR = 140 (MDR = la instrucción) y luego con MAR = 310 (MDR = 6).

</details>

### 3.5 🤓 · 🎯 Para probar — No riegues

> Un salto condicional `BEQ R1, R2, fin` cambia el PC solo si `R1` y `R2` son iguales. Aquí R2 vale siempre 0.
>
> | Celda | Instrucción |
> |---:|---|
> | 160 | `LOAD R1, [320]` |
> | 161 | `BEQ R1, R2, fin` |
> | 162 | `STORE [321], R1` |
> | 163 | `fin: HALT` |
>
> **Enunciado.** Con `MEM[321] = 9` al principio, escribe las direcciones de las instrucciones ejecutadas y el valor final de `MEM[321]` en dos casos: `MEM[320] = 0` y `MEM[320] = 4`.

<details>
<summary>🃏 <b>3.5 — Solución</b></summary>

- `MEM[320] = 0`: R1 = 0 = R2, la `BEQ` salta. Direcciones: **160 → 161 → 163**. `MEM[321]` sigue valiendo 9.
- `MEM[320] = 4`: R1 = 4 ≠ 0, la `BEQ` no salta. Direcciones: **160 → 161 → 162 → 163**. `MEM[321]` pasa a valer 4.

El salto cambia **qué instrucción viene después**, no el valor de los registros.

</details>

---

## 🛠️ Dossier 4 · Direcciones, buses y capacidad

*Se usa S5: bits y direcciones, bytes y palabras, buses.*

### 📜 Caso real: tres máquinas, tres potencias de dos

Tres máquinas, tres números que parecen al azar y, en cambio, son todos **potencias de dos**.

- **EDSAC** (1949): 512 palabras de memoria. Son 2⁹: bastan 9 bits para escribir una dirección.
- **Apollo Guidance Computer**, el computador de a bordo de las misiones Apolo: 2 048 palabras de RAM (2¹¹) y 36 864 palabras de memoria de solo lectura. Funcionaba a 2,048 MHz. Una palabra estaba formada por 16 bits: 15 de dato y 1 de control.
- **IBM PC** (1981), con el procesador Intel 8088: **20 líneas de dirección**. Con 20 bits se distinguen 2²⁰ = 1 048 576 posiciones, es decir, **1 MiB**. Pero la RAM llegaba a **640 KB**: los 384 KB restantes del espacio estaban reservados a ROM, memoria de vídeo y otros periféricos.

Es la historia más famosa del «límite de los 640 KB». <u>El espacio de direcciones no es la RAM que has instalado</u>: dice cuántas posiciones se pueden distinguir, no cuántas existen.

🧠 <u>Con n bits se distinguen 2ⁿ posiciones. Cada bit más las duplica.</u>

### 4.1 ✏️ Práctica · ✅ · 🟢 Resuelto — De cuántas celdas a cuántos bits

**Enunciado.** Para cada máquina, halla el número de bits de la dirección o el número de posiciones.

| Máquina | Dato | Qué hallar |
|---|---|---|
| EDSAC | 512 posiciones | bits de la dirección |
| Apolo (RAM) | 2 048 posiciones | bits de la dirección |
| IBM PC | 20 bits de dirección, 1 byte por posición | posiciones y capacidad |

**Desarrollo.**

1. **EDSAC.** Se duplica: 1, 2, 4, 8, 16, 32, 64, 128, 256, **512**. Hacen falta 9 duplicaciones: **9 bits**. Direcciones de 0 a 511.
2. **Apolo.** Después de 512 (2⁹) se duplica dos veces: 1 024, **2 048**. Son 2¹¹: **11 bits**. Direcciones de 0 a 2 047.
3. **IBM PC.** 2²⁰ = **1 048 576 posiciones**. Con 1 byte por posición son 1 048 576 bytes, es decir, **1 MiB**. La última dirección es 1 048 575.

📌 **Control.** El número de posiciones no es la última dirección: se cuenta desde 0, así que la última es una menos.

⚠️ **Error común:** pensar que 11 bits dan 11 posiciones, o 22. El número de posiciones crece **por duplicación**, no en proporción.

### 4.2 ✏️ Práctica · ✅ · 🎯 Para probar — La memoria de la estación meteorológica

**Enunciado.** Una estación meteorológica registra una medida de temperatura cada minuto, y cada medida ocupa 8 bits, es decir, **1 byte**. El museo guarda las medidas en una memoria con direcciones de **13 bits** (valores inventados).

a) ¿Cuántas posiciones tiene esta memoria?
b) ¿Cuál es la última dirección?
c) ¿Cuál es la capacidad, si cada posición es de 1 byte?
d) Si cada posición pasara a ser de **2 bytes**, ¿qué cambiaría: el número de direcciones o la capacidad?

<details>
<summary>🃏 <b>4.2 — Solución</b></summary>

a) 2¹³ = **8 192** posiciones. b) **8 191**. c) 8 192 × 1 byte = **8 192 bytes**, es decir, 8 KiB. d) Cambia la **capacidad**: 8 192 × 2 = 16 384 bytes, es decir, 16 KiB. El número de direcciones sigue siendo 8 192.

⚠️ **Error común:** decir que, si se duplican los bytes por posición, hacen falta más bits de dirección. Haría falta un bit más solo si se duplicaran las **posiciones**.

</details>

### 4.3 ✏️ Práctica · 🔍 · 🎯 Para probar — ¿Cuántos bits hacen falta?

**Enunciado.** El museo quiere direccionar al menos **3 000 posiciones**. ¿Cuántos bits de dirección hacen falta, como mínimo? ¿Cuántas posiciones distinguen de verdad? ¿Y si hicieran falta 36 864, como la ROM del Apolo, cuántos bits serían necesarios en nuestro modelo?

<details>
<summary>🃏 <b>4.3 — Solución</b></summary>

Con 11 bits se distinguen 2 048 posiciones: pocas. Con **12 bits** se distinguen **4 096**: bastan. Así que hacen falta **12 bits**, y las posiciones distintas son 4 096 (sobran 1 096).

Para 36 864: con 15 bits son 32 768, pocas; con **16 bits** son 65 536. En nuestro modelo hacen falta **16 bits**. El computador real del Apolo usaba otros mecanismos que aquí no estudiamos.

📌 Se busca la primera potencia de dos **mayor o igual** que el número pedido.

</details>

### 4.4 📖 Teoría · ✅ · 🎯 Para probar — ¿Qué bus?

**Enunciado.** Para cada una de estas frases, di a qué bus (direcciones, datos o control) se refiere.

A. «Quiero la celda 305.»
B. «¡Escribe!»
C. «El valor que hay que escribir es 17.»

Luego explica en una frase: ¿un bus de datos de 16 bits demuestra que la memoria solo tiene 2¹⁶ bytes?

<details>
<summary>🃏 <b>4.4 — Solución</b></summary>

A. **Direcciones** (dónde). B. **Control** (qué acción, aquí WRITE). C. **Datos** (qué contenido).

**No.** El ancho del bus de datos indica cuánto se transfiere de una vez; es el ancho del bus de **direcciones** el que dice cuántas posiciones se distinguen.

</details>

### 4.5 📖 Teoría · 🔍 · 🎯 Para probar — Por qué 640 y no 1 024

**Enunciado.** El IBM PC distinguía 1 MiB de direcciones, pero la RAM disponible para los programas era de 640 KB. Explica en dos o tres frases adónde iban los otros 384 KB. Luego responde: si hoy lees «16 GB de RAM» y «512 GB de SSD» en la ficha de un computador, ¿qué no debes hacer con esos dos números?

<details>
<summary>🃏 <b>4.5 — Solución</b></summary>

Los otros 384 KB del espacio de direcciones estaban **reservados** a ROM, memoria de vídeo y otros periféricos: no eran RAM para los programas. El espacio de direcciones dice cuántas posiciones se pueden distinguir, no cuánta RAM está instalada.

No debes **sumarlos**: RAM y SSD son memorias con funciones distintas (la RAM para lo que se usa ahora, el SSD para guardar los datos incluso con la máquina apagada). «528 GB de RAM» sería un error.

</details>

### 4.6 🤓 · 🎯 Para probar — ¿Por qué los PC de 32 bits «perdían» RAM?

> Con 32 bits de dirección y 1 byte por posición se distinguen 2³² = 4 294 967 296 posiciones, es decir, **4 GiB**. Pero no todas las direcciones corresponden a RAM: una parte estaba reservada a los dispositivos. Por eso muchos PC con sistemas de 32 bits «veían» menos RAM que la instalada.
>
> **Enunciado.** En una frase, ¿qué parecido hay con el límite de los 640 KB?

<details>
<summary>🃏 <b>4.6 — Solución</b></summary>

En los dos casos el espacio de direcciones era más grande que la RAM utilizable: una parte estaba reservada a otra cosa. <u>Una fórmula es fiable cuando sus hipótesis están escritas con claridad.</u>

</details>

---

## 🛠️ Dossier 5 · Jerarquía y caché

*Se usa S5 y S6: niveles de memoria, volatilidad, acierto y fallo, localidad.*

### 📜 Escena verosímil: la ficha del portátil (inventada)

Clara tiene que comprar un portátil para la escuela. La tienda le enseña la ficha (valores inventados): *procesador con 8 MB de caché, 8 GB de RAM, 256 GB de SSD.* Ella pregunta: «Entonces tengo 8 + 8 + 256 gigabytes de memoria, ¿no?». El técnico sonríe: «Son tres cosas distintas».

Ninguna memoria es a la vez grande, rápida, barata y capaz de guardar los datos sin electricidad. Por eso los computadores usan **varios niveles**. Los programas y los archivos en uso se cargan en la RAM; la caché, en cambio, la gestiona el hardware por sí solo.

🧠 <u>«Grande» no significa «rápido». Y «rápido» no significa «permanente».</u>

### 5.1 📖 Teoría · ✅ · 🟢 Resuelto — Lee la ficha

**Enunciado.** Para la ficha de Clara, di para cada fila **para qué sirve** y **qué pasa si se corta la electricidad**.

**Desarrollo.**

| Fila | Para qué sirve | Si se corta la electricidad |
|---|---|---|
| Caché 8 MB | Guarda copias de partes que se usan a menudo, cerca de la CPU | Se pierde (volátil) |
| RAM 8 GB | Guarda los programas y los datos **que se usan ahora** | Se pierde (volátil) |
| SSD 256 GB | Conserva los archivos y los proyectos a largo plazo | Se conserva (no volátil) |

📌 **Control.** Los tres números no se suman: son memorias distintas, con funciones distintas. Más RAM permite tener listos más datos; no hace más rápido el cálculo de la CPU.

⚠️ **Error común:** pensar que la caché es «un trozo de RAM extra» donde el programa elige dónde escribir. Es una **copia** que gestiona el hardware.

### 5.2 ✏️ Práctica · ✅ · 🎯 Para probar — La escala de las memorias

**Enunciado.** Completa la tabla de los cuatro niveles. Para «velocidad» y «capacidad», escribe **más** o **menos** que el nivel siguiente.

| Nivel | ¿Volátil? | Velocidad | Capacidad |
|---|:-:|:-:|:-:|
| Registros | `__` | `__` | `__` |
| Caché | `__` | `__` | `__` |
| RAM | `__` | `__` | `__` |
| SSD | `__` | `__` | `__` |

<details>
<summary>🃏 <b>5.2 — Solución</b></summary>

| Nivel | ¿Volátil? | Velocidad | Capacidad |
|---|:-:|:-:|:-:|
| Registros | sí | más rápidos que todos | menos que todos |
| Caché | sí | más rápida que la RAM | menos que la RAM |
| RAM | sí | más rápida que el SSD | menos que el SSD |
| SSD | **no** | menos rápido | más capacidad |

⚠️ **Error común:** pensar que la persistencia crece poco a poco al bajar en la jerarquía. Es una propiedad **aparte**: o la hay o no la hay.

</details>

### 5.3 ✏️ Práctica · ✅ · 🟢 Resuelto — Acierto y fallo, bloques de 4

**Enunciado.** La caché guarda **bloques de 4 posiciones consecutivas** (… 48-51, 52-55, 56-59 …). Un programa lee, en orden, las direcciones **52, 53, 54, 55, 56, 57, 58**. La caché está vacía al principio; no se reemplaza ningún bloque. Para cada lectura escribe ACIERTO (hit) o FALLO (miss).

**Desarrollo.**

| Lectura | Bloque | Resultado | Por qué |
|---:|---|---|---|
| 52 | 52-55 | **FALLO** | Caché vacía: carga todo el bloque |
| 53 | 52-55 | ACIERTO | Ya se había cargado |
| 54 | 52-55 | ACIERTO | Igual |
| 55 | 52-55 | ACIERTO | Igual |
| 56 | 56-59 | **FALLO** | Bloque nuevo |
| 57 | 56-59 | ACIERTO | Ya se había cargado |
| 58 | 56-59 | ACIERTO | Igual |

📌 **Control.** 2 FALLOS y 5 ACIERTOS. Los FALLOS son uno por cada bloque nuevo. Un acierto puede ser una dirección **nunca pedida antes**: basta con que su bloque ya esté en caché.

🧠 <u>Después de una dirección pueden hacer falta las vecinas: es la localidad espacial.</u>

### 5.4 ✏️ Práctica · 🔍 · 🎯 Para probar — El bucle que se repite

**Enunciado.** Un programa repite en bucle la lectura de tres medidas: lee, en orden, las direcciones **90, 91, 92**, y luego vuelve a empezar, **100 veces**. Los bloques son de 4 posiciones (88-91, 92-95). La caché está vacía al principio.

a) Si la caché tiene espacio para varios bloques, ¿cuántos FALLOS hay en total?
b) ¿Qué tipo de localidad hace más rápidas las repeticiones?
c) Ahora el bucle lee **90, 92, 90, 92, …** durante 100 veces, pero la caché tiene **una sola línea** (cada FALLO reemplaza la única línea). ¿Cuántos FALLOS hay?

<details>
<summary>🃏 <b>5.4 — Solución</b></summary>

a) **2 FALLOS**: uno por el bloque 88-91 (con 90 y 91) y uno por el bloque 92-95. Las otras 298 lecturas son ACIERTOS.
b) La **localidad temporal**: se reutilizan los mismos datos. (El 91 también es un caso de localidad espacial: está en el bloque del 90.)
c) **200 FALLOS**: el 90 y el 92 están en bloques distintos. En cada lectura, el bloque correcto acaba de ser sustituido por el otro.

⚠️ **Error común:** creer que volver a leer un dato garantiza un ACIERTO. Depende del espacio: con una sola línea, el bloque se reemplaza antes de volver a ser útil.

</details>

### 5.5 📖 Teoría · ✅ · 🎯 Para probar — Las frases del técnico

**Enunciado.** Corrige cada frase en una línea.

A. «Un fallo significa que el programa está roto.»
B. «La caché de 8 MB es un trozo de RAM extra.»
C. «Si duplico la RAM, el procesador calcula el doble de rápido.»

<details>
<summary>🃏 <b>5.5 — Solución</b></summary>

A. **No.** Un fallo es un suceso previsto: el dato no está en caché y hay que tomarlo del nivel siguiente, con una espera extra.
B. **No.** La caché es una **copia** de algunos contenidos, guardada cerca de la CPU: no es un espacio extra donde elegir dónde escribir.
C. **No.** Más RAM permite tener listos más programas y datos; no cambia la velocidad con la que la CPU calcula.

</details>

---

## 🛠️ Dossier 6 · El reloj

*Se usa S6: reloj, frecuencia, periodo.*

### 📜 Caso real: la carrera de los GHz

En noviembre de 2000 Intel presenta el **Pentium 4**. Con los años, su frecuencia de reloj sube de **1,3 GHz a 3,8 GHz**. Durante un tiempo, la cifra «GHz» de la caja se convierte en el número con el que se comparan los computadores: cuanto más alto, se cree, mejor.

Pero el reloj es solo un **ritmo**: dice cuánto dura un ciclo, no cuánto trabajo se hace en cada uno. Un procesador rápido puede quedarse parado esperando los datos.

🧠 <u>El reloj marca el tiempo. Cuánto trabajo se hace en ese tiempo es otra pregunta.</u>

### 6.1 ✏️ Práctica · ✅ · 🟢 Resuelto — Del GHz al nanosegundo

**Enunciado.** Halla la duración de un ciclo de reloj (el **periodo**) a 3,8 GHz y a 1,3 GHz.

**Desarrollo.** El periodo es el inverso de la frecuencia: `T = 1 ÷ f`.

1. **3,8 GHz** = 3,8 × 10⁹ Hz. `T = 1 ÷ (3,8 × 10⁹) ≈ 0,263 ns`.
2. **1,3 GHz** = 1,3 × 10⁹ Hz. `T = 1 ÷ (1,3 × 10⁹) ≈ 0,769 ns`.

📌 **Control.** Más frecuencia, periodo más corto: 3,8 GHz tiene un ciclo más corto que 1,3 GHz.

⚠️ **Error común:** decir que 3,8 GHz «completa 3,8 mil millones de instrucciones por segundo». Son **ciclos** por segundo.

### 6.2 ✏️ Práctica · ✅ · 🎯 Para probar — Cuánto dura un ciclo

**Enunciado.** Dos procesadores (valores inventados): **A** tiene un reloj de 2,5 GHz, **B** de 500 MHz.

a) ¿Cuánto dura un ciclo de A? ¿Y uno de B?
b) ¿Cuál de los dos tiene el ciclo más corto?
c) ¿Cuántos ciclos completa cada uno en **1 microsegundo** (1 µs = 10⁻⁶ s)?

<details>
<summary>🃏 <b>6.2 — Solución</b></summary>

a) A: `1 ÷ (2,5 × 10⁹) = 0,4 ns`. B: `1 ÷ (5 × 10⁸) = 2 ns`.
b) **A**: frecuencia más alta, periodo más corto.
c) A: 2,5 × 10⁹ × 10⁻⁶ = **2 500 ciclos**. B: 5 × 10⁸ × 10⁻⁶ = **500 ciclos**.

📌 Frecuencia y periodo son **inversos**: si uno sube, el otro baja.

</details>

### 6.3 📖 Teoría · ✅ · 🎯 Para probar — Verdadero o falso, GHz

**Enunciado.** Escribe verdadero o falso, y corrige si hace falta.

A. «Un reloj de 3 GHz significa tres mil millones de instrucciones por segundo.»
B. «A 1 GHz, un ciclo dura un nanosegundo.»
C. «Más GHz significan una caché más grande.»

<details>
<summary>🃏 <b>6.3 — Solución</b></summary>

A. **Falso.** Son tres mil millones de **ciclos** por segundo. Cuántas instrucciones se completan depende de cuántos ciclos necesita cada una.
B. **Verdadero.** `T = 1 ÷ 10⁹ s = 1 ns`.
C. **Falso.** La frecuencia y la capacidad de la caché son cosas distintas.

</details>

### 6.4 ✏️ Práctica · 🔍 · 🎯 Para probar — ¿Quién hace más trabajo?

**Enunciado.** Dos procesadores (valores inventados). El procesador **A** tiene un reloj de 2 GHz y completa una instrucción cada 2 ciclos. El procesador **B** tiene un reloj de 3 GHz y completa una instrucción cada 4 ciclos. ¿Cuántas instrucciones por segundo completa cada uno? ¿Cuál hace más?

<details>
<summary>🃏 <b>6.4 — Solución</b></summary>

A: 2 × 10⁹ ciclos por segundo ÷ 2 ciclos por instrucción = **1 000 millones** de instrucciones por segundo.
B: 3 × 10⁹ ÷ 4 = **750 millones** de instrucciones por segundo.

Hace más trabajo **A**, aunque tenga menos GHz. Para comparar dos sistemas hay que mirar el trabajo realizado y el tiempo empleado, no solo los GHz de la caja.

⚠️ Es un modelo simplificado: las CPU reales hacen varias cosas a la vez. Lo veremos en noviembre-diciembre.

</details>

### 6.5 🤓 · 🎯 Para probar — Más transistores, no necesariamente más rápido

> En 1965 Gordon Moore describió una tendencia: el número de componentes que se podían meter en un chip crecía a un ritmo regular. No es una ley de la naturaleza.
>
> **Enunciado.** Si en un chip entran más transistores, ¿por qué tu programa no se vuelve necesariamente más rápido? Pon un ejemplo con la caché.

<details>
<summary>🃏 <b>6.5 — Solución</b></summary>

Más transistores pueden convertirse en más caché, más núcleos o nuevas funciones. La ventaja depende de cómo los usen el sistema y el programa: un computador muy rápido puede igualmente quedarse parado esperando los datos. La pregunta útil es: **¿qué recurso limita este trabajo?**

</details>

---

## 🛠️ Dossier 7 · Reconstruye la máquina

*Nivel final. Se usa todo S1–S6.*

El museo ha vuelto a poner en marcha su máquina. Antes de reabrir la sala, te piden la prueba final: tres pruebas, con todo lo que has aprendido.

### 7.1 ✏️ Práctica · 🔍 · 🎯 Para probar — Suma tres medidas

**Enunciado.** Usando solo `LOAD`, `ADD`, `STORE` y `HALT`, escribe un programa que **sume las medidas de tres sensores**, que están en las celdas `MEM[410]`, `MEM[411]` y `MEM[412]`, y que escriba el resultado en `MEM[413]`. Una instrucción por celda, a partir de la celda 500.

| Celda | Instrucción |
|---:|---|
| 500 | `______________________` |
| 501 | `______________________` |
| 502 | `______________________` |
| 503 | `______________________` |
| 504 | `______________________` |
| 505 | `______________________` |
| 506 | `______________________` |

<details>
<summary>🃏 <b>7.1 — Solución</b></summary>

| Celda | Instrucción |
|---:|---|
| 500 | `LOAD R1, [410]` |
| 501 | `LOAD R2, [411]` |
| 502 | `LOAD R3, [412]` |
| 503 | `ADD R1, R1, R2` |
| 504 | `ADD R1, R1, R3` |
| 505 | `STORE [413], R1` |
| 506 | `HALT` |

Vale cualquier programa que lea los tres valores con tres `LOAD` en registros, los sume con dos `ADD` (el destino siempre primero) y los escriba con una `STORE` (la dirección primero). Se aceptan registros y orden distintos, siempre que la suma esté en el registro que escribe la `STORE` y haya un `HALT`.

⚠️ **Errores comunes:** `LOAD R1, 410` sin corchetes (el número 410 en lugar del contenido); `STORE R1, [413]` con los argumentos cambiados; un `ADD` antes de haber cargado los registros.

</details>

### 7.2 ✏️ Práctica · 🔍 · 🎯 Para probar — La prueba del programa

**Enunciado.** Ejecuta el programa del 7.1 con `MEM[410] = 5`, `MEM[411] = 10`, `MEM[412] = 15`, `MEM[413] = 0`, `PC = 500` y registros a 0.

a) ¿Cuánto valen R1, R2 y R3 al final?
b) ¿Cuánto vale `MEM[413]`?
c) Durante la fase de execute de la `STORE`, ¿qué pasa por el bus de direcciones, por el bus de datos y por el bus de control?
d) En ese momento, ¿cuánto valen MAR y MDR?

<details>
<summary>🃏 <b>7.2 — Solución</b></summary>

a) **R1 = 30**, **R2 = 10**, **R3 = 15**. b) **`MEM[413] = 30`**.

c) Bus de direcciones: **413**. Bus de datos: **30**, de la CPU a la memoria. Bus de control: **WRITE**.
d) **MAR = 413** y **MDR = 30**: el MAR guarda la dirección, y el MDR, el contenido que se escribe.

</details>

### 7.3 📖 Teoría · 🔍 · 🎯 Para probar — ¿«Basta con más GHz»?

**Enunciado.** Un compañero quiere comprar un portátil para programar y dice: «Basta con el procesador con más GHz». Responde en tres o cuatro frases. Menciona al menos tres de estos elementos: reloj, caché, RAM, SSD.

<details>
<summary>🃏 <b>7.3 — Solución</b></summary>

Una buena respuesta dice **qué** (la tesis), **cómo** funciona (el mecanismo) y trae un **ejemplo**. Por ejemplo:

«No, no basta. Los GHz indican cuántos ciclos de reloj hay en un segundo, no cuántas instrucciones se completan. Si el programa espera los datos, un reloj más rápido no ayuda: importa también si los datos ya están en caché (acierto) o hay que buscarlos en la RAM (fallo). Los programas en uso están en la RAM y se pierden si se apaga el computador, mientras que el SSD conserva los archivos. Por ejemplo, un portátil con menos GHz pero más RAM puede manejar un proyecto más grande sin pararse.»

📌 Comprueba: ¿has separado **reloj**, **caché**, **RAM** y **SSD**? ¿Has evitado decir «es más rápido» sin explicar por qué?

</details>

---

## 📚 Fuentes y recursos

Los datos de los casos 📜 vienen de estas páginas. Son un buen punto de partida: si necesitas un dato para un trabajo, compruébalo también en otra fuente.

- **EDSAC.** [EDSAC](https://en.wikipedia.org/wiki/EDSAC): 6 de mayo de 1949; 512 palabras de 17 bits en líneas de retardo de mercurio.
- **Apollo.** [Apollo Guidance Computer](https://en.wikipedia.org/wiki/Apollo_Guidance_Computer): 2 048 palabras de RAM, 36 864 palabras de ROM, 2,048 MHz, palabra de 15 bits más 1 de control.
- **IBM PC.** [Conventional memory](https://en.wikipedia.org/wiki/Conventional_memory): el procesador 8088 tenía 20 líneas de dirección (1 MB); los primeros 640 KB eran la RAM, y los 384 KB restantes estaban reservados al sistema y a los periféricos.
- **Pentium 4.** [Pentium 4](https://en.wikipedia.org/wiki/Pentium_4): lanzado el 20 de noviembre de 2000; frecuencias de 1,3 GHz a 3,8 GHz.
- **ENIAC y Shannon.** En los apuntes [S1](%28STU%29%20ESP%203EI%20sett-ott%20S1%20-%20De%20las%20m%C3%A1quinas%20a%20la%20CPU.md) y [S2](%28STU%29%20ESP%203EI%20sett-ott%20S2%20-%20La%20m%C3%A1quina%20de%20Von%20Neumann.md).
