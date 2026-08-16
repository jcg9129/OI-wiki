author: GoodCoder666, Ir1d, Marcythm, ouuan, hsfzLZH1, Xeonacid, greyqz, Chrogeek, ftxj, sshwy, LuoshuiTianyi, hyp1231, sun2snow, Desmos666-xh

## Introduction

Tree-path decomposition is used to split a tree into several chains, so as to maintain information of paths on the tree.

Specifically, decompose the whole tree into several chains, making them combine into a linear structure, and then use other data structures to maintain the information.

**Tree-path decomposition** (tree decomposition / chain decomposition) has multiple forms, such as **heavy-path decomposition**, **long-path decomposition**, and the decomposition used for the Link/Cut Tree (sometimes called "real-chain decomposition"). In most cases (when not specifically noted), "tree-path decomposition" refers to "heavy-path decomposition".

Heavy-path decomposition can divide any path on the tree into no more than $O(\log n)$ consecutive chains, and the points on each chain have distinct depths (i.e. it is a bottom-up chain, and the LCA of all points on the chain is one endpoint of the chain).

Heavy-path decomposition can also guarantee that the nodes on each divided chain have consecutive DFS order, so it is convenient to use some data structures that maintain sequences (such as a segment tree) to maintain information of paths on the tree. For example:

1.  Modify the values of all points **on the path between two points on the tree**.
2.  Query the **sum/extremum/other (information that can be maintained with a data structure on a sequence and is convenient to merge)** of node weights **on the path between two points on the tree**.

Besides cooperating with data structures to maintain tree-path information, tree decomposition can also be used to find the LCA in $O(\log n)$ (with a relatively small constant factor). In some problems, its properties can also be flexibly used with tree decomposition.

## Heavy-path decomposition

We give some definitions:

Define the **heavy child** as the child with the largest subtree among the children. If there are multiple children with the largest subtree, take one of them. If there is no child, then there is no heavy child.

Define the **light children** as all the remaining children.

The edge from this node to the heavy child is a **heavy edge**.

The edge to other light children is a **light edge**.

Several head-to-tail connected heavy edges constitute a **heavy chain**.

Regarding solitary nodes as heavy chains too, the whole tree is decomposed into several heavy chains.

As shown:

![HLD](./images/hld.png)

## Implementation

The implementation of tree decomposition is divided into two DFS processes. The pseudocode is as follows:

The first DFS records the parent node ($\textit{father}$), depth ($\textit{depth}$), subtree size ($\textit{size}$), and heavy child ($\textit{hson}$) of each node.

$$
\begin{array}{l}
\text{TREE-BUILD }(u,\textit{dep}) \\
\begin{array}{ll}
1 & u.\textit{hson}\gets 0 \\
2 & u.\textit{hson}.\textit{size}\gets 0 \\
3 & u.\textit{depth}\gets \textit{dep} \\
4 & u.\textit{size}\gets 1 \\
5 & \textbf{for }\text{each son }v\text{ of }u \\
6 & \qquad u.\textit{size}\gets u.\textit{size} + \text{TREE-BUILD }(v,\textit{dep}+1) \\
7 & \qquad v.\textit{father}\gets u \\
8 & \qquad \textbf{if }v.\textit{size}> u.\textit{hson}.\textit{size} \\
9 & \qquad \qquad u.\textit{hson}\gets v \\
10 & \textbf{return } u.\textit{size}
\end{array}
\end{array}
$$

The second DFS records the chain top of the chain it is in ($\textit{top}$, which should be initialized to the node itself), the DFS order when traversing heavy edges first ($\textit{dfn}$), and the node number corresponding to the DFS order ($\textit{rank}$).

$$
\begin{array}{l}
\text{TREE-DECOMPOSITION }(u,\textit{top}) \\
\begin{array}{ll}
1 & u.\textit{top}\gets \textit{top} \\
2 & \textit{tot}\gets \textit{tot}+1\\
3 & u.\textit{dfn}\gets \textit{tot} \\
4 & \textit{rank}(\textit{tot})\gets u \\
5 & \textbf{if }u.\textit{hson}\text{ is not }0 \\
6 & \qquad \text{TREE-DECOMPOSITION }(u.\textit{hson},\textit{top}) \\
7 & \qquad \textbf{for }\text{each son }v\text{ of }u \\
8 & \qquad \qquad \textbf{if }v\text{ is not }u.\textit{hson} \\
9 & \qquad \qquad \qquad \text{TREE-DECOMPOSITION }(v,v) 
\end{array}
\end{array}
$$

