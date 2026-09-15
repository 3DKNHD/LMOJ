# Editorial: Subarreglos XOR

## Qué pide

Cuántos $L\le R$ cumplen $a_L \oplus \cdots \oplus a_R = X$. $n\le 2\cdot 10^5$.

## Idea

Prefijo XOR: $p_0=0$, $p_i = a_1 \oplus \cdots \oplus a_i$. Entonces

$$
a_L \oplus \cdots \oplus a_R = p_R \oplus p_{L-1}
$$

porque $x\oplus x=0$. Quieres $p_R \oplus p_{L-1} = X$, o sea $p_{L-1} = p_R \oplus X$.

Recorres $R=1..n$. Antes de insertar $p_R$, sumas cuántos prefijos anteriores valen $p_R \oplus X$. Luego incrementas la frecuencia de $p_R$.

`f[0]=1` cuenta el prefijo vacío: subarreglos que empiezan en $1$.

## Por qué $O(n)$

Un hashmap. El oficial usa `unordered_map` con `reserve`. `map` sería $O(n\log n)$ y también entra.

## 64 bits

Peor caso: todo $0$, $X=0$: $\binom{n+1}{2}$ subarreglos. `long long`.

## Otras soluciones

Trie de bits de prefijos: overkill con $X$ dado (un mapa basta). $O(n^2)$: TLE.

## Trampas

- Olvidar `f[0]=1`.
- Insertar $p$ **antes** de consultar: cuentas el subarreglo vacío si $X=0$ de más, o duplicas.
- `int` en el contador.

## Código de referencia (C++)

```cpp
unordered_map<int, int> f;
f[0] = 1;
int p = 0;
long long ans = 0;
for (...) {
    p ^= a;
    ans += f[p ^ X];
    f[p]++;
}
```
