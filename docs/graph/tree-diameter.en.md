The longest simple path between any two nodes on a tree is the "diameter" of the tree.

Prerequisite knowledge: [tree basics](./tree-basic.md).

## Introduction

Obviously, a tree can have multiple diameters; their lengths are equal.

We can use two DFS or the tree DP method to find the diameter of the tree in $O(n)$ time.

## Two DFS

First, start a first DFS from any node $y$, reaching the node farthest from it, denoted $z$; then start a second DFS from $z$, reaching the node farthest from $z$, denoted $z'$; then $\delta(z,z')$ is the diameter of the tree.

Obviously, if the node $z$ reached by the first DFS is one end of the diameter, then the node $z'$ reached by the second DFS must be one end of the diameter. We only need to prove that in any case, $z$ must be one end of the diameter.

Theorem: On a tree, starting a DFS from any node $y$, the node $z$ reached that is farthest from it must be one end of the diameter.

???+ note "Proof"
    Use proof by contradiction. Denote the starting node as $y$. Let the real diameter be $\delta(s,t)$, and the node $z$ farthest from $y$ reached by the first DFS starting from $y$ is not $t$ or $s$. There are three cases in total:
    
    -   If $y$ is on $\delta(s,t)$:
    
    ![y is on s-t](./images/tree-diameter1.svg)
    
    We have $\delta(y,z) > \delta(y,t) \Longrightarrow \delta(x,z) > \delta(x,t) \Longrightarrow \delta(s,z) > \delta(s,t)$, contradicting $\delta(s,t)$ being the longest simple path between any two nodes on the tree.
    
    -   If $y$ is not on $\delta(s,t)$, and $\delta(y,z)$ and $\delta(s,t)$ have an overlapping path:
    
    ![y is not on s-t, y-z and s-t have an overlapping path](./images/tree-diameter2.svg)
    
    We have $\delta(y,z) > \delta(y,t) \Longrightarrow \delta(x,z) > \delta(x,t) \Longrightarrow \delta(s,z) > \delta(s,t)$, contradicting $\delta(s,t)$ being the longest simple path between any two nodes on the tree.
    
    -   If $y$ is not on $\delta(s,t)$, and $\delta(y,z)$ and $\delta(s,t)$ have no overlapping path:
    
    ![y is not on s-t, y-z and s-t have no overlapping path](./images/tree-diameter3.svg)
    
    We have $\delta(y,z) > \delta(y,t) \Longrightarrow \delta(x',z) > \delta(x',t) \Longrightarrow \delta(x,z) > \delta(x,t) \Longrightarrow \delta(s,z) > \delta(s,t)$, contradicting $\delta(s,t)$ being the longest simple path between any two nodes on the tree.
    
    In summary, the assumption produces a contradiction in all three cases, so the original theorem is proved.

???+ warning "Negative-weight edges"
    The above proof process is built on the premise that all paths are non-negative. If there are negative-weight edges on the tree, then the above proof does not hold. So if there are negative-weight edges, we cannot use the two-DFS method to solve for the diameter.

If we need to find all nodes on a diameter, then during the second DFS process, record the predecessor node of each point, and then we can go all the way forward from one end of the diameter, traversing all nodes on the diameter.

## Tree DP

### Method 1

We record, when $1$ is the root of the tree, the longest path length $d_1$ and the second-longest path (with no common edge with the longest path) length $d_2$ that each node, as the root of a subtree, can extend downward; then the diameter is, for each point, the maximum value that $d_1 + d_2$ of that point can take.

Tree DP can solve for the diameter of the tree in the presence of negative-weight edges.

If we need to find all nodes on a diameter, then during the DP process, record the child nodes corresponding to the longest path and second-longest path (same definition as above) that each node can extend downward; while computing $d$, also record the corresponding node $u$ such that $d = d_1[u] + d_2[u]$, and then we can go along the child nodes corresponding to the longest path and second-longest path starting from $u$, all the way in some direction (for an unrooted tree, although $1$ is designated as the root of the tree here, we still need to record the jump direction of each point; for a rooted tree, just jump upward all the way), traversing all nodes on the diameter.

### Method 2

Here we provide a tree DP method that uses only one array.

We define $dp[u]$ as the longest path starting from $u$ in the subtree rooted at $u$. Then it is easy to obtain the transition equation: $dp[u] = \max(dp[u], dp[v] + w(u, v))$, where $v$ is a child node of $u$, and $w(u, v)$ denotes the weight of the edge passed.

For the diameter of the tree, it can actually be found by enumerating the maximum value of the sum of two different paths starting from a certain node. Therefore, during the DP solving process, we only need to compute $d = \max(d, dp[u] + dp[v] + w(u, v))$ before updating $dp[u]$ to compute the diameter $d$.

## Example problems

???+ example "[Luogu B4016 Tree diameter](https://www.luogu.com.cn/problem/B4016)"
    Given a tree with $n$ nodes, find the length of its diameter. $1\leq n\leq 10^5$.

??? note "Reference implementation of two DFS"
    ```cpp
    --8<-- "docs/graph/code/tree-diameter/tree-diameter_1.cpp"
    ```

??? note "Reference implementation of tree DP using two arrays"
    ```cpp
    --8<-- "docs/graph/code/tree-diameter/tree-diameter_2.cpp"
    ```

??? note "Reference implementation of tree DP using one array"
    ```cpp
    --8<-- "docs/graph/code/tree-diameter/tree-diameter_3.cpp"
    ```

## Properties

The diameter of a tree has the following property: if all edge weights on the tree are positive, then the midpoints of all diameters of the tree coincide.

???+ note "Proof"
    Proof: Use proof by contradiction. Let two diameters with non-coinciding midpoints be $\delta(s,t)$ and $\delta(s',t')$, with midpoints $x$ and $x'$ respectively. Obviously, $\delta(s,x) = \delta(x,t) = \delta(s',x') = \delta(x',t')$.
    
    ![The midpoints of all diameters of a tree with no negative-weight edges coincide](./images/tree-diameter4.svg)
    
    We have $\delta(s,t') = \delta(s,x) + \delta(x,x') + \delta(x',t') > \delta(s,x) + \delta(x,t) = \delta(s,t)$, contradicting $\delta(s,t)$ being the longest simple path between any two nodes on the tree, so the property is proved.

## Exercises

-   [CodeChef, Diameter of Tree](https://www.codechef.com/problems/DTREE)
-   [Educational Codeforces Round 35, Problem F, Tree Destruction](https://codeforces.com/contest/911/problem/F)
-   [ZOJ 3820 Building Fire Stations](https://pintia.cn/problem-sets/91827364500/exam/problems/type/7?problemSetProblemId=91827369872&page=28)
-   [CEOI2019/CodeForces 1192B. Dynamic Diameter](https://codeforces.com/contest/1192/problem/B)
-   [ICPC 2019 Shanghai Regional Online Round Lightning Routing I](https://vjudge.net/problem/%E8%AE%A1%E8%92%9C%E5%AE%A2-A2290)
-   [NOIP2007 Senior Group Core of tree network](https://www.luogu.com.cn/problem/P1099)
-   [SDOI2011 Fire fighting](https://www.luogu.com.cn/problem/P2491)
-   [APIO2010 Patrol](https://www.luogu.com.cn/problem/P3629)
