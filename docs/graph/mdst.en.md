Before learning about the Minimum Diameter Spanning Tree, it is recommended to first read the content of [tree diameter](./tree-diameter.md).

## Definition

Among all spanning trees of an undirected graph, the spanning tree with the smallest diameter is the minimum diameter spanning tree.

## Absolute center of a graph

To solve for the minimum diameter spanning tree, we first need to find the **absolute center of the graph**. The **absolute center of the graph** may exist on an edge or on some node; the maximum of the shortest distances from this center to all points is minimized.

According to the definition of the **absolute center of the graph**, we know that there are at least two nodes farthest from the absolute center.

Let $d(i,j)$ be the shortest-path length between vertices $i,j$; compute the shortest paths of all nodes through a multi-source shortest-path algorithm.

$\textit{rk}(i,j)$ records the $j$-th closest node among all other nodes from point $i$.

The absolute center of the graph may be on some edge. Enumerate each edge $w=(u,v)$, and assume the absolute center of the graph $c$ is on this edge. Then the length to $u$ is $x$ ($x \leq w$), and the length to $v$ is $w - x$.

For any point $i$ in the graph, the distance from the absolute center of the graph $c$ to $i$ is $d(c,i)=\min(d(u,i) + x, d(v,i) + (w - x))$.

Take a node $i$ as an example; the positional relationship between this node and the absolute center of the graph is shown in the figure below.

![mdst1](./images/mdst-graph.svg)

As the absolute center of the graph $c$ changes along the edge, a function graph of distance versus the position of $c$ is generated. Obviously, the current function graph of $d(c,i)$ is a polyline segment composed of two line segments with the same slope.

![mdst2](./images/mdst-plot1.svg)

For any node on the graph, the function of the farthest distance from the absolute center of the graph to a node is written as $f = \max\{ d(c,i)\},i \in[1,n]$, and its function graph is as follows.

![mdst3](./images/mdst-plot2.svg)

And the lowest point among the intersection points of these polylines has an abscissa that is the position of the absolute center of the graph.

The absolute center of the graph may be on some node; update using the node farthest from the pre-selected node, i.e. $\textit{ans}\leftarrow \min(\textit{ans},d(i,\textit{rk}(i,n))\times 2)$.

### Procedure

