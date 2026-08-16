author: Chrogeek, Enter-tainer, HeRaNO, Ir1d, Marcythm, ShadowsEpic, StudyingFather, Xeonacid, bear-good, billchenchina, diauweb, diauweb, greyqz, kawa-yoiko, ouuan, partychicken, sshwy, stevebraveman, zhouyuyang2002, renbaoshuo, Hszzzx, y-kx-b, toprise

## Definition

Before reading the following content, please be sure to read the [graph-theory-related concepts](./concept.md) and [tree basics](./tree-basic.md) parts, and understand the following definitions:

1.  spanning subgraph
2.  spanning tree

We define the **Minimum Spanning Tree** (MST) of an undirected connected graph as the spanning tree with the minimum sum of edge weights.

Note: Only connected graphs have spanning trees, while for disconnected graphs there only exist spanning forests.

## Kruskal algorithm

The Kruskal algorithm is a common and easy-to-write minimum spanning tree algorithm, invented by Kruskal. The basic idea of this algorithm is to add edges from small to large; it is a greedy algorithm.

### Prerequisite knowledge

[Disjoint set union](../ds/dsu.md), [greedy](../basic/greedy.md), [graph storage](./save.md).

### Implementation

Illustration:

![](./images/mst-2.apng)

Pseudocode:

<!--
```pseudo
\begin{algorithm}
\caption{Kruskal}
\begin{algorithmic}
\INPUT{ The edges of the graph $e$ where each element in $e$ is $(u, v, w)$ denoting that there is an edge between $u$ and $v$ weighted $w$. }
\OUTPUT The edges of the MST of the input graph
\STATE $result \gets \varnothing$
\STATE sort $e$ into nondecreasing order by weight $w$
\FOR{each $(u, v, w)$ in the sorted $e$}
    \IF{$u$ \AND $v$ are not connected in the union-find set}
        \STATE connect $u$ \AND $v$ in the union-find set
        \STATE $result \gets result \bigcup (u, v, w)$
    \ENDIF
\ENDFOR
\RETURN $result$
\end{algorithmic}
\end{algorithm}
```
-->

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{The edges of the graph } e , \text{ where each element in } e \text{ is } (u, v, w) \\
  &  \text{ denoting that there is an edge between } u \text{ and } v \text{ weighted } w . \\
2 &  \textbf{Output. } \text{The edges of the MST of the input graph}.\\
3 &  \textbf{Method. } \\ 
4 &  result \gets \varnothing \\
5 &  \text{sort } e \text{ into nondecreasing order by weight } w \\ 
6 &  \textbf{for} \text{ each } (u, v, w) \text{ in the sorted } e \\ 
7 &  \qquad \textbf{if } u \text{ and } v \text{ are not connected in the union-find set } \\
8 &  \qquad\qquad \text{connect } u \text{ and } v \text{ in the union-find set} \\
9 &  \qquad\qquad  result \gets result\;\bigcup\ \{(u, v, w)\} \\
10 &  \textbf{return }  result
\end{array}
$$

Although the algorithm is simple, it needs corresponding data structures to support it…… Specifically, maintain a forest, query whether two nodes are in the same tree, and connect two trees.

Speaking a bit more abstractly, maintain a bunch of **sets**, query whether two elements belong to the same set, and merge two sets.

Among these, querying whether two points are connected and connecting two points can be maintained using a disjoint set union.

If we use an $O(m\log m)$ sorting algorithm and use an $O(m\alpha(m, n))$ or $O(m\log n)$ disjoint set union, we can obtain a Kruskal algorithm with time complexity $O(m\log m)$.

### Proof

The idea is very simple: to construct a minimum spanning tree, we start from the edge with the smallest edge weight, add edges in order of edge weight from small to large; if some edge addition produces a cycle, discard this edge, until $n-1$ edges have been added, i.e. a tree is formed.

Proof: Use induction to prove that at any time the edge set chosen by the K algorithm is contained in some MST.

