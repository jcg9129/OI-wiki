author: GitPinkRabbit, Early0v0, Backl1ght, mcendu, ksyx, iamtwz, Xeonacid, kenlig, Menci, Enter-tainer, CCXXXI, hcx2012Git

Before reading the following content, please be sure to understand the [graph-theory related concepts](./concept.md) section.

Related reading: [cut vertices and bridges](./cut.md).

## Introduction

As is well known, trees (or forests) have very good properties and are easy to maintain with many common data structures.

General graphs, however, do not have such good properties; fortunately, sometimes we can transform certain problems on general graphs into consideration on trees.

The block forest (or Round-square tree) [^ref1] is a method of turning a graph into a tree. This article will introduce the construction, properties, and some applications of the block forest.

Limited by length, some conclusions in this article are not proved; the reader may understand or prove them on their own.

## Definition

The block forest was originally a tool for handling "cactus graphs" (undirected graphs where each edge is in no more than one simple cycle), but by exploring more of its properties, we can sometimes use it on general undirected graphs.

To introduce the block forest, we first need to introduce **vertex-biconnected components**.

One definition of a **vertex-biconnected graph** is: between any two distinct points in the graph there are at least two vertex-disjoint paths.  
Vertex-disjoint refers both to the points on a path not repeating (a simple path), and to the intersection of the two paths being empty (of course, the paths must both pass through the departure point and the arrival point, which is not within consideration).

We can find that for a graph with only one point, it is relatively hard to define whether it is a vertex-biconnected component; here we first do not consider graphs with node count $1$.

A nearly equivalent definition is: a graph with no cut vertex.  
This definition only fails when the graph has only two points and one edge connecting them. It has no cut vertex, but two disjoint paths cannot be found, because there is only one path.  
(It can also be understood that that one path can be counted twice, and indeed there is no intersection, because it does not pass through other points)

Although the original definition is indeed the former, for convenience, we stipulate that the definition of a vertex-biconnected graph adopts the latter.

And a **vertex-biconnected component** of a graph is a **maximal vertex-biconnected subgraph**.  
Unlike strongly connected components etc., a point may belong to multiple vertex-biconnected components, but an edge belongs to exactly one vertex-biconnected component (if the definition adopts the former, it may not belong to any vertex-biconnected component).

In the block forest, each original point corresponds to a **round vertex**, and each vertex-biconnected component corresponds to a **square vertex**.  
So there are a total of $n+c$ points, where $n$ is the number of points in the original graph, and $c$ is the number of vertex-biconnected components of the original graph.

And for each vertex-biconnected component, the square vertex it corresponds to connects an edge to each point in this vertex-biconnected component.  
Each vertex-biconnected component forms a "star graph", and multiple "star graphs" are connected together through the cut vertices in the original graph (because the separating points of vertex-biconnected components are cut vertices).

Obviously, each edge in the block forest connects a round vertex and a square vertex.

The figure below shows the vertex-biconnected components and the block forest shape corresponding to a graph. [^ref2]

![](./images/block-forest1.svg)![](./images/block-forest2.svg)![](./images/block-forest3.svg)

The number of points in the block forest is less than $2n$, because the number of cut vertices is less than $n$, so please note to allocate various array sizes as double.

Actually, if the original graph is connected, then the "block forest" is a tree; if the original graph has $k$ connected components, then its block forest will also form a forest of $k$ trees.

If a certain connected component in the original graph has only one point, then it needs to be analyzed case by case; in the subsequent discussion we do not consider isolated points.

## Process

For a graph, how to construct its block forest? First, we can find that if the graph is not connected, it can be split into each connected subgraph for consideration, so we only consider connected graphs.

Because the block forest is based on vertex-biconnected components, and vertex-biconnected components are in turn based on cut vertices, we only need to use a method similar to finding cut vertices.

The common algorithm for finding cut vertices is Tarjan's algorithm; if you know it, understanding the following content is easy, and if you don't, that's fine too.

We skip Tarjan for finding cut vertices, and directly introduce the algorithm used by the block forest (actually a variant of Tarjan):

Perform DFS on the graph, and use two key arrays `dfn` and `low` in the middle (similar to Tarjan).

`dfn[u]` stores the DFS order of node $u$, i.e. the ordinal of the node when $u$ is first visited.  
`low[u]` stores the **minimum** DFS order of the points that some point $v$ in the subtree of node $u$ in the DFS tree can reach through **at most one back edge or tree edge toward the parent**.  
If you have not heard of Tarjan's algorithm it may be a bit hard to understand; let's give an example:

![](./images/block-forest4.svg)

