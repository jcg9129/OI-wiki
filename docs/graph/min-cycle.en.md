## Introduction

???+ question "Problem"
    Given a graph, how large is the cycle with the minimum sum of edge weights formed by $n$ nodes ($n\ge 3$)?

The minimum cycle of a graph is also called the girth.

## Procedure

### Brute-force solution

Suppose there is an edge of length $w$ between $u$ and $v$, and $dis(u,v)$ denotes the shortest path between $u$ and $v$ after deleting the edge between $u$ and $v$.

Then the minimum cycle in the undirected graph is $dis(u,v)+w$.

Note that if we are finding the minimum cycle in a directed graph, the corresponding formula must be modified: the minimum cycle is $dis(v,u)+w$.

The total time complexity is $O(n^2m)$.

### Dijkstra

Related link: [Shortest path/Dijkstra](./shortest-path.md#dijkstra-algorithm)

#### Procedure

Enumerate all edges; each time, after deleting an edge, run Dijkstra once for the start point of this edge; the reasoning is the same as above.

#### Properties

The time complexity is $O(m(n+m)\log n)$.

### Floyd

Related link: [Shortest path/Floyd](./shortest-path.md#floyd-algorithm)

#### Procedure

Denote the edge weight of the edge between $u,v$ in the original graph as $val\left(u,v\right)$.

We note that the Floyd algorithm has a property: when the outermost loop reaches point $k$ (before the $k$-th iteration has started), in the shortest-path array $dis$, $dis_{u,v}$ denotes the shortest path from $u$ to $v$ passing only through points whose numbers are in the interval $\left[1, k\right)$.

By the definition of the minimum cycle, we know that it has at least three vertices. Let the vertex with the largest number among them be $w$, and the two points adjacent to $w$ on both sides of the cycle be $u,v$; then when the outermost loop enumerates $k=w$, the length of this cycle is $dis_{u,v}+val\left(v,w\right)+val\left(w,u\right)$.

Therefore, during the loop, for each $k$ enumerate the $(i,j)$ satisfying $i<k,j<k$, and update the answer.

#### Recording the path

Now we already know that the form of the cycle is $u\to k\to v$, and then from $v$ back to $u$ (the numbers of the points passed are all $<k$).

The problem is transformed into finding the path $v\leadsto u$. By the triangle inequality $dis_{u,v}\le dis_{u,i}+dis_{i,v}$, consider recording $pos_{u,v}=j$, denoting the point that makes $dis_{u,v}=dis_{u,j}+dis_{j,v}$. Obviously $j$ is on the path $v\leadsto u$.

So we can transform the path into two segments $v\leadsto j$ and $j\leadsto u$, and process each recursively.

???+ note "Proof that the recursion will not fall into an infinite loop"
    Use proof by contradiction.
    
    Assume the cycle repeatedly passes through a point $u$; then there must be an edge on the cycle that starts from $u$, passes through several edges, and returns to $u$. This constitutes a new cycle.
    
    Since there is no negative cycle in the graph (if there were a negative cycle there would be no minimum cycle), the sum of the edge weights of the new cycle must be less than or equal to that of the original cycle.
    
    So we only need to take this one cycle, and then it will not repeatedly pass through a point $u$; the assumption does not hold, so the cycle will not repeatedly pass through a point.
    
    So when recursing to the two points $u,v$, their $pos_{u,v}$ must not equal the numbers of the two points, i.e. a new point has been added.
    
    In particular, when $u$ and $v$ are adjacent, we can directly return.
    
    Since the total number of points is $n$, the number of times a new point is added (i.e. the number of recursions) will not exceed $n$, so the recursion will not fall into an infinite loop.

#### Properties

Time complexity: $O(n^3)$.

#### Implementation

Below are reference implementations in C++ and Python (recording the path):

=== "C++"
    ```cpp
    // number of points of the graph is n
    int val[MAXN + 1][MAXN + 1];  // adjacency matrix of the original graph
    int cnt, path[MAXN + 5];      // record the path and length of the minimum cycle
    
    void get_path(int u, int v) {  // get the path between u and v
      if (pos[u][v] == 0) return;
    
      int k = pos[u][v];
      get_path(u, k);
      path[++cnt] = k;
      get_path(k, v);
    }
    
    void Floyd(const int &n) {
      static int dis[MAXN + 1][MAXN + 1];  // shortest-path matrix
      static int pos[MAXN + 1][MAXN + 1];
      memcpy(dis, val, sizeof(val));
      memset(pos, 0, sizeof(pos));
      for (int k = 1; k <= n; ++k) {
        for (int i = 1; i < k; ++i)
          for (int j = 1; j < i; ++j)
            if (ans >
                (long long)val[i][k] + val[k][j] + dis[i][j]) {  // found a shorter cycle
              // since j<i<k is guaranteed here, the three points are distinct, so no zero cycle appears.
              ans = val[i][k] + val[k][j] + dis[i][j], cnt = 0;
              path[++cnt] = i, path[++cnt] = k,
              path[++cnt] = j;  // add the three points i,k,j in order
              get_path(j, i);   // add the path from j to i
            }
    
        for (int i = 1; i <= n; ++i)  // normal Floyd update of shortest paths
          for (int j = 1; j <= n; ++j) {
            if (dis[i][j] > dis[i][k] + dis[k][j]) {
              dis[i][j] = dis[i][k] + dis[k][j];
              pos[i][j] = k;  // the current path can be updated via k
            }
          }
      }
    }
    ```

=== "Python"
    ```python
    # define a sufficiently large value to represent infinity
    INF = sys.maxsize
    
    
    def get_path(i, j, pos, path, cnt):
        """
        Recursively get the intermediate nodes on the shortest path from node i to node j.
    
        Args:
            i (int): start node (0-based index).
            j (int): end node (0-based index).
            pos (list[list[int]]): matrix recording the intermediate nodes of shortest paths. pos[i][j] = k means the shortest path from i to j passes through k.
            path (list[int]): list storing the path nodes (using 0-based index).
            cnt (int): current number of path nodes.
    
        Returns:
            int: updated number of path nodes.
        """
        # if pos[i][j] is -1, it means there is no intermediate node from i to j
        if pos[i][j] == -1:
            return cnt
    
        # get the intermediate node k
        k = pos[i][j]
        # recursively get the path from i to k
        cnt = get_path(i, k, pos, path, cnt)
        # add the intermediate node k to the path
        path[cnt] = k
        cnt += 1
        # recursively get the path from k to j
        cnt = get_path(k, j, pos, path, cnt)
        return cnt
    
    
    def find_minimum_cycle_undirected(n, edges):
        """
        Use the Floyd-Warshall algorithm to find the minimum cycle in an undirected graph.
    
        Args:
            n (int): number of nodes of the graph (1 to n).
            edges (list[tuple]): list of edges, each element is (u, v, w), meaning there is an edge of weight w between nodes u and v.
                                 node indices are 1 to n.
    
        Returns:
            tuple: contains the length and path of the minimum cycle.
                   if no cycle exists, returns (INF, []).
                   the path is a list of node indices (1-based index).
        """
        # internally use 0-based indexing
        N = n
        # initialize the adjacency matrix g, representing the weights of the original edges
        g = [[INF for _ in range(N)] for _ in range(N)]
        # initialize the shortest-path matrix dis, initially the same as g
        dis = [[INF for _ in range(N)] for _ in range(N)]
        # initialize the pos matrix, recording the intermediate nodes of shortest paths
        pos = [[-1 for _ in range(N)] for _ in range(N)]
    
        # initialize the diagonal to 0 (distance from a node to itself)
        for i in range(N):
            g[i][i] = 0
            dis[i][i] = 0
    
        # build the adjacency matrix from the input edges (undirected graph)
        for u, v, w in edges:
            # convert 1-based index to 0-based
            u -= 1
            v -= 1
            # for an undirected graph, edges are bidirectional
            g[u][v] = min(g[u][v], w)
            g[v][u] = min(g[v][u], w)
            dis[u][v] = min(dis[u][v], w)
            dis[v][u] = min(dis[v][u], w)
    
        # initialize the minimum cycle length to infinity
        min_cycle_len = INF
        # initialize the minimum cycle path
        min_cycle_path = []
    
        # core part of the Floyd-Warshall algorithm
        # k as the intermediate node (0-based index)
        for k in range(N):
            # before updating dis[i][j], check whether passing through node k can form a smaller cycle
            # the cycle consists of i -> k -> j -> ... -> i
            # here dis[i][j] is the shortest path when considering nodes 0 to k-1 as intermediate nodes
            # the C++ code uses the loop order i < k and j < i, and this logic is also followed here (0-based)
            for i in range(k):  # 0 <= i < k
                for j in range(i):  # 0 <= j < i
                    # check whether i, k, j form a cycle, connected through dis[i][j]
                    # ensure that the original edges g[i][k] and g[k][j] exist (not INF)
                    # and the shortest path dis[i][j] from i to j exists (not INF)
                    if g[i][k] != INF and g[k][j] != INF and dis[i][j] != INF:
                        current_cycle_len = g[i][k] + g[k][j] + dis[i][j]
                        if current_cycle_len < min_cycle_len:
                            min_cycle_len = current_cycle_len
                            # reconstruct the path
                            path = [0] * (N + 5)  # array to temporarily store the path, large enough
                            cnt = 0
                            # add to the path in the order i, k, j
                            path[cnt] = i
                            cnt += 1
                            path[cnt] = k
                            cnt += 1
                            path[cnt] = j
                            cnt += 1
                            # get the intermediate nodes on the shortest path from j to i (using the previously computed dis and pos)
                            cnt = get_path(j, i, pos, path, cnt)
                            # extract the actual path nodes (removing the unused part)
                            # convert 0-based index to 1-based
                            min_cycle_path = [node + 1 for node in path[:cnt]]
    
            # standard Floyd-Warshall update of shortest paths
            for i in range(N):
                for j in range(N):
                    if (
                        dis[i][k] != INF
                        and dis[k][j] != INF
                        and dis[i][j] > dis[i][k] + dis[k][j]
                    ):
                        dis[i][j] = dis[i][k] + dis[k][j]
                        # record that the shortest path from i to j passes through k
                        pos[i][j] = k
    
        return min_cycle_len, min_cycle_path
    ```

## Template problem

??? note "[AcWing 344 Sightseeing tour](https://www.acwing.com/problem/content/346)"
    Given an undirected graph with $n$ points, find a cycle in the graph containing at least $3$ points, where the nodes on the cycle are not repeated, and the sum of the lengths of the edges on the cycle is minimized.
    
    This problem is called the minimum cycle problem of an undirected graph.
    
    You need to output the scheme of the minimum cycle; if the minimum cycle is not unique, outputting any one is acceptable.
    
    $n \le 100$

The time complexity accepts an $O(n^3)$ approach; just apply the approach of finding the minimum cycle with Floyd.

=== "C++"
    ```cpp
    #include <bits/stdc++.h>
    using lint = long long;
    // define a sufficiently large constant to represent the maximum number of nodes of the graph
    const int MAXN = 110;
    
    // define a sufficiently large value to represent infinity, initializing the minimum cycle length
    lint ans = 1e9;  // lint is an alias of long long
    
    // number of nodes n, number of edges m of the graph
    // cnt records the number of nodes in the minimum cycle path
    // path stores the path nodes of the minimum cycle
    int n, m, cnt, path[MAXN];
    
    // g stores the adjacency matrix of the original graph
    // dis stores the shortest-path matrix (updated during the Floyd-Warshall computation)
    // pos records the intermediate nodes of shortest paths; pos[i][j] = k means the shortest path from i to j passes through k
    int g[MAXN][MAXN], dis[MAXN][MAXN], pos[MAXN][MAXN];
    
    // recursive function: get the intermediate nodes on the shortest path from node u to node v
    // reconstruct the path according to the pos matrix
    void get_path(int u, int v) {
      // if pos[u][v] is 0, it means there is no intermediate node from u to v, return directly
      if (pos[u][v] == 0) return;
    
      // get the intermediate node k
      int k = pos[u][v];
      // recursively get the path from u to k
      get_path(u, k);
      // add the intermediate node k to the path
      path[++cnt] = k;
      // recursively get the path from k to v
      get_path(k, v);
    }
    
    // Floyd-Warshall algorithm function: find the minimum cycle in the graph
    void Floyd() {
      // outer loop: k as the intermediate node (1 to n)
      for (int k = 1; k <= n; ++k) {
        // inner loop: i and j, used to check whether passing through node k can form a smaller cycle
        // here the loop order is i from 1 to k-1, j from 1 to i-1
        // this can check the cycle formed by i -> k -> j -> ... -> i
        for (int i = 1; i < k; ++i)
          for (int j = 1; j < i; ++j)
            // check whether connecting i and j through node k forms a smaller cycle
            // the cycle length is the original edge weight g[i][k] from i to k + the original edge weight g[k][j] from k to j
            // + the current shortest path dis[i][j] from i to j
            if (ans > (long long)g[i][k] + g[k][j] + dis[i][j]) {
              // found a smaller cycle
              ans = g[i][k] + g[k][j] + dis[i][j];  // update the minimum cycle length
              cnt = 0;                              // reset the path count
              // add i, k, j to the path in order
              path[++cnt] = i, path[++cnt] = k, path[++cnt] = j;
              // get the intermediate nodes on the shortest path from j to i, and add them to the path
              get_path(j, i);
            }
    
        // standard Floyd-Warshall update of shortest paths
        // i from 1 to n, j from 1 to n
        for (int i = 1; i <= n; ++i)
          for (int j = 1; j <= n; ++j) {
            // if a shorter path from i to j can be obtained through intermediate node k
            if (dis[i][j] > dis[i][k] + dis[k][j]) {
              // update the shortest path
              dis[i][j] = dis[i][k] + dis[k][j];
              // record that the shortest path from i to j passes through k
              pos[i][j] = k;
            }
          }
      }
    }
    
    // main function
    int main() {
      // read the number of nodes n and the number of edges m
      std::cin >> n >> m;
      // initialize the original adjacency matrix g, setting the weights of all edges to infinity (0x3f usually represents a very large value)
      memset(g, 0x3f, sizeof(g));
      // set the distance from a node to itself to 0
      for (int i = 1; i <= n; ++i) g[i][i] = 0;
      // read m edges, building the original adjacency matrix g
      // for an undirected graph, edges are bidirectional, take the smaller weight
      for (int i = 0, u, v, w; i < m; ++i) {
        std::cin >> u >> v >> w;
        g[u][v] = g[v][u] = std::min(g[u][v], w);
      }
      // copy the original adjacency matrix g to the shortest-path matrix dis
      memcpy(dis, g, sizeof(g));
      // call the Floyd algorithm to find the minimum cycle
      Floyd();
      // determine whether a cycle exists based on the minimum cycle length
      if (ans == 1e9) {  // if the minimum cycle length is still infinity, it means no cycle exists
        puts("No solution.");
      } else {
        // if a cycle exists, print the path nodes
        // std::cout << "ans = " << ans << std::endl; // print the minimum cycle length (commented out)
        // print the path nodes, separated by spaces
        for (int i = 1; i <= cnt; ++i)
          std::cout << path[i]
                    << (i == cnt ? "" : " ");  // no space after the last node
        std::cout << std::endl;                // newline after the path is printed
      }
      return 0;
    }
    ```

=== "Python"
    ```python
    import copy
    import sys
    
    # define a sufficiently large value to represent infinity
    INF = sys.maxsize
    
    
    def get_path(i, j, pos, path, cnt):
        """
        Recursively get the intermediate nodes on the shortest path from node i to node j.
    
        Args:
            i (int): start node (0-based index).
            j (int): end node (0-based index).
            pos (list[list[int]]): matrix recording the intermediate nodes of shortest paths. pos[i][j] = k means the shortest path from i to j passes through k.
            path (list[int]): list storing the path nodes (using 0-based index).
            cnt (int): current number of path nodes.
    
        Returns:
            int: updated number of path nodes.
        """
        # if pos[i][j] is -1, it means there is no intermediate node from i to j
        if pos[i][j] == -1:
            return cnt
    
        # get the intermediate node k
        k = pos[i][j]
        # recursively get the path from i to k
        cnt = get_path(i, k, pos, path, cnt)
        # add the intermediate node k to the path
        path[cnt] = k
        cnt += 1
        # recursively get the path from k to j
        cnt = get_path(k, j, pos, path, cnt)
        return cnt
    
    
    def find_minimum_cycle_undirected(n, edges):
        """
        Use the Floyd-Warshall algorithm to find the minimum cycle in an undirected graph.
    
        Args:
            n (int): number of nodes of the graph (1 to n).
            edges (list[tuple]): list of edges, each element is (u, v, w), meaning there is an edge of weight w between nodes u and v.
                                 node indices are 1 to n.
    
        Returns:
            tuple: contains the length and path of the minimum cycle.
                   if no cycle exists, returns (INF, []).
                   the path is a list of node indices (1-based index).
        """
        # internally use 0-based indexing
        N = n
        # initialize the adjacency matrix g, representing the weights of the original edges
        g = [[INF for _ in range(N)] for _ in range(N)]
        # initialize the shortest-path matrix dis, initially the same as g
        dis = [[INF for _ in range(N)] for _ in range(N)]
        # initialize the pos matrix, recording the intermediate nodes of shortest paths
        pos = [[-1 for _ in range(N)] for _ in range(N)]
    
        # initialize the diagonal to 0 (distance from a node to itself)
        for i in range(N):
            g[i][i] = 0
            dis[i][i] = 0
    
        # build the adjacency matrix from the input edges (undirected graph)
        for u, v, w in edges:
            # convert 1-based index to 0-based
            u -= 1
            v -= 1
            # for an undirected graph, edges are bidirectional
            g[u][v] = min(g[u][v], w)
            g[v][u] = min(g[v][u], w)
            dis[u][v] = min(dis[u][v], w)
            dis[v][u] = min(dis[v][u], w)
    
        # initialize the minimum cycle length to infinity
        min_cycle_len = INF
        # initialize the minimum cycle path
        min_cycle_path = []
    
        # core part of the Floyd-Warshall algorithm
        # k as the intermediate node (0-based index)
        for k in range(N):
            # before updating dis[i][j], check whether passing through node k can form a smaller cycle
            # the cycle consists of i -> k -> j -> ... -> i
            # here dis[i][j] is the shortest path when considering nodes 0 to k-1 as intermediate nodes
            # the C++ code uses the loop order i < k and j < i, and this logic is also followed here (0-based)
            for i in range(k):  # 0 <= i < k
                for j in range(i):  # 0 <= j < i
                    # check whether i, k, j form a cycle, connected through dis[i][j]
                    # ensure that the original edges g[i][k] and g[k][j] exist (not INF)
                    # and the shortest path dis[i][j] from i to j exists (not INF)
                    if g[i][k] != INF and g[k][j] != INF and dis[i][j] != INF:
                        current_cycle_len = g[i][k] + g[k][j] + dis[i][j]
                        if current_cycle_len < min_cycle_len:
                            min_cycle_len = current_cycle_len
                            # reconstruct the path
                            path = [0] * (N + 5)  # array to temporarily store the path, large enough
                            cnt = 0
                            # add to the path in the order i, k, j
                            path[cnt] = i
                            cnt += 1
                            path[cnt] = k
                            cnt += 1
                            path[cnt] = j
                            cnt += 1
                            # get the intermediate nodes on the shortest path from j to i (using the previously computed dis and pos)
                            cnt = get_path(j, i, pos, path, cnt)
                            # extract the actual path nodes (removing the unused part)
                            # convert 0-based index to 1-based
                            min_cycle_path = [node + 1 for node in path[:cnt]]
    
            # standard Floyd-Warshall update of shortest paths
            for i in range(N):
                for j in range(N):
                    if (
                        dis[i][k] != INF
                        and dis[k][j] != INF
                        and dis[i][j] > dis[i][k] + dis[k][j]
                    ):
                        dis[i][j] = dis[i][k] + dis[k][j]
                        # record that the shortest path from i to j passes through k
                        pos[i][j] = k
    
        return min_cycle_len, min_cycle_path
    
    
    # --- main program entry ---
    if __name__ == "__main__":
        # read the number of nodes n and the number of edges m
        n, m = map(int, sys.stdin.readline().split())
    
        # read the edge information
        edges = []
        for _ in range(m):
            u, v, w = map(int, sys.stdin.readline().split())
            edges.append((u, v, w))
    
        # find the minimum cycle
        min_len, path = find_minimum_cycle_undirected(n, edges)
    
        # output the result
        if min_len == INF:
            print("No solution.")
        else:
            # print the path nodes (1-based index), separated by spaces
            print(" ".join(map(str, path)))
    ```

## Example problem 2

GDOI2018 Day2 Patrol

Given an undirected graph with $n$ points and no negative-weight edges, we are required to execute $q$ operations, of three kinds:

1.  Delete a point in the graph and the edges related to it
2.  Restore a deleted point and the edges related to it
3.  Query the size of the minimum cycle in which point $x$ lies

For $50\%$ of the data, $n,q \le 100$.

For every simple cycle in which each point $x$ lies, there exist two edges adjacent to $x$; deleting any one of them turns the simple cycle into a simple path.

So enumerate all edges adjacent to $x$, each time delete one of them, and then run Dijkstra once.

Or directly run Floyd once for each query to find the minimum cycle, $O(qn^3)$.

For $100\%$ of the data, $n,q \le 400$.

We still use the algorithm of finding the minimum cycle with Floyd.

If there is no deletion, deleting the queried point splits the simple cycle into a simple path.

However, the solution of the second step instead uses Floyd to obtain the result.

Then the answer requires finding the distance between any two points without passing through the queried point $x$.

How to do it online?

Force it offline, using the offline method to avoid deletion operations.

Arrange the queries in chronological order, and build a segment tree over these queries.

The appearance time of each point covers all queries except the moment when that point is queried; assuming a point is queried $x$ times, then its appearance time can be regarded as $x + 1$ intervals, inserted into the segment tree.

After this is done, traverse the entire segment tree; when passing a node, store a backup of the Floyd array, then add all points inserted on this interval, and when leaving, use the backup array to roll back.

The time complexity of this approach is $O(qn^2\log q)$.

There is also an online approach with better time complexity.

For a query on point $x$, we run a shortest path once with $x$ as the start point, then build the shortest-path tree, and along the way work out which subtree of $x$ each point is in.

Then we can definitely find a non-tree edge such that the two endpoints of this non-tree edge are in different subtrees of the root, so that this non-tree edge $+$ the paths from the two endpoints to the root is the minimum cycle.

Proof:

Obviously the minimum cycle contains a non-tree edge whose two endpoints are in different subtrees of the root.

Assume this edge is $(u,v)$; then the path from $x$ to $u$ on the shortest-path tree is the shortest among all paths from $x$ to $u$, and the path from $x$ to $v$ is also the shortest one, so the cycle $x\to u\to v\to x$ will definitely not be longer than the minimum cycle.

Then we can enumerate all non-tree edges and update the answer.

The complexity of each query is the complexity of running a single-source shortest path once, which is $O(n^2)$.

The total time complexity is $O(qn^2)$.
