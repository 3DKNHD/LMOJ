# Editorial: La vitrina

## Qué hay que hacer

Una ventana de ancho $k$ se desliza sobre el arreglo. En cada lugar quieres el **máximo** de los $k$ números que se ven.

Si por cada posición recorres los $k$, es $n\cdot k$. Con ambos $2\cdot 10^5$, no entra.

## La idea: una cola de dos extremos (deque) que guarda índices

La cola guarda posiciones de candidatos al máximo, **de mayor a menor** el valor.

Cuando llega el índice $i$:

1. Quita de **adelante** a los que ya se salieron de la ventana (`índice <= i-k`).
2. Quita de **atrás** a los que son $\le a[i]$: nunca van a ser máximo mientras $i$ esté. $i$ es más nuevo y más grande (o igual).
3. Metes $i$ atrás.
4. Si ya completaste $k$ elementos ($i >= k-1$), el máximo de la ventana es `a[el de adelante]`.

## Ejemplo

$a=[1,3,2,5]$, $k=3$

- $i=0$: cola $[0]$
- $i=1$: $3>1$, saco $0$, cola $[1]$
- $i=2$: $2<3$, cola $[1,2]$. Ventana $0..2$, máximo $a[1]=3$
- $i=3$: se sale $0$ (ya no estaba). $5$ echa a todos. Cola $[3]$. Máximo $5$

Salida: $3\ 5$.

## Si te da TLE

Máximo recorriendo todo en cada ventana.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,k; cin>>n>>k;
    vector<ll> a(n);
    for (int i=0;i<n;++i) cin>>a[i];
    deque<int> dq;
    vector<ll> out;
    for (int i=0;i<n;++i) {
        while (!dq.empty() && dq.front()<=i-k) dq.pop_front();
        while (!dq.empty() && a[dq.back()]<=a[i]) dq.pop_back();
        dq.push_back(i);
        if (i>=k-1) out.push_back(a[dq.front()]);
    }
    for (int i=0;i<(int)out.size();++i) {
        if (i) cout<<" ";
        cout<<out[i];
    }
    cout<<"\n";
    return 0;
}
```
