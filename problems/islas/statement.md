# Tierra y mar

Tienes un mapa rectangular de $n$ filas por $m$ columnas. Cada celda es `.` (tierra) o `#` (agua).

Una **isla** es un conjunto maximal de celdas de tierra donde puedes ir de cualquiera a cualquiera pisando solo tierra y moviéndote en cruz: arriba, abajo, izquierda, derecha. **Las diagonales no cuentan**: dos tierras que se tocan solo por una esquina son islas distintas. El agua no se camina.

El mapa puede ser grande y tener muchas islas, o ser todo mar (entonces la respuesta es $0$). Cuenta las islas.

## Entrada

La primera línea contiene $n$ y $m$ ($1 \le n,m \le 1000$).

Siguen $n$ líneas de exactamente $m$ caracteres `.` o `#`.

## Salida

Un único entero: el número de islas.
