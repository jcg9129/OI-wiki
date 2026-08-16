A chordal graph is a special kind of graph; many NP-Hard problems on general graphs have excellent linear-time-complexity algorithms on chordal graphs.

## Some definitions and properties

**Subgraph**: a graph whose vertex set and edge set are both subsets of the original graph's vertex set and edge set.

**Induced subgraph**: a graph whose vertex set is a subset of the original graph's vertex set, and whose edge set is all edges satisfying **both endpoints being in the chosen vertex set**.

**Clique**: a complete subgraph.

**Maximal clique**: a clique that is not a subgraph of another clique.

**Maximum clique**: the clique with the most points.

**Clique number**: the number of points of the maximum clique, denoted $\omega(G)$.

**Minimum coloring**: coloring the points with the fewest colors such that the two points connected by every edge have different colors.

**Chromatic number**: the number of colors of the minimum coloring, denoted $\chi(G)$.

**Maximum independent set**: the largest point set such that any two points in the set have no edge directly connecting them. The size of this set is denoted $\alpha(G)$.

**Minimum clique cover**: covering all points with the fewest cliques. The number of cliques used is denoted $\kappa(G)$.

**Chord**: an edge connecting two non-adjacent points in a cycle.

**Chordal graph**: a graph where every cycle of length greater than $3$ has a chord is called a chordal graph.

**Lemma 1**: clique number $\omega(G)\le \chi(G)$ chromatic number

Proof: consider separately coloring the induced subgraph of the maximum clique; at least $\omega(G)$ colors are needed.

**Lemma 2**: maximum independent set number $\alpha(G)\le \kappa(G)$ minimum clique cover number

Proof: at most one point is chosen in each clique.

**Lemma 3**: any induced subgraph of a chordal graph must be a chordal graph.

Proof: if a chordal graph has an induced subgraph that is not a chordal graph, it means there exists a chordless cycle of length greater than $3$ on this induced subgraph; then no matter how the original graph is (however edges are added), the original graph will not be a chordal graph, a contradiction.

**Lemma 4**: any induced subgraph of a chordal graph cannot be a cycle with more than $3$ points.

Proof: a cycle with more than $3$ points is not a chordal graph; just use the above theorem.

## Determination of chordal graphs

### Problem description

Given an undirected graph, determine whether it is a chordal graph.

### Vertex cut set

For two points $u,v$ in a graph $G$, define the **vertex cut set** between these two points as a set satisfying that after deleting this set, the two points $u,v$ are disconnected. If any subset of a vertex cut set between $u,v$ is not a vertex cut set, then this vertex cut set is called a **minimal vertex cut set**.

**Lemma 5**: a minimal vertex cut set of the graph with respect to $u,v$ divides the original graph into several connected components; let the connected component containing $u$ be $V_1$ and the connected component containing $v$ be $V_2$; then for any point $a$ on the minimal vertex cut set, $N(a)$ must contain points in $V_1$ and $V_2$.

Proof: if $N(a)$ only contains points in at most one of the connected components $V_1$ or $V_2$, then deleting point $a$ from the vertex cut set is still disconnected, so the original vertex cut set is not a minimal vertex cut set.

**Lemma 6**: the induced subgraph of a minimal vertex cut set between any two points on a chordal graph must be a clique.

Proof: when the minimal vertex cut set size $\le 1$, the induced subgraph must be a clique.

Otherwise, suppose there are two points $x,y$ on the minimal vertex cut set; by **Lemma 5**, $N(x)$ has points in $V_1,V_2$, say $x_1,x_2$; likewise, say $y_1,y_2$; note that there may be $x_1=y_1,x_2=y_2$.

Since $V_1,V_2$ are both connected components, there exist shortest paths between the two point pairs $x_1,y_1$ and $x_2,y_2$. Let the shortest paths of $x,y$ inside $V_1,V_2$ be $x-x_1\sim y_1-y,x-x_2\sim y_2-y$; then there exists a cycle $x-x_1\sim y_1-y-y_2\sim x_2-x$ on the graph; the size of this cycle must be $\ge 4$; according to the definition of a chordal graph, at this point there must exist a chord on this cycle.

If this chord connects the two connected components $V_1,V_2$, then the point set is not a vertex cut set. If this chord connects two points inside a single connected component, or a point inside a connected component and a point on the vertex cut set, neither satisfies the shortest-path property. So this chord can only connect the two points $x,y$.

From this, it can be proved that the two points in each minimal vertex cut set in a chordal graph have edges directly connecting them, so the property is proved.

### Simplicial vertex

Let $N(x)$ denote the set of points adjacent to point $x$. If the induced subgraph of the point set $\{x\}+N(x)$ is a clique, then point $x$ is called a simplicial vertex.

