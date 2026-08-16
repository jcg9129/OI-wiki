author: Marcythm, Ir1d, Ycrpro, Xeonacid, konnyakuxzy, CJSoft, HeRaNO, ethan-enhe, ChungZH, Chrogeek, hsfzLZH1, billchenchina, orzAtalod, luoguojie, Early0v0, wy-luke

## Introduction

The segment tree is a data structure commonly used in algorithm competitions to maintain **interval information**.

The segment tree can perform operations such as single-point modification, interval modification, and interval query (interval sum, interval maximum, interval minimum) in $O(\log N)$ time complexity.

## Basic structure of the segment tree and building the tree

### Process

The segment tree divides each interval of length not equal to $1$ into two intervals, left and right, and solves recursively, dividing the whole segment into a tree-shaped structure, obtaining the information of an interval by merging the information of its left and right intervals. This data structure can conveniently perform most interval operations.

There is an array of size $5$, $a=\{10,11,12,13,14\}$; to convert it into a segment tree, we have the following approach: let the root node of the segment tree have number $1$, use array $d$ to store our segment tree, and $d_i$ stores the value of the node with number $i$ on the segment tree (here the value maintained by each node is the total sum of the interval this node represents).

Let's first give the shape of this segment tree, as shown:

![](./images/segt1.svg)

In the figure, the interval marked in red font in each node represents the position interval on the $a$ array that this node governs. For example, the interval governed by $d_1$ is $[1,5]$ ($a_1,a_2, \cdots ,a_5$), i.e. the value stored by $d_1$ is $a_1+a_2+ \cdots +a_5$, and $d_1=60$ means $a_1+a_2+ \cdots +a_5=60$.

By observation, it is not hard to find that the left child node of $d_i$ is $d_{2\times i}$, and the right child node of $d_i$ is $d_{2\times i+1}$. If $d_i$ represents the interval $[s,t]$ (i.e. $d_i=a_s+a_{s+1}+ \cdots +a_t$), then the left child node of $d_i$ represents the interval $[ s, \frac{s+t}{2} ]$, and the right child of $d_i$ represents the interval $[ \frac{s+t}{2} +1,t ]$.

In implementation, we consider building the tree recursively. Let the current root node be $p$; if the length of the interval governed by the root node is already $1$, then this node can be directly initialized according to the value at the corresponding position on the $a$ array. Otherwise we split the interval at the midpoint into two subintervals, enter the left and right child nodes respectively to recursively build the tree, and finally merge the information of the two child nodes.

### Implementation

Here is the code implementation; you can refer to the comments for understanding:

=== "C++"
    ```cpp
    void build(int s, int t, int p) {
      // build a segment tree on the interval [s,t], the current root has number p
      if (s == t) {
        d[p] = a[s];
        return;
      }
      int m = s + ((t - s) >> 1);
      // the precedence of the shift operator is lower than addition/subtraction, so add parentheses
      // writing it as (s + t) >> 1 may exceed the int range
      build(s, m, p * 2), build(m + 1, t, p * 2 + 1);
      // recursively build the tree on the left and right intervals
      d[p] = d[p * 2] + d[(p * 2) + 1];
    }
    ```

=== "Python"
    ```python
    def build(s, t, p):
        # build a segment tree on the interval [s,t], the current root has number p
        if s == t:
            d[p] = a[s]
            return
        m = s + ((t - s) >> 1)
        # the precedence of the shift operator is lower than addition/subtraction, so add parentheses
        # writing it as (s + t) >> 1 may exceed the int range
        build(s, m, p * 2)
        build(m + 1, t, p * 2 + 1)
        # recursively build the tree on the left and right intervals
        d[p] = d[p * 2] + d[(p * 2) + 1]
    ```

Regarding the space of the segment tree: if heap-style storage is used ($2p$ is the left child of $p$, $2p+1$ is the right child of $p$), if there are $n$ leaf nodes, then the range of the d array is at most $2^{\left\lceil\log{n}\right\rceil+1}$.

