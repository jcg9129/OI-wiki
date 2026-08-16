author: marscheng1

## Definition

The problem that topological sorting is to solve is how to sort all nodes of a directed acyclic graph.

We can use the example of arranging courses each semester in university to describe this process. For example, among university courses there are: "Program Design", "Algorithmic Languages", "Advanced Mathematics", "Discrete Mathematics", "Compilation Technology", "General Physics", "Data Structures", "Database Systems", etc. According to the course arrangement in the example, when we want to study "Data Structures", we must first learn "Discrete Mathematics"; after finishing this course we obtain the prerequisite for studying "Compilation Technology". Of course, "Compilation Technology" has an even earlier course "Algorithmic Languages". These courses are equivalent to several vertices $u$, and a directed edge $(u,v)$ between vertices is equivalent to the order of studying courses. The academic affairs office arranges these courses so that a timetable is laid out under conditions that conform to the logical relationships, which is the process of topological sorting.

![topo](images/topo-example-1.svg)

But if one day the teacher arranging courses dozes off and says that to study Data Structures, one must first study Operating Systems, while the prerequisite course of Operating Systems is Data Structures, then which one should be studied first (not considering the case of studying simultaneously)? Here, a cycle appears between Data Structures and Operating Systems; obviously the students now cannot figure out what they need to study first, and thus cannot perform topological sorting. Because if there is a cycle in the directed graph, then we cannot perform topological sorting.

Therefore we can say that in a [DAG (directed acyclic graph)](./dag.md), we sort the vertices in the graph in a linear manner, such that for any directed edge $(u,v)$ from vertex $u$ to $v$, $u$ can be in front of $v$.

Also, given a DAG, if there is an edge from $i$ to $j$, then $j$ is considered to depend on $i$. If there is a path from $i$ to $j$ ($i$ can reach $j$), then $j$ is said to indirectly depend on $i$.

The goal of topological sorting is to sort all nodes such that the nodes ranked in front cannot depend on the nodes ranked behind.

## AOV network

In daily life, a large project can be regarded as a collection composed of several sub-projects, and there must be a certain order among these sub-projects, i.e. some sub-projects must be started only after some other sub-projects are completed.

We use a directed graph to represent the ordering relationship among sub-projects; the ordering relationship among sub-projects is a directed edge; this kind of directed graph is called a vertex activity network, i.e. **AOV network (Activity On Vertex Network)**. An AOV network must be a directed acyclic graph, i.e. without loops. Unlike a DAG, the activities of an AOV are all represented on the vertices. (The example figure above is an AOV network.)

In an AOV network, vertices represent activities, and arcs represent priority relationships between activities. Cycles should not appear in an AOV network, so that we can find a vertex sequence such that the predecessor activities of the activity represented by each vertex are all ranked in front of that vertex; such a sequence is called a topological sequence (the topological sequence of an AOV network is not unique), and the process of constructing a topological sequence from an AOV network is called topological sorting. Therefore, topological sorting can also be interpreted as arranging all activities in an AOV network into a sequence such that the predecessor activities of each activity are all ranked in front of that activity (the topological sorting in an AOV network is also not unique).

-   Predecessor activity: the activity at the start point of a directed edge is called the predecessor activity of the end point (only when all predecessors of an activity are completed can this activity proceed).

-   Successor activity: the activity at the end point of a directed edge is called the successor activity of the start point.

The way to detect whether an AOV network has a cycle is to construct a topological sequence and see whether it contains all vertices.

### Steps to construct a topological sequence

1.  Select a point with in-degree zero from the graph.
2.  Output this vertex, and delete this vertex and all its out-edges from the graph.

Repeat the above two steps until all vertices are output and topological sorting is complete, or there is no point with in-degree zero in the graph, at which point it means the graph is a cyclic graph, topological sorting cannot be completed, and it falls into deadlock.

## Critical path and AOE network

Corresponding to the AOV network is the **AOE network (Activity On Edge Network)**, i.e. the network where edges represent activities. An AOE network is a weighted directed acyclic graph, where vertices represent events and arcs represent the durations of activities. Usually, an AOE network can be used to estimate the completion time of a project. An AOE network should be acyclic, and there exists a unique starting vertex (source) with in-degree zero, as well as a unique completion vertex (sink) with out-degree zero.

![topo](images/topo-example-2.svg)