The following is the code implementation.

We first give some definitions:

-   $\operatorname{fa}(x)$ denotes the parent of node $x$ on the tree.
-   $\operatorname{dep}(x)$ denotes the depth of node $x$ on the tree.
-   $\operatorname{siz}(x)$ denotes the number of nodes in the subtree of node $x$.
-   $\operatorname{son}(x)$ denotes the **heavy child** of node $x$.
-   $\operatorname{top}(x)$ denotes the top node (smallest depth) of the **heavy chain** where node $x$ is located.
-   $\operatorname{dfn}(x)$ denotes the **DFS order** of node $x$, which is also its number in the segment tree.
-   $\operatorname{rnk}(x)$ denotes the node number corresponding to the DFS order, with $\operatorname{rnk}(\operatorname{dfn}(x))=x$.

We perform two DFS passes to preprocess these values, where the first DFS finds $\operatorname{fa}(x)$, $\operatorname{dep}(x)$, $\operatorname{siz}(x)$, $\operatorname{son}(x)$, and the second DFS finds $\operatorname{top}(x)$, $\operatorname{dfn}(x)$, $\operatorname{rnk}(x)$.

```cpp
void dfs1(int u, int f) {
  fa[u] = f, dep[u] = dep[f] + 1, siz[u] = 1;
  for (auto v : G[u]) {
    if (v == f) continue;
    dfs1(v, u);
    siz[u] += siz[v];
    if (siz[v] > siz[son[u]]) son[u] = v;
  }
}

void dfs2(int u, int ftop) {
  top[u] = ftop, dfn[u] = ++idx, rnk[idx] = u;
  if (son[u]) dfs2(son[u], ftop);
  for (auto v : G[u])
    if (v != son[u] && v != fa[u]) dfs2(v, v);
}
```

## Properties of heavy-path decomposition

**Each node on the tree belongs to and only belongs to one heavy chain.**

The node at the head of a heavy chain must not be a heavy child (because the node at the head of a heavy chain is either the root or a light child of its parent node).

All the heavy chains **completely decompose** the whole tree.

When traversing **heavy edges first** during decomposition, in the final DFS order of the tree, the DFS order within a heavy chain is consecutive. The sequence sorted by DFN is the chain after decomposition.

The DFS order within a subtree is consecutive.

We can find that when we go down through a **light edge**, the size of the subtree we are in is at least divided by two.

Therefore, for any path on the tree, split it into going down from the [LCA](./lca.md) to both sides separately, each side going down at most $O(\log n)$ times, so each path on the tree can be split into no more than $O(\log n)$ heavy chains.

??? info "How to break tree decomposition in a justified way"
    Generally, the $O(\log n)$ constant of tree decomposition is not fully run and hard to break; to break it, one can only build a binary tree with low depth.
    
    So we can consider a compromise scheme.
    
    We build a binary tree with $\sqrt{n}$ nodes. For each edge from a node to its child, we replace it with a chain of length $\sqrt{n}$.
    
    In this way we can push the number of light/heavy chain switches for a random query to an average of $\frac{\log n}{2}$ times, while having a depth of $O(\sqrt{n} \log n)$.
    
    Adding several random leaves seemingly can break tree decomposition. But since the constant of tree decomposition is small, it may not be broken.

## Common applications

### Maintaining on a path

Using tree-path decomposition to find the sum of weights on the path between two points on the tree, the pseudocode is as follows:

$$
\begin{array}{l}
\text{TREE-PATH-SUM }(u,v) \\
\begin{array}{ll}
1 & \textit{tot}\gets 0 \\
2 & \textbf{while }u.\textit{top}\text{ is not }v.\textit{top} \\
3 & \qquad \textbf{if }u.\textit{top}.\textit{depth}< v.\textit{top}.\textit{depth} \\
4 & \qquad \qquad \text{SWAP}(u, v) \\
5 & \qquad \textit{tot}\gets \textit{tot} + \text{sum of values between }u\text{ and }u.\textit{top} \\
6 & \qquad u\gets u.\textit{top}.\textit{father} \\
7 & \textit{tot}\gets \textit{tot} + \text{sum of values between }u\text{ and }v \\
8 & \textbf{return } \textit{tot} 
\end{array}
\end{array}
$$

The DFS order on a chain is consecutive, and can be maintained with a segment tree or Fenwick tree.

Each time choose the chain with the larger depth to jump up, until the two points are on the same chain.

The same chain-jumping structure applies to maintaining and counting other information on a path.

### Maintaining on a subtree

Sometimes it is required to maintain information on a subtree, for example increasing the weights of all nodes of the subtree rooted at $x$ by $v$.

During the DFS search, the DFS order of the nodes in a subtree is consecutive.

Each node records bottom, denoting the node at the end of the consecutive interval of the subtree it is in.

In this way the subtree information is converted into information of a consecutive interval.

### Finding the lowest common ancestor

Continually jump up heavy chains; when jumping to the same heavy chain, the node with the smaller depth is the LCA.

When jumping up heavy chains, we need to first jump the one whose heavy-chain top has the larger depth.

Reference code:

```cpp
int lca(int u, int v) {
  while (top[u] != top[v]) {
    if (dep[top[u]] > dep[top[v]])
      u = fa[top[u]];
    else
      v = fa[top[v]];
  }
  return dep[u] > dep[v] ? v : u;
}
```

### Rerooting operation

Consider a new kind of problem: besides the basic operations supported by tree-path decomposition, add a rerooting operation.

Since the information maintained by tree-path decomposition is static and does not support dynamic modification. At the same time, it is impossible to re-preprocess the information each time after rerooting, as the complexity is too high. So, we need to fully utilize the previously-obtained information to help solve the rerooting operation.

For path modification and query operations, since the simple path between two points on the tree is unique, it will not change, and the handling is the same as normal.

