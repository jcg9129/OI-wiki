author: billchenchina, c-forrest, CCXXXI, danielqfmai, Enter-tainer, Great-designer, HeRaNO, lychees, Menci, Nanarikom, ouuan, shuzhouliu, sshwy, Tiphereth-A

This article introduces the Dirichlet convolution and the Dirichlet generating function.

## Dirichlet convolution

The **Dirichlet convolution** of arithmetic functions $f(n)$ and $g(n)$, denoted $f \ast g$, is defined as the arithmetic function

$$
(f \ast g)(n) = \sum_{k\mid n}f(k)g\left(\dfrac{n}{k}\right) = \sum_{k\ell=n}f(k)g(\ell).
$$

Dirichlet convolution is an important operation on arithmetic functions. Many properties of arithmetic functions are uncovered through this operation.

???+ example "Examples"
    1.  The unit function $\varepsilon$ is the Dirichlet convolution of the Möbius function $\mu$ and the constant function $1$:
    
        $$
        \varepsilon=\mu \ast 1 \iff\varepsilon(n)=\sum_{d\mid n}\mu(d).
        $$
    
    2.  The number-of-divisors function $\tau$ is the Dirichlet convolution of the constant function $1$ with itself:
    
        $$
        \tau=1 \ast 1 \iff \tau(n)=\sum_{d\mid n}1.
        $$
    
    3.  The sum-of-divisors function $\sigma$ is the Dirichlet convolution of the identity function $\mathrm{id}$ and the constant function $1$:
    
        $$
        \sigma=\mathrm{id} \ast 1 \iff\sigma(n)=\sum_{d\mid n}d.
        $$
    
    4.  Euler's totient function $\varphi$ is the Dirichlet convolution of the identity function $\mathrm{id}$ and the Möbius function $\mu$:
    
        $$
        \varphi=\mathrm{id}\ast \mu \iff\varphi(n)=\sum_{d\mid n}d\cdot\mu\left(\frac{n}{d}\right).
        $$

[Möbius inversion](./mobius.md) uses $\varepsilon=\mu \ast 1$ to transform arithmetic-function identities.

### Properties

Dirichlet convolution has a series of algebraic properties.

???+ note "Theorem"
    Let $f,g,h$ all be arithmetic functions. Then, we have:
    
    1.  **Commutativity**: $f\ast g=g\ast f$.
    2.  **Associativity**: $(f\ast g)\ast h=f\ast(g\ast h)$.
    3.  **Distributivity**: $(f+g)\ast h = f\ast h + g\ast h$.
    4.  **Identity element**: $f\ast\varepsilon = \varepsilon \ast f = f$, where $\varepsilon(n) = [n=1]$ is the convolution identity and $[\cdot]$ is the Iverson bracket.
    5.  **Inverse element**: if and only if $f(1)\neq 0$, there exists $g$ such that $f\ast g=g\ast f=\varepsilon$, and $g$ is called the **Dirichlet inverse** of $f$, which can be denoted $f^{-1}$. Moreover, the inverse $g$ satisfies the recurrence
    
        $$
        g(n) = \dfrac{\varepsilon(n) - \sum_{k\ell = n,~k\neq 1}f(k)g(\ell)}{f(1)}.
        $$

