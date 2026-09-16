# El jurado

Hay que armar el jurado de la olimpiada: de $n$ profesores disponibles se eligen $k$. Dos jurados son distintos si no tienen exactamente las mismas personas. El reglamento no distingue el orden dentro del jurado.

La cantidad de jurados posibles es el coeficiente binomial $C(n, k)$. Como el número puede ser astronómico, el comité pide esa cantidad **módulo** $10^9+7$.

Convenciones que ya están escritas en el reglamento: si piden más jurados que profesores ($k > n$), la respuesta es $0$. Elegir a nadie de un conjunto vacío cuenta: $C(0, 0) = 1$. Aquí siempre $k \ge 0$.

Hay $T$ sedes, cada una con su par $n, k$.

## Entrada

La primera línea contiene $T$ ($1 \le T \le 10^5$).

Siguen $T$ líneas con $n$ $k$ ($0 \le n,k \le 10^6$).

## Salida

$T$ líneas, cada una con $C(n, k) \bmod (10^9+7)$.
