# Editorial: Del S al E

## Qué pide

Grilla, 4-conectado, `#` muro. Distancia mínima en pasos de `S` a `E`, o $-1$. $n,m\le 1000$.

## Idea

BFS desde `S`. Primera vez que tocas `E` es el camino más corto en número de pasos (todas las aristas pesan $1$). `S` y `E` son celdas transitables.

`dist = -1` marca no visitado. Muros no se encolan.

## Por qué no DFS

DFS encuentra *un* camino, no el más corto. En una grilla puede dar un paseo enorme.

## Complejidad

$O(nm)$. Cada celda una vez.

## DFS recursivo

Aunque no sea óptimo, además revienta el stack en $10^6$ celdas. BFS con `queue`.

## Trampas

- Diagonales (8 vecinos).
- No poder pisar `E` (tratarlo como muro).
- `S==E`: distancia $0$ (el oficial pone `dist[S]=0`).

## Código de referencia (C++)

```cpp
dist[sr][sc] = 0;
q.push({sr, sc});
// vecinos 4, skip # y dist!=-1
cout << dist[er][ec] << "\n";  // -1 si no se alcanzó
```
