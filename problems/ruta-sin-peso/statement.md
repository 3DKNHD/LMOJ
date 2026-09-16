# Hasta la sala $n$

El edificio de la olimpiada es un grafo: $n$ salas y $m$ pasillos. Cada pasillo une dos salas y se recorre en los dos sentidos. Recorrer un pasillo cuesta **un paso**, todos iguales: no hay distancias en metros, solo «cuántos pasillos». Puede haber bucles y pasillos repetidos; no te acortan el camino de forma mágica.

Empiezas en la sala $1$ (el hall) y quieres la sala $n$ (el auditorio). La respuesta es el mínimo número de pasillos de algún recorrido. Si $n = 1$, ya estás: $0$. Si no existe camino, imprime $-1$.

## Entrada

La primera línea contiene $n$ y $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

Siguen $m$ líneas con $u$ $v$ ($1 \le u,v \le n$).

## Salida

Un único entero: la distancia en pasillos, o $-1$.
