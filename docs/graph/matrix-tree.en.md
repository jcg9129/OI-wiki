author: pw384, s0cks5, Watersail2005, Xeonacid

The matrix-tree theorem solves the problem of counting the number of spanning trees of a graph.

## Notation declaration for this article

The graphs in this article, whether undirected or directed, allow multiple edges, but by default have no self-loops.

??? note "The case with self-loops"
    Self-loops do not affect the number of spanning trees, nor do they affect the computation of the Laplace matrix in the following text, so the matrix-tree theorem still holds in the case with self-loops. There is no need to remove self-loops when computing. If self-loops are removed, it will affect the application of the matrix-tree theorem to count the number of Euler circuits of a directed graph according to the BEST theorem.

### Undirected graph case

Let $G$ be an undirected graph with $n$ vertices. Define the degree matrix $D(G)$ as

$$
D_{ii}(G) = \mathrm{deg}(i),\ D_{ij} = 0,\ i\neq j.
$$

Let $\#e(i,j)$ be the number of edges connecting point $i$ and point $j$, and define the adjacency matrix $A$ as

$$
A_{ij}(G)=A_{ji}(G)=\#e(i,j),\ i\neq j.
$$

Define the Laplace matrix (also called the Kirchhoff matrix) $L$ as

$$
L(G) = D(G) - A(G).
$$

Denote the number of all spanning trees of the graph $G$ as $t(G)$.

### Directed graph case

Let $G$ be a directed graph with $n$ vertices. Define the out-degree matrix $D^{out}(G)$ as

$$
D^\mathrm{out}_{ii}(G) = \mathrm{deg}^\mathrm{out}(i),\ D^\mathrm{out}_{ij} = 0,\ i\neq j.
$$

Similarly define the in-degree matrix $D^\mathrm{in}(G)$.

Let $\#e(i,j)$ be the number of directed edges from point $i$ pointing to point $j$, and define the adjacency matrix $A$ as

$$
A_{ij}(G)=\#e(i,j),\ i\neq j.
$$

Define the out-degree Laplace matrix $L^\mathrm{out}$ as

$$
L^\mathrm{out}(G) = D^\mathrm{out}(G) - A(G).
$$

Define the in-degree Laplace matrix $L^\mathrm{in}$ as

$$
L^\mathrm{in}(G) = D^\mathrm{in}(G) - A(G).
$$

Denote the number of all root-directed arborescences of the graph $G$ rooted at $k$ as $t^\mathrm{root}(G,k)$. A so-called root-directed arborescence means that the underlying graph of this graph is a tree, and all edges point toward the parent.

Denote the number of all leaf-directed arborescences of the graph $G$ rooted at $k$ as $t^\mathrm{leaf}(G,k)$. A so-called leaf-directed arborescence means that the underlying graph of this graph is a tree, and all edges point toward the children.

## Statement of the theorem

The matrix-tree theorem has multiple forms.

Define $[n]=\{1,2,\cdots,n\}$; the submatrix $A_{S,T}$ of a matrix $A$ is the submatrix obtained by selecting the elements $A_{i,j}\pod{i\in S,j\in T}$.

