author: Dev-jqe, HeRaNO, huaruoji

## Common uses

In competitive programming, we sometimes need to maintain multi-dimensional information. In such cases, we often need a tree-of-trees to record the information. When we need to maintain the predecessor, successor, $k$-th largest, the rank of some number, or insertion and deletion, we usually need a balanced tree to satisfy our needs, i.e. a balanced tree nested inside a segment tree.

## Process

We take the **second-degree balanced tree** (二逼平衡树) as an example to explain the implementation principle.

Regarding the construction of a tree-of-trees, we build the outer segment tree normally, and for a certain node on the segment tree, we build a balanced tree containing the sequence that node covers. In the specific operation, we can insert the sequence elements one by one, and each time we pass a segment-tree node, we add that element into that node's balanced tree.

Operation one, find the rank of some value in some interval: we operate on the outer segment tree normally, and for the balanced tree of a node within some interval, we return the number of elements in the balanced tree smaller than that value; when merging intervals, we sum the counts of smaller elements. Finally, add $1$ to the return value, which is the rank of the value in the interval.

Operation two, find the value ranked $k$ in some interval: we can use a binary-search strategy. Because an element may have multiple copies, its rank is an interval, and some elements do not exist in the original sequence. So we adopt an idea similar to operation one: we use the number of elements smaller than that value as a reference for binary search, and thus obtain the solution.

Operation three, replace some number with another number: we only need to delete that number in all balanced trees containing it, and then insert the other number. The outer layer still operates as a normal segment tree.

Operation four, find the predecessor of some value in some interval: we operate on the outer segment tree normally, and for the balanced tree of a node within some interval, we return the predecessor of that value in that balanced tree; when merging the segment tree's interval results, we take the maximum.

## Properties

### Space complexity

Each element is added to $O(\log n)$ balanced trees, so the space complexity is $O((n + q)\log{n})$.

### Time complexity

-   For operations 1, 3, 4, we consider that we perform $O(\log{n})$ operations on the outer segment tree, and each operation performs $O(\log{n})$ operations on an inner balanced tree, so the time complexity is $O(\log^2{n})$.
-   For operation 2, there is one more binary-search process, giving $O(\log^3{n})$.

## Classic example

[Second-degree balanced tree](https://loj.ac/problem/106): outer segment tree, inner balanced tree.

## Implementation

For the balanced-tree part of the code, refer to [Splay](./splay.md) and other entries.

Operation one:

```cpp
int vec_rank(int k, int l, int r, int x, int y, int t) {
  if (x <= l && r <= y) {
    return spy[k].chk_rank(t);
  }
  int mid = l + r >> 1;
  int res = 0;
  if (x <= mid) res += vec_rank(k << 1, l, mid, x, y, t);
  if (y > mid) res += vec_rank(k << 1 | 1, mid + 1, r, x, y, t);
  if (x <= mid && y > mid) res--;
  return res;
}
```

Operation two:

```cpp
int el = 0, er = 100000001, emid;
while (el != er) {
  emid = el + er >> 1;
  if (vec_rank(1, 1, n, tl, tr, emid) - 1 < tk)
    el = emid + 1;
  else
    er = emid;
}
printf("%d\n", el - 1);
```

Operation three:

```cpp
void vec_chg(int k, int l, int r, int loc, int x) {
  int t = spy[k].find(dat[loc]);
  spy[k].dele(t);
  spy[k].insert(x);
  if (l == r) return;
  int mid = l + r >> 1;
  if (loc <= mid) vec_chg(k << 1, l, mid, loc, x);
  if (loc > mid) vec_chg(k << 1 | 1, mid + 1, r, loc, x);
}
```

Operation four:

```cpp
int vec_front(int k, int l, int r, int x, int y, int t) {
  if (x <= l && r <= y) return spy[k].chk_front(t);
  int mid = l + r >> 1;
  int res = 0;
  if (x <= mid) res = max(res, vec_front(k << 1, l, mid, x, y, t));
  if (y > mid) res = max(res, vec_front(k << 1 | 1, mid + 1, r, x, y, t));
  return res;
}
```

## Related algorithms

When facing problems with multi-dimensional information, if the problem does not require forced online processing, we can also consider divide-and-conquer algorithms such as [CDQ divide and conquer](../misc/cdq-divide.md) or [parallel binary search](../misc/parallel-binsearch.md) to avoid using advanced data structures and reduce the difficulty of code implementation.
