author: Ir1d, HeRaNO, Xeonacid

## Introduction

In fact, sqrt decomposition (blocking) is an idea, not a data structure.

From NOIP to NOI to IOI, the blocking idea appears at all difficulty levels.

The basic idea of blocking is to obtain a better time complexity than the general brute-force algorithm by appropriately dividing the original data and preprocessing partial information on each divided block.

The time complexity of blocking mainly depends on the block length; one can generally use the mean inequality to find the optimal block length for a given problem and the corresponding time complexity.

Blocking is a very flexible idea; compared with the Fenwick tree and segment tree, the advantage of blocking is that it is more general and can maintain much information that Fenwick trees and segment trees cannot.

Of course, the disadvantage of blocking is that its asymptotic complexity is not as good as that of segment trees and Fenwick trees.

However, on most problems, blocking is still a good choice for solving them.

Below are several examples.

## Interval sum

??? note "Example [LibreOJ 6280 Introduction to Sequence Blocking 4](https://loj.ac/problem/6280)"
    Given a sequence $\{a_i\}$ of length $n$, $n$ operations need to be performed. The operations are of two kinds:
    
    1.  Add $x$ to all numbers between $a_l$ and $a_r$;
    2.  Compute $\sum_{i=l}^r a_i$.
    
        $1 \leq n \leq 5 \times 10^4$

We block the sequence with $s$ elements per block and record the interval sum $b_i$ of each block.

$$
\underbrace{a_1, a_2, \ldots, a_s}_{b_1}, \underbrace{a_{s+1}, \ldots, a_{2s}}_{b_2}, \dots, \underbrace{a_{(s-1) \times s+1}, \dots, a_n}_{b_{\frac{n}{s}}}
$$

The last block may be incomplete (because $n$ is very likely not a multiple of $s$), but this does not have much impact on our discussion.

First, look at the query operation:

-   If $l$ and $r$ are within the same block, just sum by brute force directly; because the block length is $s$, the worst-case complexity is $O(s)$.
-   If $l$ and $r$ are not within the same block, then the answer consists of three parts: the incomplete block starting with $l$, several complete blocks in the middle, and the incomplete block ending with $r$. For the incomplete blocks, still use the brute-force computation above; for the complete blocks, directly use the already-computed $b_i$ to sum. In this case, the worst-case complexity is $O(\dfrac{n}{s}+s)$.

Next is the modification operation:

-   If $l$ and $r$ are within the same block, just modify by brute force directly; because the block length is $s$, the worst-case complexity is $O(s)$.
-   If $l$ and $r$ are not within the same block, then three parts need to be modified: the incomplete block starting with $l$, several complete blocks in the middle, and the incomplete block ending with $r$. For the incomplete blocks, still brute-force modify each element's value (don't forget to update the interval sum $b_i$); for the complete blocks, directly modify $b_i$. In this case, the worst-case complexity is still $O(\dfrac{n}{s}+s)$.

By the mean inequality, when $\dfrac{n}{s}=s$, i.e. $s=\sqrt n$, the time complexity of a single operation is optimal, being $O(\sqrt n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/decompose/decompose_1.cpp"
    ```

## Interval sum 2

The complexity of the previous approach is $\Omega(1) , O(\sqrt{n})$.

Here we introduce an $O(\sqrt{n}) - O(1)$ algorithm.

For $O(1)$ queries, we can maintain various prefix sums.

However, in the presence of modifications, it is inconvenient to maintain; we can only maintain the prefix sum within a single block.

As well as the prefix sum with a whole block as a unit.

Each modification is $O(T+\frac{n}{T})$.

Query: it involves three parts, each of which can be obtained directly via prefix sums, with time complexity $O(1)$.

## Blocking the queries

The same problem, now with sequence length $n$ and $m$ operations.

If the number of operations is relatively small, we can record the operations and add the effect of these operations when querying.

Suppose at most $T$ operations are recorded; then modification is $O(1)$ and query is $O(T)$.

After $T$ operations, recompute the prefix sums, $O(n)$.

Total complexity: $O(mT+n\frac{m}{T})$.

When $T=\sqrt{n}$, the total complexity is $O(m \sqrt{n})$.

### Other problems

The blocking idea can also be applied to other integer-related problems: finding the number of zero elements, finding the first nonzero element, counting the number of elements satisfying some property, and so on.

There are also some problems that can be solved by blocking, such as maintaining a set that allows adding or deleting numbers, checking whether a number belongs to this set, and finding the $k$-th largest number. To solve this problem, the numbers must be stored in increasing order and split into multiple blocks, each block containing $\sqrt{n}$ numbers. Each time a number is added or deleted, one must re-block by moving numbers across the boundaries of adjacent blocks.

A very famous offline algorithm, [Mo's algorithm](../misc/mo-algo.md), is also implemented based on the blocking idea.

## Practice problems

-   [UVa - 12003 - Array Transformer](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3154)
-   [UVa - 11990 Dynamic Inversion](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3141)
-   [SPOJ - Give Away](http://www.spoj.com/problems/GIVEAWAY/)
-   [Codeforces - Till I Collapse](http://codeforces.com/contest/786/problem/C)
-   [Codeforces - Destiny](http://codeforces.com/contest/840/problem/D)
-   [Codeforces - Holes](http://codeforces.com/contest/13/problem/E)
-   [Codeforces - XOR and Favorite Number](https://codeforces.com/problemset/problem/617/E)
-   [Codeforces - Powerful array](http://codeforces.com/problemset/problem/86/D)
-   [SPOJ - DQUERY](https://www.spoj.com/problems/DQUERY)

    **This page is mainly translated from the blog post [Sqrt-декомпозиция](http://e-maxx.ru/algo/sqrt_decomposition) and its English translation [Sqrt Decomposition](https://cp-algorithms.com/data_structures/sqrt_decomposition.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**
