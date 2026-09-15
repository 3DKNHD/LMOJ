# Mochila 0/1

$n$ objetos, cada uno **a lo sumo una vez**. Capacidad $W$. Maximiza la suma de valores.

Recorre $W$ **de atrás hacia adelante**. $n \cdot W \le 10^7$.

## Entrada

$n$ $W$ ($1 \le n \le 100$, $1 \le W \le 10^5$).

$n$ líneas $w_i$ $v_i$ ($1 \le w_i \le W$, $1 \le v_i \le 10^9$).

## Salida

El valor máximo (64 bits).