**Lemma 7**: any chordal graph has at least one simplicial vertex, and a chordal graph that is not a complete graph has at least two non-adjacent simplicial vertices.

Proof: mathematical induction. Consider each connected component separately.

Induction base: when the graph is isomorphic to a complete graph, any point in the graph is a simplicial vertex. When the number of points of the graph $\le 3$, the lemma holds.

If the number of points on the graph $\ge 4$ and the graph is not a complete graph, we know there must exist $u,v$ such that $(u,v)\notin E$. Let $I$ be a minimal vertex cut set of the graph with respect to $u,v$. Let $A,B$ be the connected components where $u,v$ are located on the induced subgraph after deleting $I$ respectively. Due to the symmetry of the problem, we only consider the $A$ side; let $L=A+I$. If $L$ is a complete graph, then $u$ is a simplicial vertex; if not, because $L$ is an induced subgraph of the original graph, it must also be a chordal graph, so it has two non-adjacent simplicial vertices; because $I$ is a clique, its two points are both adjacent, so there must be a simplicial vertex in $A$. This simplicial vertex extended to the whole graph is also a simplicial vertex.

Since each time the whole graph is divided into several connected components for the proof, the size must decrease, and all satisfy the property, so the induction holds.

### Perfect elimination ordering

Let $n=|V|$; the perfect elimination ordering $v_1,v_2,\ldots ,v_n$ is a permutation of $1,2,\ldots ,n$ satisfying that $v_i$ is a simplicial vertex in the induced subgraph of $\{v_i,v_{i+1},\ldots ,v_n\}$.

**Lemma 8**: an undirected graph is a chordal graph if and only if it has a perfect elimination ordering.

Sufficiency: a chordal graph with $1$ point has a perfect elimination ordering. By **Lemma 3** and **Lemma 7**, the perfect elimination ordering of a chordal graph with $n$ points can be obtained by adding a simplicial vertex to the perfect elimination ordering of a chordal graph with $n-1$ points.

Necessity: suppose an undirected graph has a cycle with $>3$ nodes and has a perfect elimination ordering; let the first point on the cycle appearing in the perfect elimination ordering be $v$; suppose $v$ is connected to $v_1,v_2$ on the cycle; then by the property of the perfect elimination ordering, i.e. the definition of a simplicial vertex, $v_1,v_2$ have an edge directly connecting them, a contradiction.

### Naive algorithm

Each time find a **simplicial vertex** $v$, and add it to the perfect elimination ordering.

Delete point $v$ and its adjacent edges from the graph.

Repeat the above process; if all points are deleted, then the original graph is a chordal graph and a perfect elimination ordering is found; if there is no simplicial vertex in the graph, then the original graph is not a chordal graph.

Time complexity $O(n^4)$.

### MCS algorithm

**Maximum Cardinality Search** is a method that can find the perfect elimination ordering of an undirected graph in $O(n+m)$ time complexity.

Number the nodes in reverse order, i.e. label the points in the order from $n$ to $1$.

Let $label_x$ denote how many already-labeled points the $x$-th point is adjacent to; each time choose the unlabeled node with the largest $label$ value to label.

Use a linked list to maintain, for each $i$, the $x$ satisfying $label_x=i$.

Since the contribution of each edge to $\sum_{i=1}^n label_i$ is at most $2$, the time complexity is $O(n+m)$.

**Correctness proof**:

Let $\alpha(x)$ be the position of $x$ in this ordering.
We need to prove that for any chordal graph, the ordering found by the algorithm must be a perfect elimination ordering, i.e. all points located after a certain point in the ordering and connected to this point are pairwise connected.

**Lemma 9**: consider three points $u,v,w$ satisfying $\alpha(u)<\alpha(v)<\alpha(w)$; if $uw$ are connected and $vw$ are not connected, then $w$ only contributes to $u$'s $label$, not to $v$. To make $v$ enter the ordering before $u$, an $x$ is needed satisfying $\alpha(v)<\alpha(x)$ and $vx$ are connected and $ux$ are not connected, i.e. $x$ only contributes to $v$ and not to $u$.

**Lemma 10**: any chordal graph must not have a sequence $v_0,v_1,\dots,v_k(k\ge 2)$ satisfying the following properties:

1.  $v_iv_j$ are connected if and only if $|i-j|=1$.
2.  $\alpha(v_0)>\alpha(v_i)(i\in[1,k])$.
3.  There exists $i\in[1,k-1]$ satisfying $\alpha(v_i)<\alpha(v_{i+1})<\dots<\alpha(v_k)$ and $\alpha(v_i)<\alpha(v_{i-1})<\dots<\alpha(v_1)<\alpha(v_k)<\alpha(v_0)$.

