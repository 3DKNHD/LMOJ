# Consultas de suma

Tienes un arreglo estático $a_1,\dots,a_n$ y $q$ consultas. Cada consulta pide la suma $a_L + \cdots + a_R$.

$O(nq)$ no entra.

## Entrada

La primera línea contiene $n$ y $q$ ($1 \le n,q \le 2 \cdot 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

Siguen $q$ líneas con $L$ $R$ ($1 \le L \le R \le n$).

## Salida

$q$ líneas, cada una con la suma del rango (cabe en 64 bits).
