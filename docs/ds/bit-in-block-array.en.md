author: Backl1ght, Tiphereth-A, Enter-tainer, Ir1d, ksyx, leoleoasd, Xeonacid, aaron20100919

## Introduction

A Fenwick tree nested inside a block array can, under specific conditions, do some things that a tree-of-trees can do; but compared with a tree-of-trees, a Fenwick-tree-in-a-block-array is shorter to code and easier to implement.

## A simple example

A simple example is querying the number of points within a rectangular region on the 2D plane.

???+ note "Rectangular region query"
    Given $n$ points $(x_i, y_i)$ on the 2D plane, where $1 \le i \le n, 1 \le x_i, y_i \le n, 1 \le n \le 10^5$, implement the following operations:
    
    1.  Given $a, b, c, d$, query the number of points within the rectangular region with $(a, b)$ as its top-left corner and $(c, d)$ as its bottom-right corner.
    2.  Given $x, y$, change the y-coordinate of the point with x-coordinate $x$ to $y$.
    
    The problem is **forced online**, and it is guaranteed that $x_i \ne x_j(1 \le i, j \le n, i \ne j)$.

For operation 1, it can be turned into 4 two-dimensional-dominance queries via rectangle inclusion-exclusion; then, because it is forced online, offline algorithms like CDQ divide and conquer cannot solve it, so we think of a tree-of-trees, such as a Fenwick tree nested with a Treap. This can indeed solve the problem, but the code is too long and not particularly easy to implement.

Note that the problem additionally guarantees $x_i \ne x_j(1 \le i, j \le n, i \ne j)$; in this case we can solve it with a Fenwick tree in a block array.

### Initialization

First, an $x$ corresponds to only one $y$, so we can use an array to record this mapping relation, for example letting $Y_i$ denote the y-coordinate of the point with x-coordinate $i$.

Then, block the x-coordinates with block size $\sqrt n$. Build a weighted Fenwick tree for each block. Let $T_i$ be the Fenwick tree corresponding to the $i$-th block, and $T_{i, j}$ denote the number of points in block $i$ whose y-coordinate is within $(j - lowbit(j), j]$.

### Query

For operation 1, turn it into 4 two-dimensional-dominance queries. Now we only need to solve: given $a, b$, query how many points satisfy $1 \le x_i \le a, 1\le y_i \le b$.

Now we want to query the x-coordinate range $[1, a]$. Because the rightmost part of the query range may be an incomplete block, brute-force scan this part to see whether $Y_i \le b$, and count the number of points in this part satisfying the requirement.

Now we only need to handle the complete blocks. Brute-force scan the preceding blocks, query the number of values smaller than $b$ in each block's corresponding Fenwick tree, and accumulate them into the answer.

Is that it? No; note that handling the complete blocks is actually equivalent to querying a prefix sum of $T$, and if we also use the Fenwick-tree technique to handle $T$ during modification, then the query complexity will be lower.

### Modification

The ordinary approach is to first find the block that point $x$ is in, then do a decrement and an increment—two single-point modifications of the weighted Fenwick tree—and then set $Y_x$ to $y$.

If we use the optimization mentioned above, then we also go through a Fenwick-tree modification process for $T$; each modification is likewise a decrement and an increment, two single-point modifications of the weighted Fenwick tree.

By making certain changes to the above steps—for example, changing the decrement-and-increment to only a decrement is deleting a point; changing it to only an increment is adding a point. But we must note that an $x$ can correspond to only one $y$.

### Space complexity

The block decomposition divides into $\sqrt n$ blocks, each block having a Fenwick tree with $O(n)$ space, so the space complexity is $O(n \sqrt n)$.

### Time complexity

For a query, traversing the incomplete-block part is $O(\sqrt n)$. Then, doing a Fenwick-tree query over $T$, each encountered $T_i$ also does a Fenwick-tree query, and this step has complexity $O(\log (\sqrt n) \log n)$. So the query time complexity is $O (\sqrt n + \log (\sqrt n) \log n)$.

Modification is the same as query, with complexity $O (\sqrt n + \log (\sqrt n) \log n)$.

## Example 1

