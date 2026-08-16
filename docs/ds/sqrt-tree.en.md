## Introduction

Given a sequence ${\left\langle a_i\right\rangle}_{i=1}^n$ of length n, and an associative operation $\circ$ (for example $\gcd,\min,\max,+,\operatorname{and},\operatorname{or},\operatorname{xor}$ are all associative), then for each interval query $[l,r]$, we need to compute $a_l\circ a_{l+1}\circ\dotsb\circ a_{r}$.

The Sqrt Tree can preprocess in $O(n\log\log n)$ time and answer queries in $O(1)$ time.

## Explanation

### Blocking the sequence

First we divide the whole sequence into $O(\sqrt{n})$ blocks, each block of size $O(\sqrt{n})$. For each block, we compute:

1.  $P_i$ the prefix interval query within the block
2.  $S_i$ the suffix interval query within the block
3.  Maintain an additional array $\left\langle B_{i,j}\right\rangle$ representing the interval answer from the $i$-th block to the $j$-th block.

For example, suppose $\circ$ represents the addition operation $+$, and the sequence is $\{1,2,3,4,5,6,7,8,9\}$.

First we divide the sequence into three blocks, becoming $\{1,2,3\},\{4,5,6\},\{7,8,9\}$.

Then the prefix interval answer and suffix interval answer of each block are respectively

$$
\begin{aligned}
&P_1=\{1,3,6\},S_1=\{6,5,3\}\\
&P_2=\{4,9,15\},S_2=\{15,11,6\}\\
&P_3=\{7,15,24\},S_3=\{24,17,9\}\\
\end{aligned}
$$

The $B$ array is:

$$
B=\begin{bmatrix}
6 & 21 & 45\\
0 & 15 & 39\\
0 & 0 & 24\\
\end{bmatrix}
$$

(For the invalid case where $i>j$ we assume the answer is 0)

Obviously we can preprocess these values in $O(n)$ time, and the space complexity is also $O(n)$. After processing, we can use them to answer some cross-block queries in $O(1)$ time. But for those queries whose whole interval is within one block, we still cannot handle them, so we still need to process some things.

### Building a tree

It is easy to think of recursively constructing the above structure within each block to support queries within the block. For a block of size $1$ we can answer queries in $O(1)$. In this way we build a tree, each node of which represents an interval of the sequence. The interval length of a leaf node is $1$ or $2$. A node of size $k$ has $O(\sqrt{k})$ child nodes, so the height of the whole tree is $O(\log\log n)$, and the total interval length of each layer is $O(n)$, so the complexity of building this tree is $O(n\log\log n)$.

??? note "Proof of the tree height"
    By definition, let the height of the subtree of a node "controlling" $n$ elements be $T(n)$; we can write the recurrence:
    
    $$
    T(n)=T(\sqrt n)+1
    $$
    
    Making the substitution $n=2^m$ gives
    
    $$
    T(2^m)=T(2^{\frac m2})+1
    $$
    
    Further defining $S(m)=T(2^m)$, substituting gives
    
    $$
    S(m)=S(\dfrac m2)+1
    $$
    
    By the master theorem, we know $S(m)=O(\log m)$, so $T(n)=S(\log n)=O(\log\log n)$.

Now we can answer queries in $O(\log\log n)$ time. For a query $[l,r]$, we only need to quickly find a node $u$ with the smallest interval length such that $u$ can contain $[l,r]$; in this way $[l,r]$ must be cross-block in $u$'s blocked interval, and we can compute the answer in $O(1)$. The overall complexity of a single query is $O(\log\log n)$, because the tree height is $O(\log\log n)$. However, we can still optimize this process.

### Optimizing the query complexity

It is easy to think of binary-searching the height, and then we can judge validity in $O(1)$. In this way the complexity becomes $O(\log\log\log n)$. However, we can still further accelerate this process.

We assume

1.  The size of each block is an integer power of $2$;
2.  The block sizes on each layer are the same.

For this we need to pad some $0$ elements at the end of the sequence to make its length an integer power of $2$. Although some blocks may become twice the original size, this is still $O(\sqrt{k})$, so the complexity of preprocessing the blocking is still $O(n)$.

