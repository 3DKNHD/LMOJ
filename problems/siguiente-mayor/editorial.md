# Editorial: Siguiente mayor

## Qué pide

Para cada $i$, el **valor** $a_j$ del mínimo $j>i$ con $a_j > a_i$ (estrictamente). Si no hay, $-1$. No pides el índice.

## Idea

Stack monótono **de índices**, de derecha a izquierda. El stack guarda candidatos en valores **estrictamente crecientes** hacia el tope (el oficial saca mientras $a[\mathrm{top}] \le a[i]$).

Al estar en $i$:

1. Tira del tope todo lo $\le a[i]$: nunca serán el siguiente mayor de $i$ (son $\le$) ni de nadie a la izquierda de $i$ respecto a un candidato peor.
2. Si el stack no está vacío, el tope es el primer mayor a la derecha.
3. Empuja $i$.

Cada índice entra/sale una vez: $O(n)$.

## Por qué de derecha a izquierda

Cuando procesas $i$, el stack ya contiene solo posiciones $>i$, en el orden en que pueden ser “próximo mayor”.

De izquierda a derecha también se puede (stack de no resueltos); es el dual. El oficial va hacia atrás y guarda **valores** en `ans[i]`.

## Estrictamente mayor

`<=` al popear: iguales no sirven. Si el enunciado pidiera $\ge$, cambiarías a `<`.

## Complejidad

$O(n)$ tiempo y memoria.

## Otras soluciones

Sparse table / segment tree de “primer índice con valor $> a_i$ a la derecha”: más pesado. $O(n^2)$: TLE.

## Trampas

- Imprimir el **índice** en vez del valor.
- Usar $\ge$ y aceptar iguales.
- Olvidar $-1$ cuando el stack queda vacío (el máximo global a la derecha no tiene next).

## Código de referencia (C++)

```cpp
vector<int> st;
for (int i = n - 1; i >= 0; --i) {
    while (!st.empty() && a[st.back()] <= a[i]) st.pop_back();
    if (!st.empty()) ans[i] = a[st.back()];
    st.push_back(i);
}
```
