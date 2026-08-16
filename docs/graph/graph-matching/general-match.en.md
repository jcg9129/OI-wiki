author: H-J-Granger, accelsao, Ir1d, Early0v0, Henry-ZHR, HeliumOI, AntiLeaf, ShizuhaAki, pukui

## Blossom Algorithm

The Blossom Algorithm (also called the blossom tree) can solve the general graph maximum cardinality matching problem. This algorithm was proposed by Jack Edmonds in 1961.
After some modifications, it can also solve the general graph maximum-weight matching problem.
This algorithm was the first to give a proof that maximum matching has polynomial complexity.

The difference between general graph matching and bipartite matching is that the graph may have odd cycles.

![general-matching-1](./images/general-matching-1.png)

Taking this figure as an example, if we directly invert (swap matching edges and unmatched edges), it will make the inverted $M$ invalid, and some points will appear on two matchings; the problem lies precisely in the odd cycle.

Below we consider the augmentation algorithm for a general graph.
Starting from the bipartite graph perspective, each time we enumerate an unmatched point, set the starting point as the root, mark it as **"o"**, then alternately mark **"o"** and **"i"**; it is not hard to find that the segment of edge from **"i"** to **"o"** is a matching edge.

Suppose the current point is $v$ and the adjacent point is $u$; we can divide into the following two cases:

1.  $u$ has not been visited; when $u$ is an unmatched point, then an augmenting path is found, otherwise find an augmenting path from $u$'s partner.
2.  $u$ has been visited; encountering the mark "o" represents the need to **contract the blossom**, otherwise it represents encountering an even cycle, skip.

The case of encountering an even cycle, we treat it as a bipartite graph to solve, so it can be ignored. After **contracting the blossom**, continue to find augmenting paths in the new graph.

![general-matching-2](./images/general-matching-2.png)

Let the original graph be $G$ and the graph after **contracting the blossom** be $G'$; we only need to prove:

1.  If $G$ has an augmenting path, $G'$ also has one.
2.  If $G'$ has an augmenting path, $G$ also has one.

![general-matching-3](./images/general-matching-3.png)

Let the non-tree edge (the edge forming the cycle) be $(u,v)$, and define the blossom root $h=LCA(u,v)$.
The odd cycle is alternating; only the two adjacent edges of $h$ have the same type, both being non-matching edges.
Then the tree edge entering $h$ must be a matching edge, and the edges from the other points on the cycle except $h$ going outside the cycle are all non-matching edges.

By observation, going out from the edges outside the cycle has two cases, clockwise or counterclockwise.

![general-matching-4](./images/general-matching-4.png)

So both **contracting the blossom** and **not contracting the blossom** do not affect correctness.

In implementation, after finding the **blossom** we do not need to actually **contract the blossom**; we can use an array to record which blossom each point is in, rooted at which point.

### Complexity Analysis

Each time we find an augmenting path, we traverse all edges, and encountering a **blossom** we maintain the points on the **blossom**, $O(|E|^2)$.

Enumerating all unmatched points to find augmenting paths, in total $O(|V||E|^2)$.

### Reference code

