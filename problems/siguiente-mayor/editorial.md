# Editorial: El próximo récord

## Qué hay que hacer

Para cada posición, el primer número **a la derecha** que sea **estrictamente más grande**. Si no hay, `-1`. Quieres el **valor**, no el índice.

## Recorre de derecha a izquierda con una pila de índices

La pila tiene candidatos, con valores **crecientes** hacia arriba (el tope es el más cercano a la derecha que todavía sirve).

En $i$, de derecha a izquierda:

1. Mientras el tope sea $\le a[i]$, sacalo: no es estrictamente mayor.
2. Si la pila no está vacía, `ans[i] = a[tope]`.
3. Mete $i$ en la pila.

¿Por qué funciona? Todo lo que sacaste era $\le a[i]$, así que para la izquierda de $i$, $i$ es un candidato mejor (más cerca y más grande o igual).

## Ejemplo

$2, 1, 3$

- $i=2$ ($3$): pila vacía → $-1$, pila $[2]$
- $i=1$ ($1$): tope $3>1$ → ans $3$, pila $[2,1]$
- $i=0$ ($2$): saco $1$ ($1\le 2$), tope $3>2$ → ans $3$

Salida: $3\ 3\ -1$.

## Si te da WA

Pusiste $\ge$ y no encuentras nada estrictamente mayor. O imprimiste índices.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin>>n;
    vector<ll> a(n);
    for (int i=0;i<n;++i) cin>>a[i];
    vector<int> ans(n, -1);
    vector<int> st;
    for (int i=n-1;i>=0;--i) {
        while (!st.empty() && a[st.back()]<=a[i]) st.pop_back();
        if (!st.empty()) ans[i]=a[st.back()];
        st.push_back(i);
    }
    for (int i=0;i<n;++i) {
        if (i) cout<<" ";
        cout<<ans[i];
    }
    cout<<"\n";
    return 0;
}
```
