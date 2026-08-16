author: 383494, CCXXXI, chunibyo-wly, Enter-tainer, Great-designer, megakite, Menci, shawlleyw, shuzhouliu, StudyingFather, Tiphereth-A, untitledunrevised, c-forrest

## Introduction

Continued fractions can represent a real number as the limit of a convergent sequence of rational numbers. The rational numbers in this sequence are easy to compute and provide the best approximation of this real number, so continued fractions are often used in competitive programming. In addition, continued fractions are closely related to the Euclidean algorithm, so they can be applied to a series of number-theory problems.

???+ info "About the algorithm implementations related to continued fractions"
    This article will provide a series of algorithm implementations of continued fractions, some of which may not be able to guarantee that all integers involved in the intermediate computation are within the value range of 32-bit or 64-bit integer variables. For this case, please refer to the corresponding Python implementation, or replace the integer variables in the C++ implementation with the [high-precision integer class](../bignum.md). To highlight the key points, some code in the text of this article may call functions implemented earlier without repeating the implementation.

## Continued fractions

A **continued fraction** is itself just a form of notation.

???+ abstract "Finite continued fraction"
    For a sequence $\{a_k\}_{i=0}^n$, the continued fraction $[a_0,a_1,\cdots,a_n]$ denotes the expansion
    
    $$
    x = a_0+\dfrac{1}{a_1+\dfrac{1}{a_2+\dfrac{1}{\cdots+\dfrac{1}{a_n}}}}.
    $$
    
    The continued fraction is meaningful if and only if the corresponding expansion is meaningful. These $a_k$ are called the **terms** or **coefficients** of the continued fraction.

???+ info "Notation"
    A more general continued fraction allows the numerators in the expansion not to be constantly $1$, and the corresponding continued fraction notation also needs to be modified, which is beyond the scope of this article. In addition, some literature writes the first comma "$,$" as a semicolon "$;$", which has no difference in meaning from the notation in this article.

Of course, continued fractions can also be generalized to the case of infinite sequences.

???+ abstract "Infinite continued fraction"
    For an infinite sequence $\{a_k\}_{i=0}^\infty$, the continued fraction $[a_0,a_1,\cdots]$ denotes the limit
    
    $$
    x = \lim_{k\rightarrow\infty} x_k = \lim_{k\rightarrow\infty} [a_0,a_1,\cdots,a_k].
    $$
    
    The continued fraction is meaningful if and only if the corresponding limit is meaningful. Here, $x_k=[a_0,a_1,\cdots,a_k]$ is called the $k$-th **convergent** of $x$, and $r_k=[a_k,a_{k+1},\cdots]$ is called the $k$-th **remainder term** or **complete quotient** of $x$. Correspondingly, the term $a_k$ is sometimes also called the $k$-th **partial quotient**.

### Simple continued fractions

In number theory, we mainly consider the case where the terms of the continued fraction are all integers.

???+ abstract "Simple continued fraction"
    For a continued fraction $[a_0,a_1,\cdots]$, if $a_0$ is an integer and $a_1,a_2,\cdots$ are all positive integers, then it is called a **simple continued fraction**, also abbreviated as **continued fraction**. If the sequence $\{a_i\}$ is finite, it is called a **finite (simple) continued fraction**; otherwise it is called an **infinite (simple) continued fraction**. Moreover, $a_0$ is called its **integer part**.

Unless otherwise specified, the continued fractions mentioned in this article all refer to simple continued fractions. It can be proven that an infinite simple continued fraction must be convergent, and the remainder terms of a simple continued fraction must be positive.

Continued fractions have the following basic properties:

???+ note "Properties"
    Let the real number $x=[a_0,a_1,a_2,\cdots]$. Then, the following properties hold:
    
    1.  For any $k\in\mathbf Z$, $x+k=[a_0+k,a_1,a_2,\cdots]$;
    2.  For a real number $x>1$, $a_0>0$, and its reciprocal $x^{-1}=[0,a_0,a_1,a_2,\cdots]$.

A finite continued fraction corresponds to a rational number. Every rational number can be represented as a continued fraction in exactly two ways, and the lengths must be one odd and one even. The only difference between these two ways is whether the last term is $1$, i.e.

$$
x = [a_0,a_1,\cdots,a_n] = [a_0,a_1,\cdots,a_n-1,1].
$$

These two continued fractions are called the **continued fraction representations** of the rational number $x$. Among them, the one whose last term is not one is called the standard representation, and the one whose last term is one is called the non-standard representation.[^one-representation]

??? example "Example"
    The continued fraction representations of the rational number $x=\dfrac{5}{3}$ are
    
    $$
    \begin{aligned}
    x = [1,1,1,1] &= 1+\dfrac{1}{1+\dfrac{1}{1+\dfrac{1}{1}}},\\
    x = [1,1,2] &= 1+\dfrac{1}{1+\dfrac{1}{2}}.
    \end{aligned}
    $$

An infinite continued fraction corresponds to an irrational number. Moreover, every irrational number has a unique way to be represented as a continued fraction, called the continued fraction representation of the irrational number.

### Finding the continued fraction representation

To find the continued fraction representation of some real number $x$, we only need to note that its remainder term $r_k$, if it is not an integer, must satisfy

$$
r_k = [a_k,a_{k+1},\cdots] = [a_k,r_{k+1}] = a_k + \dfrac{1}{r_{k+1}}.
$$

Moreover, $r_{k+1}>1$. Therefore, we can recursively compute, starting from $r_0=x$,

$$
a_k = \lfloor r_k\rfloor,\ r_{k+1} = \dfrac{1}{r_k-a_k}.
$$

The sequence $\{a_k\}$ produced by this process is always uniquely determined, unless some remainder term $r_k$ becomes an integer. If it happens that $r_k$ is an integer, then the process should terminate, and we can choose to output the corresponding standard representation or non-standard representation.

In competitive programming, we often deal with the case of a rational number $x=\dfrac{p}{q}$. In this case, each remainder term $r_k$ is a rational number $\dfrac{p_k}{q_k}$, and for $k>0$, because $r_k>1$, we always have $p_k>q_k$. Computing the above recurrence specifically, we find

$$
a_k = \left\lfloor\frac{p_k}{q_k}\right\rfloor,\ r_{k+1} = \dfrac{1}{r_k-a_k} = \dfrac{q_k}{p_k-a_kq_k} = \dfrac{q_k}{p_k\bmod q_k}.
$$

