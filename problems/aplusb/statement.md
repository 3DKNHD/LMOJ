# Las dos facturas

El kiosco de la esquina anota cada venta en **dos** talonarios distintos. En uno va lo que el cliente pagó en el momento; en el otro, un ajuste (positivo si quedó debiendo algo de otra vez, negativo si había una nota de crédito). Al cierre, para cada venta, el dueño quiere un solo número: cuánto dinero **movió en total**, es decir la suma de las dos cantidades.

Hoy hubo $T$ ventas. La $i$-ésima quedó registrada con los enteros $A$ y $B$. Los importes no son juguete: pueden ser muy grandes o muy negativos, y hay muchas ventas, así que el programa tiene que aguantar el volumen del día.

Tu tarea es, para cada venta, imprimir $A+B$ en su propia línea.

## Entrada

La primera línea contiene un entero $T$ ($1 \le T \le 10^5$).

Siguen $T$ líneas, cada una con dos enteros $A$ y $B$ ($-10^{18} \le A,B \le 10^{18}$).

## Salida

$T$ líneas. La $i$-ésima contiene el resultado de esa venta.