For subtree modification and query operations, the general idea is to map the subtree after rerooting to the original subtree. This requires a case discussion of the relative positions of the root node of the operated subtree, the root node of the whole tree after rerooting, and the root node of the original tree. For specific details see the [example problem later](./hld.md#loj-139-树链剖分).

## Example problems

This article shows how to apply heavy-path decomposition through example problems. First is a template problem.

???+ example "[「ZJOI2008」Tree Statistics](https://loj.ac/problem/10138)"
    On a static tree with $n$ nodes, where nodes have weights, perform three kinds of operations, $q$ times in total:
    
    1.  Modify the weight of a single node;
    2.  Query the maximum weight on the path from $u$ to $v$;
    3.  Query the sum of weights on the path from $u$ to $v$.
    
    It is guaranteed that $1\le n\le 30000$, $0\le q\le 200000$.

??? note "Solution"
    According to the problem and the properties described above, the segment tree needs to maintain three kinds of operations:
    
    1.  Single-point modification;
    2.  Interval query maximum;
    3.  Interval query sum.
    
    Single-point modification is easy to implement.
    
    Since the DFS order of a subtree is consecutive (whether or not tree decomposition is done), modifying the subtree of a node only needs to modify this consecutive DFS-order interval.
    
    The problem is how to modify/query the path between two nodes.
    
    Consider how we use **binary lifting to find the LCA**. First we **lift the two nodes to the same height, and then jump the two nodes up together**. For tree-path decomposition we can also use this idea.
    
    In the process of jumping up, if the current node is on a heavy chain, jump up to the top of the heavy chain; if the current node is not on a heavy chain, jump up one node. Repeat until the two nodes are the same. Update/query the interval information along the way.
    
    For each query, at most $O(\log n)$ heavy chains are passed, and the complexity of the segment tree on each heavy chain is $O(\log n)$, so the total time complexity is $O(n\log n+q\log^2 n)$. In fact, it is hard for the number of heavy chains to reach $O(\log n)$ (a complete binary tree can push it to the limit), so tree decomposition generally has a relatively small constant factor.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_1.cpp"
    ```

Then is a heavy-path decomposition template problem with a rerooting operation.

<a id="loj-139-树链剖分"></a>

???+ example "[LOJ 139. Tree-Path Decomposition](https://loj.ac/p/139)"
    Given a tree with $n$ nodes (initial root node is $1$), required to support the following $m$ operations:
    
    -   Reroot, set node $u$ as the new tree root.
    -   Modify node weights on a path, increase the weights of all nodes on the path between node $u$ and node $v$ (including these two nodes) by $w$.
    -   Modify node weights on a subtree, increase the weights of all nodes on the subtree rooted at node $u$ by $w$.
    -   Query a path, query the sum of weights of all nodes on the path between node $u$ and node $v$ (including these two nodes).
    -   Query a subtree, query the sum of weights of all nodes on the subtree rooted at node $u$.
    
    $1 \le n,m \le 10^5$.

??? note "Solution"
    First run DFS with $1$ as the root node, preprocessing the information necessary for tree-path decomposition. For convenience of description, call the tree rooted at $1$ the "original tree", and call the tree after several rerooting operations the "current tree". During the operation process, we need to maintain $\textit{root}$ as the root node of the current tree. Since the segment tree stores the DFS-order information of the original tree, each query and modification needs to convert the query and modification operation of the current tree to the original tree.
    
    For the rerooting operation, we directly let $\textit{root}\gets u$. For path operations, since rerooting does not affect the path, just directly do the corresponding operation on the original tree.
    
    Focus on the problem of operating on a subtree. We do a case discussion according to the relative position of $u$ and $\textit{root}$:
    
    -   $u = \textit{root}$: this is the most special case, equivalent to operating on the whole tree. For this, just directly apply a tag to the root node of the segment tree or query the answer.
    -   $u$ is an ancestor of $\textit{root}$ on the original tree, i.e. $u$ is on the simple path from $1$ to $\textit{root}$.
    
        This is the most noteworthy case. Define $v$ as the point with the smallest depth other than $u$ on the simple path from $u$ to $\textit{root}$ on the original tree; we can find that the part of the original tree other than $v$ and its subtree is exactly $u$ and its subtree on the current tree.
    
        Consider how to efficiently find $v$. We first let $v\gets\textit{root}$, then jump up along heavy chains until $\operatorname{dep}(\operatorname{top}(v))\le\operatorname{dep}(u)+1$.
    
        -   If $\operatorname{dep}(\operatorname{top}(v))=\operatorname{dep}(u)+1$, let $v\gets\operatorname{top}(v)$. At this point, $v$ is a light child of $u$.
        -   If $\operatorname{dep}(\operatorname{top}(v))<\operatorname{dep}(u)+1$, i.e. $\operatorname{dep}(\operatorname{top}(v))\le \operatorname{dep}(u)$, this shows that $u,v$ are on the same heavy chain. According to the property that DFS order is consecutive on the same heavy chain, the sought $v$ must satisfy $\operatorname{dfn}(v)=\operatorname{dfn}(u)+1$. So, we can let $v\gets\operatorname{rnk}(\operatorname{dfn}(u)+1)$.
    
        Note that these two cases can be merged: after jumping, we can directly let
    
        $$
        v\gets\operatorname{rnk}(\operatorname{dfn}(\operatorname{top}(v))+\operatorname{dep}(u)+1-\operatorname{dep}(\operatorname{top}(v))).
        $$
    
        It is easy to verify that the $v$ found using this expression is equivalent to the $v$ found by the case discussion. This expression is used in the reference implementation.
    
        Since the interval covered by the subtree of $v$ is $[\operatorname{dfn}(v),\operatorname{dfn}(v)+\operatorname{siz}(v))$, we only need to operate on $[1,\operatorname{dfn}(v))\cup[\operatorname{dfn}(v)+\operatorname{siz}(v),n]$.
    -   Other cases. We can find that the rerooting operation does not affect the subtree of $u$, and just maintain it in the normal way.
    
    The complexity of doing this is the same as the approach without rerooting, both $O(n\log^2 n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_4.cpp"
    ```

Finally is an interactive problem, which is also a non-traditional application of tree decomposition.

???+ example "[Nauuo and Binary Tree](https://loj.ac/problem/6669)"
    There is a binary tree rooted at $1$; you can ask the distance between any two points, and find the parent of each point.
    
    The number of nodes does not exceed $3000$, and you can make at most $30000$ queries.

??? note "Solution"
    First we can determine the depth of each node through $n-1$ queries.
    
    Then consider determining the parent of each node in order of increasing depth, so that when determining the parent of a node, all its ancestors are definitely known.
    
    Before determining the parent of a node, first perform heavy-path decomposition on the known part of the tree.
    
    Suppose we need to find the position of node $k$ in the subtree $u$; we can ask the distance between $k$ and the tail end of the heavy chain where $u$ is located, and we can further determine the position of $k$; see the figure for details:
    
    ![](./images/hld2.png)
    
    where the red dashed line is a heavy chain, $d$ is the query result, i.e. $\textit{dis}(k, \textit{bot}(u))$, and the depth of $v$ is $(\textit{dep}(k)+\textit{dep}(\textit{bot}(u))-d)/2$.
    
    In this way, if $v$ has only one child, then the parent of $k$ is $v$, otherwise we can recursively find the parent of $k$ in the subtree of $w$.
    
    The time complexity is $O(n^2)$, and the query complexity is $O(n\log n)$.
    
    Specifically, let $T(n)$ be the number of queries needed to find the position of a new node in a tree of size $n$ in the worst case; we can obtain:
    
    $$
    T(n)\le
    \begin{cases}
    0&n=1\\
    T\left(\left\lfloor\frac{n-1}2\right\rfloor\right)+1&n\ge2
    \end{cases}
    $$
    
    $2999+\sum_{i=1}^{2999}T(i)\le 29940$; in fact this upper bound can be reached by constructing data, however as long as some random perturbation is done (such as using an unstable sorting algorithm when sorting the depths), it is hard for the number of queries to exceed $21000$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_2.cpp"
    ```

## Long-path decomposition

Long-path decomposition is essentially another way of chain decomposition.

Define the **heavy child** as the child with the largest subtree depth among the children. If there are multiple children with the largest subtree depth, take one of them. If there is no child, then there is no heavy child.

Define the **light children** as the remaining children.

The edge from this node to the heavy child is a **heavy edge**.

The edge to other light children is a **light edge**.

Several head-to-tail connected heavy edges constitute a **heavy chain**.

Regarding solitary nodes as heavy chains too, the whole tree is decomposed into several heavy chains.

As shown (this decomposition method can be seen as both heavy-path decomposition and long-path decomposition):

![HLD](./images/hld.png)

The implementation of long-path decomposition is similar to heavy-path decomposition, so it is not elaborated here.

### Common applications

First, we find that the number of light-edge switches on the path from a node to the root in long-path decomposition is on the order of $\sqrt{n}$.

??? info "How to construct data to push the number of light/heavy edge switches to the limit"
    We can construct such a binary tree T:
    
    Suppose the parameter of the constructed binary tree is $D$.
    
    If $D \neq 0$, then construct a binary tree with parameter $D-1$ in the left child, and construct a chain of length $2D-1$ in the right child.
    
    If $D = 0$, then we can directly construct a single leaf node and end the call.
    
    Constructing this way can definitely make the path from the single leaf node to the root all light edges, and requires a number of nodes on the order of $D^2$.
    
    Just take $D=\sqrt{n}$.

#### Optimizing DP with long-path decomposition

Generally, DP that can be optimized with long-path decomposition has a dimension of state being the depth dimension.

We can consider using long-path decomposition to optimize tree DP.

Specifically, each node's state directly inherits the node state of its heavy child, while brute-force merging the DP states of the light children.

???+ example "[Codeforces 1009 F. Dominant Indices](http://codeforces.com/contest/1009/problem/F)"
    Given a rooted tree with $n$ vertices, with vertex $1$ as the root.
    
    Define the depth array of vertex $x$ as an infinite sequence $[d_{x, 0}, d_{x, 1}, d_{x, 2}, \dots]$, where $d_{x, i}$ denotes the number of vertices $y$ satisfying the following two conditions:
    
    -   $x$ is an ancestor of $y$;
    -   The simple path from $x$ to $y$ passes exactly $i$ edges.
    
    The dominant index of the depth array of vertex $x$ (abbreviated the dominant index of vertex $x$) is defined as an index $j$ satisfying:
    
    -   For all $k < j$, $d_{x, k} < d_{x, j}$;
    -   For all $k > j$, $d_{x, k} \le d_{x, j}$.
    
    Please compute the dominant index of each vertex in the tree.

??? note "Solution"
    We let $f_{i,j}$ denote the number of points in subtree i at distance j from i.
    
    Directly brute-force transition has time complexity $O(n^2)$.
    
    We consider that each transition we directly inherit the DP array and answer of the heavy child, and consider updating on this basis.
    
    First we need to insert an element 1 at the front of the heavy child's DP array, which represents the current node.
    
    Then we brute-force merge the DP arrays of all light children with the DP array of the current node.
    
    Note that because the length of a light child's DP array is the length of the heavy chain where the light child is located, and the sum of all heavy chain lengths is $n$.
    
    That is to say, the total time complexity of directly brute-force merging light children is $O(n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/hld/hld_3.cpp"
    ```

Note that generally the memory allocation of the DP array is allocated for a whole heavy chain, and different nodes on the chain have different head-position pointers.

The length of the DP array can be computed according to the deepest node of the subtree.

Of course, there are many long-path decomposition DP optimization techniques, including but not limited to applying tags, etc. This is not elaborated here.

See [Zusuyu's blog](https://www.cnblogs.com/zhoushuyu/p/9468669.html).

#### Finding the k-th ancestor with long-path decomposition

That is, querying the node reached by jumping to the parent $k$ times from a point.

First we assume we have preprocessed the $2^i$-th ancestor of each node.

Now we assume we found the $2^i$-th ancestor of the query node satisfying $2^i \le k < 2^{i+1}$.

We consider finding the nodes on the heavy chain it is on and listing them in a table by depth. Suppose the heavy chain length is $d$.

At the same time, during preprocessing, we find the $1$-st to $d$-th ancestors of the root node of each heavy chain, and likewise put them into the table.

According to the property of long-path decomposition, $k-2^i \le 2^i \leq d$, that is to say, we can find the $k$-th ancestor of this node on the table of this heavy chain in $O(1)$.

Preprocessing needs to binary-lift the $2^i$-th ancestor, and also needs to preprocess the table corresponding to each heavy chain.

The preprocessing complexity is $O(n\log n)$, and the query complexity is $O(1)$.

## Exercises

-   [「Luogu P3379」【Template】Lowest Common Ancestor (LCA)](https://www.luogu.com.cn/problem/P3379) (tree decomposition finding LCA needs no data structure, can be used for practice)
-   [「JLOI2014」Squirrel's New Home](https://loj.ac/problem/2236) (of course it can also use tree difference)
-   [「HAOI2015」Tree Operations](https://loj.ac/problem/2125)
-   [「Luogu P3384」【Template】Heavy-Path Decomposition / Tree-Path Decomposition](https://www.luogu.com.cn/problem/P3384)
-   [「Luogu P1505」\[National Training Team\] Travel](https://www.luogu.com.cn/problem/P1505)
-   [「NOI2015」Software Package Manager](https://uoj.ac/problem/128)
-   [「SDOI2011」Coloring](https://www.luogu.com.cn/problem/P2486)
-   [「SDOI2014」Travel](https://hydro.ac/p/bzoj-P3531)
-   [「Luogu P3979」Distant Kingdom](https://www.luogu.com.cn/problem/P3979)
-   [「POI2014」Hotel Enhanced Version](https://hydro.ac/p/bzoj-P4543) (long-path decomposition optimizing DP)
-   [Strategy](https://hydro.ac/p/bzoj-P3252) (long-path decomposition optimizing greedy)
