#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>

using ll = long long;
using ld = long double;
const int maxn = 1e5, maxm = 1e5;
const ll inf = std::numeric_limits<ll>::max();

struct edge {
    int i, n, t;
};

std::vector<std::pair<ll,ll>>C[maxm+1];

int n,m,k,p,s,f;

struct node {
    ll t;
    bool v;
    std::vector<edge>e;
}nodes[maxn+1];

ll calc(ll t, ll T){
    ld a = std::ceil((ld(T)/100+1)*t);

    if(100500.0*t < a) return 100500.0*t;
    return ll(a+0.1);
}
ll getT(ll t, edge e){

}

int main() {
    scanf("%d %d",&n,&m);

    for(int i=0; i<=m; i++){
        int a, b, t;

        scanf("%d %d %d",&a,&b,&t);       
    }
}