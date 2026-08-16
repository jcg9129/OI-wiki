## Preface

In 1959, the concept of "domination" was proposed by Reese T. Prosser in [a paper on network flow](http://portal.acm.org/ft_gateway.cfm?id=1460314&type=pdf&coll=GUIDE&dl=GUIDE&CFID=79528182&CFTOKEN=33765747), but no specific solving algorithm was proposed; it was not until 1969 that Edward S. Lowry and C. W. Medlock first proposed an [efficient solving algorithm](http://portal.acm.org/ft_gateway.cfm?id=362838&type=pdf&coll=GUIDE&dl=GUIDE&CFID=79528182&CFTOKEN=33765747). And the currently most widely-used Lengauer–Tarjan algorithm was proposed by Lengauer and Tarjan in 1979 in [a paper](https://www.cs.princeton.edu/courses/archive/fall03/cs528/handouts/a%20fast%20algorithm%20for%20finding.pdf).

In the OI community, the concept of the dominator tree was first introduced in [ZJOI2012 Disaster](https://www.luogu.com.cn/problem/P2597), and at that time it was also called the "extinction tree"; Chen Sunli also introduced this algorithm in his 2020 National Training Team paper.

Currently the dominator tree is not popular in the competition community, and its related exercises are not commonly seen; but the dominator tree has already been widely applied in industry, especially in the compiler-related field.

This article will introduce the concept of the dominator tree and several solving methods.

## Domination relation

We designate an entry node $s$ on an arbitrary directed graph; for a node $u$, if every path from $s$ to $u$ passes through some node $v$, then we say $v$ **dominates** $u$, and also say $v$ is a **dominator** of $u$, denoted $v\ dom\ u$.

For nodes unreachable from $s$, discussing their domination relation is meaningless, so unless otherwise specified, this article assumes by default that $s$ can reach any node on the graph.

![](images/dom-tree1.png)

For example, in this directed graph, $2$ is dominated by $1$, $3$ is dominated by $1, 2$, 4 is dominated by $1, 2, 3$, 5 is dominated by $1, 2$, etc.

### Lemmas

In the lemmas below, $u, v, w\ne s$ by default.

**Lemma 1:** $s$ is a dominator of all its nodes; any node is a dominator of itself.

**Proof:** Obviously any path from $s$ to $u$ must pass through both nodes $s$ and $u$.

**Lemma 2:** The domination relation derived considering only simple paths is the same as the relation derived considering all paths.

**Proof:** For a non-simple path, let the point set of all nodes passed between two passes of some node be $S$; if the nodes in $S$ are deleted, then each non-simple path can be corresponded to a simple path.

In $S$, points that are on the non-simple path but not on the simple path cannot possibly be dominators, because there is at least one simple path from $s$ to $u$ not including this point; and points on both the simple path and the non-simple path only need to be discussed on the simple path.

In summary, deleting non-simple paths has no effect on the domination relation.

**Lemma 3:** If $u$ $dom$ $v$ and $v$ $dom$ $w$, then $u$ $dom$ $w$.

**Proof:** A path passing through $w$ must pass through $v$, and a path passing through $v$ must pass through $u$, so a path passing through $w$ must pass through $u$, i.e. $u \ dom \ w$.

**Lemma 4:** If $u \ dom \ v$ and $v \ dom\ u$, then $u=v$.

**Proof:** Suppose $u \ne v$; then any path reaching $v$ has already reached $u$, and at the same time any path reaching $u$ has already reached $v$, a contradiction.

**Lemma 5:** If $u \ne v \ne w$, $u \ dom \ w$ and $v \ dom \ w$, then $u \ dom \ v$ or $v \ dom \ u$.

**Proof:** Consider a path $s \rightarrow \dots \rightarrow u \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow w$; if there is no domination relation between $u$, $v$, then there must exist a path from $s$ to $v$ not passing through $u$, i.e. there exists a path $s \rightarrow \dots \rightarrow v \rightarrow \dots \rightarrow w$, contradicting $u\ dom\ w$.

### Solving the domination relation

#### Node-deletion method

A conclusion equivalent to the definition: if after deleting a certain node in the graph some nodes become unreachable, then this deleted node dominates these nodes that became unreachable.

Therefore we only need to try deleting each node and then dfs; the code complexity is $O(n^3)$. The core code is given below.

```cpp
// suppose there are n nodes in the graph, start point s = 1
std::bitset<N> vis;
std::vector<int> edge[N];
std::vector<int> dom[N];

void dfs(int u, int del) {
  vis[u] = true;
  for (int v : edge[u]) {
    if (v == del or vis[v]) {
      continue;
    }
    dfs(v, del);
  }
}

void getdom() {
  for (int i = 2; i <= n; ++i) {
    vis.reset();
    dfs(1, i);
    for (int j = 1; j <= n; ++j) {
      if (!vis[j]) {
        dom[j].push_back(i);
      }
    }
  }
}
```

#### Data-flow iteration method

The data-flow iteration method is also a knowledge point uncommon in OI; here we first make a brief introduction.

Data-flow analysis is a concept in compiler theory, used to analyze how data flows along the execution paths of a program; and the data-flow iteration method is a method that lists equations on the nodes of the program's flow graph and continually iterates to solve, thereby obtaining the data-flow values at certain points of the program. Here we regard the directed graph as a program flow graph.

In this problem, the equation is:

$$
dom(u)=\{u\} \cup \left(\bigcap_{v\in pre(u)}{dom(v)}\right)
$$

where $pre(u)$ is defined as the point set composed of the predecessor nodes of $u$. This equation can be obtained by Lemma 3.

Translated into plain language, the dominator set of a point is the intersection of the dominator sets of all its predecessor nodes, unioned with itself. According to this equation, continually iterate the dominator set on each node until the answer does not change.

To improve efficiency, we hope that in each round of iteration, all predecessor nodes of the currently-iterated node have finished this iteration as much as possible, so we use depth-first ordering to derive the reverse post-order of this graph, and iterate according to this order.

Below is a reference implementation of the core code. Here we need to preprocess the predecessor node set of each point and the reverse post-order of the graph, but this is not the main content discussed in this article, so a reference implementation is not provided here.

```cpp
std::vector<int> pre[N];  // the predecessor nodes of each node
std::vector<int> ord;     // the reverse post-order of the graph
std::bitset<N> dom[N];
std::vector<int> Dom[N];

void getdom() {
  dom[1][1] = true;
  flag = true;
  while (flag) {
    flag = false;
    for (int u : ord) {
      std::bitset<N> tmp;
      tmp[u] = true;
      for (int v : pre[u]) {
        tmp &= dom[v];
      }
      if (tmp != dom[u]) {
        dom[u] = tmp;
        flag = true;
      }
    }
  }
  for (int i = 2; i <= n; ++i) {
    for (int j = 1; j <= n; ++j) {
      if (dom[i][j]) {
        Dom[i].push_back(j);
      }
    }
  }
}
```

It is not hard to see that the complexity of the above algorithm is $O(n^2)$.

## Dominator tree

In the previous section we found that, except for $s$, a point has at least two dominators, $s$ and itself.

Among the dominators of any node $u$, we call the node $v$ closest to itself other than itself the immediate dominator of $u$, denoted $idom(u) = v$. Obviously, except that $s$ has no immediate dominator, each node has a unique immediate dominator.

We consider, for each node $u$ except $s$, connecting an edge from $idom(u)$ to $u$, which constitutes a directed graph with $n$ nodes and $n - 1$ edges. According to Lemma 3 and Lemma 4, we know that the domination relation must not constitute a loop, i.e. these edges must not constitute a cycle, so the graph we obtain is in fact a tree. We call this tree the **dominator tree** of the original graph.

## Solving the dominator tree

### Solving based on dom

Consider the dominator set $\{s_1, s_2, \dots, s_k\}$ of some node; then there must exist a path $s \rightarrow \dots \rightarrow s_1 \rightarrow \dots \rightarrow s_2 \rightarrow \dots \rightarrow \dots \rightarrow s_k \rightarrow\dots \rightarrow u$. Obviously the immediate dominator of $u$ is $s_k$. Therefore the definition of the immediate dominator is equivalent to:

For the dominator set $S$ of a node $u$, if $v \in S$ satisfies $\forall w \in S\setminus\{u,v\}, w\ dom \ v$, then $idom(u)=v$.

Therefore, after using the algorithm described above to obtain the dominator set of each node, according to the above definition we can very easily obtain the immediate dominator of each point, thereby constructing the dominator tree. The reference code is given below.

```cpp
std::bitset<N> dom[N];
std::vector<int> Dom[N];
int idom[N];

void getidom() {
  for (int u = 2; u <= n; ++u) {
    for (int v : Dom[u]) {
      std::bitset<N> tmp = (dom[v] & dom[u]) ^ dom[u];
      if (tmp.count() == 1 and tmp[u]) {
        idom[u] = v;
        break;
      }
    }
  }
  for (int u = 2; u <= n; ++u) {
    e[idom[u]].push_back(u);
  }
}
```

### Special case on a tree

Obviously the dominator tree of a tree-shaped graph is itself.

### Special case on a DAG

We find that a DAG has a very good property: solving according to the topological order, the earlier-obtained solutions will not affect the subsequent solutions. We can use this feature to quickly find the dominator tree of a DAG.

???+ warning "Reminder"
    It is worth noting that the DAG here can only have one start point; if there are multiple start points, the points dominated by the start points will have multiple parents on the dominator tree, so that the domination relation cannot be simply expressed with a dominator tree.

**Lemma 6:** On a directed graph, $v\ dom\ u$ if and only if $\forall w \in pre(u), v\ dom \ w$.

**Proof:** First let's prove sufficiency. Consider that any path from $s$ to $u$ must pass through a node $w \in pre(u)$, and $v$ dominates this node, so any path from $s$ to $u$ must pass through $v$, so we obtain $v \ dom \ u$.

Then necessity. If $\exists w\in pre(u)$ such that $v$ does not dominate $w$, then there must be a path $s \rightarrow \cdots \rightarrow w \rightarrow \cdots \rightarrow u$ not passing through $v$, so $v$ does not dominate $u$.

We find that the dominator of $u$ must be a common ancestor of all its predecessor nodes on the dominator tree, so obviously the immediate dominator of $u$ is the LCA of all predecessor nodes on the dominator tree. Considering binary-lifting to solve the LCA, which can support adding a node each time, the above algorithm is obviously feasible.

Below is a reference implementation:

```cpp
std::stack<int> sta;
std::vector<int> e[N], g[N], tree[N];  // g is the reverse graph of the original graph, tree is the dominator tree
int n, s, in[N], tpn[N], dep[N], idom[N];  // n is the total number of points, s is the start point, in is the in-degree
int fth[N][17];

void topo(int s) {
  sta.push(s);
  while (!sta.empty()) {
    int u = sta.top();
    sta.pop();
    tpn[++tot] = u;
    for (int v : e[u]) {
      --in[v];
      if (!in[v]) {
        sta.push(v);
      }
    }
  }
}

int lca(int u, int v) {
  if (dep[u] < dep[v]) {
    std::swap(u, v);
  }
  for (int i = 15; i >= 0; --i) {
    if (dep[fth[u][i]] >= dep[v]) {
      u = fth[u][i];
    }
  }
  if (u == v) {
    return u;
  }
  for (int i = 15; i >= 0; --i) {
    if (fth[u][i] != fth[v][i]) {
      u = fth[u][i];
      v = fth[v][i];
    }
  }
  return fth[u][0];
}

void build() {
  topo(s);
  for (int i = 1; i <= n; ++i)
    for (int j = 0; j <= 15; ++j) fth[i][j] = s;
  for (int i = 1; i <= n; ++i) {
    int u = tpn[i];
    if (g[u].size()) {
      int v = g[u][0];
      for (int j = 1, q = g[u].size(); j < q; ++j) {
        v = lca(v, g[u][j]);
      }
      tree[v].push_back(u);
      fth[u][0] = v;
      dep[u] = dep[v] + 1;
      for (int i = 1; i <= 15; ++i) {
        fth[u][i] = fth[fth[u][i - 1]][i - 1];
      }
    }
  }
}

```

### Lengauer–Tarjan algorithm

The Lengauer–Tarjan algorithm is one of the most famous algorithms for solving the dominator tree; it can find the dominator tree of a directed graph in $O(n\alpha(n, m))$ time complexity. This algorithm introduces the concept of the **semi-dominator**, and uses the semi-dominator to help find the immediate dominator.

#### Conventions

First, we perform dfs on this directed graph starting from $s$; the points and edges passed form a tree $T$. We call the traversed edges tree edges, and the rest non-tree edges; let $dfn(u)$ denote the ordinal at which node $u$ is traversed; define $u<v$ if and only if $dfn(u) < dfn(v)$.

#### Semi-dominator

The semi-dominator of a node $u$ is the smallest one among the nodes $v$ satisfying that there is a path starting from this node $v$ where every node on the path except $u, v$ is greater than $u$. Formally, the semi-dominator $sdom(u)$ of $u$ is defined as:

$sdom(u) = \min(v|\exists v=v_0 \rightarrow v_1 \rightarrow\dots \rightarrow v_k = u, \forall 1\le i\le k - 1, v_i > u)$

We find that the semi-dominator has some useful properties:

**Lemma 7:** For any node $u$, $sdom(u) < u$.

**Proof:** By the definition, it is not hard to find that the parent $fa(u)$ of $u$ on $T$ also satisfies the condition of being a semi-dominator, and $fa(u) < u$, so any node greater than $u$ cannot possibly be its semi-dominator.

**Lemma 8:** For any node $u$, $idom(u)$ is its ancestor on $T$.

**Proof:** The path from $s$ to $u$ on $T$ corresponds to a path on the original graph, so $idom(u)$ must be on this path.

**Lemma 9:** For any node $u$, $sdom(u)$ is its ancestor on $T$.

**Proof:** Suppose $sdom(u)$ is not an ancestor of $u$; then $sdom(u)$ cannot possibly connect to any node with $\mathrm{dfs}$ order greater than or equal to $u$ (otherwise this point should be in the subtree of $sdom(u)$ rather than another subtree), a contradiction.

**Lemma 10:** For any node $u$, $idom(u)$ is an ancestor of $sdom(u)$.

**Proof:** Consider that we can go from $s$ to $sdom(u)$ and then walk to $u$ via the path in the definition. By the definition, the points on the path from $sdom(u)$ to $u$ do not dominate $u$, so $idom(u)$ must be an ancestor of $sdom(u)$.

**Lemma 11:** For any nodes $u \ne v$ satisfying that $v$ is an ancestor of $u$, then either $v$ is an ancestor of $idom(u)$, or $idom(u)$ is an ancestor of $idom(v)$.

**Proof:** For any node $w$ between $v$ and $idom(v)$, according to the definition of the immediate dominator, there must exist a path from $s$ to $idom(v)$ and then to $v$ not passing through $w$. Therefore these nodes $w$ must not be $idom(u)$, so $idom(u)$ is either a descendant of $v$ or an ancestor of $idom(v)$.

According to the above lemmas, we can obtain the following theorem:

**Theorem 1:** The semi-dominator of a point $u$ is the smallest node among the semi-dominators of its predecessors and of all ancestors of its dominators on $T$ that are greater than $u$. Formally, $sdom(u)=\min(\{v|\exists v \rightarrow u, v < u \} \cup \{sdom(w) | w > u\ and\ \exists w \rightarrow \dots \rightarrow v \rightarrow u \})$.

**Proof:** Let $x$ equal the right side of the above expression.

We first prove $sdom(u) \le x$. According to Lemma 7 we know this proposition is equivalent to proving that both of the above satisfy the condition of being a semi-dominator. The case where $x$ is a predecessor of $u$ is obvious; for the latter part, we consider concatenating the path $x=v_0\rightarrow\dots\rightarrow v_j=w$ described in the definition of the semi-dominator, a path $w=v_j \rightarrow\dots\rightarrow v_k=v$ on $T$ satisfying $\forall i\in[j, k-1], v_i\ge w > u$, and the path $v \rightarrow u$, thereby constructing a path satisfying the definition of the semi-dominator.

Then we prove $sdom(u)\ge x$. Consider the path $sdom(u)=v_0\rightarrow v_1 \rightarrow\dots\rightarrow v_k=u$ described in the definition from $u$ to its semi-dominator. It is not hard to see that $k=1$ and $k > 1$ correspond to the two selection methods in the definition respectively. If $k = 1$, then there exists a directed edge $sdom(u) \rightarrow u$, and it is proved by Lemma 7; if $k>1$, let $j$ be the smallest number satisfying $j \ge 1$ and $v_j$ is an ancestor of $v_{k-1}$ on $T$. Considering that $k$ satisfies the above condition, such a $j$ must exist.

Consider proving that $v_0 \rightarrow \dots \rightarrow v_j$ is a path satisfying the condition of being a semi-dominator of $v_j$, i.e. proving $\forall i \in [1, j), v_i>v_j$. If not, then let $i$ be the number making $v_i$ smallest among those satisfying $v_i < v_j$; according to Lemma 11 we know $v_i$ is an ancestor of $v_j$, which contradicts the definition of $j$. So $sdom(v_j)\le sdom(u)$. In summary $sdom(u) \le x$, so $x=sdom(u)$.

According to Theorem 1 we can find the semi-dominator of each point. It is not hard to find that the complexity bottleneck of computing the semi-dominator is in the second case; we consider using a weighted DSU for optimization, updating the minimum value each time during path compression.

```cpp
void dfs(int u) {
  dfn[u] = ++dfc;
  pos[dfc] = u;
  for (int i = h[0][u]; i; i = e[i].x) {
    int v = e[i].v;
    if (!dfn[v]) {
      dfs(v);
      fth[v] = u;
    }
  }
}

int find(int x) {
  if (fa[x] == x) {
    return x;
  }
  int tmp = fa[x];
  fa[x] = find(fa[x]);
  if (dfn[sdm[mn[tmp]]] < dfn[sdm[mn[x]]]) {
    mn[x] = mn[tmp];
  }
  return fa[x];
}

void getsdom() {
  dfs(1);
  for (int i = 1; i <= n; ++i) {
    mn[i] = fa[i] = sdm[i] = i;
  }
  for (int i = dfc; i >= 2; --i) {
    int u = pos[i], res = INF;
    for (int j = h[1][u]; j; j = e[j].x) {
      int v = e[j].v;
      if (!dfn[v]) {
        continue;
      }
      find(v);
      if (dfn[v] < dfn[u]) {
        res = std::min(res, dfn[v]);
      } else {
        res = std::min(res, dfn[sdm[mn[v]]]);
      }
    }
    sdm[u] = pos[res];
    fa[u] = fth[u];
  }
}

```

#### Solving the immediate dominator

##### Converting to a DAG

But I still don't know what the semi-dominator is useful for!

We consider adding, for each $u$, a directed edge $sdom(u) \rightarrow u$ on $T$. According to Lemma 9, this newly-obtained graph $G$ must be a directed acyclic graph; and according to Lemma 10, we also find that adding edges this way will not change the domination relation, so we have converted the original graph into a DAG, and just solve it using the algorithm above.

##### Solving via the semi-dominator

Building a bunch of graphs is too inelegant!

**Theorem 2:** For any node $u$, if any node $v$ on the path from $sdom(u)$ to $w$ on $T$ satisfies $sdom(v)\ge sdom(w)$, then $idom(u) =sdom(u)$.

**Proof:** According to Lemma 10 we know $idom(u)$ is $sdom(u)$ or its ancestor, so we only need to prove $sdom(u) \ dom \ u$.

Consider any path $P$ from $s$ to $u$; we need to prove that $sdom(u)$ must be in $P$. Let $v$ be the last node in $P$ satisfying $v<sdom(u)$. If $v$ does not exist then it must be that $sdom(u)=idom(u) =s$, otherwise let $w$ be the first point in $P$ after $v$ on the path from $sdom(u)$ to $u$ in the DFS tree.

We next prove $sdom(w)\le v <sdom(v)$. Consider the path $v = v_0 \rightarrow \dots v_k = w$ from $v$ to $w$ on $T$; if it does not hold, then there exists $i\in[1, k- 1], v_i < w$. At this point there must exist some $j\in [i, k - 1]$ satisfying that $v_j$ is an ancestor of $w$. From the value of $v$ we know $sdom(u)\le v_j$, so $v_j$ is also on the path from $sdom(u)$ to $u$ in the DFS tree, contradicting the definition of $w$, so $sdom(w)\le v < sdom(v)$; combined with the condition of the theorem, we have $y=sdom(u)$, i.e. the path $P$ contains $sdom(u)$.

**Theorem 3:** For any node $u$, the node $v$ with the smallest semi-dominator among all nodes on the path from $sdom(u)$ to $u$ on $T$ must satisfy $sdom(v)\le sdom(u)$ and $idom(v) = idom(u)$.

**Proof:** Considering that $u$ itself also satisfies the condition of $v$, so $sdom(v)\le sdom(u)$.

Since $idom(u)$ is an ancestor of $v$ on $T$, by Lemma 11 we know $idom(u)$ is also an ancestor of $idom(v)$, so we only need to prove that $idom(v)$ dominates $u$.

Consider any path $P$ from $s$ to $u$; we need to prove that $sdom(u)$ must be in $P$. Let $x$ be the last node in $P$ satisfying $x<sdom(u)$. If $x$ does not exist then it must be that $sdom(u)=idom(u) =s$, otherwise let $y$ be the first point in $P$ after $x$ on the path from $sdom(u)$ to $u$ in the DFS tree.

Similar to the proof process of Theorem 2, we can obtain $sdom(y) \le x$. According to Lemma 10, $sdom(y)\le x<idom(v) \le sdom(v)$. At this point, from the definition of $v$ we know $y$ cannot be a descendant of $sdom(u)$; on the other hand, $y$ cannot be both a descendant of $idom(v)$ and an ancestor of $v$, otherwise the path going along the DFS tree from $s$ to $sdom(y)$, then along $P$ to $y$, and finally along the DFS tree to $v$ does not pass through $idom(v)$, contradicting the definition of the dominator. Therefore $y=idom(v)$, i.e. $P$ contains $idom(v)$.

According to the above two theorems we can obtain the relationship between $sdom(u)$ and $idom(u)$.

Let $v$ be the node with the smallest $sdom(v)$ among all nodes that are between $sdom(u)$ and $u$; then:

$$
idom(u) =
\left\{ 
\begin{aligned} 
& sdom(u), &\text{if}\ sdom(u) = sdom(v)
\\
&idom(v), &\text{otherwise}
\end{aligned}
\right.
$$

We only need to slightly modify the code for solving the semi-dominator above.

```cpp
struct E {
  int v, x;
} e[MAX * 4];

int h[3][MAX * 2];

int dfc, tot, n, m, u, v;
int fa[MAX], fth[MAX], pos[MAX], mn[MAX], idm[MAX], sdm[MAX], dfn[MAX],
    ans[MAX];

void add(int x, int u, int v) {
  e[++tot] = {v, h[x][u]};
  h[x][u] = tot;
}

void dfs(int u) {
  dfn[u] = ++dfc;
  pos[dfc] = u;
  for (int i = h[0][u]; i; i = e[i].x) {
    int v = e[i].v;
    if (!dfn[v]) {
      dfs(v);
      fth[v] = u;
    }
  }
}

int find(int x) {
  if (fa[x] == x) {
    return x;
  }
  int tmp = fa[x];
  fa[x] = find(fa[x]);
  if (dfn[sdm[mn[tmp]]] < dfn[sdm[mn[x]]]) {
    mn[x] = mn[tmp];
  }
  return fa[x];
}

void tar(int st) {
  dfs(st);
  for (int i = 1; i <= n; ++i) {
    fa[i] = sdm[i] = mn[i] = i;
  }
  for (int i = dfc; i >= 2; --i) {
    int u = pos[i], res = INF;
    for (int j = h[1][u]; j; j = e[j].x) {
      int v = e[j].v;
      if (!dfn[v]) {
        continue;
      }
      find(v);
      if (dfn[v] < dfn[u]) {
        res = std::min(res, dfn[v]);
      } else {
        res = std::min(res, dfn[sdm[mn[v]]]);
      }
    }
    sdm[u] = pos[res];
    fa[u] = fth[u];
    add(2, sdm[u], u);
    u = fth[u];
    for (int j = h[2][u]; j; j = e[j].x) {
      int v = e[j].v;
      find(v);
      if (sdm[mn[v]] == u) {
        idm[v] = u;
      } else {
        idm[v] = mn[v];
      }
    }
    h[2][u] = 0;
  }
  for (int i = 2; i <= dfc; ++i) {
    int u = pos[i];
    if (idm[u] != sdm[u]) {
      idm[u] = idm[idm[u]];
    }
  }
}

```

## Example problems

### [Luogu P5180 【Template】Dominator Tree](https://www.luogu.com.cn/problem/P5180)

One can just solve the domination relation, recording during the solving process how many nodes each point dominates, or one can build the dominator tree to solve the size of each node.

Here we give the code for the latter solution.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/dom-tree/dom-tree_1.cpp"
    ```

### [ZJOI2012 Disaster](https://www.luogu.com.cn/problem/P2597)

Just find the dominator tree on the DAG and then find the node size.

??? note "Reference code"
    ```cpp
    --8<-- "docs/graph/code/dom-tree/dom-tree_2.cpp"
    ```
