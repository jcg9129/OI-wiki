author: du33169, lingkerio, Taoran-01

## Definition

(Remember these definitions? Before reading the following content, please be sure to understand the basic part of [graph-theory-related concepts](./concept.md).)

-   path
-   shortest path
-   shortest path in a directed graph, shortest path in an undirected graph
-   single-source shortest path, shortest path between every pair of nodes

## Notation

For convenience of description, here we first give the meanings of some notations that will be used below.

-   $n$ is the number of points on the graph, $m$ is the number of edges on the graph;
-   $s$ is the source point of the shortest path;
-   $D(u)$ is the **actual** shortest-path length from point $s$ to point $u$;
-   $dis(u)$ is the **estimated** shortest-path length from point $s$ to point $u$. At any time we have $dis(u) \geq D(u)$. In particular, when the shortest-path algorithm terminates, we should have $dis(u)=D(u)$.
-   $w(u,v)$ is the edge weight of the edge $(u,v)$.

## Properties

For a graph with positive edge weights, the shortest path between any two nodes does not pass through repeated nodes.

For a graph with positive edge weights, the shortest path between any two nodes does not pass through repeated edges.

For a graph with positive edge weights, for the shortest path between any two nodes, the number of nodes of any such path does not exceed $n$, and the number of edges does not exceed $n-1$.

## Floyd algorithm

It is used to find the shortest path between any two nodes.

The complexity is relatively high, but the constant factor is small, and it is easy to implement (only three `for`s).

It applies to any graph, regardless of directed or undirected, positive or negative edge weights, but the shortest path must exist. (There cannot be a negative cycle.)

### Implementation

