# Editorial: Dos fichas

## Qué hay que hacer

Tienes $n$ fichas (pueden repetirse). Quieres cuántas **parejas de personas distintas** suman exactamente $X$. Persona $i$ con persona $j$, $i<j$.

Si hay tres $5$ y $X=10$, las parejas $5+5$ son $\binom{3}{2}=3$, no $1$.

Un doble `for` ($i$ contra todos los $j$) es $n^2$. Con $n=2\cdot 10^5$ eso es $40$ mil millones de operaciones. No entra. No alcanza el tiempo.

## La idea

Cuenta cuántas veces aparece cada valor (un `map`).

Para cada valor $v$ que aparece $c$ veces, el compañero que necesita es $need = X-v$.

- Si $need = v$: estás armando parejas **dentro** del mismo número. Fórmula: $c\cdot(c-1)/2$. (Elegir $2$ de $c$.)
- Si $need > v$: busca cuántos $need$ hay, digamos $d$, y sumá $c\cdot d$. El $>$ evita contar dos veces el mismo par $(v, need)$ y $(need, v)$.
- Si $need < v$: no hagas nada, ya lo viste cuando procesaste el más pequeño.

## Ejemplo

Lista $1,5,5,3$, $X=6$.

- Un $1$ y… necesita $5$. Hay dos $5$ → $2$ parejas.
- Dos $5$: $5+5=10\neq 6$, no suman entre ellos.
- $3$ necesita $3$: hay uno solo → $0$ parejas de $3+3$.

Total $2$. Las parejas son (el $1$ con cada $5$).

## 64 bits

$c$ puede ser $2\cdot 10^5$. $c\cdot(c-1)/2$ no entra en `int`. `long long`.

## Si te da TLE / WA

- $O(n^2)$.
- Contar $(v,need)$ y $(need,v)$.
- Tratar repetidos como si fueran uno solo.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

long long contar_pares(const vector<long long>& a, long long objetivo) {
    map<long long, long long> freq;
    for (long long x : a) {
        freq[x]++;
    }

    long long respuesta = 0;
    for (auto [valor, veces] : freq) {
        long long falta = objetivo - valor;
        if (falta < valor) {
            continue;
        }
        if (falta == valor) {
            respuesta += veces * (veces - 1) / 2;
            continue;
        }
        auto it = freq.find(falta);
        if (it != freq.end()) {
            respuesta += veces * it->second;
        }
    }
    return respuesta;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long objetivo;
    cin >> n >> objetivo;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    cout << contar_pares(a, objetivo) << "\n";
    return 0;
}
```
