## Definition

![ST table schematic](images/st.svg)

The ST table (Sparse Table) is a data structure used to solve **repeatable-contribution problems**.

???+ note "What is a repeatable-contribution problem?"
    A **repeatable-contribution problem** means that for an operation $\operatorname{opt}$ satisfying $x\operatorname{opt} x=x$, the corresponding interval query is a repeatable-contribution problem. For example, the maximum has $\max(x,x)=x$, and gcd has $\operatorname{gcd}(x,x)=x$, so RMQ and interval GCD are repeatable-contribution problems. Something like interval sum does not have this property; if the preprocessed intervals used to compute the interval sum overlap, it will cause the overlapping part to be counted twice, which is what we do not want to see. In addition, $\operatorname{opt}$ must also satisfy associativity in order to be solved with the ST table.

???+ note "What is RMQ?"
    RMQ is the abbreviation for the English Range Maximum/Minimum Query, meaning the interval maximum (minimum) value. There are many methods to solve the RMQ problem; you can refer to the [RMQ topic](../topic/rmq.md).

## Introduction

???+ example "[Luogu P3865 【Template】ST Table & RMQ Problem](https://www.luogu.com.cn/problem/P3865)"
    Given $n$ ($1\le n\le 10^5$) integers, there are $m$ ($1\le m\le 2\times 10^6$) queries; for each query, you need to answer the maximum value in the interval $[l,r]$.

Consider the brute-force approach. Each time, scan the interval $[l,r]$ once and find the maximum value.

Obviously, this algorithm will time out.

## ST table

The ST table is based on the [binary lifting](../basic/binary-lifting.md) idea, and can achieve $\Theta(n\log n)$ preprocessing and $\Theta(1)$ answering of each query. But it does not support modification operations.

Based on the binary-lifting idea, we consider how to find the interval maximum. It can be found that if we follow the general binary-lifting procedure, jumping $2^i$ steps each time, the complexity of a query is still $\Theta(\log n)$, which is not better than a segment tree; on the contrary, the preprocessing step is even slower than a segment tree.

We find that $\max(x,x)=x$, which means the interval maximum is a problem with the "repeatable-contribution" property. Even if the preprocessed intervals used to solve it have overlapping parts, as long as the union of these intervals is the queried interval, the final computed answer is correct.

If we manually simulate it, we can find that we can use at most two preprocessed intervals to cover the query interval, which means the time complexity of a query can be reduced to $\Theta(1)$, which is very effective when handling problems with a large number of queries.

The specific implementation is as follows:

Let $f(i,j)$ denote the maximum value of the interval $[i,i+2^j-1]$.

Obviously $f(i,0)=a_i$.

According to the definition, the second dimension corresponds to "jumping $2^j-1$ steps" in binary lifting; following the binary-lifting idea, write out the state transition equation: $f(i,j)=\max(f(i,j-1),f(i+2^{j-1},j-1))$.

![](./images/st-preprocess-lift.svg)

The above is the preprocessing part. And for the query, it can be simply implemented as follows:

For each query $[l,r]$, we split it into two parts: $[l,l+2^s-1]$ and $[r-2^s+1,r]$, where $s=\left\lfloor\log_2(r-l+1)\right\rfloor$. The maximum of the results of the two parts is the answer.

![ST table query process](./images/st-query.svg)

According to the above argument for the "repeatable-contribution problem", since the maximum is a "repeatable-contribution problem", the overlap does not affect the interval maximum. And because these two intervals completely cover $[l,r]$, the correctness of the answer can be guaranteed.

???+ example "[Luogu P3865 【Template】ST Table & RMQ Problem](https://www.luogu.com.cn/problem/P3865) reference implementation"
    === "C style"
        ```cpp
        --8<-- "docs/ds/code/sparse-table/sparse-table_1.cpp"
        ```
    
    === "C++ style"
        ```cpp
        --8<-- "docs/ds/code/sparse-table/sparse-table_2.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/ds/code/sparse-table/sparse-table_1.py"
        ```

## Points to note

1.  The input and output data are generally very large, so it is recommended to enable input/output optimization.

2.  When preprocessing the ST table, it is usually necessary to establish an array with one dimension of size $\log n$ and the other dimension of size $n$; at this point the dimension of size $\log n$ should preferentially be the first dimension, to improve cache locality.