???+ note "Theorem 1 (matrix-tree theorem, undirected graph, determinant form)"
    For an undirected graph $G$ and any $k$, we have
    
    $$
    t(G) = \det L(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    That is to say, all $(n-1)$-order principal minors of the Laplace matrix of an undirected graph are equal, and all equal the number of spanning trees of the graph.

???+ note "Corollary 1 (matrix-tree theorem, undirected graph, eigenvalue form)"
    Let $\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_{n-1}\ge\lambda_n=0$ be the $n$ eigenvalues of $L(G)$; then we have
    
    $$
    t(G) = \frac{1}{n}\lambda_1\lambda_2\cdots\lambda_{n-1}.
    $$

???+ note "Theorem 2 (matrix-tree theorem, directed graph root-directed tree, determinant form)"
    For a directed graph $G$ and any $k$, we have
    
    $$
    t^\mathrm{root}(G,k) = \det L^\mathrm{out}(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    That is to say, the principal minor obtained by deleting the $k$-th row and $k$-th column of the out-degree Laplace matrix of a directed graph equals the number of root-directed arborescences rooted at $k$.

Therefore, if we want to count all root-directed arborescences of a graph, we only need to enumerate all roots $k$ and sum over $t^\mathrm{root}(G,k)$.

???+ note "Theorem 3 (matrix-tree theorem, directed graph leaf-directed tree, determinant form)"
    For a directed graph $G$ and any $k$, we have
    
    $$
    t^\mathrm{leaf}(G,k) = \det L^\mathrm{in}(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    That is to say, the principal minor obtained by deleting the $k$-th row and $k$-th column of the in-degree Laplace matrix of a directed graph equals the number of leaf-directed arborescences rooted at $k$.

Therefore, if we want to count all leaf-directed arborescences of a graph, we only need to enumerate all roots $k$ and sum over $t^\mathrm{leaf}(G,k)$.

???+ note "Note"
    A root-directed arborescence is also called an in-tree (inward arborescence), but because computing the in-tree uses the out-degree, in order to avoid confusion between $\mathrm{in}$ and $\mathrm{out}$, the term "root-directed" is adopted.

## Proof of the theorem

Observing that the above theorem forms are extremely similar, here we give a unified way of proving them, and extend the previous conclusions to weighted graphs.

The general idea of the proof is as follows:

-   First, all cases can be reduced to the case of counting root-directed arborescences on directed graphs;
-   Use matrix language to give the necessary and sufficient condition that the several selected edges can form a root-directed arborescence;
-   Connect the edge-selection operation with the determinant of the Laplace matrix using the Cauchy–Binet formula;
-   Finally, convert the determinant-form conclusion into the eigenvalue-form conclusion.

### Lemma: Cauchy–Binet formula

???+ note "Lemma 1 (Cauchy–Binet)"
    Given an $n\times m$ matrix $A$ and an $m\times n$ matrix $B$, we have
    
    $$
    \det(AB)=\sum_{S\subset[m];~|S|=n}\det A_{[n],S}\det B_{S,[n]},
    $$
    
    where the meaning of the summation symbol is that $S$ ranges over all subsets of $[m]$ of size $n$. If $n>m$, then necessarily $\det(AB)=0$.

??? note "Proof (combinatorial viewpoint)"
    Referring to the model of [「NOI2021」Path intersection](https://loj.ac/p/3533), first consider the following combinatorial meaning of the determinant. For an $n\times n$ matrix $C$, build a directed acyclic graph $G=(V,E)$. Here, the vertex set is $V=[2]\times[n]\subset\mathbb R^2$, i.e. two columns of points on the plane. Denote the left column of points as $L=\{l_i=(1,i):i\in[n]\}$, and the right column of points as $R=\{r_i=(2,i):i\in[n]\}$; the directed edge set is $E=\{(l_i,r_j):i,j\in[n]\}$, with edge weights $w(l_i,r_j)=C_{i,j}$. In the graph, a subset of edges $E^\sigma\subset E$ of size $n$ is called a path set if its start points are pairwise distinct and its end points are also pairwise distinct. Obviously, path sets $E^\sigma$ correspond one-to-one with permutations $\sigma$ on $[n]$. Note that if a path set is drawn on the plane, these edges may pairwise intersect, and the number of these intersection points (counting multiplicity) equals the number of inversions of $\sigma$. This is because edge $(l_i,r_{\sigma(i)})$ and edge $(l_j,r_{\sigma(j)})$ intersect if and only if $(i-j)(\sigma(i)-\sigma(j))< 0$, i.e. this is an inversion. For convenience, the parity of the number of inversions of the corresponding permutation, i.e. the parity of the number of intersection points of the path set, is called the parity of the path set. So, if these path sets are counted according to weight, and the number of path sets with an even number of intersection points is subtracted by the number of path sets with an odd number of intersection points, we obtain the Leibniz expansion of the determinant:
    
    $$
    \det(C)=\sum_{\sigma\in S_n}\mathrm{sgn}(\sigma)\prod_{i\in[n]}C_{i,\sigma(i)},
    $$
    
    where $S_n$ is the permutation group on $[n]$, and $\mathrm{sgn}(\sigma)$ is the sign of the permutation $\sigma$ (when the number of inversions is even, it equals $1$; when the number of inversions is odd, it equals $-1$).
    
    After understanding the combinatorial meaning of the determinant, we can use the following combinatorial model to prove the Cauchy–Binet formula. For an $n\times m$ matrix $A$ and an $m\times n$ matrix $B$, build a directed acyclic graph $G=(V,E)$. Here, the vertex set is $V=L\cup D\cup R$, where $L=\{l_i=(1,i):i\in[n]\}$, $D=\{d_i=(2,i):i\in[m]\}$ and $R=\{r_i=(3,i):i\in[n]\}$; the directed edge set is $E=E_L\cup E_R$, where $E_L=\{(l_i,d_j):i\in[n],j\in[m]\}$ and $E_R=\{(d_j,r_i):j\in[m],i\in[n]\}$, respectively assigned edge weights $w(l_i,d_j)=A_{i,j}$ and $w(d_j,r_i)=B_{j,i}$. Likewise consider the path sets from $L$ through $D$ to $R$ (paths pairwise not sharing vertices), count according to weight, and subtract the number of path sets with an odd number of intersection points from the number of path sets with an even number of intersection points. Below we explain that the left and right sides of the Cauchy–Binet formula compute this number in two ways respectively.
    
    For the left side, based on the graph $G$ described above, build a new graph $G'$, whose vertex set is $V'=L\cup R$, and edge set is $E'=\{(l_i,r_j):i,j\in[n]\}$, and for edge $(l_i,r_j)$ assign the edge weight $\sum_{k\in[m]}A_{i,k}B_{k,j}$, i.e. the weighted count of simple paths from $l_i$ to $r_j$ in the original graph $G$. This edge weight is exactly $(AB)_{i,j}$. This amounts to simplifying the above three-layer graph into a two-layer graph. However, the path sets in the two-layer graph $G'$ (counted by weight) do not correspond one-to-one with the path sets in the three-layer graph $G$. Since in the two-layer graph, each path corresponds to several simple paths in the three-layer graph, when counting path sets of the two-layer graph, the weights need to be multiplied, which is equivalent to pairwise combining the sets of paths in the corresponding three-layer graph, which will inevitably cause situations where an intermediate stopover point is shared. However, these path pairs sharing an intermediate stopover point do not contribute to the final answer, because for $i_1< i_2$ and $j_1< j_2$ and any intermediate point $d$, there exist two kinds of simple path pairs $(l_{i_1}\rightarrow d\rightarrow r_{j_1}, l_{i_2}\rightarrow d\rightarrow r_{j_2})$ and $(l_{i_1}\rightarrow d\rightarrow r_{j_2}, l_{i_2}\rightarrow d\rightarrow r_{j_1})$, but the parities of the numbers of intersection points of these two sets of paths in the three-layer graph must be opposite, because if we look only at the start and end points, the two sets of paths swapped their end points. So, these paths sharing an intermediate stopover point will cancel pairwise when counting in the simplified two-layer graph. For the remaining cases, if the start and end points of two paths are given, then no matter how the intermediate points are chosen (as long as they do not choose the same point), the parity of the number of intersection points of these two paths does not change. Therefore, every path set in $G'$ corresponds to all path sets in the original graph $G$ that have the same parity. Thus, $\det(AB)$ provides one way of computing the difference of the path-set counts described above.
    
    For the right side, it amounts to enumerating all possible combinations of intermediate points. Given any intermediate point set $S\subset D=[m]$ with $|S|=n$, respectively consider the path sets from $L$ to $S$ and the path sets from $S$ to $R$; they can be connected to obtain path sets from $L$ to $R$, and the composition of the permutations corresponding to the first two path sets equals the permutation corresponding to the subsequent path set, so the product of the parities of the first two path sets equals the parity of the subsequent path set. So, the difference of the counts of all path sets with intermediate point set $S$ is exactly the product of the difference of the counts of path sets from $L$ to $S$ and the difference of the counts of path sets from $S$ to $R$. Summing over all possible $S$ gives the right side, so it is exactly the difference of the path-set counts described above.

??? note "Proof (algebraic viewpoint)"
    The above combinatorial proof can actually be translated word for word into an algebraic proof. Here we instead provide another more technical algebraic proof, but which uses several common conclusions. When $m< n$, the determinant is zero, because
    
    $$
    \mathrm{rank}(AB)\le \min\{\mathrm{rank}(A),\mathrm{rank}(B)\}\le m< n.
    $$
    
    When $m=n$, the Cauchy–Binet formula is exactly that the determinant of the product of square matrices equals the product of the determinants of the square matrices.
    
    When $m>n$, note that
    
    $$
    x^{m-n}\det(xI_n+AB) = \det(xI_m+BA).
    $$
    
    It is also a known conclusion that the coefficient of $x^{n-k}$ in $\det(xI_n+C)$ is the sum of all $k$-order principal minors of $C$. Therefore, comparing the coefficients on both sides of the above equation, we have
    
    $$
    \det(AB) = \sum_{S\subset[m];~|S|=n}\det(BA)_{S,S} = \sum_{S\subset[m];~|S|=n}\det(B)_{S,[n]}\det(A)_{[n],S} = \sum_{S\subset[m];~|S|=n}\det(A)_{[n],S}\det(B)_{S,[n]}.
    $$
    
    Here, the second equals sign uses the conclusion of the $m=n$ case.

### Characterizing the graph structure with incidence matrices

For a directed graph $G=(V,E)$, with number of vertices $n$, number of edges $m$, and edge $e$ assigned edge weight $w(e)$. From this, we can define the $m\times n$ out-degree incidence matrix

$$
M^\mathrm{out}_{ij}=\begin{cases}
\sqrt{w(e_i)},&\exists u(e_i=(v_j,u)),\\
0,&\textrm{otherwise},
\end{cases}
$$

and the $m\times n$ in-degree incidence matrix

$$
M^\mathrm{in}_{ij}=\begin{cases}
\sqrt{w(e_i)},&\exists u(e_i=(u,v_j)),\\
0,&\textrm{otherwise}.
\end{cases}
$$

Each row of them records one edge: the out-degree incidence matrix $M^\mathrm{out}$ records the start point of the edge, and the in-degree incidence matrix $M^\mathrm{in}$ records the end point of the edge.

A simple computation shows

$$
D^\mathrm{out}(G) = (M^\mathrm{out})^T M^\mathrm{out},\ A(G) = (M^\mathrm{out})^T M^\mathrm{in},\ D^\mathrm{in}(G) = (M^\mathrm{in})^T M^\mathrm{in}.
$$

Furthermore we have

$$
L^\mathrm{out}(G) = (M^\mathrm{out})^T (M^\mathrm{out}-M^\mathrm{in}),\ L^\mathrm{in}(G) = (M^\mathrm{in}-M^\mathrm{out})^T M^\mathrm{in}.
$$

The Cauchy–Binet formula above shows that the principal minors of the Laplace matrix are actually a sum of a series of substructures. Each substructure reflects the property of the corresponding subgraph.

???+ note "Lemma 2"
    For a subgraph $(W,S)$ of $G$, if it satisfies $|W|=|S|\le n$, then the subgraph $T=(V,S)$ is a root-directed forest rooted at $V\setminus W$ if and only if the corresponding expression
    
    $$
    \det(M^\mathrm{out}_{S,W})\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W})
    $$
    
    is not zero. Moreover, when this expression is not zero, it must equal $\prod_{e\in S}w(e)$, denoted $w(T)$.

??? note "Proof"
    Without loss of generality, assume $w(e)=1$. This is by the multilinearity of the determinant: each row of each determinant can extract a factor $\sqrt{w(e)}$, and the product of these factors is $w(T)$.
    
    First analyze the conditions under which the two factors equal zero. The former factor $\det(M^\mathrm{out}_{S,W})$ has at most one nonzero number per row, namely $+1$. If any row is all zeros, then this determinant must be zero. So, this determinant is not zero if and only if each row has exactly one $+1$, i.e. each point in $W$ is exactly the start point of one edge in $S$, and no two edges share the same start point. Given that $T$ becomes a root-directed forest rooted at $V\setminus W$, a necessary condition is that except for the roots, all vertices have exactly one parent node, which necessarily makes this factor nonzero; but the converse does not necessarily hold, because it cannot be guaranteed that there is no cycle, so we still need to examine the second factor. Note that the end point of $S$ is not necessarily in $W$.
    
    Assume the former factor is nonzero; then at this time the subgraph $T$ becomes a root-directed forest if and only if $T$ has no cycles. At this time, each row of the latter term $\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W})$ has one $+1$, but may have one or zero $-1$. For an edge whose end point is also in $W$, if the end point of $e_i$ is the start point of $e_j$, then adding the row corresponding to $e_j$ to the row corresponding to $e_i$ can eliminate the $-1$ in the $e_i$ row. As can be imagined, at this time this row describes the simple path in which $e_i$ and $e_j$ are connected head-to-tail. If a new $-1$ appears in this row, then it means the end point of $e_j$ is also in $W$, and the position of the $-1$ is the end point of $e_j$; accordingly, we can continue to find the edge whose start point is the end point of $e_j$, and add it to this row again. Such an edge always exists, because the previous paragraph shows that each point in $W$ is exactly the start point of one edge in $S$. This process continues until this row no longer has a $-1$, which is equivalent to continually adding new edges to the simple path $e_i\rightarrow e_j\rightarrow \cdots\rightarrow e_k$. At this time, if this row has only one $+1$ left, then it means the end point of $e_k$ is not in the selected vertices $W$, and the process terminates; if the last added edge happens to cancel the existing $+1$, i.e. this row has only zero left, then it means the end point of the new edge $e_k$ is exactly the start point of the initial edge $e_i$, i.e. a cycle appears. So, the necessary and sufficient condition for having no cycle is that this determinant can be transformed by the above operations into a form where each row has exactly one $+1$. Since the positions of these $+1$s are the start points of the edges corresponding to the rows, the matrix obtained at this time is actually $\det(M^\mathrm{out}_{S,W})$.
    
    In summary, if $T$ is not a root-directed forest, then either $\det(M^\mathrm{out}_{S,W})=0$ or $\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W})=0$; otherwise, both are nonzero, and the product equals $\left(\det(M^\mathrm{out}_{S,W})\right)^2=1$.

