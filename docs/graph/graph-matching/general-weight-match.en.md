author: accelsao, Henry-ZHR, yuhuoji

This page goes from general graph maximum-weight perfect matching to general graph maximum-weight matching (maximum-weight matching can become maximum-weight perfect matching by adding zero edges).

## Preliminary knowledge

### Blossom

The difference between general graph matching and bipartite matching is that the graph may have odd cycles. Even cycles can be regarded as bipartite graphs.

The way the Blossom Algorithm handles this is that when it encounters an odd cycle, it contracts it into a **Blossom**, and sets all the points in the blossom as even points. Since the points on the blossom can all become even points, we can directly contract the whole blossom into an even point. Note that a blossom can contain other blossoms.

This can also become a linear programming and dual problem, but the blossom needs some processing.

### Vertex labeling and Equality Edge

Define $z_u$ as the vertex labeling of point $u$, with the same meaning as the vertex label defined in the $KM$ algorithm. Define an edge $e(u,v)$ as an "equality edge" if and only if the sum of the labels of point $u$ and point $v$ equals the weight of edge $e$ ($z_u + z_v = w(e)$); at this point the edge label $z_e = z_u + z_v − w(e) = 0$.

## Linear programming of general graph maximum-weight perfect matching

### Definition

Because a blossom has at least three points, after contraction it becomes a single point. Let $O$ be the set of sets of odd size $≥3$ (containing all blossoms), and $\gamma(S)$ denote the edges within set $S$.

$$
\begin{aligned}
& \text{Let } S\subseteq V \\
& \gamma(S)=\{(u,v)\in E:u\in S,v\in S\} \\
& O=\{B\subseteq V:|B|\text{ is odd and }|B|\geq3\} \\
\end{aligned}
$$

### Dual problem

???+ note "Primal problem"
    $$
    \begin{aligned}
    & \max\sum_{e\in E}w(e)x_e \\
    & \text{constraints:} \\
    & x(\delta(u))=1:\forall u\in V \\
    & x(\gamma(B))\leq\lfloor\frac{|B|}{2}\rfloor:\forall B\in O \\
    & x_e\geq0:\forall e\in E \\
    \end{aligned}
    $$

Then convert the problem into a dual problem through Primal-Dual.

???+ note "Dual problem"
    $$
    \begin{aligned}
    & \min\sum_{u\in V}z_u+\sum_{B\in O}\left\lfloor\frac{|B|}{2}\right\rfloor z_B \\
    & \text{constraints:} \\
    & z_B\geq0:\forall B\in O \\
    & z_e\geq0:\forall e\in E \\
    & \text{Let } e=(u,v), \text{ here} \\
    & \begin{array}{lll}
    z_e & = & z_u + z_v - w(e) + \sum_{\substack{B \in O \\ u,v \in \gamma(B)}} z_B
    \end{array}
    \end{aligned}
    $$

Edges with $x_e=1$ are matching edges, and edges with $x_e=0$ are non-matching edges. Same as a bipartite graph, we must satisfy $x_e\in\{0,1\}:\forall e\in E$. Therefore, at the maximum-weight perfect matching, all matching edges must be **equality edges**.

Different from a bipartite graph, a general graph has an additional $z_B$ to handle. Below we consider when $z_B$ is greater than $0$.

We can see that making $z_B=0$ as much as possible is the best practice, but when unavoidable we still have to let $z_B>0$. When $x(\gamma(B)) = \left\lfloor \dfrac{|B|}2 \right\rfloor \text{ and } x(\delta(B)) = 1$, just let $z_B>0$. Because except in this case, $z_B>0$ is meaningless.

According to the complementary slackness conditions, there is the following correspondence:

-   For a chosen edge $e$, we must have $z_e=0$.

    $$
    x_e>0 \longrightarrow z_e=0,\quad \forall e\in E
    $$

-   For a chosen set $B$, $z_B>0 \longrightarrow x(\gamma(B))= \left\lfloor \dfrac{|B|}2 \right\rfloor$, i.e. all sets $B$ with $z_B>0$ have half of the set size in edges chosen, i.e. the set $B$ is a blossom, and one edge in the blossom is chosen for augmentation. At the same time, we add a condition: $x(\delta(B))=1$, i.e. only when the blossom $B$ connects one edge outward is $z_B>0$ meaningful.

    $$
    z_B>0 \longrightarrow x(\gamma(B))=\left\lfloor\frac{|B|}2\right\rfloor, x(\delta(B))=1\quad \forall B\in O
    $$

