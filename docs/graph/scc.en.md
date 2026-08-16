## Introduction

Before reading the following content, please be sure to understand the basic part of [graph-theory-related concepts](./concept.md).

The definition of strongly connected is: a directed graph G being strongly connected means that any two nodes in G are connected.

The definition of a strongly connected component (SCC) is: a maximal strongly connected subgraph.

What we want to introduce here is how to find strongly connected components.

## Tarjan algorithm

### Introduction

Robert E. Tarjan (1948\~), born in Pomona, California, USA, is a computer scientist.

Tarjan invented many algorithms and data structures. Quite a few of the algorithms he invented are named after him, so much so that sometimes people confuse several different algorithms. For example, the Tarjan algorithm for finding various connected components, and the Tarjan algorithm for finding LCA (Lowest Common Ancestor). The disjoint set union, Splay, and Toptree were also invented by Tarjan.

What we want to introduce here is the Tarjan algorithm for finding strongly connected components in a directed graph.

### DFS spanning tree

Before introducing this algorithm, let us first understand the **DFS spanning tree**, taking the following directed graph as an example:

![DFS spanning tree](./images/dfs-tree.svg)

When running the DFS algorithm on a directed graph $G$, since edges have directionality, starting from a single node may not be able to access all nodes in the graph. Therefore, we need to traverse the entire vertex set: for each not-yet-visited node, we restart a DFS. In each DFS process starting from and completed at some starting node, the tree edges (see below) it passes through form a tree, called a **DFS spanning tree**. When all nodes have been visited, the entirety of the obtained DFS spanning trees forms the **DFS spanning forest** of this directed graph.

It should be noted that the specific structure of the spanning tree (and the spanning forest), as well as the edge classification below, all depend on the choice of the starting node of the DFS and the visiting order of adjacent points.

The edges of a directed graph $G$ can be divided into four classes:

1.  Tree edge: represented by black edges in the schematic diagram; a tree edge is formed each time the search finds a not-yet-visited node. All adjacent tree edges form the DFS spanning tree.
2.  Back edge: also called a return edge, represented by red edges in the schematic diagram (i.e. $7 \rightarrow 1$); it refers to a non-tree edge pointing from some node to its ancestor node during the search process.
3.  Forward edge: represented by green edges in the schematic diagram (i.e. $3 \rightarrow 6$); it refers to a non-tree edge pointing from some node to a descendant node in its subtree during the search process.
4.  Cross edge: represented by blue edges in the schematic diagram (i.e. $9 \rightarrow 7$); it refers to an edge pointing from some node to a non-ancestor, non-descendant and already-visited node during the search process, i.e. an edge that does not belong to the above three classes.

We consider the relationship between the DFS spanning tree and strongly connected components.

If node $u$ is the first node of some strongly connected component encountered in the search tree, then the remaining nodes of this strongly connected component are definitely in the subtree rooted at $u$ in the search tree. Node $u$ is called the root of this strongly connected component.

Proof by contradiction: Assume there is a node $v$ in this strongly connected component but not in the subtree rooted at $u$; then there must be an edge leaving the subtree on the path from $u$ to $v$. But such an edge can only be a cross edge or a back edge, and yet both of these edges require the pointed-to node to have already been visited, which contradicts $v$ not being in the subtree rooted at $u$. Proved.

### Tarjan algorithm for finding strongly connected components

The Tarjan algorithm is based on performing a [depth-first search](./dfs.md) on the graph. We regard each connected component as a subtree in the search tree; during the search process, we maintain a stack, and each time push the not-yet-processed nodes in the search tree onto the stack.

In the Tarjan algorithm, the following variables are maintained for each node $u$:

1.  $\textit{dfn}_u$: the order in which node $u$ is searched during the depth-first search traversal.
2.  $\textit{low}_u$: the earliest node already in the stack that can be traced back to in the subtree of $u$. Let the subtree rooted at $u$ be $\textit{Subtree}_u$. $\textit{low}_u$ is defined as the minimum $\textit{dfn}$ of the following nodes: nodes in $\textit{Subtree}_u$; nodes reachable from $\textit{Subtree}_u$ through one edge not on the search tree.

The dfn of the nodes inside a node's subtree are all greater than the dfn of that node.

On a path starting from the root, the dfn is strictly increasing and the low is strictly non-decreasing.

Search all nodes in the graph in the order of the depth-first search algorithm, maintain the `dfn` and `low` variables of each node, and push the searched nodes onto the stack. Whenever a strongly connected element is found, pop elements from the stack according to the number of nodes contained in this element. During the search process, for node $u$ and a node $v$ adjacent to it ($v$ is not the parent node of $u$), consider 3 cases:

