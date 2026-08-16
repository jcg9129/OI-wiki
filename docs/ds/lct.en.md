## Introduction

The Link/Cut Tree is a data structure that we use to solve the **dynamic tree problem**.

The Link/Cut Tree, also written as Link-Cut Tree, abbreviated LCT, is not called a dynamic tree; a dynamic tree refers to a class of problems.

The Splay Tree is the foundation of the LCT, but the Splay Tree used by the LCT is a bit different in details from an ordinary Splay (it has been extended somewhat).

## Problem introduction

Maintain a tree, supporting the following operations:

-   Modify the path weight between two points.
-   Query the sum of path weights between two points.
-   Modify the subtree weight of a point.
-   Query the sum of subtree weights of a point.

This is a template problem of heavy-path decomposition.

But add one more operation:

-   Disconnect and connect some edges, guaranteeing it is still a tree.

Required to answer the above online.

This becomes the dynamic tree problem, which can be solved using the LCT.

## The dynamic tree problem

Maintain a **forest**, supporting deleting a certain edge, adding a certain edge, and guaranteeing that it is still a forest after adding and deleting edges. We want to maintain some information of this forest.

The general operations are the connectivity of two points, the sum of path weights between two points, connecting two points and cutting a certain edge, modifying information, etc.

### Reviewing heavy-path decomposition from the perspective of the LCT

-   Decompose the whole tree by subtree size, and relabel it.
-   We find that after relabeling, some continuous intervals in units of chains are formed on the tree, and a segment tree can be used for interval operations.

### Turning to the dynamic tree problem

We find that the heavy-path decomposition we just discussed uses subtree size as the partitioning condition. Can we redefine a kind of decomposition to make it more suited to our dynamic tree problem?

Consider what kind of chains the dynamic tree problem needs.

Since we dynamically maintain a forest, obviously we want this chain to be a chain we specify, so as to utilize it for solving.

## Real-chain decomposition

For the edges from a point to all its children, we ourselves choose one edge to decompose; we call the chosen edge a real edge and the other edges virtual edges. For a real edge, we call the child it connects a real child. For a chain composed of real edges, we likewise call it a real chain. Please remember the most important reason we choose real-chain decomposition: it is chosen by us, flexible and mutable. It is precisely because of this flexibility and mutability that we use the Splay Tree to maintain these real chains.

## LCT

We can simply understand the LCT as using some Splays to maintain a dynamic heavy-path decomposition, in the hope of realizing interval operations on a dynamic tree. For each real chain, we build a Splay to maintain the information of the whole chain interval.

## Auxiliary tree

Let's first look at some properties of the auxiliary tree, and then understand the specific structure of the auxiliary tree through a figure.

In this article, you can consider that some Splays constitute an auxiliary tree, each auxiliary tree maintains one tree, and some auxiliary trees constitute the LCT, which maintains the whole forest.

1.  The auxiliary tree is composed of multiple Splays; each Splay maintains a path in the original tree, and the sequence of points obtained by an in-order traversal of this Splay, from front to back, corresponds to a path in the original tree "from top to bottom".
2.  Each node of the original tree corresponds one-to-one with a Splay node of the auxiliary tree.
3.  The various Splays of the auxiliary tree are not independent. The parent node of the root node of each Splay should originally be empty, but in the LCT the parent node of the root node of each Splay points to the parent node of **this chain** in the original tree (i.e. the parent node of the topmost point of the chain). This kind of parent link differs from the parent link of an ordinary Splay in that the child recognizes the parent, but the parent does not recognize the child, corresponding to a **virtual edge** of the original tree. Therefore, each connected component has exactly one point whose parent node is empty.
4.  Because of the above properties of the auxiliary tree, we do not need to maintain the original tree for any operation; the auxiliary tree can, in any situation, produce a unique original tree, so we only need to maintain the auxiliary tree.

Now we have an original tree, as shown. (The bold edges are real edges, the dashed edges are virtual edges.)

![tree](images/lct-atree-1.svg)

By the definition just given, the structure of the auxiliary tree is as shown.

![auxtree](images/lct-atree-2.svg)

### Consider the structural relationship between the original tree and the auxiliary tree

-   Real chains in the original tree: in the auxiliary tree, the nodes are all in one Splay.
-   Virtual chains in the original tree: in the auxiliary tree, the Father of the Splay where the child node lies points to the parent node, but neither of the two children of the parent node points to the child node.
-   Note: the root of the original tree does not equal the root of the auxiliary tree.
-   The Father pointer of the original tree does not equal the Father pointer of the auxiliary tree.
-   The auxiliary tree can be re-rooted arbitrarily while satisfying the properties of the auxiliary tree and the Splay.
-   The virtual-real chain transformation can be easily completed on the auxiliary tree, which realizes dynamically maintaining heavy-path decomposition.

### Variable declarations to be used below

-   `ch[N][2]` left and right children
-   `f[N]` parent pointer
-   `sum[N]` sum of path weights
-   `val[N]` point weight
-   `tag[N]` reversal tag
-   `laz[N]` weight tag
-   `siz[N]` subtree size on the auxiliary tree
-   Other\_Vars

### Function declarations

#### General data-structure functions (literal meaning)

1.  `PushUp(x)`
2.  `PushDown(x)`

#### Functions of the Splay tree

Below are the functions used in the Splay tree; for details you can refer to [Splay tree](./splay.md).

1.  `Get(x)` gets which child of the parent $x$ is.
2.  `Splay(x)` works in conjunction with the Rotate operation to rotate $x$ to **the root of the current Splay**.
3.  `Rotate(x)` the operation of rotating $x$ up by one level.

#### New operations