??? note "Reference code"
    ```cpp
    // graph
    template <typename T>
    class graph {
     public:
      struct edge {
        int from;
        int to;
        T cost;
      };
    
      vector<edge> edges;
      vector<vector<int>> g;
      int n;
    
      graph(int _n) : n(_n) { g.resize(n); }
    
      virtual int add(int from, int to, T cost) = 0;
    };
    
    // undirectedgraph
    template <typename T>
    class undirectedgraph : public graph<T> {
     public:
      using graph<T>::edges;
      using graph<T>::g;
      using graph<T>::n;
    
      undirectedgraph(int _n) : graph<T>(_n) {}
    
      int add(int from, int to, T cost = 1) {
        assert(0 <= from && from < n && 0 <= to && to < n);
        int id = (int)edges.size();
        g[from].push_back(id);
        g[to].push_back(id);
        edges.push_back({from, to, cost});
        return id;
      }
    };
    
    // blossom / find_max_unweighted_matching
    template <typename T>
    vector<int> find_max_unweighted_matching(const undirectedgraph<T> &g) {
      std::mt19937 rng(std::random_device{}());
      vector<int> match(g.n, -1);   // matching
      vector<int> aux(g.n, -1);     // timestamp
      vector<int> label(g.n);       // "o" or "i"
      vector<int> orig(g.n);        // blossom root
      vector<int> parent(g.n, -1);  // parent node
      queue<int> q;
      int aux_time = -1;
    
      auto lca = [&](int v, int u) {
        aux_time++;
        while (true) {
          if (v != -1) {
            if (aux[v] == aux_time) {  // found a visited point, i.e. the LCA
              return v;
            }
            aux[v] = aux_time;
            if (match[v] == -1) {
              v = -1;
            } else {
              v = orig[parent[match[v]]];  // continue searching with the parent node of the matched point
            }
          }
          swap(v, u);
        }
      };  // lca
    
      auto blossom = [&](int v, int u, int a) {
        while (orig[v] != a) {
          parent[v] = u;
          u = match[v];
          if (label[u] == 1) {  // the initial point is set to "o" to find an augmenting path
            label[u] = 0;
            q.push(u);
          }
          orig[v] = orig[u] = a;  // contract the blossom
          v = parent[u];
        }
      };  // blossom
    
      auto augment = [&](int v) {
        while (v != -1) {
          int pv = parent[v];
          int next_v = match[pv];
          match[v] = pv;
          match[pv] = v;
          v = next_v;
        }
      };  // augment
    
      auto bfs = [&](int root) {
        fill(label.begin(), label.end(), -1);
        iota(orig.begin(), orig.end(), 0);
        while (!q.empty()) {
          q.pop();
        }
        q.push(root);
        // the initial point is set to "o", here "0" replaces "o" and "1" replaces "i"
        label[root] = 0;
        while (!q.empty()) {
          int v = q.front();
          q.pop();
          for (int id : g.g[v]) {
            auto &e = g.edges[id];
            int u = e.from ^ e.to ^ v;
            if (label[u] == -1) {  // found an unvisited point
              label[u] = 1;        // mark "i"
              parent[u] = v;
              if (match[u] == -1) {  // found an unmatched point
                augment(u);          // find an augmenting path
                return true;
              }
              // found a matched point, throw the point matched with it into the queue to extend the alternating tree
              label[match[u]] = 0;
              q.push(match[u]);
              continue;
            } else if (label[u] == 0 && orig[v] != orig[u]) {
              // found a visited point, and the mark is also "o", representing that a "blossom" is found
              int a = lca(orig[v], orig[u]);
              // find the LCA and then contract the blossom
              blossom(u, v, a);
              blossom(v, u, a);
            }
          }
        }
        return false;
      };  // bfs
    
      auto greedy = [&]() {
        vector<int> order(g.n);
        // randomly shuffle order
        iota(order.begin(), order.end(), 0);
        shuffle(order.begin(), order.end(), rng);
    
        // match the points that can be matched
        for (int i : order) {
          if (match[i] == -1) {
            for (auto id : g.g[i]) {
              auto &e = g.edges[id];
              int to = e.from ^ e.to ^ i;
              if (match[to] == -1) {
                match[i] = to;
                match[to] = i;
                break;
              }
            }
          }
        }
      };  // greedy
    
      // first do a random matching at the start
      greedy();
      // find augmenting paths for unmatched points
      for (int i = 0; i < g.n; i++) {
        if (match[i] == -1) {
          bfs(i);
        }
      }
      return match;
    }
    ```

