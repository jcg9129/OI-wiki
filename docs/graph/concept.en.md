This page outlines some concepts in graph theory; these concepts are not all common in OI. For an OIer, it is only necessary to master the basic parts of this page; if you encounter a concept you don't understand while studying, you can come back to look it up.

??? warning "Warning"
    Graph-theory related definitions often differ in different textbooks; when you encounter them you need to judge according to the context.

## Graph

A **graph** is a two-tuple $G=(V(G), E(G))$. Here $V(G)$ is a non-empty set, called the **vertex set**; for each element in $V$, we call it a **vertex** or **node**; $E(G)$ is the set of edges between the nodes of $V(G)$, called the **edge set**.

$G=(V,E)$ is commonly used to denote a graph.

When both $V,E$ are finite sets, $G$ is called a **finite graph**.

When $V$ or $E$ is an infinite set, $G$ is called an **infinite graph**.

There are many kinds of graphs, including **undirected graphs**, **directed graphs**, **mixed graphs**, etc.

If $G$ is an undirected graph, then each element in $E$ is an unordered two-tuple $(u, v)$, called an **undirected edge**, abbreviated **edge**, where $u, v \in V$. Let $e = (u, v)$; then $u$ and $v$ are called the **endpoints** of $e$.

If $G$ is a directed graph, then each element in $E$ is an ordered two-tuple $(u, v)$, sometimes also written $u \to v$, called a **directed edge** or **arc**, and can also be called an **edge** when no confusion arises. Let $e = u \to v$; then at this point $u$ is called the **tail** of $e$, and $v$ is called the **head** of $e$; the tail and head are also called the **endpoints** of $e$. And $u$ is called the direct predecessor of $v$, and $v$ is the direct successor of $u$.

???+ note "Why is the start point the tail and the end point the head?"
    An edge is usually represented by an arrow, and the arrow points from the "tail" to the "head".

If $G$ is a mixed graph, then $E$ has both **directed edges** and **undirected edges**.

If each edge $e_k=(u_k,v_k)$ of $G$ is assigned a number as the **weight** of that edge, then $G$ is called a **weighted graph**. If these weights are all positive real numbers, then $G$ is called a **positively-weighted graph**.

The number of points $\left| V(G) \right|$ of graph $G$ is also called the **order** of graph $G$.

Vividly speaking, a graph is composed of several points and edges connecting points to points.

## Adjacency

In an undirected graph $G = (V, E)$, if point $v$ is an endpoint of edge $e$, then $v$ and $e$ are said to be **incident** or **adjacent**. For two vertices $u$ and $v$, if the edge $(u, v)$ exists, then $u$ and $v$ are said to be **adjacent**.

The **neighborhood** of a vertex $v \in V$ is the set of all vertices adjacent to it, denoted $N(v)$.

The neighborhood of a point set $S$ is the set of all points adjacent to at least one point in $S$, denoted $N(S)$, i.e.:

$$
N(S) = \bigcup_{v \in S} N(v)
$$

## Simple graph

**Loop**: for an edge $e = (u, v)$ in $E$, if $u = v$, then $e$ is called a loop.

**Multiple edge**: if there exist two completely identical elements (edges) $e_1, e_2$ in $E$, then they are called (a set of) multiple edges.

**Simple graph**: if a graph has no loops and no multiple edges, it is called a simple graph. In a simple undirected graph with at least two vertices, there must exist nodes with the same degree. ([Pigeonhole principle](../math/combinatorics/drawer-principle.md))

If a graph has loops or multiple edges, then it is called a **multigraph**.

??? warning "Warning"
    In an undirected graph $(u, v)$ and $(v, u)$ count as a set of multiple edges, while in a directed graph, $u \to v$ and $v \to u$ are not multiple edges.

??? warning "Warning"
    In problems, if there is no special note, loops and multiple edges can exist, and need special consideration when solving problems.

## Degree

