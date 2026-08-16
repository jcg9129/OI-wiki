## The problem of segments

We introduce it with a light, elegant problem:

> For a permutation of $1-n$, we call an interval whose value range is continuous a segment. Ask the number of segments of a permutation. For example, the segments of $\{5 ,3 ,4, 1 ,2\}$ are: $[1,1],[2,2],[3,3],[4,4],[5,5],[2,3],[4,5],[1,3],[2,5],[1,5]$.

Seeing this, it feels like we need to maintain the value-range set of intervals, and the complexity seems rather unfriendly. A segment tree can query whether some interval is a segment, but cannot really count the number of segments.

Here we introduce this magical data structure—the divide-combine tree!

## Continuous segments

Before introducing the divide-combine tree, we first make some prerequisite restrictions. Since the definitions given in LCA's courseware are hard to understand, for the reader's convenience we give some not-too-rigorous (but easier-to-understand) definitions here.

### Permutations and continuous segments

**Permutation**: define an order-$n$ permutation $P$ as a sequence of size $n$ such that $P_i$ ranges over $1,2,\cdots,n$. More formally, an order-$n$ permutation $P$ is an ordered set satisfying:

1.  $|P|=n$.
2.  $\forall i,P_i\in[1,n]$.
3.  $\nexists i,j\in[1,n],P_i=P_j$.

    **Continuous segment**: for a permutation $P$, define a continuous segment $(P,[l,r])$ to denote an interval $[l,r]$ requiring the value range of $P_{l\sim r}$ to be continuous. More formally, for a permutation $P$, a continuous segment denotes an interval $[l,r]$ satisfying:

$$
(\nexists\ x,z\in[l,r],y\notin[l,r],\ P_x<P_y<P_z)
$$

In particular, when $l>r$, we consider this an empty continuous segment, denoted $(P,\varnothing)$.

We call the set of all continuous segments of permutation $P$ as $I_P$, and we consider $(P,\varnothing)\in I_P$.

### Operations on continuous segments

Continuous segments are defined relying on intervals and value ranges, so we can define the intersection, union, and difference operations of continuous segments.

Define $A=(P,[a,b]),B=(P,[x,y])$, with $A,B\in I_P$. Then the relations and operations of continuous segments can be expressed as:

1.  $A\subseteq B\iff x\le a\wedge b\le y$.
2.  $A=B\iff a=x\wedge b=y$.
3.  $A\cap B=(P,[\max(a,x),\min(b,y)])$.
4.  $A\cup B=(P,[\min(a,x),\max(b,y)])$.
5.  $A\setminus B=(P,\{i|i\in[a,b]\wedge i\notin[x,y]\})$.

In fact these operations are just the ordinary set intersection, union, and difference placed on intervals.

### Properties of continuous segments

Some obvious properties of continuous segments. We define $A,B\in I_P,A \cap B \neq \varnothing,A \notin B,B \notin A$; then $A\cup B,A\cap B,A\setminus B,B\setminus A\in I_P$.

Proof? The essence of the proof is just the intersection, union, and difference operations of sets.

## The divide-combine tree

OK, now we get to the key point. You may have guessed it: the divide-combine tree is exactly a tree composed of continuous segments. But note that a permutation may have as many as $O(n^2)$ continuous segments, so we need to extract the more basic continuous segments among them to compose the divide-combine tree.

### Primitive segments

The full name of this definition is actually **primitive continuous segment**. But the author thinks "primitive segment" is more concise.

For a permutation $P$, we consider a primitive segment $M$ to denote one in the set $I_P$ for which there is no continuous segment that intersects it without containing it. Formally defined, we consider $X\in I_P$ satisfying $\forall A\in I_P,\ X\cap A= (P,\varnothing)\vee X\subseteq A\vee A\subseteq X$.

The set of all primitive segments is $M_P$. Obviously, $(P,\varnothing)\in M_P$.

Clearly, primitive segments have only a disjoint or containment relationship with each other. And you find that **a continuous segment can be composed of several mutually disjoint primitive segments**. The largest primitive segment is the whole permutation itself, which contains all other primitive segments, so we consider that primitive segments can form a tree structure, which we call the **divide-combine tree**. More rigorously, the divide-combine tree of a permutation $P$ is composed of **all primitive segments** of the permutation $P$.

Having dryly stated so many definitions above, how can we do without a figure? Consider the permutation $P=\{9,1,10,3,2,5,7,6,8,4\}$. The divide-combine tree composed of its primitive segments is as follows:

![p1](./images/div-com1.png)

In the figure we did not mark the primitive segments. And **each node in the figure represents a primitive segment**. We only marked the value range of each primitive segment. For example, the primitive segment represented by node $[5,8]$ is $(P,[6,9])=\{5,7,6,8\}$. So here is a question: **what are divide nodes and combine nodes?**

### Divide nodes and combine nodes

Here we directly give the definitions and discuss their correctness later.

1.  **Value-range interval**: for a node $u$, use $[u_l,u_r]$ to denote the value-range interval of that node.
2.  **Child sequence**: for a node $u$ on the divide-combine tree, suppose its child nodes are an **ordered** sequence, whose elements are value-range intervals (a single number $x$ can be understood as the interval $[x,x]$). We call this sequence the child sequence, denoted $S_u$.
3.  **Child permutation**: for a child sequence $S_u$, the permutation formed after discretizing its elements into positive integers is called the child permutation. For example, for node $[5,8]$, its child sequence is $\{[5,5],[6,7],[8,8]\}$, so sorting the intervals and labeling them, its child permutation is $\{1,2,3\}$; similarly, the child permutation of node $[4,8]$ is $\{2,1\}$. The child permutation of node $u$ is denoted $P_u$.
4.  **Combine node**: we consider a node whose child permutation is in ascending or descending order to be a combine node. Formally, a node satisfying $P_u=\{1,2,\cdots,|S_u|\}$ or $P_u=\{|S_u|,|S_u-1|,\cdots,1\}$ is called a combine node. **A leaf node has no child permutation; we also consider it a combine node**.
5.  **Divide node**: one that is not a combine node is a divide node.

From the figure we can see that only $[1,10]$ is not a combine node, because the child permutation of $[1,10]$ is $\{3,1,4,2\}$.

### Properties of divide nodes and combine nodes

The naming of divide nodes and combine nodes comes from their properties. First we have a very obvious property: for any node $u$ in the divide-combine tree, the union of its child-sequence intervals is the value-range interval of node $u$. That is, $\bigcup_{i=1}^{|S_u|}S_u[i]=[u_l,u_r]$.

For a combine node $u$: any **subinterval** of its child sequence forms a **continuous segment**. Formally, $\forall S_u[l\sim r]$, $\bigcup_{i=l}^rS_u[i]\in I_P$.

For a divide node $u$: any subinterval of its child sequence of **length greater than 1 (the length here refers to the number of elements in the child sequence, not the length of the index interval)** does **not** form a **continuous segment**. Formally, $\forall S_u[l\sim r],l<r$, $\bigcup_{i=l}^rS_u[i]\notin I_P$.

The property of combine nodes is not hard to prove. Because the child permutation of a combine node is either in ascending or descending order, and the value-range intervals are also connected end-to-end, so any continuous subsequence (interval) is a continuous segment.

The property of divide nodes may be hard for many readers to understand: why does **any** subinterval of length greater than $1$ not form a continuous segment?

Use proof by contradiction. Suppose for a node $u$, there is a **longest** interval $S_u[l\sim r]$ in its child sequence that forms a continuous segment. Then this $A=\bigcup_{i=l}^rS_u[i]\in I_P$, which means $A$ is a primitive segment! (Because $A$ is the longest in the child sequence, no continuous segment can be found that intersects it without containing it.) So you did not use all primitive segments to compose this divide-combine tree. Contradiction.

### Construction of the divide-combine tree

For the specific construction of the divide-combine tree, LCA provides a linear construction algorithm[^ref1]; below we give a relatively understandable $O(n\log n)$ algorithm.

#### Incremental method

We consider the incremental method. Use a stack to maintain the divide-combine forest composed of the first $i-1$ elements. Here we need to **emphasize** that the divide-combine forest means that at any time, a node in the stack is either a divide node or a combine node. Now consider the current node $P_i$.

1.  We first determine whether it can become a child of the stack-top node; if it can, it becomes the child of the stack top, then take the stack top out as the current node. Repeat the above process until the stack is empty or it cannot become a child of the stack-top node.
2.  If it cannot become a child of the stack top, then see whether we can merge several consecutive nodes at the stack top into one node (the method for determining whether they can be merged is given later), and take the merged node as the current node.
3.  Repeat the above process until it can no longer be done. Then end this increment and directly push the current node onto the stack.

Next we explain this in detail.

#### The specific strategy