1.  $v$ has not been visited: continue the depth search on $v$. During the backtracking process, update $\textit{low}_u$ with $\textit{low}_v$. Because there is a direct path from $u$ to $v$, the node already in the stack that $v$ can trace back to, $u$ can definitely also trace back to.
2.  $v$ has been visited and is already in the stack: according to the definition of the low value, update $\textit{low}_u$ with $\textit{dfn}_v$.
3.  $v$ has been visited and is no longer in the stack: this means $v$ has been fully searched, and the connected component it is in has been processed, so no operation needs to be done on it.

Writing the above algorithm as pseudocode:

???+ note "Implementation"
    ```text
    TARJAN_SEARCH(int u)
        vis[u]=true
        low[u]=dfn[u]=++dfncnt
        push u to the stack
        for each (u,v) then do
            if v hasn't been searched then
                TARJAN_SEARCH(v) // search
                low[u]=min(low[u],low[v]) // backtrack
            else if v has been in the stack then
                low[u]=min(low[u],dfn[v])
    ```

For a connected component graph, we can easily think that in this connected graph there is one and only one $u$ such that $\textit{dfn}_u=\textit{low}_u$. This node must be the first node visited in this connected component during the depth traversal, because its dfn and low values are the smallest and will not be affected by other nodes in this connected component.

Therefore, during the backtracking process, we determine whether $\textit{dfn}_u=\textit{low}_u$ holds; if it holds, then $u$ and the nodes above it in the stack form an SCC.

### Implementation

=== "C++"
    ```cpp
    int dfn[N], low[N], dfncnt, s[N], in_stack[N], tp;
    int scc[N], sc;  // the number of the SCC that node i is in
    int sz[N];       // the size of strongly connected component i
    
    void tarjan(int u) {
      low[u] = dfn[u] = ++dfncnt, s[++tp] = u, in_stack[u] = 1;
      for (int i = h[u]; i; i = e[i].nex) {
        const int &v = e[i].t;
        if (!dfn[v]) {
          tarjan(v);
          low[u] = min(low[u], low[v]);
        } else if (in_stack[v]) {
          low[u] = min(low[u], dfn[v]);
        }
      }
      if (dfn[u] == low[u]) {
        ++sc;
        do {
          scc[s[tp]] = sc;
          sz[sc]++;
          in_stack[s[tp]] = 0;
        } while (s[tp--] != u);
      }
    }
    ```

=== "Python"
    ```python
    dfn = [0] * N
    low = [0] * N
    dfncnt = 0
    s = [0] * N
    in_stack = [0] * N
    tp = 0
    scc = [0] * N
    sc = 0  # the number of the SCC that node i is in
    sz = [0] * N  # the size of strongly connected component i
    
    
    def tarjan(u):
        low[u] = dfn[u] = dfncnt
        s[tp] = u
        in_stack[u] = 1
        dfncnt = dfncnt + 1
        tp = tp + 1
        i = h[u]
        while i:
            v = e[i].t
            if dfn[v] == False:
                tarjan(v)
                low[u] = min(low[u], low[v])
            elif in_stack[v]:
                low[u] = min(low[u], dfn[v])
            i = e[i].nex
        if dfn[u] == low[u]:
            sc = sc + 1
            while s[tp] != u:
                scc[s[tp]] = sc
                sz[sc] = sz[sc] + 1
                in_stack[s[tp]] = 0
                tp = tp - 1
            scc[s[tp]] = sc
            sz[sc] = sz[sc] + 1
            in_stack[s[tp]] = 0
            tp = tp - 1
    ```

The time complexity is $O(n + m)$.

### Relationship between component labels and topological order

During the processing of the Tarjan algorithm, it actually discovers strongly connected components in a certain **reverse topological order**, because during the depth-first search the algorithm first finishes visiting those nodes with no out-edges, which is the reverse of the topological sorting process.

If we contract all strongly connected components in the graph into single nodes, then performing topological sorting in the DAG formed by these contracted nodes, the obtained order will be the reverse of the label order of the strongly connected components given by the Tarjan algorithm.

Therefore, we can say that in the contracted DAG, **the label order of the strongly connected components (after contraction) is the reverse of their topological order**. But note that this statement only holds when considering the dependency relationships between strongly connected components (i.e. the directed edges from one strongly connected component to another). Because the nodes inside a single strongly connected component have cycles, the interior does not satisfy the definition of topological order.

## Kosaraju algorithm

### Introduction

The Kosaraju algorithm was first proposed in 1978 by S. Rao Kosaraju in an unpublished paper, but Micha Sharir first published it.

### Procedure

This algorithm relies on two simple DFS to implement:

The first DFS selects any vertex as the start point, traverses all not-yet-visited vertices, and numbers the vertices before backtracking, i.e. a postorder traversal.