Analysis: it is easy to know that the depth of the segment tree is $\left\lceil\log{n}\right\rceil$, so under heap-style storage the number of leaf nodes (including useless leaf nodes) is $2^{\left\lceil\log{n}\right\rceil}$, and since it is a complete binary tree, its total number of nodes is $2^{\left\lceil\log{n}\right\rceil+1}-1$. Of course, if you are too lazy to calculate, you can directly set the array length to $4n$, because the maximum value of $\frac{2^{\left\lceil\log{n}\right\rceil+1}-1}{n}$ is attained when $n=2^{x}+1(x\in N_{+})$, at which point the number of nodes is $2^{\left\lceil\log{n}\right\rceil+1}-1=2^{x+2}-1=4n-5$.

And heap-style storage has useless leaf nodes; one can consider using a memory pool to manage segment-tree nodes, obtaining from the pool whenever a new node needs to be created. Considering from bottom to top, every two bottom-level nodes must merge into one upper-level node, so, similar to a Huffman tree, one can prove that if there are $n$ leaf nodes, such a segment tree has $2n-1$ nodes in total. Its space efficiency is better than heap-style storage and is the best possible case.

Such a segment tree can be maintained from bottom to top; refer to "[The Power of Statistics - Zhang Kunwei](https://github.com/hzwer/shareOI/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/%E7%BB%9F%E8%AE%A1%E7%9A%84%E5%8A%9B%E9%87%8F%E2%80%94%E2%80%94%E7%BA%BF%E6%AE%B5%E6%A0%91%E5%85%A8%E6%8E%A5%E8%A7%A6_%E5%BC%A0%E6%98%86%E7%8E%AE.pptx)".

## Interval query of the segment tree

### Process

Interval query, such as finding the total sum of interval $[l,r]$ (i.e. $a_l+a_{l+1}+ \cdots +a_r$), finding the interval maximum/minimum, and similar operations.

![](./images/segt1.svg)

Still taking the initial figure as an example, if we want to query the sum of interval $[1,5]$, then just directly obtain the value of $d_1$ ($60$).

If the interval to query is $[3,5]$, then at this time we cannot directly obtain the value of the interval, but $[3,5]$ can be split into $[3,3]$ and $[4,5]$, and the answer of this interval can be obtained by merging the answers of these two intervals.

Generally, if the interval to query is $[l,r]$, then it can be split into at most $O(\log n)$ **maximal** intervals, and merging these intervals gives the answer of $[l,r]$.

### Implementation

Here is the code implementation; you can refer to the comments for understanding:

=== "C++"
    ```cpp
    int getsum(int l, int r, int s, int t, int p) {
      // [l, r] is the query interval, [s, t] is the interval the current node contains, p is the number of the current node
      if (l <= s && t <= r)
        return d[p];  // when the current interval is a subset of the query interval, directly return the sum of the current interval
      int m = s + ((t - s) >> 1), sum = 0;
      if (l <= m) sum += getsum(l, r, s, m, p * 2);
      // if the interval [s, m] represented by the left child intersects the query interval, recursively query the left child
      if (r > m) sum += getsum(l, r, m + 1, t, p * 2 + 1);
      // if the interval [m + 1, t] represented by the right child intersects the query interval, recursively query the right child
      return sum;
    }
    ```

=== "Python"
    ```python
    def getsum(l, r, s, t, p):
        # [l, r] is the query interval, [s, t] is the interval the current node contains, p is the number of the current node
        if l <= s and t <= r:
            return d[p]  # when the current interval is a subset of the query interval, directly return the sum of the current interval
        m = s + ((t - s) >> 1)
        sum = 0
        if l <= m:
            sum = sum + getsum(l, r, s, m, p * 2)
        # if the interval [s, m] represented by the left child intersects the query interval, recursively query the left child
        if r > m:
            sum = sum + getsum(l, r, m + 1, t, p * 2 + 1)
        # if the interval [m + 1, t] represented by the right child intersects the query interval, recursively query the right child
        return sum
    ```

## Interval modification of the segment tree and lazy tags

### Process

If we are required to modify the interval $[l,r]$, and traverse and modify every node contained in the interval $[l,r]$ once each, the time complexity is unbearable. Here we need to introduce something called a **"lazy tag"**.

A lazy tag, simply put, reduces the possibly unnecessary number of operations by delaying changes to node information. Each time a modification is performed, we use a tagging method to indicate that the interval corresponding to this node was changed in a certain operation, but do not update the information of this node's child nodes. The substantive modification is only performed the next time the tagged node is visited.

