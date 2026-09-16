#include <bits/stdc++.h>
using namespace std;

bool alcanza(long long tiempo, const vector<long long>& velocidades, long long k) {
    long long hechas = 0;
    for (long long v : velocidades) {
        hechas += tiempo / v;
        if (hechas >= k) {
            return true;
        }
    }
    return false;
}

long long minimo_tiempo(const vector<long long>& velocidades, long long k) {
    long long menor = *min_element(velocidades.begin(), velocidades.end());
    long long lo = 1;
    long long hi = menor * k;
    long long respuesta = hi;

    while (lo <= hi) {
        long long mid = lo + (hi - lo) / 2;
        if (alcanza(mid, velocidades, k)) {
            respuesta = mid;
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return respuesta;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long k;
    cin >> n >> k;
    vector<long long> velocidades(n);
    for (int i = 0; i < n; ++i) {
        cin >> velocidades[i];
    }

    cout << minimo_tiempo(velocidades, k) << "\n";
    return 0;
}
