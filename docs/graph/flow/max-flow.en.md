This page mainly introduces the algorithmic knowledge related to the maximum flow problem.

## Overview

For the basic concepts of network flow, see [Introduction to network flow](../flow.md).

Let $G=(V,E)$ be a network with source and sink points; we hope to assign a suitable flow $f$ on $G$ to maximize the flow value $|f|$ of the whole network (i.e. $\sum_{x \in V} f(s, x) - \sum_{x \in V} f(x, s)$); this problem is called the Maximum flow problem.

## Ford–Fulkerson augmentation

Ford–Fulkerson augmentation is a general term for a class of algorithms that compute the maximum flow. This method uses the greedy idea, updating and solving the maximum flow by finding augmenting paths.

### Overview

Given a network $G$ and a flow $f$ on $G$, we make the following definitions.

For an edge $(u, v)$, we call the difference between its capacity and flow the residual capacity $c_f(u,v)$, i.e. $c_f(u,v)=c(u,v)-f(u,v)$.

We call the subgraph composed of all nodes in $G$ and the edges with residual capacity greater than $0$ the residual network $G_f$, i.e. $G_f=(V,E_f)$, where $E_f=\left\{(u,v) \mid c_f(u,v)>0\right\}$.

???+ warning "Warning"
    As we will soon mention, the flow may be a negative value, so the edges of $E_f$ may not be in $E$. After introducing the concept of augmentation, this will be specifically explained below.

We call a path from the source $s$ to the sink $t$ on $G_f$ an augmenting path. For an augmenting path, we add an equal amount of flow to each edge $(u, v)$ to increase the flow value of the whole network; this process is called augmentation. Thus, the solving of the maximum flow can be regarded as the superposition of the flows obtained from several augmentations.

In addition, in the process of Ford–Fulkerson augmentation, for each edge $(u, v)$, we create a reverse edge $(v, u)$. We stipulate $f(u, v) = -f(v, u)$; this property can be guaranteed by introducing a flow-return operation in each augmentation, i.e. when $f(u, v)$ increases, $f(v, u)$ should decrease by the same amount.

???+ tip "Tip"
    In the code implementation of the maximum flow algorithm, we often need to support the operation of quickly accessing the reverse edge. In an adjacency matrix, this operation is trivial ($g_{u, v} \leftrightarrow g_{v, u}$). But the mainstream implementation is the more excellent chained forward star. Among them, a common technique is that we number the edges starting from an even number (usually $0$), and when adding an edge always immediately add its reverse edge so that their numbers are adjacent. Thus, we can make the edge numbered $i$ and the edge numbered $i \oplus 1$ always maintain a mutually-reverse-edge relationship.

Readers first encountering this method may notice a counterintuitive situation—the flow $f(v, u)$ of the reverse edge may be a negative value. In fact we can note that in the process of Ford–Fulkerson augmentation, what is truly meaningful is the residual capacity $c_f$, and the absolute value of $f(v, u)$ is irrelevant; we can regard the decrease of the reverse-edge flow as the increase of the reverse-edge residual capacity $c_f(v, u)$—this also coincides with the meaning of flow-return—the increase of the reverse-edge residual capacity means that we may next offset the original forward augmentation by walking the reverse edge, representing a kind of "regret" operation.

The following case may help you understand this process. Suppose $G$ is a unit-capacity network; we consider the following process:

-   There are multiple augmenting paths on $G$; among them, we choose to perform one augmentation passing successively through $u, v$ (as shown in the left figure), increasing the flow value by $1$.
-   We note that if we perform the augmentation in the middle figure, this local maximum flow value is not $1$ but $2$. But because the edges pointing to $u$ and the edges starting from $v$ exhausted their capacity in the first augmentation, at this point we cannot perform the augmentation in the middle figure. This means our current flow is not good enough, but locally there may be no other augmenting paths (only passing through edges in the original graph and not passing through reverse edges).
-   Now introduce the flow-return operation. After the first augmentation, flow-return means $c_f(v, u)$ increased by $1$ residual capacity, i.e. equivalent to newly adding the edge $(v, u)$, so we can perform another augmentation passing successively through $p, v, u, q$ (as shown by the orange path in the right figure). The flow on the undirected edge $(u, v)$ is offset in the two augmentations, and we surprisingly find that the result of superposing the two augmentations is actually equivalent to the middle figure.

![](./images/flow2.png)

The above case tells us that the "offset" effect brought by the flow-return operation makes us not need to worry about choosing augmenting paths in the "wrong" order.

It is easy to find that as long as there is an augmenting path on $G_f$, augmenting it can increase the total flow value; otherwise it means the total flow value has already reached the maximum possible value, and the solving process is complete. This is the process of Ford–Fulkerson augmentation.

### Max-flow min-cut theorem

We have roughly understood the idea of Ford–Fulkerson augmentation, but how to prove the correctness of this method? Why is the flow $f$ after augmentation ends a maximum flow?

In fact, the correctness of Ford–Fulkerson augmentation is equivalent to the Maxflow-Mincut Theorem. This theorem states that for any network $G = (V, E)$, its maximum flow $f$ and minimum cut $\{S, T\}$ always satisfy $|f| = ||S, T||$.

To prove the max-flow min-cut theorem, we first start from a lemma: for a network $G = (V, E)$, for any flow $f$ and any cut $\{S, T\}$, there is always $|f| \leq ||S, T||$, where equality holds if and only if all edges of $\{(u, v) | u \in S, v \in T\}$ are at full flow, and all edges of $\{(u, v) | u \in T, v \in S\}$ are at zero flow.

???+ note "Proof"
    $$
    \begin{aligned}
    |f| & = f(s) \\
        & = \sum_{u \in S} f(u) \\
        & = \sum_{u \in S} \left( \sum_{v \in V} f(u, v) - \sum_{v \in V} f(v, u) \right) \\
        & = \sum_{u \in S} \left( \sum_{v \in T} f(u, v) + \sum_{v \in S} f(u, v) - \sum_{v \in T} f(v, u) - \sum_{v \in S} f(v, u) \right) \\
        & = \sum_{u \in S} \left( \sum_{v \in T} f(u, v) - \sum_{v \in T} f(v, u) \right) + \sum_{u \in S} \sum_{v \in S} f(u, v) - \sum_{u \in S} \sum_{v \in S} f(v, u) \\
        & = \sum_{u \in S} \left( \sum_{v \in T} f(u, v) - \sum_{v \in T} f(v, u) \right) \\
        & \leq \sum_{u \in S} \sum_{v \in T} f(u, v) \\
        & \leq \sum_{u \in S} \sum_{v \in T} c(u, v) \\
        & = ||S, T|| \\
    \end{aligned}
    $$
    
    To achieve equality, the first inequality requires all edges of $\{(u, v) \mid u \in T, v \in S\}$ to be at zero flow, and the second inequality requires all edges of $\{(u, v) \mid u \in S, v \in T\}$ to be at full flow. The lemma is proved.

So, for any network, can the above equality condition always be satisfied? If the answer is affirmative, then the max-flow min-cut theorem is proved. Below we attempt to prove it.

???+ note "Proof"
    Suppose after a certain round of augmentation, we obtain a flow $f$ such that there is no augmenting path on $G_f$, i.e. there is no path from $s$ to $t$ on $G_f$. At this point we denote the point set composed of the nodes reachable from $s$ as $S$, and denote $T = V \setminus S$.
    
    Obviously, $\{S, T\}$ is a cut of $G_f$, and $||S, T|| = \sum_{u \in S} \sum_{v \in T} c_f(u, v) = 0$. Since the residual capacity is non-negative, this also means that for any $u \in S, v \in T, (u, v) \in E_f$, there is $c_f(u, v) = 0$. Below we discuss these edges in two cases, edges existing in the original graph and reverse edges:
    
    -   $(u, v) \in E$: at this point, $c_f(u, v) = c(u, v) - f(u, v) = 0$, so $c(u, v) = f(u, v)$, i.e. all edges of $\{(u, v) \mid u \in S, v \in T\}$ are at full flow;
    -   $(v, u) \in E$: at this point, $c_f(u, v) = c(u, v) - f(u, v) = 0 - f(u, v) = f(v, u) = 0$, i.e. all edges of $\{(v, u) \mid u \in S, v \in T\}$ are at zero flow.
    
    Therefore, after augmentation stops, the above flow $f$ satisfies the equality condition. According to the size relationship indicated by the lemma, naturally, $f$ is a maximum flow of $G$, and $\{S, T\}$ is a minimum cut of $G$.