Some activities in an AOE network can be performed in parallel, so the shortest time to complete the whole project is the length of the longest activity path from the start point to the completion point (the path length referred to here is the sum of the durations of the activities on the path, i.e. the sum of the edge weights, not the number of arcs on the path). Because a project needs to complete all activities within the project, the longest activity path is also the critical path, which determines the total time for the project to complete.

### Related basic concepts of AOE networks

-   Activity: in an AOE network, arcs represent activities. The weight of an arc represents the duration of the activity; an activity starts after its predecessor event (i.e. the start point of the arc) is triggered.

-   Event: in an AOE network, vertices represent events; an event is triggered when all its predecessor activities (i.e. the arcs pointing to this vertex) are completed.

-   Earliest occurrence time of event (vertex) $v_i$: the earliest possible occurrence time of this event, denoted $ve(i)$, which determines the earliest occurrence time of the activities starting at this vertex; obviously the earliest occurrence time of the source is 0. Because the occurrence of an event requires all its predecessor activities to be completed, it equals the maximum path length from the initial point to this vertex, written as a recurrence: $ve(i) = \max\{ve(j) + val^j_i ~\vert~ j \in pre_i\}$, where $val^j_i$ denotes the weight of the edge from j to i (i.e. the duration of the activity from j to i), and $pre_i$ denotes the set of all predecessor events of i.

-   Latest occurrence time of event (vertex) $v_i$: the latest tolerable occurrence time of this event without delaying the whole project period, denoted $vl(i)$, which determines the latest occurrence time of all activities ending at this state; it equals the minimum of the latest start times of all successor activities of the event, i.e. $vl(i) = \min\{vl(j) - val^i_j ~\vert~ j \in nxt_i\}$, where $val^i_j$ denotes the weight of the edge from i to j (i.e. the duration of the activity from i to j), and $nxt_i$ denotes the set of all successor events of i.

-   Earliest start time of activity (arc) $(u, v)$: the earliest possible occurrence time of this activity, denoted $e(u,v)$; obviously, it equals the earliest occurrence time of its predecessor event, i.e. $e(u,v)=ve(u)$.

-   Latest start time of activity (arc) $(u, v)$: the latest tolerable time for the activity to start without delaying the whole project period, denoted $l(u,v)$; it equals the latest occurrence time of its successor event − the duration (weight) of this event, i.e. $l(u,v)=vl(v)-val^u_v$, where $val^u_v$ denotes the weight of the edge from u to v (i.e. the duration of the activity from u to v).

-   Critical path: the length of the longest path from the source to the sink in an AOE network.

-   Critical activity: the activity on the critical path, whose earliest start time and latest start time are equal.

### Recursively finding the earliest and latest occurrence times

Find them in topological order; the earliest occurrence time is recursed from front to back, and the latest occurrence time is recursed from back to front; the recurrence formulas are as shown in **Related basic concepts of AOE networks** above.

## Kahn algorithm

### Procedure

In the initial state, the set $S$ contains all points with in-degree $0$, and $L$ is an empty list.

Each time, take a point $u$ from $S$ (can take any) and put it into $L$, then delete all edges $(u, v_1), (u, v_2), (u, v_3) \cdots$ of $u$. For an edge $(u, v)$, if the in-degree of point $v$ becomes $0$ after deleting this edge, then put $v$ into $S$.

Continuously repeat the above process until the set $S$ is empty. Check whether there is any edge in the graph; if there is, then this graph must have a cycle, otherwise return $L$, and the order of the vertices in $L$ is the result of constructing the topological sequence.

First, look at the pseudocode from [Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm)

???+ note "Implementation"
    ```text
    L ← Empty list that will contain the sorted elements
    S ← Set of all nodes with no incoming edges
    while S is not empty do
        remove a node n from S
        insert n into L
        for each node m with an edge e from n to m do
            remove edge e from the graph
            if m has no other incoming edges then
                insert m into S
    if graph has edges then
        return error (graph has at least one cycle)
    else
        return L (a topologically sorted order)
    ```

The core of the code is to maintain a set of vertices with in-degree 0.

You can refer to this figure

![topo](images/topo-example.svg)

The result of sorting it is: 2 -> 8 -> 0 -> 3 -> 7 -> 1 -> 5 -> 6 -> 9 -> 4 -> 11 -> 10 -> 12

### Time complexity

