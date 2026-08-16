author: Ir1d, sshwy, GavinZhengOI, Planet6174, ouuan, Marcythm, ylxmf2005, 0xis-cn

Related reading: [biconnected components](./bcc.md)

For more rigorous definitions of cut vertices and bridges, see [graph-theory related concepts](./concept.md).

## Cut vertices

> For an undirected graph, if deleting a point increases the number of maximal connected components of this graph, then this point is a cut vertex (also called a cut point) of this graph.

### Process

If we try to delete each point and judge the connectivity of this graph, then the complexity is especially high. So we need to introduce a commonly-used algorithm: Tarjan.

First, let's put up a graph:

![](./images/cut1.svg)

It is easy to see that the cut vertex is 2, and this graph has only this one cut vertex.

First, we stamp it with timestamps (the order of visiting) according to DFS order.

![](./images/cut2.svg)

This information is stored by us in an array called `dfn`.

We also need another array `low`, used to store the minimum timestamp reachable without passing through its parent.

For example, `low[2]` is 1, and `low[5]` and `low[6]` are 3.

Then we start DFS; the basis on which we judge whether a certain point is a cut vertex is: for a certain vertex $u$, if there exists at least one vertex $v$ (a child of $u$) such that $low_v \geq dfn_u$, i.e. it cannot return to an ancestor, then point $u$ is a cut vertex.

This basis is uniquely inapplicable to the starting point of the search, which needs special consideration: if this point is not a cut vertex, then other paths can also reach all nodes, so from the starting point we only "searched down once", i.e. there is only one child node inside the search tree. If there are two or more children inside the search tree, then it must be a cut vertex (imagine searching from 2 in the figure above; there should be two child nodes inside the search tree: 3 or 4, and 5 or 6). If there is only one child, then deleting it has no effect at all. For example, in the graph below, a cycle is formed here.

![](./images/cut3.svg)

When we visit the children of 1, suppose we first DFS to 2, then mark it used, then recurse down, arriving at 4, and 4 arrives at 3; when the recursion backtracks, it will find that 3 has already been visited, so it is not a cut vertex.

The pseudocode for updating `low` is as follows:

$$
\begin{array}{ll}
1 & \textbf{if } v \text{ is a son of } u \\
2 & \qquad \text{low}_u = \min(\text{low}_u, \text{low}_v) \\
3 & \textbf{else} \\
4 & \qquad \text{low}_u = \min(\text{low}_u, \text{dfn}_v) \\
\end{array}
$$

### Example problem

[Luogu P3388 【Template】Cut Vertices (Cut Points)](https://www.luogu.com.cn/problem/P3388)

??? note "Example problem code"
    ```cpp
    --8<-- "docs/graph/code/cut/cut_1.cpp"
    ```

## Cut edges (without multiple edges)

Similar to cut vertices, called bridges.

> For an undirected graph, if deleting an edge increases the number of connected components in the graph, then this edge is called a bridge or a cut edge. Rigorously, that is: suppose there is a connected graph $G=\{V,E\}$, and $e$ is one of its edges (i.e. $e \in E$); if $G-e$ is disconnected, then edge $e$ is a cut edge (bridge) of the graph $G$.

For example, in the figure below,

![Cut-edge example figure](./images/bridge1.svg)

the red edge is the cut edge.

### Process

Similar to cut vertices, we only need to change one place: $low_v>dfn_u$ suffices, and there is no need to consider the root-node problem.

Cut edges have nothing to do with whether it is a root node; originally, when we found cut vertices, it meant point $v$ cannot return to an ancestor node (including the parent node) without passing through the parent node $u$, so vertex $u$ is a cut vertex. If $low_v=dfn_u$ it means it can still return to the parent node; if vertex $v$ cannot return to an ancestor and has no other path back to the parent, then the edge $u-v$ is a cut edge.

### Implementation

The following code implements finding cut edges of an undirected graph **without multiple edges**, where, when `isbridge[x]` is true, `(father[x],x)` is a cut edge.

=== "C++"
    ```cpp
    int low[MAXN], dfn[MAXN], idx;
    bool isbridge[MAXN];
    vector<int> G[MAXN];
    int cnt_bridge;
    int father[MAXN];
    
    void tarjan(int u, int fa) {
      father[u] = fa;
      low[u] = dfn[u] = ++idx;
      for (const auto &v : G[u]) {
        if (!dfn[v]) {
          tarjan(v, u);
          low[u] = min(low[u], low[v]);
          if (low[v] > dfn[u]) {
            isbridge[v] = true;
            ++cnt_bridge;
          }
        } else if (v != fa) {
          low[u] = min(low[u], dfn[v]);
        }
      }
    }
    ```

=== "Python"
    ```python
    low = [0] * MAXN
    dfn = [0] * MAXN
    idx = 0
    isbridge = [False] * MAXN
    G = [[0 for i in range(MAXN)] for j in range(MAXN)]
    cnt_bridge = 0
    father = [0] * MAXN
    
    
    def tarjan(u, fa):
        father[u] = fa
        idx = idx + 1
        low[u] = dfn[u] = idx
        for i in range(0, len(G[u])):
            v = G[u][i]
            if dfn[v] == False:
                tarjan(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > dfn[u]:
                    isbridge[v] = True
                    cnt_bridge = cnt_bridge + 1
            elif v != fa:
                low[u] = min(low[u], dfn[v])
    ```

## Cut edges (with multiple edges)

However, the above approach without multiple edges is problematic on an undirected graph with multiple edges.

Because there may be more than one edge between two nodes, in which case none of them will be a bridge.

### Process

One idea is to change the parameter `fa` to the number of the edge just traversed (the number of each edge being consistent), i.e. change "do not update with the parent node" to "do not update with the incoming edge".

Another simpler idea is to set up a mark to judge whether an edge has already reached the parent node; after marking, when the parent node is visited again, update normally.

The following code implements finding cut edges of an undirected graph that may **have multiple edges**.

=== "C++"
    ```cpp
    int low[MAXN], dfn[MAXN], idx;
    bool isbridge[MAXN];
    vector<int> G[MAXN];
    int cnt_bridge;
    int father[MAXN];
    
    void tarjan(int u, int fa) {
      bool flag = false;
      father[u] = fa;
      low[u] = dfn[u] = ++idx;
      for (const auto &v : G[u]) {
        if (!dfn[v]) {
          tarjan(v, u);
          low[u] = min(low[u], low[v]);
          if (low[v] > dfn[u]) {
            isbridge[v] = true;
            ++cnt_bridge;
          }
        } else {
          if (v != fa || flag)
            low[u] = min(low[u], dfn[v]);
          else
            flag = true;
        }
      }
    }
    ```

## Practice

-   [P3388 【Template】Cut Vertices (Cut Points)](https://www.luogu.com.cn/problem/P3388)
-   [POJ2117 Electricity](http://poj.org/problem?id=2117)
-   [HDU4738 Caocao's Bridges](https://acm.hdu.edu.cn/showproblem.php?pid=4738)
-   [HDU2460 Network](https://acm.hdu.edu.cn/showproblem.php?pid=2460)
-   [POJ1523 SPF](http://poj.org/problem?id=1523)

Tarjan's algorithm has many other uses; common ones include finding strongly connected components, contraction, and the use of finding 2-SAT, etc.
