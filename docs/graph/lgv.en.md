## Introduction

The Lindström–Gessel–Viennot lemma, i.e. the LGV lemma, can be used to handle problems such as counting non-intersecting paths on a directed acyclic graph.

Prerequisite knowledge: the basic part of [graph-theory-related concepts](./concept.md), [matrices](../math/linear-algebra/matrix.md), [computing determinants by Gaussian elimination](../math/numerical/gauss.md).

The LGV lemma applies only to **directed acyclic graphs**.

## Definition

$\omega(P)$ denotes the product of the edge weights of all edges on the path $P$. (When counting paths, all edge weights can be set to $1$.) (In fact, edge weights can be generating functions.)

$e(u, v)$ denotes the sum of $\omega(P)$ over **every** path $P$ from $u$ to $v$, i.e. $e(u, v)=\sum\limits_{P:u\rightarrow v}\omega(P)$.

The start-point set $A$ is a subset of the vertex set of the directed acyclic graph, with size $n$.

The end-point set $B$ is also a subset of the vertex set of the directed acyclic graph, also with size $n$.

A set of non-intersecting paths $S$ from $A\rightarrow B$: $S_i$ is a path from $A_i$ to $B_{\sigma(S)_i}$ ($\sigma(S)$ is a permutation), and for any $i\ne j$, $S_i$ and $S_j$ have no common vertex.

$t(\sigma)$ denotes the number of inversions of the permutation $\sigma$.

## Lemma

$$
M = \begin{bmatrix}e(A_1,B_1)&e(A_1,B_2)&\cdots&e(A_1,B_n)\\
e(A_2,B_1)&e(A_2,B_2)&\cdots&e(A_2,B_n)\\
\vdots&\vdots&\ddots&\vdots\\
e(A_n,B_1)&e(A_n,B_2)&\cdots&e(A_n,B_n)\end{bmatrix}
$$

$$
\det(M)=\sum\limits_{S:A\rightarrow B}(-1)^{t(\sigma(S))}\prod\limits_{i=1}^n \omega(S_i)
$$

where $\sum\limits_{S:A\rightarrow B}$ denotes every set $S$ of non-intersecting paths from $A\rightarrow B$ satisfying the requirements above.

### Proof

By the definition of the determinant, we get

$$
\begin{align}
\det(M)&=\sum_{\sigma}(-1)^{t(\sigma)}\prod_{i=1}^n e(a_i,b_{\sigma(i)})\\
&=\sum_{\sigma}(-1)^{t(\sigma)}\prod_{i=1}^n \sum_{P:a_i\to b_{\sigma(i)}} \omega(P)
\end{align}
$$

Observe that $\prod\limits_{i=1}^n \sum\limits_{P:a_i\to b_{\sigma(i)}} \omega(P)$ is actually the sum of $\omega(P)$ over all path sets $P$ from $A$ to $B$ with permutation $\sigma$.

$$
\begin{align}
&\sum_{\sigma}(-1)^{t(\sigma)}\prod_{i=1}^n \sum_{P:a_i\to b_{\sigma(i)}} \omega(P)\\
=&\sum_{\sigma}(-1)^{t(\sigma)}\sum_{P=\sigma}\omega(P)\\
=&\sum_{P:A\to B}(-1)^{t(\sigma)}\prod_{i=1}^n \omega(P_i)
\end{align}
$$

Here $P$ is an arbitrary path set.

Let $U$ be a non-intersecting path set and $V$ be an intersecting path set,

$$
\begin{align}
&\sum_{P:A\to B}(-1)^{t(\sigma)}\prod_{i=1}^n \omega(P_i)\\
=&\sum_{U:A\to B}(-1)^{t(U)}\prod_{i=1}^n \omega(U_i)+\sum_{V:A\to B}(-1)^{t(V)}\prod_{i=1}^n \omega(V_i)
\end{align}
$$

Suppose there exists in $P$ an intersecting path pair $P_i:a_1 \to u \to b_1,P_j:a_2 \to u \to b_2$; then there must exist a corresponding intersecting path pair $P_i'=a_1\to u\to b_2,P_j'=a_2\to u\to b_1$, and the other paths of $P'$ are the same as $P$. We obtain $\omega(P)=\omega(P'),t(P)=t(P')\pm 1$.

Therefore we have $\sum\limits_{V:A\to B}(-1)^{t(\sigma)}\prod\limits_{i=1}^n \omega(V_i)=0$.

Then $\det(M)=\sum\limits_{U:A\to B}(-1)^{t(U)}\prod\limits_{i=1}^n \omega(U_i)$.

Q.E.D.[^1]

## Example problems

???+ note "Example 1 [CF348D Turtles](https://codeforces.com/contest/348/problem/D)"
    Problem statement: There is an $n\times m$ grid-point chessboard, where some cells are walkable and some cells are not walkable. A turtle from $(x, y)$ can only walk to the positions $(x+1, y)$ and $(x, y+1)$; find the number of non-intersecting paths of the turtle from $(1, 1)$ to $(n, m)$, modulo $10^9+7$. $2\le n,m\le3000$.

A relatively direct application of the LGV lemma. Considering all valid paths, we find that starting from $(1,1)$ one must pass through $A=\{(1,2), (2,1)\}$, while reaching the end point one must pass through $B=\{(n-1, m), (n, m-1)\}$, so $A, B$ can be immediately determined. Applying the LGV lemma, the answer is:

$$
\begin{vmatrix}
f(a_1, b_1) & f(a_1, b_2) \\
f(a_2, b_1) & f(a_2, b_2)
\end{vmatrix} = f(a_1, b_1)\times f(a_2, b_2) - f(a_1, b_2)\times f(a_2, b_1)
$$

where $f(a, b)$ is the number of paths $a\rightarrow b$ on the graph. The path-counting problem with obstacle grid points can be solved directly with an $O(nm)$ dp, so $f$ is easy to find. The final complexity is $O(nm)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/lgv/lgv_2.cpp"
    ```

???+ note "Example 2 [HDU 5852 Intersection is not allowed!](https://acm.hdu.edu.cn/showproblem.php?pid=5852)"
    Problem statement: There is an $n\times n$ chessboard; a piece from $(x, y)$ can only walk to $(x, y+1)$ or $(x + 1, y)$. There are $k$ pieces; initially the $i$-th piece is placed at $(1, a_i)$, and finally must reach $(n, b_i)$; the paths must be pairwise non-intersecting. Find the number of schemes modulo $10^9+7$. $1\le n\le 10^5$, $1\le k\le 100$; it is guaranteed that $1\le a_1<a_2<\dots<a_n\le n$, $1\le b_1<b_2<\dots<b_n\le n$.

Observe that if the paths do not intersect then it must be $a_i$ to $b_i$, so in the LGV lemma we must have $\sigma(S)_i=i$, and there is no need to consider the sign issue. Set the edge weights to $1$ and directly apply the lemma.

The number of paths from $(1, a_i)$ to $(n, b_j)$ is equivalent to choosing $n-1$ downward steps out of $n-1+b_j-a_i$ steps, so $e(A_i, B_j)=\binom{n-1+b_j-a_i}{n-1}$.

The determinant can be computed using Gaussian elimination.

The complexity is $O(n+k(k^2 + \log p))$, where $\log p$ is the complexity of finding modular inverses.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/lgv/lgv_1.cpp"
    ```

## References

[^1]: The proof comes from [Zhihu - Proof of the LGV lemma](https://zhuanlan.zhihu.com/p/517819133)