Base: At the start of the algorithm, this obviously holds (a minimum spanning tree exists).

Induction: Assume it holds at some moment, with the current edge set being $F$; let $T$ be this MST, and consider the next edge $e$ to be added.

If $e$ belongs to $T$, then it holds.

Otherwise, $T+e$ must have a cycle; consider another edge $f$ on this cycle that does not belong to $F$ (at least one exists).

First, the weight of $f$ definitely cannot be smaller than $e$, otherwise $f$ would be selected before $e$.

Then, the weight of $f$ definitely cannot be larger than $e$, otherwise $T+e-f$ would be a spanning tree even better than $T$.

So, $T+e-f$ contains $F$, and is also a minimum spanning tree; the induction holds.

### Example problem

???+ note "[Luogu P1195 Sky of the pocket](https://www.luogu.com.cn/problem/P1195)"
    There are $n$ clouds, and you want to connect them into $k$ marshmallows; connecting cloud $X_i$ and $Y_i$ requires a cost of $L_i$; find the minimum cost.

??? note "Example problem code"
    === "C++"
        ```cpp
        --8<-- "docs/graph/code/mst/mst_3.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/graph/code/mst/mst_3.py"
        ```
    
    === "Java"
        ```java
        --8<-- "docs/graph/code/mst/mst_3.java"
        ```

## Prim algorithm

The Prim algorithm is another common and easy-to-write minimum spanning tree algorithm. The basic idea of this algorithm is to start from one node and continuously add points (rather than adding edges as in the Kruskal algorithm).

### Implementation

Illustration:

![](./images/mst-3.apng)

Specifically, each time we select a node with the smallest distance, and update the distances of other nodes with the new edges.

Actually, just like the Dijkstra algorithm, each time we find a point with the smallest distance, we can find it by brute force or maintain it with a heap.

The heap-optimization method is similar to Dijkstra's heap optimization, but if we use a heap such as a binary heap that does not support $O(1)$ decrease-key, the complexity is no better than Kruskal, and the constant factor is also larger than Kruskal. So, in general we use the Kruskal algorithm; on dense graphs, especially complete graphs, the complexity of brute-force Prim is better than Kruskal, but it does **not necessarily** run faster in practice.

Brute force: $O(n^2+m)$.

Binary heap: $O((n+m) \log n)$.

Fibonacci heap: $O(n \log n + m)$.

Pseudocode:

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{The nodes of the graph }V\text{ ; the function }g(u, v)\text{ which}\\
  &  \text{means the weight of the edge }(u, v)\text{; the function }adj(v)\text{ which}\\
  &  \text{means the nodes adjacent to }v.\\
2 &  \textbf{Output. } \text{The sum of weights of the MST of the input graph.} \\
3 &  \textbf{Method.} \\
4 &  result \gets 0 \\
5 & \text{choose an arbitrary node in }V\text{ to be the }root \\
6 &  dis(root)\gets 0 \\
7 &  \textbf{for } \text{each node }v\in(V-\{root\}) \\
8 &  \qquad  dis(v)\gets\infty \\
9 &  rest\gets V \\
10 &  \textbf{while }  rest\ne\varnothing \\
11 &  \qquad cur\gets \text{the node with the minimum }dis\text{ in }rest \\
12 &  \qquad  result\gets result+dis(cur) \\
13 &  \qquad  rest\gets rest-\{cur\} \\
14 &  \qquad  \textbf{for}\text{ each node }v\in adj(cur) \\
15 &  \qquad\qquad  dis(v)\gets\min(dis(v), g(cur, v)) \\
16 &  \textbf{return }  result 
\end{array}
$$

Note: The above code only computes the weight of the minimum spanning tree; if we want to output the scheme, we also need to record which edge the $dis$ of each point represents.