1.  Use a multi-source shortest-path algorithm ([Floyd](./shortest-path.md#floyd-algorithm), [Johnson](./shortest-path.md#johnson-all-source-shortest-path-algorithm), etc.) to compute the $d$ array;

2.  Compute $\textit{rk}(i,j)$, and sort it in ascending order;

3.  The absolute center of the graph may be on some node; update using the node farthest from the pre-selected node, traverse all nodes and update the minimum value with $\textit{ans}\leftarrow \min(\textit{ans},d(i,\textit{rk}(i,n)) \times 2)$.

4.  The absolute center of the graph may be on some edge; enumerate all edges. For an edge $w(u,v)$, update starting from the node farthest from $u$. When the situation $d(v,\textit{rk}(u,i)) > \max_{j=i+1}^n d(v,\textit{rk}(u,j))$ occurs, update with $\textit{ans}\leftarrow  \min(\textit{ans}, d(u,\textit{rk}(u,i))+\max_{j=i+1}^n d(v,\textit{rk}(u,j))+w(u,v))$. Because this situation will change the absolute center of the graph.

??? note "Implementation"
    ```cpp
    bool cmp(int a, int b) { return val[a] < val[b]; }
    
    void Floyd() {
      for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
          for (int j = 1; j <= n; j++) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    }
    
    void solve() {
      Floyd();
      for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
          rk[i][j] = j;
          val[j] = d[i][j];
        }
        sort(rk[i] + 1, rk[i] + 1 + n, cmp);
      }
      int ans = INF;
      // the absolute center of the graph may be on a node
      for (int i = 1; i <= n; i++) ans = min(ans, d[i][rk[i][n]] * 2);
      // the absolute center of the graph may be on an edge
      for (int i = 1; i <= m; i++) {
        int u = a[i].u, v = a[i].v, w = a[i].w;
        for (int p = n, i = n - 1; i >= 1; i--) {
          if (d[v][rk[u][i]] > d[v][rk[u][p]]) {
            ans = min(ans, d[u][rk[u][i]] + d[v][rk[u][p]] + w);
            p = i;
          }
        }
      }
    }
    ```

### Example problems

-   [CodeForce 266D BerDonalds](https://codeforces.com/contest/266/problem/D)

## Minimum diameter spanning tree

According to the definition of the absolute center of the graph, it is easy to know that the absolute center of the graph is the midpoint of the diameter of the minimum diameter spanning tree.

To solve for the minimum diameter spanning tree, we first need to find the absolute center of the graph. Taking the absolute center of the graph as the start point, generate a shortest-path tree, and then we can obtain the minimum diameter spanning tree.

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <climits>
    #include <iostream>
    #include <vector>
    using namespace std;
    constexpr int MAXN = 502;
    using ll = long long;
    using pii = pair<int, int>;
    ll d[MAXN][MAXN], dd[MAXN][MAXN], rk[MAXN][MAXN], val[MAXN];
    constexpr ll INF = 1e17;
    int n, m;
    
    bool cmp(int a, int b) { return val[a] < val[b]; }
    
    void floyd() {
      for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
          for (int j = 1; j <= n; j++) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
    }
    
    struct node {
      ll u, v, w;
    } a[MAXN * (MAXN - 1) / 2];
    
    void solve() {
      // find the absolute center of the graph
      floyd();
      for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
          rk[i][j] = j;
          val[j] = d[i][j];
        }
        sort(rk[i] + 1, rk[i] + 1 + n, cmp);
      }
      ll P = 0, ansP = INF;
      // on a point
      for (int i = 1; i <= n; i++) {
        if (d[i][rk[i][n]] * 2 < ansP) {
          ansP = d[i][rk[i][n]] * 2;
          P = i;
        }
      }
      // on an edge
      int f1 = 0, f2 = 0;
      ll disu = INT_MIN, disv = INT_MIN, ansL = INF;
      for (int i = 1; i <= m; i++) {
        ll u = a[i].u, v = a[i].v, w = a[i].w;
        for (int p = n, i = n - 1; i >= 1; i--) {
          if (d[v][rk[u][i]] > d[v][rk[u][p]]) {
            if (d[u][rk[u][i]] + d[v][rk[u][p]] + w < ansL) {
              ansL = d[u][rk[u][i]] + d[v][rk[u][p]] + w;
              f1 = u, f2 = v;
              disu = (d[u][rk[u][i]] + d[v][rk[u][p]] + w) / 2 - d[u][rk[u][i]];
              disv = w - disu;
            }
            p = i;
          }
        }
      }
      cout << min(ansP, ansL) / 2 << '\n';
      // minimum path spanning tree
      vector<pii> pp;
      for (int i = 1; i <= 501; ++i)
        for (int j = 1; j <= 501; ++j) dd[i][j] = INF;
      for (int i = 1; i <= 501; ++i) dd[i][i] = 0;
      if (ansP <= ansL) {
        for (int j = 1; j <= n; j++) {
          for (int i = 1; i <= m; ++i) {
            ll u = a[i].u, v = a[i].v, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
            u = a[i].v, v = a[i].u, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
          }
        }
        for (auto [x, y] : pp) cout << x << ' ' << y << '\n';
      } else {
        d[n + 1][f1] = disu;
        d[f1][n + 1] = disu;
        d[n + 1][f2] = disv;
        d[f2][n + 1] = disv;
        a[m + 1].u = n + 1, a[m + 1].v = f1, a[m + 1].w = disu;
        a[m + 2].u = n + 1, a[m + 2].v = f2, a[m + 2].w = disv;
        n += 1;
        m += 2;
        floyd();
        P = n;
        for (int j = 1; j <= n; j++) {
          for (int i = 1; i <= m; ++i) {
            ll u = a[i].u, v = a[i].v, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
            u = a[i].v, v = a[i].u, w = a[i].w;
            if (dd[P][u] + w == d[P][v] && dd[P][u] + w < dd[P][v]) {
              dd[P][v] = dd[P][u] + w;
              pp.push_back({u, v});
            }
          }
        }
        cout << f1 << ' ' << f2 << '\n';
        for (auto [x, y] : pp)
          if (x != n && y != n) cout << x << ' ' << y << '\n';
      }
    }
    
    void init() {
      for (int i = 1; i <= 501; ++i)
        for (int j = 1; j <= 501; ++j) d[i][j] = INF;
      for (int i = 1; i <= 501; ++i) d[i][i] = 0;
    }
    
    int main() {
      init();
      cin >> n >> m;
      for (int i = 1; i <= m; ++i) {
        ll u, v, w;
        cin >> u >> v >> w;
        w *= 2;
        d[u][v] = w, d[v][u] = w;
        a[i].u = u, a[i].v = v, a[i].w = w;
      }
      solve();
      return 0;
    }
    ```

### Example problems

[SPOJ MDST](https://www.spoj.com/problems/MDST/)

[timus 1569. Networking the "Iset"](https://acm.timus.ru/problem.aspx?space=1&num=1569)

[SPOJ PT07C - The GbAaY Kingdom](https://www.spoj.com/problems/PT07C)

## References

[Play with Trees Solutions The GbAaY Kingdom](https://adn.botao.hu/adn-backup/blog/attachments/month_0705/32007531153238.pdf)
