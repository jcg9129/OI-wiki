## Definition

The minimum spanning tree on a directed graph (Directed Minimum Spanning Tree) is called a minimum arborescence.

The commonly-used algorithm is Zhu-Liu's algorithm (also called Edmonds' algorithm), which can solve the minimum arborescence problem in $O(nm)$ time.

## Process

1.  For each point, choose the edge pointing to it with the smallest edge weight.
2.  If there is no cycle, the algorithm terminates; otherwise contract the cycle and update the distances from other points to the cycle.

## Implementation

```cpp
bool solve() {
  ans = 0;
  int u, v, root = 0;
  for (;;) {
    f(i, 0, n) in[i] = 1e100;
    f(i, 0, m) {
      u = e[i].s;
      v = e[i].t;
      if (u != v && e[i].w < in[v]) {
        in[v] = e[i].w;
        pre[v] = u;
      }
    }
    f(i, 0, m) if (i != root && in[i] > 1e50) return 0;
    int tn = 0;
    memset(id, -1, sizeof id);
    memset(vis, -1, sizeof vis);
    in[root] = 0;
    f(i, 0, n) {
      ans += in[i];
      v = i;
      while (vis[v] != i && id[v] == -1 && v != root) {
        vis[v] = i;
        v = pre[v];
      }
      if (v != root && id[v] == -1) {
        for (int u = pre[v]; u != v; u = pre[u]) id[u] = tn;
        id[v] = tn++;
      }
    }
    if (tn == 0) break;
    f(i, 0, n) if (id[i] == -1) id[i] = tn++;
    f(i, 0, m) {
      u = e[i].s;
      v = e[i].t;
      e[i].s = id[u];
      e[i].t = id[v];
      if (e[i].s != e[i].t) e[i].w -= in[v];
    }
    n = tn;
    root = id[root];
  }
  return ans;
}
```

## Tarjan's DMST algorithm

Tarjan proposed an algorithm that can solve the minimum arborescence problem in $O(m+n\log n)$ time.

The algorithm description and reference code here are based on the lecture notes of Professor Uri Zwick; for more details refer to the original text.

### Process

Tarjan's algorithm is divided into two processes: **contraction** and **expansion**. Next we first introduce the **contraction** process.

We need to assume the input graph is strongly connected; if not, then add $O(n)$ edges to make it so, and the edge weights of these edges are infinite.

We need a heap to store related information such as the incoming-edge number of nodes, the incoming-edge weight, and the total cost of a node; since there will be heap-merging operations in the subsequent process, here we implement it with a [leftist tree](../ds/leftist-tree.md) and a [DSU](../ds/dsu.md). Each step of the algorithm chooses an arbitrary node $v$; we need to ensure that $v$ is not the root node, and that its incoming edge is not in the heap. Then add $v$'s minimum incoming edge to the heap; if this newly-added edge causes the edges in the heap to form a cycle, then contract the nodes constituting the cycle; we may as well name these already-contracted nodes **super nodes**, and continue this process; if all vertices are contracted into one super node, then the contraction process ends. After the whole contraction process ends, a contraction tree is obtained, on which the expansion operation is then performed.

The edges in the heap always form a path $v_0\leftarrow v_1\leftarrow \dots\leftarrow v_k$; since the graph is strongly connected, this path must exist, and the $v_i$ in it may be the initial single nodes, or may be super nodes after compression.

Initially there is $v_o=a$, where $a$ is any node in the graph; each time a minimum incoming edge $v_k\leftarrow u$ is chosen; if $u$ is not one of the nodes $v_0,v_1,\dots,v_k$, then extend the node to $v_{k+1}=u$. If $u$ is one of them $v_i$, then a cycle about $v_i\leftarrow\dots\leftarrow v_k\leftarrow v_i$ is found, and they are contracted into one super node $c$.

Put all nodes or super nodes into the queue $P$, and initially choose an arbitrary node $a$; as long as the queue is not empty, perform the following steps:

1.  Choose $a$'s minimum incoming edge, ensuring there is no self-loop, and find the node $b$ at the other end. If node $b$ has not been recorded, it means no cycle has formed; let $a\leftarrow b$, and continue the current operation to look for a cycle.

2.  If $b$ has been recorded, it means a cycle has appeared. Increase the total number of nodes by one, renumber all nodes on the cycle, merge the heap, and update the total weight of the nodes/super nodes. The weight-update operation collects all incoming edges of all nodes on the cycle and subtracts the edge weight of the incoming edge on the cycle.

![dmst1](./images/dmst1.png)

Taking the figure as an example, the strongly connected graph on the left forms the contraction tree on the right after contraction, where $a$ is the super node after node 1 and node 2 are contracted, $b$ is the super node after node 3, node 4, and node 5 are contracted, and $A$ is formed after the two super nodes $a$ and $b$ are contracted.

