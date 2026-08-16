## Vertex divide and conquer

Vertex divide and conquer is suitable for handling large-scale tree path information problems.

??? note "Example problem 1 [Luogu P3806 [Template] Vertex divide and conquer 1](https://www.luogu.com.cn/problem/P3806)"
    Given a tree with $n$ points and edge weights, $m$ queries; each query gives $k$ and asks whether there exists a pair of points on the tree with distance $k$.
    
    $n\le 10000,m\le 100,k\le 10000000$

We first arbitrarily choose a node as the root node $\mathit{rt}$; all paths completely located in its subtree can be divided into two kinds, one is the paths passing through the current root node, and one is the paths not passing through the current root node. For the paths passing through the current root node, they can further be divided into two kinds, one is the paths with the root node as one endpoint, and the other is the paths where neither endpoint is the root node. The latter can in turn be obtained by merging two chains belonging to the former. So, for the enumerated root node $rt$, we first compute the contribution to the answer of the paths in its subtree and passing through this node, then recurse into its subtrees to solve for the paths not passing through this node.

In this problem, for the paths passing through the root node $\mathit{rt}$, we first enumerate all its child nodes $\mathit{ch}$, and with $\mathit{ch}$ as the root, compute the distances from all nodes in the $\mathit{ch}$ subtree to $\mathit{rt}$. Denote the distance from node $i$ to the current root node $rt$ as $\mathit{dist}_i$, and $\mathit{tf}_{d}$ denotes whether there exists a node $v$ in the previously-processed subtrees such that $\mathit{dist}_v=d$. If a query's $k$ satisfies $tf_{k-\mathit{dist}_i}=true$, then there exists a path of length $k$. After computing whether the edges connected in the $\mathit{ch}$ subtree can become the answer, we add these new distances to the $\mathit{tf}$ array.

Note that when clearing the $\mathit{tf}$ array, we cannot directly use `memset`, but should add the previously-occupied $\mathit{tf}$ positions to a queue and clear them; only this way can the time complexity be guaranteed.

During the vertex divide-and-conquer process, all recursion processes at each level collectively process each point once; assuming a total of $h$ levels of recursion, the total time complexity is $O(hn)$.

If we each time choose the [centroid](./tree-centroid.md) of the subtree as the root node, we can guarantee the minimum number of recursion levels, with time complexity $O(n\log n)$. Therefore, vertex divide and conquer is also often called **centroid decomposition** of the tree in the foreign competition community.

Please note that after re-choosing the root node, we must recompute the size of the subtree, otherwise a seemingly minor change may make the time complexity incorrect or the correctness hard to guarantee.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-divide/tree-divide_1.cpp"
    ```

??? note "Example problem 2 [Luogu P4178 Tree](https://www.luogu.com.cn/problem/P4178)"
    Given a weighted tree with $n$ points, given $k$, ask the number of pairs of points on the tree with distance less than or equal to $k$.
    
    $n\le 40000,k\le 20000,w_i\le 1000$

Since what is queried here is the number of pairs of points with tree distance in $[0,k]$, we use a segment tree to support maintenance and querying.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-divide/tree-divide_2.cpp"
    ```

??? note "Example problem 3 [Luogu P2664 Tree game](https://www.luogu.com.cn/problem/P2664)"
    A tree where each node is given a color; define $s(i,j)$ as the number of colors from $\mathit{i}$ to $\mathit{j}$, and $\mathit{sum_{i}}=\sum_{j=1}^n s(i,j)$. For all $1\leq i\leq n$, find $sum_i$. ($1 \le n, c_i \le 10^5$)

This problem greatly tests the understanding and application of the vertex divide-and-conquer idea, and is suitable as a relatively difficult example and practice problem for vertex divide and conquer.

First, we need to figure out a transformation. The problem defines $\mathit{sum_i}$ as the sum of the numbers of colors on the paths from $i$ to all nodes, but if we use this method, it is not easy to count the answer in vertex divide and conquer, because this way it is difficult to merge the information of the two subtrees starting from the current root. So we think of transforming the meaning of $\mathit{sum_i}$. For each color $j$, denote the number of paths with one endpoint being $i$ and containing color $j$ as $\mathit{cnt_j}$; $\mathit{sum_i}$ is actually $\sum \mathit{cnt_j}$. This step of transformation actually just changes the object of observation, considering the contribution of each color to $\mathit{sum_i}$. And $\mathit{cnt_j}$ is actually easy to work out; we only need to, each time we encounter a new color, do $\mathit{cnt_{col_u}}+=\mathit{size_u}$, where $\mathit{size_u}$ is the subtree size of u, meaning that all nodes in this subtree have a contribution to $u$'s answer on this color.

Considering that during the vertex divide-and-conquer process, we only need to consider counting separately:

1.  The contribution to the root of the paths in the subtree with the current root node as an endpoint
2.  The contribution to each point in the subtree of the paths whose lca is the current root node

