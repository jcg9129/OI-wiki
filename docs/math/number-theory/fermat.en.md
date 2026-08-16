author: PeterlitsZo, Tiphereth-A

This article discusses Fermat's little theorem, Euler's theorem, and their extension. These theorems solve the problem of computing powers with arbitrarily large exponents under any modulus.

## Fermat's little theorem

**Fermat's little theorem** is one of the most basic theorems in number theory. It is also the theoretical basis of the [Fermat primality test](./prime.md#fermat-素性测试).

???+ note "Fermat's little theorem"
    Let $p$ be a prime. For any integer $a$ with $p\nmid a$, $a^{p-1}\equiv 1\pmod p$ holds.

???+ note "Theorem"
    Let $p$ be a prime. For any integer $a$, $a^{p}\equiv a\pmod p$ holds.

These two congruences are equivalent when $p\nmid a$; and when $p\mid a$, $a^p\equiv 0\equiv a\pmod p$ holds trivially. Therefore, these two propositions are equivalent. Both of these propositions are often called Fermat's little theorem.

??? note "Proof 1"
    Let $p$ be a prime and $p\nmid a$. First we prove: for $i=1,2,\cdots,p-1$, the remainders $ia \bmod p$ are all distinct. Proof by contradiction. If there are $1\le i < j < p$ such that
    
    $$
    ia \bmod p = ja \bmod p. \iff (j-i)a\equiv 0.\pmod p
    $$
    
    But $(j-i)$ and $a$ are both not multiples of $p$, which is obviously a contradiction.
    
    In other words, these remainders are a permutation of $\{1,2,\cdots,p-1\}$. Therefore,
    
    $$
    \prod_{i=1}^{p-1}i = \prod_{i=1}^{p-1}(ia\bmod p) \equiv \prod_{i=1}^{p-1}ia = a^{p-1}\prod_{i=1}^{p-1}i.\pmod p
    $$
    
    This shows
    
    $$
    (a^{p-1}-1)\prod_{i=1}^{p-1}i \equiv 0. \pmod{p}
    $$
    
    That is, the left side of the equation is a multiple of $p$, but $i=1,2,\cdots, p-1$ are all not multiples of $p$, so there can only be $p\mid (a^{p-1}-1)$, i.e. Fermat's little theorem holds.

??? note "Proof 2"
    Note that the second formulation of Fermat's little theorem holds for all $a\in\mathbf N$, so one can consider using mathematical induction. The case of negative integers is easily reduced to the case of non-negative integers.
    
    The induction base is $0^p\equiv 0\pmod p$, which obviously holds. Suppose it holds for $a\in\mathbf N$; we need to prove that it also holds for $a+1$. By the binomial theorem,
    
    $$
    (a+1)^p=a^p+\binom{p}{1}a^{p-1}+\binom{p}{2}a^{p-2}+\cdots +\binom{p}{p-1}a+1.
    $$
    
    Except for the first and last terms, in the binomial-coefficient expression $\dbinom{p}{k} = \dfrac{p!}{k!(p-k)!}$, $p$ divides the numerator but not the denominator, so these coefficients are all multiples of $p$ for $k\neq 0,p$. Therefore,
    
    $$
    (a+1)^p \equiv a^p + 1\equiv a + 1. \pmod{p}
    $$
    
    where the second step applies the induction hypothesis. Therefore, by mathematical induction, Fermat's little theorem holds.

The converse of Fermat's little theorem does not hold. Even if $a^{n-1}\equiv 1\pmod n$ holds for all $a$ coprime with $n$, $n$ is not necessarily a prime. For the relevant discussion, see the [Fermat primality test](./prime.md#fermat-素性测试) section.

## Euler's theorem

**Euler's theorem** generalizes Fermat's little theorem to the case of a general modulus, but still requires the base and the modulus to be coprime.

