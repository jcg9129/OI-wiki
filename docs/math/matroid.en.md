## Introduction

A **matroid** is an abstract algebraic structure proposed by Hassler Whitney in 1935, aimed at unifying and generalizing the concept of independence, such as linear independence in linear algebra and acyclicity in graph theory.

Matroids provide a powerful theoretical tool for handling optimization problems related to independence, and are widely applied in fields such as combinatorics, graph theory, and algorithm design, playing an especially important role in providing mathematical theoretical support for optimization methods such as greedy algorithms.

## Definition

### Matroid

A **matroid** can be represented as $M = (E, \mathcal{I})$, where:

-   $E$ is a finite set, called the **ground set**.
-   $\mathcal{I}$ is a family of subsets of $E$, called the **family of independent sets**, and the sets in it are called **independent sets**. It has the following three properties:

    -   **Non-emptiness**: the empty set is independent, i.e. $\emptyset \in \mathcal{I}$.

    -   **Heredity**: any subset of an independent set is also an independent set. If $I \in \mathcal{I}$, then for any $I' \subseteq I$, $I' \in \mathcal{I}$.

    -   **Exchange (augmentation) property**: if $I, J \in \mathcal{I}$ and $|I| < |J|$, then there exists $j \in J \setminus I$ such that $I \cup \{j\} \in \mathcal{I}$.

If a structure of the form $(E, \mathcal{I})$ satisfies the above three properties, then it is called a matroid.

### Basis

A **basis** is a maximal independent set in a matroid, i.e. an independent set to which no element can be added while maintaining independence. The set of all bases is called the **family of bases**, denoted $\mathcal{B}$.

**Properties**:

1.  **Equicardinality**: all bases have the same size, called the **rank** of the matroid.

2.  **Augmentation property**: any independent set can be extended into a basis by adding elements from a basis.

### Circuit

A **circuit** is a minimal dependent set in a matroid, i.e. one all of whose proper subsets are independent but which is not itself an independent set; there is no containment relation between any two circuits.

### Rank

The **rank function** $r: 2^E \rightarrow \mathbb{Z}_{\geq 0}$ maps subsets of the ground set $E$ to non-negative integers. For any $S \subseteq E$, $r(S)$ is defined as the size of the largest independent set in $S$, i.e.

$$
r(S) = \max \{ |I| \mid I \subseteq S \wedge I \in \mathcal{I} \}.
$$

**Properties**:

1.  **Non-negativity**: for any $S \subseteq E$, $0 \leq r(S) \leq |S|$.

2.  **Monotonicity**: if $A \subseteq B \subseteq E$, then $r(A) \leq r(B)$.

3.  **Submodularity**: for any $A, B \subseteq E$, $r(A \cup B) + r(A \cap B) \leq r(A) + r(B)$.

## Typical examples

### 1. Uniform matroid

**Definition**: Given a ground set $E$ and a non-negative integer $k$, the family of independent sets of the uniform matroid $U_{k,E}$ is all subsets of size not exceeding $k$, represented as:

$$
\mathcal{I} = \{ I \subseteq E \mid |I| \leq k \}.
$$

-   **Bases**: all subsets of size $k$.

-   **Circuits**: all subsets of size $k + 1$.

-   **Rank**: $r(E) = \min(k, |E|)$, i.e. an independent set can have at most $k$ elements.

### 2. Graphical matroid

**Definition**: Given an undirected graph $G = (V, E)$, the ground set of the graphical matroid $M(G)$ is the edge set $E$, and its family of independent sets is all edge sets containing no cycle, i.e. all forests.

-   **Bases**: spanning trees of the graph (in the case of a connected graph). A spanning tree is a maximal independent set to which no edge can be added without forming a cycle.

-   **Circuits**: simple cycles in the graph; removing any edge of a cycle, the remaining part is an independent set.

