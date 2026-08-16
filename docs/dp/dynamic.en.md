Prerequisites: [matrices](../math/linear-algebra/matrix.md), [heavy-light decomposition](../graph/hld.md).

The dynamic DP problem is a piece of "black technology" presented by Maokun at WC2018, generally used to solve DP problems on trees with vertex-weight (edge-weight) modification operations.

## Example

Take this template problem as an example to explain the process of dynamic DP.

???+ note "Example [Luogu P4719 【Template】Dynamic DP](https://www.luogu.com.cn/problem/P4719)"
    Given a tree with $n$ vertices, where the vertices have vertex weights. There are $m$ operations; each operation gives $x,y$ meaning to modify the weight of vertex $x$ to $y$. After each operation you need to find the weight of the maximum-weight independent set of this tree.

### Generalized matrix multiplication

Define generalized matrix multiplication $A\times B=C$ as:

$$
C_{i,j}=\max_{k=1}^{n}(A_{i,k}+B_{k,j})
$$

This is equivalent to changing the multiplication in ordinary matrix multiplication to addition, and the addition to the $\max$ operation.

Meanwhile, generalized matrix multiplication satisfies associativity, so fast matrix exponentiation can be used.

### Without modification operations

Let $f_{i,0}$ denote the maximum answer without selecting $i$, and $f_{i,1}$ denote the maximum answer with selecting $i$.

Then we have the DP equations:

$$
\begin{cases}f_{i,0}=\sum_{son}\max(f_{son,0},f_{son,1})\\f_{i,1}=w_i+\sum_{son}f_{son,0}\end{cases}
$$

The answer is $\max(f_{root,0},f_{root,1})$.

### With modification operations

First perform heavy-light decomposition on this tree; suppose there is such a heavy chain:

![](./images/dynamic.png)

Let $g_{i,0}$ denote the maximum answer when $i$ is not selected and only the subtrees of $i$'s light children are allowed to be selected, and $g_{i,1}$ denote the maximum answer when $i$ is selected, not considering $son_i$, where $son_i$ denotes $i$'s heavy child.

Assuming we already know $g_{i,0/1}$, we have the DP equations:

$$
\begin{cases}f_{i,0}=g_{i,0}+\max(f_{son_i,0},f_{son_i,1})\\f_{i,1}=g_{i,1}+f_{son_i,0}\end{cases}
$$

The answer is $\max(f_{root,0},f_{root,1})$.

We can construct the matrix:

$$
\begin{bmatrix}
g_{i,0} & g_{i,0}\\
g_{i,1} & -\infty
\end{bmatrix}\times 
\begin{bmatrix}
f_{son_i,0}\\f_{son_i,1}
\end{bmatrix}=
\begin{bmatrix}
f_{i,0}\\f_{i,1}
\end{bmatrix}
$$

Note that we use the generalized multiplication rule here.

We can see that during a modification operation we only need to modify $g_{i,1}$ and each heavy chain going upward.

### The specific approach

1.  DFS-preprocess to compute $f_{i,0/1}$ and $g_{i,0/1}$.

2.  Perform heavy-light decomposition on this tree (note that, because querying a vertex requires computing the interval matrix product from that vertex to the end of the heavy chain it lies on, for each vertex record $End_i$ denoting the number of the end vertex of the heavy chain $i$ lies on), and build a segment tree for each heavy chain; the segment tree maintains the $g$ matrix and the interval product of the $g$ matrices.

3.  When modifying, first modify $g_{i,1}$ and the matrix of vertex $i$ in the segment tree, compute the change of the $top_i$ matrix, and modify up to the $fa_{top_i}$ matrix.

4.  When querying, it is the interval product from 1 to the end of the heavy chain it lies on, and finally take a $\max$.

??? note "Implementation"
    ```cpp
    --8<-- "docs/dp/code/dynamic/dynamic_1.cpp"
    ```

## Exercises

-   [SPOJ GSS3 - Can you answer these queries III](https://www.spoj.com/problems/GSS3/)
-   ["NOIP2018" Defend the Kingdom](https://loj.ac/p/2955)
-   ["SDOI2017" Tree-Cutting Game](https://loj.ac/p/2269)