Proof:

Since $\alpha(v_1)<\alpha(v_k)<\alpha(v_0)$, and $v_1v_0$ are connected and $v_kv_0$ are not connected, so by property one, there exists $x$ satisfying $\alpha(v_k)<\alpha(x)$ and $v_kx$ are connected and $v_1x$ are not connected.

Consider the smallest $j\in(1,k]$ satisfying $v_jx$ are connected; we can deduce $v_0x$ are not connected, otherwise $v_0v_1\cdots v_jx$ constitute a chordless cycle of length $\ge 4$.

If $x<v_0$, then $v_0,v_1,\dots,v_j,x$ is also a sequence satisfying the properties; if $v_0<x$ then $x,v_j,\dots,v_1,v_0$ is also a sequence satisfying the properties.

In the above derivation, we enlarged $\min(v_0,v_k)$, so continuing to deduce, a contradiction will surely be produced.

**Theorem 1**: for any chordal graph, the ordering found by the maximum cardinality search algorithm must be a perfect elimination ordering.

Proof: consider any three points $u,v,w$ satisfying $\alpha(u)<\alpha(v)<\alpha(w)$; we need to prove that if $uv$ are connected and $uw$ are connected, then $vw$ must be connected.

Consider proof by contradiction; suppose not connected, then $w,u,v$ is a sequence satisfying the properties in **Lemma 10**; we proved such a sequence does not exist, so it is a contradiction, and $vw$ are connected.

Reference code:

```cpp
while (cur) {
  p[cur] = h[nww];
  rnk[p[cur]] = cur;
  h[nww] = nxt[h[nww]];
  lst[h[nww]] = 0;
  lst[p[cur]] = nxt[p[cur]] = 0;
  tf[p[cur]] = true;
  for (vector<int>::iterator it = G[p[cur]].begin(); it != G[p[cur]].end();
       it++)
    if (!tf[*it]) {
      if (h[deg[*it]] == *it) h[deg[*it]] = nxt[*it];
      nxt[lst[*it]] = nxt[*it];
      lst[nxt[*it]] = lst[*it];
      lst[*it] = nxt[*it] = 0;
      deg[*it]++;
      nxt[*it] = h[deg[*it]];
      lst[h[deg[*it]]] = *it;
      h[deg[*it]] = *it;
    }
  cur--;
  if (h[nww + 1]) nww++;
  while (nww && !h[nww]) nww--;
}
```

If the original graph is a chordal graph at this point, then what is found is the perfect elimination ordering; but since the original graph may not be a chordal graph, what is found at this point is definitely not a perfect elimination ordering, so the problem is transformed into **judging whether the found ordering is a perfect elimination ordering of the original graph**.

### Judging whether a sequence is a perfect elimination ordering

#### Naive algorithm

According to the definition, judge in turn whether the points in $\{v_i,v_{i+1},\ldots ,v_n\}$ adjacent to $v_i$ on the perfect elimination ordering $v$ form a clique. Time complexity $O(nm)$.

#### Optimized algorithm

According to the definition of the perfect elimination ordering, let the points adjacent to $v_i$ in $\{v_i,v_{i+1},\ldots , v_n\}$, from small to large, be $\{v_{c_1},v_{c_2},\ldots ,v_{c_k} \}$; then we only need to judge whether $v_{c_1}$ is directly connected to the other points. Time complexity $O(n+m)$.

```cpp
jud = true;
for (int i = 1; i <= n; i++) {
  cur = 0;
  for (vector<int>::iterator it = G[p[i]].begin(); it != G[p[i]].end(); it++)
    if (rnk[p[i]] < rnk[*it]) {
      s[++cur] = *it;
      if (rnk[s[cur]] < rnk[s[1]]) swap(s[1], s[cur]);
    }
  for (int j = 2; j <= cur; j++)
    if (!st[s[1]].count(s[j])) {
      jud = false;
      break;
    }
}
if (!jud)
  printf("Imperfect\n");
else
  printf("Perfect\n");
```

At this point, the **chordal graph determination problem** can be solved in $O(n+m)$ time complexity.

## Maximal cliques of a chordal graph

Let $N(x)$ be the sequence of points that have an edge directly connecting to $x$ and are after $x$ on the perfect elimination ordering. Then a maximal clique of the chordal graph must be $\{x\}+N(x)$.

Proof: consider a maximal clique $V$ of the chordal graph, and the first point $x$ among its points appearing in the perfect elimination ordering; there must be $V\subseteq \{x\}+N(x)$, and because $V$ is a maximal clique, $V=\{x\}+N(x)$.

