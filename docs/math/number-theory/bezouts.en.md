Bézout's identity reveals a profound connection between the greatest common divisor and integer linear combinations, and is one of the most basic and important conclusions in number theory. Based on it, this article further discusses methods for solving linear Diophantine equations.

## Bézout's identity

**Bézout's lemma**, also called Bézout's theorem, or Bézout's identity, gives a necessary and sufficient condition for an integer to be expressible as an integer-coefficient linear combination of two integers.

???+ note "Bézout's identity"
    Let $a,b$ be integers not both zero. Then, for any integers $x,y$, $\gcd(a,b)\mid ax+by$ holds; moreover, there exist integers $x,y$ such that $ax+by=\gcd(a,b)$ holds.

??? note "Proof"
    Denote $d=\gcd(a,b)$. Because $d\mid a,b$, there exist integers $u,v$ such that $a=du,~b=dv$ hold. Therefore,
    
    $$
    ax + by = d(ux+vy).
    $$
    
    This shows $d\mid ax+by$.
    
    Conversely, we need to show there exist $x,y$ such that the equation holds. If one of $a,b$ is $0$, without loss of generality suppose $b=0$; then their greatest common divisor is $d=a$, and obviously $(x,y)=(1,0)$ makes the equation hold. Next, consider the case where both $a,b$ are nonzero. Since $\gcd(a,b)=\gcd(-a,b)=\gcd(a,-b)$, we may assume $a,b$ are both positive.
    
    Consider the process of the Euclidean algorithm:
    
    $$
    \begin{aligned}
    a   &= q_1b   + r_1, && 0\le r_1 < b,\\
    b   &= q_2r_1 + r_2, && 0\le r_2 < r_1,\\
    r_1 &= q_3r_2 + r_3, && 0\le r_3 < r_2,\\
        & \cdots \\
    r_{n-3} &= q_{n-1}r_{n-2} + r_{n-1}, && 0\le r_{n-1} < r_{n-2},\\
    r_{n-2} &= q_nr_{n-1} + r_n,         && 0\le r_n     < r_{n-1},\\
    r_{n-1} &= q_{n+1}r_n.
    \end{aligned}
    $$
    
    Since the greatest common divisor is $d$, at the last step of the Euclidean algorithm there must be $r_n=d$. So the second-to-last equation can be written as
    
    $$
    d = r_n = r_{n-2} - q_nr_{n-1}.
    $$
    
    Solving from the third-to-last equation for
    
    $$
    r_{n-1} = r_{n-3} - q_{n-1}r_{n-2}
    $$
    
    and substituting it into the above, one can eliminate $r_{n-1}$:
    
    $$
    \begin{aligned}
    d &= r_{n-2} - q_n(r_{n-3} - q_{n-1}r_{n-2}) \\
    &= (1 + q_nq_{n-1})r_{n-2} - q_nr_{n-3}.
    \end{aligned}
    $$
    
    Similarly, one can step by step eliminate all of $r_{n-2},r_{n-3},\cdots,r_2,r_1$, and finally obtain
    
    $$
    d = xa + yb.
    $$
    
    This proves that there exist $x,y$ such that $ax+by=d$ holds. By the earlier analysis, this also proves the original proposition.

