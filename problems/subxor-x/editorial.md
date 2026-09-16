# Editorial: El código X

## Qué hay que hacer

XOR compara cada bit: si los dos bits son distintos, el resultado es $1$; si son iguales, $0$.
Dos reglas útiles: $x \oplus x = 0$ y $x \oplus 0 = x$.
También: si $p \oplus y = X$, entonces $y = p \oplus X$.

Hay que contar cuántos trozos **contiguos** del arreglo tienen XOR igual a $X$.

## Prefijo XOR

Define $p_0 = 0$ y $p_i = a_1 \oplus a_2 \oplus \cdots \oplus a_i$.

El XOR del intervalo $L..R$ es $p_R \oplus p_{L-1}$, porque los elementos anteriores a $L$ se cancelan ($x \oplus x = 0$).

Se busca $p_R \oplus p_{L-1} = X$, que es lo mismo que $p_{L-1} = p_R \oplus X$.

Recorre el arreglo de izquierda a derecha y mantén el prefijo actual $p$. Un mapa guarda cuántas veces apareció cada prefijo. Antes de anotar el $p$ actual, pregunta al mapa cuántas veces ya viste el valor $p \oplus X$. Cada una corresponde a un $L$ válido que termina en esta posición. Después suma $1$ a la cuenta de $p$.

Empieza el mapa con `{0: 1}`: el prefijo vacío, para intervalos que empiezan en $1$.

## Si te da TLE

$O(n^2)$ calculando XOR de cada par $L,R$.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; int X; cin>>n>>X;
    unordered_map<int,int> f;
    f.reserve(n*2);
    f[0]=1;
    int p=0; ll ans=0;
    for (int i=0;i<n;++i) {
        int a; cin>>a;
        p ^= a;
        auto it=f.find(p^X);
        if (it!=f.end()) ans += it->second;
        f[p]++;
    }
    cout << ans << "\n";
    return 0;
}
```