With the concept of "**equality edge**", combined with the earlier blossom algorithm: continually expand using augmenting paths composed of "equality edges"; since the edges used for expansion are all "equality edges", the maximum-weight perfect matching finally obtained is still all "equality edges".

### Handling the blossom problem

When encountering a blossom, we need to contract it into an even point. Set all points in the blossom as even points, and let its $z_B=0$.

Since after contracting a blossom it will be stored until certain conditions are met before it is expanded, we cannot use the previous method to record blossoms.

If there is no special note, the points mentioned earlier all include the even points formed by contracting blossoms.

Since blossoms may also be contracted into points and added to the queue, and the number of blossoms is not fixed, we cannot enumerate each point to check for augmenting paths as before. Therefore, when performing breadth-first search (BFS), all unmatched points must be put into the queue.

This will simultaneously produce many alternating trees.

### The four steps of the algorithm

This algorithm can be divided into four steps.

1.  GROW (equality edge): use "equality edges" to form an alternating tree.
2.  AUGMENT: find an augmenting path and expand the matching.
3.  SHRINK: contract a blossom into a point.
4.  EXPAND: expand a blossom.

![general-weight-match-1](images/general-weight-match-1.png)

In the AUGMENT stage, because all unmatched points are on different alternating trees, when the even points of two alternating trees are connected together during augmentation, it means an augmenting path is found.

### Cannot find an equality edge to expand

Same as a bipartite graph, there is also the problem of not being able to find an "equality edge" to expand. At this point we need to adjust the vertex labeling.

### Adjusting VERTEX LABELING

The vertex labeling still needs to maintain the greater-than-or-equal property, and the existing "equality edges" cannot be changed, and we also need to make $z_B$ as small as possible.

???+ note "Definition of odd/even point symbols"
    Use $u^−$ to indicate that $u$ is an odd point on the alternating tree.  
    Use $u^+$ to indicate that $u$ is an even point on the alternating tree.  
    Use $u^\varnothing$ to indicate that $u$ is not on any alternating tree.  
    All subsequently mentioned $B$ are presumed to be blossoms, and simultaneously represent the point after the blossom is contracted.  
    A blossom can also be distinguished into an odd blossom or even blossom, so symbols such as $B^+$, $B^−$, $B^\varnothing$ also apply.

Suppose there are currently r alternating trees $T_i=(U_{t_i},V_{t_i}):1\leq i\leq r$; let

$$
\begin{aligned}
d1 &= \min(\{z_e : e = (u^+,v^\varnothing)\}) \\
d2 &= \min(\{z_e : e = (u^+,v^+), ~ u^+ \in T_i, ~ v^+ \in T_j, ~ i \neq j\}) / 2 \\
d3 &= \min(\{z_{B^-} : B^- \in O\}) / 2
\end{aligned}
$$

Note that here $B$ is the point after the blossom is contracted, so it can have parity.

Let $d=min(d1,d2,d3)$; let

$$
\begin{aligned}
z_{u^+} - &= d \\
z_{v^-} + &= d \\
z_{B^+} + &= 2d \\
z_{B^-} - &= 2d \\
\end{aligned}
$$

If $z_B=0(d=d3)$ appears, to prevent the situation $z_B<0$, we need to expand this blossom (EXPAND).
After expanding the blossom, only the alternating path in the blossom is kept, and the points in the blossom not on the alternating path are set as unvisited ($\varnothing$).

In this way one (or more) equality edge is created, the existing equality edges remain unchanged, and the property $z_e\geq0:\forall e\in E$ is maintained, and $z_B$ is increased minimally, so we can continue to find augmenting paths.

## General graph maximum-weight matching

The above finds the maximum-weight perfect matching; finding the maximum-weight matching requires adding an extra constraint to the vertex labeling: for all matched points $u$, $z_u>0$.

At the start, set all $z_u=max(\{w(e):e\in E\})/2$.

Points with vertex labeling $0$ will finally become unmatched points.

### Reference code

