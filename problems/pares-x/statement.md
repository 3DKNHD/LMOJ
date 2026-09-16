# Dos fichas

En el taller de programación cada estudiante recibe una ficha con un entero escrito. El mismo número puede repetirse: dos personas distintas pueden tener la misma ficha, y los valores pueden ser negativos.

Para el ejercicio de la semana hay que armar **equipos de exactamente dos** estudiantes. Un equipo es válido si la suma de sus dos fichas es exactamente $X$, el objetivo que la profesora dejó en el pizarrón. Cada pareja se identifica por las **dos personas**, no por los números: si Ana y Bruno tienen $3$ y $5$, y Carla también tiene $3$, entonces $(Ana, Bruno)$ y $(Carla, Bruno)$ son dos equipos distintos. Nadie se empareja consigo mismo.

No hace falta listar los equipos. La profesora solo quiere saber **cuántos** hay. El total puede no caber en 32 bits.

## Entrada

La primera línea contiene $n$ y $X$ ($1 \le n \le 2 \cdot 10^5$, $-2 \cdot 10^9 \le X \le 2 \cdot 10^9$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

## Salida

Un único entero: la cantidad de pares de índices $i < j$ con $a_i + a_j = X$.
