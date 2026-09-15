# Inversiones

Una **inversión** es un par de índices $(i, j)$ con $1 \le i < j \le n$ y $a_i > a_j$.
Dado el arreglo, cuenta cuántas inversiones hay.

## Entrada

La primera línea contiene un entero $n$ ($1 \le n \le 2 \cdot 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($1 \le a_i \le 10^9$). Puede haber repetidos.

## Salida

Un único entero: el número de inversiones.

## Restricciones

$O(n^2)$ no entra en el caso máximo. Valores repetidos **no** forman inversión.