### The matrix-tree theorem for weighted directed graphs

Now we can prove the main result of this article. The matrix-tree theorems stated above are all special cases of this theorem.

???+ note "Theorem 4 (matrix-tree theorem, weighted directed graph root-directed tree, determinant form)"
    For any $k$, we have
    
    $$
    \sum_{T\in\mathcal T^\mathrm{root}(G,k)}w(T)=\det L^\mathrm{out}(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Here, $\mathcal T^\mathrm{root}(G,k)$ is the set of root-directed arborescences of $G$ rooted at $k$.

??? note "Proof"
    Denote $W=[n]\setminus\{k\}$ as the set of remaining vertices except point $k$. Then, according to the Cauchy–Binet formula, the right side can be written as
    
    $$
    \det L^\mathrm{out}(G)_{W,W} = \sum_{S\subset[m];~|S|=n-1}\det(M^\mathrm{out}_{S,W})\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W}).
    $$
    
    Traversing all $S$, by Lemma 2, if and only if $T=(V,S)$ forms a root-directed forest rooted at $V\setminus W=\{k\}$, i.e. $T$ is a root-directed arborescence rooted at $k$, the right side accumulates a $w(T)$.

When $w(e)=1$, the weight of every tree is $1$, so the left side is the count of all trees, i.e. $t^\mathrm{root}(G,k)$, which gives Theorem 2. Analogously to the above, the conclusion can be directly generalized to leaf-directed arborescences, which gives Theorem 3. Finally, to obtain the count of spanning trees on undirected graphs, we can apply the following corollary.

