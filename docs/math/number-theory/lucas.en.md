Prerequisite knowledge: [factorial modulo](./factorial.md)

## Introduction

This article discusses solving large binomial coefficients modulo a number. The binomial coefficient, also called the combination number, refers to the expression:

$$
\binom{n}{k} = \dfrac{n!}{k!(n-k)!}.
$$

When the scale is not large, the binomial coefficient can be solved via the [recurrence formula](../combinatorics/combination.md#properties-of-binomial-coefficients-binomial-corollaries), with time complexity $O(nk)$; it can also be solved in $O(n)$ time by computing the factorials of the numerator and denominator under a relatively large prime modulus $p>n$. But when the problem scale is very large ($n\sim 10^{18}$), these methods no longer apply.

Based on Lucas' theorem and its generalization, this article discusses a method that can solve binomial coefficients when the modulus is not too large ($m \sim 10^6$). More precisely, as long as the sum of all prime powers in the unique factorization $m=\prod p_i^{e_i}$ of the modulus (i.e. $\sum p_i^{e_i}$) is on the scale of $10^6$, this method can be used, because the preprocessing of the algorithm is roughly equivalent to this scale.

## Lucas' theorem

First discuss the case where the modulus is a prime $p$. In this case, we have Lucas' theorem:

???+ note "Lucas' theorem"
    For a prime $p$, we have
    
    $$
    \binom{n}{k}\equiv \binom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}\binom{n\bmod p}{k\bmod p}\pmod p.
    $$
    
    where, when $n<k$, the binomial coefficient $\dbinom{n}{k}$ is defined to be $0$.

??? note "Proof using generating functions"
    Consider the value of $\displaystyle\binom{p}{n} \bmod p$. Because
    
    $$
    \binom{p}{n} = \frac{p!}{n!(p-n)!},
    $$
    
    so, when $n\neq 0,p$, the denominator has no factor $p$, but the numerator has a factor $p$, so the fraction must be a multiple of $p$, and the remainder modulo $p$ is $0$; when $n=0,p$, the fraction is $1$. Therefore,
    
    $$
    \binom{p}{n} \equiv [n=0\lor n=p] \pmod p.
    $$
    
    Denote $f(x) = ax^n + bx^m$. In general, by [binomial expansion](../combinatorics/combination.md#binomial-theorem) and [Fermat's little theorem](./fermat.md#fermats-little-theorem), we have
    
    $$
    \begin{aligned}
    (f(x))^p 
    &= \left(ax^n + bx^m\right)^p \\
    &= \sum_{k=0}^p\binom{p}{k}(ax^n)^k(bx^m)^{p-k}\\
    &\equiv a^px^{pn} + b^px^{pm} \\
    &\equiv a(x^p)^n+b(x^p)^m\\
    &= f(x^p) \pmod p.
    \end{aligned}
    $$
    
    Here, the congruence in the third line uses the conclusion explained earlier, namely that only when $k=0,p$ is the binomial coefficient not a multiple of $p$.
    
    Using this conclusion, examine the binomial expansion:
    
    $$
    \begin{aligned}
    (1+x)^n &= (1+x)^{p\lfloor n/p\rfloor}(1+x)^{n\bmod p} \\
    &\equiv (1+x^p)^{\lfloor n/p\rfloor}(1+x)^{n\bmod p} \pmod p.
    \end{aligned}
    $$
    
    On the left side of the equation, the coefficient of the term $x^k$ is
    
    $$
    \binom{n}{k}\bmod p.
    $$
    
    Turn to computing the coefficient of the term $x^k$ on the right side of the equation. The degrees of the various terms in the first factor must be multiples of $p$, and the degrees of the various terms in the second factor must be less than $p$, and the way to decompose $k$ into the sum of two such parts is unique, i.e. division with remainder: $k=p\lfloor k/p\rfloor +(k\bmod p)$. Therefore, the first factor can only contribute its $p\lfloor k/p\rfloor$-degree term, and the second factor can only contribute its $k\bmod p$-degree term. So, the coefficient of $x^k$ on the right side of the equation is the product of the coefficients of the terms contributed by the two factors:
    
    $$
    \binom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}\binom{n\bmod p}{k\bmod p}\bmod p.
    $$
    
    Setting the coefficients on both sides equal, we obtain Lucas' theorem.

