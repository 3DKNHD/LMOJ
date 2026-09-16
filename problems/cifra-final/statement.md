# El candado

El laboratorio cerró el depósito con un candado de **un solo dígito**. El código del día es un entero $n$ (puede ser enorme, y a veces el encargado lo anota con signo de menos). El candado no entiende signos: abre con la **última cifra decimal** del valor absoluto. Así, $17$ abre con $7$ y $-17$ también abre con $7$. El $0$ abre con $0$.

Hoy hay $T$ códigos en la lista. Para cada uno, imprime el dígito que abre el candado.

## Entrada

La primera línea contiene un entero $T$ ($1 \le T \le 10^5$).

Siguen $T$ líneas con un entero $n$ ($-10^{18} \le n \le 10^{18}$).

## Salida

$T$ líneas, cada una con un dígito $0$–$9$.