-   **Rank**: $r(E) = |V| - c$, where $c$ is the number of connected components of the graph. For a connected undirected graph, its rank equals the number of vertices minus one, i.e. $|V| - 1$.

### 3. Linear matroid

**Definition**: The linear matroid is based on a vector space. Given a vector space $V$, the ground set $E$ is a finite group of vectors in $V$, and its family of independent sets is all linearly independent subsets of vectors in $E$.

-   **Bases**: maximal linearly independent sets of vectors, whose size equals the dimension of the vector space.

-   **Circuits**: minimal sets of linearly dependent vectors, any proper subset of which is independent while itself is linearly dependent.

-   **Rank**: the rank of the linear matroid $r(E) = \dim(V)$, i.e. the dimension of the vector space. The size of an independent set cannot exceed the dimension of the vector space.

### 4. Partition matroid

**Definition**: Divide the ground set $E$ into disjoint subsets $E_1, E_2, \dots, E_m$, and assign to each subset $E_i$ a non-negative integer $k_i$. The family of independent sets of the partition matroid consists of subsets satisfying that the number of elements selected in each part does not exceed $k_i$, represented as:

$$
\mathcal{I} = \left\{ I \subseteq E \mid \forall i,\, |I \cap E_i| \leq k_i \right\}.
$$

-   **Bases**: independent sets satisfying $|I \cap E_i| = k_i$ are bases of the partition matroid. Each basis selects exactly $k_i$ elements in each subset.

-   **Circuits**: a circuit of the partition matroid is a minimal dependent set, i.e. one containing at least one subset whose number of elements exceeds $k_i$.

-   **Rank**: the rank of the partition matroid is $r(E) = \sum_{i=1}^m k_i$, i.e. the size of the maximum independent set equals the sum of the maximum number of elements allowed to be selected in each subset.

### 5. Colored matroid

**Definition**: A colored matroid is a special form of partition matroid in which each element is assigned a color. Given a ground set $E$ and a color set $C$, each element $e \in E$ is associated with some color $c \in C$. An independent set of a colored matroid needs to satisfy not only the independence condition of an ordinary matroid, but also the color-specified restrictions, for example that at most a certain number of elements of the same color can be selected in an independent set.

-   **Bases**: a basis of a colored matroid is a maximal independent set meeting the color restrictions and independence condition.

-   **Circuits**: a circuit is a minimal dependent set, containing at least one set of elements violating independence or a color restriction.

-   **Rank**: the rank of a colored matroid is the size of the maximum independent set under the color restrictions. It depends on both the structure of the matroid and the specific stipulations of the color restrictions.

## Constructions and operations

### Dual

Given a matroid $M = (E, \mathcal{I})$, its **dual matroid** $M^* = (E, \mathcal{I}^*)$ is defined as:

$$
\mathcal{I}^* = \{ I^* \subseteq E \mid \exists B \in \mathcal{I}, |B| = r(E), B \subseteq E \setminus I^* \}.
$$

**Properties**:

-   **Bases**: a basis of the dual matroid $M^*$ is the complement in the ground set $E$ of a basis of $M$. In other words, if $B$ is a basis of $M$, then $E \setminus B$ is a basis of $M^*$.

-   **Rank function**: the rank function of the dual matroid is $r^*(S) = |S| - r(E) + r(E \setminus S)$, where $S$ is a subset of $E$. This means the rank of the dual matroid can be computed from the size of the ground set, the rank of the original matroid, and the rank after removing $S$ from the ground set.

-   **Involutivity**: the dual of the dual matroid is still the original matroid, i.e. $(M^*)^* = M$.

**Example**:

For an undirected graph $G = (V, E)$, the dual $M(G)^*$ of the graphical matroid $M(G)$ is the matroid consisting of the cut sets of the graph. The bases of the graphical matroid $M(G)$ are the spanning trees of the graph, while the bases of its dual $M(G)^*$ are the complements of these spanning trees, and the circuits of the dual $M(G)^*$ are the minimum cut sets of the graph, i.e. the minimum edge sets that divide the graph into two disconnected parts.

