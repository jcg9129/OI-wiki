## Concepts

### Cut

For a network flow graph $G=(V,E)$, its cut is defined as a **way of partitioning the points**: partition all points into two sets $S$ and $T=V-S$, where the source $s\in S$ and the sink $t\in T$.

### Capacity of a cut

We define the capacity $c(S,T)$ of the cut $(S,T)$ as the sum of the capacities of all edges from $S$ to $T$, i.e. $c(S,T)=\sum_{u\in S,v\in T}c(u,v)$. Of course we can also use $c(s,t)$ to denote $c(S,T)$.

### Minimum cut

The minimum cut is finding a cut $(S,T)$ such that the capacity $c(S,T)$ of the cut is minimized.

## Proof

### Max-flow min-cut theorem

See the max-flow min-cut theorem section of the [maximum flow](max-flow.md) page.

## Code

### Minimum cut

Through the **max-flow min-cut theorem**, we can directly obtain the following code:

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <queue>
    
    constexpr int N = 1e4 + 5, M = 2e5 + 5;
    int n, m, s, t, tot = 1, lnk[N], ter[M], nxt[M], val[M], dep[N], cur[N];
    
    void add(int u, int v, int w) {
      ter[++tot] = v, nxt[tot] = lnk[u], lnk[u] = tot, val[tot] = w;
    }
    
    void addedge(int u, int v, int w) { add(u, v, w), add(v, u, 0); }
    
    int bfs(int s, int t) {
      memset(dep, 0, sizeof(dep));
      memcpy(cur, lnk, sizeof(lnk));
      std::queue<int> q;
      q.push(s), dep[s] = 1;
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int i = lnk[u]; i; i = nxt[i]) {
          int v = ter[i];
          if (val[i] && !dep[v]) q.push(v), dep[v] = dep[u] + 1;
        }
      }
      return dep[t];
    }
    
    int dfs(int u, int t, int flow) {
      if (u == t) return flow;
      int ans = 0;
      for (int &i = cur[u]; i && ans < flow; i = nxt[i]) {
        int v = ter[i];
        if (val[i] && dep[v] == dep[u] + 1) {
          int x = dfs(v, t, std::min(val[i], flow - ans));
          if (x) val[i] -= x, val[i ^ 1] += x, ans += x;
        }
      }
      if (ans < flow) dep[u] = -1;
      return ans;
    }
    
    int dinic(int s, int t) {
      int ans = 0;
      while (bfs(s, t)) {
        int x;
        while ((x = dfs(s, t, 1 << 30))) ans += x;
      }
      return ans;
    }
    
    int main() {
      scanf("%d%d%d%d", &n, &m, &s, &t);
      while (m--) {
        int u, v, w;
        scanf("%d%d%d", &u, &v, &w);
        addedge(u, v, w);
      }
      printf("%d\n", dinic(s, t));
      return 0;
    }
    ```

### Scheme

We can, by DFS starting from the source $s$, walking edges with residual greater than $0$ each time, find all points in the point set $S$.

```cpp
void dfs(int u) {
  vis[u] = 1;
  for (int i = lnk[u]; i; i = nxt[i]) {
    int v = ter[i];
    if (!vis[v] && val[i]) dfs(v);
  }
}
```

### Number of cut edges

If we need to minimize the number of cut edges under the premise of the minimum cut, then first find the minimum cut, change the capacity of the edges that are not at full flow to $\infty$, change the capacity of the edges at full flow to $1$, and re-run the minimum cut to find the minimum number of cut edges; if there is no minimum-cut premise, directly set the capacity of all edges to $1$ and run a minimum cut.

## Problem model 1

There are $n$ items and two sets $A,B$; if an item is not placed in set $A$ it costs $a_i$, and if not placed in set $B$ it costs $b_i$; there are also several constraints of the form $u_i,v_i,w_i$, meaning if $u_i$ and $v_i$ are simultaneously not in one set it costs $w_i$. Each item must and can only belong to one set; find the minimum cost.

This is a classic **choose one of two** minimum-cut problem. For each set we set a source $s$ and a sink $t$; the $i$-th point connects an edge with capacity $a_i$ from $s$ and an edge with capacity $b_i$ to $t$. For the constraint $u,v,w$, we connect a bidirectional edge with capacity $w$ between $u,v$.

Note that when the source and sink are not connected, it represents that these points all chose one of the sets. If we cut the edge connecting to $s$ or $t$, it represents not placing it in set $A$ or $B$; if we cut the edge between items, it represents that these two items are not placed in the same set.

The minimum cut is the minimum cost.

## Problem model 2

Maximum-weight closure of a graph, i.e. given a directed graph where each point has a weight (which can be positive, negative, or $0$), you need to choose a subgraph with the maximum sum of weights such that the successors of each point in the subgraph are all in the subgraph.

Approach: establish a super source $s$ and a super sink $t$; if node $u$ has a positive weight, then $s$ connects a directed edge to $u$, with edge weight equal to that point's weight; if node $u$ has a negative weight, then $u$ connects a directed edge to $t$, with edge weight equal to the negation of that point's weight. Change all edge weights on the original graph to $\infty$. Run the network maximum flow, and subtract the maximum flow from the sum of all positive weights, which is the answer.

A few small conclusions to prove it:

1.  Each qualifying subgraph corresponds to a cut in the flow network. Because each cut divides the network into two parts, the part connected to $s$ satisfies that no edge points to the other part, so it satisfies the above condition. This proposition is necessary and sufficient.
2.  The edges removed by the minimum cut must be connected to one of $s$ and $t$. Because otherwise the edge weight is $\infty$, and it cannot possibly be part of the minimum cut.
3.  For the part of the subgraph we choose, sum of weights $=$ sum of all positive weights $-$ sum of the weights of the positive-weight points we did not choose $+$ sum of the weights of the negative-weight points we chose. When we do not choose a positive-weight point, its connecting edge with $s$ will be cut; when we choose a negative-weight point, its connecting edge with $t$ will be cut. The sum of the edge weights of the cut edges is the capacity of the cut. So the above formula is transformed into: sum of weights $=$ sum of all positive weights $-$ capacity of the cut.
4.  So we reach the conclusion, maximum sum of weights $=$ sum of all positive weights $-$ minimum cut $=$ sum of all positive weights $-$ maximum flow.

## Exercises

-   [「USACO 4.4」Pollutant Control](https://www.luogu.com.cn/problem/P1344)
-   [「USACO 5.4」Telecowmunication](https://www.luogu.com.cn/problem/P1345)
-   [「Luogu 1361」Little M's Crops](https://www.luogu.com.cn/problem/P1361)
-   [「SHOI 2007」Well-Intentioned Voting](https://www.luogu.com.cn/problem/P2057)
-   [Space Flight Plan Problem](https://www.luogu.com.cn/problem/P2762)