Here for convenience of implementation, the edge weight multiplied by $2$ is used to compute the value of $z_e$, so that floating-point errors will not appear.

???+ note "Storage"
    ```cpp
    constexpr int INF = INT_MAX;
    constexpr int MAXN = 400;
    
    struct edge {
      int u, v, w;
    
      // means (u,v) is an edge with weight w
      edge() {}
    
      edge(int u, int v, int w) : u(u), v(v), w(w) {}
    };
    
    int n, n_x;
    // there are n points, numbered 1 ~ n
    // n_x denotes the current number of points plus blossoms; numbers from n+1 to n_x are blossom nodes
    edge g[MAXN * 2 + 1][MAXN * 2 + 1];
    // the graph is stored with an adjacency matrix; because there are at most n-1 blossoms, the size is MAXN*2
    vector<int> flower[MAXN * 2 + 1];
    // flower[b] records which points are in blossom b
    // the way we record the points in a blossom is to only record the outermost blossom in the blossom
    ```

Below is an example of nested blossoms.

![general-weight-match-2](images/general-weight-match-2.png)

Where $\{ 6, 5, 8\} \in b1,\{ b1, 4, 3, 2, 11, 10, 9\} \in b2$. Stored as:

```text
flower[b2] = {b1, 4, 3, 2, 11, 10, 9} 
flower[b1] = {6, 5, 8}
```

![general-weight-match-3](images/general-weight-match-3.png)

```text
flower[b2] = {9, b1, 4, 3, 2, 11, 10} 
flower[b1] = {5, 8, 6}
```

```cpp
int lab[MAXN * 2 + 1];
// lab[u] is used to record z_u, lab[b] is used to record z_B
int match[MAXN * 2 + 1], slack[MAXN * 2 + 1], st[MAXN * 2 + 1],
    pa[MAXN * 2 + 1];
// match[x]=y means (x,y) is a matching, here x, y may be blossoms
// slack[x]=u means z(x,u) is the smallest edge among all edges adjacent to x
// st[x]=b means the blossom where node x is located is b. If x=b and b<=n, then it means x
// is an ordinary node (not belonging to any blossom). pa[v]=u means in the alternating tree, the parent node of node v is u
int flower_from[MAXN * 2 + 1][MAXN + 1], S[MAXN * 2 + 1], vis[MAXN * 2 + 1];
/*
flower_from[b][x]=xs means the largest sub-blossom of b containing x is xs
x is a point in b, xs is a blossom or point in b, and x=xs or x is one of the points of xs
*/
// S[u]={-1: not visited, 0: even point, 1: odd point}
// vis is only used to check whether it has been visited when finding the lca
queue<int> q;
// the queue used for BFS to find augmenting paths
```

![general-weight-match-4](images/general-weight-match-4.png)

```text
flower_from[b2][6] = b1 
flower_from[b2][5] = b1 
flower_from[b2][9] = 9 
flower_from[b1][6] = 6 
and so on
```

```cpp
int e_delta(const edge &e) {
  // compute ze; for convenience first multiply the weights of all edges by two
  // directly computing the e_delta value inside a blossom will cause errors
  return lab[e.u] + lab[e.v] - g[e.u][e.v].w * 2;
}

void update_slack(int u, int x) {
  // update the value of slack[x] with u
  if (!slack[x] || e_delta(g[u][x]) < e_delta(g[slack[x]][x])) {
    slack[x] = u;
  }
}

void set_slack(int x) {
  // compute the value of slack[x]; slack[x]=0 means x is a node in the alternating tree
  slack[x] = 0;
  for (int u = 1; u <= n; ++u) {
    if (g[u][x].w > 0 && st[u] != x && S[st[u]] == 0) {
      update_slack(u, x);
    }
  }
}
```

```cpp
void q_push(int x) {
  // throw x into the queue; we set that the queue cannot directly push a blossom
  if (x <= n)
    q.push(x);
  else {
    // if we want to push a blossom, we must add the points of the original graph inside the blossom into the queue
    for (size_t i = 0; i < flower[x].size(); i++) {
      q_push(flower[x][i]);
    }
  }
}

void set_st(int x, int b) {
  // set the blossom where x is located to b
  st[x] = b;
  if (x > n) {
    // if x is also a blossom, we must set the blossoms where the points inside x are located to b
    for (size_t i = 0; i < flower[x].size(); ++i) {
      set_st(flower[x][i], b);
    }
  }
}
```