Still taking the initial figure as an example, we will perform several operations of adding a value to the numbers in an interval. We now add a $t_i$ to each node, representing the tag value the node carries.

The situation at the very beginning is like this (to save space, the interval governed by each node is no longer shown here):

![](./images/segt2.svg)

Now we prepare to add $5$ to each number in $[3,5]$. Based on the earlier experience of interval query, we quickly find two maximal intervals $[3,3]$ and $[4,5]$ (corresponding to node $5$ and node $3$ on the segment tree respectively).

We directly modify these two nodes and tag them:

![](./images/segt3.svg)

We find that although the information of node $3$ has been modified (because this interval governs two numbers, the number added to $d_3$ is $5 \times 2=10$), its two child nodes have not yet been updated, still retaining the information from before the modification. But don't worry; although the modification has not yet been performed, when we want to query the information of these two child nodes, we will use the tag to modify the information of these two child nodes, so that the query result is still accurate.

Next let's query the sum of each number in the interval $[4,4]$.

We recursively find the interval $[4,5]$, and find that this interval is not our target interval, and there is still a tag on this interval. At this point it is time to push down the tag. We update the information of the two subintervals of this interval, and clear the tag on this interval.

![](./images/segt4.svg)

Now the values of nodes $6$ and $7$ become the latest values, and the query result is also accurate.

### Implementation

Next is the reference implementation of the interval modification and query operations in the presence of tags.

Interval modification (adding a value to an interval):

=== "C++"
    ```cpp
    // [l, r] is the modification interval, c is the change amount of the modified elements, [s, t] is the interval the current node contains, p
    // is the number of the current node
    void update(int l, int r, int c, int s, int t, int p) {
      // when the current interval is a subset of the modification interval, directly modify the value of the current node, then tag it, and end the modification
      if (l <= s && t <= r) {
        d[p] += (t - s + 1) * c, b[p] += c;
        return;
      }
      int m = s + ((t - s) >> 1);
      if (b[p] && s != t) {
        // if the current node's lazy tag is non-empty, update the values and lazy-tag values of the current node's two child nodes
        d[p * 2] += b[p] * (m - s + 1), d[p * 2 + 1] += b[p] * (t - m);
        b[p * 2] += b[p], b[p * 2 + 1] += b[p];  // push the tag down to the child nodes
        b[p] = 0;                                // clear the current node's tag
      }
      if (l <= m) update(l, r, c, s, m, p * 2);
      if (r > m) update(l, r, c, m + 1, t, p * 2 + 1);
      d[p] = d[p * 2] + d[p * 2 + 1];
    }
    ```

=== "Python"
    ```python
    def update(l, r, c, s, t, p):
        # [l, r] is the modification interval, c is the change amount of the modified elements, [s, t] is the interval the current node contains, p
        # is the number of the current node
        if l <= s and t <= r:
            d[p] = d[p] + (t - s + 1) * c
            b[p] = b[p] + c
            return
        # when the current interval is a subset of the modification interval, directly modify the value of the current node, then tag it, and end the modification
        m = s + ((t - s) >> 1)
        if b[p] and s != t:
            # if the current node's lazy tag is non-empty, update the values and lazy-tag values of the current node's two child nodes
            d[p * 2] = d[p * 2] + b[p] * (m - s + 1)
            d[p * 2 + 1] = d[p * 2 + 1] + b[p] * (t - m)
            # push the tag down to the child nodes
            b[p * 2] = b[p * 2] + b[p]
            b[p * 2 + 1] = b[p * 2 + 1] + b[p]
            # clear the current node's tag
            b[p] = 0
        if l <= m:
            update(l, r, c, s, m, p * 2)
        if r > m:
            update(l, r, c, m + 1, t, p * 2 + 1)
        d[p] = d[p * 2] + d[p * 2 + 1]
    ```

Interval query (interval sum):