Part 1 is relatively easy to handle; since in vertex divide and conquer, the number of recursion levels does not exceed $\log{n}$, at each level we can traverse all subtrees, and at this time we can use the definition of $\mathit{sum_i}$ to count incidentally during the traversal of the subtrees.

And for part 2, let a child node of the current root node $u$ be $d$, and arbitrarily take a point $v$ in the subtree of $d$; then the answer of $v$ can be divided into two parts:

1.  The colors that have appeared on the path $(u, v)$, with the number set as $\mathit{num}$, and the total size of all subtrees of $u$ other than $d$ set as $\mathit{siz1}$; then the contribution of these appeared colors to $v$'s answer is $\mathit{num}\times \mathit{siz1}$.
2.  The colors $j$ that have not appeared on the path $(u, v)$; their contribution comes from the $\mathit{cnt_j}$ of all subtrees of $u$ other than $d$, and this part of the answer is $\sum_{j \notin (u, v)} \mathit{cnt_j}$.

The above is the entire counting idea; for implementation details, see the reference code.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-divide/tree-divide_3.cpp"
    ```

## Edge divide and conquer

Similar to the vertex divide and conquer above, we select an edge, dividing the tree as evenly as possible into two parts (making the $\mathit{size}$s of the two subtrees connected by the edge as close as possible). Then we recursively process the left and right subtrees, counting information.

But this does not work; consider a star graph:

![star graph](./images/tree-divide1.svg)

We find that when a point has multiple sons with close $\mathit{size}$, the time complexity of applying edge divide and conquer is unacceptable.

If this graph is a binary tree, we can avoid the drawback of applying edge divide and conquer in the star graph above. Therefore we consider transforming a multi-way tree into a binary tree.

Obviously, we only need to build the tree like a segment tree. Like this

![building the tree](./images/tree-divide2.svg)

Give the newly created points appropriate information according to the problem requirements. For example: when counting path length, assign the original edge weight as $1$ and the newly created edge weight as $0$.

Analyzing the complexity, we find that at most $O(n)$ points will be added, so the total complexity is $O(n\log n)$.

Almost all vertex divide-and-conquer problems can be done with edge divide (there is a gap in the constant factor, but it is not adversarial), so we do not give example problems.

## Vertex divide-and-conquer tree

The vertex divide-and-conquer tree is a reconstructed tree that changes the form of the original tree so that the number of levels of the tree becomes a stable $\log n$.

It is commonly used to solve modification problems unrelated to the original form of the tree.

### Algorithm analysis

We reconstruct the original tree by finding the centroid each time in vertex divide and conquer.

Establish a parent-child relationship between the centroid found each time and the centroid of the previous level, so that a tree with $\log n$ levels can be formed.

Since the tree has $\log n$ levels, many brute-force methods that were originally not sound all have correct complexity on the vertex divide-and-conquer tree.

### Code implementation

There is a small trick: each time subtract the heavy son size of the previous level's point from the total size $\mathit{tot}$ recursed from the previous level, and what is obtained is the total size of this level. This way, finding the centroid only needs one DFS.

???+ note "Reference code"
    ```cpp
    #include <algorithm>
    #include <iostream>
    #include <vector>
    using namespace std;
    
    using IT = vector<int>::iterator;
    
    struct Edge {
      int to, nxt, val;
    
      Edge() {}
    
      Edge(int to, int nxt, int val) : to(to), nxt(nxt), val(val) {}
    } e[300010];
    
    int head[150010], cnt;
    
    void addedge(int u, int v, int val) {
      e[++cnt] = Edge(v, head[u], val);
      head[u] = cnt;
    }
    
    int siz[150010], son[150010];
    bool vis[150010];
    
    int tot, lasttot;
    int maxp, root;
    
    void getG(int now, int fa) {
      siz[now] = 1;
      son[now] = 0;
      for (int i = head[now]; i; i = e[i].nxt) {
        int vs = e[i].to;
        if (vs == fa || vis[vs]) continue;
        getG(vs, now);
        siz[now] += siz[vs];
        son[now] = max(son[now], siz[vs]);
      }
      son[now] = max(son[now], tot - siz[now]);
      if (son[now] < maxp) {
        maxp = son[now];
        root = now;
      }
    }
    
    struct Node {
      int fa;
      vector<int> anc;
      vector<int> child;
    } nd[150010];
    
    int build(int now, int ntot) {
      tot = ntot;
      maxp = 0x7f7f7f7f;
      getG(now, 0);
      int g = root;
      vis[g] = true;
      for (int i = head[g]; i; i = e[i].nxt) {
        int vs = e[i].to;
        if (vis[vs]) continue;
        int tmp = build(vs, ntot - son[vs]);
        nd[tmp].fa = now;
        nd[now].child.push_back(tmp);
      }
      return g;
    }
    
    int virtroot;
    
    int main() {
      int n;
      cin >> n;
      for (int i = 1; i < n; i++) {
        int u, v, val;
        cin >> u >> v >> val;
        addedge(u, v, val);
        addedge(v, u, val);
      }
      virtroot = build(1, n);
    }
    ```