The number of edges incident to a vertex $v$ is called the **degree** of that vertex, denoted $d(v)$. In particular, for an edge $(v, v)$, each such edge contributes $2$ to $d(v)$.

For an undirected simple graph, $d(v) = \left| N(v) \right|$.

Handshaking theorem (also called the fundamental theorem of graph theory): for any undirected graph $G = (V, E)$, $\sum_{v \in V} d(v) = 2 \left| E \right|$.

Corollary: in any graph, the number of points with odd degree must be even.

If $d(v) = 0$, then $v$ is called an **isolated vertex**.

If $d(v) = 1$, then $v$ is called a **leaf vertex**/**pendant vertex**.

If $2 \mid d(v)$, then $v$ is called an **even vertex**.

If $2 \nmid d(v)$, then $v$ is called an **odd vertex**. The number of odd vertices in a graph is even.

If $d(v) = \left| V \right| - 1$, then $v$ is called a **universal vertex**.

For a graph, the minimum of the degrees of all nodes is called the **minimum degree** of $G$, denoted $\delta (G)$; the maximum is called the **maximum degree**, denoted $\Delta (G)$. That is: $\delta (G) = \min_{v \in G} d(v)$, $\Delta (G) = \max_{v \in G} d(v)$.

In a directed graph $G = (V, E)$, the number of edges with a vertex $v$ as the tail is called the **out-degree** of that vertex, denoted $d^+(v)$. The number of edges with a vertex $v$ as the head is called the **in-degree** of that node, denoted $d^-(v)$. Obviously $d^+(v)+d^-(v)=d(v)$.

For any directed graph $G = (V, E)$:

$$
\sum_{v \in V} d^+(v) = \sum_{v \in V} d^-(v) = \left| E \right|
$$

If for an undirected graph $G = (V, E)$, the degree of each vertex is a fixed constant $k$, then $G$ is called a **$k$-regular graph**.

If given a sequence a, a graph G can be found with it as its degree sequence, then a is said to be **graphical**.

If given a sequence a, a simple graph G can be found with it as its degree sequence, then a is said to be **simply graphical**.

## Path

**Walk**: a walk is a sequence of edges connecting a series of vertices, which can be of finite or infinite length. Formally, a finite walk $w$ is a sequence of edges $e_1, e_2, \ldots, e_k$ such that there exists a vertex sequence $v_0, v_1, \ldots, v_k$ satisfying $e_i = (v_{i-1}, v_i)$, where $i \in [1, k]$. Such a walk can be abbreviated as $v_0 \to v_1 \to v_2 \to \cdots \to v_k$. Generally, the number of edges $k$ is called the **length** of this walk (if the edges are weighted, the length usually refers to the sum of edge weights on the walk, and the problem may also define it otherwise).

**Trail**: for a walk $w$, if $e_1, e_2, \ldots, e_k$ are pairwise distinct, then $w$ is called a trail.

**Path** (also called **simple path**): for a trail $w$, if the points in the sequence of points it connects are pairwise distinct, then $w$ is called a path.

**Circuit**: for a trail $w$, if $v_0 = v_k$, then $w$ is called a circuit.

**Cycle** (also called **simple circuit**): for a circuit $w$, if $v_0 = v_k$ is the only repeatedly-appearing point pair in the point sequence, then $w$ is called a cycle.

??? warning "Warning"
    The definition of a path may differ in different places; for example, "path" may refer to what this article calls "walk", and "cycle" may refer to what this article calls "circuit". If you see similar vocabulary in a problem, and there is no special note such as "simple path"/"non-simple path" (i.e. what this article calls "walk"), it is best to ask what specifically it refers to.

## Subgraph

For a graph $G = (V, E)$, if there exists another graph $H = (V', E')$ satisfying $V' \subseteq V$ and $E' \subseteq E$, then $H$ is called a **subgraph** of $G$, denoted $H \subseteq G$.

If for $H \subseteq G$, $\forall u, v \in V'$, as long as $(u, v) \in E$, we always have $(u, v) \in E'$, then $H$ is called an **induced subgraph** of $G$.

It is easy to find that an induced subgraph of a graph is determined only by the subgraph's vertex set, so an induced subgraph with vertex set $V'$($V' \subseteq V$) is called the subgraph induced by $V'$, denoted $G \left[ V' \right]$.

If $H \subseteq G$ satisfies $V' = V$, then $H$ is called a **spanning subgraph** of $G$.

Obviously, $G$ is a subgraph, spanning subgraph, and induced subgraph of itself; the [edgeless graph](#special-graphs) is a spanning subgraph of $G$. The original graph $G$ and the edgeless graph are both trivial subgraphs of $G$.

If a certain spanning subgraph $F$ of an undirected graph $G$ is a $k$-regular graph, then $F$ is called a **$k$-factor** of $G$.

If an induced subgraph $H = G \left[ V^\ast \right]$ of a directed graph $G = (V, E)$ satisfies $\forall v \in V^\ast, (v, u) \in E$, then $u \in V^\ast$, then $H$ is called a **closed subgraph** of $G$.

## Connectivity

### Undirected graph

For an undirected graph $G = (V, E)$, for $u, v \in V$, if there exists a walk such that $v_0 = u, v_k = v$, then $u$ and $v$ are said to be **connected**. By the definition, any vertex is connected to itself, and the two endpoints of any edge are connected.

If an undirected graph $G = (V, E)$ satisfies that any two vertices in it are connected, then $G$ is called a **connected graph**, and this property of $G$ is called **connectivity**.

If $H$ is a connected subgraph of $G$, and there does not exist $F$ satisfying $H\subsetneq F \subseteq G$ and $F$ being a connected graph, then $H$ is a **connected component** of $G$ (a maximal connected subgraph).

### Directed graph

For a directed graph $G = (V, E)$, for $u, v \in V$, if there exists a walk such that $v_0 = u, v_k = v$, then $u$ **can reach** $v$. By the definition, any vertex can reach itself, and the tail of any edge can reach its head. (Connectivity in an undirected graph can also be regarded as bidirectional reachability.)

If the nodes of a directed graph can pairwise reach each other, then this graph is said to be **strongly connected**.

If replacing the edges of a directed graph with undirected edges can yield a connected graph, then the original directed graph is said to be **weakly connected**.

Similar to connected components, there are also **weakly connected components** (maximal weakly connected subgraphs) and **strongly connected components** (maximal strongly connected subgraphs).

For related algorithms see [strongly connected components](./scc.md).

### Cut

For related algorithms see [cut vertices and bridges](./cut.md) and [biconnected components](./bcc.md).

In this part, "connectivity" of a directed graph generally refers to "strong connectivity".

For a connected graph $G = (V, E)$, if $V'\subseteq V$ and $G\left[V\setminus V'\right]$ (i.e. deleting the points in $V'$ from $G$) is not a connected graph, then $V'$ is a **vertex cut / separating set** of the graph $G$. A vertex cut of size one is also called a **cut vertex**.

For a connected graph $G = (V, E)$ and an integer $k$, if $|V|\ge k+1$ and $G$ has no vertex cut of size $k-1$, then the graph $G$ is said to be **$k$-vertex-connected**, and the largest $k$ making the above hold is called the **vertex connectivity** of the graph $G$, denoted $\kappa(G)$. (For a non-complete graph, the vertex connectivity is the size of the minimum vertex cut, and the vertex connectivity of the complete graph $K_n$ is $n-1$.)

For a graph $G = (V, E)$ and $u, v\in V$ satisfying $u\ne v$, $u$ and $v$ not adjacent, $u$ can reach $v$, if $V'\subseteq V$, $u, v\notin V'$, and in $G\left[V\setminus V'\right]$ $u$ and $v$ are disconnected, then $V'$ is called a vertex cut from $u$ to $v$. The size of the minimum vertex cut from $u$ to $v$ is called the **local connectivity** from $u$ to $v$, denoted $\kappa(u, v)$.

Similar definitions can also be made on edges:

For a connected graph $G = (V, E)$, if $E'\subseteq E$ and $G' = (V, E\setminus E')$ (i.e. deleting the edges in $E'$ from $G$) is not a connected graph, then $E'$ is an **edge cut** of the graph $G$. An edge cut of size one is also called a **bridge**.

For a connected graph $G = (V, E)$ and an integer $k$, if $G$ has no edge cut of size $k-1$, then the graph $G$ is said to be **$k$-edge-connected**, and the largest $k$ making the above hold is called the **edge connectivity** of the graph $G$, denoted $\lambda(G)$. (For any graph, the edge connectivity is the size of the minimum edge cut.)

For a graph $G = (V, E)$ and $u, v\in V$ satisfying $u\ne v$, $u$ can reach $v$, if $E'\subseteq E$, and in $G'=(V, E\setminus E')$ $u$ and $v$ are disconnected, then $E'$ is called an edge cut from $u$ to $v$. The size of the minimum edge cut from $u$ to $v$ is called the **local edge-connectivity** from $u$ to $v$, denoted $\lambda(u, v)$.

**Biconnected** is almost completely identical to $2$-vertex-connected, except for a graph formed by one edge connecting two points, which is biconnected but not $2$-vertex-connected. In other words, a connected graph with no cut vertex is biconnected.

**$2$-edge-connected** is completely identical to $2$-edge-connected. In other words, a connected graph with no bridge is edge-biconnected.

Similar to connected components, there are also **biconnected components** (maximal biconnected subgraphs) and **$2$-edge-connected components** (maximal edge-biconnected subgraphs).

**Whitney's theorem**: for any graph $G$, $\kappa(G)\le \lambda(G)\le \delta(G)$. (The three terms in the inequality are respectively the vertex connectivity, edge connectivity, and minimum degree.)

## Sparse graph / dense graph

If the number of edges of a graph is far less than the square of its number of points, then it is a **sparse graph**.

If the number of edges of a graph is close to the square of its number of points, then it is a **dense graph**.

These two concepts do not have strict definitions, and are generally used to discuss the efficiency difference between algorithms with [time complexity](../basic/complexity.md) $O(|V|^2)$ and $O(|E|)$ (on a dense graph these two algorithms are comparable in efficiency, while on a sparse graph the $O(|E|)$ algorithm is significantly more efficient).

## Complement graph

For an undirected simple graph $G = (V, E)$, its **complement graph** refers to such a graph: denoted $\bar G$, satisfying $V \left( \bar G \right) = V \left( G \right)$, and for any node pair $(u, v)$, $(u, v) \in E \left( \bar G \right)$ if and only if $(u, v) \notin E \left( G \right)$.

## Transpose graph

For a directed graph $G = (V, E)$, its **transpose graph** refers to the graph obtained by keeping the vertex set unchanged and reversing each edge, i.e.: if the transpose graph of $G$ is $G'=(V, E')$, then $E'=\{(v, u)|(u, v)\in E\}$.

## Special graphs

If an undirected simple graph $G$ satisfies that there is an edge between any two distinct points, then $G$ is called a **complete graph**, and the complete graph of order $n$ is denoted $K_n$. If a directed graph $G$ satisfies that between any two distinct points there are two edges of different directions, then $G$ is called a **complete digraph**.

A graph with an empty edge set is called an **edgeless graph**, **empty graph**, or **null graph**, and the edgeless graph of order $n$ is denoted $\overline{K}_n$ or $N_n$. $N_n$ and $K_n$ are complements of each other.

??? warning "Warning"
    **Null graph** may also refer to the **order-zero graph** $K_0$, i.e. a graph whose vertex set and edge set are both empty.

If a directed simple graph $G$ satisfies that between any two distinct points there is exactly one edge (one-directional), then $G$ is called a **tournament graph**.

If all edges of an undirected simple graph $G = \left( V, E \right)$ exactly constitute a cycle, then $G$ is called a **cycle graph**, and the cycle graph of order $n$($n \geq 3$) is denoted $C_n$. It is easy to know that a necessary and sufficient condition for a graph to be a cycle graph is that it is a $2$-regular connected graph.

If an undirected simple graph $G = \left( V, E \right)$ satisfies that there exists a point $v$ that is a universal vertex, and the remaining points have no edges connecting them, then $G$ is called a **star graph**, and the star graph of order $n + 1$($n \geq 1$) is denoted $S_n$.

If an undirected simple graph $G = \left( V, E \right)$ satisfies that there exists a point $v$ that is a universal vertex, and the other points constitute a cycle, then $G$ is called a **wheel graph**, and the wheel graph of order $n + 1$($n \geq 3$) is denoted $W_n$.

If all edges of an undirected simple graph $G = \left( V, E \right)$ exactly constitute a simple path, then $G$ is called a **chain (path graph)**, and the chain of order $n$ is denoted $P_n$. It is easy to know that a chain is obtained by deleting one edge from a cycle graph.

If an undirected connected graph contains no cycle, then it is called a **tree**. For related content see [tree basics](./tree-basic.md).

If an undirected connected graph contains exactly one cycle, then it is called a **pseudotree**.

If a directed weakly connected graph has in-degree $1$ for every point, then it is called an **outward pseudotree**.

If a directed weakly connected graph has out-degree $1$ for every point, then it is called an **inward pseudotree**.

Multiple trees can form a **forest**, multiple pseudotrees can form a **pseudoforest**, multiple outward pseudotrees can form an **outward pseudoforest**, and multiple inward pseudotrees can form an **inward pseudoforest (functional graph)**.

If every edge of an undirected connected graph is in at most one cycle, then it is called a **cactus**. Multiple cacti can form a **desert**.

If the vertex set of a graph can be divided into two parts, and there are no edges within each part, then this graph is a **bipartite graph**. If in a bipartite graph any two points not in the same part have an edge connecting them, then this graph is a **complete bipartite graph (biclique)**, and a complete bipartite graph with $n$ points and $m$ points in the two parts respectively is denoted $K_{n, m}$. For related content see [bipartite graph](./bi-graph.md).

If a graph can be drawn on a plane with no two edges intersecting at non-endpoints, then this graph is a **planar graph**. For a simple connected planar graph $G=(V, E)$ with $V\ge 3$, $|E|\le 3|V|-6$.  
**Kuratowski's theorem**: a graph is a planar graph if and only if it has no subgraph **homeomorphic** to $K_5$ or $K_{3, 3}$. Here graph $G$ and graph $G'$ being homeomorphic means both graphs can become the same graph by adding several vertices of degree $2$[^ref1] on edges.

## Isomorphism

Two graphs $G$ and $H$, if there exists a bijection $f : V(G) \to V(H)$ satisfying $(u,v)\in E(G)$ if and only if $(f(u),f(v))\in E(H)$, then we call $f$ an **isomorphism** from $G$ to $H$, and graph $G$ and graph $H$ are **isomorphic**, denoted $G \cong H$.

From the definition, if $G \cong H$, the following must be satisfied:

-   $|V(G)|=|V(H)|,|E(G)|=|E(H)|$
-   The non-increasing sequences of node degrees of $G$ and $H$ are the same
-   $G$ and $H$ have isomorphic induced subgraphs

## Binary operations on undirected simple graphs

For undirected simple graphs, we can define the following binary operations:

**Intersection**: the intersection of graphs $G = \left( V_1, E_1 \right), H = \left( V_2, E_2 \right)$ is defined as the graph $G \cap H = \left( V_1 \cap V_2, E_1 \cap E_2 \right)$.

It is easy to prove that the intersection of two undirected simple graphs is still an undirected simple graph.

**Union**: the union of graphs $G = \left( V_1, E_1 \right), H = \left( V_2, E_2 \right)$ is defined as the graph $G \cup H = \left( V_1 \cup V_2, E_1 \cup E_2 \right)$.

**Sum / direct sum**: for $G = \left( V_1, E_1 \right), H = \left( V_2, E_2 \right)$, arbitrarily construct $H' \cong H$ such that $V \left( H' \right) \cap V_1 = \varnothing$($H'$ can equal $H$). At this point any graph isomorphic to $G \cup H'$ is called the sum / direct sum / disjoint union of $G$ and $H$, denoted $G + H$ or $G \oplus H$.

If the vertex sets of $G$ and $H$ are themselves disjoint, then $G \cup H = G + H$.

For example, a forest can be defined as the sum of several trees.

???+ note "The difference between union and sum"
    It can be understood that "union" merges the "same-named" points and edges in the two graphs, while "sum" does not.

## Special point sets / edge sets

### Dominating set

For an undirected graph $G=(V, E)$, if $V'\subseteq V$ and $\forall v\in(V\setminus V')$ there exists an edge $(u, v)\in E$ satisfying $u\in V'$, then $V'$ is a **dominating set** of the graph $G$.

The size of the minimum dominating set of an undirected graph $G$ is denoted $\gamma(G)$. Finding the minimum dominating set of a graph is [NP-hard](../misc/cc-basic.md#np-hard).

For a directed graph $G=(V, E)$, if $V'\subseteq V$ and $\forall v\in(V\setminus V')$ there exists an edge $(u, v)\in E$ satisfying $u\in V'$, then $V'$ is an **out-dominating set** of the graph $G$. Similarly, an **in-dominating set** of a directed graph can be defined.

The size of the minimum out-dominating set of a directed graph $G$ is denoted $\gamma^+(G)$, and the size of the minimum in-dominating set is denoted $\gamma^-(G)$.

### Edge dominating set

For a graph $G=(V, E)$, if $E'\subseteq E$ and $\forall e\in(E\setminus E')$ there exists an edge in $E'$ having a common point with it, then $E'$ is called an **edge dominating set** of the graph $G$.

Finding the minimum edge dominating set of a graph is [NP-hard](../misc/cc-basic.md#np-hard).

### Independent set

For a graph $G=(V, E)$, if $V'\subseteq V$ and any two points in $V'$ are not adjacent, then $V'$ is an **independent set** of the graph $G$.

The size of the maximum independent set of a graph $G$ is denoted $\alpha(G)$. Finding the maximum independent set of a graph is [NP-hard](../misc/cc-basic.md#np-hard).

### Matching

For a graph $G=(V, E)$, if $E'\subseteq E$ and any two distinct edges in $E'$ have no common endpoint, and any edge in $E'$ is not a loop, then $E'$ is a **matching** of the graph $G$, also called an **independent edge set**. If a point is an endpoint of some edge in the matching, then this point is said to be **matched / saturated**, otherwise this point is said to be **unmatched**.

The matching with the most edges is called the **maximum-cardinality matching** of a graph. The size of the maximum matching of a graph $G$ is denoted $\nu(G)$.

If the edges are weighted, then the matching with the largest sum of weights is called the **maximum-weight matching** of a graph.

If a matching is no longer a matching after adding any edge, then this matching is a **maximal matching**. The largest maximal matching is the maximum matching, and any maximum matching is a maximal matching. A maximal matching must be an edge dominating set, but an edge dominating set is not necessarily a matching. The minimum maximal matching and the minimum edge dominating set have equal size, but the minimum edge dominating set is not necessarily a matching. Finding the minimum maximal matching is NP-hard.

If in a matching all points are matched, then this matching is a **perfect matching**. If in a matching only one point is unmatched, then this matching is a **near-perfect matching**.

Finding the number of matchings or perfect matchings of an ordinary graph or a bipartite graph is both [#P-complete](../misc/cc-basic.md#p_1).

For a matching $M$, if a path starts at a non-matched point, and one of every two adjacent edges is in the matching while the other is not, then this path is called an **alternating path**; an alternating path that terminates at a non-matched point is called an **augmenting path**.

**Tutte's theorem**: an undirected graph $G$ of order $n$ has a perfect matching if and only if for any $V' \subset V(G)$, $p_{\text{odd}}(G-V')\leq |V'|$, where $p_{\text{odd}}$ denotes the number of odd-order connected branches.

**Tutte's theorem (corollary)**: any bridgeless 3-regular graph has a perfect matching.

### Vertex cover

For a graph $G=(V, E)$, if $V'\subseteq V$ and $\forall e\in E$ satisfies that at least one endpoint of $e$ is in $V'$, then $V'$ is called a **vertex cover** of the graph $G$.

A vertex cover must be a dominating set, but a minimal vertex cover is not necessarily a minimal dominating set.

A point set is a vertex cover if and only if its complement is an independent set, so the complement of the minimum vertex cover is the maximum independent set. Finding the minimum vertex cover of a graph is [NP-hard](../misc/cc-basic.md#np-hard).

The size of any matching of a graph does not exceed the size of any vertex cover of it. The maximum matching and minimum vertex cover of the complete bipartite graph $K_{n, m}$ both have size $\min(n, m)$.

### Edge cover

For a graph $G=(V, E)$, if $E'\subseteq E$ and $\forall v\in V$ satisfies that $v$ is adjacent to at least one edge in $E'$, then $E'$ is called an **edge cover** of the graph $G$.

The size of the minimum edge cover is denoted $\rho(G)$, which can be found by greedily extending the maximum matching: for all non-matched points, add one of their adjacent edges to the maximum matching, obtaining a minimum edge cover.

The maximum matching can also be found from the minimum edge cover: for each pair of edges with a common point in the minimum edge cover, delete one of them.

The size of the minimum edge cover of a graph plus the size of the maximum matching equals the number of points of the graph, i.e. $\rho(G)+\nu(G)=|V(G)|$.

The size of the maximum matching of a graph does not exceed the size of the minimum edge cover, i.e. $\nu(G)\le\rho(G)$. In particular, a perfect matching must be a minimum edge cover, which is also the only case where the above equality is attained.

The size of any independent set of a graph does not exceed the size of any edge cover of it. The maximum independent set and minimum edge cover of the complete bipartite graph $K_{n, m}$ both have size $\max(n, m)$.

### Clique

For a graph $G=(V, E)$, if $V'\subseteq V$ and any two distinct vertices in $V'$ are adjacent, then $V'$ is a **clique** of the graph $G$. The induced subgraph of a clique is a complete graph.

If a clique is no longer a clique after adding any vertex, then this clique is a **maximal clique**.

The size of the maximum clique of a graph is denoted $\omega(G)$; the size of the maximum clique equals the size of the maximum independent set of its complement, i.e. $\omega(G)=\alpha(\bar{G})$. Finding the maximum clique of a graph is [NP-hard](../misc/cc-basic.md#np-hard).

## References

[OI transit station - Combing through graph-theory concepts](https://yhx-12243.github.io/OI-transit/memos/14.html)

[Wikipedia](https://en.wikipedia.org/wiki/Glossary_of_graph_theory_terms) (and the corresponding entries of related concepts)

Discrete Mathematics (Revised Edition), edited by Tian Wencheng and Zhou Luxin, Tianjin Literature Publishing House, P184-187

Dai Yiqi, Hu Guanzhang, Chen Wei. Graph Theory and Algebraic Structures \[M]. Beijing: Tsinghua University Press, 1995.

[^ref1]: This operation is also called subdivision.