??? note "Code implementation"
    ```cpp
    // Prim algorithm optimized with a binary heap.
    #include <cstring>
    #include <iostream>
    #include <queue>
    using namespace std;
    constexpr int N = 5050, M = 2e5 + 10;
    
    struct E {
      int v, w, x;
    } e[M * 2];
    
    int n, m, h[N], cnte;
    
    void adde(int u, int v, int w) { e[++cnte] = E{v, w, h[u]}, h[u] = cnte; }
    
    struct S {
      int u, d;
    };
    
    bool operator<(const S &x, const S &y) { return x.d > y.d; }
    
    priority_queue<S> q;
    int dis[N];
    bool vis[N];
    
    int res = 0, cnt = 0;
    
    void Prim() {
      memset(dis, 0x3f, sizeof(dis));
      dis[1] = 0;
      q.push({1, 0});
      while (!q.empty()) {
        if (cnt >= n) break;
        int u = q.top().u, d = q.top().d;
        q.pop();
        if (vis[u]) continue;
        vis[u] = true;
        ++cnt;
        res += d;
        for (int i = h[u]; i; i = e[i].x) {
          int v = e[i].v, w = e[i].w;
          if (w < dis[v]) {
            dis[v] = w, q.push({v, w});
          }
        }
      }
    }
    
    int main() {
      cin >> n >> m;
      for (int i = 1, u, v, w; i <= m; ++i) {
        cin >> u >> v >> w, adde(u, v, w), adde(v, u, w);
      }
      Prim();
      if (cnt == n)
        cout << res;
      else
        cout << "No MST.";
      return 0;
    }
    ```

### Proof

Starting from any node, divide the nodes into two classes: added and not-yet-added.

Each time, from the not-yet-added nodes, find a node whose minimum edge weight to an added node is the smallest.

Then add this node and connect the edge with the smallest edge weight.

Repeat $n-1$ times.

Proof: Again show that at each step, there exists a minimum spanning tree containing the chosen edge set.

Base: When there is only one node, it obviously holds.

Induction: If some step holds, with the current edge set being $F$, belonging to $T$ this MST, and next we want to add edge $e$.

If $e$ belongs to $T$, then it holds.

Otherwise, consider another edge $f$ on the cycle in $T+e$ that can be added to the current edge set.

First, the weight of $f$ is definitely not less than the weight of $e$, otherwise $f$ would be chosen instead of $e$.

Then, the weight of $f$ is definitely not greater than the weight of $e$, otherwise $T+e-f$ would be a smaller spanning tree.

Therefore, the weights of $e$ and $f$ are equal, $T+e-f$ is also a minimum spanning tree, and contains $F$.

## Boruvka algorithm

Next we introduce another algorithm for solving the minimum spanning tree——the Boruvka algorithm. The idea of this algorithm is a combination of the previous two algorithms. It can be used to solve the minimum spanning forest of an undirected graph. (For an undirected connected graph it is the minimum spanning tree.)

