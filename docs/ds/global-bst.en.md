## Introduction

Prerequisite: [heavy-light decomposition](../graph/hld.md)

Since the time complexity of heavy-light decomposition is $O(n\log^2 n)$, while the LCT we are familiar with, although its time complexity is $O(n\log n)$, has a relatively large constant factor and may be even slower than heavy-light decomposition. So is there a method that is both $O(n\log n)$ and has a relatively small constant factor? This is where the global balanced binary tree appears.

The global balanced binary tree is actually a forest of binary trees, each of which maintains a heavy chain. But the binary trees in this forest are also connected to each other: the root of each binary tree connects to the parent of the head of that heavy chain, just as in the LCT. But the global balanced binary tree is a static tree, differing from the LCT: after it is built, the shape of the tree does not change.

The global balanced binary tree is a data structure that can handle chain modification/query on a tree, achieving:

-   $O(\log n)$ for whole-chain modification.
-   $O(\log n)$ for whole-chain query.
-   $O(\log n)$ for finding the lowest common ancestor, subtree modification, subtree query, etc.; these complexities are the same as heavy-light decomposition.

## Main properties

1.  A global balanced binary tree is composed of many binary trees connected by light edges, and each binary tree maintains a heavy chain of the original tree, where the order of its inorder traversal is the order of monotonically increasing depth of this heavy chain. Each node appears in only one binary tree.
2.  Edges are divided into heavy edges and light edges; heavy edges are the edges contained in a binary tree, and when maintaining them, we just maintain the binary tree normally, recording the left and right children and the parent. A light edge points from the root of a binary tree to the parent of the top node of the heavy chain it corresponds to. When maintaining a light edge, it "recognizes the parent but not the child", i.e. one can only access the parent from the child, not the reverse. Note that the edges in the global balanced binary tree have no correspondence with the edges in the original tree.
3.  Counting both heavy edges and light edges, the height of the global balanced binary tree is on the order of $O(\log n)$. This is the property that guarantees the time complexity of the global balanced binary tree.

Below is an example of building a global balanced binary tree. The first figure is the original tree, rooted at node 1. Solid lines are heavy edges.

![global-bst-1](images/global-bst-1.svg)

The second figure is the built global balanced binary tree, where dashed lines are light edges, solid lines are heavy edges, and each binary tree is indicated by a red circle.

![global-bst-2](images/global-bst-2.svg)

## Building the tree

First, as with ordinary heavy-light decomposition, one DFS finds the heavy child of each node. Then, starting from the root, find the heavy chain the root node is on; for the light children of these points, recursively build the tree and connect light edges. Then we need to build a binary tree for the points on the heavy chain. We first store the points on the heavy chain into an array and compute the sum of the subtree sizes of each point's light children plus one (i.e. the size contributed by the point itself). Then, according to this, we find the weighted midpoint of this heavy chain, take it as the root of the binary tree, recursively build the tree on both sides, and connect heavy edges.

The code is as follows:

???+ note "Implementation"
    ```cpp
    std::vector<int> G[N];
    int n, fa[N], son[N], sz[N];
    
    void dfsS(int u) {
      sz[u] = 1;
      for (int v : G[u]) {
        dfsS(v);
        sz[u] += sz[v];
        if (sz[v] > sz[son[u]]) son[u] = v;
      }
    }
    
    int b[N], bs[N], l[N], r[N], f[N], ss[N];
    
    // build a binary tree for the points in [bl,br) of b, and return the root of the binary tree
    int cbuild(int bl, int br) {
      int x = bl, y = br;
      while (y - x > 1) {
        int mid = (x + y) >> 1;
        if (2 * (bs[mid] - bs[bl]) <= bs[br] - bs[bl])
          x = mid;
        else
          y = mid;
      }
      // binary-search for the midpoint weighted by bs
      y = b[x];
      ss[y] = br - bl;  // ss: the size of the heavy subtree in the binary tree
      if (bl < x) {
        l[y] = cbuild(bl, x);
        f[l[y]] = y;
      }
      if (x + 1 < br) {
        r[y] = cbuild(x + 1, br);
        f[r[y]] = y;
      }
      return y;
    }
    
    int build(int x) {
      int y = x;
      do
        for (int v : G[y])
          if (v != son[y])
            f[build(v)] =
                y;  // recursively build the tree and connect the light edge; note the edge is connected from the binary tree's root, not from the child
      while (y = son[y]);
      y = 0;
      do {
        b[y++] = x;                              // store the points in the heavy chain
        bs[y] = bs[y - 1] + sz[x] - sz[son[x]];  // bs: light children's size sum + 1, take the prefix sum
      } while (x = son[x]);
      return cbuild(0, y);
    }
    ```

From the code we can see that the time complexity of building the tree is $O(n\log n)$. Next we can prove that the tree height is $O(\log n)$: consider jumping from any point to the root via parents. Jumping a light edge amounts to jumping to another heavy chain in the original tree, and by the property of heavy-light decomposition, we jump at most $O(\log n)$ light edges; because when building the binary tree the root is found as the weighted midpoint counting light children, jumping a heavy edge once at least doubles the size counting light children, so we jump at most $O(\log n)$ heavy edges too. The overall tree height is $O(\log n)$.

