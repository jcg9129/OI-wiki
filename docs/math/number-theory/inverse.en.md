This article introduces the multiplicative inverse under a modulus and discusses its common methods of computation.

## Basic concepts

The multiplicative inverse of a nonzero real number $a\in\mathbf R$ is its reciprocal $a^{-1}$. Similarly, in number theory one can define the inverse $a^{-1}\bmod m$ of an integer $a$ modulo $m$, or simply denote it $a^{-1}$. This is the **modular multiplicative inverse**.

???+ abstract "Inverse"
    For nonzero integers $a,m$, if there exists $b$ such that $ab\equiv 1\pmod m$, then $b$ is called the **inverse** of $a$ modulo $m$.

This is equivalent to saying that $b$ is a solution of the linear congruence equation $ax\equiv 1\pmod m$. By the properties of the [linear congruence equation](./linear-equation.md), the inverse $a^{-1}\bmod m$ exists and is unique modulo $m$ if and only if $\gcd(a,m)=1$, i.e. $a,m$ are coprime.

## Finding a single inverse

Using the extended Euclidean algorithm or fast exponentiation, one can find the inverse of a single integer in $O(\log m)$ time.

### Extended Euclidean algorithm

Finding the inverse is equivalent to solving a linear congruence equation. Therefore, one can use the [extended Euclidean algorithm](./gcd.md#extended-euclidean-algorithm) to find the inverse in $O(\log\min\{a,m\})$ time. At the same time, since the linear equation corresponding to the inverse is relatively special, one can appropriately simplify the corresponding steps.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-1.py:core"
        ```

This algorithm applies to all cases where the inverse exists.

### Fast exponentiation

This method is mainly applicable to the case where the modulus is a prime $p$. In this case, by [Fermat's little theorem](./fermat.md#fermats-little-theorem), for any $a\perp p$,

$$
a\cdot a^{p-2} = a^{p-1} \equiv 1 \pmod p.
$$

By the uniqueness of the inverse, the inverse $a^{-1}\bmod p$ equals $a^{p-2}\bmod p$, so one can directly use [fast exponentiation](../binary-exponentiation.md) to compute it in $O(\log p)$ time:

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-2.py:core"
        ```

Of course, in theory, this method can be generalized to the general modulus $m$ case using [Euler's theorem](./fermat.md#eulers-theorem), i.e. computing the inverse using $a^{\varphi(m)-1}\bmod m$. But computing [Euler's totient function](./euler-totient.md) $\varphi(m)$ once is not easy, so this algorithm is not efficient in the general case.

## Finding multiple inverses

In some scenarios, one needs to quickly process the inverses of multiple integers $a_1,a_2,\cdots,a_n$ modulo $m$. In this case, finding the inverses one by one requires a total of $O(n\log m)$ time. In fact, if one processes them uniformly, one can find the inverses of all integers in $O(n+\log m)$ time.

Consider the prefix products of the sequence $\{a_i\}$:

$$
S_0 = 1,~ S_i = a_iS_{i-1},~ i=1,2,\cdots,n.
$$

As long as each $a_i$ is coprime with $m$, their product $S_n$ is coprime with $m$. Therefore, one can find the value of $S_n^{-1}\bmod m$ through the algorithm described earlier. Because the inverse of a product is the product of the inverses, starting from $S_n^{-1}$ and traversing the sequence in reverse, one can find the inverse of each $S_i$:

$$
S_{i-1}^{-1} = a_iS_i^{-1} \bmod m,~ i = n,n-1,\cdots,1.
$$

From this, the inverse of a single $a_i$ can be computed by the following:

$$
a_i^{-1} = S_{i-1}S_i^{-1} \bmod m,~ i = 1,2,\cdots,n.
$$

The reference implementation is as follows:

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-3.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-3.py:core"
        ```

In the algorithm, the inverse of a single element is found only once, so the total time complexity is $O(n+\log m)$.

## Linear-time preprocessing of inverses

If one wants to preprocess the inverses of the first $n$ positive integers modulo a prime $p$, one can also compute them in $O(n)$ time through the recurrence to be discussed in this section. This method is commonly used in combinatorics computations for preprocessing the reciprocals of the factorials of the first $n$ positive integers.

For a positive integer $i$ with $1< i < p$, consider the division with remainder:

$$
p = \left\lfloor \dfrac{p}{i} \right\rfloor i + (p\bmod i).
$$

Taking this equation modulo the prime $p$ gives

$$
0 \equiv \left\lfloor \dfrac{p}{i} \right\rfloor i + (p\bmod i) \pmod p.
$$

Multiplying both sides of the equation by $i^{-1}(p\bmod i)^{-1}$ gives

$$
i^{-1} \equiv - \left\lfloor \dfrac{p}{i} \right\rfloor (p\bmod i)^{-1} \pmod p.
$$

This is the formula used for linear-time recursive computation of inverses. Since $p\bmod i < i$, this formula transforms the problem of finding $i^{-1}\bmod p$ into the smaller problem $(p\bmod i)^{-1}\bmod p$. Therefore, starting from $1^{-1}\bmod p=1$ and applying this formula successively to each $i$, one can obtain the inverses of the first $n$ integers in $O(n)$ time.

The reference implementation is as follows:

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/inverse/inverse-4.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/inverse/inverse-4.py:core"
        ```

This algorithm applies only to the case where the modulus is a prime. For the case where the modulus $m$ is not a prime, one cannot guarantee that the $m\bmod i$ obtained in the recurrence is still coprime with $m$, so the $(m\bmod i)^{-1}$ needed by the recurrence may not exist. One such example is $m=8,i=3$. In this case, $m\bmod i = 2$, and there is no inverse modulo $m$.

In addition, after obtaining this recurrence, one natural idea is to directly recursively find the inverse of any number $a$. Each recursion uses the recurrence to transform it into the inverse of a smaller remainder $p\bmod a$, stopping when the remainder becomes $1$. The complexity of doing so is currently unclear[^linear-recursion], so it is recommended to use the conventional method described earlier.

## Exercises

-   [LOJ 110 乘法逆元](https://loj.ac/problem/110)
-   [LOJ 161 乘法逆元 2](https://loj.ac/problem/161)
-   [LOJ 2605「NOIP2012」同余方程](https://loj.ac/problem/2605)
-   [Luogu P2054「AHOI2005」洗牌](https://www.luogu.com.cn/problem/P2054)
-   [LOJ 2034「SDOI2016」排列计数](https://loj.ac/problem/2034)

## References and notes

-   [Modular multiplicative inverse - Wikipedia](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)

[^linear-recursion]: [riteme's answer on Zhihu](https://www.zhihu.com/question/59033693/answer/323292359) points out that the theoretically known upper bound of the complexity of doing so is $O(p^{1/3+\varepsilon})$, while its performance on actual random data is close to $O(\log p)$.