1.  `Access(x)` puts all points from the root to $x$ in one real chain, making the root-to-$x$ path a real path and in the same Splay. **Only this operation must be implemented; the other operations are implemented depending on the problem.**
2.  `IsRoot(x)` determines whether $x$ is the root of the tree it lies in.
3.  `Update(x)` after the `Access` operation, recursively `PushDown` from top to bottom to update information.
4.  `MakeRoot(x)` makes point $x$ the root of the tree it lies in.
5.  `Link(x, y)` connects an edge between the two points $x, y$.
6.  `Cut(x, y)` deletes the edge between the two points $x, y$.
7.  `Find(x)` finds the number of the root node of the tree $x$ lies in.
8.  `Fix(x, v)` modifies the point weight of $x$ to $v$.
9.  `Split(x, y)` extracts the path between $x, y$, convenient for interval operations.

### Macro definitions

-   `#define ls ch[p][0]`
-   `#define rs ch[p][1]`

## Function explanations

### `PushUp()`

```cpp
void PushUp(int p) {
  // maintain other variables
  siz[p] = siz[ls] + siz[rs] + 1;
}
```

### `PushDown()`

```cpp
void PushDown(int p) {
  if (tag[p] != std_tag) {
    // pushdown the tag
    tag[p] = std_tag;
  }
}
```

### `Splay() && Rotate()`

Here `Splay()` and `Rotate()` are somewhat different from the implementation of the Splay tree.

```cpp
#define Get(x) (ch[f[x]][1] == x)

void Rotate(int x) {
  int y = f[x], z = f[y], k = Get(x);
  if (!isRoot(y)) ch[z][ch[z][1] == y] = x;
  // the line above must be written first; an ordinary Splay does not need it, because of isRoot (explained later)
  ch[y][k] = ch[x][!k], f[ch[x][!k]] = y;
  ch[x][!k] = y, f[y] = x, f[x] = z;
  PushUp(y), PushUp(x);
}

void Splay(int x) {
  Update(
      x);  // you'll see it soon. Before Splay, PushDown all the points on the path the rotation will pass through
  for (int fa; fa = f[x], !isRoot(x); Rotate(x)) {
    if (!isRoot(fa)) Rotate(Get(fa) == Get(x) ? fa : x);
  }
}
```

The above functions can be looked up in [Splay tree](./splay.md).

Below are functions unique to the LCT.

### `isRoot()`

```cpp
// as we said earlier, the LCT has the property that if a child is not a real child, its parent cannot find it
// so when a point is neither its parent's left child nor its parent's right child, it is the root of the current Splay
#define isRoot(x) (ch[f[x]][0] != x && ch[f[x]][1] != x)
```

### `Access()`

```cpp
// Access is the core operation of the LCT;
// imagine we want to solve a path, and this path happens to be one of our current Splays,
// then we just directly invoke its information. Let's first look at the code, then look at the process combined with figures
int Access(int x) {
  int p;
  for (p = 0; x; p = x, x = f[x]) {
    Splay(x), ch[x][1] = p, PushUp(x);
  }
  return p;
}
```

-   We have such a tree; solid lines are real edges, dashed lines are virtual edges.

    ![initial tree](images/lct-access-1.svg)

-   Its auxiliary tree may look like this (different construction methods may give the LCT a different structure).

    ![initial auxtree](images/lct-access-2.svg)

-   Now we want to `Access(N)`, turning all the edges on the path from $A$ to $N$ into real edges, pulling them into one Splay.

    ![access tree](images/lct-access-3.svg)

-   The implementation method is to gradually update the Splay from bottom to top.

-   First we want to rotate $N$ to the root of the current Splay.

-   To guarantee the properties of the AuxTree (auxiliary tree), the original real edge from $N$ to $O$ must be changed to a virtual edge.

-   Because of the property that the child recognizes the parent but not vice versa, we can unilaterally change $N$'s child to `NULL`.

-   So the original AuxTree changes from the figure below to the one after it.

    ![step 1 auxtree](images/lct-access-4.svg)

-   In the next step, we also rotate the Father $I$ pointed to by $N$ to the root of $I$'s Splay tree.

-   The original real edge $I$—$K$ must be removed; at this time we point $I$'s right child to $N$, obtaining a Splay like $I$—$L$.

    ![step 2 auxtree](images/lct-access-5.svg)

-   Next, following the operation steps just now, since $I$'s Father points to $H$, we rotate $H$ to the root of the Splay Tree it lies in, then set $H$'s rs to $I$.

-   The tree afterwards is like this.

    ![step 3 auxtree](images/lct-access-6.svg)

-   Similarly we `Splay(A)`, and point $A$'s right child to $H$.

-   So we obtain such an AuxTree. And we find that the entire path $A$—$N$ is already in the same Splay.

    ![step final auxtree](images/lct-access-7.svg)

```cpp
// let's review the code
int Access(int x) {
  int p;
  for (p = 0; x; p = x, x = f[x]) {
    Splay(x), ch[x][1] = p, PushUp(x);
  }
  return p;
}
```

We find that `Access()` is actually very easy, with only the following four steps:

1.  Rotate the current node to the root.
2.  Change the child to the previous node.
3.  Update the information of the current point.
4.  Change the current point to the parent of the current point, and continue the operation.

The Access provided here also has a return value. This return value is equivalent to the number of the virtual-edge parent node at the last virtual-real chain transformation. This value has two meanings:

-   When two consecutive Access operations are performed, the return value of the second Access operation equals the LCA of these two nodes.
-   It represents the root of the Splay tree where the chain from $x$ to the root lies. This node must already have been rotated to the root node, and its parent must be empty.

### `Update()`

```cpp
// just pushDown layer by layer from top to bottom
void Update(int p) {
  if (!isRoot(p)) Update(f[p]);
  pushDown(p);
}
```

### `makeRoot()`

