# Reparto exacto

Después de la olimpiada quedó una bolsa con $n$ caramelos idénticos. Quieren guardarlos en cajitas **todas con la misma cantidad**, usando todos los caramelos, y sin dejar cajitas vacías.

Elegir un tamaño de cajita $d$ que divida a $n$ da un reparto distinto: habrá $n/d$ cajitas de $d$ caramelos. Siempre existen al menos dos maneras cuando $n > 1$: una sola cajita con $n$, o $n$ cajitas con $1$. Si $n = 1$, solo cabe una cajita con un caramelo.

El comité no hace una bolsa, hace $T$. Para cada $n$, ¿de cuántas maneras se puede hacer el reparto?

## Entrada

La primera línea contiene $T$ ($1 \le T \le 10^5$).

Siguen $T$ líneas con $n$ ($1 \le n \le 10^6$).

## Salida

$T$ líneas, cada una con la cantidad de divisores positivos de ese $n$.