The computation process in this case is actually doing the [Euclidean algorithm](./gcd.md#euclidean-algorithm) on $p$ and $q$. This also shows that for a rational number $r=\dfrac{p}{q}$, the length of the continued fraction representation is $O(\log\min\{p, q\})$. The complexity of computing the rational number $\dfrac{p}{q}$ is also $O(\log\min\{p, q\})$.

???+ example "Reference implementation"
    Given the numerator $p$ and denominator $q$ of a fraction, output the coefficient sequence of the continued fraction $[a_0,a_1,\cdots,a_n]$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/diophantine.cpp:fraction"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/diophantine.py:fraction"
        ```

## Convergents

The concept of convergents was introduced in the definition of continued fractions. The convergent of a real number is exactly the convergent of its continued fraction representation: in the continued fraction representation of the real number $x$, keeping only the first $k$ terms, the continued fraction $x_k$ obtained is called the $k$-th convergent of the real number $x$. The convergents $x_k$ of the real number $x$ are all rational numbers, and the sequence $\{x_k\}$ converges to the real number $x$.

??? example "Example: convergents of the golden ratio"
    The first few convergents of the continued fraction $x=[1,1,1,1,\cdots]$ are
    
    $$
    \begin{aligned}
    x_0 &= [1]=1,\\
    x_1 &= [1,1]=2,\\
    x_2 &= [1,1,1]=\dfrac{3}{2},\\
    x_3 &= [1,1,1,1]=\dfrac{5}{3},\\
    x_4 &= [1,1,1,1,1]=\dfrac{8}{5}.
    \end{aligned}
    $$
    
    It can be proven inductively that
    
    $$
    x_k = \frac{F_{k+2}}{F_{k+1}},
    $$
    
    where $\{F_k\}$ is the [Fibonacci sequence](../combinatorics/fibonacci.md). By its closed-form formula,
    
    $$
    x_k = \frac{\phi^{k+2}-(-\phi)^{-(k+2)}}{\phi^{k+1}-(-\phi)^{-(k+1)}},
    $$
    
    where $\phi=\dfrac{1+\sqrt{5}}{2}$ is the golden ratio. When $k$ tends to infinity,
    
    $$
    x=\lim_{k\rightarrow\infty}x_k=\phi.
    $$
    
    Therefore, the continued fraction $x=[1,1,1,1,\cdots]$ represents the golden ratio $\phi$.

These convergents approach the corresponding real number, so they can be used to approximate that real number. To this end, it is necessary to understand the properties of convergents.

### Recurrence relations

First, we need to solve the computation of these convergents. Although the convergent always adds one term after the continued fraction, we do not need to recompute its value each time. In fact, convergents have the following recurrence relation:

???+ note "Recurrence formula"
    For a continued fraction $x=[a_0,a_1,a_2,\cdots]$, let its $k$-th convergent $x_k$ be written as the fraction $\dfrac{p_k}{q_k}$. Then, we have
    
    $$
    \begin{aligned}
    p_k &= a_kp_{k-1}+p_{k-2},\\
    q_k &= a_kq_{k-1}+q_{k-2}.
    \end{aligned}
    $$
    
    The starting point of the recurrence is the (formal) fractions
    
    $$
    x_{-1}=\frac{p_{-1}}{q_{-1}}=\frac{1}{0},\ x_{-2}=\frac{p_{-2}}{q_{-2}}=\frac{0}{1}.
    $$

??? note "Proof"
    The numerator and denominator of the convergent $x_k$ can be viewed as multivariate polynomials in $a_0, a_1, \cdots, a_k$:
    
    $$
    r_k = \frac{P_k(a_0, a_1, \cdots, a_k)}{Q_k(a_0,a_1, \cdots, a_k)}.
    $$
    
    By the definition of the convergent,
    
    $$
    r_k = a_0 + \frac{1}{[a_1,a_2,\cdots, a_k]}= a_0 + \frac{Q_{k-1}(a_1, \cdots, a_k)}{P_{k-1}(a_1, \cdots, a_k)} = \frac{a_0 P_{k-1}(a_1, \dots, a_k) + Q_{k-1}(a_1, \cdots, a_k)}{P_{k-1}(a_1, \cdots, a_k)}.
    $$
    
    Comparing with the above, suppose $Q_k(a_0, \cdots, a_k) = P_{k-1}(a_1, \cdots, a_k)$; then we can write the convergent as
    
    $$
    r_k =  \frac{P_k(a_0, a_1, \cdots, a_k)}{P_{k-1}(a_1, \cdots, a_k)}
    $$
    
    and the polynomial $P_k$ has the recurrence relation
    
    $$
    P_k(a_0, \cdots, a_k) = a_0 P_{k-1}(a_1, \cdots, a_k) + P_{k-2}(a_2, \cdots, a_k).
    $$
    
    Because
    
    $$
    r_0 = a_0,\ r_1 = a_0+\dfrac{1}{a_1} = \frac{a_0a_1+1}{a_1},
    $$
    
    the starting point of the recurrence is
    
    $$
    P_0(a_0) = a_0,\ P_1(a_0,a_1) = a_0a_1 + 1.
    $$
    
    If we set
    
    $$
    P_{-1} = 1,\ P_{-2} = 0,
    $$
    
    we can verify that the above recurrence relation also holds for $k=0,1$. This amounts to stipulating the formal fractions $r_{-1}=\dfrac{1}{0}$ and $r_{-2}=\dfrac{0}{1}$.
    
    The polynomial sequence $P_k$ satisfying the above recurrence relation is called a **continuant**[^continuant]. It can be written in the form of a determinant:
    
    $$
    P_k(a_0,\cdots,a_k)=\det
    \begin{pmatrix}
    a_0 & 1 & 0 & \cdots & 0 \\
    -1 & a_1 & 1 & \ddots & \vdots \\
    0 & -1 & a_2 & \ddots & 0 \\
    \vdots & \ddots & \ddots & \ddots & 1 \\
    0 & \cdots & 0 & -1 & a_k
    \end{pmatrix}.
    $$
    
    This is the determinant of a [tridiagonal matrix](https://en.wikipedia.org/wiki/Tridiagonal_matrix); expanding from the upper-left corner, we can verify that it has the above recurrence relation and initial conditions. Conversely, expanding from the lower-right corner, we can obtain the recurrence relation
    
    $$
    P_k(a_0, \cdots, a_k) = a_k P_{k-1}(a_0, \cdots, a_{k-1}) + P_{k-2}(a_0, \cdots, a_{k-2}),
    $$
    
    which is what needed to be proved.

???+ info "Notation"
    When this article writes the convergent $x_k$ as $\dfrac{p_k}{q_k}$, it is always assumed that the numerator $p_k$ and $q_k$ are given by the above recurrence relation. It will be explained below that this always gives the reduced representation of the convergent.

This recurrence shows that

$$
x_k=\dfrac{a_kp_{k-1}+p_{k-2}}{a_kq_{k-1}+q_{k-2}}
$$

lies between $x_{k-1}$ and $x_{k-2}$.

As corollaries of the recurrence relation of convergents, the following reverse-order theorem and reciprocal theorem hold:

???+ note "Reverse-order theorem"
    Let the $k$-th convergent of the real number $x=[a_0,a_1,a_2,\cdots]$ be $\dfrac{p_k}{q_k}$; then the ratios of the numerators and denominators of two adjacent convergents are respectively
    
    $$
    \begin{aligned}
    \frac{p_k}{p_{k-1}}&=[a_k,a_{k-1},\cdots,a_1,a_0],\\
    \frac{q_k}{q_{k-1}}&=[a_k,a_{k-1},\cdots,a_1].
    \end{aligned}
    $$
    
    If $a_0=0$, then the first continued fraction should be understood as truncated at the second-to-last term, i.e. $[a_k,a_{k-1},\cdots,a_2]$.

??? note "Proof"
    In the recurrence relations of $p_k$ and $q_k$, dividing both sides by $p_{k-1}$ and $q_{k-1}$ respectively, we obtain
    
    $$
    \begin{aligned}
    \frac{p_k}{p_{k-1}} &= a_k + \frac{p_{k-2}}{p_{k-1}},\\
    \frac{q_k}{q_{k-1}} &= a_k + \frac{q_{k-2}}{q_{k-1}}.
    \end{aligned}
    $$
    
    Iterating these two expressions, we obtain two continued fractions. Then substituting the initial values $\dfrac{p_0}{p_{-1}}=a_0$ and $\dfrac{q_1}{q_0}=a_1$. As for the case $a_0=0$, understanding the obtained continued fraction as a formal expression, its remainder term
    
    $$
    [a_2,a_1,0]=a_2+\dfrac{1}{a_1+\dfrac{1}{0}}=a_2+\dfrac{0}{0a_1+1}=a_2.
    $$
    
    So we can directly omit the last two terms. If a rigorous proof is needed, we only need to note that this expression can be viewed as the limit as $a_0\rightarrow 0$.

???+ note "Reciprocal theorem"
    The reciprocal of a convergent of a real number $x>0$ is a convergent of $x^{-1}$.

??? note "Proof"
    Suppose $x>1$ with continued fraction representation $[a_0,a_1,a_2,\cdots]$; then the continued fraction representation of $x^{-1}$ is $[0,a_0,a_1,a_2,\cdots]$. Their convergents can be found from the recurrence relation. Moreover, for $x$, there are the initial conditions $x_{-2}=\dfrac{0}{1}$ and $x_{-1}=\dfrac{1}{0}$; for $y=x^{-1}$, there are the initial conditions $y_{-1}=\dfrac{1}{0}$ and $y_{0}=\dfrac{0}{1}$. Therefore, $x_{-2}=(y_{-1})^{-1}$ and $x_{-1}=(y_0)^{-1}$. By the recurrence relation, we can obtain $x_k=y_{k+1}^{-1}$. This shows that the reciprocal of a convergent of $x$ is a convergent of $y=x^{-1}$. For the case $0<x\le 1$, a similar discussion can be made.

Using the recurrence relation obtained in this section, we can obtain the algorithm for computing convergents as follows:

???+ example "Reference implementation"
    Given the coefficients $a_0,a_1,\cdots,a_n$ of a continued fraction, find the numerator and denominator sequence of the convergents $(p_0,q_0),(p_1,q_1),\cdots,(p_n,q_n)$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/diophantine.cpp:convergents"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/diophantine.py:convergents"
        ```

### Error estimation

Using the recurrence formula of convergents, we can estimate the error produced by approximating a real number with convergents.

First, we can compute the difference between adjacent convergents:

???+ note "Difference of convergents"
    Let $x_k=\dfrac{p_k}{q_k}$ be the $k$-th convergent of the real number $x$. Then, we have
    
    $$
    p_{k+1}q_k − p_kq_{k+1} = (−1)^k.
    $$
    
    Therefore, the difference of two adjacent convergents is
    
    $$
    x_{k+1} - x_k = \dfrac{(-1)^k}{q_{k+1}q_k}.
    $$

??? note "Proof"
    By the recurrence relation,
    
    $$
    \begin{aligned}
    \det\begin{pmatrix}
    p_{k+1} & p_k \\
    q_{k+1} & q_k 
    \end{pmatrix}
    &=
    \det\begin{pmatrix}
    a_{k+1}p_{k}+p_{k-1} & p_k \\
    a_{k+1}q_{k}+q_{k-1} & q_k 
    \end{pmatrix}
    =
    \det\begin{pmatrix}
    p_{k-1} & p_k\\
    q_{k-1} & q_k
    \end{pmatrix}
    \\
    &=
    -
    \det\begin{pmatrix}
    p_k & p_{k-1}\\
    q_k & q_{k-1}
    \end{pmatrix}
    =
    (-1)^{k+2}
    \det\begin{pmatrix}
    1 & 0\\
    0 & 1
    \end{pmatrix}
    =(-1)^k.
    \end{aligned}
    $$
    
    This is $p_{k+1}q_k − p_kq_{k+1} = (−1)^k$. Dividing both sides by $q_{k+1}q_k$, we obtain the conclusion about $x_{k+1}-x_k$.

Therefore, odd-indexed convergents are always greater than their two neighbors, and even-indexed convergents are always less than their two neighbors: the convergents vary in an alternating manner.

If we only look at the even-indexed (odd-indexed) convergents, the sequence is also monotonically increasing (decreasing). This is because

$$
x_{k+2}-x_k = \dfrac{(-1)^{k+1}}{q_{k+2}q_{k+1}}+\dfrac{(-1)^{k}}{q_{k+1}q_{k}} = \dfrac{(-1)^k(q_{k+2}-q_k)}{q_{k+2}q_{k+1}q_k} = \dfrac{(-1)^ka_{k+2}}{q_{k+2}q_k}
$$

is positive (negative) when $k$ is even (odd). At the same time, because the recurrence relation $q_{k}=a_kq_{k-1}+q_{k-2}$ holds, the denominator $q_k$ grows no slower than the Fibonacci sequence. So, the difference of two adjacent terms must tend to zero. This shows that the even-indexed and odd-indexed convergents approach the same limit from below and from above respectively. This proves that an infinite simple continued fraction must converge. The dynamics of the convergents approaching the corresponding real number can be seen in the figure below:

![](./images/golden-ratio-convergents.svg)

???+ abstract "Upper (lower) convergent"
    For a real number $x$ and its convergent $x_k$, if $x_k>x$ ($x_k<x$), then $x_k$ is called an **upper (lower) convergent** of $x$.

As explained earlier, the upper convergents are exactly the odd-indexed convergents, and the lower convergents are exactly the even-indexed convergents.

Using the difference formula, we can write the real number $x$ in the form of an alternating series:

$$
x = a_0+\sum_{k=0}^{\infty}\dfrac{(-1)^k}{q_{k+1}q_k}.
$$

The convergents and remainder terms in the definition of the continued fraction are exactly the partial sums and remainders of this series.

Using the difference formula, we can also directly estimate the error produced by approximating a real number with convergents:

???+ note "Error"
    Let $x_k=\dfrac{p_k}{q_k}\neq x$ be the $k$-th convergent of the real number $x$. Then, we have
    
    $$
    x_k - x = \dfrac{(-1)^k}{q_k\left(r_{k+1}q_k+q_{k-1}\right)},
    $$
    
    where $r_{k+1}$ is the $(k+1)$-th remainder term of the real number $x$. Furthermore,
    
    $$
    \dfrac{1}{2q_{k+1}^2} \le \dfrac{1}{q_k(q_k+q_{k+1})} \le \left|x-\frac{p_k}{q_k}\right| \le \dfrac{1}{q_kq_{k+1}} \le \dfrac{1}{q_k^2}.
    $$

??? note "Proof"
    Because $x=[a_0,a_1,\cdots,a_k,r_{k+1}]$, and the difference formula of convergents also holds for formal continued fractions,
    
    $$
    x-x_k = \dfrac{(-1)^k}{q_k\left(r_{k+1}q_k+q_{k-1}\right)},
    $$
    
    where $r_{k+1}q_k+q_{k-1}$ is exactly the denominator of the $(k+1)$-th convergent of this formal continued fraction obtained by the recurrence formula.
    
    To complete the subsequent inequality estimate, we only need to note that when $x_k\neq x$, we always have
    
    $$
    1\le a_{k+1}\le r_{k+1} \le a_{k+1}+1,
    $$
    
    so
    
    $$
    q_{k+1}=a_{k+1}q_k+q_{k-1}\le r_{k+1}q_k+q_{k-1} \le q_k+(a_{k+1}q_k+q_{k-1}) = q_k+q_{k+1}.
    $$
    
    Therefore, we have the inequality
    
    $$
    \dfrac{1}{q_k(q_k+q_{k+1})} \le \left|x-\frac{p_k}{q_k}\right| = \dfrac{1}{q_k\left(r_{k+1}q_k+q_{k-1}\right)} \le \dfrac{1}{q_kq_{k+1}}.
    $$
    
    To obtain the outer bounds, we only need to note that $q_k\le q_{k+1}$.

The difference formula in this section also has a simple corollary: the convergents $\dfrac{p_k}{q_k}$ are all reduced.

???+ note "Corollary"
    For any real number $x$, and the numerator and denominator of the convergent $x_k=\dfrac{p_k}{q_k}$ given by the recurrence formula, $\dfrac{p_k}{q_k}$ is a reduced fraction, i.e. $\gcd(p_k,q_k)=1$.

??? note "Proof"
    Apply [Bézout's identity](./bezouts.md) to the difference formula.

In fact, the solution of a binary linear indeterminate equation can be found via the continued fraction method.

???+ example "Solving a binary linear indeterminate equation"
    Given $A, B, C \in \mathbf Z$. Find $x, y \in \mathbf Z$ such that $Ax + By = C$ holds.

??? note "Solution"
    Although this problem is usually solved with the [extended Euclidean algorithm](./bezouts.md#the-case-of-two-variables), it can also be solved via continued fractions.
    
    Let $\dfrac{A}{B}=[a_0, a_1, \cdots, a_k]$. It was proven above that $p_k q_{k-1} - p_{k-1} q_k = (-1)^{k-1}$. Replacing $p_k$ and $q_k$ with $A$ and $B$, we obtain
    
    $$
    Aq_{k-1} - Bp_{k-1} = (-1)^{k-1} g,
    $$
    
    where $g = \gcd(A, B)$. If $g$ divides $C$, then a set of solutions is $x = (-1)^{k-1}\dfrac{C}{g} q_{k-1}$ and $y = (-1)^{k}\dfrac{C}{g} p_{k-1}$; otherwise there is no solution.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/diophantine.cpp:dio"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/diophantine.py:dio"
        ```

## Diophantine approximation

An important application of continued fraction theory is the theory of Diophantine approximation. Diophantine approximation refers to approximating real numbers with rational numbers. Of course, due to the density of the rational numbers, if no restriction is imposed, we can obtain approximations with arbitrarily small error. Therefore, we need to impose a restriction on the rational numbers that can be used, for example only being able to choose rational numbers with denominator less than some value. This section discusses the relationship between the best approximation under such a restriction and continued fractions.

### Approximating real numbers with convergents

First, using the error estimate of convergents, we immediately obtain the following result:

???+ note "Theorem (Dirichlet)"
    For an irrational number $x$, there exist infinitely many reduced fractions $\dfrac{p}{q}$ such that
    
    $$
    \left|x-\dfrac{p}{q}\right| < \dfrac{1}{q^2} 
    $$
    
    holds.

??? note "Proof"
    By the error estimate of convergents, for the $k$-th convergent $x_k=\dfrac{p_k}{q_k}$ of the irrational number $x$,
    
    $$
    \left|x-\dfrac{p_k}{q_k}\right|\le\frac{1}{q_k^2}.
    $$
    
    Checking the proof of the error formula, we know that for any irrational number $x$, the equality condition does not hold. Therefore, the numerators and denominators of all its convergents satisfy the requirement.

This theorem can also be viewed as a corollary of the [Dirichlet approximation theorem](https://en.wikipedia.org/wiki/Dirichlet%27s_approximation_theorem). This is almost already the best result. The exponent $2$ in the denominator on the right side of the inequality can no longer be improved, but the constant can be made better. Hurwitz's theorem shows that the right side of the inequality can be reduced to $\dfrac{1}{\sqrt{5}q^2}$, and this is the best bound.

???+ note "Hurwitz's theorem"
    For an irrational number $x$, there exist infinitely many reduced fractions $\dfrac{p}{q}$ such that
    
    $$
    \left|x-\dfrac{p}{q}\right| < \dfrac{1}{\sqrt{5}q^2} 
    $$
    
    holds, and the $\sqrt{5}$ on the right side of the inequality cannot be replaced by a larger real number.

??? note "Proof (Borel)"
    Borel actually proved that among any three consecutive convergents of an irrational number $x$, there must be at least one satisfying the above condition. Because there are infinitely many convergents and they are all reduced fractions, the first part of Hurwitz's theorem must hold.
    
    Proof by contradiction. Suppose there exists an irrational number $x$ and its convergents $x_{k-1},x_k,x_{k+1}$ such that
    
    $$
    \left|x-\dfrac{p_{k-1}}{q_{k-1}}\right|\ge\dfrac{1}{\sqrt{5}q_{k-1}^2},\ 
    \left|x-\dfrac{p_{k}}{q_{k}}\right|\ge\dfrac{1}{\sqrt{5}q_{k}^2},\ 
    \left|x-\dfrac{p_{k+1}}{q_{k+1}}\right|\ge\dfrac{1}{\sqrt{5}q_{k+1}^2}
    $$
    
    hold. Because adjacent convergents must be on opposite sides of $x$, by the difference formula
    
    $$
    \dfrac{1}{q_{k-1}q_{k}}=\left|\dfrac{p_{k-1}}{q_{k-1}}-\dfrac{p_{k}}{q_{k}}\right|=\left|x-\dfrac{p_{k-1}}{q_{k-1}}\right|+\left|x-\dfrac{p_{k}}{q_{k}}\right|\ge\dfrac{1}{\sqrt{5}q_{k-1}^2}+\dfrac{1}{\sqrt{5}q_{k}^2}.
    $$
    
    It can be written as an inequality about the ratio $\dfrac{q_{k}}{q_{k-1}}$
    
    $$
    \dfrac{q_k}{q_{k-1}}+\dfrac{q_{k-1}}{q_k}\le\sqrt 5.
    $$
    
    Because the left side is rational and the right side is irrational, equality cannot be attained. And because $q_k\ge q_{k-1}$, we can solve
    
    $$
    1\le \dfrac{q_{k}}{q_{k-1}} < \dfrac{\sqrt{5}+1}{2}.
    $$
    
    Similarly, we can prove
    
    $$
    1\le \dfrac{q_{k+1}}{q_{k}} < \dfrac{\sqrt{5}+1}{2}.
    $$
    
    But by the recurrence formula, combining the two expressions,
    
    $$
    a_{k+1} = \frac{q_{k+1}}{q_k}-\frac{q_{k-1}}{q_k} < \dfrac{\sqrt{5}+1}{2}-\dfrac{\sqrt{5}-1}{2} = 1
    $$
    
    which contradicts the definition of a simple continued fraction. So, Borel's conclusion holds.
    
    To show that the bound obtained this way is the best, we only need to find $x$ such that for any $C>\sqrt{5}$, there exist only finitely many reduced fractions $\dfrac{p}{q}$ such that the inequality
    
    $$
    \left|x-\dfrac{p}{q}\right| < \dfrac{1}{Cq^2} 
    $$
    
    holds. Below we prove that $\phi=\dfrac{\sqrt{5}+1}{2}$ is such an $x$.[^sqrt5]
    
    Let $\phi'=\dfrac{-\sqrt{5}+1}{2}$ be the conjugate root of $\phi$. They are both roots of the equation $x^2-x-1=0$. Therefore, for any real number $x$,
    
    $$
    x^2-x-1 = (x-\phi)(x-\phi').
    $$
    
    Substituting the reduced fraction $\dfrac{p}{q}$, we obtain
    
    $$
    \dfrac{1}{q^2}\le\frac{|p^2-pq-q^2|}{q^2}=\left|\dfrac{p}{q}-\phi\right|\left|\dfrac{p}{q}-\phi'\right|\le\left|\dfrac{p}{q}-\phi\right|\left(\left|\dfrac{p}{q}-\phi\right|+|\phi-\phi'|\right)<\dfrac{1}{Cq^2}\left(\dfrac{1}{Cq^2}+\sqrt{5}\right).
    $$
    
    For $C>\sqrt{5}$, we can directly solve $q<\sqrt{C(C-\sqrt{5})}$, so there cannot exist infinitely many solutions satisfying the above inequality.

The proofs of these theorems show that convergents provide fairly good Diophantine approximations. But this is not necessarily the best approximation. To discuss the best approximation, we need to specify the measure of the degree of approximation. There are often two choices.

???+ warning "Cases where the best-approximation conclusions may not hold"
    The next two sections will state some results about best approximation. These results may not hold for certain uninteresting cases. For example, both types of definitions of best approximation require strict inequality, but for a half-integer $x=n+\dfrac12$ with $n\in\mathbf Z$, the form of its continued fraction can be $[n,1,1]$. In this case, the denominators of its first two convergents $x_0=n$ and $x_1=n+1$ are both $1$, and the distances to $x$ are the same. This shows that neither of them is the best approximation. For the statements of the conclusions in this section, the reader should assume by default that such cases have been excluded. If the reader does not care about the last few convergents, or only cares about the approximation of irrational numbers, then these additional complex cases need not be considered.

### Best approximation of the first kind: intermediate fractions

The best approximation of the first kind uses

$$
\left|x-\dfrac{p}{q}\right|
$$

to measure the degree of approximation.

???+ abstract "Best approximation of the first kind"
    For a real number $x$ and a rational number $\dfrac{p}{q}$, if for any $\dfrac{p'}{q'}\neq \dfrac{p}{q}$ with $0<q'\le q$,
    
    $$
    \left|x-\dfrac{p}{q}\right|<\left|x-\dfrac{p'}{q'}\right|,
    $$
    
    then the rational number $\dfrac{p}{q}$ is called a **best approximation of the first kind** of the real number $x$.

Best approximations of the first kind are not necessarily convergents, but a broader class of fractions.

???+ abstract "Intermediate fraction"
    Let the real number $x$ have the convergent $x_{k+1}=[a_0,a_1,\cdots,a_k,a_{k+1}]$, and let the integer $t$ satisfy $0\le t\le a_{k+1}$[^semi-range]; then the fraction $x_{k,t}=[a_0,a_1,\cdots,a_{k},t]$ is called an **intermediate fraction**, **semiconvergent**, or **secondary convergent** of $x$.[^semiconvergent]
    
    Similar to the case of convergents, an intermediate fraction greater than (less than) $x$ is called an **upper (lower) semiconvergent**.

By the recurrence formula, an intermediate fraction can be written as

$$
x_{k,t} = \frac{tp_{k}+p_{k-1}}{tq_{k}+q_{k-1}}.
$$

It must be a reduced fraction and lies between the convergents $x_{k-1}$ and $x_{k+1}$. As $t$ increases, it also gradually approaches $x_{k+1}$: (taking the case where $k$ is even as an example)

$$
x_{k-1} = x_{k,0} < x_{k,1} < x_{k,2} < \cdots < x_{k,a_{k+1}} = x_{k+1}.
$$

Because the numerators and denominators of the convergents are both increasing, the numerator and denominator of the intermediate fraction $x_{k,t}$ ($t\neq 0$) fall between $x_{k}$ and $x_{k+1}$. If we arrange these fractions by the size of their denominators, the intermediate fractions are exactly the fractions located between adjacent convergents.

All best approximations of the first kind are intermediate fractions, but not all intermediate fractions are best approximations of the first kind.

???+ note "Theorem"
    All best approximations of the first kind are intermediate fractions.

??? note "Proof"
    Because $a_0\le x\le a_0+1$, a best approximation of the first kind must lie between $x_{1,0}=a_0$ and $x_{0,1}=a_0+1$. All intermediate fractions can be arranged from small to large as
    
    $$
    x_{1,0}<x_{1,1}< \cdots < x_{1,a_2}=x_{3,0}<\ldots<x<\ldots<x_{2,0}=x_{0,a_1}<\cdots<x_{0,1}.
    $$
    
    Intermediate fractions of the same order appear consecutively, and there is no gap between intermediate fractions of different orders. This means that any rational number $\dfrac{p}{q}$ located between $x_{1,0}=a_0$ and $x_{0,1}=a_0+1$ must fall between two intermediate fractions $x_{k,t}$ and $x_{k,t+1}$ of the same order. Suppose it is not an intermediate fraction and is less than $x$; then
    
    $$
    x_{k,t}<\dfrac{p}{q}<x_{k,t+1}<x.
    $$
    
    In this case, on the one hand,
    
    $$
    \left|x_{k,t}-\dfrac{p}{q}\right| \le \left|x_{k,t}-x_{k,t+1}\right| = \dfrac{1}{((t+1)q_k+q_{k-1})(tq_k+q_{k-1})}.
    $$
    
    On the other hand,
    
    $$
    \left|x_{k,t}-\dfrac{p}{q}\right| = \dfrac{|q(tp_k+p_{k-1})-p((t+1)q_k+q_{k-1})|}{q(tq_k+q_{k-1})}\ge\dfrac{1}{q(tq_k+q_{k-1})}.
    $$
    
    Therefore, we must have
    
    $$
    q>(t+1)q_k+q_{k-1}.
    $$
    
    That is, the denominator of the rational number $\dfrac{p}{q}$ is definitely greater than the denominator of $x_{k,t+1}$, but it is not a better approximation:
    
    $$
    \left|x-\dfrac{p}{q}\right|>\left|x-x_{k,t+1}\right|
    $$
    
    Therefore, it cannot be a best approximation of the first kind. This shows that if it is not an intermediate fraction, it is not a best approximation of the first kind; i.e. all best approximations of the first kind are intermediate fractions.

Conversely, we cannot assert that all intermediate fractions are best approximations of the first kind. But we can indeed give the condition for an intermediate fraction to be a best approximation of the first kind.

???+ note "Theorem"
    All convergents are best approximations of the first kind. In addition, let $0<t<a_{k+1}$; then the intermediate fraction $x_{k,t}$ is a best approximation of the first kind if and only if $t>\dfrac{a_{k+1}}{2}$, or $t=\dfrac{a_{k+1}}{2}$ and $r_{k+2}>\dfrac{q_k}{q_{k-1}}$.

??? note "Proof"
    Below we will prove that convergents are all best approximations of the second kind, so they must be best approximations of the first kind. The key is those intermediate fractions that are not convergents.
    
    As stated earlier, the denominator of the intermediate fraction $x_{k,t}$ lies between $x_k$ and $x_{k+1}$ and gradually increases as $t$ increases, but $x_{k,t}$ gradually approaches $x_{k+1}$ and thus approaches $x$. Taking $x_{k,t}<x$ as an example, its relative position with respect to the adjacent intermediate fractions satisfies:
    
    $$
    x_{k-1} < x_{k,t} < x_{k+1} < x < x_{k}.
    $$
    
    Because the denominator of $x_k$ is less than that of $x_{k,t}$, a necessary condition for $x_{k,t}$ to be a best approximation of the first kind is that it is closer to $x$ than $x_k$. This is also a sufficient condition, because as a convergent, there is nothing with a smaller denominator than $x_k$ that is closer, and those intermediate fractions with denominators even larger than $x_k$ must be of the same order as $x_{k,t}$ but with smaller denominators, so they must be farther from $x$. For the errors of the convergent and the intermediate fraction, computation shows
    
    $$
    \begin{aligned}
    \left|x_k-x\right| &= \dfrac{1}{q_k(r_{k+1}q_k+q_{k-1})},\\
    \left|x_{k,t}-x\right| &= \left|\dfrac{tp_{k}+p_{k-1}}{tq_{k}+q_{k-1}}-\dfrac{r_{k+1}p_{k}+p_{k-1}}{r_{k+1}q_{k}+q_{k-1}}\right| \\
    &=\dfrac{r_{k+1}-t}{(tq_{k}+q_{k-1})(r_{k+1}q_{k}+q_{k-1})}.
    \end{aligned}
    $$
    
    Here we used $r_{k+1}\ge a_{k+1}>t$. Therefore, $x_{k,t}$ is closer to $x$ than $x_k$ and becomes a best approximation of the first kind if and only if
    
    $$
    \dfrac{r_{k+1}-t}{tq_{k}+q_{k-1}}<\dfrac{1}{q_k} \iff r_{k+1}<2t+\dfrac{q_{k-1}}{q_k}.
    $$
    
    In this case, there are three possible cases:
    
    1.  If $t<\dfrac{a_{t+1}}{2}$, then $2t<a_{t+1}$. Because both sides are integers, $2t\le a_{k+1}-1$, so $2t+\dfrac{q_{k-1}}{q_k}\le 2t+1\le a_{k+1}\le r_{t+1}$. In this case, $x_{k,t}$ is not a best approximation of the first kind;
    2.  If $t>\dfrac{a_{t+1}}{2}$, then $2t>a_{t+1}$. Because both sides are integers, $2t\ge a_{t+1}+1>r_{t+1}$. In this case, $x_{k,t}$ is a best approximation of the first kind;
    3.  If $a_{t+1}$ is even, there is a third case, namely $t=\dfrac{a_{t+1}}{2}$. The above condition is equivalent to $\dfrac{1}{r_{k+1}}=r_{k+1}-a_{k+1}<\dfrac{q_{k-1}}{q_k}$, i.e. $r_{k+2}>\dfrac{q_k}{q_{k-1}}$.

So, if we arrange all best approximations of the first kind of the real number $x$ in order of increasing denominator, then it is divided into several segments according to its size relationship with $x$. Each segment always consists of several (possibly zero) consecutive intermediate fractions of the same order and always ends with a convergent. Within a segment it always stays on one side of the real number $x$, and the segments are arranged alternately on the two sides of $x$.

??? example "Example: best approximations of the first kind of $\pi$"
    $\pi=[3,7,15,1,292,\cdots]$, so its first 15 best approximations of the first kind with the smallest denominators are:
    
    $$
    \begin{aligned}
    &x_0 = \dfrac{3}{1},\
    x_{0,4} = \dfrac{13}{4},\
    x_{0,5} = \dfrac{16}{5},\
    x_{0,6} = \dfrac{19}{6},\
    x_1 = \dfrac{22}{7},\\
    &x_{1,8} = \dfrac{179}{57},\
    x_{1,9} = \dfrac{201}{64},\
    x_{1,10} = \dfrac{223}{71},\
    x_{1,11} = \dfrac{245}{78},\
    x_{1,12} = \dfrac{267}{85},\\
    &x_{1,13} = \dfrac{289}{92},
    x_{1,14} = \dfrac{311}{99},\
    x_2 = \dfrac{333}{106},\
    x_3 = \dfrac{355}{113},\
    x_{3,146} = \dfrac{52163}{16604}.
    \end{aligned}
    $$

### Best approximation of the second kind

The best approximation of the second kind uses $|qx-p|$ to measure the degree of approximation.

???+ abstract "Best approximation of the second kind"
    For a real number $x$ and a rational number $\dfrac{p}{q}$, if for any $\dfrac{p'}{q'}\neq \dfrac{p}{q}$ with $0<q'\le q$,
    
    $$
    \left|qx-p\right|<\left|q'x-p'\right|,
    $$
    
    then the rational number $\dfrac{p}{q}$ is called a **best approximation of the second kind** of the real number $x$.

The condition for the best approximation of the second kind is equivalent to

$$
\left|x-\dfrac{p}{q}\right|<\dfrac{q'}{q}\left|x-\dfrac{p'}{q'}\right|.
$$

Because $q'\le q$, the condition for the best approximation of the second kind is more stringent than that of the first kind.

The best approximations of the second kind can and can only be convergents.

???+ note "Theorem"
    All best approximations of the second kind must be convergents, and all convergents must be best approximations of the second kind.

??? note "Proof"
    To prove the first part, because a best approximation of the second kind must also be a best approximation of the first kind, we only need to prove that an intermediate fraction that is not a convergent cannot be a best approximation of the second kind. To this end, let $x_{k,t}=\dfrac{p}{q}$ be an intermediate fraction but not a convergent; then, letting $x_{k,t}<x$,
    
    $$
    x_{k-1} < x_{k,t} < x_{k+1} < x < x_{k}.
    $$
    
    Because the error between $x_{k,t}$ and $x$
    
    $$
    |x_{k,t}-x|\ge |x_{k,t}-x_{k+1}|=\left|\dfrac{p}{q}-\dfrac{p_{k+1}}{q_{k+1}}\right|=\dfrac{|pq_{k+1}-p_{k+1}q|}{qq_{k+1}}\ge\dfrac{1}{qq_{k+1}},
    $$
    
    and using the error estimate of convergents, we always have
    
    $$
    |qx_{k,t}-p| \ge \dfrac{1}{q_{k+1}} \ge |q_kx_k-p_k|,
    $$
    
    i.e. the degree of approximation of $x_{k,t}$ is no better than that of $x_k$ which has a smaller denominator, so it cannot be a best approximation of the second kind.
    
    Conversely, to prove the second part, i.e. every convergent $x_k=\dfrac{p_k}{q_k}$ is a best approximation of the second kind. This is to show that for all fractions $\dfrac{p}{q}$ with $q\le q_k$, $|q_kx-p_k|<|qx-p|$. Not considering the half-integer case, we can assume $k>0$. First, by the error estimate of approximating a real number with convergents,
    
    $$
    |q_{k-1} x-p_{k-1}| \ge \frac{1}{q_{k-1}+q_{k}} \ge \dfrac{1}{q_{k+1}}\ge |q_kx-p_k|.
    $$
    
    All inequalities hold with equality if and only if $a_{k+1}=1$ and is the last term of the continued fraction. Not considering such a case, $x_{k-1}=\dfrac{p_{k-1}}{q_{k-1}}$ is strictly inferior to $x_k=\dfrac{p_k}{q_k}$.
    
    Take any fraction $\dfrac{p}{q}\neq x_k$ with $0<q\le q_k$; because of the difference formula $p_{k}q_{k-1} − p_{k-1}q_{k} = (−1)^{k-1}$, by Cramer's rule, the linear system
    
    $$
    \begin{cases}
    \lambda p_k+\mu p_{k-1} = p,\\
    \lambda q_k+\mu q_{k-1} = q
    \end{cases}
    $$
    
    must have a unique integer solution $(\lambda,\mu)$. If $\lambda\mu>0$, then $q>|\lambda|q_k\ge q_k$, a contradiction. Otherwise, $\lambda\mu\le 0$, i.e. $\lambda$ and $\mu$ have opposite signs; then because $q_{k-1}x-p_{k-1}$ and $q_kx-p_k$ also have opposite signs, $\lambda(q_{k-1}x-p_{k-1})$ and $\mu(q_kx-p_k)$ have the same sign, so
    
    $$
    |qx-p|=|\lambda||q_kx-p_k|+|\mu||q_{k-1}x-p_{k-1}|>|q_{k}x-p_{k}|.
    $$
    
    The last inequality is strict, because $x_{k-1}$ is strictly inferior to $x_k$ and $\dfrac{p}{q}\neq x_k$. This shows that $x_k$ is a best approximation of the second kind.

This property shows that convergents are indeed fairly good Diophantine approximations.

### Determination of convergents

The best approximation of the second kind provides a necessary and sufficient condition for determining whether a fraction is a convergent. This shows that we can determine whether a fraction is a convergent by checking the relative degree of its approximation. Legendre's criterion provides a method for determining convergents based on the absolute degree of approximation. The original statement of Legendre's criterion provides a necessary and sufficient condition, but its form is not practical. This section provides a simplified version of Legendre's criterion and explains that it does not miss too many convergents.

???+ note "Theorem (Legendre)"
    For a real number $x$ and a fraction $\dfrac{p}{q}$, if
    
    $$
    \left|x−\dfrac{p}{q}\right|<\dfrac{1}{2q^2}
    $$
    
    then $\dfrac{p}{q}$ must be a convergent of $x$.

??? note "Proof"
    Let $\epsilon\in\{-1,1\}$ and $\theta\in(0,1/2)$ be constants such that
    
    $$
    x−\dfrac{p}{q} = \dfrac{\epsilon\theta}{q^2}
    $$
    
    holds. Expand the rational number $\dfrac{p}{q}$ into a continued fraction $[a_0,a_1,\cdots,a_n]$. Here, a rational number has two continued fraction representations, whose $n$ differ by exactly one, so we can take the representation such that $(-1)^n=\epsilon$, and denote the convergents of this representation as $\dfrac{p_k}{q_k}$. Let the real number $\omega$ satisfy
    
    $$
    x = \dfrac{\omega p_n+p_{n-1}}{\omega q_n+q_{n-1}}.
    $$
    
    Then, we must have
    
    $$
    \dfrac{\epsilon\theta}{q^2} = x−\dfrac{p}{q} = x-\dfrac{p_n}{q_n} = \dfrac{p_{n-1}q_n-p_nq_{n-1}}{(\omega q_n+q_{n-1})q_n} = \dfrac{(-1)^n}{(\omega q_n+q_{n-1})q_n}.
    $$
    
    Hence,
    
    $$
    \theta = \dfrac{q_n}{\omega q_n+q_{n-1}}.
    $$
    
    This shows that
    
    $$
    \omega=\dfrac{1}{\theta}-\dfrac{q_{n-1}}{q_n}>1.
    $$
    
    Expanding $\omega$ into a continued fraction $[b_0,b_1,\cdots]$ as well, then
    
    $$
    x = \dfrac{\omega p_n+p_{n-1}}{\omega q_n+q_{n-1}} = [a_0,a_1,\cdots,a_n,\omega] = [a_0,a_1,\cdots,a_n,b_0,b_1,\cdots].
    $$
    
    This is a valid simple continued fraction, so $\dfrac{p}{q}$ is a convergent of $x$.
    
    This proof actually shows that a necessary and sufficient condition for $\dfrac{p}{q}$ to be a convergent is $\omega>1$ in the above proof, which is exactly the original form of Legendre's criterion.

This criterion shows that as long as the degree of approximation is good enough, it must be a convergent. The next theorem shows that there are enough such good convergents: at least half of the convergents satisfy this condition.

???+ note "Theorem (Valhen)"
    Among any two adjacent convergents of a real number $x$, at least one satisfies
    
    $$
    \left|x−\dfrac{p}{q}\right|<\dfrac{1}{2q^2}.
    $$

??? note "Proof"
    Suppose not. There exists a real number $x$ with two adjacent convergents $x_{k-1}$ and $x_k$ satisfying
    
    $$
    \left|x-\dfrac{p_k}{q_k}\right|\ge \dfrac{1}{2q_{k}^2},\ \left|x-\dfrac{p_{k+1}}{q_{k+1}}\right|\ge \dfrac{1}{2q_{k+1}^2}.
    $$
    
    Because $x$ lies between $x_{k-1}$ and $x_k$,
    
    $$
    \dfrac{1}{2q_{k}^2} + \dfrac{1}{2q_{k+1}^2} \le \left|x-\dfrac{p_k}{q_k}\right| + \left|x-\dfrac{p_{k+1}}{q_{k+1}}\right| = \left|\dfrac{p_k}{q_k}-\dfrac{p_{k+1}}{q_{k+1}}\right| = \dfrac{1}{q_kq_{k+1}}.
    $$
    
    This shows that $q_k=q_{k+1}$. So we must have $k=0$ and $a_1=1$. In this case the first two convergents are $x_0=a_0$ and $x_1=a_0+1$. So the only counterexample to the proposition is a half-integer, which, as explained earlier, this article does not consider.

## Geometric interpretation

Continued fraction theory has an elegant geometric interpretation.

![](./images/continued-convergents-geometry.svg)

As shown in the figure, for a real number $\xi>0$, the line $y=\xi x$ divides the lattice points in the first quadrant (including points on the $x$ and $y$ coordinate axes but excluding the origin, likewise below) into upper and lower parts. For the case of a rational number $\xi$, the points on the line $y=\xi x$ are counted both as points above the line and as points below the line. Consider the convex hulls of these two parts of points. Then, the odd-indexed convergents are the vertices of the convex hull of the upper part, and the even-indexed convergents are the vertices of the convex hull of the lower part. The lattice points on the line segment between two adjacent vertices of the convex hull are exactly the intermediate fractions. The figure shows the convergents and intermediate fractions (gray points) of $\xi=\dfrac{9}{7}$.

Most of the earlier conclusions about continued fractions have corresponding geometric interpretations:

??? note "Geometric interpretation"
    -   Each fraction $\nu=\dfrac{p}{q}$ corresponds to a lattice point $\vec\nu=(q,p)$ in the first quadrant, and the size of the fraction corresponds to the slope of the line connecting it to the origin.
    -   The direction vector of the line $y=\xi x$ is $\vec\xi=(1,\xi)$. Using the concept of the [cross product](../linear-algebra/product.md#the-case-of-two-dimensional-vectors) $(x_1,y_1)\times(x_2,y_2)=x_1y_2-x_2y_1$, we can determine whether a point is above or below the line by the sign of $\vec\xi\times\vec\nu=p-q\xi$. Therefore, points above the line correspond to fractions greater than or equal to $\xi$, and points below the line correspond to fractions less than or equal to $\xi$. The absolute value of the cross product $|\vec\xi\times\vec\nu|$ is proportional to the distance between the point $\vec\nu$ and the line $y=\xi x$
    
        $$
        \dfrac{|p-qx|}{\sqrt{1+\xi^2}},
        $$
    
        corresponding to the degree of approximation of the fraction $\nu$ to the real number $\xi$.
    -   Denoting the point corresponding to the convergent $\xi_k=\dfrac{p_k}{q_k}$ as $\vec\xi_k=(p_k,q_k)$, the recurrence formula can be written as
    
        $$
        \vec\xi_k = a_k\vec\xi_{k-1} + \vec\xi_{k-2}.
        $$
    
        The starting point of the recursion is $\xi_{-2} = (1,0)$ and $\xi_{-1} = (0,1)$.
    -   For an integer $t$, if $0\le t\le a_k$, then the point
    
        $$
        \vec\xi_{k-1,t} = t\vec\xi_{k-1} + \vec\xi_{k-2}
        $$
    
        falls on the line segment connecting the point $\vec\xi_{k-2}$ and the point $\vec\xi_k$. They correspond to the intermediate fractions $\xi_{k-1,t}$.
    -   Using geometric methods, we can construct all convergents and intermediate fractions. Starting from the point $\vec\xi_{-2}=(1,0)$ and the point $\vec\xi_{-1}=(0,1)$, the two points are on opposite sides of the line $y=\xi x$, which means $\vec\xi\times\vec\xi_{-2}$ and $\vec\xi\times\vec\xi_{-1}$ have opposite signs. Add $\vec\xi_{-1}$ to $\vec\xi_{-2}$ by vector addition until it cannot be added further without crossing the line $y=\xi x$, and denote the result as $\vec\xi_0$, which is still on a different side from $\vec\xi_{-1}$. Then add $\vec\xi_0$ to $\vec\xi_{-1}$ until it cannot be added further without crossing the line $y=\xi x$, and denote the result as $\vec\xi_1$, which is still on a different side from $\vec\xi_0$. This process can continue indefinitely, unless within a finite number of steps some $\vec\xi_n$ happens to fall exactly on the line $y=\xi x$. The latter means the vector $\vec\xi$ is collinear with $\vec\xi_n$, i.e. $\xi=\dfrac{p_n}{q_n}$ is a rational point. This process gives the figure in the earlier illustration. Boris Delaunay vividly called this process the nose-stretching algorithm[^nose-streching].
    -   If we need to quickly compute the number of times $\vec\xi_{k-1}$ needs to be added to $\vec\xi_{k-2}$ at each step, we can use the cross product. Because $\vec\xi\times\vec\xi_{k-1}$ and $\vec\xi\times\vec\xi_{k-2}$ have opposite signs, if we denote $\vec\xi_{k-1,t}=t\vec\xi_{k-1}+\vec\xi_{k-2}$ as the result of adding $\vec\xi_{k-1}$ to $\vec\xi_{k-2}$ $t$ times, then $\vec\xi\times\vec\xi_{k-1,t}=t(\vec\xi\times\vec\xi_{k-1})+(\vec\xi\times\vec\xi_{k-2})$ not changing sign means it has not crossed the line. Before the sign changes, the absolute value of $\vec\xi\times\vec\xi_{k-1,t}$ gradually decreases. Denote
    
        $$
        r_{k} = \left|\dfrac{\vec\xi\times\vec\xi_{k-2}}{\vec\xi\times\vec\xi_{k-1}}\right| = -\dfrac{\vec\xi\times\vec\xi_{k-2}}{\vec\xi\times\vec\xi_{k-1}}.
        $$
    
        Then, the maximum number of times it can decrease is
    
        $$
        a_{k} = \lfloor r_{k}\rfloor = \left\lfloor\left|\dfrac{q_{k-1}\xi-p_{k-1}}{q_{k-2}\xi-p_{k-2}}\right|\right\rfloor.
        $$
    
        This is exactly the $k$-th term of the continued fraction expansion. Moreover, $r_k$ is exactly the remainder term of the continued fraction expansion, satisfying the relation:
    
        $$
        r_k = -\dfrac{q_{k-1}\xi-p_{k-1}}{q_{k-2}\xi-p_{k-2}} \iff \xi = \dfrac{p_{k-1}r_k + p_{k-2}}{q_{k-1}r_k+q_{k-2}}.
        $$
    
        This is exactly the continued fraction relation $\xi = [a_0,a_1,\cdots,a_{k-1},r_k]$.
    -   Because the step size of the change in $\vec\xi\times\vec\xi_{k-1,t}$ caused by each vector addition is $|\vec\xi\times\vec\xi_{k-1}|$, the final remaining distance $|\vec\xi\times\vec\xi_k|$ must be strictly less than $|\vec\xi\times\vec\xi_{k-1}|$. This shows that the degree of approximation of the convergents (measured by $|qx-p|$) is strictly better as $k$ increases.
    -   Using the rules of the cross product,
    
        $$
        \vec\xi_{k}\times\vec\xi_{k+1} = \vec\xi_{k}\times(a_{k+1}\vec\xi_k+\vec\xi_{k-1}) = \vec\xi_{k}\times\vec\xi_{k-1} = -\vec\xi_{k-1}\times\vec\xi_{k}.
        $$
    
        By induction,
    
        $$
        \vec\xi_{k}\times\vec\xi_{k+1} = (-1)^{k+2}\vec\xi_{k-2}\times\vec\xi_{k-1} = (-1)^{k}.
        $$
    
        This is exactly the difference formula of convergents $p_{k+1}q_k-p_kq_{k+1}=(-1)^k$.
    -   The area between the upper and lower convex hulls can be divided into several (possibly infinitely many) triangles, where the vertices of each triangle are $\vec\xi_{k-2}$, $\vec\xi_k$, and $\vec 0$. The area of such a triangle is
    
        $$
        \dfrac12|\vec\xi_{k-2}\times\vec\xi_k| = \dfrac12|\vec\xi_{k-2}\times(a_k\vec\xi_{k-1}+\vec\xi_{k-2})| = \dfrac{a_k}{2}|\vec\xi_{k-2}\times\vec\xi_{k-1}| = \dfrac{a_k}{2}.
        $$
    
        By [Pick's theorem](../../geometry/pick.md), this means that if we let $I$ and $B$ be the number of lattice points in the interior and on the boundary of the triangle respectively, then
    
        $$
        I + \dfrac{B}{2} - 1 = \dfrac{a_k}{2}.
        $$
    
        And it is known that the boundary of the triangle already has $\{\vec 0\}\cup\{\vec\xi_{k-1,t}:0\le t\le a_k\}$, a total of $a_k+2$ lattice points. This shows that we must have $I=0$ and $B=a_k+2$. Therefore, there are no more lattice points on the edges of the triangle, and no lattice points in the interior of the triangle. That is, $q_k$ and $p_k$ are reduced, the intermediate fractions are all the lattice points on the edge connecting $\vec\xi_{k-2}$ and $\vec\xi_k$, and all lattice points in the first quadrant are within the upper and lower convex hulls.

The upper and lower convex hulls obtained this way are called Klein polygons. A similar definition can be made in higher-dimensional space, obtaining the [Klein polyhedron](https://en.wikipedia.org/wiki/Klein_polyhedron), which can generalize the concept of continued fractions to higher-dimensional space.

## The tree of continued fractions

Main article: [Stern–Brocot tree and Farey sequence](./stern-brocot.md)

The Stern–Brocot tree is a [binary search tree](../../ds/bst.md) that stores all fractions located between $[0,\infty]$. A finite continued fraction actually encodes the path from the root to the position of some fraction on the Stern–Brocot tree. That is, the continued fraction representation $[a_0,a_1,\cdots,a_{n-1},1]$ of the rational number $x$ means that starting from the tree root $\dfrac{1}{1}$, we need to first move to the right child $a_0$ times, then to the left child $a_1$ times, alternating direction, until we move $a_{n-1}$ times in some direction. Note that here we can only use the continued fraction representation ending in $1$.

Understanding the continued fraction representation as a path on the Stern–Brocot tree, we can obtain an algorithm for comparing the sizes of continued fractions.

???+ example "Comparing sizes of continued fractions"
    Given continued fractions $\alpha=[\alpha_0,\alpha_1,\cdots,\alpha_n]$ and $\beta=[\beta_0,\beta_1,\cdots,\beta_m]$, compare their sizes.

??? note "Solution"
    First convert both continued fraction representations into the form ending in $1$. Suppose the given continued fractions are already in this form, i.e. $\alpha_n=\beta_m=1$. Because even positions (with index starting from $0$) are the number of steps moving right, and odd positions are the number of steps moving left, $\alpha<\beta$ if and only if, when comparing by [lexicographic order](../../string/basic.md#字典序),
    
    $$
    (\alpha_0,-\alpha_1,\alpha_2,\cdots,(-1)^{n-1}\alpha_{n-1},0,\cdots)<(\beta_0,-\beta_1,\beta_2,\cdots,(-1)^{m-1}\beta_{m-1},0,\cdots).
    $$
    
    Compared with the continued fraction representation, we alternately add positive and negative signs, delete the trailing $1$, and pad the positions of insufficient length with $0$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/compare.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/compare.py:core"
        ```

???+ example "Best inner point"
    For $\dfrac{0}{1}\le\dfrac{p_0}{q_0}<\dfrac{p_1}{q_1}\le\dfrac{1}{0}$, find the rational number $\dfrac{p}{q}$ with the smallest $(q,p)$ such that $\dfrac{p_0}{q_0}<\dfrac{p}{q}<\dfrac{p_1}{q_1}$ holds.

??? note "Solution"
    Because the Stern–Brocot tree is both a binary search tree of the fractions in $[0,\infty]$ and a [Cartesian tree](../../ds/cartesian-tree.md) of the pairs $(q,p)$, the problem can almost be transformed into finding the LCA (lowest common ancestor) of two points on the Stern–Brocot tree. But LCA can only handle the case within a closed interval, and the LCA may be an endpoint itself. To avoid extra discussion, we can first construct $\dfrac{p_0}{q_0}+\varepsilon$ and $\dfrac{p_1}{q_1}-\varepsilon$, and then compute the LCA. When the path from the root to a node has already been computed via continued fractions, the LCA only needs to take the longest common path.
    
    To construct $x\pm\varepsilon$, we only need to first move right (left) once at the node $x$, and then move left (right) $\infty$ times. Translating into the language of continued fractions, for a fraction $x=[a_0,a_1,\cdots,a_{n-1},1]$, we know that $x\pm\varepsilon$ must be $[a_0,a_1,\cdots,a_{n-1}+1,\infty]$ and $[a_0,a_1,\cdots,a_{n-1},1,\infty]$, so we only need to compare these two continued fractions and define the larger (smaller) as $x\pm\varepsilon$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/inner-point.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/inner-point.py:core"
        ```

???+ example "[GCJ 2019, Round 2 - New Elements: Part 2](https://github.com/google/coding-competitions-archive/blob/main/codejam/2019/round_2/new_elements_part_2/statement.pdf)"
    Given $N$ pairs of positive integers $(C_i,J_i)$, find a pair of positive integers $(x,y)$ such that $\{C_ix+J_iy\}$ is strictly increasing. Among all pairs meeting the requirement, output the lexicographically smallest one.

??? note "Solution"
    Suppose $A_i=C_i-C_{i-1}$ and $B_i=J_i-J_{i-1}$. The problem is transformed into finding $(x,y)$ such that all $A_ix+B_iy$ are integers. These pairs can be divided into four cases:
    
    1.  The case $A_i,B_i>0$ can be ignored, because we have already assumed $(x,y)>0$;
    2.  The case $A_i,B_i\le 0$ directly outputs "IMPOSSIBLE";
    3.  The case $A_i>0,B_i\le 0$ amounts to the constraint $\dfrac{y}{x}<\dfrac{A_i}{-B_i}$;
    4.  The case $A_i\le 0,B_i>0$ amounts to the constraint $\dfrac{y}{x}>\dfrac{-A_i}{B_i}$.
    
    Therefore, take $\dfrac{p_0}{q_0}$ to be the largest $\dfrac{-A_i}{B_i}$ in the fourth case, and take $\dfrac{p_1}{q_1}$ to be the smallest $\dfrac{A_i}{-B_i}$ in the third case. The original problem becomes finding the lexicographically smallest $(q,p)$ such that $\dfrac{p_0}{q_0}<\dfrac{p}{q}<\dfrac{p_1}{q_1}$ holds.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/gcj-2019.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/gcj-2019.py:core"
        ```

To learn more about the properties and applications of the Stern–Brocot tree, refer to its main article page.

## Linear fractional transformations

Another important concept related to continued fractions is the so-called linear fractional transformation.

???+ abstract "Linear fractional transformation"
    A **fractional linear transformation** is a function $L:\mathbf R\rightarrow\mathbf R$ such that
    
    $$
    L(x) = \dfrac{ax+b}{cx+d},
    $$
    
    where $a,b,c,d\in\mathbf R$ and $ad-bc\neq 0$.

???+ info "About the condition $ad-bc\neq 0$"
    It is easy to verify that when $ad-bc=0$, the function may be undefined or a constant function.

Linear fractional transformations have the following properties:

???+ note "Properties of linear fractional transformations"
    Let $L_1,L_2,L_3$ be linear fractional transformations, and denote the matrix formed by the coefficients of $L_i$ as
    
    $$
    M_i=\begin{pmatrix}a_i & b_i \\ c_i & d_i\end{pmatrix}
    $$
    
    Then they have the following properties:[^pgl2]
    
    1.  The composition $L_1\circ L_2$ and inverse transformation $L_1^{-1}$ of linear fractional transformations are still linear fractional transformations, i.e. all linear fractional transformations form a [group](../algebra/basic.md#groups);
    2.  A linear fractional transformation remains unchanged after its coefficients are multiplied by a nonzero constant, i.e. for any $\lambda\neq 0$, if $M_2=\lambda M_1$, then $L_2=L_1$;
    3.  The coefficient matrix of the composition of linear fractional transformations corresponds to the product of the coefficient matrices, i.e. if $M_1M_2=M_3$, then $L_1\circ L_2=L_3$;
    4.  The coefficient matrix of the inverse transformation of a linear fractional transformation corresponds to the inverse matrix of the coefficient matrix, i.e. if $M_1^{-1}=M_2$, then $L_1^{-1}=L_2$.

??? note "Proof"
    Here we only provide the forms of the composition and inverse transformation of linear fractional transformations. After obtaining these forms, all properties are easy to verify.
    
    The composition of linear fractional transformations $L_1$ and $L_2$:
    
    $$
    \begin{aligned}
    L_1\circ L_2 &= \dfrac{a_1\dfrac{a_2x+b_2}{c_2x+d_2}+b_1}{c_1\dfrac{a_2x+b_2}{c_2x+d_2}+d_1} = \dfrac{(a_1a_2+b_1c_2)x+(a_1b_2+b_1d_2)}{(c_1a_2+d_1c_2)x+(c_1b_2+d_1d_2)}.
    \end{aligned}
    $$
    
    The inverse transformation of the linear fractional transformation $L_1(x)$:
    
    $$
    y = L_1(x) = \dfrac{a_1x+b_1}{c_1x+d_1} \iff x = L_1^{-1}(y) = \dfrac{d_1y - b_1}{-c_1y + a_1}.
    $$

A finite continued fraction $[a_0,a_1,\cdots,a_n]$ can be viewed as the result of the composition of a series of linear fractional transformations. Let

$$
L_i(x) = \dfrac{a_ix+1}{x} = [a_i,x]. 
$$

Then, the finite continued fraction

$$
[a_0,a_1,\cdots,a_n] = L_0\circ L_1\circ \cdots L_n(\infty).
$$

Here, the value of the linear fractional transformation $L(x)=\dfrac{ax+b}{cx+d}$ at $x=\infty$ is $\dfrac{a}{c}$, which is the limit value of the function as $x\rightarrow\pm\infty$.

For a general continued fraction, let the remainder term of the real number $x$ be $r_{k+1}$, i.e. $x=[a_0,\cdots,a_k,r_{k+1}]$; then

$$
x = L_0\circ L_1\circ \cdots L_k(r_{k+1}) = \dfrac{p_kr_{k+1}+p_{k-1}}{q_kr_{k+1}+q_{k-1}}.
$$

This also gives the form of the linear fractional transformation $L_0\circ L_1\circ\cdots\circ L_k$.

Of course we can also directly verify this expression. At the very beginning,

$$
x=\dfrac{x+0}{0x+1}=\dfrac{p_{-1}x+p_{-2}}{q_{-1}x+q_{-2}}.
$$

Subsequently, if $L_0\circ L_1\circ\cdots\circ L_{k-1}$ has the form

$$
\dfrac{p_{k-1}x+p_{k-2}}{q_{k-1}x+q_{k-2}}
$$

then by the composition formula of linear fractional transformations,

$$
L_0\circ L_1\circ\cdots\circ L_{k-1}\circ L_k = \dfrac{(p_{k-1}a_k+p_{k-2})x+p_{k-1}}{(q_{k-1}a_k+q_{k-2})x+q_{k-1}} = \dfrac{p_kx+p_{k-1}}{q_kx+q_{k-1}}.
$$

This inductively gives the above form. Linear fractional transformations also provide another perspective on understanding the recurrence formula and initial conditions.

???+ example "[DMOPC '19 Contest 7 P4 - Bob and Continued Fractions](https://dmoj.ca/problem/dmopc19c7p4)"
    Given a positive integer array $a_1,\cdots,a_n$ and $m$ queries, each query gives $l\le r$ and requires computing the value of $[a_l,\cdots,a_r]$.

??? note "Solution"
    Understanding a continued fraction as the value of the composition of a sequence of linear fractional transformations at $x=\infty$, we only need to be able to query the composition of a segment of linear fractional transformations multiple times. Because each linear fractional transformation can be inverted, we can preprocess prefix sums and query using the difference method, with complexity $O(n+m)$; if modifications are needed, we can also use a structure such as a segment tree to store.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/flt-presum.cpp"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/flt-presum.py"
        ```

### Arithmetic operations on continued fractions

Using linear fractional transformations, we can perform arithmetic operations on continued fractions. This algorithm was first proposed by Gosper.

The cornerstone of the algorithm is computing the linear fractional transformation of a continued fraction. This section takes finite continued fractions as an example, but because the algorithm reads in only finitely many terms of the continued fraction for each output digit, it also applies to infinite continued fractions, and can compute to arbitrary precision. Combined with the earlier continued-fraction comparison algorithm, we can precisely compare the difference of real numbers of arbitrary precision.

???+ example "Linear fractional transformation of a continued fraction"
    Given a linear fractional transformation $L(x)=\dfrac{ax+b}{cx+d}$ and a continued fraction $\alpha=[\alpha_0,\alpha_1,\cdots,\alpha_n]$, find the continued fraction representation $[\beta_0,\beta_1,\cdots,\beta_m]$ of $\beta=L(\alpha)$.

??? note "Solution"
    The basic idea of the algorithm is to determine the value of $\beta_i$ one by one. Denote
    
    $$
    L_\gamma(x) = \gamma+\dfrac{1}{x} = \dfrac{\gamma x+1}{x}.
    $$
    
    Because the continued fraction
    
    $$
    L(\alpha) = L\circ L_{\alpha_0}\circ L_{\alpha_1}\circ \cdots \circ L_{\alpha_n}(\infty),
    $$
    
    we can compute the value of $L(\alpha)$ by gradually composing $L_{\alpha_k}$ onto $L$. But if we want to obtain the continued fraction representation of $L(\alpha)$, then we do not need to fully compute the value of $L(\alpha)$ before finding the continued fraction representation. We can determine the values of $\beta_0,\beta_1,\cdots$ during the process of composing $L_{\alpha_i}$.
    
    For example, suppose we have currently computed
    
    $$
    L\circ L_{\alpha_0}\circ L_{\alpha_1}\circ \cdots \circ L_{\alpha_k}(x) = \dfrac{a_kx+b_k}{c_kx+d_k}
    $$
    
    with $c_k,d_k$ of the same sign. Then, $L\circ L_{\alpha_0}\circ L_{\alpha_1}\circ \cdots \circ L_{\alpha_k}(x)$ is monotonic on $[0,\infty]$ and must take values between $\dfrac{a_k}{c_k}$ and $\dfrac{b_k}{d_k}$. So, if
    
    $$
    \left\lfloor\dfrac{a_k}{c_k}\right\rfloor = \left\lfloor\dfrac{b_k}{d_k}\right\rfloor,
    $$
    
    we can determine that it is the integer part $\beta_0$ of $L\circ L_{\alpha_0}\circ L_{\alpha_1}\circ \cdots \circ L_{\alpha_k}(x)$. In this case, composing $L_{\beta_0}^{-1}$ on the left gives
    
    $$
    L_{\beta_0}^{-1}\circ L\circ L_{\alpha_0}\circ L_{\alpha_1}\circ \cdots \circ L_{\alpha_k}.
    $$
    
    In this case, continuing to add $L_{\alpha_{k+1}},L_{\alpha_{k+2}},\cdots$ allows us to determine the new integer part, i.e. $\beta_1$. Computing this way until we determine the values of all $\beta_j$.
    
    The algorithm requires $c$ and $d$ to have the same sign, because we want to guarantee that the discontinuity point of the function is not within the range $[0,\infty]$. This is always possible, because the definition of a simple continued fraction requires the coefficients (except $\alpha_0$) to all be positive integers. From this, we can prove that $c$ and $d$ must have the same sign within a finite number of steps, and will remain of the same sign afterwards.
    
    In the specific implementation, we only need to maintain the coefficient matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ of the current linear fractional transformation and check whether $c$ and $d$ have the same sign and whether $\dfrac{a}{c}$ and $\dfrac{b}{d}$ have the same integer part. When composing $L_{\alpha_i}$ on the right, we obtain $\begin{pmatrix}a\alpha_i+b&a\\ c\alpha_i+d&c\end{pmatrix}$. If both have the same integer part $\beta_j$, then add $\beta_j$ to the resulting continued fraction and compose $L_{\beta_j}^{-1}$ on the left, which amounts to computing $\begin{pmatrix}c&d\\ a\bmod c & b \bmod d \end{pmatrix}$.

The linear fractional transformation of a continued fraction can already be used to compute the arithmetic operations between a fraction and a continued fraction:

$$
\dfrac{p}{q}\pm x = \dfrac{\pm qx+p}{0x+q},\ \dfrac{p}{q}x = \dfrac{px+0}{0x+q},\ \frac{p}{q}/x = \dfrac{0x+p}{qx+0}.
$$

For arithmetic operations between general continued fractions, we need to use bilinear fractional transformations:

$$
x+y = \dfrac{0xy+x+y+0}{0xy+0x+0y+1},\ xy = \dfrac{1xy+0x+0y+0}{0xy+0x+0y+1},\ \dfrac{x}{y} = \dfrac{0xy+x+0y+0}{0xy+0x+y+0}.
$$

???+ example "Bilinear fractional transformation of continued fractions"
    Given a bilinear fractional transformation $L(x,y)=\dfrac{axy+bx+cy+d}{exy+fx+gy+h}$ and continued fractions $\alpha=[\alpha_0,\alpha_1,\cdots,\alpha_n]$ and $\beta=[\beta_0,\beta_1,\cdots,\beta_m]$, find the continued fraction representation $[\gamma_0,\gamma_1,\cdots,\gamma_\ell]$ of $\gamma=L(\alpha,\beta)$.

??? note "Solution"
    Similar to the case of the single-variable linear fractional transformation, to determine the integer part we only need to guarantee that the integer part of the current linear fractional transformation within $(x,y)\in[0,\infty]\times[0,\infty]$ remains unchanged, i.e. $e,f,g,h$ all have the same sign, and
    
    $$
    \left\lfloor\dfrac{a}{e}\right\rfloor = \left\lfloor\dfrac{b}{f}\right\rfloor = \left\lfloor\dfrac{c}{g}\right\rfloor = \left\lfloor\dfrac{d}{h}\right\rfloor.
    $$
    
    Right-composition is replaced by computing $L(x,y)\mapsto L(L_{\alpha_i}(x),y)$ and $L(x,y)\mapsto L(x,L_{\beta_j}(y))$, which is likewise expressed as a linear transformation of the coefficients. Left-composition is entirely consistent with the single-variable case, requiring only computing the modulo.
    
    Compared with the single-variable case, the bivariate case needs to decide whether to compose $L_{\alpha_i}$ or $L_{\beta_j}$ first. Because the order of composition is unrelated to the final result, we can freely choose the composition order, for example alternately composing $L_{\alpha_i}$ and $L_{\beta_j}$. Or adopt the heuristic rule of prioritizing composing the dimension with the larger ratio difference: if $\left|\dfrac{b}{f}-\dfrac{d}{h}\right|>\left|\dfrac{c}{g}-\dfrac{d}{h}\right|$, then compose $L_{\alpha_i}$ first; otherwise, compose $L_{\beta_j}$ first.

## Periodic continued fractions

Similar to the concept of repeating decimals, if the coefficients of a continued fraction form a cycle, it is called a periodic continued fraction.

???+ abstract "Periodic continued fraction"
    Let the continued fraction $x=[a_0,a_1,a_2,\cdots]$, and suppose there exist a natural number $K$ and a positive integer $L$ such that for any $k\ge K$, $a_k=a_{k+L}$; then the continued fraction $x$ is called a **periodic continued fraction**. The smallest $L$ satisfying this condition is called its minimal positive period, and the sequence $a_{k},\cdots,a_{k+L-1}$ that repeats in the continued fraction is called its period. Using the period, a periodic continued fraction can be written as $x=[a_0,\cdots,a_{k-1},\overline{a_k,\cdots,a_{k+L-1}}]$. If $K$ can be taken as $0$, i.e. $x=[\overline{a_0,\cdots,a_{L-1}}]$, then it is called a **purely periodic continued fraction**, otherwise it is called an **eventually periodic continued fraction**.

### Quadratic irrationals

A concept closely related to periodic continued fractions is the [(real) quadratic irrational](./quadratic.md), i.e. the irrational solution of an integer-coefficient quadratic equation. All quadratic irrationals can be represented in the form

$$
a+b\sqrt D
$$

where $a,b$ are rational numbers and $D$ is a squarefree positive integer. The quadratic irrationals mentioned in this article are all real by default. Moreover, the conjugate of $a+b\sqrt D$ refers to $a-b\sqrt{D}$.

Euler's result shows that all periodic continued fractions are quadratic irrationals.

???+ note "Theorem (Euler)"
    Periodic continued fractions all represent quadratic irrationals.

??? note "Proof"
    For a general periodic continued fraction $x=[a_0,\cdots,a_{k-1},\overline{a_k,\cdots,a_{k+L-1}}]$, we can set $y=[\overline{a_k,\cdots,a_{k+L-1}}]$; then
    
    $$
    \begin{aligned}
    x&=[a_0,\cdots,a_{k-1},y] = L_0(y),\\
    y&=[a_k,\cdots,a_{k+L-1},y] = L_1(y),
    \end{aligned}
    $$
    
    where $L_0(\cdot)$ and $L_1(\cdot)$ are both linear fractional transformations. So, we obtain the equation satisfied by $x$
    
    $$
    x = L_0\circ L_1\circ L_0^{-1}(x). 
    $$
    
    Suppose the linear fractional transformation $L_0\circ L_1\circ L_0^{-1}(x) = \dfrac{ax+b}{cx+d}$; then we obtain the equation satisfied by $x$
    
    $$
    cx^2+(d-a)x-b=0.
    $$
    
    Therefore, periodic continued fractions are all solutions of integer-coefficient quadratic equations. And because infinite continued fractions are all irrational, periodic continued fractions all represent quadratic irrationals.

Lagrange's result shows that the converse also holds, so quadratic irrationals and periodic continued fractions are equivalent.

???+ note "Theorem (Lagrange)"
    A quadratic irrational can be represented as a periodic continued fraction.

??? note "Proof"
    The idea is to prove that the remainder terms will repeat. Let the quadratic irrational $x$ be written in the form
    
    $$
    x = \dfrac{P_0+\sqrt{D}}{Q_0}
    $$
    
    where $P_0,Q_0,D$ are all integers and $Q_0\mid D-P_0^2$. This is always possible, for example the quadratic irrational $x$ can always be written as
    
    $$
    a+b\sqrt{D'} = \dfrac{p_a}{q_a}+\dfrac{p_b}{q_b}\sqrt{D'} = \dfrac{p_aq_b+p_bq_a\sqrt{D'}}{q_aq_b} = \dfrac{p_ap_bq_aq_b+\sqrt{(q_aq_b)^2D'}}{(q_aq_b)^2}
    $$
    
    and then setting $P=p_ap_bq_aq_b$, $Q=(q_aq_b)^2$ and $D=QD'$.
    
    The benefit of writing it in this form is that we can prove that all its remainder terms have a similar form:
    
    $$
    r_k=\dfrac{P_k+\sqrt D}{Q_k},
    $$
    
    where $P_k,Q_k$ are integers and $Q_k\mid D-P_k^2$. Here, the condition $Q_k\mid D-P_k^2$ guarantees that in the numerator of all remainder terms, the coefficient before $\sqrt{D}$ is $1$.
    
    To obtain the form of the remainder term, we can use mathematical induction. When $k=0$, obvious. Assuming we have obtained the form of $r_k$, and setting $a_k=\lfloor r_k\rfloor$,
    
    $$
    r_k = a_k+\dfrac{1}{r_{k+1}}.
    $$
    
    Suppose $r_{k+1}$ also has a similar form, and substitute it together with $r_k$ into the above,
    
    $$
    \dfrac{P_k+\sqrt D}{Q_k} = a_k + \dfrac{Q_{k+1}}{P_{k+1}+\sqrt{D}} = a_k + \dfrac{Q_{k+1}P_{k+1}-Q_{k+1}\sqrt{D}}{P_{k+1}^2-D}.
    $$
    
    Because the way to represent a quadratic irrational as $a+b\sqrt{D}$ is unique, comparing the coefficients on both sides,
    
    $$
    \dfrac{P_k}{Q_k} = a_k+\dfrac{Q_{k+1}P_{k+1}}{P_{k+1}^2-D},\ \dfrac{1}{Q_k}=-\dfrac{Q_{k+1}}{P_{k+1}^2-D}.
    $$
    
    Substituting the second equation into the first, we can solve for $P_{k+1}$:
    
    $$
    \dfrac{P_k}{Q_k} = a_k-\dfrac{P_{k+1}}{Q_k} \iff P_{k+1} = a_kQ_k-P_k.
    $$
    
    Then substituting into the second equation, we can solve for $Q_{k+1}$:
    
    $$
    Q_{k+1} = \dfrac{D-P_{k+1}^2}{Q_k} = \dfrac{D-(a_kQ_k-P_k)^2}{Q_k} = -a_k^2Q_k+2a_kP_k+\dfrac{D-P_k^2}{Q_k}.
    $$
    
    By the induction hypothesis, $Q_k\mid D-P_k^2$, so indeed both $P_{k+1}$ and $Q_{k+1}$ are integers, i.e. $r_{k+1}$ also has the required form.
    
    Finally, prove that the remainder terms can take only finitely many values, so they must repeat. It was already found earlier that the remainder term
    
    $$
    \dfrac{P_k+\sqrt{D}}{Q_k} = r_k = -\dfrac{q_{k-2}x-p_{k-2}}{q_{k-1}x-p_{k-1}}
    $$
    
    and for an irrational number, we always have $r_k>1$. At the same time, its conjugate
    
    $$
    \dfrac{P_k-\sqrt{D}}{Q_k} = r_k^* = -\dfrac{q_{k-2}x^*-p_{k-2}}{q_{k-1}x^*-p_{k-1}} = -\dfrac{q_{k-2}}{q_{k-1}}\dfrac{x^*-\dfrac{p_{k-2}}{q_{k-2}}}{x^*-\dfrac{p_{k-1}}{q_{k-1}}}
    $$
    
    must be less than $0$ for sufficiently large $k$, because
    
    $$
    \dfrac{q_{k-2}}{q_{k-1}}>0,\ \lim_{k\rightarrow\infty}\dfrac{x^*-\dfrac{p_{k-2}}{q_{k-2}}}{x^*-\dfrac{p_{k-1}}{q_{k-1}}}=\dfrac{x^*-x}{x^*-x}=1.
    $$
    
    This shows that
    
    $$
    \dfrac{2\sqrt{D}}{Q_k} = r_k-r_k^*>1 \iff 0<Q_k\le 2\sqrt{D}.
    $$
    
    Therefore, $Q_k$ can take only finitely many values. Furthermore,
    
    $$
    D-P_{k}^2=Q_kQ_{k-1}>0 \iff |P_k|<\sqrt{D},
    $$
    
    so $P_k$ can also take only finitely many values. Therefore, the remainder term $r_k$ has only finitely many possible values, and must repeat within infinitely many terms.

The proof of the theorem also provides a recurrence formula for computing the remainder terms of a quadratic irrational:

???+ note "Recurrence formula for the remainder terms of a quadratic irrational"
    A quadratic irrational can always be represented in the form
    
    $$
    x=\dfrac{P_0+\sqrt{D}}{Q_0}
    $$
    
    with $Q_0\mid D-P^2_0$. In its remainder term
    
    $$
    r_{k}=\dfrac{P_k+\sqrt{D}}{Q_k}
    $$
    
    $P_k,Q_k$ are both integers and satisfy the recurrence relation
    
    $$
    \begin{aligned}
    P_{k+1} &= a_kQ_k-P_k,\\
    Q_{k+1} &= \dfrac{D-P_{k+1}^2}{Q_k}.
    \end{aligned}
    $$

This recurrence formula can be directly used for computing the continued fraction of a quadratic irrational, and by the proof of the theorem, $|P_k|<\sqrt{D}$ and $Q_k\le 2\sqrt{D}$. The complexity of this algorithm depends on the length of the period, and the latter can be proven to be $O(\sqrt{D}\log D)$[^period-surd].

???+ example "Quadratic irrational"
    Given a quadratic irrational $\alpha=\dfrac{x+y\sqrt{n}}{z}$, find its continued fraction representation. Here, $x,y,z,n\in\mathbf Z$ and $n>0$ is not a perfect square.

??? note "Solution"
    First represent the quadratic irrational in the above form, and then compute using the recurrence formula. The terms of the continued fraction are given by $a_k=\lfloor r_k\rfloor$. To find the period, we need to store the index of the first occurrence of $(P_k,Q_k)$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/quadratic-irrational.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/quadratic-irrational.py:core"
        ```

???+ example "[Tavrida NU Akai Contest - Continued Fraction](https://timus.online/problem.aspx?space=1&num=1814)"
    Given $x$ and $k$, with $x$ not a perfect square and $0\le k\le 10^9$. Find the $k$-th convergent $x_k$ of $\sqrt{x}$.

??? note "Solution"
    First use the above algorithm to solve for the period of $\sqrt{x}$, represent the period as a linear fractional transformation, and then we can use [fast exponentiation](../binary-exponentiation.md) to obtain the value of $x_k$. Of course, for the parts that have not entered the period and less than one period, we need to handle them separately.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/surd-convergent.cpp"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/surd-convergent.py"
        ```

### Purely periodic continued fractions

Being a quadratic irrational is a necessary and sufficient condition for having a periodic continued fraction representation; the discussion in this section gives a necessary and sufficient condition for a real number to have a purely periodic continued fraction representation.

First, because a purely periodic continued fraction has a form similar to a finite continued fraction, we can perform a "reverse-order" operation. Similar to the reverse-order theorem, the continued fraction representation obtained this way has a definite relationship with the original continued fraction representation.

???+ note "Theorem (Galois)"
    For a purely periodic continued fraction
    
    $$
    x = \left[\overline{a_0,a_1,\cdots,a_{\ell}}\right],
    $$
    
    denote
    
    $$
    x' = \left[\overline{a_{\ell},\cdots,a_1,a_0}\right].
    $$
    
    Then $x$ and $x'$ are mutual "reciprocal negative conjugates", i.e. the negative of the reciprocal of the conjugate of $x$ is $x'$.

??? note "Proof"
    Because $\ell+1$ is not required to be the minimal positive period, suppose $\ell>0$. By the reverse-order theorem,
    
    $$
    \begin{aligned}
    \dfrac{p_\ell}{p_{\ell-1}} &= [a_\ell,\cdots,a_1,a_0] = \dfrac{p'_\ell}{q'_\ell},\\
    \dfrac{q_\ell}{q_{\ell-1}} &= [a_\ell,\cdots,a_1] = \dfrac{p'_{\ell-1}}{q'_{\ell-1}}.
    \end{aligned}
    $$
    
    Because both sides of the equations are reduced fractions,
    
    $$
    p'_\ell = p_\ell,\ q'_\ell = p_{\ell-1},\ p'_{\ell-1}=q_\ell,\ q'_{\ell-1} = q_{\ell-1}.
    $$
    
    For the purely periodic continued fraction $x$, its $(\ell+1)$-th remainder term is exactly $x$, so
    
    $$
    x = \dfrac{xp_\ell+p_{\ell-1}}{xq_\ell+q_{\ell-1}}.
    $$
    
    So it satisfies the quadratic equation
    
    $$
    q_\ell x^2+(q_{\ell-1}-p_\ell)x-p_{\ell-1} = 0.
    $$
    
    Similarly, $x'$ satisfies the quadratic equation
    
    $$
    q'_\ell(x')^2+(q'_{\ell-1}-p'_\ell)x'-p'_{\ell-1} = 0.
    $$
    
    Using the relations of the coefficients, this equation can be written as
    
    $$
    p_{\ell-1}(x')^2+(q_{\ell-1}-p_\ell)x'-q_\ell = 0.
    $$
    
    Let $y=-\dfrac{1}{x'}$; then $x$ and $y$ satisfy the same equation. But $x>0>y$, so they are not the same root, but are mutually conjugate, which proves the original proposition.

Using this observation, Galois further gave a necessary and sufficient condition for a quadratic irrational to have a purely periodic continued fraction representation.

???+ note "Theorem (Galois)"
    A quadratic irrational $x$ can be represented as a purely periodic continued fraction if and only if $x>1$ and its conjugate $-1<x^*<0$.

??? note "Proof"
    If $x$ is a purely periodic continued fraction, then using the earlier notation, $a_0=a_{\ell+1}\ge 1$, so $x>1$. And because its reciprocal negative conjugate is also a periodic continued fraction, its conjugate $x^*$ satisfies $-\dfrac{1}{x^*}>1$, i.e. $-1<x^*<0$. This proves that purely periodic continued fractions all satisfy this condition.
    
    Conversely, suppose the quadratic irrational $x>1$ and $-1<x^*<0$. For the remainder term $r_k$ of $x$, there is the recurrence relation
    
    $$
    r_k = a_k+\dfrac{1}{r_{k+1}}.
    $$
    
    Both sides are quadratic irrationals; taking conjugates,
    
    $$
    r_{k}^* = a_k+\dfrac{1}{r_{k+1}^*}.
    $$
    
    Using this recurrence relation, we can prove that $-1<r_{k}^*<0$ holds for all $k\ge 0$.
    
    First, for $k=0$, $-1<r_0^*=x_0^*<0$, obvious. For $k\ge 0$, by the definition of a simple continued fraction and $x>1$, $a_k\ge 1$. So, assuming $-1<r_k^*<0$,
    
    $$
    -1<-\dfrac{1}{a_k}< r_{k+1}^* = \dfrac{1}{r_k^*-a_k} < -\dfrac{1}{1+a_k} < 0.
    $$
    
    This inductively proves that $-1<r_{k}^*<0$ holds for all $k\ge 0$. Therefore,
    
    $$
    a_k = -\dfrac{1}{r_{k+1}^*}+r_k^* = \left\lfloor-\dfrac{1}{r_{k+1}^*}\right\rfloor.
    $$
    
    Because a quadratic irrational must be a periodic continued fraction, there exist a positive integer $L$ and at least some sufficiently large $k$ with $r_{k}=r_{k+L}$. But in this case we must also have
    
    $$
    a_{k-1} = \left\lfloor-\dfrac{1}{r_{k}^*}\right\rfloor = \left\lfloor-\dfrac{1}{r_{k+L}^*}\right\rfloor = a_{k+L-1}.
    $$
    
    Hence,
    
    $$
    r_{k-1} = a_{k-1}+\dfrac{1}{r_k} = a_{k+L-1}+\dfrac{1}{r_{k+L}} = r_{k+L-1}.
    $$
    
    This means that the smallest $k$ making $r_{k}=r_{k+L}$ hold must be $0$. That is, $x$ can be represented as a purely periodic continued fraction.

Galois's theorem reveals the pattern of the continued fraction representation of a pure quadratic surd—that is, a quadratic irrational of the form $\sqrt{r}$.

???+ note "Corollary"
    For a rational number $r>1$, if $\sqrt{r}$ is irrational, then
    
    $$
    \sqrt{r} = [\lfloor\sqrt{r}\rfloor,\overline{a_1,\cdots,a_{\ell},2\lfloor\sqrt{r}\rfloor}]
    $$
    
    and for any $1\le k\le\ell$, $a_k = a_{\ell+1-k}$.

??? note "Proof"
    For the quadratic irrational $\sqrt{r}$, because $\lfloor\sqrt{r}\rfloor+\sqrt{r}>1$ and $-1<\lfloor\sqrt{r}\rfloor-\sqrt{r}<0$, $\lfloor\sqrt{r}\rfloor+\sqrt{r}$ is a purely periodic continued fraction:
    
    $$
    \lfloor\sqrt{r}\rfloor+\sqrt{r} = [\overline{2\lfloor\sqrt{r}\rfloor,a_1,\cdots,a_\ell}].
    $$
    
    By the above theorem, its reciprocal negative conjugate has the form
    
    $$
    \dfrac{1}{\sqrt{r}-\lfloor\sqrt{r}\rfloor} = [\overline{a_\ell,\cdots,a_1,2\lfloor\sqrt{r}\rfloor}].
    $$
    
    By the basic properties of continued fractions,
    
    $$
    \sqrt{r}=\lfloor\sqrt{r}\rfloor+\dfrac{1}{\dfrac{1}{\sqrt{r}-\lfloor\sqrt{r}\rfloor}}=[\lfloor\sqrt{r}\rfloor,\overline{a_\ell,\cdots,a_1,2\lfloor\sqrt{r}\rfloor}].
    $$
    
    But also from the continued fraction representation of $\lfloor\sqrt{r}\rfloor+\sqrt{r}$,
    
    $$
    \sqrt{r} = -\lfloor\sqrt{r}\rfloor+\left(\lfloor\sqrt{r}\rfloor+\sqrt{r}\right) = [\lfloor\sqrt{r}\rfloor,\overline{a_1,\cdots,a_\ell,2\lfloor\sqrt{r}\rfloor}].
    $$
    
    Because the continued fraction representation of an irrational number is unique, comparing the middle coefficients we know that $a_k=a_{\ell+1-k}$ holds for all $1\le k\le\ell$.

??? example "Example: continued fraction expansion of $\sqrt{74}$"
    The continued fraction of $\sqrt{74}$ can be computed as follows: (this is only for illustration; programmatic computation should use the recursive algorithm mentioned earlier)
    
    $$
    \begin{aligned}
    \sqrt{74}&=8+(-8)+\sqrt{74}=\left[8,\frac{8+\sqrt{74}}{10}\right]\\
    &=\left[8,1+\frac{-2+\sqrt{74}}{10}\right]=\left[8,1,\frac{2+\sqrt{74}}{7}\right]\\
    &=\left[8,1,1+\frac{-5+\sqrt{74}}{7}\right]=\left[8,1,1,\frac{5+\sqrt{74}}{7}\right]\\
    &=\left[8,1,1,1+\frac{-2+\sqrt{74}}{7}\right]=\left[8,1,1,1,\frac{2+\sqrt{74}}{10}\right]\\
    &=\left[8,1,1,1,1+\frac{-8+\sqrt{74}}{10}\right]=\left[8,1,1,1,1,8+\sqrt{74}\right]\\
    &=\left[8,1,1,1,1,16+(-8)+\sqrt{74}\right]=\left[8,\overline{1,1,1,1,16}\right]
    \end{aligned}
    $$
    
    The various remainder terms are:
    
    $$
    \begin{alignedat}{3}
    r_1&=\frac{8+\sqrt{74}}{10}&&=\left[\overline{1,1,1,1,16}\right]\\
    r_2&=\frac{2+\sqrt{74}}{7}&&=\left[\overline{1,1,1,16,1}\right]\\
    r_3&=\frac{5+\sqrt{74}}{7}&&=\left[\overline{1,1,16,1,1}\right]\\
    r_4&=\frac{2+\sqrt{74}}{10}&&=\left[\overline{1,16,1,1,1}\right]\\
    r_5&=8+\sqrt{74}&&=\left[\overline{16,1,1,1,1}\right]
    \end{alignedat}
    $$
    
    By Galois's conclusion, the periodic parts of the remainder terms $r_k$ and $r_{L+1-k}$ are exactly reversed, so they are mutual reciprocal negative conjugates. If the period length $L$ of $\sqrt{D}$ is odd, then the middle term is its own reciprocal negative conjugate; if the period length $L$ is even, there is no such term. The discussion in the Pell equation section will explain that the parity of the period length determines whether the equation $x^2-Dy^2=-1$ has a solution.

The continued fraction expansion of the quadratic irrational $\sqrt{D}$ is mainly applied in solving the [Pell equation](./pell-equation.md).

## Example problems

After mastering the basic concepts, we need to study some specific example problems to understand how to apply the continued fraction method in competitive programming.

???+ example "Convex hull below a line"
    Given $r=[a_0,a_1,\cdots,a_n]$, find the convex hull of the set of lattice points $(x,y)$ satisfying $0\le x\le N$ and $0\le y\le rx$.

??? note "Solution"
    For the unbounded set $x\ge 0$, the upper convex hull is the line $y=rx$ itself. However, as shown in the figure below, if we also require $x\le N$, then the upper convex hull will eventually deviate from the line.
    
    ![](./images/lattice-hull.svg)
    
    Starting from $(0,0)$, we can find all lattice points of the upper convex hull from left to right. Suppose the last lattice point of the currently found upper convex hull is $(x,y)$. Now we want to find the next lattice point $(x',y')$. The vertex $(x',y')$ is to the upper right of $(x,y)$; denote $(\Delta x,\Delta y)=(x'-x,y'-y)$ as the difference of the two. Then, we must have
    
    $$
    0<\Delta x\le N-x,\ 0\le \Delta y\le r\Delta x.
    $$
    
    The second inequality holds, because the condition $\Delta y>r\Delta x$ contradicts the fact that $(x,y)$ is already on the upper convex hull. Observing the conditions that $(\Delta x,\Delta y)$ needs to satisfy, for different points $(x,y)$, only the upper bound of $\Delta x$ changes. So, as long as we can solve this subproblem, we can recursively find all lattice points of the original problem.
    
    Then, consider the solution of the subproblem. Compared with the original problem, the subproblem amounts to changing the upper bound of $x$ to $N'$ and finding the first lattice point in the upper convex hull adjacent to the origin. Denote the solution of the subproblem as $(q,p)$. Then, $p$ and $q$ must be coprime (otherwise it is not the first lattice point), and the slope $\dfrac{p}{q}$ of the line connecting it to the origin is the largest among all lattice points below the line $y=rx$ with horizontal coordinate not exceeding $N'$ (otherwise it is not on the convex hull). Combined with the earlier [geometric interpretation](#geometric-interpretation), such a point $(x,y)$ must correspond to a lower intermediate fraction of $r$. Because the lower intermediate fraction with a larger denominator is closer to $r$, the solution $(q,p)$ of the subproblem corresponds to the one with the largest denominator among all lower intermediate fractions with denominator not exceeding $N'$.
    
    Of course, in actual solving, there is no need to recompute such a lower intermediate fraction for each subproblem. We should first find all convergents, which amounts to providing a method to traverse all lower intermediate fractions. Then traverse the lower intermediate fractions from large denominator to small, each time trying to add it to the previous lattice point $(x,y)$, until it cannot be added, before continuing to try the next lower intermediate fraction.
    
    There are some obvious optimizations here. First, for a lower intermediate fraction $(q,p)$, there must exist an odd number $k$ and $0\le t<a_k$ such that $(q,p)=(q_{k-1},p_{k-1})+t(q_k,p_k)$. We only need to find the largest $t$ such that $q_{k-1}+tq_k+x\le N$ holds, i.e. $t=\left\lfloor\dfrac{N-q_{k-1}-x}{q_k}\right\rfloor$. Do not worry about $t$ going out of bounds, because the larger lower convergent $(q_{k+2},p_{k+2})$ has already been added. And each time we determine the number of additions, we directly compute $\left\lfloor\dfrac{N-x}{q}\right\rfloor$, without trying one by one.
    
    The complexity of the optimized algorithm is $O(n)$. Although there may be many lattice points corresponding to lower intermediate fractions, not many actually become increments. Below we show that among all lower intermediate fractions $(q,p)=(q_{k-1},p_{k-1})+t(q_k,p_k)$ with $0\le t<a_k$, at most two increments will appear. Suppose an increment indeed appears among these lower intermediate fractions; then we must have $q_{k-1}\le N-x<q_{k+1}$. Suppose $t=\left\lfloor\dfrac{N-q_{k-1}-x}{q_k}\right\rfloor$. If $t=0$, then the increment is $\Delta x=q_{k-1}$, so after adding the increment, $N-x'<q_{k-1}$, and no new increment will appear among these lower intermediate fractions; if $t>0$, then after adding the increment, we must have $N-x'=(N-q_{k-1}-x)\bmod q_k<q_k$, and even if a new increment appears in the same segment of lower intermediate fractions, the next time can only have $t'=0$. Therefore, in such a segment of lower intermediate fractions, at most two increments can appear. This shows that the total time complexity is $O(n)$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/hull-under-line.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/hull-under-line.py:core"
        ```

???+ example "[Timus - Crime and Punishment](https://timus.online/problem.aspx?space=1&num=1430)"
    Given positive integers $A,B,N \le 2\times 10^9$, find $x,y\ge 0$ such that $Ax+By\le N$ and $Ax+By$ is as large as possible.

??? note "Solution"
    This problem has a solution of complexity $O(\sqrt N)$: suppose $A\ge B$; because $A(B+x)+By=Ax+B(A+y)$, we only need to search for the answer in $x\le\min\{N/A, B\}$. This is enough to pass this problem. But if we apply the continued fraction method, then the time complexity can be reduced to $O(\log N)$.
    
    For convenience of discussion, first change the sign of $x$ via the substitution $x\mapsto\left\lfloor N/A\right\rfloor-x$. Let $C=N\bmod A$ and $M=\left\lfloor N/A\right\rfloor$; then the original problem is transformed into finding the optimal $(x,y)$ under the conditions $0\le x\le M$ and $By-Ax\le C$ such that $By-Ax$ is maximized. For each fixed $x$, the optimal value of $y$ is $\left\lfloor\dfrac{Ax+C}{B}\right\rfloor$.
    
    What we want to show next is that this problem has a solution similar to the previous example. But unlike the previous example which uses lower intermediate fractions to deviate from the line, this problem needs to use upper intermediate fractions to approach the line. Specifically, the value of $C-(By-Ax)$ is proportional to the distance between the point $(x,y)$ and the line $By-Ax=C$. To maximize $By-Ax$ is equivalent to minimizing this distance. The goal of the algorithm is to find the feasible lattice point below the line $By-Ax=C$ closest to it. The idea of the algorithm is to start from the leftmost point, search along the upper convex hull of these lattice points, and gradually reduce the distance to the line until we obtain the optimal solution.
    
    In the coordinate system of $(x,y)$, the algorithm starts from $(0,\lfloor C/B\rfloor)$, recursively finds and adds the optimal increment $(\Delta x,\Delta y)$, and guarantees that the point after addition is closer to the line $By-Ax=C$ than before, but cannot reach the other side of the line, and cannot make the horizontal coordinate greater than $M$. Let the obtained point be $(x,y)$; then the conditions that the increment $(\Delta x,\Delta y)$ satisfies are
    
    $$
    0<B\Delta y-A\Delta x\le C-(By-Ax),\ 0<\Delta x\le M-x.
    $$
    
    Following the idea of searching along the lower convex hull, we only need to find the point with the smallest $\Delta x$ among the points satisfying these conditions. Rewrite the first inequality as
    
    $$
    \Delta y \le \dfrac{A}{B}\Delta x+\dfrac{C-(By-Ax)}{B}.
    $$
    
    Combined with the earlier [geometric interpretation](#geometric-interpretation), as long as the following constant term is less than $1$, then among the lattice points $(\Delta x,\Delta y)$ satisfying this inequality, the one with the smallest horizontal coordinate must correspond to some upper intermediate fraction. This is because it is the best at approaching some real number from above among all fractions with denominator not exceeding its denominator, which can only be an upper intermediate fraction. And each time an increment is added, it makes the upper bound of $\Delta y$ tighter, which means we must examine upper intermediate fractions with larger denominators.
    
    Following the idea of the previous example. Examine all upper intermediate fractions from small denominator to large; if we can find an upper intermediate fraction whose horizontal and vertical coordinates are both within bounds, add it and update the corresponding upper bound. When all feasible upper intermediate fractions have been added, the obtained result is the optimal solution. Compared with before, this problem needs to simultaneously guarantee that both the horizontal and vertical coordinates are within bounds, which requires extra care. Based on an argument similar to the previous example, but this time using $B\Delta y-A\Delta x$ instead of the previous $\Delta x$, we can show that the complexity of this algorithm is $O(\log\min\{A,B\})$.
    
    === "C++"
        ```py
        --8<-- "docs/math/code/continued-fraction/closest-dio.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/closest-dio.py:core"
        ```

???+ example "[June Challenge 2017 - Euler Sum](https://www.codechef.com/problems/ES)"
    Find the value of $\sum\limits_{x=1}^N \lfloor \mathrm{e}x \rfloor$, where $\mathrm{e}$ is the base of the natural logarithm.
    
    Hint: $e = [2,1,2,1,1,4,1,1,6,1,\cdots,1,2n,1, \cdots]$.[^continued-fraction-of-e]

??? note "Solution"
    This sum equals the number of lattice points in the set $\{(x,y):1\le x\le N,1\le y\le\mathrm{e}x\}$. After constructing the convex hull of the lattice points below the line $y=\mathrm{e}x$, we can use [Pick's theorem](../../geometry/pick.md) to compute the number of lattice points. The time complexity is $O(\log N)$.
    
    The original problem requires $N \le 10^{4000}$. Here the C++ code is only for illustration and does not implement a high-precision computation class.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/sum-floor.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/sum-floor.py:core"
        ```

???+ example "[NAIPC 2019 - It's a Mod, Mod, Mod, Mod World](https://open.kattis.com/problems/itsamodmodmodmodworld)"
    Given positive integers $p,q,n$, find the value of $\sum\limits_{i=1}^n [pi \bmod q]$.

??? note "Solution"
    Because the sum can be transformed into
    
    $$
    \sum_{i=1}^n [pi \bmod q] 
    =\sum_{i=1}^n\left(pi - q\left\lfloor\dfrac{pi}{q}\right\rfloor\right) = \dfrac{pn(n+1)}{2} - q\sum_{i=1}^n\left\lfloor\dfrac{p}{q}i\right\rfloor,
    $$
    
    this problem can be transformed into the previous problem, only using $\dfrac{p}{q}$ instead of $\mathrm{e}$. The time complexity of a single query is $O(\log\min\{p,q\})$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/mod-mod-mod.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/mod-mod-mod.py:core"
        ```

???+ example "[Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)"
    Given positive integers $N,M,A,B$, find the value of $\displaystyle\sum_{i=0}^{N-1} \left\lfloor \frac{A \cdot i + B}{M} \right\rfloor$.

??? note "Solution"
    This is the most complex problem so far. It can be computed via the [Euclidean-like algorithm](./euclidean.md). Here we give an algorithm based on continued fractions, with time complexity $O(\log\min\{A,B\})$.
    
    We can construct the convex hull of all lattice points below the line $y=\dfrac{Ax+B}{M}$ with $0\le x< N$, and use Pick's theorem to compute the number of lattice points. The case $B=0$ has already been solved. For the general case, we can proceed in two steps. First gradually approach the line by adding upper intermediate fractions (i.e. the second example), until we find the point closest to the line, and then gradually move away from the line by adding lower intermediate fractions (i.e. the first example).
    
    === "C++"
        ```py
        --8<-- "docs/math/code/continued-fraction/sum-floor-axbc.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/sum-floor-axbc.py:core"
        ```

???+ example "[OKC 2 - From Modular to Rational](https://codeforces.com/gym/102354/problem/I)"
    There is an unknown rational number $\dfrac{p}{q}$ with $1\le p, q\le 10^9$; we can query the value of $pq^{-1}$ modulo some prime $m\in[10^9,10^{12}]$. Determine the values of $p$ and $q$ within no more than ten queries.
    
    This problem is equivalent to finding the $x$ in $[1,N]$ that minimizes $Ax\bmod M$.

??? note "Solution"
    By the [Chinese Remainder Theorem](./crt.md), querying the result modulo several primes amounts to querying the result modulo the product of these primes. Therefore, this problem can be viewed as querying the result of the fraction modulo a sufficiently large modulus $m$, and requiring us to determine the numerator and denominator of the fraction.
    
    For some modulus $m$, the pair $(p,q)$ making $qr\equiv p\pmod m$ hold may not be unique. Suppose $(p_1,q_1)$ and $(p_2,q_2)$ both make this equation hold; then we must have $(p_1q_2-p_2q_1)r\equiv 0\pmod m$. By the construction of $r$, $r$ is coprime with $m$, so $p_1q_2-p_2q_1\equiv 0\pmod m$, i.e. $m\mid(p_1q_2-p_2q_1)$. If $p_1q_2-p_2q_1$ is not zero, then its absolute value is at least $m$. The problem limits $p,q\in[1,10^9]$, which means this difference should not exceed $10^{18}$, so as long as we take $m>10^{18}$, we can guarantee that the $(p,q)$ found is unique.
    
    Now the problem reduces to: given a modulus $m$ and a remainder $r$, find a pair of positive integers $(p,q)$ not exceeding $n$ such that $qr\equiv p\pmod m$. Knowing that such a solution is unique, we actually only need to find the $q\in[1,n]$ that minimizes $qr\bmod m$, because in this case there is exactly one $q$ making the remainder not exceed $n$. This is exactly the equivalent statement mentioned earlier.
    
    In the coordinate system of $(q,k)$, this amounts to finding the lattice point closest to the line $qr-km=0$ from below with $q\in[1,n]$, because the remainder $qr\bmod m$ is proportional to the distance between the lattice point and the line. Combined with the earlier [geometric interpretation](#geometric-interpretation), such a lattice point must correspond to some lower intermediate fraction of the rational fraction $\dfrac{r}{m}$. The algorithm complexity is $O(\log\min\{r,m\})$.
    
    === "C++"
        ```cpp
        --8<-- "docs/math/code/continued-fraction/recover-fraction.cpp:core"
        ```
    
    === "Python"
        ```py
        --8<-- "docs/math/code/continued-fraction/recover-fraction.py:core"
        ```

## Exercises

-   [UVa OJ - Continued Fractions](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=775)
-   [ProjectEuler+ #64: Odd period square roots](https://www.hackerrank.com/contests/projecteuler/challenges/euler064/problem)
-   [「LibreOJ NOI Round #2」单枪匹马](https://loj.ac/p/573)
-   [Codeforces Round #184 (Div. 2) - Continued Fractions](https://codeforces.com/contest/305/problem/B)
-   [Codeforces Round #201 (Div. 1) - Doodle Jump](https://codeforces.com/contest/346/problem/E)
-   [Codeforces Round #325 (Div. 1) - Alice, Bob, Oranges and Apples](https://codeforces.com/contest/585/problem/C)
-   [POJ Founder Monthly Contest 2008.03.16 - A Modular Arithmetic Challenge](http://poj.org/problem?id=3530)
-   [2019 Multi-University Training Contest 5 - fraction](http://acm.hdu.edu.cn/showproblem.php?pid=6624)
-   [SnackDown 2019 Elimination Round - Election Bait](https://www.codechef.com/SNCKEL19/problems/EBAIT)
-   [Luogu P5179. Fraction](https://www.luogu.com.cn/problem/P5179)
-   [Luogu P7739. \[NOI2021\] 密码箱](https://www.luogu.com.cn/problem/P7739)

## References and further reading

-   Hardy, G. H., Wright, E. M., Heath-Brown, R., & Silverman, J. (2008). An Introduction to the Theory of Numbers. Oxford Mathematics.
-   朱尧辰，王连祥《丢番图逼近引论》
-   [FatFish 的博客 - 连分数入门](https://chaoli.club/index.php/2756)
-   [Simple continued fraction - Wikipedia](https://en.wikipedia.org/wiki/Simple_continued_fraction)
-   [Periodic continued fraction - Wikipedia](https://en.wikipedia.org/wiki/Periodic_continued_fraction)
-   [Gosper's original notes on continued fraction arithmetic algorithms](https://perl.plover.com/yak/cftalk/INFO/gosper.txt)
-   [Understanding Bill Gosper's continued fraction arithmetic (implemented in Python)](https://hsinhaoyu.github.io/cont_frac/)

**The main content of this page is translated from the blog post [Continued fractions](https://cp-algorithms.com/algebra/continued-fractions.html), under the CC-BY-SA 4.0 license, with modifications.**

[^one-representation]: The natural number $1$ has only the non-standard representation: $1=[1]=[0,1]$.

[^continuant]: The translated name comes from Section 6.7 of *Concrete Mathematics* translated by Zhang Mingyao and Zhang Fan.

[^sqrt5]: Here we cannot assume by default that the reduced fraction $\dfrac{p}{q}$ must be a convergent, although Legendre's theorem shows that $\dfrac{p}{q}$ can indeed only be some convergent. For the case of convergents, it can be proven by starting from the error of approximating a real number with convergents.

[^semi-range]: Different literature may handle differently whether the value range of $t$ here includes the endpoints.

[^semiconvergent]: When $t=0$, it should be understood as a formal continued fraction, amounting to truncating to the second-to-last term of the continued fraction.

[^nose-streching]: This term is not a technical term. It may be transliterated from the Russian-language reference [ЦЕПНЫЕ ДРОБИ](https://old.mccme.ru/free-books/mmmf-lectures/book.14-full.pdf), in the section Алгоритм «вытягивания носов».

[^pgl2]: These properties show that the group of all linear fractional transformations is isomorphic to the [projective linear group](https://en.wikipedia.org/wiki/Projective_linear_group) $PGL_2(\mathbf R)$.

[^period-surd]: For the proof, see the references of the [Wikipedia page](https://en.wikipedia.org/wiki/Periodic_continued_fraction#Length_of_the_repeating_block).

[^continued-fraction-of-e]: For the proof of the continued fraction expansion of the base of the natural logarithm $\mathrm{e}$, one can refer to [here](https://proofwiki.org/wiki/Continued_Fraction_Expansion_of_Euler%27s_Number).
