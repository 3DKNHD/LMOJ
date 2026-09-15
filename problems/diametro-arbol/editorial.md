# Editorial: Diámetro del árbol

## Qué pide

Máxima distancia (aristas) entre dos nodos de un **árbol**. $n\le 2\cdot 10^5$.

## Idea

Dos BFS:

1. Desde un nodo cualquiera (p.ej. $1$), halla el más lejano $u$.
2. Desde $u$, halla el más lejano $v$. `dist(u,v)` es el diámetro.

Por qué funciona en árboles: $u$ es un extremo de algún diámetro. (Si el diámetro fuera $a$–$b$ y $u$ no estuviera en él, el camino de $1$ a $u$ contradice maximalidad; prueba estándar por casos.)

En grafos con ciclos **no** vale.

## $n=1$

Diámetro $0$. BFS desde $1$: farthest es $1$, dist $0$.

## Complejidad

$O(n)$. Dos recorridos.

## Otras soluciones

DP en raíces: `altura` y `mejor combinación de dos hijos`. $O(n)$, más código. Tree-DP útil si hay pesos.

## Trampas

- Un solo BFS desde $1$ (el más lejano desde $1$ no es el diámetro si $1$ está “en medio”).
- Grafo no árbol (el input es árbol: $n-1$ aristas).
- DFS recursivo: $n=2\cdot 10^5$ cadena $\Rightarrow$ stack overflow. BFS.

## Código de referencia (C++)

```cpp
int u = farthest(1).first;
cout << farthest(u).second << "\n";
```