???+ note "Euler's theorem"
    For an integer $m>0$ and an integer $a$ with $\gcd(a,m)=1$, $a^{\varphi(m)}\equiv 1\pmod{m}$, where $\varphi(\cdot)$ is [Euler's totient function](./euler-totient.md).

??? note "Proof"
    Similar to Proof 1 of Fermat's little theorem, we again take a sequence of numbers coprime with $m$ and operate. Consider the set
    
    $$
    R = \{r\in\mathbf N : 0 < r < m,~\gcd(r,m)=1\}.
    $$
    
    This is a [reduced residue system](./basic.md#congruence-classes-and-residue-systems) modulo $m$. By the definition of Euler's totient function, $|R|=\varphi(m)$. Similar to the above, multiplying them by $a$ amounts to rearranging this set:
    
    $$
    R = \{ar\bmod m: r\in R\}.
    $$
    
    This is because one can easily verify $\gcd(ar,m)=1$, and different $r_1,r_2\in R$ correspond to different $ar_1\bmod m$ and $ar_2\bmod m$. Therefore,
    
    $$
    \prod_{r\in R}r \equiv \prod_{r\in R}ar = a^{\varphi(m)}\prod_{r\in R}r. \pmod{m}
    $$
    
    Repeating the earlier argument once more, canceling $\prod_{r\in R}r$, we obtain $a^{\varphi(m)}\equiv 1\pmod m$.

For a prime $p$, $\varphi(p)=p-1$, so Fermat's little theorem is a special case of Euler's theorem. In addition, the exponent $\varphi(m)$ in Euler's theorem is in general not the smallest exponent making the formula hold. It can be improved to $\lambda(m)$, where $\lambda(\cdot)$ is the [Carmichael function](./primitive-root.md#carmichael-函数). For the algebraic background of the relevant conclusions, one can refer to the section [the multiplicative group of integer congruence classes](../algebra/ring-theory.md#application-the-multiplicative-group-of-integer-congruence-classes).

## Extended Euler's theorem

The extended Euler's theorem[^ex-euler] further generalizes the conclusion to the case where the base and the exponent are not coprime. From this, it completely solves the problem of computing powers of any base under any modulus, transforming them into the case where the exponent is less than $2\varphi(m)$, so that one can compute them via [fast exponentiation](../binary-exponentiation.md) in $O(\log\varphi(m))$ time.

???+ note "Extended Euler's theorem"
    For any positive integer $m$, integer $a$, and non-negative integer $k$,
    
    $$
    a^k \equiv \begin{cases}
    a^{k \bmod \varphi(m)},                &\gcd(a,m) =  1,                   \\
    a^k,                                   &\gcd(a,m)\ne 1, k <   \varphi(m), \\
    a^{(k \bmod \varphi(m)) + \varphi(m)}, &\gcd(a,m)\ne 1, k \ge \varphi(m).
    \end{cases} \pmod m
    $$

The second case says that if $k < \varphi(m)$, then there is no need to continue reducing the exponent, and one directly applies fast exponentiation; the biggest difference between the third case and the first is whether, after reducing the exponent by taking the modulus, one needs to add a term $\varphi(m)$. Of course, merging the first case into the second and third cases is also correct.

### Intuitive understanding

Before rigorously proving the theorem, one can first intuitively understand the meaning of the theorem.

![fermat1](./images/fermat.svg)

Consider how the remainder $a^k\bmod m$ changes as $b$ increases. Since the value of the remainder must be in the interval $[0,m)$, while $k$ has infinitely many values. Regard $a^k\bmod m \mapsto a^{k+1}\bmod m$ as a directed edge between these remainder nodes. Then, one can necessarily form a cycle as shown in the figure.

The extended Euler's theorem shows that these cycles may be pure cycles (the first case) or mixed cycles (the second and third cases). In a pure cycle, no node has two predecessors, while in a mixed cycle such a situation occurs. Therefore, for the general case, as long as one can find the length of the cycle and the length before entering the cycle, one can use this property to reduce the exponent.

### Rigorous proof

This section gives a rigorous proof of the extended Euler's theorem.

??? note "Proof"
    First we show that there exists $k_0\in\mathbf N$ such that the integer $a$ and $m':=\dfrac{m}{\gcd(a^{k_0},m)}$ are coprime. To this end, let $\nu_p(n)$ be the power of the prime $p$ in the prime factorization of the integer $n$; then we may take
    
    $$
    k_0 = \max\left\{\left\lceil\dfrac{\nu_p(m)}{\nu_p(a)}\right\rceil : \nu_p(a)>0\right\}.
    $$
    
    Because all the powers of the common prime factors of $m$ with $a$ are already contained in $a^{k_0}$, $a$ is coprime with the remaining factor $m'=\dfrac{m}{\gcd(a^{k_0},m)}$ of $m$.
    
    Furthermore, for $k\ge k_0$ consider the congruence
    
    $$
    b\equiv a^k. \pmod m
    $$
    
    Since $\gcd(a^{k_0},m)=\gcd(a^k,m)\mid b$, dividing both sides of the equation (including the modulus) by $\gcd(a^{k_0},m)$,
    
    $$
    \dfrac{b}{\gcd(a^{k_0},m)} = \dfrac{a^{k_0}}{\gcd(a^{k_0},m)}\cdot a^{k-k_0}. \pmod{m'}
    $$
    
    In this case, because $a$ is coprime with the modulus $m'$, one can directly apply Euler's theorem, obtaining
    
    $$
    \dfrac{b}{\gcd(a^{k_0},m)} \equiv \dfrac{a^{k_0}}{\gcd(a^{k_0},m)}\cdot a^{(k-k_0)\bmod\varphi(m')}. \pmod{m'}
    $$
    
    Therefore, multiplying back the factor $\gcd(a^{k_0},m)$,
    
    $$
    b \equiv a^{k_0}\cdot a^{(k-k_0)\bmod\varphi(m')} = a^{k_0 + (k-k_0)\bmod\varphi(m')}. \pmod{m}
    $$
    
    This gives the form of the extended Euler's theorem. The formula shows that the length of the cycle is $\varphi(m')$, and the length before entering the cycle is $k_0$.
    
    The parameters obtained here are tighter than those in the extended Euler's theorem, but relatively speaking, the computation of these parameters is not easy. One can show that these parameters can be relaxed to the case in the extended Euler's theorem. First, using the [expression for Euler's totient function](./euler-totient.md), since $m'\mid m$, $\varphi(m')\mid\varphi(m)$. That is, $\varphi(m)$ is also its cycle. Second, $k_0$ can also be relaxed to $\varphi(m)$. This is because for all $m\in\mathbf N_+$ and any $p\mid m$,
    
    $$
    \begin{aligned}
    \varphi(m) &\ge \varphi(p^{\nu_p(m)}) = (p-1)p^{\nu_p(m)-1} \ge p^{\nu_p(m)-1} \\
    &= (1+(p-1))^{\nu_p(m)-1} \ge 1 + (p-1)(\nu_p(m)-1) \\
    &\ge 1 + (\nu_p(m)-1) = \nu_p(m).
    \end{aligned}
    $$
    
    where the inequality in the second line uses the binomial expansion, keeping only the constant and first-order terms. Therefore,
    
    $$
    k_0 \le \max\{\nu_p(m):p\in\mathbf P\}\le \varphi(m).
    $$
    
    This completely proves the stated conclusion.

## Example problem

This section demonstrates, through an example problem, a classic application of the extended Euler's theorem—computing a power tower under any modulus. A **power tower** refers to an expression of the form $A\uparrow(B\uparrow(C\uparrow(D\uparrow\cdots)))$, where $\uparrow$ is Knuth's up-arrow notation and $A,B,C,D,\cdots$ are a series of non-negative integers.

???+ example "[Library Checker - Tetration Mod](https://judge.yosupo.jp/problem/tetration_mod)"
    $T$ test cases. In each test case, given $A,B,M$, find $(A\uparrow\uparrow B)\bmod M$, where $A\uparrow\uparrow B$ denotes the power tower composed of $B$ copies of $A$. Or, formally, define
    
    $$
    A \uparrow\uparrow B =
    \begin{cases}
    1 , & B = 0,\\
    A\uparrow(A\uparrow\uparrow(B-1)), & B > 0.
    \end{cases}
    $$
    
    It is stipulated that $0^0=1$.

??? note "Solution"
    Using the definition of $A\uparrow\uparrow B$, recursive computation suffices. To compute $(A\uparrow\uparrow B)\bmod M$, one only needs to apply the extended Euler's theorem, computing $(A\uparrow\uparrow(B-1))\bmod\varphi(M)$. Since $\varphi(\varphi(n)) \le n/2$ holds for all $n\ge 2$, the recursion is sure to complete within $O(\log M)$ steps. Since the extended Euler's theorem needs to be applied, one needs to distinguish whether the current computation result is strictly less than the current modulus. To this end, one only needs to make one more check when taking the modulus. In addition, one needs to note the handling of boundary cases.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/fermat/tetration.cpp"
    ```

## Exercises

-   [Luogu P5091 【模板】扩展欧拉定理](https://www.luogu.com.cn/problem/P5091)
-   [Codeforces 906 D. Power Tower](https://codeforces.com/problemset/problem/906/D)
-   [Luogu P3747 \[六省联考 2017\] 相逢是问候](https://www.luogu.com.cn/problem/P3747)
-   [Luogu P4139 上帝与集合的正确用法](https://www.luogu.com.cn/problem/P4139)
-   [Luogu P3934 \[Ynoi Easy Round 2016\] 炸脖龙 I](https://www.luogu.com.cn/problem/P3934)
-   [Luogu P6736「Wdsr-2」白泽教育](https://www.luogu.com.cn/problem/P6736)

## References and notes

-   [Fermat's little theorem - Wikipedia](https://en.wikipedia.org/wiki/Fermat%27s_little_theorem)
-   [Euler's theorem - Wikipedia](https://en.wikipedia.org/wiki/Euler%27s_theorem)
-   Hardy, Godfrey Harold, and Edward Maitland Wright. An introduction to the theory of numbers. Oxford university press, 1979.

[^ex-euler]: This name mainly appears in the competitive programming community, and is not the common name of this conclusion.