A chordal graph has at most $n$ maximal cliques. To find each maximal clique of the chordal graph, we can judge whether each $\{x\}+N(x)$ is a maximal clique.

Let $A=\{x\}+N(x),B=\{y\}+N(y)$; if $A\subsetneqq B$, then $A$ is not a maximal clique. At this point, on the perfect elimination ordering, obviously $y$ is before $x$.

Let $nxt_x$ denote the point in $N(x)$ that is earliest on the perfect elimination ordering, and $y*$ denote the latest point among all $y$ satisfying $A\subseteq B$. At this point there must be $nxt_{y*}=x$, otherwise $y*$ is not the latest, and letting $y*=nxt_{y*}$ still satisfies the condition.

$A\subsetneqq B$ if and only if $|A|+1\le |B|$.

The problem is transformed into judging whether there exists $y$ satisfying $nxt_y=x$ and $|N(x)|+1\le |N(y)|$. Time complexity $O(n+m)$.

```cpp
for (int i = 1; i <= n; i++) {
  cur = 0;
  for (vector<int>::iterator it = G[p[i]].begin(); it != G[p[i]].end(); it++)
    if (rnk[p[i]] < rnk[*it]) {
      s[++cur] = *it;
      if (rnk[s[cur]] < rnk[s[1]]) swap(s[1], s[cur]);
    }
  fst[p[i]] = s[1];
  N[p[i]] = cur;
}
for (int i = 1; i <= n; i++) {
  if (!vis[p[i]]) ans++;
  if (N[p[i]] >= N[fst[p[i]]] + 1) vis[fst[p[i]]] = true;
}
```

## Chromatic number of a chordal graph / clique number of a chordal graph

One construction method: color each point in turn from back to front along the perfect elimination ordering, coloring each point with the smallest color it can be colored. Time complexity $O(m+n)$.

Correctness proof: suppose the above method uses $t$ colors, then $t\ge \chi(G)$. Since each point on a clique has a different color, $t=\omega(G)$; by **Lemma 1**, $t=\omega(G)\le \chi(G)$. In summary, $t=\chi(G)=\omega(G)$.

When no coloring scheme is needed, and only the chromatic number / clique number of the chordal graph needs to be found, we can take the maximum value of $|\{x\}+N(x)|$.

```cpp
for (int i = 1; i <= n; i++) ans = max(ans, deg[i] + 1);
```

## Maximum independent set / minimum clique cover of a chordal graph

Maximum independent set: from front to back along the perfect elimination ordering, choose all points that have no edge directly connecting them to already-chosen points.

Minimum clique cover: let the maximum independent set be $\{v_1,v_2,\ldots ,v_t\}$; then the set of cliques $\{\{v_1+N(v_1)\},\{v_2+N(v_2)\},\ldots ,\{v_t+N(v_t)\} \}$ is the minimum clique cover of the graph. The time complexity of both is $O(n+m)$.

Correctness proof: suppose the independent set number and clique cover number of the above scheme are both $t$; by the definition, $t\le \alpha(G),t\ge \kappa(G)$; by **Lemma 2**, $\alpha(G)\le \kappa(G)$, so $t=\alpha(G)=\kappa(G)$.

```cpp
for (int i = 1; i <= n; i++)
  if (!vis[p[i]]) {
    ans++;
    for (vector<int>::iterator it = G[p[i]].begin(); it != G[p[i]].end(); it++)
      vis[*it] = true;
  }
```

## Exercises

[SPOJ FISHNET - Fishing Net](https://www.spoj.com/problems/FISHNET)

[P3196 \[HNOI2008\] Magical Kingdom](https://www.luogu.com.cn/problem/P3196)

[P3852 \[TJOI2007\] Kids](https://www.luogu.com.cn/problem/P3852)

## References

[Chordal-graph related](https://yhx-12243.github.io/OI-transit/memos/15.html)

[2009 WC lecture notes](https://github.com/hzwer/shareOI/blob/master/%E5%9B%BE%E8%AE%BA/%E5%BC%A6%E5%9B%BE%E4%B8%8E%E5%8C%BA%E9%97%B4%E5%9B%BE_%E9%99%88%E4%B8%B9%E7%90%A6.pptx)

[Chordal graph summary - Zusuyu](https://www.cnblogs.com/zhoushuyu/p/8716935.html)

[R. E. Tarjan and M. Yannakakis, Simple linear-time algorithms to test chordality of graphs, test acyclicity of hypergraphs, and selectively reduce acyclic hypergraphs, SIAM J. Comput., 13 (1984), pp. 566–579.](https://dl.acm.org/doi/abs/10.1137/0213035)
