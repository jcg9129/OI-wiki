## Ordinary cycle counting

???+ note "[Example problem 1: Codeforces Beta Round 11 D. A Simple Task](https://codeforces.com/problemset/problem/11/D)"
    Given a simple graph, find the number of simple cycles in the graph. A simple cycle is a cycle with no repeated vertices or edges.
    
    Number of nodes $1\leq n\leq 19$.

??? note "Solution idea"
    Consider bitmask dynamic programming. Let $f(s,i)$ denote the number of paths satisfying that the set of currently-passed nodes is $s$, we are now at node $i$, and the first node is **the one with the smallest number** in the node set $s$.
    
    For the state $f(s,i)$, enumerate the next node $u$. If $u$ is in the set $s$ and is the one with the smallest number (i.e. the start point), then add $f(s,i)$ to the answer $A$. If $u$ is not in $s$, then add $f(s\cup\{u\},u)$ to $f(s,i)$.
    
    This will also count the 2-node cycles (i.e. multiple edges), and each non-2-node cycle will be counted twice (because fixing the start point, we can walk in two directions), so the answer is $\dfrac{A-m}2$, where $m$ denotes the number of edges. The time complexity is $O(2^nm)$.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_1.cpp"
    ```

## Triangle counting

A **triangle** refers to an unordered triple $(u,\ v,\ w)$ in a simple graph $G$ satisfying that there exist three edges connecting $(u,\ v)$, $(v,\ w)$ and $(w,\ u)$ respectively. And the **triangle counting problem** requires computing the number of all triangles in the graph.

First, orient all edges. We stipulate that we point from the point with the smaller degree to the point with the larger degree; if the degrees are the same, point from the point with the smaller number to the point with the larger number. Then at this time this graph is a directed acyclic graph (DAG).

??? note "Proof that this graph has no cycle"
    By contradiction, assume a cycle exists; then the degrees of the points in the cycle are one larger than the next; to form a cycle, the degrees of all points must be equal, but the numbers are certainly different, a contradiction.
    
    So the oriented graph definitely has no cycle.
    
    In fact, we can construct a [partial order](../math/order-theory.md#二元关系) according to the above orientation rule, so the graph constructed by this rule (i.e. the [Hasse diagram](../math/order-theory.md#偏序集的可视化表示hasse-图) of this partial order) must be a DAG.

Enumerate $u$ and the point $v$ that $u$ points to, then enumerate $w$ among the points that $v$ points to, and check whether $u$ is connected to $w$.

The time complexity of this algorithm is $O(m\sqrt m)$.

???+ note "Time complexity proof"
    For the orientation part, we traversed all edges, with time complexity $O(n+m)$.
    
    For each pair $(v,\ w)$, the number of $u$ does not exceed the in-degree $d^-(v)$ of $v$.
    
    If $d^-(v)\leq\sqrt m$, since the number of $w$ is at most $n$, this part has time complexity $O(n\sqrt m)$.
    
    If $d^-(v) > \sqrt m$, since $v$ points to $w$, so $d(v) \leq d(w)$, giving $d(w) > \sqrt m$; but the total number of edges is only $m$, so the number of such $w$ is at most $\sqrt m$, so the time complexity is $O(m\sqrt m)$.
    
    The total time complexity is $O(n+m+n\sqrt m+m\sqrt m)=O(m\sqrt m)$.
    
    In fact, if during orientation we point from the point with the larger degree to the point with the smaller degree, the complexity is also correct; we only need to swap the two points $u,\ w$, and the above proof also holds.

???+ note "Sample code ([Luogu P1989 Undirected graph triangle counting](https://www.luogu.com.cn/problem/P1989))"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_2.cpp"
    ```

### Example problem 2

???+ note "[HDU 6184 Counting Stars](https://acm.hdu.edu.cn/showproblem.php?pid=6184)"
    Given an undirected graph with $n$ points and $m$ edges, find the number of occurrences of the following figure.
    
    ![](./images/rings-count1.svg)
    
    $2\leq n\leq 10^5$, $1\leq m\leq\min\left\{2\times 10^5,\ \dfrac{n(n-1)}2\right\}$.

