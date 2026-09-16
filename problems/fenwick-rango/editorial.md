# Editorial: El libro que se corrige

## Qué hay que hacer

El arreglo **cambia**. Operación $1$: suma $x$ a la posición $i$ (no reemplaza el valor; le suma $x$). Operación $2$: imprime la suma de $a_L + \cdots + a_R$.

Si guardas sumas de prefijo y luego cambia una casilla, tendrías que recalcular todo lo que está a su derecha. Eso es demasiado lento.

## Fenwick (árbol binario indexado)

Usa un arreglo extra `t[1..n]`. Cada índice $i$ guarda la suma de un bloque que **termina** en $i`. El largo de ese bloque es $i\ \&\ -i$ (en bits: el $1$ más a la derecha de $i$). No hace falta entender esa fórmula para usar las dos funciones:

**Sumar $v$ en $i$:**

```
for (; i <= n; i += i & -i) t[i] += v;
```

**Suma $1..i$:**

```
for (; i > 0; i -= i & -i) r += t[i];
```

Suma $L..R$ = $pref(R) - pref(L-1)$.

Índices desde **$1$**. Si pones $0$, el $i += i & -i$ se queda en $0$ para siempre: loop infinito.

Al principio, por cada $a_i$ haces $add(i, a_i)$. Un update del enunciado es **sumar** $x$, no reemplazar.

Todo en `long long`.

## Si te da WA / TLE

Tratar tipo $1$ como “poner $a_i = x$”. Sumar $L..R$ uno por uno. `int`.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Fenwick {
    int n; vector<ll> t;
    Fenwick(int n): n(n), t(n+1,0) {}
    void add(int i, ll v) { for (; i<=n; i+=i&-i) t[i]+=v; }
    ll pref(int i) { ll r=0; for (; i>0; i-=i&-i) r+=t[i]; return r; }
    ll range(int l, int r) { return pref(r)-pref(l-1); }
};
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,q; cin>>n>>q;
    Fenwick fw(n);
    for (int i=1;i<=n;++i) { ll x; cin>>x; fw.add(i,x); }
    while (q--) {
        int tp; cin>>tp;
        if (tp==1) { int i; ll x; cin>>i>>x; fw.add(i,x); }
        else { int l,r; cin>>l>>r; cout<<fw.range(l,r)<<"\n"; }
    }
    return 0;
}
```
