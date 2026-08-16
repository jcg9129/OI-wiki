This page briefly introduces the concept, implementation, and applications of Eulerian graphs.

## Definition

This article only discusses finite graphs.

In graph theory, an **Eulerian path** is a path passing through each edge in the graph exactly once, and an **Eulerian circuit** is a circuit passing through each edge in the graph exactly once.
If an Eulerian circuit exists in a graph, then this graph is called an **Eulerian graph**; if an Eulerian circuit does not exist in a graph but an Eulerian path exists, then this graph is called a **semi-Eulerian graph**.

??? warning "Warning"
    Although the word "path" is used in this definition, strictly speaking the concept used here should be a "trail". An Eulerian path and Eulerian circuit can only use each edge exactly once, but there is no restriction on the situation of passing through vertices.

## Properties

Below we assume that there is no isolated vertex in the graph $G$ being discussed. This assumption is without loss of generality, because for a graph $G$ with isolated vertices, the following properties still hold for the graph $G'$ obtained by deleting the isolated vertices from $G$.

For a connected graph $G$, the following three properties are mutually equivalent:

1.  $G$ is an Eulerian graph;
2.  The degrees of all vertices in $G$ are even (for a directed graph, the in-degree of each vertex equals its out-degree);
3.  $G$ can be decomposed into the union of several edge-disjoint circuits.

Below we prove the equivalence.

If a graph $G$ is an Eulerian graph, then the degrees of all vertices in $G$ are even: consider walking around once along the Eulerian circuit starting from any vertex; then the degree of each point $v$ equals the number of times leaving point $v$ plus the number of times arriving at point $v$. And since the trajectory of the action is a circuit, for each point $v$, the number of times leaving that point equals the number of times arriving at that point. This means that the degree of each point is of the form $2k$, i.e. even.
In particular, for a directed graph, according to the same proof process, the in-degree of each vertex equals its out-degree.

If the degrees of all vertices in a graph $G$ are even (or in-degree equals out-degree), then it can be decomposed into a disjoint union of several edge-disjoint circuits: consider starting from any vertex $u$, choosing any out-edge $(u, v)$, walking to the corresponding adjacent vertex $v$ and deleting $(u, v)$, until returning to the initially-started vertex $u$. We can prove that this process must eventually return to $u$: whenever arriving at a new vertex $v \neq u$, according to the previous property, the remaining degree of that vertex is odd, that is to say there must exist an out-edge, and this process will not terminate at point $v$. (In other words, this process will and can only stop when returning to point $u$.) And because the number of edges in the graph $G$ is finite, this process must stop within a finite number of steps, so it must eventually return to $u$ and obtain a circuit. Note that in the preceding proof we only used the property that the point degrees are all even, and after finding and deleting a circuit the remaining part of the graph still satisfies this property, so we can continually repeat this process until the remaining graph is empty, thereby splitting $G$ into several edge-disjoint circuits.
Furthermore, each circuit can be decomposed at the vertices it passes multiple times into a disjoint union of several simple cycles, so the simple circuits in the above property can also be replaced by simple cycles.

If a connected graph $G$ can be decomposed into a disjoint union of several edge-disjoint circuits, then $G$ is an Eulerian graph: for a set of edge-disjoint circuits, each time select two circuits with a common vertex from them and merge them into one, repeating this process until there are no two circuits with a common vertex.
We can prove that the circuit remaining when this process ends is unique. For any two edge-disjoint circuits $P_1, P_2$, if $P_1$ and $P_2$ share a point, then they can be directly merged at the shared point; otherwise, take any point $v_1$ on $P_1$ and any point $v_2$ on $P_2$; according to the connectivity of $G$, there exists a path $e_1, e_2, \ldots, e_k$ connecting $v_1$ and $v_2$, where each edge $e_i$ is contained by a circuit $C_i$, and $P_1$ and $C_1$, $C_i$ and $C_{i+1}$, $C_k$ and $P_2$ all share points (or $C_i = C_{i+1}$, which does not affect the proof). In this case, $P_1$ and $P_2$ can be merged via $C_1, \ldots, C_k$. That is to say, any two circuits can be merged, and the circuit remaining at the end must be unique, and the edge set composing this circuit is the union of all edge-disjoint circuits, i.e. $E(G)$; this circuit is an Eulerian circuit on $G$, and $G$ is an Eulerian graph.

