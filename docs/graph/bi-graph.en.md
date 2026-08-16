## Introduction

A bipartite graph is a class of graphs with a special structure. Its vertex set can be divided into two mutually disjoint subsets, such that every edge in the graph connects a pair of points between these two sets, without connecting points within the same set.

Thanks to this simple structure, bipartite graphs not only exhibit many elegant properties, but are also widely used in real-life modeling scenarios, such as task assignment, recommendation systems, matching markets, etc. Many optimization problems that are difficult on general graphs can be solved efficiently and accurately on bipartite graphs.

## Definition

If the vertex set $V$ of a graph $G=(V,E)$ can be divided into two mutually disjoint subsets $X$ and $Y$, such that the two endpoints of every edge $e\in E$ belong to $X$ and $Y$ respectively, then the graph $G$ is called a **bipartite graph**. The sets $X$ and $Y$ are often called its two **parts**, or respectively called the left part and right part of the bipartite graph. When the two parts $X$ and $Y$ of a bipartite graph are known, the bipartite graph $G$ can also be represented by the triple $(X, Y, E)$.

A typical bipartite graph is shown in the figure below.

![](./images/bi-graph-1.svg)

Trees, even cycles, grid graphs, etc. are all common examples of bipartite graphs.

## Characterization

A bipartite graph can also be equivalently defined by the following properties:

-   The graph $G$ is 2-colorable. That is, all vertices of the graph can be colored with at most two colors, guaranteeing that adjacent vertices have different colors.
-   There is no odd-length cycle in the graph $G$.

Obviously, the first property is equivalent to the definition of a bipartite graph: just color the two parts of the bipartite graph with one color each.

The second property is slightly more complex. We can consider trying to color the graph $G$ with two colors. Because the coloring of different connected components does not interfere with each other, we only need to consider the connected components one by one. Choose any vertex $s$ in a connected component, perform DFS, and record the distance from each vertex $v$ in the connected component to $s$. Starting from $s$, by induction on the DFS spanning tree, we know that if there is a feasible coloring method, it must color into two colors according to the parity of the distance from each vertex $v$ to the start point $s$.

![](./images/bi-graph-2.svg)

Then consider those edges not in the spanning tree. If the two endpoints of these non-tree edges have different colors, then it means the current coloring scheme is feasible; otherwise, there is no feasible scheme. Further, two vertices having different colors if and only if their distances to the tree root $s$ are one odd and one even, which is in turn equivalent to the addition of this non-tree edge forming an even cycle rather than an odd cycle. Therefore, as long as there is no odd cycle, these non-tree edges must connect points of different colors, so the whole graph can be colored with two colors, and the graph must be a bipartite graph.

## Determination

To determine whether a graph is a bipartite graph, we only need to use the above equivalent characterization and try to color the bipartite graph. For this, we can use [DFS](./dfs.md) or [BFS](./bfs.md) to traverse this graph. If we find an odd cycle, i.e. a situation where coloring is impossible occurs, then it is not a bipartite graph; otherwise, it is a bipartite graph.

The specific process is as follows:

-   Traverse the vertices; if we find a not-yet-colored vertex, it means we found a new connected component.
-   Choose any color to color this vertex, and take it as the start point to do [DFS](./dfs.md) or [BFS](./bfs.md), trying to color this connected component.
-   When traversing adjacent vertices, if we find an already-colored vertex, check whether the color is the same as the current vertex. If the same, then it is not a bipartite graph, return directly; otherwise, continue traversing.
-   If we find a not-yet-colored vertex, color the not-yet-colored vertex with the opposite color of the current vertex.

The reference code is as follows:

???+ example "Reference code"
    ```cpp
    --8<-- "docs/graph/code/bi-graph/check-bipartite.cpp:core"
    ```

The time complexity is $O(|V|+|E|)$.

## Applications

Because of the simple structure, many graph-theory optimization problems can be efficiently solved on bipartite graphs. For details refer to the relevant main entries.

-   Maximal clique (trivial)
-   Minimum vertex coloring (trivial)
-   [Minimum edge coloring](./color.md#constructive-proof-of-vizings-theorem-for-bipartite-graphs)
-   [Maximum matching](./graph-matching/bigraph-match.md)
-   [Minimum edge cover](./graph-matching/graph-match.md#minimum-weight-edge-cover)
-   [Minimum vertex cover](./graph-matching/bigraph-match.md#bipartite-graph-minimum-vertex-cover)
-   [Maximum independent set](./graph-matching/bigraph-match.md#bipartite-graph-maximum-independent-set)
-   [Maximum weight matching](./graph-matching/bigraph-weight-match.md)
-   [Bipartite graph game](../math/game-theory/impartial-game.md#bipartite-graph-game)