Now we can easily determine whether a query interval is entirely contained in one block. For an interval $[l,r]$ (with 0 as the start), we write the endpoints in binary form. Take an example: for $k=4, l=39, r=46$, the binary representation is

$$
l = 39_{10} = 100111_2,
r = 46_{10} = 101110_2
$$

We know that the interval length of each layer is the same, and the block size is also the same (in the above example $2^k=2^4=16$). These blocks completely cover the whole sequence, so the elements represented by the first block are $[0,15]$ (binary representation $[000000_2,001111_2]$), the interval of elements represented by the second block is $[16,31]$ (binary representation $[010000_2,011111_2]$), and so on. We find that the positions of these elements within the same block differ only in the last $k$ bits in binary (in the above example $k=4$). And the $l,r$ of the example also differ only in the last $k$ bits, so they are in the same block.

Therefore we need to check whether the two endpoints of the interval differ only in the last $k$ bits, i.e. $l\oplus r\le 2^k-1$. Therefore we can quickly find the layer where the answer interval lies:

1.  For each $i\in [1,n]$, we find the highest bit that is $1$ in $i$;
2.  Now for a query $[l,r]$, we compute the highest bit of $l\oplus r$, so that we can quickly determine the layer where the answer interval lies.

In this way we can answer queries in $O(1)$ time.

## Process of updating an element

We can update elements on the Sqrt Tree; both single-point modification and interval modification are supported.

### Single-point modification

Consider a single-point assignment operation $a_x=val$; we hope to efficiently update the information of this operation.

#### Naive implementation

First let's look at what the Sqrt Tree becomes after doing a single-point modification.

Consider a node of length $l$ and the corresponding sequences: $\left\langle P_i\right\rangle,\left\langle S_i\right\rangle,\left\langle B_{i,j}\right\rangle$. It is easy to find that only $O(\sqrt{l})$ elements change in both $\left\langle P_i\right\rangle$ and $\left\langle S_i \right\rangle$. While in $\left\langle B_{i,j}\right\rangle$ there are $O(l)$ elements changed. So $O(l)$ elements are updated in the tree. Therefore the complexity of a single-point modification on the Sqrt Tree is $O(n+\sqrt{n}+\sqrt{\sqrt{n}}+\dotsb)=O(n)$.

#### Using a Sqrt Tree to replace the B array

Note that the bottleneck of the single-point update is updating the $\left\langle B_{i,j}\right\rangle$ of the root node. So we try to replace the root node's $\left\langle B_{i,j}\right\rangle$ with another Sqrt Tree, calling it $index$. Its role is the same as the original two-dimensional array, maintaining the answer of the whole interval query. Other non-root nodes still use $\left\langle B_{i,j}\right\rangle$ for maintenance. Note that if a Sqrt Tree root node has an $index$ structure, its Sqrt Tree is said to be **with index**; if a Sqrt Tree root node has a $\left\langle B_{i,j}\right\rangle$ structure, it is said to be **without index**. And the $index$ tree itself is without index.

So we can update the $index$ tree like this:

1.  Update $\left\langle P_i\right\rangle$ and $\left\langle S_i\right\rangle$ in $O(\sqrt{n})$ time.
2.  Update $index$; its length is $O(n)$, but we only need to update one of its elements (this element represents the changed block); the time complexity of this step is $O(\sqrt{n})$ (using the naive-implementation algorithm).
3.  Enter the changed child node and use the naive-implementation algorithm to update the information in $O(\sqrt{n})$ time.

Note that the query complexity is still $O(1)$, because we use the $index$ tree at most once. So the complexity of single-point modification is $O(\sqrt{n})$.

### Updating an interval

The Sqrt Tree also supports the interval-cover operation $\operatorname{Update}(l,r,x)$, i.e. turning all numbers in the interval $[l,r]$ into $x$. For this we have two implementation methods, one of which spends $O(\sqrt{n}\log\log n)$ complexity to update the information and $O(1)$ time to query; the other is $O(\sqrt{n})$ to update the information, but the query time increases to $O(\log\log n)$.

We can apply lazy tags on the Sqrt Tree like a segment tree. But there is a difference on the Sqrt Tree. Because pushing down a node's lazy tag may reach a complexity of $O(\sqrt{n})$, we do not push down the tag when querying, but check whether the parent node has a tag, and if it does, push it down.