-   The importance of `Make_Root()` is by no means less than that of `Access()`. When we need to maintain path information, a situation will inevitably arise where the path depth cannot strictly increase; according to the properties of the AuxTree, such a path cannot appear in one Splay.
-   At this time we need to use `Make_Root()`.
-   The purpose of `Make_Root()` is to make the specified point become the root of the original tree; consider how to implement this operation.
-   Let the return value of `Access(x)` be $y$; then at this time the path from $x$ to the current root exactly constitutes a Splay, and the root of this Splay is $y$.
-   Consider representing the tree as a directed graph, assigning each edge a direction, representing the direction from child to parent. It is easy to find that re-rooting is equivalent to reversing all the edges of the path from $x$ to the root (please think carefully).
-   Therefore just reverse the path from $x$ to the current root.
-   Since $y$ is the root of the Splay represented by the path from $x$ to the current root, just perform an interval reversal on the Splay tree rooted at $y$.

```cpp
void makeRoot(int p) {
  p = Access(p);
  swap(ch[p][0], ch[p][1]);
  tag[p] ^= 1;
}
```

### `Link()`

-   Linking two points is actually very simple: first `Make_Root(x)`, then point $x$'s parent to $y$. Obviously, this operation certainly cannot occur within the same tree, so remember to check first.

```cpp
void Link(int x, int p) {
  makeRoot(x);
  splay(x);
  f[x] = p;
}
```

### `Split()`

-   The meaning of the `Split` operation is very simple: take out a Splay that maintains the path from $x$ to $y$.
-   First `MakeRoot(x)`, then `Access(y)`. If you want $y$ to be the root, then `Splay(y)`.
-   In addition, these three operations of Split can directly take out the needed path onto the subtree of $y$, allowing other operations.

### `Cut()`

-   `Cut` has two cases: guaranteed legal and not necessarily guaranteed legal.
-   If guaranteed legal, directly `Split(x, y)`; at this time $y$ is the root, $x$ must be its child, and just disconnect bidirectionally. Like this:

```cpp
void Cut(int x, int p) { makeRoot(x), Access(p), Splay(p), ls = f[x] = 0; }
```

If it is not guaranteed legal, we need to check whether it exists; here we choose to use a `map` to store it, but there is a method that utilizes a property:

To delete an edge, the following three conditions must be satisfied:

1.  $x,y$ are connected.
2.  There are no other chains on the path of $x,y$.
3.  $x$ has no right child.

To summarize, the meaning of the above three sentences is just one: there is an edge between $x,y$.

The specific implementation is left as a thinking exercise for everyone. Determining connectivity requires the later `Find`; for the other two points, with a little thought and analysis of the structure you will know how to judge.

### `Find()`

-   `Find()` looks for the root of the **original tree** where $x$ lies; please do not confuse the original-tree root and the auxiliary-tree root. After `Access(p)`, then `Splay(p)`. This way the root is the one with the smallest depth in the tree; just keep going to the left child, `PushDown` along the way.
-   Keep going until there is no ls; very simple.
-   Note that after each query, you need to `Splay` the node corresponding to the queried answer up, to guarantee the complexity.

```cpp
int Find(int p) {
  Access(p);
  Splay(p);
  pushDown(p);
  while (ls) p = ls, pushDown(p);
  Splay(p);
  return p;
}
```

### Notes

-   Before an operation, always think about whether `PushUp` or `PushDown` is needed; because the LCT is especially flexible, missing one `Pushdown` or `Pushup` may modify a point that should not be modified!
-   The `Rotate` of the LCT is a bit different from that of the Splay; `if (z)` must be placed first.
-   The `Splay` operation of the LCT is simply rotating to the root; there is no operation of rotating to someone's child, because it is not needed.

## Time complexity

Most operations in the LCT are based on `Access`, and the time complexity of the other operations is all constant, so we only need to analyze the time complexity of the `Access` operation.

Among them, the time complexity of `Access` mainly comes from multiple splay operations and access to the virtual edges in the path; next we analyze the time complexity of these two parts separately.

