# Un solo aula

El centro cultural tiene **un** aula decente y $n$ propuestas de taller. La $i$-ésima ocuparía el intervalo cerrado de minutos $[L_i, R_i]$ (el reloj es un entero: minuto $1$, $2$, $3$, …).

Dos talleres son incompatibles si existe al menos un minuto en el que ambos querrían el aula. En particular, si uno termina en el minuto $t$ y el otro empieza en el minuto $t$, **chocan**: ese minuto no se comparte.

No se pueden partir talleres ni moverlos. Hay que aceptar el **máximo** subconjunto en el que nadie se pisa. No piden cuáles, solo cuántos.

## Entrada

La primera línea contiene $n$ ($1 \le n \le 2 \cdot 10^5$).

Siguen $n$ líneas con $L$ $R$ ($1 \le L \le R \le 10^9$).

## Salida

Un único entero: el máximo de talleres compatibles.
