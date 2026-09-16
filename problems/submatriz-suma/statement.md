# La cosecha del plano

El predio de la feria es una grilla de $n$ filas por $m$ columnas. En cada celda $(i, j)$ hay un entero $a_{ij}$: ganancia de ese puesto, o pérdida si es negativo.

El organizador hace $q$ preguntas. Cada una elige un rectángulo alineado con la grilla, de la fila $r_1$ a la $r_2$ y de la columna $c_1$ a la $c_2$ (todo inclusivo, filas y columnas numeradas desde $1$). Quiere la **suma** de todas las celdas de ese rectángulo.

Los puestos no cambian entre preguntas. Una respuesta puede no caber en 32 bits.

## Entrada

La primera línea contiene $n$, $m$ y $q$ ($1 \le n,m \le 1000$, $1 \le q \le 10^5$).

Siguen $n$ líneas con $m$ enteros ($-10^9 \le a_{ij} \le 10^9$).

Siguen $q$ líneas con $r_1$ $c_1$ $r_2$ $c_2$ ($1 \le r_1 \le r_2 \le n$, $1 \le c_1 \le c_2 \le m$).

## Salida

$q$ líneas, cada una con la suma del rectángulo pedido.