In problems where the edges have more special properties, the Boruvka algorithm has an advantage. For example, the complete-graph problem of [CF888G](https://codeforces.com/problemset/problem/888/G).

To describe this algorithm, we need to introduce some definitions:

1.  Define $E'$ as the edges of the minimum spanning forest we have currently found. During the execution of the algorithm, we gradually add edges to $E'$; define a **connected block** to represent a point set $V'\subseteq V$ such that any two points $u$, $v$ in this point set are connected (mutually reachable) in the subgraph formed by the edges in $E'$.
2.  Define the **minimum edge** of a connected block as the edge with the smallest weight among the edges connecting it to other connected blocks.

Initially, $E'=\varnothing$, and each point is its own connected block:

1.  Compute which connected block each point belongs to. Set each connected block to "no minimum edge".
2.  Traverse each edge $(u, v)$; if $u$ and $v$ are not in the same connected block, use the edge weight of this edge to update the minimum edges of the connected blocks where $u$ and $v$ are located respectively.
3.  If all connected blocks have no minimum edge, exit the program; the $E'$ at this time is the edge set of the minimum spanning forest of the original graph. Otherwise, add the minimum edge of each connected block that has a minimum edge to $E'$, and return to the first step.

Below we give an example through a dynamic figure (figure sourced from [Wikipedia](https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm)):

![eg](./images/mst-1.apng)

When the original graph is connected, the number of connected blocks decreases by at least half in each iteration, so the algorithm iterates no more than $O(\log V)$ times; when the original graph is disconnected it is equivalent to multiple subproblems, so the algorithm complexity is $O(E\log V)$. The pseudocode of the algorithm is given: (modified from [Wikipedia](https://en.wikipedia.org/wiki/Bor%C5%AFvka%27s_algorithm))

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{A graph }G\text{ whose edges have distinct weights. } \\
2 &  \textbf{Output. } \text{The minimum spanning forest of }G .  \\
3 &  \textbf{Method. }  \\
4 & \text{Initialize a forest }F\text{ to be a set of one-vertex trees} \\
5 &  \textbf{while } \text{True} \\
6 &  \qquad \text{Find the components of }F\text{ and label each vertex of }G\text{ by its component } \\
7 &  \qquad \text{Initialize the cheapest edge for each component to "None"} \\
8 &  \qquad  \textbf{for } \text{each edge }(u, v)\text{ of }G  \\
9 &  \qquad\qquad  \textbf{if }  u\text{ and }v\text{ have different component labels} \\
10 &  \qquad\qquad\qquad  \textbf{if }  (u, v)\text{ is cheaper than the cheapest edge for the component of }u  \\
11 &  \qquad\qquad\qquad\qquad\text{ Set }(u, v)\text{ as the cheapest edge for the component of }u \\
12 &  \qquad\qquad\qquad  \textbf{if }  (u, v)\text{ is cheaper than the cheapest edge for the component of }v  \\
13 &  \qquad\qquad\qquad\qquad\text{ Set }(u, v)\text{ as the cheapest edge for the component of }v  \\
14 &  \qquad  \textbf{if }\text{ all components'cheapest edges are "None"} \\
15 &  \qquad\qquad  \textbf{return }  F \\
16 &  \qquad  \textbf{for }\text{ each component whose cheapest edge is not "None"} \\
17 &  \qquad\qquad\text{ Add its cheapest edge to }F \\
\end{array}
$$

Note that comparing edges usually requires a secondary key (e.g. sorting by number), so that when edge weights are the same, the ordering of edges can be distinguished.

## Exercises

-   [「HAOI2006」Clever monkeys](https://www.luogu.com.cn/problem/P2504)
-   [「SCOI2005」Busy city](https://loj.ac/problem/2149)

## Uniqueness of the minimum spanning tree

Consider the uniqueness of the minimum spanning tree. If an edge is **not in the edge set of the minimum spanning tree**, and it can replace another edge with **the same weight and in the edge set of the minimum spanning tree**, then this minimum spanning tree is not unique.

For the Kruskal algorithm, we only need to compute how many edges of the current weight can be placed and how many were actually placed; if these two values differ, then it means these edges form a cycle with the previous edges (this cycle has at least two edges of the current weight, otherwise according to the disjoint set union this edge could not be placed), i.e. the minimum spanning tree is not unique.

To find edges with the same weight as the current edge, we only need to record head and tail pointers, and use a monotonic queue to elegantly solve this problem in $O(\alpha(m))$ (m is the number of edges) time complexity (basically the same time as the original algorithm).

??? note "Example problem: [POJ 1679](http://poj.org/problem?id=1679)"
    ```cpp
    --8<-- "docs/graph/code/mst/mst_1.cpp"
    ```

## Second-best spanning tree

### Non-strict second-best spanning tree

#### Definition

In an undirected graph, the spanning tree with the minimum sum of edge weights that satisfies its sum of edge weights being **greater than or equal to** the sum of edge weights of the minimum spanning tree.

#### Solution method

-   Find the minimum spanning tree $T$ of the undirected graph, and let its sum of weights be $M$
-   Traverse each unselected edge $e = (u,v,w)$, find the edge $e' = (s,t,w')$ with the largest edge weight on the path from $u$ to $v$ in $T$; then replacing $e'$ with $e$ in $T$ yields a spanning tree $T'$ with sum of weights $M' = M + w - w'$.
-   Take the minimum value over all answers $M'$ obtained by replacement

How to find the maximum edge weight on the path from $u,v$?

We can maintain it using binary lifting, preprocessing the $2^i$-th ancestor of each node and the maximum edge weight on the path to its $2^i$-th ancestor, so that it can be directly obtained during the process of finding the LCA by binary lifting.

### Strict second-best spanning tree

#### Definition

In an undirected graph, the spanning tree with the minimum sum of edge weights that satisfies its sum of edge weights being **strictly greater than** the sum of edge weights of the minimum spanning tree.

#### Solution method

Consider the process of solving the non-strict second-best spanning tree just now; why is the obtained solution non-strict?

Because the minimum spanning tree guarantees that the maximum edge weight on the path from $u$ to $v$ in the spanning tree is definitely **not greater than** the maximum edge weight of other paths from $u$ to $v$. In other words, when the weight of the edge we use for replacement equals the weight of the replaced edge in the original spanning tree, the obtained second-best spanning tree is non-strict.

The solution is very natural: while we maintain the maximum edge weight on the path to the $2^i$-th ancestor, we also maintain the **strict second-largest edge weight**; when the weight of the edge used for replacement equals the maximum edge weight on the original path in the spanning tree, we replace using the strict second-largest value.

This process can be solved using binary lifting, with complexity $O(m \log m)$.

??? note "Code implementation"
    ```cpp
    #include <algorithm>
    #include <iostream>
    
    constexpr int INF = 0x3fffffff;
    constexpr long long INF64 = 0x3fffffffffffffffLL;
    
    struct Edge {
      int u, v, val;
    
      bool operator<(const Edge &other) const { return val < other.val; }
    };
    
    Edge e[300010];
    bool used[300010];
    
    int n, m;
    long long sum;
    
    class Tr {
     private:
      struct Edge {
        int to, nxt, val;
      } e[600010];
    
      int cnt, head[100010];
    
      int pnt[100010][22];
      int dpth[100010];
      // the edge with the largest edge weight on the path to the ancestor
      int maxx[100010][22];
      // the edge with the second-largest edge weight on the path to the ancestor, -INF if it does not exist
      int minn[100010][22];
    
     public:
      void addedge(int u, int v, int val) {
        e[++cnt] = Edge{v, head[u], val};
        head[u] = cnt;
      }
    
      void insedge(int u, int v, int val) {
        addedge(u, v, val);
        addedge(v, u, val);
      }
    
      void dfs(int now, int fa) {
        dpth[now] = dpth[fa] + 1;
        pnt[now][0] = fa;
        minn[now][0] = -INF;
        for (int i = 1; (1 << i) <= dpth[now]; i++) {
          pnt[now][i] = pnt[pnt[now][i - 1]][i - 1];
          int kk[4] = {maxx[now][i - 1], maxx[pnt[now][i - 1]][i - 1],
                       minn[now][i - 1], minn[pnt[now][i - 1]][i - 1]};
          // take the maximum value among the four values
          std::sort(kk, kk + 4);
          maxx[now][i] = kk[3];
          // take the strict second-largest value
          int ptr = 2;
          while (ptr >= 0 && kk[ptr] == kk[3]) ptr--;
          minn[now][i] = (ptr == -1 ? -INF : kk[ptr]);
        }
    
        for (int i = head[now]; i; i = e[i].nxt) {
          if (e[i].to != fa) {
            maxx[e[i].to][0] = e[i].val;
            dfs(e[i].to, now);
          }
        }
      }
    
      int lca(int a, int b) {
        if (dpth[a] < dpth[b]) std::swap(a, b);
    
        for (int i = 21; i >= 0; i--)
          if (dpth[pnt[a][i]] >= dpth[b]) a = pnt[a][i];
    
        if (a == b) return a;
    
        for (int i = 21; i >= 0; i--) {
          if (pnt[a][i] != pnt[b][i]) {
            a = pnt[a][i];
            b = pnt[b][i];
          }
        }
        return pnt[a][0];
      }
    
      int query(int a, int b, int val) {
        int res = -INF;
        for (int i = 21; i >= 0; i--) {
          if (dpth[pnt[a][i]] >= dpth[b]) {
            if (val != maxx[a][i])
              res = std::max(res, maxx[a][i]);
            else
              res = std::max(res, minn[a][i]);
            a = pnt[a][i];
          }
        }
        return res;
      }
    } tr;
    
    int fa[100010];
    
    int find(int x) { return fa[x] == x ? x : fa[x] = find(fa[x]); }
    
    void Kruskal() {
      int tot = 0;
      std::sort(e + 1, e + m + 1);
      for (int i = 1; i <= n; i++) fa[i] = i;
    
      for (int i = 1; i <= m; i++) {
        int a = find(e[i].u);
        int b = find(e[i].v);
        if (a != b) {
          fa[a] = b;
          tot++;
          tr.insedge(e[i].u, e[i].v, e[i].val);
          sum += e[i].val;
          used[i] = true;
        }
        if (tot == n - 1) break;
      }
    }
    
    int main() {
      std::ios::sync_with_stdio(false);
      std::cin.tie(nullptr);
    
      std::cin >> n >> m;
      for (int i = 1; i <= m; i++) {
        int u, v, val;
        std::cin >> u >> v >> val;
        e[i] = Edge{u, v, val};
      }
    
      Kruskal();
      long long ans = INF64;
      tr.dfs(1, 0);
    
      for (int i = 1; i <= m; i++) {
        if (!used[i]) {
          int _lca = tr.lca(e[i].u, e[i].v);
          // find the maximum edge weight on the path that is not equal to e[i].val
          long long tmpa = tr.query(e[i].u, _lca, e[i].val);
          long long tmpb = tr.query(e[i].v, _lca, e[i].val);
          // such an edge may not exist, only update the answer when such an edge exists
          if (std::max(tmpa, tmpb) > -INF)
            ans = std::min(ans, sum - std::max(tmpa, tmpb) + e[i].val);
        }
      }
      // output -1 when the second-best spanning tree does not exist
      std::cout << (ans == INF64 ? -1 : ans) << '\n';
      return 0;
    }
    ```

## Bottleneck spanning tree

### Definition

The bottleneck spanning tree of an undirected graph $G$ is a spanning tree whose maximum edge weight is the smallest among all spanning trees of $G$.

### Properties

**The minimum spanning tree is a sufficient but not necessary condition for a bottleneck spanning tree.** That is, the minimum spanning tree is definitely a bottleneck spanning tree, while a bottleneck spanning tree is not necessarily a minimum spanning tree.

Regarding the proposition that the minimum spanning tree is definitely a bottleneck spanning tree, it can be proved by contradiction: We set the maximum edge weight in the minimum spanning tree to be $w$; if the minimum spanning tree is not a bottleneck spanning tree, then all edge weights of the bottleneck spanning tree are less than $w$; we only need to delete the longest edge in the original minimum spanning tree, and use an edge in the bottleneck spanning tree to connect the two trees formed after deleting the edge; the new spanning tree obtained must have a smaller sum of weights than the original minimum spanning tree, which produces a contradiction.

### Example problem

???+ note "POJ 2395 Out of Hay"
    Given n farms and m edges, farms are numbered 1 to n; now a person wants to start from the farm numbered 1 and go to the other farms; find the maximum weight of water he needs to carry during this journey; note that each time he reaches a farm, he can replenish water, and the total path length should be minimized.
    What the problem requires is exactly the maximum edge of the bottleneck tree, which can be solved by finding the minimum spanning tree.

## Minimum bottleneck path

### Definition

The minimum bottleneck path from x to y in an undirected graph $G$ is a class of simple paths satisfying that the maximum edge weight on this path is the smallest among all simple paths from x to y.

### Properties

According to the definition of the minimum spanning tree, the maximum edge weight on the minimum bottleneck path from x to y equals the maximum edge weight on the path from x to y on the minimum spanning tree. Although the minimum spanning tree is not unique, the maximum edge weight on the path from x to y is the same for every minimum spanning tree and is the minimum value. That is to say, the path from x to y on every minimum spanning tree is a minimum bottleneck path.

However, it is not the case that for every minimum bottleneck path there exists a minimum spanning tree such that it is the simple path from x to y on the tree.

For example, the figure below:

![](./images/mst5.png)

The minimum bottleneck paths from 1 to 4 obviously have the following two: 1-2-3-4. 1-3-4.

However, 1-2 will not appear on any minimum spanning tree.

### Applications

Since the minimum bottleneck path is not unique, in general the maximum edge weight on the minimum bottleneck path is queried.

That is to say, we need to find the max on the chain of the minimum spanning tree.

Both binary lifting and heavy-light decomposition can solve this; we do not expand on it here.

## Kruskal reconstruction tree

### Definition

During the process of running Kruskal, we add several edges from small to large. Now we still follow this order.

First, create $n$ sets, each set having exactly one node, with node weight $0$.

Each edge addition merges two sets; we can create a new point, with node weight being the edge weight of the added edge, and at the same time set the root nodes of the two sets as the left child and right child of the newly created point respectively. Then we merge the two sets and the newly created point into one set. Set the newly created point as the root.

It is not hard to find that after $n-1$ rounds we obtain a binary tree with exactly $n$ leaves, and each non-leaf node has exactly two children. This tree is called the Kruskal reconstruction tree.

For example:

![](./images/mst5.png)

The Kruskal reconstruction tree of this graph is as follows:

![](./images/mst6.png)

### Properties

It is not hard to find that the minimum of the maximum edge weight on all simple paths between two points in the original graph = the maximum value on the simple path between two points on the minimum spanning tree = the weight of the LCA of the two points on the Kruskal reconstruction tree.

That is to say, all points $y$ whose minimum of the maximum edge weight on the simple path to point $x$ is $\leq val$ are within some subtree on the Kruskal reconstruction tree, and are exactly all the leaf nodes of that subtree.

We find on the Kruskal reconstruction tree the shallowest node on the path from $x$ to the root whose weight is $\leq val$. Obviously this is the root node of the subtree where all nodes satisfying the condition are located.

If we need to find the maximum of the minimum edge weight on all simple paths between two points in the original graph, then during the process of running Kruskal we add edges in order of edge weight from large to small.

??? note "[「LOJ 137」Minimum bottleneck path, enhanced version](https://loj.ac/problem/137)"
    ```cpp
    --8<-- "docs/graph/code/mst/mst_2.cpp"
    ```

??? note "[NOI 2018 Return trip](https://uoj.ac/problem/393)"
    First preprocess the shortest path from each point to the root node.
    
    We construct the maximum spanning tree according to altitude. Obviously, the nodes reachable in each query are the nodes on the path with the query point in the maximum spanning tree whose minimum edge weight $> p$.
    
    According to the properties of the Kruskal reconstruction tree, these nodes are all within one subtree and are all its leaf nodes.
    
    That is to say, we only need to find the min of the leaf weights of each subtree on the Kruskal reconstruction tree to support subtree queries.
    
    The root node of the query can be found using binary lifting on the Kruskal reconstruction tree.
    
    The time complexity is $O((n+m+Q) \log n)$.
