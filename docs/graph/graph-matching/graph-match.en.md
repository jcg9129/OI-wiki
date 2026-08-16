author: 310552025atNYCU, accelsao, Chrogeek, Enter-tainer, iamtwz, mcendu, Shen-Linwood, shuzhouliu, StudyingFather, t4rf9, Tiphereth-A, TrickEye, wlbksy, Xeonacid, yuhuoji, c-forrest, aaron20100919

## Introduction

A **matching** or **independent edge set** is a set of edges in a graph with no common endpoints. Graph matching algorithms are algorithms commonly used in informatics competitions, and can roughly be divided into two categories: maximum matching and maximum-weight matching. Because a matching in a [bipartite graph](../bi-graph.md) is equivalent to a network-flow problem, has good properties, and is relatively easy to handle, here we will first introduce the two categories of algorithms starting from bipartite graphs, and then discuss algorithms for general graphs.

## Matching of a graph

Let $G=(V,E)$ be an undirected graph, where $V$ is the vertex set and $E$ is the edge set. If a set of edges $M\subseteq E$ contains no self-loops and has no common vertices pairwise, then the edge set $M$ is called a **matching** or **independent edge set** of graph $G$. An edge $e\in E$, if it appears in the matching $M$, is called a **matching edge**, otherwise it is called a **non-matching edge**. Correspondingly, a vertex $v\in V$, if it is an endpoint of a matching edge, is called a **matched point**, otherwise it is called an **unmatched point**.

The size of a matching $M$ is the number of edges it contains. For matchings in (weighted) undirected graphs, the following concepts are often considered:

-   **Maximal matching**: a matching that cannot continue to add matching edges. A maximal matching is not necessarily a maximum matching.

    ![maximal matching](images/graph-match-1.svg)

-   **Maximum matching (or maximum cardinality matching)**: the matching with the most matching edges. There may be more than one maximum matching, but the number of edges of a maximum matching is determined, and cannot exceed half the number of vertices in the graph.

    ![maximum cardinality matching](images/graph-match-2.svg)

-   **Maximum weight matching**: in a weighted graph, the matching with the maximum sum of edge weights.

    ![maximum weight matching](images/graph-match-3.svg)

-   **Maximum weight maximum matching (maximum weight maximum cardinality matching)**: under the premise of the most matching edges, the matching with the maximum sum of edge weights. That is, among all maximum matchings, the matching with the maximum sum of edge weights.

    ![maximum weight maximum cardinality matching](images/graph-match-4.svg)

-   **Perfect matching**: a matching where every vertex is a matched point. A perfect matching must be a maximum matching. A complete graph with an even number of vertices must have a perfect matching.

-   **Near-perfect matching**: a matching with exactly one unmatched point. This can only happen when the number of vertices of the graph is odd. A near-perfect matching must also be a maximum matching. A complete graph with an odd number of vertices must have a near-perfect matching.

The graph matching problems involved in algorithm competitions mainly refer to the maximum matching or maximum-weight matching of a graph.

## Augmenting path

In graph matching algorithms, the augmenting path is the core structure used to improve the matching.

### Definition

For a graph $G=(V,E)$ and one of its matchings $M$, the following two (simple) paths can be defined:

-   An **alternating path** is a path formed by matching edges and non-matching edges alternating;
-   An **augmenting path** is an alternating path that starts at an unmatched point and ends at an unmatched point.

Because on an augmenting path the number of non-matching edges is $1$ more than the number of matching edges, the number of edges in an augmenting path must be odd. If the matching edges and non-matching edges on an augmenting path are reversed, then it is still an alternating path, and the number of matching edges will increase by $1$. The process of finding an augmenting path and reversing it to increase the matching size is called **augmentation**. In mathematical language, augmentation is equivalent to taking the symmetric difference of the matching $M$ and the augmenting path $P$, obtaining the new matching $M\oplus P$.

The figure below shows the process of the number of matching edges increasing from $2$ to $3$ after one augmentation operation.

![augment-1](./images/augment-1.png)

### Berge's lemma

