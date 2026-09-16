# Del patio al aula

El campus es una grilla de $n$ filas por $m$ columnas. Cada celda es `.` (pasillo), `#` (pared), `S` (el patio, tu inicio) o `E` (el aula a la que tienes que llegar). Hay **exactamente un** `S` y **exactamente un** `E`.

En un paso te mueves a una celda vecina en cruz: arriba, abajo, izquierda o derecha. No puedes entrar a una pared ni salirte del mapa. Las diagonales no valen.

¿Cuál es el mínimo número de pasos para ir de `S` a `E`? Si el aula es inalcanzable, imprime $-1$. Si `S` y `E` están en la misma celda no ocurre: son dos celdas distintas.

## Entrada

La primera línea contiene $n$ y $m$ ($1 \le n,m \le 1000$).

Siguen $n$ líneas de exactamente $m$ caracteres. Exactamente un `S` y un `E`; el resto son `.` o `#`.

## Salida

Un único entero: la distancia en pasos, o $-1$.