Assume this graph $G = (V, E)$ needs to traverse the entire graph and check each edge when initializing the set $S$ with in-degree $0$, so it has a complexity of $O(E+V)$. Then operating on this set obviously also needs $O(E+V)$ time complexity.

Therefore the total time complexity is $O(E+V)$.

### Implementation

=== "C++"
    ```cpp
    int n, m;
    vector<int> G[MAXN];
    int in[MAXN];  // store the in-degree of each node
    
    bool toposort() {
      vector<int> L;
      queue<int> S;
      for (int i = 1; i <= n; i++)
        if (in[i] == 0) S.push(i);
      while (!S.empty()) {
        int u = S.front();
        S.pop();
        L.push_back(u);
        for (auto v : G[u]) {
          if (--in[v] == 0) {
            S.push(v);
          }
        }
      }
      if (L.size() == n) {
        for (auto i : L) cout << i << ' ';
        return true;
      }
      return false;
    }
    ```

=== "Python"
    ```python
    from collections import defaultdict, deque
    
    
    def topo_sort(graph):
        lst = []
        in_degree = defaultdict(int)
        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1
    
        s = deque([u for u in graph if in_degree[u] == 0])
        while s:
            u = s.popleft()
            lst.append(u)
            for v in graph.get(u, []):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    s.append(v)
    
        return None if any(in_degree.values()) else lst
    ```

## DFS algorithm

### Implementation

=== "C++"
    ```cpp
    using Graph = vector<vector<int>>;  // adjacency list
    
    struct TopoSort {
      enum class Status : uint8_t { to_visit, visiting, visited };
    
      const Graph& graph;
      const int n;
      vector<Status> status;
      vector<int> order;
      vector<int>::reverse_iterator it;
    
      TopoSort(const Graph& graph)
          : graph(graph),
            n(graph.size()),
            status(n, Status::to_visit),
            order(n),
            it(order.rbegin()) {}
    
      bool sort() {
        for (int i = 0; i < n; ++i) {
          if (status[i] == Status::to_visit && !dfs(i)) return false;
        }
        return true;
      }
    
      bool dfs(const int u) {
        status[u] = Status::visiting;
        for (const int v : graph[u]) {
          if (status[v] == Status::visiting) return false;
          if (status[v] == Status::to_visit && !dfs(v)) return false;
        }
        status[u] = Status::visited;
        *it++ = u;
        return true;
      }
    };
    ```

=== "Python"
    ```python
    from enum import Enum, auto
    
    
    class Status(Enum):
        to_visit = auto()
        visiting = auto()
        visited = auto()
    
    
    def topo_sort(graph: list[list[int]]) -> list[int] | None:
        n = len(graph)
        status = [Status.to_visit] * n
        order = []
    
        def dfs(u: int) -> bool:
            status[u] = Status.visiting
            for v in graph[u]:
                if status[v] == Status.visiting:
                    return False
                if status[v] == Status.to_visit and not dfs(v):
                    return False
            status[u] = Status.visited
            order.append(u)
            return True
    
        for i in range(n):
            if status[i] == Status.to_visit and not dfs(i):
                return None
    
        return order[::-1]
    ```

Time complexity: $O(E+V)$ Space complexity: $O(V)$

### Justification proof

Consider a graph; after deleting some node with in-degree $0$, if the new graph can be topologically sorted, then the original graph can definitely also be. Conversely, if the original graph can be topologically sorted, then after deleting it can also be.

### Applications

Topological sorting can determine whether there is a cycle in the graph, and can also be used to determine whether the graph is a chain. Topological sorting can be used to find the critical path in an AOE network, estimating the shortest time for the project to complete.

### Finding the lexicographically largest/smallest topological sort

Just replace the queue in the Kahn algorithm with a priority queue implemented by a max-heap/min-heap; at this time the total time complexity is $O(E+V \log{V})$.

## Exercises

[CF 1385E](https://codeforces.com/problemset/problem/1385/E): needs to be constructed through topological sorting.

[Luogu P1347](https://www.luogu.com.cn/problem/P1347): topological sorting template.

## References

1.  Discrete Mathematics and Its Applications. ISBN:9787111555391
2.  [Topological sorting - Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)
3.  [Data structures lecture 9 (Graphs: topological sorting, critical path, shortest path) - Zhihu column](https://zhuanlan.zhihu.com/p/164751109)
