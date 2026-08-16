author: hsfzLZH1, Ir1d, JosephusW

A k-D Tree (KDT, k-Dimension Tree) is a data structure that can **efficiently handle information in $k$-dimensional space**.

When the number of nodes $n$ is far greater than $2^k$, applying a k-D Tree has very good time efficiency.

In competitive-programming problems, generally $k=2$. When analyzing the time complexity on this page, $k$ will be considered a constant.

## Building the tree

A k-D Tree has the form of a binary search tree, where each node of the binary search tree corresponds to a point in $k$-dimensional space. Every point in each of its subtrees is within a $k$-dimensional hyper-rectangle, and all points within this hyper-rectangle are also in this subtree.

Suppose we already know the coordinates of $n$ distinct points in $k$-dimensional space and want to build them into a k-D Tree; the steps are as follows:

1.  If the current hyper-rectangle has only one point, return this point.

2.  Choose a dimension and split the current hyper-rectangle into two hyper-rectangles along this dimension.

3.  Choose the cutting point: choose a point in the chosen dimension; those whose value in this dimension is smaller than this point go into one hyper-rectangle (the left subtree), and the rest go into another hyper-rectangle (the right subtree).

4.  Take the chosen point as the root of this subtree, recursively build the left and right subtrees for the two split hyper-rectangles, and maintain the subtree information.

For ease of understanding, let's give an example for $k=2$.

![](./images/kdt1.jpg)

The form of the k-D Tree it builds might be like this:

![](./images/kdt2.jpg)

Here the coordinates at each node of the tree are the coordinates of the chosen split point, and the $x$ or $y$ beside a non-leaf node is the chosen cutting dimension.

Such complexity cannot be guaranteed. For steps $2,3$, we propose two optimizations:

1.  Choose the $k$ dimensions in turn, to ensure that within any $k$ consecutive levels, every dimension is cut.
2.  When choosing the cutting point on a dimension each time, choose the **median** on that dimension, so as to ensure that each split gives left and right subtrees as equal in size as possible.

We can see that after using optimization $2$, the height of the built k-D Tree is at most $\log n+O(1)$.

Now, the bottleneck in the time complexity of building a k-D Tree is quickly selecting the median on a dimension and placing those with a value smaller than the median on that dimension to the left of the median and the rest to the right. If we use the `sort` function to sort each time on that dimension, the time complexity is $O(n\log^2 n)$. In fact, finding the median of $n$ elements once and placing the median at its correct position after sorting can be done in $O(n)$ complexity.

Let's review the idea of quicksort. Each time we select a number, place those smaller than this number to its left and those larger to its right, ensuring this number is at its correct position after sorting, and then recursively sort the values on the left and right. The expected complexity of this is $O(n\log n)$. But since the k-D Tree only requires the median to be at its correct position after sorting, we only need to recursively sort the **one side** containing the median. It can be proven that the expected complexity of this is $O(n)$. In the `algorithm` library, there is a function `nth_element()` implementing the same functionality; to find, among the values between `s[l]` and `s[r]`, the value at position `s[mid]` after sorting by the sort rule `cmp`, while ensuring the values to the left of `s[mid]` are smaller than `s[mid]` and those to the right are larger than `s[mid]`, one only needs to write `nth_element(s+l,s+mid,s+r+1,cmp)`.

With this idea, the time complexity of building a k-D Tree is $O(n\log n)$.

## Operations in high-dimensional space

When querying some information about all points within a high-dimensional rectangular region, record the maximum and minimum values of the coordinates in each dimension within each node's subtree. If the rectangle corresponding to the current subtree has no intersection with the query rectangle, do not continue searching its subtree; if the rectangle corresponding to the current subtree is completely contained within the query rectangle, return the sum of the weights of all points in the current subtree; otherwise, determine whether the current point is within the query rectangle, update the answer, and recursively search for the answer in the left and right subtrees.

