# Editorial: La medida común

## Qué hay que hacer

El arreglo no cambia. Hay muchas preguntas. Cada una pide el gcd del intervalo $L..R$: el entero más grande que divide a todos esos números.

Recorrer $L..R$ en cada pregunta es demasiado lento. Se usa una **tabla dispersa** (sparse table).

## Cómo se arma

`st[k][i]` es el gcd de $2^k$ números seguidos que empiezan en $i$.

Un bloque de largo $2^k$ son dos bloques de largo $2^{k-1}$ pegados. Así se llena la tabla en $O(n\log n)$.

## Cómo se responde una pregunta

Sea $len = R-L+1$. Elige $k$ tal que $2^k$ es la mayor potencia de $2$ que no supera $len$.

Cubre $[L,R]$ con **dos** bloques de largo $2^k$: uno que empieza en $L$ y otro que termina en $R$. Pueden superponerse. Eso no importa: el gcd de dos trozos que se superponen sigue siendo el gcd de toda la unión.

En GCC, $k$ se puede sacar con `__builtin_clz(len)`.

Cada pregunta queda en tiempo constante.

## Si te da TLE

gcd recorriendo el rango cada vez.

## El código que pasa (C++)

Analízalo y entiéndelo. No lo copies y pegues.

```cpp
#include <bits/stdc++.h>
using namespace std;

struct TablaGcd {
    vector<vector<int>> st;
    int logn;

    TablaGcd(const vector<int>& a) {
        int n = (int)a.size() - 1;
        logn = 1;
        while ((1 << logn) <= n) {
            ++logn;
        }
        st.assign(logn, vector<int>(n + 1));
        for (int i = 1; i <= n; ++i) {
            st[0][i] = a[i];
        }
        for (int k = 1; k < logn; ++k) {
            for (int i = 1; i + (1 << k) - 1 <= n; ++i) {
                st[k][i] = gcd(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
            }
        }
    }

    int consulta(int izq, int der) const {
        int k = 31 - __builtin_clz(der - izq + 1);
        return gcd(st[k][izq], st[k][der - (1 << k) + 1]);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, consultas;
    cin >> n >> consultas;
    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    TablaGcd tabla(a);
    while (consultas--) {
        int izq, der;
        cin >> izq >> der;
        cout << tabla.consulta(izq, der) << "\n";
    }
    return 0;
}
```
