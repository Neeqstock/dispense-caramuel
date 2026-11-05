[⬅️ S3 - Registros y recorridos de datos](%28STU%29%20ESP%203EI%20sett-ott%20S3%20-%20Registros%20y%20recorridos%20de%20datos.md) · 🏠 [Índice](%28STU%29%20ESP%203EI%20-%20SETT-OTT.md) · [S4 - El ciclo de máquina](%28STU%29%20ESP%203EI%20sett-ott%20S4%20-%20El%20ciclo%20de%20m%C3%A1quina.md) ➡️

# ESP 💻 Lenguaje ensamblador: lo básico

**3EI · Septiembre-Octubre · Integración**

## 🧭 Primera distinción

El **lenguaje máquina** está formado por bits. El **lenguaje ensamblador** usa nombres cortos, como `ADD` y `LOAD`, para representar las instrucciones. La CPU no ejecuta directamente estas palabras: un ensamblador las traduce a códigos máquina.

**MIPS** es una familia de arquitecturas para procesadores, basada en un conjunto de instrucciones RISC: un repertorio de instrucciones relativamente sencillas y regulares. Se estudia a menudo porque hace visibles los pasos entre registros, cálculos y memoria. Su lenguaje ensamblador usa registros con nombres como `$t0` y `$s0`; las reglas precisas dependen de la variante de MIPS.

En los ejemplos de los apuntes S2-S4 usamos un lenguaje ensamblador didáctico, muy simplificado, no el MIPS real. La tabla de abajo lo completa y muestra, cuando es posible, la instrucción MIPS parecida. Las dos columnas no siempre son intercambiables: MIPS tiene reglas y registros propios.

## 🧰 Las instrucciones que necesitamos

| Instrucción didáctica | Qué hace                                                      | Instrucción MIPS parecida                                                                   |
| -------------------- | ------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `LOAD R1, [40]`      | Copia en `R1` el contenido de la celda de memoria 40.         | `lw $t0, 0($s0)` lee una palabra de la dirección contenida en `$s0` más el offset.          |
| `STORE [41], R3`     | Copia el contenido de `R3` en la celda de memoria 41.         | `sw $t2, 4($s0)` escribe una palabra en la dirección `$s0 + 4`.                             |
| `ADD R3, R1, R2`     | Suma `R1` y `R2`; pone el resultado en `R3`.                  | `add $t2, $t0, $t1`                                                                         |
| `SUB R3, R1, R2`     | Resta `R2` de `R1`; pone el resultado en `R3`.                | `sub $t2, $t0, $t1`                                                                         |
| `ADDI R1, R1, 1`     | Suma la constante 1 a `R1`.                                   | `addi $t0, $t0, 1`                                                                          |
| `BEQ R1, R2, uguali` | Si `R1` y `R2` son iguales, continúa desde la etiqueta `uguali`. | `beq $t0, $t1, uguali`                                                                   |
| `J inizio`           | Continúa desde la etiqueta `inizio`.                          | `j inizio`                                                                                  |
| `HALT`               | Detiene la máquina didáctica.                                 | No es una instrucción MIPS estándar: los simuladores usan convenciones específicas para terminar. |
BLE  R1, R2, miao      R1 <= R2

📌 `lw` y `sw` transfieren una **palabra** entre un registro y la memoria. En el ejemplo, `0($s0)` significa «dirección contenida en `$s0`, más 0 bytes»; `4($s0)` significa «cuatro bytes después». El offset (desplazamiento) no es el contenido de la celda.

Una **etiqueta** es un nombre asignado a la dirección de una instrucción: por ejemplo, `fine:` delante de `HALT` permite indicar ese destino sin escribir su dirección numérica. La etiqueta no es una instrucción y no ocupa una celda adicional en nuestro modelo.

**Salto si es cero:** no hace falta introducir un nuevo comando. Si R2 contiene cero, `BEQ R1, R2, fine` salta a `fine` cuando R1 es cero. R2 es un registro normal: hay que inicializarlo a cero, no lo contiene automáticamente. `BEQ` compara los dos registros, sin necesidad de un *flag* de cero ya activado. En los [apuntes sobre el ciclo de máquina](%28STU%29%20ESP%203EI%20sett-ott%20S4%20-%20El%20ciclo%20de%20m%C3%A1quina.md) se muestra un ejemplo completo con el conteo de billetes.

## ➕ Un programa pequeño

Queremos sumar los valores de las celdas 40 y 41 y escribir el resultado en la celda 42:

```text
LOAD R1, [40]
LOAD R2, [41]
ADD R3, R1, R2
STORE [42], R3
HALT
```

La CPU lee dos valores, los suma y escribe el resultado. `R1`, `R2` y `R3` son registros: en cambio, las direcciones entre corchetes indican celdas de memoria.

## ⚠️ No confundir

- `ADD destino, origen1, origen2`: el primer registro recibe el resultado.
- `LOAD` lleva un dato de la memoria a un registro; `STORE` hace el recorrido contrario.
- `HALT` pertenece a nuestro modelo didáctico: no lo copies como si fuera un comando MIPS universal.
- MIPS usa registros con nombres como `$t0` y `$s0`, y las direcciones de memoria siguen reglas propias. Aquí basta con reconocer la idea, no hace falta aprender la codificación binaria de las instrucciones.

---

[⬅️ S3 - Registros y recorridos de datos](%28STU%29%20ESP%203EI%20sett-ott%20S3%20-%20Registros%20y%20recorridos%20de%20datos.md) · 🏠 [Índice](%28STU%29%20ESP%203EI%20-%20SETT-OTT.md) · [S4 - El ciclo de máquina](%28STU%29%20ESP%203EI%20sett-ott%20S4%20-%20El%20ciclo%20de%20m%C3%A1quina.md) ➡️