It is easy to see that Kőnig's theorem is a special case of the max-flow min-cut theorem. In fact, they are both related to duality in linear programming.

### Time-complexity analysis

On a network $G = (V, E)$ with integer flows, trivially, we assume the flow of each augmentation is an integer, then an upper bound of the time complexity of Ford–Fulkerson augmentation is $O(|E||f|)$, where $f$ is the maximum flow on $G$. This is because the time complexity of a single round of augmentation is $O(|E|)$, and augmentation will cause the total flow value to increase, so the number of augmentation rounds cannot exceed $|f|$.

For different implementations of Ford–Fulkerson augmentation, the time complexity also differs. Among them, the more mainstream implementations include algorithms such as Edmonds–Karp, Dinic, SAP, ISAP, etc., which we will introduce separately below.

### Edmonds–Karp algorithm

#### Algorithm idea

How to find augmenting paths in $G_f$? When we consider the specific implementation of Ford–Fulkerson augmentation, the most natural scheme is to use BFS. At this point, Ford–Fulkerson augmentation manifests as the Edmonds–Karp algorithm. Its specific process is as follows:

-   If on $G_f$ we can BFS from $s$ to $t$, then we found a new augmenting path.

-   For the augmenting path $p$, we compute the minimum of the residual capacities of the edges $p$ passes through, $\Delta = \min_{(u, v) \in p} c_f(u, v)$. We add $\Delta$ flow to each edge on $p$, and return $\Delta$ flow from their reverse edges, increasing the maximum flow by $\Delta$.

-   Because we modified the flow, we obtain a new $G_f$; we repeat the above process on the new $G_f$ until no augmenting path exists, then the flow value no longer increases.

The above algorithm is the Edmonds–Karp algorithm.

#### Time-complexity analysis

Next let us try to analyze the time complexity of the Edmonds–Karp algorithm.

Obviously, the time complexity of a single round of BFS augmentation is $O(|E|)$.

The upper bound of the total number of augmentation rounds is $O(|V||E|)$. This assertion is often given a false proof (or vaguely glossed over) in online materials. Below we attempt to give a more formal proof[^ref_ek].

