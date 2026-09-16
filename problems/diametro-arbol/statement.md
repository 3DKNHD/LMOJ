# Los dos pueblos más lejanos

El distrito es un **árbol**: $n$ pueblos y $n-1$ caminos de tierra que los unen, sin ciclos, y se puede ir de cualquiera a cualquiera. Cada camino cuenta como distancia $1$ (un tramo).

El intendente quiere saber cuán «estirado» está el distrito: la máxima distancia, en tramos, entre algún par de pueblos. Esa distancia se llama a veces el diámetro de la red.

Si $n = 1$, no hay a dónde ir: la respuesta es $0$.

## Entrada

La primera línea contiene $n$ ($1 \le n \le 2 \cdot 10^5$).

Siguen $n-1$ líneas con $u$ $v$ ($1 \le u,v \le n$).

## Salida

Un único entero: la máxima distancia en aristas entre dos nodos.