=== "C++"
    ```cpp
    int getsum(int l, int r, int s, int t, int p) {
      // [l, r] is the query interval, [s, t] is the interval the current node contains, p is the number of the current node
      if (l <= s && t <= r) return d[p];
      // when the current interval is a subset of the query interval, directly return the sum of the current interval
      int m = s + ((t - s) >> 1);
      if (b[p]) {
        // if the current node's lazy tag is non-empty, update the values and lazy-tag values of the current node's two child nodes
        d[p * 2] += b[p] * (m - s + 1), d[p * 2 + 1] += b[p] * (t - m);
        b[p * 2] += b[p], b[p * 2 + 1] += b[p];  // push the tag down to the child nodes
        b[p] = 0;                                // clear the current node's tag
      }
      int sum = 0;
      if (l <= m) sum = getsum(l, r, s, m, p * 2);
      if (r > m) sum += getsum(l, r, m + 1, t, p * 2 + 1);
      return sum;
    }
    ```

=== "Python"
    ```python
    def getsum(l, r, s, t, p):
        # [l, r] is the query interval, [s, t] is the interval the current node contains, p is the number of the current node
        if l <= s and t <= r:
            return d[p]
        # when the current interval is a subset of the query interval, directly return the sum of the current interval
        m = s + ((t - s) >> 1)
        if b[p]:
            # if the current node's lazy tag is non-empty, update the values and lazy-tag values of the current node's two child nodes
            d[p * 2] = d[p * 2] + b[p] * (m - s + 1)
            d[p * 2 + 1] = d[p * 2 + 1] + b[p] * (t - m)
            # push the tag down to the child nodes
            b[p * 2] = b[p * 2] + b[p]
            b[p * 2 + 1] = b[p * 2 + 1] + b[p]
            # clear the current node's tag
            b[p] = 0
        sum = 0
        if l <= m:
            sum = getsum(l, r, s, m, p * 2)
        if r > m:
            sum = sum + getsum(l, r, m + 1, t, p * 2 + 1)
        return sum
    ```

If you want to implement modifying an interval to a certain value rather than adding a certain value, the code is as follows:

=== "C++"
    ```cpp
    void update(int l, int r, int c, int s, int t, int p) {
      if (l <= s && t <= r) {
        d[p] = (t - s + 1) * c, b[p] = c, v[p] = 1;
        return;
      }
      int m = s + ((t - s) >> 1);
      // an extra array stores whether the value is modified
      if (v[p]) {
        d[p * 2] = b[p] * (m - s + 1), d[p * 2 + 1] = b[p] * (t - m);
        b[p * 2] = b[p * 2 + 1] = b[p];
        v[p * 2] = v[p * 2 + 1] = 1;
        v[p] = 0;
      }
      if (l <= m) update(l, r, c, s, m, p * 2);
      if (r > m) update(l, r, c, m + 1, t, p * 2 + 1);
      d[p] = d[p * 2] + d[p * 2 + 1];
    }
    
    int getsum(int l, int r, int s, int t, int p) {
      if (l <= s && t <= r) return d[p];
      int m = s + ((t - s) >> 1);
      if (v[p]) {
        d[p * 2] = b[p] * (m - s + 1), d[p * 2 + 1] = b[p] * (t - m);
        b[p * 2] = b[p * 2 + 1] = b[p];
        v[p * 2] = v[p * 2 + 1] = 1;
        v[p] = 0;
      }
      int sum = 0;
      if (l <= m) sum = getsum(l, r, s, m, p * 2);
      if (r > m) sum += getsum(l, r, m + 1, t, p * 2 + 1);
      return sum;
    }
    ```

=== "Python"
    ```python
    def update(l, r, c, s, t, p):
        if l <= s and t <= r:
            d[p] = (t - s + 1) * c
            b[p] = c
            v[p] = 1
            return
        m = s + ((t - s) >> 1)
        if v[p]:
            d[p * 2] = b[p] * (m - s + 1)
            d[p * 2 + 1] = b[p] * (t - m)
            b[p * 2] = b[p * 2 + 1] = b[p]
            v[p * 2] = v[p * 2 + 1] = 1
            v[p] = 0
        if l <= m:
            update(l, r, c, s, m, p * 2)
        if r > m:
            update(l, r, c, m + 1, t, p * 2 + 1)
        d[p] = d[p * 2] + d[p * 2 + 1]
    
    
    def getsum(l, r, s, t, p):
        if l <= s and t <= r:
            return d[p]
        m = s + ((t - s) >> 1)
        if v[p]:
            d[p * 2] = b[p] * (m - s + 1)
            d[p * 2 + 1] = b[p] * (t - m)
            b[p * 2] = b[p * 2 + 1] = b[p]
            v[p * 2] = v[p * 2 + 1] = 1
            v[p] = 0
        sum = 0
        if l <= m:
            sum = getsum(l, r, s, m, p * 2)
        if r > m:
            sum = sum + getsum(l, r, m + 1, t, p * 2 + 1)
        return sum
    ```

