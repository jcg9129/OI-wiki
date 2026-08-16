## Introduction

???+ note "[Luogu 4097 \[HEOI2013\]Segment](https://www.luogu.com.cn/problem/P4097)"
    Required to maintain two operations in the Cartesian coordinate plane (forced online):
    
    1.  Add a segment to the plane. Denote the label of the $i$-th inserted segment as $i$; the two endpoints of the segment are $(x_0,y_0)$ and $(x_1,y_1)$.
    2.  Given a number $k$, query, among the segments intersecting the line $x = k$, the label of the segment whose intersection point has the maximum $y$-coordinate (if several segments' intersection points with the query line have the same maximum $y$-coordinate, output the segment with the smallest label). In particular, if no segment intersects the given line, output $0$.
    
    The data satisfy: total number of operations $1 \leq n \leq 10^5$, $1 \leq k, x_0, x_1 \leq 39989$, $1 \leq y_0, y_1 \leq 10^9$.

We find that a traditional segment tree cannot maintain such information well. In this case, the **Li Chao segment tree** comes into being.

## Process

We can transform the task into maintaining the following operations:

-   Add a linear function whose domain is $[l,r]$;
-   Given $k$, find, among all linear functions whose domain contains $k$, the one with the maximum value at $x=k$; if multiple functions have the same value, choose the one with the smallest label.

???+ warning "Note"
    When a segment is perpendicular to the $x$-axis, a division-by-zero situation arises. Suppose the two endpoints of the segment are $(x,y_0)$ and $(x,y_1)$, with $y_0<y_1$; then insert the linear function $f(x)=0\cdot x+y_1$ with domain $[x,x]$.

Seeing range modification, we follow the common approach of a segment tree solving range problems and give each node a lazy tag. The lazy tag of each node $i$ is a segment, denoted $l_i$, meaning to use $l_i$ to update the entire range represented by that node.

Now we need to insert a segment $f$; consider some segment-tree range completely covered by the new segment $f$. If that range has no tag, directly apply the tag updated with that segment.

If the range already has a tag, since tags are hard to merge, we can only push the tag down. But child nodes also have their own tags, which may also conflict, so we must recursively push down the tag.

![](images/li-chao-tree-1.png)

As shown, according to whether the new segment $f$ takes a larger value than the original tag $g$, we can split the current range into two sub-ranges. Among them, **one sub-range is certainly completely contained in the left range or the right range**; that is, among the two segments, there is certainly one that can only possibly be the answer of the left range or only possibly be the answer of the right range. We use this segment to recursively update the corresponding subtree, and use the other segment as the lazy tag to update the entire range, which guarantees the complexity of recursive pushdown. A segment is pushed down only when it can only possibly be the answer of the left or right range, so we need not worry about missing some segments.

Specifically, let the midpoint of the current range be $m$; we compare the value of the new segment $f$ at the midpoint with the value of the original best segment $g$ at the midpoint.

If the new segment $f$ is better, swap $f$ and $g$. Now consider the case where $f$ is not as good as $g$ at the midpoint:

1.  If $f$ is better at the left endpoint, then $f$ and $g$ must have an intersection point in the left half range, and $f$ can only be better than $g$ in the left range, so recurse into the left child for pushdown;
2.  If $f$ is better at the right endpoint, then $f$ and $g$ must have an intersection point in the right half range, and $f$ can only be better than $g$ in the right range, so recurse into the right child for pushdown;
3.  If $g$ is better at both the left and right endpoints, then $f$ cannot become the answer, and no further pushdown is needed.

Besides these two cases, there is another case where $f$ and $g$ intersect exactly at the midpoint; in the program implementation this can be classified into the case where $f$ is not as good as $g$ at the midpoint, and the result will recurse and push down toward the endpoint where $f$ is better.

Finally, take $g$ as the lazy tag of the current range.

Pushing down the tag:

???+ note "Implementation"
    ```cpp
    constexpr double eps = 1e-9;
    
    int cmp(double x, double y) {  // because floating-point is used, there is precision error
      if (x - y > eps) return 1;
      if (y - x > eps) return -1;
      return 0;
    }
    
    //...
    
    void upd(int root, int cl, int cr, int u) {  // modify the range completely covered by the segment
      int &v = s[root], mid = (cl + cr) >> 1;
      int bmid = cmp(calc(u, mid), calc(v, mid));
      if (bmid == 1 || (!bmid && u < v))  // in this problem remember to compare the segment labels
        swap(u, v);
      int bl = cmp(calc(u, cl), calc(v, cl)), br = cmp(calc(u, cr), calc(v, cr));
      if (bl == 1 || (!bl && u < v)) upd(root << 1, cl, mid, u);
      if (br == 1 || (!br && u < v)) upd(root << 1 | 1, mid + 1, cr, u);
      // at most one of the two if conditions above holds, which guarantees the time complexity of the Li Chao tree
    }
    ```

Splitting the segment:

???+ note "Implementation"
    ```cpp
    void update(int root, int cl, int cr, int l, int r,
                int u) {  // locate the range completely covered by the inserted segment
      if (l <= cl && cr <= r) {
        upd(root, cl, cr, u);  // completely covers the current range, update the current range's tag
        return;
      }
      int mid = (cl + cr) >> 1;
      if (l <= mid) update(root << 1, cl, mid, l, r, u);  // recursively split the range
      if (mid < r) update(root << 1 | 1, mid + 1, cr, l, r, u);
    }
    ```

Note that the lazy tag is not equivalent to the segment with the maximum value at the range midpoint.

![](images/li-chao-tree-2.png)

As shown, after adding the yellow segment, only the tag of the red node is updated, while the tag of the green node has not yet been changed. But at the midpoints of the second, third, and fourth green ranges, the yellow segment obviously has the maximum value.

When querying, we can use the tag-permanence idea, and among the tag segments of all segment-tree ranges containing $x$ (no more than $O(\log n)$ of them), compare to obtain the final answer.

Query:

???+ note "Implementation"
    ```cpp
    pdi query(int root, int l, int r, int d) {  // query
      if (r < d || d < l) return {0, 0};
      int mid = (l + r) >> 1;
      double res = calc(s[root], d);
      if (l == r) return {res, s[root]};
      return pmax({res, s[root]}, pmax(query(root << 1, l, mid, d),
                                       query(root << 1 | 1, mid + 1, r, d)));
    }
    ```

According to the description above, the time complexity of the query process is obviously $O(\log n)$, while during insertion, we need to split the original segment into $O(\log n)$ ranges, and for each range we again need to spend $O(\log n)$ time recursively pushing down, so the time complexity of the insertion process is $O(\log^2 n)$.

??? note "[\[HEOI2013\]Segment](https://www.luogu.com.cn/problem/P4097) reference code"
    ```cpp
    --8<-- "docs/ds/code/li-chao-tree/li-chao-tree_1.cpp"
    ```

## Merging

Similar to the merging of an ordinary segment tree, we define the following procedure to merge two Li Chao segment tree nodes $u,v$, and take $u$ as the new root.

1.  If $v$ is empty, end the procedure.

2.  If $u$ is empty, copy $v$ to $u$.

3.  Insert the segment corresponding to $v$ into the subtree rooted at $u$.

4.  Recursively merge the left and right subtrees of $u,v$ correspondingly.

If the total number of points involved in merging several Li Chao segment trees is $n$, then the complexity of this procedure is $O(n\log n)$: for the node any segment corresponds to on the tree, each time it is moved, we either increase its depth by $1$ or delete it directly from the tree, and the cost of both operations is $O(1)$; and each point has depth at most $O(\log n)$, so the complexity is as above.

???+ note "Implementation"
    ```cpp
    void upd(int &root, int cl, int cr,
             int u) {  // merging multiple Li Chao segment trees, using dynamic node allocation
      static int idx = 0;
      if (!root) {
        s[root = ++idx] = u;
        return;
      }
      int &v = s[root], mid = (cl + cr) >> 1;
      int bmid = cmp(calc(u, mid), calc(v, mid));
      if (bmid == 1 || (!bmid && u < v)) swap(u, v);
      int bl = cmp(calc(u, cl), calc(v, cl)), br = cmp(calc(u, cr), calc(v, cr));
      if (bl == 1 || (!bl && u < v)) upd(ls[root], cl, mid, u);
      if (br == 1 || (!br && u < v)) upd(rs[root], mid + 1, cr, u);
    }
    
    int merge(int &u, int &v, int l, int r) {
      if (!u || !v) {
        return u + v;
      }
      if (l == r) {
        int b = cmp(calc(s[v], l), calc(s[u], l));
        if (b == 1 || (!b && s[v] < s[u])) return v;
        return u;
      }
      upd(u, l, r, s[v]);
      int mid = (l + r) >> 1;
      ls[u] = merge(ls[u], ls[v], l, mid);
      rs[u] = merge(rs[u], rs[v], mid + 1, r);
      return u;
    }
    ```

## Exercises

[「JSOI2008」Blue Mary Starts a Company](https://www.luogu.com.cn/problem/P4254)

[「CodeChef」TSUM2 Sum on Tree](https://www.codechef.com/problems/TSUM2)

[「USACO13MAR」Hill Walk G](https://www.luogu.com.cn/problem/P3081)

[「CF932F」Escape Through Leaf](https://codeforces.com/problemset/problem/932/F)
