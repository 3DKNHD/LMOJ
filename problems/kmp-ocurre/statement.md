# El estribillo

El coro ensaya un estribillo $P$ y un canto largo $T$, ambos escritos solo con letras minúsculas. Quieren saber **cuántas veces** aparece el estribillo dentro del canto.

Las apariciones pueden **solaparse**. Por ejemplo, si el estribillo es `aa` y el canto es `aaa`, cuenta $2$ veces: posiciones $1$–$2$ y $2$–$3$. El estribillo nunca es vacío.

Imprime esa cantidad.

## Entrada

La primera línea contiene $P$ ($1 \le |P| \le 10^6$, solo `a`–`z`).

La segunda línea contiene $T$ ($1 \le |T| \le 10^6$, solo `a`–`z`).

## Salida

Un único entero: cuántas veces $P$ aparece en $T$, contando solapes.
