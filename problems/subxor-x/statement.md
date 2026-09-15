# Subarreglos XOR

Cuántos subarreglos contiguos tienen XOR igual a $X$.
Prefijo XOR $p_i = a_1 \oplus \cdots \oplus a_i$. Un subarreglo $(L,R)$ vale $p_R \oplus p_{L-1}$.
Mapa de frecuencias de prefijos. $O(n)$.

## Entrada

$n$ $X$ ($1 \le n \le 2 \cdot 10^5$, $0 \le X < 2^{30}$).

$n$ enteros $a_i$ ($0 \le a_i < 2^{30}$).

## Salida

Un entero (64 bits).