???+ note "Corollary 4 (matrix-tree theorem, weighted undirected graph, determinant form)"
    For an undirected graph $G$ and any $k$, we have
    
    $$
    \sum_{T\in\mathcal T(G)}w(T) = \det L(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Here, $\mathcal T(G)$ is the set of spanning trees of $G$. This also shows that all $(n-1)$-order principal minors of $L(G)$ are equal.

??? note "Proof"
    For an undirected graph $G=(V,E)$, we can construct a directed graph $G'=(V,E')$, where $E'=\{(v_i,v_j):(v_i,v_j)\in E\}\cup\{(v_j,v_i):(v_i,v_j)\in E\}$, i.e. each undirected edge in $G$ is split into two directed edges of opposite directions in the directed graph. Choose any $k$; then the root-directed arborescences of $G'$ rooted at $k$ correspond one-to-one with the spanning trees of $G$. From the former to the latter, we only need to remove the orientation of the edges and the selection of the root; from the latter to the former, we only need to start from the selected root $k$ and select the root-directed orientation edge by edge as the orientation of the edges. So, at this time we have
    
    $$
    \sum_{T\in\mathcal T(G)}w(T) = \sum_{T\in\mathcal T^\mathrm{root}(G',k)}w(T) = \det L^\mathrm{out}(G')_{[n]\setminus\{k\},[n]\setminus\{k\}} = \det L(G)_{[n]\setminus\{k\},[n]\setminus\{k\}}.
    $$
    
    Here we use the conclusion $L^\mathrm{out}(G')=L(G)$, which is easy to verify directly.

### Eigenvalue form

We still first consider the conclusion on directed graphs.

???+ note "Theorem 5"
    For a directed graph $G$, define the multivariate polynomial
    
    $$
    \chi(x_1,\cdots,x_n)=\det(\mathrm{diag}(x_1,\cdots,x_n)-L^\mathrm{out}(G)).
    $$
    
    Here, $\mathrm{diag}(x_1,\cdots,x_n)$ refers to the diagonal matrix with $x_1,\cdots,x_n$ as diagonal elements. Then,
    
    $$
    (-1)^{n-r}[x_{k_1},\cdots,x_{k_r}]\chi(x_1,\cdots,x_n)
    $$
    
    equals the (weighted) count of root-directed forests of $G$ rooted at $\{k_1,\cdots,k_r\}$.

??? note "Proof"
    Imitating the proof of Theorem 4, note that if we let $W=[n]\setminus\{k_1,\cdots,k_r\}$, then the coefficient in the theorem is exactly $\det L^\mathrm{out}(G)_{W,W}$ (this may be observed directly from the Leibniz expansion of the determinant). According to the Cauchy–Binet formula, it equals
    
    $$
    \det L^\mathrm{out}(G)_{W,W} = \sum_{S\subset[m];~|S|=n-r}\det(M^\mathrm{out}_{S,W})\det(M^\mathrm{out}_{S,W}-M^\mathrm{in}_{S,W}).
    $$
    
    Traversing all $S$, by Lemma 2, if and only if $T=(V,S)$ forms a root-directed forest rooted at $V\setminus W=\{k_1,\cdots,k_r\}$, the right side accumulates a $w(T)$.

Substituting $x$ into all unknowns, we obtain the characteristic polynomial of the Laplace matrix

$$
P(x) = \det(xI-L^\mathrm{out}(G)) = \chi(x,\cdots,x).
$$

???+ note "Lemma 3"
    The Laplace matrix $L^\mathrm{out}(G)$ has at least one eigenvalue equal to zero.

??? note "Proof"
    It suffices to prove that its determinant is zero. Imitating the proofs of Theorems 4 and 5, take $W=\varnothing$; then the size of this determinant should equal the number of root-directed forests with zero trees. This does not exist, so this determinant equals zero.

???+ note "Corollary 5"
    For a directed graph $G$, the sum of the weights of all root-directed forests consisting of $k$ trees equals the coefficient
    
    $$
    (-1)^{n-k}[x^k]P(x).
    $$

??? note "Proof"
    Just sum over all possible choices of $k$ roots.

Define a **$k$-spanning forest** as a spanning subgraph of the graph such that this subgraph has $k$ connected components and no cycle.

???+ note "Corollary 6"
    Denote the set of $k$-spanning forests of the undirected graph $G$ as $\mathcal T_k(G)$; then
    
    $$
    \sum_{T\in\mathcal T_k(G)}w(T)Q(T) = (-1)^{n-k}[x^k]P(x).
    $$
    
    Here, $Q(T)$ is the product of the numbers of vertices of each connected component in the forest $T$. In particular, when $k=1$, we have $Q(T)=n$, so
    
    $$
    n\sum_{T\in\mathcal T(G)}w(T) = \lambda_1\lambda_2\cdots\lambda_{n-1}.
    $$

??? note "Proof"
    Imitating the proof of Corollary 4, we can directly use the conclusion of Corollary 5. Every root-directed forest consisting of $k$ trees in a directed graph corresponds to a $k$-spanning forest in an undirected graph. However, since each $k$-spanning forest $T$ has $Q(T)$ ways of choosing roots, it appears in $Q(T)$ root-directed forests of the directed graph.

## Applications

### Cayley's formula

???+ note "Corollary 7 (Cayley)"
    There are $n^{n-2}$ labeled unrooted trees of size $n$.

??? note "Proof"
    Equivalently, it suffices to find that the number of spanning trees of the complete graph on $n$ vertices is $n^{n-2}$. For this, write out the Laplace matrix
    
    $$
    L(G) = \left(\begin{matrix} n-1 & -1 & \cdots & -1 \\ -1 & n-1 & \cdots & -1 \\ \vdots & \vdots & \ddots & \vdots \\ -1 & -1 & \cdots & n-1  \end{matrix}\right)_{n\times n}.
    $$
    
    Computing any of its principal minors, we have
    
    $$
    \det(nI_{n-1}-{\bf 1}{\bf 1}^T) = n^{n-1}\det(I_{n-1}-n^{-1}{\bf 1}{\bf 1}^T) = n^{n-1}(1-n^{-1}{\bf 1}^T{\bf 1}) = n^{n-1}(1-(n-1)/n) = n^{n-2}.
    $$
    
    Applying Theorem 1 gives the conclusion.

### BEST theorem

Prerequisite knowledge: [Euler graph](./euler.md)

This theorem connects the number of Euler circuits in a directed Euler graph with the number of root-directed arborescences of the graph, thereby solving the problem of counting Euler circuits in a directed graph. Note that the problem of counting Euler circuits in an arbitrary undirected graph is NP-complete.

When implementing this algorithm, we should first determine whether the given graph is an Euler graph, remove all zero-degree vertices, then build the graph and compute the number of root-directed arborescences, and obtain the count of Euler circuits by the BEST theorem. Note that if the required number of Euler circuits requires a given point as the start point, we need to multiply the answer by the out-degree of that point, which amounts to enumerating the first edge in the circuit.

Before proving the BEST theorem, we need to know the following conclusion.

???+ note "Property (determination of whether a directed graph has an Euler circuit)"
    A directed graph has an Euler circuit if and only if the nonzero-degree vertices are strongly connected, and the out-degree and in-degree of all vertices are equal.

For an Euler graph, because the out-degree and in-degree are equal, we can omit their superscripts and denote them as $\mathrm{deg}(v)$. The BEST theorem can be stated as follows.

???+ note "Theorem 6 (BEST theorem)"
    Let $G$ be a directed Euler graph and $k$ any vertex; then the total number of distinct Euler circuits $\mathrm{ec}(G)$ of $G$ is
    
    $$
    \mathrm{ec}(G) = t^\mathrm{root}(G,k)\prod_{v\in V}(\deg (v) - 1)!.
    $$
    
    This also shows that for any two nodes $k, k'$ of an Euler graph $G$, we have $t^\mathrm{root}(G,k)=t^\mathrm{root}(G,k')$.

??? note "Proof"
    The general idea of the proof is to establish a correspondence between Euler circuits starting from $k$ and root-directed arborescences rooted at $k$ together with the arrangements of the out-edges at each vertex. After specifying the vertex of the Euler circuit, the count to be proved should equal
    
    $$
    \mathrm{deg}(k)\mathrm{ec}(G) = t^\mathrm{root}(G,k)\deg(k)!\prod_{v\neq k}(\deg (v) - 1)!.
    $$
    
    The construction corresponding to the combinatorial meaning of this count is as follows. For an Euler circuit starting from $k$, according to the order of appearance of each edge in the circuit, we can construct
    
    -   a root-directed arborescence rooted at $k$, consisting of the last out-edge at all non-root vertices, i.e. $t^\mathrm{root}(G,k)$,
    -   the arrangement order of all out-edges at the root $k$, i.e. $\mathrm{deg}(k)!$, and
    -   the arrangement order of all out-edges except the last out-edge at each non-root vertex $v\neq k$, i.e. $(\mathrm{deg}(v)-1)!$.
    
    Below we explain that the mapping obtained by this construction is a bijection.
    
    On one hand, given an Euler circuit, we want to prove that the last out-edges at all non-root vertices constitute a root-directed arborescence. According to the construction, each non-root vertex in the tree indeed has only one out-edge, so we only need to prove that these out-edges do not form a cycle. Note that if we sort all vertices according to the order of their last appearance in the Euler circuit, then the last out-edge of a non-root vertex must point to a vertex strictly later in the order. If there is a cycle, then there is a latest-order vertex in the cycle; because it is in the cycle, it points to a vertex that is not later in the order, which contradicts the above. So, the last out-edges of the non-root vertices must constitute a root-directed arborescence.
    
    On the other hand, given any root-directed arborescence and the arrangement order of the remaining out-edges, we can recover an Euler circuit such that this Euler circuit, after the above construction, gives the given root-directed arborescence and the arrangement order of the remaining out-edges. For this, we only need to start from the root $k$; each time we reach a vertex, according to the given arrangement order of the out-edges of that vertex, choose the earliest-order, not-yet-passed out-edge as this out-edge in the Euler circuit; if all out-edges in the arrangement at that vertex have already been passed, choose the out-edge of that vertex in the root-directed arborescence as this out-edge in the Euler circuit. Because the graph is an Euler graph, the in-degree of each vertex equals its out-degree, so this process will not terminate at a non-root vertex, i.e. the obtained path is indeed a circuit. To prove that the obtained path is a valid Euler circuit, we only need to prove that this process can traverse all edges.
    
    If it cannot, then there must be some out-edge of some vertex $v$ that is not traversed. Examine vertex $v$. Vertex $v$ cannot be the root, because we terminate at the root in the end; if the root still has out-edges remaining, this contradicts the termination of the process. So, $v$ must not be the root. According to the process described above, as long as the non-root vertex $v$ has any out-edge remaining, then the out-edge $e$ of the non-root vertex in the tree must remain. Denote $e=(v,u)$. Because some in-edge of $u$ is not traversed, according to the fact that the out-degree of $u$ equals its in-degree, there must be some out-edge of $u$ that is not traversed. Then, we can similarly examine vertex $u$. This reasoning moves the vertex being examined from $v$ to $u$, i.e. moves one step toward the root of the tree along the root-directed arborescence. We can prove by induction that at this time there must be some out-edge of the root $k$ that is not traversed. It has already been explained above that this is impossible, so we reach a contradiction. This shows that the path obtained in the previous paragraph is indeed a valid Euler circuit.
    
    We can verify that these mappings are all injections, so they must all be bijections. The original proposition is proved.

## Implementation

Write out the Laplace matrix according to the graph, delete one row and one column, and find the determinant of the resulting matrix. The determinant can be computed using Gauss–Jordan elimination.

For example, the number of spanning trees of a square graph

$$
\begin{pmatrix}
2 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & 2 & 0 \\
0 & 0 & 0 & 2 \end{pmatrix}-\begin{pmatrix}
0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1 \\
1 & 0 & 1 & 0 \end{pmatrix}=\begin{pmatrix}
2 & -1 & 0 & -1 \\
-1 & 2 & -1 & 0 \\
0 & -1 & 2 & -1 \\
-1 & 0 & -1 & 2 \end{pmatrix}
$$

$$
\begin{vmatrix}
2 & -1 & 0 \\
-1 & 2 & -1 \\
0 & -1 & 2 \end{vmatrix} = 4
$$

This can be solved with Gauss–Jordan elimination, with time complexity $O(n^3)$.

??? note "Implementation"
    ```cpp
    #include <algorithm>
    #include <cassert>
    #include <cmath>
    #include <cstdio>
    #include <cstring>
    #include <iostream>
    using namespace std;
    constexpr int MOD = 100000007;
    constexpr double eps = 1e-7;
    
    struct matrix {
      static constexpr int MAXN = 20;
      int n, m;
      double mat[MAXN][MAXN];
    
      matrix() { memset(mat, 0, sizeof(mat)); }
    
      void print() {
        cout << "MATRIX " << n << " " << m << endl;
        for (int i = 0; i < n; i++) {
          for (int j = 0; j < m; j++) {
            cout << mat[i][j] << "\t";
          }
          cout << endl;
        }
      }
    
      void random(int n) {
        this->n = n;
        this->m = n;
        for (int i = 0; i < n; i++)
          for (int j = 0; j < n; j++) mat[i][j] = rand() % 100;
      }
    
      void initSquare() {
        this->n = 4;
        this->m = 4;
        memset(mat, 0, sizeof(mat));
        mat[0][1] = mat[0][3] = 1;
        mat[1][0] = mat[1][2] = 1;
        mat[2][1] = mat[2][3] = 1;
        mat[3][0] = mat[3][2] = 1;
        mat[0][0] = mat[1][1] = mat[2][2] = mat[3][3] = -2;
        this->n--;  // remove one row
        this->m--;  // remove one column
      }
    
      double gauss() {
        double ans = 1;
        for (int i = 0; i < n; i++) {
          int sid = -1;
          for (int j = i; j < n; j++)
            if (abs(mat[j][i]) > eps) {
              sid = j;
              break;
            }
          if (sid == -1) continue;
          if (sid != i) {
            for (int j = 0; j < n; j++) {
              swap(mat[sid][j], mat[i][j]);
              ans = -ans;
            }
          }
          for (int j = i + 1; j < n; j++) {
            double ratio = mat[j][i] / mat[i][i];
            for (int k = 0; k < n; k++) {
              mat[j][k] -= mat[i][k] * ratio;
            }
          }
        }
        for (int i = 0; i < n; i++) ans *= mat[i][i];
        return abs(ans);
      }
    };
    
    int main() {
      srand(1);
      matrix T;
      // T.random(2);
      T.initSquare();
      T.print();
      double ans = T.gauss();
      T.print();
      cout << ans << endl;
    }
    ```

## Example problems

???+ note "Example problem 1: [「HEOI2015」Little Z's room](https://loj.ac/problem/2122)"
    **Solution** A bare problem of the matrix-tree theorem. Treat each empty room as a node, build the graph according to the input information, obtain the Laplace matrix, then arbitrarily delete the $i$-th row and $i$-th column of $L$, and find the determinant of this minor. The method for finding the determinant is to Gaussian-eliminate into an upper triangular matrix and then compute the product of the diagonal. In addition, this problem requires performing Gaussian elimination over the integer subring $\mathbb{Z}_k$ modulo $k$, for which the Euclidean algorithm can be used.

???+ note "Example problem 2: [「FJOI2007」Wheel virus](https://www.luogu.com.cn/problem/P2144)"
    **Solution** There are many solutions to this problem; here using the matrix-tree theorem is the most direct solution. When the input is $n$, it is easy to write out its $(n+1)$-order Laplace matrix as:
    
    $$
    L_n = \begin{bmatrix}
    n&  -1&  -1&  -1&  \cdots&  -1&  -1\\
    -1&  3&  -1&  0&  \cdots&  0&  -1\\
    -1&  -1&  3&  -1&  \cdots&  0&  0\\
    -1&  0&  -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    -1&  0&  0&  0&  \cdots&  3&  -1\\
    -1&  -1&  0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n+1}
    $$
    
    Just find the determinant of its $n$-order minor; what remains is only big-integer computation.

