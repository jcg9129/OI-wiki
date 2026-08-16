author: Ir1d, sshwy, Xeonacid, partychicken, Anguei, HeRaNO
In OI, to operate on a graph, we first need to learn the ways of storing a graph.

## Conventions

This article assumes by default that the reader has read and understood the basic content in [graph-theory-related concepts](./concept.md); if you encounter difficulties while reading, you can also look it up in [graph-theory-related concepts](./concept.md).

In this article, we use $n$ to refer to the number of points of the graph, $m$ to refer to the number of edges of the graph, and $d^+(u)$ to refer to the out-degree of point $u$, i.e. the number of edges starting from $u$.

## Storing edges directly

### Method

Use an array to store edges, where each element in the array contains the start point and end point of an edge (a weighted graph also contains the edge weight). (Or use multiple arrays to store the start points, end points, and edge weights separately.)

??? note "Reference code"
    === "C++"
        ```cpp
        #include <iostream>
        #include <vector>
        
        using namespace std;
        
        struct Edge {
          int u, v;
        };
        
        int n, m;
        vector<Edge> e;
        vector<bool> vis;
        
        bool find_edge(int u, int v) {
          for (int i = 1; i <= m; ++i) {
            if (e[i].u == u && e[i].v == v) {
              return true;
            }
          }
          return false;
        }
        
        void dfs(int u) {
          if (vis[u]) return;
          vis[u] = true;
          for (int i = 1; i <= m; ++i) {
            if (e[i].u == u) {
              dfs(e[i].v);
            }
          }
        }
        
        int main() {
          cin >> n >> m;
        
          vis.resize(n + 1, false);
          e.resize(m + 1);
        
          for (int i = 1; i <= m; ++i) cin >> e[i].u >> e[i].v;
        
          return 0;
        }
        ```
    
    === "Python"
        ```python
        class Edge:
            def __init__(self, u=0, v=0):
                self.u = u
                self.v = v
        
        
        n, m = map(int, input().split())
        
        e = [Edge() for _ in range(m)]
        vis = [False] * n
        
        for i in range(m):
            e[i].u, e[i].v = map(int, input().split())
        
        
        def find_edge(u, v):
            for i in range(m):
                if e[i].u == u and e[i].v == v:
                    return True
            return False
        
        
        def dfs(u):
            if vis[u]:
                return
            vis[u] = True
            for i in range(m):
                if e[i].u == u:
                    dfs(e[i].v)
        ```

### Complexity

Querying whether a certain edge exists: $O(m)$.

Traversing all out-edges of a point: $O(m)$.

Traversing the entire graph: $O(nm)$.

Space complexity: $O(m)$.

### Applications

Since the traversal efficiency of directly storing edges is low, it is generally not used to traverse graphs.

