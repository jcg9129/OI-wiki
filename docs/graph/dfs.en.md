author: Ir1d, greyqz, yjl9903, partychicken, ChungZH, qq1010903229, Marcythm, Acfboy, shenshuaijie, Craneplayz

## Introduction

The full name of DFS is [Depth First Search](https://en.wikipedia.org/wiki/Depth-first_search); it is an algorithm for traversing or searching a tree or graph. So-called depth-first means that each time it tries to walk toward a deeper node.

When explaining this algorithm, it is often juxtaposed with BFS, but besides both being able to traverse the connected components of a graph, their uses are completely different, and there are few cases where the two algorithms can be used interchangeably.

DFS is often used to refer to a search implemented with a recursive function, but the two are actually not the same. For the idea of this kind of search, please refer to [DFS (search)](../search/dfs.md).

## Process

The most notable characteristic of DFS is its **recursive call of itself**. At the same time, similar to BFS, DFS marks the points it has visited, and skips the marked points when traversing the graph, to ensure that **each point is visited only once**. A function conforming to the above two rules is a DFS in the broad sense.

Specifically, the rough structure of DFS is as follows:

    DFS(v) // v can be a vertex in the graph, or an abstract concept, such as a dp state, etc.
      mark v as visited
      for u in v's adjacent nodes
        if u has not been marked as visited then
          DFS(u)
        end
      end
    end

The above code only contains the main structure required for DFS. Actual DFS will add some code on the basis of the above code, utilizing the properties of DFS to perform other operations.

## Properties

The usual time complexity of this algorithm is $O(n+m)$, and the space complexity is $O(n)$, where $n$ denotes the number of points and $m$ denotes the number of edges. Note that the space complexity includes the stack space, and the space complexity of the stack space is $O(n)$. This time complexity can only be achieved under the condition of traversing an edge in average $O(1)$, for example storing the graph with a forward star or adjacency list; if using an adjacency matrix, this complexity may not necessarily be achieved.

> Note: currently most algorithm competitions (including NOIP, most provincial selections, and various events held by CCF) support **unlimited stack space**, i.e.: the stack space is not limited separately, but the total memory space is still limited by the problem statement. But most operating systems impose additional limits on the stack space, so when debugging locally you need some ways to cancel the stack-space limit.
>
> -   On Windows, the usual method is to add `-Wl,--stack=1000000000` in the **compile options**, meaning setting the stack-space limit to 1000000000 bytes.
> -   On Linux, the usual method is to execute `ulimit -s unlimited` **in the terminal** before running the program, meaning unlimited stack space. Each terminal only needs to execute it once, and it is effective for every subsequent program run.

## Implementation

### Stack implementation

DFS can be implemented using a [stack](../ds/stack.md) as the temporary-storage container for nodes during traversal; this forms a high correspondence with BFS implemented using a [queue](../ds/queue.md).

=== "C++"
    ```cpp
    vector<vector<int>> adj;  // adjacency list
    vector<bool> vis;         // record whether a node has been traversed
    
    void dfs(int s) {
      stack<int> st;
      st.push(s);
      vis[s] = true;
    
      while (!st.empty()) {
        int u = st.top();
        st.pop();
    
        for (int v : adj[u]) {
          if (!vis[v]) {
            vis[v] = true;  // ensure there are no duplicate elements in the stack
            st.push(v);
          }
        }
      }
    }
    ```

=== "Python"
    ```python
    # adj : List[List[int]] adjacency list
    # vis : List[bool] record whether a node has been traversed
    
    
    def dfs(s: int) -> None:
        stack = [s]  # use a list to simulate a stack, add the start point to the stack
        vis[s] = True  # the start point is traversed
    
        while stack:  # continue while the stack is non-empty
            u = (
                stack.pop()
            )  # take and discard the last element (the element at the top of the stack), can be understood as walking to element u
    
            for v in adj[u]:  # for each element v adjacent to u
                if not vis[v]:  # if v has not been walked before
                    vis[v] = True  # ensure there are no duplicate elements in the stack
                    stack.append(v)  # add v to the stack
    ```

### Recursive implementation

The evaluation of a function during recursive calls is like the order of adding and removing elements to/from a stack, so the virtual address occupied by function calls is called the function call stack (Call Stack); DFS can be implemented recursively.

Taking the [adjacency list](./save.md#adjacency-list) as the graph storage method:

=== "C++"
    ```cpp
    vector<vector<int>> adj;  // adjacency list
    vector<bool> vis;         // record whether a node has been traversed
    
    void dfs(const int u) {
      vis[u] = true;
      for (int v : adj[u])
        if (!vis[v]) dfs(v)
    }
    ```

=== "Python"
    ```python
    # adj : List[List[int]] adjacency list
    # vis : List[bool] record whether a node has been traversed
    
    
    def dfs(u: int) -> None:
        vis[u] = True
        for v in adj[u]:
            if not vis[v]:
                dfs(v)
    ```

Taking the [chained forward star](./save.md#linked-forward-star) as an example:

=== "C++"
    ```cpp
    void dfs(int u) {
      vis[u] = 1;
      for (int i = head[u]; i; i = e[i].x) {
        if (!vis[e[i].t]) {
          dfs(v);
        }
      }
    }
    ```

=== "Java"
    ```Java
    public void dfs(int u) {
        vis[u] = true;
        for (int i = head[u]; i != 0; i = e[i].x) {
            if (!vis[e[i].t]) {
                dfs(v);
            }
        }
    }
    ```

=== "Python"
    ```python
    def dfs(u):
        vis[u] = True
        i = head[u]
        while i:
            if vis[e[i].t] == False:
                dfs(v)
            i = e[i].x
    ```

### DFS sequence

The DFS sequence refers to the sequence of node numbers visited during the DFS call process.

We find that each subtree corresponds to a continuous segment (an interval) in the DFS sequence.

### Bracket sequence

When DFS enters a certain node, record a left bracket `(`, and when exiting a certain node, record a right bracket `)`.

Each node appears twice. The depths of two adjacent nodes differ by 1.

### DFS on a general graph

For a non-connected graph, only the connected component where the start point is located can be visited.

For a connected graph, the DFS sequence is usually not unique.

Note: the DFS sequence of a tree is also not unique.

During the DFS process, by recording from which point each node is visited, one can establish a tree structure, called the DFS tree. The DFS tree is a spanning tree of the original graph.

The [DFS tree](./scc.md#dfs-spanning-tree) has many properties, for example it can be used to find [strongly connected components](./scc.md).