```cpp
int get_pr(int b, int xr) {
  // xr is a point in flower[b]; the return value pr is its position
  // for convenience of program running, we let flower[b][0]~flower[b][pr] be the alternating path in the blossom
  int pr = find(flower[b].begin(), flower[b].end(), xr) - flower[b].begin();
  if (pr % 2 == 1) {
    // check its position in the blossom; if flower[b][0]~flower[b][pr] is not an alternating path
    // then reverse the whole blossom and recompute pr
    // let flower[b][0]~flower[b][pr] be the alternating path in the blossom
    reverse(flower[b].begin() + 1, flower[b].end());
    return (int)flower[b].size() - pr;
  } else
    return pr;
}
```

![general-weight-match-5](images/general-weight-match-5.png)

If we use `get_pr(b2,11)`, `flower[b2]` will become `{9,10,11,2,3,4,b1}` and return 2.

If we use `get_pr(b2,2)`, `flower[b2]` will become `{9,b1,4,3,2,11,10}` and return 4.

```cpp
void set_match(int u, int v) {
  // set u and v as a matching edge; u and v may be blossoms
  match[u] = g[u][v].v;
  if (u > n) {
    // if u is a blossom
    edge e = g[u][v];
    int xr = flower_from[u][e.u];  // find which blossom e.u is on in flower[u]
    int pr = get_pr(u, xr);  // find the position of xr and let 0~pr be the alternating path in the blossom
    for (int i = 0; i < pr; ++i) {  // reverse the matching edges and non-matching edges on the alternating path in the blossom
      set_match(flower[u][i], flower[u][i ^ 1]);
    }
    set_match(xr, v);  // set (xr,v) as a matching edge
    rotate(flower[u].begin(), flower[u].begin() + pr, flower[u].end());
    // finally set pr as the blossom base; because the storage of the blossom is flower[u][0] being the base of u
    // so we need to rotate flower[u][pr] to the front
  }
}

void augment(int u, int v) {
  // augment u and all ancestors of u, and set (u,v) as a matching edge
  for (;;) {
    int xnv = st[match[u]];
    set_match(u, v);
    if (!xnv) return;
    set_match(xnv, st[pa[xnv]]);
    u = st[pa[xnv]];
    v = xnv;
  }
}

int get_lca(int u, int v) {
  // find the lca of u, v on the alternating tree
  static int t = 0;
  for (++t; u || v; swap(u, v)) {
    if (u == 0) continue;
    if (vis[u] == t) return u;
    vis[u] = t;  // this method avoids clearing the vis array
    u = st[match[u]];
    if (u) u = st[pa[u]];
  }
  return 0;
}
```

???+ note "Add an odd blossom"
    ```cpp
    void add_blossom(int u, int lca, int v) {
      // contract the blossom u,v,lca into a point b
      // the lca of u,v on the alternating tree is the blossom base
      int b = n + 1;
      while (b <= n_x && st[b]) ++b;
      if (b > n_x) ++n_x;
      // find the currently unused blossom number
      lab[b] = 0;             // set zB=0
      S[b] = 0;               // the whole blossom is an even point
      match[b] = match[lca];  // set the matching edge of the blossom to the matching edge of the blossom base
      flower[b].clear();
      flower[b].push_back(lca);
      for (int x = u, y; x != lca; x = st[pa[y]]) {
        flower[b].push_back(x);
        y = st[match[x]];
        flower[b].push_back(y);
        q_push(y);
      }
      reverse(flower[b].begin() + 1, flower[b].end());
      for (int x = v, y; x != lca; x = st[pa[y]]) {
        flower[b].push_back(x);
        y = st[match[x]];
        flower[b].push_back(y);
        q_push(y);
      }
      // all points in b are added to flower[b] in a circular manner, with the blossom base as the first element
      set_st(b, b);  // set the blossom where all elements in the whole blossom are located to b
      for (int x = 1; x <= n_x; ++x) {
        g[b][x].w = 0;
        g[x][b].w = 0;
      }
      for (int x = 1; x <= n; ++x) {
        flower_from[b][x] = 0;
      }
      for (size_t i = 0; i < flower[b].size(); ++i) {
        int xs = flower[b][i];
        for (int x = 1; x <= n_x; ++x) {
          // set the edge adjacent to b and x to be the one with the smallest e_delta among the edges inside b adjacent to x
          if (g[b][x].w == 0 || e_delta(g[xs][x]) < e_delta(g[b][x])) {
            g[b][x] = g[xs][x];
            g[x][b] = g[x][xs];
          }
        }
        for (int x = 1; x <= n; ++x) {
          if (flower_from[xs][x]) {
            // if the point xs in b contains x
            // then flower_from[b][x] is xs
            flower_from[b][x] = xs;
          }
        }
      }
      set_slack(b);
      // finally we must set the slack value of b
    }
    ```