We consider that if the current point can become a child of the stack-top node, then the stack-top node is a combine node. If it is a divide node, then after merging, this divide node would have a child continuous segment, which does not satisfy the property of a divide node. Therefore it must be a combine node.

If it cannot become a child of the stack-top node, then we see whether several consecutive nodes at the stack top can be merged together with the current point. Let $l$ be the left endpoint of the interval the current point is in. We compute $L_i$ to denote, among the continuous segments whose right-endpoint index is $i$, the maximum left endpoint $< l$. The current node is $P_i$, and the stack-top node is denoted $t$.

1.  If $L_i$ does not exist, then clearly the current node cannot be merged;
2.  If $t_l=L_i$, then this is a merge of two nodes, and after merging it is a **combine node**;
3.  Otherwise there must exist in the stack a point $t'$ with left endpoint ${t'}_l=L_i$, then one can certainly merge from the current node to $t'$ to form a **divide node**;

#### Determining whether they can be merged

Finally, we consider how to handle $L_i$. In fact, a continuous segment $(P,[l,r])$ is equivalent to the interval range being equal to the interval length minus 1. That is,

$$
\max_{l\le i\le r}P_i-\min_{l\le i\le r}P_i=r-l
$$

And since P is a permutation, for any interval $[l,r]$,

$$
\max_{l\le i\le r}P_i-\min_{l\le i\le r}P_i\ge r-l
$$

So we maintain $\max_{l\le i\le r}P_i-\min_{l\le i\le r}P_i-(r-l)$, and then finding a continuous segment amounts to querying a minimum!

With the above idea, it is not hard to think of the following algorithm. For the current $i$ in the incremental process, we maintain an array $Q$ denoting the range minus length of the interval $[j,i]$. That is,

$$
Q_j=\max_{j\le k\le i}P_k-\min_{j\le k\le i}P_k-(i-j),\ \ 0<j<i
$$

Now we want to know whether there exists, among $1\sim i-1$, a smallest $j$ such that $Q_j=0$. This is equivalent to finding the minimum of $Q_{1\sim i-1}$. The smallest $j$ found is $L_i$. If there is none, then $L_i=i$.

But when the $i$-th increment ends, we need to quickly update the $Q$ array to the case of i+1. The original interval changes from $[j,i]$ to $[j,i+1]$; if $P_{i+1}>\max$ or $P_{i+1}<\min$, then $Q_j$ changes. How does it change? If $P_{i+1}>\max$, it amounts to first subtracting $\max$ from $Q_j$ and then adding $P_{i+1}$ to complete the update of $Q_j$; $P_{i+1}<\min$ is analogous, amounting to $Q_j=Q_j+\min-P_{i+1}$.

Then what if, for an interval $[x,y]$, the interval $\max$ of $P_{x\sim i},P_{x+1\sim i},P_{x+2\sim i},\cdots,P_{y\sim i}$ are all the same? You have already found that this amounts to doing an interval-add operation; similarly, when the interval $\min$ of $P_{x\sim i},P_{x+1\sim i},\cdots,P_{y\sim i}$ are all the same, it is also an interval-add operation. At the same time, the updates of $\max$ and $\min$ are mutually independent, so they can be updated separately.

Therefore our maintenance of $Q$ can be described as follows:

1.  Find the largest $j$ such that $P_{j}>P_{i+1}$; then clearly, the segment $P_{j+1\sim i}$ of numbers are all less than $P_{i+1}$, so we need to update the maximum of $Q_{j+1\sim i}$. Since $P_{i},\max(P_i,P_{i-1}),\max(P_i,P_{i-1},P_{i-2}),\cdots,\max(P_i,P_{i-1},\cdots,P_{j+1})$ are (non-strictly) monotonically increasing, we can do the same update for each segment with the same $\max$, i.e. an interval-add operation.
2.  Updating $\min$ is analogous.
3.  Subtract $1$ from each $Q_j$, because the interval length increases by $1$.
4.  Query $L_i$: i.e. query the **index** where the minimum of $Q$ is.

That's right, we can use a segment tree to maintain $Q$! Now there is still a problem: how to find a segment such that their $\max/\min$ are all the same? Use a monotonic stack to maintain it! Maintain two monotonic stacks representing $\max/\min$ respectively. Then clearly, the $\max/\min$ of the interval with two adjacent elements in the stack as endpoints are the same, so update the segment tree along the way while maintaining the monotonic stack.

See the code for the specific maintenance method.

Having talked so much dry theory, our friends are probably confused, so let's first show a figure. Long-image warning!

![p2](./images/div-com2.jpg)

