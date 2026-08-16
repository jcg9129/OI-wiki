Before reading this article, please first read the definition part of the [Introduction to network flow](../flow.md) wiki.

## Cost flow

Given a network $G=(V,E)$, each edge, besides having a capacity constraint $c(u,v)$, also has a cost per unit flow $w(u,v)$.

When the flow of $(u,v)$ is $f(u,v)$, it costs $f(u,v)\times w(u,v)$.

$w$ also satisfies skew symmetry, i.e. $w(u,v)=-w(v,u)$.

Then the maximum flow with the smallest total cost in this network is called the **minimum-cost maximum flow**, i.e. minimizing $\sum_{(u,v)\in E}f(u,v)\times w(u,v)$ under the premise of maximizing $\sum_{(s,v)\in E}f(s,v)$.

## SSP algorithm

The SSP (Successive Shortest Path) algorithm is a greedy algorithm. Its idea is to find the augmenting path with the smallest unit cost each time to augment, until no augmenting path exists on the graph.

If there is a cycle with negative unit cost on the graph, the SSP algorithm cannot correctly find the minimum-cost maximum flow of this network. In this case, the cycle-canceling algorithm needs to be used first to eliminate the negative cycles on the graph.

### Proof

We consider using mathematical induction and proof by contradiction to prove the correctness of the SSP algorithm.

Let the minimum cost when the flow is $i$ be $f_i$. We assume that the initial network **has no negative cycle**; in this case $f_0=0$.

Assume the $f_i$ found by the SSP algorithm is the minimum cost; on the basis of $f_i$, we find a shortest augmenting path, thereby finding $f_{i+1}$. At this point $f_{i+1}-f_i$ is the length of this shortest augmenting path.

Suppose there exists a smaller $f_{i+1}$, denote it as $f'_{i+1}$. Because $f_{i+1}-f_i$ is already the shortest augmenting path, $f'_{i+1}-f_i$ must correspond to an augmenting path passing through **at least one negative cycle**.

At this point the contradiction appears: since there exists an augmenting path passing through at least one negative cycle, then $f_i$ is not the minimum cost. Because just by adding flow to this negative cycle, we can make the cost corresponding to $f_i$ smaller without increasing the flow out of $s$.

In summary, the SSP algorithm can correctly find the minimum-cost maximum flow of a network without negative cycles.

### Time complexity

