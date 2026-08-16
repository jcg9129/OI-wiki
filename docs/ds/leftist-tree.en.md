author: JiZiQian, llleixx, firefly-zjyjoe

## What is a leftist tree?

The **leftist tree**, like the [**pairing heap**](./pairing-heap.md), is a **mergeable heap** that has the heap property and can be quickly merged.

## Definition and properties of the leftist tree

For a binary tree, we define an **external node** as a node with fewer than two children, and define the $\mathrm{dist}$ of a node as the number of edges passed on its way to the nearest external node in its subtree. The $\mathrm{dist}$ of an empty node is $0$.

???+ note "Note"
    In some materials, the definition of $\mathrm{dist}$ is the $\mathrm{dist}$ in this article minus $1$; this definition is because when writing code some null-check procedures can be omitted, but note that the $\mathrm{dist}$ of an empty node should be preset to $-1$. In all code in this article, the definition of $\mathrm{dist}$ **is the one where an empty node's $\mathrm{dist}$ is $-1$**; please note the difference from the $\mathrm{dist}$ definition in the prose.

The leftist tree is a binary tree; it not only has the heap property but is also "leftist": the $\mathrm{dist}$ of each node's left child is greater than or equal to the $\mathrm{dist}$ of its right child.

Therefore, the $\mathrm{dist}$ of each node of a leftist tree equals the $\mathrm{dist}$ of its right child plus one.

Note that $\mathrm{dist}$ is not the depth; **the depth of a leftist tree is not guaranteed**, and a leftward chain also conforms to the definition of a leftist tree.

## Core operation: merge

When merging two heaps, since the heap property must be satisfied, first take the root with the smaller value (for convenience, this article discusses a min-heap) as the root of the merged heap, then take this root's left child as the left child of the merged heap, recursively merge its right child with the other heap as the right child of the merged heap. To satisfy the leftist property, if after merging the left child's $\mathrm{dist}$ is smaller than the right child's $\mathrm{dist}$, swap the two children.

Reference code:

???+ note "Implementation"
    ```cpp
    int merge(int x, int y) {
      if (!x || !y) return x | y;  // if one heap is empty, return the other heap
      if (t[x].val > t[y].val) swap(x, y);  // take the one with the smaller value as the root
      t[x].rs = merge(t[x].rs, y);          // recursively merge the right child with the other heap
      if (t[t[x].rs].d > t[t[x].ls].d)
        swap(t[x].ls, t[x].rs);   // if the leftist property is not satisfied, swap the left and right children
      t[x].d = t[t[x].rs].d + 1;  // update dist
      return x;
    }
    ```

Because of the leftist property, each level of recursion decreases the $\mathrm{dist}$ of one heap's root by $1$, and for a binary tree with $n$ nodes, the root's $\mathrm{dist}$ does not exceed $\left\lceil\log (n+1)\right\rceil$, so the complexity of merging two heaps of sizes $n$ and $m$ is $O(\log n+\log m)$.

???+ note "About the proof of the $\mathrm{dist}$ property"
    A binary tree whose root has $\mathrm{dist}$ $x$ has at least $x-1$ levels that form a full binary tree, so it has at least $2^x-1$ nodes. Note that this property is possessed by all binary trees, not unique to leftist trees.

The leftist tree also has a way of writing that needs no swapping of left and right children: regard the child with larger $\mathrm{dist}$ as the left child and the child with smaller $\mathrm{dist}$ as the right child:

???+ note "Implementation"
    ```cpp
    int& rs(int x) { return t[x].ch[t[t[x].ch[1]].d < t[t[x].ch[0]].d]; }
    
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[x].val < t[y].val) swap(x, y);
      int& rs_ref = rs(x);
      rs_ref = merge(rs_ref, y);
      t[x].d = t[rs(x)].d + 1;
      return x;
    }
    ```

## Other operations of the leftist tree

### Inserting a node

A single node can also be regarded as a heap; just merge.

### Deleting the root

Just merge the root's left and right children.

### Deleting an arbitrary node

#### Method