??? note "Proof"
    To verify commutativity, direct computation shows
    
    $$
    (f\ast g)(n) = \sum_{k\ell=n}f(k)g(\ell) = (g\ast f)(n).
    $$
    
    To verify associativity, direct computation shows
    
    $$
    ((f\ast g)\ast h)(n) = \sum_{k\ell m = n}f(k)g(\ell)h(m) = (f\ast (g\ast h))(n).
    $$
    
    To verify distributivity, direct computation shows
    
    $$
    \begin{aligned}
    ((f+g)\ast h)(n) &= \sum_{k\ell = n}(f(k) + g(k))h(\ell) \\
    &= \sum_{k\ell=n}f(k)h(\ell) + \sum_{k\ell=n}g(k)h(\ell) = (f\ast h+g\ast h)(n).
    \end{aligned}
    $$
    
    To verify that $\varepsilon(n)$ is the identity element, direct computation shows
    
    $$
    (f\ast\varepsilon)(n) = \sum_{k\ell = n}f(k)\varepsilon(\ell) = f(n).
    $$
    
    The second equality is because $\varepsilon(\ell)$ takes a nonzero value only when $\ell=1$, i.e. $k=n$.
    
    Finally, we need to prove that $f^{-1}$ exists if and only if $f(1)\neq 0$. For any $f$, suppose there exists $g$ such that $f\ast g=\varepsilon$. This means
    
    $$
    (f\ast g)(n) = \sum_{k\ell = n}f(k)g(\ell) = \varepsilon(n).
    $$
    
    This in fact gives a series of equations about the values of $g(n)$, from which $g(n)$ can be directly solved. In particular, when $n=1$, the equation becomes $f(1)g(1)=1$, so for $g$ to exist, it is at least required that $f(1)\neq 0$. And as long as $f(1)\neq 0$, we can directly solve
    
    $$
    g(n) = \dfrac{\varepsilon(n) - \sum_{k\ell = n,~k\neq 1}f(k)g(\ell)}{f(1)}.
    $$
    
    It can be used to recursively compute the values of $g(n)$. Therefore, the inverse $g$ exists if and only if $f(1)\neq 0$.

