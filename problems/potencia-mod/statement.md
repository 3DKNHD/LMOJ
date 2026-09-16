# El sello

En la imprenta de la facultad cada certificado lleva un sello circular con exactamente $10^9+7$ marcas, numeradas $0, 1, \dots, 10^9+6$. El operario no lo gira “a ojo”: elige dos enteros $a$ y $b$ y aplica la regla del gremio.

El sello empieza en la marca $1$. Después, $b$ veces seguidas, avanza **$a$ marcas** desde donde quedó. Si se pasa de $10^9+6$, da la vuelta y sigue contando. El número que queda impreso es, en matemáticas, $a^b$ módulo $10^9+7$.

Hay una excepción en el reglamento y nadie la discute: cuando $a = 0$ y $b = 0$, el certificado se considera sellado con $1$. El resto de los ceros se comporta como uno espera: si $a = 0$ y $b > 0$, la marca final es $0$.

Hoy hay $T$ certificados en la cola, cada uno con su par $a, b$. Ambos pueden ser enormes. Para cada certificado, imprime la marca que debe quedar.

## Entrada

La primera línea contiene $T$ ($1 \le T \le 10^5$).

Siguen $T$ líneas con $a$ $b$ ($0 \le a,b \le 10^{18}$).

## Salida

$T$ líneas, cada una con un entero entre $0$ y $10^9+6$.
