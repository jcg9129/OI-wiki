In combinatorics, graph enumeration is the branch that studies counting problems of graphs satisfying specific properties. [Generating functions](../poly/intro.md), the [Pólya enumeration theorem](./polya.md), the [symbolic method](../poly/symbolic-method.md#%E9%9B%86%E5%90%88%E7%9A%84-cycle-%E6%9E%84%E9%80%A0), and [OEIS](https://oeis.org/) are the most important mathematical tools for solving such problems. Graph enumeration can be divided into two major classes of problems, labeled and unlabeled; in most cases[^1] the labeled version of a problem is simpler than its corresponding unlabeled problem, so we will first examine the counting of labeled problems.

[^1]: Perhaps unlabeled binary trees are a counterexample; in the case of simple structure, the corresponding permutation group is the identity group, and in this case the labeled version can be obtained directly by multiplying by $n!$.

## Labeled trees

This is Cayley's formula; see the article [Prüfer sequence](../../graph/prufer.md). We can also use the [Kirchhoff matrix-tree theorem](../../graph/matrix-tree.md), or [generating functions](../poly/intro.md#生成函数) and [Lagrange's theorem](https://codeforces.com/blog/entry/104184), to obtain this result.

### Exercises

-   [Hihocoder 1047. Random Tree](https://vjudge.net/problem/HihoCoder-1047)

## Labeled connected graphs

### Example problem "POJ 1737" Connected Graph

???+ note "Example problem [\"POJ 1737\" Connected Graph](http://poj.org/problem?id=1737)"
    Problem summary: Find the number of labeled connected graphs with $n$ nodes ($n \leq 50$).

This kind of problem first appeared in Lou Jiaozhu's "eight problems for men" series. We let $g_n$ be the number of labeled graphs with $n$ nodes, and $c_n$ be the sequence to be found. A graph with $n$ nodes has at most $\binom{n}{2}$ edges, and each edge has two states according to whether it appears, with each state independent, so $g_n = 2^{\binom{n}{2}}$. We fix one of the nodes and enumerate the size of the connected block it lies in; then we still need to choose $i-1$ nodes from the remaining $n-1$ nodes to form a connected block. The nodes outside the connected block can be connected by edges arbitrarily, so we have the following recurrence relation:

$$
\begin{align}
\sum_{i=1}^{n} \binom{n-1}{i-1} c_i g_{n-i} &= g_n \\
c_n &= g_n - \sum_{i=1}^{n-1} \binom{n-1}{i-1} c_i g_{n-i} 
\end{align}
$$

Rearranging gives an $O(n^2)$ recurrence formula for the $c_n$ sequence, which can pass this problem.

### Example problem "Training Team Assignment 2013" Urban Planning

???+ note "Example problem [\"Training Team Assignment 2013\" Urban Planning](https://www.luogu.com.cn/problem/P4841)"
    Problem summary: Find the number of labeled connected graphs with $n$ nodes ($n \leq 130000$).

For sequence problems with larger data ranges, we often need to construct the generating functions of these sequences in order to use efficient polynomial algorithms.

#### Method 1: divide-and-conquer FFT

The above recurrence can be regarded as a form of self-convolution, so it can be computed using divide-and-conquer FFT, with complexity $O(n\log^2n)$.

#### Method 2: polynomial inversion

We expand the binomial coefficient in the above recurrence and transform it:

$$
\begin{align}
\sum_{i=1}^{n} \binom{n-1}{i-1} c_i g_{n-i} &= g_n \\
\sum_{i=1}^{n} \frac{c_i}{(i-1)!} \frac{g_{n-i}}{(n-i)!} &= \frac{g_n}{(n-1)!}
\end{align}
$$

Construct polynomials:

$$
\begin{align}
C(x) &= \sum_{n=1} \frac{c_n}{(n-1)!} x^n \\
G(x) &= \sum_{n=0} \frac{g_n}{n!} x^n \\
H(x) &= \sum_{n=1} \frac{g_n}{(n-1)!} x^n
\end{align}
$$

Substituting into the above gives $CG = H$; after using [polynomial inversion](../poly/elementary-func.md#%E5%A4%9A%E9%A1%B9%E5%BC%8F%E6%B1%82%E9%80%86) and then convolution, one can solve for $C(x)$.

#### Method 3: polynomial exp

Another approach is to use the [combinatorial meaning of polynomial exp in EGFs](../poly/egf.md#egf-%E4%B8%AD%E5%A4%9A%E9%A1%B9%E5%BC%8F-exp-%E7%9A%84%E7%BB%84%E5%90%88%E6%84%8F%E4%B9%89). We let the EGFs of the labeled connected graph and simple graph sequences be $C(x)$ and $G(x)$ respectively; then they have the following relationship:

$$
\begin{align}
\exp(C(x)) &= G(x) \\
C(x) &= \ln(G(x))
\end{align}
$$

Using [polynomial ln](../poly/elementary-func.md#多项式对数函数--指数函数) one can solve for $C(x)$.

## Labeled Eulerian graphs, bipartite graphs

### Example problem "SPOJ KPGRAPHS" Counting Graphs

???+ note "Example problem [\"SPOJ KPGRAPHS\" Counting Graphs](http://www.spoj.com/problems/KPGRAPHS/)"
    Problem summary: Find the number of labeled graphs with $n$ nodes satisfying each of the following properties respectively ($n \leq 1000$).
    
    -   Connected graph [A001187](https://oeis.org/A001187).
    -   Eulerian graph [A033678](https://oeis.org/A033678).
    -   Bipartite graph [A047864](https://oeis.org/A047864).

This problem limits the code length, so a polynomial template cannot be used directly, but generating functions can still help us analyze.

The connected-graph problem was already solved in the previous example; consider the Eulerian graph. Note that the several methods for counting connected graphs above can all be generalized to labeled connected graphs satisfying arbitrary properties. For example, we can replace $g_n$ in the connected-graph recurrence formula, from arbitrary graphs to graphs in which all vertex degrees are even; the $c_n$ obtained in this case is the Eulerian graph.

We encapsulate the recurrence process of POJ 1737 into a connectivization function:

```cpp
void ln(Int C[], Int G[]) {
  for (int i = 1; i <= n; ++i) {
    C[i] = G[i];
    for (int j = 1; j <= i - 1; ++j)
      C[i] -= binom[i - 1][j - 1] * C[j] * G[i - j];
  }
}
```

The first two subproblems can then be easily solved:

```cpp
for (int i = 1; i <= n; ++i) G[i] = pow(2, binom[i][2]);
ln(C, G);
for (int i = 1; i <= n; ++i) G[i] = pow(2, binom[i - 1][2]);
ln(E, G);
```

Note that the connectivization recurrence process here is in fact equivalent to taking the polynomial ln of its EGF; similarly, we can also write the inverse-connectivization function, which is equivalent to taking the polynomial exp of its EGF.

```cpp
void exp(Int G[], Int C[]) {
  for (int i = 1; i <= n; ++i) {
    G[i] = C[i];
    for (int j = 1; j <= i - 1; ++j)
      G[i] += binom[i - 1][j - 1] * C[j] * G[i - j];
  }
}
```

Below we discuss the counting of labeled bipartite graphs.

We let $b_n$ denote the number of bipartite graphs with $n$ nodes, and $g_n$ denote the number of graphs on $n$ nodes obtained by 2-coloring the nodes such that there is no edge between nodes of the same color. Enumerating the number of nodes of one color, we have[^2]:

$$
g_n = \sum_{i=0}^{n} \binom{n}{i}2^{i(n-i)}
$$

[^2]: [PinkRabbit's blog](https://www.luogu.com.cn/blog/PinkRabbit/solution-sp4420) tells us that this sequence can also be optimized using the [Chirp Z-Transform](../poly/czt.md).

Next we use two different methods to establish the relationship between $g_n$ and $b_n$.

#### Method 1: counting twice

We let $c_{n, k}$ denote the number of bipartite graphs with $k$ connected components; then it is not hard to obtain the following relationships:

$$
\begin{align}
b_n &= \sum_{i=1}^{n} c_{n, i} \\
g_n &= \sum_{i=1}^{n} c_{n, i} 2^i 
\end{align}
$$

Comparing the two expressions for $g_n$ and expanding gives:

$$
\begin{align}
\sum_{i=0}^{n} \binom{n}{i}2^{i(n-i)} &= \sum_{i=1}^{n} c_{n, i} 2^i \\
c_{n, i} &= \sum_{i=0}{n-1} \binom{n-1}{i-1} c_{n, 1}c_{n-i,k-1}
\end{align}
$$

It is not hard to obtain a recurrence relation for $b_n$, with complexity $O(n^3)$; further using the inclusion-exclusion principle, it can be optimized to $O(n^2)$ to pass this problem.

#### Method 2: connectivization recurrence

Both Method 2 and Method 3 use the connected bipartite graph $b1_n$ [A001832](https://oeis.org/A001832) to build the bridge between $g_n$ and $b_n$.

Note that for each connected bipartite graph, we have exactly two different coloring methods, corresponding to two different sets of connected 2-colored graphs;
so connectivizing $g_n$ gives a sequence that is exactly twice $b1_n$, while $b_n$ is obtained by inverse-connectivizing $b1_n$.

Therefore:

```cpp
for (int i = 1; i <= n; ++i) {
  G[i] = 0;
  for (int j = 0; j < i + 1; ++j) G[i] += binom[i][j] * pow(2, j * (i - j));
}
ln(B1, G);
for (int i = 1; i <= n; ++i) B1[i] /= 2;
exp(B, B1);
```

Both recurrence processes have complexity $O(n^2)$, and can pass this problem.

#### Method 3: polynomial exp

We note that the above recurrence process can also be understood using EGFs.

Let $G(x)$ be the EGF of $g_n$, $B1(x)$ be the EGF of $b1_n$, and $B(x)$ be the EGF of $b_n$; applying the approach of Method 2, we have:

$$
\begin{align}
G(x) &= \exp(2B1(x)) \\
B(x) &= \exp(B1(x))  \\
     &= \exp(\frac{\ln{G(x)}}{2}) \\
     &= \sqrt{G}
\end{align}
$$

We can differentiate both sides of the equation and compare the coefficients of the two sides to obtain a recurrence formula that is easy to code, and pass this problem.
Note that Method 2 and Method 3 are essentially the same, and in general Method 3 can obtain a better time complexity.

$$
\begin{align}
B_n^2 &= G  \\
2B_nB_n' &= G' 
\end{align}
$$

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/combinatorics/graph-enumeration/graph-enumeration_1.cpp"
    ```

### Exercises

-   [UOJ Goodbye Jihai D. 新年的追逐战](https://uoj.ac/contest/50/problem/498)
-   [BZOJ 3864. 大朋友和多叉树](https://hydro.ac/p/bzoj-P3864)
-   [BZOJ 2863. 愤怒的元首](https://hydro.ac/p/bzoj-P2863)
-   [Luogu P6295. 有标号 DAG 计数](https://www.luogu.com.cn/problem/P6295)
-   [LOJ 6569. 仙人掌计数](https://loj.ac/p/6569)
-   [LOJ 6570. 毛毛虫计数](https://loj.ac/p/6570)
-   [Luogu P5434. 有标号荒漠计数](https://www.luogu.com.cn/problem/P5434)
-   [Luogu P3343. \[ZJOI2015\] 地震后的幻想乡](https://www.luogu.com.cn/problem/P3343)
-   [HDU 5279. YJC plays Minecraft](https://acm.hdu.edu.cn/showproblem.php?pid=5279)
-   [Luogu P7364. 有标号二分图计数](https://www.luogu.com.cn/problem/P7364)
-   [Luogu P5827. 点双连通图计数](https://www.luogu.com.cn/problem/P5827)
-   [Luogu P5827. 边双连通图计数](https://www.luogu.com.cn/problem/P5828)
-   [Luogu P6596. How Many of Them](https://www.luogu.com.cn/problem/P6596)
-   [Luogu U152448. 有标号强连通图计数](https://www.luogu.com.cn/problem/U152448)
-   [Project Euler 434. Rigid graphs](https://projecteuler.net/problem=434)

## Riddell's Formula

The above usage of the exp of EGFs is sometimes called Riddell's formula for labeled graphs; the [Euler transform](../poly/symbolic-method.md#%E9%9B%86%E5%90%88%E7%9A%84-multiset-%E6%9E%84%E9%80%A0) of a generating function is sometimes called Riddell's formula for unlabeled graphs, the latter first appearing in Euler's study of partition numbers; besides solving graph-enumeration problems, it also appears in the unbounded knapsack problem.

For a given sequence $a_i$ and the corresponding OGF $A(x)$, define the Euler transform of $A(x)$ as:

$$
\begin{align}
\mathcal{E}(A(x)) &= \prod_{i} (1-x^i)^{-a_i}  \\
                  &= \exp (\sum_{i} \frac{A(x^i)}{i})  
\end{align}
$$

Let the coefficients of $\mathcal{E}(A(x))$ be $b_i$, and define an auxiliary array $c_i = \sum_{d|n} d a_d$; then we have the recurrence formula

$$
n b_n = c_n + \sum_{i=1}^{n-1} c_i b_{n-i}
$$

## Unlabeled trees

### Example problem "SPOJ PT07D" Let us count 1 2 3

???+ note "Example problem [\"SPOJ PT07D\" Let us count 1 2 3](https://www.spoj.com/problems/PT07D/)"
    Problem summary: Find the number of trees with $n$ nodes satisfying each of the following properties respectively.
    
    -   Labeled rooted tree [A000169](https://oeis.org/A000169).
    -   Labeled unrooted tree [A000272](https://oeis.org/A000272).
    -   Unlabeled rooted tree [A000081](https://oeis.org/A000081).
    -   Unlabeled unrooted tree [A000055](https://oeis.org/A000055).

#### Rooted trees

The labeled case was solved earlier; below we examine unlabeled rooted trees. Let its OGF be $F(x)$; applying the Euler transform, we obtain:

$$
F(x) = x\mathcal{E}(F(x))
$$

Just extract the coefficients.

#### Unrooted trees

Consider inclusion-exclusion: we subtract from the count of rooted trees the cases where the root is not the centroid, and discuss according to the parity of $n$.

When $n$ is odd:

There must exist a subtree of size $\geq \left\lceil \frac{n}{2}\right\rceil$; enumerating the size of this subtree gives.

$$
g_n = f_n - \sum_{i=\left\lceil\frac{n}{2}\right\rceil}^{n-1} f_i f_{n-i}
$$

When $n$ is even:

Note that when there are two centroids, the above process only subtracts once, so we also need to subtract

$$
g_n = f_n - \sum_{i=\frac{n}{2}+1}^{n-1} f_i f_{n-i} - \binom{f_{\frac{n}{2}}}{2}
$$

### Example problem "Luogu P5900" Counting unlabeled unrooted trees

???+ note "Example problem [\"Luogu P5900\" Counting unlabeled unrooted trees](https://www.luogu.com.cn/problem/P5900)"
    Problem summary: Find the number of unlabeled unrooted trees with $n$ nodes ($n \leq 200000$).

For cases with larger data ranges, the approach is analogous: after the Euler transform, just use a polynomial template.

## Unlabeled simple graphs

### Example problem "SGU 282. Isomorphism" Isomorphism

???+ note "Example problem [\"SGU 282. Isomorphism\" Isomorphism](https://codeforces.com/problemsets/acmsguru/problem/99999/282)"
    Problem summary: Find the number of ways to $m$-color the edges of an unlabeled complete graph with $n$ nodes.

Note that when $m = 2$, the object sought is precisely the unlabeled simple graph [A000088](https://oeis.org/A000088); examining the Pólya enumeration theorem,

$$
\frac{1}{|G|}\sum_{g\in G} m^{c(g)}
$$

In this problem the permutation group $G$ is the edge-set permutation group generated by the symmetric group of order $n$ on the vertices, but the enumeration amount of the brute-force approach is $O(n!)$, which cannot pass this problem.

Consider classifying according to the cycle structure of the permutations; each cycle structure corresponds to a partition of a number. We use dfs() to generate the partitions, and then the problem is transformed into finding, for each partition $p$, the number of permutations $w(p)$ corresponding to it and the number of cycles $c(p)$ in each class of permutations; the answer is

$$
\frac{1}{|G|} \sum_{p \in P} w(p) m^{c(p)}
$$

Consider $w(p)$: each partition corresponds to a cyclic permutation, and at the same time the order among partitions of the same size is irrelevant, so we have:

$$
w(p) = \frac{n!}{\prod_{i}(p_i)\prod_{i}(q_i!)} 
$$

Here $q_i$ denotes the number of times a partition of size $i$ appears in $p$.

Consider $c(p)$: the cycle of the point set affected by $p$ is $|p|$, but the problem examines edge coloring, so we also need to examine the edge permutation generated by the point permutation.

If the vertices incident to an edge lie in the same cycle, and the size of this cycle is $p_i$, then the number of cycles generated by the edge is exactly $\left\lfloor \frac{p_i}{2} \right\rfloor$.

If the vertices incident to an edge lie in two different cycles, say $p_i$ and $p_j$, then the length of each cycle is $\operatorname{lcm}(p_i,p_j)$, so the number of cycles generated by the edge is exactly $\frac{p_i p_j}{\operatorname{lcm}(p_i,p_j)} = \gcd(p_i, p_j)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/combinatorics/graph-enumeration/graph-enumeration_2.cpp"
    ```

## Exercises

-   [CodeForces 438 E. The Child and Binary Tree](https://codeforces.com/problemset/problem/438/E)
-   [Luogu P5448. \[THUPC2018\] 好图计数](https://www.luogu.com.cn/problem/P5448)
-   [Luogu P5818. \[JSOI2011\] 同分异构体计数](https://www.luogu.com.cn/problem/P5818)
-   [Luogu P6597. 烯烃计数](https://www.luogu.com.cn/problem/P6597)
-   [Luogu P6598. 烷烃计数](https://www.luogu.com.cn/problem/P6598)
-   [Luogu P4128. \[SHOI2006\] 有色图](https://www.luogu.com.cn/problem/P4128)
-   [Luogu P4727. \[HNOI2009\] 图的同构计数](https://www.luogu.com.cn/problem/P4727)
-   [AtCoder Beginner Contest 222 H. Binary Tree](https://atcoder.jp/contests/abc222/tasks/abc222_h)
-   [AtCoder Beginner Contest 284 Ex. Count Unlabeled Graphs](https://atcoder.jp/contests/abc284/tasks/abc284_h)
-   [Luogu P4708. 画画](https://www.luogu.com.cn/problem/P4708)
-   [Luogu P7592. 数树（2021 CoE-II E）](https://www.luogu.com.cn/problem/P7592)
-   [Luogu P5206. \[WC2019\] 数树](https://www.luogu.com.cn/problem/P5206)

## References and notes

1.  [WC2015, 顾昱洲营员交流资料 Graphical Enumeration](https://github.com/lychees/ACM-Training/blob/master/Note/%E5%86%AC%E4%BB%A4%E8%90%A5/2015/%E9%A1%BE%E6%98%B1%E6%B4%B2%E8%90%A5%E5%91%98%E4%BA%A4%E6%B5%81%E8%B5%84%E6%96%99%20Graphical%20Enumeration.pdf)
2.  [WC2019, 生成函数，多项式算法与图的计数](https://github.com/lychees/ACM-Training/tree/master/Note/%E5%86%AC%E4%BB%A4%E8%90%A5/2019/d4)
3.  [Counting labeled graphs - Algorithms for Competitive Programming](https://cp-algorithms.com/combinatorics/counting_labeled_graphs.html)
4.  [Graphical Enumeration Paperback, Frank Harary, Edgar M. Palmer](https://github.com/lychees/ACM-Training/blob/master/Note/Book/)
5.  [The encyclopedia of integer sequences, N. J. A. Sloane, Simon Plouffe](https://github.com/lychees/ACM-Training/blob/master/Note/Book/The%20encyclopedia%20of%20integer%20sequences%20\(N.%20J.A.%20Sloane%2C%20Simon%20Plouffe\).pdf)
6.  [Combinatorial Problems and Exercises, László Lovász](https://github.com/lychees/ACM-Training/blob/master/Note/Book/Combinatorial%20Problems%20and%20Exercises_L%C3%A1szl%C3%B3%20Lov%C3%A1sz.pdf)
7.  [Graph Theory and Additive Combinatorics](https://yufeizhao.com/gtacbook/)
