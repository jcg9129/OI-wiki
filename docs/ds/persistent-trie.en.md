## Introduction

The way of making a Trie persistent is similar to the way of making a segment tree persistent: each time we only modify the nodes that are added or whose values are modified, retaining the nodes that are not changed, and connecting edges on the basis of the previous version, so that in the end the Trie tree separated out by traversing from each version's Trie root is complete and contains all the information.

In most persistent-Trie problems, the Trie appears in the form of a [01-Trie](../string/trie.md#维护异或极值).

??? note "Example [Maximum XOR Sum](https://www.luogu.com.cn/problem/P4735)"
    Maintain the following operations on an array $a$ of length $n$:
    
    1.  Append a number $x$ to the end of the array, and the array length $n$ increments by $1$.
    2.  Given a query interval $[l,r]$ and a value $k$, find the maximum of $k \oplus \bigoplus^{n}_{i=p} a_i$ over $l\le p\le r$.

## Process

The value to find may be a bit troublesome; using the common method for handling continuous XOR, let $s_x=\bigoplus_{i=1}^x a_i$; then the original expression is equivalent to $s_{p-1}\oplus s_n\oplus k$. Observing that $s_n \oplus k$ is fixed during the query, the query of the problem changes to querying the maximum of the XOR with a fixed value ($s_n\oplus k$) within the interval $[l-1,r-1]$.

Continuing with an idea similar to the persistent segment tree, consider that each query queries the whole interval. We only need to build a Trie tree for this interval, adding each number in this interval into this Trie, and when querying, jump as much as possible to the place different from the current bit.

To query an interval, we only need to use the idea of prefix sums and difference: subtracting two prefix Trie trees (i.e. two historical versions of adding numbers in order) gives the Trie tree of that interval. Then using the idea of dynamic node allocation, we do not add uncomputed points to reduce space usage.

```cpp
--8<-- "docs/ds/code/persistent-trie/persistent-trie_1.cpp"
```