#### The first implementation

In the first implementation, we only apply lazy tags to layer-$1$ nodes (node interval length $O(\sqrt{n})$), and when pushing down the tag we directly update the whole subtree, with complexity $O(\sqrt{n}\log\log n)$. The operation process is as follows:

1.  Consider the layer-$1$ nodes; for those nodes completely contained by the modified interval, apply a lazy tag to them;

2.  There are two blocks with only part of their interval covered; we directly **rebuild** these two blocks in $O(\sqrt{n}\log\log n)$ time. If it itself carries a lazy tag from a previous modification, push down the tag while rebuilding;

3.  Update the root node's $\left\langle P_i\right\rangle$ and $\left\langle S_i\right\rangle$, with time complexity $O(\sqrt{n})$;

4.  Rebuild the $index$ tree, with time complexity $O(\sqrt{n}\log\log n)$.

Now we can efficiently complete interval modification. So how to use the lazy tag to answer queries? The operations are as follows:

1.  If our query is contained in a block with a lazy tag, we can use the lazy tag to compute the answer;

2.  If our query contains multiple blocks, then we only need to care about the answers of the leftmost and rightmost incomplete blocks. The answers of the middle blocks can be queried in the $index$ tree (because the $index$ tree is rebuilt after each modification), with complexity $O(1)$.

Therefore the query complexity is still $O(1)$.

#### The second implementation

In this implementation, every node can be applied a lazy tag. So when handling a query, we need to consider the lazy tags in the ancestors, so the query complexity becomes $O(\log\log n)$. However, the complexity of updating the information becomes faster. The operations are as follows:

1.  For blocks completely contained by the modified interval, we add the lazy tag to these blocks, with complexity $O(\sqrt{n})$;
2.  For blocks partially covered by the modified interval, update $\left\langle P_i\right\rangle$ and $\left\langle S_i\right\rangle$, with complexity $O(\sqrt{n})$ (because there are only two modified blocks);
3.  Update the $index$ tree, with complexity $O(\sqrt{n})$ (using the same update algorithm);
4.  For subtrees without index, update their $\left\langle B_{i,j}\right\rangle$;
5.  Recursively update the two intervals that are not completely covered.

The time complexity is $O(\sqrt{n}+\sqrt{\sqrt{n}}+\dotsb)=O(\sqrt{n})$.

## Implementation

The following implementation builds the tree in $O(n\log\log n)$ time, answers queries in $O(1)$ time, and does single-point modification in $O(\sqrt{n})$ time.

