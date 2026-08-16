## Introduction

The Catalan numbers frequently appear in various counting problems. The Belgian mathematician Eugène Charles Catalan discovered this sequence in 1958 while studying the problem of counting bracket sequences, which is how it got its name. The Qing-dynasty mathematician Ming Antu had already discovered this sequence as early as the 1730s.

The Catalan numbers satisfy the following recurrence relation:

$$
C_n = \begin{cases}
1, & n = 0, \\
\sum_{i=0}^{n-1} C_{i}C_{n-1-i}, & n > 0.
\end{cases}\tag{1}
$$

The first few terms of the sequence are: ([OEIS: A000108](https://oeis.org/A000108), indexed from $0$)

$$
1,1,2,5,14,42,132,429,1430,\ldots
$$

## Applications

The recurrence relation of the Catalan number $C_n$ has a natural recursive structure: a counting problem $C_n$ of size $n$ can be split, by enumerating a dividing point, into two subproblems of sizes $i$ and $(n-1-i)$. This recurrence relation causes the Catalan numbers to appear widely in various problems with a similar recursive structure.

-   <a id="path-counting"></a>**Path counting problem**: There is a grid of size $n\times n$, with the lower-left corner at $(0, 0)$ and the upper-right corner at $(n, n)$. Starting from the lower-left corner, each step can only go right or up by one unit; the total number of paths that reach the upper-right corner without going above the diagonal $y=x$ (touching it is allowed) is $C_n$.

    ??? note "Proof"
        Let the number of ways be $T_n$. Consider the case $n \ge 2$. Suppose the point where the path **first** reaches the diagonal $y=x$ is $(k,k)~(k \in [1,n])$. Consider the paths from $(0,0)$ to $(k,k)$ whose intermediate points, excluding the start and end, **do not pass through the diagonal (cannot touch it)**.
        
        ![catalan2](./images/catalan-2.svg)
        
        As shown in the figure, the first step of these paths must go right, from $(0,0)$ to $(1,0)$; the last step must go up, from $(k,k-1)$ to $(k,k)$. Therefore, these paths are precisely the paths from $(1,0)$ to $(k,k-1)$ that do not cross the line $y=x-1$, and the number of such paths is $T_{k-1}$. At the same time, the number of valid paths from $(k,k)$ to $(n,n)$ is $T_{n-k}$. By the multiplication principle, the number of paths that first touch the diagonal at $(k,k)$ is $T_{k-1} T_{n-k}$. Enumerating all possibilities for $k$, the number of all valid paths is
        
        $$
        T_n = \sum_{k=1}^n T_{k-1}T_{n-k}.
        $$
        
        Making the substitution $k=i+1$, one can see that this is precisely the recurrence relation of the Catalan numbers. From $T_0=1$ it follows that $T_n = C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Non-crossing chord counting problem**: There are $2n$ points on a circle; the number of ways to connect these points in pairs so that the resulting $n$ segments are pairwise non-crossing is $C_n$.

    ??? note "Proof"
        Let the number of ways for $2n$ points be $T_n$. Label the $2n$ points clockwise as $1,2,\ldots,2n$. Since the chords are pairwise non-crossing, point $1$ can only connect to an even-numbered point; otherwise, the odd number of points between the two points cannot be paired up without crossing the line connecting the two points. If $1$ is connected to $2k~(k\in[1,n])$, then there are $2k-2$ points on the left and $2n-2k$ points on the right, and by the multiplication principle the number of such ways is $T_{k-1}T_{n-k}$. Therefore, enumerating $k$, we have $T_n = \sum_{k=1}^n T_{k-1} T_{n-k}$. Letting $k=i+1$ gives the recurrence relation of the Catalan numbers. From $T_0=1$ it follows that $T_n=C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   <a id="triangulation-counting"></a>**Triangulation counting problem**: The number of ways to divide a convex $(n+2)$-gon region into triangular regions with non-crossing diagonals is $C_n$.

    ??? note "Proof"
        Let the number of triangulations of an $(n+2)$-gon be $T_n$. First fix an edge $(1,n+2)$ as the base edge; it must belong to a triangle, and let the third point of this triangle be $k~(k\in[2,n+1])$. Thus, the original convex polygon becomes three parts:
        
        -   Triangle $(1,k,n+2)$.
        -   A $k$-gon, with vertices $1\sim k$.
        -   An $(n+3-k)$-gon, with vertices $k\sim (n+2)$.
        
        The latter two parts are both subproblems, so we have the recurrence relation
        
        $$
        T_n = \sum_{k=2}^{n+1} T_{k-2}T_{n+1-k}.
        $$
        
        Letting $k=i+2$ gives the recurrence relation of the Catalan numbers. From $T_0=T_1=1$ it follows that $T_n=C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Binary tree counting problem**: The number of structurally distinct binary trees with $n$ nodes is $C_n$. Equivalently, the number of structurally distinct full binary trees with $n$ non-leaf nodes is $C_{n}$.

    ??? note "Proof"
        Let the number of binary trees with $n$ nodes be $T_n$. Take any root node and enumerate the sizes of the left and right subtrees. Suppose the left subtree has size $i\in[0,n-1]$; then the right subtree has size $(n-1-i)$. Both the left and right subtrees are subproblems, so we have the recurrence relation
        
        $$
        T_n = \sum_{i=0}^{n-1}T_iT_{n-1-i}.
        $$
        
        This is the recurrence relation of the Catalan numbers. From $T_0=T_1=1$ it follows that $T_n=C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Bracket sequence counting problem**: The number of valid bracket sequences composed of $n$ pairs of brackets is $C_n$.

    ??? note "Proof"
        Relate this to the path counting problem. Regard a left bracket as going up and a right bracket as going right. A valid bracket sequence means that at any position the number of left brackets is no less than the number of right brackets. This is equivalent to the path counting problem, where at any moment the number of upward steps is no less than the number of rightward steps. Therefore, there is a bijection between valid bracket sequences and valid paths. The number of valid bracket sequences is likewise $C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   **Pop-sequence counting problem**: The push sequence of a stack (of infinite size) is $1,2,3, \ldots ,n$; the number of valid pop sequences is $C_n$.

    ??? note "Proof"
        Relate this to the bracket sequence counting problem. Regard a push as a left bracket and a pop as a right bracket. At any moment, the number of pushes is no less than the number of pops. Therefore, there is a bijection between valid pop sequences and valid bracket sequences. The number of valid pop sequences is likewise $C_n$.

    <!-- To make bot happy. Do NOT delete this line. -->

-   <a id="seq-counting"></a>**Sequence counting problem**: Among the sequences $a_1,a_2, \ldots ,a_{2n}$ composed of $n$ copies of $+1$ and $n$ copies of $-1$, the number of sequences whose partial sums satisfy $a_1+a_2+ \ldots +a_k \geq 0~(k=1,2,3, \ldots ,2n)$ is $C_n$.

    ??? note "Proof"
        Relate this to the bracket sequence counting problem. Regard $+1$ as a left bracket and $-1$ as a right bracket. At any moment, the number of $+1$s is no less than the number of $-1$s. Therefore, there is a bijection between valid sequences and valid bracket sequences. The number of valid sequences is likewise $C_n$.

Although this recurrence relation has wide applications, computing it directly has high complexity, so we need to find simpler formulas.

## Common forms

The Catalan numbers have the following common expressions:

$$
C_n = \frac{1}{n+1}\binom{2n}{n} = \dfrac{(2n)!}{n!(n+1)!},~ n\ge 0. \tag{2}
$$

$$
C_n = \binom{2n}{n} - \binom{2n}{n+1},~n \ge 0. \tag{3}
$$

$$
C_n = \frac{(4n-2)}{n+1}C_{n-1},~ n > 0,~ C_0 = 1. \tag{4}
$$

These forms of the Catalan numbers can all be computed efficiently: the first two forms convert it into a computation involving factorials and binomial coefficients, while the third form provides a recurrence formula for computing them in sequence.

For these three common forms, this article provides two proof methods.

### Algebraic derivation

Deriving the above expressions for the Catalan numbers by algebraic methods takes two steps. First, verify that the three forms are equivalent to one another.

??? note "Proof that expressions $(2)\sim(4)$ are equivalent"
    We only need to prove that expression $(3)$ can be transformed into the factorial form of expression $(2)$:
    
    $$
    \begin{aligned}
    C_n &= \binom{2n}{n} - \binom{2n}{n+1} \\
    &= \frac{(2n)!}{n!n!} - \frac{(2n)!}{(n-1)!(n+1)!} \\
    &= \frac{(2n)!}{n!n!}\left(1 - \frac{n!}{(n-1)!(n+1)}\right) \\
    &= \frac{(2n)!}{n!n!}\left(1- \frac{n}{n+1}\right) \\
    &= \dfrac{(2n)!}{n!(n+1)!}.
    \end{aligned}
    $$
    
    And expression $(4)$ can also be transformed into the factorial form of expression $(2)$:
    
    $$
    C_n = \prod_{i=1}^n\frac{(4i-2)}{i+1} = \prod_{i=1}^n\frac{2i(2i-1)}{i(i+1)} = \dfrac{(2n)!}{n!(n+1)!}.
    $$
    
    Therefore, the three expressions are equivalent to one another.

Next, verify that these forms are indeed solutions of the recurrence formula of the Catalan numbers. To this end, consider using the generating-function method to directly find the solution of the recurrence formula $(1)$.

??? note "Solving the recurrence formula $(1)$ using the generating-function method"
    Consider the ordinary generating function $C(x)=\sum_{n=0}^{\infty}C_nx^n$ of the Catalan numbers. Since the recurrence relation of the Catalan numbers closely resembles a convolution, consider using convolution to construct an equation for $C(x)$:
    
    $$
    \begin{aligned}
    C(x)&=\sum_{n=0}^{\infty}C_nx^n\\
    &=1+\sum_{n=1}^{\infty}\left(\sum_{i=0}^{n-1}C_iC_{n-i-1}\right)x^{n}\\
    &=1+x\sum_{n=1}^{\infty}\sum_{i=0}^{n-1}C_ix^iC_{n-i-1}x^{n-i-1}\\
    &=1+x\sum_{i=0}^{\infty}C_ix^i\sum_{j=0}^{\infty}C_jx^j\\
    &=1+xC^2(x).
    \end{aligned}
    $$
    
    Here, the second-to-last equality swaps the summation order and lets $j=n-1-i$. From this, we solve:
    
    $$
    C(x)=\dfrac{1\pm \sqrt{1-4x}}{2x} = \frac{2}{1\mp \sqrt{1-4x}}.
    $$
    
    From the initial condition $C_0=1$ we know that $C(0)=1$. Substituting to check, one finds that the only feasible solution is
    
    $$
    C(x) = \dfrac{1- \sqrt{1-4x}}{2x}.
    $$
    
    Next, we need to expand it into a power series. Using the [power series expansion](../poly/intro.md#常见的幂级数展开式) of $(1+x)^a$, we know:
    
    $$
    \sqrt{1-4x} = \sum_{n=0}^{\infty} \dfrac{\left(\frac{1}{2}\right)_{-n}}{n!}(-4x)^n,
    $$
    
    where $\left(\dfrac{1}{2}\right)_{-n}$ is the falling factorial power:
    
    $$
    \begin{aligned}
    \left(\frac{1}{2}\right)_{-n} &= \prod_{k=0}^{n-1}\left(\dfrac{1}{2}-k\right) = \dfrac{1}{2^n}\prod_{k=1}^{n-1}(1-2k) = \dfrac{(-1)^{n-1}}{2^n}\prod_{k=1}^{n-1}(2k-1)\\
    &= \dfrac{(-1)^{n-1}}{2^{2n-1}}\prod_{k=1}^{n-1}\dfrac{(2k-1)2k}{k} = \dfrac{(-1)^{n-1}}{2^{2n-1}}\dfrac{(2n-2)!}{(n-1)!}.
    \end{aligned}
    $$
    
    Substituting into the expression for $C(x)$, we have
    
    $$
    \begin{aligned}
    C(x) &= \dfrac{1}{2x}\left(1-\sum_{n=0}^{\infty} \dfrac{\left(\frac{1}{2}\right)_{-n}}{n!}(-4x)^n\right)\\
    &= -\dfrac{1}{2x}\sum_{n=1}^\infty \dfrac{(-4x)^n}{n!}\left(\frac{1}{2}\right)_{-n} \\
    &= -\dfrac{1}{2x}\sum_{n=1}^\infty \dfrac{(-4x)^n}{n!}\dfrac{(-1)^{n-1}}{2^{2n-1}}\dfrac{(2n-2)!}{(n-1)!} \\
    &= \sum_{n=1}^{\infty}\dfrac{(2n-2)!}{(n-1)!n!}x^{n-1}\\
    &= \sum_{n=0}^{\infty}\dfrac{(2n)!}{n!(n+1)!}x^n.
    \end{aligned}
    $$
    
    From this, we obtain expression $(2)$ for $C_n$.

### Combinatorial meaning

Since the Catalan numbers have a clear combinatorial meaning, these forms can also be proved using only combinatorial counting methods. This section provides a combinatorial-meaning proof for each of the three expressions.

??? note "Proof of expression $(2)$"
    Consider the [sequence counting problem](#seq-counting). For any sequence $\{a_i\}_{i=1}^{2n}$ composed of $\pm 1$, define its partial sum as $S_i = \sum_{j=1}^{i}a_i$, and define its **exceedance** as the number of indices for which $S_i < 0$ and $a_i = -1$. Exceedance $0$ is equivalent to the sequence being valid; the range of the exceedance is $[0,n]$, a total of $(n+1)$ possible values. What needs to be proved is that the number of sequences with different exceedances is actually the same.
    
    To this end, one can construct a map $f$ from sequences with exceedance $e > 0$ to sequences with exceedance $(e-1)$. For a sequence $\{a_i\}$ with exceedance $e > 0$, take the index $k$ to be the smallest index for which $S_i = 0$ and $a_i = +1$ hold. Swapping the parts of the sequence on the left and right of $a_k$ gives the following sequence $\{a'_i\}$:
    
    $$
    a_{k+1},a_{k+2},\cdots,a_{2n},a_k,a_{1},a_{2},\cdots,a_{k-1}.
    $$
    
    Since the partial-sum sequence corresponding to the part of the original sequence to the right of $a_k$ is unchanged before and after the swap, the exceedance they contribute is also unchanged. For the part of the original sequence to the left of $a_k$, their corresponding partial sums all increase by $1$ after the swap, so the exceedance they contribute decreases, and the amount of decrease is exactly equal to the number of indices in the part of the original sequence to the left of $a_k$ for which $S_i=-1$ and $a_i=-1$. Because the choice of $a_k$ guarantees that there is exactly one such index, the exceedance of the sequence $\{a'_i\}$ equals $(e-1)$. That is, the map $f$ decreases the exceedance of the sequence by exactly $1$.
    
    The map $f$ is invertible. Note that in the sequence $\{a'_i\}$, the position corresponding to $a_k$ is exactly the largest index for which $S'_k=+1$ and $a'_i = +1$. This is because after the swap, these partial sums are all exactly $1$ larger than the corresponding partial sums before the swap, so a current partial sum of $+1$ corresponds to a partial sum of $0$ before the swap. But by the choice of $k$, this part before the swap (i.e. the part of the original sequence to the left of $a_k$) has no index for which $S_i = 0$ and $a_i = +1$ hold.
    
    From this, the map $f$ constitutes a bijection between sequences with exceedance $e>0$ and sequences with exceedance $(e-1)$. This shows that the number of sequences with different exceedances is actually the same. Since the total number of sequences is $\dbinom{2n}{n}$, the number of valid sequences (i.e. sequences with exceedance $0$) equals
    
    $$
    C_n = \dfrac{1}{n+1}\dbinom{2n}{n}.
    $$
    
    This proves expression $(2)$ of the Catalan numbers.

??? note "Proof of expression $(3)$"
    Consider the [path counting problem](#path-counting). This is a typical lattice-path counting problem, which can be solved via the reflection principle. Specifically for this problem, consider subtracting the number of invalid paths from the total number of paths. A total path takes $2n$ steps, of which $n$ steps go right, so the number of ways is $\dbinom{2n}{n}$. A path is invalid if and only if it touches the line $y = x+1$. For any invalid path, one can find the position where it first touches the line $y = x+1$, and reflect the part of the path after that position about the line $y=x+1$. At this point, one can find that an invalid path from $(0,0)$ to $(n,n)$ becomes a path from $(0,0)$ to $(n-1,n+1)$.
    
    ![catalan1](./images/catalan-1.svg)
    
    Since a path from $(0,0)$ to $(n-1,n+1)$ must cross the line $y = x+1$, each such path corresponds to an invalid path from $(0,0)$ to $(n,n)$. Similar to the computation of the total number of paths, the total number of invalid paths is $\dbinom{2n}{n+1}$. Therefore, the total number of valid paths is
    
    $$
    C_n = \binom{2n}{n} - \binom{2n}{n+1}.
    $$
    
    This is expression $(3)$ of the Catalan numbers.

??? note "Proof of expression $(4)$"
    Consider the [triangulation counting problem](#triangulation-counting). Let $P$ be a convex $(n+2)$-gon, with one of its edges fixed as the base edge. For each triangulation of the polygon $P$, one can choose one of its non-base edges (including edges newly added during triangulation) to mark and orient. This gives a total of $(4n+2)C_n$ triangulation-plus-marking schemes. Now let $Q$ be a convex $(n+3)$-gon, still with one of its edges fixed as the base edge. For the polygon $Q$, one can choose one of its non-base edges to mark, and then triangulate. This gives a total of $(n+2)C_{n+1}$ marking-plus-triangulation schemes.
    
    ![](./images/catalan-triangulation.svg)
    
    As shown in the figure, there is a clear bijection between the results obtained by these two groups of operations. For a result of triangulating and marking $P$, one can expand its marked edge into a triangle, expand the endpoint pointed to by the orientation into a new edge, and mark this new edge, which gives a result of marking and triangulating $Q$; for a result of marking and triangulating $Q$, one can contract its marked edge into a point, and mark the diagonal obtained from the contraction, oriented toward the vertex obtained from the contraction, which gives a result of triangulating and marking $P$. Therefore,
    
    $$
    (4n+2)C_n = (n+2)C_{n+1}.
    $$
    
    Rearranging a little and combining with $C_0=1$ gives expression $(4)$ of the Catalan numbers.

## Example problems

???+ example "[Luogu P1044 栈](https://www.luogu.com.cn/problem/P1044)"
    The push order is $1,2,\ldots ,n$; find the total number of all possible pop orders.

??? note "Reference code"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/combinatorics/catalan/catalan_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/combinatorics/catalan/catalan_1.py"
        ```

## Exercises

-   [Luogu P2532 \[AHOI2012\] 树屋阶梯](https://www.luogu.com.cn/problem/P2532)
-   [Luogu P1641 \[SCOI2010\] 生成字符串](https://www.luogu.com.cn/problem/P1641)
-   [Luogu P3200 \[HNOI2009\] 有趣的数列](https://www.luogu.com.cn/problem/P3200)
-   [AtCoder Beginner Contest 205 E - White and Black Balls](https://atcoder.jp/contests/abc205/tasks/abc205_e)
-   [AtCoder Regular Contest 145 C - Split and Maximize](https://www.luogu.com.cn/problem/AT_arc145_c)
-   [Luogu P5014 水の三角（修改版）](https://www.luogu.com.cn/problem/P5014)
-   [Luogu P3978 \[TJOI2015\] 概率论](https://www.luogu.com.cn/problem/P3978)

## References and notes

-   [Catalan number - Wikipedia](https://en.wikipedia.org/wiki/Catalan_number)