??? note "Proof using the conclusions of factorial modulo"
    Here we provide a proof method based on the conclusions related to [factorial modulo](./factorial.md#the-case-of-a-prime-modulus), to facilitate establishing a connection with the exLucas method later. We know the binomial coefficient
    
    $$
    \binom{n}{k} = \dfrac{n!}{k!(n-k)!}.
    $$
    
    Separating the power of $p$ in the factorial $n!$ from the other factors, we obtain the decomposition:
    
    $$
    n! = p^{\nu_p(n!)}(n!)_p.
    $$
    
    We then obtain the expression for the binomial coefficient:
    
    $$
    \binom{n}{k} = p^{\nu_p(n!)-\nu_p(k!)-\nu_p((n-k)!)}\dfrac{(n!)_p}{(k!)_p((n-k)!)_p}.
    $$
    
    The power $\nu_p(n!)$ and the factorial remainder $(n!)_p\bmod p$ both have recurrence formulas:
    
    $$
    \begin{aligned}
    \nu_p(n!) &= \lfloor n/p\rfloor+\nu_p( \lfloor n/p\rfloor!),\\
    (n!)_p &\equiv (-1)^{\lfloor n/p\rfloor}\cdot (n\bmod p)!\cdot (\lfloor n/p\rfloor!)_p\pmod p.
    \end{aligned}
    $$
    
    The former is a corollary of Legendre's formula, and the latter is a corollary of Wilson's theorem.
    
    Substituting the recurrence formulas into the expression for the binomial coefficient and rearranging, we obtain:
    
    $$
    \begin{aligned}
    \binom{n}{k} &\equiv (-p)^{\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor}\cdot\dfrac{(n\bmod p)!}{(k\bmod p)!((n-k)\bmod p)!} \\
    &\quad \cdot p^{\nu_p(\lfloor n/p\rfloor!)-\nu_p(\lfloor k/p\rfloor!)-\nu_p(\lfloor(n-k)/p\rfloor!)}\dfrac{(\lfloor n/p\rfloor!)_p}{(\lfloor k/p\rfloor!)_p(\lfloor(n-k)/p\rfloor!)_p} \pmod p.
    \end{aligned}
    $$
    
    Now examine the value of $\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor$. Because we have
    
    $$
    \begin{aligned}
    n &= \lfloor n/p\rfloor p + (n\bmod p),\\
    k &= \lfloor k/p\rfloor p + (k\bmod p),\\
    n-k &= \lfloor (n-k)/p\rfloor p + ((n-k)\bmod p),\\
    \end{aligned}
    $$
    
    so, subtracting the latter two equations from the first, we obtain
    
    $$
    (\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor)p = (k\bmod p)+((n-k)\bmod p)-(n\bmod p).
    $$
    
    On the right side of the equation, the sum of the first two terms is strictly less than $2p$, and the third term $n\bmod p$ is exactly the remainder of the sum of the first two terms, so the right side must be non-negative but less than $2p$, and also needs to be a multiple of $p$, so it can only be $0$ or $p$. This shows that $\lfloor n/p\rfloor-\lfloor k/p\rfloor-\lfloor(n-k)/p\rfloor$ can only be $0$ or $1$:
    
    -   If it is $0$, then in this case $(n\bmod p) = (k\bmod p)+((n-k)\bmod p)$ also holds. Therefore, the exponent of the first factor in the above expression is $0$, and this factor equals one; the second factor is $\dbinom{n\bmod p}{k\bmod p}$; and the third factor, by the expansion earlier, equals $\dbinom{\lfloor n/p\rfloor}{\lfloor k/p\rfloor}$. In this case, Lucas' formula holds;
    -   If it is $1$, then the exponent of the first factor is $1$, and this factor equals zero, so the remainder of the binomial coefficient is zero. At the same time, the $\dbinom{n\bmod p}{k\bmod p}$ on the right side of the equation that Lucas' theorem seeks to prove must also be zero, because in this case we must have $(n\bmod p)<(k\bmod p)$; otherwise, we would have
    
        $$
        ((n-k)\bmod p) = p + (n\bmod p)  - (k\bmod p) \ge p.
        $$
    
        This obviously contradicts the definition of the remainder.
    
    Combining the two cases, we obtain the Lucas' theorem to be proved. This proof shows that when solving binomial coefficients under a prime modulus, the result obtained using Lucas' theorem is equivalent to that obtained using the exLucas algorithm.

Lucas' theorem indicates that when the modulus is a prime $p$, the computation of a large binomial coefficient can be transformed into the computation of a smaller-scale binomial coefficient. In the right-hand expression, the first binomial coefficient can continue to recurse until $n,k<p$; the second binomial coefficient can be computed directly, or preprocessed in advance. Written in code form:

???+ example "Illustration"
    ```cpp
    long long Lucas(long long n, long long k, long long p) {
      if (k == 0) return 1;
      return (C(n % p, k % p, p) * Lucas(n / p, k / p, p)) % p;
    }
    ```

Here, `C(n, k, p)` is used to compute the small-scale binomial coefficient.

The recursion is performed at most $O(\log_p n)$ times, so the complexity of the algorithm is $O(f(p)+g(p)\log_p n)$, where $f(p)$ is the complexity of preprocessing the binomial coefficients and $g(p)$ is the complexity of computing a single binomial coefficient.

### Reference implementation

The reference implementation given here, after preprocessing the factorials up to $p$ and their inverses in $O(p)$ time, can compute a single binomial coefficient in $O(1)$ time:

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/lucas/lucas.cpp"
    ```

The time complexity of this implementation is $O(p+T\log_p n)$, where $T$ is the number of queries.

## exLucas algorithm

Lucas' theorem requires the modulus $p$ to be prime; for the case where $p$ is not prime, one needs to use the exLucas algorithm. Despite the name, this algorithm does not actually use Lucas' theorem in its actual operation. Its key step is [computing the factorial under a prime power modulus](./factorial.md). The second proof above pointed out its connection with Lucas' theorem.

### The case of a prime power modulus

First consider the case where the modulus is a prime power $p^\alpha$. Separating the power of $p$ in the factorial $n!$ from the other powers, we obtain the decomposition:

$$
n! = p^{\nu_p(n!)}(n!)_p.
$$

Here, $\nu_p(n!)$ is the power of $p$ in the prime factorization of $n!$, and $(n!)_p$ is obviously coprime with $p$. Therefore, the binomial coefficient can be written as:

$$
\binom{n}{k} = p^{\nu_p(n!)-\nu_p(k!)-\nu_p((n-k)!)}\dfrac{(n!)_p}{(k!)_p((n-k)!)_p}.
$$

The $\nu_p(n!)$ etc. in the expression can be computed via [Legendre's formula](./factorial.md#legendres-formula), and the $(n!)_p$ etc. can be computed via the [recurrence relation](./factorial.md#the-case-of-a-prime-power-modulus). Because the latter is coprime with $p^\alpha$, the inverse of the product in the denominator can be computed via the [extended Euclidean algorithm](./inverse.md#extended-euclidean-algorithm). The problem is thus solved.

Note that if the power $\nu_p(n!)-\nu_p(k!)-\nu_p((n-k)!)\ge\alpha$, the remainder must be zero, and no more computation is needed.

### The case of a general modulus

For the case where $m$ is a general composite number, we only need to first do its [prime factorization](./pollard-rho.md):

$$
m = p_1^{\alpha_1}p_2^{\alpha_2}\cdots p_s^{\alpha_s}.
$$

Then, computing the remainder of the binomial coefficient $\dbinom{n}{k}$ modulo $p_i^{\alpha_i}$ respectively, we obtain $s$ congruence equations:

$$
\begin{cases}
\dbinom{n}{k} \equiv r_1, &\pmod{p_1^{\alpha_1}}, \\
\dbinom{n}{k} \equiv r_2, &\pmod{p_2^{\alpha_2}}, \\
\quad\quad\cdots\\
\dbinom{n}{k} \equiv r_s, &\pmod{p_s^{\alpha_s}}.
\end{cases}
$$

Finally, use the [Chinese Remainder Theorem](./crt.md) to find the remainder modulo $m$.

### Reference implementation

Finally, we give a reference implementation for the template problem [二项式系数](https://loj.ac/p/181).

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/lucas/exlucas.cpp"
    ```

During preprocessing, this algorithm decomposes the modulus $m$ into prime powers, then for all $p^\alpha$ preprocesses the product of all natural numbers from $1$ to $p^\alpha$ that are not multiples of $p$, as well as its corresponding coefficient when merging the answers using the Chinese Remainder Theorem. The time complexity of preprocessing is $O(\sqrt{m}+\sum_ip_i^{\alpha_i})$. For each query, the complexity is $O(\log m+\sum_i\log_{p_i}n)$, and the two terms in the complexity are the complexity of computing the inverse and the complexity of computing the powers and factorial remainders, respectively.

## Exercises

-   [Luogu3807【模板】卢卡斯定理](https://www.luogu.com.cn/problem/P3807)
-   [SDOI2010 古代猪文  卢卡斯定理](https://loj.ac/problem/10229)
-   [Luogu4720【模板】扩展卢卡斯](https://www.luogu.com.cn/problem/P4720)
-   [Ceizenpok’s formula](http://codeforces.com/gym/100633/problem/J)
