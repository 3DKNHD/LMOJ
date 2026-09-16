# Editorial: El estribillo

## Qué hay que hacer

Cuántas veces aparece $P$ dentro de $T$, **contando superposiciones**. $aa$ en `aaa` vale $2$.

## KMP, paso a paso

Junta las dos cadenas en una sola: $s = P + \# + T$. El carácter `#` no aparece en $P$ ni en $T$, así que no mezcla las dos partes.

Para cada posición $i$ calcula $\pi[i]$: el largo del **borde** más largo de $s[0..i]$. Un borde es un trozo que es a la vez prefijo y sufijo, y más corto que toda la cadena.

Cada vez que $\pi[i]$ llega a $|P|$, acabas de leer una copia completa de $P$ dentro de $T$.

Para calcular $\pi$: $j$ es el borde de la posición anterior. Si el carácter actual no coincide, sustituye $j$ por $\pi[j-1]$ (prueba un borde más corto). Si coincide, aumenta $j$ en $1$. El total es proporcional a $|P|+|T|$.

## Si te da TLE / WA

`T.find` en un loop que avanza $1$ (lento o omites superposiciones). O no contar superposiciones.

## El código que pasa (C++)

Código completo en C++. Es el mismo que usa el juez. Puedes copiarlo.

```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string p, t;
    cin >> p >> t;
    string s = p + "#" + t;
    int m = (int)p.size();
    vector<int> pi(s.size());
    int ans = 0;
    for (int i = 1; i < (int)s.size(); ++i) {
        int j = pi[i - 1];
        while (j && s[i] != s[j]) j = pi[j - 1];
        if (s[i] == s[j]) ++j;
        pi[i] = j;
        if (j == m) ++ans;
    }
    cout << ans << "\n";
    return 0;
}
```
