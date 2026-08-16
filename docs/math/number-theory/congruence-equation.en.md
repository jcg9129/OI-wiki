author: iamtwz, aofall, CCXXXI, CoelacanthusHex, Great-designer, Marcythm, Persdre, shuzhouliu, Tiphereth-A, Xeonacid

## Definition

???+ abstract "Congruence equation"
    For a positive integer $m$ and a univariate integer-coefficient polynomial $f(x)=\sum_{i=0}^n a_ix^i$ where the unknown $x\in\mathbf{Z}_m$, an equation of the form
    
    $$
    f(x)\equiv 0\pmod m\tag{1}
    $$
    
    is called a univariate **congruence equation** in the unknown $x$ modulo $m$.
    
    If $a_n\not\equiv 0\pmod m$, then the above is called an $n$-th degree congruence equation.
    
    A system of congruence equations can be defined similarly.

For content related to linear congruence equations and systems, see [linear congruence equation](./linear-equation.md) and [Chinese remainder theorem](./crt.md).

This article first studies the solvability and solution-set structure of congruence equations, and afterward briefly introduces methods for solving higher-degree congruence equations.

By the [Chinese remainder theorem](./crt.md), solving a congruence equation modulo a composite $m$ can be reduced to solving the case of a prime-power modulus. So the following only introduces the theory related to congruence equations modulo a prime power and modulo a prime.

## Congruence equations modulo a prime power

The following assumes the modulus $m=p^e~(p\in\mathbf{P},~e\in\mathbf{Z}_{>1})$.

Note that if $x_0$ is a solution of the equation

$$
f(x)\equiv 0\pmod{p^e}
$$

then $x_0$ is a solution of the equation

$$
f(x)\equiv 0\pmod{p^{e-1}}
$$

This inspires us to try to construct solutions of a higher modular power from solutions of a lower modular power. We have the following theorem:

<a id="theorem-1"></a>

???+ note "Theorem 1 (Hensel's lemma)"
    For a prime $p$ and an integer $e>1$, take an integer-coefficient polynomial $f(x)=\sum_{i=0}^na_ix^i~(p^e\nmid a_n)$, and let $f'(x)=\sum_{i=1}^nia_ix^{i-1}$ be its derivative. Let $x_0$ be a solution of the equation
    
    $$
    f(x)\equiv 0\pmod{p^{e-1}}\tag{2}
    $$
    
    then:
    
    1.  If $f'(x_0)\not\equiv 0\pmod p$, then there exists an integer $t$ such that
    
        $$
        x=x_0+p^{e-1}t \tag{3}
        $$
    
        is a solution of the equation
    
        $$
        f(x)\equiv 0\pmod{p^e} \tag{4}
        $$
    
    2.  If $f'(x_0)\equiv 0\pmod p$ and $f(x_0)\equiv 0\pmod{p^e}$, then for $t=0,1,\dots,p-1$, all $x$ determined by equation $(3)$ are solutions of equation $(4)$.
    3.  If $f'(x_0)\equiv 0\pmod p$ and $f(x_0)\not\equiv 0\pmod{p^e}$, then a solution of equation $(4)$ cannot be constructed by equation $(3)$.

???+ note "Proof"
    We assume equation $(3)$ is a solution of equation $(4)$, i.e.
    
    $$
    f(x_0+p^{e-1}t)\equiv 0\pmod{p^e}
    $$
    
    Rearranging gives
    
    $$
    f(x_0)+p^{e-1}tf'(x_0)\equiv 0\pmod{p^e}
    $$
    
    so
    
    $$
    tf'(x_0)\equiv -\frac{f(x_0)}{p^{e-1}}\pmod p\tag{5}
    $$
    
    1.  If $f'(x_0)\not\equiv 0\pmod p$, then equation $(5)$ in $t$ has a unique solution $t_0$; substituting into equation $(3)$ one can verify it is a solution of equation $(4)$.
    2.  If $f'(x_0)\equiv 0\pmod p$ and $f(x_0)\equiv 0\pmod{p^e}$, then any $t$ makes equation $(5)$ hold; substituting into equation $(3)$ one can verify they are all solutions of equation $(4)$.
    3.  If $f'(x_0)\equiv 0\pmod p$ and $f(x_0)\not\equiv 0\pmod{p^e}$, then equation $(5)$ has no solution, so a solution of equation $(4)$ cannot be constructed by equation $(3)$.

We further have a corollary:

<a id="corollary-1"></a>

