This page introduces the random walk problem on graphs. It mainly explores from three angles: grid graphs, sparse graphs, and general graphs, introduces various methods for solving this kind of problem, and compares their advantages and disadvantages when solving various problems.

## Definition

Given a directed simple graph $G=(V, E)(V=\{v_1, v_2, \cdots, v_{|V|}\})$, a start point $s \in V$, and an end point $t \in V$, each edge $e=\left(x, y\right)$ has a positive weight $w_e$ satisfying that for all $x \in V \backslash\left\{t\right\}$, $\sum_{\left(x, y\right) \in E} w_{\left(x, y\right)}=1$, and for any point $x$ there exists a path from $x$ to $t$. There is a piece starting from the start point; each second, from the current point $x$, it chooses the out-edge $\left(x, y\right)$ with probability $w_{(x, y)}$ and walks to $y$; when it reaches the end point it stops; find the expected time spent.

In fact, this problem can also be written in matrix form. Define the matrix $P$:

$$
P_{x, y}=
\begin{cases}
w_{(x, y)} & \text{if } (x, y) \in E \text{ and } x \neq t \\
0 & \text{if } (x, y) \notin E \text{ or } x=t \\
\end{cases}
$$

The answer to find is:

$$
\sum_{k \geq 0} k \times\left(P^k\right)_{s, t}
$$

where $\left(P^k\right)_{s, t}$ denotes the probability of reaching the end point for the first time after walking $k$ steps. When the graph is finite and all points can reach the end point, by the definition of $P$ it can be proved that its eigenvalues are all less than 1, so the answer must converge.

For convenience of description, in this page, unless otherwise specified, $n$ refers to $|V|$ and $m$ refers to $|E|$.

In addition, in this page, a sparse graph refers to a graph where the number of edges and the number of points are of the same order.

## Grid graph

???+ note "Example problem 1 [Circles of Waiting](https://codeforces.com/problemset/problem/963/E)"
    A piece is initially placed at the point $(0,0)$ of the Cartesian coordinate plane. Each second the piece moves randomly. Suppose it is currently at $(x, y)$; the next second it has probability $p_1$ of moving to $(x-1, y)$, probability $p_2$ of moving to $(x, y-1)$, probability $p_3$ of moving to $(x+1, y)$, and probability $p_4$ of moving to $(x, y+1)$. It is guaranteed that $p_1+p_2+p_3+p_4=1$.
    Find the expected time it takes for it to move to a position whose Euclidean distance from the origin is greater than $R$. $0 \leq R \leq 50$, $p_1, p_2, p_3, p_4>0$, and the answer is taken modulo $10^9+7$.

### Naive approach

Denote $f(i, j)$ as the expected time for the piece at $(i, j)$ to move to a position whose Euclidean distance from the origin is greater than $R$; the transition equation is:

$$
f(i, j)=
\begin{cases}
p_1 f(i-1, j) + p_2 f(i, j-1) + p_3 f(i+1, j) + p_4 f(i, j+1) + 1 & i^2 + j^2 \leq R^2 \\
0 & i^2 + j^2 > R^2
\end{cases}
$$

Since the transitions have no topological order, Gaussian elimination is needed to solve. The time complexity is $O\left(R^6\right)$, which cannot pass this problem.

### Direct elimination method

Note that the coefficients of the equations to be eliminated are mostly 0; when eliminating, only computing the positions with nonzero values can reduce the complexity.

Consider the elimination process; eliminate the equations in the order of top to bottom in the coordinate system, and left to right within the same layer; color the already-eliminated equations yellow, color the points adjacent to yellow points green, and color the remaining points black, as shown in the figure below:

![graph-random-walk-1](images/graph-random-walk-1.svg)

Next we eliminate the equation corresponding to the next green cell. In this equation, only the variable coefficients corresponding to the green cell and the first black cell below it may be nonzero; and only in the equations corresponding to the green cell and the first black cell below it may the variable coefficient corresponding to the current cell be nonzero.

Note that there are only $O(R)$ green cells, so the time complexity of eliminating a single equation is $O\left(R^2\right)$. There are only $O\left(R^2\right)$ equations in total, so the time complexity is reduced to $O\left(R^4\right)$, which can pass this problem.

### Pivot method

There are $O\left(R^2\right)$ equations and variables; if we can reduce the scale to $O(R)$, then naive Gaussian elimination can pass.