For example, consider a simple triangle graph $G$ with edge set $E = \{e_1, e_2, e_3\}$. The bases of the graphical matroid $M(G)$ are the sets of two edges (such as $\{e_1, e_2\}$), while the bases of the dual matroid $M(G)^*$ are the sets of a single edge (such as $\{e_3\}$), and the circuits of $M(G)^*$ are the sets of two edges (i.e. the minimum cut sets, such as $\{e_2,e_3\}$), because removing one of these edges divides the graph into two connected components.

### Deletion and contraction

**Deletion**:

For $A \subseteq E$, deleting $A$ from the matroid $M$ gives a new matroid $M \setminus A$, whose family of independent sets $\mathcal{I}'$ is defined as:

$$
\mathcal{I}' = \{ I \subseteq E \setminus A \mid I \in \mathcal{I} \}.
$$

As one can see, the deletion operation removes some elements from the matroid and keeps the independent sets formed by the remaining elements; it keeps the original independent sets unchanged, only removing elements.

**Contraction**:

For $A \subseteq E$, contracting $A$ from the matroid $M$ gives the matroid $M / A$, whose family of independent sets $\mathcal{I}''$ is defined as:

$$
\mathcal{I}'' = \left\{ I \subseteq E \setminus A \,\bigg|\, \exists B \subseteq A,\, B \in \mathcal{I},\, r(B) = r(A),\, I \cup B \in \mathcal{I} \right\}
$$

The contraction operation can be understood as contracting the elements in the set $A$ and considering the independent sets formed by the remaining elements together with a basis of $A$. The result of contraction depends on a basis of the set $A$; the contracted independent set is in fact the independent set obtained after reducing a higher-rank subset in the original matroid.

**Example - graphical matroid**:

-   **Deletion**: in a graphical matroid, the deletion operation deletes some edges from the graph. After a graph $G$ deletes some edge, what is considered is the independent sets formed by the remaining edges, i.e. those edge sets containing no cycle. For example, if one edge is deleted from a triangle graph, the remaining two edges are still a forest.

-   **Contraction**: the contraction operation contracts some edge into a vertex. For a graphical matroid, contracting an edge amounts to merging the two vertices of this edge into one vertex and deleting the edge; after merging the vertices, the other edges in the graph can still form independent sets. For example, in a triangle graph, contracting any edge merges two vertices into one, and the remaining two edges form a new matroid.

## Matroids and greedy

**Problem statement**:

One application of matroids is solving optimization problems in greedy algorithms. Specifically, given a matroid $M = (S, \mathcal{I})$, where $S$ is the ground set and $\mathcal{I}$ is the family of independent sets, assign to each element $x \in S$ a positive integer weight $w(x)$; the goal is to find the independent set with maximum weight, formalized as:

$$
\max_{A \in \mathcal{I}} w(A) = \max_{A \in \mathcal{I}} \sum_{x \in A} w(x)
$$

Obviously, the maximum-weight independent set must be a maximal independent set. If an independent set $A$ is not a maximal independent set, then there exists an element $x$ that can be added to $A$, and since $w(x) > 0$, the weight increases after adding this element, showing that $A$ is not the maximum-weight independent set.

### Steps

The steps of the greedy algorithm for finding the maximum-weight independent set are as follows:

1.  **Element sorting**: sort the ground set $S$ by weight from large to small, denoted as the sequence $e_1, e_2, \dots, e_n$.
2.  **Initialization**: let the independent set $A = \emptyset$.
3.  **Building the independent set**: consider the sorted elements $e_i$ in turn; if $A \cup \{ e_i \} \in \mathcal{I}$, then update $A = A \cup \{ e_i \}$.
4.  **Output the result**: the final set $A$ is the maximum-weight independent set.

**Complexity analysis**:

