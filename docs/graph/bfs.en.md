author: Ir1d, greyqz, yjl9903, Anguei, Marcythm, ChungZH, Xeonacid, ylxmf2005

The full name of BFS is [Breadth First Search](https://en.wikipedia.org/wiki/Breadth-first_search).

It is one of the most basic and important search algorithms on graphs.

So-called breadth-first: each time it tries to visit the nodes of the same layer.
If the same layer is all visited, then it visits the next layer.

The result of this is that the path found by the BFS algorithm is the **shortest** valid path from the start point. In other words, this path contains the minimum number of edges.

When BFS ends, each node is visited via the shortest path from the start point to that point.

The algorithm process can be seen as the process of flame spreading on the graph: at the beginning only the start point is on fire, and at each moment, the nodes on fire spread the flame to all their adjacent nodes.

## Implementation

The C++ and Python code implementations below are based on the chained forward-star graph storage method; for its implementation see the [graph storage](./save.md) page.

=== "Pseudocode"
    ```text
    bfs(s) {
      q = new queue()
      q.push(s), visited[s] = true
      while (!q.empty()) {
        u = q.pop()
        for each edge(u, v) {
          if (!visited[v]) {
            q.push(v)
            visited[v] = true
          }
        }
      }
    }
    ```

=== "C++"
    ```cpp
    void bfs(int u) {
      while (!Q.empty()) Q.pop();
      Q.push(u);
      vis[u] = 1;
      d[u] = 0;
      p[u] = -1;
      while (!Q.empty()) {
        u = Q.front();
        Q.pop();
        for (int i = head[u]; i; i = e[i].nxt) {
          if (!vis[e[i].to]) {
            Q.push(e[i].to);
            vis[e[i].to] = 1;
            d[e[i].to] = d[u] + 1;
            p[e[i].to] = u;
          }
        }
      }
    }
    
    void restore(int x) {
      vector<int> res;
      for (int v = x; v != -1; v = p[v]) {
        res.push_back(v);
      }
      std::reverse(res.begin(), res.end());
      for (int i = 0; i < res.size(); ++i) printf("%d", res[i]);
      puts("");
    }
    ```

=== "Python"
    ```python
    from queue import Queue
    
    
    def bfs(u):
        Q = Queue()
        Q.put(u)
        vis[u] = True
        d[u] = 0
        p[u] = -1
        while Q.qsize() != 0:
            u = Q.get()
            i = head[u]
            while i:
                if vis[e[i].to] == False:
                    Q.put(e[i].to)
                    vis[e[i].to] = True
                    d[e[i].to] = d[u] + 1
                    p[e[i].to] = u
                i = e[i].nxt
    
    
    def restore(x):
        res = []
        v = x
        while v != -1:
            res.append(v)
            v = p[v]
        res.reverse()
        for i in range(0, len(res)):
            print(res[i])
    ```

Specifically, we use a queue Q to record the nodes to be processed, then create a boolean array `vis[]` to mark whether a certain node has been visited.

At the beginning, we set the `vis` value of all nodes to 0, indicating not visited; then put the start point s into the queue Q and set `vis[s]` to 1.

After that, each time we take out the front node u from the queue Q, then mark all nodes v adjacent to u as visited and put them into the queue Q.

Loop until the queue Q is empty, indicating BFS ends.

During the BFS process, some extra information can also be recorded. For example, in the above code, the d array is used to record the shortest distance from the start point to a certain node (the minimum number of edges to pass), and the p array records from which node the current node is reached.

With the d array, one can conveniently obtain the distance from the start point to a node.

With the p array, one can conveniently restore the shortest path from the start point to a point. The `restore` function in the above code uses this array to output in turn the nodes passed by the shortest path from the start point to node x.

Time complexity $O(n + m)$

Space complexity $O(n)$ (the `vis` array and the queue)

## open-closed table

When implementing BFS, essentially we put the not-yet-visited nodes in a container called open, and put the already-visited nodes in a container called closed.

## BFS on trees/graphs

### BFS sequence

Similar to the DFS sequence, the BFS sequence refers to the sequence of node numbers visited during the BFS process.

### BFS on a general graph

If the original graph is not connected, only the points reachable from the start point can be visited.

The BFS sequence is usually also not unique.

Similarly, we can also define the BFS tree: during the BFS process, by recording from which point each node is visited, one can establish a tree structure, which is the BFS tree.

## Applications

-   Find the shortest path from the start point to all other points on an unweighted graph.
-   Find all connected components in $O(n+m)$ time. (We only need to do BFS starting from each not-yet-visited node; obviously each BFS will traverse a connected component)
-   If we regard an action in a game as an edge (a transition) on the state graph, then BFS can be used to find the minimum number of steps needed to go from one state to another state in the game.
-   Find the minimum cycle in a directed unweighted graph. (Do BFS starting from each point; when we are about to arrive at a point previously visited from the start, we know we have encountered a cycle. The minimum cycle of the graph is the average of the minimum cycles obtained from each BFS.)
-   Find edges that are definitely on a shortest path of $(a, b)$. (Do BFS from a and b separately to obtain two d arrays. Then for each edge $(u, v)$, if $d_a[u]+1+d_b[v]=d_a[b]$, then this edge is on a shortest path)
-   Find points that are definitely on a shortest path of $(a, b)$. (Do BFS from a and b separately to obtain two d arrays. Then for each point v, if $d_a[v]+d_b[v]=d_a[b]$, then this point is on some shortest path)
-   Find a shortest path of even length. (We need to construct a new graph, splitting each point into two new points; an edge $(u, v)$ of the original graph becomes $((u, 0), (v, 1))$ and $((u, 1), (v, 0))$. Do BFS on the new graph, and the shortest path between $(s, 0)$ and $(t, 0)$ is what is sought)
-   Find the shortest path on a graph with edge weights 0/1, see double-ended queue BFS below.

## Double-ended queue BFS

If you are not familiar with the double-ended queue `deque`, please refer to the [deque related section](../lang/csl/sequence-container.md#deque).

Double-ended queue BFS is also called 0-1 BFS.

### Scope of application

Edge weights may or may not exist (since BFS applies to graphs with weight 1, generally the weight is 0 or 1), or a shortest-path problem that can be converted to such edge weights.

For example, in the maze problem, you can spend 1 gold coin to walk 5 steps, or spend no gold coin to walk 1 step; this can be solved with 0-1 BFS.

### Implementation

Generally, we put the points reached by edges without weight at the front of the queue, and put the points reached by edges with weight at the back of the queue. This guarantees that, like ordinary BFS, the weight from the front to the back of the whole queue is monotonically non-decreasing.

Below is the pseudocode:

```cpp
while (queue is not empty) {
  int u = front of queue;
  pop the front of the queue;
  for (enumerate the neighbors of u) {
    update data
    if (...)
      add to the front of the queue;
    else
      add to the back of the queue;
  }
}
```

### Example problem

### [Codeforces 173B](http://codeforces.com/problemset/problem/173/B)

An $n \times m$ grid; now there is a laser beam shooting out to the right from the top-left corner; each time it encounters a '#', you can choose to have the light shoot out in four directions, or do nothing; ask the minimum number of '#'s that need to shoot in four directions so that the light shoots out to the right in row $n$.

The intended solution of this problem is not 0-1 BFS, but 0-1 BFS applies and reduces the thinking intensity; many masters did it this way during the contest.

The approach is very simple: shooting out in one direction costs nothing (0), while shooting out in four directions costs (1), then just do it directly.

#### Code

```cpp
--8<-- "docs/graph/code/bfs/bfs_1.cpp"
```

## Priority-queue BFS

A priority queue is equivalent to a binary heap; the STL provides [`std::priority_queue`](../lang/csl/container-adapter.md), which conveniently lets us use a priority queue.

In priority-queue-based BFS, each time we take out the node with the smallest cost from the front of the queue for further search. It is easy to prove that this greedy idea is correct, because the search expanded from this node will definitely not update those originally-higher-cost nodes. In other words, for the remaining higher-cost nodes, we do not go back to consider updating them.

Of course, each node may be enqueued multiple times, only that the cost of each enqueue is different. When this node is taken out of the priority queue for the first time, there is no need to search at this node afterwards; just ignore it directly. So, in priority-queue BFS, each node is processed only once.

Compared with ordinary-queue BFS, the time complexity has an extra $\log n$, after all we have to maintain this priority queue. However, ordinary BFS may have each node enqueued and dequeued multiple times, and the time complexity can reach $O(n^2)$, not $O(n)$. So priority-queue BFS is usually still fast.

Huh? Why does this sound so much like the heap-optimized [Dijkstra](./shortest-path.md#dijkstra-algorithm) algorithm? In fact, heap-optimized Dijkstra is priority-queue BFS.

## Exercises

-   [「NOIP2017」Cheese](https://uoj.ac/problem/332)

Double-ended queue BFS:

-   [CF1063B. Labyrinth](https://codeforces.com/problemset/problem/1063/B)
-   [CF173B. Chamber of Secrets](https://codeforces.com/problemset/problem/173/B)
-   [「BalticOI 2011 Day1」Switch the Lamp On](https://loj.ac/p/2632)

## Reference

<https://cp-algorithms.com/graph/breadth-first-search.html>
