# La vitrina

En la librería pusieron una vitrina que solo muestra $k$ lomos seguidos del estante. El estante es una fila de $n$ libros, cada uno con un «peso visual» $a_i$ (un entero; los lomos oscuros pesan más a la vista).

El encargado desliza la vitrina de izquierda a derecha: primero cubre las posiciones $1..k$, después $2..k+1$, y así hasta $n-k+1$. En cada colocación quiere saber cuál es el lomo **más llamativo** de esa ventana, es decir el máximo de esos $k$ valores.

Imprime esos máximos, en el orden en que recorre el estante, en una sola línea.

## Entrada

La primera línea contiene $n$ y $k$ ($1 \le k \le n \le 2 \cdot 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

## Salida

Una línea con $n-k+1$ enteros separados por espacios.
