# El tramo del viaje

Vas a hacer un viaje por una ruta de $n$ peajes seguidos. El peaje $i$ cobra $a_i$ (nunca negativo). Llevas un presupuesto $S$: la suma de los peajes que elijas, **en un tramo contiguo**, no puede pasarse de $S$.

Quieres el tramo **más largo** que aún puedas pagar. Si hasta un solo peaje ya supera $S$, no sales: la respuesta es $0$. Si varios tramos empardan en longitud, cualquiera sirve: solo importa esa longitud.

## Entrada

La primera línea contiene $n$ y $S$ ($1 \le n \le 2 \cdot 10^5$, $0 \le S \le 10^{18}$).

La segunda línea contiene $n$ enteros $a_i$ ($0 \le a_i \le 10^9$).

## Salida

Un único entero: la máxima longitud de un subarreglo contiguo con suma $\le S$, o $0$.
