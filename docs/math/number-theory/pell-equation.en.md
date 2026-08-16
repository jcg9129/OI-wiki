Prerequisite knowledge: [continued fractions](./continued-fraction.md), [quadratic fields](./quadratic.md)

## Introduction

This article discusses solving the (generalized) Pell equation. The generalized Pell equation refers to the indeterminate equation in $x$ and $y$

$$
x^2-Dy^2=N,
$$

where $D$ is a positive integer that is not a perfect square[^not-square], and $N$ is a nonzero integer. The narrow-sense Pell equation specifically refers to the special cases $N=1$ or $N=\pm 1$, and sometimes also includes the case $N=\pm 4$. The generalized Pell equation is closely related to finding a quadratic integer of norm $N$ in a real quadratic integer ring, and these cases often called the (narrow-sense) Pell equation can be viewed as finding units in a real quadratic integer ring.

When this article refers to the Pell equation, it specifically means the case $N=1$. Correspondingly, the case $N=-1$ is called the negative Pell equation[^neg-pell].

## Structure of the solutions

The integer solutions $(x,y)$ of the generalized Pell equation are closely related to the quadratic integer $x+y\sqrt{D}$, so in the literature the solutions of the Pell equation are often written in the form $x+y\sqrt{D}$. Because the norm of a quadratic integer is

$$
N(x+y\sqrt{D}) = x^2-Dy^2,
$$

the generalized Pell equation is roughly equivalent to finding a quadratic integer of norm $N$. But there is indeed a subtle difference between the two. When $x$ and $y$ are both integers, $x+y\sqrt{D}$ must be a quadratic integer; conversely, a quadratic integer does not necessarily require $x$ and $y$ to both be integers—in the case $D\equiv 1\pmod 4$, $x$ and $y$ can also both be half-integers[^half-int].

