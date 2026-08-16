author: Marcythm, Xeonacid, CSPNOIP

## Definition

In terms of the idea and method of this kind of sieve, it is also called the "Extended Eratosthenes Sieve".

Because it was invented and first used by [Min\_25](https://web.archive.org/web/20211104125457/http://min-25.hatenablog.com/), it is called the "Min\_25 sieve".

## Properties

It can solve a class of prefix-sum problems of **multiplicative functions** in $O\left(\frac{n^{\frac{3}{4}}}{\log{n}}\right)$ or $\Theta\left(n^{1 - \epsilon}\right)$ time complexity.

Requirements: $f(p)$ is a sum of completely multiplicative functions that can be quickly evaluated in terms of $p$ (for example, a polynomial); $f(p^{c})$ can be quickly evaluated.

## Notation

-   **Unless otherwise specified, the value set of all variables denoted $p$ in this section is the set of all primes.**
-   $x / y := \left\lfloor\frac{x}{y}\right\rfloor$
-   $\operatorname{isprime}(n) := [ |\{d : d \mid n\}| = 2 ]$, i.e. its value is $1$ when $n$ is prime, and $0$ otherwise.
-   $p_{k}$: the $k$-th smallest prime among all primes (e.g. $p_{1} = 2, p_{2} = 3$). In particular, let $p_{0} = 1$.
-   $\operatorname{lpf}(n) := [1 < n] \min\{p : p \mid n\} + [1 = n]$, i.e. the smallest prime factor of $n$. In particular, when $n=1$, its value is $1$.
-   $F_{\mathrm{prime}}(n) := \sum_{2 \le p \le n} f(p)$
-   $F_{k}(n) := \sum_{i = 2}^{n} [p_{k} \le \operatorname{lpf}(i)] f(i)$

## Explanation

Observing the definition of $F_{k}(n)$, we can find that the answer is $F_{1}(n) + f(1) = F_{1}(n) + 1$.

Consider how to find $F_{k}(n)$. By enumerating the smallest prime factor of each $i$ and its exponent, we can obtain the recurrence:

$$
\begin{aligned}
    F_{k}(n)
    &= \sum_{i = 2}^{n} [p_{k} \le \operatorname{lpf}(i)] f(i) \\
    &= \sum_{\substack{k \le i \\ p_{i}^{2} \le n}} \sum_{\substack{c \ge 1 \\ p_{i}^{c} \le n}} f\left(p_{i}^{c}\right) ([c > 1] + F_{i + 1}\left(n / p_{i}^{c}\right)) + \sum_{\substack{k \le i \\ p_{i} \le n}} f(p_{i}) \\
    &= \sum_{\substack{k \le i \\ p_{i}^{2} \le n}} \sum_{\substack{c \ge 1 \\ p_{i}^{c} \le n}} f\left(p_{i}^{c}\right) ([c > 1] + F_{i + 1}\left(n / p_{i}^{c}\right)) + F_{\mathrm{prime}}(n) - F_{\mathrm{prime}}(p_{k - 1}) \\
    &= \sum_{\substack{k \le i \\ p_{i}^{2} \le n}} \sum_{\substack{c \ge 1 \\ p_{i}^{c + 1} \le n}} \left(f\left(p_{i}^{c}\right) F_{i + 1}\left(n / p_{i}^{c}\right) + f\left(p_{i}^{c + 1}\right)\right) + F_{\mathrm{prime}}(n) - F_{\mathrm{prime}}(p_{k - 1})
\end{aligned}
$$

The last step of the derivation is based on the following fact: for $c$ satisfying $p_{i}^{c} \le n < p_{i}^{c + 1}$, we have $p_{i}^{c + 1} > n \iff n / p_{i}^{c} < p_{i} < p_{i + 1}$, so $F_{i + 1}\left(n / p_{i}^{c}\right) = 0$.  
Its boundary value is $F_{k}(n) = 0 (p_{k} > n)$.

Assuming we have now found all $F_{\mathrm{prime}}(n)$, then there are two ways to find all $F_{k}(n)$:

1.  Compute directly according to the recurrence.
2.  Enumerate $p$ from large to small for the transition; the transition increment is nonzero only when $p^{2} < n$, so we can optimize with a suffix sum according to the recurrence.

Now consider how to compute $F_{\mathrm{prime}}{(n)}$.  
Observing the process of finding $F_{k}(n)$, it is easy to find that $F_{\mathrm{prime}}$ has useful point values only at the $O(\sqrt{n})$ points $1, 2, \dots, \left\lfloor\sqrt{n}\right\rfloor, n / \sqrt{n}, \dots, n / 2, n$.  
In general, $f(p)$ is a low-degree polynomial in $p$, which can be expressed as $f(p) = \sum a_{i} p^{c_{i}}$.  
Then for each $p^{c_{i}}$, its contribution to $F_{\mathrm{prime}}(n)$ is $a_{i} \sum_{2 \le p \le n} p^{c_{i}}$.  
Considering the contribution of each $p^{c_{i}}$ separately, the problem becomes: given $n, s, g(p) = p^{s}$, for all $m = n / i$, find $\sum_{p \le m} g(p)$.

???+ tip "Note"
    $g(p) = p^{s}$ is a completely multiplicative function!

So let $G_{k}(n) := \sum_{i = 2}^{n} \left[p_{k} < \operatorname{lpf}(i) \lor \operatorname{isprime}(i)\right] g(i)$, i.e. the sum of the $g$ values of the numbers remaining after the $k$-th round of the sieve of Eratosthenes.  
For a composite number $x \le n$, we must have $\operatorname{lpf}(x) \le \sqrt{x} \le \sqrt{n}$. Let $p_{\ell(n)}$ be the largest prime not greater than $\sqrt{n}$; then $\sum_{2\le p\le n}g(p) = G_{\ell(n)}(n)$, i.e. after $\ell$ rounds of the sieve of Eratosthenes, the remaining are all primes.
Consider the boundary value of $G$, which is obviously $G_{0}(n) = \sum_{i = 2}^{n} g(i)$. (Remember? We specially agreed that $p_{0} = 1$.)  
For the transition, consider the process of the sieve of Eratosthenes, and discuss the contribution of each part separately:

1.  For the part with $n < p_{k}^{2}$, the $G$ value is unchanged, i.e. $G_{k}(n) = G_{k - 1}(n)$.
2.  For the part with $p_{k}^{2} \le n$, the sieved-out numbers must have the prime factor $p_{k}$, i.e. $-g(p_{k}) G_{k - 1}(n / p_{k})$.
3.  For the second part, since $p_{k}^{2} \le n \iff p_{k} \le n / p_{k}$, the $i$ satisfying $\operatorname{lpf}(i) < p_{k}$ are additionally subtracted. This part should be added back, i.e. $g(p_{k}) G_{k - 1}(p_{k - 1})$.

Then we have:

$$
G_{k}(n) = G_{k - 1}(n) - \left[p_{k}^{2} \le n\right] g(p_{k}) (G_{k - 1}(n / p_{k}) - G_{k - 1}(p_{k - 1}))
$$

## Complexity analysis

For the computation of $F_{k}(n)$, the time complexity of the first method is proven to be $O\left(n^{1 - \epsilon}\right)$ (see Zhu Zhenting's national team training paper [《一些特殊的数论函数求和问题》](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2018%E8%AE%BA%E6%96%87%E9%9B%86.pdf) 2.3);  
for the second method, its essence is the second part of the Zhouge sieve, which is also mentioned in Ren Zhizhou's paper [《积性函数求和的几种方法》](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2016%E8%AE%BA%E6%96%87%E9%9B%86.pdf) (6.5.4), and its time complexity is proven to be $O\left(\frac{n^{\frac{3}{4}}}{\log{n}}\right)$.

For the computation of $F_{\mathrm{prime}}(n)$, in fact, its implementation is the same as the first part of the Zhouge sieve.  
Consider that for each $m = n / i$, only the transition when enumerating $p_{k}$ satisfying $p_{k}^{2} \le m$ contributes to the time complexity, so the time complexity can be estimated as:

$$
\begin{aligned}
    T(n)
    &= \sum_{i^{2} \le n} O\left(\pi\left(\sqrt{i}\right)\right) + \sum_{i^{2} \le n} O\left(\pi\left(\sqrt{\frac{n}{i}}\right)\right) \\
    &= \sum_{i^{2} \le n} O\left(\frac{\sqrt{i}}{\ln{\sqrt{i}}}\right) + \sum_{i^{2} \le n} O\left(\frac{\sqrt{\frac{n}{i}}}{\ln{\sqrt{\frac{n}{i}}}}\right) \\
    &= O\left(\int_{1}^{\sqrt{n}} \frac{\sqrt{\frac{n}{x}}}{\log{\sqrt{\frac{n}{x}}}} \mathrm{d} x\right) \\
    &= O\left(\frac{n^{\frac{3}{4}}}{\log{n}}\right)
\end{aligned}
$$

For the space complexity, we can find that whether it is $F_{k}$ or $F_{\mathrm{prime}}$, they only take effective point values at $n / i$, $O(\sqrt{n})$ in total, and recording only the effective values can optimize the space complexity to $O(\sqrt{n})$.

First, all effective values can be obtained through one round of number-theoretic block decomposition, recorded with an array $\text{lis}$ of size $O(\sqrt{n})$. For an effective value $v$, denote $\text{id}(v)$ as the index of $v$ in $\text{lis}$; it is easy to obtain: for all effective values $v$, $\text{id}(v) \le \sqrt{n}$.

Then consider separately the effective values less than or equal to $\sqrt{n}$ and the effective values greater than $\sqrt{n}$: for an effective value $v$ less than or equal to $\sqrt{n}$, record its $\text{id}(v)$ with an array $\text{le}$, i.e. $\text{le}_v = \text{id}(v)$; for an effective value $v$ greater than $\sqrt{n}$, record $\text{id}(v)$ with an array $\text{ge}$, and since $v$ is too large, we record $\text{id}(v)$ with the help of $v' = n / v < \sqrt{n}$, i.e. $\text{ge}_{v'} = \text{id}(v)$.

In this way, we can use two arrays of size $O(\sqrt{n})$ to record the $\text{id}$ of all effective values and query in $O(1)$. When computing $F_{k}$ or $F_{\mathrm{prime}}$, using the $\text{id}$ of an effective value instead of the effective value as the index optimizes the space complexity to $O(\sqrt{n})$.

## Process

For the computation of $F_{k}(n)$, when implementing we generally choose the first method, which has lower implementation difficulty and often performs better than the second method when the data scale is small;

For the computation of $F_{\mathrm{prime}}(n)$, simply implement directly according to the recurrence.

For $p_{k}^{2} \le n$, we can use a linear sieve to preprocess $s_{k} := F_{\mathrm{prime}}(p_{k})$ to replace $F_{\mathrm{prime}}(p_{k - 1})$ in the recurrence of $F_{k}$.  
Correspondingly, $G_{k - 1}(p_{k - 1}) = \sum_{i = 1}^{k - 1} g(p_{i})$ in the recurrence of $G$ can also be preprocessed using this method.

When using the Extended Eratosthenes Sieve to find the prefix sum of a **multiplicative function** $f$, the following points should be made clear:

-   How to quickly (generally in linear time complexity) sieve out the first $\sqrt{n}$ values of $f$;
-   The polynomial representation of $f(p)$;
-   How to quickly find $f(p^{c})$.

After clarifying the above points, implement the following parts in order:

1.  Sieve out the primes within $[1, \sqrt{n}]$ and the first $\sqrt{n}$ values of $f$;
2.  For each term in the polynomial representation of $f(p)$, sieve out the corresponding $G$, and merge to obtain all $O(\sqrt{n})$ useful point values of $F_{\mathrm{prime}}$;
3.  Implement the recursion according to the recurrence of $F_{k}$ to find $F_{1}(n)$.

## Example problems

???+ example "[Luogu P4213【模板】杜教筛](https://www.luogu.com.cn/problem/P4213)"
    Find $\displaystyle \sum_{i = 1}^{n} \varphi(i)$ and $\displaystyle \sum_{i = 1}^{n} \mu(i)$.

??? note "Solution"
    For finding the prefix sum of $\varphi(i)$, first it is easy to know that $f(p) = p - 1$. For the linear term $(p)$ of $f(p)$, we have $g(p) = p, G_{0}(n) = \sum_{i = 2}^{n} g(i) = \frac{(n + 2) (n - 1)}{2}$; for the constant term $(-1)$ of $f(p)$, we have $g(p) = -1, G_{0}(n) = \sum_{i = 2}^{n} g(i) = -n + 1$. Sieving twice and adding them gives all $O(\sqrt{n})$ required point values of $F_{\mathrm{prime}}$.
    
    For finding the prefix sum of $\mu(i)$, it is easy to know that $f(p) = -1$. Then $g(p) = -1, G_{0}(n) = \sum_{i = 2}^{n} g(i) = -n + 1$. Sieving directly gives all $O(\sqrt{n})$ required point values of $F_{\mathrm{prime}}$.

???+ example "[LOJ 6053 简单的函数](https://loj.ac/p/6053)"
    Given $f(n)$:
    
    $$
    f(n) = \begin{cases}
        1 & n = 1 \\
        p \operatorname{xor} c & n = p^{c} \\
        f(a)f(b) & n = ab \land a \perp b
    \end{cases}
    $$
    
    Find $\displaystyle \sum_{i = 1}^{n} f(i)$.

??? note "Solution"
    It is easy to know that $f(p) = p - 1 + 2[p = 2]$. Then sieve using the method for sieving $\varphi$, and discuss the case of $2$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/math/code/min-25/min-25_1.cpp"
    ```
