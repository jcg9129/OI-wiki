author: Ir1d, sshwy, Enter-tainer, H-J-Granger, ouuan, GavinZhengOI, hsfzLZH1, xyf007

The problem of [static interval k-th smallest value (POJ 2104 K-th Number)](http://poj.org/problem?id=2104) can be solved with a [weighted segment tree](./persistent-seg.md) in $O(n\log n)$ time complexity.

What if the interval becomes dynamic? That is, what if we also need to support an operation: single-point modification of the value at a certain position, how should we handle it?

??? note "Example problem [Fake Balanced Tree (tree of trees)](https://loj.ac/problem/106)"
    Maintain an ordered sequence, where the following operations need to be provided:
    
    -   Query the rank of $x$ within an interval;
    -   Query the value whose rank is $k$ within an interval;
    -   Modify the numeric value at a certain position;
    -   Query the predecessor of $x$ within an interval (the predecessor is defined as the largest number smaller than $x$);
    -   Query the successor of $x$ within an interval (the successor is defined as the smallest number larger than $x$).

??? note "Example problem [Luogu P2617 Dynamic Rankings](https://www.luogu.com.cn/problem/P2617)"
    Given a sequence of $n$ numbers $a_1,a_2 \dots a_n$, we need to support two kinds of operations:
    
    -   `Q l r k` means query the $k$-th smallest number whose index is in the interval $[l,r]$
    -   `C x y` means change $a_x$ to $y$

If we use what is discussed in [balanced tree nested in a segment tree](./balanced-in-seg.md), i.e. a segment tree nesting balanced trees—for each node of the segment tree, maintain a balanced tree for the interval it represents, then use binary search to find the $k$-th smallest value—since each query operation has to cover multiple intervals, i.e. multiple nodes, but a balanced tree cannot search multiple values together, the time complexity is $O(n\log^3 n)$, which is not optimal.

The idea of optimization is to combine the two operations of binary-searching the answer and querying the count of numbers less than a value, using a **segment tree nesting a dynamically-allocated weighted segment tree**; since the structure of all the segment trees is the same, one can do segment-tree binary search simultaneously on multiple trees.

When a modification operation is performed, first jump from top to bottom on the segment tree to the point being modified, delete the original value on the dynamically-allocated weighted segment tree pointed to by the points passed through, then insert the new value; this needs to pass through $O(\log n)$ nodes on the segment tree, and one modification operation on the dynamically-allocated weighted segment tree is $O(\log n)$, so the time complexity of the modification operation is $O(\log^2 n)$.

When querying the answer, first take out all the points that this interval covers on the segment tree, then use a method similar to the static interval $k$-th smallest value, jumping these points together to the left child or the right child. If the value stored in the left children of all these points is greater than or equal to $k$, then jump left, otherwise jump right. Since at most $O(\log n)$ nodes can be covered, at most this many nodes jump down at a time, and the time complexity is $O(\log^2 n)$.

Since the constant factor of the segment tree is relatively large, in implementation a **Fenwick tree**, which has a smaller constant factor and is more convenient for handling prefix sums, is often used for implementation. In addition, the space complexity is $O(n\log^2 n)$, so **pay attention to the space limit** when using it.

Here is one code implementation:

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <cstdio>
    #include <cstring>
    #include <map>
    #include <set>
    #define LC o << 1
    #define RC o << 1 | 1
    using namespace std;
    constexpr int MAXN = 1000010;
    int n, m, a[MAXN], u[MAXN], x[MAXN], l[MAXN], r[MAXN], k[MAXN], cur, cur1, cur2,
        q1[MAXN], q2[MAXN], v[MAXN];
    char op[MAXN];
    set<int> ST;
    map<int, int> mp;
    
    struct segment_tree  // encapsulated dynamically-allocated weighted segment tree
    {
      int cur, rt[MAXN * 4], sum[MAXN * 60], lc[MAXN * 60], rc[MAXN * 60];
    
      void build(int& o) { o = ++cur; }
    
      void print(int o, int l, int r) {
        if (!o) return;
        if (l == r && sum[o]) printf("%d ", l);
        int mid = (l + r) >> 1;
        print(lc[o], l, mid);
        print(rc[o], mid + 1, r);
      }
    
      void update(int& o, int l, int r, int x, int v) {
        if (!o) o = ++cur;
        sum[o] += v;
        if (l == r) return;
        int mid = (l + r) >> 1;
        if (x <= mid)
          update(lc[o], l, mid, x, v);
        else
          update(rc[o], mid + 1, r, x, v);
      }
    } st;
    
    // Fenwick tree implementation
    namepace fenwick_impl {
      int lowbit(int o) { return (o & (-o)); }
    
      void upd(int o, int x, int v) {
        for (; o <= n; o += lowbit(o)) st.update(st.rt[o], 1, n, x, v);
      }
    
      void gtv(int o, int* A, int& p) {
        p = 0;
        for (; o; o -= lowbit(o)) A[++p] = st.rt[o];
      }
    
      int qry(int l, int r, int k) {
        if (l == r) return l;
        int mid = (l + r) >> 1, siz = 0;
        for (int i = 1; i <= cur1; i++) siz += st.sum[st.lc[q1[i]]];
        for (int i = 1; i <= cur2; i++) siz -= st.sum[st.lc[q2[i]]];
        // printf("j %d %d %d %d\n",cur1,cur2,siz,k);
        if (siz >= k) {
          for (int i = 1; i <= cur1; i++) q1[i] = st.lc[q1[i]];
          for (int i = 1; i <= cur2; i++) q2[i] = st.lc[q2[i]];
          return qry(l, mid, k);
        } else {
          for (int i = 1; i <= cur1; i++) q1[i] = st.rc[q1[i]];
          for (int i = 1; i <= cur2; i++) q2[i] = st.rc[q2[i]];
          return qry(mid + 1, r, k - siz);
        }
      }
    }
    using namespace fenwick_impl;
    
    // segment tree implementation
    namespace segtree_impl {
    void build(int o, int l, int r) {
      st.build(st.rt[o]);
      if (l == r) return;
      int mid = (l + r) >> 1;
      build(LC, l, mid);
      build(RC, mid + 1, r);
    }
    
    void print(int o, int l, int r) {
      printf("%d %d:", l, r);
      st.print(st.rt[o], 1, n);
      printf("\n");
      if (l == r) return;
      int mid = (l + r) >> 1;
      print(LC, l, mid);
      print(RC, mid + 1, r);
    }
    
    void update(int o, int l, int r, int q, int x, int v) {
      st.update(st.rt[o], 1, n, x, v);
      if (l == r) return;
      int mid = (l + r) >> 1;
      if (q <= mid)
        update(LC, l, mid, q, x, v);
      else
        update(RC, mid + 1, r, q, x, v);
    }
    
    void getval(int o, int l, int r, int ql, int qr) {
      if (l > qr || r < ql) return;
      if (ql <= l && r <= qr) {
        q[++cur] = st.rt[o];
        return;
      }
      int mid = (l + r) >> 1;
      getval(LC, l, mid, ql, qr);
      getval(RC, mid + 1, r, ql, qr);
    }
    
    int query(int l, int r, int k) {
      if (l == r) return l;
      int mid = (l + r) >> 1, siz = 0;
      for (int i = 1; i <= cur; i++) siz += st.sum[st.lc[q[i]]];
      if (siz >= k) {
        for (int i = 1; i <= cur; i++) q[i] = st.lc[q[i]];
        return query(l, mid, k);
      } else {
        for (int i = 1; i <= cur; i++) q[i] = st.rc[q[i]];
        return query(mid + 1, r, k - siz);
      }
    }
    }  // namespace segtree_impl
    
    int main() {
      scanf("%d%d", &n, &m);
      for (int i = 1; i <= n; i++) scanf("%d", a + i), ST.insert(a[i]);
      for (int i = 1; i <= m; i++) {
        scanf(" %c", op + i);
        if (op[i] == 'C')
          scanf("%d%d", u + i, x + i), ST.insert(x[i]);
        else
          scanf("%d%d%d", l + i, r + i, k + i);
      }
      for (set<int>::iterator it = ST.begin(); it != ST.end(); it++)
        mp[*it] = ++cur, v[cur] = *it;
      for (int i = 1; i <= n; i++) a[i] = mp[a[i]];
      for (int i = 1; i <= m; i++)
        if (op[i] == 'C') x[i] = mp[x[i]];
      n += m;
      // build(1,1,n);
      for (int i = 1; i <= n; i++) upd(i, a[i], 1);
      // print(1,1,n);
      for (int i = 1; i <= m; i++) {
        if (op[i] == 'C') {
          upd(u[i], a[u[i]], -1);
          upd(u[i], x[i], 1);
          a[u[i]] = x[i];
        } else {
          gtv(r[i], q1, cur1);
          gtv(l[i] - 1, q2, cur2);
          printf("%d\n", v[qry(1, n, k[i])]);
        }
      }
      return 0;
    }
    ```
