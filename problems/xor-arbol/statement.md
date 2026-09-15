# XOR en el árbol

Tienes un árbol de $n$ nodos (1-indexados). El nodo $i$ tiene un valor $a_i$.
Te hacen $q$ preguntas: para cada par $(u, v)$ imprime el XOR de los valores en el **camino único** entre $u$ y $v$, **incluyendo** ambos extremos.

## Entrada

La primera línea contiene $n$ y $q$ ($1 \le n, q \le 2 \cdot 10^4$).

La segunda línea contiene $n$ enteros $a_i$ ($0 \le a_i < 2^{30}$).

Siguen $n-1$ líneas con aristas $u$ $v$.

Siguen $q$ líneas con consultas $u$ $v$.

## Salida

$q$ líneas, una por consulta.

El XOR de un camino de un solo nodo $u$ es $a_u$.
