# Cuántos divisores

Para cada $n$, imprime cuántos divisores positivos tiene. $1$ tiene $1$ divisor. Un primo tiene $2$.

$T$ llega a $10^5$ y $n$ a $10^6$: criba (SPF) o contar divisores precalculado, no $\sqrt{n}$ por consulta.

## Entrada

La primera línea contiene $T$ ($1 \le T \le 10^5$).

Siguen $T$ líneas con $n$ ($1 \le n \le 10^6$).

## Salida

$T$ líneas con $d(n)$.