Let $n = |S|$ be the size of the ground set, and $f(n)$ denote the complexity of determining whether a set is an independent set. The time complexity of the greedy algorithm is:

$$
O(n \log n + n f(n))
$$

where $O(n \log n)$ is the complexity of sorting, and $O(n f(n))$ is the complexity of determining independence one by one.

???+ note "Remark"
    -   In a graphical matroid, one can use a [disjoint-set union](../ds/dsu.md) to efficiently detect whether a cycle is formed, making $f(n)$ close to constant time.
    -   In a linear matroid, independence detection usually involves matrix operations, whose complexity depends on the specific implementation.

**Proof of correctness**:

Let $M = (S, \mathcal{I})$ be a matroid, $A \in \mathcal{I}$ be an independent set, and $A$ be a subset of some maximum-weight independent set $T$. Define the set $P = \{ x \in S \setminus A \mid A \cup \{x\} \in \mathcal{I} \}$, i.e. the set formed by all elements that, when added to $A$, still keep $A$ independent.

Let $y$ be the maximum-weight element in $P$; then $A' = A \cup \{ y \}$ is also a subset of some maximum-weight independent set, as proved below:

Suppose $A' = A \cup \{ y \}$ is not a subset of any maximum-weight independent set; then there exists a maximum-weight independent set $T$ with $|A'| < |T|$.

Since $|A'| < |T|$, by the **exchange property** of the matroid, there exists $x \in T \setminus A'$ such that $A' \cup \{ x \} \in \mathcal{I}$.

Using the **exchange property**, continually add $x$ to $A'$, and eventually construct a new independent set $A''$ with $|A''| = |T|$.

Let $K = A'' \cap T$; then $x = T \setminus K$, $y = A'' \setminus K$. Since $y$ is the maximum-weight element in $P$, $w(x) \leq w(y)$.

Therefore, $w(A'') = w(K) + w(y) \geq w(K) + w(x) = w(T)$, and in this case:

-   If $w(A'') > w(T)$, then $T$ is not a maximum-weight independent set, contradicting the assumption.
-   If $w(A'') = w(T)$, then $A''$ is a maximum-weight independent set with $A'$ as its subset, contradicting the assumption that $A'$ is not a subset of any maximum-weight independent set.

In summary, the assumption does not hold, that is, $A' = A \cup \{ y \}$ must be a subset of some maximum-weight independent set; therefore, by continually using the greedy strategy, one can eventually find the maximum-weight independent set.

### Example

**Minimum spanning tree**:

Given a connected undirected graph $G = (V, E)$ where each edge $e \in E$ has a weight $w(e)$, the goal is to find a spanning tree that contains all vertices and has minimum total weight.

**Construction of the matroid**:

To formalize the minimum spanning tree problem as a matroid problem, one can construct the graphical matroid $M(G)$:

-   **Ground set**: $S = E$, i.e. all edges of the graph.
-   **Family of independent sets**: $\mathcal{I}$ is all edge sets containing no cycle (i.e. all forests).

**Greedy algorithm**:

