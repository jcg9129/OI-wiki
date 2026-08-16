author: accelsao, thallium, Chrogeek, Enter-tainer, ksyx, StudyingFather, H-J-Granger, Henry-ZHR, countercurrent-time, william-song-shy, 5ab-juruo, XiaoQuQuSD, hhc0001, GCVillager

Prerequisites: [bipartite graph](../bi-graph.md), [graph matching](./graph-match.md)

## Introduction

This article discusses the maximum matching problem of a bipartite graph $G=(X,Y,E)$.

A typical example of bipartite graph matching in life is male-female pairing. Suppose there are several boys ($X$) and girls ($Y$), each person can only pair once, and the allowed pairing combinations are already limited by some list ($E$). At this point, the task of the bipartite graph maximum matching algorithm is to find the maximum number of pairs under these constraints, so that as many people as possible are successfully paired.

???+ info "Tip"
    This article assumes a known way of partitioning (coloring) the vertex set $V$ of the bipartite graph: $V=X\cup Y$. If the partitioning method of the bipartite graph's vertex set $V$ is not known in advance, such a partition can be found in $O(|V|+|E|)$ time through the [coloring algorithm of the bipartite graph](../bi-graph.md#determination).

## Kuhn's algorithm

Kuhn's algorithm is a direct application of [Berge's lemma](./graph-match.md#berges-lemma). It is also part of the [Hungarian algorithm](./bigraph-weight-match.md#hungarian-algorithmkuhnmunkres-algorithm).

### Process

To find the maximum matching, the algorithm enumerates all vertices in turn, finds an augmenting path starting from it, and augments. Because the length of an augmenting path is always odd, in a bipartite graph, its endpoints must be located in the left and right parts respectively. This shows that we only need to consider augmenting paths starting from the left part.

To find an augmenting path, we can orient the bipartite graph according to the current matching $M$. In an augmenting path (or any alternating path) starting from an unmatched left-part point, one can only go from a left-part point to a right-part point along non-matching edges, and then from a right-part point to a left-part point along matching edges. Therefore, we can stipulate that all non-matching edges point to right-part points, and all matching edges point to left-part points. The problem of finding an augmenting path is then converted into finding a simple path in a directed graph from some unmatched left-part point to some unmatched point. This problem can be easily solved by [DFS](../dfs.md) or [BFS](../bfs.md) in $O(|E|)$ time.

![](images/bigraph-match-1.svg)

(In the figure, dark points are matched points, light points are unmatched points, red edges are matching edges, black edges are non-matching edges, and the arrows indicate the orientation corresponding to the current matching. From the figure, the path $1\rightarrow 8\rightarrow 3\rightarrow 11\rightarrow 6\rightarrow 12$ is an augmenting path relative to the current matching.)

At the start of the algorithm, all edges point to right-part points. Each time an augmenting path is found, all edges passed along the augmenting path need to be reversed, to indicate that their matching status has been flipped. When the algorithm ends, all edges pointing to left-part points are matching edges.

Because we need to enumerate at most $O(|V|)$ left-part points [once each](./graph-match.md#berges-lemma), the total time complexity of the algorithm is $O(|V||E|)$.

### Optimization

There are some simple techniques that can optimize the constant factor of Kuhn's algorithm:

1.  Kuhn's algorithm is based on Berge's lemma, which does not require giving the left and right parts of the bipartite graph in advance. Therefore, even when the left and right parts are not explicitly partitioned, Kuhn's algorithm can run correctly, as long as the graph itself is a bipartite graph. But, first coloring the bipartite graph and determining its left and right parts is often more efficient.
2.  Because the time complexity of the Kuhn's algorithm described above is actually $O(|X||E|)$, we can choose the smaller of the two parts of the bipartite graph as the left part $X$.
3.  When finding augmenting paths, the marks used to avoid repeated searching do not need to be cleared each DFS. We can, before clearing the marks, try to find augmenting paths for all unmatched left-part points. In one such round of searching, each edge is visited at most once, and the complexity is still $O(|E|)$; but, in one round of searching, multiple augmenting paths may be found, so the total number of rounds $k$ does not exceed $|M|+1$, where $M$ is the maximum matching. Correspondingly, the overall complexity of the algorithm is reduced to $O(k|E|)$.
4.  When finding an augmenting path, prioritize unmatched right-part points, because this means a shorter augmenting path.
5.  Because Berge's lemma does not require the initial matching to be empty, at the start of Kuhn's algorithm, we can randomly select some mutually disjoint edges as the initial matching, to reduce the number of subsequent searches. If optimization 3 has already been applied, this optimization can be ignored.

Although the worst-case complexity is still $O(|V||E|)$, a fully optimized Kuhn's algorithm is not inefficient. But to avoid particular data pushing it to the worst-case complexity, the order of edges or vertices needs to be randomly shuffled first before matching.

### Reference implementation

In implementation, one does not need to actually maintain the orientation; one only needs to maintain the vertex matched with each vertex.

??? example "Template problem [Library Checker - Matching on Bipartite Graph](https://judge.yosupo.jp/problem/bipartitematching)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_1.cpp"
    ```

## Hopcroft–Karp algorithm

The Hopcroft–Karp algorithm further optimizes the process of finding augmenting paths in Kuhn's algorithm, reducing the total number of rounds to $O(|V|^{1/2})$, thereby obtaining a time complexity of $O(|V|^{1/2}|E|)$. This algorithm is actually a special case of the [Dinic algorithm](../flow/max-flow.md#dinic-algorithm).

### Process

The algorithm is still finding augmenting paths, but to complete the matching in fewer rounds, the algorithm adopts the following strategy in each round:

1.  Orient the matching edges to point to left-part points, and non-matching edges to point to right-part points.
2.  Starting from all unmatched left-part points, perform BFS on the directed graph, recording the layer $d(v)$ of each visited vertex, until some layer has an unmatched right-part point. If BFS ends without finding an unmatched right-part point, it means the current matching is already the maximum matching.
3.  Perform DFS in turn from each unmatched left-part point, finding augmenting paths and augmenting. During DFS, extend forward along edges satisfying continuous and strictly increasing layers (i.e. $d(v') = d(v) + 1$), and only visit vertices not yet visited in this round of DFS. In particular, DFS will not visit vertices not yet visited in the previous BFS step.

In network-flow terminology, step 2 constructs a level graph, and step 3 finds the blocking flow on the level graph. The so-called level graph means that each of its edges necessarily points from this layer to the next layer; and the so-called blocking flow, in the current context, means a set of maximal augmenting paths with no common vertex pairwise. The set of augmenting paths obtained in step 3 must be maximal: assuming not, there exists a new augmenting path, then when its start point was originally enumerated, such a path should have already been found.

Compared with the earlier Kuhn's algorithm, the most critical change of the Hopcroft–Karp algorithm is adding the step of finding the level graph before finding the blocking flow. Performing DFS based on the level graph is equivalent to restricting the algorithm to always reach each vertex along the shortest path. The benefit of doing so is that between different rounds of the algorithm, the length of the augmenting paths found by the algorithm strictly increases. Moreover, it can be proved that, until the maximum matching is found, the length of the augmenting path increases at most $3|M|^{1/2}$ times, where $|M|$ is the size of the maximum matching. So, this controls the total number of augmentation rounds to $O(|M|^{1/2})$, thereby obtaining a time complexity of $O(|M|^{1/2}|E|)$. Since $2|M|\le |V|$, the time complexity can also be written as the looser upper bound $O(|V|^{1/2}|E|)$.

??? note "Proof"
    First we show that between different rounds of the algorithm, the length of the augmenting paths found by the algorithm strictly increases.
    
    Suppose in the current round's BFS, vertices extend forward by $\ell$ layers; then, because the unmatched right-part points found in BFS are all located in the same layer, the length of all augmenting paths that this round's DFS can find is all $\ell$. What needs to be proved is that after augmenting along the set of augmenting paths $\{P_i\}$ found in this round, in the re-oriented directed graph obtained, there will no longer exist augmenting paths of length not exceeding $\ell$.
    
    In fact, if $P$ is the shortest augmenting path relative to $M$, and $P'$ is an augmenting path relative to $M\oplus P$, then $|P'|\ge |P| + 2|P\cap P'|$ always holds. This is because $N=(M\oplus P)\oplus P'$ is augmented twice relative to $M$, so, similar to the [proof of Berge's lemma](./graph-match.md#berges-lemma), it can be shown that the symmetric difference $M\oplus N=P\oplus P'$ contains at least two disjoint augmenting paths $P_1$ and $P_2$ relative to $M$. Due to the shortness of $P$, we have
    
    $$
    2|P|\le |P_1|+|P_2|\le |P\oplus P'| = |P| + |P'| - 2|P\cap P'|.
    $$
    
    This shows $|P'|\ge |P| + 2|P\cap P'|$. Therefore, if after adding the augmenting paths $\{P_i\}$, the new augmenting path $P'$ is still as long as them, it must be pairwise disjoint from them, which contradicts the maximality of $\{P_i\}$. This contradiction shows that after augmenting the blocking flow, the new augmenting path must be strictly longer.
    
    Finally, we need to show that the length of the augmenting path increases at most $3|M|^{1/2}$ times.
    
    Denote $p=\lfloor|M|^{1/2}\rfloor$. After the first $p$ rounds end, the length of the remaining augmenting paths is at least $|M|^{1/2}$. Let the current matching be $M_p$; then, similar to the previous case, it can be shown that the graph $(V,M\oplus M_p)$ has $|M|-|M_p|$ augmenting paths relative to $M_p$ with no common vertex pairwise. Each augmenting path uses at least $|M|^{1/2}/2$ matching edges in $M$, so the total number of these augmenting paths does not exceed $2|M|^{1/2}$, that is, $|M|-|M_p|\le 2|M|^{1/2}$. This shows that starting from $M_p$, at most $2|M|^{1/2}$ more augmentations can be performed, which also means the algorithm performs at most $2|M|^{1/2}$ more rounds of augmentation. So, the length of the augmenting path increases at most $3|M|^{1/2}$ times in total.

This is merely an estimate of the worst-case complexity of the Hopcroft–Karp algorithm. In fact, in random graphs, the time complexity of the Hopcroft–Karp algorithm is with high probability $O(|E|\log |V|)$[^hk-comp-ref].

### Optimization

When building the level graph, same as the general Dinic algorithm, the Hopcroft–Karp algorithm terminates when reaching an unmatched right-part point. But, purely for the bipartite matching problem, doing so is unnecessary. Moreover, because BFS terminates too early, restricting the range of subsequent DFS, it causes the number of augmenting paths found per round to be limited, thereby slowing down the overall matching efficiency. On some graphs, its efficiency is even inferior to the optimized Kuhn's algorithm. So, a simple improvement is to not terminate BFS early, but build the level graph for all reachable vertices.

??? note "Correctness proof"
    In the optimized algorithm, the lengths of the augmenting paths in the blocking flow will no longer be the same, so the earlier proof about complexity no longer holds. But, it can be shown that by building an auxiliary graph for each round of the algorithm, the conclusion that the shortest augmenting-path length strictly increases can likewise be established, thereby guaranteeing that the worst-case complexity is still correct.
    
    Let the bipartite graph be $G=(X,Y,E)$ and the current matching be $M$. Let the set of unmatched right-part points reachable by BFS be $W\subseteq Y$, and the length of the shortest augmenting path reaching $y\in W$ be $d(y)$. Denote $d_\text{max} = \max_{y\in W}d(y)$; then, for each $y\in W$, we can create a chain starting from $y$ of length $d_\text{max} - d(y)$, and mark the newly created vertices as left-part points and right-part points in turn, and mark the newly created edges as matching edges and non-matching edges in turn. Let the graph thus obtained be $G'=(X',Y',E')$, the matching be $M'$, and the shortest augmenting-path length be $d_\text{max}$. Then, there is a bijection between the augmenting paths relative to $M$ that can be found along the level graph in graph $G$—that is, the shortest augmenting paths reaching the corresponding vertices—and the globally shortest augmenting paths relative to $M'$ in graph $G'$. Therefore, finding the blocking flow and augmenting in the level graph of graph $G$ is equivalent to finding the blocking flow and augmenting in the level graph of graph $G'$. By the earlier proof, after augmentation, there will no longer exist augmenting paths of length $d_\text{max}$ in graph $G'$. So, there will no longer exist augmenting paths of length $d_\text{min}=\min_{y\in W} d(y)$ in graph $G$ either: because such an augmenting path, through the newly extended alternating path, must correspond to an augmenting path of length $d_\text{max}$ in graph $G'$. This again obtains the conclusion that between different rounds of the algorithm, the shortest augmenting-path length strictly increases. Therefore, the overall complexity is still $O(|M|^{1/2}|E|)$.

### Reference implementation

??? example "Template problem [Library Checker - Matching on Bipartite Graph](https://judge.yosupo.jp/problem/bipartitematching)"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_2.cpp"
    ```

## Reduction to the maximum flow problem

The bipartite graph maximum matching problem can be reduced to the maximum flow problem.

![](images/bigraph-match-2.svg)

As shown, add two vertices as the source and sink respectively. From the source, connect an edge to each left-part point; from each right-part point, connect an edge to the sink; and for each undirected edge in the bipartite graph, connect an edge from the left-part point to the right-part point. The capacity of all edges is $1$. Each network flow in the directed graph thus obtained corresponds one-to-one with a matching in the bipartite graph, and the capacity of the network flow is the size of the corresponding matching. Therefore, solving the bipartite graph maximum matching is equivalent to solving the maximum flow in the corresponding directed graph.

Any algorithm that can solve the maximum flow problem can be used to solve the bipartite graph maximum matching problem. It is easy to find that both Kuhn's algorithm and the Hopcroft–Karp algorithm are special cases of the corresponding algorithms in the maximum flow problem. Similarly, the [preflow-push algorithm](../flow/max-flow.md#push-relabel-preflow-push-algorithm) etc. can likewise be used to solve the bipartite graph maximum matching problem. But, it should be noted that any maximum flow algorithm, when applied to the bipartite graph maximum matching problem, needs to be optimized in a targeted manner to avoid an excessively large constant factor.

### Linear programming form

Like other maximum flow problems, the maximum matching problem of a bipartite graph $G=(V,E)$ can be written as a linear programming problem. If we use $x_e\in\{0,1\}$ to indicate whether edge $e$ belongs to the matching, then we can obtain the following linear programming problem:

$$
\begin{aligned}
\max_{\{x_e\}}\;& \sum_{e\in E}x_e \\
\text{subject to } & \sum_{e\sim v} x_{e} \le 1,~\forall v\in V,\\
& x_e\ge 0,~\forall e\in E.
\end{aligned}
$$

Here, $e\sim v$ denotes the incidence relation, i.e. vertex $v$ is one of the endpoints of edge $e$. Besides the non-negativity constraint, the constraints of the problem also require each vertex $v\in V$ to be incident to at most one edge, which is exactly the definition of a matching. Therefore, all matchings correspond to some integer points in the feasible region of this linear program.

The reverse, however, is not true. In a feasible solution, $x_e$ may be a fraction, which does not represent any actual matching. Nevertheless, for a bipartite graph $G$, all extreme-point solutions of the above linear program are integer points. This means that the optimal value of the objective function can always be attained at an integer point, without considering non-integer cases. This property does not hold for general graphs, so the above linear program is not equivalent to the maximum matching problem in general graphs.

The dual problem of this linear programming problem can be written in the following form:

$$
\begin{aligned}
\min_{\{y_v\}}\;& \sum_{v\in V}y_v \\
\text{subject to } & y_u+y_v \ge 1,~\forall (u,v)\in E,\\
& y_v\ge 0,~\forall v\in V.
\end{aligned}
$$

As we will see, this is exactly the minimum vertex cover problem of the bipartite graph.

## Dulmage–Mendelsohn decomposition

Using the maximum matching of a bipartite graph, the vertices can be partitioned into several mutually disjoint subsets, thereby completely characterizing the distribution and structural features of all maximum matchings of this bipartite graph. This is the Dulmage–Mendelsohn decomposition. In algorithm competitions, using this decomposition, one can identify the critical points and critical edges in a maximum matching, thereby judging the uniqueness of the maximum matching or solving problems such as bipartite graph games.

### Construction method

Let a maximum matching of the bipartite graph $G=(X,Y,E)$ be $M$.

![](images/bigraph-match-4.svg)

As shown, we can define the following three subsets for all vertices $V=X\cup Y$:

-   Even-reachable points $\mathcal E$, i.e. the set of all vertices that can be reached from an unmatched point along an alternating path of even length;
-   Odd-reachable points $\mathcal O$, i.e. the set of all vertices that can be reached from an unmatched point along an alternating path of odd length;
-   Unreachable points $\mathcal U$, i.e. the set of all vertices that cannot be reached from an unmatched point along an alternating path.

It can be proved that the three vertex sets $\mathcal E,\mathcal O,\mathcal U$ thus obtained have the following properties:

???+ note "Properties"
    1.  The sets $\mathcal E,\mathcal O,\mathcal U$ constitute a partition of the vertex set, and this partition is independent of the choice of the maximum matching $M$.
    2.  Any maximum matching of graph $G$ contains a perfect matching among the vertices of $\mathcal U$, and matches every vertex in $\mathcal O$ to a vertex in $\mathcal E$. That is to say, the size of the maximum matching of graph $G$ equals $|\mathcal O|+|\mathcal U|/2$.
    3.  Graph $G$ contains no edge connecting a vertex in $\mathcal E$ and a vertex in $\mathcal E\cup\mathcal U$.

??? note "Proof"
    1.  By definition, $\mathcal U$ and $\mathcal E\cup\mathcal O$ are disjoint. We only need to prove that $\mathcal E$ and $\mathcal O$ are disjoint. If not, for a vertex $v\in\mathcal E\cap\mathcal O$, there exists an alternating path of even length from an unmatched point $a$ to $v$, and also an alternating path of odd length from an unmatched point $b$ to $v$. Since graph $G$ is a bipartite graph, $a\neq b$, and the edges of the two paths reaching $v$ are a matching edge and a non-matching edge respectively. Therefore, connecting the two paths yields an alternating path from $a$ through $v$ to $b$. This is an augmenting path. This contradicts the point that $M$ is a maximum matching. Therefore, $\mathcal E\cap\mathcal O=\varnothing$.
    
        Let $M'$ be a maximum matching different from $M$. Repeating the [proof of Berge's lemma](./graph-match.md#berges-lemma) can show that $M'\oplus M$ consists only of even-length paths and even cycles. Starting from the maximum matching $M$, we can flip the edges in these connected components (paths and cycles) one by one (swapping matching edges and non-matching edges) to obtain the maximum matching $M'$. When flipping an even cycle, unmatched points are still unmatched points, and the parity of the length of the alternating path starting from it does not change; when flipping an even-length path, the matching status of the two endpoints of the path is swapped, but the parity of the length of the path from them to any point in the path is also consistent. Therefore, during the flipping process, the sets $\mathcal E,\mathcal O,\mathcal U$ always remain unchanged. This shows that this decomposition is independent of the choice of the maximum matching $M$.
    2.  If a matching edge appears in some alternating path starting from an unmatched point $v$, then the parity of the distances of its two endpoints to point $v$ must be different, so they belong to sets $\mathcal E$ and $\mathcal O$ respectively; otherwise, both its endpoints must be in $\mathcal U$. This shows that the matching edges in the maximum matching must be $\mathcal E\mathcal O$ edges or $\mathcal U\mathcal U$ edges. Conversely, an unmatched point can be reached along an alternating path of length zero starting from itself, so it only appears in the set $\mathcal E$; this shows that the sets $\mathcal O$ and $\mathcal U$ are both matched points. Simple counting shows that the size of the maximum matching is $|\mathcal O|+|\mathcal U|/2$.
    3.  By definition, any vertex $a$ in $\mathcal E$ can be reached from an unmatched point $v$ along an alternating path of even length, that is, a vertex in $\mathcal E$ is either an unmatched point, or the alternating path $P$ reaching that point ends with a matching edge. If there exists an edge in graph $G$ connecting $a$ and some vertex $b$ in $\mathcal E\cup\mathcal U$, then according to the discussion in the previous paragraph, this edge must be a non-matching edge, and the alternating path $P$ can be extended along it. This shows that vertex $b$ also belongs to the set $\mathcal O$, which contradicts the first property. Therefore, there is no edge in graph $G$ connecting a vertex in $\mathcal E$ and a vertex in $\mathcal E\cup\mathcal U$.

The decomposition of the vertex set thus obtained, $V=\mathcal E\cup\mathcal O\cup\mathcal U$, is called the **Dulmage–Mendelsohn decomposition**. After finding the maximum matching using the algorithm described above, the Dulmage–Mendelsohn decomposition can be found through BFS in $O(|V|+|E|)$ time.

### Critical points of the maximum matching

If a vertex $v$ is a matched point in every maximum matching of the bipartite graph $G$, then it is called a critical point of the maximum matching. The following conclusion shows that a vertex is a critical point if and only if in a maximum matching, there is no even-length alternating path from an unmatched point to that vertex.

???+ note "Theorem"
    Let the Dulmage–Mendelsohn decomposition of the bipartite graph $G=(X,Y,E)$ be $V=\mathcal E\cup\mathcal O\cup\mathcal U$. Then, vertex $v\in V$ is a critical point if and only if $v\in\mathcal O\cup \mathcal U$.

??? note "Proof"
    According to the properties of the Dulmage–Mendelsohn decomposition, in any maximum matching of graph $G$, the vertices in $\mathcal O$ and $\mathcal U$ must be matched points. Therefore, the vertices in $\mathcal O\cup \mathcal U$ must be critical points. Then, we need to show that there is definitely no critical point in the set $\mathcal E$. If in the maximum matching $M$, vertex $a\in\mathcal E$ is a critical point, then there exists an alternating path $P$ of even length connecting vertex $a$ and some unmatched point $b\in\mathcal E$. Flipping all edges on this path, in the obtained maximum matching $M\oplus P$, vertex $a$ becomes an unmatched point. Therefore, there is no critical point in the set $\mathcal E$.

Therefore, to find the critical points of the maximum matching, we only need to find the Dulmage–Mendelsohn decomposition.

### Critical edges of the maximum matching

Similarly, if an edge $e$ is a matching edge in every maximum matching of the bipartite graph $G$, then it is called a critical edge of the maximum matching. The maximum matching of a bipartite graph is unique if and only if in one of its maximum matchings, all matching edges are critical edges.

???+ note "Theorem"
    Let the Dulmage–Mendelsohn decomposition of the bipartite graph $G=(X,Y,E)$ be $V=\mathcal E\cup\mathcal O\cup\mathcal U$, and let $M$ be one of its maximum matchings. Then, edge $e\in E$ is a critical edge if and only if both endpoints of $e$ are in $\mathcal U$, edge $e$ is a matching edge in $M$, and there is no alternating cycle containing edge $e$ relative to $M$.

??? note "Proof"
    The endpoints of a critical edge must be critical points. According to the properties of the Dulmage–Mendelsohn decomposition, edges of the maximum matching can only be $\mathcal E\mathcal O$ edges or $\mathcal U\mathcal U$ edges. But, there is no critical point in $\mathcal E$, so a critical edge can only be a $\mathcal U\mathcal U$ edge. Of course, a critical edge must also be a matching edge in $M$. Let $e\in M$ be a $\mathcal U\mathcal U$ edge. It is not a critical edge if and only if there exists another maximum matching $M'\neq M$ such that $e\in M\oplus M'$. Repeating the [proof of Berge's lemma](./graph-match.md#berges-lemma) can show that $M'\oplus M$ consists only of even-length paths and even cycles. One of the endpoints of these paths is an unmatched point relative to $M$, so the vertices in the paths are not points in $\mathcal U$, which contradicts the choice of edge $e$. Therefore, edge $e$ can only appear in an even cycle. Therefore, a $\mathcal U\mathcal U$ edge $e\in M$ is not a critical edge if and only if there exists an alternating cycle containing edge $e$ relative to $M$. This is what was to be proved.

Therefore, to find the critical edges of the maximum matching, we need to proceed according to the following steps:

1.  Find the maximum matching $M$ of graph $G$;
2.  Orient the edges of graph $G$ according to $M$, obtaining the directed graph $G_M$;
3.  Perform BFS to find the set $\mathcal U$ in the Dulmage–Mendelsohn decomposition, i.e. the set of vertices that cannot be reached from unmatched points along alternating paths;
4.  Use [Tarjan's algorithm](../scc.md#tarjan-algorithm) to find all strongly connected components of the directed graph $G_M$;
5.  Traverse the edges in the matching $M$; if both its endpoints are in $\mathcal U$ but not in the same strongly connected component, then it is a critical edge.

After obtaining the maximum matching, the time complexity of the subsequent steps is $O(|V|+|E|)$.

## Related problems

Using the bipartite graph maximum matching algorithm, other combinatorial optimization problems can be solved.

### Bipartite graph minimum vertex cover

The minimum vertex cover problem refers to choosing the fewest vertices in an undirected graph such that each edge has at least one endpoint chosen.

The minimum vertex cover problem for general graphs is NP-hard, but for bipartite graphs, Kőnig's theorem shows that it can be reduced to the maximum matching problem, thereby being solved efficiently. The proof of the theorem also gives the construction of the minimum vertex cover.

???+ note "Kőnig's theorem"
    In a bipartite graph, the number of vertices in the minimum vertex cover equals the number of edges in the maximum matching.

??? note "Proof"
    Let a maximum matching of the bipartite graph $G=(X,Y,E)$ be $M$. Let the set of vertices in graph $G$ that can be reached from an unmatched left-part point $U$ along some alternating path be $Z$. Then, the vertex set $C=(X\setminus Z)\cup(Y\cap Z)$ is the sought minimum vertex cover.
    
    ![](images/bigraph-match-3.svg)
    
    First, the set $C$ is a vertex cover. Suppose not, there exists an edge $(u,v)\in E$ such that $u\in X\cap Z$ and $v\in Y\setminus Z$. Let $P_u$ be an alternating path reaching $u$. If edge $(u,v)$ is a matching edge, then the last edge in path $P_u$ is $(v,u)$, which contradicts $v\notin Z$; if edge $(u,v)$ is not a matching edge, then we can extend $P_u$ along edge $(u,v)$ to get an alternating path reaching $v$, likewise contradicting $v\notin Z$. These contradictions show that all edges contain at least one endpoint in $C$, so $C$ is a vertex cover.
    
    Then, we need to show that $C$ is the minimum vertex cover. To cover all edges of the maximum matching $M$, any vertex cover needs at least $|M|$ vertices. Therefore, we only need to prove $|C|=|M|$, and it must be the minimum vertex cover. This is equivalent to proving that, besides containing one endpoint of each matching edge, $C$ contains no other vertices; that is, $C$ contains no unmatched points. Suppose not, there exists an unmatched point $v\in C$. If $v\in X$, then there must be $v\in U\subseteq Z$, which contradicts the construction of $C$; if $v\in Y$, then an alternating path reaching $v$ is an augmenting path relative to $M$, which, by Berge's lemma, contradicts $M$ being a maximum matching. These contradictions show that no such unmatched point exists, so $C$ is the minimum vertex cover.

From the network-flow perspective, the minimum vertex cover problem is the minimum cut problem: choosing a left-part point is equivalent to cutting its edge with the source; choosing a right-part point is equivalent to cutting its edge with the sink. From the linear programming perspective, the minimum vertex cover problem is the dual problem of the maximum matching problem. Therefore, König's theorem can be regarded as a special case of the [max-flow min-cut theorem](../flow/max-flow.md#max-flow-min-cut-theorem), or more generally, a special case of the strong duality theorem of linear programming.

### Bipartite graph maximum independent set

The maximum independent set problem refers to choosing the most vertices in an undirected graph such that no two are adjacent.

For general graphs, the following theorem holds:

???+ note "Theorem"
    In a graph $G=(V,E)$, a point set $C\subseteq V$ is a vertex cover if and only if its complement $V\setminus C$ is an independent set.

??? note "Proof"
    A point set $C$ is a vertex cover if and only if at least one of the two endpoints of any edge $e$ in $E$ appears in the set $C$, if and only if no edge in $E$ has both its endpoints appearing in the set $V\setminus C$, if and only if $V\setminus C$ is an independent set.

???+ note "Corollary"
    In a graph $G=(V,E)$, the sum of the sizes of the minimum vertex cover and the maximum independent set equals the number of vertices.

Therefore, like the minimum vertex cover problem, the maximum independent set problem is NP-hard for general graphs, but for bipartite graphs it can be reduced to the maximum matching problem, thereby being solved efficiently.

### Minimum path cover of a directed acyclic graph

The minimum path cover problem refers to choosing the fewest number of simple paths in a directed graph such that all vertices appear in exactly one path.

The minimum path cover problem on a general directed graph is NP-hard, but for a directed acyclic graph, this problem can be reduced to the bipartite graph maximum matching problem. For a directed acyclic graph $G=(V,E)$, we can construct a bipartite graph $G'=(V^\text{in},V^\text{out},E')$ as follows:

-   For each vertex $v\in V$, establish an in-point $v^\text{in}$ and an out-point $v^\text{out}$ respectively. Let the sets of all in-points and out-points be $V^\text{in}$ and $V^\text{out}$ respectively. They become the left part and right part of the new graph respectively.
-   For each directed edge $(u,v)\in E$, establish an undirected edge $(u^\text{out},v^\text{in})$. The set of all undirected edges is $E'$.

For this, there is the following conclusion:

???+ note "Theorem"
    The sum of the sizes of the minimum path cover of the directed acyclic graph $G=(V,E)$ and the maximum matching of the corresponding bipartite graph $G'=(V^\text{in},V^\text{out},E')$ equals the number of vertices.

??? note "Proof"
    Each matching $M'$ of the bipartite graph $G'$ corresponds to a subgraph $F$ of graph $G$, and the in-degree and out-degree of each vertex in subgraph $F$ are at most one, that is to say, subgraph $F$ is actually a set of several mutually disjoint paths or cycles in the directed graph $G$. But, we already assumed there is no cycle in $G$, so $F$ only contains several disjoint paths. Conversely, for each such subgraph $F$, we can construct the corresponding matching. Because the size of the matching $M$ is the difference between the number of vertices and the number of paths in $F$, the minimum path cover problem of graph $G$ corresponds to the maximum matching problem of graph $G'$.

The proof is constructive, so it is easy to construct the corresponding minimum path cover from the obtained maximum matching. Moreover, this construction shows that for a general directed graph, this reduction no longer holds, precisely because a matching in a bipartite graph may correspond to a cycle in a directed graph.

In particular, for a set $X$ and a partial order relation $P$ on it, we can establish a directed acyclic graph $G=(X,P)$. At this point, according to [Dilworth's theorem](../../math/order-theory.md#dilworth-定理与-mirsky-定理), the size of the minimum path cover of graph $G$ equals the length of its longest antichain, which is the width of the poset $(X,P)$. Therefore, this section actually gives an efficient method for computing the width of any poset.

## Example problems

The difficulty of applying bipartite graph matching lies in building the graph; this section shows the techniques of building the graph through some example problems.

???+ example "[Luogu P1129 Matrix Game](https://www.luogu.com.cn/problem/P1129)"
    There is a 01 square matrix; each time we can swap two rows or two columns; ask whether it can be swapped so that the main diagonal (top-left to bottom-right) is all 1.

??? note "Solution"
    Note that when there exist $n$ $1$s such that these $1$s are not in the same row or the same column, then there must be a solution, otherwise there must be no solution. The problem is transformed into whether these $n$ $1$s can be found.
    
    Consider that for a $1$, in the final scheme choosing this $1$ represents this $1$'s row and column being occupied. So we can build a bipartite graph with $n$ left-part points and $n$ right-part points, where for an element that is $1$, we build an edge connecting the left-part point of its row and the right-part point of its column. So we can do bipartite matching.

??? note "Code"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_3.cpp"
    ```

???+ example "[Gym 104427B Lawyers](https://codeforces.com/gym/104427/problem/B)"
    There are $n$ lawyers, all accused of fraud. So they need to defend each other to ensure that every lawyer is released. These $n$ lawyers have $m$ trust relationships; a trust relationship $(a, b)$ means $a$ can defend $b$. Any lawyer who is defended will be acquitted, except for one case: if $a$ and $b$ defend each other, they will both be found guilty.
    
    Find whether it is possible to make every lawyer released.

??? note "Solution"
    For each **unordered pair** $(a, b)$, when $a$ can defend $b$, connect an edge from this unordered pair to $b$, and vice versa.
    
    Only keeping the $(a, b)$ connected by edges, the problem is transformed into a bipartite graph maximum matching with $m$ left-part points and $n$ right-part points.

??? note "Code"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_4.cpp"
    ```

???+ example "[Codeforces 1404E Bricks](https://codeforces.com/problemset/problem/1404/E)"
    Precisely cover an $n \times m$ grid with some $1 \times x$ bricks; the bricks can be rotated, and some cells cannot be covered.

??? note "Solution"
    Consider how the final scheme is composed:
    
    First lay $1 \times 1$ bricks on all coverable grid cells. For a $1 \times x$ brick, it can be formed by $x$ consecutive $1 \times 1$ bricks in the same row "row-merging" in turn. Similarly, for an $x \times 1$ brick, it can be formed by $x$ consecutive $1 \times 1$ bricks in the same column "column-merging" in turn.
    
    Obviously, one row-merge and one column-merge cannot interfere with the same brick, and the more merges, the fewer bricks. So, we can take row-merges as left-part points, column-merges as right-part points, and the aforementioned conflicts as edges, to build a bipartite graph. Then the original problem becomes a bipartite graph maximum independent set problem.

??? note "Code"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_5.cpp"
    ```

???+ example "[Codeforces 1139E - Maximize Mex](https://codeforces.com/problemset/problem/1139/E)"
    There are $m$ multisets with a total of $n$ elements; each time we delete an element from some multiset, and then query "the maximum $\operatorname{mex}$ that can be achieved by choosing at most one element from each multiset".

??? note "Solution"
    First consider how to do it if there is no element deletion.
    
    For each multiset, open a new point; for each possible answer, open a new point. Then, for an element $a$ of the multiset corresponding to point $l_i$, connect an edge from $l_i$ to $r_a$. At this point this weakened version becomes a bipartite graph maximum matching.
    
    Now add back the element-deletion operation, and we find it is completely intractable: deleting an edge may cause a huge change in the matching, and the complexity is unacceptable. So, we might as well do it in reverse; each time we add an edge, and then re-augment along it. So this problem can only use Kuhn's algorithm.

??? note "Code"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_6.cpp"
    ```

???+ example "[Luogu P3355 - Knight Coexistence Problem](https://www.luogu.com.cn/problem/P3355)"
    There is an $n \times n$ chessboard where some positions cannot place pieces; ask how many knights can be placed at most so that these knights do not attack each other.

??? note "Solution"
    We can find that if the whole chessboard is colored so that all black cells and white cells are not adjacent, then a knight can only attack cells of a different color from it.
    
    Then we can directly do bipartite graph maximum independent set.

??? note "Code"
    ```cpp
    --8<-- "docs/graph/code/graph-matching/bigraph-match/bigraph-match_7.cpp"
    ```

## Exercises

-   [Codeforces 1765A - Access Levels](https://codeforces.com/problemset/problem/1765/A)
-   [AtCoder abc274G - Security Camera 3](https://atcoder.jp/contests/abc274/tasks/abc274_g)
-   [Codeforces 1773D - Dominoes](https://codeforces.com/problemset/problem/1773/D)
-   [Luogu P5030 - Long-Necked Deer Placement](https://www.luogu.com.cn/problem/P5030)
-   [Luogu P2071 - Seat Arrangement](https://www.luogu.com.cn/problem/P2071)
-   [LibreOJ 6002 - Minimum Path Cover](https://loj.ac/p/6002)

## References

-   [Kuhn's Algorithm - Maximum Bipartite Matching](https://cp-algorithms.com/graph/kuhn_maximum_bipartite_matching.html)
-   [König's theorem for bipartite graph maximum matching and its proof](https://matrix67.com/blog/archives/116)
-   [Implementing Dinitz on bipartite graphs by adamant - Codeforces blogs](https://codeforces.com/blog/entry/118098)
-   Bondy, John Adrian, and Uppaluri Siva Ramachandra Murty. Graph theory with applications. Vol. 290. London: Macmillan, 1976.
-   Chen Yinbo. A brief discussion of graph matching algorithms and their applications. 2015 Informatics Olympiad China National Team Candidate Papers.
-   [Dulmage–Mendelsohn decomposition - Wikipedia](https://en.wikipedia.org/wiki/Dulmage%E2%80%93Mendelsohn_decomposition)
-   [Notes on Dulmage–Mendelsohn decomposition](https://www.cse.iitm.ac.in/~meghana/matchings/bip-decomp.pdf)

[^hk-comp-ref]: Bast, Holger; Mehlhorn, Kurt; Schäfer, Guido; Tamaki, Hisao (2006), "Matching algorithms are fast in sparse random graphs", Theory of Computing Systems, 39 (1): 3–14.