1.  splay

    -   Define $w(x) = \log size(x)$, where $size(x)$ denotes the sum of the number of all virtual and real edges rooted at $x$.

    -   Define the potential function $\Phi = \sum_{x \in T} w(x)$, where $T$ denotes the set of all nodes.

    From the analysis of [the time complexity of Splay](./splay.md#time-complexity), it is easy to know that the amortized time complexity of the splay operation is $O(\log n)$.

2.  Accessing virtual edges

    Referring to [heavy-path decomposition](../graph/hld.md#heavy-path-decomposition), define two kinds of virtual edges:

    -   **Heavy virtual edge**: a virtual edge from node $v$ to its parent, where $size(v) > \frac{1}{2} size(parent(v))$.

    -   **Light virtual edge**: a virtual edge from node $v$ to its parent, where $size(v) \leq \frac{1}{2} size(parent(v))$.

    For the handling of virtual edges, potential analysis can be used; define the potential function $\Phi$ as the number of all heavy virtual edges, and define the amortized cost $c_i = t_i + \Delta \Phi_i$, where $t_i$ is the cost of the actual operation and $\Delta \Phi_i$ is the change in potential.

    -   After passing through a heavy virtual edge, the heavy virtual edge is converted into a real edge; this operation decreases the potential by $1$, because it optimizes the tree structure by strengthening important connections. And since its actual operation cost is $O(1)$, offsetting the increase in potential, it does not increase the amortized cost, and all amortized cost is concentrated on the handling of light virtual edges.

    -   Each `Access` operation traverses at most $O(\log n)$ light virtual edges, so it consumes at most $O(\log n)$ actual operation cost, converting to obtain $O(\log n)$ heavy virtual edges, i.e. the potential increases at a cost of $O(\log n)$.

    From this, the final amortized complexity of accessing virtual edges is the sum of the actual operation cost and the change in potential, i.e. $O(\log n)$.

In summary, the time complexity of the `Access` operation in the LCT is the sum of the complexities of splay and virtual-edge access, so the final amortized complexity is $O(\log n)$; that is, for an LCT of n nodes, the time complexity of doing m `Access` operations is $O(n \log n + m \log n)$, and thus the amortized complexity of operations such as `Cut`, `Link`, `Findroot` based on the `Access` operation is also $O(\log n)$.

## Exercises

-   [「BZOJ 3282」Tree](https://hydro.ac/p/bzoj-P3282)
-   [「HNOI2010」Bouncing Sheep](https://www.luogu.com.cn/problem/P3203)

## Maintaining tree-chain information

Through the `Split(x,y)` operation, the LCT can extract the path from point $x$ to point $y$ on the tree into the Splay rooted at $y$, turning the modification and statistics of tree-chain information into operations on the balanced tree, which gives the LCT an advantage in maintaining tree-chain information. In addition, binary search on a tree chain implemented with the LCT has one fewer factor of $O(\log n)$ in complexity than heavy-path decomposition.

???+ note "Example problem [「National Training Team」Tree II](https://www.luogu.com.cn/problem/P1501)"
    Given a tree with $n$ nodes, the initial weight of each point is $1$. There are $q$ operations, each of which is one of the following four:
    
    1.  `- u1 v1 u2 v2`: delete the edge between the two points $u_1,v_1$ on the tree, and connect the two points $u_2,v_2$; it is guaranteed that the operation is legal and that after adding the edge it is still a tree.
    2.  `+ u v c`: increase the point weights on the path between the two points $u,v$ on the tree all by $c$.
    3.  `* u v c`: multiply the point weights on the path between the two points $u,v$ on the tree all by $c$.
    4.  `/ u v`: output the sum of the point weights on the path between the two points $u,v$ on the tree, modulo $51061$.
    
        $1\le n,q\le 10^5,0\le c\le 10^4$
    
        The `-` operation can directly be `Cut(u1,v1),Link(u2,v2)`.

When modifying the path between the two points $u,v$ on the tree, first `Split(u,v)`.

This problem requires performing subtree-add, subtree-multiply, and subtree-sum operations on the auxiliary tree, so besides the subtree reversal tag that an ordinary LCT needs to maintain, we also need to maintain a subtree addition tag and a subtree multiplication tag. The method of handling tags is the same as on a Splay.

When applying and pushing down the addition tag, the change in the subtree weight sum is related to the number of nodes in the subtree, so we also need to maintain the subtree size `siz`.

When pushing down tags, note the order: push down the multiplication tag first, then push down the addition tag. The subtree reversal tag and the two subtree add/multiply tags do not conflict.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    using namespace std;
    constexpr long long MAXN = 100010;
    constexpr long long mod = 51061;
    long long n, q, u, v, c;
    char op;
    
    struct Splay {
      long long ch[MAXN][2], fa[MAXN], siz[MAXN], val[MAXN], sum[MAXN], rev[MAXN],
          add[MAXN], mul[MAXN];
    
      void clear(long long x) {
        ch[x][0] = ch[x][1] = fa[x] = siz[x] = val[x] = sum[x] = rev[x] = add[x] =
            0;
        mul[x] = 1;
      }
    
      long long getch(long long x) { return (ch[fa[x]][1] == x); }
    
      long long isroot(long long x) {
        clear(0);
        return ch[fa[x]][0] != x && ch[fa[x]][1] != x;
      }
    
      void maintain(long long x) {
        clear(0);
        siz[x] = (siz[ch[x][0]] + 1 + siz[ch[x][1]]) % mod;
        sum[x] = (sum[ch[x][0]] + val[x] + sum[ch[x][1]]) % mod;
      }
    
      void pushdown(long long x) {
        clear(0);
        if (mul[x] != 1) {
          if (ch[x][0])
            mul[ch[x][0]] = (mul[x] * mul[ch[x][0]]) % mod,
            val[ch[x][0]] = (val[ch[x][0]] * mul[x]) % mod,
            sum[ch[x][0]] = (sum[ch[x][0]] * mul[x]) % mod,
            add[ch[x][0]] = (add[ch[x][0]] * mul[x]) % mod;
          if (ch[x][1])
            mul[ch[x][1]] = (mul[x] * mul[ch[x][1]]) % mod,
            val[ch[x][1]] = (val[ch[x][1]] * mul[x]) % mod,
            sum[ch[x][1]] = (sum[ch[x][1]] * mul[x]) % mod,
            add[ch[x][1]] = (add[ch[x][1]] * mul[x]) % mod;
          mul[x] = 1;
        }
        if (add[x]) {
          if (ch[x][0])
            add[ch[x][0]] = (add[ch[x][0]] + add[x]) % mod,
            val[ch[x][0]] = (val[ch[x][0]] + add[x]) % mod,
            sum[ch[x][0]] = (sum[ch[x][0]] + add[x] * siz[ch[x][0]] % mod) % mod;
          if (ch[x][1])
            add[ch[x][1]] = (add[ch[x][1]] + add[x]) % mod,
            val[ch[x][1]] = (val[ch[x][1]] + add[x]) % mod,
            sum[ch[x][1]] = (sum[ch[x][1]] + add[x] * siz[ch[x][1]] % mod) % mod;
          add[x] = 0;
        }
        if (rev[x]) {
          if (ch[x][0]) rev[ch[x][0]] ^= 1, swap(ch[ch[x][0]][0], ch[ch[x][0]][1]);
          if (ch[x][1]) rev[ch[x][1]] ^= 1, swap(ch[ch[x][1]][0], ch[ch[x][1]][1]);
          rev[x] = 0;
        }
      }
    
      void update(long long x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void print(long long x) {
        if (!x) return;
        pushdown(x);
        print(ch[x][0]);
        printf("%lld ", x);
        print(ch[x][1]);
      }
    
      void rotate(long long x) {
        long long y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        maintain(z);
      }
    
      void splay(long long x) {
        update(x);
        for (long long f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(long long x) {
        for (long long f = 0; x; f = x, x = fa[x])
          splay(x), ch[x][1] = f, maintain(x);
      }
    
      void makeroot(long long x) {
        access(x);
        splay(x);
        swap(ch[x][0], ch[x][1]);
        rev[x] ^= 1;
      }
    
      long long find(long long x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    } st;
    
    main() {
      scanf("%lld%lld", &n, &q);
      for (long long i = 1; i <= n; i++) st.val[i] = 1, st.maintain(i);
      for (long long i = 1; i < n; i++) {
        scanf("%lld%lld", &u, &v);
        if (st.find(u) != st.find(v)) st.makeroot(u), st.fa[u] = v;
      }
      while (q--) {
        scanf(" %c%lld%lld", &op, &u, &v);
        if (op == '+') {
          scanf("%lld", &c);
          st.makeroot(u), st.access(v), st.splay(v);
          st.val[v] = (st.val[v] + c) % mod;
          st.sum[v] = (st.sum[v] + st.siz[v] * c % mod) % mod;
          st.add[v] = (st.add[v] + c) % mod;
        }
        if (op == '-') {
          st.makeroot(u);
          st.access(v);
          st.splay(v);
          if (st.ch[v][0] == u && !st.ch[u][1]) st.ch[v][0] = st.fa[u] = 0;
          scanf("%lld%lld", &u, &v);
          if (st.find(u) != st.find(v)) st.makeroot(u), st.fa[u] = v;
        }
        if (op == '*') {
          scanf("%lld", &c);
          st.makeroot(u), st.access(v), st.splay(v);
          st.val[v] = st.val[v] * c % mod;
          st.sum[v] = st.sum[v] * c % mod;
          st.mul[v] = st.mul[v] * c % mod;
        }
        if (op == '/')
          st.makeroot(u), st.access(v), st.splay(v), printf("%lld\n", st.sum[v]);
      }
      return 0;
    }
    ```

### Exercises

-   [luogu P3690 【Template】Link Cut Tree (Dynamic Tree)](https://www.luogu.com.cn/problem/P3690)
-   [「SDOI2011」Coloring](https://www.luogu.com.cn/problem/P2486)
-   [「SHOI2014」Trigeminal Nerve Tree](https://loj.ac/problem/2187)

## Maintaining connectivity properties

### Determining whether connected

With the help of the LCT's `Find()` function, one can determine whether two points on a dynamic forest are connected. If `Find(x)==Find(y)`, then it means the two points $x,y$ are on one tree and connected to each other.

???+ note "Example problem [「SDOI2008」Cave Exploration](https://www.luogu.com.cn/problem/P2147)"
    Initially there are $n$ independent points, and $m$ operations. Each operation is one of the following:
    
    1.  `Connect u v`: connect an edge between the two points $u,v$.
    2.  `Destroy u v`: delete the edge between the two points $u,v$; it is guaranteed that such an edge existed before.
    3.  `Query u v`: ask whether the two points $u,v$ are connected.
    
    It is guaranteed that at any moment the shape of the graph is a forest.
    
    $n\le 10^4, m\le 2\times 10^5$

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    using namespace std;
    constexpr int MAXN = 10010;
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], tag[MAXN];
    
      void clear(int x) { ch[x][0] = ch[x][1] = fa[x] = tag[x] = 0; }
    
      int getch(int x) { return ch[fa[x]][1] == x; }
    
      int isroot(int x) { return ch[fa[x]][0] != x && ch[fa[x]][1] != x; }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) swap(ch[ch[x][0]][0], ch[ch[x][0]][1]), tag[ch[x][0]] ^= 1;
          if (ch[x][1]) swap(ch[ch[x][1]][0], ch[ch[x][1]][1]), tag[ch[x][1]] ^= 1;
          tag[x] = 0;
        }
      }
    
      void update(int x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void rotate(int x) {
        int y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
      }
    
      void splay(int x) {
        update(x);
        for (int f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = fa[x]) splay(x), ch[x][1] = f;
      }
    
      void makeroot(int x) {
        access(x);
        splay(x);
        swap(ch[x][0], ch[x][1]);
        tag[x] ^= 1;
      }
    
      int find(int x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    } st;
    
    int n, q, x, y;
    char op[MAXN];
    
    int main() {
      scanf("%d%d", &n, &q);
      while (q--) {
        scanf("%s%d%d", op, &x, &y);
        if (op[0] == 'Q') {
          if (st.find(x) == st.find(y))
            printf("Yes\n");
          else
            printf("No\n");
        }
        if (op[0] == 'C')
          if (st.find(x) != st.find(y)) st.makeroot(x), st.fa[x] = y;
        if (op[0] == 'D') {
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          if (st.ch[y][0] == x && !st.ch[x][1]) st.ch[y][0] = st.fa[x] = 0;
        }
      }
      return 0;
    }
    ```

### Maintaining edge-biconnected components

If it is required to contract edge-biconnected components into points, each time an edge is added, if the two points on the tree it connects are connected to each other, then all points on this path will be contracted into one point.

???+ note "Example problem [「AHOI2005」Route Planning](https://www.luogu.com.cn/problem/P2542)"
    Given $n$ points, initially with $m$ undirected edges, and $q$ operations, each of which is one of the following:
    
    1.  `0 u v`: delete the edge between $u,v$; it is guaranteed that such an edge exists at this time.
    2.  `1 u v`: query the number of edges that all possible paths between the two points $u,v$ must pass through at this time.
    
    It is guaranteed that the graph is connected at any moment.
    
    $1<n<3\times 10^4,1<m<10^5,0\le q\le 4\times 10^4$

We can find that the number of edges that all possible paths between the two points $u,v$ must pass through is the number of nodes on the path between the point where $u$ lies and the point where $v$ lies after contracting all edge-biconnected components into points, minus $1$.

Since the edge-deletion operation in the problem is inconvenient to perform, we consider processing the operations offline in reverse, changing edge deletion into edge addition.

When adding an edge, if the two points were originally not connected, then connect the two points on the LCT; otherwise extract the path between these two points on the LCT before adding this edge, traverse this subtree on the auxiliary tree, which is equivalent to traversing this path, merge these points, and maintain the merged information with a DSU.

Use the representative element of the merged DSU to replace the original path on the tree. Note that in each subsequent operation, you must find the representative element of the operated point in the DSU to operate on.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <map>
    using namespace std;
    constexpr int MAXN = 200010;
    int f[MAXN];
    
    int findp(int x) { return f[x] ? f[x] = findp(f[x]) : x; }
    
    void merge(int x, int y) {
      x = findp(x);
      y = findp(y);
      if (x != y) f[x] = y;
    }
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], tag[MAXN], siz[MAXN];
    
      void clear(int x) { ch[x][0] = ch[x][1] = fa[x] = tag[x] = siz[x] = 0; }
    
      int getch(int x) { return ch[findp(fa[x])][1] == x; }
    
      int isroot(int x) {
        return ch[findp(fa[x])][0] != x && ch[findp(fa[x])][1] != x;
      }
    
      void maintain(int x) {
        clear(0);
        if (x) siz[x] = siz[ch[x][0]] + 1 + siz[ch[x][1]];
      }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) tag[ch[x][0]] ^= 1, swap(ch[ch[x][0]][0], ch[ch[x][0]][1]);
          if (ch[x][1]) tag[ch[x][1]] ^= 1, swap(ch[ch[x][1]][0], ch[ch[x][1]][1]);
          tag[x] = 0;
        }
      }
    
      void print(int x) {
        if (!x) return;
        pushdown(x);
        print(ch[x][0]);
        printf("%d ", x);
        print(ch[x][1]);
      }
    
      void update(int x) {
        if (!isroot(x)) update(findp(fa[x]));
        pushdown(x);
      }
    
      void rotate(int x) {
        x = findp(x);
        int y = findp(fa[x]), z = findp(fa[y]), chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        if (z) maintain(z);
      }
    
      void splay(int x) {
        x = findp(x);
        update(x);
        for (int f = findp(fa[x]); f = findp(fa[x]), !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = findp(fa[x]))
          splay(x), ch[x][1] = f, maintain(x);
      }
    
      void makeroot(int x) {
        x = findp(x);
        access(x);
        splay(x);
        tag[x] ^= 1;
        swap(ch[x][0], ch[x][1]);
      }
    
      int find(int x) {
        x = findp(x);
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    
      void dfs(int x) {
        pushdown(x);
        if (ch[x][0]) dfs(ch[x][0]), merge(ch[x][0], x);
        if (ch[x][1]) dfs(ch[x][1]), merge(ch[x][1], x);
      }
    } st;
    
    int n, m, q, x, y, cur, ans[MAXN];
    
    struct oper {
      int op, a, b;
    } s[MAXN];
    
    map<pair<int, int>, int> mp;
    
    int main() {
      scanf("%d%d", &n, &m);
      for (int i = 1; i <= n; i++) st.maintain(i);
      for (int i = 1; i <= m; i++)
        scanf("%d%d", &x, &y), mp[{x, y}] = mp[{y, x}] = 1;
      while (scanf("%d", &s[++q].op)) {
        if (s[q].op == -1) {
          q--;
          break;
        }
        scanf("%d%d", &s[q].a, &s[q].b);
        if (!s[q].op) mp[{s[q].a, s[q].b}] = mp[{s[q].b, s[q].a}] = 0;
      }
      reverse(s + 1, s + q + 1);
      for (map<pair<int, int>, int>::iterator it = mp.begin(); it != mp.end(); it++)
        if (it->second) {
          mp[{it->first.second, it->first.first}] = 0;
          x = findp(it->first.first);
          y = findp(it->first.second);
          if (st.find(x) != st.find(y))
            st.makeroot(x), st.fa[x] = y;
          else {
            if (x == y) continue;
            st.makeroot(x);
            st.access(y);
            st.splay(y);
            st.dfs(y);
            int t = findp(y);
            st.fa[t] = findp(st.fa[y]);
            st.ch[t][0] = st.ch[t][1] = 0;
            st.maintain(t);
          }
        }
      for (int i = 1; i <= q; i++) {
        if (s[i].op == 0) {
          x = findp(s[i].a);
          y = findp(s[i].b);
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          st.dfs(y);
          int t = findp(y);
          st.fa[t] = st.fa[y];
          st.ch[t][0] = st.ch[t][1] = 0;
          st.maintain(t);
        }
        if (s[i].op == 1) {
          x = findp(s[i].a);
          y = findp(s[i].b);
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          ans[++cur] = st.siz[y] - 1;
        }
      }
      for (int i = cur; i >= 1; i--) printf("%d\n", ans[i]);
      return 0;
    }
    ```

### Exercises

-   [Luogu P3950 Tribal Conflict](https://www.luogu.com.cn/problem/P3950)
-   [BZOJ 4998 Planet Alliance](https://hydro.ac/p/bzoj-P4998)
-   [BZOJ 2959 Long-Distance Running](https://hydro.ac/p/bzoj-P2959)

## Maintaining edge weights

The LCT cannot directly handle edge weights; in this case one needs to create a corresponding point for each edge, convenient for querying the edge information on a chain. Using this technique one can dynamically maintain a spanning tree.

???+ note "Example problem [luogu P4234 Minimum Difference Spanning Tree](https://www.luogu.com.cn/problem/P4234)"
    Given a weighted undirected graph with $n$ points and $m$ edges, find the spanning tree that minimizes the difference between the maximum edge weight and the minimum edge weight, and output this difference.
    
    The data guarantee that at least one spanning tree exists.
    
    $1\le n\le 5\times 10^4,1\le m\le 2\times 10^5,1\le w_i\le 10^4$

Sort the edges by edge weight from small to large, and enumerate the rightmost chosen edge; to obtain the optimal solution, we need to maximize the edge weight of the minimum-weight edge.

Each time, add edges in order; if the two points about to be connected are already connected, then delete the edge with the smallest edge weight between these two points. If the whole graph is already connected into a tree, then update the answer with the current edge weight minus the minimum edge weight. The minimum edge weight can be updated using the two-pointer method.

There is no fixed parent-child relationship on the LCT, so edge weights cannot be recorded in point weights.

To record the information of edges on a tree chain, one can use **edge splitting**. Create a corresponding point for each edge, and connect an edge from this edge to its two endpoints; the original edge-adding and edge-deleting operations both become two operations.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <set>
    using namespace std;
    constexpr int MAXN = 5000010;
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], tag[MAXN], val[MAXN], minn[MAXN];
    
      void clear(int x) {
        ch[x][0] = ch[x][1] = fa[x] = tag[x] = val[x] = minn[x] = 0;
      }
    
      int getch(int x) { return ch[fa[x]][1] == x; }
    
      int isroot(int x) { return ch[fa[x]][0] != x && ch[fa[x]][1] != x; }
    
      void maintain(int x) {
        if (!x) return;
        minn[x] = x;
        if (ch[x][0]) {
          if (val[minn[ch[x][0]]] < val[minn[x]]) minn[x] = minn[ch[x][0]];
        }
        if (ch[x][1]) {
          if (val[minn[ch[x][1]]] < val[minn[x]]) minn[x] = minn[ch[x][1]];
        }
      }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) tag[ch[x][0]] ^= 1, swap(ch[ch[x][0]][0], ch[ch[x][0]][1]);
          if (ch[x][1]) tag[ch[x][1]] ^= 1, swap(ch[ch[x][1]][0], ch[ch[x][1]][1]);
          tag[x] = 0;
        }
      }
    
      void update(int x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void print(int x) {
        if (!x) return;
        pushdown(x);
        print(ch[x][0]);
        printf("%d ", x);
        print(ch[x][1]);
      }
    
      void rotate(int x) {
        int y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        if (z) maintain(z);
      }
    
      void splay(int x) {
        update(x);
        for (int f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = fa[x]) splay(x), ch[x][1] = f, maintain(x);
      }
    
      void makeroot(int x) {
        access(x);
        splay(x);
        tag[x] ^= 1;
        swap(ch[x][0], ch[x][1]);
      }
    
      int find(int x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    
      void link(int x, int y) {
        makeroot(x);
        fa[x] = y;
      }
    
      void cut(int x, int y) {
        makeroot(x);
        access(y);
        splay(y);
        ch[y][0] = fa[x] = 0;
        maintain(y);
      }
    } st;
    
    constexpr int inf = 2e9 + 1;
    int n, m, ans, nww, x, y;
    
    struct Edge {
      int u, v, w;
    
      bool operator<(Edge x) const { return w < x.w; };
    } s[MAXN];
    
    multiset<int> mp;
    
    int main() {
      scanf("%d%d", &n, &m);
      for (int i = 1; i <= n; i++) st.val[i] = inf, st.maintain(i);
      for (int i = 1; i <= m; i++) scanf("%d%d%d", &s[i].u, &s[i].v, &s[i].w);
      sort(s + 1, s + m + 1);
      for (int i = 1; i <= m; i++) st.val[n + i] = s[i].w, st.maintain(n + i);
      for (int i = 1; i <= m; i++) {
        x = s[i].u;
        y = s[i].v;
        if (x == y) continue;
        if (st.find(x) != st.find(y)) {
          nww++;
          st.link(x, n + i);
          st.link(n + i, y);
          mp.insert(s[i].w);
          if (nww == n - 1) ans = s[i].w - (*(mp.begin()++));
        } else {
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          int t = st.minn[y] - n;
          st.cut(s[t].u, t + n);
          st.cut(t + n, s[t].v);
          mp.erase(mp.find(s[t].w));
          st.link(x, n + i);
          st.link(n + i, y);
          mp.insert(s[i].w);
          if (nww == n - 1) ans = min(ans, s[i].w - (*(mp.begin()++)));
        }
      }
      printf("%d\n", ans);
      return 0;
    }
    ```

### Exercises

-   [「WC2006」Water Pipe Director](https://www.luogu.com.cn/problem/P4172)
-   [「BJWC2010」Strict Second-Minimum Spanning Tree](https://www.luogu.com.cn/problem/P4180)
-   [「NOI2014」Magic Forest](https://uoj.ac/problem/3)

## Maintaining subtree information

The LCT is not good at maintaining subtree information. By counting the information of all virtual subtrees of a node, one can obtain the information of the whole tree.

???+ note "Example problem [「BJOI2014」Great Fusion](https://loj.ac/problem/2230)"
    Given $n$ nodes and $q$ operations, each operation is of the following form:
    
    1.  `A x y` connect an edge between nodes $x$ and $y$.
    2.  `Q x y` given an already existing edge $(x,y)$, find how many simple paths contain the edge $(x,y)$.
    
    It is guaranteed that at any moment, the shape of the graph is a forest.
    
    $1\le n,q,x,y\le 10^5$

Consider another formulation for the query `Q`; we find that the answer equals the product of the number of nodes on the $x$ side and the number of nodes on the $y$ side of the edge $(x,y)$, i.e. the number of nodes of the trees containing $x$ and $y$ respectively after disconnecting the edge $(x,y)$. To eliminate the effect of disconnecting the edge, after the query we reconnect the edge $(x,y)$.

The operations in the problem include both connecting edges and deleting edges, and also guarantee that it is a forest at any moment; we cannot help but think of using the LCT to maintain it. But in this problem the LCT maintains the size of the subtree, unlike maintaining the information of a chain as in our impression, and the LCT's construction **recognizes the parent but not the child**, which is inconvenient for us to directly perform subtree statistics. What to do?

The method is to count the contribution of the subtree represented by all virtual children of a node $x$ (i.e. those whose parent is $x$, but which are not among $x$'s left and right children in the Splay).

Define $siz2[x]$ as the number of nodes of the subtrees represented by all virtual children of node $x$, and $siz[x]$ as the number of nodes in the subtree of node $x$.

Different from our previous method of maintaining the number of subtree nodes in the Splay, when computing the number of nodes in the subtree of node $x$, we also need to add $siz2[x]$, i.e.

```cpp
void maintain(int x) {
  clear(0);
  if (x) siz[x] = siz[ch[x][0]] + 1 + siz[ch[x][1]] + siz2[x];
}
```

Moreover, when we **change the shape of the Splay** (i.e. change the left/right child pointers of a node in the Splay), we need to modify the value of $siz2[x]$ in time.

In the `Rotate(),Splay()` operations, we only change the relative positions of nodes in the Splay, without changing the virtual-real status of any edge, so we do not make any modification to $siz2[x]$.

In the `access` operation, after each splay, the right child of the just-splayed node is changed, i.e. the virtual-real status of the edge between this node and its original right child, and the edge between this node and the new right child, changes; we need to add the contribution of the subtree connected by the newly-become virtual edge, and subtract the contribution of the subtree connected by the just-become real edge. The code is as follows:

```cpp
void access(int x) {
  for (int f = 0; x; f = x, x = fa[x])
    splay(x), siz2[x] += siz[ch[x][1]] - siz[f], ch[x][1] = f, maintain(x);
}
```

In the `MakeRoot(),Find()` operations, we only invoke previous functions or splay along edges on the Splay, and do not need to make any modification.

When connecting two points, we modify the parent of one node. We need to add the subtree-size contribution of the new child node to the $siz2$ value of the parent node.

```cpp
st.makeroot(x);
st.makeroot(y);
st.fa[x] = y;
st.siz2[y] += st.siz[x];
```

When disconnecting an edge, we only delete a real edge on the Splay; the `Maintain` operation will maintain this information, and no modification is needed.

The above are the details of code modification; finally let's summarize the requirements and methods of maintaining subtree information with the LCT:

1.  The maintained information must have **subtractability**, such as the number of subtree nodes or the sum of subtree weights, but one cannot directly maintain the subtree maximum/minimum, because when turning a virtual edge into a real edge, one needs to exclude the contribution of the original virtual edge.
2.  Create an additional value to store the contribution of the virtual subtrees, add it into this node's answer when counting, and maintain it in time when changing the virtual-real status of edges.
3.  The rest is the same as an ordinary LCT; when counting subtree information, always make it the root node.
4.  If the maintained information does not have subtractability, such as maintaining the interval extremum, one can create a balanced tree for each node to maintain the extremum in the node's virtual subtrees.

??? note "Reference code"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    using namespace std;
    constexpr int MAXN = 100010;
    using ll = long long;
    
    struct Splay {
      int ch[MAXN][2], fa[MAXN], siz[MAXN], siz2[MAXN], tag[MAXN];
    
      void clear(int x) {
        ch[x][0] = ch[x][1] = fa[x] = siz[x] = siz2[x] = tag[x] = 0;
      }
    
      int getch(int x) { return ch[fa[x]][1] == x; }
    
      int isroot(int x) { return ch[fa[x]][0] != x && ch[fa[x]][1] != x; }
    
      void maintain(int x) {
        clear(0);
        if (x) siz[x] = siz[ch[x][0]] + 1 + siz[ch[x][1]] + siz2[x];
      }
    
      void pushdown(int x) {
        if (tag[x]) {
          if (ch[x][0]) swap(ch[ch[x][0]][0], ch[ch[x][0]][1]), tag[ch[x][0]] ^= 1;
          if (ch[x][1]) swap(ch[ch[x][1]][0], ch[ch[x][1]][1]), tag[ch[x][1]] ^= 1;
          tag[x] = 0;
        }
      }
    
      void update(int x) {
        if (!isroot(x)) update(fa[x]);
        pushdown(x);
      }
    
      void rotate(int x) {
        int y = fa[x], z = fa[y], chx = getch(x), chy = getch(y);
        fa[x] = z;
        if (!isroot(y)) ch[z][chy] = x;
        ch[y][chx] = ch[x][chx ^ 1];
        fa[ch[x][chx ^ 1]] = y;
        ch[x][chx ^ 1] = y;
        fa[y] = x;
        maintain(y);
        maintain(x);
        maintain(z);
      }
    
      void splay(int x) {
        update(x);
        for (int f = fa[x]; f = fa[x], !isroot(x); rotate(x))
          if (!isroot(f)) rotate(getch(x) == getch(f) ? f : x);
      }
    
      void access(int x) {
        for (int f = 0; x; f = x, x = fa[x])
          splay(x), siz2[x] += siz[ch[x][1]] - siz[f], ch[x][1] = f, maintain(x);
      }
    
      void makeroot(int x) {
        access(x);
        splay(x);
        swap(ch[x][0], ch[x][1]);
        tag[x] ^= 1;
      }
    
      int find(int x) {
        access(x);
        splay(x);
        while (ch[x][0]) x = ch[x][0];
        splay(x);
        return x;
      }
    } st;
    
    int n, q, x, y;
    char op;
    
    int main() {
      scanf("%d%d", &n, &q);
      while (q--) {
        scanf(" %c%d%d", &op, &x, &y);
        if (op == 'A') {
          st.makeroot(x);
          st.makeroot(y);
          st.fa[x] = y;
          st.siz2[y] += st.siz[x];
        }
        if (op == 'Q') {
          st.makeroot(x);
          st.access(y);
          st.splay(y);
          st.ch[y][0] = st.fa[x] = 0;
          st.maintain(x);
          st.makeroot(x);
          st.makeroot(y);
          printf("%lld\n", (ll)(st.siz[x] * st.siz[y]));
          st.makeroot(x);
          st.makeroot(y);
          st.fa[x] = y;
          st.siz2[y] += st.siz[x];
        }
      }
      return 0;
    }
    ```

### Exercises

-   [luogu P4299 Capital](https://www.luogu.com.cn/problem/P4299)
-   [SPOJ QTREE5 - Query on a tree V](https://www.spoj.com/problems/QTREE5)
