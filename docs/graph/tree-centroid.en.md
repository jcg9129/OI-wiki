author: Ir1d, Marcythm, LucienShui, Anguei, H-J-Granger, CornWorld, ttzc

This article introduces the concept and basic properties of the centroid of a tree.

## Definition

If, after deleting some node $v$ in a tree $T$, the size of each connected component in the obtained graph $T\setminus\{v\}$ does not exceed half of the number of nodes of the original tree, then this node $v$ is called the **centroid** of the whole tree. The size of the largest connected component obtained after deleting a certain node is also called the **weight** of that node. Using this concept, the definition of the centroid can be stated as a node whose weight does not exceed half of the number of tree nodes.

???+ info "\"Subtree\""
    This article may simultaneously involve unrooted trees, rooted trees, and the tree obtained by rerooting a rooted tree to a non-root node. To avoid confusion, this article will use $T$ to denote an unrooted tree, and $T^{(v)}$ to denote the rooted tree rooted at node $v$. The "subtree" mentioned in this article all refers to, in a **rooted tree**, the tree formed by a node and all its descendant nodes. In the rooted tree $T^{(v)}$, the subtree corresponding to node $u$ is denoted $T^{(v)}_u$. A subtree defined this way of course includes the whole tree itself. If we want to explicitly exclude the whole tree itself, we will call it a "proper subtree".
    
    A "subtree" in an unrooted tree usually refers to one of its connected subgraphs. When discussing the centroid, some authors use the term "subtree" to specifically refer to a maximal connected subgraph not containing a certain node, or specifically refer to one of the two connected components obtained after deleting a certain edge. It is easy to verify that the "subtree" sets defined by these two ways are consistent, and do not include the whole tree itself. Since it is not consistent with the subtree set of a rooted tree, this article will avoid using the "subtree" concept for unrooted trees.
    
    When actually solving for the centroid or handling certain problems, there is usually a default tree root. At this time, among the connected components obtained by deleting a non-root node $v$, besides the subtrees corresponding to the child nodes of this node, there is also an "upward" subtree. At this time, let the parent node of node $v$ be $u$; this "upward" subtree is exactly $T_u^{(v)}$. When mentioning this kind of subgraph, this article will explicitly call it the "upward" subtree. Unless otherwise specified, the subtrees mentioned in this article do not include this kind of "upward" subtree.