## Query

The above is the part about the global balanced binary tree. The remaining operation methods for chain modification and chain query are relatively simple; one only needs to start from the point to operate on and keep jumping to the root. Operating on all points on the heavy chain of some point with depth smaller than it is essentially equivalent to operating on all nodes to the left of the target node in that heavy chain's binary tree. These operations can be decomposed into a series of subtree operations, similar to the maintenance method of an ordinary binary tree, involving maintaining the subtree sum and applying subtree tags. In this process, permanent tagging is used. One can also use pushdown to apply tags and pushup to maintain the subtree sum, but this way may be relatively complex, because usually handling a binary tree is done top-down, whereas here one needs to first determine the jump path and then pushdown from top to bottom, possibly leading to a larger constant factor.

The code is as follows:

???+ note "Implementation"
    ```cpp
    // a: subtree-add tag
    // s: subtree sum (not counting the add tag)
    int a[N], s[N];
    
    void add(int x) {
      bool t = true;
      int z = 0;
      while (x) {
        s[x] += z;
        if (t) {
          a[x]++;
          if (r[x]) a[r[x]]--;
          z += 1 + ss[l[x]];
          s[x] -= ss[r[x]];
        }
        t = (x != l[f[x]]);
        if (t && x != r[f[x]]) z = 0;  // clear when skipping a light edge
        x = f[x];
      }
    }
    
    int query(int x) {
      int ret = 0;
      bool t = true;
      int z = 0;
      while (x) {
        if (t) {
          ret += s[x] - s[r[x]];
          ret -= 1ll * ss[r[x]] * a[r[x]];
          z += 1 + ss[l[x]];
        }
        ret += 1ll * z * a[x];
        t = (x != l[f[x]]);
        if (t && x != r[f[x]]) z = 0;  // clear when skipping a light edge
        x = f[x];
      }
      return ret;
    }
    ```

In addition, for subtree operations, which need to consider light children, one needs to maintain another subtree sum and subtree tag including light children; you can go do "[P3384 【Template】Heavy-Light Decomposition](https://www.luogu.com.cn/problem/P3384)".

## Example

