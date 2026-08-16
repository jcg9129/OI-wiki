author: accelsao, Enter-tainer, guodong2005, StudyingFather, Backl1ght, Chrogeek, H-J-Granger, Henry-ZHR

The maximum-weight matching of a bipartite graph refers to the matching with the maximum sum of edge weights in a bipartite graph.

## Hungarian Algorithm（Kuhn–Munkres Algorithm）

The Hungarian algorithm, also called the **KM** algorithm, can find the **maximum-weight perfect matching** of a bipartite graph in $O(n^3)$ time.

Considering that the points in the two sets of a bipartite graph are not always the same, in order to apply the KM algorithm to solve the maximum-weight matching of a bipartite graph, the following processing needs to be done first: pad points to the set with fewer points, so that the number of points on both sides is the same, then set the weights of non-existent edges to $0$; in this case, the problem is converted into finding the **maximum-weight perfect matching problem**, so that the KM algorithm can be applied to solve it.

???+ note "Feasible vertex labeling"
    Assign a weight $l(i)$ to each node $i$, such that for all edges $(u,v)$, $w(u,v) \leq l(u) + l(v)$.

???+ note "Equality subgraph"
    Under a set of feasible vertex labels, the spanning subgraph of the original graph, containing all points but only the edges $(u,v)$ satisfying $w(u,v) = l(u) + l(v)$.