??? note "Example problem 2+"
    Strengthen the data of example problem 2, requiring $n\leq 100000$, but the answer is taken modulo 1000007. (Solving this problem requires some linear algebra knowledge.)
    
    **Solution** After deriving the recurrence relation, use matrix fast exponentiation to solve.
    
    The process of deriving the recurrence relation:
    
    Note that the matrix obtained after deleting the first row and first column of $L_n$ is very regular, so we are actually finding the determinant of the matrix
    
    $$
    M_n = \begin{bmatrix}
    3&  -1&  0&  \cdots&  0&  -1\\
    -1&  3&  -1&  \cdots&  0&  0\\
    0&  -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  0&  \cdots&  3&  -1\\
    -1&  0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n}
    $$
    
    Expanding the determinant of $M_n$ along the first column, we get
    
    $$
    \det M_n = 3\det \begin{bmatrix}
    3&  -1&  \cdots&  0&  0\\
    -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  \cdots&  3&  -1\\
    0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n-1} + \det\begin{bmatrix}
    -1&  0&  \cdots&  0&  -1\\
    -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  \cdots&  3&  -1\\
    0&  0&  \cdots&  -1&  3\\
    \end{bmatrix}_{n-1} + (-1)^n \det\begin{bmatrix}
    -1&  0&  \cdots&  0&  -1\\
    3&  -1&  \cdots&  0&  0\\
    -1&  3&  \cdots&  0&  0\\
    \vdots&  \vdots&  \ddots&  \vdots&  \vdots\\
    0&  0&  \cdots&  3&  -1\\
    \end{bmatrix}_{n-1}
    $$
    
    Denote the determinants of the above three matrices as $d_{n-1}, a_{n-1}, b_{n-1}$.  
    Note that $d_n$ is a tridiagonal determinant; using a similar expansion method, we can obtain that $d_n$ has the recurrence formula $d_n=3d_{n-1}-d_{n-2}$. Similarly, using the expansion method, we can obtain $a_{n-1}=-d_{n-2}-1$, and $(-1)^n b_{n-1}=-d_{n-2}-1$.  
    Substituting these recurrence formulas into the above equation, we get:
    
    $$
    \det M_n = 3d_{n-1}-2d_{n-2}-2
    $$
    
    $$
    d_n = 3d_{n-1}-d_{n-2}
    $$
    
    So we conjecture that $\det M_n$ is also a non-homogeneous second-order linear recurrence. Using the method of undetermined coefficients, we can obtain the final recurrence formula as
    
    $$
    \det M_n = 3\det M_{n-1} - \det M_{n-2} + 2
    $$
    
    After rewriting it as $(\det M_n+2) = 3(\det M_{n-1}+2) - (\det M_{n-2} + 2)$, use matrix fast exponentiation to find the answer.