This difference is especially important when solving for the fundamental unit. Because a unit in a quadratic integer ring is a quadratic integer of norm $\pm 1$. For $D\equiv 2,3\pmod 4$, to find such a unit, we only need to solve the generalized Pell equation in the case $N=\pm 1$; but for $D\equiv 1\pmod 4$, we also need to consider the case $N=\pm 4$. The [method of solving for units](#the-case-of-norm-4) is discussed below.

To understand the structure of the solutions of the generalized Pell equation, we need to start from the [Brahmagupta identity](https://en.wikipedia.org/wiki/Brahmagupta%27s_identity):

$$
(x_1^2-Dy_1^2)(x_2^2-Dy_2^2)=(x_1x_2+Dy_1y_2)^2-D(x_1y_2+x_2y_1)^2.
$$

It amounts to the norm of a quadratic integer being multiplicative, i.e.

$$
\begin{aligned}
N\left(x_1+y_1\sqrt{D}\right)N\left(x_2+y_2\sqrt{D}\right) &= N\left((x_1+y_1\sqrt{D})(x_2+y_2\sqrt{D})\right) \\
&= N\left((x_1x_2+Dy_1y_2)+(x_1y_2+x_2y_1)\sqrt{D}\right).
\end{aligned}
$$

Using this identity, we can compose the integer solutions of the equation $x^2-Dy^2=N_1$ and the equation $x^2-Dy^2=N_2$ into an integer solution of the equation $x^2-Dy^2=N_1N_2$. Of course, from the perspective of quadratic integers, the composition of solutions is exactly the multiplication of quadratic integers, which reflects the convenience of recording the solutions of the Pell equation in quadratic integer form. In particular, taking $N_1=N$ and $N_2=1$, we can find that if we know a set of solutions of $x^2-Dy^2=N$ and all solutions of the corresponding Pell equation $x^2-Dy^2=1$, we can obtain more solutions of $x^2-Dy^2=N$. Of course, this method may not generate all the solutions. But this at least shows that understanding the structure of the solutions of the Pell equation plays an important role in understanding the structure of the solutions of the generalized Pell equation.

### Pell equation

The geometric meaning of the equation $x^2-Dy^2=1$ is a hyperbola with the real axis on the $x$-axis and the imaginary axis on the $y$-axis. Each point on the hyperbola uniquely corresponds to a nonzero value of $x+y\sqrt{D}$: the left branch of the hyperbola corresponds to negative values of $x+y\sqrt{D}$, and the right branch corresponds to positive values. Moreover, on each branch, the value of $x+y\sqrt{D}$ corresponding to the hyperbola from bottom to top is strictly increasing. The values of the quadratic integer endow the solutions of the Pell equation with a natural order.

The hyperbola is symmetric about both the $x$-axis and the $y$-axis, so to discuss the solutions of the Pell equation we only need to consider the segment in the first quadrant, and the other solutions can be obtained through symmetry. This amounts to only considering the solutions with $x+y\sqrt{D}>1$. If the equation has a nontrivial solution besides $(\pm 1,0)$, then there must exist in the first quadrant the solution $(x_1,y_1)$ with the smallest value of $x+y\sqrt{D}$, which is also the lattice point with the smallest horizontal and vertical coordinates in the first quadrant (excluding the coordinate axes); it is called the fundamental solution of the Pell equation[^fundamental-solution]. According to the earlier discussion, the integer pairs $(x_k,y_k)$ satisfying $x_k+y_k\sqrt{D}=(x_1+y_1\sqrt{D})^k$ are all solutions of the Pell equation and are all in the first quadrant. Conversely, these are indeed all the solutions of the Pell equation in the first quadrant. Using symmetry again, we can obtain the following conclusion:

???+ note "Theorem"
    Let the fundamental solution of the Pell equation $x^2-Dy^2=1$ be $(x_1,y_1)$. Then, all its solutions are
    
    $$
    \{(x,y):x+y\sqrt{D}=\pm(x_1+y_1\sqrt{D})^k,k\in\mathbf Z\}.
    $$

??? note "Proof"
    First prove that there is no other solution in the first quadrant. Suppose there exists another solution $x+y\sqrt{D}$ and for some $k\ge 0$ we have
    
    $$
    x_k+y_k\sqrt{D}< x+y\sqrt{D}< x_{k+1}+y_{k+1}\sqrt{D}.
    $$
    
    Geometrically, this amounts to saying that the lattice point $(x,y)$ falls between $(x_k,y_k)$ and $(x_{k+1},y_{k+1})$ on the hyperbola (excluding the endpoints). Multiplying the inequality by $x_k-y_k\sqrt{D}=(x_k+y_k\sqrt{D})^{-1}$, we obtain
    
    $$
    1< (x+y\sqrt{D})(x_k-y_k\sqrt{D})=(xx_k-Dyy_k)+(x_ky-xy_k)\sqrt{D} < x_1+y_1\sqrt{D}.
    $$
    
    According to the monotonicity mentioned earlier, this inequality shows that $(xx_k-Dyy_k,x_ky-xy_k)$ is a lattice point located between $(1,0)$ and $(x_1,y_1)$. This contradicts the choice of $(x_1,y_1)$.
    
    When extending the first-quadrant solutions to the entire plane, taking the exponent $k$ to its negative (i.e. taking the reciprocal of the whole) is symmetry about the $x$-axis, and taking the negative of the whole is symmetry about the origin. Adding the trivial solution when $k=0$, we obtain all the solutions of the Pell equation.

The earlier discussion only assumed the existence of the fundamental solution. Now we want to show that the Pell equation always has a nontrivial solution.

???+ note "Theorem"
    The Pell equation $x^2-Dy^2=1$ always has integer solutions besides $(\pm 1,0)$.

??? note "Proof"
    First, [Dirichlet's theorem](./continued-fraction.md#approximating-real-numbers-with-convergents) shows that there exist infinitely many pairs of positive integers $(x,y)$ such that
    
    $$
    \left|\dfrac{x}{y}-\sqrt{D}\right| \le \dfrac{1}{y^2}
    $$
    
    holds, and they all satisfy the inequality
    
    $$
    |x^2-Dy^2|=y^2\left|\dfrac{x}{y}-\sqrt{D}\right|\left|\dfrac{x}{y}+\sqrt{D}\right| \le \dfrac{1}{y^2}+2\sqrt{D}<1+2\sqrt{D}.
    $$
    
    Therefore, there must exist an integer $m\in(-1-2\sqrt{D},1+2\sqrt{D})$ such that infinitely many pairs $(x,y)$ all satisfy $x^2-Dy^2 = m$. Classifying these $(x,y)$ according to their remainders modulo $m$, we know that for some pair of integers $(x_0,y_0)$, there must exist infinitely many pairs $(x,y)$ such that $x\equiv x_0\pmod m$ and $y\equiv y_0\pmod m$ hold. Taking any two distinct pairs $(x_1,y_1)$ and $(x_2,y_2)$ satisfying these conditions, then
    
    $$
    \dfrac{x_1+y_1\sqrt{D}}{x_2+y_2\sqrt{D}}=\dfrac{x_1x_2-Dy_1y_2}{m}+\dfrac{x_2y_1-x_1y_2}{m}\sqrt{D}.
    $$
    
    Because by the congruence relation
    
    $$
    \begin{aligned}
    x_1x_2-Dy_1y_2 &\equiv x_0^2-Dy_0^2 = m \equiv 0 \pmod{|m|},\\
    x_2y_1-x_1y_2 &\equiv x_0y_0-x_0y_0 = 0 \pmod{|m|},
    \end{aligned}
    $$
    
    this shows that the right side of the above expression is an integer solution. Moreover, because $(x_1,y_1)\neq(x_2,y_2)$, it is not trivial. This shows that the Pell equation does indeed have a nontrivial solution.

Of course, this section provides a non-constructive proof; when discussing the solution methods of the Pell equation below, we will directly use the convergents of the continued fraction to construct the solution of the Pell equation, thereby providing another proof of the existence of a nontrivial solution of the Pell equation. In addition, although the structure of the Pell equation solutions obtained in this section is consistent with the structure of the units of the real quadratic integer ring, for the case $D\equiv 1\pmod 4$, this section has not completely solved the corresponding problem of the structure of the units of the quadratic integer ring, which will be discussed further below.

### Generalized Pell equation

The graph of the generalized Pell equation $x^2-Dy^2=N$ is likewise a hyperbola on the plane, likewise with the $x$-axis and $y$-axis as axes of symmetry. As already pointed out earlier, some solutions of the equation $x^2-Dy^2=N$ may differ by only a factor of a Pell equation solution, which means we can divide the solutions of the equation $x^2-Dy^2=N$ into equivalence classes. For two solutions $(x_1,y_1)$ and $(x_2,y_2)$ of the equation $x^2-Dy^2=N$, if there exists a solution $(u,v)$ of the Pell equation such that $x_2+y_2\sqrt{D}=(x_1+y_1\sqrt{D})(u+v\sqrt{D})$ holds, then the solutions $(x_1,y_1)$ and $(x_2,y_2)$ are said to be equivalent. A necessary and sufficient condition for two solutions to be equivalent is

$$
N\mid (x_1x_2-Dy_1y_2),\ N\mid (x_2y_1-x_1y_2).
$$

Because the solutions of the Pell equation are relatively easy to find, a natural idea is to find one solution in each of the above equivalence classes. As long as we know these solutions, we can use the corresponding Pell equation solutions to obtain all the required solutions of the generalized Pell equation. Among the equivalence classes of the solutions of the generalized Pell equation, due to symmetry, each equivalence class has a solution with vertical coordinate $y$ non-negative but as small as possible: if such a solution is unique, it is called the fundamental solution of that equivalence class; otherwise, that equivalence class must have two solutions with non-negative and smallest $y$, and they are symmetric about the $y$-axis, in which case we choose the one with $x>0$ as the fundamental solution. From this, solving the generalized Pell equation $x^2-Dy^2=N$ amounts to solving its set of fundamental solutions $U$. Let the fundamental solution of its corresponding Pell equation be $(r,s)$; then the set of all solutions of the generalized Pell equation is

$$
\{(x,y):x+y\sqrt{D}=\pm(r+s\sqrt{D})^k(u+v\sqrt{D}),k\in\mathbf Z,u+v\sqrt{D}\in U\}.
$$

The fundamental solutions of the generalized Pell equation must be finite. This is because from the general solution expression above, the absolute value $|u+v\sqrt{D}|$ must lie between $r-s\sqrt{D}$ and $r+s\sqrt{D}$. The references at the end of the article provide a more rigorous estimate of the range of the coordinates of the fundamental solutions. Of course, unlike the case of the Pell equation, the generalized Pell equation may have no solution.

To obtain all solutions in the same equivalence class using a solution $(u,v)$ of the generalized Pell equation and the fundamental solution $(r,s)$ of the Pell equation, besides using the composition of solutions, we can also use the following recurrence relation

$$
x_{k} = 2rx_{k-1} - x_{k-2},\ y_{k} = 2ry_{k-1} - y_{k-2},
$$

where $x_k+y_k\sqrt{D}=(r+s\sqrt{D})^k(u+v\sqrt{D})$. This is because both $x_n$ and $y_n$ can be written for some pair of real numbers $(A,B)$ in the form $A(r+s\sqrt{D})^k+B(r-s\sqrt{D})^k$, and by Vieta's theorem, $r\pm s\sqrt{D}$ are the two real roots of the equation $x^2-2rx+1=0$, so both $x_n$ and $y_n$ satisfy the above second-order constant-coefficient recurrence relation. Compared with the composition of solutions, this recurrence formula has fewer multiplications.

## Solution methods

The solving of both the Pell equation and the generalized Pell equation can be based on continued fractions.

### PQa algorithm

The algorithms discussed in this article are all based on the PQa algorithm, which can be used to find the continued fraction expansion of a specific quadratic irrational.

Let integers $P_0,Q_0,D$ satisfy $Q_0\neq 0$, $D>0$ and not a perfect square, and $P_0^2\equiv D\pmod{Q_0}$. Then, the continued fraction expansion $[a_0,a_1,\cdots]$ of the quadratic irrational

$$
\omega=\dfrac{P_0+\sqrt{D}}{Q_0}
$$

can be found via the following [recurrence formula](./continued-fraction.md#quadratic-irrationals):

$$
a_k = \left\lfloor\dfrac{P_k+\sqrt{D}}{Q_k}\right\rfloor,\ P_{k+1} = a_kQ_k - P_k,\ Q_{k+1} = \dfrac{D-P_{k+1}^2}{Q_k}.
$$

Then, the numerator and denominator $A_k$ and $B_k$ of the $k$-th convergent of $\omega$ are given by the following [recurrence formula](./continued-fraction.md#recurrence-relations):

$$
A_k = a_kA_{k-1} + A_{k-2},\ B_k = a_kB_{k-1} + B_{k-2}
$$

with $A_{-1} = 1$, $A_{-2}=0$, $B_{-1}=0$, $B_{-2}=1$.

The correctness of these formulas has already been proven in the continued fractions article. It is also explained there that, because a quadratic irrational is a [periodic continued fraction](./continued-fraction.md#quadratic-irrationals), the triple $(P_k,Q_k,a_k)$ will eventually enter a cycle, and the algorithm can always terminate in a finite number of steps. Suppose the minimum length of the period is $\ell$, and the earliest starting position of the cycle is $k_0$; then the continued fraction expansion of the quadratic irrational can be written as

$$
\omega=[a_0,\cdots,a_{k_0-1},\overline{a_{k_0},\cdots,a_{k_0+\ell-1}}].
$$

To use the PQa algorithm to solve the Pell equation, we need to establish the following conclusion:

???+ note "Theorem"
    Continuing the above notation. Let $G_k=Q_0A_k-P_0B_k$; then the integer pair $(G_{k-1},B_{k-1})$ satisfies the relation
    
    $$
    G_{k-1}^2-DB_{k-1}^2=(-1)^{k}Q_0Q_{k},
    $$
    
    and their greatest common divisor $\gcd(G_{k-1},B_{k-1})$ divides $Q_{k}$.

??? note "Proof"
    Let the $k$-th remainder term (complete quotient) in the continued fraction expansion of $\omega$ be $\omega_{k}$, i.e.
    
    $$
    \omega = [a_0,a_1,\cdots,a_{k-1},\omega_k] = \dfrac{\omega_k A_{k-1}+A_{k-2}}{\omega_k B_{k-1}+B_{k-2}}.
    $$
    
    Substituting $\omega=(P_0+\sqrt{D})/Q_0$ and $\omega_k=(P_k+\sqrt{D})/Q_k$ into the above, we obtain
    
    $$
    \dfrac{P_0+\sqrt{D}}{Q_0} = \dfrac{(P_k+\sqrt{D})A_{k-1}+Q_kA_{k-2}}{(P_k+\sqrt{D})B_{k-1}+Q_kB_{k-2}}.
    $$
    
    Eliminating the denominators on both sides and comparing the coefficients of the rational and irrational parts, then substituting the expression for $G_k$, we obtain the following equations:
    
    $$
    \begin{aligned}
    G_{k-1} &= P_kB_{k-1} + Q_kB_{k-2},\\
    DB_{k-1} &= P_kG_{k-1} + Q_kG_{k-2}.
    \end{aligned}
    $$
    
    Therefore, multiplying the first equation by $G_{k-1}$ and subtracting the second equation multiplied by $B_{k-1}$, we have
    
    $$
    \begin{aligned}
    G_{k-1}^2-DB_{k-1}^2 &= (B_{k-2}G_{k-1}-B_{k-1}G_{k-2})Q_k \\
    &= (A_{k-1}B_{k-2}-B_{k-1}A_{k-2})Q_0Q_k \\
    &= (-1)^kQ_0Q_k.
    \end{aligned}
    $$
    
    The last step uses the [difference formula](./continued-fraction.md#error-estimation) of the convergents. This proves the first conclusion.
    
    To prove the second conclusion, substitute the expression for $G_k$ into the first conclusion:
    
    $$
    (Q_0A_{k-1}-P_0B_{k-1})^2 - DB_{k-1}^2 = (-1)^kQ_0Q_k.
    $$
    
    So, using $Q_0\mid(P_0^2-D)$, we have
    
    $$
    Q_0A_{k-1}^2 +\left(\dfrac{P_0^2-D}{Q_0}B_{k-1}- 2P_0A_{k-1}\right)B_{k-1} = (-1)^kQ_k.
    $$
    
    Hence, $\gcd(G_{k-1},B_{k-1}) = \gcd(Q_0A_{k-1},B_{k-1})$ divides $Q_k$.

This conclusion provides a method for finding solutions of the equation $x^2-Dy^2=N$. If we reasonably choose $Q_0>0$ and choose $P_0$ to be a solution of the congruence equation $P_0^2\equiv D\pmod{Q_0}$, then by executing the PQa algorithm on $(P_0+\sqrt{D})/Q_0$ until we find $(-1)^kQ_0Q_{k}=N$, at which point $(G_{k-1},B_{k-1})$ becomes a set of solutions of the original equation. Moreover, if $Q_k=\pm 1$, then the solution obtained this way must be a primitive solution, that is, $G_{k-1}$ and $B_{k-1}$ must be coprime.

This idea is the core of solving the Pell equation and the generalized Pell equation. After understanding this idea, below we set about handling some details of the algorithm and prove that all solutions can be obtained in this way.

### Pell equation

To solve the Pell equation $x^2-Dy^2=1$, we only need to run the PQa algorithm on $(P_0,Q_0,D)=(0,1,D)$ until $(-1)^kQ_k=1$ appears, at which point $(A_{k-1},B_{k-1})$ is a set of solutions of the Pell equation (because $G_{k-1}$ is then exactly $A_{k-1}$). Of course, for the Pell equation, this process can be described more precisely.

First, the solution must appear at the end of the period. The above process amounts to doing the continued fraction expansion of $\sqrt{D}$. For this, there is already a [conclusion](./continued-fraction.md#purely-periodic-continued-fractions):

$$
\sqrt{D} = [\lfloor\sqrt{D}\rfloor,\overline{a_1,\cdots,a_{\ell-1},2\lfloor\sqrt{D}\rfloor}].
$$

Here, the period length is $\ell$, and the starting position is the $1$-st term (with index starting from $0$). Moreover, its $\ell$-th remainder term equals $\lfloor\sqrt{D}\rfloor+\sqrt{D}$, which shows that $Q_{\ell}=1$. Therefore, if $\ell$ is even, then $(A_{\ell-1},B_{\ell-1})$ is a set of nontrivial solutions of the Pell equation; if $\ell$ is odd, then $(A_{2\ell-1},B_{2\ell-1})$ is a set of nontrivial solutions of the Pell equation.

Next we want to show that the set of solutions just obtained must be the fundamental solution. This conclusion is based on two reasons: first, the fraction $x/y$ corresponding to every positive integer solution $(x,y)$ of the Pell equation appears in the convergents of $\sqrt{D}$, which guarantees that $(x,y)$ must be some $(A_k,B_k)$ in the PQa algorithm process; second, apart from the end of the period, there is no other position with $Q_k=1$, because the recurrence relation of $A_k$ and $B_k$ guarantees that they increase in size as the index increases, so the smallest positive integer solution (i.e. the fundamental solution) must appear at the position just indicated. These two reasons can be derived from the following two theorems respectively:

???+ note "Theorem"
    Suppose the equation $x^2-Dy^2=N$ has a positive integer solution $(x,y)$; if $|N|<\sqrt{D}$, then $\dfrac{x}{y}$ must equal a convergent of $\sqrt{D}$.

??? note "Proof"
    When $N>0$, because $x^2-Dy^2>0$, we have $x>y\sqrt{D}$. Hence,
    
    $$
    \left|\dfrac{x}{y}-\sqrt{D}\right| = \dfrac{N}{y(x+y\sqrt{D})}<\dfrac{N}{2y^2\sqrt{D}}<\dfrac{1}{2y^2}.
    $$
    
    By [Legendre's criterion](./continued-fraction.md#determination-of-convergents), $\dfrac{x}{y}$ is a convergent of $\sqrt{D}$.
    
    When $N<0$, $x>y\sqrt{D}$ no longer holds. So, instead consider the solution of the equation $y^2-\dfrac{1}{D}x^2=-\dfrac{N}{D}$. Because $\dfrac{|N|}{D}<\sqrt{\dfrac{1}{D}}$, the above argument still holds. This shows that $\dfrac{y}{x}$ is a convergent of $\dfrac{1}{\sqrt{D}}$. By the [reciprocal theorem](./continued-fraction.md#recurrence-relations), $\dfrac{x}{y}$ is also a convergent of $\sqrt{D}$.

???+ note "Theorem"
    In the process of running the above PQa algorithm on $(P_0,Q_0,D)=(0,1,D)$, $Q_k=1$ must imply $\ell\mid k$.

??? note "Proof"
    In the continued fraction expansion of $\sqrt{D}$, except for the $0$-th remainder term, all other remainder terms are [purely periodic continued fractions](./continued-fraction.md#purely-periodic-continued-fractions). Suppose $Q_k=1$. By Galois's conclusion, there must be a remainder term $\omega_k=P_k+\sqrt{D}>1$, and its conjugate $-1<P_k-\sqrt{D}<0$, which shows that $P_k=\lfloor\sqrt{D}\rfloor$. Therefore, the remainder term $\omega_k$ equals $\omega_\ell$. But the repetition of the remainder term means the continued fraction is periodic; if $k$ is not an integer multiple of $\ell$, it contradicts $\ell$ being the minimal positive period. So, we must have $\ell\mid k$.

Combining the discussion in this section, as long as we do the continued fraction expansion of $\sqrt{D}$, i.e. do the PQa algorithm starting from $(P_0,Q_0,D)=(0,1,D)$, when we first obtain $Q_\ell=1$, we reach the end of the first period. At this point, if $\ell$ is even, then $(A_{\ell-1},B_{\ell-1})$ is the fundamental solution of the Pell equation; otherwise, $(A_{2\ell-1},B_{2\ell-1})$ is the fundamental solution of the Pell equation. For the case where the period length $\ell$ is odd, we do not need to continue the PQa algorithm to twice the period; we will show shortly that $A_{2\ell-1}+B_{2\ell-1}\sqrt{D}=(A_{\ell-1}+B_{\ell-1}\sqrt{D})^2$, so we can directly compute the fundamental solution of the Pell equation from $(A_{\ell-1},B_{\ell-1})$. All other solutions of the Pell equation can be computed from the fundamental solution of the Pell equation.

??? example "Examples"
    1.  Solve the equation $x^2-14y^2=1$.
    
        Running the PQa algorithm on $(P_0,Q_0,D)=(0,1,14)$ gives the following result: (the red part is the first period)
    
        | $k$ | $P$ | $Q$ |        $a$       |  $A$  |  $B$ |  $G$  | $G^2-DB^2$ |
        | :-: | :-: | :-: | :--------------: | :---: | :--: | :---: | :--------: |
        | $0$ | $0$ | $1$ |        $3$       |  $3$  |  $1$ |  $3$  |    $-5$    |
        | $1$ | $3$ | $5$ | $\color{red}{1}$ |  $4$  |  $1$ |  $4$  |     $2$    |
        | $2$ | $2$ | $2$ | $\color{red}{2}$ |  $11$ |  $3$ |  $11$ |    $-5$    |
        | $3$ | $2$ | $5$ | $\color{red}{1}$ |  $15$ |  $4$ |  $15$ |     $1$    |
        | $4$ | $3$ | $1$ | $\color{red}{6}$ | $101$ | $27$ | $101$ |    $-5$    |
        | $5$ | $3$ | $5$ |        $1$       | $116$ | $31$ | $116$ |     $2$    |
    
        The period length $\ell=4$ is even. The smallest positive integer solution of the equation is $(G_3,B_3)=(15,4)$.
    2.  Solve the equation $x^2-41y^2=1$.
    
        Running the PQa algorithm on $(P_0,Q_0,D)=(0,1,41)$ gives the following result: (the red part is the first period)
    
        | $k$ | $P$ | $Q$ |        $a$        |   $A$   |   $B$  |   $G$   | $G^2-DB^2$ |
        | :-: | :-: | :-: | :---------------: | :-----: | :----: | :-----: | :--------: |
        | $0$ | $0$ | $1$ |        $6$        |   $6$   |   $1$  |   $6$   |    $-5$    |
        | $1$ | $6$ | $5$ |  $\color{red}{2}$ |   $13$  |   $2$  |   $13$  |     $5$    |
        | $2$ | $4$ | $5$ |  $\color{red}{2}$ |   $32$  |   $5$  |   $32$  |    $-1$    |
        | $3$ | $6$ | $1$ | $\color{red}{12}$ |  $397$  |  $62$  |  $397$  |     $5$    |
        | $4$ | $6$ | $5$ |        $2$        |  $826$  |  $129$ |  $826$  |    $-5$    |
        | $5$ | $4$ | $5$ |        $2$        |  $2049$ |  $320$ |  $2049$ |     $1$    |
        | $6$ | $6$ | $1$ |        $12$       | $25414$ | $3969$ | $25414$ |    $-5$    |
        | $7$ | $6$ | $5$ |        $2$        | $52877$ | $8258$ | $52877$ |     $5$    |
    
        The period length $\ell=3$ is odd. The smallest positive integer solution of the equation is $(G_5,B_5)=(2049,320)$. It can also be computed from $(G_2,B_2)=(32,5)$:
    
        $$
        (32+5\sqrt{41})^2=2049+320\sqrt{41}.
        $$

### Negative Pell equation

According to the discussion in the previous section, the solution of the negative Pell equation must also correspond to a convergent of $\sqrt{D}$, and can only appear at $(-1)^kQ_k=-1$. This can only appear at the end of the period. Therefore, the negative Pell equation has a solution if and only if the period length $\ell$ is odd. When a solution exists, $(A_{\ell-1},B_{\ell-1})$ is the fundamental solution of the negative Pell equation. Its solution method is consistent with that in the previous section.

Using an idea similar to the earlier proof of the structure of the Pell equation solutions, we can prove the following conclusion:

???+ note "Theorem"
    Suppose the equation $x^2-Dy^2=-1$ has a solution, and the fundamental solution is $(x_1,y_1)$. Then, all integer solutions of $x^2-Dy^2=\pm 1$ belong to the set
    
    $$
    \{(x,y):x+y\sqrt{D}=\pm(x_1+y_1\sqrt{D})^k,k\in\mathbf Z\}.
    $$
    
    In particular, the integer solution $(x_2,y_2)$ satisfying $x_2+y_2\sqrt{D}=(x_1+y_1\sqrt{D})^2$ is exactly the fundamental solution of $x^2-Dy^2=1$.

??? note "Proof"
    Due to symmetry, we only need to consider positive integer solutions, i.e. the case $x+y\sqrt{D}>1$. But since $x^2-Dy^2=\pm 1$ is two segments of a hyperbola, $x+y\sqrt{D}$ cannot establish a one-to-one correspondence with $(x,y)$. To handle this difficulty, we first prove that the above $(x_2,y_2)$ is the fundamental solution of $x^2-Dy^2=1$.
    
    Obviously, $(x_2,y_2)$ is a solution of $x^2-Dy^2=1$. If we let $(z,w)$ be the fundamental solution of $x^2-Dy^2=1$, then we must have $1<z+w\sqrt{D}\le x_2+y_2\sqrt{D}$. If the right inequality does not include equality, then dividing the inequality by $x_1+y_1\sqrt{D}$ gives $-x_1+y_1\sqrt{D}<(z+w\sqrt{D})(-x_1+y_1\sqrt{D})<x_1+y_1\sqrt{D}$. Expanding the expression of the middle term of this inequality gives the form $x'+y'\sqrt{D}$, whose norm is $-1$ and $(x',y')$ is also an integer solution. Taking the reciprocal of this inequality, we find that $-x'+y'\sqrt{D}$ likewise falls between $-x_1+y_1\sqrt{D}$ and $x_1+y_1\sqrt{D}$. The quadratic integers $\pm x'+y'\sqrt{D}$ are mutual reciprocals, so one of them must be greater than $1$. But between $1$ and $x_1+y_1\sqrt{D}$ there should be no other quadratic integer of norm $-1$, which contradicts the minimality of $x_1+y_1\sqrt{D}$. So, we must have $x_2+y_2\sqrt{D}=z+w\sqrt{D}$, i.e. $(x_2,y_2)$ is the fundamental solution of the equation $x^2-Dy^2=1$.
    
    Based on this, if there is a solution $(x,y)$ of the equation $x^2-Dy^2=\pm 1$ that does not correspond to some $(x_1+y_1\sqrt{D})^k$, then there must exist $k$ such that $(x_1+y_1\sqrt{D})^{2k}<x+y\sqrt{D}<(x_1+y_1\sqrt{D})^{2k+2}$; eliminating the factor $(x_1+y_1)^{2k+1}$, this shows that there exists a quadratic integer $x'+y'\sqrt{D}\neq 1$ of norm $\pm 1$ located between $-x_1+y_1\sqrt{D}$ and $x_1+y_1\sqrt{D}$. Repeating the argument using reciprocals from the previous paragraph, this contradicts the minimality of $x_1+y_1\sqrt{D}$. Therefore the original proposition is proven.

Because $(A_{\ell-1},B_{\ell-1})$ is the smallest positive integer solution of the negative Pell equation, and all positive integer solutions of $x^2-Dy^2=\pm 1$ appear in the set

$$
\{(x,y):x+y\sqrt{D}=(A_{\ell-1}+B_{\ell-1}\sqrt{D})^k,k\in\mathbf N_+\}
$$

and because these positive integer solutions must correspond to the convergents of $\sqrt{D}$ at the end of the period (the previous position), and the numerator and denominator of the convergents are strictly monotonically increasing, for all $k\in\mathbf N_+$ we always have

$$
(A_{\ell-1}+B_{\ell-1}\sqrt{D})^k = A_{k\ell-1}+B_{k\ell-1}\sqrt{D}.
$$

Among all these positive integer solutions, when $k$ is odd it is a solution of the negative Pell equation, and when $k$ is even it is a solution of the Pell equation, and the two appear alternately.

To determine whether the negative Pell equation has a solution, we need to compute the period length of the continued fraction expansion of $\sqrt{D}$, which is not easy to compute, so we hope to find a simpler determination method. But at present there is no determination method with a concise, easily computed condition[^solubility-neg-pell]. Here we only provide a simple conclusion.

???+ note "Theorem"
    If the equation $x^2-Dy^2=-1$ has a solution, then $4$ does not divide $D$ and $D$ does not contain a prime factor of type $4k+3$. Conversely, if $D=2$ or $D$ is a prime of type $4k+1$, then the equation must have a solution.

??? note "Proof"
    First, the negative Pell equation having a solution means that $-1$ is a quadratic residue of $D$, so $-1$ is also a quadratic residue of any factor $d$ of $D$, hence $d\neq 4$ and $d$ is not a prime of type $4k+3$. Conversely, the equation $x^2-2y^2=-1$ has a nontrivial solution $(1,1)$. The rest is the case where $D$ is a prime of type $4k+1$.
    
    Let $D$ be a prime of type $4k+1$; we want to prove that the equation $x^2-Dy^2=-1$ has a solution. The idea is to start from the fundamental solution $(u,v)$ of the Pell equation $x^2-Dy^2=1$ and construct a solution $(\alpha,\beta)$ of $x^2-Dy^2=-1$. If $u$ is even, taking both sides of $u^2-Dv^2=1$ modulo $4$, we obtain $v^2\equiv -1\pmod 4$, but $-1$ is not a quadratic residue modulo $4$. This contradiction shows that $u$ is odd. Examine the equation $Dv^2=u^2-1=(u+1)(u-1)$. Because $u$ is odd, $\gcd(u+1,u-1)=\gcd(u+1,2)=2$. Based on this fact, distributing the factors of $Dv^2$ to $u+1$ and $u-1$, one must be $2\alpha^2$ and the other $2D\beta^2$, where $\alpha$ and $\beta$ are coprime positive integers and $v=2\alpha\beta$. Substituting $u=\alpha^2+D\beta^2$ and $v=2\alpha\beta$ into $u^2-Dv^2=1$, we obtain $\alpha^2-D\beta^2=\pm 1$. Because $(u,v)$ is the fundamental solution of the Pell equation and $(\alpha,\beta)$ is a positive integer pair smaller than $(u,v)$, the right side of this equation cannot be $+1$, so it can only be $-1$. This proves that $x^2-Dy^2=-1$ has a solution $(\alpha,\beta)$.

If $D$ is composite, then not containing a prime factor of type $4k+3$ and having no square factor still cannot guarantee that the equation $x^2-Dy^2=-1$ has a solution; for example, $x^2-34y^2=-1$ has no solution.

??? example "Example"
    Using the computation results in the above examples, the equation $x^2-14y^2=-1$ has no solution, and the smallest positive integer solution of the equation $x^2-41y^2=-1$ is $(G_2,B_2)=(32,5)$.

### The case of norm ±4

Next we discuss the solutions of the equation $x^2-Dy^2=\pm 4$. In this case, the nature of the solutions depends on the value of $D\bmod 4$.

Some cases are easy. If $D\equiv 0\pmod 4$, then $x$ is even, so $(x/2,y)$ is a solution of the equation $u^2-(D/4)v^2=\pm 1$. In the remaining cases, $x,y$ must be simultaneously odd or simultaneously even. If $x,y$ are simultaneously odd, taking both sides of the equation modulo $4$ gives $D\equiv 1\pmod 4$. So, if $D\equiv 2,3\pmod 4$, then $x,y$ can only be simultaneously even, so $(x/2,y/2)$ is a solution of the equation $u^2-Dv^2=\pm 1$. Therefore, except for the case $D\equiv 1\pmod 4$, the solutions of the equation $x^2-Dy^2=\pm 4$ can all be obtained from the solutions of the corresponding (negative) Pell equation.

Now discuss the case $D\equiv 1\pmod 4$, which cannot simply be transformed into an already-solved case. To find the fundamental solution, we can apply the PQa algorithm to $(P_0,Q_0,D)=(1,2,D)$; when we first obtain $Q_\ell=2$, we reach the end of the first period. If the period length $l$ is even, then $(G_{\ell-1},B_{\ell-1})$ is the fundamental solution of the equation $x^2-Dy^2=4$; otherwise, $(G_{\ell-1},B_{\ell-1})$ is the fundamental solution of the equation $x^2-Dy^2=-4$. Starting from $(G_{\ell-1},B_{\ell-1})$, we can obtain all solutions of the equation $x^2-Dy^2=\pm 4$:

$$
\left\{(x,y):\dfrac{x+y\sqrt{D}}{2}=\pm\left(\dfrac{G_{\ell-1}+B_{\ell-1}\sqrt{D}}{2}\right)^k,k\in\mathbf Z\right\}.
$$

If the period length $\ell$ is even, all of these are solutions of the equation $x^2-Dy^2=4$; otherwise, when $k$ is odd, $(x,y)$ is a solution of the equation $x^2-Dy^2=-4$, and when $k$ is even, $(x,y)$ is a solution of the equation $x^2-Dy^2=4$.

The correctness of this algorithm relies on the following fact:

???+ note "Theorem"
    Suppose the equation $x^2-Dy^2=\pm 4$ has a positive integer solution $(x,y)$. If $D\equiv 1\pmod 4$, then $\dfrac{(x+y)/2}{y}$ must be a convergent of $\dfrac{1+\sqrt{D}}{2}$.

??? note "Proof"
    First note that in this case $x,y$ must have the same parity, so $(x+y)/2$ is an integer. If $(x,y)$ is a solution of the equation $x^2-Dy^2=4$, then $x>y\sqrt{D}>2y$, so
    
    $$
    \left|\dfrac{(x+y)/2}{y}-\dfrac{1+\sqrt{D}}{2}\right| = \dfrac{2}{y(x+y\sqrt{D})}<\dfrac{1}{2y^2}.
    $$
    
    By [Legendre's criterion](./continued-fraction.md#determination-of-convergents), $\dfrac{(x+y)/2}{y}$ is a convergent of $\dfrac{1+\sqrt{D}}{2}$.
    
    If $(x,y)$ is a solution of the equation $x^2-Dy^2=-4$, then to establish the above inequality, we only need to prove $4y<x+y\sqrt{D}$. This holds at least for all cases except $D=5,13$. For the cases $D=5,13$, substituting $x=\sqrt{Dy^2-4}$ into this inequality, it is equivalent to $2(\sqrt{D}-2)y^2>1$ holding. Except for $(D,y)=(5,1)$, this inequality holds for all $D=5,13$ and positive integers $y$. The rest is verifying the case $(D,y)=(5,1)$; in this case, the solution of the equation $x^2-5y^2=-4$ is $(x,y)=(1,1)$, and what needs to be verified is that $\dfrac{1}{1}$ is a convergent of $\dfrac{1+\sqrt{5}}{2}=[\overline{1}]$, which obviously holds.

???+ note "Theorem"
    Let $D$ be a positive integer that is not a perfect square. The continued fraction expansion of the quadratic irrational $\omega=\dfrac{1+\sqrt{D}}{2}$ has the form
    
    $$
    \omega = [\lfloor\omega\rfloor,\overline{a_1,\cdots,a_{\ell-1},2\lfloor\omega\rfloor-1}],
    $$
    
    where $\ell$ is the period length, and $a_k=a_{\ell-k}$ holds for any $1<k<\ell$.

??? note "Proof"
    Because $\lfloor\omega\rfloor-1+\omega>1$, and its conjugate equals $\lfloor\omega\rfloor - \omega$, lying between $-1$ and $0$, by [Galois's conclusion](./continued-fraction.md#purely-periodic-continued-fractions), $\lfloor\omega\rfloor-1+\omega$ is a purely periodic continued fraction and can be written as
    
    $$
    \lfloor\omega\rfloor-1+\omega = [\overline{2\lfloor\omega\rfloor-1,a_1,\cdots,a_{\ell-1}}].
    $$
    
    And Galois's conclusion about the reciprocal of the negative conjugate shows that
    
    $$
    \dfrac{1}{\omega-\lfloor\omega\rfloor} = [\overline{a_{\ell-1},\cdots,a_1,2\lfloor\omega\rfloor-1}].
    $$
    
    Therefore, by the definition of the continued fraction,
    
    $$
    \lfloor\omega\rfloor-1+\omega = 2\lfloor\omega\rfloor-1 + \dfrac{1}{\dfrac{1}{\omega-\lfloor\omega\rfloor}} = [2\lfloor\omega\rfloor-1,\overline{a_{\ell-1},\cdots,a_1,2\lfloor\omega\rfloor-1}].
    $$
    
    The uniqueness of the continued fraction expansion shows that $a_k=a_{\ell-k}$ holds for all $1<k<\ell$, so the expansion to be proved also holds.

???+ note "Theorem"
    Let $D\equiv 1\pmod 4$. In the process of running the above PQa algorithm on $(P_0,Q_0,D)=(1,2,D)$, $Q_k=2$ must imply $\ell\mid k$.

??? note "Proof"
    In the continued fraction expansion of $\dfrac{1+\sqrt{D}}{2}$, except for the $0$-th remainder term, all other remainder terms are [purely periodic continued fractions](./continued-fraction.md#purely-periodic-continued-fractions). Suppose $Q_k=2$. By Galois's conclusion, there must be a remainder term $\omega_k=\dfrac{P_k+\sqrt{D}}{2}$ whose conjugate satisfies $-1<\dfrac{P_k-\sqrt{D}}{2}<0$, i.e. $\sqrt{D}-2<P_k<\sqrt{D}$. Because in the PQa algorithm we always have $Q_k\mid P_k^2-D$ (see [proof of algorithm correctness](./continued-fraction.md#quadratic-irrationals)), $P_k$ must be odd, which shows that the value of $P_k$ is unique, i.e. $P_k=P_0+2(\lfloor\omega\rfloor-1)$, that is, the remainder term $\omega_k=\omega_\ell$. But the repetition of the remainder term means the continued fraction is periodic; if $k$ is not an integer multiple of $\ell$, it contradicts $\ell$ being the minimal positive period. So, we must have $\ell\mid k$.

???+ note "Theorem"
    Let the smallest positive integer solution of the equation $x^2-Dy^2=\pm 4$ be $(x_1,y_1)$. Then, all its solutions are
    
    $$
    \left\{(x,y):\dfrac{x+y\sqrt{D}}{2}=\pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^k,k\in\mathbf Z\right\}.
    $$

??? note "Proof"
    By symmetry, we only need to consider positive integer solutions $(x,y)$. What needs to be proved here is only that the real number pairs $(x,y)$ in the set are indeed integer solutions of the equation $x^2-Dy^2=\pm 4$. The rest only requires repeating the proof of the structure of the solutions of the equation $x^2-Dy^2=\pm 1$.
    
    Actually, what needs to be proved is that for any integer solutions $(x_1,y_1)$ and $(x_2,y_2)$ of the equation $x^2-Dy^2=\pm 4$, the positive real number pair $(x_3,y_3)$ defined as follows is still an integer solution:
    
    $$
    \dfrac{x_3+y_3\sqrt{D}}{2} = \dfrac{x_1+y_1\sqrt{D}}{2}\dfrac{x_2+y_2\sqrt{D}}{2}.
    $$
    
    Expanding the right side and comparing the coefficients of the rational and irrational terms:
    
    $$
    x_3=\dfrac{x_1x_2+Dy_1y_2}{2},\ y_3=\dfrac{x_1y_2+x_2y_1}{2}.
    $$
    
    Because for $i=1,2$ we have $x_i\equiv x_i^2\equiv Dy_i^2\equiv Dy_i\pmod 2$,
    
    $$
    \begin{aligned}
    2x_3 &= x_1x_2+Dy_1y_2 \equiv D^2y_1y_2+Dy_1y_2=D(D+1)y_1y_2 \equiv 0 \pmod 2,\\
    2y_3 &= x_1y_2+x_2y_1 \equiv Dy_1y_2+Dy_2y_1 = 2Dy_1y_2 \equiv 0 \pmod 2.
    \end{aligned}
    $$
    
    This shows that $x_3$ and $y_3$ are both integers. Using the property that the norm is multiplicative, $(x_3,y_3)$ is a solution of $x^2-Dy^2=\pm 4$.

Combining these facts and repeating the arguments of the previous sections, we can show the correctness of the above algorithm for solving the equation $x^2-Dy^2=\pm 4$. These results show that the equation $x^2-Dy^2=\pm 4$ has a simple solution structure similar to that of the equation $x^2-Dy^2=\pm 1$: all its solutions can be expressed through its smallest positive integer solution, without needing to solve other equations.

In fact, all solutions of the equation $x^2-Dy^2=\pm 1$ can be found among the solutions of the equation $x^2-Dy^2=\pm 4$, so from this perspective, the equation $x^2-Dy^2=\pm 4$ is more fundamental. Obviously, $(x,y)$ is a solution of the equation $x^2-Dy^2=\pm 1$ if and only if $(2x,2y)$ is a solution of the equation $x^2-Dy^2=\pm 4$. The earlier analysis pointed out that when $D\equiv 2,3\pmod 4$, all solutions of the equation $x^2-Dy^2=\pm 4$ must be simultaneously even, so they correspond to the solutions of $x^2-Dy^2=\pm 1$.

When $D\equiv 0\pmod 4$, in the solution $(x,y)$ of the equation $x^2-Dy^2=\pm 4$, $x$ must be even, but $y$ may be odd. If in the smallest positive integer solution $(x_1,y_1)$ of the equation $x^2-Dy^2=\pm 4$, $y_1$ is even, then in all solutions $y$ must also be even, and in this case these integer solutions correspond one-to-one with the integer solutions of the equation $x^2-Dy^2=\pm 1$; but if in the smallest integer solution $(x_1,y_1)$, $y_1$ is odd, then the parity of $y_k$ is consistent with $k$, alternating, so only when $k$ is even does it correspond to a solution of the equation $x^2-Dy^2=\pm 1$. If in the smallest positive integer solution of $x^2-Dy^2=\pm 4$, $y_1$ is odd and the norm of $x_1+y_1\sqrt{D}$ is $-4$, then for such $D$, $x^2-Dy^2=-4$ has a solution, but $x^2-Dy^2=-1$ has no solution.

When $D\equiv 1\pmod 4$, the solution $(x,y)$ of the equation $x^2-Dy^2=\pm 4$ may be simultaneously odd or simultaneously even. If the smallest positive integer solution $(x_1,y_1)$ is already simultaneously even, then all its integer solutions must also be simultaneously even, so they always correspond to integer solutions of the equation $x^2-Dy^2=\pm 1$. If the smallest positive integer solution $(x_1,y_1)$ is simultaneously odd, then we have the following conclusion:

???+ note "Theorem"
    Let the smallest positive integer solution of the equation $x^2-Dy^2=\pm 4$ be $(x_1,y_1)$. If $x_1$ and $y_1$ are simultaneously odd, then $D\equiv 5\pmod 8$, and the integer solution $(x,y)$ of this equation is simultaneously even if and only if
    
    $$
    \dfrac{x+y\sqrt{D}}{2} = \pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3k},k\in\mathbf Z.
    $$

??? note "Proof"
    Taking both sides of the equation $x_1^2-Dy_1^2=\pm 4$ modulo $8$, we obtain $D\equiv 5\pmod 8$. To prove the second conclusion, we first prove that $(x_3,y_3)$ are both even, because
    
    $$
    \dfrac{x_3+y_3\sqrt{D}}{2} = \left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3} = \dfrac{x_1^3+3Dxy_1^2}{8}+\dfrac{3x_1^2y_1+Dy_1^3}{8}\sqrt{D},
    $$
    
    so we only need to prove that the right side is an integer. Because the square of an odd number is $\equiv 1\pmod 8$,
    
    $$
    \begin{aligned}
    &x_1^3+3Dxy_1 = x_1(x_1^2+3Dy_1) \equiv x_1(1+3\times 5\times 1) = 16x_1 = 0 \pmod 8,\\
    &3x_1^2y_1+Dy_1^3 = y_1(3x_1^2+Dy_1^2) \equiv y_1(3\times 1+5\times 1) = 8y_1 = 0 \pmod 8.
    \end{aligned}
    $$
    
    This shows that $x_3,y_3$ are both even. Then, for all $k\in\mathbf Z$,
    
    $$
    \dfrac{x+y\sqrt{D}}{2} = \pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3k} = \pm\left(\dfrac{x_3+y_3\sqrt{D}}{2}\right)^k \in \mathbf Z,
    $$
    
    so in this case $(x,y)$ are both even. Conversely, for $r=1,2$, we always have
    
    $$
    \pm\left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^{3k+r} = \pm\left(\dfrac{x_3+y_3\sqrt{D}}{2}\right)^k\left(\dfrac{x_r+y_r\sqrt{D}}{2}\right).
    $$
    
    To prove that the corresponding $(x,y)$ is not an integer, we only need to prove that this expression is not an integer, i.e. that the second term in the product on the right is not an integer. When $r=1$, this is exactly the given condition; when $r=2$, because
    
    $$
    \dfrac{x_2+y_2\sqrt{D}}{2} = \left(\dfrac{x_1+y_1\sqrt{D}}{2}\right)^2 = \dfrac{x_1^2+Dy_1^2}{4} + \dfrac{x_1y_1}{2}\sqrt{D},
    $$
    
    and $x_1^2+Dy_1^2\equiv 1+1\times 1=2\pmod 4$, $x_1y_1\equiv 1\pmod 2$, this expression is also not an integer. This proves that only when the power is a multiple of $3$ are the corresponding solutions both even.

That is to say, one in every three solutions of the equation $x^2-Dy^2=\pm 4$ is simultaneously even, and it corresponds to an integer solution of $x^2-Dy^2=\pm 1$. This also shows that for $D\equiv 1\pmod 4$, the equation $x^2-Dy^2=-4$ has a solution if and only if the equation $x^2-Dy^2=-1$ has a solution.

The discussion so far is already sufficient to compute the fundamental unit of the real quadratic integer ring. Let $D$ be a positive integer with no square factor. For the case $D\equiv 2,3\pmod 4$, we only need to find the smallest positive integer solution of $x^2-Dy^2=\pm 1$; and for the case $D\equiv 1\pmod 4$, we only need to find the smallest positive integer solution of $x^2-Dy^2=\pm 4$. When we obtain the smallest positive integer solution $(x,y)$, for $D\equiv 2,3\pmod 4$, the fundamental unit is $\pm x\pm y\sqrt{D}$; for $D\equiv 1\pmod 4$, the fundamental unit is $\dfrac{\pm x\pm y\sqrt{D}}{2}$.

??? example "Examples"
    1.  Solve the equation $x^2-14y^2=\pm 4$.
    
        Using the computation in the earlier examples, the smallest positive integer solution of the equation $x^2-14y^2=4$ is $(30,8)$, and the equation $x^2-14y^2=-4$ has no solution.
    2.  Solve the equation $x^2-41y^2=\pm 4$.
    
        Running the PQa algorithm on $(P_0,Q_0,D)=(1,2,41)$ gives the following result: (the red part is the first period)
    
        |  $k$ | $P$ | $Q$ |        $a$       |   $A$   |   $B$  |   $G$   | $G^2-DB^2$ |
        | :--: | :-: | :-: | :--------------: | :-----: | :----: | :-----: | :--------: |
        |  $0$ | $1$ | $2$ |        $3$       |   $3$   |   $1$  |   $5$   |    $-16$   |
        |  $1$ | $5$ | $8$ | $\color{red}{1}$ |   $4$   |   $1$  |   $7$   |     $8$    |
        |  $2$ | $3$ | $4$ | $\color{red}{2}$ |   $11$  |   $3$  |   $19$  |    $-8$    |
        |  $3$ | $5$ | $4$ | $\color{red}{2}$ |   $26$  |   $7$  |   $45$  |    $16$    |
        |  $4$ | $3$ | $8$ | $\color{red}{1}$ |   $37$  |  $10$  |   $64$  |    $-4$    |
        |  $5$ | $5$ | $2$ | $\color{red}{5}$ |  $211$  |  $57$  |  $365$  |    $16$    |
        |  $6$ | $5$ | $8$ |        $1$       |  $248$  |  $67$  |  $429$  |    $-8$    |
        |  $7$ | $3$ | $4$ |        $2$       |  $707$  |  $191$ |  $1223$ |     $8$    |
        |  $8$ | $5$ | $4$ |        $2$       |  $1662$ |  $449$ |  $2875$ |    $-16$   |
        |  $9$ | $3$ | $8$ |        $1$       |  $2369$ |  $640$ |  $4098$ |     $4$    |
        | $10$ | $5$ | $2$ |        $5$       | $13507$ | $3649$ | $23365$ |    $-16$   |
        | $11$ | $5$ | $8$ |        $1$       | $15876$ | $4289$ | $27463$ |     $8$    |
    
        The period length $\ell=5$ is odd. The smallest positive integer solution of the equation $x^2-41y^2=-4$ is $(G_4,B_4)=(64,10)$, and the smallest positive integer solution of the equation $x^2-41y^2=4$ is $(G_9,B_9)=(4098,640)$. They have the following relation:
    
        $$
        \dfrac{4098+640\sqrt{41}}{2} = \left(\dfrac{64+10\sqrt{41}}{2}\right)^2.
        $$
    
        Of course, because $D\equiv 1\pmod 8$, according to the earlier conclusion, in this case the smallest positive integer solutions of the equation $x^2-41y^2=\pm 4$ must both be even, and are always $2$ times the smallest positive integer solutions of the equation $x^2-41y^2=\pm 1$, so they can also be directly obtained from the earlier examples.
    3.  Solve the equation $x^2-13y^2=\pm 4$.
    
        Running the PQa algorithm on $(P_0,Q_0,D)=(1,2,13)$ gives the following result: (the red part is the first period)
    
        | $k$ | $P$ | $Q$ |        $a$       |  $A$ |  $B$ |  $G$  | $G^2-DB^2$ |
        | :-: | :-: | :-: | :--------------: | :--: | :--: | :---: | :--------: |
        | $0$ | $1$ | $2$ |        $2$       |  $2$ |  $1$ |  $3$  |    $-4$    |
        | $1$ | $3$ | $2$ | $\color{red}{3}$ |  $7$ |  $3$ |  $11$ |     $4$    |
        | $2$ | $3$ | $2$ |        $3$       | $23$ | $10$ |  $36$ |    $-4$    |
        | $3$ | $3$ | $2$ |        $3$       | $74$ | $33$ | $119$ |     $4$    |
    
        The period length $\ell=1$ is odd. The smallest positive integer solution of the equation $x^2-13y^2=-4$ is $(G_0,B_0)=(3,1)$, and the smallest positive integer solution of the equation $x^2-13y^2=4$ is $(G_1,B_1)=(11,3)$.
    
        Because the smallest positive integer solutions of this equation are both odd, we can use the number pair $(G_2,B_2)=(36,10)$ at the end of the third period to obtain the smallest positive integer solution $(18,5)$ of the corresponding (negative) Pell equation $x^2-13y^2=\pm 1$. It can also be obtained by direct computation:
    
        $$
        \dfrac{36+10\sqrt{13}}{2}=\left(\dfrac{3+\sqrt{13}}{2}\right)^3.
        $$
    
        Moreover, this is a solution of the negative Pell equation. The smallest positive integer solution of the corresponding Pell equation is $(649,180)$.
    4.  Solve the equation $x^2-52y^2=\pm 4$.
    
        Because the smallest positive integer solutions of the equation $x^2-13y^2=\pm 1$ are $(18,5)$ and $(649,180)$ respectively, the smallest positive integer solutions of the equation $x^2-52y^2=\pm 4$ are $(36,10)$ and $(1298,360)$ respectively.

### General case

Finally, discuss the solution method of the generalized Pell equation.

For the case $|N|<\sqrt{D}$ there is a simple solution method. The earlier conclusion shows that the solution $(x,y)$ of the equation $x^2-Dy^2=N$ must satisfy $\dfrac{x}{y}$ equal to some convergent of $\sqrt{D}$. Moreover, according to the structure of the solutions discussed earlier, each fundamental solution $(x,y)$ satisfies $x+y\sqrt{D}$ less than or equal to the fundamental solution $x_1+y_1\sqrt{D}$ of the corresponding Pell equation $x^2-Dy^2=1$. Using the monotonicity of the denominator sequence $B_k$ in the PQa algorithm, these fundamental solutions of the generalized Pell equation must appear before the fundamental solution of the corresponding Pell equation appears. From this, we only need to run the PQa algorithm on $(P_0,Q_0,D)=(0,1,D)$ until $Q_{\ell'}=1$ with $\ell'$ even, and during the process check for each $(A_k,B_k)$ that appears whether there exists an integer $f$ such that

$$
A_k^2-DB_k^2 = (-1)^{k+1}Q_{k+1} = N/f^2
$$

holds; if so, record that $(fA_{k},fB_{k})$ is a smallest positive integer solution. All the $(fA_k,fB_k)$ recorded in this process are all the smallest positive integer solutions of the equation $x^2-Dy^2=N$. Using $(A_{\ell'-1},B_{\ell'-1})$, i.e. the fundamental solution of the corresponding Pell equation, we can generate all solutions of the generalized Pell equation from these smallest positive integer solutions found. Note that depending on whether the period length $\ell$ is even or odd, the above $\ell'$ may be $\ell$ or $2\ell$.

For the more general case of $N$, the above method no longer applies. First, enumerate all square factors $f^2$ of $N$, set $m=N/f^2$, and enumerate all solutions $z$ of the congruence equation $z^2\equiv D\pmod{|m|}$ satisfying $-|m|/2<z \le |m|/2$. Then, run the PQa algorithm on $(P_0,Q_0,D)=(z,|m|,D)$ until $Q_k=\pm 1$ or a period has already ended. In the second case, the solution of the equation related to this pair $(f,z)$ does not exist. In the first case, we need to further determine whether $(-1)^kQ_k=N/|N|$ or not. If the signs are consistent, then $(fG_{k-1},fB_{k-1})$ is a solution of the equation $x^2-Dy^2=N$. Otherwise, it is a solution of the equation $x^2-Dy^2=-N$, and if and only if the solution of the corresponding negative Pell equation exists can we obtain a solution of the equation $x^2-Dy^2=N$ by composing it with the fundamental solution of the corresponding negative Pell equation. After completing the traversal of all pairs $(f,z)$, we can obtain exactly one solution in each equivalence class of the solutions of the equation $x^2-Dy^2=N$, and that solution is the fundamental solution or smallest positive integer solution of that equivalence class. Using them and the fundamental solution of the corresponding Pell equation, we can generate all integer solutions of that equation. This algorithm is called the **Lagrange–Matthews–Mollin algorithm**.

The correctness of this algorithm is guaranteed by the following theorem:

???+ note "Theorem"
    Suppose the equation $x^2-Dy^2=N$ has an integer solution $(x,y)$ with $x\ge 0, y>0,\gcd(x,y)=1$. Let $Q_0=|N|$; then $\gcd(Q_0,y)=1$. Let $P_0$ be a solution of the congruence equation $x\equiv -P_0y\pmod{Q_0}$ with $-Q_0/2<P_0\le Q_0/2$, and let the integer $X$ be such that $x=Q_0X-P_0y$ holds. Then, $P_0^2\equiv D\pmod{Q_0}$, $\dfrac{X}{y}$ is a convergent $\dfrac{A_{k-1}}{B_{k-1}}$ of $\omega=\dfrac{P_0+\sqrt{D}}{Q_0}$, and $Q_k=(-1)^k\dfrac{N}{|N|}$.

??? note "Proof"
    Using $x\equiv -P_0y\pmod{Q_0}$ and $x^2-Dy^2=N\equiv 0\pmod{Q_0}$, obviously $P_0^2\equiv D\pmod{Q_0}$. Therefore,
    
    $$
    P_0x+Dy\equiv -P_0^2y+Dy = (D-P_0^2)y\equiv 0\pmod{Q_0}.
    $$
    
    From this, we can examine the integer-coefficient matrix
    
    $$
    \begin{pmatrix}P & R \\ Q & S\end{pmatrix}
    =
    \begin{pmatrix}X & \dfrac{P_0x+Dy}{Q_0} \\ y & x\end{pmatrix}.
    $$
    
    Its determinant
    
    $$
    PS-QR = \dfrac{x(x+P_0y)-y(P_0x+Dy)}{Q_0} = \dfrac{x^2-Dy^2}{Q_0} = \pm 1.
    $$
    
    Moreover, letting $\zeta =\sqrt{D} > 1$, we have
    
    $$
    \dfrac{P\zeta+R}{Q\zeta+S} = \dfrac{(x+P_0y)\sqrt{D}+(P_0x+Dy)}{(x+y\sqrt{D})Q_0} = \dfrac{P_0+\sqrt{D}}{Q_0} = \omega.
    $$
    
    Below we prove that $\dfrac{P}{Q}$ is a convergent of $\omega$. Suppose $\dfrac{P}{Q}$ has the [continued fraction expansion](./continued-fraction.md#simple-continued-fractions)
    
    $$
    \dfrac{P}{Q} = [a_0,a_1,\cdots,a_k]
    $$
    
    with $PS-QR = (-1)^{k-1}$. If we let $\dfrac{p_k}{q_k}$ be its $k$-th convergent, then $(p_k,q_k)=(P,Q)$, and by the [difference formula of convergents](./continued-fraction.md#error-estimation), $p_kq_{k-1}-q_kp_{k-1}=(-1)^{k-1}$. This shows that
    
    $$
    p_k(S-q_{k-1}) = q_k(R-p_{k-1}).
    $$
    
    Discuss by cases:
    
    -   If $S=0$, then it is easy to verify that $Q=R=1$, so $\omega=P+\zeta^{-1}=[P,\zeta]$, hence $\dfrac{P}{Q}=P$ is the $0$-th convergent of $\omega$;
    -   If $Q=S>0$, then $Q=S=1$ and $P-R=\pm 1$. In this case,
        -   if $P=R+1$, then $\omega=R+\dfrac{1}{1+\zeta^{-1}}=[R,1,\zeta]$, hence $\dfrac{P}{Q}=\dfrac{R+1}{1}=[R,1]$ is the $1$-st convergent of $\omega$;
        -   if $P=R-1$, then $\omega=R-1+\dfrac{1}{1+\zeta}=[R-1,\zeta-1]$, hence $\dfrac{P}{Q}=R-1$ is the $0$-th convergent of $\omega$;
    -   If $Q\neq S>0$, then since $Q=q_k\mid(S-q_{k-1})$, there always exists an integer $\kappa$ such that $S=\kappa q_k+q_{k-1}$ and $R=\kappa p_k+p_{k-1}$ hold. Because $q_k\ge q_{k-1}$ and $S>0$, we have $\kappa\ge 0$. Therefore, $\omega=\dfrac{(\kappa+\zeta)p_k+p_{k-1}}{(\kappa+\zeta)q_k+q_{k-1}}=[a_0,a_1,\cdots,a_k,\kappa+\zeta]$, hence $\dfrac{P}{Q}$ is its $k$-th convergent.
    
    In summary, $\dfrac{X}{y}$ is always a convergent of $\omega=\dfrac{P_0+\sqrt{D}}{Q_0}$, and following the notation in the PQa algorithm it is denoted $\dfrac{A_{k-1}}{B_{k-1}}$. Because $A_{k-1}^2-DB_{k-1}^2=(-1)^kQ_0Q_k$, we have $Q_k=(-1)^k\dfrac{N}{|N|}$.

This theorem guarantees that all positive solutions of the equation exist among the convergents of the corresponding quadratic irrational. Because when computing convergents using the PQa algorithm, as long as we enter the period, the convergents are guaranteed to always be positive. So, as long as we enumerate all quadratic irrationals permitted by the theorem's conditions and compute their convergents up to one period, we can find a solution. Because two solutions appearing in the convergents of the same quadratic irrational must be equivalent, as long as we obtain the first solution satisfying $(-1)^kQ_k=N/|N|$, we can stop the subsequent computation. Unlike all the previous algorithms, here the $k$ satisfying the condition may appear before entering the period.

??? example "Examples"
    1.  Solve the equation $x^2-157y^2=12$.
    
        Because $12^2<157$, running the PQa algorithm on $(P_0,Q_0,D)=(0,1,157)$ gives the following result: (the red part is the first period)
    
        |  $k$ |  $P$ |  $Q$ |        $a$        |         $A$        |        $B$       |         $G$        | $G^2-DB^2$ |
        | :--: | :--: | :--: | :---------------: | :----------------: | :--------------: | :----------------: | :--------: |
        |  $0$ |  $0$ |  $1$ |        $12$       |        $12$        |        $1$       |        $12$        |    $-13$   |
        |  $1$ | $12$ | $13$ |   $\color{red}1$  |        $13$        |        $1$       |        $13$        |    $12$    |
        |  $2$ |  $1$ | $12$ |   $\color{red}1$  |        $25$        |        $2$       |        $25$        |    $-3$    |
        |  $3$ | $11$ |  $3$ |   $\color{red}7$  |        $188$       |       $15$       |        $188$       |    $19$    |
        |  $4$ | $10$ | $19$ |   $\color{red}1$  |        $213$       |       $17$       |        $213$       |    $-4$    |
        |  $5$ |  $9$ |  $4$ |   $\color{red}5$  |       $1253$       |       $100$      |       $1253$       |     $9$    |
        |  $6$ | $11$ |  $9$ |   $\color{red}2$  |       $2719$       |       $217$      |       $2719$       |    $-12$   |
        |  $7$ |  $7$ | $12$ |   $\color{red}1$  |       $3972$       |       $317$      |       $3972$       |    $11$    |
        |  $8$ |  $5$ | $11$ |   $\color{red}1$  |       $6691$       |       $534$      |       $6691$       |    $-11$   |
        |  $9$ |  $6$ | $11$ |   $\color{red}1$  |       $10663$      |       $851$      |       $10663$      |    $12$    |
        | $10$ |  $5$ | $12$ |   $\color{red}1$  |       $17354$      |      $1385$      |       $17354$      |    $-9$    |
        | $11$ |  $7$ |  $9$ |   $\color{red}2$  |       $45371$      |      $3621$      |       $45371$      |     $4$    |
        | $12$ | $11$ |  $4$ |   $\color{red}5$  |      $244209$      |      $19490$     |      $244209$      |    $-19$   |
        | $13$ |  $9$ | $19$ |   $\color{red}1$  |      $289580$      |      $23111$     |      $289580$      |     $3$    |
        | $14$ | $10$ |  $3$ |   $\color{red}7$  |      $2271269$     |     $181267$     |      $2271269$     |    $-12$   |
        | $15$ | $11$ | $12$ |   $\color{red}1$  |      $2560849$     |     $204378$     |      $2560849$     |    $13$    |
        | $16$ |  $1$ | $13$ |   $\color{red}1$  |      $4832118$     |     $385645$     |      $4832118$     |    $-1$    |
        | $17$ | $12$ |  $1$ | $\color{red}{24}$ |     $118531681$    |     $9459858$    |     $118531681$    |    $13$    |
        | $18$ | $12$ | $13$ |        $1$        |     $123363799$    |     $9845503$    |     $123363799$    |    $-12$   |
        | $19$ |  $1$ | $12$ |        $1$        |     $241895480$    |    $19305361$    |     $241895480$    |     $3$    |
        | $20$ | $11$ |  $3$ |        $7$        |    $1816632159$    |    $144983030$   |    $1816632159$    |    $-19$   |
        | $21$ | $10$ | $19$ |        $1$        |    $2058527639$    |    $164288391$   |    $2058527639$    |     $4$    |
        | $22$ |  $9$ |  $4$ |        $5$        |    $12109270354$   |    $966424985$   |    $12109270354$   |    $-9$    |
        | $23$ | $11$ |  $9$ |        $2$        |    $26277068347$   |   $2097138361$   |    $26277068347$   |    $12$    |
        | $24$ |  $7$ | $12$ |        $1$        |    $38386338701$   |   $3063563346$   |    $38386338701$   |    $-11$   |
        | $25$ |  $5$ | $11$ |        $1$        |    $64663407048$   |   $5160701707$   |    $64663407048$   |    $11$    |
        | $26$ |  $6$ | $11$ |        $1$        |   $103049745749$   |   $8224265053$   |   $103049745749$   |    $-12$   |
        | $27$ |  $5$ | $12$ |        $1$        |   $167713152797$   |   $13384966760$  |   $167713152797$   |     $9$    |
        | $28$ |  $7$ |  $9$ |        $2$        |   $438476051343$   |   $34994198573$  |   $438476051343$   |    $-4$    |
        | $29$ | $11$ |  $4$ |        $5$        |   $2360093409512$  |  $188355959625$  |   $2360093409512$  |    $19$    |
        | $30$ |  $9$ | $19$ |        $1$        |   $2798569460855$  |  $223350158198$  |   $2798569460855$  |    $-3$    |
        | $31$ | $10$ |  $3$ |        $7$        |  $21950079635497$  |  $1751807067011$ |  $21950079635497$  |    $12$    |
        | $32$ | $11$ | $12$ |        $1$        |  $24748649096352$  |  $1975157225209$ |  $24748649096352$  |    $-13$   |
        | $33$ |  $1$ | $13$ |        $1$        |  $46698728731849$  |  $3726964292220$ |  $46698728731849$  |     $1$    |
        | $34$ | $12$ |  $1$ |        $24$       | $1145518138660728$ | $91422300238489$ | $1145518138660728$ |    $-13$   |
        | $35$ | $12$ | $13$ |        $1$        | $1192216867392577$ | $95149264530709$ | $1192216867392577$ |    $12$    |
    
        The period length $\ell=17$ is odd, so we need to examine the cases within two periods where $G_{k-1}^2-157B_{k-1}^2$ differs from $12$ by a square factor, i.e. the cases $k=1,9,13,19,23,31$. Their corresponding solutions are the $(fG,fB)$ in the following table:
    
        |  $k$ | $f$ |    $fG_{k-1}$    |    $fB_{k-1}$   |    $x$    |   $y$   |
        | :--: | :-: | :--------------: | :-------------: | :-------: | :-----: |
        |  $1$ | $1$ |       $13$       |       $1$       |    $13$   |   $1$   |
        |  $9$ | $1$ |      $10663$     |      $851$      |  $10663$  |  $851$  |
        | $13$ | $2$ |     $579160$     |     $46222$     |  $579160$ | $46222$ |
        | $19$ | $2$ |    $483790960$   |    $38610722$   | $-579160$ | $46222$ |
        | $23$ | $1$ |   $26277068347$  |   $2097138361$  |  $-10663$ |  $851$  |
        | $31$ | $1$ | $21950079635497$ | $1751807067011$ |   $-13$   |   $1$   |
    
        All $(fG,fB)$ are the smallest positive integer solutions in all equivalence classes of the solution set of the equation $x^2-157y^2=12$. To obtain all solutions from these solutions, we can use the fundamental solution $(46698728731849,3726964292220)$ of the corresponding Pell equation. For example, we can transform them into the fundamental solution $(x,y)$ of that equivalence class, and the corresponding solutions are also listed in the above table.
    2.  Solve the equation $x^2-157y^2=12$.
    
        This time we use the Lagrange–Matthews–Mollin algorithm to solve it. First, enumerate the square factors of $N=12$:
    
        -   when $f^2=1^2$, we have $m=12$, and the congruence equation $P^2\equiv 157\pmod{12}$ has solutions $z=\pm 1,\pm 5$;
        -   when $f^2=2^2$, we have $m=3$, and the congruence equation $P^2\equiv 157\pmod{3}$ has solutions $z=\pm 1$.
    
        Running the PQa algorithm with initial parameters $(P_0,Q_0,D)=(z,|m|,D)$ for all possible $(f,z)$ combinations, and finding the first position with $(-1)^kQ_k=1$, the corresponding $(fG_{k-1},fB_{k-1})$ is a solution. The results are shown in the following table:
    
        | $f$ |  $z$ |  $m$ |  $k$ |    $fG_{k-1}$    |    $fB_{k-1}$   |
        | :-: | :--: | :--: | :--: | :--------------: | :-------------: |
        | $1$ |  $1$ | $12$ | $32$ | $21950079635497$ | $1751807067011$ |
        | $1$ | $-1$ | $12$ |  $2$ |       $13$       |       $1$       |
        | $1$ |  $5$ | $12$ | $24$ |   $26277068347$  |   $2097138361$  |
        | $1$ | $-5$ | $12$ | $10$ |      $10663$     |      $851$      |
        | $2$ |  $1$ |  $3$ | $20$ |    $483790960$   |    $38610722$   |
        | $2$ | $-1$ |  $3$ | $14$ |     $579160$     |     $46222$     |
    
        These are all the smallest positive integer solutions in all equivalence classes listed earlier; we can transform them into the fundamental solutions using the fundamental solution of the Pell equation.
    3.  Solve the equation $x^2-79y^2=\pm 101$.
    
        Again use the Lagrange–Matthews–Mollin algorithm to solve it. Because $N=101$ is prime, we must have $f=1$. In this case, $m=101$, and the corresponding congruence equation $P^2\equiv 79\pmod{101}$ has solutions $P=\pm 33$.
    
        Running the PQa algorithm on $(P_0,Q_0,D)=(33,101,79)$ gives the following result: (the red part is the first period)
    
        | $k$ |  $P$  |  $Q$  |       $a$      |  $A$  |   $B$  |   $G$   | $G^2-DB^2$ |
        | :-: | :---: | :---: | :------------: | :---: | :----: | :-----: | :--------: |
        | $0$ |  $33$ | $101$ |       $0$      |  $0$  |   $1$  |  $-33$  |   $1010$   |
        | $1$ | $-33$ | $-10$ |       $2$      |  $1$  |   $2$  |   $35$  |    $909$   |
        | $2$ |  $13$ |  $9$  |       $2$      |  $2$  |   $5$  |   $37$  |   $-606$   |
        | $3$ |  $5$  |  $6$  | $\color{red}2$ |  $5$  |  $12$  |  $109$  |    $505$   |
        | $4$ |  $7$  |  $5$  | $\color{red}3$ |  $17$ |  $41$  |  $364$  |   $-303$   |
        | $5$ |  $8$  |  $3$  | $\color{red}5$ |  $90$ |  $217$ |  $1929$ |   $1010$   |
        | $6$ |  $7$  |  $10$ | $\color{red}1$ | $107$ |  $258$ |  $2293$ |   $-707$   |
        | $7$ |  $3$  |  $7$  | $\color{red}1$ | $197$ |  $475$ |  $4222$ |    $909$   |
        | $8$ |  $4$  |  $9$  | $\color{red}1$ | $304$ |  $733$ |  $6515$ |   $-606$   |
        | $9$ |  $5$  |  $6$  |       $2$      | $805$ | $1941$ | $17252$ |    $505$   |
    
        The period length $\ell=6$ is even. Until a period ends, there is no $Q_k=\pm 1$, so this case has no solution. Correspondingly, running the PQa algorithm on $(P_0,Q_0,D)=(-33,101,79)$ shows a similar situation. Therefore, this equation has no solution.

## Exercises

-   [LOJ 6687.「Project Euler 66」解方程](https://loj.ac/p/6687)
-   [SPOJ EQU2 - Yet Another Equation](https://www.spoj.com/problems/EQU2/)
-   [SPOJ PELL2 - Pell (Mid pelling)](https://www.spoj.com/problems/PELL2/)
-   [UVa 12909. Numeric Center](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4774)
-   [UVa 10241. Semi-triangular and also Square](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=14&page=show_problem&problem=1182)

## References and notes

-   [Pell's equation - Wikipedia](https://en.wikipedia.org/wiki/Pell%27s_equation)
-   [John P. Robertson - Solving the generalized Pell equation $x^2-Dy^2=N$](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=5ac34a344ee346855184ff949eeaed18685b155c)
-   [Keith Matthews - The Diophantine Equation $x^2-Dy^2=N$,$D>0$](http://www.numbertheory.org/PDFS/patz5.pdf)
-   [Existence of Solution to Pell’s Equation - Suryateja Gavva's Blog](https://surya-teja.com/2011/01/11/existence-of-solution-to-pells-equation/)
-   [Calculating the simple continued fraction of a quadratic irrational - Number Theory Web](http://www.numbertheory.org/php/surd.html) (PQa algorithm)
-   [Solving the diophantine equation x2–Dy2 = N, D > 0 and not a perfect square, N ≠ 0 - Number Theory Web](http://www.numbertheory.org/php/patz.html) (Lagrange–Matthews–Mollin algorithm)

[^not-square]: When $D$ is a perfect square, directly doing the factorization shows that $(x+y\sqrt{D})(x-y\sqrt{D})=N$, so all solutions can be found by traversing the divisors of $N$. In particular, when $N=1$, the equation has only the solution $(\pm 1,0)$; when $N=-1$ and $D\neq 1$, the equation has no solution.

[^neg-pell]: Some Chinese-language literature also calls it the Pell equation of the second kind.

[^half-int]: That is, a rational number of the form $n+\dfrac12$ with $n\in\mathbf Z$.

[^fundamental-solution]: Note that the definition of the fundamental solution in the Pell equation is inconsistent with the definition of the fundamental unit in the real quadratic integer ring. First, in some real quadratic integer rings, the $x,y$ in the fundamental unit $x+y\sqrt{D}$ are half-integers, so they are not solutions of the Pell equation. Second, the same real quadratic integer ring has four fundamental units, but only one fundamental solution, because the fundamental solution requires both $x,y$ to be positive.

[^solubility-neg-pell]: A more practical determination method and tool are [here](http://www.numbertheory.org/php/hardy_williams.html) and its references. The list of positive integers $D$ for which the equation $x^2-Dy^2=-1$ has a solution is [OEIS A031396](https://oeis.org/A031396).
