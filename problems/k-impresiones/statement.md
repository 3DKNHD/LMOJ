# K impresiones

Hay $n$ impresoras. La $i$-ésima saca **una** copia cada $t_i$ segundos (en el segundo $t_i$, $2t_i$, $3t_i$, …). ¿Cuál es el mínimo tiempo $T$ para tener al menos $k$ copias en total?

Busca $T$ por búsqueda binaria. Ojo con overflow: $t_i$ y $k$ llegan a $10^9$.

## Entrada

La primera línea contiene $n$ y $k$ ($1 \le n \le 2 \cdot 10^5$, $1 \le k \le 10^9$).

La segunda línea contiene $n$ enteros $t_i$ ($1 \le t_i \le 10^9$).

## Salida

Un único entero: el mínimo $T$.