???+ note "Proof of the upper bound of the total number of augmentation rounds"
    First, we introduce a lemma—the shortest-path non-decreasing lemma. Specifically, we denote $d_f(u)$ as the distance from node $u$ to the source $s$ on $G_f$ (i.e. the shortest-path length, likewise below). For a certain round of augmentation, we use $f$ and $f'$ to denote the flow before augmentation and the flow after augmentation respectively; we assert that for any node $u$, augmentation always makes $d_{f'}(u) \geq d_f(u)$. We will prove this lemma later.
    
    We may as well call the edge with the smallest residual capacity on the augmenting path the saturating edge (if there are multiple smallest edges, take any one). If a directed edge $(u, v)$ is chosen as the saturating edge, augmentation will empty its residual capacity causing the saturating edge to disappear, and flow-return will cause the reverse edge to be newly added (if the reverse edge did not exist before), i.e. $(u, v) \not \in E_{f'}$ and $(v, u) \in E_{f'}$. The above analysis lets us know that for an undirected edge $(u, v)$, its two augmented directions always appear alternately.
    
    When augmenting along $(u, v)$ on $G_f$, $d_f(u) + 1 = d_f(v)$; afterwards the residual network becomes $G_{f'}$. When augmenting along $(v, u)$ on $G_{f'}$, $d_{f'}(v) + 1 = d_{f'}(u)$. According to the shortest-path non-decreasing lemma we also have $d_{f'}(v) \geq d_f(v)$; connecting all the equations, we obtain $d_{f'}(u) \geq d_{f}(u) + 2$. In other words, if a directed edge $(u, v)$ is chosen as the saturating edge, then compared with the last time it was chosen as the saturating edge, the distance from $u$ to $s$ increases by at least $2$.
    
    The distance from $s$ to any node cannot exceed $|V|$; combined with the above property, we find that the number of times each edge is chosen as the saturating edge is $O(|V|)$; multiplied by the number of edges, we obtain the upper bound of the total number of augmentation rounds, $O(|V||E|)$.
    
    Next we prove the shortest-path non-decreasing lemma, i.e. $d_{f'}(u) \geq d_f(u)$. This proof is not hard, but may be a bit convoluted; the reader may pause to think carefully for a moment.
    
    ???+ note "Proof of the shortest-path non-decreasing lemma"
        Consider proof by contradiction. For a certain round of augmentation, we assume there exist several nodes whose distance to $s$ after this round of augmentation is smaller than before augmentation. We denote $v$ as the one among them with the smallest distance to $s$ (i.e. $v = \arg \min_{x \in V, d_{f'}(x) < d_f(x)} d_{f'}(x)$). Note that according to the contradiction assumption, at this point $d_{f'}(v) < d_f(v)$ is a known condition.
        
        On the shortest path from $s$ to $v$ in $G_{f'}$, we denote $u$ as the previous node of $v$, i.e. $d_{f'}(u) + 1 = d_{f'}(v)$.
        
        In order not to let $u$ break the "smallest distance" property of $v$, $u$ must satisfy $d_{f'}(u) \geq d_f(u)$.
        
        For the above expression, we add to both sides of the inequality, obtaining $d_{f'}(v) \geq d_f(u) + 1$. Scaling according to the contradiction assumption, we obtain $d_f(v) > d_f(u) + 1$.
        
        Below we attempt to discuss the augmentation direction on $(u, v)$.
        
        -   Suppose the directed edge $(u, v) \in E_f$. According to the "breadth-first" property of BFS, we have $d_f(u) + 1 \geq d_f(v)$. This expression conflicts with the scaling result, deriving a contradiction.
        -   Suppose the directed edge $(u, v) \not \in E_f$. According to the definition of $u$ we already know $(u, v) \in E_{f'}$, so the existence of this edge must be the result of the current round's augmentation passing through $(v, u)$ and returning flow to produce the reverse edge, i.e. $d_f(v) + 1 = d_f(u)$. This expression conflicts with the scaling result, deriving a contradiction.
        
        Since augmenting $(u, v)$ in any direction derives a contradiction, we know the contradiction assumption does not hold, and the shortest-path non-decreasing lemma is proved.

Multiplying the complexity of a single round of BFS augmentation by the upper bound of the number of augmentation rounds, we obtain that the time complexity of the Edmonds–Karp algorithm is $O(|V||E|^2)$.

#### Code implementation

A possible implementation of the Edmonds–Karp algorithm is as follows.

??? note "Reference code"
    ```cpp
    constexpr int MAXN = 250;
    constexpr int INF = 0x3f3f3f3f;
    
    struct Edge {
      int from, to, cap, flow;
    
      Edge(int u, int v, int c, int f) : from(u), to(v), cap(c), flow(f) {}
    };
    
    struct EK {
      int n, m;             // n: number of points, m: number of edges
      vector<Edge> edges;   // edges: the set of all edges
      vector<int> G[MAXN];  // G: the indices in edges of all edges from point x -> x
      int a[MAXN], p[MAXN];  // a: the maximum flow given to point x by the edge nearest to point x during BFS
                             // p: the edge nearest to point x during BFS
    
      void init(int n) {
        for (int i = 0; i < n; i++) G[i].clear();
        edges.clear();
      }
    
      void AddEdge(int from, int to, int cap) {
        edges.push_back(Edge(from, to, cap, 0));
        edges.push_back(Edge(to, from, 0, 0));
        m = edges.size();
        G[from].push_back(m - 2);
        G[to].push_back(m - 1);
      }
    
      int Maxflow(int s, int t) {
        int flow = 0;
        for (;;) {
          memset(a, 0, sizeof(a));
          queue<int> Q;
          Q.push(s);
          a[s] = INF;
          while (!Q.empty()) {
            int x = Q.front();
            Q.pop();
            for (int i = 0; i < G[x].size(); i++) {  // traverse the edges with x as the start
              Edge& e = edges[G[x][i]];
              if (!a[e.to] && e.cap > e.flow) {
                p[e.to] = G[x][i];  // G[x][i] is the edge nearest to point e.to
                a[e.to] =
                    min(a[x], e.cap - e.flow);  // the flow given to it by the edge nearest to point e.to
                Q.push(e.to);
              }
            }
            if (a[t]) break;  // if the sink received flow, exit BFS
          }
          if (!a[t])
            break;  // if the sink did not receive flow, the source and sink are not in the same connected component
          for (int u = t; u != s;
               u = edges[p[u]].from) {  // trace the s -> t path during BFS via u
            edges[p[u]].flow += a[t];      // increase the flow value of the edges on the path
            edges[p[u] ^ 1].flow -= a[t];  // decrease the flow value of the reverse path
          }
          flow += a[t];
        }
        return flow;
      }
    };
    ```

### Dinic algorithm

#### Algorithm idea

Consider first performing BFS layering on $G_f$ before augmentation, i.e. dividing the nodes into several layers according to the distance $d(u)$ from node $u$ to the source $s$. Let the flow passing through $u$ only flow to nodes $v$ of the next layer, i.e. delete the out-edges from $u$ to nodes with equal or smaller layer numbers; we call the remaining part of $G_f$ the level graph. Formally, we call $G_L = (V, E_L)$ the level graph of $G_f = (V, E_f)$, where $E_L = \left\{ (u, v) \mid (u, v) \in E_f, d(u) + 1 = d(v) \right\}$.

If we find a maximal augmenting flow $f_b$ on the level graph $G_L$ such that it is impossible to further expand the flow $f_b$ only on $G_L$, then we call $f_b$ a blocking flow of $G_L$.

??? warning "Warning"
    Although above we only defined augmentation/augmenting flow on a single augmenting path, in a broad sense, the word "augmentation" can be used not only for the augmenting flow on a single path, but also for the union of several augmenting flows—the latter is the meaning used when we define a blocking flow.

After defining the level graph and blocking flow, the process of the Dinic algorithm is as follows.

1.  BFS the level graph $G_L$ on $G_f$.
2.  DFS the blocking flow $f_b$ on $G_L$.
3.  Add $f_b$ into the original flow $f$, i.e. $f \leftarrow f + f_b$.
4.  Repeat the above process until there is no path from $s$ to $t$.

At this point $f$ is the maximum flow.

Before analyzing the complexity of this algorithm, we need to specifically explain the process of "DFS the blocking flow $f_b$ on $G_L$". Although BFS the level graph should be trivial for readers of this page, the process of DFS the blocking flow requires a bit of technique—we need to introduce the current-arc optimization.

Note that in the process of DFS on $G_L$, if node $u$ has a large number of both in-edges and out-edges, and $u$ traverses the out-edge list each time it receives flow from an in-edge to decide which out-edge to pass the flow to, then the local time complexity at $u$ can reach $O(|E|^2)$ in the worst case. To avoid this defect, if at some moment we already know that edge $(u, v)$ has been augmented to the limit (edge $(u, v)$ has no residual capacity or the rear side of $v$ has been augmented to blocking), then $u$'s flow need not try to flow to the out-edge $(u, v)$ anymore. Accordingly, for each node $u$, we maintain the first out-edge in $u$'s out-edge list that is still worth trying. Conventionally, we call this maintained pointer the current arc, and call this practice the current-arc optimization.

??? note "Multi-path augmentation"
    Multi-path augmentation is a constant-factor optimization of the Dinic algorithm—if we find an augmenting path $p$ from $s$ to $t$ on the level graph, then next we do not necessarily need to re-find the next augmenting path starting from $s$, but may find a fork for augmentation starting from the last position on $p$ that still has residual capacity. Considering its consistency with the backtracking form, this optimization is also natural in the code implementation of DFS.
    
    ??? failure "Common misconception"
        Possibly due to the erroneous statements in a large number of online materials causing a case of hearsay passing on errors, a considerable number of contestants like to juxtapose the current-arc optimization and multi-path augmentation as two optimizations of the Dinic algorithm. In fact, the current-arc optimization is part of guaranteeing the correctness of the Dinic time complexity, while multi-path augmentation is just a constant-factor optimization that does not affect the complexity.

#### Time-complexity analysis

After applying the current-arc optimization, the time-complexity analysis of the Dinic algorithm is as follows.

First, we attempt to prove that the time complexity of DFS finding the blocking flow in a single round of augmentation is $O(|V||E|)$.

???+ note "Proof of the time complexity of a single round of augmentation"
    Consider each augmenting path in the blocking flow $f_b$; they are all the result of jumping along the current arc each time on $G_L$, where the number of jumps experienced by each augmenting path cannot be more than $|V|$.
    
    Each time an augmenting path is found, one saturating edge disappears (residual capacity cleared to zero). Consider each augmenting path in the blocking flow $f_b$; we denote the edge set formed by the saturating edges cleared to zero by them as $E_1$. Considering the layering property of $G_L$, after a saturating edge disappears its reverse edge cannot be passed by other augmenting paths within the same round of augmentation, so $E_1$ is a subset of $E_L$.
    
    In addition, for the case where jumping along the current arc but not successfully obtaining an augmenting path due to blocking at a certain position, we denote the edge set formed by the last edge on these incomplete paths as $E_2$. The members of $E_2$ are unsaturated, so $E_1$ and $E_2$ are disjoint, and $E_1 \cup E_2$ is still a subset of $E_L$.
    
    Since each member of $E_1 \cup E_2$ costs no more than $|V|$ jumps (and after using the multi-path augmentation optimization some jumps will be double-counted), therefore, in summary, the total number of jumps in the DFS process cannot be more than $|V||E_L|$.
    
    ??? failure "A common false proof"
        For each node, we maintain the next edge that can be augmented, and the current arc changes at most $|E|$ times, so the worst-case time complexity of a single round of augmentation is $O(|V||E|)$.
    
    ??? bug "Bug"
        "The current arc changes at most $|E|$ times" cannot deduce "each node accesses its out-edges at most $|E|$ times". This is because accessing the current arc does not necessarily exhaust the residual capacity on it, and node $u$ may access the same current arc multiple times.

Note that the number of layers of the level graph obviously cannot exceed $|V|$; if we can prove that the number of layers of the level graph strictly increases during augmentation, then the number of augmentation rounds of the Dinic algorithm is $O(|V|)$. Next we attempt to prove this conclusion[^ref_dinic].

???+ note "Proof of the monotonicity of the number of layers of the level graph"
    We need to introduce a concept from the preflow-push class of algorithms (another class of maximum flow algorithms)—the height label. To more conveniently express our proof in combination with the height label, in the proof process, we let $d_f(u)$ be the distance from node $u$ to the **sink** $t$ on $G_f$, layering starting from the **sink** rather than the source (this makes no essential difference). For a certain round of augmentation, we use $f$ and $f'$ to denote the flow before augmentation and the flow after augmentation respectively. After solving and adding the blocking flow in this round of augmentation, denote the level graph changing from $G_L = (V, E_L)$ to $G'_{L} = (V, E'_L)$.
    
    We give the height label a non-rigorous temporary definition—on a network $G = (V, E)$, let $h$ be a function from the point set $V$ to the integer set $N$; $h$ is a valid height label on $G$ if and only if $h(u) \leq h(v) + 1$ holds for $(u, v) \in E$.
    
    Examining all members $(u, v)$ of $E_{f'}$, we find that the reason $(u, v) \in E_{f'}$ is one of the following two.
    
    -   $(u, v) \in E_f$, and the residual capacity was not exhausted in this round of augmentation—according to the definition of the shortest path, at this point we have $d_f(u) \leq d_f(v) + 1$;
    -   $(u, v) \not \in E_f$, but during this round of augmentation the blocking flow passed through $(v, u)$ and returned flow to produce the reverse edge—according to the definition of the level graph and blocking flow, at this point we have $d_f(u) + 1 = d_f(v)$.
    
    The above observation lets us reach a conclusion—$d_f$ is a valid height label on $G_{f'}$. Of course, it is also on the subgraph $G'_L$ of $G_{f'}$.
    
    Now, for an augmenting path $p = (s, \dots, u, v, \dots, t)$ on $G'_L$, consider the process of adding one node at a time starting from the empty path in the reverse order of the nodes on $p$ (the order from $t$ to $s$). Suppose node $v$ has been added and node $u$ is being added; we find that after adding node $u$, according to the definition of the level graph, the value of $d_{f'}(u)$ increases by $1$ compared with $d_{f'}(v)$; at the same time, since $d_f$ is a height label on $G'_L$, the value of $d_f(u)$ may either increase by $1$ compared with $d_f(v)$, or remain unchanged or decrease. Therefore, after the whole path is added, we obtain $d_{f'}(s) \geq d_f(s)$, where the necessary and sufficient condition for equality is that $d_f(u) = d_f(v) + 1$ holds for $(u, v) \in p$. If this inequality cannot achieve equality, then $d_{f'}(s) > d_f(s)$—i.e. the conclusion we want, "the number of layers of the level graph strictly increases during augmentation". Below we attempt to prove that this inequality cannot achieve equality.
    
    Consider proof by contradiction; we assume $d_{f'}(s) = d_f(s)$ holds, and attempt to derive a contradiction. Now we assert that on $G'_L$, $p$ contains at least one edge $(u, v)$ satisfying that $(u, v)$ does not exist on $G_L$. If there is no such edge, considering that $d_f(s) = d_{f'}(s)$, combined with the definition of the level graph and blocking flow, the augmentation on $G_L$ should not be complete yet. In order not to produce the above contradiction, our assertion had better be correct.
    
    Let $(u, v)$ be the edge satisfying the assertion condition; the reason it satisfies the assertion can only be one of the following two.
    
    -   $(u, v) \in E_f$ but $d_f(u) \leq d_f(v) + 1$ does not achieve equality, so according to the definition of the level graph we know $(u, v) \not \in E_L$, and it was added to $E'_L$ in the new round of re-layering after augmentation;
    -   $(u, v) \not \in E_f$, which means the production of this edge $(u, v)$ is the result of the blocking flow passing through $(v, u)$ in the current round of augmentation and returning flow to produce the reverse edge, i.e. $d_f(u) = d_f(v) - 1$.
    
    Since no matter which way we satisfy the assertion we obtain $d_f(u) \neq d_f(v) + 1$, i.e. the necessary and sufficient condition for $d_{f'}(s) \geq d_f(s)$ to achieve equality cannot be satisfied, which conflicts with the contradiction assumption $d_{f'}(s) = d_f(s)$, the original proposition is proved.
    
    ??? failure "Another common false proof"
        Consider proof by contradiction. Suppose the number of layers of the level graph after one round of augmentation is equal to the original, then there should still exist at least one augmenting path from $s$ to $t$ on the level graph satisfying that the layer difference between two adjacent points is $1$. That this augmenting path was not augmented indicates that this round of augmentation is not yet complete. In order not to produce the above contradiction, the original proposition holds.
    
    ??? bug "Bug"
        "The $s$-$t$ shortest path on the new level graph after one round of augmentation is equal to the original" cannot deduce "this round of augmentation on the old level graph is not yet complete". This is because there is no reason to indicate that the edge sets of the two level graphs are the same; the $s$-$t$ shortest path on the new level graph may pass through edges that do not exist on the old level graph.

Multiplying the time complexity of a single round of augmentation $O(|V||E|)$ by the number of augmentation rounds $O(|V|)$, the time complexity of the Dinic algorithm is $O(|V|^2|E|)$.

If we need to make the actual running time of the Dinic algorithm approach its theoretical upper bound, we need to construct a network with special properties as input. Since in algorithm competition practice, the examination related to network-flow knowledge often focuses on the technique of modeling the original problem as a network-flow problem. At this point, our modeling usually does not contain the special properties that make the Dinic algorithm execute slowly; on the contrary, the Dinic algorithm is very efficient on most graphs. Therefore, the data range of network-flow problems is usually large, and the method of "substituting the values of $|V|, |E|$ into $|V|^2|E|$ to estimate the running time" is not applicable. In fact, making an accurate estimate requires the contestant to have some experience with the actual efficiency of the Dinic algorithm; the reader can practice more.

#### Time-complexity analysis in special cases

On some graphs with good properties, the Dinic algorithm has a better time complexity.

For a network $G = (V, E)$, if all its edge capacities are $1$, i.e. $c(u, v) \in \{0, 1\}$ holds for $(u, v) \in E$, then we call $G$ unit-capacity.

In a unit-capacity network, the time complexity of a single round of augmentation of the Dinic algorithm is $O(|E|)$.

???+ note "Proof"
    This is because each augmentation causes all edges on the augmenting path to be saturated and disappear, so each edge can only be augmented once in a single round of augmentation.

In a unit-capacity network, the number of augmentation rounds of the Dinic algorithm is $O(|E|^{\frac{1}{2}})$.

???+ note "Proof"
    Layering centered on the source $s$, denote $d_f(u)$ as the distance from node $u$ to the source $s$ on $G_f$. In addition, we define the point set $\left\{u \mid u \in V, d_f(u) = k \right\}$ as the layer numbered $k$, $D_k$, and denote $S_k = \cup_{i \leq k} D_i$.
    
    Suppose we have performed $|E|^{\frac{1}{2}}$ rounds of augmentation. By the pigeonhole principle, there exists at least one $k$ satisfying that the size of the edge set $\left\{ (u, v) \mid u \in D_k, v \in D_{k+1}, (u, v) \in E_f \right\}$ does not exceed $\frac {|E|} {|E|^{\frac{1}{2}}} \approx |E|^{\frac{1}{2}}$. Obviously, $\{S_k, V - S_k\}$ is an $s$-$t$ cut on $G_f$, and its cut capacity does not exceed $|E|^{\frac{1}{2}}$. According to the max-flow min-cut theorem, the maximum flow on $G_f$ does not exceed $|E|^{\frac{1}{2}}$, i.e. at most $|E|^{\frac{1}{2}}$ more rounds of augmentation can be performed on $G_f$. Therefore, the total number of augmentation rounds is $O(|E|^{\frac{1}{2}})$.

In a unit-capacity network, the number of augmentation rounds of the Dinic algorithm is $O(|V|^{\frac{2}{3}})$.

???+ note "Proof"
    Suppose we have performed $2 |V|^{\frac{2}{3}}$ rounds of augmentation. Since at most half of the ($|V|^{\frac{2}{3}}$) layers contain more than $|V|^{\frac{1}{3}}$ points, no matter how we allocate the sizes of all layers, there exists at least one $k$ satisfying that two adjacent layers simultaneously contain no more than $|V|^{\frac{1}{3}}$ points, i.e. $|D_k| \leq |V|^{\frac{1}{3}}$ and $|D_{k+1}| \leq |V|^{\frac{1}{3}}$.
    
    To maximize the number of edges between $D_k$ and $D_{k+1}$, we assume this is a complete bipartite graph, at which point the size of the edge set $\left\{ (u, v) \mid u \in D_k, v \in D_{k+1}, (u, v) \in E_f \right\}$ does not exceed $|V|^{\frac{2}{3}}$. Obviously, $\{S_k, V - S_k\}$ is an $s$-$t$ cut on $G_f$, and its cut capacity does not exceed $|V|^{\frac{2}{3}}$. According to the max-flow min-cut theorem, the maximum flow on $G_f$ does not exceed $|V|^{\frac{2}{3}}$, i.e. at most $|V|^{\frac{2}{3}}$ more rounds of augmentation can be performed on $G_f$. Therefore, the total number of augmentation rounds is $O(|V|^{\frac{2}{3}})$.

In a unit-capacity network, if every node $u$ except the source and sink satisfies $\mathit{deg}_{\mathit{in}}(u) = 1$ or $\mathit{deg}_{\mathit{out}}(u) = 1$, then the number of augmentation rounds of the Dinic algorithm is $O(|V|^{\frac{1}{2}})$. Here, $\mathit{deg}_{\mathit{in}}(u)$ and $\mathit{deg}_{\mathit{out}}(u)$ represent the in-degree and out-degree of node $u$ respectively.

???+ note "Proof"
    We introduce the following lemma—for a network of this form, any flow on it can always be decomposed into several unit-flow, **vertex-disjoint** augmenting paths.
    
    Suppose we have performed $|V|^{\frac{1}{2}}$ rounds of augmentation. According to the definition of the level graph, at this point the length of any new augmenting path is at least $|V|^{\frac{1}{2}}$.
    
    Considering the augmenting-path decomposition of the maximum flow on $G_f$, the number of augmenting paths we obtain cannot be more than $\frac {|V|} {|V|^{\frac{1}{2}}} \approx |V|^{\frac{1}{2}}$, which means at most $|V|^{\frac{1}{2}}$ more rounds of augmentation can be performed on $G_f$. Therefore, the total number of augmentation rounds is $O(|V|^{\frac{1}{2}})$.

In summary, we reach some corollaries.

-   On a unit-capacity network, the total time complexity of the Dinic algorithm is $O(|E| \min(|E|^\frac{1}{2}, |V|^{\frac{2}{3}}))$.
-   On a unit-capacity network, if every node $u$ except the source and sink satisfies $\mathit{deg}_{\mathit{in}}(u) = 1$ or $\mathit{deg}_{\mathit{out}}(u) = 1$, the total time complexity of the Dinic algorithm is $O(|E||V|^{\frac{1}{2}})$. For the bipartite-graph maximum matching problem, we often use the Hopcroft–Karp algorithm to solve it, and this algorithm is actually a special case of the Dinic algorithm on a unit-capacity network satisfying the above degree constraint.

#### Code implementation

??? note "Reference code"
    ```cpp
    struct MF {
      struct edge {
        int v, nxt, cap, flow;
      } e[N];
    
      int fir[N], cnt = 0;
    
      int n, S, T;
      ll maxflow = 0;
      int dep[N], cur[N];
    
      void init() {
        memset(fir, -1, sizeof fir);
        cnt = 0;
      }
    
      void addedge(int u, int v, int w) {
        e[cnt] = {v, fir[u], w, 0};
        fir[u] = cnt++;
        e[cnt] = {u, fir[v], 0, 0};
        fir[v] = cnt++;
      }
    
      bool bfs() {
        queue<int> q;
        memset(dep, 0, sizeof(int) * (n + 1));
    
        dep[S] = 1;
        q.push(S);
        while (q.size()) {
          int u = q.front();
          q.pop();
          for (int i = fir[u]; ~i; i = e[i].nxt) {
            int v = e[i].v;
            if ((!dep[v]) && (e[i].cap > e[i].flow)) {
              dep[v] = dep[u] + 1;
              q.push(v);
            }
          }
        }
        return dep[T];
      }
    
      int dfs(int u, int flow) {
        if ((u == T) || (!flow)) return flow;
    
        int ret = 0;
        for (int& i = cur[u]; ~i; i = e[i].nxt) {
          int v = e[i].v, d;
          if ((dep[v] == dep[u] + 1) &&
              (d = dfs(v, min(flow - ret, e[i].cap - e[i].flow)))) {
            ret += d;
            e[i].flow += d;
            e[i ^ 1].flow -= d;
            if (ret == flow) return ret;
          }
        }
        return ret;
      }
    
      void dinic() {
        while (bfs()) {
          memcpy(cur, fir, sizeof(int) * (n + 1));
          maxflow += dfs(S, INF);
        }
      }
    } mf;
    ```

### MPM algorithm

The **MPM** (Malhotra, Pramodh-Kumar and Maheshwari) algorithm obtains the maximum flow in two ways: using a heap-based priority queue, with time complexity $O(n^3\log n)$; the commonly-used BFS solution, with time complexity $O(n^3)$. Note that this section only focuses on analyzing the better and more concise $O(n^3)$ algorithm.

The overall structure of the MPM algorithm is similar to the Dinic algorithm, also running in phases. In each phase, an augmenting path is found in the layered network of the residual network of $G$. Its main difference from the Dinic algorithm is the different way of finding augmenting paths: the part of finding augmenting paths in the MPM algorithm only takes $O(n^2)$, with a better time complexity than the Dinic algorithm.

The MPM algorithm needs to consider the capacity of vertices rather than edges. In the layered network $L$, if we define the capacity $p(v)$ of a point $v$ as the minimum of its incoming residual and outgoing residual, then:

$$
\begin{aligned}
p_{in}(v) &= \sum\limits_{(u,v) \in L} (c(u, v) - f(u, v)) \\
p_{out}(v) &= \sum\limits_{(v,u) \in L} (c(v, u) - f(v, u)) \\
p(v) &= \min (p_{in}(v), p_{out}(v))
\end{aligned}
$$

We call node $r$ a reference node if and only if $p(r) = \min {p(v)}$. For a reference node $r$, we can definitely increase the flow through $r$ by $p(r)$ to make its capacity become $0$. This is because $L$ is a directed acyclic graph and the node capacities in $L$ are at least $p(r)$, so we can definitely find a directed path from $s$ through $r$ to $t$. Then we just increase the edge flow on this path by $p(r)$. This path is the augmenting path of this phase. Finding the augmenting path can use BFS. After augmentation, all full-flow edges can be deleted from $L$, because they will not be used after this phase. Similarly, all nodes different from $s$ and $t$ and having no out-edge or in-edge can be deleted.

#### Time-complexity analysis

Each phase of the MPM algorithm needs $O(V^2)$, because there are at most $V$ iterations (because at least the chosen reference node is deleted), and in each iteration, we delete all passed edges except at most $V$. Summing up, we obtain $O(V^2+E)=O(V^2)$. Since the total number of phases is less than $V$, the total running time of the MPM algorithm is $O(V^3)$.

???+ note "Proof that the total number of phases is less than V"
    The MPM algorithm ends within fewer than $V$ phases. To prove this, we must first prove two lemmas.
    
    **Lemma 1**: after each iteration, the distance from $s$ to each point does not decrease, that is, $level_{i+1}[v] \ge level_{i}[v]$.
    
    **Proof**: fix a phase $i$ and a point $v$. Consider any shortest path $P$ from $s$ to $v$ in $G_{i}^R$. The length of $P$ equals $level_{i}[v]$. Note that $G_{i}^R$ can only contain the backward edges and forward edges of $G_{i}^R$. If $P$ has no backward edge of $G_{i}^R$, then $level_{i+1}[v] \ge level_{i}[v]$, because $P$ is also a path in $G_{i}^R$. Now, suppose $P$ has at least one backward edge and the first such edge is $(u,w)$, then $level_{i+1}[u] \ge level_{i}[u]$ (because of the first case). The edge $(u,w)$ does not belong to $G_{i}^R$, so $(u,w)$ is affected by the augmenting path of the previous iteration. This means $level_{i}[u] = level_{i}[w]+1$. In addition, $level_{i+1}[w] = level_{i+1}[u]+1$. From these two equations and $level_{i+1}[u] \ge level_{i}[u]$ we obtain $level_{i+1}[w] \ge level_{i}[w]+2$. The remaining part of the path can also use the same idea.
    
    **Lemma 2**: $level_{i+1}[t] > level_{i}[t]$.
    
    **Proof**: from Lemma 1 we conclude that $level_{i+1}[t] \ge level_{i}[t]$. Suppose $level_{i+1}[t] = level_{i}[t]$; note that $G_{i}^R$ can only contain the backward edges and forward edges of $G_{i}^R$. This means there is a shortest path in $G_{i}^R$ not blocked by an augmenting path. This forms a contradiction.

#### Implementation

??? note "Reference code"
    ```cpp
    struct MPM {
      struct FlowEdge {
        int v, u;
        long long cap, flow;
    
        FlowEdge() {}
    
        FlowEdge(int _v, int _u, long long _cap, long long _flow)
            : v(_v), u(_u), cap(_cap), flow(_flow) {}
    
        FlowEdge(int _v, int _u, long long _cap)
            : v(_v), u(_u), cap(_cap), flow(0ll) {}
      };
    
      constexpr static long long flow_inf = 1e18;
      vector<FlowEdge> edges;
      vector<char> alive;
      vector<long long> pin, pout;
      vector<list<int>> in, out;
      vector<vector<int>> adj;
      vector<long long> ex;
      int n, m = 0;
      int s, t;
      vector<int> level;
      vector<int> q;
      int qh, qt;
    
      void resize(int _n) {
        n = _n;
        ex.resize(n);
        q.resize(n);
        pin.resize(n);
        pout.resize(n);
        adj.resize(n);
        level.resize(n);
        in.resize(n);
        out.resize(n);
      }
    
      MPM() {}
    
      MPM(int _n, int _s, int _t) {
        resize(_n);
        s = _s;
        t = _t;
      }
    
      void add_edge(int v, int u, long long cap) {
        edges.push_back(FlowEdge(v, u, cap));
        edges.push_back(FlowEdge(u, v, 0));
        adj[v].push_back(m);
        adj[u].push_back(m + 1);
        m += 2;
      }
    
      bool bfs() {
        while (qh < qt) {
          int v = q[qh++];
          for (int id : adj[v]) {
            if (edges[id].cap - edges[id].flow < 1) continue;
            if (level[edges[id].u] != -1) continue;
            level[edges[id].u] = level[v] + 1;
            q[qt++] = edges[id].u;
          }
        }
        return level[t] != -1;
      }
    
      long long pot(int v) { return min(pin[v], pout[v]); }
    
      void remove_node(int v) {
        for (int i : in[v]) {
          int u = edges[i].v;
          auto it = find(out[u].begin(), out[u].end(), i);
          out[u].erase(it);
          pout[u] -= edges[i].cap - edges[i].flow;
        }
        for (int i : out[v]) {
          int u = edges[i].u;
          auto it = find(in[u].begin(), in[u].end(), i);
          in[u].erase(it);
          pin[u] -= edges[i].cap - edges[i].flow;
        }
      }
    
      void push(int from, int to, long long f, bool forw) {
        qh = qt = 0;
        ex.assign(n, 0);
        ex[from] = f;
        q[qt++] = from;
        while (qh < qt) {
          int v = q[qh++];
          if (v == to) break;
          long long must = ex[v];
          auto it = forw ? out[v].begin() : in[v].begin();
          while (true) {
            int u = forw ? edges[*it].u : edges[*it].v;
            long long pushed = min(must, edges[*it].cap - edges[*it].flow);
            if (pushed == 0) break;
            if (forw) {
              pout[v] -= pushed;
              pin[u] -= pushed;
            } else {
              pin[v] -= pushed;
              pout[u] -= pushed;
            }
            if (ex[u] == 0) q[qt++] = u;
            ex[u] += pushed;
            edges[*it].flow += pushed;
            edges[(*it) ^ 1].flow -= pushed;
            must -= pushed;
            if (edges[*it].cap - edges[*it].flow == 0) {
              auto jt = it;
              ++jt;
              if (forw) {
                in[u].erase(find(in[u].begin(), in[u].end(), *it));
                out[v].erase(it);
              } else {
                out[u].erase(find(out[u].begin(), out[u].end(), *it));
                in[v].erase(it);
              }
              it = jt;
            } else
              break;
            if (!must) break;
          }
        }
      }
    
      long long flow() {
        long long ans = 0;
        while (true) {
          pin.assign(n, 0);
          pout.assign(n, 0);
          level.assign(n, -1);
          alive.assign(n, true);
          level[s] = 0;
          qh = 0;
          qt = 1;
          q[0] = s;
          if (!bfs()) break;
          for (int i = 0; i < n; i++) {
            out[i].clear();
            in[i].clear();
          }
          for (int i = 0; i < m; i++) {
            if (edges[i].cap - edges[i].flow == 0) continue;
            int v = edges[i].v, u = edges[i].u;
            if (level[v] + 1 == level[u] && (level[u] < level[t] || u == t)) {
              in[u].push_back(i);
              out[v].push_back(i);
              pin[u] += edges[i].cap - edges[i].flow;
              pout[v] += edges[i].cap - edges[i].flow;
            }
          }
          pin[s] = pout[t] = flow_inf;
          while (true) {
            int v = -1;
            for (int i = 0; i < n; i++) {
              if (!alive[i]) continue;
              if (v == -1 || pot(i) < pot(v)) v = i;
            }
            if (v == -1) break;
            if (pot(v) == 0) {
              alive[v] = false;
              remove_node(v);
              continue;
            }
            long long f = pot(v);
            ans += f;
            push(v, s, f, false);
            push(v, t, f, true);
            alive[v] = false;
            remove_node(v);
          }
        }
        return ans;
      }
    };
    ```

### ISAP

In the Dinic algorithm, we have to run BFS to layer after finding each augmenting path; is there a more efficient method?

The answer is the ISAP algorithm to be introduced below.

#### Process

Same as the Dinic algorithm, we still first run BFS to layer the points on the graph, but slightly different from Dinic, we choose to BFS from point $t$ to point $s$ on the reverse graph.

After executing the layering process, we find augmenting paths through DFS.

The augmentation process is similar to Dinic; we only choose points with a layer number $1$ less than the current point to augment.

Different from Dinic, we do not re-run BFS to re-layer the points on the graph, but complete the re-layering process during the augmentation process.

Specifically, let the layer of point $i$ be $d_i$; after we finish the augmentation process at point $i$, we traverse all out-edges of $i$ on the residual network, find the out-point $j$ with the smallest layer, and then let $d_i \gets d_j+1$. In particular, if $i$ has no out-edge on the residual network, then $d_i \gets n$.

It is easy to find that when $d_s \geq n$, there is no augmenting path on the graph, and the algorithm can terminate.

Similar to Dinic, there is also **current-arc optimization** in ISAP.

And ISAP has another optimization: we record the number $num_i$ of points with layer $i$; each time a point's layer is updated from $x$ to $y$, we also update the value of the $num$ array; if after the update $num_x=0$, it means a fault appeared on the graph, and no augmenting path can be found anymore, at which point the algorithm can be directly terminated (in implementation directly mark $d_s$ as $n$); this optimization is called **GAP optimization**.

#### Implementation

??? note "Reference code"
    ```cpp
    struct Edge {
      int from, to, cap, flow;
    
      Edge(int u, int v, int c, int f) : from(u), to(v), cap(c), flow(f) {}
    };
    
    bool operator<(const Edge& a, const Edge& b) {
      return a.from < b.from || (a.from == b.from && a.to < b.to);
    }
    
    struct ISAP {
      int n, m, s, t;
      vector<Edge> edges;
      vector<int> G[MAXN];
      bool vis[MAXN];
      int d[MAXN];
      int cur[MAXN];
      int p[MAXN];
      int num[MAXN];
    
      void AddEdge(int from, int to, int cap) {
        edges.push_back(Edge(from, to, cap, 0));
        edges.push_back(Edge(to, from, 0, 0));
        m = edges.size();
        G[from].push_back(m - 2);
        G[to].push_back(m - 1);
      }
    
      bool BFS() {
        memset(vis, 0, sizeof(vis));
        queue<int> Q;
        Q.push(t);
        vis[t] = true;
        d[t] = 0;
        while (!Q.empty()) {
          int x = Q.front();
          Q.pop();
          for (int i = 0; i < G[x].size(); i++) {
            Edge& e = edges[G[x][i] ^ 1];
            if (!vis[e.from] && e.cap > e.flow) {
              vis[e.from] = true;
              d[e.from] = d[x] + 1;
              Q.push(e.from);
            }
          }
        }
        return vis[s];
      }
    
      void init(int n) {
        this->n = n;
        for (int i = 0; i < n; i++) G[i].clear();
        edges.clear();
      }
    
      int Augment() {
        int x = t, a = INF;
        while (x != s) {
          Edge& e = edges[p[x]];
          a = min(a, e.cap - e.flow);
          x = edges[p[x]].from;
        }
        x = t;
        while (x != s) {
          edges[p[x]].flow += a;
          edges[p[x] ^ 1].flow -= a;
          x = edges[p[x]].from;
        }
        return a;
      }
    
      int Maxflow(int s, int t) {
        this->s = s;
        this->t = t;
        int flow = 0;
        BFS();
        memset(num, 0, sizeof(num));
        for (int i = 0; i < n; i++) num[d[i]]++;
        int x = s;
        memset(cur, 0, sizeof(cur));
        while (d[s] < n) {
          if (x == t) {
            flow += Augment();
            x = s;
          }
          int ok = 0;
          for (int i = cur[x]; i < G[x].size(); i++) {
            Edge& e = edges[G[x][i]];
            if (e.cap > e.flow && d[x] == d[e.to] + 1) {
              ok = 1;
              p[e.to] = G[x][i];
              cur[x] = i;
              x = e.to;
              break;
            }
          }
          if (!ok) {
            int m = n - 1;
            for (int i = 0; i < G[x].size(); i++) {
              Edge& e = edges[G[x][i]];
              if (e.cap > e.flow) m = min(m, d[e.to]);
            }
            if (--num[d[x]] == 0) break;
            num[d[x] = m + 1]++;
            cur[x] = 0;
            if (x != s) x = edges[p[x]].from;
          }
        }
        return flow;
      }
    };
    ```

## Push-Relabel preflow-push algorithm

This method ignores flow conservation in the solving process, and updates the information of one node at a time to solve the maximum flow.

### General preflow-push algorithm

First we introduce the main idea of the preflow-push algorithm, and a feasible brute-force implementation algorithm.

The preflow-push algorithm solves the maximum flow through update operations on a single node, until no node needs to be updated.

The flow function maintained by the algorithm process does not necessarily maintain flow conservation; for a node, we allow the flow entering the node to exceed the flow leaving the node, and the excess part is called the **excess flow** $e(u)$ of node $u(u\in V-\{s,t\})$:

$$
e(u)=\sum_{(x,u)\in E}f(x,u)-\sum_{(u,y)\in E}f(u,y)
$$

If $e(u)>0$, node $u$ is said to be **overflowing**[^note1]; note that when we mention overflowing nodes, $s$ and $t$ are not included.

The preflow-push algorithm maintains the height $h(u)$ of each node, and stipulates that if an overflowing node $u$ wants to push excess flow, it can only push to nodes with height less than $u$; if $u$ has no adjacent node with height less than $u$, then modify the height of $u$ (relabel).

#### Height function[^note2]

Precisely, preflow-push maintains the following mapping $h:V\to \mathbf{N}$:

-   $h(s)=|V|,h(t)=0$
-   $\forall (u,v)\in E_f,h(u)\leq h(v)+1$

$h$ is called the height function of the residual network $G_f=(V_f,E_f)$.

Lemma 1: let the height function on $G_f$ be $h$; for any two nodes $u,v\in V$, if $h(u)>h(v)+1$, then $(u,v)$ is not an edge in $G_f$.

The algorithm only performs pushing on edges where $h(u)=h(v)+1$.

#### Push

Applicability condition: node $u$ is overflowing, and there exists a node $v((u,v)\in E_f,c(u,v)-f(u,v)>0,h(u)=h(v)+1)$, then the push operation applies to $(u,v)$.

So, we push the excess flow from $u$ to $v$ as much as possible; during the push process we only care about the minimum of the excess flow and $c(u,v)-f(u,v)$, and do not care whether $v$ overflows.

If $(u,v)$ is at full flow after pushing, delete it from the residual network.

#### Relabel

Applicability condition: if node $u$ is overflowing, and $\forall (u,v)\in E_f,h(u)\leq h(v)$, then the relabel operation applies to $u$.

Then just update $h(u)$ to $\min_{(u,v)\in E_f}h(v)+1$.

#### Initialization

$$
\forall (u,v)\in E,~~f(u,v)=\begin{cases}
c(u,v),&u=s\\
0,&u\neq s
\end{cases}
$$

$$
\forall u\in V,~~h(u)=\begin{cases}
|V|,&u=s\\
0,&u\neq s
\end{cases}
$$

$$
e(u)=\sum_{(x,u)\in E}f(x,u)-\sum_{(u,y)\in E}f(u,y)
$$

The above fills the $(s,v)\in E$ with flow, and raises $h(s)$ so that $(s,v)\notin E_f$, because $h(s)>h(v)$, and $(s,v)$ is after all at full flow and there is no need to keep it in the residual network; the above also initializes $e(s)$ to the negation of $\sum_{(s,v)\in E}f(s,v)$.

#### Process

We scan the whole graph each time; as long as there exists a node $u$ satisfying the condition of the push or relabel operation, we perform the corresponding operation.

As shown, the middle of each node represents the number, the lower left represents the height value $h(u)$, the lower right represents the excess flow $e(u)$, and the depth of the node color also represents the height of the node; the edge weight represents $c(u,v)-f(u,v)$, and the green edges represent edges $(u,v)$ satisfying $h(u)=h(v)+1$ (i.e. the edges $E_f$ of the residual network):

![p1](./images/2148.png)

Let us roughly browse through the process of the whole algorithm; here the author uses a brute-force algorithm, i.e. brute-force scanning whether there is an overflowing node, and if so, updating

![p2](./images/2149.gif)

The final result

![p3](./images/2150.png)

We can find that part of the final excess flow returned to $s$, and except for the source and sink, no other node overflows; at this point the flow function $f$ satisfies flow conservation, is the maximum flow, and the flow value is $e(t)$.

But in fact the paper[^ref1] points out that only processing overflowing nodes with height less than $n$ can also obtain the correct maximum flow value, however in this way when the algorithm ends the preflow does not yet satisfy the flow-function property, and the real flow on each edge cannot be known.

#### Implementation

???+ note "Core code"
    ```cpp
    constexpr int N = 1e4 + 4, M = 1e5 + 5, INF = 0x3f3f3f3f;
    int n, m, s, t, maxflow, tot;
    int ht[N], ex[N];
    
    void init() {  // initialization
      for (int i = h[s]; i; i = e[i].nex) {
        const int &v = e[i].t;
        ex[v] = e[i].v, ex[s] -= ex[v], e[i ^ 1].v = e[i].v, e[i].v = 0;
      }
      ht[s] = n;
    }
    
    bool push(int ed) {
      const int &u = e[ed ^ 1].t, &v = e[ed].t;
      int flow = min(ex[u], e[ed].v);
      ex[u] -= flow, ex[v] += flow, e[ed].v -= flow, e[ed ^ 1].v += flow;
      return ex[u];  // if u is still overflowing, return 1
    }
    
    void relabel(int u) {
      ht[u] = INF;
      for (int i = h[u]; i; i = e[i].nex)
        if (e[i].v) ht[u] = min(ht[u], ht[e[i].t]);
      ++ht[u];
    }
    ```

### HLPP algorithm

The Highest Label Preflow Push algorithm, in the above general preflow-push algorithm, when selecting a node each time, always preferentially selects the overflowing node with the highest height; its algorithm complexity is $O(n^2\sqrt m)$.

#### Process

Specifically, the HLPP algorithm process is as follows:

1.  Initialize (based on the preflow-push algorithm);
2.  Select the node $u$ with the highest height among the overflowing nodes, and push on all its edges that can be pushed;
3.  If $u$ is still overflowing, relabel it, and return to step 2;
4.  If there is no overflowing node, the algorithm ends.

A paper[^ref2] testing the actual performance of maximum flow algorithms shows that in fact for preflow-based algorithms, a considerable part of the time is spent on the relabel step. Below we introduce two optimizations from the paper[^ref3] that can significantly reduce the number of relabels.

#### BFS optimization

The upper bound of HLPP is $O(n^2\sqrt m)$, but it is relatively tight in use; we can optimize when initializing the height. Specifically, we initialize $h(u)$ to the shortest distance from $u$ to $t$; in particular, $h(s)=n$.

While doing BFS we also check the connectivity of the graph, ruling out the case of no solution.

#### GAP optimization

The condition for HLPP to push is $h(u)=h(v)+1$, and if at some moment of the algorithm there exists some $k$ such that the number of nodes with $h(u)=k$ is $0$, then for nodes with $h(u)>k$ it will forever be impossible to push excess flow to $t$, so it can only be sent back to $s$, so at this time we directly let their height become at least $n+1$, to push back to $s$ as soon as possible, reducing the relabel operations.

The following implementation adopts the implementation method in the paper[^ref2], using $N*2-1$ buckets `B`, where `B[i]` records all overflowing nodes with current height $i$. The two optimizations mentioned above are added, and only overflowing nodes with height less than $n$ are processed.

It is worth noting that the buckets used in the paper[^ref2] are stacks based on linked lists, while the default container of `stack` in the STL is `deque`. Simple testing found that `vector`, `deque`, `list` have little difference in efficiency in the actual running process of this problem.

#### Implementation

??? note "Luogu P4722 【Template】Maximum Flow Enhanced Version / Preflow-Push"
    ```cpp
    #include <cstdio>
    #include <cstring>
    #include <queue>
    #include <stack>
    using namespace std;
    constexpr int N = 1200, M = 120000, INF = 0x3f3f3f3f;
    int n, m, s, t;
    
    struct qxx {
      int nex, t;
      long long v;
    };
    
    qxx e[M * 2 + 1];
    int h[N + 1], cnt = 1;
    
    void add_path(int f, int t, long long v) {
      e[++cnt] = qxx{h[f], t, v}, h[f] = cnt;
    }
    
    void add_flow(int f, int t, long long v) {
      add_path(f, t, v);
      add_path(t, f, 0);
    }
    
    int ht[N + 1];        // height;
    long long ex[N + 1];  // excess flow;
    int gap[N];           // gap optimization. gap[i] is the number of nodes with height i
    stack<int> B[N];      // bucket B[i] records all v with ht[v]==i
    int level = 0;        // the highest height of overflowing nodes
    
    int push(int u) {      // push excess flow through the pushable edges as much as possible
      bool init = u == s;  // whether in initialization
      for (int i = h[u]; i; i = e[i].nex) {
        const int &v = e[i].t;
        const long long &w = e[i].v;
        // during initialization the height difference of 1 is not considered
        if (!w || (init == false && ht[u] != ht[v] + 1) || ht[v] == INF) continue;
        long long k = init ? w : min(w, ex[u]);
        // take the minimum of the residual capacity and the excess flow; during initialization the source's overflow amount can be a negative number.
        if (v != s && v != t && !ex[v]) B[ht[v]].push(v), level = max(level, ht[v]);
        ex[u] -= k, ex[v] += k, e[i].v -= k, e[i ^ 1].v += k;  // push
        if (!ex[u]) return 0;  // if pushing is done, return
      }
      return 1;
    }
    
    void relabel(int u) {  // relabel (height)
      ht[u] = INF;
      for (int i = h[u]; i; i = e[i].nex)
        if (e[i].v) ht[u] = min(ht[u], ht[e[i].t]);
      if (++ht[u] < n) {  // only process nodes with height less than n
        B[ht[u]].push(u);
        level = max(level, ht[u]);
        ++gap[ht[u]];  // new height, update gap
      }
    }
    
    bool bfs_init() {
      memset(ht, 0x3f, sizeof(ht));
      queue<int> q;
      q.push(t), ht[t] = 0;
      while (q.size()) {  // reverse BFS, enqueue nodes not visited
        int u = q.front();
        q.pop();
        for (int i = h[u]; i; i = e[i].nex) {
          const int &v = e[i].t;
          if (e[i ^ 1].v && ht[v] > ht[u] + 1) ht[v] = ht[u] + 1, q.push(v);
        }
      }
      return ht[s] != INF;  // if the graph is not connected, return 0
    }
    
    // select one of the nodes with the current highest height, return 0 if there is no overflowing node anymore
    int select() {
      while (level > -1 && B[level].size() == 0) level--;
      return level == -1 ? 0 : B[level].top();
    }
    
    long long hlpp() {            // return the maximum flow
      if (!bfs_init()) return 0;  // graph is not connected
      memset(gap, 0, sizeof(gap));
      for (int i = 1; i <= n; i++)
        if (ht[i] != INF) gap[ht[i]]++;  // initialize gap
      ht[s] = n;
      push(s);  // initialize the preflow
      int u;
      while ((u = select())) {
        B[level].pop();
        if (push(u)) {  // still overflowing
          if (!--gap[ht[u]])
            for (int i = 1; i <= n; i++)
              if (i != s && ht[i] > ht[u] && ht[i] < n + 1)
                ht[i] = n + 1;  // the nodes relabeled to n+1 here are all not overflowing nodes
          relabel(u);
        }
      }
      return ex[t];
    }
    
    int main() {
      scanf("%d%d%d%d", &n, &m, &s, &t);
      for (int i = 1, u, v, w; i <= m; i++) {
        scanf("%d%d%d", &u, &v, &w);
        add_flow(u, v, w);
      }
      printf("%lld", hlpp());
      return 0;
    }
    ```

Get a feel for the running process

![HLPP](./images/1152.png)

Among them, pic13 to pic14 executed Relabel(4) and performed GAP optimization.

## Footnotes

[^ref_ek]: <http://pisces.ck.tp.edu.tw/~peng/index.php?action=showfile&file=f6cdf7ef750d7dc79c7d599b942acbaaee86a2e3e>

[^ref_dinic]: <https://people.orie.cornell.edu/dpw/orie633/LectureNotes/lecture9.pdf>

[^ref1]: Cherkassky B V, Goldberg A V. On implementing push-relabel method for the maximum flow problem\[C]//International Conference on Integer Programming and Combinatorial Optimization. Springer, Berlin, Heidelberg, 1995: 157-171.

[^ref2]: Ahuja R K, Kodialam M, Mishra A K, et al. Computational investigations of maximum flow algorithms\[J]. European Journal of Operational Research, 1997, 97(3): 509-542.

[^ref3]: Derigs U, Meier W. Implementing Goldberg's max-flow-algorithm—A computational investigation\[J]. Zeitschrift für Operations Research, 1989, 33(6): 383-403.

[^note1]: In English literature it is usually called "active".

[^note2]: In English literature, the height of a node is usually called a "distance label". The term "height" used here originates from the relevant chapter in Introduction to Algorithms. You can find the reason for doing so in the footnote on P432 of Introduction to Algorithms (3rd edition, published by China Machine Press).
