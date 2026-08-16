author: ChungZH, billchenchina, Chrogeek, Early0v0, ethan-enhe, HeRaNO, hsfzLZH1, iamtwz, Ir1d, konnyakuxzy, luoguojie, Marcythm, orzAtalod, StudyingFather, wy-luke, Xeonacid, CCXXXI, chenryang, chenzheAya, CJSoft, cjsoft, countercurrent-time, DawnMagnet, Enter-tainer, GavinZhengOI, Haohu Shen, Henry-ZHR, hjsjhn, hly1204, jaxvanyang, Jebearssica, kenlig, ksyx, megakite, Menci, moon-dim, NachtgeistW, onelittlechildawa, ouuan, shadowice1984, shawlleyw, shuzhouliu, SukkaW, Tiphereth-A, x2e6, Ycrpro, yifan0305, zeningc

The merging and splitting of segment trees are common techniques for segment trees, frequently seen in scenarios where a weighted segment tree maintains a multiset.

For example, when some nodes on a tree have several operations, if child-node information needs to be passed bottom-up to the parent node, and the information at a single node is conveniently maintained with a segment tree, then the technique of segment-tree merging can be applied to control the overall complexity.

## Segment-tree merging

### Process

As the name implies, segment-tree merging means building a new segment tree, in which each node is the result of merging the corresponding nodes of the two original segment trees. It is often used to maintain information on trees or graphs.

Obviously, we cannot really build a full new segment tree each time, so we need to use the dynamically-allocated segment tree mentioned above.

The process of segment-tree merging is essentially quite brute-force:

Suppose the two segment trees are A and B; we start recursively merging from node number 1.

When recursing to a certain node, if the corresponding node on tree A or tree B is empty, directly return the corresponding node on the other tree; this uses the characteristic of the dynamically-allocated segment tree.

If we recurse to a leaf node, we merge the corresponding nodes on the two trees.

Finally, update the current node according to its children and return.

???+ note "Complexity of segment-tree merging"
    Obviously, for two full segment trees, the complexity of a single merge operation is $O(n)$. But in practice a weighted segment tree is often used, and the total number of points of all the segment trees to be merged does not differ much from the scale of $n$. Moreover, when merging one generally does not repeatedly merge a certain segment tree, so the number of points we finally add is roughly on the order of $n\log n$. In this way, the total complexity of merging all segment trees is on the order of $O(n\log n)$. Of course, in some cases, a mergeable heap may be a better choice.

### Implementation

```cpp
int merge(int a, int b, int l, int r) {
  if (!a) return b;
  if (!b) return a;
  if (l == r) {
    // do something...
    return a;
  }
  int mid = (l + r) >> 1;
  tr[a].l = merge(tr[a].l, tr[b].l, l, mid);
  tr[a].r = merge(tr[a].r, tr[b].r, mid + 1, r);
  pushup(a);
  return a;
}
```

### Example problem

???+ note "[luogu P4556 \[Vani has a date\] Tail of a Rainy Day / 【Template】Segment-Tree Merging](https://www.luogu.com.cn/problem/P4556)"
    ??? note "Solution idea"
        A template problem for segment-tree merging; use difference to convert tree modifications into single-point modifications, then dfs upward and merge segment trees to count the answer.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/ds/code/seg/seg_6.cpp"
        ```

## Segment-tree splitting

### Process

Segment-tree splitting is essentially the inverse process of segment-tree merging. Segment-tree splitting only applies to ordered sequences; it is meaningless for unordered sequences, and is commonly used in dynamically-allocated weighted segment trees.

Note that when both splitting and merging exist, we must reclaim nodes when merging, to avoid the problem that nodes may be occupied repeatedly when splitting.

To split $[l,r]$ out of a segment tree whose interval is $[1,N]$, building a new tree:

Start recursively splitting from node number 1; when the node does not exist or the interval $[s,t]$ it represents has no intersection with $[l,r]$, directly backtrack.

When $[s,t]$ has an intersection with $[l,r]$, a new node needs to be created.

When $[s,t]$ is contained in $[l,r]$, the current node needs to be directly attached under the new tree, and the old edge disconnected.

???+ note "Complexity of segment-tree splitting"
    It can be found that there are at most $\log n$ edges that get disconnected, so the final time complexity of each split is $O(\log⁡ n)$, equivalent to the complexity of an interval query.

### Implementation

```cpp
void split(int &p, int &q, int s, int t, int l, int r) {
  if (t < l || r < s) return;
  if (!p) return;
  if (l <= s && t <= r) {
    q = p;
    p = 0;
    return;
  }
  if (!q) q = New();
  int m = s + t >> 1;
  if (l <= m) split(ls[p], ls[q], s, m, l, r);
  if (m < r) split(rs[p], rs[q], m + 1, t, l, r);
  push_up(p);
  push_up(q);
}
```

### Example problem

???+ note "[P5494 【Template】Segment-Tree Splitting](https://www.luogu.com.cn/problem/P5494)"
    ??? note "Solution idea"
        A template problem for segment-tree splitting; split $[x,y]$ out.
        
        -   Merge tree $t$ into tree $p$: a single merge suffices.
        
        -   Insert $x$ copies of $q$ into tree $p$: single-point modification.
        
        -   Query the number of numbers in $[x,y]$: interval sum.
        
        -   Query the $k$-th smallest.
    
    ??? note "Reference code"
        ```cpp
        --8<-- "docs/ds/code/seg/seg_7.cpp"
        ```

## Exercises

-   [Luogu P4556 \[Vani has a date\] Tail of a Rainy Day / 【Template】Segment-Tree Merging](https://www.luogu.com.cn/problem/P4556)
-   [Luogu P5494 【Template】Segment-Tree Splitting](https://www.luogu.com.cn/problem/P5494)
-   [Luogu P1600 Loving to Run Every Day](https://www.luogu.com.cn/problem/P1600)
-   [Luogu P4577 \[FJOI2018\] Leadership Group Problem](https://www.luogu.com.cn/problem/P4577)
-   [Luogu P2824 \[HEOI2016/TJOI2016\] Sorting](https://www.luogu.com.cn/problem/P2824)
