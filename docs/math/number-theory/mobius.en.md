author: hydingsy, hyp1231, ranwen, 383494

Prerequisite knowledge: [number-theoretic block decomposition](./sqrt-decomposition.md), [Dirichlet convolution](./dirichlet.md#dirichlet-convolution)

Möbius inversion is an important topic in number theory. For some functions $f(n)$, if it is hard to directly find their value but easy to find the sum over their multiples or the sum over their divisors $g(n)$, then Möbius inversion can be used to simplify the computation and find the value of $f(n)$.

## Möbius function

The Möbius function is defined as

$$
\mu(n)=
\begin{cases}
1,&n=1,\\
0,&n\text{ is divisible by a square }>1,\\
(-1)^k,&n\text{ is the product of }k\text{ distinct primes}.\\
\end{cases}
$$

Specifically, suppose the positive integer $n$ has the prime factorization $n=\prod_{i=1}^kp_i^{e_i}$, where $p_i$ are primes and $e_i$ are positive integers. Then, the three cases correspond respectively to:

1.  $\mu(1) = 1$;
2.  when there exists $i$ such that $e_i > 1$, i.e. when any prime factor appears more than once, $\mu(n)=0$;
3.  otherwise, for all $i$ we have $e_i = 1$, i.e. when every prime factor appears only once, $\mu(n)=(-1)^k$, where $k$ is the number of distinct prime factors.

### Properties

It is easy to verify from the definition that the Möbius function $\mu(n)$ is a multiplicative function, but not a completely multiplicative function. In addition, the most important property is the following identity:

???+ note "Property"
    For a positive integer $n$, we have
    
    $$
    \sum_{d\mid n}\mu(d) = [n = 1] =
    \begin{cases}
    1,&n=1,\\
    0,&n\neq 1.\\
    \end{cases}
    $$
    
    where $[\cdot]$ is the Iverson bracket.

??? note "Proof"
    Let $n=\prod_{i=1}^kp_i^{e_i}$, and set $n' = \prod_{i=1}^kp_i$. By the [binomial theorem](../combinatorics/combination.md#binomial-theorem), we have
    
    $$
    \sum_{d\mid n}\mu(d) = \sum_{d\mid n'}\mu(d) = \sum_{i=0}^k\binom{k}{i}(-1)^i = (1 + (-1))^k = [k = 0] = [n = 1].
    $$

Using Dirichlet convolution, this expression can be written as $\varepsilon = 1 * \mu$. That is to say, the Möbius function is the Dirichlet inverse of the constant function $1$.

This property has a very common application:

$$
[i\perp j] = [\gcd(i,j) = 1] = \sum_{d\mid\gcd(i,j)} \mu(d) = \sum_{d}[d\mid i][d\mid j]\mu(d).
$$

It transforms the coprimality condition into a sum involving the Möbius function, facilitating further derivation.

### Computation

If one needs to compute the value of the Möbius function $\mu(n)$ for a single $n$, one can use its [prime factorization](./pollard-rho.md). For example, when $n$ is not too large, the value of $\mu(n)$ can be found in $O(\sqrt{n})$ time.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/mobius/mobius-func-1.py:core"
        ```

If one needs to preprocess the values of $\mu(n)$ for the first $n$ positive integers, one can use the fact that it is a multiplicative function, and compute it in $O(n)$ time via the [linear sieve](./sieve.md#筛法求莫比乌斯函数).

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/mobius/mobius-func-2.py:core"
        ```

## Möbius inversion

The most important application of the Möbius function is Möbius inversion.

???+ note "Möbius inversion"
    Let $f(n),g(n)$ be two arithmetic functions. Then, we have
    
    $$
    f(n) = \sum_{d\mid n}g(d) \iff g(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)f(d).
    $$

??? note "Proof one"
    Direct verification:
    
    $$
    \begin{aligned}
    \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)f(d)
    &= \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\sum_{k\mid d}g(k)\\
    &= \sum_{k\mid n}g(k)\sum_d[k\mid d\mid n]\mu\left(\dfrac{n}{d}\right)\\
    &= \sum_{k\mid n}g(k)\sum_{d\mid n}\left[\frac{n}{d}\mid\frac{n}{k}\right]\mu\left(\dfrac{n}{d}\right)\\
    &= \sum_{k\mid n}g(k)\left[\frac{n}{k} = 1\right] \\
    &= g(n).
    \end{aligned}
    $$
    
    The key to transforming the expression is to exchange the summation order and note that $k\mid d\mid n$ is equivalent to $\dfrac{n}{d}\mid\dfrac{n}{k}$. The second-to-last equality amounts to summing the Möbius function over the divisors $\dfrac{n}{d}$ of $\dfrac{n}{k}$, so it equals $\left[\dfrac{n}{k} = 1\right]$. This expression is nonzero only at $n=k$, and in the end we obtain $g(n)$.

??? note "Proof two"
    Using Dirichlet convolution, the proposition is equivalent to
    
    $$
    f = 1 * g \iff g = \mu * f.
    $$
    
    Using $1 * \mu = \varepsilon$, convolving both sides of the left equation with $\mu$, we obtain
    
    $$
    f * \mu = (1 * g) * \mu = (1 * \mu) * g = \varepsilon * g = g.
    $$

In the summation of arithmetic functions involving various divisibility relations, Möbius inversion is a powerful transformation tool.

???+ example "Examples"
    1.  [Euler's totient function](./euler-totient.md) $\varphi(n)$ satisfies the relation $n = \sum_{d\mid n}\varphi(d)$, i.e. $\mathrm{id}=1*\varphi$. Inverting it, we obtain $\varphi = \mu * \mathrm{id}$, i.e.
    
        $$
        \varphi(n) = \sum_{d\mid n}d\mu\left(\dfrac{n}{d}\right).
        $$
    2.  The divisor function $\sigma_k(n) = \sum_{d\mid n}d^k$, i.e. $\sigma_k = 1 * \mathrm{id}_k$. Inverting it, we obtain $\mathrm{id}_k = \mu * \sigma_k$, i.e.
    
        $$
        n^k = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\sigma_k(d).
        $$
    3.  The function counting distinct prime factors $\omega(n)=\sum_{d\mid n}[d\in\mathbf P]$, i.e. $\omega = 1* \mathbf{1}_{\mathbf P}$, where $\mathbf{1}_{\mathbf P}$ is the indicator function of the set of primes $\mathbf P$. Inverting it, we obtain $\mathbf{1}_{\mathbf P} = \mu * \omega$, i.e.
    
        $$
        [n\in\mathbf P] = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\omega(d).
        $$
    4.  Consider the arithmetic function $\Lambda(n)$ satisfying $\log n = \sum_{d\mid n}\Lambda(d)$. It is exactly the Möbius inversion of the logarithm function, also called the von Mangoldt function:
    
        $$
        \Lambda(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)\log d = 
        \begin{cases}
        \log p, & n = p^e,~p\in\mathbf P,~e\in\mathbf N_+, \\
        0, &\text{otherwise}.
        \end{cases}
        $$

??? note "Appendix: proof of the expression for $\Lambda(n)$"
    For a prime power $n=p^e~(e\in\mathbf N_+)$, we have
    
    $$
    \Lambda(n) = \sum_{i=0}^e\mu(p^{e-i})\log p^i = \log p^{e} - \log p^{e-1} = \log p.
    $$
    
    For $n=1$, obviously $\Lambda(n)=\log 1=0$. For other composite numbers $n$, we have
    
    $$
    \Lambda(n) = \sum_{d\mid n}\mu(d)(\log n-\log d) = \left(\sum_{d\mid n}\mu(d)\right)\log n-\sum_{d\mid n}\mu(d)\log d.
    $$
    
    By the property of the Möbius function, the coefficient of the $\log n$ term is $[n=1]=0$. For the latter term, we can further decompose $d$ into a product of prime factors. For any prime $p\mid n$, examining the coefficient of $\log p$, we have:
    
    $$
    -\sum_{p\mid d\mid n}\mu(d) = \sum_{(d/p)\mid(n/p)}\mu\left(\dfrac{d}{p}\right) = \left[\dfrac{n}{p}=1\right]=0.
    $$
    
    Hence, for a composite number $n$ with more than one prime factor, we have $\Lambda(n)=0$.

### Extended forms

Besides the above basic form, Möbius inversion also has some common extended forms. First, we can consider its sum-over-multiples form.

???+ note "Extension one"
    Let $f(n),g(n)$ be two arithmetic functions. Then, we have
    
    $$
    f(n) = \sum_{n\mid d}g(d) \iff g(n) = \sum_{n\mid d}\mu\left(\dfrac{d}{n}\right)f(d).
    $$

??? note "Proof"
    Direct verification:
    
    $$
    \begin{aligned}
    \sum_{n\mid d}\mu\left(\dfrac{d}{n}\right)f(d)
    &= \sum_{n\mid d}\mu\left(\dfrac{d}{n}\right)\sum_{d\mid k}g(k)\\
    &= \sum_{n\mid k}g(k)\sum_{d}[n\mid d\mid k]\mu\left(\dfrac{d}{n}\right)\\
    &= \sum_{n\mid k}g(k)\sum_{n\mid d}\left[\dfrac{d}{n}\mid\dfrac{k}{n}\right]\mu\left(\dfrac{d}{n}\right)\\
    &= \sum_{n\mid k}g(k)\left[\dfrac{k}{n}=1\right]\\
    &= g(n).
    \end{aligned}
    $$
    
    This is entirely dual to the derivation of the basic form.

Second, Möbius inversion is not limited to addition; it actually holds for the operation in any [Abelian group](../algebra/basic.md#groups). For example, it has the following multiplicative form:

???+ note "Extension two"
    Let $f(n),g(n)$ be two arithmetic functions. Then, we have
    
    $$
    f(n) = \prod_{d\mid n}g(d) \iff g(n) = \prod_{d\mid n}f(d)^{\mu(n/d)}.
    $$

??? note "Proof"
    Direct verification:
    
    $$
    \begin{aligned}
    \prod_{d\mid n}f(d)^{\mu(n/d)}
    &= \prod_{d\mid n}\left(\prod_{k\mid d}g(k)\right)^{\mu(n/d)}\\
    &= \prod_{k\mid n}g(k)\uparrow\left(\sum_d[k\mid d\mid n]\mu\left(\dfrac{n}{d}\right)\right)\\
    &= \prod_{k\mid n}g(k)\uparrow\left(\sum_{d\mid n}\left[\frac{n}{d}\mid\frac{n}{k}\right]\mu\left(\dfrac{n}{d}\right)\right)\\
    &= \prod_{k\mid n}g(k)\uparrow\left[\frac{n}{k} = 1\right] \\
    &= g(n).
    \end{aligned}
    $$
    
    Here, $a\uparrow b = a^b$ is the Knuth arrow. Comparing with the proof of the basic form, the only difference is that addition is replaced by multiplication, and multiplication is replaced by exponentiation.

From the perspective of Dirichlet convolution, Möbius inversion only uses the fact that "the Möbius function is the Dirichlet inverse of the constant function". It is easy to imagine that relations analogous to Möbius inversion also hold for a general [Dirichlet inverse](./dirichlet.md#dirichlet-convolution).

???+ note "Extension three"
    Let $f(n),g(n),\alpha(n)$ all be arithmetic functions, and let $\alpha^{-1}(n)$ be the Dirichlet inverse of $\alpha(n)$, i.e.
    
    $$
    [n=1] = \sum_{d\mid n}\alpha\left(\dfrac{n}{d}\right)\alpha^{-1}(d).
    $$
    
    Then, we have
    
    $$
    f(n) = \sum_{d\mid n}\alpha\left(\dfrac{n}{d}\right)g(d) \iff g(n) = \sum_{d\mid n}\alpha^{-1}\left(\dfrac{n}{d}\right)f(d).
    $$

??? note "Proof"
    Direct verification:
    
    $$
    \begin{aligned}
    \sum_{d\mid n}\alpha^{-1}\left(\dfrac{n}{d}\right)f(d)
    &= \sum_{d\mid n}\alpha^{-1}\left(\dfrac{n}{d}\right)\sum_{k\mid d}\alpha\left(\dfrac{d}{k}\right)g(k)\\
    &= \sum_{k\mid n}g(k)\sum_d[k\mid d\mid n]\alpha\left(\dfrac{d}{k}\right)\alpha^{-1}\left(\dfrac{n}{d}\right)\\
    &= \sum_{k\mid n}g(k)\sum_{d\mid n}\left[\frac{n}{d}\mid\frac{n}{k}\right]\alpha\left(\dfrac{d}{k}\right)\alpha^{-1}\left(\dfrac{n/k}{d/k}\right)\\
    &= \sum_{k\mid n}g(k)\left[\frac{n}{k} = 1\right] \\
    &= g(n).
    \end{aligned}
    $$
    
    Compared with the proof of the basic form, we only need to replace the second-to-last equality with the definition of the Dirichlet inverse.

???+ note "Corollary"
    Let $f(n),g(n)$ be arithmetic functions, and let $t(n)$ be a completely multiplicative function. Then, we have
    
    $$
    f(n) = \sum_{d\mid n}t\left(\dfrac{n}{d}\right)g(d) \iff g(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)t\left(\dfrac{n}{d}\right)f(d).
    $$

??? note "Proof"
    By the [properties](./dirichlet.md#properties) of Dirichlet convolution, for a completely multiplicative function $t(n)$, its Dirichlet inverse is $\mu(n)t(n)$.

Finally, Möbius inversion can also be generalized to complex-valued functions on $[1,+\infty)$, not just arithmetic functions. The basic form of Möbius inversion can be viewed as the special case where the complex-valued function takes the value zero at all non-integer points.

???+ note "Extension four"
    Let $F(x)$ and $G(x)$ both be complex-valued functions on $[1,+\infty)$. Then, we have
    
    $$
    F(x) = \sum_{n = 1}^{\lfloor x\rfloor}G\left(\dfrac{x}{n}\right) \iff G(x) = \sum_{n = 1}^{\lfloor x\rfloor}\mu(n)F\left(\dfrac{x}{n}\right).
    $$

??? note "Proof"
    Suppose we supplement the definitions of $F$ and $G$ so that when $x < 1$, always $F(x)=G(x)=0$. Then, the proposition is equivalent to:
    
    $$
    F(x) = \sum_n G\left(\dfrac{x}{n}\right) \iff G(x) = \sum_n \mu(n)F\left(\dfrac{x}{n}\right).
    $$
    
    These sums are all over $n\in\mathbf N_+$.
    
    Direct verification:
    
    $$
    \begin{aligned}
    \sum_n \mu(n)F\left(\dfrac{x}{n}\right)
    &= \sum_n\mu(n)\sum_d G\left(\dfrac{x/n}{d}\right)\\
    &= \sum_k G\left(\dfrac{x}{k}\right)\sum_{n\mid k}\mu(n)\\
    &= \sum_k G\left(\dfrac{x}{k}\right)[k=1]\\
    &= G(x).
    \end{aligned}
    $$
    
    Here, to obtain the second equality, we need to let $k = nd$.

???+ note "Corollary"
    Let $f(n),g(n)$ be arithmetic functions. Then, we have
    
    $$
    f(n) = \sum_{k=1}^ng\left(\left\lfloor\dfrac{n}{k}\right\rfloor\right) \iff g(n)=\sum_{k=1}^n\mu(k)f\left(\left\lfloor\dfrac{n}{k}\right\rfloor\right).
    $$

??? note "Proof"
    We only need to take $F(x)=f(\lfloor x\rfloor)$ and $G(x)=g(\lfloor x\rfloor)$.

These extended forms can be combined with each other, yielding more complex inversion relations.

### Dirichlet prefix sum

Prerequisite knowledge: [prefix sum and difference](../../basic/prefix-sum.md)

Consider the basic form of the Möbius inversion relation:

$$
f(n) = \sum_{d\mid n}g(d) \iff g(n) = \sum_{d\mid n}\mu\left(\dfrac{n}{d}\right)f(d).
$$

In the left equation, the value of $f(n)$ is the sum of the values of $g(n)$ over all divisors of $n$. If we understand $a\mid b$ as $a$ being ranked before $b$, then $f(n)$ can be understood as a prefix sum of $g(n)$ in some sense. Therefore, in the domestic competitive programming community, the process of finding $\{f(k)\}_{k=1}^n$ from $\{g(k)\}_{k=1}^n$ is also called the **Dirichlet prefix sum**, and the corresponding inverse process is called the Dirichlet difference. These methods mostly appear in situations that require preprocessing the values of some arithmetic function at the first $N$ points.

Next, discuss the computation of the Dirichlet prefix sum. If we regard each prime as a dimension, this is a kind of higher-dimensional prefix sum. Recall the [dimension-by-dimension prefix sum algorithm](../../basic/prefix-sum.md#dimension-by-dimension-prefix-sums) of the higher-dimensional prefix sum: traverse all dimensions one by one, and accumulate the value of each position into the successor position of that position in that dimension. For arithmetic functions, this amounts to saying: traverse all primes $p$ from small to large, and accumulate the function value at $n$ into $np$. This is consistent with the traversal order of the [Sieve of Eratosthenes](./sieve.md#埃拉托斯特尼筛法). Therefore, this algorithm can compute the Dirichlet prefix sum of a sequence of length $n$ in $O(n\log\log n)$ time. Similarly, using dimension-by-dimension difference, one can find the Dirichlet difference of a sequence in the same time complexity.

???+ example "Reference implementation"
    === "Dirichlet prefix sum"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-3.cpp:presum"
        ```
    
    === "Dirichlet difference"
        ```cpp
        --8<-- "docs/math/code/mobius/mobius-func-3.cpp:diff"
        ```

This computation method can be generalized to extended forms such as the sum over multiples (extension one), the multiplicative form (extension two), and using a completely multiplicative function instead of the constant function (the corollary of extension three).

## Example problems

This section demonstrates the application methods of Möbius inversion and some common transformation techniques through example problems. First, through an example problem, we get familiar with the basic technique of handling the greatest-common-divisor condition in a sum.

???+ example "[Luogu P2522 \[HAOI 2011\] Problem b](https://www.luogu.com.cn/problem/P2522)"
    $T$ groups of data. For each group of data, find the value:
    
    $$
    \sum_{i=x}^{n}\sum_{j=y}^{m}[\gcd(i,j)=k].
    $$
    
    Data range: $1\le T,x,y,n,m,k\le 5\times 10^4$.

??? note "Solution"
    By the inclusion–exclusion principle, the original expression can be divided into $4$ blocks to handle, and the expression for each block has the form
    
    $$
    f(n,m,k)=\sum_{i=1}^{n}\sum_{j=1}^{m}[\gcd(i,j)=k].
    $$
    
    For this kind of expression, the following is a standard derivation flow: extract the common factor, apply the property of the Möbius function, exchange the summation order.
    
    First, since $i,j$ can only take multiples of $k$, we can first extract this factor—this amounts to substituting $i=ki'$ and $j=kj'$, obtaining:
    
    $$
    f(n,m,k)=\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor m/k\rfloor}[\gcd(i,j)=1].
    $$
    
    Then using the property of the Möbius function:
    
    $$
    [\gcd(i,j)=1] = \sum_{d\mid\gcd(i,j)}\mu(d) = \sum_d[d\mid i][d\mid j]\mu(d).
    $$
    
    Substituting it into the expression and exchanging the summation order, we obtain:
    
    $$
    f(n,m,k)=\sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/k\rfloor}[d\mid i]\right)\left(\sum_{j=1}^{\lfloor m/k\rfloor}[d\mid j]\right).
    $$
    
    The benefit of such an operation is that, with $d$ fixed, the terms in the sum concerning $i$ and $j$ are separated from each other and can be summed separately. Next, because
    
    $$
    \sum_{i=1}^{\lfloor n/k\rfloor}[d\mid i] = \left\lfloor\dfrac{\lfloor n/k\rfloor}{d}\right\rfloor,~\sum_{j=1}^{\lfloor m/k\rfloor}[d\mid j]=\left\lfloor\dfrac{\lfloor m/k\rfloor}{d}\right\rfloor,
    $$
    
    we have
    
    $$
    f(n,m,k)=\sum_d\mu(d)\left\lfloor\dfrac{\lfloor n/k\rfloor}{d}\right\rfloor\left\lfloor\dfrac{\lfloor m/k\rfloor}{d}\right\rfloor.
    $$
    
    After preprocessing $\mu(d)$ with a linear sieve and preprocessing its prefix sum, we can solve via number-theoretic block decomposition. The total time complexity is $O(N + T\sqrt{N})$, where $N$ is the upper bound of $n,m$ and $T$ is the number of data groups.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_1.cpp"
    ```

The following two example problems demonstrate the method of handling by enumerating the common factor, and use the [sieve](./sieve.md#一般的积性函数) to compute the value of a general multiplicative function.

???+ example "[SPOJ LCMSUM](https://www.spoj.com/problems/LCMSUM/)"
    $T$ groups of data. For each group of data, find the value:
    
    $$
    \sum_{i=1}^n \operatorname{lcm}(i,n).
    $$
    
    Data range: $1\le T\le 3\times 10^5,~1\le n\le 10^6$.

??? note "Solution one"
    The problem provides the least common multiple, but often the greatest common divisor is easier to handle. So, first do the transformation:
    
    $$
    f(n)=\sum_{i=1}^n \operatorname{lcm}(i,n) = \sum_{i=1}^n \frac{i\cdot n}{\gcd(i,n)}.
    $$
    
    Extract $n$ and enumerate the greatest common divisor $k$:
    
    $$
    f(n)=n\sum_{k\mid n}\sum_{i=1}^n\dfrac{i}{k}[\gcd(i,n)=k].
    $$
    
    For the inner sum, this is the most common case involving the greatest common divisor; repeating the standard handling flow, we have:
    
    $$
    \begin{aligned}
    f(n) &= n\sum_{k\mid n}\sum_{i=1}^{n/k}i\left[\gcd\left(i,\dfrac{n}{k}\right)=1\right]\\
    &= n\sum_{k\mid n}\sum_{i=1}^{n/k}i\sum_d\mu(d)[d\mid i]\left[d\mid \dfrac{n}{k}\right]\\
    &= n\sum_{k\mid n}\sum_d\mu(d)\left[d\mid \dfrac{n}{k}\right]\left(\sum_{i=1}^{n/k}i[d\mid i]\right).
    \end{aligned}
    $$
    
    Once again, the sum concerning $i$ is separated from the other parts and can be handled separately. The last sum is actually the sum of an arithmetic sequence: (take $i=di'$)
    
    $$
    \sum_{i=1}^{n/k}i[d\mid i] = d\frac{1}{2}\left(\dfrac{n}{kd}+1\right)\dfrac{n}{kd}=:dG\left(\dfrac{n}{kd}\right).
    $$
    
    From this, we obtain the following expression:
    
    $$
    f(n) = n\sum_{k\mid n}\sum_d\mu(d)\left[d\mid \dfrac{n}{k}\right]dG\left(\dfrac{n}{kd}\right).
    $$
    
    After enumerating the common factor, a double sum of this form is very common. For it, there is likewise a fixed handling method: set the product as a new variable $\ell=kd$, and then exchange the summation order again. Because $d\mid(n/k)$ is equivalent to $d\mid\ell\mid n$, the original expression transforms into:
    
    $$
    f(n) = n\sum_{\ell\mid n}G\left(\dfrac{n}{\ell}\right)\sum_{d\mid\ell}\mu(d)d.
    $$
    
    Let $F(\ell)=\sum_{d\mid\ell}\mu(d)d$; then the original expression has the form:
    
    $$
    f(n) = n\sum_{\ell\mid n}G\left(\dfrac{n}{\ell}\right)F(\ell).
    $$
    
    Because $\mu(d)d$ is a multiplicative function, its convolution $F(n)$ with the constant function $1$ is also a multiplicative function. Although in the above expression the sum takes the form of a Dirichlet convolution, $G(n)$ is not a multiplicative function, so the whole of this sum is not a multiplicative function. However, $G(n)$ is a polynomial, so it is actually a linear combination of several completely multiplicative functions. So, we have
    
    $$
    f(n) = \dfrac{1}{2}n\left(\sum_{\ell}\left(\dfrac{n}{\ell}\right)^2F(\ell) + \sum_{\ell}\dfrac{n}{\ell}F(\ell)\right).
    $$
    
    Both of these terms (excluding the coefficient) are multiplicative functions and can be directly preprocessed via a linear sieve (or one can also linearly sieve the inner function and then use the Dirichlet prefix sum to preprocess in $O(N\log\log N)$ time). Specifically, let
    
    $$
    H_s(n) = \sum_{\ell}\left(\dfrac{n}{\ell}\right)^sF(\ell),~s=1,2.
    $$
    
    To derive their expressions, we only need to determine their values at prime powers. To this end, for a prime $p$ and a positive exponent $e$, we have
    
    $$
    \begin{aligned}
    F(p^e) &= \mu(1) + \mu(p)p + \sum_{j=2}^e\mu(p^j)p^j = 1-p,\\
    H_s(p^e) &= (p^e)^{s}F(1) + \sum_{j=1}^e(p^{e-j})^sF(p^j) = p^{es} + (1-p)\dfrac{1-p^{es}}{1-p^s},~s=1,2.
    \end{aligned}
    $$
    
    In particular, $H_1(p^e)\equiv 1$ is the constant function, and
    
    $$
    H_2(p^e) = p^{2e} + (1-p)\dfrac{1-p^{2e}}{1-p^2} = H_2(p^{e-1}) + p^{2e} - p^{2e-1}.
    $$
    
    This is easy to solve via a linear sieve. After preprocessing $H_2(n)$ with a linear sieve, a single query can be solved in $O(1)$ time via the expression $f(n)=(n/2)(H_2(n)+1)$. The total time complexity is $O(N+T)$, where $N$ is the upper bound of $n$ and $T$ is the number of data groups.
    
    In the reference implementation, using the specialness of this problem's expression, the linear sieve part is further derived, which is not necessary. Using only the values at prime powers, the preprocessing can still be completed in $O(N)$ time. These derivations are detailed in solution two.

??? note "Solution two"
    For this problem, there is a more flexible handling method. From solution one, we can see that
    
    $$
    f(n) = n\sum_{k\mid n}\sum_{i=1}^{n/k}i\left[\gcd\left(i,\dfrac{n}{k}\right)=1\right] = n\sum_{k\mid n}F\left(\dfrac{n}{k}\right).
    $$
    
    If at this step we do not continue to do Möbius inversion, but instead observe that the subsequent sum is actually the sum of integers not exceeding $d=n/k$ and coprime with it. For $d>1$, because the integers coprime with $d$ appear in pairs, i.e. $i$ and $d-i$ must be simultaneously coprime with $d$, we have
    
    $$
    F(d)=\sum_{i=1}^{n'}i[i\perp d] = \sum_{i=1}^{d}(d-i)[i\perp d] = \dfrac{1}{2}d\sum_{i=1}^{d}[i\perp d] = \dfrac{1}{2}d\varphi(d).
    $$
    
    For $d=1$, we have
    
    $$
    F(d)=1=\dfrac{1}{2}+\dfrac{1}{2}d\varphi(d).
    $$
    
    Then, the original expression can be represented as
    
    $$
    f(n) = \dfrac{1}{2}n\left(\sum_{d\mid n}d\varphi(d) + 1\right).
    $$
    
    Since $G(n)=\sum_{d\mid n}d\varphi(d)$ is the Dirichlet convolution of the multiplicative function $n\varphi(n)$ with the constant function $1$, it is also a multiplicative function and can be preprocessed via a linear sieve. To this end, we only need to determine its values at prime powers. For a prime $p$ and a positive exponent $e$, we have
    
    $$
    G(p^e) = 1 + \sum_{i=1}^ep^e(p^e-1) = G(p^{e-1}) + p^{2e} - p^{2e-1}.
    $$
    
    It can be seen that this expression is consistent with the result derived in solution one. The total time complexity of this method is still $O(N+T)$.
    
    Finally, using this problem's expression of the multiplicative function, we can further optimize the computation process of the linear sieve. For a prime $p$, we have
    
    $$
    G(p) = 1 - p + p^2.
    $$
    
    The key to the linear sieve is that for a general $n$, we need to find the value of $G(pn)$. This is further divided into two cases. When $p\perp n$, because $G$ is a multiplicative function, we have
    
    $$
    G(pn) = G(p)G(n).
    $$
    
    Otherwise, when $p\mid n$, set $n=p^em$ and $p\perp m$; then we have
    
    $$
    \begin{aligned}
    G(pn) &= G(p^{e+1})G(m)\\
    &= G(p^e)G(m) + (p^{2e+2} - p^{2e+1})G(m)\\
    &= G(n) + (p^{2e+2} - p^{2e+1})G(m).
    \end{aligned}
    $$
    
    Direct verification shows that this expression also holds for the case $p\perp n$. Therefore, we have
    
    $$
    G(n) - G\left(\dfrac{n}{p}\right) = (p^{2e}-p^{2e-1})G(m).
    $$
    
    Substituting into the above expression, we obtain
    
    $$
    G(pn) = G(n) + p^2\left(G(n) - G\left(\dfrac{n}{p}\right)\right).
    $$
    
    This simplifies the computation of the linear sieve part. Of course, this derivation is not necessary; for a multiplicative function with no special properties, directly using $G(pn)=G(p^{e+1})G(m)$ can complete the linear sieve computation.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_2.cpp"
    ```

???+ example "[BZOJ 2154 \[国家集训队\] Crash 的数字表格](https://hydro.ac/p/bzoj-P2154)"
    Find the value:
    
    $$
    \sum_{i=1}^n\sum_{j=1}^m\operatorname{lcm}(i,j)\mod{20101009}.
    $$
    
    Data range: $1\le n,m\le 10^7$.

??? note "Solution"
    Ignore the modulus during the derivation. Let
    
    $$
    f(n,m) = \sum_{i=1}^n\sum_{j=1}^m\operatorname{lcm}(i,j).
    $$
    
    Again convert the least common multiple to the greatest common divisor, enumerate the common factor, and apply the standard handling flow, obtaining
    
    $$
    \begin{aligned}
    f(n,m)
    &= \sum_k\sum_{i=1}^n\sum_{j=1}^m\dfrac{ij}{k}[\gcd(i,j)=k] \\
    &= \sum_k\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor m/k\rfloor} kij[\gcd(i,j)=1]\\
    &= \sum_k\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor m/k\rfloor} kij\sum_d\mu(d)[d\mid i][d\mid j]\\
    &= \sum_kk\sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/k\rfloor}i[d\mid i]\right)\left(\sum_{j=1}^{\lfloor m/k\rfloor}j[d\mid j]\right).
    \end{aligned}
    $$
    
    Once again, the sum is separated for $i$ and $j$. First compute these inner sums; extracting the factor (i.e. taking $i=di'$), we have
    
    $$
    \sum_{i=1}^{\lfloor n/k\rfloor}i[d\mid i] = d\sum_{i=1}^{\lfloor\lfloor n/k\rfloor/d\rfloor}i = dG\left(\left\lfloor\dfrac{\lfloor n/k\rfloor}{d}\right\rfloor\right) = dG\left(\left\lfloor\dfrac{n}{kd}\right\rfloor\right).
    $$
    
    Here, $G(n)=\dfrac{1}{2}n(n+1)$ is exactly the sum of an arithmetic sequence, and the last equality uses the property of the [floor function](./basic.md#rounding-functions). Symmetrically, the other sum can be computed similarly. Substituting back into the earlier expression, we have
    
    $$
    f(n,m) = \sum_k k\sum_{d}\mu(d)d^2G\left(\left\lfloor\dfrac{n}{kd}\right\rfloor\right)G\left(\left\lfloor\dfrac{m}{kd}\right\rfloor\right).
    $$
    
    Consistent with the earlier case, for this kind of expression enumerating the common factor, we often need to enumerate the product $\ell = kd$ and exchange the summation order again:
    
    $$
    f(n,m) = \sum_{\ell}\left(\sum_{d\mid\ell}\mu(d)d\ell\right)G\left(\left\lfloor\dfrac{n}{\ell}\right\rfloor\right)G\left(\left\lfloor\dfrac{m}{\ell}\right\rfloor\right).
    $$
    
    Let
    
    $$
    F(\ell) = \sum_{d\mid\ell}\mu(d)d\ell.
    $$
    
    This is the product of the multiplicative function $\ell$ and the multiplicative function $\sum_{d\mid\ell}\mu(d)d$, so it is also a multiplicative function and can be directly preprocessed with a linear sieve, along with preprocessing its prefix sum. Then, we can compute the value of $f(n,m)$ with number-theoretic block decomposition. The total time complexity is $O(\min\{n,m\})$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_3.cpp"
    ```

The following example problem is rather special and requires transforming the divisor-count function of a product.

???+ example "[LOJ 2185. \[SDOI2015\] 约数个数和](https://loj.ac/problem/2185)"
    $T$ groups of data. For each group of data, find the value:
    
    $$
    \sum_{i=1}^n\sum_{j=1}^m\sigma_0(ij).
    $$
    
    where $\sigma_0(n)=\sum_{d \mid n}1$ denotes the number of divisors of $n$.
    
    Data range: $1\le n,m,T\le 5\times 10^4$.

??? note "Solution"
    The difficulty of this problem lies in transforming $\sigma_0(ij)$ into an expression involving the greatest common divisor. Since $\sigma_0$ is a multiplicative function, we can first consider the case of prime powers. For a prime $p$ and non-negative exponents $e_1,e_2$, set $i=p^{e_1},~j=p^{e_2}$; then we have
    
    $$
    \sigma_0(ij) = 1 + e_1 + e_2 = \sum_{x\mid i}\sum_{y\mid j}[x\perp y].
    $$
    
    For the general case, suppose $i=\prod_p i_p$ and $j=\prod_p j_p$, where $i_p,j_p$ are the powers of $p$ in the prime factorizations of $i,j$ respectively. Then, we have
    
    $$
    \sigma_0(ij) = \prod_p\sigma_0(i_pj_p)= \prod_p\sum_{x_p\mid i_p}\sum_{y_p\mid j_p}[x_p\perp y_p].
    $$
    
    Note that enumerating the divisor $x_p$ of each prime-power factor $i_p$ of $i$ amounts to enumerating the divisor $x$ of $i$ and then decomposing all prime-power factors $x_p$; the same for $j$. Therefore, using the distributive law of multiplication, this expression becomes
    
    $$
    \sigma_0(ij) = \sum_{x\mid i}\sum_{y\mid j}\prod_p[x_p\perp y_p] = \sum_{x\mid i}\sum_{y\mid j}[x\perp y].
    $$
    
    The last step uses the conclusion: $x\perp y$ if and only if for every prime factor $p$, $x_p\perp y_p$ holds.
    
    After obtaining this expression, we can apply the standard handling flow:
    
    $$
    \begin{aligned}
    \sigma_0(ij) 
    &= \sum_{x\mid i}\sum_{y\mid j}[x\perp y]\\
    &= \sum_{x\mid i}\sum_{y\mid j}\sum_d\mu(d)[d\mid x][d\mid y]\\
    &= \sum_d\mu(d)\left(\sum_{x}[d\mid x\mid i]\right)\left(\sum_{y}[d\mid y\mid j]\right)\\
    &= \sum_d\mu(d)[d\mid i][d\mid j]\sigma_0\left(\dfrac{i}{d}\right)\sigma_0\left(\dfrac{j}{d}\right).
    \end{aligned}
    $$
    
    The meaning of the last step of the derivation is: the function takes a nonzero value only when $d\mid i$ and $d\mid j$, and in this case, enumerating $x$ satisfying $d\mid x\mid i$ amounts to enumerating the divisor $\dfrac{x}{d}$ of $\dfrac{i}{d}$, and similarly for enumerating $y$ satisfying $d\mid y\mid j$.
    
    Substituting this expression back into the original expression and exchanging the summation order:
    
    $$
    \begin{aligned}
    f(n,m)
    &= \sum_{i=1}^n\sum_{j=1}^m\sigma_0(ij)\\
    &= \sum_{i=1}^n\sum_{j=1}^m\sum_d\mu(d)[d\mid i][d\mid j]\sigma_0\left(\dfrac{i}{d}\right)\sigma_0\left(\dfrac{j}{d}\right)\\
    &= \sum_d\mu(d)\left(\sum_{i=1}^n[d\mid i]\sigma_0\left(\dfrac{i}{d}\right)\right)\left(\sum_{j=1}^m[d\mid j]\sigma_0\left(\dfrac{j}{d}\right)\right)\\
    &= \sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/d\rfloor}\sigma_0(i)\right)\left(\sum_{j=1}^{\lfloor m/d\rfloor}\sigma_0(j)\right).
    \end{aligned}
    $$
    
    Let $G(n)=\sum_{i=1}^n\sigma_0(i)$; then we have
    
    $$
    f(n,m)=\sum_{d}\mu(d)G\left(\left\lfloor\dfrac{n}{d}\right\rfloor\right)G\left(\left\lfloor\dfrac{m}{d}\right\rfloor\right).
    $$
    
    This can be solved via number-theoretic block decomposition. We only need to preprocess the prefix sums of $\mu(n)$ and $\sigma_0(n)$. The total time complexity is $O(N+T\sqrt{N})$, where $N$ is the upper bound of $n,m$ and $T$ is the number of data groups.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_4.cpp"
    ```

The last example problem demonstrates how to apply the multiplicative version of Möbius inversion.

???+ example "[Luogu P5221 Product](https://www.luogu.com.cn/problem/P5221)"
    Find the value:
    
    $$
    \prod_{i=1}^n\prod_{j=1}^n\dfrac{\operatorname{lcm}(i,j)}{\gcd(i,j)}\pmod{104857601}.
    $$
    
    Data range: $1\le n\le 1\times 10^6$.

??? note "Solution one"
    Ignore the modulus during the derivation. Let
    
    $$
    f(n) = \prod_{i=1}^n\prod_{j=1}^n\dfrac{\operatorname{lcm}(i,j)}{\gcd(i,j)}.
    $$
    
    Again convert the least common multiple to the greatest common divisor:
    
    $$
    f(n) = \prod_{i=1}^n\prod_{j=1}^n\dfrac{ij}{(\gcd(i,j))^2}.
    $$
    
    Note that the products of these factors are mutually independent and can be computed separately. Let
    
    $$
    g(n) = \prod_{i=1}^n\prod_{j=1}^n\gcd(i,j).
    $$
    
    Then the original expression equals:
    
    $$
    f(n) = \dfrac{(n!)^{2n}}{g(n)^2}.
    $$
    
    The key is to solve the computation of $g(n)$. Its handling flow is similar to that described earlier, but we need to switch to the corresponding multiplicative version. First, enumerate and extract the common factor:
    
    $$
    \begin{aligned}
    g(n) &= \prod_k\prod_{i=1}^n\prod_{j=1}^nk\uparrow[\gcd(i,j)=k]\\
    &= \prod_k\prod_{i=1}^{\lfloor n/k\rfloor}\prod_{j=1}^{\lfloor n/k\rfloor}k\uparrow[\gcd(i,j)=1].
    \end{aligned}
    $$
    
    Here, $a\uparrow b=a^b$ is the Knuth arrow. Then, substitute $[\gcd(i,j)=1]=\sum_d\mu(d)[d\mid i][d\mid j]$ and convert the sum in the exponent into a product of powers, obtaining:
    
    $$
    g(n) = \prod_k\prod_d\prod_{i=1}^{\lfloor n/k\rfloor}\prod_{j=1}^{\lfloor n/k\rfloor}k\uparrow(\mu(d)[d\mid i][d\mid j]).
    $$
    
    Further extracting the factor (i.e. letting $i=di'$, $j=dj'$) and applying the property of the [floor function](./basic.md#rounding-functions), we obtain:
    
    $$
    g(n) = \prod_k\prod_d\prod_{i=1}^{\lfloor n/(kd)\rfloor}\prod_{j=1}^{\lfloor n/(kd)\rfloor}k\uparrow\mu(d).
    $$
    
    Then separating the product concerning $i,j$, we find that the product does not contain $i,j$, so it amounts to raising the product to a power:
    
    $$
    g(n) = \prod_k\prod_d k\uparrow\left(\mu(d)\left\lfloor\dfrac{n}{kd}\right\rfloor^2\right).
    $$
    
    Because we enumerated the common factor earlier, for this expression we need to exchange the order of the product again. Let $\ell = kd$; we have:
    
    $$
    \begin{aligned}
    g(n) &= \prod_{\ell}\prod_{d\mid\ell}\left(\dfrac{\ell}{d}\right)\uparrow\left(\mu(d)\left\lfloor\dfrac{n}{\ell}\right\rfloor^2\right)\\
    &= \prod_\ell\left(\prod_{d\mid\ell}\left(\dfrac{\ell}{d}\right)\uparrow\mu(d)\right)\uparrow\left\lfloor\dfrac{n}{\ell}\right\rfloor^2.
    \end{aligned}
    $$
    
    Let
    
    $$
    F(n) = \prod_{d\mid n}\left(\dfrac{n}{d}\right)\uparrow\mu(d).
    $$
    
    It is easy to find that this is the multiplicative-form Möbius inversion of $\tilde F(n)=n$. Even without knowing its expression, one can apply the [Dirichlet difference](#dirichlet-prefix-sum) method to preprocess in $O(n\log\log n)$ time. Of course, since the form of $\tilde F(n)$ is very simple, the expression for $F(n)$ can be directly found:
    
    $$
    F(n) = 
    \begin{cases}
    p, & n = p^e,~p\in\mathbf P,~e\in\mathbf N_+, \\
    1, &\text{otherwise}.
    \end{cases}
    $$
    
    The [von Mangoldt function](#möbius-inversion) is exactly its natural logarithm. After obtaining the values of $F(n)$, directly applying the product version of number-theoretic block decomposition allows us to find the value of $g(n)$ in $O(\sqrt{n})$ time, and thus obtain the value of $f(n)$. The total time complexity is $O(n)$.
    
    It is worth noting that when computing products, we often need to use [Euler's theorem](./fermat.md), so the modulus used for taking the exponent modulo is not the same as the modulus given in the problem.

??? note "Solution two"
    The difficulty of the multiplicative-version derivation lies in the relative unfamiliarity of handling products and powers, so for this kind of problem, we can also take the logarithm before deriving. For this problem, we only consider the derivation of $g(n)$. After taking its logarithm, we have:
    
    $$
    \log g(n) = \sum_{i=1}^n\sum_{j=1}^n\log\gcd(i,j).
    $$
    
    For this kind of expression involving the greatest common divisor, directly applying the standard derivation flow, we obtain:
    
    $$
    \begin{aligned}
    \log g(n) 
    &= \sum_k\log k\sum_{i=1}^n\sum_{j=1}^n[\gcd(i,j)=k]\\
    &= \sum_k\log k\sum_{i=1}^{\lfloor n/k\rfloor}\sum_{j=1}^{\lfloor n/k\rfloor}[\gcd(i,j)=1]\\
    &= \sum_k\log k\sum_d\mu(d)\left(\sum_{i=1}^{\lfloor n/k\rfloor}[i\mid d]\right)\left(\sum_{j=1}^{\lfloor n/k\rfloor}[j\mid d]\right)\\
    &= \sum_k\log k\sum_d\mu(d)\left\lfloor\dfrac{n}{kd}\right\rfloor^2\\
    &= \sum_{\ell}\left(\sum_d\mu(d)\log\dfrac{\ell}{d}\right)\left\lfloor\dfrac{n}{\ell}\right\rfloor^2\\
    &= \sum_{\ell}\Lambda(\ell)\left\lfloor\dfrac{n}{\ell}\right\rfloor^2.
    \end{aligned}
    $$
    
    Here, $\Lambda(n)$ is the [von Mangoldt function](#möbius-inversion). Raising this derivation result to a power gives the result of solution one.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/mobius/mobius_5.cpp"
    ```

## Exercises

-   [Luogu P3312 \[SDOI2014\] 数表](https://www.luogu.com.cn/problem/P3312)
-   [Luogu P3700 \[CQOI2017\] 小 Q 的表格](https://www.luogu.com.cn/problem/P3700)
-   [Luogu P3704 \[SDOI2017\] 数字表格](https://www.luogu.com.cn/problem/P3704)
-   [Luogu P3768 简单的数学题](https://www.luogu.com.cn/problem/P3768)
-   [Luogu P4464 \[国家集训队\] JZPKIL](https://www.luogu.com.cn/problem/P4464)
-   [Luogu P4619 \[SDOI2018\] 旧试题](https://www.luogu.com.cn/problem/P4619)
-   [Luogu P5518 \[MtOI2019\] 幽灵乐团](https://www.luogu.com.cn/problem/P5518)
-   [Luogu P6222 简单题 加强版](https://www.luogu.com.cn/problem/P6222)
-   [Luogu P6825「EZEC-4」求和](https://www.luogu.com.cn/problem/P6825)
-   [Luogu P7486「Stoi2031」彩虹](https://www.luogu.com.cn/problem/P7486)
-   [AtCoder Grand Contest 038 C - LCMs](https://atcoder.jp/contests/agc038/tasks/agc038_c)
-   [Codeforeces 1139 D. Steps to One](https://codeforces.com/problemset/problem/1139/D)

## References

-   [Möbius function - Wikipedia](https://en.wikipedia.org/wiki/M%C3%B6bius_function)
-   [Möbius inversion formula - Wikipedia](https://en.wikipedia.org/wiki/M%C3%B6bius_inversion_formula)
-   [Von Mangoldt function - Wikipedia](https://en.wikipedia.org/wiki/Von_Mangoldt_function)
-   [algocode 算法博客](https://web.archive.org/web/20190523150159/https://algocode.net/2018/04/18/20180418-KB-Mobius-Inversion-Formula/)
