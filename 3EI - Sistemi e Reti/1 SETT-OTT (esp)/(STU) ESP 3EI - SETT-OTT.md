# ESP 🗺️ 3EI - Septiembre/Octubre: cómo una máquina ejecuta un programa

**Sistemas y Redes · Teoría · 2 horas por semana · año escolar 2026/2027**

## 🧭 ¿De qué hablamos?

¿Cómo pasamos de una máquina construida para una sola tarea a otra que cambia su comportamiento cuando cambia el programa? Ya hemos seguido la historia hasta el modelo de Von Neumann. Ahora vamos a abrir ese mapa: seguiremos una instrucción para entender por qué necesitamos memoria, registros, cálculo, control y conexiones. También veremos por qué, a veces, un procesador rapidísimo se queda esperando. ⏳

## 📅 Las ocho semanas

| Semana | Tema | En pocas palabras |
|---|---|---|
| **S1** | [🖥️ De las máquinas a la CPU](%28STU%29%20ESP%203EI%20sett-ott%20S1%20-%20De%20las%20m%C3%A1quinas%20a%20la%20CPU.md) | De las máquinas de una sola tarea a una CPU con partes que guardan, calculan y coordinan; del relé al microprocesador y a los niveles de abstracción. |
| **S2** | [🏛️ La máquina de Von Neumann](%28STU%29%20ESP%203EI%20sett-ott%20S2%20-%20La%20m%C3%A1quina%20de%20Von%20Neumann.md) | Una máquina, muchos programas: las instrucciones y los datos comparten la misma memoria. |
| **S3** | [🗃️ Registros y recorridos de datos](%28STU%29%20ESP%203EI%20sett-ott%20S3%20-%20Registros%20y%20recorridos%20de%20datos.md) | Los pequeños «puestos de trabajo» de la CPU: quién guarda la dirección, el dato o la instrucción. |
| **S4** | [🔄 El ciclo de máquina](%28STU%29%20ESP%203EI%20sett-ott%20S4%20-%20El%20ciclo%20de%20m%C3%A1quina.md) | Buscar, interpretar y ejecutar: seguimos un programa paso a paso. |
| **S5** | [🧮 Direcciones y jerarquía de memoria](%28STU%29%20ESP%203EI%20sett-ott%20S5%20-%20Direcciones%20y%20jerarqu%C3%ADa%20de%20memoria.md) | Cuántas celdas se pueden direccionar con n bits y por qué ninguna memoria es a la vez grande, rápida y barata. |
| **S6** | [⚡ Caché, localidad y reloj](%28STU%29%20ESP%203EI%20sett-ott%20S6%20-%20Cach%C3%A9%2C%20localidad%20y%20reloj.md) | Mantener cerca lo que pronto se necesitará; el reloj como ritmo, no como medida de todo. |
| **S7** | [🧠 Reconstruir la máquina](%28STU%29%20ESP%203EI%20sett-ott%20S7%20-%20Reconstruir%20la%20m%C3%A1quina.md) | Repaso: conectamos las piezas y hacemos una prueba de entrenamiento. |
| **S8** | 🎯 Evaluación y recuperación (en preparación) | Evaluación de teoría, lectura de errores y recuperación. |

El calendario real puede moverse un poco: importa el orden de los temas, no la fecha exacta.

## 🧰 Cómo están organizados los apuntes

Al principio de cada apunte encontrarás un **mapa mental** con todos los títulos: es el índice de la lección. Cada tema tiene tres niveles, señalados con un emoji:

1. ✅ **Hay que saber:** lo que realmente debes saber y explicar.
2. 🔍 **Para entender a fondo:** los detalles que completan lo esencial.
3. 🤓 **Para curiosos:** opcional, para quien quiera descubrir más. No entra en la evaluación.

🃏 Después de cada parte hay **tarjetas de estudio (flashcards)**: lee la pregunta, responde en voz alta y luego despliega la respuesta para comprobar. En conjunto cubren todo el apunte: son la forma más rápida de repasar.

Al final encontrarás ejercicios y fuentes para profundizar.

## 🔭 Lo que todavía no estudiaremos

La comparación CISC/RISC y el rendimiento cuantitativo llegan en **noviembre-diciembre**. Las tuberías (*pipeline*) solo aparecen, si acaso, como idea de solapar trabajos: sin *hazards*, cuadrículas ni cálculos que haya que verificar ahora.

## 🔗 Integraciones

- [Lenguaje ensamblador básico](%28STU%29%20ESP%203EI%20-%20Lenguaje%20ensamblador%20b%C3%A1sico.md) — Completa las instrucciones usadas en los ejemplos.
