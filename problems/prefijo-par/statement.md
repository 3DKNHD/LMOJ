# La balanza

En el laboratorio hay una balanza digital un poco caprichosa: no muestra el peso, solo si el acumulado hasta ahora es **par** o **impar**.

Colocan $n$ pesas, una por una, en el orden $a_1, a_2, \dots, a_n$. Después de colocar la $i$-ésima, el peso sobre el plato es $a_1 + \cdots + a_i$. Las pesas pueden marcar negativo: son contrapesos.

A la ayudante le interesa cuántas veces, a lo largo de ese proceso, la balanza quedó en par. El prefijo de longitud $1$ también cuenta, si $a_1$ es par.

## Entrada

La primera línea contiene un entero $n$ ($1 \le n \le 2 \cdot 10^5$).

La segunda línea contiene $n$ enteros $a_i$ ($-10^9 \le a_i \le 10^9$).

## Salida

Un único entero: cuántos prefijos tienen suma par.
