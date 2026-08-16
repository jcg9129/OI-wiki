## Introduction

> The "counting the unknown number of things" problem: there are some things whose number is unknown. Counting them by threes, there remain two; counting by fives, there remain three; counting by sevens, there remain two. How many things are there?

That is, find an integer satisfying the following conditions: it leaves a remainder of $2$ when divided by $3$, a remainder of $3$ when divided by $5$, and a remainder of $2$ when divided by $7$.

This problem is first seen in *Sunzi Suanjing* (*The Mathematical Classic of Sunzi*), which also gives a specific solution. The Song dynasty mathematician Qin Jiushao, in his 1247 work *Shushu Jiuzhang* (*Mathematical Treatise in Nine Sections*), volumes one and two, "Dayan category", gave a complete and systematic answer to the "counting the unknown number of things" problem. The mnemonic for the answer to the specific problem above was given by the Ming dynasty mathematician Cheng Dawei in *Suanfa Tongzong* (*General Source of Computational Methods*):

> 三人同行七十希，五树梅花廿一支，七子团圆正半月，除百零五便得知．

$2\times 70+3\times 21+2\times 15=233=2\times 105+23$, so the answer is $23$.

## Definition

The Chinese Remainder Theorem (CRT) can solve a system of one-variable linear congruence equations of the following form (where $n_1, n_2, \cdots, n_k$ are pairwise coprime):

$$
\begin{cases}
x &\equiv a_1 \pmod {n_1} \\
x &\equiv a_2 \pmod {n_2} \\
  &\vdots \\
x &\equiv a_k \pmod {n_k} \\
\end{cases}
$$

The "counting the unknown number of things" problem above is an instance of a system of one-variable linear congruence equations.

## Process

1.  Compute the product of all moduli $n$;
2.  For the $i$-th equation:
    1.  Compute $m_i=\frac{n}{n_i}$;
    2.  Compute the [inverse](./inverse.md) $m_i^{-1}$ of $m_i$ modulo $n_i$;
    3.  Compute $c_i=m_im_i^{-1}$ (**do not take the modulus with respect to $n_i$**).
3.  The unique solution of the system modulo $n$ is: $x=\sum_{i=1}^k a_ic_i \pmod n$.

## Implementation

=== "C++"
    ```cpp
    LL CRT(int k, LL* a, LL* r) {
      LL n = 1, ans = 0;
      for (int i = 1; i <= k; i++) n = n * r[i];
      for (int i = 1; i <= k; i++) {
        LL m = n / r[i], b, y;
        exgcd(m, r[i], b, y);  // b * m mod r[i] = 1
        ans = (ans + a[i] * m * b % n) % n;
      }
      return (ans % n + n) % n;
    }
    ```

=== "Python"
    ```python
    def CRT(k, a, r):
        n = 1
        ans = 0
        for i in range(1, k + 1):
            n = n * r[i]
        for i in range(1, k + 1):
            m = n // r[i]
            b = y = 0
            exgcd(m, r[i], b, y)  # b * m mod r[i] = 1
            ans = (ans + a[i] * m * b % n) % n
        return (ans % n + n) % n
    ```

## Proof

We need to prove that the $x$ computed by the above algorithm satisfies $x\equiv a_i \pmod {n_i}$ for any $i=1,2,\cdots,k$.

When $i\neq j$, we have $m_j \equiv 0 \pmod {n_i}$, so $c_j \equiv m_j \equiv 0 \pmod {n_i}$. We also have $c_i \equiv m_i \cdot (m_i^{-1} \bmod {n_i}) \equiv 1 \pmod {n_i}$, so we have:

$$
\begin{aligned}
x&\equiv \sum_{j=1}^k a_jc_j                      &\pmod {n_i} \\
 &\equiv a_ic_i                                   &\pmod {n_i} \\
 &\equiv a_i \cdot m_i \cdot (m^{-1}_i \bmod n_i) &\pmod {n_i} \\
 &\equiv a_i                                      &\pmod {n_i}
\end{aligned}
$$

That is, for any $i=1,2,\cdots,k$, the $x$ obtained by the above algorithm always satisfies $x\equiv a_i \pmod{n_i}$, which proves the correctness of the algorithm for solving the system of congruence equations.

Because we did not impose any special restriction on the input $a_i$, any input $\{a_i\}$ corresponds to a solution $x$. Moreover, if $x\neq y$, then there always exists an $i$ such that $x$ and $y$ are not congruent modulo $n_i$. Therefore there is a one-to-one correspondence between the coefficient list $\{a_i\}$ and the solution $x$, and the system always has a unique solution.

