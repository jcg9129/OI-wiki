## Introduction

Before reading the following content, please be sure to understand the [graph-theory related concepts](./concept.md) section.

Related reading: [Cut vertices and bridges](./cut.md)

## Definition

For more rigorous definitions of cut vertices and bridges, see [graph-theory related concepts](./concept.md).

In a connected undirected graph, for two points $u$ and $v$, if no matter which edge is deleted (only one can be deleted) they cannot be made disconnected, then we say $u$ and $v$ are **edge-biconnected**.

In a connected undirected graph, for two points $u$ and $v$, if no matter which vertex is deleted (only one can be deleted, and $u$ and $v$ themselves cannot be deleted) they cannot be made disconnected, then we say $u$ and $v$ are **vertex-biconnected**.

Edge-biconnectivity is transitive, i.e. if $x,y$ are edge-biconnected and $y,z$ are edge-biconnected, then $x,z$ are edge-biconnected.

Vertex-biconnectivity is **not** transitive; a counterexample is the figure below, where $A,B$ are vertex-biconnected, $B,C$ are vertex-biconnected, but $A,C$ are **not** vertex-biconnected.

![bcc-counterexample.png](./images/bcc-0.svg)

For a **maximal** edge-biconnected subgraph in an undirected graph, we call this subgraph an **edge-biconnected component**.

For a **maximal** vertex-biconnected subgraph in an undirected graph, we call this subgraph a **vertex-biconnected component**.

## DFS spanning tree

For a connected undirected graph, we can start DFS from any point to obtain a DFS spanning tree of the original graph (with the point where DFS started as the root); the edges on this spanning tree are called **tree edges**, and edges not on the spanning tree are called **non-tree edges**.

Because of the property of DFS, we can guarantee that for the two points connected by any non-tree edge, one is an ancestor of the other on the spanning tree.

The DFS code is as follows:

???+ note "Implementation"
    === "C++"
        ```cpp
        void DFS(int p) {
          visited[p] = true;
          for (int to : edge[p])
            if (!visited[to]) DFS(to);
        }
        ```
    
    === "Python"
        ```python
        def DFS(p):
            visited[p] = True
            for to in edge[p]:
                if visited[to] == False:
                    DFS(to)
        ```

## Edge-biconnected components

???+ note "[Example problem: Luogu P8436 【Template】Edge-Biconnected Component](https://www.luogu.com.cn/problem/P8436)"
    For a graph with $n$ nodes and $m$ undirected edges, output the number of its edge-biconnected components, and output each edge-biconnected component.

### Tarjan's algorithm 1

The process of finding biconnected components with Tarjan is similar to finding strongly connected components; you can first read the Tarjan algorithm of [strongly connected components](./scc.md).

We consider first finding all bridges, then DFS to find the edge-biconnected components.

For finding bridges see the bridges part of [cut vertices and bridges](./cut.md).

Time complexity $O(n+m)$.

??? note "Example code"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_1.cpp"
    ```

### Tarjan's algorithm 2

We first summarize an important property: in an undirected graph, an edge on the DFS spanning tree is either a tree edge or a non-tree edge.

Let's connect this with the method of finding strongly connected components; in an undirected graph, as long as a component has no bridge, then on the DFS spanning tree, all its points are in the same strongly connected component.

Conversely, a strongly connected component on the DFS spanning tree is an edge-biconnected component in the original undirected graph.

We can find that the process of finding edge-biconnected components is actually the process of finding strongly connected components.

Time complexity $O(n+m)$.

??? note "Example code"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_2.cpp"
    ```

### Difference algorithm

Similar to Tarjan's algorithm 1, we first find all bridges, then use differencing to find the edge-biconnected components.

First, perform DFS on the original graph.

![bcc-1.png](./images/bcc-1.svg)

As shown above, the black and green edges are tree edges, and the red edges are non-tree edges. The two endpoints of each non-tree edge uniquely correspond to a simple path composed of tree edges on the tree; we say this non-tree edge **covers** all edges on this simple path.

In the figure, the green tree edges are covered by **at least** one non-tree edge, and the black tree edges are not covered by **any** non-tree edge.

Obviously, **non-tree edges** and **green tree edges** are definitely not bridges, and **black tree edges** are definitely bridges.

First consider a brute-force approach: for each non-tree edge, set each tree edge it covers to green one by one, with time complexity $O(nm)$.

Consider optimizing with differencing. For each non-tree edge, apply a `-1` mark at the endpoint with smaller tree depth, and apply a `+1` mark at the endpoint with larger tree depth, then find the sum of marks inside the subtree of each point in $O(n)$.

For a point $u$, the sum of marks inside its subtree equals the number of non-tree edges covering the tree edge between $u$ and $fa_u$. If this value equals $0$, then the tree edge between $u$ and $fa_u$ is a **bridge**.

Then use DFS to find the edge-biconnected components.

Time complexity $O(n+m)$.

??? note "Example code"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_4.cpp"
    ```

???+ note "[#2788.「CEOI2015 Day1」Pipe](https://loj.ac/p/2788)"
    Given an undirected graph with $N$ points and $M$ edges, not guaranteed connected. Regarding each connected component as a subgraph, find the bridges in each subgraph. **You only have 16 MB of memory space.**

??? note "Solution"
    The biggest feature of this problem is that you cannot store all the edges.
    
    Consider optimizing edge storage; if a non-tree edge is completely covered by another non-tree edge, then this edge is useless.
    
    Just maintain it with a DSU.

## Vertex-biconnected components

???+ note "[Example problem: Luogu P8435 【Template】Vertex-Biconnected Component](https://www.luogu.com.cn/problem/P8435)"
    For a graph with $n$ nodes and $m$ undirected edges, output the number of its vertex-biconnected components, and output each vertex-biconnected component.

### Tarjan's algorithm

You need to first learn cut vertices; you can first see the cut-vertices part of [cut vertices and bridges](./cut.md).

First give two properties:

1.  Two vertex-biconnected components have at most one common point, and it must be a cut vertex.
2.  For a vertex-biconnected component, the point with the smallest dfn value in the DFS search tree must be a cut vertex or the tree root.

According to the second property, we discuss by cases:

1.  When this point is a cut vertex, it must be the root of the vertex-biconnected component, because once its parent node is included, it is still a cut vertex.
2.  When this point is the tree root:
    1.  It has two or more subtrees, it is a cut vertex.
    2.  It has only one subtree, it is the root of a vertex-biconnected component.
    3.  It has no subtree, regarded as a vertex-biconnected component.

??? note "Example code"
    ```cpp
    --8<-- "docs/graph/code/bcc/bcc_3.cpp"
    ```

### Difference algorithm

![bcc-2.png](./images/bcc-2.svg)

As shown above, the black edges are tree edges and the red edges are non-tree edges; the two endpoints of each non-tree edge uniquely correspond to a simple path composed of tree edges on the tree.

Consider a new graph, where each point in the new graph corresponds to each tree edge in the original graph (represented by blue points in the figure). For each non-tree edge in the original graph, connect the blue points in the new graph corresponding to all edges in the simple path on the tree corresponding to this non-tree edge into a connected component (reflected by blue edges in the figure).

In this way, a point is **not** a cut vertex if and only if the blue points in the new graph corresponding to all edges connected to it **belong** to the same connected component.

Two points **are** vertex-biconnected if and only if the blue points in the new graph corresponding to all edges in their path on the tree of the original graph **belong** to the same connected component, i.e. each connected component formed by blue points in the figure is a vertex-biconnected component.

The connectivity relation between blue points can be maintained with a method similar to the differencing used when finding edge-biconnected components, with time complexity $O(n+m)$.
