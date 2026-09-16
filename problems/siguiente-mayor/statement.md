# El próximo récord

Anotaron $n$ marcas de un ranking, de izquierda a derecha: $a_1, a_2, \dots, a_n$. Para cada posición $i$, el jurado quiere el **próximo récord a la derecha**: el primer valor estrictamente mayor que $a_i$ que aparezca después, es decir $a_j$ con el menor $j > i$ tal que $a_j > a_i$.

No piden el índice $j$, sino **el valor** $a_j$. Si a la derecha de $i$ nadie lo supera, esa posición queda en $-1$.

Puede haber empates y números negativos. Imprime $n$ enteros, uno por posición.

## Entrada

La primera línea contiene $n$ ($1 \le n \le 2 \cdot 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

## Salida

Una línea con $n$ enteros separados por espacios.
