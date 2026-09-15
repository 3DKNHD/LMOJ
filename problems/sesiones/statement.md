# Sesiones sin choque

Hay $n$ sesiones, cada una ocupa el intervalo cerrado $[L, R]$ de tiempo. Quieres elegir el **máximo** número de sesiones que no se pisen: dos sesiones se pisan si comparten al menos un instante.

Si una termina en $t$ y la otra empieza en $t$, **chocan**.

## Entrada

La primera línea contiene $n$ ($1 \le n \le 2 \cdot 10^5$).

Siguen $n$ líneas con $L$ $R$ ($1 \le L \le R \le 10^9$).

## Salida

Un único entero: el máximo de sesiones compatibles.