Set the variable corresponding to the first cell from left to right in each row as a pivot, $2 R+1$ in total, and try to express the variables corresponding to the other cells as linear functions of these pivots. Consider column by column from left to right; for each cell $(i, j)$ in the current column, note that $f(i, j), f(i-1, j), f(i, j-1), f(i, j+1)$ are all known linear functions of the pivots; rearranging the transition equation, we have:

$$
f(i+1, j)=\frac{f(i, j)-p_1 f(i-1, j)-p_2 f(i, j-1)-p_4 f(i, j+1)-1}{p_3}
$$

In this way we can obtain the linear-function representation of $f(i+1, j)$ in terms of the pivots. If $(i+1, j)$ already has a Euclidean distance from the origin exceeding $R$, then we can obtain an equation: $f(i+1, j)=0$. In the end, we will obtain $2 R+1$ equations, and just perform Gaussian elimination on these equations.

In the stage of recurring the linear functions of the pivots, there are $O\left(R^2\right)$ variables in total, and recurring a single variable costs $O(R)$ time; after that, the scale of the problem is reduced to $O(R)$. The time complexity of both parts is $O\left(R^3\right)$, and the total time complexity is also $O\left(R^3\right)$, which can pass this problem.

### Comparison of the two approaches

Below we compare the two approaches from various aspects:

In terms of time complexity, the worst-case time complexity of the pivot method on a grid graph is $O(n \sqrt{n})$ (the time complexity is highest when the length and width of the grid graph are both on the order of $O(\sqrt{n})$), and the worst-case time complexity of the direct elimination method on a grid graph is $O\left(n^2\right)$; the pivot method is better.

In terms of precision, for some problems that need to perform real-number computation rather than modulo, the precision of the direct elimination method is better than the pivot method.

In terms of applicability, the two approaches apply to different aspects.

When there are obstacles in the grid graph or the probability of walking some edges is $0$, for each obstacle or edge with probability $0$, the pivot method needs to add a pivot; when the number of obstacles or edges with probability $0$ is more than $O(R)$, the time complexity of the pivot method increases, while the time complexity of the direct elimination method still remains unchanged.

But the pivot method can also do elimination of transition equations similar to grid graphs, for example $f(i, j)=p_1 f(i+1, j)+p_2 f(i, j+1)+p_3 f(\operatorname{pre}(i, j))+1$, where $\operatorname{pre}(i, j)=(x, y)(x \leq i, y \leq j)$ is a value given by the problem, and the complexity analysis of the direct elimination method does not apply in this model.

In addition, the computation of the determinant of the adjacency matrix of a grid graph also cannot use the pivot method, and can only use the direct elimination method to optimize the time complexity.

In summary, the two approaches each have their strengths, and different approaches need to be adopted according to the specific problem analysis.

## Sparse graph

???+ note "Example problem 2 Expected Value"
    Given a simple undirected connected sparse graph $G=(V, E)$, a piece is initially placed at $v_1$; each second the piece chooses an edge with equal probability from the edges connected to the current point and walks to the point the out-edge points to; find the expected time to reach $v_n$. $n \leq 2000$, and the answer is taken modulo $p$, where $p$ is a prime randomly generated in the interval $\left[10^9, 1.01 \times 10^9\right]$.

### Basic knowledge

**Definition 4.1.** All polynomials $p(λ)$ satisfying $p(A) = 0$ are called annihilating polynomials of the matrix $A$.

**Definition 4.2.** Denote $I_n$ as the $n$-order identity matrix, and define the characteristic polynomial of an $n × n$ matrix $A$ as $p(λ) = \det(λI_n - A)$, where $\det$ denotes the determinant of a matrix.
It is not hard to find that the degree of the characteristic polynomial of an $n$-order matrix $A$ does not exceed $n$.

**Theorem 4.2.** (Cayley–Hamilton theorem) The characteristic polynomial of any matrix is its annihilating polynomial.

So, the degree of the minimum-degree annihilating polynomial of an $n$-order matrix also does not exceed $n$.

### Solving the original problem

Note that the expected walking time $E(t)=\sum_{i\geq0}\Pr[t>i]$; if we can find the probability of not having ended after walking $i$ steps, summing over all $i ≥ 0$ gives the answer.

Denote $f(i, j)$ as the probability of having walked $i$ steps, currently staying at $j$, and not having walked to $n$; then:

$$
f(i,j)=\sum_{(k,j)\in E}\frac{f(i-1,k)}{\deg_k}(j\neq n)
$$

where $\deg_k$ denotes the degree of $k$.

