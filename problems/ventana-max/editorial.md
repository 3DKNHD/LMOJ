# Editorial: Máximo en ventana

## Qué pide

Para cada $i=1,\dots,n-k+1$, el máximo de $a_i,\dots,a_{i+k-1}$. $n\le 2\cdot 10^5$: no puedes recomputar cada ventana en $O(k)$.

## Idea

Deque de **índices** con valores **estrictamente decrecientes** (el oficial usa $\le$ al sacar: iguales, gana el más a la derecha). El frente es siempre el máximo de la ventana actual.

Al entrar $i$:

1. Saca de **adelante** índices $\le i-k$ (ya salieron de la ventana).
2. Saca de **atrás** mientras $a[\mathrm{back}] \le a[i]$ (nunca van a ser máximos si $i$ está más a la derecha y es $\ge$).
3. Empuja $i$.
4. Si $i \ge k-1$, el máximo es $a[\mathrm{front}]$.

## Por qué $O(n)$

Cada índice entra y sale de la deque **a lo sumo una vez**. Amortizado $O(1)$ por posición.

## Por qué no `multiset`

`multiset` de $k$ elementos: $O(n\log k)$, también entra. La deque es la solución clásica y más rápida.

Un sparse table de máximos da cada ventana en $O(1)$ tras $O(n\log n)$: más memoria, válido.

## Empates

Si hay dos máximos iguales, da igual cuál reportas: pides el **valor**. Sacar con $\le$ deja el índice más reciente; con `<` dejarías el más viejo. Ambos correctos.

## Trampas

- Deque de valores, no de índices: no sabes cuándo expiró.
- Ventanas 1-based vs 0-based: hay $n-k+1$ respuestas.
- $k=n$: una sola ventana, el máximo global.

## Código de referencia (C++)

```cpp
deque<int> dq;
for (int i = 0; i < n; ++i) {
    while (!dq.empty() && dq.front() <= i - k) dq.pop_front();
    while (!dq.empty() && a[dq.back()] <= a[i]) dq.pop_back();
    dq.push_back(i);
    if (i >= k - 1) out.push_back(a[dq.front()]);
}
```