(We can find that this graph is actually equivalent to the graph in the picture above)  
Here tree edges are drawn from top to bottom with straight lines, and back edges are drawn from bottom to top with curved lines. The number of a node is its DFS order.

Then the `low` array is as follows:

|        $i$        | $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ |
| :---------------: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| $\mathrm{low}[i]$ | $1$ | $1$ | $1$ | $3$ | $3$ | $4$ | $3$ | $3$ | $7$ |

Not very hard to understand, right? Note that here the `low` of $9$ is $7$, which differs from some cut-vertex-finding approaches, because for convenience, we stipulated that one can go up through the parent edge, but the main idea is the same.

We can easily write the DFS function for computing `dfn` and `low` (initially the `dfn` array is cleared to zero):

???+ note "Implementation"
    === "C++"
        ```cpp
        void Tarjan(int u) {
          low[u] = dfn[u] = ++dfc;                // low is initialized to the current node's dfn
          for (int v : G[u]) {                    // traverse u's adjacent nodes
            if (!dfn[v]) {                        // if not visited
              Tarjan(v);                          // recurse
              low[u] = std::min(low[u], low[v]);  // for the unvisited, take min with low
            } else
              low[u] = std::min(low[u], dfn[v]);  // for the visited, take min with dfn
          }
        }
        ```
    
    === "Python"
        ```python
        def Tarjan(u):
            low[u] = dfn[u] = dfc  # low is initialized to the current node's dfn
            dfc = dfc + 1
            for v in G[u]:  # traverse u's adjacent nodes
                if dfn[v] == False:  # if not visited
                    Tarjan(v)  # recurse
                    low[u] = min(low[u], low[v])  # for the unvisited, take min with low
                else:
                    low[u] = min(low[u], dfn[v])  # for the visited, take min with dfn
        ```

Next, we consider the association among vertex-biconnected components, the DFS tree, and these two arrays.

We can find that each vertex-biconnected component is a connected subtree on the DFS tree, and contains at least two points; in particular, the topmost node only connects downward to one point.

At the same time, we can also find that each tree edge is in exactly one vertex-biconnected component.

We consider the topmost node $u$ of a vertex-biconnected component in the DFS tree, and determine this vertex-biconnected component at $u$, because the subtree of $u$ contains all the information of the whole vertex-biconnected component.

Because there are at least two points, consider the next point $v$ of this vertex-biconnected component; then there is a tree edge between $u$ and $v$.

It is not hard to find that at this point there must be $\mathrm{low}[v]=\mathrm{dfn}[u]$.  
More precisely, for a tree edge $u\to v$, $u,v$ are in the same vertex-biconnected component, and $u$ is the shallowest node in this vertex-biconnected component **if and only if** $\mathrm{low}[v]=\mathrm{dfn}[u]$.

Then we can determine during the DFS process where vertex-biconnected components exist, but we cannot yet accurately determine the point set contained by a vertex-biconnected component.

This is not hard to handle; we can maintain a stack during the DFS process, storing the nodes whose belonging vertex-biconnected component (there may be multiple) has not yet been determined.

When a vertex-biconnected component is found, the points other than $u$ in the vertex-biconnected component are all concentrated at the top of the stack; just keep popping the stack until $v$ is popped.

Of course, we can process the popped nodes at the same time; just connect them to the newly-created square vertex. Finally we also need to connect $u$ to the square vertex.

This naturally completes the construction of the block forest; we can number the square vertices with integers starting from $n+1$, which effectively distinguishes round vertices from square vertices.