???+ note "Theorem 1: For a set of feasible vertex labels, if its equality subgraph has a perfect matching, then this matching is the maximum-weight perfect matching of the original bipartite graph."
    Proof 1.
    
    Consider any perfect matching $M$ of the original bipartite graph; its edge weight sum is
    
    $val(M) = \sum_{(u,v)\in M} {w(u,v)} \leq \sum_{(u,v)\in M} {l(u) + l(v)} \leq \sum_{i=1}^{n} l(i)$
    
    The edge weight sum of the perfect matching $M'$ of the equality subgraph of any set of feasible vertex labels
    
    $val(M') = \sum_{(u,v)\in M} {l(u) + l(v)} = \sum_{i=1}^{n} l(i)$
    
    That is, the edge weight sum of any perfect matching will not be greater than $val(M')$, so that $M'$ is the maximum-weight matching.

With Theorem 1, our goal is to make the equality subgraph a perfect matching by continually adjusting the feasible vertex labels.

Because the number of points on both sides is equal, suppose the number of points is $n$; $lx(i)$ denotes the vertex label of the $i$-th point on the left, $ly(i)$ denotes the vertex label of the $i$-th point on the right, and $w(u,v)$ denotes the weight between the $u$-th point on the left and the $v$-th point on the right.

First initialize a set of feasible vertex labels, for example

$lx(i) = \max_{1\leq j\leq n} \{ w(i, j)\},\, ly(i) = 0$

Then choose an unmatched point, and find an augmenting path as in maximum matching. If an augmenting path is found, augment; otherwise, an alternating tree is obtained.

Let $S$, $T$ denote the points on the left and right of the bipartite graph in the alternating tree, and $S'$, $T'$ denote the points not in the alternating tree.

![bigraph-weight-match-1](./images/bigraph-weight-match-1.png)

In the equality subgraph:

-   $S-T'$ edges do not exist, otherwise the alternating tree would grow.
-   $S'-T$ must be a non-matching edge, otherwise it would belong to $S$.

Suppose we give the vertex labels in $S$ $-a$ and the vertex labels in $T$ $+a$; we can find that

-   $S-T$ edges still exist in the equality subgraph.
-   $S'-T'$ does not change.
-   $lx + ly$ in $S-T'$ decreases, possibly joining the equality subgraph.
-   $lx + ly$ in $S'-T$ increases, so it cannot possibly join the equality subgraph.

So the choice of this $a$ value obviously has to be the smallest edge weight among $S-T'$,

$a = \min \{ lx(u) + ly(v) - w(u,v) | u\in{S} , v\in{T'} \}$.

When a new edge $(u,v)$ joins the equality subgraph, there are two cases

-   $v$ is an unmatched point, then an augmenting path is found
-   $v$ is already matched with a point in $S'$

In this way, after modifying the vertex labels at most $n$ times, an augmenting path can be found.

Each time the vertex labels are modified, the edges in the alternating tree will not leave the equality subgraph, so we directly maintain this tree.

For each point $v$ in $T$ we maintain

$slack(v) = \min \{ lx(u) + ly(v) - w(u,v) | u\in{S} \}$.

So the vertex-label modification value $a$ can be computed in $O(n)$

$a = \min \{ slack(v) | v\in{T'} \}$

When the alternating tree adds a new point into $S$, we need $O(n)$ to update $slack(v)$. Modifying the vertex labels needs $O(n)$ to subtract $a$ from each $slack(v)$. As long as the alternating tree finds an unmatched point, an augmenting path is found.

At the start we enumerate $n$ points to find augmenting paths; to find an augmenting path we need to extend the alternating tree $n$ times, and each extension needs $n$ maintenance operations, totaling $O(n^3)$.

??? note "Reference code"
    ```cpp
    template <typename T>
    struct hungarian {  // km
      int n;
      vector<int> matchx;  // the matched point corresponding to the left set
      vector<int> matchy;  // the matched point corresponding to the right set
      vector<int> pre;     // the left point connecting the right set
      vector<bool> visx;   // visit array, left
      vector<bool> visy;   // visit array, right
      vector<T> lx;
      vector<T> ly;
      vector<vector<T>> g;
      vector<T> slack;
      T inf;
      T res;
      queue<int> q;
      int org_n;
      int org_m;
    
      hungarian(int _n, int _m) {
        org_n = _n;
        org_m = _m;
        n = max(_n, _m);
        inf = numeric_limits<T>::max();
        res = 0;
        g = vector<vector<T>>(n, vector<T>(n));
        matchx = vector<int>(n, -1);
        matchy = vector<int>(n, -1);
        pre = vector<int>(n);
        visx = vector<bool>(n);
        visy = vector<bool>(n);
        lx = vector<T>(n, -inf);
        ly = vector<T>(n);
        slack = vector<T>(n);
      }
    
      void addEdge(int u, int v, int w) {
        g[u][v] = max(w, 0);  // a negative value is worse than not matching, so setting it to 0 has no effect
      }
    
      bool check(int v) {
        visy[v] = true;
        if (matchy[v] != -1) {
          q.push(matchy[v]);
          visx[matchy[v]] = true;  // in S
          return false;
        }
        // found a new unmatched point, update the matched point; the pre array records the point connected to it on the "non-matching edge"
        while (v != -1) {
          matchy[v] = pre[v];
          swap(v, matchx[pre[v]]);
        }
        return true;
      }
    
      void bfs(int i) {
        while (!q.empty()) {
          q.pop();
        }
        q.push(i);
        visx[i] = true;
        while (true) {
          while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v = 0; v < n; v++) {
              if (!visy[v]) {
                T delta = lx[u] + ly[v] - g[u][v];
                if (slack[v] >= delta) {
                  pre[v] = u;
                  if (delta) {
                    slack[v] = delta;
                  } else if (check(v)) {  // delta=0 means there is a chance to join the equality subgraph, find an augmenting path
                                          // return if found, rebuild the alternating tree
                    return;
                  }
                }
              }
            }
          }
          // no augmenting path, modify the vertex labels
          T a = inf;
          for (int j = 0; j < n; j++) {
            if (!visy[j]) {
              a = min(a, slack[j]);
            }
          }
          for (int j = 0; j < n; j++) {
            if (visx[j]) {  // S
              lx[j] -= a;
            }
            if (visy[j]) {  // T
              ly[j] += a;
            } else {  // T'
              slack[j] -= a;
            }
          }
          for (int j = 0; j < n; j++) {
            if (!visy[j] && slack[j] == 0 && check(j)) {
              return;
            }
          }
        }
      }
    
      void solve() {
        // initial vertex labels
        for (int i = 0; i < n; i++) {
          for (int j = 0; j < n; j++) {
            lx[i] = max(lx[i], g[i][j]);
          }
        }
    
        for (int i = 0; i < n; i++) {
          fill(slack.begin(), slack.end(), inf);
          fill(visx.begin(), visx.end(), false);
          fill(visy.begin(), visy.end(), false);
          bfs(i);
        }
    
        // custom
        for (int i = 0; i < n; i++) {
          if (g[i][matchx[i]] > 0) {
            res += g[i][matchx[i]];
          } else {
            matchx[i] = -1;
          }
        }
        cout << res << "\n";
        for (int i = 0; i < org_n; i++) {
          cout << matchx[i] + 1 << " ";
        }
        cout << "\n";
      }
    };
    ```

## Dynamic Hungarian Algorithm

Original paper [The Dynamic Hungarian Algorithm for the Assignment Problem with Changing Costs](https://www.ri.cmu.edu/publications/the-dynamic-hungarian-algorithm-for-the-assignment-problem-with-changing-costs/)

Paper with clearer pseudocode [A Fast Dynamic Assignment Algorithm for Solving Resource Allocation Problems](https://www.researchgate.net/publication/352490780_A_Fast_Dynamic_Assignment_Algorithm_for_Solving_Resource_Allocation_Problems)

Related OJ problem [DAP](https://www.spoj.com/problems/DAP/)

???+ note "Algorithm idea"
    1.  Modify the weights between a single point $u_i$ and all $v_j$, i.e. a row in the weight matrix
        -   Modify the vertex label $lx(u_i) = max(w_{ij} - v_{j}), \forall j$
        -   Delete the matchings related to $u_i$
    2.  Modify the weights between all $u_i$ and a single point $v_j$, i.e. a column in the weight matrix
        -   Modify the vertex label $ly(v_j) = max(w_{ij} - u_{i}), \forall i$
        -   Delete the matchings related to $v_j$
    3.  Modify the weight between a single point $u_i$ and a single point $v_j$, i.e. a single element in the weight matrix
        -   Just do one of operations 1 or 2
    4.  Add a single point $u_i$, or a single point $v_j$, i.e. add or delete a row or a column in the weight matrix
        -   Just correspondingly do 1 or 2; note that the add-point operation here is only adding a point, without additionally setting a weight value, and the weight between the newly added point and other points is 0.

???+ note "Algorithm proof"
    -   Let the original graph be G, the vertex labels on the left and right be $\alpha^{i}$ and $\beta^{j}$, and the feasible vertex label be l; then $G_l$ is a subgraph of G, containing the points and edges in graph G satisfying $w_{ij} = alpha_{i}+beta_{j}$.
    -   In the Hungarian algorithm part above, Theorem 1 proved: for a set of feasible vertex labels, if its equality subgraph has a perfect matching, then this matching is the maximum-weight perfect matching of the original bipartite graph.
    -   Suppose the original optimal matching is $M^*$; when a modification occurs, we update the feasible vertex labels according to the rules, and set the updated vertex labels as $\alpha^{i^*}$ or $\beta^{j^*}$; the following situations will occur:
        1.  A whole row of the weight matrix is modified; let the modified row be row $i^*$, i.e. all edges of $v_{i^*}$ are modified, so $v_{i^*}$'s original vertex label may not satisfy the condition, because we need $w_{i^{*}j} \leq alpha_{i^*}+beta_{j}$, but for the other $u_j$, except for the edges related to $i^*$, their edge weights are unchanged, so their vertex labels are all valid, so the algorithm modifies the vertex label related to $v_{i^*}$ so that this set of vertex labels is a set of feasible vertex labels.
        2.  A whole column of the weight matrix is modified; similarly, the algorithm modifies the vertex labels so that this set of vertex labels is a set of feasible vertex labels.
        3.  Modifying an element of the weight matrix; arbitrarily modifying one of the vertex labels satisfies the vertex-label condition.
    -   Each time the weight matrix is modified, it relates to a specific node; this node may be on the left or on the right, so we directly denote it as $x$; this node is matched with some node $y$ in the original optimal matching. Each modification operation, at most, unpairs this pair of nodes, so we just need to run one round of the search in the Hungarian algorithm and we can get a new match, and according to Theorem 1, the newly obtained match is optimal.

The following code should be the code submitted by the author of paper 2 (the following code is the maximization-weight version; the original paper is minimization of cost)

??? note "Dynamic Hungarian algorithm reference code"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-weight-match/bigraph-weight-match_1.cpp"
    ```

## Converting to a cost-flow model

Similar to [bipartite graph maximum matching](./bigraph-match.md), the maximum-weight matching of a bipartite graph can also be converted into a network-flow problem to solve.

First, add a source and a sink to the graph.

From the source, connect an edge with flow $1$ and cost $0$ to each left-part point of the bipartite graph; from each right-part point of the bipartite graph, connect an edge with flow $1$ and cost $0$ to the sink.

Next, for each edge connecting a left-part point $u$ and a right-part point $v$ with edge weight $w$ in the bipartite graph, connect an edge from $u$ to $v$ with flow $1$ and cost $w$.

In addition, considering that under maximum-weight matching, the number of matching edges is not necessarily equal to the number of matching edges of the maximum matching, so for each left-part point, we also need to connect an edge to the sink with flow $1$ and cost $0$.

Finding the [maximum-cost maximum flow](../flow/min-cost.md) of this network gives the answer. At this point, the maximum flow of this network must be the number of left-part points, and the maximum cost under the maximum flow corresponds to a maximum-weight matching scheme.

## Exercises

??? note "[UOJ #80. Bipartite Graph Maximum-Weight Matching](https://uoj.ac/problem/80)"
    Template problem
    
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-weight-match/bigraph-weight-match_2.cpp"
    ```