???+ note "[Intersection of Permutations](https://codeforces.com/problemset/problem/1093/E)"
    Given two permutations $a$ and $b$, implement the following two operations:
    
    1.  Given $l_a, r_a, l_b, r_b$, query the number of elements that appear both in $a[l_a ... r_a]$ and in $b[l_b ... r_b]$.
    2.  Given $x, y$, $swap(b_x, b_y)$.
    
    The sequence length $n$ satisfies $2 \le n \le 2 \cdot 10^5$, and the number of operations $q$ satisfies $1 \le q \le 2 \cdot 10^5$.

For each value $i$, let $x_i$ be its index in permutation $b$ and $y_i$ be its index in permutation $a$. This way, operation one becomes a query for the number of points within a rectangular region, and operation 2 can be seen as two modification operations. And because they are permutations, it satisfies that one $x$ corresponds to one $y$, so this problem can be written with a Fenwick tree in a block array.

??? note "Reference code (Fenwick tree in a block array - 1s)"
    ```cpp
    #include <cmath>
    #include <cstdio>
    using namespace std;
    constexpr int N = 2e5 + 5;
    constexpr int M = 447 + 5;  // sqrt(N) + 5
    
    int n, m, pa[N], pb[N];
    
    int nn, block_size, block_cnt, block_id[N], L[N], R[N], T[M][N];
    
    void build(int n) {
      nn = n;
      block_size = sqrt(nn);
      block_cnt = nn / block_size;
      for (int i = 1; i <= block_cnt; ++i) {
        L[i] = R[i - 1] + 1;
        R[i] = i * block_size;
      }
      if (R[block_cnt] < nn) {
        ++block_cnt;
        L[block_cnt] = R[block_cnt - 1] + 1;
        R[block_cnt] = nn;
      }
      for (int j = 1; j <= block_cnt; ++j)
        for (int i = L[j]; i <= R[j]; ++i) block_id[i] = j;
    }
    
    int lb(int x) { return x & -x; }
    
    void add(int p, int v, int d) {
      for (int i = block_id[p]; i <= block_cnt; i += lb(i))
        for (int j = v; j <= nn; j += lb(j)) T[i][j] += d;
    }
    
    int getsum(int p, int v) {
      if (!p) return 0;
      int res = 0;
      int id = block_id[p];
      for (int i = L[id]; i <= p; ++i)
        if (pb[i] <= v) ++res;
      for (int i = id - 1; i; i -= lb(i))
        for (int j = v; j; j -= lb(j)) res += T[i][j];
      return res;
    }
    
    void update(int x, int y) {
      add(x, pb[x], -1);
      add(y, pb[y], -1);
      swap(pb[x], pb[y]);
      add(x, pb[x], 1);
      add(y, pb[y], 1);
    }
    
    int query(int la, int ra, int lb, int rb) {
      int res = getsum(rb, ra) - getsum(rb, la - 1) - getsum(lb - 1, ra) +
                getsum(lb - 1, la - 1);
      return res;
    }
    
    int main() {
      scanf("%d %d", &n, &m);
      int v;
      for (int i = 1; i <= n; ++i) scanf("%d", &v), pa[v] = i;
      for (int i = 1; i <= n; ++i) scanf("%d", &v), pb[i] = pa[v];
    
      build(n);
      for (int i = 1; i <= n; ++i) add(i, pb[i], 1);
    
      int op, la, lb, ra, rb, x, y;
      for (int i = 1; i <= m; ++i) {
        scanf("%d", &op);
        if (op == 1) {
          scanf("%d %d %d %d", &la, &ra, &lb, &rb);
          printf("%d\n", query(la, ra, lb, rb));
        } else if (op == 2) {
          scanf("%d %d", &x, &y);
          update(x, y);
        }
      }
      return 0;
    }
    ```

