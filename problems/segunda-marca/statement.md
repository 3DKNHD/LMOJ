# La plata

En el torneo de salto en largo cada atleta puede tener varios intentos. Lo que queda en la planilla es la lista de $n$ marcas (enteros; un intento nulo o con viento en contra puede ser negativo).

La **oro** es la mejor marca **distinta** que apareció. La **plata** es la segunda mejor distinta: repetir el oro no da medalla de plata. Si todos los intentos midieron exactamente lo mismo, el jurado no entrega plata e imprime $-1$.

Por ejemplo, con las marcas $5,1,5,3,3,4$ los valores distintos de mayor a menor son $5,4,3,1$. Oro $5$, plata $4$.

Dada la lista, imprime la plata (o $-1$).

## Entrada

La primera línea contiene un entero $n$ ($1 \le n \le 2 \cdot 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

## Salida

Un único entero: la segunda mayor entre las marcas distintas, o $-1$ si no existe.