???+ note "Example problem 3: [「BZOJ3659」WHICH DREAMED IT](https://hydro.ac/p/bzoj-P3659)"
    **Solution** This problem is a direct application of the BEST theorem, but note that since the problem stipulates that "two ways of completing the task are considered different if and only if the order of using keys is different", for each Euler circuit, room number 1 can start along any out-edge, so the answer must also be multiplied by the out-degree of room number 1.

???+ note "Example problem 4: [「Joint Provincial Selection 2020 A」Homework problem](https://loj.ac/p/3304)"
    **Solution** First, we need to use Möbius inversion to transform it into computing the sum of edge weights of all spanning trees; because it is not much related to this article, it is omitted.
    
    Write the terms of the determinant as $w_ix+1$; the final answer is the coefficient of the linear term of the determinant, because the answer is actually the number of spanning trees after fixing an edge $\times$ the sum of the edge weights of this edge, so the edge multiplied by the linear-term coefficient is the fixed edge. At this time we can ignore the terms higher than linear, with complexity $O(n^3)$.
    
    [「Beijing Provincial Selection Training 2019」Counting spanning trees](https://www.luogu.com.cn/problem/P5296) is a more general case: compute the sum of the $k$-th powers of the weights of spanning trees; just use a similar method to construct the terms of the determinant, see the Luogu problem solution for details.

???+ note "Example problem 5: [AGC051D C4](https://atcoder.jp/contests/agc051/tasks/agc051_d)"
    **Solution** Counting Euler circuits of an undirected graph is an NPC problem, but the graph in this problem is relatively simple; after determining how many of the $S-T$ edges point from $S$ to $T$, we can determine the orientation scheme of the other three edges, and then directly apply the BEST theorem to obtain an $O(a+b+c+d)$ approach.
