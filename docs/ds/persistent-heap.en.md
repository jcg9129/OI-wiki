A persistent mergeable heap is generally used to solve the $k$-th shortest path problem.

If a mergeable heap's time complexity is not amortized, then after making it persistent, the time complexity of a single operation is guaranteed to be $O(\log n)$, i.e. the complexity will not degrade due to special data.

## Persistent leftist tree

Before studying this content, please first understand the relevant content of the [leftist tree](./leftist-tree.md).

### Process

Recall the merge process of a leftist tree. Suppose we want to merge two leftist trees rooted at $x$ and $y$ respectively, and the maintained leftist tree satisfies the min-heap property:

1.  If one of $x,y$ is empty, return $x+y$.

2.  Choose the node with the smaller value among $x,y$ as the root of the merged leftist tree.

3.  Recursively merge $x$'s right subtree with $y$, and take the merged root as $x$'s right child.

4.  Maintain the leftist property of the current merged leftist tree, maintain the `dist` value, and return the chosen root.

Since each recursion decreases `dist[x]+dist[y]` by one, and `dist[x]` is $O(\log n)$, a single merge modifies at most $O(\log n)$ nodes, so the time complexity of doing this is $O(\log n)$.

Persistence requires retaining historical information so that previous versions can be accessed later. To make a leftist tree persistent, we need to copy the path modified along the way.

So the merge process of a persistent leftist tree is like this:

1.  If one of $x,y$ is empty, return $x+y$.

2.  Choose the node with the smaller value among $x,y$, create a copy $p$ of that node, and take it as the root of the merged leftist tree.

3.  Recursively merge $p$'s right subtree with $y$, and take the merged root as $p$'s right child.

4.  Maintain the leftist property of the leftist tree rooted at $p$, maintain its `dist` value, and return $p$.

Since a leftist tree modifies and newly creates at most $O(\log n)$ nodes per merge, letting the number of operations be $m$, the time complexity and space complexity of a persistent leftist tree are both $O(m\log n)$.

### Reference implementation

```cpp
int merge(int x, int y) {
  if (!x || !y) return x + y;
  if (v[x] > v[y]) swap(x, y);
  int p = ++cnt;
  lc[p] = lc[x];
  v[p] = v[x];
  rc[p] = merge(rc[x], y);
  if (dist[lc[p]] < dist[rc[p]]) swap(lc[p], rc[p]);
  dist[p] = dist[rc[p]] + 1;
  return p;
}
```