???+ note "Corollary 1"
    For the $p$, $e$, $f(x)$, $x_0$ of [Theorem 1](#theorem-1),
    
    1.  If $s$ is a solution of the equation $f(x)\equiv 0\pmod p$ and $f'(s)\not\equiv 0\pmod p$, then there exists $x_s\in\mathbf{Z}_{p^e}$, $x_s\equiv s\pmod p$ such that $x_s$ is a solution of equation $(4)$.
    2.  If the equations $f(x)\equiv 0\pmod p$ and $f'(x)\equiv 0\pmod p$ have no common solution, then equation $(4)$ and the equation $f(x)\equiv 0\pmod p$ have the same number of solutions.

Thus we can reduce a congruence equation modulo a prime power to the case of a congruence equation modulo a prime.

## Congruence equations modulo a prime

The following lets $p\in\mathbf{P}$, an integer-coefficient polynomial $f(x)=\sum_{i=0}^na_ix^i$ where $p\nmid a_n$, $x\in\mathbf{Z}_p$.

<a id="theorem-2"></a>

???+ note "Theorem 2"
    If the equation
    
    $$
    f(x)\equiv 0\pmod p\tag{6}
    $$
    
    has $k$ distinct solutions $x_1,x_2,\dots,x_k~(k\leq n)$, then
    
    $$
    f(x)\equiv g(x)\prod_{i=1}^k(x-x_i)\pmod p,
    $$
    
    where $\deg g=n-k$ and $[x^{n-k}]g(x)=a_n$.

???+ note "Proof"
    Apply mathematical induction on $k$.
    
    -   When $k=1$, doing polynomial division with remainder, $f(x)=(x-x_1)g(x)+r$ where $r\in\mathbf{Z}$.
    
        From $f(x_1)\equiv 0\pmod p$ we know $r\equiv 0\pmod p$, so $f(x)\equiv(x-x_1)g(x)\pmod p$.
    -   Suppose the proposition holds for the case $k-1$ ($k>1$); now suppose $f(x)$ has $k$ distinct solutions $x_1,x_2,\dots,x_k$; then $f(x)\equiv(x-x_1)h(x)\pmod p$, and further
    
        $$
        (\forall i=2,3,\dots,k),~~0\equiv f(x_i)\equiv (x_i-x_1)h(x_i)\pmod p
        $$
    
        so $h(x)$ has $k-1$ distinct solutions $x_2,x_3,\dots,x_k$; by the induction hypothesis
    
        $$
        h(x)\equiv g(x)\prod_{i=2}^k(x-x_i)\pmod p
        $$
    
        where $\deg g=n-k$ and $[x^{n-k}]g(x)=a_n$.
    
        Therefore the proposition is proved.

<a id="corollary-2"></a>

???+ note "Corollary 2"
    For a prime $p$,
    
    -   $(\forall x\in\mathbf{Z}),~~x^{p-1}-1 \equiv \prod_{i=1}^{p-1}(x-i)\pmod p$.
    -   ([Wilson's theorem](./factorial.md#wilsons-theorem)) $(p-1)! \equiv -1 \pmod p$.

<a id="theorem-3-lagrange"></a>

???+ note "Theorem 3 (Lagrange's theorem)"
    Equation $(6)$ has at most $n$ distinct solutions.

???+ note "Proof"
    Suppose $f(x)$ has $n+1$ distinct solutions $x_1,x_2,\dots,x_{n+1}$; then by [Theorem 2](#theorem-2), for $x_1,x_2,\dots,x_n$,
    
    $$
    f(x)\equiv a_n\prod_{i=1}^n(x-x_i)\pmod p
    $$
    
    Letting $x=x_{n+1}$,
    
    $$
    0\equiv f(x_{n+1})\equiv a_n\prod_{i=1}^n(x_{n+1}-x_i)\pmod p
    $$
    
    but the right side is obviously not a multiple of $p$, so the assumption is contradictory.

<a id="corollary-3"></a>

???+ note "Corollary 3"
    If the congruence equation $\sum_{i=0}^nb_ix^i\equiv 0\pmod p$ has more than $n$ solutions, then
    
    $$
    (\forall i=0,1,\dots,n),~~p\mid b_i.
    $$

<a id="theorem-4"></a>

???+ note "Theorem 4"
    If the number of solutions of equation $(6)$ is not $p$, then there must exist an integer-coefficient polynomial $r(x)$ with $\deg r<p$ such that $f(x)\equiv 0\pmod p$ and $r(x)\equiv 0\pmod p$ have the same solution set.

???+ note "Proof"
    Without loss of generality suppose $n\geq p$; doing polynomial division with remainder on $f(x)$,
    
    $$
    f(x)=g(x)\left(x^p-x\right)+r(x)
    $$
    
    where $\deg r<p$.
    
    By [Fermat's little theorem](./fermat.md), for any integer $x$, $x^p\equiv x\pmod p$, so
    
    -   If $r(x)\equiv 0\pmod p$, then by [Corollary 2](#corollary-2) $f(x)$ has $p$ distinct solutions.
    -   If $r(x)\not\equiv 0\pmod p$, then from $f(x)\equiv r(x)\pmod p$, $f(x)$ and $r(x)$ have the same solution set.

We can use this theorem to reduce the degree of a congruence equation.

<a id="theorem-5"></a>

???+ note "Theorem 5"
    Let $n\leq p$; then the equation
    
    $$
    x^n+\sum_{i=0}^{n-1}a_ix^i\equiv 0\pmod p\tag{7}
    $$
    
    has $n$ solutions if and only if there exist integer-coefficient polynomials $q(x)$, $r(x)~(\deg r < n)$ such that
    
    $$
    x^p-x=f(x)q(x)+pr(x). \tag{8}
    $$

???+ note "Proof"
    -   Necessity: by polynomial division, there exist integer-coefficient polynomials $q(x)$, $r_1(x)~(\deg r_1 < n)$ such that
    
        $$
        x^p-x=f(x)q(x)+r_1(x).
        $$
    
        If equation $(7)$ has $n$ solutions, then $r_1\equiv 0\pmod p$ also has the same $n$ solutions, and by [Corollary 3](#corollary-3) there exists an integer-coefficient polynomial $r(x)$ satisfying $r_1(x)=pr(x)$, which proves the proposition.
    -   Sufficiency: if equation $(8)$ holds, then by [Fermat's little theorem](./fermat.md), for any integer $x$,
    
        $$
        0\equiv x^p-x\equiv f(x)q(x)\pmod p.
        $$
    
        That is, the equation $f(x)q(x)\equiv 0\pmod p$ has $p$ solutions.
    
        Let the number of solutions of equation $(7)$ be $s$; then by [Lagrange's theorem](#theorem-3-lagrange), $s\leq n$.
    
        And since $\deg q=p-n$, by [Lagrange's theorem](#theorem-3-lagrange) the number of solutions of $q(x)\equiv 0\pmod p$ does not exceed $p-n$; and the solution set of the equation $f(x)q(x)\equiv 0\pmod p$ is the union of the solution set of $f(x)\equiv 0\pmod p$ and the solution set of $q(x)\equiv 0\pmod p$, so $s+(p-n)\geq p$, giving $s\geq n$.
    
        Therefore $s=n$.

For a non-monic polynomial, since $\mathbf{Z}_p$ is a field, one can turn it into a monic polynomial, and thus this theorem applies.

<a id="theorem-6"></a>

???+ note "Theorem 6"
    Let $n\mid p-1$, $p\nmid a$; then the equation
    
    $$
    x^n\equiv a\pmod p\tag{9}
    $$
    
    has a solution if and only if
    
    $$
    a^{\frac{p-1}{n}}\equiv 1\pmod p.
    $$
    
    Moreover, if $(9)$ has a solution, then the number of solutions is $n$.

???+ note "Note"
    For the specific structure of the solution set of equation $(9)$, see [$k$-th power residue](./residue.md).

???+ note "Proof"
    -   Necessity: if equation $(9)$ has a solution $x_0$, then
    
        $$
        a^{\frac{p-1}{n}}\equiv {\left(x_0^n\right)}^{\frac{p-1}{n}}\equiv 1\pmod p
        $$
    -   Sufficiency: if $a^{\frac{p-1}{n}}\equiv 1\pmod p$, then
    
        $$
        \begin{aligned}
            x^p-x&=x\left(x^{p-1}-1\right)\\
            &=x\left(\left(x^n\right)^{\frac{p-1}{n}}-a^{\frac{p-1}{n}}+a^{\frac{p-1}{n}}-1\right)\\
            &=\left(x^n-a\right)P(x)+x\left(a^{\frac{p-1}{n}}-1\right)\\
        \end{aligned}
        $$
    
        where $P(x)$ is some integer-coefficient polynomial, so by [Theorem 5](#theorem-5) equation $(9)$ has $n$ solutions.

## Methods for solving higher-degree congruence equations (systems)

First, with the help of the [Chinese remainder theorem](./crt.md), we can convert solving a **system of congruence equations** into solving a **congruence equation**, and convert solving a congruence equation modulo a **composite** $m$ into solving a congruence equation modulo a **prime power**. Afterward, with the help of [Theorem 1](#theorem-1), we convert solving a congruence equation modulo a **prime power** into solving a congruence equation modulo a **prime**.

Combining the several theorems on congruence equations modulo a prime, we only need to consider the method for the equation

$$
x^n+\sum_{i=0}^{n-1}a_ix^i\equiv 0\pmod p
$$

where $p$ is prime and $n<p$.

We can eliminate the $x^{n-1}$ term by substituting $x$ with $x-\dfrac{a_{n-1}}{n}$, so we only need to consider the method for the equation

$$
x^n+\sum_{i=0}^{n-2}a_ix^i\equiv 0\pmod p\tag{10}
$$

where $p$ is prime and $n<p$.

-   If $n=1$, for the method see [linear congruence equation](./linear-equation.md).
-   If $n=2$, for the method see [quadratic residue](./quad-residue.md).
-   If equation $(10)$ can be reduced to

    $$
    x^n\equiv a\pmod p,
    $$

    then for the method see [$k$-th power residue](./residue.md).

## References

1.  [Congruence Equation -- from Wolfram MathWorld](https://mathworld.wolfram.com/CongruenceEquation.html)
2.  [Lagrange's theorem (number theory) - Wikipedia](https://en.wikipedia.org/wiki/Lagrange%27s_theorem_%28number_theory%29)
3.  Pan Chengdong, Pan Chengbiao. Elementary Number Theory.
4.  Feng Keqin. Elementary Number Theory and Its Applications.
5.  Min Sihe, Yan Shijian. Elementary Number Theory.