Note that the transition of $f$ is independent of $i$; we can consider that one transition is multiplication by a matrix, i.e. $f{i+1}=f_iM$. Since the degree of the minimum annihilating polynomial of $M$ does not exceed $n$, the length of the shortest recurrence of $f$ also does not exceed $n$, so the length of the shortest recurrence of $\Pr[t>i]=\sum_{j=1}^{n-1}f(i,j)$ also does not exceed $n$. We can find $\Pr[t>0],\Pr[t>1],\cdots,\Pr[t>3n]$ in $O(nm)$ time, and then use the *Berlekamp–Massey* algorithm to find the shortest recurrence of $\Pr[t > i]$ in $O(n^2)$ time.

Consider finding the generating function of a $k$-order linear recurrence sequence $a$. We may as well assume $a_i=\sum_{j=1}^kc_ja_{i-j}$ when $i ≥ i_0$; denote the generating functions of $a$ and $c$ as $A(x)$ and $C(x)$; then $A(x)=A(x)C(x)+A_0(x)$, where $A_0(x)$ is determined by the terms with $i < i_0$.

Back to the original problem, since we can find the shortest recurrence of $\Pr[t > i]$, we can find $C(x)$ and $A_0(x)$ (defined the same as the previous paragraph), and rearranging we get $A(x)=\frac{A_0(x)}{1-C(x)}$. What we want is $\sum_{i\geq0}[x^i]A(x)$; it is not hard to find that this value equals $A(1)$, so just substitute $x = 1$ to solve the original problem. Since the modulus is a random prime, we can consider that the denominator will not be $0$.

In this way, we solve this problem in $O(nm+n^2)$ time complexity. If the number of points and the number of edges of graph $G$ are of the same order, the time complexity in this problem can be considered as $O(n^2)$.

## General graph

???+ note "Example problem 3 Frank"
    Given a simple strongly connected directed graph $G = (V, E)$, for all $1 ≤ s ≤ n$, $1 ≤ t ≤ n$, $s ≠ t$, answer the following question:
    A piece is initially placed at $v_s$; each second the piece chooses an edge with equal probability from the out-edges of the current point and walks to the point the out-edge points to; find the expected time to reach $v_t$. $3 ≤ n ≤ 400$.

### Analysis and transformation

Denote $p_{i, j}$ as the probability that the piece at $i$ chooses the out-edge $(i, j)$ to walk to $j$; in particular, when the out-edge does not exist the probability is $0$. Denote $f_{i,j}$ as the expected time for $i$ to random-walk to $j$; in particular, $f_{i,i} = 0$. When $i ≠ j$, the transition equation is:

$$
f_{i,j}=1+\sum_{1\leq k\leq n}p_{i,k}f_{k,j}
$$

When $i = j$, denote $g_i$ as the expected time to first return to $i$ starting a random walk from $i$; then:

$$
f_{i,i}=1-g_i+\sum_{1\le k\le n}p_{i,k}f_{k,i}
$$

For convenience of observation, we write the transition equation in matrix form. Denote $P$ as the transition matrix of this graph, $F$ as the answer matrix, $I$ as the $n$-order identity matrix, $J$ as the $n$-order all-$1$ matrix, and $G$ as an $n$-order matrix satisfying $G_{i,i} = g_i$ with other positions being $0$; then:

$$
F=J-G+PF
$$

If we can find $G$, then we only need to solve the equation:

$$
(I − P)F = J − G
$$

### Method for finding G

**Definition 5.1.** Define the steady-state distribution of an $n$-order transition matrix $P$ as an $n$-dimensional vector $π$ satisfying $\sum_{i=1}^{n}\pi_{i}=1$, $πP = π$. Here, the value of each dimension of $π$ is in the interval $[0,1]$.

We can easily find the practical meaning of the steady-state distribution. If at some moment the piece has probability $π_i$ of staying at $v_i$, then at any subsequent moment, the piece still satisfies this probability distribution. We can find $π$ by solving equations through Gaussian elimination in $O(n^3)$ time; so what is the relationship between $π$ and $G$?

**Theorem 5.1.** For any $1 ≤ i ≤ n$, $π_ig_i = 1$.

???+ note "Proof"
    From $F = J - G + PF$, rearranging:
    
    $$
    G = PF + J − F
    $$
    
    Multiplying $π$ on the left of both sides:
    
    $$
    πG = πPF + πJ − πF
    $$
    
    By the definition of $π$, $πP = π$, so:
    
    $$
    πG = πJ
    $$
    
    So:
    
    $$
    \pi_ig_i=\sum_{j=1}^n\pi_j=1  
    $$