???+ note "Expand a blossom"
    ```cpp
    void expand_blossom(int b) {
      // when b is an odd blossom and zB=0, we must expand b
      // because only b is expanded, so if b contains other blossoms
      // we do not need to expand them
      for (size_t i = 0; i < flower[b].size(); ++i) {
        set_st(flower[b][i], flower[b][i]);
        // first set the blossom where each element in flower[b] is located to itself
      }
      int xr = flower_from[b][g[b][pa[b]].u];
      // xr denotes which blossom in flower[b] the parent node of b on the alternating path is on
      int pr = get_pr(b, xr);  // find the position of xr and let 0~pr be the alternating path in the blossom
      for (int i = 0; i < pr; i += 2) {
        // expand the alternating path into the alternating tree
        // and throw the even points on the alternating path into the queue
        int xs = flower[b][i];
        int xns = flower[b][i + 1];
        pa[xs] = g[xns][xs].u;
        S[xs] = 1;
        S[xns] = 0;
        slack[xs] = 0;
        set_slack(xns);
        q_push(xns);
      }
      S[xr] = 1;  // at this point xr will be an odd point or odd blossom
      pa[xr] = pa[b];
      for (size_t i = pr + 1; i < flower[b].size(); ++i) {
        // set all points in the blossom no longer on the alternating path as unvisited
        int xs = flower[b][i];
        S[xs] = -1;
        set_slack(xs);
      }
      st[b] = 0;
    }
    ```

???+ note "Try to augment an equality edge"
    ```cpp
    bool on_found_edge(const edge &e) {
      // an equality edge e is found during BFS
      // we need to perform the following processing on it
      // here u must be an even point
      int u = st[e.u], v = st[e.v];
      if (S[v] == -1) {
        // v is an unvisited node
        pa[v] = e.u;
        S[v] = 1;
        int nu = st[match[v]];
        slack[v] = 0;
        slack[nu] = 0;
        S[nu] = 0;
        q_push(nu);
      } else if (S[v] == 0) {
        // v is an even point
        int lca = get_lca(u, v);
        if (!lca) {  // lca=0 means u,v are on different alternating trees, there is an augmenting path
          augment(u, v);
          augment(v, u);
          return true;  // augmenting path found
        } else
          add_blossom(u, lca, v);
        // otherwise u,v being on the same tree will be a blossom, contract the blossom
      }
      return false;
    }
    ```