3.  Recomputing the logarithm function value with [std::log](https://en.cppreference.com/w/cpp/numeric/math/log) each time is not worthwhile; it is recommended to use built-in functions such as `__builtin_clz` or `__lg` for the computation. If these built-in functions cannot be used, one can also preprocess the logarithm function values. The preprocessing method is shown below:

$$
\begin{cases}
\texttt{Logn}[1] \gets 0, \\
\texttt{Logn}\left[i\right] \gets \texttt{Logn}\left[\frac{i}{2}\right] + 1.
\end{cases}
$$

## ST table maintaining other information

Besides RMQ, there are other "repeatable-contribution problems". For example "interval bitwise AND", "interval bitwise OR", and "interval GCD" can all be efficiently solved by the ST table.

Note that for "interval GCD", the query complexity of the ST table is not better than that of a segment tree (let the value range be $w$; the query complexity of the ST table is $\Theta(\log w)$, while that of the segment tree is $\Theta(\log n+\log w)$, and the value range is generally larger than $n$), but the preprocessing complexity of the ST table is also not worse than that of the segment tree, and in terms of programming complexity the ST table is much simpler than the segment tree.

If we analyze it, "repeatable-contribution problems" generally carry some kind of RMQ-like component. For example, "interval bitwise AND" is taking the minimum for each bit, while "interval GCD" is taking the minimum of the exponent of each prime factor.

## Summary

The ST table can well maintain "repeatable-contribution" interval information (which should also satisfy associativity), has relatively low time complexity, and has a very small amount of code compared with other algorithms. However, the information the ST table can maintain is very limited, cannot be well extended, and does not support modification operations.

## Exercises

-   [「SCOI2007」Rainfall](https://loj.ac/p/2279)

-   [\[USACO07JAN\] Balanced Lineup](https://www.luogu.com.cn/problem/P2880)

## Appendix: time-complexity analysis of the ST table for interval GCD

While the algorithm runs, it may go through $\Theta(\log n)$ iterations. Each iteration may use the GCD function for recursion; let the value range be $w$; the time complexity of the GCD function is at most $\Omega(\log w)$, so the total time complexity seemingly is $O(n\log n\log w)$.

However, in the GCD process, each recursion (except the last) will at least halve some number in the sequence, and the maximum number of times a number in the sequence can be halved is $\log_2 (w^n)=\Theta(n\log w)$, so the recursive part of GCD runs at most $O(n\log w)$ times. Adding the $\Theta(n\log n)$ of the loop part (and the last layer of recursion), the final time complexity is $O(n(\log w+\log n))$; since data can be constructed to make the time complexity $\Omega(n(\log w+\log n))$, the final time complexity is $\Theta(n(\log w+\log n))$.

The time complexity of the query part is easy to analyze; considering the worst case, i.e. each query queries the worst pair of numbers, the time complexity is $\Theta(\log w)$. Therefore, the time complexity of the ST table maintaining "interval GCD" is preprocessing $\Theta(n(\log n+\log w))$, and a single query $\Theta(\log w)$.

The corresponding operations of the segment tree are preprocessing $\Theta(n\log w)$, and a single query $\Theta(\log n+\log w)$.

This is not a rigorous mathematical argument; a more rigorous one is attached below:

??? note "A more rigorous proof"
    To understand this passage, one may need to have knowledge of the "potential analysis method" from [time complexity](../basic/complexity.md).
    
    First analyze the time complexity of the preprocessing part:
    
    Let the "sequence under consideration" be the sequence of the current layer's loop when preprocessing the ST table. For example, the sequence of layer zero is the original sequence, and the sequence of layer one is the sequence of layer zero after one iteration, i.e. `st[1..n][1]`, which we denote as $A$.
    
    And the potential function is defined as the base-two logarithm of the cumulative product of all numbers in the "sequence under consideration". That is: $\Phi(A)=\log_2\left(\prod\limits_{i=1}^n A_i\right)$.
    
    In one iteration, the time spent is the sum of the time spent by the iteration loop and the time spent by GCD. Among them, the time spent by GCD varies in length. The shortest may have only two or even one recursion, while the longest may have $O(\log w)$ recursions. However, in the GCD process, except for the very first layer and the very last layer, each recursion will at least halve some result in the "sequence under consideration". That is, $\Phi(A)$ will decrease by at least $1$, and the time used by that layer of recursion can be amortized by the potential function.
    
    At the same time, we can see that the initial value of $\Phi(A)$ is at most $\log_2 (w^n)=\Theta(n\log w)$, and $\Phi(A)$ is non-increasing. So, the time complexity of the preprocessing part of the ST table is $O(n(\log w+\log n))$.