??? note "[P4751 【Template】"Dynamic DP" & Dynamic Tree Divide-and-Conquer (enhanced)](https://www.luogu.com.cn/problem/P4751)"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    constexpr int MAXN = 1000000;
    constexpr int MAXM = 3000000;
    constexpr int INF = 0x3FFFFFFF;
    using namespace std;
    
    struct edge {
      int to;
      edge *nxt;
    } edges[MAXN * 2 + 5];
    
    edge *ncnt = &edges[0], *Adj[MAXN + 5];
    int n, m;
    
    struct Matrix {
      int M[2][2];
    
      Matrix operator*(const Matrix &B) const {
        static Matrix ret;
        for (int i = 0; i < 2; i++)
          for (int j = 0; j < 2; j++) {
            ret.M[i][j] = -INF;
            for (int k = 0; k < 2; k++)
              ret.M[i][j] = max(ret.M[i][j], M[i][k] + B.M[k][j]);
          }
        return ret;
      }
    } matr1[MAXN + 5], matr2[MAXN + 5];  // each point maintains two matrices
    
    int root;
    int w[MAXN + 5], dep[MAXN + 5], son[MAXN + 5], siz[MAXN + 5], lsiz[MAXN + 5];
    int g[MAXN + 5][2], f[MAXN + 5][2], trfa[MAXN + 5], bstch[MAXN + 5][2];
    int stk[MAXN + 5], tp;
    bool vis[MAXN + 5];
    
    void AddEdge(int u, int v) {
      edge *p = ++ncnt;
      p->to = v;
      p->nxt = Adj[u];
      Adj[u] = p;
    
      edge *q = ++ncnt;
      q->to = u;
      q->nxt = Adj[v];
      Adj[v] = q;
    }
    
    void DFS(int u, int fa) {
      siz[u] = 1;
      for (edge *p = Adj[u]; p != NULL; p = p->nxt) {
        int v = p->to;
        if (v == fa) continue;
        dep[v] = dep[u] + 1;
        DFS(v, u);
        siz[u] += siz[v];
        if (!son[u] || siz[son[u]] < siz[v]) son[u] = v;
      }
      lsiz[u] = siz[u] - siz[son[u]];  // light children's siz sum + 1
    }
    
    void DFS2(int u, int fa) {
      f[u][1] = w[u], f[u][0] = 0;
      g[u][1] = w[u], g[u][0] = 0;
      if (son[u]) {
        DFS2(son[u], u);
        f[u][0] += max(f[son[u]][0], f[son[u]][1]);
        f[u][1] += f[son[u]][0];
      }
      for (edge *p = Adj[u]; p != NULL; p = p->nxt) {
        int v = p->to;
        if (v == fa || v == son[u]) continue;
        DFS2(v, u);
        f[u][0] += max(f[v][0], f[v][1]);  // f[][] is the normal DP array
        f[u][1] += f[v][0];
        g[u][0] += max(f[v][0], f[v][1]);  // the g[][] array only counts the information of itself and its light children
        g[u][1] += f[v][0];
      }
    }
    
    void PushUp(int u) {
      matr2[u] = matr1[u];  // matr1 is the single point plus light-children information, matr2 is the interval information
      if (bstch[u][0]) matr2[u] = matr2[bstch[u][0]] * matr2[u];
      // note the direction of the transition, but if our matrix-multiplication definition differs, the direction may also differ
      if (bstch[u][1]) matr2[u] = matr2[u] * matr2[bstch[u][1]];
    }
    
    int getmx2(int u) { return max(matr2[u].M[0][0], matr2[u].M[0][1]); }
    
    int getmx1(int u) { return max(getmx2(u), matr2[u].M[1][0]); }
    
    int SBuild(int l, int r) {
      if (l > r) return 0;
      int tot = 0;
      for (int i = l; i <= r; i++) tot += lsiz[stk[i]];
      for (int i = l, sumn = lsiz[stk[l]]; i <= r; i++, sumn += lsiz[stk[i]])
        if (sumn * 2 >= tot)  // it is the centroid now
        {
          int lch = SBuild(l, i - 1), rch = SBuild(i + 1, r);
          bstch[stk[i]][0] = lch;
          bstch[stk[i]][1] = rch;
          trfa[lch] = trfa[rch] = stk[i];
          PushUp(stk[i]);  // count up the interval information
          return stk[i];
        }
      return 0;
    }
    
    int Build(int u) {
      for (int pos = u; pos; pos = son[pos]) vis[pos] = true;
      for (int pos = u; pos; pos = son[pos])
        for (edge *p = Adj[pos]; p != NULL; p = p->nxt)
          if (!vis[p->to])  // it is a light child
          {
            int v = p->to, ret = Build(v);
            trfa[ret] = pos;  // connect the light child's treefa[] up
          }
      tp = 0;
      for (int pos = u; pos; pos = son[pos]) stk[++tp] = pos;  // take out the heavy chain
      int ret = SBuild(1, tp);  // do a separate SBuild on the heavy chain (I guess it's Special Build?)
      return ret;               // return the root of the current heavy chain's binary tree
    }
    
    void Modify(int u, int val) {
      matr1[u].M[1][0] += val - w[u];
      w[u] = val;
      for (int pos = u; pos; pos = trfa[pos])
        if (trfa[pos] && bstch[trfa[pos]][0] != pos && bstch[trfa[pos]][1] != pos) {
          matr1[trfa[pos]].M[0][0] -= getmx1(pos);
          matr1[trfa[pos]].M[0][1] = matr1[trfa[pos]].M[0][0];
          matr1[trfa[pos]].M[1][0] -= getmx2(pos);
          PushUp(pos);
          matr1[trfa[pos]].M[0][0] += getmx1(pos);
          matr1[trfa[pos]].M[0][1] = matr1[trfa[pos]].M[0][0];
          matr1[trfa[pos]].M[1][0] += getmx2(pos);
        } else
          PushUp(pos);
    }
    
    int read() {
      int ret = 0, f = 1;
      char c = 0;
      while (c < '0' || c > '9') {
        c = getchar();
        if (c == '-') f = -f;
      }
      ret = 10 * ret + c - '0';
      while (true) {
        c = getchar();
        if (c < '0' || c > '9') break;
        ret = 10 * ret + c - '0';
      }
      return ret * f;
    }
    
    void print(int x) {
      if (x == 0) return;
      print(x / 10);
      putchar(x % 10 + '0');
    }
    
    int main() {
      scanf("%d %d", &n, &m);
      for (int i = 1; i <= n; i++) w[i] = read();
      int u, v;
      for (int i = 1; i < n; i++) {
        u = read(), v = read();
        AddEdge(u, v);
      }
      DFS(1, -1);
      // find the heavy children
      DFS2(1, -1);
      // find the initial DP values; this can also be done inside Build(), but writing it this way unifies it with the heavy-light-decomposition style
      for (int i = 1; i <= n; i++) {
        matr1[i].M[0][0] = matr1[i].M[0][1] = g[i][0];
        matr1[i].M[1][0] = g[i][1], matr1[i].M[1][1] = -INF;  // initialize the matrix
      }
      root = Build(1);  // root is the centroid of the heavy chain the root node is on
      int lastans = 0;
      for (int i = 1; i <= m; i++) {
        u = read(), v = read();
        u ^= lastans;  // forced online
        Modify(u, v);
        lastans = getmx1(root);  // directly take the value
        if (lastans == 0)
          putchar('0');
        else
          print(lastans);
        putchar('\n');
      }
      return 0;
    }
    ```

## References

[P4211 \[LNOI2014\] LCA | Global Balanced Binary Tree](https://www.luogu.com.cn/blog/nederland/globalbst)
