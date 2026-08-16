## Introduction

Prefix sums and difference arrays are techniques commonly used in competitive programming: the former is used to quickly compute range sums, and the latter to efficiently perform range modifications.

???+ tip "Convention"
    For convenience of discussion, this article by default indexes the array $\{a_i\}$ starting from $1$, and additionally defines $a_0 = 0$.

## Prefix sums

A prefix sum can be simply understood as "the sum of the first $n$ terms of a sequence"; it is an important preprocessing technique.

### One-dimensional prefix sums

For a sequence $\{a_i\}$ of length $n$, if you need to query the sum of the numbers in the range $[l,r]$ many times, you can consider using prefix sums. The prefix sum of the sequence is

$$
S_{i} = \sum_{j=1}^i a_j.
$$

It can be computed term by term using the recurrence relation

$$
S_0 = 0,~ S_i = S_{i-1} + a_i
$$

To query the sum of the sequence within the range $[l,r]$, you only need to compute the difference

$$
S([l,r]) = S_r - S_{l-1}.
$$

In this way, through $O(n)$-time preprocessing, the complexity of a single range-sum query can be reduced to $O(1)$.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_1.py:core"
        ```

The C++ standard library implements a prefix-sum function [`std::partial_sum`](https://zh.cppreference.com/w/cpp/algorithm/partial_sum), defined in the header `<numeric>`. Since C++17, the standard library also provides a prefix-sum function with the same functionality, [`std::inclusive_scan`](https://zh.cppreference.com/w/cpp/algorithm/inclusive_scan), also defined in the header `<numeric>`.

### Two-dimensional / multi-dimensional prefix sums

Extending the one-dimensional prefix sum to the multi-dimensional case gives multi-dimensional prefix sums. There are two common methods for computing multi-dimensional prefix sums.

#### Based on the inclusion–exclusion principle

This method is mostly used for the two-dimensional prefix-sum case. Given a two-dimensional array $A$ of size $m\times n$, we want to compute its prefix sum $S$. Then $S$ is likewise a two-dimensional array of size $m\times n$, and

$$
S_{i,j} = \sum_{i'\le i}\sum_{j'\le j}A_{i',j'}.
$$

By analogy with the one-dimensional case, $S_{i,j}$ should be computable from $S_{i-1,j}$ or $S_{i,j-1}$, thereby avoiding recomputing the sum of the preceding terms. However, if we directly add $S_{i-1,j}$ and $S_{i,j-1}$ and then add $A_{i,j}$, we would double-count the prefix sum of the overlapping part $S_{i-1,j-1}$, so we still need to subtract this part off. This is the [inclusion–exclusion principle](../math/combinatorics/inclusion-exclusion-principle.md). This gives the following recurrence relation:

$$
S_{i,j} = A_{i,j} + S_{i-1,j} + S_{i,j-1} - S_{i-1,j-1}. 
$$

In the implementation, simply traverse $(i,j)$ and sum.

???+ note "Example"
    Consider a concrete example.
    
    ![two-dimensional prefix sum example](./images/prefix-sum-2d.svg)
    
    Here $S$ is the prefix sum of the matrix $A$. By definition, $S_{3,3}$ is the sum of the submatrix within the dashed box in the left figure. Moreover, $S_{3,2}$ is the sum of the blue submatrix, $S_{2,3}$ is the sum of the red submatrix, and the sum of their overlapping part is $S_{2,2}$. It can thus be seen that directly adding $S_{3,2}$ and $S_{2,3}$ double-counts $S_{2,2}$, so we should have
    
    $$
    S_{3,3} = A_{3,3} + S_{2,3} + S_{3,2} - S_{2,2} = 5 + 18 + 15 - 9 = 29.
    $$

By the same reasoning, once the two-dimensional prefix sum has been precomputed, to query the sum of the submatrix with top-left corner $(i_1,j_1)$ and bottom-right corner $(i_2,j_2)$, you can compute

$$
S_{i_2,j_2} - S_{i_1-1,j_2} - S_{i_2,j_1-1} + S_{i_1-1,j_1-1}.
$$

This can be done in $O(1)$ time.

In the two-dimensional case, the time complexity of the above algorithm can be simply regarded as $O(mn)$, i.e. linear in the size of the given array. However, as the dimension $k$ increases, since the number of terms involved in the inclusion–exclusion principle grows exponentially, the time complexity becomes $O(2^kN)$, where $k$ is the array dimension and $N$ is the size of the given array. Therefore, this algorithm is no longer applicable.

???+ example "[Luogu P1387 Largest Square](https://www.luogu.com.cn/problem/P1387)"
    In an $n\times m$ matrix containing only $0$s and $1$s, find the largest square that contains no $0$, and output its side length.

??? note "Reference code"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_2.cpp:full-text"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/prefix-sum/prefix-sum_2.py:full-text"
        ```