The second DFS, for the reversed graph, starts DFS with the vertex with the largest label as the start point. The set of vertices traversed this way is a strongly connected component. For all not-yet-visited nodes, select the one with the largest label, and repeat the above process.

After the two DFS end, the strongly connected components are found. The time complexity of the Kosaraju algorithm is $O(n+m)$.

### Implementation

=== "C++"
    ```cpp
    // g is the original graph, g2 is the reverse graph
    
    void dfs1(int u) {
      vis[u] = true;
      for (int v : g[u])
        if (!vis[v]) dfs1(v);
      s.push_back(u);
    }
    
    void dfs2(int u) {
      color[u] = sccCnt;
      for (int v : g2[u])
        if (!color[v]) dfs2(v);
    }
    
    void kosaraju() {
      sccCnt = 0;
      for (int i = 1; i <= n; ++i)
        if (!vis[i]) dfs1(i);
      for (int i = n; i >= 1; --i)
        if (!color[s[i]]) {
          ++sccCnt;
          dfs2(s[i]);
        }
    }
    ```

=== "Python"
    ```python
    def dfs1(u):
        vis[u] = True
        for v in g[u]:
            if vis[v] == False:
                dfs1(v)
        s.append(u)
    
    
    def dfs2(u):
        color[u] = sccCnt
        for v in g2[u]:
            if color[v] == False:
                dfs2(v)
    
    
    def kosaraju(u):
        sccCnt = 0
        for i in range(1, n + 1):
            if vis[i] == False:
                dfs1(i)
        for i in range(n, 0, -1):
            if color[s[i]] == False:
                sccCnt = sccCnt + 1
                dfs2(s[i])
    ```

## Garbow algorithm

### Procedure

The Garbow algorithm is another implementation of the Tarjan algorithm. The Tarjan algorithm uses dfn and low to compute the root of a strongly connected component, while Garbow maintains a node stack, and uses a second stack to determine when to pop nodes belonging to the same strongly connected component from the first stack. During the DFS process starting from node $w$, when a path shows that this group of nodes all belong to the same strongly connected component, as long as the access time of the stack-top node is greater than the access time of the root node $w$, this node is popped from the second stack, so that finally only the root node $w$ is left. In this process, each popped node belongs to the same strongly connected component.

When backtracking to some node $w$, if this node is at the top of the second stack, it means this node is the starting node of a strongly connected component; those nodes searched after this node all belong to the same strongly connected component, so those nodes are popped from the first stack, forming a strongly connected component.

### Implementation

=== "C++"
    ```cpp
    int garbow(int u) {
      stack1[++p1] = u;
      stack2[++p2] = u;
      low[u] = ++dfs_clock;
      for (int i = head[u]; i; i = e[i].next) {
        int v = e[i].to;
        if (!low[v])
          garbow(v);
        else if (!sccno[v])
          while (low[stack2[p2]] > low[v]) p2--;
      }
      if (stack2[p2] == u) {
        p2--;
        scc_cnt++;
        do {
          sccno[stack1[p1]] = scc_cnt;
          // all_scc[scc_cnt] ++;
        } while (stack1[p1--] != u);
      }
      return 0;
    }
    
    void find_scc(int n) {
      dfs_clock = scc_cnt = 0;
      p1 = p2 = 0;
      memset(sccno, 0, sizeof(sccno));
      memset(low, 0, sizeof(low));
      for (int i = 1; i <= n; i++)
        if (!low[i]) garbow(i);
    }
    ```

=== "Python"
    ```python
    def garbow(u):
        stack1[p1] = u
        stack2[p2] = u
        p1 = p1 + 1
        p2 = p2 + 1
        low[u] = dfs_clock
        dfs_clock = dfs_clock + 1
        i = head[u]
        while i:
            v = e[i].to
            if low[v] == False:
                garbow(v)
            elif sccno[v] == False:
                while low[stack2[p2]] > low[v]:
                    p2 = p2 - 1
        if stack2[p2] == u:
            p2 = p2 - 1
            scc_cnt = scc_cnt + 1
            while stack1[p1] != u:
                p1 = p1 - 1
                sccno[stack1[p1]] = scc_cnt
    
    
    def find_scc(n):
        dfs_clock = scc_cnt = 0
        p1 = p2 = 0
        sccno = []
        low = []
        for i in range(1, n + 1):
            if low[i] == False:
                garbow(i)
    ```

## Applications

We can contract each strongly connected component of a graph into a single point.

Then this graph becomes a DAG, on which we can perform topological sorting and many other operations.

To give a simple example, find a path that can pass through repeated nodes, requiring the number of distinct nodes passed to be maximized.

## Exercises

[USACO Fall/HAOI 2006 Popular cows](https://loj.ac/problem/10091)

[POJ1236 Network of Schools](http://poj.org/problem?id=1236)
