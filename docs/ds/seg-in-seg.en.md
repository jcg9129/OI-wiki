author: Chrogeek, HeRaNO, Dev-XYS, Dev-jqe

## Common uses

In algorithm competitions, we sometimes need to maintain multi-dimensional information. At such times, we often need a tree of trees to record the information.

## Implementation principle

Let's consider how to use a tree of trees to perform single-point modification and region query on a 2D plane. Consider the outer segment tree; the subtrees of the bottommost nodes $1$ to $n$ represent the segment trees of rows $1$ to $n$ respectively. Then the parent node corresponding to these bottom-level nodes represents a region where the subtrees of its two child nodes lie.

## Properties

### Space complexity

Under normal circumstances, we cannot build a sub-segment-tree for every node of the outer segment tree, as the space requirement would be too large. A tree of trees generally adopts the strategy of dynamic node allocation. For a single modification, we will involve $\log{n}$ nodes of the outer segment tree, and for the subtree of each node we involve $\log{n}$ nodes, so the space produced by a single modification is at most $\log^2{n}$.

### Time complexity

For the query operation, consider that we perform $\log{n}$ operations on the outer segment tree, and each operation performs $\log{n}$ operations on an inner segment tree, so the time complexity is $\log^2{n}$.
The modification operation has the same complexity as the query operation, also $\log^2{n}$.

## Classic example problem

[Mo Shang Hua Kai](https://www.luogu.com.cn/problem/P3810) Sort and process the first dimension, then use a tree of trees to maintain the second and third dimensions.

## Example code

Second-dimension query

```cpp
int tree_query(int k, int l, int r, int x) {
  if (k == 0) return 0;
  if (1 <= l && r <= sec[x].y) return vec_query(ou_root[k], 1, p, 1, sec[x].z);
  int mid = l + r >> 1, res = 0;
  if (1 <= mid) res += tree_query(ou_ch[k][0], l, mid, x);
  if (sec[x].y > mid) res += tree_query(ou_ch[k][1], mid + 1, r, x);
  return res;
}
```

Second-dimension modification

```cpp
void tree_insert(int &k, int l, int r, int x) {
  if (k == 0) k = ++ou_tot;
  vec_insert(ou_root[k], 1, p, sec[x].z);
  if (l == r) return;
  int mid = l + r >> 1;
  if (sec[x].y <= mid)
    tree_insert(ou_ch[k][0], l, mid, x);
  else
    tree_insert(ou_ch[k][1], mid + 1, r, x);
}
```

Third-dimension query

```cpp
int vec_query(int k, int l, int r, int x, int y) {
  if (k == 0) return 0;
  if (x <= l && r <= y) return data[k];
  int mid = l + r >> 1, res = 0;
  if (x <= mid) res += vec_query(ch[k][0], l, mid, x, y);
  if (y > mid) res += vec_query(ch[k][1], mid + 1, r, x, y);
  return res;
}
```

Third-dimension modification

```cpp
void vec_insert(int &k, int l, int r, int loc) {
  if (k == 0) k = ++tot;
  data[k]++;
  if (l == r) return;
  int mid = l + r >> 1;
  if (loc <= mid) vec_insert(ch[k][0], l, mid, loc);
  if (loc > mid) vec_insert(ch[k][1], mid + 1, r, loc);
}
```

## Related algorithms

When facing problems with multi-dimensional information, if the problem does not require forced online, we can also consider divide-and-conquer algorithms such as **CDQ divide-and-conquer** or **overall binary search** to avoid using advanced data structures and reduce the difficulty of code implementation.