The expansion process is relatively simple; starting from the originally-required root node $r$, expand each cycle on the path from $r$ to the root of the contraction tree. Then starting from $r$'s ancestor node $f_r$, expand the cycle on its path to the root, until all nodes are traversed.

### Implementation

```cpp
#include <cstdio>
#include <cstring>
#include <queue>
#include <vector>
using namespace std;

using ll = long long;
constexpr int MAXN = 102;
constexpr int INF = 0x3f3f3f3f;

struct UnionFind {
  int fa[MAXN << 1];

  UnionFind() { memset(fa, 0, sizeof(fa)); }

  void clear(int n) { memset(fa + 1, 0, sizeof(int) * n); }

  int find(int x) { return fa[x] ? fa[x] = find(fa[x]) : x; }

  int operator[](int x) { return find(x); }
};

struct Edge {
  int u, v, w, w0;
};

struct Heap {
  Edge *e;
  int rk, constant;
  Heap *lch, *rch;

  Heap(Edge *_e) : e(_e), rk(1), constant(0), lch(NULL), rch(NULL) {}

  void push() {
    if (lch) lch->constant += constant;
    if (rch) rch->constant += constant;
    e->w += constant;
    constant = 0;
  }
};

Heap *merge(Heap *x, Heap *y) {
  if (!x) return y;
  if (!y) return x;
  if (x->e->w + x->constant > y->e->w + y->constant) swap(x, y);
  x->push();
  x->rch = merge(x->rch, y);
  if (!x->lch || x->lch->rk < x->rch->rk) swap(x->lch, x->rch);
  if (x->rch)
    x->rk = x->rch->rk + 1;
  else
    x->rk = 1;
  return x;
}

Edge *extract(Heap *&x) {
  Edge *r = x->e;
  x->push();
  x = merge(x->lch, x->rch);
  return r;
}

vector<Edge> in[MAXN];
int n, m, fa[MAXN << 1], nxt[MAXN << 1];
Edge *ed[MAXN << 1];
Heap *Q[MAXN << 1];
UnionFind id;

void contract() {
  bool mark[MAXN << 1];
  // record each node on the graph and the nodes connected to it.
  for (int i = 1; i <= n; i++) {
    queue<Heap *> q;
    for (int j = 0; j < in[i].size(); j++) q.push(new Heap(&in[i][j]));
    while (q.size() > 1) {
      Heap *u = q.front();
      q.pop();
      Heap *v = q.front();
      q.pop();
      q.push(merge(u, v));
    }
    Q[i] = q.front();
  }
  mark[1] = true;
  for (int a = 1, b = 1, p; Q[a]; b = a, mark[b] = true) {
    // find the minimum incoming edge and its endpoint, ensuring no cycle.
    do {
      ed[a] = extract(Q[a]);
      a = id[ed[a]->u];
    } while (a == b && Q[a]);
    if (a == b) break;
    if (!mark[a]) continue;
    // contract the found cycle, renumber the nodes in the cycle, and update the total weight.
    for (a = b, n++; a != n; a = p) {
      id.fa[a] = fa[a] = n;
      if (Q[a]) Q[a]->constant -= ed[a]->w;
      Q[n] = merge(Q[n], Q[a]);
      p = id[ed[a]->u];
      nxt[p == n ? b : p] = a;
    }
  }
}

ll expand(int x, int r);

ll expand_iter(int x) {
  ll r = 0;
  for (int u = nxt[x]; u != x; u = nxt[u]) {
    if (ed[u]->w0 >= INF)
      return INF;
    else
      r += expand(ed[u]->v, u) + ed[u]->w0;
  }
  return r;
}

ll expand(int x, int t) {
  ll r = 0;
  for (; x != t; x = fa[x]) {
    r += expand_iter(x);
    if (r >= INF) return INF;
  }
  return r;
}

void link(int u, int v, int w) { in[v].push_back({u, v, w, w}); }

int main() {
  int rt;
  scanf("%d %d %d", &n, &m, &rt);
  for (int i = 0; i < m; i++) {
    int u, v, w;
    scanf("%d %d %d", &u, &v, &w);
    link(u, v, w);
  }
  // ensure strong connectivity
  for (int i = 1; i <= n; i++) link(i > 1 ? i - 1 : n, i, INF);
  contract();
  ll ans = expand(rt, n);
  if (ans >= INF)
    puts("-1");
  else
    printf("%lld\n", ans);
  return 0;
}
```

## References

Uri Zwick. (2013), [Directed Minimum Spanning Trees](http://www.cs.tau.ac.il/~zwick/grad-algo-13/directed-mst.pdf), Lecture notes on "Analysis of Algorithms"

<https://riteme.site/blog/2018-6-18/mdst.html#_3>