If the [Bellman–Ford algorithm](../shortest-path.md#bellmanford-algorithm) is used to solve the shortest path, the time complexity of finding an augmenting path each time is $O(nm)$. Let the maximum flow of this network be $f$; then the worst-case time complexity is $O(nmf)$. In fact, the SSP algorithm is [pseudo-polynomial time](../../misc/cc-basic.md#pseudo-polynomial-time-伪多项式时间).

???+ note "Why is the SSP algorithm pseudo-polynomial time?"
    The time complexity of the SSP algorithm has an upper bound of $O(nmf)$, which is a polynomial in the value range, so it is pseudo-polynomial time.
    
    A network with $m=n^2,f=2^{n/2}$ can be constructed[^note1] to make the time complexity of the SSP algorithm reach $O(n^3 2^{n/2})$, so the SSP algorithm is not polynomial time.

### Implementation

We just need to replace the process of finding augmenting paths in the EK algorithm or Dinic algorithm with using a shortest-path algorithm to find the augmenting path with the smallest unit cost.

??? note "Implementation based on the EK algorithm"
    ```cpp
    struct qxx {
      int nex, t, v, c;
    };
    
    qxx e[M];
    int h[N], cnt = 1;
    
    void add_path(int f, int t, int v, int c) {
      e[++cnt] = qxx{h[f], t, v, c}, h[f] = cnt;
    }
    
    void add_flow(int f, int t, int v, int c) {
      add_path(f, t, v, c);
      add_path(t, f, 0, -c);
    }
    
    int dis[N], pre[N], incf[N];
    bool vis[N];
    
    bool spfa() {
      memset(dis, 0x3f, sizeof(dis));
      queue<int> q;
      q.push(s), dis[s] = 0, incf[s] = INF, incf[t] = 0;
      while (q.size()) {
        int u = q.front();
        q.pop();
        vis[u] = false;
        for (int i = h[u]; i; i = e[i].nex) {
          const int &v = e[i].t, &w = e[i].v, &c = e[i].c;
          if (!w || dis[v] <= dis[u] + c) continue;
          dis[v] = dis[u] + c, incf[v] = min(w, incf[u]), pre[v] = i;
          if (!vis[v]) q.push(v), vis[v] = true;
        }
      }
      return incf[t];
    }
    
    int maxflow, mincost;
    
    void update() {
      maxflow += incf[t];
      for (int u = t; u != s; u = e[pre[u] ^ 1].t) {
        e[pre[u]].v -= incf[t], e[pre[u] ^ 1].v += incf[t];
        mincost += incf[t] * e[pre[u]].c;
      }
    }
    
    // call: while(spfa())update();
    ```

??? note "Implementation based on the Dinic algorithm"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <queue>
    
    constexpr int N = 5e3 + 5, M = 1e5 + 5;
    constexpr int INF = 0x3f3f3f3f;
    int n, m, tot = 1, lnk[N], cur[N], ter[M], nxt[M], cap[M], cost[M], dis[N], ret;
    bool vis[N];
    
    void add(int u, int v, int w, int c) {
      ter[++tot] = v, nxt[tot] = lnk[u], lnk[u] = tot, cap[tot] = w, cost[tot] = c;
    }
    
    void addedge(int u, int v, int w, int c) { add(u, v, w, c), add(v, u, 0, -c); }
    
    bool spfa(int s, int t) {
      memset(dis, 0x3f, sizeof(dis));
      memcpy(cur, lnk, sizeof(lnk));
      std::queue<int> q;
      q.push(s), dis[s] = 0, vis[s] = true;
      while (!q.empty()) {
        int u = q.front();
        q.pop(), vis[u] = false;
        for (int i = lnk[u]; i; i = nxt[i]) {
          int v = ter[i];
          if (cap[i] && dis[v] > dis[u] + cost[i]) {
            dis[v] = dis[u] + cost[i];
            if (!vis[v]) q.push(v), vis[v] = true;
          }
        }
      }
      return dis[t] != INF;
    }
    
    int dfs(int u, int t, int flow) {
      if (u == t) return flow;
      vis[u] = true;
      int ans = 0;
      for (int &i = cur[u]; i && ans < flow; i = nxt[i]) {
        int v = ter[i];
        if (!vis[v] && cap[i] && dis[v] == dis[u] + cost[i]) {
          int x = dfs(v, t, std::min(cap[i], flow - ans));
          if (x) ret += x * cost[i], cap[i] -= x, cap[i ^ 1] += x, ans += x;
        }
      }
      vis[u] = false;
      return ans;
    }
    
    int mcmf(int s, int t) {
      int ans = 0;
      while (spfa(s, t)) {
        int x;
        while ((x = dfs(s, t, INF))) ans += x;
      }
      return ans;
    }
    
    int main() {
      int s, t;
      scanf("%d%d%d%d", &n, &m, &s, &t);
      while (m--) {
        int u, v, w, c;
        scanf("%d%d%d%d", &u, &v, &w, &c);
        addedge(u, v, w, c);
      }
      int ans = mcmf(s, t);
      printf("%d %d\n", ans, ret);
      return 0;
    }
    ```

### Primal-Dual algorithm

The time complexity of using Bellman–Ford to solve the shortest path is $O(nm)$, which, whether on a sparse graph or a dense graph, is inferior to the Dijkstra algorithm[^note2]. But there are edges with negative unit cost on the network, so the Dijkstra algorithm cannot be used directly.

The idea of the Primal-Dual algorithm is similar to the [Johnson all-pairs shortest path algorithm](../shortest-path.md#johnson-all-source-shortest-path-algorithm); by setting a potential for each point, it changes the cost of all edges on the network (hereinafter abbreviated as edge weight) to non-negative values, so that the Dijkstra algorithm can be applied to find the augmenting path with the smallest unit cost on the network.

First run a shortest path once to find the shortest distance from the source to each point (which is also the initial potential of that point) $h_i$. Next, same as the Johnson algorithm, for an edge from $u$ to $v$ with unit cost $w$, reset its edge weight to $w+h_u-h_v$.

We can find that after setting the potentials this way, the shortest path on the new network must correspond to the shortest path on the original network. The proof was already given when introducing the Johnson algorithm, and is not elaborated here.

Different from the conventional shortest-path problem, after each augmentation the shape of the graph changes, in which case the potentials of each point need to be updated.

How to update? First give the conclusion: let the shortest distance from the source to point $i$ after augmentation be $d'_i$ (the distance here is the distance obtained after resetting each edge's edge weight); just add $d'_i$ to $h_i$. Below we prove that after updating the edge weights this way, the edge weights of all edges on the graph are non-negative.

It is easy to find that after one round of augmentation, since some $(i,j)$ edges are on the augmenting path, some $(j,i)$ edges will correspondingly appear on the residual network, and it must be satisfied that $d'_i+(w(i,j)+h_i-h_j)=d'_j$ (otherwise the $(i,j)$ edge would not be on the augmenting path). After a slight transformation, we obtain $w(j,i)+(h_j+d'_j)-(h_i+d'_i)=0$. Therefore the edge weight of the newly added edge is non-negative.

And for the original edges, before augmentation, $d'_i+(w(i,j)+h_i-h_j) - d'_j \geq 0$, so $w(i,j)+(d'_i+h_i)-(d'_j+h_j) \geq 0$, i.e. using $h_i+d'_i$ as the new potential will not make the edge weight of $(i,j)$ become negative.

In summary, after augmentation the edge weights of all edges are non-negative, and using the Dijkstra algorithm can correctly find the shortest path on the graph.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <queue>
    constexpr int INF = 0x3f3f3f3f;
    using namespace std;
    
    struct edge {
      int v, f, c, next;
    } e[100005];
    
    struct node {
      int v, e;
    } p[10005];
    
    struct mypair {
      int dis, id;
    
      bool operator<(const mypair& a) const { return dis > a.dis; }
    
      mypair(int d, int x) { dis = d, id = x; }
    };
    
    int head[5005], dis[5005], vis[5005], h[5005];
    int n, m, s, t, cnt = 1, maxf, minc;
    
    void addedge(int u, int v, int f, int c) {
      e[++cnt].v = v;
      e[cnt].f = f;
      e[cnt].c = c;
      e[cnt].next = head[u];
      head[u] = cnt;
    }
    
    bool dijkstra() {
      priority_queue<mypair> q;
      for (int i = 1; i <= n; i++) dis[i] = INF;
      memset(vis, 0, sizeof(vis));
      dis[s] = 0;
      q.push(mypair(0, s));
      while (!q.empty()) {
        int u = q.top().id;
        q.pop();
        if (vis[u]) continue;
        vis[u] = 1;
        for (int i = head[u]; i; i = e[i].next) {
          int v = e[i].v, nc = e[i].c + h[u] - h[v];
          if (e[i].f && dis[v] > dis[u] + nc) {
            dis[v] = dis[u] + nc;
            p[v].v = u;
            p[v].e = i;
            if (!vis[v]) q.push(mypair(dis[v], v));
          }
        }
      }
      return dis[t] != INF;
    }
    
    void spfa() {
      queue<int> q;
      memset(h, 63, sizeof(h));
      h[s] = 0, vis[s] = 1;
      q.push(s);
      while (!q.empty()) {
        int u = q.front();
        q.pop();
        vis[u] = 0;
        for (int i = head[u]; i; i = e[i].next) {
          int v = e[i].v;
          if (e[i].f && h[v] > h[u] + e[i].c) {
            h[v] = h[u] + e[i].c;
            if (!vis[v]) {
              vis[v] = 1;
              q.push(v);
            }
          }
        }
      }
    }
    
    int main() {
      scanf("%d%d%d%d", &n, &m, &s, &t);
      for (int i = 1; i <= m; i++) {
        int u, v, f, c;
        scanf("%d%d%d%d", &u, &v, &f, &c);
        addedge(u, v, f, c);
        addedge(v, u, 0, -c);
      }
      spfa();  // first find the initial potentials
      while (dijkstra()) {
        int minf = INF;
        for (int i = 1; i <= n; i++) h[i] += dis[i];
        for (int i = t; i != s; i = p[i].v) minf = min(minf, e[p[i].e].f);
        for (int i = t; i != s; i = p[i].v) {
          e[p[i].e].f -= minf;
          e[p[i].e ^ 1].f += minf;
        }
        maxf += minf;
        minc += minf * h[t];
      }
      printf("%d %d\n", maxf, minc);
      return 0;
    }
    ```

## Exercises

-   [「Luogu 3381」【Template】Minimum-Cost Maximum Flow](https://www.luogu.com.cn/problem/P3381)
-   [「Luogu 4452」Flight Arrangement](https://www.luogu.com.cn/problem/P4452)
-   [「SDOI 2009」Morning Run](https://www.luogu.com.cn/problem/P2153)
-   [「SCOI 2007」Repairing Cars](https://www.luogu.com.cn/problem/P2053)
-   [「HAOI 2010」Ordering Goods](https://www.luogu.com.cn/problem/P2517)
-   [「NOI 2012」Food Festival](https://loj.ac/problem/2674)

## References and notes

[^note1]: For the detailed construction method, refer to [min\_25's blog](https://web.archive.org/web/20211009144446/https://min-25.hatenablog.com/entry/2018/03/19/235802).

[^note2]: On a sparse graph, using heap optimization can achieve $O(m \log n)$ time complexity, while on a dense graph, without heap optimization, one can achieve $O(n^2)$ time complexity.
