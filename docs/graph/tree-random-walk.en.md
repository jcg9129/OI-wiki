Given a rooted tree, there is a coin on a certain node of the tree; at a certain moment the coin will move to an adjacent node with equal probability; find the expected distance for the coin to move to an adjacent node.

## Definitions needed

-   $T=(V,E)$: the tree under discussion
-   $d(u)$: the degree of node $u$
-   $w(u,v)$: the edge weight of the edge between node $u$ and node $v$
-   $p_u$: the parent node of node $u$
-   $\textit{root}$: the root node of the tree
-   $\textit{son}_u$: the set of child nodes of node $u$
-   $\textit{sibling}_u$: the set of sibling nodes of node $u$

## Expected distance of walking to the parent node

Let $f(u)$ represent the expected distance for node $u$ to walk to its parent node $p_u$; then we have:

$$
f(u) = \cfrac{w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v) + f(u))}{d(u)}
$$

The first half of the numerator represents walking directly to the parent node, and the second half represents first walking to a child node and then walking back from the child node and then walking to the parent node; the denominator $d(u)$ represents that the probability of walking from node $u$ to any of its adjacent points is the same.

Simplified as follows:

$$
\begin{aligned}
    f(u) &= \cfrac{w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v) + f(u))}{d(u)} \\
         &= \cfrac{w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v)) + (d(u)-1)f(u)}{d(u)} \\
         &= w(u,p_u) + \sum\limits_{v \in \textit{son}_u}(w(u,v) + f(v)) \\
         &= \sum\limits_{(u,t) \in E}w(u,t) + \sum\limits_{v \in \textit{son}_u}f(v)
\end{aligned}
$$

For a leaf node $l$, the initial state is $f(l) = w(p_l, l)$.

When all edge weights on the tree are $1$, the above formula can be simplified to:

$$
f(u) = d(u) + \sum\limits_{v \in \textit{son}_u}f(v)
$$

That is, the sum of degrees of all nodes in the subtree of $u$, i.e. twice the size of the subtree of $u$ minus $1$ (each node has one and only one edge connecting to its parent; except that the edge between $u$ and $p_u$ contributes only $1$ point of degree, each edge produces $2$ points of degree contribution).

## Expected distance of walking to a child node

Let $g(u)$ represent the expected distance for node $p_u$ to walk to its child node $u$; then we have:

$$
g(u) = \cfrac{w(p_u,u) + \left(w(p_u,p_{p_u})+g(p_u)+g(u)\right) + \sum\limits_{s \in \textit{sibling}_u}(w(p_u,s)+f(s)+g(u))}{d(p_u)}
$$

The first part of the numerator represents walking directly to the child node $u$, the second part represents first walking to the parent node and then walking back from the parent node and then walking to node $u$, and the third part represents first walking to a sibling node of node $u$ and then walking back from it and then walking to node $u$; the denominator $d(p_u)$ represents that the probability of walking from node $p_u$ to any of its adjacent points is the same.

Simplified as follows:

$$
\begin{aligned}
    g(u) &= \cfrac{w(p_u,u) + \left(w(p_u,p_{p_u})+g(p_u)+g(u)\right) + \sum\limits_{s \in \textit{sibling}_u}(w(p_u,s)+f(s)+g(u))}{d(p_u)} \\
         &= \cfrac{w(p_u,u) + w(p_u,p_{p_u}) + g(p_u) + \sum\limits_{s \in \textit{sibling}_u}\left(w(p_u,s)+f(s)\right)+(d(p_u)-1)g(u)}{d(p_u)} \\
         &= w(p_u,u) + w(p_u,p_{p_u}) + g(p_u) + \sum\limits_{s \in \textit{sibling}_u}(w(p_u,s)+f(s)) \\
         &= \sum\limits_{(p_u,t) \in E}w(p_u,t) + g(p_u) + \sum\limits_{s \in \textit{sibling}_u}f(s) \\
         &= \sum\limits_{(p_u,t) \in E}w(p_u,t) + g(p_u) + \left(f(p_u)-\sum\limits_{(p_u,t) \in E}w(p_u,t)-f(u)\right) \\
         &= g(p_u) + f(p_u) - f(u)
\end{aligned}
$$

The initial state is $g(\text{root}) = 0$.

## Code implementation (taking an unweighted tree as an example)

```cpp
vector<int> G[MAXN];

void dfs1(int u, int p) {
  f[u] = G[u].size();
  for (auto v : G[u]) {
    if (v == p) continue;
    dfs1(v, u);
    f[u] += f[v];
  }
}

void dfs2(int u, int p) {
  if (u != root) g[u] = g[p] + f[p] - f[u];
  for (auto v : G[u]) {
    if (v == p) continue;
    dfs2(v, u);
  }
}
```