#### Dimension-by-dimension prefix sums

For the general case, given a $k$-dimensional array $A$ of size $N$, we again want to compute its prefix sum $S$. Here,

$$
S_{i_1,\cdots,i_k} = \sum_{i'_1\le i_1}\cdots\sum_{i'_k\le i_k} A_{i'_1,\cdots,i'_k}.
$$

From the above formula we can see that a $k$-dimensional prefix sum is equal to $k$ summations. So an obvious algorithm is: each time consider only one dimension, fix all other dimensions, and compute several one-dimensional prefix sums; after summing over all $k$ dimensions separately in this way, the result is the $k$-dimensional prefix sum.

??? example "Reference implementation of a three-dimensional prefix sum"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_4.cpp:core"
    ```

Because when considering each dimension we traverse the entire array only once, the complexity of this algorithm is $O(kN)$, which is usually acceptable.

#### Special case: sum-over-subsets DP

The case of relatively large dimension often appears in a class of problems called **sum over subsets (SOS)**. This is a special case of high-dimensional prefix sums.

The problem is described as follows. Consider a function $f$ defined over all subsets of a set of size $n$; we now want to compute its subset-sum function $g$, which satisfies

$$
g(S) = \sum_{T\subseteq S}f(T).
$$

That is, $g(S)$ equals the sum of the function values $f(T)$ over all its subsets $T\subseteq S$.

First, the subset-sum problem can be written in the form of a high-dimensional prefix sum. Note that a subset of $S$ can be represented, using the idea of bitmasking, as a 0-1 string $s$ of length $n$. Regarding each bit of the string as a dimension of the array index, $f$ is actually an $n$-dimensional array, and every dimension's index must be in $\{0,1\}$. At the same time, the containment relation of subsets is equivalent to the magnitude relation of the indices, i.e.

$$
T\subseteq S \iff \forall i(t_i \le s_i). 
$$

So summing over subsets is computing the prefix sum of this $n$-dimensional array.

Now we can directly use the dimension-by-dimension prefix-sum method described above to compute the subset sum. The time complexity is $O(n2^n)$.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_5.cpp:core"
    ```

The inverse operation of the subset sum needs to be performed via the [inclusion–exclusion principle](../math/combinatorics/inclusion-exclusion-principle.md). The subset-sum problem is also one of the necessary steps of the fast Möbius transform.

### Prefix sums on trees

The one-dimensional prefix sum can also be generalized to the case of a rooted tree (with root $1$). By precomputing prefix sums, we can quickly compute the sum of weights along a path on the tree.

#### The case of vertex weights

First discuss the case where weights are stored at the nodes. Suppose node $x$ has weight $a_x$. Using the recurrence relation

$$
S_1 = a_1,~ S_{x} = S_{\operatorname{fa}(x)} + a_x
$$

we can compute the sum of the weights of the nodes on the path from the root to node $x$, where $\operatorname{fa}(x)$ denotes the parent of $x$. After precomputing the prefix sums, the sum of the node weights on the path connecting nodes $x$ and $y$ can be computed by