## Explanation

The following demonstrates how CRT solves the "counting the unknown number of things" problem.

1.  $n=3\times 5\times 7=105$;
2.  三人同行 **七十** 希 (three people traveling together, **seventy** rare): $n_1=3, m_1=n/n_1=35, m_1^{-1}\equiv 2\pmod 3$, so $c_1=35\times 2=70$;
3.  五树梅花 **廿一** 支 (five plum trees, **twenty-one** branches): $n_2=5, m_2=n/n_2=21, m_2^{-1}\equiv 1\pmod 5$, so $c_2=21\times 1=21$;
4.  七子团圆正 **半月** (seven sons reunited, exactly **half a month**): $n_3=7, m_3=n/n_3=15, m_3^{-1}\equiv 1\pmod 7$, so $c_3=15\times 1=15$;
5.  So the unique solution of the system is $x\equiv 2\times 70+3\times 21+2\times 15\equiv 233\equiv 23 \pmod {105}$. (除 **百零五** 便得知 — subtracting **one hundred and five**, we obtain the answer.)

## Garner's algorithm

Another use of CRT is to represent a large integer using a set of relatively small primes.

For example, if $a$ satisfies the following system of linear equations, and $a < \prod_{i=1}^k p_i$ (where $p_i$ are primes):

$$
\begin{cases}
a &\equiv a_1 \pmod {p_1} \\
a &\equiv a_2 \pmod {p_2} \\
  &\vdots \\
a &\equiv a_k \pmod {p_k} \\
\end{cases}
$$

We can represent $a$ using an expression of the following form (called the mixed radix representation of $a$):

$$
a = x_1 + x_2 p_1 + x_3 p_1 p_2 + \ldots + x_k p_1 \ldots p_{k-1}
$$

**Garner's algorithm** will be used to compute the coefficients $x_1, \ldots, x_k$.

Let $r_{ij}$ be the [inverse](./inverse.md) of $p_i$ modulo $p_j$:

$$
p_i \cdot r_{i,j} \equiv 1 \pmod{p_j}
$$

Substituting $a$ into the first equation we obtained:

$$
a_1 \equiv x_1 \pmod{p_1}
$$

Substituting into the second equation gives:

$$
a_2 \equiv x_1 + x_2 p_1 \pmod{p_2}
$$

Subtracting $x_1$ from both sides of the equation and dividing by $p_1$ gives

$$
\begin{aligned}
    a_2 - x_1           &\equiv x_2 p_1             &\pmod{p_2} \\
    (a_2 - x_1) r_{1,2} &\equiv x_2                 &\pmod{p_2} \\
    x_2                 &\equiv (a_2 - x_1) r_{1,2} &\pmod{p_2}
\end{aligned}
$$

Similarly, we can obtain:

$$
x_k=(\dots((a_k-x_1)r_{1,k}-x_2)r_{2,k})-\dots)r_{k-1,k} \bmod p_k
$$

??? note "Implementation"
    === "C++"
        ```cpp
        for (int i = 0; i < k; ++i) {
          x[i] = a[i];
          for (int j = 0; j < i; ++j) {
            x[i] = r[j][i] * (x[i] - x[j]);
            x[i] = x[i] % p[i];
            if (x[i] < 0) x[i] += p[i];
          }
        }
        ```
    
    === "Python"
        ```python
        for i in range(0, k):
            x[i] = a[i]
            for j in range(0, i):
                x[i] = r[j][i] * (x[i] - x[j])
                x[i] = x[i] % p[i]
                if x[i] < 0:
                    x[i] = x[i] + p[i]
        ```

The time complexity of this algorithm is $O(k^2)$. In fact, Garner's algorithm does not require the moduli to be prime, only that the moduli be pairwise coprime. We have the following pseudocode:

$$
\begin{array}{ll}
&\textbf{Chinese Remainder Algorithm }\operatorname{cra}(\mathbf{v}, \mathbf{m})\text{:} \\
&\textbf{Input}\text{: }\mathbf{m}=(m_0,m_1,\dots ,m_{n-1})\text{, }m_i\in\mathbb{Z}^+\land\gcd(m_i,m_j)=1\text{ for all } i\neq j\text{,} \\
&\qquad \mathbf{v}=(v_0,\dots ,v_{n-1}) \text{ where }v_i=x\bmod m_i\text{.} \\
&\textbf{Output}\text{: }x\bmod{\prod_{i=0}^{n-1} m_i}\text{.} \\
1&\qquad \textbf{for }i\text{ from }1\text{ to }(n-1)\textbf{ do} \\
2&\qquad \qquad C_i\gets \left(\prod_{j=0}^{i-1}m_j\right)^{-1}\bmod{m_i} \\
3&\qquad x\gets v_0 \\
4&\qquad \textbf{for }i\text{ from }1\text{ to }(n-1)\textbf{ do} \\
5&\qquad \qquad u\gets (v_i-x)\cdot C_i\bmod{m_i} \\
6&\qquad \qquad x\gets x+u\prod_{j=0}^{i-1}m_j \\
7&\qquad \textbf{return }(x)
\end{array}
$$

One can see that the computation process in line six corresponds to the mixed radix representation above.

## Applications

Some counting problems or number-theory problems, for reasons of lengthening the code, increasing the difficulty, or some other reasons, give a modulus that is **not prime**!

But upon prime-factoring it, one finds that it has no square factors, that is, the modulus is obtained by multiplying some distinct primes.

Then we can compute for each of these moduli separately, and finally merge the answers using CRT.

The following problem is a good example.

???+ note "[Luogu P2480 \[SDOI2010\] 古代猪文](https://www.luogu.com.cn/problem/P2480)"
    Given $G,n$ ($1 \leq G,n \leq 10^9$), find:
    
    $$
    G^{\sum_{k\mid n}\binom{n}{k}} \bmod 999~911~659
    $$

First, when $G=999~911~659$, the desired value is obviously $0$.

Otherwise, according to [Euler's theorem](./fermat.md), the desired value is:

$$
G^{\sum_{k\mid n}\binom{n}{k} \bmod 999~911~658} \bmod 999~911~659
$$

Now consider how to compute:

$$
\sum_{k\mid n}\binom{n}{k} \bmod 999~911~658
$$

Because $999~911~658$ is not prime, we cannot guarantee that $\forall x \in [1,999~911~657]$, $x$ has an inverse. We cannot directly compute the above expression.

Noting that $999~911~658=2 \times 3 \times 4679 \times 35617$, where the highest power of each prime factor is one, we can consider computing $\sum_{k\mid n}\binom{n}{k}$ modulo the primes $2$, $3$, $4679$, $35617$ separately, and finally merge the answers using the Chinese Remainder Theorem.

That is to say, we actually need to find the solution of the following system of linear equations:

$$
\begin{cases}
x \equiv a_1 \pmod 2\\
x \equiv a_2 \pmod 3\\
x \equiv a_3 \pmod {4679}\\
x \equiv a_4 \pmod {35617}
\end{cases}
$$

And computing the result of a binomial coefficient modulo a relatively small prime can use [Lucas' theorem](./lucas.md).

## Extension: the case where moduli are not coprime

### Two equations

Let the two equations be $x\equiv a_1 \pmod {m_1}$ and $x\equiv a_2 \pmod {m_2}$;

Transform them into an indeterminate equation: $x=m_1p+a_1=m_2q+a_2$, where $p, q$ are integers, then we have $m_1p-m_2q=a_2-a_1$.

By [Bézout's identity](./bezouts.md), when $a_2-a_1$ is not divisible by $\gcd(m_1,m_2)$, there is no solution;

In other cases, we can use the [extended Euclidean algorithm](./gcd.md) to solve for a feasible solution $(p, q)$;

Then the solution of the modular equation system composed of the original two equations is $x\equiv b\pmod M$, where $b=m_1p+a_1$, $M=\text{lcm}(m_1, m_2)$.

### Multiple equations

Simply merge them pairwise using the method above.

## Exercises

-   [【模板】中国剩余定理（CRT）/曹冲养猪](https://www.luogu.com.cn/problem/P1495)
-   [【模板】扩展中国剩余定理](https://www.luogu.com.cn/problem/P4777)
-   [「NOI2018」屠龙勇士](https://uoj.ac/problem/396)
-   [「TJOI2009」猜数字](https://www.luogu.com.cn/problem/P3868)

    **Part of the content of this page is translated from the blog post [Китайская теорема об остатках](http://e-maxx.ru/algo/chinese_theorem) and its English translation [Chinese Remainder Theorem](https://cp-algorithms.com/algebra/chinese-remainder-theorem.html). The Russian version is under the Public Domain + Leave a Link license; the English version is under the CC-BY-SA 4.0 license.**