This part may not be explained clearly enough; below we paste a piece of code, with detailed comments and output statements to aid understanding, plus a sample; it is recommended that the reader copy the code and practice and understand on their own, after all code is what best helps understanding (don't forget to enable `c++11`).

???+ note "Implementation"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <vector>
    
    constexpr int MN = 100005;
    
    int N, M, cnt;
    std::vector<int> G[MN], T[MN * 2];
    
    int dfn[MN], low[MN], dfc;
    int stk[MN], tp;
    
    void Tarjan(int u) {
      printf("  Enter : #%d\n", u);
      low[u] = dfn[u] = ++dfc;                // low is initialized to the current node's dfn
      stk[++tp] = u;                          // push into the stack
      for (int v : G[u]) {                    // traverse u's adjacent nodes
        if (!dfn[v]) {                        // if not visited
          Tarjan(v);                          // recurse
          low[u] = std::min(low[u], low[v]);  // for the unvisited, take min with low
          if (low[v] == dfn[u]) {  // marks that a vertex-biconnected component rooted at u is found
            ++cnt;                 // increase the number of square vertices
            printf("  Found a New BCC #%d.\n", cnt - N);
            // pop the points other than u in the vertex-biconnected component off the stack, and connect edges in the block forest
            for (int x = 0; x != v; --tp) {
              x = stk[tp];
              T[cnt].push_back(x);
              T[x].push_back(cnt);
              printf("    BCC #%d has vertex #%d\n", cnt - N, x);
            }
            // note that u itself also needs to connect an edge (but not be popped)
            T[cnt].push_back(u);
            T[u].push_back(cnt);
            printf("    BCC #%d has vertex #%d\n", cnt - N, u);
          }
        } else
          low[u] = std::min(low[u], dfn[v]);  // for the visited, take min with dfn
      }
      printf("  Exit : #%d : low = %d\n", u, low[u]);
      printf("  Stack:\n    ");
      for (int i = 1; i <= tp; ++i) printf("%d, ", stk[i]);
      puts("");
    }
    
    int main() {
      scanf("%d%d", &N, &M);
      cnt = N;  // vertex-biconnected component / square vertex numbering starts from N
      for (int i = 1; i <= M; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        G[u].push_back(v);  // add a bidirectional edge
        G[v].push_back(u);
      }
      // handle non-connected graphs
      for (int u = 1; u <= N; ++u)
        if (!dfn[u]) Tarjan(u), --tp;
      // note that when exiting Tarjan there is still one element in the stack, namely the root; pop it off
      return 0;
    }
    ```

Here is a test case:

```text
13 15
1 2
2 3
1 3
3 4
3 5
4 5
5 6
4 6
3 7
3 8
7 8
7 9
10 11
11 10
11 12
```

The graph corresponding to this example (including the cases of multi-edges and isolated points):

![](./images/block-forest5.svg)

## Example problems

We discuss some example problems that can be solved using the block forest.

???+ note "[「APIO2018」Duathlon](https://loj.ac/p/2587)"
    ??? note "Brief problem meaning"
        Given a simple undirected graph, ask how many triples $\langle s, c, f \rangle$ (with $s, c, f$ mutually distinct) there are such that there exists a simple path from $s$, passing through $c$, to $f$.
    
    ??? note "Solution"
        Speaking of simple paths, we must mention a very good property about vertex-biconnected components: for two points in a vertex-biconnected component, the union of the simple paths between them is exactly equal to this vertex-biconnected component.  
        That is, between two distinct points $u,v$ in the same vertex-biconnected component there must exist a simple path passing through a given other point $w$ in the same vertex-biconnected component.
        
        Proof of this property:
        
        -   Obviously if a simple path leaves the vertex-biconnected component, it cannot return to this vertex-biconnected component, otherwise it conflicts with the definition of a vertex-biconnected component.
        -   So we only need to consider proving that for any three distinct points $u,v,c$ in a vertex-biconnected graph, there must exist a simple path from $u$ to $v$ passing through $c$.
        -   First exclude the case of point count $2$, which satisfies this property, but $3$ distinct points cannot be taken out.
        -   For the remaining cases, consider building a network-flow model; the source connects an edge of capacity $2$ to $c$, and $u$ and $v$ connect edges of capacity $1$ to the sink.
        -   A bidirectional edge $\langle x,y\rangle$ in the original graph becomes $x$ connecting an edge of capacity $1$ to $y$, and $y$ also connecting an edge of capacity $1$ to $x$.
        -   Finally, give each point except the source, sink, and $c$ a capacity of $1$, which can be achieved by splitting points.
        -   Because the capacity of the edge from the source to $c$ is $2$, then if the maximum flow of this network is $2$, it proves that there must be a path passing through $c$.
        -   Considering the max-flow min-cut theorem, obviously the minimum cut is less than or equal to $2$; next we only need to prove the minimum cut is greater than $1$.
        -   This is equivalent to proving that cutting any edge of capacity $1$ cannot disconnect the source and the sink.
        -   Consider cutting the point where $u$ or $v$ connects to the sink; according to the first definition of a vertex-biconnected component, there must exist a simple path from $c$ to the other uncut point.
        -   Consider cutting an edge formed by splitting a node; this is equivalent to deleting a point; according to the second definition of a vertex-biconnected component, the remaining graph is still connected.
        -   Consider cutting an edge built from an original edge; this is equivalent to deleting an edge, which is weaker than deleting a point, so obviously a path exists.
        -   So we have proved the minimum cut is greater than $1$, i.e. the maximum flow equals $2$. Q.E.D.
        
        What can this conclusion tell us? It tells us: considering the path of two round vertices on the block forest, the set of round vertices adjacent to the square vertices passed on the path equals the point set on the simple paths between the two points in the original graph.
        
        Back to the problem, consider fixing $s$ and $f$ and finding the number of valid $c$; obviously the number of valid $c$ equals the number of points in the union of the simple paths between $s,f$ minus $2$ (removing $s,f$ themselves).
        
        Then, after building the block forest for the original graph, the number of points of the simple paths between two points is related to the number of square vertices (vertex-biconnected components) and round vertices passed on their path on the block forest.
        
        Next is a common technique for the block forest: when counting paths, assign points appropriate weights.  
        In this problem, the weight of each square vertex is the size of the corresponding vertex-biconnected component, and the weight of each round vertex is $-1$.
        
        After weighting this way, the sum of point weights on the block-forest path between two round vertices is exactly equal to the size of the simple-path union in the original graph minus $2$.
        
        The problem is transformed into counting $\sum$ of the path weight sums between two round vertices on the block forest.
        
        Considering from another angle, change to counting the contribution of each point to the answer, i.e. the weight multiplied by the number of paths passing through it, which can be found through simple tree DP.
        
        Finally, don't forget to handle the case where the graph is not connected. Below is the corresponding code:
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/graph/code/block-forest/block-forest_1.cpp"
        ```
    
    By the way, the answer of the earlier test case for this problem is $212$.

???+ note "[Codeforces #487 E. Tourists](https://codeforces.com/contest/487/problem/E)"
    ??? note "Brief problem meaning"
        Given a simple undirected connected graph, required to support two kinds of operations:
        
        1.  Modify the weight of a point.
        
        2.  Query the minimum of the point weights on all simple paths between two points.
    
    ??? note "Solution"
        Likewise, we build the block forest of the original graph, let the weight of a square vertex be the minimum of the weights of adjacent round vertices, and the problem is transformed into finding the minimum on a path.
        
        The path minimum can be maintained with heavy-path decomposition and a segment tree, but what about modification?
        
        A single modification of the weight of a round vertex requires modifying all square vertices adjacent to it, which can easily be blown up to $O(n)$ modifications.
        
        At this point we use the property that the block forest is a tree, and let the weight of a square vertex be the minimum of the weights of its child round vertices; in this way, when modifying, we only need to modify the parent square vertex.
        
        For the maintenance of square vertices, we only need to open a `multiset` for each square vertex to maintain the weight set.
        
        Note that when querying, if the LCA is a square vertex, we also need to query the weight of the LCA's parent round vertex.
        
        Note: the number of points in the block forest should be double that of the original graph, otherwise there will be array out-of-bounds.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/graph/code/block-forest/block-forest_2.cpp"
        ```

???+ note "[「SDOI2018」Strategy Game](https://loj.ac/p/2562)"
    ??? note "Brief problem meaning"
        Given a simple undirected connected graph. There are $q$ queries:
        
        Each time a point set $S$ is given ($2 \le |S| \le n$), ask how many points $u$ satisfy $u \notin S$ and, after deleting $u$, the points in $S$ are not all in one connected component.
        
        Each test point has multiple groups of data.
    
    ??? note "Solution"
        First build the block forest; then it becomes querying the number of round vertices in the connected subgraph corresponding to $S$ on the block forest minus $|S|$.
        
        How to compute the number of round vertices in a connected subgraph? There is a method:
        
        Put the weight of a round vertex on the edge between it and its parent square vertex, and the problem is transformed into finding the sum of edge weights; this problem can refer to a solution of [「SDOI2015」Treasure Hunt Game](https://loj.ac/p/2182).  
        That is, sort the points in $S$ by DFS order, and compute the sum of distances between adjacent points after sorting (also including the distance between the first and last points); the answer is half of the distance sum, because each edge is passed exactly twice.
        
        Finally, if the shallowest node in the subgraph is a round vertex, the answer also needs to add $1$, because we did not count it.
        
        Because there are multiple groups of data, note to initialize the arrays.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/graph/code/block-forest/block-forest_3.cpp"
        ```

## Exercises

-   [UVa 1464 Traffic Real Time Query](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=447&page=show_problem&problem=4210)
-   [Luogu P4320 Roads Meet](https://www.luogu.com.cn/problem/P4320)
-   [Luogu P10517 Territory Planning](https://www.luogu.com.cn/problem/P10517)

## External links

immortalCO, [The block forest — a powerful tool for handling cacti](https://immortalco.blog.uoj.ac/blog/1955), Universal OJ.

## References and notes

[^ref1]: In 2017, Chen Junkun defined and named the block-forest structure in his IOI2017 China National Training Team paper "Proposition Report and Extension of 〈Magical Subgraphs〉".

[^ref2]: Chen Junkun, "The Ordinary Block Forest and the Magical (~~Dynamic~~) Dynamic Programming", NOI2018 Winter Camp, page 4.