Berge's lemma shows that the method of using augmenting paths to improve the matching is sufficient. That is to say, when no augmenting path can be found, it means the maximum matching has already been obtained.

???+ note "Berge's lemma"
    For a graph $G=(V,E)$ and one of its matchings $M$, the matching $M$ is a maximum matching if and only if there is no augmenting path relative to the matching $M$.

??? note "Proof"
    It has been shown above that when there is an augmenting path $P$, the matching $M\oplus P$ is a larger matching than $M$, so $M$ must not be a maximum matching.
    
    Conversely, we need to show that if there exists a matching $M'$ larger than the matching $M$, then there must exist an augmenting path $P$ relative to $M$. For this, examine the symmetric difference $M\oplus M'$. The degrees of vertices in the graph $(V,M\oplus M')$ can only be $0$, $1$, or $2$; the connected components of such a graph must be one of a path, a cycle, or an isolated point. Moreover, the two edges adjacent to a vertex of degree $2$ must come from different matchings, so the number of edges from $M$ and $M'$ in these cycles is the same. Because $M'$ is larger than $M$, there exists at least one path where the number of edges from $M'$ is more than $M$; denote this path as $P$. Then, the start point and end point of $P$ are both unmatched points of $M$, and $P$ is an alternating path relative to $M$, so $P$ must be an augmenting path relative to $M$. This completes the proof.

From this theorem, we know the core idea of finding the maximum matching:

-   Enumerate all unmatched points, find augmenting paths, until no augmenting path can be found.

In fact, after each augmentation operation ends, there is no need to re-traverse all unmatched points once. In the whole process of finding the maximum matching, each vertex only needs to be traversed once.

??? note "Proof"
    We only need to show that if when the enumeration proceeds to vertex $v$, there is no augmenting path starting from $v$, then after several rounds of augmentation, there is also no augmenting path starting from $v$. This shows that even if augmentation causes a change in the matching, there is no need to re-check the previously-enumerated unmatched points.
    
    Suppose not. That is, suppose $v$ is an already-enumerated unmatched point, and in some round after augmenting along the augmenting path $P$ from $u$ to $w$, a previously-nonexistent augmenting path $P'$ starting from $v$ is newly added. Then, the path $P'$ must have a common edge with $P$; otherwise, augmenting along $P$ would not cause the matching status of the edges in $P'$ to change, and $P'$ would not be an augmenting path newly added because of this augmentation.
    
    ![augment-2](./images/augment-2.svg)
    
    (In the figure, black represents non-matching edges, and red and blue represent different matching statuses)
    
    Let $x$ be the first vertex in $P$ reached from $v$ along the path $P'$. Because before this augmentation, there already existed an alternating path from $v$ to $x$, $x$ must be a matched point, and cannot be one of vertex $u$ or vertex $w$. Therefore, on the augmenting path $P$, there are two edges adjacent to $x$, and their matching statuses are opposite. This shows that no matter what the matching status of the edge is when reaching vertex $x$ along the alternating path starting from $v$, the alternating path can be extended along path $P$ to one of $u$ or $w$. This shows that before augmentation there already existed an augmenting path starting from $v$, which contradicts the assumption.

### Alternating tree

Another concept closely related to the augmenting path is the alternating tree. It is a tree produced in the process of DFS or BFS from an unmatched point $r$ to find augmenting paths.

For a graph $G=(V,E)$ and one of its matchings $M$, if a subgraph $H\subseteq G$ is a tree rooted at an unmatched point $r$, and the path connecting $r$ and any $v\in H$ is an alternating path, then $H$ is called an **alternating tree**. Here, points on the tree with even depth are called even points, and points on the tree with odd depth are called odd points.

The figure below shows an alternating tree that may be obtained by BFS starting from the unmatched point $1$. (In the figure, red edges are matching edges, black edges are non-matching edges; dark vertices are matched points, light vertices are unmatched points.)

![](images/alternating-tree.svg)

## Existence of a perfect matching

In graph matching theory, there are two important existence theorems that can be used to determine whether a perfect matching exists in a bipartite graph or a general graph.

### Hall's theorem

Suppose $G=(X,Y,E)$ is a bipartite graph, and $|X|\le |Y|$. For a matching $M$ of graph $G$, if all vertices in $X$ are matched points, then $M$ is called an **$X$-perfect matching**, sometimes also simply called (the bipartite graph $G$'s) perfect matching. This is the largest matching that can be achieved in a bipartite graph. Hall's theorem provides a necessary and sufficient condition for judging whether such a matching exists.

Hall's theorem shows that as long as it is guaranteed that for any subset of $X$, there are enough vertices in $Y$ that can match it, then an $X$-perfect matching must exist.

???+ note "Hall's theorem"
    Suppose $G=(X,Y,E)$ is a bipartite graph, and $|X|\le |Y|$. For any $W\subseteq X$, denote $N_G(W)$ as the set of all vertices in graph $G$ adjacent to the vertices in $W$. Then, an $X$-perfect matching exists if and only if $|W|\le |N_G(W)|$ holds for all $W\subseteq X$.

??? note "Proof"
    The condition is obviously necessary. Suppose an $X$-perfect matching $M$ exists, then each vertex in $X$ is matched to a distinct vertex in $Y$. The set $N_G(W)$ at least includes those vertices matched with the vertices in $W$, so its size is at least $|W|$.
    
    The condition is also sufficient. Suppose an $X$-perfect matching does not exist, then there must be a maximum matching $M$ such that a vertex $v\in X$ is still an unmatched point. Let $Z$ be the set of all vertices that can be reached through an alternating path starting from $v$, and let $S=Z\cap X$, $T=Z\cap Y$. The set $S\setminus\{v\}$ must all be matched points, otherwise an odd cycle would appear, contradicting $G$ being a bipartite graph; the set $T$ must also all be matched points, otherwise an augmenting path exists, which, by Berge's lemma, contradicts $M$ being a maximum matching. Because all are matched points, and matching can only happen between $X$ and $Y$, the vertices in the set $S\setminus\{v\}$ and the set $T$ correspond one-to-one, that is, $|T|=|S|-1$. At the same time, because the vertices in $T$ are already matched with vertices in $S$, there is at least $T\subseteq N_G(S)$; but, there is no unmatched point $u$ in $N_G(S)$, because if it is adjacent to $v'$ in $S$, then one can necessarily obtain an alternating path reaching $u$ by extending the alternating path reaching $v'$: this shows that $T=N_G(S)$. These arguments show $|N_G(S)|<|S|$, which contradicts the condition assumed in Hall's theorem. This shows that an $X$-perfect matching exists.

???+ note "Corollary"
    All regular bipartite graphs have a perfect matching.

??? note "Proof"
    In a regular bipartite graph, the degrees of all vertices are the same, say $k$. First verify that the Hall condition holds, i.e. for any $W\subseteq X$, $|N_G(W)|\ge |W|$. Because the number of edges adjacent to the vertices in $W$ is $k|W|$, and each vertex in the set $N_G(W)$ can be adjacent to at most $k$ of these edges, there must be $k|W|\le k|N_G(W)|$, i.e. $|W|\le |N_G(W)|$. In particular, $|X|\le |Y|$; because $X$ and $Y$ are symmetric, $|X|=|Y|$. This shows that in a regular bipartite graph, an $X$-perfect matching must also be a perfect matching. Since Hall's theorem guarantees that an $X$-perfect matching exists, a perfect matching must also exist.

### Tutte's theorem

Tutte's theorem provides a necessary and sufficient condition for judging whether a perfect matching exists in a general graph. This condition stems from a direct observation: a perfect matching must not exist in a graph with an odd number of vertices.

???+ note "Tutte's theorem"
    A graph $G=(V,E)$ has a perfect matching if and only if for any $U\subseteq V$, $\operatorname{odd}(G-U)\le |U|$, where $G-U$ denotes the subgraph obtained by deleting the vertices in $U$ and the edges adjacent to them from graph $G$, and $\operatorname{odd}(G-U)$ denotes the number of connected components with an odd number of vertices in the subgraph $G-U$.

??? note "Proof"
    We only need to consider simple graphs, because multi-edges and self-loops do not affect the Tutte condition and the existence of a perfect matching.
    
    The necessity of the condition is relatively easy. Suppose a perfect matching $M$ exists. For any $U\subseteq V$, after deleting the vertices in $U$ from graph $G$, each connected component with an odd number of vertices has at least one vertex that cannot be matched with a vertex in the same connected component; these vertices can only seek to be matched with vertices in $U$. Such a matching existing requires at least $\operatorname{odd}(G-U)\le |U|$. This is the Tutte condition.
    
    The sufficiency of the condition is more complex. Suppose $G$ satisfies the Tutte condition but has no perfect matching. Because adding any edge to $G$ will keep the Tutte condition holding, we may as well assume $G$ is a maximal such graph, that is, $G$ has no perfect matching, but adding any not-yet-existing edge $e$ to $G$ will make $G+e$ have a perfect matching. Let $U\subseteq V$ be the set of all vertices with degree $|V|-1$. We can prove that each connected component of $G-U$ is a complete graph. From this, we can construct a perfect matching of $G$: first take the maximum matching of each connected component of $G-U$; in this way only when the number of vertices of a connected component is odd will there be an unmatched point; match these unmatched points to vertices in $U$; because the number of vertices of $G$ is even (taking $U=\varnothing$ in the Tutte condition), the number of remaining not-yet-matched vertices in $U$ is also even, and we just pair them up two by two. This contradiction shows that there is no $G$ that satisfies the Tutte condition but has no perfect matching.
    
    The key is to prove that each connected component of $G-U$ is a complete graph. Suppose not. We may as well assume vertices $x,y,z$ belong to such a connected component, and $(x,y)\in E$, $(y,z)\in E$, $(x,z)\notin E$. Moreover, because $y\notin U$, there must exist $w\in V\setminus U$ but $(y,w)\notin E$. Due to the maximality of $G$, the graphs $G+(x,z)$ and $G+(y,w)$ have perfect matchings $M_1$ and $M_2$ respectively. Examine their symmetric difference $M_1\oplus M_2$. Because the degrees of all vertices in the graph $(V,M_1\oplus M_2)$ are either $0$ or $2$, $M_1\oplus M_2$ is actually a disjoint union of several even cycles, and each even cycle is composed of the matching edges in $M_1$ and $M_2$ alternating.
    
    ![](images/tutte-proof.svg)
    
    As shown, we can divide into two cases:
    
    -   $(x,z)$ and $(y,w)$ are in different cycles (as shown on the left): let the cycle containing $(y,w)$ be $C$; then, the edge set $M_2\oplus C$ is a perfect matching of graph $G$;
    -   $(x,z)$ and $(y,w)$ are in the same cycle (as shown on the right): by symmetry, we may as well assume the cycle passes through $x,y,w,z$ in turn, so we can take the path $P$ on the cycle from $y$ through $w$ to $z$, denote $\{(y,z)\}\cup P$ as the cycle $C$; then, the edge set $M_2\oplus C$ is likewise a perfect matching of graph $G$.
    
    In either case, it contradicts the choice of $G$. This contradiction shows that each connected component of $G-U$ is a complete graph.

???+ note "Corollary"
    A bridgeless 3-regular graph has a perfect matching.

??? note "Proof"
    To verify that the Tutte condition holds, take any $U\subseteq V$; we need to prove $\operatorname{odd}(G-U)\le |U|$. Let $G_1,\cdots,G_n$ be all the connected components of $G-U$ with an odd number of vertices. Let $m_i$ be the number of edges connecting the vertices in $G_i$ and the vertices in $U$. Simple counting shows
    
    $$
    3|V(G_i)| = \sum_{v\in V(G_i)} d(v) = 2|E(G_i)| + m_i.
    $$
    
    Therefore, $m_i$ must be odd. Because there is no bridge (i.e. cut edge) in $G$, $m_i\ge 3$. This shows
    
    $$
    \operatorname{odd}(G-U) = n \le \dfrac{1}{3}\sum_{i=1}^n m_i \le \dfrac{1}{3}\sum_{v\in U} d(v) = |U|.
    $$
    
    Therefore, the Tutte condition holds, and graph $G$ must have a perfect matching.

## Common algorithms

A basic problem in combinatorial optimization is finding the maximum matching and maximum-weight matching of a graph.

### Bipartite graph maximum matching

See the [bipartite graph maximum matching](./bigraph-match.md) page for details.

In an unweighted bipartite graph, one can use Kuhn's algorithm to solve it in $O(|V||E|)$ time, or use the Hopcroft–Karp algorithm to solve it in $O(|V|^{1/2}|E|)$ time.

### Bipartite graph maximum-weight matching

See the [bipartite graph maximum-weight matching](./bigraph-weight-match.md) page for details.

In a weighted bipartite graph, the Hungarian algorithm can be used to solve it. If the Bellman–Ford algorithm is used when finding the shortest path, the time complexity is $O(|V|^2|E|)$; if the Dijkstra algorithm or a Fibonacci heap is used, it can be solved in $O(|V|^{2}\log {|V|}+|V||E|)$ time.

### General graph maximum matching

See the [general graph maximum matching](./general-match.md) page for details.

In an unweighted general graph, one can use Edmonds' blossom algorithm to solve it in $O(|V|^2|E|)$ time.

### General graph maximum-weight matching

See the [general graph maximum-weight matching](./general-weight-match.md) page for details.

In a weighted general graph, one can use Edmonds' blossom algorithm to solve it in $O(|V|^2|E|)$ time.

## Related problems

Maximum (weight) matching is closely related to other graph-theory problems. This section only discusses general graphs; for conclusions about bipartite graphs, refer to the [bipartite graph maximum matching](./bigraph-match.md#related-problems) page.

### Maximum weight maximum matching

The maximum-weight-maximum-matching problem and the maximum-weight-matching problem can be reduced to each other. A very notable difference between them is that a maximum-weight-maximum-matching may have negative-weight edges, but a maximum-weight-matching will not have negative-weight edges.

First, the maximum-weight-matching problem can be reduced to the maximum-weight-maximum-matching problem. First, set the weights of all negative-weight edges of graph $G$ to $0$; then, by connecting several edges with weight $0$, expand the graph into a complete graph $G'$. Note that in a complete graph with non-negative edge weights, the maximum-weight-maximum-matching and the maximum-weight-matching are consistent. So, we only need to compute the maximum-weight-maximum-matching $M'$ of $G'$, then delete all zero-weight edges in $M'$, and the obtained edge set $M$ is the maximum-weight-matching of graph $G$. [^other-approach]

![graph-match](images/graph-match-5.svg)

Conversely, the maximum-weight-maximum-matching problem can also be reduced to the maximum-weight-matching problem. We only need to add a sufficiently large positive number $K$ to the edge weights of all edges of graph $G$, and then we can guarantee that the maximum-weight-matching of the obtained graph $G'$ must also be a maximum matching, so it must be a maximum-weight-maximum-matching. This is because computing the maximum-weight-matching of graph $G'$ is equivalent to maximizing, among all matchings of graph $G$,

$$
K|M| + \sum_{e\in M}w(e).
$$

When $K$ is sufficiently large, the gain $K$ brought by matching one more edge will exceed the change in the weight sum of the latter term. Therefore, the algorithm will first match as many edges as possible, and only then maximize the edge weight sum of the matching edges. The choice of the constant $K$ only needs to guarantee that it is strictly greater than the difference between two possible matchings. An obvious choice is

$$
K = \sum_{e\in E}|w(e)| + 1.
$$

![graph-match](images/graph-match-6.svg)

### Minimum (weight) edge cover

Another problem closely related to maximum (weight) matching is minimum (weight) edge cover. The relationship between edge cover and matching (also called independent edge set) is similar to the relationship between vertex cover and independent set.

For a set of edges $C\subseteq E$ in a graph $G=(V,E)$, if any vertex $v\in V$ is an endpoint of some edge in $C$, then $C$ is called an **edge cover** of graph $G$. When discussing edge cover, we always assume that graph $G$ has no isolated points.

For an unweighted graph, the minimum edge cover problem is almost the maximum matching problem. For any maximum matching $M$ of graph $G$, we can obtain a minimum edge cover $C$ just by adding a connected edge for each unmatched point. Their sizes satisfy a simple quantitative relationship: $|M|+|C|=|V|$. The figure below shows some examples of minimum edge covers:

![graph-match](images/graph-match-7.svg)

For a weighted graph, the minimum-weight edge cover problem can be reduced to a **minimum-weight perfect matching** problem. First, copy graph $G=(V,E)$ to get $\tilde G=(\tilde V,\tilde E)$, with edge weights consistent with the original graph; then, connect each vertex $v\in V$ with its copy $\tilde v\in\tilde V$, with the edge weight being the minimum of the weights of the edges adjacent to $v$ in graph $G$. The graph thus obtained is denoted as $G'=(V',E')$. If graph $G$ is a bipartite graph or a sparse graph, then graph $G'$ is likewise a bipartite graph or a sparse graph respectively. Moreover, the minimum-weight edge cover problem of graph $G$ is reduced to the minimum-weight perfect matching problem of graph $G'$[^edge-cover]: for the minimum-weight perfect matching $M'$ of graph $G'$, we just keep the edges in $E$, then replace all matched $(v,v')$ with the minimum-weight edge adjacent to $v$ in graph $G$, and we obtain the minimum-weight edge cover of graph $G$.

## References

1.  [Wikiwand - Matching (graph theory)](https://www.wikiwand.com/en/Matching_%28graph_theory%29)
2.  [Wikiwand - Blossom algorithm](https://www.wikiwand.com/en/Blossom_algorithm)
3.  2015 "A brief discussion of graph matching algorithms and their applications" - Chen Yinbo
4.  [Algorithm Notes - Matching](http://web.ntnu.edu.tw/~algo/Matching.html)
5.  [the-tourist/algo](https://github.com/the-tourist/algo)
6.  [Bill Yang's Blog - Blossom tree study notes](https://blog.bill.moe/blossom-algorithm-notes/)
7.  [Bipartite graph maximum matching, perfect matching, and the Hungarian algorithm](https://www.renfei.org/blog/bipartite-matching.html)
8.  [Wikiwand - Hopcroft–Karp algorithm](https://www.wikiwand.com/en/Hopcroft%E2%80%93Karp_algorithm)
9.  Bondy, John Adrian, and Uppaluri Siva Ramachandra Murty. Graph theory with applications. Vol. 290. London: Macmillan, 1976.

[^other-approach]: Of course, this is not the only way of reduction. For graph $G=(V,E)$, we can also connect a copy of it $\tilde G=(\tilde V,\tilde E)$ point by point to the original graph, and set the weights of all edges newly added relative to the original graph $G$ (including the edges in the copy) to $0$, obtaining graph $G'=(V',E')$. In other words, the vertex set of the new graph $G'$ is $V\cup V'$, and its edge set, besides the edges in graph $G$, also connects all vertices $v\in V$ with their copies $\tilde v\in V$ with zero-weight edges, and for all edges $(u,v)\in E$, connects $\tilde u$ with $\tilde v$ with zero-weight edges. All matchings $M$ in graph $G$ correspond to a perfect matching in graph $G'$ with the same weight sum: we just match all unmatched points $v$ in $G$ with their copies $\tilde v$, and for all matching edges $(u,v)$, match $\tilde u$ with $\tilde v$. Therefore, the maximum-weight-maximum-matching in graph $G'$, i.e. the maximum-weight perfect matching, restricted to $E$, gives the maximum-weight-matching of graph $G$. The benefit of reducing this way is that if graph $G$ is a bipartite graph or a sparse graph, then the expanded graph $G'$ is also a bipartite graph or a sparse graph respectively.

[^edge-cover]: For each perfect matching $M'$ of graph $G'$, we can obtain an edge cover $C$ of graph $G$ in the way described here, and the weight sum of the latter is half that of the former; reversing this construction process, for each edge cover $C$ of graph $G$, we can construct a perfect matching $M'$ of graph $G'$, and the weight sum of the latter does not exceed twice that of the former. This shows that the reduction holds.