First merge the left and right children, then update $\mathrm{dist}$ from the bottom up, swapping the left and right children when the leftist property is not satisfied, and end the recursion when $\mathrm{dist}$ does not need to be updated:

???+ note "Implementation"
    ```cpp
    int& rs(int x) { return t[x].ch[t[t[x].ch[1]].d < t[t[x].ch[0]].d]; }
    
    // with pushup, directly merging the left and right children implements deleting the node while keeping the leftist property
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[x].val < t[y].val) swap(x, y);
      int& rs_ref = rs(x);
      rs_ref = merge(rs_ref, y);
      t[rs_ref].fa = x;
      t[x].d = t[rs(x)].d + 1;
      return x;
    }
    
    void pushup(int x) {
      if (!x) return;
      if (t[x].d != t[rs(x)].d + 1) {
        t[x].d = t[rs(x)].d + 1;
        pushup(t[x].fa);
      }
    }
    
    void erase(int x) {
      int y = merge(t[x].ch[0], t[x].ch[1]);
      t[y].fa = t[x].fa;
      if (t[t[x].fa].ch[0] == x)
        t[t[x].fa].ch[0] = y;
      else if (t[t[x].fa].ch[1] == x)
        t[t[x].fa].ch[1] = y;
      pushup(t[y].fa);
    }
    ```

#### Complexity proof

First consider the `merge` process; each time it moves $x$ or $y$ down one level, i.e. in the most extreme case, it always chooses the right node of the leftist tree (the node with the smallest $\mathrm{dist}$) to go down one level, at which point $\mathrm{dist}$ decreases by $1$.

Then consider the `pushup` process; let the node currently being `pushup`ed be $x$, its parent be $y$, and a node's "initial $\mathrm{dist}$" be its $\mathrm{dist}$ before `pushup`. Recursing from the parent of the deleted node, there are two cases:

1.  $x$ is $y$'s right child; in this case $y$'s initial $\mathrm{dist}$ is $x$'s initial $\mathrm{dist}$ plus one.
2.  $x$ is $y$'s left child; since a node's $\mathrm{dist}$ decreases by at most one, only when $y$'s left and right children have equal initial $\mathrm{dist}$ (in which case the left child's $\mathrm{dist}$ decreasing by one causes the left and right children to swap) does the recursion continue, so $y$'s initial $\mathrm{dist}$ is still $x$'s initial $\mathrm{dist}$ plus one.

So we obtain that each level of recursion increases $x$'s initial $\mathrm{dist}$ by one, so it recurses at most $O(\log n)$ levels.

### Adding/subtracting a value to the whole heap, or multiplying by a positive number

Actually any operation that can be tagged and does not change the relative magnitude is fine.

Apply a tag at the root, and push down the tag when deleting the root / merging heaps (accessing the children):

???+ note "Implementation"
    ```cpp
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[x].val > t[y].val) swap(x, y);
      pushdown(x);
      t[x].rs = merge(t[x].rs, y);
      if (t[t[x].rs].d > t[t[x].ls].d) swap(t[x].ls, t[x].rs);
      t[x].d = t[t[x].rs].d + 1;
      return x;
    }
    
    int pop(int x) {
      pushdown(x);
      return merge(t[x].ls, t[x].rs);
    }
    ```

## Other mergeable heaps

### Randomized heap

???+ note "Implementation"
    ```cpp
    int merge(int x, int y) {
      if (!x || !y) return x | y;
      if (t[y].val < t[x].val) swap(x, y);
      if (rand() & 1)  // randomly choose whether to swap the left and right children
        swap(t[x].ls, t[x].rs);
      t[x].ls = merge(t[x].ls, y);
      return x;
    }
    ```