The above properties also constitute the judgment conditions for an Eulerian graph. Specifically, a graph is an Eulerian graph if and only if the non-zero-degree vertices are mutually (strongly) connected, and the degrees of the vertices are all even (or in-degree equals out-degree).

For a semi-Eulerian graph, its properties are similar to those of an Eulerian graph: a semi-Eulerian graph has exactly two odd-degree vertices, and these two vertices are the two endpoints of the Eulerian path. By connecting these two points, a semi-Eulerian graph can be converted into an Eulerian graph. By deleting any edge in an Eulerian graph, a semi-Eulerian graph can be obtained.
From this we can derive the discriminant method for a semi-Eulerian graph: a graph is a semi-Eulerian graph if and only if the non-zero-degree vertices are mutually (strongly) connected, and there are exactly two odd-degree vertices. For a directed graph, the second condition is that there exist exactly two vertices $u, v$ where $\deg^+(u) - \deg^-(u) = 1, \deg^+(v) - \deg^-(v) = -1$, and the in-degrees of the remaining vertices equal their out-degrees.

## Construction of Eulerian circuits / Eulerian paths

Here we introduce the most commonly-used Hierholzer algorithm; the core idea of this algorithm is to utilize the third point in the above Eulerian graph properties, i.e. an Eulerian graph can be decomposed into the union of several edge-disjoint circuits.
Note that in the above proof we have actually already mentioned the complete feasible operation of merging edge-disjoint circuits into an Eulerian circuit, and when using an appropriate data structure to store it (such as using a linked-list-like structure to store cycles), the implementation is not difficult.

The specific process of the algorithm is: first find a circuit from the graph as the current circuit; each time select a point with non-zero remaining degree from the current circuit, find a new simple circuit starting from that point, and merge this simple circuit with the current circuit; repeat this process until all points in the current circuit have no remaining degree, at which point the current circuit is the Eulerian circuit.

This algorithm also applies to directed graphs. For a semi-Eulerian graph, one can find a path connecting the two odd-degree points from the graph as the current path, each time select a point with non-zero degree to find a simple circuit and merge it with the current path, and finally obtain the Eulerian path.

### Implementation

The pseudocode of the Hierholzer algorithm is as follows:

$$
\begin{array}{ll}
1 &  \textbf{Input. } \text{The edges of the graph } e , \text{ where each element in } e \text{ is } (u, v) \\
2 &  \textbf{Output. } \text{The vertex of the Euler Road of the input graph}.\\
3 &  \textbf{Method. } \\
4 &  \textbf{Function } \text{Hierholzer } (v) \\
5 &  \qquad circle \gets \text{Find a Circle in } e \text{ Begin with } v \\
6 &  \qquad \textbf{if } circle=\varnothing \\
7 &  \qquad\qquad \textbf{return } v \\
8 &  \qquad e \gets e-circle \\
9 &  \qquad \textbf{for} \text{ each } v \in circle \\
10&  \qquad\qquad v \gets \text{Hierholzer}(v) \\
11&  \qquad \textbf{return } circle \\
12&  \textbf{Endfunction}\\
13&  \textbf{return } \text{Hierholzer}(\text{any vertex})
\end{array}
$$

### Time-complexity analysis

The time complexity of the Hierholzer algorithm is $O(|E| + |V|)$.

Note that in the preceding correctness analysis, the process of finding a simple circuit (or the initial path of a semi-Eulerian graph) on an Eulerian graph or semi-Eulerian graph **requires no backtracking**; just walking along the remaining edges will surely find the sought circuit or path, and **each edge is visited only once**.
To utilize this property, in implementation one should adopt a linked-list-like way to store the edges in the graph, such as an adjacency list or chained forward star, so that each edge is deleted immediately after being visited. If a naive adjacency matrix is used for storage, then each edge-finding takes $O(|V|)$ time, and the total complexity is $O(|V||E|)$.

