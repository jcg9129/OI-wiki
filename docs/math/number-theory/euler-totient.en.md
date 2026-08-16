author: iamtwz, Chrogeek, Enter-tainer, StudyingFather, aofall, CCXXXI, CoelacanthusHex, frank-xjh, Great-designer, greyqz, guodong2005, henrytbtrue, Ir1d, kZime, lihaoyu1234, Marcythm, MegaOwIer, Menci, nalemy, orzAtalod, ouuan, Persdre, segment-tree, ShaoChenHeng, shuzhouliu, sshwy, Struggler-q, Tiphereth-A, TrisolarisHD, Xeonacid, yuhuoji

## Definition

Euler's totient function, i.e. $\varphi(n)$, denotes the number of integers less than or equal to $n$ that are coprime with $n$.

For example, $\varphi(1) = 1$.

When $n$ is prime, obviously $\varphi(n) = n - 1$.

## Properties

-   Euler's totient function is a [multiplicative function](./basic.md#multiplicative-function).

    That is, for any integers $a,b$ satisfying $\gcd(a, b) = 1$, $\varphi(ab) = \varphi(a)\varphi(b)$.

    In particular, when $n$ is odd, $\varphi(2n) = \varphi(n)$.

    For the proof, see [composition of residue systems](./basic.md#composition-of-residue-systems).

-   $n = \sum_{d \mid n}{\varphi(d)}$.

    ???+ note "Proof"
        This can be derived using knowledge related to [Möbius inversion](./mobius.md).
        
        One can also consider it this way: if $\gcd(k, n) = d$, then $\gcd(\dfrac{k}{d},\dfrac{n}{d}) = 1, ( k < n )$.
        
        If we let $f(x)$ denote the number of integers with $\gcd(k, n) = x$, then $n = \sum_{i = 1}^n{f(i)}$.
        
        By the above proof, we find that $f(x) = \varphi(\dfrac{n}{x})$, so $n = \sum_{d \mid n}\varphi(\dfrac{n}{d})$. Noting that the divisors $d$ and $\dfrac{n}{d}$ have symmetry, the above becomes $n = \sum_{d \mid n}\varphi(d)$.

-   If $n = p^k$ where $p$ is prime, then $\varphi(n) = p^k - p^{k - 1}$.
    (This follows from the definition.)

-   By the unique factorization theorem, letting $n = \prod_{i=1}^{s}p_i^{k_i}$ where $p_i$ are primes, $\varphi(n) = n \times \prod_{i = 1}^s{\dfrac{p_i - 1}{p_i}}$.

    ???+ note "Proof"
        -   Lemma: let $p$ be any prime; then $\varphi(p^k)=p^{k-1}\times(p-1)$.
        
            Proof: obviously, among all the numbers from 1 to $p^k$, except for the $p^{k-1}$ multiples of $p$, all other numbers are coprime with $p^k$, so $\varphi(p^k)=p^k-p^{k-1}=p^{k-1}\times(p-1)$. Q.E.D.
        
        Next we prove $\varphi(n) = n \times \prod_{i = 1}^s{\dfrac{p_i - 1}{p_i}}$. By the unique factorization theorem and the multiplicativity of the $\varphi(x)$ function,
        
        $$
        \begin{aligned}
            \varphi(n) &= \prod_{i=1}^{s} \varphi(p_i^{k_i}) \\
            &= \prod_{i=1}^{s} (p_i-1)\times {p_i}^{k_i-1}\\
            &=\prod_{i=1}^{s} {p_i}^{k_i} \times(1 - \frac{1}{p_i})\\
            &=n~ \prod_{i=1}^{s} (1- \frac{1}{p_i})
            &\square
        \end{aligned}
        $$

-   For any integers $m,n$ not both $0$, $\varphi(mn)\varphi(\gcd(m,n))=\varphi(m)\varphi(n)\gcd(m,n)$.

    This can be directly computed from the previous item.

## Implementation

If one only needs the value of Euler's totient function for one number, then one directly computes it while doing prime factorization according to the definition. This process can be optimized with the [Pollard Rho](./pollard-rho.md) algorithm.

???+ note "Reference implementation"
    === "C++"
        ```cpp
        #include <cmath>
        
        int euler_phi(int n) {
          int ans = n;
          for (int i = 2; i * i <= n; i++)
            if (n % i == 0) {
              ans = ans / i * (i - 1);
              while (n % i == 0) n /= i;
            }
          if (n > 1) ans = ans / n * (n - 1);
          return ans;
        }
        ```
    
    === "Python"
        ```python
        import math
        
        
        def euler_phi(n):
            ans = n
            for i in range(2, math.isqrt(n) + 1):
                if n % i == 0:
                    ans = ans // i * (i - 1)
                    while n % i == 0:
                        n = n // i
            if n > 1:
                ans = ans // n * (n - 1)
            return ans
        ```

If it is the value of Euler's totient function for multiple numbers, one can find it using the linear sieve mentioned later.

For details, see: [finding Euler's totient function via a sieve](./sieve.md#筛法求欧拉函数)

## Applications

Euler's totient function is often used to simplify a sum of a series of greatest common divisors. Some domestic articles call it **Euler inversion**[^1].

Substituting $n=\gcd(a,b)$ into the conclusion

$$
n=\sum_{d|n}\varphi(d)
$$

gives

$$
\gcd(a,b) = \sum_{d|\gcd(a,b)}\varphi(d) = \sum_d [d|a][d|b]\varphi(d),
$$

where $[\cdot]$ is the Iverson bracket. Summing the above, one obtains

$$
\sum_{i=1}^n\gcd(i,n)=\sum_{d}\sum_{i=1}^n[d|i][d|n]\varphi(d)=\sum_d\left\lfloor\frac{n}{d}\right\rfloor[d|n]\varphi(d)=\sum_{d|n}\left\lfloor\frac{n}{d}\right\rfloor\varphi(d).
$$

The key observation here is $\sum_{i=1}^n[d|i]=\lfloor\frac{n}{d}\rfloor$, i.e. the number of $i$ between $1$ and $n$ divisible by $d$ is $\lfloor\frac{n}{d}\rfloor$.

Using this expression, one can iterate over the divisors to sum. When multiple queries are needed, one can preprocess the prefix sums of Euler's totient function and query using number-theoretic block decomposition.

???+ note "[GCD SUM](https://www.luogu.com.cn/problem/P2398)"
    Given $n\le 100000$, find
    
    $$
    \sum_{i=1}^n\sum_{j=1}^n\gcd(i,j).
    $$
    
    ??? note "Idea"
        Following the derivation above, one can obtain
        
        $$
        \sum_{i=1}^n\sum_{j=1}^n\gcd(i,j) = \sum_{d=1}^n\left\lfloor\frac{n}{d}\right\rfloor^2\varphi(d).
        $$
        
        In this case one needs to iterate from $1$ to $n$ to compute Euler's totient function; using a linear sieve, one can obtain the answer in $O(n)$.

## Euler's theorem

A theorem closely related to Euler's totient function is Euler's theorem. It is described as follows:

If $\gcd(a, m) = 1$, then $a^{\varphi(m)} \equiv 1 \pmod{m}$.

### Extended Euler's theorem

Of course there is also the extended Euler's theorem, used to handle the general case of $a$ and $m$.

$$
a^b\equiv
\begin{cases}
a^{b\bmod\varphi(m)},\,&\gcd(a,\,m)=1\\
a^b,&\gcd(a,\,m)\ne1,\,b<\varphi(m)\\
a^{b\bmod\varphi(m)+\varphi(m)},&\gcd(a,\,m)\ne1,\,b\ge\varphi(m)
\end{cases}
\pmod m
$$

For the proof and exercises, see [Euler's theorem](./fermat.md).

## Exercises

-   [SPOJ ETF. Euler Totient Function](http://www.spoj.com/problems/ETF/)
-   [UVa 10179. Irreducible Basic Fractions](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1120)
-   [UVa 10299. Relatives](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1240)
-   [UVa 11327. Enumerating Rational Numbers](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2302)
-   [TIMUS 1673. Admission to Exam](http://acm.timus.ru/problem.aspx?space=1&num=1673)
-   [Luogu P1390 公约数的和](https://www.luogu.com.cn/problem/P1390)
-   [Luogu P2155 \[SDOI2008\] 沙拉公主的困惑](https://www.luogu.com.cn/problem/P2155)
-   [Luogu P2568 GCD](https://www.luogu.com.cn/problem/P2568)

## References and notes

[^1]: This term has not been seen in academic journals or foreign forums, and one should be careful when using it.