## Dynamically-allocated segment tree

Earlier it was mentioned that under heap-style storage, one needs to allocate an array of size $4n$ for the segment tree. To save space, we can avoid building the tree all at once, and initially build only one root node representing the whole interval. Only when we need to access a certain subinterval do we build the child node representing this interval. In this way we no longer use $2p$ and $2p+1$ to represent the children of node $p$, but use $\text{ls}$ and $\text{rs}$ to record the child numbers. In short, the core idea of the dynamically-allocated segment tree is: **a node is created only when it is needed**.

The time complexity of a single operation is unchanged, being $O(\log n)$. Since each operation may create and access a whole new series of nodes, the scale of the number of nodes after $m$ single-point operations is $O(m\log n)$. At most $2n-1$ nodes are also needed, with no waste.

Single-point modification:

```cpp
// root represents the root node of the whole segment tree; cnt represents the current number of nodes
int n, cnt, root;
int sum[n * 2], ls[n * 2], rs[n * 2];

// usage: update(root, 1, n, x, f); where x is the number of the node to modify
void update(int& p, int s, int t, int x, int f) {  // pass by reference
  if (!p) p = ++cnt;  // when the node is empty, create a new node
  if (s == t) {
    sum[p] += f;
    return;
  }
  int m = s + ((t - s) >> 1);
  if (x <= m)
    update(ls[p], s, m, x, f);
  else
    update(rs[p], m + 1, t, x, f);
  sum[p] = sum[ls[p]] + sum[rs[p]];  // pushup
}
```

Interval query:

```cpp
// usage: query(root, 1, n, l, r);
int query(int p, int s, int t, int l, int r) {
  if (!p) return 0;  // if the node is empty, return 0
  if (s >= l && t <= r) return sum[p];
  int m = s + ((t - s) >> 1), ans = 0;
  if (l <= m) ans += query(ls[p], s, m, l, r);
  if (r > m) ans += query(rs[p], m + 1, t, l, r);
  return ans;
}
```

Interval modification is the same, but when pushing down the tag, note that if a child is missing, directly create a new child. Or use the tag-permanence technique.

## Some optimizations

Here we summarize several optimizations of the segment tree:

-   At leaf nodes there is no need to push down the lazy tag, so the lazy tag need not be pushed down to leaf nodes.

-   Pushing down the lazy tag can be written as a dedicated function `pushdown`, and updating the current node from child nodes can also be written as a dedicated function `maintain` (or, symmetrically, `pushup`), reducing the difficulty of writing code.

-   Tag permanence: if it is certain that the lazy tag will not be added to overflow midway (i.e. exceed the maximum range representable by that type of data), then the tag can be made permanent. Tag permanence can avoid pushing down the lazy tag; one only needs to add the effect of the tag into the answer when querying, thereby reducing the program's constant factor. How to handle it specifically is related to the characteristics of the problem, and needs to be written in combination with the problem. This is also a technique used in trees of trees and persistent data structures.

## C++ templates

??? note "SegTreeLazyRangeAdd, a segment-tree template that can do interval add/sum"
    ```cpp
    --8<-- "docs/ds/code/seg/seg_4.hpp"
    ```

??? note "SegTreeLazyRangeSet, a segment-tree template that can do interval modification/sum"
    ```cpp
    --8<-- "docs/ds/code/seg/seg_5.hpp"
    ```

## Example problems

???+ note "[luogu P3372 【Template】Segment Tree 1](https://www.luogu.com.cn/problem/P3372)"
    Given a sequence, you need to perform the following two operations:
    
    -   Add $k$ to each number in a certain interval.
    
    -   Find the sum of each number in a certain interval.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/ds/code/seg/seg_1.cpp"
        ```

???+ note "[luogu P3373 【Template】Segment Tree 2](https://www.luogu.com.cn/problem/P3373)"
    Given a sequence, you need to perform the following three operations:
    
    -   Multiply each number in a certain interval by $x$.
    
    -   Add $x$ to each number in a certain interval.
    
    -   Find the sum of each number in a certain interval.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/ds/code/seg/seg_2.cpp"
        ```

