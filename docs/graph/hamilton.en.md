## Definition

A path passing through all vertices in a graph once and only once is called a Hamiltonian path.

A cycle passing through all vertices in a graph once and only once is called a Hamiltonian cycle.

A graph that has a Hamiltonian cycle is called a Hamiltonian graph.

A graph that has a Hamiltonian path but not a Hamiltonian cycle is called a semi-Hamiltonian graph.

## Properties

Let $G=\langle V, E\rangle$ be a Hamiltonian graph; then for any non-empty proper subset $V_1$ of $V$, $p(G-V_1) \leq |V_1|$, where $p(x)$ is the number of connected branches of $x$.

Corollary: let $G=\langle V, E\rangle$ be a semi-Hamiltonian graph; then for any non-empty proper subset $V_1$ of $V$, $p(G-V_1) \leq |V_1|+1$, where $p(x)$ is the number of connected branches of $x$.

The complete graph $K_{2k+1} (k \geq 1)$ contains $k$ edge-disjoint Hamiltonian cycles, and these $k$ edge-disjoint Hamiltonian cycles contain all edges in $K_{2k+1}$.

The complete graph $K_{2k} (k \geq 2)$ contains $k-1$ edge-disjoint Hamiltonian cycles, and the graph obtained by deleting these $k-1$ edge-disjoint Hamiltonian cycles from $K_{2k}$ contains $k$ mutually non-adjacent edges.

## Sufficient conditions

Let $G$ be an undirected simple graph of order $n(n \geq 2)$; if for any non-adjacent vertices $v_i, v_j$ in $G$, $d(v_i)+ d(v_j) \geq n - 1$, then a Hamiltonian path exists in $G$.

Corollary 1: let $G$ be an undirected simple graph of order $n(n \geq 3)$; if for any non-adjacent vertices $v_i, v_j$ in $G$, $d(v_i)+ d(v_j) \geq n$, then a Hamiltonian cycle exists in $G$, so $G$ is a Hamiltonian graph.

Corollary 2: let $G$ be an undirected simple graph of order $n(n \geq 3)$; if for any vertex $v_i$ in $G$, $d(v_i) \geq \frac{n}{2}$, then a Hamiltonian cycle exists in $G$, so $G$ is a Hamiltonian graph.

Let $D$ be a tournament graph of order $n(n \geq 2)$; then $D$ has a Hamiltonian path.

If $D$ contains a tournament graph of order $n(n \geq 2)$ as a subgraph, then $D$ has a Hamiltonian path.

A strongly connected tournament graph is a Hamiltonian graph.

If $D$ contains a strongly connected tournament graph of order $n(n \geq 2)$ as a subgraph, then $D$ has a Hamiltonian cycle.