In the [Kruskal algorithm](./mst.md#kruskal-algorithm), since the edges need to be sorted by edge weight, we need to store edges directly.

In some problems, we need to build the graph multiple times (e.g. build the original graph once and build the reverse graph once); at this time we can either use multiple other data structures to store multiple graphs simultaneously, or store the edges directly, and when we need to rebuild the graph, use the directly-stored edges to build the graph.

## Adjacency matrix

### Method

Use a two-dimensional array `adj` to store edges, where `adj[u][v]` being 1 means an edge from $u$ to $v$ exists, and being 0 means it does not exist. If it is a weighted graph, we can store the edge weight of the edge from $u$ to $v$ in `adj[u][v]`.

??? note "Reference code"
    === "C++"
        ```cpp
        #include <iostream>
        #include <vector>
        
        using namespace std;
        
        int n, m;
        vector<bool> vis;
        vector<vector<bool>> adj;
        
        bool find_edge(int u, int v) { return adj[u][v]; }
        
        void dfs(int u) {
          if (vis[u]) return;
          vis[u] = true;
          for (int v = 1; v <= n; ++v) {
            if (adj[u][v]) {
              dfs(v);
            }
          }
        }
        
        int main() {
          cin >> n >> m;
        
          vis.resize(n + 1);
          adj.resize(n + 1, vector<bool>(n + 1));
        
          for (int i = 1; i <= m; ++i) {
            int u, v;
            cin >> u >> v;
            adj[u][v] = true;
          }
        
          return 0;
        }
        ```
    
    === "Python"
        ```python
        vis = [False] * (n + 1)
        adj = [[False] * (n + 1) for _ in range(n + 1)]
        
        for i in range(1, m + 1):
            u, v = map(lambda x: int(x), input().split())
            adj[u][v] = True
        
        
        def find_edge(u, v):
            return adj[u][v]
        
        
        def dfs(u):
            if vis[u]:
                return
            vis[u] = True
            for v in range(1, n + 1):
                if adj[u][v]:
                    dfs(v)
        ```

### Complexity

Querying whether a certain edge exists: $O(1)$.

Traversing all out-edges of a point: $O(n)$.

Traversing the entire graph: $O(n^2)$.

Space complexity: $O(n^2)$.

### Applications

The adjacency matrix only applies to the case where there are no multiple edges (or multiple edges can be ignored).

Its most notable advantage is that it can query whether an edge exists in $O(1)$.

Since the adjacency matrix is very inefficient on sparse graphs (especially on graphs with many points, where the space is unbearable), the adjacency matrix is generally only used on dense graphs.

## Adjacency list

### Method

Use an array composed of a data structure that supports dynamically adding elements, such as `vector<int> adj[n + 1]`, to store edges, where `adj[u]` stores the relevant information (end point, edge weight, etc.) of all out-edges of point $u$.

??? note "Reference code"
    === "C++"
        ```cpp
        #include <iostream>
        #include <vector>
        
        using namespace std;
        
        int n, m;
        vector<bool> vis;
        vector<vector<int>> adj;
        
        bool find_edge(int u, int v) {
          for (int i = 0; i < adj[u].size(); ++i) {
            if (adj[u][i] == v) {
              return true;
            }
          }
          return false;
        }
        
        void dfs(int u) {
          if (vis[u]) return;
          vis[u] = true;
          for (int i = 0; i < adj[u].size(); ++i) dfs(adj[u][i]);
        }
        
        int main() {
          cin >> n >> m;
        
          vis.resize(n + 1);
          adj.resize(n + 1);
        
          for (int i = 1; i <= m; ++i) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
          }
        
          return 0;
        }
        ```
    
    === "Python"
        ```python
        vis = [False] * (n + 1)
        adj = [[] for _ in range(n + 1)]
        
        for i in range(1, m + 1):
            u, v = map(lambda x: int(x), input().split())
            adj[u].append(v)
        
        
        def find_edge(u, v):
            for i in range(0, len(adj[u])):
                if adj[u][i] == v:
                    return True
            return False
        
        
        def dfs(u):
            if vis[u]:
                return
            vis[u] = True
            for i in range(0, len(adj[u])):
                dfs(adj[u][i])
        ```

### Complexity

Querying whether an edge from $u$ to $v$ exists: $O(d^+(u))$ (if sorting is done in advance, we can use [binary search](../basic/binary.md) to achieve $O(\log(d^+(u)))$).

Traversing all out-edges of point $u$: $O(d^+(u))$.

Traversing the entire graph: $O(n+m)$.

Space complexity: $O(m)$.

### Applications

It is very suitable for storing all kinds of graphs, unless there are special needs (e.g. if we need to quickly query whether an edge exists and the number of points is small, we can use an adjacency matrix).

It is especially suitable for occasions where we need to sort all out-edges of a point.

## Linked forward star

### Method

Essentially it is an adjacency list implemented with a linked list; the core code is as follows:

=== "C++"
    ```cpp
    // the initial values of head[u] and cnt are both -1
    void add(int u, int v) {
      nxt[++cnt] = head[u];  // the successor of the current edge
      head[u] = cnt;         // the first edge of the start point u
      to[cnt] = v;           // the end point of the current edge
    }
    
    // traverse the out-edges of u
    for (int i = head[u]; ~i; i = nxt[i]) {  // ~i means i != -1
      int v = to[i];
    }
    ```

=== "Python"
    ```python
    # the initial values of head[u] and cnt are both -1
    def add(u, v):
        cnt = cnt + 1
        nex[cnt] = head[u]  # the successor of the current edge
        head[u] = cnt  # the first edge of the start point u
        to[cnt] = v  # the end point of the current edge
    
    
    # traverse the out-edges of u
    i = head[u]
    while ~i:  # ~i means i != -1
        v = to[i]
        i = nxt[i]
    ```

??? note "Reference code"
    ```cpp
    #include <iostream>
    #include <vector>
    
    using namespace std;
    
    int n, m;
    vector<bool> vis;
    vector<int> head, nxt, to;
    
    void add(int u, int v) {
      nxt.push_back(head[u]);
      head[u] = to.size();
      to.push_back(v);
    }
    
    bool find_edge(int u, int v) {
      for (int i = head[u]; ~i; i = nxt[i]) {  // ~i means i != -1
        if (to[i] == v) {
          return true;
        }
      }
      return false;
    }
    
    void dfs(int u) {
      if (vis[u]) return;
      vis[u] = true;
      for (int i = head[u]; ~i; i = nxt[i]) dfs(to[i]);
    }
    
    int main() {
      cin >> n >> m;
    
      vis.resize(n + 1, false);
      head.resize(n + 1, -1);
    
      for (int i = 1; i <= m; ++i) {
        int u, v;
        cin >> u >> v;
        add(u, v);
      }
    
      return 0;
    }
    ```

### Complexity

Querying whether an edge from $u$ to $v$ exists: $O(d^+(u))$.

Traversing all out-edges of point $u$: $O(d^+(u))$.

Traversing the entire graph: $O(n+m)$.

Space complexity: $O(m)$.

### Applications

It is very suitable for storing all kinds of graphs, but cannot quickly query whether an edge exists, nor conveniently sort the out-edges of a point.

Its advantage is that the edges are numbered, which is sometimes very useful; and if the initial value of `cnt` is odd, when storing bidirectional edges, `i ^ 1` is the reverse edge of `i` (commonly used in [network flow](./flow.md)).