$$
S_x + S_y - S_{\operatorname{lca}(x, y)} - S_{\operatorname{fa}(\operatorname{lca}(x, y))}
$$

where $\operatorname{lca}(x, y)$ denotes the [lowest common ancestor](../graph/lca.md) of nodes $x$ and $y$.

#### The case of edge weights

The case where weights are stored on edges can almost be reduced to the case of vertex weights. For every non-root node $x\neq 1$, let $\operatorname{edge}(x)$ denote the edge connecting node $x$ and its parent $\operatorname{fa}(x)$. Then we can assume the edge weight is stored at the node farther from the root. That is, node $x$ stores the edge weight of edge $\operatorname{edge}(x)$. The weight stored at the root is $0$. Then, via the recurrence relation discussed in the previous subsection, we can likewise precompute the sum $S_x$ of the weights of all edges passed on the path from the root to node $x$.

At this point, the sum of the weights on the path connecting nodes $x$ and $y$ can be queried by

$$
S_x + S_y - 2S_{\operatorname{lca}(x, y)}
$$

Note that, unlike the vertex-weight case, the queried weight sum does not include the weight at $\operatorname{lca}(x, y)$, because the edge weight it stores is not on the requested path.

#### Subtree sums

Unlike the array case, since a tree is asymmetric between its ends, computing the "prefix sum" bottom-up (from leaves to root) and top-down (from root to leaves) gives different results. Generally, "prefix sum on a tree" refers to the prefix sum computed top-down. For convenience of discussion, this article calls the "prefix sum" computed bottom-up the **subtree sum**.

The sum of the vertex weights of the subtree rooted at node $x$, i.e. the corresponding subtree sum, is

$$
T_x = \sum_{y\in\operatorname{desc}(x)} a_x.
$$

where $\operatorname{desc}(x)$ denotes the set of all descendants of $x$ (including itself).

Unlike prefix sums on a tree, subtree sums cannot be applied to computing path weight sums in $O(1)$, but they can be used to understand the tree difference discussed below.

## Difference arrays

A difference array is a strategy complementary to prefix sums; it is the inverse operation of the prefix sum. Compared with computing the difference of a given sequence, a more common scenario in contests is to perform many range modifications by maintaining information of the difference sequence. After the range modifications end, the information of the original sequence can be recovered via prefix sums, enabling queries on the original sequence. Note that the modification operations must precede the query operations.

If you need to support a mix of many modifications and queries, you need to use a [Fenwick tree](../ds/fenwick.md), but the ideas are shared.

### One-dimensional difference

For a sequence $\{a_i\}$, its difference sequence $\{D_i\}$ is defined as

$$
D_i = a_i - a_{i-1},~ a_0 = 0.
$$

