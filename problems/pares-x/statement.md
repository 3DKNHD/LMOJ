# Pares que suman X

Dado un arreglo y un objetivo $X$, cuenta cuántos pares de **índices** $i < j$ cumplen $a_i + a_j = X$.

Puede haber repetidos. $O(n^2)$ no entra.

## Entrada

La primera línea contiene $n$ y $X$ ($1 \le n \le 2 \cdot 10^5$, $-2 \cdot 10^9 \le X \le 2 \cdot 10^9$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

## Salida

Un único entero: la cantidad de pares (cabe en 64 bits).
