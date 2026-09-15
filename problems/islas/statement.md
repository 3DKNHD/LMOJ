# Islas de puntos

Tienes una grilla $n \times m$ de `.` (tierra) y `#` (agua). Una **isla** es un grupo 4-conectado de `.` (arriba/abajo/izquierda/derecha, no diagonales). Cuenta las islas.

No uses DFS recursivo en $1000 \times 1000$: el stack se muere. BFS o DFS iterativo.

## Entrada

La primera línea contiene $n$ y $m$ ($1 \le n,m \le 1000$).

Siguen $n$ líneas de exactamente $m$ caracteres `.` o `#`.

## Salida

Un único entero: el número de islas.
