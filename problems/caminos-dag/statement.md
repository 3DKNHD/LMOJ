# Senderos hacia el auditorio

El campus tiene $n$ puntos (el $1$ es la entrada, el $n$ es el auditorio) y $m$ senderos **de un solo sentido**: un arco $u \rightarrow v$ se recorre solo de $u$ a $v$. El mapa está pensado para no dar vueltas: no hay ciclos. Desde un punto puedes tener varias salidas, o ninguna.

Un **camino** es una secuencia de senderos que empieza en $1$ y termina en $n$. Dos caminos son distintos si no usan exactamente la misma secuencia de puntos. El camino que consiste en quedarse en $1$ cuando $n = 1$ cuenta como uno.

¿Cuántos caminos hay? Como pueden ser muchos, imprime el número módulo $10^9+7$. Si no se puede llegar, la respuesta es $0$.

## Entrada

La primera línea contiene $n$ y $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$).

Siguen $m$ líneas con $u$ $v$ (arco $u \rightarrow v$, $1 \le u,v \le n$).

## Salida

Un único entero: la cantidad de caminos módulo $10^9+7$.