Note that these obtained connected components are also unrooted trees. By deleting the centroid of the tree, a tree will become several trees at most half the size of the original tree. This characteristic of the centroid makes it possible to apply the divide-and-conquer idea on trees to solve problems. This is [vertex divide and conquer](./tree-divide.md#vertex-divide-and-conquer), also called centroid decomposition of the tree.

## Properties

This section discusses the properties of the centroid. First, the centroid of a tree has the following equivalent definitions:

???+ note "Equivalent definitions"
    A node $v$ in a tree $T$ is its centroid if and only if any one of the following holds:
    
    === "Unrooted tree version"
        1.  After deleting node $v$ in the tree, the size of each connected component in the obtained graph $T\setminus\{v\}$ does not exceed half of the number of nodes of the original tree.
        2.  Among all the sizes of the largest connected component obtained after deleting a certain node, the value obtained when deleting node $v$ is the smallest.
        3.  Among the sums of distances from all nodes in the tree to a certain node, the sum of distances to node $v$ is the smallest.
    
    === "Rooted tree version"
        1.  When the tree is rooted at node $v$, the size of any proper subtree does not exceed half of the number of nodes of the original tree.
        2.  Among all the largest proper subtree sizes when rooted at a certain node, the value obtained when rooted at node $v$ is the smallest.
        3.  Among the sums of depths of all nodes when rooted at a certain node, the sum of depths when rooted at node $v$ is the smallest.

??? note "Proof"
    First, introduce some notation. The two versions of the statement, rooted tree and unrooted tree, are obviously equivalent. Define $W(x)=\max_{u\sim x}|T_u^{(x)}|$, where $u\sim x$ means $u$ and $x$ are adjacent. Define $S(x)=\sum_{u\in T}d(u,x)$, where $d(u,x)$ denotes the distance between nodes $u$ and $x$. Then, definition 1 is equivalent to requiring $W(v)\le |T|/2$, definition 2 is equivalent to requiring $v\in\arg\min_{x\in T}W(x)$, and definition 3 is equivalent to requiring $v\in\arg\min_{x\in T}S(x)$. What needs to be proved is that these three conditions are equivalent.
    
    Understanding $S(x)$ as the sum of node depths when rooted at $x$, consider its change when the tree root is changed from node $v$ to an adjacent node $u$. Note that after deleting edge $(v,u)$ in the tree, the two obtained connected components are subtrees $T_v^{(u)}$ and $T_u^{(v)}$ respectively. Before and after rerooting, the depth of each node in subtree $T_v^{(u)}$ increases by $1$, and the depth of each node in subtree $T_u^{(v)}$ decreases by $1$, so the change in the depth sum is
    
    $$
    \Delta S_{v\to u} = S(u) - S(v) = |T_v^{(u)}| - |T_u^{(v)}| = |T| - 2|T_u^{(v)}|.
    $$
    
    So, the condition of definition 1 is equivalent to requiring $\Delta S_{v\to u}\le 0$ to hold for all adjacent nodes $u$ of $v$, that is, $v$ is a local minimum point of $S(x)$.
    
    Now let $v$ be a (one) minimum point of $S(x)$ (i.e. definition 3); it must exist and must be a local minimum point. Consider the rooted tree $T^{(v)}$ rooted at $v$. Let $u\neq v$ be a non-root node, and on the directed path from $v$ to $u$, let the node after node $v$ be $y$ (possibly $u$ itself), and the node before node $u$ be $x$ (possibly $v$ itself). Then, because $T_u^{(x)}\subseteq T_y^{(v)}$, we have
    
    $$
    2|T_x^{(u)}| = 2|T| - 2|T_u^{(x)}| \ge 2|T| - 2|T_y^{(v)}| \ge |T|.
    $$
    
    where the last step uses the fact that $v$ is a local minimum point of $S(x)$. At this time, there are two cases:
    
    -   There exists a node $u$ such that $2|T_x^{(u)}|=|T|$ holds. At this time, according to the above inequality, we must have $(x,u)=(v,y)$, and $|T_v^{(u)}|=|T_{u}^{(v)}| = |T|/2$. That is to say, the node $u$ that makes the equality hold can only be one, and it must be adjacent to $v$. At this time, for all other nodes $u'\neq u,v$, there must exist $x'\sim u'$ such that $|T_{x'}^{(u')}| > |T|/2$ holds. The set of nodes satisfying condition 1 is $\{v,u\}$.
    
        Note that when deleting any node, the sum of the sizes of the obtained connected components is always $|T|-1$, so as long as one connected component has size not less than $|T|/2$, it must be the largest connected component. Therefore, for this case, $W(v)=W(u)=|T|/2$, and for all $u'\neq u,v$ we have $W(u') > |T|/2$. Therefore, the set of nodes satisfying condition 2 is $\arg\min W(x) = \{v,u\}$.
    
        And because $\Delta S_{v\to u} = 0$, so $S(v)=S(u)$. Because $v$ is a minimum point, $u$ must also be a minimum point. And for $u'\neq u,v$ there exists $x'\sim u'$ such that $|T_{x'}^{(u')}| > |T|/2$, which violates the condition that a local minimum point needs to satisfy, so $u'$ must also not be a minimum point. Therefore, the set of nodes satisfying condition 3 is $\arg\min S(x) = \{v,u\}$.
    -   There is no node $u$ such that $2|T_x^{(u)}|=|T|$ holds. At this time, for all nodes $u\neq v$, there exists a node $x\sim u$ such that $|T_x^{(u)}| > |T|/2$. Repeating the previous analysis, for all nodes $u\neq v$, we have $W(u) > |T|/2$, and $u$ is not a local minimum point of $S(x)$. Therefore, the only node satisfying condition 1 is $v$, and $\arg\min W(x)=\arg\min S(x) = \{v\}$.
    
    In either case, the set satisfying the three conditions is the same. This proves that the three definitions are equivalent.

Besides these equivalent definitions, the centroid of a tree also has the following common properties:

???+ note "Properties"
    1.  If the centroid of a tree is not unique, then there are exactly two. These two centroids are adjacent. Moreover, after deleting the edge connecting them, the tree will become two connected components of the same size.
    2.  Adding or deleting a leaf on a tree, then its centroid moves at most a distance of one edge.
    3.  Connecting two trees through an edge to obtain a new tree, then the centroid of the new tree is on the path connecting the centroids of the original two trees.
    4.  The centroid of a rooted tree must be on the heavy chain where the root node is located. The centroid of a tree must be an ancestor of the centroid of the subtree corresponding to the heavy child node of the tree root.

??? note "Proof"
    Property 1 can be obtained from the proof of the equivalent definitions of the centroid.
    
    Property 2 only needs to consider the case of adding a leaf node. This is further divided into two cases:
    
    -   The tree $T$ has only one centroid $v$. Let $x$ be the newly added leaf node, and in the graph $T\cup\{x\}\setminus\{v\}$ obtained by deleting node $v$ in the new tree, let the connected component where $x$ is located be $B\cup\{x\}$. Because $v$ is the unique centroid of the tree $T$, so $2|B| < |T|$, that is $2|B|+1\le |T|$. Furthermore, we have
    
        $$
        2|B\cup\{x\}| = 2(|B|+1) \le |T| + 1 = |T\cup\{x\}|.
        $$
    
        Therefore, $v$ is still the centroid of the new tree $T\cup\{x\}$. Even if the centroid of the new tree is not unique, it must be an adjacent node of $v$. Therefore, the centroid moves at most one edge.
    -   The tree $T$ has two centroids $u,v$. At this time, the two connected components $T_u^{(v)}$ and $T_v^{(u)}$ obtained by deleting $(u,v)$ have equal size, both being $|T|/2$. Without loss of generality, assume the newly added leaf node $x$ is connected to the connected component $T_v^{(u)}$ where $v$ is located. Then, because
    
        $$
        |T_v^{(u)}\cup\{x\}| = |T|/2 + 1 > (|T|+1)/2 = |T\cup\{x\}|/2,
        $$
    
        so $u$ is no longer the centroid of the new tree. Conversely, because after deleting $v$, there is still a connected component $T_u^{(v)}$ of size $|T|/2$, while the sum of the sizes of the other connected components is
    
        $$
        |T\cup\{x\}| - 1 - |T_u^{(v)}| = |T|/2 \le |T_u^{(v)}|,
        $$
    
        so $v$ is still the centroid of the new tree. Because the number of nodes of the new tree is odd, the centroid must be unique. So, the centroid also moves at most one edge.
    
    Summarizing the analysis of the two cases, we can find that the centroid of the new tree must be on the path from the centroid of the old tree to the newly added leaf node.
    
    Property 3 can be explained by induction. Let the newly added edge when connecting $T$ and $T'$ be $(x,y)$, with $x\in T,y\in T'$. Without loss of generality, assume a (one) centroid of the new tree is in $T$. Consider the process of starting from tree $T$ and adding the nodes in tree $T'$ one by one as its leaf nodes. We can prove by induction that a (one) centroid of the tree is always on the path connecting the centroid of tree $T$ and node $x$. The induction base is obvious. Assume the proposition still holds up to a certain moment. Let the centroid at this time be $v$. From the analysis of property 2, the centroid of the new tree must be on the path connecting the newly added node and the current centroid $v$; and because it will not move outside tree $T$, we only need to consider the common part of the path with tree $T$, i.e. on the path connecting the current centroid $v$ and node $x$. According to the induction hypothesis, $v$ is on the path connecting the centroid of tree $T$ and node $x$, so the centroid of the new tree must also be on the path connecting the current centroid $v$ and node $x$. By induction, the proposition holds.
    
    Property 4 only needs to be combined with the [properties of heavy-path decomposition](./hld.md#properties-of-heavy-path-decomposition) to explain. Let a (one) centroid of the tree $T$ be $v$. When node $v$ is the root node, the proposition obviously holds. Below let $v$ be a non-root node and $u$ be its parent node. Because $|T_u^{(v)}| \le |T|/2$, so the size of the subtree where $v$ is located is at least $|T|/2$. But, as long as its path to the root node passes through a light edge once, the size of the subtree where it is located will be strictly less than $|T|/2$, a contradiction. So, it must be on the heavy chain where the root node is located. Furthermore, according to the definition of the heavy chain, the heavy chain where the root node is located in the subtree corresponding to the heavy child node of the root node is exactly part of the heavy chain where the root node is located in the original tree; and, according to property 3, after adding the heavy child node and the subtrees corresponding to all its light child nodes to the subtree corresponding to the heavy child node, the centroid position will move along the path of the current centroid and the root node, so the new centroid must be an ancestor of the old centroid.

## Method

According to the equivalent definitions of the centroid, there are two methods to find all centroids of a tree in $O(n)$ time, where $n$ is the size of the tree.

### DFS to count subtree sizes

Compute the size of each subtree through DFS. For each node, record the sizes of the subtrees corresponding to all its child nodes, and use the total number of nodes minus the current subtree size to obtain the size of the "upward" subtree, and then we can find the centroid according to the definition.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/graph/code/tree-centroid/tree-centroid-2.cpp:core"
    ```

### Rerooting DP to count depth sums

We can also compute, through rerooting DP, the sum of depths of all nodes (i.e. the sum of distances to the current root node) when rooted at different nodes. According to the definition, we only need to find the node that minimizes this depth sum.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/graph/code/tree-centroid/tree-centroid-3.cpp:core"
    ```

## Example problems

???+ example "[Codeforces Round 359 (Div. 1) B. Kay and Snowflake](https://codeforces.com/problemset/problem/685/B)"
    Given a rooted tree, find the centroid of each subtree.

??? note "Solution idea"
    According to property 3, for a subtree rooted at point $u$, its centroid must be on the path from the centroids of all subtrees rooted at the direct child nodes of $u$ to point $u$.
    
    Similar to the DFS method for finding the centroid mentioned above, for each subtree rooted at node $u$, first find the centroids of all subtrees rooted at its direct child nodes (the centroid of a leaf node is itself), then judge upward whether the nodes on the path are the centroid.
    
    All subtree centroids can be found in $O(n)$ time.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/tree-centroid/tree-centroid-1.cpp"
    ```

## Exercises

-   [Gym 101649G Godfather](https://codeforces.com/gym/101649/problem/G)
-   [POJ 1655 Balancing Art](http://poj.org/problem?id=1655)
-   [Luogu P1364 Hospital placement](https://www.luogu.com.cn/problem/P1364)
-   [Codeforces 1406C Link Cut Centroids](https://codeforces.com/contest/1406/problem/C)
-   [Codeforces 708C Centroids](https://codeforces.com/problemset/problem/708/C)

## References

-   [Some properties and dynamic maintenance of the "centroid" of a tree - fanhq666](https://web.archive.org/web/20181122041458/http://fanhq666.blog.163.com/blog/static/81943426201172472943638) ([Cnblogs repost](https://www.cnblogs.com/qlky/p/5781081.html))
-   [Tree diameter, tree centroid and tree vertex divide and conquer - cyendra](https://www.cnblogs.com/zinthos/p/3899075.html)
-   [Properties of the tree centroid and their proofs - suxxsfe](https://www.cnblogs.com/suxxsfe/p/13543253.html)
-   《Dictionary of Informatics Olympiad》 Chapter 2.4.7.11 1. Centroid of a tree
