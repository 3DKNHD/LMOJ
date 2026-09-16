#include <bits/stdc++.h>
using namespace std;

vector<int> prefijo_kmp(const string& s) {
    vector<int> pi(s.size(), 0);
    for (int i = 1; i < (int)s.size(); ++i) {
        int j = pi[i - 1];
        while (j && s[i] != s[j]) {
            j = pi[j - 1];
        }
        if (s[i] == s[j]) {
            ++j;
        }
        pi[i] = j;
    }
    return pi;
}

int contar_ocurrencias(const string& patron, const string& texto) {
    string s = patron + "#" + texto;
    vector<int> pi = prefijo_kmp(s);
    int m = (int)patron.size();
    int cuantos = 0;
    for (int v : pi) {
        if (v == m) {
            ++cuantos;
        }
    }
    return cuantos;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string patron, texto;
    cin >> patron >> texto;
    cout << contar_ocurrencias(patron, texto) << "\n";
    return 0;
}
