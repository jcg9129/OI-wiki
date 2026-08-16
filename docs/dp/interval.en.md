## Definition

Interval dynamic programming is an extension of linear dynamic programming; when it divides the problem in stages, it has a lot to do with the order in which elements appear within a stage and which elements from the previous stage they are merged from.

Let the state $f(i,j)$ denote the maximum value obtainable by merging all elements from index position $i$ to $j$; then $f(i,j)=\max\{f(i,k)+f(k+1,j)+cost\}$, where $cost$ is the value of merging these two groups of elements.

## Properties

Interval DP has the following characteristics:

**Merging**: integrating two or more parts, and of course this can also be reversed;

**Feature**: the problem can be decomposed into a form where parts can be merged pairwise;

**Solving**: set the optimal value for the whole problem, enumerate the merge point, decompose the problem into left and right parts, and finally merge the optimal values of the two parts to obtain the optimal value of the original problem.

## Explanation

### Example

???+ note "["NOI1995" Stone Merging](https://loj.ac/problem/10147)"
    Problem summary: on a ring there are $n$ numbers $a_1,a_2,\dots,a_n$; perform $n-1$ merge operations, each merging two adjacent piles into one pile and earning a score equal to the sum of the number of stones in the new pile. You need to maximize your score.

Consider the case where the stones are on a chain rather than a ring.

Let $f(i,j)$ denote the maximum score of merging all stones in the interval $[i,j]$ together.

Write the **state-transition equation**: $f(i,j)=\max\{f(i,k)+f(k+1,j)+\sum_{t=i}^{j} a_t \}~(i\le k<j)$

Let $sum_i$ denote the prefix sum of the array $a$; the state-transition equation transforms into $f(i,j)=\max\{f(i,k)+f(k+1,j)+sum_j-sum_{i-1} \}$.

### How to perform the state transition

Since computing the value of $f(i,j)$ requires knowing the values of all $f(i,k)$ and $f(k+1,j)$, and both of these contain a number of elements smaller than $f(i,j)$, we use $len=j-i+1$ as the stage of the DP. First enumerate $len$ from small to large, then enumerate the value of $i$, compute the value of $j$ from $len$ and $i$ using the formula, and then enumerate $k$; the time complexity is $O(n^3)$.

### How to handle the ring

In the problem the stones form a ring rather than a chain; what should we do?

**Method one**: since the stones form a ring, we can enumerate the position at which to split it, turning this ring into a chain; since this must be enumerated $n$ times, the final time complexity is $O(n^4)$.

**Method two**: we double this chain into $2\times n$ piles, where the $i$-th pile is the same as the $(n+i)$-th pile; after solving with dynamic programming, take the optimal value among $f(1,n),f(2,n+1),\dots,f(n,2n-1)$ as the final answer. The time complexity is $O(n^3)$.

## Implementation

=== "C++"
    ```cpp
    for (len = 2; len <= n; len++)
      for (i = 1; i <= 2 * n - len; i++) {
        int j = len + i - 1;
        for (k = i; k < j; k++)
          f[i][j] = max(f[i][j], f[i][k] + f[k + 1][j] + sum[j] - sum[i - 1]);
      }
    ```

=== "Python"
    ```python
    for len in range(2, n + 1):
        for i in range(1, 2 * n - len + 1):
            j = len + i - 1
            for k in range(i, j):
                f[i][j] = max(f[i][j], f[i][k] + f[k + 1][j] + sum[j] - sum[i - 1])
    ```

## A few practice problems

[NOIP 2006 Energy Necklace](https://www.luogu.com.cn/problem/P1063)

[NOIP 2007 Matrix Number-Taking Game](https://www.luogu.com.cn/problem/P1005)

["IOI2000" Post Office](https://www.luogu.com.cn/problem/P4767)