Under the framework of the graphical matroid, [Kruskal's algorithm](../graph/mst.md#kruskal-算法) is a typical greedy algorithm based on matroid theory that can be used to construct the minimum spanning tree. Although [Prim's algorithm](../graph/mst.md#prim-算法) is also an effective greedy algorithm that can likewise find the minimum spanning tree, it does not strictly depend on matroid greedy. Therefore, in the discussion of matroid theory, Kruskal's algorithm is the main example of a greedy algorithm.

-   **Kruskal's algorithm**:
    1.  **Edge sorting**: sort all edges by weight from small to large.
    2.  **Step-by-step selection**: select the edges of smallest weight in turn; if adding one does not form a cycle, add it to the spanning tree.
    3.  **Termination condition**: repeat the above process until the spanning tree contains $|V| - 1$ edges.

-   **Prim's algorithm**:
    -   **Principle**: Prim's algorithm starts from a starting vertex and gradually expands the spanning tree, each time selecting the minimum-weight edge connecting a vertex inside the tree with a vertex outside the tree.
    -   Although Prim's algorithm is also greedy, its selection strategy differs from other greedy algorithms based on the matroid exchange property. Therefore, in the strict sense of matroid theory, Prim's algorithm is not regarded as a typical matroid greedy algorithm.

## Matroid intersection

For two matroids $M_1 = (S, \mathcal{I}_1)$ and $M_2 = (S, \mathcal{I}_2)$ defined on the same ground set $S$, if $\mathcal{I} = \mathcal{I}_1 \cap \mathcal{I}_2$ satisfies the three properties of a matroid's family of independent sets, then $M = (S, \mathcal{I})$ is called the **intersection** of $M_1$ and $M_2$.

**Note**: not every intersection of two matroids is a matroid; only when the intersection of their families of independent sets satisfies the three properties in the definition of a matroid's family of independent sets does their intersection constitute a matroid.

### Problem statement

1.  **Maximum independent set**: find the largest independent set (i.e. the independent set with maximum cardinality) in $\mathcal{I}_1 \cap \mathcal{I}_2$.
2.  **Weighted maximum independent set**: given a weight function $w: S \to \mathbb{R}$, find the independent set with maximum weight sum in $\mathcal{I}_1 \cap \mathcal{I}_2$.

### Algorithm

**Unweighted version**:

1.  **Initialization**: choose an initial independent set $I \in \mathcal{I}_1 \cap \mathcal{I}_2$, usually setting $I = \emptyset$.
2.  **Iteration**:
    -   **Build the exchange graph**: build the exchange graph $D_{M_1, M_2}(I)$ according to the current independent set $I$.
    -   **Path selection**: in the exchange graph, find an augmenting path $P$ from the source $s$ to the sink $t$.
    -   **Augmentation**: traverse each node along the path $P$ from $s$ to $t$:
        -   if the node belongs to the left vertices (i.e. elements in $I$), then remove this element from $I$.
        -   if the node belongs to the right vertices (i.e. elements in $S \setminus I$), then add this element to $I$.
    -   **Repeat**: after updating the independent set $I$, repeat the above steps until no new augmenting path can be found.
3.  **Result**: the finally obtained independent set $I$ is a maximum independent set in the matroid intersection $M = M_1 \cap M_2$.

**Weighted version**:

To find the independent set with maximum weight sum, the algorithm needs to optimize the selection of the augmenting path.

1.  **Weight setting**: for each element $e \in S$, define its weight $w'(e)$ in the exchange graph:
    -   **Left vertex** (element in $I$): $w'(e) = -w(e)$.
    -   **Right vertex** (element in $S \setminus I$): $w'(e) = w(e)$.
2.  **Path selection**: in the exchange graph $D_{M_1, M_2}(I)$, find an **augmenting path** $P$ from the source $s$ to the sink $t$ such that after performing the augmentation operation along the path, the total weight of the independent set $I$ increases the most.
    -   **Augmentation condition**: the sum of the weights of the elements added along the path $P$ is greater than the sum of the weights of the elements removed, i.e. $\sum_{y \in \text{added elements}} w(y) > \sum_{x \in \text{removed elements}} w(x)$
3.  **Augmentation operation**: traverse each node along the path $P$ from $s$ to $t$:
    -   if the node belongs to the left vertices (i.e. elements in $I$), then remove this element from $I$.
    -   if the node belongs to the right vertices (i.e. elements in $S \setminus I$), then add this element to $I$.
4.  **Iteration**: repeat steps 1 to 3, continually building the exchange graph and finding augmenting paths, gradually optimizing the total weight of the independent set $I$.
5.  **Termination condition**: when no path satisfying the augmentation condition can be found in the exchange graph, the algorithm terminates.
6.  **Result**: the finally obtained independent set $I$ is a **maximum-weight independent set** in the matroid intersection $M = M_1 \cap M_2$.

**Complexity**:

-   **Number of augmentations**: let the maximum ranks of the two matroids be $r_1$ and $r_2$ respectively; then the maximum number of augmentations is $\min(r_1, r_2)$.

-   **Complexity of each augmentation**:
    -   The complexity of building the exchange graph is $O(n^2)$, where $n = |S|$.
    -   The complexity of finding an augmenting path depends on the path search strategy, usually $O(n^2)$, for example using breadth-first search.

-   **Total time complexity**: the overall time complexity is $O(r \cdot n^2)$, where $r = \min(r_1, r_2)$.

## Example problems

**Minimum spanning tree**:

Given an undirected graph $G = (V, E)$ where each edge $e \in E$ has a weight $w(e)$, find a spanning tree that contains all vertices and has minimum total weight.

-   Detailed introduction: [minimum spanning tree](../graph/mst.md).
-   Problem template: [Luogu P3366 【模板】最小生成树](https://www.luogu.com.cn/problem/P3366).

??? note "Solution idea"
    Use Kruskal's algorithm: sort all edges by weight from small to large, then select edges step by step; if adding one does not form a cycle, add it to the spanning tree; the finally obtained spanning tree is the minimum spanning tree.

**Colorful Graph**:

Given an undirected graph $G = (V, E)$ with multiple colors, where each edge has a color attribute, find a maximum edge set such that:

1.  The selected edges do not form any cycle.
2.  The number of edges of each color does not exceed $k$ ($k$ being a given positive integer).

??? note "Solution idea"
    1.  **Matroid modeling**:
    
        -   **Graphical matroid ($M_1$)**: defined as all edge sets that do not form a cycle, i.e. the family of independent sets $\mathcal{I}_1$ contains all edge sets that do not form a cycle.
        -   **Color matroid ($M_2$)**: defined as edge sets in which the number of edges of each color does not exceed $k$, i.e. the family of independent sets $\mathcal{I}_2$ contains all edge sets satisfying that the number of edges of each color $\leq k$.
    2.  **Solve the matroid intersection**: by solving $M = M_1 \cap M_2$, find the maximum edge set that neither forms a cycle nor has the number of edges of any color exceeding $k$.

**Constrained resource allocation problem**:

In a resource allocation problem, there is a set of resources $R = \{r_1, r_2, \dots, r_n\}$ and a set of projects $P = \{p_1, p_2, \dots, p_m\}$. Each project $p_i$ needs a certain amount of resources allocated, and the total allocation of each resource cannot exceed its supply.

**Goal**: find a resource allocation scheme that satisfies all project demands and does not exceed the resource supply.

??? note "Solution idea"
    1.  **Matroid modeling**:
    
        -   **Demand matroid ($M_1$)**: defined as allocation schemes satisfying the resource demands of each project, i.e. the family of independent sets $\mathcal{I}_1$ contains all resource allocation sets satisfying the project demands.
        -   **Supply matroid ($M_2$)**: defined as allocation schemes not exceeding the supply of each resource, i.e. the family of independent sets $\mathcal{I}_2$ contains all resource allocation sets satisfying the resource supply restrictions.
    2.  **Solve the matroid intersection**: by solving $M = M_1 \cap M_2$, find a resource allocation scheme that both satisfies all project demands and does not exceed the resource supply.

## References and notes

1.  [Wikipedia - Matroid](https://en.wikipedia.org/wiki/Matroid)
2.  [Baidu Baike - 拟阵](https://baike.baidu.com/item/%E6%8B%9F%E9%98%B5)
3.  [Luogu - 拟阵与最优化问题](https://www.luogu.com.cn/article/87d02q9f)
4.  [Luogu - 从拟阵基础到 Shannon 开关游戏](https://www.luogu.com.cn/article/fuj3x886)
