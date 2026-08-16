This article introduces (planar) graphs and their related concepts.

## Planar graph

If a graph $G$ can be drawn on a plane $S$, i.e. no edges intersect except at vertices, then we say $G$ can be embedded in the plane $S$, and $G$ is a **planar graph**. The drawn graph with no intersecting edges is called a planar representation or **planar embedding** of $G$. This planar embedding of a planar graph is also called a **plane graph**.

???+ info "\"Plane graph\""
    In different Chinese texts, the meaning of "plane graph" (平面图) may differ. In the definition of this article, a planar graph is a graph-theory object that may be embedded in the plane in different ways; a plane graph is a geometric object that, besides the graph-theory structure, also needs to specify the drawing method of the graph. The same planar graph often corresponds to multiple plane graphs. Therefore, the conclusions stated in this article will use the term "planar graph" if they depend only on the graph-theory structure; if they also depend on the planar-embedding method of the graph, they will use the term "plane graph".

The following are simple examples of plane graphs:

![](images/planar-1.svg)

(Left: butterfly graph; right: complete graph $K_4$ of order $4$)

The following are simple examples of non-planar graphs:

![](images/planar-2.svg)

(Left: complete graph $K_5$ of order $5$; right: complete bipartite graph $K_{3,3}$ with $3$ vertices in each of the two parts)

## Properties

This section introduces the properties of plane graphs.

### Faces and their degrees

Let $G$ be a plane graph; the edges of $G$ divide the plane where $G$ lies into several regions, each region being called a **face** of $G$. Among them, the unbounded face is called the **unbounded face** or **external face**, and the bounded ones are called finite faces or internal faces. Every plane graph has one and only one external face.

The circuit composed of all the edges surrounding each face is called the **boundary** of that face, and the edges in the boundary are said to be **incident** with that face. The length of the boundary is called the **degree** of that face. When computing the degree of a face, each bridge is counted twice. The sum of the degrees of all faces in a plane graph equals $2$ times the number of edges $|E|$.

In a plane graph, the boundary of a degree-$1$ face corresponds to a self-loop of the graph, and the boundary of a degree-$2$ face usually corresponds to a pair of multiple edges of the graph[^face-2]. In a simple connected plane graph with number of vertices $|V|\ge 3$, all face degrees are at least $3$.

### Euler's formula

An important property of plane graphs is **Euler's formula**. It gives the relationship between the number of vertices $|V|$, the number of edges $|E|$, and the number of faces $|F|$ of a graph.

???+ note "Euler's formula"
    For a connected plane graph $G$, we have
    
    $$
    |V| - |E| + |F| = 2.
    $$

??? note "Proof"
    Apply mathematical induction on the number of faces $|F|$. The induction base is $|F|=1$. At this time, the plane graph has one and only one external face, and all edges are bridges. So, the graph $G$ is a tree, and necessarily $|E|=|V|-1$; substituting into Euler's formula, we find that it holds. Assume Euler's formula holds for plane graphs with number of faces $|F| = k$. For a plane graph $G$ with number of faces $|F|=k + 1$, there must exist a non-bridge edge $e$, which is the common edge of two different faces. Deleting edge $e$ from the graph gives the graph $G-e$, which has $|V|$ vertices, $|E|-1$ edges, and $|F|-1$ faces. By the induction hypothesis, Euler's formula holds for the graph $G-e$, i.e. $|V|-(|E|-1)+(|F|-1)=2$; rearranging gives Euler's formula for the graph $G$. So, by mathematical induction, Euler's formula holds for all plane graphs.

???+ note "Corollary"
    For a plane graph $G$ with $k$ connected components, we have
    
    $$
    |V| - |E| + |F| = k + 1.
    $$

??? note "Proof"
    Each connected component of the graph $G$ is a plane graph, but these connected components share the same external face. So, directly applying Euler's formula to these connected components and summing them up, the total number of vertices and total number of edges are both correct, but the total number of faces is $(k-1)$ too many, because the unique external face is counted $k$ times in total. Taking this correction into account, we obtain $|V|-|E|+|F| = 2k - (k-1) = k+1$.