??? note "Solution idea"
    This figure is formed by two triangles sharing an edge. So we first run triangle counting once, count the number of triangles on each edge, then enumerate the shared edge; suppose there are $x$ triangles containing this edge, then the contribution to the answer is $\dbinom x2$.
    
    The time complexity is $O(m\sqrt m)$.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_3.cpp"
    ```

## 4-cycle counting

Similarly, a **4-cycle** refers to four points $a,\ b,\ c,\ d$ satisfying that $(a,\ b)$, $(b,\ c)$, $(c,\ d)$ and $(d,\ a)$ are all connected by edges.

Consider first sorting the points. Those with smaller degrees are placed in front, and those with larger degrees are placed in back.

Consider enumerating the point $a$ ranked last; at this time we only need to, for each point $c$ ranked before $a$, compute how many points $b$ ranked before $a$ satisfy that $(a,\ b)$, $(b,\ c)$ have edges. Then we only need to take any two of these $b$ to form a 4-cycle. Finding the number of $b$ only needs traversing $b$ and $c$ once.

Note that the complexity of our enumeration is essentially equivalent to enumerating triangles, so the time complexity is also $O(m\sqrt m)$ (assuming $n,\ m$ are of the same order).

It is worth noting that $(a,\ b,\ c,\ d)$ and $(a,\ c,\ b,\ d)$ can be two different 4-cycles.

In addition, the ranks of nodes with the same degree will be different, and we need to be careful to judge $a\neq c$.

???+ note "Sample code ([LibreOJ P191 Undirected graph 4-cycle counting](https://loj.ac/p/191))"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_4.cpp"
    ```

### Example problem 3

???+ note "[Gym 102028L Connected Subgraphs](https://codeforces.com/gym/102028/problem/L)"
    Given an undirected graph with $n$ points and $m$ edges, find the number of cases where the induced subgraph of four edges is connected.
    
    $4\leq n\leq 10^5$, $4\leq m\leq 2\times 10^5$.

??? note "Solution idea"
    It is easy to divide the cases into five kinds: the star graph, the 4-cycle, an edge leading out of a point on a triangle, an edge leading out of the middle point of a chain formed by four points, and a chain formed by five points.
    
    For the star graph, directly enumerate the degree of the point and solve using combinatorial numbers. The 4-cycle can be directly found according to the above algorithm. For the triangle part, we only need to enumerate the triangle $(u,\ v,\ w)$; then the contribution to the answer is $[d(u)-2]+[d(v)-2]+[d(w)-2]$.
    
    Below we consider the fourth case. Consider enumerating the point $x$ with degree $2$, then enumerating a node $y$ adjacent to it as the point with degree $3$. At this time the contribution to the answer is $[d(x)-1]\cdot\dbinom{d(y)-1}2$. But note that the adjacent nodes of $y$ may coincide with the adjacent nodes of $x$; at this time the figure is equivalent to the third case. But each over-counted third case will be over-counted twice (because there are two points with degree $3$), so we should subtract twice the number of third cases.
    
    For the last case, first enumerate the middle point $x$; then it is easy to find that the contribution to the answer is
    
    $$
    \sum_{y\in son_x}\sum_{z\in son_x}[d(y)-1]\cdot[d(z)-1].
    $$
    
    Similarly, there is an over-counted part in this. Let the adjacent node of $y$ be $s$ and the adjacent node of $z$ be $t$; then after thinking, we find that the over-counted cases are the following:
    
    1.  When $y$ coincides with $t$, but $s$ does not coincide with $z$, it is equivalent to the third case;
    2.  When $s$ coincides with $z$, but $y$ does not coincide with $t$, it is likewise equivalent to the third case;
    3.  When both $y$ and $t$, and $s$ and $z$ coincide, it is equivalent to a triangle;
    4.  When $s$ coincides with $t$, it is equivalent to a 4-cycle (the second case).
    
    Considering that in the third case the two degree-2 points, when taken as $x$, correspond exactly to the over-counted cases 1 and 2 above respectively, so we need to additionally subtract twice the number of third cases. For a triangle, all three nodes can be taken as $x$, so it is over-counted $3$ times. Similarly, the 4-cycle case is over-counted $4$ times.
    
    So we obtain the algorithm for all cases, with time complexity $O(n+m\sqrt m)$.

??? note "Sample code"
    ```cpp
    --8<-- "docs/graph/code/rings-count/rings-count_5.cpp"
    ```

## Exercises

[Luogu P3547 \[POI2013\] CEN-Price List](https://www.luogu.com.cn/problem/P3547)

[CodeForces 985G Team Players](https://codeforces.com/contest/985/problem/G) (inclusion-exclusion principle)
