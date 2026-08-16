author: Ir1d, Anguei, hsfzLZH1

## Definition

A **system of difference constraints** is a special system of $n$-variable linear inequalities; it contains $n$ variables $x_1,x_2,\dots,x_n$ and $m$ constraints, where each constraint is formed by taking the difference of two of the variables, of the form $x_i-x_j\leq c_k$, where $1 \leq i, j \leq n, i \neq j, 1 \leq k \leq m$ and $c_k$ is a constant (can be non-negative or negative). The problem we want to solve is: find a set of solutions $x_1=a_1,x_2=a_2,\dots,x_n=a_n$ such that all constraints are satisfied, otherwise determine that there is no solution.

Each constraint $x_i-x_j\leq c_k$ in a system of difference constraints can be transformed into $x_i\leq x_j+c_k$, which is very similar to the triangle inequality $dist[y]\leq dist[x]+z$ in single-source shortest paths. Therefore, we can regard each variable $x_i$ as a node in the graph, and for each constraint $x_i-x_j\leq c_k$, connect a directed edge of length $c_k$ from node $j$ to node $i$.

Note that if $\{a_1,a_2,\dots,a_n\}$ is a set of solutions to this system of difference constraints, then for any constant $d$, $\{a_1+d,a_2+d,\dots,a_n+d\}$ is obviously also a set of solutions to this system of difference constraints, because after taking the difference this way, $d$ is exactly cancelled out.

## Process

Set $dist[0]=0$ and connect an edge of weight $0$ to every point, run single-source shortest paths; if there is a negative cycle in the graph, then the given system of difference constraints has no solution, otherwise, $x_i=dist[i]$ is a set of solutions to this system of difference constraints.

## Properties

Generally, Bellman–Ford or queue-optimized Bellman–Ford (commonly called SPFA, which runs very fast on some random graphs) is used to judge whether a negative cycle exists in the graph, with worst-case time complexity $O(nm)$.

## Common transformation techniques

### Example problem [luogu P1993 Little K's Farm](https://www.luogu.com.cn/problem/P1993)

Problem summary: solve a system of difference constraints; there are $m$ constraints, each of the form $x_a-x_b\geq c_k$, $x_a-x_b\leq c_k$, or $x_a=x_b$; determine whether this system of difference constraints has a solution.

| Problem meaning | Transformation | Edge connection |
| :----------------: | :-----------------------------------------: | :---------------------------: |
| $x_a - x_b \geq c$ |             $x_b - x_a \leq -c$             |        `add(a, b, -c);`       |
| $x_a - x_b \leq c$ |              $x_a - x_b \leq c$             |        `add(b, a, c);`        |
|     $x_a = x_b$    | $x_a - x_b \leq 0, \space x_b - x_a \leq 0$ | `add(b, a, 0), add(a, b, 0);` |

Run negative-cycle detection; if there is no negative cycle, output `Yes`, otherwise output `No`.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/diff-constraints/diff-constraints_1.cpp"
    ```

### Example problem [P4926 \[1007\] Multiple-Kill Measurer](https://www.luogu.com.cn/problem/P4926)

Without considering binary search and other things, here we only discuss the method of solving the difference system $\frac{x_i}{x_j}\leq c_k$.

Taking a $\log$ of each $x_i,x_j$ and $c_k$ can turn multiplication into addition, i.e. $\log x_i-\log x_j \leq \log c_k$; in this way it can be solved with difference constraints.

## Code implementation of Bellman–Ford negative-cycle detection

Below is the code implementation of using the Bellman–Ford algorithm to judge whether a negative cycle exists in the graph; please ensure the graph is connected before calling.

???+ note "Implementation"
    === "C++"
        ```cpp
        bool Bellman_Ford() {
          for (int i = 0; i < n; i++) {
            bool jud = false;
            for (int j = 1; j <= n; j++)
              for (int k = h[j]; ~k; k = nxt[k])
                if (dist[j] > dist[p[k]] + w[k])
                  dist[j] = dist[p[k]] + w[k], jud = true;
            if (!jud) break;
          }
          for (int i = 1; i <= n; i++)
            for (int j = h[i]; ~j; j = nxt[j])
              if (dist[i] > dist[p[j]] + w[j]) return false;
          return true;
        }
        ```
    
    === "Python"
        ```python
        def Bellman_Ford():
            for i in range(0, n):
                jud = False
                for j in range(1, n + 1):
                    while ~k:
                        k = h[j]
                        if dist[j] > dist[p[k]] + w[k]:
                            dist[j] = dist[p[k]] + w[k]
                            jud = True
                        k = nxt[k]
                if jud == False:
                    break
            for i in range(1, n + 1):
                while ~j:
                    j = h[i]
                    if dist[i] > dist[p[j]] + w[j]:
                        return False
                    j = nxt[j]
            return True
        ```

## Exercises

[Usaco2006 Dec Wormholes](https://loj.ac/problem/10085)

[「SCOI2011」Candy](https://loj.ac/problem/2436)

[POJ 1364 King](http://poj.org/problem?id=1364)

[POJ 2983 Is the Information Reliable?](http://poj.org/problem?id=2983)
