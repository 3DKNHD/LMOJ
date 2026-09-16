# Adelantamientos

En el recreo se formó una fila de $n$ personas, de la puerta hacia atrás. La persona en la posición $i$ (más cerca de la puerta si $i$ es chico) mide $a_i$.

Un **adelantamiento** es un par de posiciones $i < j$ ($i$ más adelante, $j$ más atrás) donde el de adelante es **estrictamente más alto** que el de atrás: $a_i > a_j$. La idea es que, para salir, el de atrás tendría que esquivar a alguien más alto que ya está delante. Si miden igual, no cuenta.

Puede haber muchas personas y estaturas repetidas. Cuenta cuántos adelantamientos hay en la fila.

## Entrada

La primera línea contiene un entero $n$ ($1 \le n \le 2 \cdot 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($1 \le a_i \le 10^9$).

## Salida

Un único entero: la cantidad de pares $(i, j)$ con $i < j$ y $a_i > a_j$.