### Implementation

Finally, we present an implementation code for reference. The code is reproduced from [Damibing's blog](https://www.cnblogs.com/Paul-Guderian/p/11020708.html), with some comments added.

```cpp
#include <algorithm>
#include <cstdio>
using namespace std;
constexpr int N = 200010;

int n, m, a[N], st1[N], st2[N], tp1, tp2, rt;
int L[N], R[N], M[N], id[N], cnt, typ[N], bin[20], st[N], tp;

// the original problem of this code should be CERC2017 Intrinsic Interval
// the a array is the permutation in the original problem
// st1 and st2 are two monotonic stacks; tp1, tp2 are their tops; rt is the root of the divide-combine tree
// the L, R arrays denote the left and right endpoints of the divide-combine-tree node; the role of the M array was mentioned in the tree construction
// id stores the node number corresponding to a certain position in the permutation; typ marks whether it is a divide node or combine node
// st stores the stack of divide-combine-tree node numbers; tp is its top
struct RMQ {  // preprocess RMQ (Max & Min)
  int lg[N], mn[N][17], mx[N][17];

  void chkmn(int& x, int y) {
    if (x > y) x = y;
  }

  void chkmx(int& x, int y) {
    if (x < y) x = y;
  }

  void build() {
    for (int i = bin[0] = 1; i < 20; ++i) bin[i] = bin[i - 1] << 1;
    for (int i = 2; i <= n; ++i) lg[i] = lg[i >> 1] + 1;
    for (int i = 1; i <= n; ++i) mn[i][0] = mx[i][0] = a[i];
    for (int i = 1; i < 17; ++i)
      for (int j = 1; j + bin[i] - 1 <= n; ++j)
        mn[j][i] = min(mn[j][i - 1], mn[j + bin[i - 1]][i - 1]),
        mx[j][i] = max(mx[j][i - 1], mx[j + bin[i - 1]][i - 1]);
  }

  int ask_mn(int l, int r) {
    int t = lg[r - l + 1];
    return min(mn[l][t], mn[r - bin[t] + 1][t]);
  }

  int ask_mx(int l, int r) {
    int t = lg[r - l + 1];
    return max(mx[l][t], mx[r - bin[t] + 1][t]);
  }
} D;

// maintain L_i

struct SEG {  // segment tree
#define ls (k << 1)
#define rs (k << 1 | 1)
  int mn[N << 1], ly[N << 1];  // interval add; interval minimum

  void pushup(int k) { mn[k] = min(mn[ls], mn[rs]); }

  void mfy(int k, int v) { mn[k] += v, ly[k] += v; }

  void pushdown(int k) {
    if (ly[k]) mfy(ls, ly[k]), mfy(rs, ly[k]), ly[k] = 0;
  }

  void update(int k, int l, int r, int x, int y, int v) {
    if (l == x && r == y) {
      mfy(k, v);
      return;
    }
    pushdown(k);
    int mid = (l + r) >> 1;
    if (y <= mid)
      update(ls, l, mid, x, y, v);
    else if (x > mid)
      update(rs, mid + 1, r, x, y, v);
    else
      update(ls, l, mid, x, mid, v), update(rs, mid + 1, r, mid + 1, y, v);
    pushup(k);
  }

  int query(int k, int l, int r) {  // query the position of 0
    if (l == r) return l;
    pushdown(k);
    int mid = (l + r) >> 1;
    if (!mn[ls])
      return query(ls, l, mid);
    else
      return query(rs, mid + 1, r);
    // if there is no position with 0, it automatically returns the position you are querying
  }
} T;

int o = 1, hd[N], dep[N], fa[N][18];

struct Edge {
  int v, nt;
} E[N << 1];

void add(int u, int v) {  // add an edge to the tree structure
  E[o] = Edge{v, hd[u]};
  hd[u] = o++;
}

void dfs(int u) {
  for (int i = 1; bin[i] <= dep[u]; ++i) fa[u][i] = fa[fa[u][i - 1]][i - 1];
  for (int i = hd[u]; i; i = E[i].nt) {
    int v = E[i].v;
    dep[v] = dep[u] + 1;
    fa[v][0] = u;
    dfs(v);
  }
}

int go(int u, int d) {
  for (int i = 0; i < 18 && d; ++i)
    if (bin[i] & d) d ^= bin[i], u = fa[u][i];
  return u;
}

int lca(int u, int v) {
  if (dep[u] < dep[v]) swap(u, v);
  u = go(u, dep[u] - dep[v]);
  if (u == v) return u;
  for (int i = 17; ~i; --i)
    if (fa[u][i] != fa[v][i]) u = fa[u][i], v = fa[v][i];
  return fa[u][0];
}

// determine whether the current interval is a continuous segment
bool judge(int l, int r) { return D.ask_mx(l, r) - D.ask_mn(l, r) == r - l; }

// build the tree
void build() {
  for (int i = 1; i <= n; ++i) {
    // monotonic stack
    // the minimum in the interval [st1[tp1-1]+1,st1[tp1]] is a[st1[tp1]]
    // now popping it means we need to add back the Min that was over-subtracted.
    // the leaf-node position j of the segment tree maintains
    // Max{j,i}-Min{j,i}-(i-j) from j to the current i
    // interval add is just a Tag.
    // the purpose of maintaining the monotonic stack is to assist the segment tree in updating from i-1 to i.
    // after updating to i, just querying the global minimum tells whether there is a solution

    while (tp1 && a[i] <= a[st1[tp1]])  // monotonically increasing stack, maintaining Min
      T.update(1, 1, n, st1[tp1 - 1] + 1, st1[tp1], a[st1[tp1]]), tp1--;
    while (tp2 && a[i] >= a[st2[tp2]])
      T.update(1, 1, n, st2[tp2 - 1] + 1, st2[tp2], -a[st2[tp2]]), tp2--;

    T.update(1, 1, n, st1[tp1] + 1, i, -a[i]);
    st1[++tp1] = i;
    T.update(1, 1, n, st2[tp2] + 1, i, a[i]);
    st2[++tp2] = i;

    id[i] = ++cnt;
    L[cnt] = R[cnt] = i;  // here L,R are the left and right endpoints of the interval corresponding to the node
    int le = T.query(1, 1, n), now = cnt;
    while (tp && L[st[tp]] >= le) {
      if (typ[st[tp]] && judge(M[st[tp]], i)) {
        // determine whether it can become a child; if it can, do it
        R[st[tp]] = i, M[st[tp]] = L[now], add(st[tp], now), now = st[tp--];
      } else if (judge(L[st[tp]], i)) {
        typ[++cnt] = 1;  // a combine node must be built this way
        L[cnt] = L[st[tp]], R[cnt] = i, M[cnt] = L[now];
        // here the M array records the left endpoint of the node's rightmost child, used for the above determination of whether it can become a child
        add(cnt, st[tp--]), add(cnt, now);
        now = cnt;
      } else {
        add(++cnt, now);  // create a new node and add now as a child
        // if a continuous segment cannot be formed starting from the current node, merge.
        // until a node is found that can form a continuous segment. And we can certainly find such
        // a node.
        do add(cnt, st[tp--]);
        while (tp && !judge(L[st[tp]], i));
        L[cnt] = L[st[tp]], R[cnt] = i, add(cnt, st[tp--]);
        now = cnt;
      }
    }
    st[++tp] = now;  // the increment ends, push the current point onto the stack

    T.update(1, 1, n, 1, i, -1);  // because the interval's right endpoint moves back one position, subtract 1 overall
  }

  rt = st[1];  // the last point remaining in the stack is the root node
}

// classify lca as divide or combine; here leaves are regarded as divide
void query(int l, int r) {
  int x = id[l], y = id[r];
  int z = lca(x, y);
  if (typ[z] & 1)
    l = L[go(x, dep[x] - dep[z] - 1)], r = R[go(y, dep[y] - dep[z] - 1)];
  // the reason for the special case here for a combine node is that this combine node is not necessarily the smallest continuous segment containing l, r.
  // because the subintervals of the interval represented by the combine node are all also continuous segments, and we only need one segment of them.
  else
    l = L[z], r = R[z];
  printf("%d %d\n", l, r);
}

int main() {
  scanf("%d", &n);
  for (int i = 1; i <= n; ++i) scanf("%d", &a[i]);
  D.build();
  build();
  dfs(rt);
  scanf("%d", &m);
  for (int i = 1; i <= m; ++i) {
    int x, y;
    scanf("%d%d", &x, &y);
    query(x, y);
  }
  return 0;
}

// 20190612
// divide-combine tree
```

## References and links

[Damibing's blog - 【Study Notes】Divide-Combine Tree](https://www.cnblogs.com/Paul-Guderian/p/11020708.html)

[^ref1]: Liu Cheng'ao. Simple Continuous-Segment Data Structures. WC2019 Camper Exchange.
