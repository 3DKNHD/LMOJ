# El más barato

En la góndola hay $n$ productos alineados de izquierda a derecha. El de más a la izquierda es la posición $1$, el siguiente la $2$, y así hasta $n$. Cada uno tiene un precio $a_i$ (el encargado a veces pone ofertas raras, incluso negativas).

Te llevas **el más barato**. Si hay varios con el mismo precio mínimo, eliges el que está más a la izquierda: menos camino con el changuito.

Imprime esa posición (un índice entre $1$ y $n$).

## Entrada

La primera línea contiene un entero $n$ ($1 \le n \le 2 \cdot 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

## Salida

Un único entero: el menor índice $i$ tal que $a_i$ es el mínimo del arreglo.
