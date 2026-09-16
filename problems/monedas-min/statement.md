# El vuelto

En el kiosco hay $n$ tipos de moneda. Del tipo $i$ hay **cantidad ilimitada**, y cada una vale $c_i$. Quieres formar **exactamente** $S$ (ni un peso más). Cada moneda cuenta: quieres usar el **mínimo** número de monedas posible.

Si con esos valores no se puede armar $S$, imprime $-1$. Puedes repetir el mismo tipo las veces que haga falta.

## Entrada

La primera línea contiene $n$ y $S$ ($1 \le n \le 100$, $1 \le S \le 10^5$).

La segunda línea contiene $n$ enteros $c_i$ ($1 \le c_i \le 10^5$).

## Salida

Un único entero: el mínimo número de monedas, o $-1$.
