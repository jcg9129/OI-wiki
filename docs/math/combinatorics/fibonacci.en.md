The Fibonacci sequence ([OEIS A000045](http://oeis.org/A000045)) is defined as follows:

$$
F_0 = 0, F_1 = 1, F_n = F_{n-1} + F_{n-2}
$$

The first few terms of this sequence are:

$$
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, \dots
$$

## Lucas sequence

The Lucas sequence ([OEIS A000032](http://oeis.org/A000032)) is defined as follows:

$$
L_0 = 2, L_1 = 1, L_n = L_{n-1} + L_{n-2}
$$

The first few terms of this sequence are:

$$
2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, \dots
$$

In studying the Fibonacci sequence, it is often necessary to use the Lucas sequence as a tool.

## Closed-form formula for the Fibonacci sequence

The $n$-th Fibonacci number can be computed in $\Theta (n)$ time using the recurrence formula. But we still have faster methods to compute it.

### Analytic solution

The analytic solution is the formula solution. We have the closed-form formula (Binet's Formula) for the Fibonacci sequence:

$$
F_n = \frac{\left(\frac{1 + \sqrt{5}}{2}\right)^n - \left(\frac{1 - \sqrt{5}}{2}\right)^n}{\sqrt{5}}
$$

This formula can easily be proved by induction, and of course can also be derived through the concept of generating functions, or obtained by solving an equation.

Of course, you may notice that the second term in the numerator of this formula is always less than $1$, and it decreases at an exponential rate. Therefore we can write this formula as

$$
F_n = \left[\frac{\left(\frac{1 + \sqrt{5}}{2}\right)^n}{\sqrt{5}}\right]
$$

where the brackets denote taking the nearest integer.

These two formulas require extremely high precision when computing, so they are rarely used in practice. But please do not ignore them! Combined with the concepts of quadratic residues and inverses under a modulus, using this formula in OI is still useful.

### Closed-form formula for the Lucas sequence

We have the closed-form formula for the Lucas sequence:

$$
L_n = \left(\frac{1 + \sqrt{5}}{2}\right)^n + \left(\frac{1 - \sqrt{5}}{2}\right)^n
$$

very similar to the Fibonacci sequence. In fact:

$$
\frac{L_n + F_n\sqrt{5}}{2} = \left(\frac{1 + \sqrt{5}}{2}\right)^n
$$

That is, $L_n$ and $F_n$ are exactly the numerator coefficients after the binomial expansion of $\left(\frac{1 + \sqrt{5}}{2}\right)^n$ and combining like terms. That is, the set of all solutions of the Pell equation

$$
x^2-5y^2=-4
$$

is exactly

$$
\frac{x_n + y_n\sqrt{5}}{2} = \frac{L_n + F_n\sqrt{5}}{2}
$$

which is exactly the Lucas sequence and the Fibonacci sequence. Therefore we have

$$
{L_n}^2-5{F_n}^2=-4
$$

### Matrix form

The recurrence of the Fibonacci sequence can be expressed in the form of matrix multiplication:

$$
\begin{bmatrix}F_{n-1} & F_{n} \cr\end{bmatrix} = \begin{bmatrix}F_{n-2} & F_{n-1} \cr\end{bmatrix} \begin{bmatrix}0 & 1 \cr 1 & 1 \cr\end{bmatrix}
$$

Let $P = \begin{bmatrix}0 & 1 \cr 1 & 1 \cr\end{bmatrix}$; we obtain

$$
\begin{bmatrix}F_n & F_{n+1} \cr\end{bmatrix} = \begin{bmatrix}F_0 & F_1 \cr\end{bmatrix} P^n
$$

So we can use matrix multiplication to compute the Fibonacci sequence in $\Theta(\log n)$ time. In addition, the formula described in the previous section can also be obtained through the technique of matrix diagonalization.

### Fast doubling method

Using the above method we can obtain the following equalities:

$$
\begin{aligned}
F_{2k} &= F_k (2 F_{k+1} - F_{k}) \\
F_{2k+1} &= F_{k+1}^2 + F_{k}^2
\end{aligned}
$$

So we can quickly compute two adjacent Fibonacci numbers this way (with a smaller constant than matrix multiplication). The code is as follows; the return value is a pair $(F_n,F_{n+1})$.

```cpp
pair<int, int> fib(int n) {
  if (n == 0) return {0, 1};
  auto p = fib(n >> 1);
  int c = p.first * (2 * p.second - p.first);
  int d = p.first * p.first + p.second * p.second;
  if (n & 1)
    return {d, c + d};
  else
    return {c, d};
}
```

## Properties

The Fibonacci sequence has many interesting properties; here we list some of the simple ones:

1.  Cassini's identity: $F_{n-1} F_{n+1} - F_n^2 = (-1)^n$.
2.  Additive property: $F_{n+k} = F_k F_{n+1} + F_{k-1} F_n$.
3.  Taking $k = n$ in the previous property, we obtain $F_{2n} = F_n (F_{n+1} + F_{n-1})$.
4.  From the previous property one can prove by induction that $\forall k\in \mathbb{N},F_n|F_{nk}$.
5.  The above property is reversible, i.e. $\forall F_a|F_b,a|b$.
6.  GCD property: $(F_m, F_n) = F_{(m, n)}$.
7.  Using two adjacent terms of the Fibonacci sequence as input makes the Euclidean algorithm reach its worst-case complexity (see [Wikipedia - Lamé](https://en.wikipedia.org/wiki/Gabriel_Lam%C3%A9) for details).

### Relationship between the Fibonacci sequence and the Lucas sequence

It is not hard to find that the equalities about the Lucas sequence and the Fibonacci sequence have a high similarity to trigonometric formulas. For example:

$$
\frac{L_n + F_n\sqrt{5}}{2} = \left(\frac{1 + \sqrt{5}}{2}\right)^n
$$

is very similar to

$$
\cos nx + i\sin nx = \left(\cos x + i\sin x\right)^n
$$

And

$$
{L_n}^2-5{F_n}^2=-4
$$

is very similar to

$$
\cos^2 x + \sin^2 x = 1
$$

Therefore, the Lucas sequence is very similar to the cosine function, and the Fibonacci sequence is very similar to the sine function. For example, from

$$
\left(\frac{1 + \sqrt{5}}{2}\right)^m\left(\frac{1 + \sqrt{5}}{2}\right)^n = \left(\frac{1 + \sqrt{5}}{2}\right)^{m+n}
$$

we can obtain the equalities for the sum of two indices:

$$
2L_{m+n}=5F_mF_n+L_mL_n
$$

$$
2F_{m+n}=F_mL_n+L_mF_n
$$

Thus, as corollaries, we have the equalities for double indices:

$$
L_{2n}={L_n}^2-2{\left(-1\right)}^n
$$

$$
F_{2n}=F_nL_n
$$

This is also a way to quickly double the index. Similarly, one can also, in imitation of the trigonometric formulas, such as parity, sum-to-product, product-to-sum, half-angle, Weierstrass substitution, etc., deduce more corresponding equalities about the Lucas sequence and the Fibonacci sequence.

## Fibonacci coding

We can use the Fibonacci sequence to encode positive integers. By [Zeckendorf's theorem](https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem), any natural number $n$ can be uniquely represented as a sum of some Fibonacci numbers:

$$
N = F_{k_1} + F_{k_2} + \ldots + F_{k_r}
$$

and $k_1 \ge k_2 + 2,\ k_2 \ge k_3 + 2,\  \ldots,\  k_r \ge 2$ (i.e. two adjacent Fibonacci numbers cannot be used)

So we can use the code $d_0 d_1 d_2 \dots d_s 1$ to represent a positive integer, where $d_i=1$ indicates that $F_{i+2}$ is used. At the last bit of the code we forcibly add a 1 (so that two adjacent 1s appear), indicating that this string of code ends. Let us give a few examples:

$$
\begin{aligned}
1 &=& 1 &=& F_2 &=& (11)_F \\
2 &=& 2 &=& F_3 &=& (011)_F \\
6 &=& 5 + 1 &=& F_5 + F_2 &=& (10011)_F \\
8 &=& 8 &=& F_6 &=& (000011)_F \\
9 &=& 8 + 1 &=& F_6 + F_2 &=& (100011)_F \\
19 &=& 13 + 5 + 1 &=& F_7 + F_5 + F_2 &=& (1001011)_F
\end{aligned}
$$

The process of encoding $n$ can be solved using a greedy algorithm:

1.  Enumerate the Fibonacci numbers $F_i$ from large to small, until $F_i\le n$.
2.  Subtract $F_i$ from $n$, and place a 1 at position $i-2$ of the code (the code starts from 0 from left to right).
3.  If $n$ is positive, return to step 1.
4.  Finally, add a 1 at the last bit of the code, indicating the ending position of the code.

The decoding process is analogous: first delete the last 1, and for each position $i$ where the code is 1 (the code starts from 0 from left to right), accumulate an $F_{i+2}$ into the answer. The final answer is the original number.

## Periodicity under a modulus

For the Fibonacci sequence modulo $m$, one can easily prove using the pigeonhole principle that this sequence is periodic. Since the computation of each term of the Fibonacci numbers depends on the values of the previous two terms, we need to use a pair formed by adjacent Fibonacci numbers to describe the current state of the sequence. Consider the first $m^2+1$ Fibonacci pairs modulo $m$:

$$
(F_0,\ F_1),\ (F_1,\ F_2),\ \ldots,\ (F_{m^2},\ F_{m^2 + 1})
$$

The size of the residue system modulo $m$ is $m$, which means there can be at most $m^2$ mutually distinct pairs. Therefore, among the first $m^2+1$ pairs there must be two identical pairs, and from these two pairs the same Fibonacci sequence can be generated onward. Then, the Fibonacci sequence is periodic, and its (least positive) period does not exceed $m^2$.

### Pisano period

The least positive period of the Fibonacci sequence modulo $m$ is called the **Pisano period** ([OEIS A001175](http://oeis.org/A001175)). In this article we use $\pi(m)$ to denote the Pisano period modulo $m$.

This observation can be used to compute the value of the $n$-th Fibonacci number modulo $m$. If $n$ is very large, one needs to compute the period of the Fibonacci numbers modulo $m$. Of course, one only needs to compute a period, not necessarily the least positive period.

To this end, we have the following conclusions:

1.  For coprime moduli $m_1,m_2$, we have $\pi(m_1m_2)=\operatorname{lcm}(\pi(m_1),\pi(m_2))$.
2.  For a prime $p$ and a positive integer $e$, we have $\pi(p^{e})\mid p^{e-1}\pi(p)$.
3.  For $m=2^e~(e\in\mathbf N_+)$, we have $\pi(m)=3\cdot 2^{e-1}$.
4.  For $m=5^e~(e\in\mathbf N_+)$, we have $\pi(m)=4\cdot 5^e$.
5.  Finally, for a prime $p\equiv\pm1\pmod{10}$, we have $\pi(p)\mid(p-1)$; for a prime $p\equiv\pm3\pmod{10}$, we have $\pi(p)\mid 2(p+1)$.

Combining these cases, one can show that the Pisano period modulo $m$ does not exceed $6m$, with equality if and only if $m = 2\times 5^e~(e\in\mathbf N_+)$.

Using the above conclusions, based on a prime-factorization algorithm, one can obtain the following method for quickly computing the Pisano period:

??? example "Reference code"
    ```cpp
    --8<-- "docs/math/code/combinatorics/fibonacci/pisano_estimate.cpp:pisano"
    ```

The period obtained this way may only be a multiple of the Pisano period. To obtain the exact Pisano period, one can further examine the divisors of this period; or one can directly compute it in $O(\sqrt{m})$ time complexity via the [BSGS algorithm](../number-theory/discrete-logarithm.md#baby-step-giant-step-algorithm).

### Proof

Finally, this article briefly proves the above conclusions about the Pisano period. It is worth noting that, using the method described below, similar conclusions can be generalized to general second-order homogeneous linear recurrence sequences with constant coefficients. Although the specific constants differ, the Pisano periods of these sequences modulo $m$ are all $O(m)$.

The first observation is: using the [Chinese remainder theorem](../number-theory/crt.md), the discussion can be restricted to the case of prime-power moduli. Let $m_1,m_2$ be two coprime moduli. The period of the Fibonacci sequence modulo $m_1$ is $\pi(m_1)$ and its multiples, and modulo $m_2$ is $\pi(m_2)$ and its multiples, so its least positive period modulo $m_1m_2$ is exactly the least common multiple of $\pi(m_1)$ and $\pi(m_2)$. This is conclusion 1 above.

Another observation is: the Pisano period modulo $m$ is in fact the smallest positive integer $k$ such that

$$
A^k = \begin{pmatrix} 1&1\\1&0 \end{pmatrix}^k \equiv I \pmod{m}.
$$

That is, it is in fact the [order](../algebra/group-theory.md#order) of the matrix $A$ modulo $m$[^mod-m].

For the case of a prime-power modulus $m=p^e$, one can relate it to the corresponding prime-modulus case through the classic lifting-the-exponent argument. Let $k=\pi(p^e)$; then there exists a $2\times 2$ matrix $\Lambda$ such that

$$
A^k = p^e\Lambda + I 
$$

holds. Therefore, by the [binomial theorem](./combination.md#binomial-theorem), we know

$$
A^{kp} = (p^e\Lambda + I)^p = I + \sum_{i=1}^p\binom{p}{i}(p^e\Lambda)^i \equiv I\pmod{p^{e+1}}. 
$$

Therefore, by the [properties of order](../number-theory/primitive-root.md#幂的循环结构), we have $\pi(p^{e+1})\mid kp = p\pi(p^e)$. By induction on $e$, we know $\pi(p^e)\mid p^{e-1}\pi(p)$ always holds.

For the case of a prime modulus $p$, this article discusses two proof methods.

=== "Using the closed-form formula"
    One is to use the closed-form formula for the Fibonacci sequence:
    
    $$
    F_n = \dfrac{1}{\sqrt{5}}\left(\dfrac{1+\sqrt{5}}{2}\right)^n - \dfrac{1}{\sqrt{5}}\left(\dfrac{1-\sqrt{5}}{2}\right)^n.
    $$
    
    Expanding it using the binomial theorem and canceling the radical terms:
    
    $$
    F_n = \dfrac{1}{2^{n-1}}\sum_{i=0}^{\lfloor(n-1)/2\rfloor}\binom{n}{2i+1}5^i.
    $$
    
    For $p=2$, this expression cannot be taken modulo directly, but one can verify that the corresponding Pisano period is $\pi(2)=3$. For $p=5$, we have $F_n\equiv n\cdot 3^{n-1}\pmod{p}$, and one can directly verify that the corresponding Pisano period is $\pi(5)=20$. For the remaining odd prime moduli, we can divide into two cases:
    
    -   If $p\equiv 1,4\pmod{5}$, then
    
        $$
        \begin{aligned}
        F_{p} &\equiv \dfrac{1}{2^{p-1}}\binom{p}{p}5^{(p-1)/2} \equiv 1 \pmod{p},\\
        F_{p+1} &\equiv \dfrac{1}{2^p}\left(\binom{p+1}{1} + \binom{p+1}{p}5^{(p-1)/2}\right) \equiv 1 \pmod{p}.
        \end{aligned}
        $$
    
        In the simplification process, the following conclusions are used: by [Lucas's theorem](../number-theory/lucas.md), for $0 < k < p$ we have $\dbinom{p}{k}\equiv 0\pmod{p}$, and for $1 < k < p$ we have $\dbinom{p+1}{k}\equiv 0\pmod{p}$; by [Fermat's little theorem](../number-theory/fermat.md#fermats-little-theorem), we have $2^{p-1}\equiv 5^{p-1}\equiv 1\pmod{p}$; for $p\equiv 1,4\pmod{5}$, $p$ is a quadratic residue modulo $5$, and using [quadratic reciprocity](../number-theory/quad-residue.md#二次互反律), $5$ is also a quadratic residue modulo $p$, so $5^{(p-1)/2} \equiv 1\pmod{p}$. From this, we have $(F_p,F_{p+1}) \equiv (F_1,F_2) \pmod{p}$, so $(p-1)$ is a period modulo $p$. So $\pi(p)\mid(p-1)$.
    -   If $p\equiv 2,3\pmod{5}$, then
    
        $$
        \begin{aligned}
        F_{2p} &\equiv \dfrac{1}{2^{2p-1}}\binom{2p}{p}5^{(p-1)/2} \equiv -1 \pmod{p},\\
        F_{2p+1} &\equiv \dfrac{1}{2^{2p}}\left(\binom{2p+1}{1} + \binom{2p+1}{p}5^{(p-1)/2} + \binom{2p+1}{2p+1}5^p\right) \equiv -1\pmod{p}.
        \end{aligned}
        $$
    
        In the simplification process, the following conclusions are used: by Lucas's theorem, for $0 < k < p$ and $p < k < 2p$ we have $\dbinom{p}{k}\equiv 0\pmod{p}$, and $\dbinom{2p}{p}\equiv 2\pmod{p}$, while for $1 < k < p$ and $p + 1 < k < 2p$ we have $\dbinom{p}{k}\equiv 0\pmod{p}$, and $\dbinom{2p+1}{p}\equiv 2\pmod{p}$; by Fermat's little theorem, we have $2^{p-1}\equiv 5^{p-1}\equiv 1\pmod{p}$; for $p\equiv 2,3\pmod{5}$, $p$ is a quadratic non-residue modulo $5$, and using quadratic reciprocity, $5$ is also a quadratic non-residue modulo $p$, so $5^{(p-1)/2} \equiv -1\pmod{p}$. From this, we have $(F_{2p},F_{2p+1}) \equiv (F_{-2},F_{-1}) \pmod{p}$, so $2(p+1)$ is a period modulo $p$. So $\pi(p)\mid 2(p+1)$.
    
    This completes the proof. The limitation of this method is that it depends heavily on the closed-form formula of the Fibonacci sequence, so it is harder to directly generalize to the general case.

=== "Using a field extension"
    Another proof method attempts to directly compute the order of the matrix $A=\begin{pmatrix}1&1\\1&0\end{pmatrix}$. Its [characteristic polynomial](../linear-algebra/char-poly.md) is $f(x) = x^2-x-1$, with corresponding discriminant $\Delta = 5$. For modulus $p=5$, we have $\Delta\equiv 0\pmod{5}$, and the matrix $A$ has two identical eigenvalues $\lambda=3$ and cannot be diagonalized, so it needs to be computed separately. For modulus $p\equiv 1,4\pmod{5}$, by quadratic reciprocity the discriminant $\Delta=5$ is a quadratic residue modulo $p$, and the matrix $A$ has two distinct eigenvalues $\lambda_1\neq\lambda_2$ in the field $\mathbf F_p$; the order of the matrix $A$ is $\operatorname{lcm}(\operatorname{ord}(\lambda_1),\operatorname{ord}(\lambda_2))$, which must divide $|\mathbf F_p^\times|=p-1$. For modulus $p\equiv 2,3\pmod{5}$, by quadratic reciprocity the discriminant $\Delta=5$ is a quadratic non-residue modulo $p$, and the matrix $A$ has no eigenvalues in the field $\mathbf F_p$, but only in the [field extension](../algebra/field-theory.md#field-extensions) $\mathbf F_p[\sqrt{5}]$ does it have two distinct eigenvalues $\lambda_1\neq\lambda_2$; since the Frobenius endomorphism $x\mapsto x^p$ swaps the two roots, we have $\lambda_2=\lambda_1^p$, so $\lambda_1^{p+1}=\lambda_2^{p+1}=\lambda_1\lambda_2=-1$, i.e. $\lambda_1^{2(p+1)}=\lambda_2^{2(p+1)}=1$; from this, the order of the matrix $A$ is $\operatorname{lcm}(\operatorname{ord}(\lambda_1),\operatorname{ord}(\lambda_2))$, which must divide $2(p+1)$. This gives a conclusion consistent with the previous method.

In summary, for the different cases we correspondingly have:

-   $\pi(2^e)=\dfrac{3}{2}\cdot 2^e,~\dfrac{1}{4}\pi(5^e)=5^e$.
-   When $p\equiv\pm1\pmod{10}$, $\pi(p^e) \mid (p-1)p^{e-1}$, so $\pi(p^e)\le p^e$.
-   When $p\equiv\pm3\pmod{10}$, $\dfrac{1}{4}\pi(p^e) \mid \dfrac{p+1}{2}p^{e-1}$, so $\dfrac{1}{4}\pi(p^e)\le p^e$.

So, using conclusion 1, for a general modulus $m=\prod_i p_i^{e_i}$, we have

$$
\begin{aligned}
\pi(m)&=\operatorname{lcm}\{\pi(p_i^{e_i}):p_i\in\mathbf P\} \\
&\le \operatorname{lcm}\{\pi(p_i^{e_i}):p_i=2\text{ or }p_i\equiv\pm1~(\operatorname{mod}{10})\}\\
&\quad \cdot 4\cdot\operatorname{lcm}\{\pi(p_i^{e_i})/4:p_i=5\text{ or }p_i\equiv\pm3~(\operatorname{mod}{10})\}\\
&\le \prod\{\pi(p_i^{e_i}):p_i=2\text{ or }p_i\equiv\pm1~(\operatorname{mod}{10})\}\\
&\quad \cdot 4\cdot\prod\{\pi(p_i^{e_i})/4:p_i=5\text{ or }p_i\equiv\pm3~(\operatorname{mod}{10})\}\\
&\le \dfrac{3}{2}\cdot\prod\{p_i^{e_i}:p_i=2\text{ or }p_i\equiv\pm1~(\operatorname{mod}{10})\}\\
&\quad \cdot 4\cdot\prod\{p_i^{e_i}:p_i=5\text{ or }p_i\equiv\pm3~(\operatorname{mod}{10})\}\\
&= 6m.
\end{aligned}
$$

This shows that the Pisano period of the Fibonacci sequence modulo $m$ never exceeds $6m$, and equality is attained if and only if at $m=2\cdot 5^e$.

## Exercises

-   [SPOJ - Euclid Algorithm Revisited](http://www.spoj.com/problems/MAIN74/)
-   [SPOJ - Fibonacci Sum](http://www.spoj.com/problems/FIBOSUM/)
-   [HackerRank - Is Fibo](https://www.hackerrank.com/challenges/is-fibo/problem)
-   [Project Euler - Even Fibonacci numbers](https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem)
-   [Luogu P4000 斐波那契数列](https://www.luogu.com.cn/problem/P4000)

## References and notes

-   [Fibonacci sequence - Wikipedia](https://en.wikipedia.org/wiki/Fibonacci_sequence)
-   [Zeckendorf's theorem - Wikipedia](https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem)
-   [Pisano period - Wikipedia](https://en.wikipedia.org/wiki/Pisano_period)

**This page is mainly translated from the blog post [Числа Фибоначчи](http://e-maxx.ru/algo/fibonacci_numbers) and its English translation [Fibonacci Numbers](https://cp-algorithms.com/algebra/fibonacci-numbers.html). The Russian version is under the Public Domain + Leave a Link license; the English version is under the CC-BY-SA 4.0 license. The content has been modified.**

[^mod-m]: Strictly speaking, it is the order of the matrix $A$ in the general linear group $GL_2(\mathbf Z_m)$.
