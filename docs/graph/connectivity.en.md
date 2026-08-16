author: jifbt, Mayuri0v0

## Definitions

For the definitions of the following content, see [graph-theory related concepts](./concept.md):

-   Edge connectivity, edge cut;
-   Vertex connectivity, vertex cut;
-   Clique.

## Properties

### Whitney's inequality

**Whitney's inequality** (1932) gives the relationship among the vertex connectivity $\kappa$, edge connectivity $\lambda$, and minimum degree $\delta$:

$$
\kappa \le \lambda \le \delta
$$

???+ note "Proof"
    Intuitively, if there is an edge cut of size $\lambda$, choosing one endpoint of each edge yields a vertex cut of size $\lambda$, so the first inequality holds.
    
    All edges adjacent to the node with the minimum degree (if there are multiple, choose any one) constitute an edge cut of size $\delta$, so the second inequality also holds.

This inequality cannot be improved; in other words, for each triple satisfying it, a graph satisfying this triple can be found.

???+ note "Construction"
    Connect two cliques of size $\delta + 1$ with $\lambda$ edges, such that the two cliques have $\lambda$ and $\kappa$ distinct nodes respectively connected on these edges.

### Menger's theorem

From the [max-flow min-cut theorem](./flow/min-cut.md) (also known as the Ford–Fulkerson theorem), it can be deduced that the maximum number of disjoint (meaning pairwise having no common edge) paths between two points equals the minimum size of the cut (this corollary is also called **Menger's theorem**—translator's note).

## Computation

The edge weights of all graphs below are $1$.

### Computing edge connectivity with max flow

Enumerate point pairs $(s, t)$, with $s$ as the source and $t$ as the sink, and run a max flow with edge weight $1$. $O(n^2)$ max flows are needed; if using the Edmonds–Karp algorithm, the complexity is $O(|V|^3 |E|^2)$. Using the Dinic algorithm can be better, with complexity $O(|V|^2 |E| \min(|V|^{2/3}, |E|^{1/2}))$.

### Global minimum cut

Using the [Stoer–Wagner algorithm](./stoer-wagner.md), only one source-sink-free minimum cut needs to be run. The complexity is $O(|V||E| + |V|^{2}\log|V|)$, which can generally be approximately regarded as $O(|V|^3)$.

### Vertex connectivity

Still enumerate point pairs; this time split each non-source-sink point $x$ into two points $x_1$ and $x_2$, and connect an edge $(x_1, x_2)$. Replace all edges $(u, v)$ in the original graph with two edges $(u_2, v_1)$ and $(v_2, u_1)$. At this point the max flow equals the size of the minimum vertex cut between $s$ and $t$ (also called the local vertex connectivity). The complexity is the same as computing edge connectivity with max flow.

**This page is translated from the blog posts [Рёберная связность. Свойства и нахождение](http://e-maxx.ru/algo/rib_connectivity), [Вершинная связность. Свойства и нахождение](http://e-maxx.ru/algo/vertex_connectivity) and their English translation [Edge connectivity/Vertex connectivity](https://cp-algorithms.com/graph/edge_vertex_connectivity.html). The Russian version's copyright license is Public Domain + Leave a Link; the English version's copyright license is CC-BY-SA 4.0.**

## Further reading

-   The paper [*Connectivity Algorithms*](https://www.cse.msu.edu/~cse835/Papers/Graph_connectivity_revised.pdf) introduces the progress of connectivity computation algorithms in recent years. Interested readers can browse it on their own.