We define an array `f[k][x][y]`, denoting the shortest-path length from node $x$ to node $y$ allowing passage only through nodes $1$ to $k$ (that is, paths in the subgraph $V'={1, 2, \ldots, k}$; note that $x$ and $y$ are not necessarily in this subgraph).

Obviously, `f[n][x][y]` is the shortest-path length from node $x$ to node $y$ (because $V'={1, 2, \ldots, n}$ is $V$ itself, and the shortest path it represents is exactly the sought path).

Next, consider how to compute the value of the `f` array.

`f[0][x][y]`: the edge weight of $x$ and $y$, or $0$, or $+\infty$ (when should `f[0][x][y]` be $+\infty$? When there is a directly-connected edge between $x$ and $y$, it is their edge weight; when $x = y$, it is zero, because the distance to itself is zero; when there is no directly-connected edge between $x$ and $y$, it is $+\infty$).

`f[k][x][y] = min(f[k-1][x][y], f[k-1][x][k]+f[k-1][k][y])` (`f[k-1][x][y]` is the shortest path not passing through point $k$, while `f[k-1][x][k]+f[k-1][k][y]` is the shortest path passing through point $k$).

The above two lines are both obviously correct, so this approach uses $O(N^3)$ space; we need to increase the problem scale in order ($k$ from $1$ to $n$), and determine the shortest path between any two points under the current problem scale.

=== "C++"
    ```cpp
    for (k = 1; k <= n; k++) {
      for (x = 1; x <= n; x++) {
        for (y = 1; y <= n; y++) {
          f[k][x][y] = min(f[k - 1][x][y], f[k - 1][x][k] + f[k - 1][k][y]);
        }
      }
    }
    ```

=== "Python"
    ```python
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                f[k][x][y] = min(f[k - 1][x][y], f[k - 1][x][k] + f[k - 1][k][y])
    ```

Because the first dimension has no effect on the result, we can find that the first dimension of the array can be omitted, so we can directly change it to `f[x][y] = min(f[x][y], f[x][k]+f[k][y])`.

???+ note "Proof that the first dimension has no effect on the result"
    For a given `k`, when updating `f[k][x][y]`, the elements involved always come from the `k`-th row and `k`-th column of the `f[k-1]` array. Then we can find that for a given `k`, when updating `f[k][k][y]` or `f[k][x][k]`, no numerical update ever occurs, because according to the formula `f[k][k][y] = min(f[k-1][k][y], f[k-1][k][k]+f[k-1][k][y])`, `f[k-1][k][k]` is 0, so this value is always `f[k-1][k][y]`; the proof for `f[k][x][k]` is similar.
    
    Therefore, if the first dimension is omitted, under a given `k`, the elements used in the update of each element are not updated in this iteration, so omitting the first dimension does not affect the result.

=== "C++"
    ```cpp
    for (k = 1; k <= n; k++) {
      for (x = 1; x <= n; x++) {
        for (y = 1; y <= n; y++) {
          f[x][y] = min(f[x][y], f[x][k] + f[k][y]);
        }
      }
    }
    ```

=== "Python"
    ```python
    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                f[x][y] = min(f[x][y], f[x][k] + f[k][y])
    ```

In summary, the time complexity is $O(N^3)$, and the space complexity is $O(N^2)$.

### Applications

???+ question "Given a positive-weight undirected graph, find a cycle with the minimum sum of weights."
    First, this must be a simple cycle.
    
    Think about how this cycle is formed.
    
    Consider the node $u$ with the largest number on the cycle.
    
    `f[u-1][x][y]` and $(u,x)$, $(u,y)$ together form the cycle.
    
    During the Floyd process, enumerate $u$, and compute the minimum value of this sum.
    
    The time complexity is $O(n^3)$.
    
    For more, see the [minimum cycle](./min-cycle.md) part.

???+ question "Given whether there is a connecting edge between any two points in a directed graph, determine whether any two points are connected."
    This problem is finding the **transitive closure of the graph**.
    
    We only need to follow the Floyd process, adding points one by one to make the determination.
    
    It is just that at this time the edge weight becomes $1/0$, and taking $\min$ becomes the **or** operation.
    
    Further optimizing with bitset, the complexity can reach $O(\frac{n^3}{w})$.
    
    ```cpp
    // std::bitset<SIZE> f[SIZE];
    for (k = 1; k <= n; k++)
      for (i = 1; i <= n; i++)
        if (f[i][k]) f[i] = f[i] | f[k];
    ```

## Bellman–Ford algorithm

The Bellman–Ford algorithm is a shortest-path algorithm based on the relax operation, which can find the shortest path of a graph with negative weights, and can determine the case where the shortest path does not exist.

In the domestic OI community, the "SPFA" you may have heard of is an implementation of the Bellman–Ford algorithm.

### Procedure

First introduce the relax operation used by the Bellman–Ford algorithm (the Dijkstra algorithm also uses the relax operation).

For an edge $(u,v)$, the relax operation corresponds to the following expression: $dis(v) = \min(dis(v), dis(u) + w(u, v))$.

The meaning of doing this is obvious: we try to use the path $S \to u \to v$ (where the $S \to u$ path takes the shortest path) to update the shortest-path length of point $v$; if this path is better, then update.

What the Bellman–Ford algorithm does is continuously try to relax each edge on the graph. Each round of the loop, we try to perform a relax operation on all edges on the graph once; when there is no successful relax operation in a loop, the algorithm stops.

Each loop is $O(m)$, so at most how many times will it loop?

In the case where the shortest path exists, since one relax operation increases the number of edges of the shortest path by at least $+1$, and the number of edges of the shortest path is at most $n-1$, the whole algorithm executes at most $n-1$ rounds of relax operations. So the total time complexity is $O(nm)$.

But there is another case: if, starting from point $S$, we reach a negative cycle, the relax operation will go on endlessly. Note that the previous argument has already shown that for a graph where the shortest path exists, the relax operation executes at most $n-1$ rounds, so if there are still relaxable edges in the $n$-th round of the loop, it means that starting from point $S$, we can reach a negative cycle.

???+ warning "A common misconception in negative-cycle determination"
    It should be noted that when running the Bellman–Ford algorithm with point $S$ as the source point, if it does not give the result that a negative cycle exists, it can only indicate that starting from point $S$ one cannot reach a negative cycle, and cannot indicate that there is no negative cycle on the graph.
    
    Therefore, if we need to determine whether there is a negative cycle on the entire graph, the most rigorous approach is to establish a super source point, connect an edge of weight 0 to each node on the graph, and then execute the Bellman–Ford algorithm with the super source point as the start point.

### Implementation

??? note "Reference implementation"
    === "C++"
        ```cpp
        struct Edge {
          int u, v, w;
        };
        
        vector<Edge> edge;
        
        int dis[MAXN], u, v, w;
        constexpr int INF = 0x3f3f3f3f;
        
        bool bellmanford(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          dis[s] = 0;
          bool flag = false;  // whether a relax operation occurred during a round of the loop
          for (int i = 1; i <= n; i++) {
            flag = false;
            for (int j = 0; j < edge.size(); j++) {
              u = edge[j].u, v = edge[j].v, w = edge[j].w;
              if (dis[u] == INF) continue;
              // infinity plus/minus a constant is still infinity
              // so an edge leading out of a point with shortest-path length INF cannot have a relax operation occur
              if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                flag = true;
              }
            }
            // stop the algorithm when there is no relaxable edge
            if (!flag) {
              break;
            }
          }
          // being able to relax in the n-th round of the loop means point s can reach a negative cycle
          return flag;
        }
        ```
    
    === "Python"
        ```python
        class Edge:
            def __init__(self, u=0, v=0, w=0):
                self.u = u
                self.v = v
                self.w = w
        
        
        INF = 0x3F3F3F3F
        edge = []
        
        
        def bellmanford(n, s):
            dis = [INF] * (n + 1)
            dis[s] = 0
            for i in range(1, n + 1):
                flag = False
                for e in edge:
                    u, v, w = e.u, e.v, e.w
                    if dis[u] == INF:
                        continue
                    # infinity plus/minus a constant is still infinity
                    # so an edge leading out of a point with shortest-path length INF cannot have a relax operation occur
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        flag = True
                # stop the algorithm when there is no relaxable edge
                if not flag:
                    break
            # being able to relax in the n-th round of the loop means point s can reach a negative cycle
            return flag
        ```

### Queue optimization: SPFA

That is, Shortest Path Faster Algorithm.

Many times we do not need so many useless relax operations.

Obviously, only the edges connected to the nodes relaxed in the last time may cause the next relax operation.

So we use a queue to maintain "which nodes may cause a relax operation", and then we can visit only the necessary edges.

SPFA can also be used to determine whether point $s$ can reach a negative cycle; we only need to record how many edges the shortest path passes through, and when it passes through at least $n$ edges, it means point $s$ can reach a negative cycle.

??? note "Implementation"
    === "C++"
        ```cpp
        struct edge {
          int v, w;
        };
        
        vector<edge> e[MAXN];
        int dis[MAXN], cnt[MAXN], vis[MAXN];
        queue<int> q;
        
        bool spfa(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          dis[s] = 0, vis[s] = 1;
          q.push(s);
          while (!q.empty()) {
            int u = q.front();
            q.pop(), vis[u] = 0;
            for (auto ed : e[u]) {
              int v = ed.v, w = ed.w;
              if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                cnt[v] = cnt[u] + 1;  // record the number of edges the shortest path passes through
                if (cnt[v] >= n) return false;
                // without passing through a negative cycle, the shortest path passes through at most n - 1 edges
                // so if it passes through more than n edges, it must indicate that it passed through a negative cycle
                if (!vis[v]) q.push(v), vis[v] = 1;
              }
            }
          }
          return true;
        }
        ```
    
    === "Python"
        ```python
        from collections import deque
        
        
        class Edge:
            def __init__(self, v=0, w=0):
                self.v = v
                self.w = w
        
        
        e = [[Edge() for i in range(MAXN)] for j in range(MAXN)]
        INF = 0x3F3F3F3F
        
        
        def spfa(n, s):
            dis = [INF] * (n + 1)
            cnt = [0] * (n + 1)
            vis = [False] * (n + 1)
            q = deque()
        
            dis[s] = 0
            vis[s] = True
            q.append(s)
            while q:
                u = q.popleft()
                vis[u] = False
                for ed in e[u]:
                    v, w = ed.v, ed.w
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        cnt[v] = cnt[u] + 1  # record the number of edges the shortest path passes through
                        if cnt[v] >= n:
                            return False
                        # without passing through a negative cycle, the shortest path passes through at most n - 1 edges
                        # so if it passes through more than n edges, it must indicate that it passed through a negative cycle
                        if not vis[v]:
                            q.append(v)
                            vis[v] = True
        ```

Although in most cases SPFA runs very fast, its worst-case time complexity is $O(nm)$, and it is not hard to push it to this complexity, so it should be used with caution in exams (when there are no negative-weight edges it is best to use the Dijkstra algorithm; when there are negative-weight edges and the graph in the problem has no special properties, if SPFA is part of the intended solution, the problem should not give a data range that the Bellman–Ford algorithm cannot pass).

???+ note "Other optimizations of Bellman–Ford"
    Besides queue optimization (SPFA), Bellman–Ford also has other forms of optimization; these optimizations have obvious effects on some graphs, but on certain special graphs, the worst-case complexity may reach exponential.
    
    -   Heap optimization: replace the queue with a heap; the difference from Dijkstra is that a point is allowed to enter the queue multiple times. On a graph with negative-weight edges, it may be pushed to exponential complexity.
    -   Stack optimization: replace the queue with a stack (i.e. change the original BFS process into DFS); it may have higher efficiency when looking for negative cycles, but the worst-case time complexity is still exponential.
    -   LLL optimization: replace the ordinary queue with a double-ended queue; each time, compare the distance of the enqueuing node with the average distance within the queue; if it is larger, insert at the tail, otherwise insert at the head.
    -   SLF optimization: replace the ordinary queue with a double-ended queue; each time, compare the distance of the enqueuing node with the head of the queue; if it is larger, insert at the tail, otherwise insert at the head.
    -   D´Esopo–Pape algorithm: replace the ordinary queue with a double-ended queue; if a node has not entered the queue before, insert it at the tail, otherwise insert it at the head.
    
    For more optimizations and Hack methods targeting these optimizations, see [fstqwq's answer on Zhihu](https://www.zhihu.com/question/292283275/answer/484871888).

## Dijkstra algorithm

The Dijkstra (/ˈdikstrɑ/ or /ˈdɛikstrɑ/) algorithm was discovered by the Dutch computer scientist E. W. Dijkstra in 1956 and publicly published in 1959. It is an algorithm for solving the single-source shortest path on a **non-negative-weight graph**.

### Procedure

Divide the nodes into two sets: the set of points with determined shortest-path length (denoted as the $S$ set) and the set of points with undetermined shortest-path length (denoted as the $T$ set). At the beginning all points belong to the $T$ set.

Initialize $dis(s)=0$, and the $dis$ of all other points to $+\infty$.

Then repeat these operations:

1.  From the $T$ set, select a node with the smallest shortest-path length, and move it to the $S$ set.
2.  Perform relax operations on all out-edges of the nodes just added to the $S$ set.

Until the $T$ set is empty, and the algorithm ends.

### Time complexity

The naive implementation method is that each time after operation 2 is executed, directly brute-force search the $T$ set for the node with the smallest shortest-path length. The total time complexity of operation 2 is $O(m)$, the total time complexity of operation 1 is $O(n^2)$, and the time complexity of the whole process is $O(n^2 + m) = O(n^2)$.

We can use a heap to optimize this process: each time an edge $(u,v)$ is successfully relaxed, insert $v$ into the heap (if $v$ is already in the heap, directly perform Decrease-key), and operation 1 just takes the heap-top node. There are a total of $O(m)$ Decrease-keys and $O(n)$ pops; choosing different heaps can achieve different complexities, refer to the [heap](../ds/heap.md) page. The best complexity that heap optimization can achieve is $O(n\log n+m)$; the ones that can achieve this complexity include the Fibonacci heap, etc.

In particular, we can maintain it with a priority queue; at this time we cannot perform the Decrease-key operation, but we can re-insert this node each time we relax, and check when popping whether this node has already been relaxed, and if so skip it; the complexity is $O(m\log n)$, and the advantage is that the implementation is relatively simple.

The heap here can also be implemented with a segment tree, with complexity $O(m\log n)$; under some special non-recursive segment tree implementations, this approach has a smaller constant factor than the heap. And the segment tree supports more operations; on some special graph problems, only a segment tree can be used to maintain it.

In a sparse graph, $m = O(n)$, and the heap-optimized Dijkstra algorithm has a large efficiency advantage; while in a dense graph, $m = O(n^2)$, at which time using the naive implementation is better.

### Correctness proof

Below we use mathematical induction to prove the correctness of the Dijkstra algorithm under the premise that **all edge weights are non-negative**[^1].

Simply put, what we want to prove is that when executing operation 1, the shortest path of the taken-out node $u$ has already been determined, i.e. it satisfies $D(u) = dis(u)$.

Initially $S = \varnothing$, and the assumption holds.

Next use proof by contradiction.

Let point $u$ be the first point in the algorithm that does not satisfy $D(u) = dis(u)$ when added to the $S$ set. Because point $s$ definitely satisfies $D(u)=dis(u)=0$, and it must be the first point added to the $S$ set, so before adding $u$ to the $S$ set, $S \neq \varnothing$; if there is no path from $s$ to $u$, then $D(u) = dis(u) = +\infty$, contradicting the assumption.

So there must exist a path $s \to x \to y \to u$, where $y$ is the first point belonging to the $T$ set on the $s \to u$ path, and $x$ is the predecessor node of $y$ (obviously $x \in S$). It should be noted that there may be the case $s = x$ or $y = u$, i.e. $s \to x$ or $y \to u$ may be an empty path.

Because the nodes added before node $u$ all satisfy $D(u) = dis(u)$, so when point $x$ was added to the $S$ set, we have $D(x) = dis(x)$; at this time edge $(x,y)$ was relaxed, from which we can prove that when $u$ is added to $S$, we must have $D(y)=dis(y)$.

Below we prove that $D(u) = dis(u)$ holds. In the path $s \to x \to y \to u$, because all edge weights on the graph are non-negative, so $D(y) \leq D(u)$. Thus $dis(y) = D(y) \leq D(u)\leq dis(u)$. But because when node $u$ was taken out of the $T$ set in operation 1, node $y$ had not yet been taken out of the $T$ set, so at this time we have $dis(u)\leq dis(y)$, from which we get $dis(y) = D(y) = D(u) = dis(u)$, which contradicts the assumption $D(u)\neq dis(u)$, so the assumption does not hold.

Therefore we have proved that the point taken out each time in operation 1 has its shortest path already determined. The proposition is proved.

Note that the key inequality $D(y) \leq D(u)$ in the proof process is derived under the condition that all edge weights on the graph are non-negative. When there are negative-weight edges on the graph, this inequality no longer holds, and the correctness of the Dijkstra algorithm cannot be guaranteed; the algorithm may give an incorrect result.

### Implementation

Here we give both the $O(n^2)$ brute-force implementation and the $O(m \log m)$ priority-queue implementation.

???+ note "Naive implementation"
    === "C++"
        ```cpp
        struct edge {
          int v, w;
        };
        
        vector<edge> e[MAXN];
        int dis[MAXN], vis[MAXN];
        
        void dijkstra(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          dis[s] = 0;
          for (int i = 1; i <= n; i++) {
            int u = 0, mind = 0x3f3f3f3f;
            for (int j = 1; j <= n; j++)
              if (!vis[j] && dis[j] < mind) u = j, mind = dis[j];
            vis[u] = true;
            for (auto ed : e[u]) {
              int v = ed.v, w = ed.w;
              if (dis[v] > dis[u] + w) dis[v] = dis[u] + w;
            }
          }
        }
        ```
    
    === "Python"
        ```python
        class Edge:
            def __init(self, v=0, w=0):
                self.v = v
                self.w = w
        
        
        e = [[Edge() for i in range(MAXN)] for j in range(MAXN)]
        INF = 0x3F3F3F3F
        
        
        def dijkstra(n, s):
            dis = [INF] * (n + 1)
            vis = [0] * (n + 1)
        
            dis[s] = 0
            for i in range(1, n + 1):
                u = 0
                mind = INF
                for j in range(1, n + 1):
                    if not vis[j] and dis[j] < mind:
                        u = j
                        mind = dis[j]
                vis[u] = True
                for ed in e[u]:
                    v, w = ed.v, ed.w
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
        ```

???+ note "Priority-queue implementation"
    === "C++"
        ```cpp
        struct edge {
          int v, w;
        };
        
        struct node {
          int dis, u;
        
          bool operator>(const node& a) const { return dis > a.dis; }
        };
        
        vector<edge> e[MAXN];
        int dis[MAXN], vis[MAXN];
        priority_queue<node, vector<node>, greater<node>> q;
        
        void dijkstra(int n, int s) {
          memset(dis, 0x3f, (n + 1) * sizeof(int));
          memset(vis, 0, (n + 1) * sizeof(int));
          dis[s] = 0;
          q.push({0, s});
          while (!q.empty()) {
            int u = q.top().u;
            q.pop();
            if (vis[u]) continue;
            vis[u] = 1;
            for (auto ed : e[u]) {
              int v = ed.v, w = ed.w;
              if (dis[v] > dis[u] + w) {
                dis[v] = dis[u] + w;
                q.push({dis[v], v});
              }
            }
          }
        }
        ```
    
    === "Python"
        ```python
        def dijkstra(e, s):
            """
            Input:
            e: adjacency list
            s: start point
            Returns:
            dis: shortest-path length from s to each vertex
            """
            dis = defaultdict(lambda: float("inf"))
            dis[s] = 0
            q = [(0, s)]
            vis = set()
            while q:
                _, u = heapq.heappop(q)
                if u in vis:
                    continue
                vis.add(u)
                for v, w in e[u]:
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heapq.heappush(q, (dis[v], v))
            return dis
        ```

## Johnson all-source shortest path algorithm

Johnson, like Floyd, is an algorithm that can find the shortest path between any two points on a graph with no negative cycle. This algorithm was proposed in 1977 by Donald B. Johnson.

The shortest path between any two points can be solved by enumerating the start point and running the Bellman–Ford algorithm $n$ times, with time complexity $O(n^2m)$; it can also be solved directly with the Floyd algorithm, with time complexity $O(n^3)$.

Note that the time complexity of the heap-optimized Dijkstra algorithm for finding the single-source shortest path is better than Bellman–Ford; if we enumerate the start point and run the Dijkstra algorithm $n$ times, we can solve this problem in $O(nm\log m)$ (depending on the implementation of the Dijkstra algorithm) time complexity, which is better than the time complexity of running the Bellman–Ford algorithm $n$ times above, and on sparse graphs is also better than the time complexity of the Floyd algorithm.

But the Dijkstra algorithm cannot correctly solve the shortest path with negative-weight edges, so we need to preprocess the edges on the original graph to ensure that all edge weights are non-negative.

An easily-thought-of method is to simultaneously add a positive number $x$ to the edge weights of all edges, thereby making all edge weights non-negative. If the shortest path from the start point to the end point on the new graph passes through $k$ edges, then subtracting $kx$ from the shortest path gives the actual shortest path.

But this method is wrong. Consider the following graph:

![](./images/shortest-path1.svg)

The shortest path from $1 \to 2$ is $1 \to 5 \to 3 \to 2$, with length $−2$.

But what if we add $5$ to the edge weight of each edge?

![](./images/shortest-path2.svg)

The shortest path from $1 \to 2$ on the new graph is $1 \to 4 \to 2$, which is no longer the actual shortest path.

The Johnson algorithm instead re-labels the edge weights of each edge through another method.

We create a new virtual node (here we set its number to $0$). From this point, connect an edge of weight $0$ to all other points.

Next, use the Bellman–Ford algorithm to find the shortest path from point $0$ to all other points, denoted $h_i$.

If there is an edge from point $u$ to point $v$ with edge weight $w$, then we reset the edge weight of this edge to $w+h_u-h_v$.

Next, with each point as the start point, run $n$ rounds of the Dijkstra algorithm to find the shortest path between any two points.

The initial Bellman–Ford algorithm is not the time bottleneck; if the Dijkstra algorithm is implemented with `priority_queue`, the time complexity of this algorithm is $O(nm\log m)$.

### Correctness proof

Why is this way of re-labeling edge weights correct?

Before discussing this problem, let us first discuss a physics concept——potential energy.

Potential energies such as gravitational potential energy and electric potential energy all have a characteristic: the change in potential energy is only related to the relative position of the start point and end point, and is unrelated to the path taken from the start point to the end point.

Potential energy also has a characteristic: the absolute value of potential energy often depends on the set zero-potential-energy point, but no matter where the zero-potential-energy point is set, the difference in potential energy between two points is fixed.

Next, back to the main topic.

On the re-labeled graph, the length expression of a path $s \to p_1 \to p_2 \to \dots \to p_k \to t$ from point $s$ to point $t$ is as follows:

$(w(s,p_1)+h_s-h_{p_1})+(w(p_1,p_2)+h_{p_1}-h_{p_2})+ \dots +(w(p_k,t)+h_{p_k}-h_t)$

After simplification we get:

$w(s,p_1)+w(p_1,p_2)+ \dots +w(p_k,t)+h_s-h_t$

No matter which path we take from $s$ to $t$, the value of $h_s-h_t$ is unchanged, which exactly coincides with the property of potential energy!

For convenience, below we call $h_i$ the potential energy of point $i$.

The length expression of the shortest path $s \to t$ in the new graph above consists of two parts: the front edge-weight sum is the shortest path $s \to t$ in the original graph, and the back is the potential-energy difference between the two points. Because the potential-energy difference between two points is fixed, so the shortest path $s \to t$ on the original graph corresponds to the shortest path $s \to t$ on the new graph.

By here our correctness proof is already half solved——we have proved that the shortest path on the graph after re-labeling edge weights is still the original shortest path. Next we need to prove that all edge weights in the new graph are non-negative, because on a non-negative-weight graph, the Dijkstra algorithm can guarantee a correct result.

According to the triangle inequality, the two points on any edge $(u,v)$ on the graph satisfy: $h_v \leq h_u + w(u,v)$. The edge weight of this edge after re-labeling is $w'(u,v)=w(u,v)+h_u-h_v \geq 0$. Thus we have proved that the edge weights on the new graph are all non-negative.

In this way, we have proved the correctness of the Johnson algorithm.

## Comparison of different methods

| Shortest-path algorithm | Floyd | Bellman–Ford | Dijkstra | Johnson |
| ------- | ---------- | ------------ | ------------ | ------------- |
| Shortest-path type | Shortest path between every pair of nodes | Single-source shortest path | Single-source shortest path | Shortest path between every pair of nodes |
| Applies to | Any graph | Any graph | Non-negative-weight graph | Any graph |
| Can detect negative cycle? | Yes | Yes | No | Yes |
| Time complexity | $O(N^3)$ | $O(NM)$ | $O(M\log M)$ | $O(NM\log M)$ |

Note: The Dijkstra algorithm in the table is implemented with `priority_queue` when computing complexity.

## Outputting the scheme

Open a `pre` array, record when updating distances how the following point is transferred to, and recursively output the path before the algorithm ends.

For example, Floyd records `pre[i][j] = k;`, and Bellman–Ford and Dijkstra generally record `pre[v] = u`.

## Some special cases

-   Shortest path on a graph where edge weights consist only of $0$ and $1$: [0-1 BFS](./bfs.md#double-ended-queue-bfs);
-   Shortest-path problem allowing at most $k$ operations such as changing path cost: [layered graph shortest path](./node.md#layered-graph-shortest-path).

## References and notes

[^1]: 《Introduction to Algorithms (3rd edition Chinese translation)》, China Machine Press, 2013, pp. 384-385.