???+ note "[HihoCoder 1078 Interval Modification of a Segment Tree](https://vjudge.net/problem/HihoCoder-1078)"
    Suppose $N$ kinds of goods are placed on a shelf from left to right, numbered sequentially from $1$ to $N$, where the price of the good numbered $i$ is $Pi$. Each operation of Little Hi is one of two possibilities: the first is modifying prices—Little Hi gives an interval $[L, R]$ and a new price $\textit{NewP}$, and the prices of all goods numbered in this interval become $\textit{NewP}$. The second operation is a query—Little Hi gives an interval $[L, R]$, and what Little Ho has to do is compute the total price of all goods numbered in this interval, and then tell Little Hi.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/ds/code/seg/seg_3.cpp"
        ```

???+ note "[2018 Multi-University Training Contest 5 Problem G. Glad You Came](https://acm.hdu.edu.cn/showproblem.php?pid=6356)"
    ??? note "Solution idea"
        Just maintain the permanent tag of each interval, and finally run a DFS on the segment tree to count the result. Note to add a pruning optimization when tagging, otherwise it will TLE.

## Extensions

The segment tree has very wide applications; common extensions and variants are as follows:

-   [Persistent segment tree](./persistent-seg.md)
-   Various trees of trees:
    -   [Segment tree nesting a segment tree](./seg-in-seg.md)
    -   [Fenwick tree nesting a segment tree](./seg-in-bit.md)
    -   [Segment tree nesting a balanced tree](./balanced-in-seg.md)
    -   [Balanced tree nesting a Fenwick tree](./seg-in-balanced.md)
-   [Li Chao segment tree](./li-chao-tree.md)
-   [Cat tree](./cat-tree.md)
-   [Segment tree beats (Jiry segment tree)](./seg-beats.md)

For detailed content, please refer to the relevant pages.

## Application: segment-tree optimized graph construction

In the process of adding edges to build a graph, we sometimes encounter such problems, where a point connects an edge to a continuous interval of points, or a continuous interval connects an edge to a point; if we really connect them one by one, then once the number of points increases the complexity blows up, and here we need to use the interval property of the segment tree to optimize our graph construction.

Below is a segment tree.

![](./images/segt5.svg)

Each node represents an interval; suppose we want to connect an edge to the interval $[2, 4]$.

![](./images/segt6.svg)

In some problems, there also appears the situation where an interval connects to a point, in which case we just reverse all the directed edges of the first figure above; the tree above is called the in-tree, and the one below is called the out-tree.

![](./images/segt7.svg)

???+ note "[Legacy](https://codeforces.com/problemset/problem/786/B)"
    Problem summary: there are $n$ points and $q$ operations. Each operation is one of the following three types:
    
    -   Operation one: connect a directed edge $u \rightarrow v$ with weight $w$.
    -   Operation two: for all $i \in [l,r]$ connect a directed edge $u \rightarrow i$ with weight $w$.
    -   Operation three: for all $i \in [l,r]$ connect a directed edge $i \rightarrow u$ with weight $w$.
    
    Find the shortest path from point $s$ to the other points.
    
    $1 \le n,q \le 10^5, 1 \le w \le 10^9$.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/ds/code/seg/seg_8.cpp"
        ```

## Practice problems

-   [luogu P3372 【Template】Segment Tree 1](https://www.luogu.com.cn/problem/P3372)
-   [luogu P13825 Segment Tree 1.5 【Dynamically-Allocated Segment Tree】](https://www.luogu.com.cn/problem/P13825)
-   [luogu P3373 【Template】Segment Tree 2](https://www.luogu.com.cn/problem/P3373)
-   [luogu P4588 【TJOI2018】Mathematical Computation](https://www.luogu.com.cn/problem/P4588)
-   [luogu P5490 【Template】Scan Line & Union of Rectangle Areas](https://www.luogu.com.cn/problem/P5490)
-   [luogu P1471 Variance](https://www.luogu.com.cn/problem/P1471)