??? note "Reference code (Fenwick tree nested with a Treap — TLE)"
    ```cpp
    #include <cstdio>
    #include <random>
    using namespace std;
    constexpr int N = 2e5 + 5;
    mt19937 rng(random_device{}());
    
    int n, m, pa[N], pb[N];
    
    // Treap
    struct Treap {
      struct node {
        node *l, *r;
        int sz, rnd, v;
    
        node(int _v) : l(NULL), r(NULL), sz(1), rnd(rng()), v(_v) {}
      };
    
      int get_size(node*& p) { return p ? p->sz : 0; }
    
      void push_up(node*& p) {
        if (!p) return;
        p->sz = get_size(p->l) + get_size(p->r) + 1;
      }
    
      node* root;
    
      node* merge(node* a, node* b) {
        if (!a) return b;
        if (!b) return a;
        if (a->rnd < b->rnd) {
          a->r = merge(a->r, b);
          push_up(a);
          return a;
        } else {
          b->l = merge(a, b->l);
          push_up(b);
          return b;
        }
      }
    
      void split_val(node* p, const int& k, node*& a, node*& b) {
        if (!p)
          a = b = NULL;
        else {
          if (p->v <= k) {
            a = p;
            split_val(p->r, k, a->r, b);
            push_up(a);
          } else {
            b = p;
            split_val(p->l, k, a, b->l);
            push_up(b);
          }
        }
      }
    
      void split_size(node* p, int k, node*& a, node*& b) {
        if (!p)
          a = b = NULL;
        else {
          if (get_size(p->l) <= k) {
            a = p;
            split_size(p->r, k - get_size(p->l), a->r, b);
            push_up(a);
          } else {
            b = p;
            split_size(p->l, k, a, b->l);
            push_up(b);
          }
        }
      }
    
      void ins(int val) {
        node *a, *b;
        split_val(root, val, a, b);
        a = merge(a, new node(val));
        root = merge(a, b);
      }
    
      void del(int val) {
        node *a, *b, *c, *d;
        split_val(root, val, a, b);
        split_val(a, val - 1, c, d);
        delete d;
        root = merge(c, b);
      }
    
      int qry(int val) {
        node *a, *b;
        split_val(root, val, a, b);
        int res = get_size(a);
        root = merge(a, b);
        return res;
      }
    
      int qry(int l, int r) { return qry(r) - qry(l - 1); }
    };
    
    // Fenwick Tree
    Treap T[N];
    
    int lb(int x) { return x & -x; }
    
    void ins(int x, int v) {
      for (; x <= n; x += lb(x)) T[x].ins(v);
    }
    
    void del(int x, int v) {
      for (; x <= n; x += lb(x)) T[x].del(v);
    }
    
    int qry(int x, int mi, int ma) {
      int res = 0;
      for (; x; x -= lb(x)) res += T[x].qry(mi, ma);
      return res;
    }
    
    int main() {
      scanf("%d %d", &n, &m);
      int v;
      for (int i = 1; i <= n; ++i) scanf("%d", &v), pa[v] = i;
      for (int i = 1; i <= n; ++i) scanf("%d", &v), pb[i] = pa[v];
      for (int i = 1; i <= n; ++i) ins(i, pb[i]);
    
      int op, la, lb, ra, rb, x, y;
      for (int i = 1; i <= m; ++i) {
        scanf("%d", &op);
        if (op == 1) {
          scanf("%d %d %d %d", &la, &ra, &lb, &rb);
          printf("%d\n", qry(rb, la, ra) - qry(lb - 1, la, ra));
        } else if (op == 2) {
          scanf("%d %d", &x, &y);
          del(x, pb[x]);
          del(y, pb[y]);
          swap(pb[x], pb[y]);
          ins(x, pb[x]);
          ins(y, pb[y]);
        }
      }
      return 0;
    }
    ```

## Example 2

???+ note "[Complicated Computations](https://codeforces.com/contest/1436/problem/E)"
    Given a sequence $a$, take the array formed by the MEX of all contiguous subsequences of $a$ as $b$; ask the MEX of $b$. The MEX of a sequence is the smallest **positive integer** that has not appeared in the sequence.
    
    The sequence length $n$ satisfies $1 \le n \le 10^5$.

**Observation**: the MEX of a sequence is $mex$ if and only if this sequence contains $1$ to $mex-1$ but does not contain $mex$.

Determine in turn whether there is a contiguous subsequence with MEX from $1$ to $n+1$. If there is no contiguous subsequence with MEX $i$, then the answer is $i$. If all exist, then the answer is $n + 2$.