From this, we can derive the quantitative relationship between the edges and vertices of a plane graph.

???+ note "Theorem"
    For a plane graph $G$ with $k$ connected components, if every face of the graph $G$ has degree at least $l \ge 3$, then we have
    
    $$
    |E| \le \dfrac{l}{l-2}(|V|-k-1).
    $$

??? note "Proof"
    Because the degree of each face of $G$ is at least $l$, the sum of the degrees of all faces is at least $l|F|$, i.e. $2|E| \ge l|F|$. Substituting into the corollary of Euler's formula $|V| - |E| + |F| = k + 1$, we obtain
    
    $$
    2|E| \ge l(k + 1 - |V| + |E|).
    $$
    
    Using $l \ge 2$ to solve for $|E|$, we obtain
    
    $$
    |E| \le \dfrac{l}{l-2}(|V|-k-1).
    $$

???+ note "Corollary"
    Let $G$ be a simple planar graph with $|V|\ge 3$; then, we have
    
    $$
    |E| \le 3|V|-6.
    $$

??? note "Proof"
    When $G$ is connected, all face degrees are at least $3$. In the above theorem, taking $k=1$ and $l=3$, we obtain $|E|\le 3|V|-6$.
    
    When $G$ is disconnected, there are two cases:
    
    -   If there exists a connected component with at least $3$ vertices, then for these connected components with at least $3$ vertices we can respectively establish the inequality $|E_i|\le 3|V_i|-6$. Because those connected components with fewer than $3$ vertices must have $|E_i|\le |V_i| \le 3|V_i|$. Adding up the inequalities corresponding to all connected components, we obtain $|E|\le 3|V|-6$.
    -   If all connected components have fewer than $3$ vertices, then overall we must have $|E|\le |V|$. And because when $|V|\ge 3$, $|V|\le 3|V|-6$, so $|E|\le 3|V|-6$ still holds.
    
    In summary, the proposition is proved.

This corollary shows that a simple planar graph is a sparse graph.

### Dual graph

Every plane graph has a corresponding (geometric) dual graph.

![](images/planar-dual-1.svg)

Let $G$ be a plane graph; we can draw the graph $G^*$ as follows:

1.  Inside each face $f_i$ of $G$, draw a point $v_i^*$.
2.  For each edge $e$ of $G$, if $e$ is on the common boundary of faces $f_i$ and $f_j$, draw an edge $e^*$ connecting $v_i^*$ and $v_j^*$, so that it intersects $e$ exactly once and does not intersect other edges of graph $G$ or graph $G^*$. In particular, when $e$ appears only on the boundary of one face $f_i$, we need to draw a self-loop incident with $v_i^*$, so that it intersects $e$.

The graph $G^*$ obtained this way is called the **dual graph** of the graph $G$.

???+ note "Theorem"
    Let the graph $G^*$ be the dual graph of the plane graph $G$. Then, the graph $G^*$ is a connected plane graph. Moreover, the graph $G^{**}$ is isomorphic to $G$ if and only if $G$ is a connected graph.

