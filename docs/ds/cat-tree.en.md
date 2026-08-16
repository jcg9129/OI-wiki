author: ChungZH, billchenchina, Chrogeek, Early0v0, ethan-enhe, HeRaNO, hsfzLZH1, iamtwz, Ir1d, konnyakuxzy, luoguojie, Marcythm, orzAtalod, StudyingFather, wy-luke, Xeonacid, CCXXXI, chenryang, chenzheAya, CJSoft, cjsoft, countercurrent-time, DawnMagnet, Enter-tainer, GavinZhengOI, Haohu Shen, Henry-ZHR, hjsjhn, hly1204, jaxvanyang, Jebearssica, kenlig, ksyx, megakite, Menci, moon-dim, NachtgeistW, onelittlechildawa, ouuan, shadowice1984, shawlleyw, shuzhouliu, SukkaW, Tiphereth-A, x2e6, Ycrpro, yifan0305, zeningc, hcx2012Git

## Introduction

As is well known, a segment tree can support quickly querying the aggregate information of some interval, such as the maximum subarray sum of an interval, the interval sum, the continued product of the interval's matrices, and so on.

But there is a problem: the interval queries of an ordinary segment tree may still be a bit slow in the eyes of some hardcore people.

Simply put, building a segment tree requires $O(n)$ merge operations, and each interval query requires $O(\log{n})$ merge operations. This is tolerable when querying something like the interval sum, but when we need to query information such as the interval linear basis whose merge complexity is as high as $O(\log^2{w})$, then even doing $O(\log{n})$ merges is sometimes unacceptable in terms of time.

The so-called "cat tree" is a kind of static segment tree that does not support modification and only supports fast interval queries.

Constructing such a static segment tree requires $O(n\log{n})$ merge operations, but at this point the query complexity is accelerated to $O(1)$ merge operations.

When handling special information such as a linear basis, the complexity can even be reduced to $O(n\log^2{w})$.

## Principle

When querying the aggregate information of the interval $[l,r]$, find on the segment tree the LCA of the node representing $[l,l]$ and the node representing $[r,r]$; let the interval this node $p$ represents be $[L,R]$, and we will find some very interesting properties:

1.  The interval $[L,R]$ must contain $[l,r]$. Clearly, because it is both an ancestor of $l$ and an ancestor of $r$.

2.  The interval $[l,r]$ must cross the midpoint of $[L,R]$. Since $p$ is the LCA of $l$ and $r$, this means $p$'s left child is an ancestor of $l$ but not of $r$, and $p$'s right child is an ancestor of $r$ but not of $l$. Therefore, $l$ must be within the interval $[L,\mathit{mid}]$ and $r$ must be within the interval $(\mathit{mid},R]$.

With these two properties, we can reduce the query complexity to $O(1)$.

## Implementation

Specifically, when building the tree, for a node on the segment tree, let the interval it represents be $(l,r]$.

Unlike a traditional segment tree which keeps only the sum of $[l,r]$ at this node, we additionally store at this node the suffix-sum array of $(l,\mathit{mid}]$ and the prefix-sum array of $(\mathit{mid},r]$.

This way the complexity of building the tree is $T(n)=2T(n/2)+O(n)=O(n\log{n})$, and likewise the space complexity changes from the original $O(n)$ to $O(n\log{n})$.

Next is the most crucial query.

If the interval we query is $[l,r]$, then we find the LCA of the node representing $[l,l]$ and the node representing $[r,r]$, denoted $p$.

According to the two properties just now, $l,r$ are within the interval $p$ contains and must cross $p$'s midpoint.

This means a very crucial fact: we can use the prefix-sum array and suffix-sum array in $p$ to split $[l,r]$ into $[l,\mathit{mid}]+(\mathit{mid},r]$ and thus piece together the interval $[l,r]$.

And this process only needs $O(1)$ merge operations!

But it seems we've overlooked something?

It seems that computing the LCA is not $O(1)$; brute force is $O(\log{n})$, binary lifting is $O(\log{\log{n}})$, and turning to an ST table has too high a cost……

## Heap-style tree building

Specifically, we pad the sequence up to an integer power of $2$ and then build the segment tree.

At this point we find that the LCA number of two nodes on the segment tree is the longest common prefix (LCP) of the two nodes' binary numbers.

With a little thought, one finds that in binary, `lcp(x,y)=x>>digits[x^y]`. (Here `digits[x]` denotes the number of bits of $x$ in binary, i.e. $\lfloor \log_2 x \rfloor+1$.)

So we only need to precompute a `digits` array to easily accomplish the LCA computation.

This way we have constructed a cat tree.

Since building the tree involves computing prefix sums and suffix sums, for information like the linear basis whose merge is $O(\log^2{w})$ but whose prefix sum is $O(n\log{n})$, using a cat tree can optimize the static interval linear basis from $O(n\log^2{w}+m\log^2{w}\log{n})$ to $O(n\log{n}\log{w}+m\log^2{w})$ complexity.

### References

-   [immortalCO's blog](https://immortalco.blog.uoj.ac/blog/2102)
-   [\[Kle77\]](http://ieeexplore.ieee.org/document/1675628/) V. Klee, "Can the Measure of be Computed in Less than O (n log n) Steps?," Am. Math. Mon., vol. 84, no. 4, pp. 284–285, Apr. 1977.
-   [\[BeW80\]](https://www.tandfonline.com/doi/full/10.1080/00029890.1977.11994336) Bentley and Wood, "An Optimal Worst Case Algorithm for Reporting Intersections of Rectangles," IEEE Trans. Comput., vol. C–29, no. 7, pp. 571–577, Jul. 1980.
