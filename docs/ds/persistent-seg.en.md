## Chairman tree

The chairman tree, whose full name is the persistent weighted segment tree, see the [Zhihu discussion](https://www.zhihu.com/question/59195374).

???+ warning "About the functional segment tree"
    A **functional segment tree** refers to a segment tree using the idea of functional programming. In functional-programming thinking, computer operations are regarded as mathematical functions, and mutable state or variables are avoided. It is not hard to see that a functional segment tree is [fully persistent](persistent.md#fully-persistent).

## Introduction

Let's first introduce a problem: given a sequence $a$ of $n$ integers, for a specified closed interval $[l, r]$, query the $k$-th smallest value within that interval.

How would you solve it?

One feasible scheme is: use a chairman tree.
The main idea of the chairman tree is: save the historical version at each insertion operation, so as to query the $k$-th smallest in an interval.

How to save it? Simply and brute-forcely, open a segment tree each time.  
Wouldn't that blow up the space?

## Explanation

Let's analyze; we find that the number of points modified in each modification operation is the same.  
(For example, in the figure below, the node with weight 1 in $[1,8]$ is modified; the red points are the changed points.)  
![](./images/persistent-seg.png)

Only $O(\log{n})$ nodes are changed, forming a chain, i.e. the number of nodes changed each time = the height of the tree.  
Note that the chairman tree cannot use heap-style storage, i.e. it cannot use $x\times 2$, $x\times 2+1$ to represent the left and right children; instead it should allocate nodes dynamically and save the left- and right-child numbers of each node.  
So we only need to, on the basis of recording the left and right children, save the root node when inserting each number, and then we can achieve persistence.

Let's simplify the problem: each time find the $k$-th smallest value within $[1,r]$.  
How to do it? Just find the root-node version when inserting r, and then do it with an ordinary weighted segment tree (some call it a key-value segment tree / value-range segment tree).

I believe everyone can understand this; back to the original problem—find the $k$-th smallest value in the interval $[l,r]$.  
Here we connect it to another piece of knowledge: **prefix sums**.  
This little thing cleverly uses the property of interval subtraction, answering each query in $O(1)$ through preprocessing.

We can find that the information counted by the chairman tree also satisfies this property.  
So…… if we need to get the statistical information of $[l,r]$, we only need to subtract the information of $[1,l - 1]$ from the information of $[1,r]$.

At this point, the problem is solved!

Regarding the space problem, let's analyze: since we allocate nodes dynamically, a single segment tree has only $2n-1$ nodes.  
Then there are $n$ modifications, each adding at most $\lceil\log_2{n}\rceil+1$ nodes. Therefore, in the worst case, the total number of nodes after $n$ modifications reaches $2n-1+n(\lceil\log_2{n}\rceil+1)$.
This problem has $n \leq 10^5$, and a single modification adds at most $\lceil\log_2{10^5}\rceil+1 = 18$ nodes, so the total number of nodes after $n$ modifications is $2\times 10^5-1+18\times 10^5$; ignoring the $-1$, it is roughly $20\times 10^5$.

Finally, a piece of advice: never be stingy with space (in most problems the space limit is relatively loose, so generally there is no need to worry about exceeding the space limit)! Be bold and directly use $2^5\times 10^5$, close to twice the original space (i.e. `n << 5`).

## Implementation

```cpp
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
constexpr int MAXN = 1e5;  // data range
int tot, n, m;
int sum[(MAXN << 5) + 10], rt[MAXN + 10], ls[(MAXN << 5) + 10],
    rs[(MAXN << 5) + 10];
int a[MAXN + 10], ind[MAXN + 10], len;

int getid(const int &val) {  // discretization
  return lower_bound(ind + 1, ind + len + 1, val) - ind;
}

int build(int l, int r) {  // build the tree
  int root = ++tot;
  if (l == r) return root;
  int mid = l + r >> 1;
  ls[root] = build(l, mid);
  rs[root] = build(mid + 1, r);
  return root;  // return the root of this subtree
}

int update(int k, int l, int r, int root) {  // insertion operation
  int dir = ++tot;
  ls[dir] = ls[root], rs[dir] = rs[root], sum[dir] = sum[root] + 1;
  if (l == r) return dir;
  int mid = l + r >> 1;
  if (k <= mid)
    ls[dir] = update(k, l, mid, ls[dir]);
  else
    rs[dir] = update(k, mid + 1, r, rs[dir]);
  return dir;
}

int query(int u, int v, int l, int r, int k) {  // query operation
  int mid = l + r >> 1,
      x = sum[ls[v]] - sum[ls[u]];  // obtain the count of values stored in the left child via interval subtraction
  if (l == r) return l;
  if (k <= x)  // if k is less than or equal to x, the k-th smallest number is stored in the left child
    return query(ls[u], ls[v], l, mid, k);
  else  // otherwise it is in the right child
    return query(rs[u], rs[v], mid + 1, r, k - x);
}

void init() {
  scanf("%d%d", &n, &m);
  for (int i = 1; i <= n; ++i) scanf("%d", a + i);
  memcpy(ind, a, sizeof ind);
  sort(ind + 1, ind + n + 1);
  len = unique(ind + 1, ind + n + 1) - ind - 1;
  rt[0] = build(1, len);
  for (int i = 1; i <= n; ++i) rt[i] = update(getid(a[i]), 1, len, rt[i - 1]);
}

int l, r, k;

void work() {
  while (m--) {
    scanf("%d%d%d", &l, &r, &k);
    printf("%d\n", ind[query(rt[l - 1], rt[r], 1, len, k)]);  // answer the query
  }
}

int main() {
  init();
  work();
  return 0;
}
```

## Extension: persistent DSU based on the chairman tree

The chairman tree is a convenient way to implement a persistent DSU; here we also provide an example implementation of a persistent DSU based on the chairman tree.

```cpp
--8<-- "docs/ds/code/persistent-seg/persistent-seg_1.cpp"
```

## References

<https://en.wikipedia.org/wiki/Persistent_data_structure>

<https://www.cnblogs.com/zinthos/p/3899565.html>
