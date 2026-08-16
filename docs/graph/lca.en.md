author:ouuan, Backl1ght, billchenchina, CCXXXI, ChickenHu, ChungZH, cjsoft, countercurrent-time, diauweb, Early0v0, Enter-tainer, EtaoinWu, H-J-Granger, H-Shen, Henry-ZHR, HeRaNO, hsfzLZH1, huaruoji, iamtwz, imp2002, Ir1d, kenlig, Konano, Lyccrius, Marcythm, Menci, NachtgeistW, PeterlitsZo, psz2007, shuzhouliu, SkqLiao, sshwy, SukkaW, therehello, TrisolarisHD, ttzztztz, vincent-163, WAAutoMaton, Hunter19019

## Definition

The lowest common ancestor is abbreviated as LCA (Lowest Common Ancestor). The lowest common ancestor of two nodes is the one, among the common ancestors of these two points, that is farthest from the root.
For convenience, we denote the lowest common ancestor of some point set $S=\{v_1,v_2,\ldots,v_n\}$ as $\text{LCA}(v_1,v_2,\ldots,v_n)$ or $\text{LCA}(S)$.

## Properties

> The content of the **Properties** section of this article is translated from [wcipeg](http://wcipeg.com/wiki/Lowest_common_ancestor), with modifications.

1.  $\text{LCA}(\{u\})=u$;
2.  $u$ is an ancestor of $v$ if and only if $\text{LCA}(u,v)=u$;
3.  If $u$ is not an ancestor of $v$ and $v$ is not an ancestor of $u$, then $u,v$ lie in two different subtrees of $\text{LCA}(u,v)$ respectively;
4.  In a preorder traversal, $\text{LCA}(S)$ appears before all elements in $S$; in a postorder traversal, $\text{LCA}(S)$ appears after all elements in $S$;
5.  The lowest common ancestor of the union of two point sets is the lowest common ancestor of the respective lowest common ancestors of the two point sets, i.e. $\text{LCA}(A\cup B)=\text{LCA}(\text{LCA}(A), \text{LCA}(B))$;
6.  The lowest common ancestor of two points must lie on the shortest path between the two points on the tree;
7.  $d(u,v)=h(u)+h(v)-2h(\text{LCA}(u,v))$, where $d$ is the distance between two points on the tree, and $h$ denotes the distance from a point to the tree root.

## Methods

### Naive algorithm

#### Procedure

We can each time find the point with the larger depth and let it jump upward. Obviously, on the tree, these two points will eventually meet, and the meeting position is exactly the LCA we want.
Alternatively, first adjust the point with the larger depth upward so that they have the same depth, then jump upward together; finally they will also meet.

#### Properties

The naive algorithm needs to dfs the entire tree during preprocessing, with time complexity $O(n)$, and the time complexity of a single query is $\Theta(n)$. If the tree satisfies the random property, then the time complexity is related to the expected height of such a random tree.

### Binary lifting algorithm

#### Procedure

The binary lifting algorithm is the most classic method for finding LCA; it is an improved version of the naive algorithm. By preprocessing the $\text{fa}_{x,i}$ array, the cursor can move quickly, greatly reducing the number of cursor jumps. $\text{fa}_{x,i}$ represents the $2^i$-th ancestor of point $x$. The $\text{fa}_{x,i}$ array can be preprocessed by dfs.

Now let us look at how to optimize these jumps:
In the first stage of adjusting the cursor, we want to jump the two points $u,v$ to the same depth. We can compute the difference in depth of the two points $u,v$, and denote it by $y$. By performing binary decomposition on $y$, we optimize the $y$ cursor jumps into "the number of `1`s contained in the binary representation of $y$" cursor jumps.
In the second stage, we loop trying from the largest $i$, all the way down to $0$ (inclusive); if $\text{fa}_{u,i}\not=\text{fa}_{v,i}$, then $u\gets\text{fa}_{u,i},v\gets\text{fa}_{v,i}$, so the final LCA is $\text{fa}_{u,0}$.

#### Properties

The preprocessing time complexity of the binary lifting algorithm is $O(n \log n)$, and the single-query time complexity is $O(\log n)$.
In addition, the binary lifting algorithm can swap the two dimensions of the `fa` array so that the smaller dimension is placed first. This can reduce the number of cache misses and improve program efficiency.

??? note "Example problem"
    [HDU 2586 How far away?](https://acm.hdu.edu.cn/showproblem.php?pid=2586) Shortest-path query on a tree.

We can first find the LCA, then combine property $7$ to solve it. We can also directly obtain the result while computing the LCA.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/lca/lca_1.cpp"
    ```

### Tarjan algorithm

#### Procedure

The Tarjan algorithm is an **offline algorithm** that needs to use a [disjoint set union](../ds/dsu.md) to record the ancestor node of a certain node. The method is as follows:

1.  First accept the input edges (adjacency list) and query edges (stored in another adjacency list). The query edges are actually virtually added edges; for convenience, each time a query edge is input, this edge and its reverse edge are both added to the `queryEdge` array.
2.  Then perform a DFS traversal on it, meanwhile using the `visited` array to record whether a certain node has been visited, and `parent` to record the parent node of the current node.
3.  This involves the **backtracking idea**: each time we traverse to a certain node, we consider the root node of this node to be itself. After the DFS rooted at this node has been fully traversed, then set the root node of this node to the parent-level node of this node.
4.  During backtracking, if starting from this node, the other node of the `queryEdge` query edge has also just been visited, then directly update the LCA result of the query edge.
5.  Finally output the results.

#### Properties

The Tarjan algorithm needs to initialize the disjoint set union, so the preprocessing time complexity is $O(n)$.

The naive Tarjan algorithm processing all $m$ queries has time complexity $O(m \alpha(m+n, n) + n)$, but the Tarjan algorithm has a larger constant factor than the binary lifting algorithm. There exists an $O(m + n)$ implementation.

???+ warning "Note"
    The claim "the disjoint set union used in the naive Tarjan LCA algorithm has a rather special property, and the time complexity of a single call to the `find()` function is amortized $O(1)$" does not hold.
    
    The following naive Tarjan implementation has complexity $O(m \alpha(m+n, n) + n)$. If a strictly linear complexity is desired, one may refer to [the 1983 paper by Gabow and Tarjan](https://dl.acm.org/doi/pdf/10.1145/800061.808753), which gives an approach with complexity $O(m + n)$.

#### Implementation

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/lca/lca_tarjan.cpp"
    ```

### Converting to an RMQ problem using the Euler sequence

#### Definition

Perform a DFS on a tree; whether it is the first visit or a backtrack, each time we reach a node we record its number, and we obtain a sequence of length $2n-1$. This sequence is called the Euler sequence of this tree.

In the following, we denote the position number where node $u$ first appears in the Euler sequence as $pos(u)$ (also called the Euler order of node $u$), and denote the Euler sequence itself as $E[1..2n-1]$.

#### Procedure

With the Euler sequence, the LCA problem can be converted into an RMQ problem in linear time, i.e. $pos(LCA(u, v))=\min\{pos(k)|k\in E[pos(u)..pos(v)]\}$.

This equation is not hard to understand: in the process of walking from $u$ to $v$, we will definitely pass through $LCA(u,v)$, but will not pass through the ancestors of $LCA(u,v)$. Therefore, the node with the smallest Euler order passed through in the process of walking from $u$ to $v$ is exactly $LCA(u, v)$.

The time complexity of computing the Euler sequence by DFS is $O(n)$, and the length of the Euler sequence is also $O(n)$, so the LCA problem can be converted into an RMQ problem of the same scale in $O(n)$ time.

#### Implementation

???+ note "Reference code"
    ```cpp
    int dfn[N << 1], pos[N], tot, st[30][(N << 1) + 2],
        rev[30][(N << 1) + 2];  // rev denotes the node number corresponding to the minimum depth
    
    void dfs(int cur, int dep) {
      dfn[++tot] = cur;
      depth[tot] = dep;
      pos[cur] = tot;
      for (int i = head[t]; i; i = side[i].next) {
        int v = side[i].to;
        if (!pos[v]) {
          dfs(v, dep + 1);
          dfn[++tot] = cur, depth[tot] = dep;
        }
      }
    }
    
    void init() {
      for (int i = 2; i <= tot + 1; ++i)
        lg[i] = lg[i >> 1] + 1;  // preprocess lg to replace the library function log2 to optimize the constant factor
      for (int i = 1; i <= tot; i++) st[0][i] = depth[i], rev[0][i] = dfn[i];
      for (int i = 1; i <= lg[tot]; i++)
        for (int j = 1; j + (1 << i) - 1 <= tot; j++)
          if (st[i - 1][j] < st[i - 1][j + (1 << i - 1)])
            st[i][j] = st[i - 1][j], rev[i][j] = rev[i - 1][j];
          else
            st[i][j] = st[i - 1][j + (1 << i - 1)],
            rev[i][j] = rev[i - 1][j + (1 << i - 1)];
    }
    
    int query(int l, int r) {
      int k = lg[r - l + 1];
      return st[k][l] < st[k][r + 1 - (1 << k)] ? rev[k][l]
                                                : rev[k][r + 1 - (1 << k)];
    }
    ```

When we need to query the LCA of some point pair $(u, v)$, we just query the node represented by the minimum value on the interval $[\min\{pos[u], pos[v]\}, \max\{pos[u], pos[v]\}]$.

If an ST table is used to solve the RMQ problem, then the algorithm does not support online modification; the preprocessing time complexity is $O(n\log n)$, and the time complexity of each LCA query is $O(1)$.

### Heavy-light decomposition

The LCA is the point pointed to by the cursor with the smaller depth when the two cursors jump onto the same heavy chain.

The preprocessing time complexity of heavy-light decomposition is $O(n)$, the single-query time complexity is $O(\log n)$, and the constant factor is small.

### Link Cut Tree

In a [Link Cut Tree](../ds/lct.md), let the points of two consecutive [access](../ds/lct.md#access) operations be `u` and `v` respectively; then the point returned by the second [access](../ds/lct.md#access) operation is the LCA of `u` and `v`.

In the case where there are no operations such as link and cut, using a Link Cut Tree, the single-query time complexity is $O(\log n)$.

### Standard RMQ

We mentioned above transforming the LCA problem into an RMQ problem with the help of the Euler order, whose bottleneck lies in the RMQ. If we can solve RMQ in $O(n) \sim O(1)$, then we can also solve LCA in $O(n) \sim O(1)$.

Note that the Euler order satisfies that the difference between two adjacent numbers is 1 or -1, so we can use the $O(n) \sim O(1)$ [plus-or-minus-1 RMQ](../topic/rmq.md#加减-1rmq) to do it.

The time complexity is $O(n) \sim O(1)$, the space complexity is $O(n)$, it supports online queries, and the constant factor is large.

#### Example problem [Luogu P3379 [Template] Lowest Common Ancestor (LCA)](https://www.luogu.com.cn/problem/P3379)

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/lca/lca_2.cpp"
    ```

## Exercises

-   [Ancestor-descendant query](https://loj.ac/problem/10135)
-   [Truck transport](https://loj.ac/problem/2610)
-   [Distance between points](https://loj.ac/problem/10130)