When determining $i$, view the sequence as several segments separated by zero or more $i$s. If there exists a segment that contains $1$ to $i - 1$ but does not contain $i$, then it means there is a contiguous subsequence with value $i$.

Use an array $Y_j$ to record the position of the previous element with value $a_j$, taking $j$ as $x$, $Y_j$ as $y$, and $a_j$ as $z$. This way, computing whether a segment contains $1$ to $i - 1$ is a three-dimensional-dominance problem. Formally, determining whether the MEX value of segment $[l, r]$ is $i$ is checking whether the number of points satisfying $l \le j \le r, Y_j \le l - 1, a_j \le i - 1$ is $i-1$.

If, after determining the elements with value $i$, we then insert the corresponding points, then because only elements with $a_j \le i - 1$ exist within $[l, r]$, the above three-dimensional-dominance problem can be converted into a two-dimensional-dominance problem.

??? note "Reference code (Fenwick tree in a block array - 78ms)"
    ```cpp
    #include <cmath>
    #include <cstdio>
    #include <vector>
    using namespace std;
    constexpr int N = 1e5 + 5;
    constexpr int M = 316 + 5;  // sqrt(N) + 5
    
    // block decomposition
    int nn, b[N], block_size, block_cnt, block_id[N], L[N], R[N], T[M][N];
    
    void build(int n) {
      nn = n;
      block_size = sqrt(nn);
      block_cnt = nn / block_size;
      for (int i = 1; i <= block_cnt; ++i) {
        L[i] = R[i - 1] + 1;
        R[i] = i * block_size;
      }
      if (R[block_cnt] < nn) {
        ++block_cnt;
        L[block_cnt] = R[block_cnt - 1] + 1;
        R[block_cnt] = nn;
      }
      for (int j = 1; j <= block_cnt; ++j)
        for (int i = L[j]; i <= R[j]; ++i) block_id[i] = j;
    }
    
    int lb(int x) { return x & -x; }
    
    // d = 1: add point (p, v)
    // d = -1: delete point (p, v)
    void add(int p, int v, int d) {
      for (int i = block_id[p]; i <= block_cnt; i += lb(i))
        for (int j = v; j <= nn; j += lb(j)) T[i][j] += d;
    }
    
    // query how many points within [1, r] have a y-coordinate less than or equal to val
    int getsum(int p, int v) {
      if (!p) return 0;
      int res = 0;
      int id = block_id[p];
      for (int i = L[id]; i <= p; ++i)
        if (b[i] && b[i] <= v) ++res;
      for (int i = id - 1; i; i -= lb(i))
        for (int j = v; j; j -= lb(j)) res += T[i][j];
      return res;
    }
    
    // query how many points within [l, r] have a y-coordinate less than or equal to val
    int query(int l, int r, int val) {
      if (l > r) return -1;
      int res = getsum(r, val) - getsum(l - 1, val);
      return res;
    }
    
    // add point (p, v)
    void update(int p, int v) {
      b[p] = v;
      add(p, v, 1);
    }
    
    int n, a[N];
    vector<int> g[N];
    
    int main() {
      scanf("%d", &n);
    
      // to reduce case analysis, sentinel nodes are added
      // because when adding to a Fenwick tree, a value of 0 may cause an infinite loop, everything is shifted one position to the right
      // a_1 and a_{n+2} are sentinel nodes
      for (int i = 2; i <= n + 1; ++i) scanf("%d", &a[i]);
      for (int i = 2; i <= n + 1; ++i) g[a[i]].push_back(i);
    
      // block decomposition
      build(n + 2);
    
      int ans = n + 2, lst, ok;
      for (int i = 1; i <= n + 1; ++i) {
        g[i].push_back(n + 2);
    
        lst = 1;
        ok = 0;
        for (int pos : g[i]) {
          if (query(lst + 1, pos - 1, lst) == i - 1) {
            ok = 1;
            break;
          }
          lst = pos;
        }
    
        if (!ok) {
          ans = i;
          break;
        }
    
        lst = 1;
        g[i].pop_back();
        for (int pos : g[i]) {
          update(pos, lst);
          lst = pos;
        }
      }
      printf("%d\n", ans);
      return 0;
    }
    ```

