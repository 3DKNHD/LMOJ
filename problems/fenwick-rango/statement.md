# Suma con updates

Arreglo $a_1\dots a_n$ y $q$ operaciones:

- `1 i x` — suma $x$ a $a_i$ ($x$ puede ser negativo)
- `2 L R` — imprime $a_L+\cdots+a_R$

Fenwick (no $O(nq)$).

## Entrada

$n$ $q$ ($1 \le n,q \le 2 \cdot 10^5$).

$n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

Luego $q$ líneas: `1 i x` ($1 \le i \le n$, $-10^9 \le x \le 10^9$) o `2 L R` ($1 \le L \le R \le n$).

Hay al menos una operación tipo 2.

## Salida

Una línea por cada tipo 2.