In the language of abstract algebra, these algebraic properties show that all arithmetic functions form a [commutative ring](../algebra/basic.md#rings) under (pointwise) addition and Dirichlet convolution, and its set of units is exactly those functions taking a nonzero value at $n=1$. This ring is called the **Dirichlet ring**.

Multiplicative functions are a special class of arithmetic functions. They are closed under both Dirichlet convolution and Dirichlet inverse.

???+ note "Theorem"
    Let $f,g$ be multiplicative functions; then $f\ast g$ is also a multiplicative function. Moreover, the inverse $f^{-1}$ must exist, and it is also a multiplicative function.

??? note "Proof"
    For the first point, let $h=f\ast g$; direct verification shows that for $n_1\perp n_2$, we have
    
    $$
    \begin{aligned}
    h(n_1)h(n_2) &= \left(\sum_{k_1\ell_1=n_1}f(k_1)g(\ell_1)\right)\left(\sum_{k_2\ell_2=n_2}f(k_2)g(\ell_2)\right)\\
    &= \sum_{k_1\ell_1=n_1,~k_2\ell_2=n_2}f(k_1)f(k_2)g(\ell_1)g(\ell_2)\\
    &= \sum_{k\ell = n_1n_2}f(k)g(\ell) \\
    &= h(n_1n_2).
    \end{aligned}
    $$
    
    Here, the logic of changing the summation order in the third equality is: when $k$ ranges over the divisors of $n_1n_2$, the prime factors of $k$ can be divided into two classes according to whether they are prime factors of $n_1$ or of $n_2$; multiplying together the prime factors (with multiplicity) in the two classes respectively gives $k_1$ and $k_2$, which will range over the divisors of $n_1$ and $n_2$ respectively; conversely, from divisors $k_1$ and $k_2$ of $n_1$ and $n_2$, one can always obtain a divisor $k=k_1k_2$ of $n_1n_2$.
    
    For the second point, let $g=f^{-1}$ and consider applying mathematical induction. First, $g(1)=1/f(1)=1$. In this case, the recursive formula for the inverse can be written as
    
    $$
    g(n) = \varepsilon(n) - \sum_{k\ell = n,~k\neq 1} f(k)g(\ell).
    $$
    
    So, for $n_1\perp n_2$ and $n_1n_2 > 1$, we have
    
    $$
    \begin{aligned}
    g(n_1n_2) &= -\sum_{k\ell=n_1n_2,~k\neq 1}f(k)g(\ell) \\
    &= -\sum_{k_1\ell_1=n_1,~k_2\ell_2=n_2,~k_1k_2\neq 1}f(k_1)f(k_2)g(\ell_1)g(\ell_2)\\
    &= f(1)f(1)g(n_1)g(n_2) - \sum_{k_1\ell_1=n_1,~k_2\ell_2=n_2}f(k_1)f(k_2)g(\ell_1)g(\ell_2)\\
    &= g(n_1)g(n_2) - \left(\sum_{k_1\ell_1=n_1}f(k_1)g(\ell_1)\right)\left(\sum_{k_2\ell_2=n_2}f(k_2)g(\ell_2)\right) \\
    &= g(n_1)g(n_2) - \varepsilon(n_1)\varepsilon(n_2)\\
    &= g(n_1)g(n_2).
    \end{aligned}
    $$
    
    Here, the second equality uses the induction hypothesis, i.e. for $\ell_1\ell_2 < n_1n_2$ and $\ell_1\perp\ell_2$, the condition $g(\ell_1\ell_2)=g(\ell_1)g(\ell_2)$ holds.

In the language of abstract algebra, all multiplicative functions form a [subgroup](../algebra/group-theory.md#subgroups) of the multiplicative group of the Dirichlet ring under Dirichlet convolution.

Even more special are completely multiplicative functions.

???+ note "Theorem"
    Let $\alpha$ be a completely multiplicative function and $f,g$ be arithmetic functions. Then, we have:
    
    1.  Distributivity: $(\alpha f)\ast(\alpha g) = \alpha\cdot(f\ast g)$.
    2.  Inverse: $(\alpha f)^{-1}=\alpha f^{-1}$, as long as $f^{-1}$ exists.
    3.  A multiplicative function $f$ is completely multiplicative if and only if $f^{-1}=\mu f$, where $\mu$ is the [Möbius function](./mobius.md#möbius-function).

??? note "Proof"
    For the first item, direct verification shows
    
    $$
    \begin{aligned}
    ((\alpha f)\ast(\alpha g))(n) &= \sum_{k\ell = n}(\alpha f)(k)(\alpha g)(\ell) \\
    &= \sum_{k\ell = n}\alpha(k)f(k)\alpha(\ell)g(\ell) \\
    &= \sum_{k\ell = n}\alpha(n)f(k)g(\ell) \\
    &= \alpha(n)(f\ast g)(n).
    \end{aligned}
    $$
    
    Here, the third equality uses the property of completely multiplicative functions: $\alpha(n)=\alpha(k)\alpha(\ell)$ holds for all $n=k\ell$.
    
    For the second item, using the first item we have
    
    $$
    (\alpha f)\ast(\alpha f^{-1}) = \alpha(f\ast f^{-1}) = \alpha\varepsilon = \varepsilon.
    $$
    
    Here, the last equality only uses $\alpha(1)=1$. By the definition of the inverse, $(\alpha f)^{-1}=\alpha f^{-1}$.
    
    For the third item, using the second item and $1^{-1}=\mu$, if $f$ is completely multiplicative, then
    
    $$
    f^{-1} = (1f)^{-1} = 1^{-1}\cdot f = \mu f.
    $$
    
    Here, $1$ is the constant function. Conversely, if $f$ is a multiplicative function and $f^{-1}=\mu f$, then it suffices to prove that $f(p^e)=f(p)^e$ holds for all primes $p$ and $e\in\mathbf N_+$ to prove that $f$ is completely multiplicative. To this end, apply mathematical induction on $e\in\mathbf N_+$. At the induction base $e=1$ the proposition obviously holds. For any $e > 1$, applying the recursive formula for the inverse, we have
    
    $$
    \begin{aligned}
    f^{-1}(p^e) &= -\sum_{i=1}^{e}f(p^i)f^{-1}(p^{e-i}) \\
    &= -\sum_{i=1}^{e}f(p^i)\mu(p^{e-i})f(p^{e-i})\\
    &= -f(p^e)f(1)\mu(1) - f(p^{e-1})\mu(p)f(p)\\
    &= -f(p^e) + f(p)^e.
    \end{aligned}
    $$
    
    Here, the last equality uses the induction hypothesis $f(p^{e-1})=f(p)^{e-1}$. Applying $f^{-1}=\mu f$, we obtain
    
    $$
    f^{-1}(p^e) = \mu(p^e)f(p^e) = 0.
    $$
    
    Substituting into the previous expression, we obtain
    
    $$
    f(p^e) = f(p)^e.
    $$
    
    So, the induction step holds. The original proposition is proven.

In the language of abstract algebra, if $\alpha$ is a completely multiplicative function, the map $f\mapsto \alpha f$ is an [endomorphism](../algebra/ring-theory.md#ideals) of the Dirichlet ring.

## Dirichlet generating function

Closely related to Dirichlet convolution is the Dirichlet generating function.

The **Dirichlet series generating function** (DGF) corresponding to an arithmetic function $f(n)$—that is, the sequence $\{f(n)\}$—is defined as the formal Dirichlet series:

$$
F(s) = \sum_{n=1}^{\infty}\dfrac{f(n)}{n^s}.
$$

The $s$ in the series is a formal indeterminate. In common Dirichlet generating functions, $s$ can often be regarded as a complex variable, allowing one to discuss the analytic properties of Dirichlet series, but this is beyond the scope of competitive programming.

The product of Dirichlet generating functions corresponds to the Dirichlet convolution of the corresponding arithmetic functions:

???+ note "Theorem"
    For arithmetic functions $f,g$ and their Dirichlet generating functions $F,G$, the generating function of their Dirichlet convolution $f\ast g$ equals $F\cdot G$.

??? note "Proof"
    Direct verification:
    
    $$
    \begin{aligned}
    F(s)G(s) &= \left(\sum_{k=1}^\infty\dfrac{f(k)}{k^s}\right)\left(\sum_{\ell=1}^\infty\dfrac{g(\ell)}{\ell^s}\right)= \sum_{k=1}^\infty\sum_{\ell=1}^\infty\dfrac{f(k)g(\ell)}{(k\ell)^s}\\
    &= \sum_{n=1}^{\infty}\dfrac{\sum_{k\ell = n}f(k)g(\ell)}{n^s} = \sum_{n=1}^\infty\dfrac{(f\ast g)(n)}{n^s}.
    \end{aligned}
    $$

Using the correspondence between Dirichlet convolution and the product of Dirichlet generating functions, one can understand the properties of Dirichlet convolution from the perspective of Dirichlet generating functions. Since the multiplication of formal Dirichlet series satisfies commutativity, associativity, and distributivity over addition, the Dirichlet convolution of arithmetic functions satisfies the same algebraic properties.

### Euler product

The special nature of multiplicative functions is likewise reflected in Dirichlet generating functions. Because integers have the [unique factorization theorem](./basic.md#fundamental-theorem-of-arithmetic), the generating function $F(s)$ of a multiplicative function $f(n)$ can be written in the following form:

$$
\begin{aligned}
F(s) &= \sum_{n=1}^{\infty}\dfrac{f(n)}{n^s} = \sum_{n=1}^{\infty}\prod_{p\in\mathbf P}\dfrac{f(p^{e})}{p^{es}} = \prod_{p\in\mathbf P}\sum_{e=0}^{\infty}\dfrac{f(p^e)}{p^{es}}\\
&= \prod_{p\in\mathbf P}\left(1 + \dfrac{f(p)}{p^s} + \dfrac{f(p^2)}{p^{2s}} + \dfrac{f(p^3)}{p^{3s}} + \cdots\right).
\end{aligned}
$$

This means that $F(s)$ can be decomposed into a product of several $F_p(s)$, and the arithmetic function corresponding to each $F_p(s)$ can take nonzero values only at powers of $p$. This infinite product is also called the **Euler product**. If both $F(s)$ and $G(s)$ can be decomposed into a similar form, then so can their product; corresponding this observation to arithmetic functions, it says that the Dirichlet convolution of multiplicative functions is still a multiplicative function.

Furthermore, if $f(n)$ is also a completely multiplicative function, then $f(p^e)=f(p)^e$, and the above expression can be further simplified:

$$
F(s) = \prod_{p\in\mathbf P}\sum_{e=0}^{\infty}\dfrac{f(p)^e}{p^{es}} = \prod_{p\in\mathbf P}\left(1-\dfrac{f(p)}{p^s}\right)^{-1}.
$$

Unlike multiplicative functions, the form of the Dirichlet generating function of a completely multiplicative function is not closed under multiplication. Therefore, the Dirichlet convolution and Dirichlet inverse of completely multiplicative functions are not necessarily completely multiplicative, but they must be multiplicative.

???+ example "Examples"
    1.  The unit function $\varepsilon(n)$ is a completely multiplicative function. Its Dirichlet generating function is the constant function with respect to the indeterminate $s$
    
        $$
        E(s) = \sum_{n=1}^{\infty}\dfrac{\varepsilon(n)}{n^s} = 1.
        $$
    
    2.  The constant function $1(n)$ is a completely multiplicative function. Its Dirichlet generating function is the Riemann zeta function
    
        $$
        I(s) = \sum_{n=1}^{\infty}\dfrac{1}{n^s} = \prod_{p\in\mathbf P}\dfrac{1}{1-p^{-s}} = \zeta(s).
        $$
    
    3.  The Möbius function $\mu(n)$ is the Dirichlet inverse of the constant function. Its Dirichlet generating function is the reciprocal of $\zeta(s)$:
    
        $$
        M(s) = \sum_{n=1}^{\infty}\dfrac{\mu(n)}{n^s} = \prod_{p\in\mathbf P}(1-p^{-s}) = \dfrac{1}{\zeta(s)}.
        $$
    
    4.  The power function $\operatorname{id}_k(n)=n^k$ is a completely multiplicative function. In particular, when $k=0$ it is the constant function; when $k=1$ it is the identity function. Its Dirichlet generating function is
    
        $$
        I_k(s) = \sum_{n=1}^{\infty}\dfrac{n^k}{n^s} = \prod_{p\in\mathbf P}\dfrac{1}{1-p^{k-s}} = \zeta(s-k).
        $$
    
    5.  Euler's totient function $\varphi(n)$ is a multiplicative function. Its Dirichlet generating function is
    
        $$
        \begin{aligned}
        \Phi(s) &= \prod_{p\in\mathbf P}\left(1+\dfrac{p-1}{p^s} + \dfrac{p(p-1)}{p^{2s}} + \dfrac{p^2(p-1)}{p^{3s}}+\cdots\right)\\
        &= \prod_{p\in\mathbf P}\left(\dfrac{1}{1-p^{1-s}}-\dfrac{1}{p^s}\dfrac{1}{1-p^{1-s}}\right) = \prod_{p\in\mathbf P}\dfrac{1-p^{-s}}{1-p^{1-s}} = \dfrac{\zeta(s-1)}{\zeta(s)}.
        \end{aligned}
        $$
    
        Combined with the Dirichlet series expression of the power function, we obtain $\mathrm{id} = \varphi\ast 1$.
    
    6.  The divisor function $\sigma_k(n)=\sum_{d\mid n}d^k$ is a multiplicative function. Its Dirichlet generating function is
    
        $$
        \begin{aligned}
        \Sigma_k(s) &= \prod_{p\in\mathbf P}\left(1+\dfrac{1+p^k}{p^s}+\dfrac{1+p^k+p^{2k}}{p^{2s}}+\dfrac{1+p^k+p^{2k}+p^{3k}}{p^{3s}}+\cdots\right) \\
        &= \prod_{p\in\mathbf P}\dfrac{1}{1-p^k}\left((1-p^k)+\dfrac{1-p^{2k}}{p^s}+\dfrac{1-p^{3k}}{p^{2s}}+\dfrac{1-p^{4k}}{p^{3k}}+\cdots\right)\\
        &= \prod_{p\in\mathbf P}\dfrac{1}{1-p^k}\left(\dfrac{1}{1-p^{-s}} - \dfrac{p^k}{1-p^{k-s}}\right)\\
        &= \prod_{p\in\mathbf P}\dfrac{1}{(1-p^{-s})(1-p^{k-s})} = \zeta(s-k)\zeta(s).
        \end{aligned}
        $$
    
        Combined with the Dirichlet expression of the power function, we obtain $\sigma_k = \mathrm{id}_k\ast 1$. This is exactly the defining expression of $\sigma_k$.
    
    7.  The indicator function of squarefree numbers $u(n)=|\mu(n)|$ is a multiplicative function. Its Dirichlet generating function is
    
        $$
        U(s) = \prod_{p\in\mathbf P}(1+p^{-s}) = \prod_{p\in\mathbf P}\dfrac{1-p^{-2s}}{1-p^{-s}} = \dfrac{\zeta(s)}{\zeta(2s)}.
        $$

### Applications

Dirichlet generating functions can be used to represent a multiplicative function as a Dirichlet convolution.

For example, in the process of Du's sieve, to compute the prefix sum of a multiplicative function $f$, one needs to find another multiplicative function $g$ such that both $f\ast g$ and $g$ can have their prefix sums computed quickly. This process can be derived using Dirichlet generating functions.

Taking the example problem of the Du's sieve section, [Luogu P3768 简单的数学题](../number-theory/du.md#problem-2), as an example, one needs to construct an arithmetic function $g(n)$ satisfying the above conditions for $f(n)=n^2\varphi(n)$. Since $f$ is a multiplicative function, its Dirichlet generating function is

$$
F(s) = \prod_{p\in\mathbf P}\left(1 + \sum_{k=1}^{\infty}\dfrac{p^{3k-1}(p-1)}{p^{ks}}\right) = \prod_{p\in\mathbf P}\dfrac{1-p^{2-s}}{1-p^{3-s}} = \dfrac{\zeta(s-3)}{\zeta(s-2)}.
$$

Comparing with the Dirichlet generating function of the power function, as long as we take $g = \mathrm{id}_2$, we have $f \ast g = \mathrm{id}_3$. Both can have their prefix sums computed quickly.

## Computation of Dirichlet convolution

This section discusses the computation of Dirichlet convolution, i.e. the problem of, given sequences $\{f(k)\}_{k=1}^n$ and $\{g(k)\}_{k=1}^n$, computing the first several terms $\{h(k)\}_{k=1}^n$ of the Dirichlet convolution $h=f\ast g$. Depending on the properties of the functions involved, the complexity of the algorithm also differs slightly.

### General case

If $f,g,h$ have no special properties, then the computation of Dirichlet convolution can only use its definition:

$$
h(n) = \sum_{k\ell = n}f(k)g(\ell).
$$

Enumerate $k$ and $\ell$, and accumulate the contribution $f(k)g(\ell)$ into $h(k\ell)$. The enumeration complexity is

$$
O\left(\sum_{k=1}^{n}\dfrac{n}{k}\right) = O(n\log n).
$$

A reference implementation is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/dirichlet/dirichlet-1.cpp:core"
    ```

### Case of convolution with a multiplicative function

If $g$ is a multiplicative function, then one can use the Euler product to speed up the computation of the Dirichlet convolution. Computing $h$ is equivalent to computing the coefficients of the various terms in its Dirichlet generating function $H$. Since

$$
H(s) = F(s)G(s) = F(s)\prod_{p\in\mathbf P}G_p(s).
$$

where $G_p(s)$ is the factor in the Euler product decomposition of $G(s)$ that contains only the coefficients at powers of $p$:

$$
G_p(s) = \sum_{p^k\le n}\dfrac{f(p^k)}{p^{ks}} = 1 + \dfrac{f(p)}{p^s} + \dfrac{f(p^2)}{p^{2s}} + \cdots.
$$

Then, starting from $F(s)$, traverse all primes $p$ not exceeding $n$, and multiply $G_p(s)$ one by one; likewise we can obtain the final result $H(s)$. When multiplying $G_p(s)$, simply apply the brute-force enumeration algorithm from the general case. The total number of enumerations is

$$
\sum_{p\in\mathbf P,~p\le n}\sum_{k=1}^{\infty}\left\lfloor\dfrac{n}{p^k}\right\rfloor \le \sum_{p\in\mathbf P,~p\le n}\dfrac{n}{p-1} \le \sum_{p\in\mathbf P,~p\le n}\dfrac{2n}{p} \in O(n\log\log n).
$$

The complexity estimate in the last step is consistent with the proof of the complexity of the [Sieve of Eratosthenes](./sieve.md#埃拉托斯特尼筛法). So, the time complexity of this algorithm is $O(n\log\log n)$.

A reference implementation is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/dirichlet/dirichlet-2.cpp:core"
    ```

In particular, when the multiplicative function $g$ is a completely multiplicative function or its Dirichlet inverse, for example when $g = 1$ or $g = \mu$, the algorithm can be further simplified. In this case, the computation of the Dirichlet convolution $h = f\ast g$ can adopt the [Dirichlet prefix sum/difference](./mobius.md#dirichlet-prefix-sum) algorithm with a smaller constant factor, but the time complexity of the algorithm is still $O(n\log\log n)$.

### Case where the result is a multiplicative function

Finally, consider the case where $h$ is a multiplicative function. In particular, when $f,g$ are both multiplicative functions, $h=f \ast g$ is a multiplicative function. To compute $h$, one only needs to determine its values at prime powers, and then it can be computed in $O(n)$ time via the [linear sieve](./sieve.md#线性筛法). And the value $h(p^e)$ at the prime power $p^e$ can be directly computed by brute force:

$$
h(p^e) = \sum_{i=0}^e f(p^i)g(p^{e-i}).
$$

The number of enumerations needed for these brute-force computations is

$$
\begin{aligned}
\sum_{p\in\mathbf P,~p\le n}\sum_{e=1}^{\lfloor\log_p n\rfloor}(e+1) &\le \sum_{p\in\mathbf P,~p\le\sqrt{n}}\lfloor\log_p n\rfloor^2 + \sum_{p\in\mathbf P,~\sqrt{n} < p\le n}1 \\
&\le \sqrt{n}(\log_2 n)^2 + n \in O(n).
\end{aligned}
$$

Therefore, the total time complexity of this algorithm is $O(n)$.

A reference implementation is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/dirichlet/dirichlet-3.cpp:core"
    ```

## References and notes

-   [Dirichlet convolution - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_convolution)
-   [Dirichlet series - Wikipedia](https://en.wikipedia.org/wiki/Dirichlet_series)
-   [Euler product - Wikipedia](https://en.wikipedia.org/wiki/Euler_product)
-   [Dirichlet 積と、数論関数の累積和 by maspy](https://maspypy.com/dirichlet-%e7%a9%8d%e3%81%a8%e3%80%81%e6%95%b0%e8%ab%96%e9%96%a2%e6%95%b0%e3%81%ae%e7%b4%af%e7%a9%8d%e5%92%8c)