??? note "Reference code (segment tree nested with a Treap - 468ms)"
    ```cpp
    #include <cstdio>
    #include <random>
    #include <vector>
    using namespace std;
    constexpr int N = 1e5 + 5;
    
    vector<int> g[N];
    int n, a[N];
    
    mt19937 rng(random_device{}());
    
    struct Treap {
      struct node {
        node *l, *r;
        unsigned rnd;
        int sz, v;
    
        node(int _v) : l(NULL), r(NULL), rnd(rng()), sz(1), v(_v) {}
      };
    
      int get_size(node*& p) { return p ? p->sz : 0; }
    
      void push_up(node*& p) {
        if (!p) return;
        p->sz = get_size(p->l) + get_size(p->r) + 1;
      }
    
      node* root;
    
      node* merge(node* a, node* b) {
        if (!a) return b;
        if (!b) return a;
        if (a->rnd < b->rnd) {
          a->r = merge(a->r, b);
          push_up(a);
          return a;
        } else {
          b->l = merge(a, b->l);
          push_up(b);
          return b;
        }
      }
    
      void split_val(node* p, const int& k, node*& a, node*& b) {
        if (!p)
          a = b = NULL;
        else {
          if (p->v <= k) {
            a = p;
            split_val(p->r, k, a->r, b);
            push_up(a);
          } else {
            b = p;
            split_val(p->l, k, a, b->l);
            push_up(b);
          }
        }
      }
    
      void split_size(node* p, int k, node*& a, node*& b) {
        if (!p)
          a = b = NULL;
        else {
          if (get_size(p->l) <= k) {
            a = p;
            split_size(p->r, k - get_size(p->l), a->r, b);
            push_up(a);
          } else {
            b = p;
            split_size(p->l, k, a, b->l);
            push_up(b);
          }
        }
      }
    
      void insert(int val) {
        node *a, *b;
        split_val(root, val, a, b);
        a = merge(a, new node(val));
        root = merge(a, b);
      }
    
      int query(int val) {
        node *a, *b;
        split_val(root, val, a, b);
        int res = get_size(a);
        root = merge(a, b);
        return res;
      }
    
      int qry(int l, int r) { return query(r) - query(l - 1); }
    };
    
    // Segment Tree
    Treap T[N << 2];
    
    void insert(int x, int l, int r, int p, int val) {
      T[x].insert(val);
      if (l == r) return;
      int mid = (l + r) >> 1;
      if (p <= mid)
        insert(x << 1, l, mid, p, val);
      else
        insert(x << 1 | 1, mid + 1, r, p, val);
    }
    
    int query(int x, int l, int r, int L, int R, int val) {
      if (l == L && r == R) return T[x].query(val);
      int mid = (l + r) >> 1;
      if (R <= mid) return query(x << 1, l, mid, L, R, val);
      if (L > mid) return query(x << 1 | 1, mid + 1, r, L, R, val);
      return query(x << 1, l, mid, L, mid, val) +
             query(x << 1 | 1, mid + 1, r, mid + 1, R, val);
    }
    
    int query(int l, int r, int val) {
      if (l > r) return -1;
      return query(1, 1, n, l, r, val);
    }
    
    int main() {
      scanf("%d", &n);
      for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
      for (int i = 1; i <= n; ++i) g[a[i]].push_back(i);
    
      // a_0 and a_{n+1} are sentinel nodes
      int ans = n + 2, lst, ok;
      for (int i = 1; i <= n + 1; ++i) {
        g[i].push_back(n + 1);
    
        lst = 0;
        ok = 0;
        for (int pos : g[i]) {
          if (query(lst + 1, pos - 1, lst) == i - 1) {
            ok = 1;
            break;
          }
          lst = pos;
        }
    
        if (!ok) {
          ans = i;
          break;
        }
    
        lst = 0;
        g[i].pop_back();
        for (int pos : g[i]) {
          insert(1, 1, n, pos, lst);
          lst = pos;
        }
      }
      printf("%d\n", ans);
      return 0;
    }
    ```