The C++ standard library implements a difference function [`std::adjacent_difference`](https://zh.cppreference.com/w/cpp/algorithm/adjacent_difference), defined in the header `<numeric>`.

The relationship between prefix sums and difference arrays is as follows:

???+ note "Properties"
    Let $\{D_i\}$ be the difference sequence of $\{a_i\}$; then we have
    
    -   The sequence $\{a_i\}$ is the prefix sum of the sequence $\{D_i\}$, i.e.
    
        $$
        a_i = \sum_{j=1}^i D_j.
        $$
    -   The prefix sum of the sequence $\{a_i\}$ is
    
        $$
        S_i = \sum_{j=1}^i\sum_{k=1}^jD_k = \sum_{j=1}^i(i-j+1)D_j. 
        $$

Difference information is often used to maintain adding a number to a range of the sequence many times, and then querying the value at a certain position of the sequence one or more times afterwards.

Suppose we want to add $v$ to each number in the range $[l,r]$ of the sequence $\{a_i\}$. We can perform the following operations on its difference sequence $\{D_i\}$:

$$
D_{l} \gets D_{l} + v,~ D_{r+1}\gets D_{r+1} - v.
$$

After all modification operations end, we can recover the updated values of $\{a_i\}$ via a prefix-sum operation. A single modification is $O(1)$. When querying, one $O(n)$ prefix-sum operation is needed, after which each query is $O(1)$.

???+ example "Reference code"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_6.cpp:core"
    ```

### Two-dimensional / multi-dimensional difference

Difference arrays can likewise be generalized to the multi-dimensional case. Regarding a multi-dimensional difference as the inverse operation of a multi-dimensional prefix sum, the operation of computing a multi-dimensional difference array is equivalent to computing the original array from a multi-dimensional prefix sum. According to the earlier discussion, the inclusion–exclusion principle can be used. For example, the definition of the two-dimensional difference is

$$
D_{i,j} = a_{i,j} - a_{i-1,j} - a_{i,j-1} + a_{i-1,j-1}.
$$

However, if you want to compute the entire difference array, a simpler and more efficient approach is dimension-by-dimension difference, i.e. enumerate all dimensions and compute the difference of the array along each dimension once.

Two-dimensional difference information is often used to maintain many rectangle-additions on a two-dimensional array. For example, to add $v$ to each number in the matrix with top-left corner $(x_1,y_1)$ and bottom-right corner $(x_2,y_2)$, we can perform the following operations on its difference array $\{D_{i,j}\}$:

$$
\begin{aligned}
D_{x_1,y_1} &\gets D_{x_1,y_1} + v, \\
D_{x_1,y_2+1} &\gets D_{x_1,y_2+1} - v,\\
D_{x_2+1,y_1} &\gets D_{x_2+1,y_1} - v,\\
D_{x_2+1,y_2+1} &\gets D_{x_2+1,y_2+1} + v.
\end{aligned}
$$

After all modification operations end, executing one two-dimensional prefix sum suffices to quickly query the values of the updated array.

??? example "Reference code"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_7.cpp:core"
    ```

Of course, a similar idea also holds for dimension $k>2$, but the time complexity required for a single modification operation is $O(2^k)$, which becomes impractical as $k$ increases.

### Difference on trees

Difference can be generalized to the rooted-tree case, used to implement range-addition operations along a path on a tree. Depending on whether the maintained information is stored on nodes or edges, tree difference can be divided into **vertex difference** and **edge difference**, which differ slightly in implementation. In addition, compared with the prefix-sum operation on a tree, it is more common to do a subtree sum after all modification operations and then query. This section discusses exactly this situation.

#### Vertex difference

If you want to add $v$ to all vertex weights on the path between nodes $x$ and $y$, you can perform the following operations on its difference sequence $\{D_x\}$:

$$
\begin{aligned}
D_x &\gets D_x + v, \\
D_{\operatorname{lca}(x, y)} &\gets D_{\operatorname{lca}(x, y)} - v,\\
D_y &\gets D_y + v, \\
D_{\operatorname{fa}(\operatorname{lca}(x, y))} &\gets D_{\operatorname{fa}(\operatorname{lca}(x, y))} - v.
\end{aligned}
$$

After all modification operations are complete, computing one subtree sum yields the updated vertex weights.

???+ example "Example"
    When performing a range-addition on the vertex weights along the path between nodes $S$ and $T$, the first two lines of the formula above perform a one-dimensional difference on the path inside the blue box, and the latter two lines perform a one-dimensional difference on the path inside the red box:
    
    ![](./images/prefix_sum1.svg)
    
    Summing bottom-up is equivalent to computing the prefix sum from the bottom up over these two intervals. From this, comparing with the one-dimensional difference operation above, we can see the correctness of the vertex-difference operation.

#### Edge difference

If you want to add $v$ to all edge weights on the path between nodes $x$ and $y$, you can perform the following operations on its difference sequence $\{D_x\}$:

$$
\begin{aligned}
D_x &\gets D_x + v, \\
D_y &\gets D_y + v, \\
D_{\operatorname{lca}(x, y)} &\gets D_{\operatorname{lca}(x, y)} - 2v.
\end{aligned}
$$

After all modification operations are complete, computing one subtree sum yields the updated vertex weights.

???+ example "Example"
    As shown in the figure, the edge-difference operation can be used to solve the edge-weight range-addition problem on the red path.
    
    ![](./images/prefix_sum2.svg)
    
    Since directly performing a difference on edges is rather difficult, the value that should have been accumulated onto the red edge is moved down into the adjacent node, which makes the operation more convenient. Comparing with the vertex-difference formula, you can understand the edge-difference formula.

### Example

???+ example "[Luogu 3128 Max Flow](https://www.luogu.com.cn/problem/P3128)"
    FJ installed $N-1$ pipes among the $N(2 \le N \le 50,000)$ stalls of his barn, with stalls numbered from $1$ to $N$. All stalls are connected by the pipes.
    
    FJ has $K(1 \le K \le 100,000)$ milk-transport routes; the $i$-th route transports from stall $s_i$ to stall $t_i$. A transport route brings one unit of transport pressure to the stalls at its two endpoints as well as to all stalls it passes through in between; you need to compute the pressure of the stall with the maximum pressure.

??? note "Solution idea"
    We need to count how many times each vertex is passed; so use tree difference to add one to each vertex on each path, which quickly gives the number of times each vertex is passed. Here we use the doubling method to compute the LCA, and finally DFS the whole tree; summing the difference array during backtracking gives the answer.

??? note "Reference code"
    ```cpp
    --8<-- "docs/basic/code/prefix-sum/prefix-sum_3.cpp"
    ```

## Exercises

Prefix sums:

-   [Luogu B3612 【深进 1. 例 1】Range Sum](https://www.luogu.com.cn/problem/B3612)
-   [Luogu U69096 Inverse of a Prefix Sum](https://www.luogu.com.cn/problem/U69096)
-   [AtCoder joi2007ho\_a Maximum Sum](https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_a)
-   ["USACO16JAN" Subsequences Summing to Sevens](https://www.luogu.com.cn/problem/P3131)
-   ["USACO05JAN" Moo Volume S](https://www.luogu.com.cn/problem/P6067)

Two-dimensional / multi-dimensional prefix sums:

-   [HDU 6514 Monitor](https://acm.hdu.edu.cn/showproblem.php?pid=6514)
-   [Luogu P1387 Largest Square](https://www.luogu.com.cn/problem/P1387)
-   ["HNOI2003" Laser Bombs](https://www.luogu.com.cn/problem/P2280)
-   [CF 165E Compatible Numbers](https://codeforces.com/contest/165/problem/E)
-   [CF 383E Vowels](https://codeforces.com/problemset/problem/383/E)
-   [ARC 100C Or Plus Max](https://atcoder.jp/contests/arc100/tasks/arc100_c)

Prefix sums on trees:

-   [LOJ 10134.Dis](https://loj.ac/problem/10134)
-   [LOJ 2491. Summation](https://loj.ac/problem/2491)

Difference arrays:

-   [Fenwick Tree 3: Range Modify, Range Query](https://loj.ac/problem/132)
-   ["Poetize6" IncDec Sequence](https://www.luogu.com.cn/problem/P4552)
-   [Luogu P4231 Three Strikes to Kill](https://www.luogu.com.cn/problem/P4231)

Two-dimensional / multi-dimensional difference:

-   [Luogu P3397 Carpet](https://www.luogu.com.cn/problem/P3397)
-   [Luogu P8228 「Wdoi-5」Modular Nuclear Furnace](https://www.luogu.com.cn/problem/P8228)

Difference on trees:

-   [Luogu 3128 Max Flow](https://www.luogu.com.cn/problem/P3128)
-   [JLOI2014 Squirrel's New Home](https://loj.ac/problem/2236)
-   [NOIP2015 Transport Plan](http://uoj.ac/problem/150)
-   [NOIP2016 Running Every Day](http://uoj.ac/problem/261)