The original proposition is proved.

So, by introducing the steady-state distribution, we can find $G$ in $O(n^3)$ time.

### Solving the original problem

In the process of solving the equation, we find a problem: $(I - P)$ is not full rank, and cannot be solved by the method of multiplying by the inverse matrix.

**Definition 5.2.** Define an arborescence of a directed graph $G = (V,E)$ rooted at $r\in V$ as a subgraph $T = (V,A)$ of $G$ satisfying:

1.  For any $i ≠ r$, the out-degree of $i$ is $1$.
2.  The out-degree of $r$ is $0$.
3.  There is no cycle in $T$.

**Lemma 5.1.** (Matrix-tree theorem on directed graphs) For a directed graph $G$, denote $D$ as its out-degree matrix, i.e. $D_{i,i} = d_i$, $D_{i,j} = 0(i ≠ j)$, where $d_i$ denotes the out-degree of $i$, and denote $A$ as its adjacency matrix; then the number of arborescences rooted at $r$ is the determinant of $D - A$ after removing row $r$ and column $r$.

**Theorem 5.2.** For the transition matrix $P$ of a strongly connected graph $G = (V,E)$, the rank of $(I - P)$ is $n - 1$.

???+ note "Proof"
    Because multiplying a row of a matrix by a nonzero constant does not change its rank, we multiply row $i$ of $(I - P)$ by the out-degree of $v_i$ to get a new matrix $L$; we only need to prove that the rank of $L$ is $n - 1$.  
    Since the sum of each row of $L$ is $0$, summing all the column vectors of $L$ gives the zero vector, i.e. these vectors are linearly dependent, so the rank of $L$ is not $n$.  
    It is not hard to find that $L$ equals the out-degree matrix of graph $G$ minus its adjacency matrix; by Lemma 5.1, the determinant of $L$ after removing row $i$ and column $i$ denotes the number of arborescences rooted at $v_i$.  
    Since G is strongly connected, the number of arborescences rooted at any point is not $0$, i.e. $L$ is still full rank after removing row $i$ and column $i$.  
    Because adding a column does not decrease the rank, all row vectors of $L$ after removing row $i$ are linearly independent. So the rank of $L$ is $n - 1$.  
    Back to the original problem, consider solving the equation in the original problem. For convenience, we write the equation in the form $AX = B$, where $A$, $B$ are known and $X$ needs to be solved. Since $A$ is not full rank, there are infinitely many solutions; we first find a particular solution.  
    Do Gaussian elimination on $A$ and $B$ together. Eliminate the first $n - 1$ rows of $A$ into the form where only the main diagonal and column $n$ have values, and eliminate the last row into all $0$, i.e. the following form:
    
    $$
    \begin{bmatrix}
    1 & 0 & 0 & \cdots & 0 & a_1 \\0&1&0&\cdots&0&a_2\\0&0&1&\cdots&0&a_3\\
    \vdots&\vdots&\vdots&\ddots&\vdots&\vdots
    \\0&0&0&\cdots&1&a_{n-1}\\0&0&0&\cdots&0&0
    \end{bmatrix}
    X=
    \begin{bmatrix}
    b_{1,1}&b_{1,2}&b_{1,3}&\cdots&b_{1,n-1}&b_{1,n}
    \\b_{2,1}&b_{2,2}&b_{2,3}&\cdots&b_{2,n-1}&b_{2,n}
    \\b_{3,1}&b_{3,2}&b_{3,3}&\cdots&b_{3,n-1}&b_{3,n}
    \\\vdots&\vdots&\vdots&\ddots&\vdots&\vdots
    \\b_{n-1,1}&b_{n-1,2}&b_{n-1,3}&\cdots&b_{n-1,n-1}&b_{n-1,n}
    \\0&0&0&\cdots&0&0
    \end{bmatrix}
    $$
    
    Let $X_{n,i} = 0$, and we can solve a particular solution, denoted as $Y$. Next adjust the particular solution to the true solution.  
    Note that $X_{n,i} = 0$; considering the combinatorial meaning, $Y_{i,j} = 1 + Y_{j,j} + P_{i,k}X_{k,j}$; it is not hard to solve $X_{i,j} = Y_{i,j} - Y_{j,j}$.  
    In the end we solve this problem in $O(n^3)$ time complexity.

## Reference

1.  A brief discussion of the random walk problem on graph models. IOI2019 China National Candidate Team Papers (pp. 17-26)