??? note "Implementation"
    ```cpp
    int query(int p) {
      if (!p) return 0;
      bool flag{false};
      for (int k : {0, 1}) flag |= (!(l.x[k] <= t[p].L[k] && t[p].R[k] <= h.x[k]));
      if (!flag) return t[p].sum;
      for (int k : {0, 1})
        if (t[p].R[k] < l.x[k] || h.x[k] < t[p].L[k]) return 0;
      int ans{0};
      flag = false;
      for (int k : {0, 1}) flag |= (!(l.x[k] <= t[p].x[k] && t[p].x[k] <= h.x[k]));
      if (!flag) ans = t[p].v;
      return ans += query(t[p].l) + query(t[p].r);
    }
    ```

### Complexity analysis

First consider the two-dimensional case. When querying the rectangle $R$, we divide the nodes on the k-D Tree into three classes:

1.  Disjoint from $R$.
2.  Completely contained in $R$.
3.  Partially contained in $R$.

Clearly the complexity of a single query is the number of class-3 points. Note that the rectangles of class-3 points either completely contain $R$ or are mutually non-containing, and the former clearly number only $O(h)=O(\log n)$; now we analyze the number of the latter.

First, we may as well offset all edges of the rectangle by $\epsilon$ so that the query rectangle does not pass through any existing point. This clearly does not affect the set of points covered by the rectangle query.

Note that the rectangle corresponding to a mutually-non-containing class-3 point must have one edge of $R$ passing through it. So we only need to compute the number of rectangles each edge of $R$ passes through, i.e. how many rectangles corresponding to points a single line segment passes through at most.

