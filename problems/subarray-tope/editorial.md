# Editorial: Subarreglo con tope

## Qué pide

Máxima longitud de un subarreglo contiguo con suma $\le S$. $a_i \ge 0$. Si ningún elemento cabe, $0$.

## Idea

Two pointers. $a_i \ge 0$ $\Rightarrow$ la suma de $[L,R]$ **crece** al mover $R$ y **decrece** al mover $L$. Puedes mantener el menor $L$ tal que `sum(L..R) \le S` (o vacío).

```text
L = 0, sum = 0, ans = 0
para R = 0..n-1:
    sum += a[R]
    mientras L≤R y sum > S:
        sum -= a[L]; L++
    ans = max(ans, R-L+1)
```

Si un solo $a[R] > S$, el `while` avanza $L$ hasta $R+1$ y la longitud queda $0$ para esa ventana; `ans` no crece. Correcto.

## Por qué $O(n)$

$L$ y $R$ solo avanzan. Cada extremo se mueve $\le n$ veces.

## Por qué no binaria sobre la longitud

También entra: para longitud fija chequeas con prefijos si existe un rango de esa long $\le S$, más binaria. $O(n\log n)$. Two pointers es lineal y usa que los $a_i$ son $\ge 0$.

Si hubiera **negativos**, la monotonicidad se rompe: hay que otras técnicas (p.ej. prefijos + set).

## 64 bits

$S\le 10^{18}$, suma de ventana hasta $n\cdot 10^9$. `long long` en `sum` y `S`.

## Trampas

- `ans = max(ans, R-L+1)` **antes** de encoger: cuentas ventanas $>S$.
- Negativos imaginarios.
- `int` en `sum`.

## Código de referencia (C++)

```cpp
int ans = 0, L = 0;
long long sum = 0;
for (int R = 0; R < n; ++R) {
    sum += a[R];
    while (L <= R && sum > S) { sum -= a[L]; ++L; }
    ans = max(ans, R - L + 1);
}
```