```cpp
SqrtTreeItem op(const SqrtTreeItem &a, const SqrtTreeItem &b);

int log2Up(int n) {
  int res = 0;
  while ((1 << res) < n) {
    res++;
  }
  return res;
}

class SqrtTree {
 private:
  int n, lg, indexSz;
  vector<SqrtTreeItem> v;
  vector<int> clz, layers, onLayer;
  vector<vector<SqrtTreeItem>> pref, suf, between;

  void buildBlock(int layer, int l, int r) {
    pref[layer][l] = v[l];
    for (int i = l + 1; i < r; i++) {
      pref[layer][i] = op(pref[layer][i - 1], v[i]);
    }
    suf[layer][r - 1] = v[r - 1];
    for (int i = r - 2; i >= l; i--) {
      suf[layer][i] = op(v[i], suf[layer][i + 1]);
    }
  }

  void buildBetween(int layer, int lBound, int rBound, int betweenOffs) {
    int bSzLog = (layers[layer] + 1) >> 1;
    int bCntLog = layers[layer] >> 1;
    int bSz = 1 << bSzLog;
    int bCnt = (rBound - lBound + bSz - 1) >> bSzLog;
    for (int i = 0; i < bCnt; i++) {
      SqrtTreeItem ans;
      for (int j = i; j < bCnt; j++) {
        SqrtTreeItem add = suf[layer][lBound + (j << bSzLog)];
        ans = (i == j) ? add : op(ans, add);
        between[layer - 1][betweenOffs + lBound + (i << bCntLog) + j] = ans;
      }
    }
  }

  void buildBetweenZero() {
    int bSzLog = (lg + 1) >> 1;
    for (int i = 0; i < indexSz; i++) {
      v[n + i] = suf[0][i << bSzLog];
    }
    build(1, n, n + indexSz, (1 << lg) - n);
  }

  void updateBetweenZero(int bid) {
    int bSzLog = (lg + 1) >> 1;
    v[n + bid] = suf[0][bid << bSzLog];
    update(1, n, n + indexSz, (1 << lg) - n, n + bid);
  }

  void build(int layer, int lBound, int rBound, int betweenOffs) {
    if (layer >= (int)layers.size()) {
      return;
    }
    int bSz = 1 << ((layers[layer] + 1) >> 1);
    for (int l = lBound; l < rBound; l += bSz) {
      int r = min(l + bSz, rBound);
      buildBlock(layer, l, r);
      build(layer + 1, l, r, betweenOffs);
    }
    if (layer == 0) {
      buildBetweenZero();
    } else {
      buildBetween(layer, lBound, rBound, betweenOffs);
    }
  }

  void update(int layer, int lBound, int rBound, int betweenOffs, int x) {
    if (layer >= (int)layers.size()) {
      return;
    }
    int bSzLog = (layers[layer] + 1) >> 1;
    int bSz = 1 << bSzLog;
    int blockIdx = (x - lBound) >> bSzLog;
    int l = lBound + (blockIdx << bSzLog);
    int r = min(l + bSz, rBound);
    buildBlock(layer, l, r);
    if (layer == 0) {
      updateBetweenZero(blockIdx);
    } else {
      buildBetween(layer, lBound, rBound, betweenOffs);
    }
    update(layer + 1, l, r, betweenOffs, x);
  }

  SqrtTreeItem query(int l, int r, int betweenOffs, int base) {
    if (l == r) {
      return v[l];
    }
    if (l + 1 == r) {
      return op(v[l], v[r]);
    }
    int layer = onLayer[clz[(l - base) ^ (r - base)]];
    int bSzLog = (layers[layer] + 1) >> 1;
    int bCntLog = layers[layer] >> 1;
    int lBound = (((l - base) >> layers[layer]) << layers[layer]) + base;
    int lBlock = ((l - lBound) >> bSzLog) + 1;
    int rBlock = ((r - lBound) >> bSzLog) - 1;
    SqrtTreeItem ans = suf[layer][l];
    if (lBlock <= rBlock) {
      SqrtTreeItem add =
          (layer == 0) ? (query(n + lBlock, n + rBlock, (1 << lg) - n, n))
                       : (between[layer - 1][betweenOffs + lBound +
                                             (lBlock << bCntLog) + rBlock]);
      ans = op(ans, add);
    }
    ans = op(ans, pref[layer][r]);
    return ans;
  }

 public:
  SqrtTreeItem query(int l, int r) { return query(l, r, 0, 0); }

  void update(int x, const SqrtTreeItem &item) {
    v[x] = item;
    update(0, 0, n, 0, x);
  }

  SqrtTree(const vector<SqrtTreeItem> &a)
      : n((int)a.size()), lg(log2Up(n)), v(a), clz(1 << lg), onLayer(lg + 1) {
    clz[0] = 0;
    for (int i = 1; i < (int)clz.size(); i++) {
      clz[i] = clz[i >> 1] + 1;
    }
    int tlg = lg;
    while (tlg > 1) {
      onLayer[tlg] = (int)layers.size();
      layers.push_back(tlg);
      tlg = (tlg + 1) >> 1;
    }
    for (int i = lg - 1; i >= 0; i--) {
      onLayer[i] = max(onLayer[i], onLayer[i + 1]);
    }
    int betweenLayers = max(0, (int)layers.size() - 1);
    int bSzLog = (lg + 1) >> 1;
    int bSz = 1 << bSzLog;
    indexSz = (n + bSz - 1) >> bSzLog;
    v.resize(n + indexSz);
    pref.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
    suf.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
    between.assign(betweenLayers, vector<SqrtTreeItem>((1 << lg) + bSz));
    build(0, 0, n, 0);
  }
};
```

## Exercises

[CodeChef - SEGPROD](https://www.codechef.com/NOV17/problems/SEGPROD)

**This page is mainly translated from [Sqrt Tree - Algorithms for Competitive Programming](https://cp-algorithms.com/data_structures/sqrt-tree.html); the copyright license is CC-BY-SA 4.0.**
