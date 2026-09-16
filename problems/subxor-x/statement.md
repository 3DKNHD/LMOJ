# El código $X$

El laboratorio de señales grabó una secuencia $a_1, \dots, a_n$ de enteros no negativos. El «código secreto» de esta semana es un entero $X$.

Un **tramo** es un pedazo contiguo $a_L, a_{L+1}, \dots, a_R$. El valor del tramo es el XOR de todos esos números (el XOR de un solo elemento es él mismo).

¿Cuántos tramos tienen valor exactamente $X$? El total puede ser grande.

## Entrada

La primera línea contiene $n$ y $X$ ($1 \le n \le 2 \cdot 10^5$, $0 \le X < 2^{30}$).

La segunda línea contiene $n$ enteros $a_i$ ($0 \le a_i < 2^{30}$).

## Salida

Un único entero: la cantidad de subarreglos contiguos con XOR igual a $X$.