???+ note "Augment"
    ```cpp
    bool matching() {
      memset(S + 1, -1, sizeof(int) * n_x);
      memset(slack + 1, 0, sizeof(int) * n_x);
      q = queue<int>();  // clear the queue
      for (int x = 1; x <= n_x; ++x) {
        if (st[x] == x && !match[x]) {
          // add all non-matched points into the queue, and set them as even points
          pa[x] = 0;
          S[x] = 0;
          q_push(x);
        }
      }
      if (q.empty()) return false;  // all points are matched
      for (;;) {
        while (q.size()) {
          // BFS
          int u = q.front();
          q.pop();
          if (S[st[u]] == 1) continue;
          for (int v = 1; v <= n; ++v) {
            if (g[u][v].w > 0 && st[u] != st[v]) {
              if (e_delta(g[u][v]) == 0) {
                if (on_found_edge(g[u][v])) return true;
              } else
                update_slack(u, st[v]);
            }
          }
        }
        // modify the lab value
        int d = INF;
        for (int u = 1; u <= n; ++u) {
          // this is to prevent the case lab<0 from occurring
          // as long as any lab[u]=0, end the program
          if (S[st[u]] == 0) d = min(d, lab[u]);
        }
        for (int b = n + 1; b <= n_x; ++b) {
          if (st[b] == b && S[b] == 1) d = min(d, lab[b] / 2);
        }
        for (int x = 1; x <= n_x; ++x)
          if (st[x] == x && slack[x]) {
            if (S[x] == -1)
              d = min(d, e_delta(g[slack[x]][x]));
            else if (S[x] == 0)
              d = min(d, e_delta(g[slack[x]][x]) / 2);
          }
        for (int u = 1; u <= n; ++u) {
          if (S[st[u]] == 0) {
            if (lab[u] == d) return false;
            // if lab[u]=0, directly end the program
            lab[u] -= d;
          } else if (S[st[u]] == 1)
            lab[u] += d;
        }
        for (int b = n + 1; b <= n_x; ++b) {
          if (st[b] == b) {
            if (S[st[b]] == 0)
              lab[b] += d * 2;
            else if (S[st[b]] == 1)
              lab[b] -= d * 2;
          }
        }
        q = queue<int>();  // clear the queue
        for (int x = 1; x <= n_x; ++x) {
          // check whether an augmenting path is produced
          if (st[x] == x && slack[x] && st[slack[x]] != x &&
              e_delta(g[slack[x]][x]) == 0)
            if (on_found_edge(g[slack[x]][x])) return true;
        }
        for (int b = n + 1; b <= n_x; ++b) {
          // the EXPAND operation, expand all odd blossoms with lab[b]=0
          if (st[b] == b && S[b] == 1 && lab[b] == 0) expand_blossom(b);
        }
      }
      return false;
    }
    ```

???+ note "Main function"
    ```cpp
    pair<long long, int> weight_blossom() {
      // main function, first initialize at the start
      memset(match + 1, 0, sizeof(int) * n);
      n_x = n;  // no blossoms at the start
      int n_matches = 0;
      long long tot_weight = 0;
      for (int u = 0; u <= n; ++u) {
        // first set the blossom where itself is located to itself
        st[u] = u;
        flower[u].clear();
      }
      int w_max = 0;
      for (int u = 1; u <= n; ++u)
        for (int v = 1; v <= n; ++v) {
          // when u is a point, the point it contains is only itself
          flower_from[u][v] = (u == v ? u : 0);
          w_max = max(w_max, g[u][v].w);
          // find the maximum edge weight
        }
      for (int u = 1; u <= n; ++u) lab[u] = w_max;
      // let all lab = maximum edge weight
      // because here the implementation uses edge weight multiplied by two to compute the value of ze, so no need to divide by two
      while (matching()) ++n_matches;
      for (int u = 1; u <= n; ++u)
        if (match[u] && match[u] < u) tot_weight += g[u][match[u]].w;
      return make_pair(tot_weight, n_matches);
    }
    ```

???+ note "Initialization"
    Very important; must initialize before use
    
    ```cpp
    void init_weight_graph() {
      // must initialize before inputting edges into the graph
      // because it is maximum-weight matching, set non-existent edges to 0
      for (int u = 1; u <= n; ++u)
        for (int v = 1; v <= n; ++v) g[u][v] = edge(u, v, 0);
    }
    ```

## Complexity analysis

Each blossom is contracted or expanded only once in one BFS. The time complexity of each contraction or expansion is $O(|V|)$. There are at most $O(|V|)$ blossoms in total, so blossom handling costs $O(|V|^2)$ time. And BFS costs $O(|V| + |E|)$ time complexity. Therefore, finding an augmenting path costs $O(|V| + |E|) + O(|V|^2) = O(|V|^2)$ time complexity.

At most $|V|$ BFS operations are done. So, the total time complexity is $O(|V|^3)$.

## Exercises

-   [UOJ #81. General Graph Maximum-Weight Matching](https://uoj.ac/problem/81)

## References

1.  [Kolmogorov, Vladimir (2009), "Blossom V: A new implementation of a minimum cost perfect matching algorithm"](http://pub.ist.ac.at/~vnk/papers/BLOSSOM5.html)
2.  [From the Hungarian algorithm to the weighted blossom tree—a detailed explanation of the application of the dual problem in graph matching](https://www.luogu.com.cn/blog/potassium/solution-p6699)