???+ note "Note"
    In fact, the accurate complexity of this algorithm should be $O(|E|)$ rather than $O(|V| + |E|)$, because the implementation of this algorithm can adopt a method that depends on edges rather than points, finding the next circuit by maintaining a total linked list of remaining edges.

If the lexicographically smallest Eulerian path or Eulerian circuit needs to be output, then the edges need to be sorted, with time complexity $\Theta(|E|\log |E|)$ or $\Theta(|E|)$ (using counting sort or radix sort).

### Applications

Directed Eulerian graphs can be used for computer decoding.

Suppose there are $m$ letters, and we want to construct a disk with $m^n$ sectors, placing a letter on each sector, such that every consecutive $n$ positions on the disk correspond to a symbol string of length $n$. After turning around once ($m^n$ times), $m^n$ mutually distinct symbol strings of length $n$ produced from the $m$ letters are obtained.

![](images/euler1.svg)

Construct the following directed Eulerian graph:

Let $S = \{a_1, a_2, \cdots, a_m\}$, construct $D=\langle V, E\rangle$ as follows:

$V = \{a_{i_1}a_{i_2}\cdots a_{i_{n-1}} |a_i \in S, 1 \leq i \leq n - 1 \}$

$E = \{a_{j_1}a_{j_2}\cdots a_{j_{n-1}}|a_j \in S, 1 \leq j \leq n\}$

Stipulate the association relationship between vertices and edges in $D$ as follows:

The vertex $a_{i_1}a_{i_2}\cdots a_{i_{n-1}}$ leads out $m$ edges: $a_{i_1}a_{i_2}\cdots a_{i_{n-1}}a_r, r=1, 2, \cdots, m$.

The edge $a_{j_1}a_{j_2}\cdots a_{j_{n-1}}$ leads into the vertex $a_{j_2}a_{j_3}\cdots a_{j_{n}}$.

![](images/euler2.svg)

Such a $D$ is connected, and each vertex's in-degree equals its out-degree (both equal to $m$), so $D$ is a directed Eulerian graph.

Find any Eulerian circuit $C$ in $D$, take the last letter of each edge in $C$, and arrange them in a circle on the disk in the order of the edges in $C$.

## Example problems

???+ note "[Luogu P2731 Riding Horses and Fixing Fences](https://www.luogu.com.cn/problem/P2731)"
    Given an undirected graph with 500 vertices, find an Eulerian path or Eulerian circuit of this graph. If there are multiple solutions, output the smallest one.
    
    In this problem, the Eulerian path or Eulerian circuit does not need to pass through all vertices.
    
    The number of edges m satisfies $1\leq m \leq 1024$.

??? note "Solution idea"
    This problem is a direct application of the Hierholzer algorithm.
    
    Saving the answer can use `std::stack<int>`, because if what is found is not a circuit, that part must be placed at the end.
    
    Note, an adjacency matrix cannot be used to store the graph, otherwise the time complexity will degrade to $\Theta(nm)$. Since the edges need to be sorted, it is recommended to use a forward star or `std::vector` to store the graph. The example code uses `std::vector`.

??? note "Example code"
    ```cpp
    --8<-- "docs/graph/code/euler/euler_1.cpp"
    ```

## Exercises

-   [SGU 101 Domino](https://codeforces.com/problemsets/acmsguru/problem/99999/101)

-   [POJ 1780 Code](http://poj.org/problem?id=1780)

-   [Luogu P1127 Word Chain](https://www.luogu.com.cn/problem/P1127)

-   [Luogu P1333 Ruirui's Sticks](https://www.luogu.com.cn/problem/P1333)

-   [Luogu P1341 Unordered Letter Pairs](https://www.luogu.com.cn/problem/P1341)

-   [Luogu P6066 \[USACO05JAN\]Watchcow S](https://www.luogu.com.cn/problem/P6066)

-   [Luogu P6628 \[Provincial Selection Joint Exam 2020 B Volume\] Lilac Road](https://www.luogu.com.cn/problem/P6628)

-   [Luogu P3520 \[POI 2011\] SMI-Garbage](https://www.luogu.com.cn/problem/P3520)
