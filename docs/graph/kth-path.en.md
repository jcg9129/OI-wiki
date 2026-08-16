Prerequisites: [Dijkstra algorithm](./shortest-path.md#dijkstra-algorithm), [A\* algorithm](../search/astar.md), [persistent mergeable heap](../ds/persistent-heap.md)

## Problem description

Given a directed graph with $n$ nodes and $m$ edges, find the length of the $k$-th shortest path among all distinct paths from $s$ to $t$.

???+ info "\"Path\""
    The "path" referred to in this article allows passing through the same edge or the same node multiple times, so the strict name should be "[walk](./concept.md#path)" rather than "path". The problem discussed in this article is strictly speaking also the **$k$-th shortest walk** ($k$ shortest walk) problem. But, this article still adopts the name "path" according to convention, and calls a non-self-intersecting path a "simple path".

## A\* algorithm

The A\* algorithm is a search algorithm. It sets an evaluation function $f(x)=g(x)+h(x)$ for each current state $x$, where $g(x)$ is the actual cost of reaching the current state from the initial state, and $h(x)$ is the estimated cost of the best path from the current state to the goal state. When searching, each time take out the state $x$ with the best $f(x)$, and expand all its successor states. This value can be maintained with a **priority queue**.

When solving the $k$-shortest-path problem, let $h(x)$ be the shortest-path length from the current node to the end point $t$. This value for each node can be preprocessed by running single-source shortest paths on the reverse graph from node $t$. For each state, two values need to be recorded, i.e. the currently-reached node $x$ and the distance already walked $g(x)$; denote this state as $(x,g(x))$. At the start, add the initial state $(s,0)$ to the priority queue. Each time take out the state with the smallest evaluation function $f(x)=g(x)+h(x)$, enumerate all out-edges of the node $x$ where this state is located, and add the corresponding successor states to the priority queue. When a node is visited for the $k$-th time, the $g(x)$ of the corresponding state is the length of the $k$-th shortest path from the start node $s$ to that node.

This search process can be optimized. Since we only need to find the $k$-th shortest path from the initial node to the goal node, when the number of times an already-taken-out state reaches a node is more than $k$, its successor states need not be expanded. This state will not affect the final answer. This is because during the previous $k$ times of taking out this node, $k$ valid paths reaching this node have already been formed, sufficient to construct the top $k$ shortest paths reaching the goal node.

If the priority-queue-optimized Dijkstra algorithm is used, since at most all edges are added to the priority queue $k$ times, the time complexity of the algorithm is $O(km\log km)$, and the space complexity is $O(km)$. Compared with direct searching, the A\* algorithm prunes with respect to the goal node $t$, but this only improves the constant factor, not the asymptotic complexity. Although the algorithm described in this section does not have excellent complexity, it can find the top $k$ shortest paths from the start point $s$ to each node (in the shortest-path tree rooted at $t$) within the same complexity.

### Implementation

??? example "Template problem [Library Checker - K-Shortest Walk](https://judge.yosupo.jp/problem/k_shortest_walk) reference implementation"
    ```cpp
    --8<-- "docs/graph/code/k-shortest-walk/k-shortest-walk-1.cpp"
    ```

## Persistent mergeable heap approach

The aforementioned algorithm actually finds the $k$ shortest paths reaching all nodes. If we only want to find the $k$ shortest paths reaching a given goal node $t$, we can actually do it faster. This section provides an $O(m\log m+k\log k)$ approach based on a persistent mergeable heap.

### Shortest-path tree and sidetrack edges

The bottleneck of the aforementioned algorithm is that the answer is only updated when reaching the goal node $t$. But, different paths may not differ much. For example, the second-shortest path differs from the shortest path perhaps only in taking a detour around one extra node at one edge, while the rest of the path is the same; the aforementioned algorithm, however, may need to repeatedly search through these same edges to find the second-shortest path. Since only the detour part is crucial, to find the top $k$ shortest paths, we only need to consider the $k$ least-cost detour ways. This leads to the concept of the shortest-path tree.

Run single-source shortest paths on the reverse graph starting from the goal node $t$, record the shortest-path length $h(x)$ from each node $x$ to $t$, and record the first edge $f_x$ passed by the shortest path starting from node $x$; if there are multiple optimal choices, choose any one. All these edges $f_x$ and their endpoints constitute a tree, and the simple path from each node $x$ on the tree to the root node $t$ is a shortest path from $x$ to $t$. This is the **shortest-path tree** $T$.

After finding the shortest-path tree $T$, we can compute how much extra detour each edge not on $T$ takes. For an edge $e=(u,v)\notin T$ with edge weight $w$, we can define a new edge, still pointing from $u$ to $v$, with cost $\Delta(e)=w + h(v) - h(u)$. This article vividly calls these edges with weight $\Delta(e)$ **sidetrack edges**, and the weight $\Delta(e)$ is called the sidetrack cost. If the endpoints of an edge are not all in the shortest-path tree $T$, it will not affect the computation of the $k$ shortest paths reaching node $t$, and they can be directly deleted.

The left side of the figure below is the directed graph $G$, and the right side is its corresponding shortest-path tree $T$ (thick edges) and the corresponding sidetrack edges (thin edges):

![](./images/k-shortest-path-1.svg)

Let the edge set passed by a path from $s$ to $t$ be $P$; remove the intersection of $P$ with $T$ to get $P'$. Then, arranging the edges in $P'$ in order, its two adjacent edges $e_1=(u_1,v_1)$ and $e_2=(u_2,v_2)$ must satisfy

-   Condition $(*)$: the start point $u_2$ of the latter is an ancestor (including itself) of the end point $v_1$ of the former in the shortest-path tree $T$.

This is because in the corresponding original path $P$, $v_1$ and $u_2$ are connected by several tree edges in $T$. Conversely, for an edge set $P'$ satisfying condition $(*)$, there must exist a unique path $P$ in the graph $G$ corresponding to it. This is because the simple path between $v_1$ and $u_2$ on the shortest-path tree $T$ is unique. This shows that any path $P$ in the original graph corresponds one-to-one with a sidetrack-edge sequence $P'$ satisfying condition $(*)$. Moreover, the length of the path $P$ equals the sum of the shortest-path length $h(s)$ and these sidetrack costs:

$$
h(s)+\sum_{e\in P'}\Delta(e).
$$

These discussions show that the task of finding the $k$ shortest paths is transformed into the task of finding the sidetrack-edge sequence $P'$ with the $k$-th smallest cost and satisfying condition $(*)$.

To handle condition $(*)$, rather than searching for ancestors on the shortest-path tree each time we query, it is better to directly push down each node's sidetrack-edge set to the descendant nodes on the shortest-path tree. This is equivalent to building the following graph $G'$:

![](./images/k-shortest-path-2.svg)

On this graph, condition $(*)$ is transformed into requiring the edges in $P'$ to be head-to-tail connected, that is, $P'$ is a path in graph $G'$. The problem is further transformed into finding the $k$-th smallest-length **path reaching any node** starting from $s$ in this graph. Compared with the original $k$-shortest-path problem, here the path is no longer required to end at the goal node $t$.

The transformed problem is easy to solve. Directly start from the start node $s$ and find single-source shortest paths. Each time a node is taken out from the priority queue, it is equivalent to finding a path in graph $G'$, which corresponds to a path in graph $G$ reaching the goal node $t$.

### Persistent mergeable heap optimization

The algorithm idea is already clear. But, naively implementing this algorithm has too high a complexity. Since in graph $G'$, the scale of edges at a single node may be $\Theta(m)$, each time we find single-source shortest paths, we may need to push an edge set of scale $\Theta(m)$ into the priority queue. In fact, there is no need to push all edges into the priority queue: in many cases, among these edges pushed into the queue, only the shortest ones may be popped out of the queue in subsequent computations. That is to say, we can completely push the entire edge set at a single node into the priority queue as a storage unit, and each time we only need to be able to quickly access the shortest edge in the edge set.

This inspires us to use a min-heap to store the edge set at a single node. In the priority queue for finding single-source shortest paths, we only need to store these heaps; their cost is the shortest-path cost corresponding to the heap-top element. Each time the queue front is popped, the heap-top edge needs to be popped from the queue-front heap at the same time. Then, we need to both push the heap after popping the heap top back into the priority queue, and push the heap top corresponding to the sidetrack-edge set at the end point of the heap-top edge into the priority queue.

Using heaps to store edge sets also solves the problem of pushing down edge sets along the shortest-path tree. Because pushing down the edge set is equivalent to needing to merge the current node's edge set into its child nodes, the heap also needs to support the merge operation; while merging into child nodes, we cannot destroy the edge set at the current node, so the heap also needs to support persistence. This is exactly the persistent mergeable heap.

From this, we obtain the complete process of the algorithm:

1.  Starting from the goal node $t$, run single-source shortest paths and find the shortest-path tree.
2.  For each node on the shortest-path tree, construct the corresponding sidetrack-edge set and store it in the persistent mergeable heap.
3.  Along the edges of the shortest-path tree, starting from the goal node $t$, merge the heap at each node into the heap of the child node.
4.  Starting from the start node $s$, push the heap there into the priority queue.
5.  Pop the queue-front heap, record the answer, then push the heap after popping the heap top back into the priority queue, and push the heap at the end point of the heap-top edge into the priority queue.

The persistent mergeable heap is generally implemented with a leftist tree or randomized heap. At this point, the last step can be further optimized. The internal structure of these heaps is a binary tree. After popping the heap top, originally we were going to merge the left and right child nodes and then push the merged heap top into the priority queue; but, in this algorithm, we can not perform the merge operation, and directly push the heaps corresponding to the two child nodes into the priority queue separately. This saves the $O(\log m)$ complexity of a single merge. Since each time the queue-front heap is popped, at most three new heaps are pushed into the priority queue, the size of the priority queue is $O(k)$. In this way, the time complexity of a single query is reduced to $O(\log k)$. The total query complexity is $O(k\log k)$.

Since the complexity of building the shortest-path tree and building the persistent mergeable heap is both $O(m\log m)$, the total time complexity of the algorithm is $O(m\log m+k\log k)$.

### Implementation

??? example "Template problem [Library Checker - K-Shortest Walk](https://judge.yosupo.jp/problem/k_shortest_walk) reference implementation"
    ```cpp
    --8<-- "docs/graph/code/k-shortest-walk/k-shortest-walk-2.cpp"
    ```

## Exercises

-   [「SDOI2010」Magic Pig Academy](https://www.luogu.com.cn/problem/P2483)

## References and notes

-   [\[Tutorial\] k shortest paths and Eppstein's algorithm by meooow - Codeforces](https://codeforces.com/blog/entry/102085)