??? note "[UOJ #79. General Graph Maximum Matching](https://uoj.ac/problem/79)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/general-match/general-match_1.cpp"
    ```

## General graph matching algorithm based on Gaussian elimination

???+ tip "Tip"
    Before reading the following content, you may need to first read the content about matrices in the "Linear algebra" part:
    
    -   [Matrix](../../math/linear-algebra/matrix.md)
    -   [Determinant](../../math/linear-algebra/determinant.md)
    -   [Gaussian elimination](../../math/numerical/gauss.md)

This part will introduce a general graph matching algorithm based on Gaussian elimination. Compared with the traditional blossom algorithm, its advantage is that it is easier to understand and write, and is convenient for solving problems such as "necessary points in a maximum matching"; the disadvantage is that its constant factor is relatively large, because the $O(n^3)$ of Gaussian elimination is basically fully run, while the blossom tree generally is not fully run.

### Prerequisite: Tutte matrix

**Definition**: for an undirected graph $G = (V, E)$ with $n$ points, its Tutte matrix $\tilde{A}(G)$ is an $n \times n$ matrix, where:

$$
\tilde{A}(G)_{i,j} = \begin{cases}
x_{i,j}, & i<j,\; (v_i, v_j)\in E \\
-x_{i,j}, & i > j,\; (v_i, v_j) \in E \\
0, & \text{otherwise}
\end{cases}
$$

where $x_{i, j}$ is a variable, so there are a total of $|E|$ variables in $\tilde{A}(G)$.

In the case of no ambiguity, below $\tilde{A}(G)$ is abbreviated as $\tilde{A}$.

**Theorem** (Tutte's theorem): $G$ has a perfect matching if and only if $\det \tilde{A} \ne 0$.

??? note "Proof"
    Here we introduce the concept of "even-cycle cover": an even-cycle cover of an undirected graph $G$ refers to covering all points without repetition or omission using several even cycles (including binary cycles).
    
    It is easy to prove that $G$ has a perfect matching if and only if $G$ has an even-cycle cover.
    
    -   If $G$ has an even-cycle cover, we only need to take every other edge in each cycle, and we can obtain a perfect matching.
    -   If $G$ has a perfect matching, we only need to take out the binary cycles corresponding to the matching edges, and we can obtain an even-cycle cover.
    
    Then prove that $G$ has an even-cycle cover if and only if $\tilde{A} \ne 0$.
    
    Consider the definition of the determinant
    
    $$
    \det A = \sum_{\pi} (-1)^{\pi} \prod_{i} A_{i, \pi_i}
    $$
    
    where $\pi$ is any permutation, and $(-1)^{\pi}$ means if the number of inversions in $\pi$ is odd, then take $-1$, otherwise take $1$.
    
    It is not hard to see that each permutation can be regarded as a cycle cover of $G$. If there is an odd cycle in this cycle cover, then the sum after flipping this cycle must be $0$, so only an even-cycle cover can make the determinant nonzero. Q.E.D.

**Theorem**: $\operatorname{rank}\tilde{A}$ must be even, and the size of the maximum matching of $G$ equals half of $\operatorname{rank}\tilde{A}$.

??? note "Proof"
    The rank of an antisymmetric matrix can only be even; the latter is left for the reader to think about.

In practical applications it is impossible to compute with $|E|$ variables, but we can take a number field, for example the residue system $\mathcal{Z}_p$ of some prime $p$, randomly replace the variables with numbers in $\mathcal{Z}_p$ respectively, and then compute. For convenience, in the case of no ambiguity, below we use $\tilde{A}$ to directly refer to the matrix after replacement.

**Theorem**: $\operatorname{rank}\tilde{A}$ is at most twice the size of the maximum matching of $G$, and the probability that the two are equal is at least $1 - \frac n p$.

Considering that in general graph maximum matching $n$ basically does not exceed $10^3$, in practice taking $p$ as a prime on the order of $10^9$ is sufficient.

From the theorem, if we only need to find the maximum matching size without needing the matching scheme, then we only need to use one Gaussian elimination to find $\operatorname{rank}\tilde{A}$, which is much more concise than the blossom tree. But if we need to output the scheme, it will be a bit more complex, requiring the algorithm introduced below.

### Constructing a perfect matching

From Tutte's theorem and the above theorem, if $G$ has a perfect matching, then $\tilde{A}$ has a high probability of being full rank. For convenience, "with a high probability" is omitted in the following description.

Denote the point labeled $i$ in $G$ as $v_i$; further we have the following theorem:

**Theorem**: $\tilde{A}^{-1}_{j,i} \ne 0 \iff G - \{v_i, v_j\}$ has a perfect matching.

???+ tip "Inverse matrix and adjugate matrix"
    For any $n$-order square matrix $A$, define its adjugate matrix as $A^*_{i, j} = (-1)^{i + j} M_{j, i}$, where $M_{j, i}$ is the minor obtained by deleting row $j$ and column $i$. In other words, let the cofactor matrix of $A$ be $M$; then $A^* = M^T$.
    
    **Theorem**: if $A$ is invertible, then $A^{-1} = \frac 1 {\det A} A^*$.
    
    So here $A^{-1}_{j, i} \ne 0 \iff M_{i, j} \ne 0$, i.e. the part of $A$ after deleting row $i$ and column $j$ is full rank.

In other words, if $(v_i, v_j) \in E$ and $\tilde{A}^{-1}_{j, i} \ne 0$, it indicates that there exists a perfect matching scheme containing the edge $(v_i, v_j)$. Below this kind of edge is called a **feasible edge**.

From the above theorem, for an undirected graph $G$ with a perfect matching, we can obtain a relatively obvious brute-force algorithm to find a perfect matching: each time enumerate $i, j$; if $(v_i, v_j)$ is a feasible edge (the edge exists and $\tilde{A}^{-1}_{j, i} \ne 0$), then add $(v_i, v_j)$ to the matching scheme, delete both these two points in $G$, and recompute the new $\tilde{A}^{-1}$.

In total we do $\frac n 2$ rounds, each round is $O(n^3)$, and the total complexity is $O(n ^ 4)$, which is a bit slow. In fact, when recomputing $\tilde{A}^{-1}$, we do not have to use Gaussian elimination to find the inverse matrix from scratch each time, but can use the following theorem:

**Theorem** (elimination theorem): let

$$
A = \begin{bmatrix}
  a_{1, 1} & v^T \\
  u & B
\end{bmatrix} \quad A^{-1} = \begin{bmatrix}
  \hat a^{1, 1} & \hat v^T \\
  \hat u & \hat B
\end{bmatrix}
$$

and $\hat a_{1, 1} \ne 0$; then

$$
B^{-1} = \hat B - \frac {\hat u \hat v^T} {\hat a_{1, 1}}
$$

What the theorem describes is the case of eliminating the first row and first column. In fact, it can be very obviously generalized to the case of eliminating any row and column, so we only need to compute $\tilde{A}^{-1}$ once at the very beginning of the algorithm, and each time two points are deleted later, we only need to perform two $O(n^2)$ elimination processes.

??? note "The description is a bit abstract; you can refer to the C++ code"
    ```cpp
    void eliminate(int A[][MAXN], int r, int c) {  // eliminate row r and column c
      row_marked[r] = col_marked[c] = true;        // already eliminated
    
      int inv = quick_power(A[r][c], p - 2);  // inverse element
    
      for (int i = 1; i <= n; i++)
        if (!row_marked[i] && A[i][c]) {
          int tmp = (long long)A[i][c] * inv % p;
    
          for (int j = 1; j <= n; j++)
            if (!col_marked[j] && A[r][j])
              A[i][j] = (A[i][j] - (long long)tmp * A[r][j]) % p;
        }
    }
    ```

In total we do $\frac n 2$ rounds, each round with complexity $O(n^2)$, so the above algorithm can find a perfect matching in $O(n^3)$ time.

### Constructing the maximum matching

We have just solved the problem of constructing a perfect matching, but when solving problems we generally need the maximum matching.

As mentioned earlier, the size of the maximum matching of $G$ equals half of $\operatorname{rank}\tilde{A}$. If we can find a maximum full-rank submatrix of $\tilde{A}$, then finding a perfect matching of the induced subgraph corresponding to the submatrix gives a maximum matching of $G$.

Considering from another angle, if $G$ has a perfect matching, then $\tilde{A}$ is full rank, in other words, $\tilde{A}$ is linearly independent. So if $\tilde{A}$ is not full rank, we can find a linear basis of $\tilde{A}$, then keep only the rows and columns corresponding to the linear basis, and we can obtain a maximum full-rank submatrix of $\tilde{A}$.

After finding the maximum full-rank submatrix, use the above algorithm to find a perfect matching of the induced subgraph, and we obtain a maximum matching of the original graph. Note that since there may be row swaps in Gaussian elimination, in implementation we need to note maintaining the point numbers well.

??? note "[UOJ #79. General Graph Maximum Matching](https://uoj.ac/problem/79)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/general-match/general-match_2.cpp"
    ```

## Exercises

-   [UOJ #79. General Graph Maximum Matching](https://uoj.ac/problem/79)
-   [UOJ #171. 【WC2016】Challenge NPC](https://uoj.ac/problem/171)

## References

1.  Mucha M, Sankowski P. [Maximum matchings via Gaussian elimination](http://web.eecs.umich.edu/~pettie/matching/Mucha-Sankowski-maximum-matching-matrix-multiplication.pdf)
2.  Zhou Zixin, Yang Jiaqi "General graph matching based on linear algebra"
3.  ZYQN ["General graph matching algorithm based on linear algebra"](https://oi.cyo.ng/wp-content/uploads/2017/02/maximum_matchings_via_gaussian_elimination.pdf)