We can see that the only difference of this implementation is that it uses random numbers to implement the merge, so that the related computation of $\mathrm{dist}$ can be omitted. And its average time complexity is also $O(\log n)$; for a detailed proof, refer to [Randomized Heap](https://cp-algorithms.com/data_structures/randomized_heap.html).

### Skew heap

The skew heap is the self-adjusting form of the leftist tree. When merging two heaps, it unconditionally swaps all nodes on the merge path, thereby attempting to maintain balance. By amortized analysis, the complexity of insertion, merging, and delete-min of a top-down skew heap is $O(\log n)$[^ref1].

## Examples

### Template problems

[Luogu P3377 【Template】Leftist Tree (Mergeable Heap)](https://www.luogu.com.cn/problem/P3377)

[Monkey King](https://www.luogu.com.cn/problem/P1456)

[The Roman Game](https://www.luogu.com.cn/problem/P2713)

Note that:

1.  Before merging, check whether they are already in the same heap.

2.  The depth of a leftist tree may reach $O(n)$, so finding the heap top a point is in must be maintained with a DSU; one cannot brute-force jump to parents directly. (Although many problems have weak data, and brute-force jumping to parents can pass……) (When maintaining the root with a DSU, ensure the old root points to the new root and the new root points to itself.)

??? note "Reference code for The Roman Game"
    ```cpp
    --8<-- "docs/ds/code/leftist-tree/leftist-tree_1.cpp"
    ```

### Problems on trees

[「APIO2012」Dispatching](https://www.luogu.com.cn/problem/P1552)

[「JLOI2015」Siege of Cities](https://loj.ac/problem/2107)

This kind of problem often maintains a heap at each node, merges with the children, and pops, modifies, and computes the answer according to the problem; it is a bit like problems similar to segment-tree merging.

??? note "Reference code for Siege of Cities"
    ```cpp
    --8<-- "docs/ds/code/leftist-tree/leftist-tree_2.cpp"
    ```

### [「SCOI2011」Tricky Operations](https://loj.ac/problem/2441)

First, finding the heap top a node is in must use a DSU, not brute-force jumping upward.

Then consider single-point query; if we use the ordinary method of applying tags, we would have to query the sum of tags on the path from the point to the root, which in the worst case can reach $O(n)$ complexity. If only the heap top has a tag, we can query quickly, but how to achieve this?

We can use a way similar to heuristic merging: each time we merge, brute-force push down the tag of the smaller heap to each node, and then take the larger heap's tag as the merged heap's tag. Since after merging there is the other heap's tag, when the smaller heap pushes down its tag it should push down its tag minus the other heap's tag. Since the size of the heap a node is in at least doubles each time it is merged, each node has a tag pushed down at most $O(\log n)$ times, so the total complexity of brute-force pushing down tags is $O(n\log n)$.

Then consider single-point add: first delete, then update, and finally insert.

Then for the global maximum, one can maintain the heap top of each heap with a balanced tree / a heap supporting deletion of an arbitrary node (such as a leftist tree) / a multiset.

So, each operation is as follows:

1.  Brute-force push down the tag of the heap with fewer points, merge the two heaps, update size and tag, and remove from the multiset the original heap top that is no longer the heap top after merging.
2.  Delete the node, update the value, insert it back, and update the multiset. It is necessary to discuss whether the deleted node is the root.
3.  Apply a tag to the heap top and update the multiset.
4.  Apply a global tag.
5.  Query value + heap-top tag + global tag.
6.  Query the root's value + heap-top tag + global tag.
7.  Query the multiset maximum + global tag.

??? note "Reference code for Tricky Operations"
    ```cpp
    --8<-- "docs/ds/code/leftist-tree/leftist-tree_3.cpp"
    ```

### [「BOI2004」Sequence](https://www.luogu.com.cn/problem/P4331)

This is a paper problem; for details see [《Huang Yuanhe -- Characteristics and Applications of the Leftist Tree》](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2005%E8%AE%BA%E6%96%87%E9%9B%86/%E9%BB%84%E6%BA%90%E6%B2%B3--%E5%B7%A6%E5%81%8F%E6%A0%91%E7%9A%84%E7%89%B9%E7%82%B9%E5%8F%8A%E5%85%B6%E5%BA%94%E7%94%A8/%E9%BB%84%E6%BA%90%E6%B2%B3.pdf).

## References

[^ref1]: [Self-Adjusting Heaps](https://epubs.siam.org/doi/10.1137/0215004)
