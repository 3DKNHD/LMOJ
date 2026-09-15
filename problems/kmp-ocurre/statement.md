# Ocurrencias del patrón

Cuenta cuántas veces aparece $P$ en $T$, **contando overlaps** (`aaa` con `aa` vale 2).

KMP. $|T|+|P| \le 10^6$. Si $P$ es vacío no ocurre (aquí $|P|\ge 1$).

## Entrada

Primera línea: $P$ (solo letras minúsculas, $1 \le |P| \le 10^6$).

Segunda línea: $T$ (minúsculas, $1 \le |T| \le 10^6$).

## Salida

Un entero.