Consider a certain node $u$; it has four grandchildren, and from it to each grandchild there is one split in each of two dimensions. By observation, we can find that splitting a rectangle into four sub-rectangles by this method, an axis-parallel line segment passes through at most two regions, i.e. a query starting from $u$ enters at most two grandchildren still having class-3 points (this is not necessarily the case if the line segment coincides exactly with a split boundary, but our operation of offsetting the query rectangle's boundary makes this case not exist).

And because during tree building each point is the median of its entire subtree on the current split dimension, the subtree size must halve. So, letting $u$'s subtree size be $n$, we can write the following recurrence:

$$
T(n)=2T(n/4)+O(1)
$$

By the Master Theorem, $T(n)=O(\sqrt{n})$.

Generalizing the recurrence to $k$ dimensions, i.e. $T(n)=2^{k-1}T(n/2^k)+O(1)$, we get $T(n)=O(n^{1-\frac1k})$ (treating $k$ as a constant).

### Insertion/deletion

If this $k$-dimensional point set being maintained is mutable, i.e. some points may be inserted or deleted, then the balance of the k-D Tree cannot be guaranteed. Due to the construction of the k-D Tree, it cannot support rotations, and a random priority similar to FHQ Treap cannot guarantee its complexity either. For this, there are two relatively common maintenance methods.

???+ note "Note"
    Many contestants use the scapegoat-tree structure to maintain it. But note that in the complexity analysis just now, we required the son's subtree size to strictly halve, i.e. the tree height must be strictly $\log n+O(1)$, whereas a scapegoat tree only satisfies tree height $O(\log n)$, so the query complexity cannot be guaranteed.

#### Sqrt reconstruction

When inserting, first store the point to be inserted, and reconstruct once every $B$ insertions.

For deletion, just mark it. If the requirement is relatively strict, one can maintain how many in the tree have been deleted, and reconstruct once it reaches $B$.

The amortized modification complexity is $O(n\log n/B)$, and the query is $O(B+n^{1-\frac1k})$; if the two quantities are of the same order, then $B=O(\sqrt{n\log n})$ is optimal (modification $O(\sqrt{n\log n})$, query $O(\sqrt{n\log n}+n^{1-\frac1k})$).

#### Binary grouping

Consider maintaining several k-D Trees whose sizes are natural-number powers of $2$, such that the sum of these trees' sizes is $n$.

When inserting, add a new k-D Tree of size $1$, then continually merge trees of the same size (directly flatten and reconstruct). In implementation, one can reconstruct only once.

It is easy to see that the sizes of the trees to be merged must start from $2^0$ with consecutive exponents. The complexity is similar to binary addition, being amortized $O(n\log^2 n)$, because reconstruction itself carries a $\log$.

When querying, directly query on each tree separately, with complexity $O\left(\sum_{i\geq0} (\frac n{2^i})^{1-\frac1k}\right)=O(n^{1-\frac1k})$.

### Example

???+ note "[Luogu P4148 Simple Problem](https://www.luogu.com.cn/problem/P4148)"
    On an $n\times n$ two-dimensional matrix initially all $0$, perform $q$ operations; each operation is one of the following two:
    
    1.  `1 x y A`: add $A$ to the number at coordinate $(x,y)$.
    2.  `2 x1 y1 x2 y2`: output the sum of the numbers within the rectangle with $(x1,y1)$ as the bottom-left corner and $(x2,y2)$ as the top-right corner (including the rectangle boundary).
    
    Forced online. Memory limit `20M`. It is guaranteed that the answer and all intermediate quantities are within the `int` range.
    
    $1\le n\le 500000 , 1\le q\le 200000$

The 20M space rules out all trees-of-trees, and forced online rules out CDQ divide and conquer, so only a k-D Tree can be used.

Below is reference code for binary grouping.

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/kdt/kdt_3.cpp"
    ```

## Neighborhood queries

???+ warning "Warning"
    Using a k-D Tree, the worst-case time complexity of a single nearest-point query is still $O(n)$, but it is nonetheless a good partial-credit-grinding algorithm; please note this when using it. The explanation of neighborhood queries here is only for strengthening understanding of the k-D Tree structure.

???+ note "Example [Luogu P1429 Closest Pair of Points in the Plane (enhanced)](https://www.luogu.com.cn/problem/P1429)"
    Given $n$ points $(x_i,y_i)$ in the plane, find the [Euclidean distance](../geometry/distance.md#euclidean-distance) between the two closest points in the plane.
    
    $2\le n\le 200000 , 0\le x_i,y_i\le 10^9$

First build a 2-D Tree of these $n$ points.

Enumerate each node, and for each node find the point not equal to that node with the smallest distance, thereby computing the answer. Brute-force traversing each node on the 2-D Tree each time has time complexity $O(n)$, so pruning is needed. We can maintain the minimum and maximum values of the coordinates in each dimension of all nodes in a subtree. Suppose the distance of the currently found closest pair is $ans$; if the **nearest** distance from the query point to the rectangle containing all points in a subtree is greater than or equal to $ans$, then there is certainly no answer in this subtree, so do not enter this subtree when searching.

In addition, one can also use a heuristic search method, i.e. if both subtrees of a node may contain the answer, first search for the answer in the subtree nearest to the query point. We can consider that **the nearest distance from the query point to the rectangle corresponding to a subtree is the estimation function of this problem**.

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/kdt/kdt_1.cpp"
    ```

???+ note "Example [「CQOI2016」K-th Farthest Point Pair](https://loj.ac/problem/2043)"
    Given $n$ points $(x_i,y_i)$ in the plane, find the distance between the $k$-th farthest unordered pair of points under Euclidean distance.
    
    $n\le 100000 , 1\le k\le 100 , 0\le x_i,y_i<2^{31}$

Similar to the previous example, from the closest pair it becomes the $k$-th farthest pair, and the estimation function is changed to the farthest distance from the query point to the rectangular region corresponding to a subtree. Use a min-heap to maintain the distances of the top $k$ farthest pairs currently found; if the distance of the currently found pair is greater than the heap top, pop the heap top and insert this distance, and likewise use the heap top's distance to prune.

Since the problem emphasizes unordered pairs, i.e. swapping the order of the two points still gives the same pair, each ordered pair is counted twice, so the input $k$ must be multiplied by $2$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/kdt/kdt_2.cpp"
    ```

## Exercises

[「SDOI2010」Hide and Seek](https://www.luogu.com.cn/problem/P2479)

[「Violet」Angel Doll / SJY Placing Chess Pieces](https://www.luogu.com.cn/problem/P4169)

[「National Training Team」JZPFAR](https://www.luogu.com.cn/problem/P2093)

[「BOI2007」Mokia](https://www.luogu.com.cn/problem/P4390)

[Luogu P4475 Chocolate Kingdom](https://www.luogu.com.cn/problem/P4475)

[「CH Weak-Province Strategy R2」TATT](https://www.luogu.com.cn/problem/P3769)
