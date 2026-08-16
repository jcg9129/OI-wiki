## Definition

Edges directed, no cycles.

The English name is Directed Acyclic Graph, abbreviated DAG.

## Properties

-   A graph that can be [topologically sorted](./topo.md) must be a directed acyclic graph;

    If there is a cycle, then any two nodes on the cycle do not satisfy the condition in any sequence.

-   A directed acyclic graph must be topologically sortable;

    (Induction) Suppose all directed acyclic graphs with no more than $k$ nodes can be topologically sorted; then for one with the number of nodes equal to $k$, just consider the situation after executing the first step of topological sorting.

## Determination

How to determine whether a graph is a directed acyclic graph?

Just check whether it can be [topologically sorted](./topo.md).

Of course there is also another method: one can perform a [DFS](../search/dfs.md) on the graph, and look on the obtained DFS tree to see whether there are non-tree edges (back edges) pointing to ancestors. If there are, then there is a cycle.

## Applications

### DP for the longest (shortest) path

On a general graph, the optimal time complexity for finding the single-source longest (shortest) path is $O(nm)$ ([Bellman–Ford algorithm](./shortest-path.md#bellmanford-algorithm), applicable to graphs with negative weights) or $O(m \log m)$ ([Dijkstra algorithm](./shortest-path.md#dijkstra-algorithm), applicable to graphs without negative weights).

But on a DAG, we can use DP to find the longest (shortest) path, optimizing the time complexity to $O(n+m)$. The state transition equation is $dis_v = min(dis_v, dis_u + w_{u,v})$ or $dis_v = max(dis_v, dis_u + w_{u,v})$.

After topological sorting, traverse each node in topological order, and use the current node to update the subsequent nodes.

```cpp
struct edge {
  int v, w;
};

int n, m;
vector<edge> e[MAXN];
vector<int> L;                               // store the topological sorting result
int max_dis[MAXN], min_dis[MAXN], in[MAXN];  // in stores the in-degree of each node

void toposort() {  // topological sorting
  queue<int> S;
  memset(in, 0, sizeof(in));
  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < e[i].size(); j++) {
      in[e[i][j].v]++;
    }
  }
  for (int i = 1; i <= n; i++)
    if (in[i] == 0) S.push(i);
  while (!S.empty()) {
    int u = S.front();
    S.pop();
    L.push_back(u);
    for (int i = 0; i < e[u].size(); i++) {
      if (--in[e[u][i].v] == 0) {
        S.push(e[u][i].v);
      }
    }
  }
}

void dp(int s) {  // find the single-source longest (shortest) path with s as the start point
  toposort();     // first perform topological sorting
  memset(min_dis, 0x3f, sizeof(min_dis));
  memset(max_dis, 0, sizeof(max_dis));
  min_dis[s] = 0;
  for (int i = 0; i < L.size(); i++) {
    int u = L[i];
    for (int j = 0; j < e[u].size(); j++) {
      min_dis[e[u][j].v] = min(min_dis[e[u][j].v], min_dis[u] + e[u][j].w);
      max_dis[e[u][j].v] = max(max_dis[e[u][j].v], max_dis[u] + e[u][j].w);
    }
  }
}
```

See: [DP on a DAG](../dp/dag.md).