??? note "Proof"
    The fact that the graph $G^*$ is a plane graph can be guaranteed by its construction process. We still need to prove that the graph $G^*$ is connected. For any two vertices $v^*_i,v^*_j$ in the graph $G^*$, let the line segment connecting $v^*_i$ and $v^*_j$ in the plane pass through the faces and edges in the graph $G$ in order as $f_i,e_{s_1},f_{s_1},\cdots,f_{s_{r-1}},e_{s_r},f_j$, which respectively correspond to the vertices and edges $v_i^*,e_{s_1}^*,v^*_{s_1},\cdots,v^*_{s_{r-1}},e^*_{s_r},v^*_j$ in the dual graph. From the construction of the graph $G^*$, we know that adjacent vertices and edges in the sequence are incident, so this describes a walk in the graph $G^*$. So, the graph $G^*$ is connected.
    
    The graph $G^{**}$ is the dual graph of the graph $G^*$, and must be connected. So, for $G$ to be isomorphic to $G^{**}$, a necessary condition is that the graph $G$ is connected. Next, we need to prove that this condition is also sufficient. For this, we only need to prove that when the graph $G$ is connected, the graph $G$ satisfies the construction requirements of the dual graph of the graph $G^*$. Because the edges of the graph $G^*$ and the edges of the graph $G$ naturally correspond, we only need to prove that each face of the graph $G^*$ contains exactly one vertex of the graph $G$. For any face $f^*$ of the graph $G^*$, let $e^*$ be an edge on its boundary; then one of the endpoints of the corresponding edge $e$ in the graph $G$ must be within the face $f^*$; therefore, there is at least one vertex of the graph $G$ in the face $f^*$. Since both the graph $G^*$ and the graph $G$ are connected, Euler's formula holds; and the graph $G$ and the graph $G^*$ have the same number of edges, the number of faces of the graph $G$ equals the number of vertices of the graph $G^*$, so the number of vertices of the graph $G$ equals the number of faces of the graph $G^*$. So, each face of the graph $G^*$ has exactly one vertex of the graph $G$. The proposition is proved.

There are many correspondences between the structure of a plane graph and its dual graph:

-   Faces in $G$ correspond to points in $G^*$, edges in $G$ correspond to edges in $G^*$, and points in $G$ correspond to faces in $G^*$.
-   Self-loops in $G$ correspond to bridges in $G^*$, and self-loops in $G^*$ correspond to bridges in $G$.
-   Edge cut sets in $G$ correspond to circuits in $G^*$, and circuits in $G^*$ correspond to edge cut sets in $G$.

It should be noted that the concept of the dual graph holds only for a specific plane graph, and cannot be defined on an arbitrary planar graph. In fact, the dual graphs of two isomorphic plane graphs are not necessarily isomorphic. That is to say, the dual graphs of different planar embeddings of the same graph may not be the same.

???+ example "Example"
    The figure below draws two isomorphic plane graphs whose dual graphs are not isomorphic.
    
    ![](images/planar-dual-2.svg)
    
    The reason the dual graphs are not isomorphic is that the right figure has a degree-1 face, so its dual graph has a degree-1 vertex, while the left figure does not.

Transforming a problem on a planar graph to its dual graph is sometimes easier to solve. A typical example is that the planar-graph [minimum cut](./flow/min-cut.md) problem can be transformed into the dual-graph [shortest path](./shortest-path.md) problem. Let $G$ be a planar graph with edge weights, and $s,t$ be two of its vertices; we need to find the minimum $s$-$t$ cut.

![](images/planar-dual-3.svg)

As shown in the figure, by choosing an appropriate planar embedding, we make $s,t$ appear on the boundary of the external face of the graph $G$. In addition, add rays extending out from $s$ and $t$, dividing the external face into two parts $f_{+}$ and $f_{-}$. Based on this graph, build the dual graph, and assign the edge weights to the corresponding edges in the dual graph. Then, the path between the vertices corresponding to faces $f_{+}$ and $f_{-}$ in the dual graph $G^*$ (thick red line) corresponds one-to-one with the $s$-$t$ edge cut set of the graph $G$ (thick black line), and the two have the same weight. In this way, solving the shortest path in the dual graph gives the minimum $s$-$t$ cut in the graph $G$.

A common misconception is to claim, based on the above transformation method, that the planar-graph minimum cut equals the dual-graph shortest path. In fact, it only applies to the case where there exists a planar embedding of $G$ such that $s,t$ are on the same face; it is just that in algorithm-competition problems examining this knowledge point, the given graph often has, and comes with, such a planar embedding. Here we give a theorem that can be used to determine its existence.