Here, the proof of existence is constructive, and it simultaneously gives a method for computing these coefficients. This computation method is the [extended Euclidean algorithm](./gcd.md#extended-euclidean-algorithm).

Considering the special case of Bézout's identity when $\gcd(a,b)=1$, one obtains the following corollary:

???+ note "Corollary"
    Integers $a,b$ are coprime if and only if there exist integers $x,y$ such that $ax+by=1$ holds.

### The case of multiple integers

Bézout's identity can be generalized to the case of multiple integers.

???+ note "Theorem"
    Let $a_1,a_2,\cdots,a_n$ be integers not all zero. Then, for any integers $x_1,x_2,\cdots,x_n$, $\gcd(a_1,a_2,\cdots,a_n)\mid a_1x_1+a_2x_2+\cdots+a_nx_n$ holds; moreover, there exist integers $x_1,x_2,\cdots,x_n$ such that $\gcd(a_1,a_2,\cdots,a_n)=a_1x_1+a_2x_2+\cdots+a_nx_n$ holds.

??? note "Proof"
    Using the fact that $\gcd(a_1,a_2,\cdots,a_n)=\gcd(\gcd(a_1,a_2,\cdots,a_{n-1}),a_n)$, induction on $n$ suffices.

### Example problem

???+ example "[Codeforces 510 D. Fox And Jumping](https://codeforces.com/problemset/problem/510/D)"
    Given $n\le 300$ cards, each with $l_i$ and $c_i$. On an infinitely long tape, you can choose to spend $c_i$ money to buy card $i$, after which you can jump left or right by $l_i$ units any number of times. Ask at least how much money you need to spend to be able to jump to all positions on the tape. If impossible, output $-1$.

??? note "Solution"
    Analyzing this problem, we find that to jump to every cell, the chosen numbers $l_{i_1}, \cdots, l_{i_k}$ must yield an absolute value of $1$ through several additions or subtractions. That is, there exist integers $x_1, \cdots, x_k$ such that $l_{i_1} x_1 + \cdots + l_{i_k} x_k = 1$. By Bézout's identity for multiple integers, this is equivalent to choosing several numbers from the array $l_1, \cdots, l_n$ such that their greatest common divisor is $1$, while requiring the sum of costs to be minimum.
    
    **Method 1**: Regard the minimum sum of costs as a shortest-path problem, which can be solved with Dijkstra's algorithm. The vertices of the graph store the current value of the greatest common divisor. The start of the graph is $0$, and the target to reach is $1$. Each step, starting from the current vertex $x$, walk along an edge of length $c_i$ to the vertex $\gcd(x,l_i)$. The time complexity of this algorithm is $O(n^2\log n)$.
    
    **Method 2**: Choosing several numbers from the array $l_1, \cdots, l_n$ such that their greatest common divisor is $1$ and the sum of costs is minimum, from which one can think of the 0-1 knapsack problem.
    
    Let $f_{i, j}$ denote the minimum cost of considering the first $i$ numbers with greatest common divisor $j$; then we have the transition equation:
    
    $$
    f_{i, j} = \min_{\gcd(k, l_i) = j} f_{i - 1, k} + c_i.
    $$
    
    After the DP, the final total cost is $f_{n, 1}$.
    
    As with the general 0-1 knapsack problem, one can use a rolling array to optimize, removing the first dimension. And here the greatest common divisors $j$ that 300 numbers can form are very sparse, so a hash table can be used to store them.
    
    In fact, the graph built by Method 1 here is precisely the state transition graph of the dynamic programming in Method 2; Method 2 amounts to using dynamic programming to find the shortest path of a directed acyclic graph, so Method 1 and Method 2 are equivalent. But Method 2 does not need to store the whole graph, and the time complexity of the DP is $O(n + m)$, lower than Dijkstra's algorithm, so Method 2 is better in both time and space.

## Linear Diophantine equations

A **linear Diophantine equation** is a Diophantine equation of the form

$$
a_1x_1 + a_2x_2 + \cdots + a_nx_n = b
$$

where $a_1,a_2,\cdots,a_n$ are all integers. The goal of this section is to find all its integer solutions.

### The case of two variables

First consider the binary linear Diophantine equation:

$$
a_1x_1 + a_2x_2 = b.
$$

Bézout's identity states that this equation has a solution if and only if

$$
d = \gcd(a_1,a_2) \mid b.
$$

Next, assume this condition holds. Using the extended Euclidean algorithm one can find an integer solution $(x_1^*,x_2^*)$ of the equation $a_1x_1 + a_2x_2 = d$. From this, one can obtain a particular solution of the original equation

$$
(x_1^\circ,x_2^\circ) = \left(\frac{b}{d}x_1^*,\frac{b}{d}x_2^*\right).
$$

To obtain all solutions, one can consider subtracting the identity $a_1x_1^\circ+a_2x_2^\circ = b$ from the original equation, giving

$$
a_1(x_1 - x_1^\circ) + a_2(x_2 - x_2^\circ) = 0.
$$

This is a homogeneous linear Diophantine equation in $(x_1-x_1^\circ,x_2-x_2^\circ)$, which has the general solution

$$
(x_1-x_1^\circ,x_2-x_2^\circ) = \left(t\dfrac{a_2}{d},-t\dfrac{a_1}{d}\right).\quad(t\in\mathbf Z)
$$

Therefore, the general solution of the original equation is

$$
(x_1,x_2) = \left(x_1^\circ + t\dfrac{a_2}{d},x_2^\circ - t\dfrac{a_1}{d}\right).\quad(t\in\mathbf Z)
$$

This is a series of equally spaced integer points on the line $a_1x_1+a_2x_2 = b$.

### The case of multiple variables

Having solved the binary case, the multivariate case is also easy to solve. For the $n$-variable linear Diophantine equation

$$
a_1x_1 + a_2x_2 + \cdots + a_nx_n = b,\quad (n>3)
$$

by Bézout's identity, the equation has a solution if and only if

$$
\gcd(a_1,a_2,\cdots,a_n) \mid b.
$$

Similar to the binary case, the general solution of the multivariate linear Diophantine equation can likewise be written in the form

$$
(x_1^\circ,x_2^\circ,\cdots,x_n^\circ) + \sum_{k=1}^{n-1} t_k(x_1^{(k)},x_2^{(k)},\cdots,x_n^{(k)})
$$

where $x^\circ$ is a particular solution, and $x^{(k)}$ are the $(n-1)$ solutions of the corresponding homogeneous equation.

To find the specific form of the general solution, one can do so by transforming the $n$-variable equation into an $(n-1)$-variable equation. Let $d_1 = \gcd(a_1,a_2)$; then, by Bézout's identity, the set of all $a_1x_1+a_2x_2$ is exactly all multiples of $d_1$. Therefore, one can first solve the $(n-1)$-variable linear Diophantine equation:

$$
d_1y_1 + a_3x_3 + a_4x_4 + \cdots + a_nx_n = b.
$$

Let its general solution be

$$
\begin{aligned}
y_1 &= y_1^\circ + \sum_{k=2}^{n-1}t_ky_1^{(k)}, \\
x_i &= x_i^\circ + \sum_{k=2}^{n-1}t_kx_i^{(k)},\quad i=3,\cdots,n.
\end{aligned}
$$

Let a particular solution of $a_1x_1+a_2x_2=d_1$ be $(x_1^*,x_2^*)$; then, by the discussion of the previous section, the general solution of the binary linear Diophantine equation $a_1x_1+a_2x_2=d_1y_1$ in $x_1,x_2$ is

$$
x_1 = x_1^*y_1 + t_1\dfrac{a_2}{d_1},~x_2 = x_2^*y_1 - t_1\dfrac{a_1}{d_1}.
$$

Substituting the expression for $y_1$, one obtains the general solution of the original equation

$$
\begin{aligned}
x_1 &= x_1^*y_1^\circ + t_1\dfrac{a_2}{d_1} + \sum_{k=2}^{n-1}t_kx_1^*y_1^{(k)}, \\
x_2 &= x_2^*y_1^\circ - t_1\dfrac{a_1}{d_1} + \sum_{k=2}^{n-1}t_kx_2^*y_1^{(k)}, \\
x_i &= x_i^\circ + \sum_{k=2}^{n-1}t_kx_i^{(k)},\quad i=3,\cdots,n.
\end{aligned}
$$

## Frobenius coin problem

Bézout's identity gives a necessary and sufficient condition for an integer to be linearly represented by several integers. Closely related to this is the **Frobenius coin problem**:

-   If there are coins of several integer denominations $a_1,a_2,\cdots,a_n$ and $\gcd(a_1,a_2,\cdots,a_n)=1$, then what is the largest integer that cannot be composed from these coins?

This likewise examines when an integer $k$ can be represented in the form $a_1x_1+a_2x_2+\cdots+a_nx_n$; in Bézout's identity $x_i$ can be any integer, while in the Frobenius coin problem $x_i$ can only be a natural number.

The case of only one kind of coin is trivial, because one can only have $a_1=1$, and all natural numbers can be represented by it. And the case $n>2$ is too complex, so this section only discusses the case $n=2$.

### Sylvester's theorem

In 1882, Sylvester completely solved the Frobenius coin problem for $n = 2$:

???+ note "Theorem (Sylvester)"
    For coprime positive integers $a_1,a_2$, the largest integer that cannot be written as $a_1x_1+a_2x_2~(x_1,x_2\in\mathbf N)$ is $C = a_1a_2 - a_1 - a_2$. Moreover, for all $k\in\mathbf Z$, exactly one of the integers $k$ and $C-k$ can be written in this form.

For convenience of exposition, an integer that can be written in the form $a_1x_1+a_2x_2~(x_1,x_2\in\mathbf N)$ is called **representable**.

??? note "Proof 1"
    Since $a_1,a_2$ are coprime, for any integer $k$, the equation $a_1x_1+a_2x_2=k$ must have a solution, with general solution
    
    $$
    (x_1,x_2) = (x_1^\circ + ta_2, x_2^\circ - ta_1).\quad(t\in\mathbf Z)
    $$
    
    Take $t$ to be the quotient obtained by dividing $x_2^\circ$ by $a_1$ with remainder; then the remainder $x_2 = x_2^\circ-ta_1$ lies between $0$ and $a_1-1$. Consider the solution $(x_1,x_2)$ obtained in this case. Because $x_2$ is the smallest non-negative integer value it can take, $n$ is representable if and only if $x_1\ge 0$.
    
    **Step 1**: Prove that all integers greater than $C$ are representable.
    
    When $k > C$,
    
    $$
    a_1x_1 = k - a_2x_2 > C - a_2(a_1-1) = -a_1.
    $$
    
    So $x_1 > -1$, that is, $x_1\ge 0$. This shows that $(x_1,x_2)$ is a natural-number solution. In this case, $k$ can be written in the required form.
    
    **Step 2**: Prove that $C$ is not representable. Furthermore, $C$ is the largest non-representable integer, and $k$ and $C-k$ are not both representable.
    
    Proof by contradiction. Suppose $C$ is representable, i.e. there exist $x_1,x_2\in\mathbf N$ such that $a_1x_1+a_2x_2=C$ holds. Substituting the expression for $C$,
    
    $$
    a_1a_2 = a_1(x_1+1) + a_2(x_2+1).
    $$
    
    Therefore, $a_2\mid (x_1+1)$ and $a_1\mid (x_2+1)$. And because $x_1+1,x_2+1$ are both positive,
    
    $$
    a_1a_2 \ge a_1a_2 + a_2a_1 = 2a_1a_2.
    $$
    
    Contradiction. This shows that $C$ is not representable. Combined with Step 1, it is the largest non-representable integer.
    
    If both $k$ and $C-k$ are representable, then adding the coefficients in the representations of $k$ and $C-k$ gives the coefficients in a representation of $C$, contradicting that $C$ is not representable, so at most one of $k$ and $C-k$ is representable.
    
    **Step 3**: Prove that if $k$ is not representable, then $C-k$ must be representable.
    
    Let $(x_1,x_2)$ be the integer solution of the equation $a_1x_1+a_2x_2=k$ set up earlier. Then, as explained earlier, $k$ being not representable is equivalent to $x_1<0$. Therefore,
    
    $$
    C - k = a_1a_2 - a_1 - a_2 - a_1x_1 - a_2x_2 = a_1(-1-x_1) + a_2(a_1-1-x_2).
    $$
    
    where $-1-x_1$ and $a_1-1-x_2$ are both non-negative integers, so $C-k$ is representable.

??? note "Proof 2"
    Here we only prove that $C=a_1a_2-a_1-a_2$ is the largest non-representable natural number; the proof of the rest is similar to Proof 1.
    
    Consider, modulo $a_2$, the smallest representable natural number in each residue system. Because different natural numbers in the same residue system can be converted into one another by adding or subtracting several $a_2$s, when discussing the smallest representable number, one only needs to consider the possibility of adding or subtracting $a_1$. Since $a_1$ and $a_2$ are coprime, the smallest representable natural number in each residue system is exactly a multiple of $a_1$
    
    $$
    0,~a_1,~2a_1,~\cdots,~(a_2-1)a_1.
    $$
    
    Therefore, the largest non-representable number is
    
    $$
    \max_{0\le i < a_2} ia_1 - a_2 = (a_2-1)a_1 - a_2 = C.
    $$

### Geometric meaning

Regard the equation $a_1x_1 + a_2x_2 = k$ as a line. Then $k$ is representable if and only if this line passes through an integer point in the first quadrant (including the coordinate axes). When $k < ab$, this line can pass through at most one integer point in the first quadrant. Therefore, for $0\le k < ab$, the integer $k$ is representable if and only if $k$ passes through exactly one integer point in the first quadrant.

Therefore, the number of representable natural numbers less than or equal to $k < ab$ is exactly equal to the number of integer points under the line $a_1x_1 + a_2x_2 = k$ in the first quadrant (including the points on the boundary). This number equals

$$
\sum_{i=0}^{\lfloor k / a_1 \rfloor} \left\lfloor\dfrac{k-ia_1}{a_2}\right\rfloor.
$$

This is the classic problem of integer points under a line, which can be solved with the [Euclidean-like algorithm](./euclidean.md#euclidean-like-algorithm) in $O(\log\min\{a_1,a_2,k\})$ time.

### Exercises

-   [Luogu P3951 NOIP2017 提高组 小凯的疑惑/蓝桥杯 2013 省 买不到的数目](https://www.luogu.com.cn/problem/P3951)