???+ note "Theorem"
    For two vertices $s,t$ of a planar graph $G=(V,E)$, there exists a planar embedding of $G$ such that $s,t$ are on the same face if and only if $(V,E \cup \{(s,t)\}$ is a planar graph.

??? note "Proof"
    If there exists a planar embedding of $G$ such that $s,t$ are on the same face, then we can add an edge $(s,t)$ within this face, maintaining the planarity of the graph.
    
    If $(V, E \cup \{(s,t)\})$ is a planar graph, then take any of its planar embeddings; $s,t$ are both on the face where edge $(s,t)$ is located. After deleting $(s,t)$, $s,t$ are still on the same face. The proposition is proved.

For example, in the figure below, after adding edge $(s,t)$ we obtain the non-planar graph $K_5$, so it does not have such a planar embedding, and the above transformation does not apply.

![](images/planar-st.svg)

### More results

Of course, plane graphs also have many famous results. This section simply lists them, but does not discuss them.

???+ note "Four color theorem"
    (Self-loop-free) plane graphs are all $4$-colorable.

???+ note "Fáry's theorem"
    A simple planar graph always has a planar embedding such that all edges of the graph are straight line segments.

???+ note "Theorem (Wood)"
    A planar graph has at most $8|V|-16$ maximal cliques.

???+ note "Theorem (Tutte)"
    $4$-vertex-connected planar graphs are all Hamiltonian graphs.

## Determination

This section discusses methods for determining, given a graph, whether it is a planar graph.

### Forbidden graphs

The most classic characterization of planar graphs is given using **forbidden graphs**.

First, $K_5$ and $K_{3,3}$ are not planar graphs.

???+ note "Theorem"
    $K_5$ and $K_{3,3}$ are not planar graphs.

??? note "Proof"
    The previous text shows that a simple connected plane graph with $|V|\ge 3$ needs to satisfy
    
    $$
    |E| \le \dfrac{l}{l-2}(|V|-2).
    $$
    
    where $l$ is the minimum value of the face degree. For $K_5$, we have $l=3,~|V|=5,~|E|=10$, so $K_5$ cannot be drawn as a plane graph. For $K_{3,3}$, we have $l=4,~|V|=6,~|E|=9$, so $K_{3,3}$ cannot be drawn as a plane graph.

In fact, they are the smallest structures that make a graph non-planar. That is to say, as long as a graph does not contain (in some way) these two graphs as substructures, the graph must be planar.

The first planarity determination theorem is Kuratowski's theorem. It uses the concept of graph homeomorphism: if two graphs $G_1$ and $G_2$ are isomorphic, or become isomorphic after repeatedly inserting or removing degree-$2$ vertices, then the two are said to be **homeomorphic**. From this, we can state the following result:

???+ note "Kuratowski's theorem"
    A graph $G$ is a planar graph if and only if $G$ does not contain a subgraph homeomorphic to $K_5$ or $K_{3,3}$.

Another theorem related to this is Wagner's theorem. It uses the contraction operation to characterize planar graphs. The contraction operation means repeatedly contracting an edge of the graph into a point multiple times. From this, we can state the following result:

???+ note "Wagner's theorem"
    A graph $G$ is a planar graph if and only if $G$ has no subgraph that can be contracted to $K_5$ or $K_{3,3}$.

That planar graphs do not contain these types of subgraphs is relatively obvious, so the key part of both theorems lies in the sufficiency of the corresponding forbidden-graph condition. Since a subgraph homeomorphic to $K_5$ or $K_{3,3}$ can definitely be contracted to them, but the converse does not necessarily hold, Kuratowski's theorem provides a weaker and easier-to-check condition for determining planar graphs.

### Planarity determination algorithm

Although it does not look easy, the planarity determination problem actually has many linear algorithms. However, since the implementations of these algorithms are usually quite complex, they almost never appear in algorithm competitions.

The earliest linear algorithm is the Hopcroft–Tarjan algorithm[^ht74], but its implementation is quite complex. The de Fraysseix–Ossona de Mendez–Rosenstiehl algorithm (also called the LR planarity algorithm)[^dor06][^df08][^bra09] further improves the process of the Hopcroft–Tarjan algorithm, and is one of the best planarity determination algorithms at present. The NetworkX library of Python [implements](https://github.com/networkx/networkx/blob/main/networkx/algorithms/planarity.py) this algorithm.

Another equally excellent algorithm is the Boyer–Myrvold algorithm[^bm99][^bm04]. It can determine whether a given graph is planar in linear time. Moreover, if the graph is planar, the algorithm will output a planar embedding; otherwise, the algorithm will output a Kuratowski subgraph (i.e. a subgraph homeomorphic to $K_5$ or $K_{3,3}$). The Boost library of C++ [implements](https://www.boost.org/doc/libs/1_67_0/boost/graph/planar_detail/boyer_myrvold_impl.hpp) this algorithm.

For more related algorithms, refer to the literature provided at the end of the article.

## Special plane graphs

This section introduces several classes of special planar graphs.

### Maximal plane graph

For a simple planar graph $G$, if adding an edge between any of its non-adjacent vertices makes the resulting graph no longer a planar graph, then $G$ is called a **maximal planar graph**. The planar embedding of a maximal planar graph is called a **maximal plane graph**.

???+ note "Theorem"
    A maximal planar graph $G$ must be connected. Moreover, when the number of vertices $|V|\ge 3$, the graph $G$ has no bridge.

??? note "Proof"
    If a planar graph $G$ is disconnected, then take any of its planar embeddings; we can choose two vertices belonging to different connected components and connect them within the external face; the obtained graph is obviously still a plane graph, which shows that the graph $G$ is not a maximal planar graph. So, if the graph $G$ is a maximal planar graph, it must be connected.
    
    If a planar graph $G$ has number of vertices $|V|\ge 3$, and $G$ has a bridge $e=(u,v)$, then the graph $G - e$ after deleting edge $e$ has exactly two connected components, and $u,v$ belong to different connected components. Assume the connected component where $v$ is located has at least two vertices. Then, we can first draw the connected component $G_1$ where $u$ is located on the plane, and choose any face $f$ in the graph $G_1$ whose boundary contains $u$, and draw the other connected component $G_2$ in the face $f$. Since $G_2$ is a simple graph, the boundary of its external face is definitely not a self-loop, so there is at least another vertex $w\neq u,v$. Connecting $v,w$ respectively to $u$, we obtain a plane graph containing $G$ as a subgraph. So, the graph $G$ is not a maximal planar graph. Therefore, a maximal planar graph with number of vertices $|V|\ge 3$ definitely has no bridge.

The structure of a maximal plane graph can be described more accurately.

???+ note "Theorem"
    For a plane graph $G$ with number of vertices $|V|\ge 3$, it is a maximal plane graph if and only if it is a simple graph and every face has degree $3$.

??? note "Proof"
    The sufficiency of the condition is obvious. We only need to explain the necessity, i.e. to prove: in a maximal plane graph $G$ with number of vertices $|V|\ge 3$, every face has degree $3$. Since the graph $G$ is a connected simple plane graph and $|V|\ge 3$, all face degrees are at least $3$. So, assume the proposition does not hold; then there must exist a face $f$ whose boundary length is at least $4$. And because the graph $G$ has no bridge, this boundary can only be a cycle. Let this cycle be $v_1v_2v_3v_4\cdots v_1$. Then, if $v_1$ and $v_3$ are not adjacent, then connecting $v_1$ and $v_3$ within the face $f$ will not destroy the planarity, contradicting the maximality of $G$, so $v_1$ and $v_3$ are adjacent; similarly, $v_2$ and $v_4$ are adjacent. But, the edges $(v_1,v_3)$ and $(v_2,v_4)$ will both not appear in the face $f$. This means that the two edges must be outside the face $f$. But this is impossible: no matter how they are drawn, these two edges must intersect. So, there is no face of degree higher than $3$ in the graph $G$. The original proposition is proved.

???+ note "Corollary"
    For a graph $G$ with number of vertices $|V|\ge 3$, we always have number of edges $|E|=3|V|-6$ and number of faces $|F|=2|V|-4$.

Since in a maximal plane graph, each face is enclosed by three edges, a maximal plane graph is also called a **plane triangulation**.

### Outerplanar graph

Let $G$ be a planar graph; if $G$ has a planar embedding $\tilde{G}$ such that all vertices in $G$ are on the boundary of one face of $\tilde{G}$, then $G$ is called an **outerplanar graph**. This embedding is also called an outerplanar embedding or **outerplane graph**. Usually the face whose boundary passes through all vertices is drawn as the external face.

![](images/planar-outer.svg)

Outerplanar graphs are all planar graphs, but the converse does not necessarily hold. Outerplanar graphs can also be characterized using forbidden graphs.

???+ note "Theorem"
    A graph $G$ is an outerplane graph if and only if $G$ does not contain a subgraph homeomorphic to $K_4$ or $K_{2,3}$.

For outerplanar graphs, we can likewise discuss the concept of a maximal outerplanar graph. For a simple outerplanar graph $G$, if adding an edge between any of its non-adjacent vertices makes the resulting graph no longer an outerplanar graph, then $G$ is called a **maximal outerplanar graph**. The outerplanar embedding of a maximal outerplanar graph is called a **maximal outerplane graph**. A maximal outerplane graph is actually a triangulation of a polygon on the plane.

???+ note "Theorem"
    For a maximal outerplane graph $G$ with number of vertices $|V|\ge 3$, where all vertices are on the boundary of the external face, then the graph $G$ has exactly $|V|-2$ internal faces.

??? note "Proof"
    Apply mathematical induction on $|V|$. The induction base is $|V|=3$. At this time, the graph $G$ is a triangle, has only $1$ internal face, and the proposition holds. Assume the proposition holds for $|V| = k$. Now we want to prove that when $|V| = k+1$, the proposition still holds.
    
    First, the graph $G$ must have a degree-$2$ vertex. Otherwise, except for the adjacent vertices on the boundary of the external face, all vertices need to be connected to a third vertex. Without loss of generality, number the vertices on the boundary of the external face in order, and for each $i = 1,2,\cdots,k+1$, define $f(i)$ as the smallest number of a vertex connected to vertex $i$ and whose number is not adjacent to it. Consider the possible values of $f(i)$. First, $1 < f(1)$. Since point $1$ is already connected to $f(1)$, the connection between point $2$ and $f(2)$ cannot cross edge $(1,f(1))$, so we must have $1 < 2 < f(2) < f(1)$. Similarly, $2 < 3 < f(3) < f(2)$. Since there are only finitely many vertices, this gradually shrinking process must terminate after finitely many steps. Let $i^*$ be the maximum number $i$ satisfying $1 < \cdots < i-1 < i < f(i) < f(i-1) < \cdots < f(1)$. Then, since point $i^*$ and point $f(i^*)$ are not adjacent, we must have $i^* < i^* + 1 < f(i^*)$. And repeating the previous argument, we should still have $i^* < i^*+1 < f(i^*+1) < f(i^*)$, which contradicts the maximality of $i^*$. This contradiction shows that the graph $G$ must have a degree-$2$ vertex.
    
    Let $v$ be a degree-$2$ vertex. Deleting this vertex from the graph $G$, we obtain the outerplane graph $G-v$ with $k$ vertices. It must be a maximal outerplane graph, otherwise the method of legally adding edges on it would also apply to the graph $G$. By the induction hypothesis, the graph $G-v$ has exactly $k-2$ internal faces, and when deleting vertex $v$, exactly one internal face of the graph $G$ is reduced. So, the number of internal faces of the graph $G$ is $k-1$. The proposition is proved.

???+ note "Theorem"
    For an outerplane graph $G$ with number of vertices $|V|\ge 3$, where all vertices are on the boundary of the external face, then the graph $G$ is a maximal outerplane graph if and only if the external face boundary of the graph $G$ is a cycle of length $|V|$, and all internal face boundaries are cycles of length $3$.

??? note "Proof"
    The sufficiency is obvious. In fact, consider connecting two non-adjacent vertices on the boundary of the external face. If the connection occurs in the external face, then all vertices cannot all appear on the boundary of one face; otherwise, their connection must intersect the boundary of an internal face.
    
    Next, prove the necessity. Assume the external face boundary $v_1v_2v_3\cdots v_nv_1~(n = |V|)$ of the graph $G$ is not a cycle. Then, it repeatedly passes through a vertex multiple times, i.e. there exist $i\neq j$ and $i-j\neq\pm 1\pmod{n}$ such that $v_i=v_j$. Without loss of generality, assume $1 < i < j < n$. At this time, the edges incident with $v_{i-1}$ can only appear inside the bounded region enclosed by the circuit $v_jv_{j+1}\cdots v_nv_1\cdots v_{i-1}v_i$, and the edges incident with $v_{i+1}$ can only appear inside the bounded region enclosed by the circuit $v_iv_{i+1}\cdots v_{j-1}v_{j}$, so $v_{i-1}$ and $v_{i+1}$ cannot be adjacent. We can add an edge $e$ connecting $v_{i-1}$ and $v_{i+1}$ within the external face, obtaining the graph $G+e$. This is obviously also a plane graph, and the external face boundary contains all vertices. This contradicts the maximal outerplanarity of the graph $G$. So, the external face of the graph $G$ must be a cycle of length $|V|$. And the reason that the internal face boundaries of the graph $G$ are all cycles of length $3$ is consistent with the maximal plane graph, and is not repeated here.

???+ note "Corollary"
    For a maximal outerplane graph $G$ with number of vertices $|V|\ge 3$, we have:
    
    1.  $|E|=2|V|-3$.
    2.  In $G$ there are at least $3$ vertices with degree less than or equal to $3$, and at least $2$ vertices with degree $2$.
    3.  The vertex connectivity of $G$ is $2$.

## Exercises

-   [Luogu P3209 \[HNOI2010\] Plane graph determination](https://www.luogu.com.cn/problem/P3209)
-   [Luogu P3249 \[HNOI2016\] Mining area](https://www.luogu.com.cn/problem/P3249)
-   [Luogu P4001 \[ICPC-Beijing 2006\] Wolf catching rabbits](https://www.luogu.com.cn/problem/P4001)
-   [Luogu P4073 \[WC2013\] Plane graph](https://www.luogu.com.cn/problem/P4073)
-   [Luogu P7295 \[USACO21JAN\] Paint by Letters P](https://www.luogu.com.cn/problem/P7295)

## References and notes

-   [Planar graph - Wikipedia](https://en.wikipedia.org/wiki/Planar_graph)
-   [Planarity testing - Wikipedia](https://en.wikipedia.org/wiki/Planarity_testing)
-   Bondy, John Adrian, and Uppaluri Siva Ramachandra Murty. Graph theory with applications. Vol. 290. London: Macmillan, 1976.
-   Diestel, Reinhard. Graph theory. Vol. 173. Springer Nature, 2025.
-   Patrignani, Maurizio. "Planarity Testing and Embedding." (2013): 1-42.

[^face-2]: But this is not the only possibility. Two nested self-loops also form a degree-2 face. In addition, having a degree-2 face does not necessarily mean the graph is not simple; for example, in a graph with only one edge, the unique face (i.e. the external face) is also of degree 2.

[^ht74]: Hopcroft, John, and Robert Tarjan. "Efficient planarity testing." Journal of the ACM (JACM) 21, no. 4 (1974): 549-568.

[^dor06]: De Fraysseix, Hubert, Patrice Ossona De Mendez, and Pierre Rosenstiehl. "Trémaux trees and planarity." International Journal of Foundations of Computer Science 17, no. 05 (2006): 1017-1029.

[^df08]: De Fraysseix, Hubert. "Trémaux trees and planarity." Electronic Notes in Discrete Mathematics 31 (2008): 169-180.

[^bra09]: Brandes, Ulrik. "The left-right planarity test." Manuscript submitted for publication 3 (2009).

[^bm99]: Boyer, John M., and Wendy J. Myrvold. "Stop Minding Your p's and q's: A Simplified O (n) Planar Embedding Algorithm." In SODA, vol. 99, pp. 140-146. 1999.

[^bm04]: Boyer, John M., and Wendy J. Myrvold. "Simplified o (n) planarity by edge addition." Graph Algorithms and Applications 5 (2006): 241.
