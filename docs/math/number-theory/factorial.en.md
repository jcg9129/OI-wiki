author: aofall, c-forrest, CoelacanthusHex, Early0v0, Enter-tainer, Great-designer, iamtwz, Marcythm, Persdre, shuzhouliu, Tiphereth-A, wsyhb, Xeonacid

## Introduction

This article discusses conclusions related to factorial computation under a given modulus, and provides a computation method whose time complexity is linearly related to the size of the modulus, so this method is mainly applicable to the case where the modulus is not too large ($\sim 10^6$). In addition to the method introduced in this article, depending on the scenario, one can also apply [polynomial techniques](../poly/shift.md#模素数意义下阶乘) for fast computation.

According to the [Chinese Remainder Theorem](./crt.md), the factorial modulo problem can be transformed into the case where the modulus is a prime power $p^\alpha$. When handling such problems, one often needs, for a prime $p$ and a positive integer $n$, to extract all factors of $p$ from the factorial $n!$, thereby obtaining the decomposition:

$$
n! = p^{\nu_p(n!)}(n!)_p.
$$

Here, $\nu_p(n!)$ denotes the power of $p$ in the prime factorization of the factorial $n!$, and $(n!)_p$ denotes the integer obtained by removing all powers of $p$ from the result of the factorial $n!$. This article will discuss the remainder of $(n!)_p$ modulo a prime (power) as well as the specific computation method for the power $\nu_p(n!)$.

This decomposition is especially useful when solving problems where factorials appear simultaneously in the numerator and denominator of the desired expression, such as [computing binomial coefficients under a given modulus](./lucas.md). For such problems, the power of $p$ in the numerator and denominator can be directly subtracted, while the part $(n!)_p$ coprime with $p$ can be computed using the [modular multiplicative inverse](./inverse.md).

This article also introduces content related to the above problems, such as Wilson's theorem and its generalization, Legendre's formula, and Kummer's theorem.

## Wilson's theorem

Wilson's theorem gives a necessary and sufficient condition for judging whether a natural number is prime.

???+ note "Wilson's theorem"
    For a natural number $n>1$, $(n-1)!\equiv -1\pmod n$ if and only if $n$ is prime.

??? note "Proof"
    First, prove that for a prime $p$ we have $(p-1)!\equiv -1\pmod{p}$. For this, one can obtain two concise proofs using the [congruence equation](./congruence-equation.md#corollary-2) or the [primitive root](./primitive-root.md), which are omitted here. Below we provide a proof method with fewer prerequisites:
    
    When $p=2$, the proposition obviously holds. Below let $p\geq 3$; then we need to prove that the product of all nonzero elements (i.e. congruence classes) in $\mathbf{Z}_p$ is $\overline{-1}$. Because every nonzero element $\overline{a}$ in $\mathbf{Z}_p$ has an inverse $\overline{a}^{-1}$, the product of mutually inverse elements in $\mathbf{Z}_p$ is $\overline{1}$. But note that $\overline{a}$ and $\overline{a}^{-1}$ may be equal: $\overline{a}=\overline{a}^{-1}$ if and only if $a^2\equiv 1\pmod p$, i.e.
    
    $$
    0\equiv a^2-1\equiv (a+1)(a-1),\pmod p
    $$
    
    so $a\equiv 1\pmod p$ or $a\equiv -1\pmod p$. This shows that the product of all elements in $\mathbf{Z}_p\setminus\{\overline{0},\overline{1},\overline{-1}\}$ is $\overline{1}$, and thus the product of all nonzero elements in $\mathbf{Z}_p$ is $\overline{-1}$.
    
    Conversely, for the case of a composite number $n$, we need to prove $(n-1)!\not\equiv-1\pmod{n}$. Using proof by contradiction, suppose $(n-1)!\equiv -1\pmod{n}$, i.e. there exists an integer $k$ such that $(n-1)!=kn-1$ holds. Because $n$ is composite, there must exist a prime $p<n$ such that $n=pm$, so $(n-1)!=kpm-1\equiv -1\pmod{p}$. But the product $(n-1)!$ must already contain $p$, so we must have $(n-1)!\equiv 0\pmod{p}$. This contradiction shows that $(n-1)!\not\equiv-1\pmod{n}$.

Using the notation of this article, Wilson's theorem can be written as $(p!)_p\equiv -1\pmod{p}$.

### Generalization

Wilson's theorem can be generalized to the case of a general modulus.

???+ note "Theorem (Gauss)"
    For a natural number $m>1$, we have
    
    $$
    \prod_{1\le k<m,\ k\perp m} k \equiv \pm 1 \pmod{m}.
    $$
    
    Moreover, the $\pm 1$ in the remainder takes the value $-1$ if and only if a [primitive root exists](./primitive-root.md#原根存在定理) modulo $m$, i.e. when $m=2,4,p^\alpha,2p^\alpha$, where $p$ is an odd prime and $\alpha$ is a positive integer.

??? note "Proof"
    This theorem can be proved simply through the structure of the [multiplicative group of integers modulo $n$](../algebra/ring-theory.md#application-the-multiplicative-group-of-integer-congruence-classes). Here we give a proof with a similar idea but more elementary.
    
    For the case $m=2$, we have $1!=1\equiv -1\pmod{2}$. For other cases where a primitive root exists, let the primitive root be $g$; then every positive integer $k$ less than $m$ and coprime with it can be uniquely represented in the form $g^i\bmod m$, where $0\le i<\varphi(m)$ and $\varphi(m)$ is the [Euler's totient function](./euler-totient.md). Direct verification shows that $\varphi(m)$ must be even. Because $g^i$ and $g^{\varphi(m)-i}$ are mutual multiplicative inverses, pairing them up in the product gives
    
    $$
    \prod_{1\le k<m,\ k\perp m} k \equiv \prod_{i=0}^{\varphi(m)-1}g^i = g^{\varphi(m)/2}\prod_{i=1}^{\varphi(m)/2-1}g^{i}g^{\varphi(m)-i} \equiv g^{\varphi(m)/2} \pmod{m}.
    $$
    
    Because $g^{\varphi(m)/2}\bmod m$ is the unique element not equal to $1\bmod{m}$ whose multiplicative inverse is itself, it equals $-1\bmod{m}$. This shows that the remainder in this case equals $-1$.
    
    For the case where a primitive root modulo $m$ does not exist, we need to prove that the remainder equals $1$. To this end, we can first do the prime factorization $m=p_1^{e_1}p_2^{e_2}\cdots p_s^{e_s}$, and then applying the [Chinese Remainder Theorem](./crt.md), we only need to prove
    
    $$
    \prod_{1\le k<m,\ k\perp m} k\equiv 1\pmod{p_j^{e_j}}
    $$
    
    holds for all factors $p_j^{e_j}$. The Chinese Remainder Theorem shows that every possible remainder combination $(r_1,r_2,\cdots,r_s)$, where $1\le r_j<p_j^{e_j}$ and $p_j\perp r_j$, uniquely corresponds to a $1\le k<m$ with $k\perp m$ such that $k\equiv r_j\pmod{p_j^{e_j}}$ holds. So, for a given remainder $r_j$, there are exactly ${\varphi(m)}/{\varphi(p_j^{e_j})}$ values of $k$ such that $k\equiv r_j\pmod{p_j^{e_j}}$ holds. Using this, we can group the product, obtaining
    
    $$
    \prod_{1\le k<m,\ k\perp m} k\equiv\left(\prod_{1\le r_j<p_j^{e_j},\ r_j\perp p_j} r_j\right)^{{\varphi(m)}/{\varphi(p_j^{e_j})}}\pmod{p_j^{e_j}}.
    $$
    
    For the exponent ${\varphi(m)}/{\varphi(p_j^{e_j})}=\varphi(m/p_j^{e_j})$ here to be odd, we must have $m/p_j^{e_j}=1,2$, because Euler's totient function $\varphi(n)$ is even for all $n\ge 3$. If $p_j$ is an odd prime, because a primitive root modulo $m$ does not exist, we must have $m/p_j^{e_j}\neq 1,2$; if $p_j^{e_j}=2,4$, because a primitive root modulo $m$ does not exist, $m/p_j^{e_j}$ must contain some odd prime factor and hence is greater than $2$: in these two cases the exponent ${\varphi(m)}/{\varphi(p_j^{e_j})}$ is even. And the term inside the parentheses in the above expression has already been proven to be $\equiv -1\pmod{p_j^{e_j}}$, so the remainder of this power modulo $p_j^{e_j}$ must be $1$. The only remaining case is when $p_j=2$ and $e_j>2$; for this case, we can directly prove \`
    
    $$
    \prod_{1\le r_j<2^{e_j},\ r_j\perp 2}r_j \equiv 1\pmod{2^{e_j}}.
    $$
    
    Following the proof idea above, we can pair up and cancel all odd numbers $r_j$ with $1\le r_j<2^{e_j}$; those that cannot be paired must be solutions of the equation $x^2\equiv 1\pmod{2^{e_j}}$. This equation means $2^{e_j}\mid (x-1)(x+1)$. Let $x=2y+1$; then we must have $2^{e_j-2}\mid y(y+1)$, and $y$ and $y+1$ must be one odd and one even, so $y=t2^{e_j-2}$ or $y=t2^{e_j-2}-1$. Therefore, $x=t2^{e_j-1}\pm 1$ with $t$ an integer. Among the remainders modulo $2^{e_j}$, there are only the four values $\pm 1$ and $2^{e_j-1}\pm 1$. Therefore, we have
    
    $$
    \prod_{1\le r_j<2^{e_j},\ r_j\perp 2}r_j \equiv (-1)(2^{e_j-1}-1)(2^{e_j-1}+1) \equiv 1\pmod{2^{e_j}}.
    $$
    
    This completes the proof of all cases.

In computation, the case where the modulus is a prime power is especially important:

???+ note "Corollary"
    For a prime $p$ and a positive integer $\alpha$, we have
    
    $$
    \prod_{1\le k<p^\alpha,\ k\perp p}k \equiv 
    \begin{cases}
    1, & p=2\text{ and }\alpha\ge3,\\
    -1, &\text{otherwise}
    \end{cases}
    \pmod{p^\alpha}.
    $$

Note that the left side is not $(p^\alpha!)_p$, because the latter also needs to count the contribution of the multiples of $p$.

## Computation of the factorial remainder

This section discusses the computation of the remainder $(n!)_p\bmod p^{\alpha}$.

### The case of a prime modulus

The expression $(n!)_p$ has an obvious recursive structure. To notice this, first examine a specific example:

???+ example "Example"
    To compute $(32!)_5 \bmod{5}$, we can do the following recursive computation:
    
    $$
    \begin{aligned}
    (32!)_5 &= 1\times 2\times 3 \times 4\times \underbrace{1}_{5}\times 6 \times 7 \times 8\times 9 \times \underbrace{2}_{10} \\
    &\quad\times 11 \times 12 \times 13 \times 14\times \underbrace{3}_{15}\times 16 \times 17\times 18\times 19\times \underbrace{4}_{20} \\
    &\quad\times 21 \times 22 \times 23 \times 24\times \underbrace{1}_{25}\times 26 \times 27\times 28\times 29\times \underbrace{6}_{30} \times 31 \times 32 \\
    &\equiv 1\times 2\times 3 \times 4\times \underbrace{1}_{5}\times 1 \times 2 \times 3\times 4 \times \underbrace{2}_{10} \\
    &\quad\times 1 \times 2 \times 3 \times 4\times \underbrace{3}_{15}\times 1 \times 2\times 3\times 4\times \underbrace{4}_{20} \\
    &\quad\times 1 \times 2 \times 3 \times 4\times \underbrace{1}_{25}\times 1 \times 2\times 3\times 4\times \underbrace{1}_{30}\times 1\times 2\\
    &= (1\times 2\times 3\times 4)^{6}\times(1\times 2)\times(\underbrace{1}_{5}\times \underbrace{2}_{10}\times \underbrace{3}_{15} \times \underbrace{4}_{20}\times \underbrace{1}_{25}\times \underbrace{1}_{30}) \pmod{5}
    \end{aligned}
    $$
    
    It can be seen that using the periodicity of the remainders modulo $5$, this product can be divided into several blocks of length $5$, where the only difference in each block is the remainder of the last element. Because dividing $32$ by $5$ gives a quotient of $6$ and a remainder of $2$, this product can be divided into $6$ complete blocks and a final incomplete block of length $2$. Therefore, we can extract the part of the first $6$ blocks except the last element (this part is exactly what Wilson's theorem can solve), then multiply by the product of the last incomplete block, and finally multiply by the running product of the last elements of the first $6$ blocks. The last element of each block is a multiple of $5$; after removing the powers of $5$, their running product is exactly $(6!)_{5}\pmod{5}$. This transforms the original problem into a smaller-scale problem.

Generalizing the recursive structure in this example, we obtain the following recurrence formula:

???+ note "Recurrence formula"
    For a prime $p$ and a positive integer $n$, we have
    
    $$
    (n!)_p \equiv (-1)^{\left\lfloor n/p\right\rfloor}\cdot (n\bmod p)!\cdot\left(\left\lfloor n/p\right\rfloor!\right)_p\pmod{p}.
    $$

??? note "Proof"
    Denote $(n)_p$ as the result of removing all powers of $p$ from the prime factorization of $n$. Then, we have
    
    $$
    \begin{aligned}
    (n!)_p &= \prod_{k=1}^n(k)_p = \left(\prod_{1\le k\le n,\ k\perp p}(k)_p\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(pk)_p\right) \\
    &= \left(\prod_{i=0}^{\lfloor n/p\rfloor-1}\prod_{j=1}^{p-1}(ip+j)\right)\left(\prod_{j=1}^{n\bmod p}(\lfloor n/p\rfloor p+j)\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(k)_p\right) \\
    &\equiv\left(\prod_{j=1}^{p-1}j\right)^{\lfloor n/p\rfloor}\left(\prod_{j=1}^{n\bmod p}j\right)(\lfloor n/p\rfloor!)_p \\
    &\equiv (-1)^{\lfloor n/p\rfloor}\cdot(n\bmod p)!\cdot(\lfloor n/p\rfloor!)_p \pmod p.
    \end{aligned}
    $$
    
    This completes the proof. Below we provide a concrete explanation of this formal proof.
    
    To compute the value of $(n!)_p\bmod p$. Following the example above, we have
    
    $$
    \begin{aligned}
    (n!)_p &= 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot \underbrace{1}_{p} \cdot (p+1) \cdot (p+2) \cdot \ldots \cdot (2p-1) \cdot \underbrace{2}_{2p} \\
    &\quad \cdot (2p+1) \cdot \ldots \cdot (p^2-1) \cdot \underbrace{1}_{p^2} \cdot (p^2 +1) \cdot \ldots \cdot n \pmod{p} \\
    &= 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot \underbrace{1}_{p} \cdot 1 \cdot 2 \cdot \ldots \cdot (p-1) \cdot \underbrace{2}_{2p} \cdot 1 \cdot 2 \\
    &\quad \cdot \ldots \cdot (p-1) \cdot \underbrace{1}_{p^2} \cdot 1 \cdot 2 \cdot \ldots \cdot (n \bmod p) \pmod{p}.
    \end{aligned}
    $$
    
    It can be clearly seen that, except for the last block, the factorial is divided into several complete blocks of the same length.
    
    $$
    \begin{aligned}
    (n!)_p&= \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 1}_{1\text{st}} \cdot \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 2}_{2\text{nd}} \cdot \ldots \\
    &\quad \cdot \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 1}_{p\text{th}} \cdot \ldots \cdot \quad \underbrace{1 \cdot 2 \cdot \cdot \ldots \cdot (n \bmod p)}_{\text{tail}} \pmod{p}.
    \end{aligned}
    $$
    
    Except for the last element of the block, the main part $(p-1)!\ \mathrm{mod}\ p$ of the complete block is easy to compute, and Wilson's theorem can be applied:
    
    $$
    (p-1)!\equiv -1\pmod p.
    $$
    
    There are $\left\lfloor \dfrac{n}{p} \right\rfloor$ complete blocks in total, so we need to write $\left\lfloor \dfrac{n}{p} \right\rfloor$ as the exponent of $-1$.
    
    The value of the last partial block is exactly $(n\bmod p)!\bmod p$, which can be computed separately.
    
    The rest is the last element of each block. If we hide the already-processed elements, we can see the following pattern:
    
    $$
    (n!)_p = \underbrace{ \ldots \cdot 1 } \cdot \underbrace{ \ldots \cdot 2} \cdot \ldots \cdot \underbrace{ \ldots \cdot (p-1)} \cdot \underbrace{ \ldots \cdot 1 } \cdot \underbrace{ \ldots \cdot 1} \cdot \underbrace{ \ldots \cdot 2} \cdots
    $$
    
    This is also a modified factorial, only much shorter. It is:
    
    $$
    \left(\left\lfloor \frac{n}{p} \right\rfloor !\right)_p.
    $$
    
    Multiplying the parts together gives the recurrence formula above.

Using this recurrence for computation, the recursion depth is $O(\log_p n)$. If we recompute the middle term each time, then the complexity of each level of computation is $O(p)$, and the total time complexity is $O(p\log_p n)$; if we preprocess $n!\bmod p$ for all $n=1,2,\cdots,p-1$, then the preprocessing complexity is $O(p)$, the complexity of each level of computation is $O(1)$, and the total time complexity is $O(p+\log_p n)$.

In the implementation, because it is tail recursion, it can be implemented iteratively. The implementation below precomputes the first $p-1$ factorials; if it needs to be called multiple times, the precomputation can be done outside the function.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/factorial/fact-mod-p.cpp:core"
    ```

If space is limited and it is impossible to store all factorials, one can also compute all the $n$ in the factorials $n!\bmod p$ actually used in the function calls, then sort them, so that these factorial values can be computed all at once at the end and aggregated into the final result, thereby avoiding storing all factorial values.

### The case of a prime power modulus

For the case of a prime power modulus, it can be solved following the case of a prime modulus, only needing to replace Wilson's theorem with its generalized form. The $\pm 1$ in the two conclusions of this section both specifically refer to this definition: it takes $1$ when the modulus $p=2$ and $\alpha\ge 3$, and $-1$ in all other cases.

???+ note "Recurrence formula"
    For a prime $p$ and positive integers $\alpha,n$, we have
    
    $$
    (n!)_{p} \equiv (\pm 1)^{\lfloor n/p^\alpha\rfloor}\cdot\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}j\right)\cdot(\lfloor n/p\rfloor!)_p\pmod{p^\alpha}.
    $$
    
    Here, the value of $\pm 1$ is as specified in the [generalization of Wilson's theorem](#generalization).

??? note "Proof"
    The proof idea is entirely consistent with the case of a prime modulus. Denote $(k)_p$ as the result of removing all powers of $p$ from the prime factorization of $k$; then
    
    $$
    \begin{aligned}
    (n!)_p
    &= \prod_{1\le k\le n}(k)_p = \left(\prod_{1\le k\le n,\ k\perp p}(k)_p\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(pk)_p\right) \\
    &= \left(\prod_{i=0}^{\lfloor n/p^\alpha\rfloor-1}\prod_{1\le j\le p^\alpha,\ j\perp p}(ip^\alpha+j)_p\right)\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}(\lfloor n/p^\alpha\rfloor p^\alpha+j)_p\right)\left(\prod_{1\le k\le\lfloor n/p\rfloor}(k)_p\right)\\
    &\equiv \left(\prod_{1\le j\le p^\alpha,\ j\perp p}j\right)^{\lfloor n/p^\alpha\rfloor}\cdot\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}j\right)\cdot(\lfloor n/p\rfloor!)_p\\
    &\equiv (\pm 1)^{\lfloor n/p^\alpha\rfloor}\cdot\left(\prod_{1\le j\le (n\bmod p^\alpha),\ j\perp p}j\right)\cdot(\lfloor n/p\rfloor!)_p \pmod{p^\alpha}.
    \end{aligned}
    $$

The differences from the case of a prime modulus, besides the fact that $-1$ may need to be replaced by $\pm 1$, also include the need to note the difference in the preprocessed data. For the case of a prime power modulus, we need to preprocess, for all positive integers $n$ not exceeding $p^\alpha$, the product of all integers from $1$ to $n$ that are not multiples of $p$, i.e.

$$
\prod_{1\le k\le n,\ k\perp p} k\bmod{p^\alpha}.
$$

In the case of a prime modulus, it degenerates to $n!\bmod p$, but this expression is no longer applicable in the general prime power case.

Below we provide an example of computing the factorial remainder in the case of a prime power modulus, to help understand the above method:

???+ example "Example"
    To compute $(32!)_3\bmod 9$, we can do the following recursive computation:
    
    $$
    \begin{aligned}
    (32!)_3 
    &= 1\times 2\times \underbrace{1}_{3} \times 4\times 5\times \underbrace{2}_{6}\times 7\times 8\times\underbrace{1}_{9}\\
    &\quad\times 10\times 11\times\underbrace{4}_{12}\times 13\times 14\times\underbrace{5}_{15}\times 16\times 17\times\underbrace{2}_{18}\\
    &\quad\times 19\times 20\times\underbrace{7}_{21}\times 22\times 23\times\underbrace{8}_{24}\times 25\times 26\times\underbrace{1}_{27}\\
    &\quad\times 28\times 29\times\underbrace{10}_{30}\times 31\times 32\\
    &\equiv 1\times 2\times \underbrace{1}_{3} \times 4\times 5\times \underbrace{2}_{6}\times 7\times 8\times\underbrace{1}_{9}\\
    &\quad\times 1\times 2\times\underbrace{4}_{12}\times 4\times 5\times\underbrace{5}_{15}\times 7\times 8\times\underbrace{2}_{18}\\
    &\quad\times 1\times 2\times\underbrace{7}_{21}\times 4\times 5\times\underbrace{8}_{24}\times 7\times 8\times\underbrace{1}_{27}\\
    &\quad\times 1\times 2\times\underbrace{1}_{30}\times 4\times 5\\
    &=(1\times 2\times 4\times 5\times 7\times 8)^{3}\times (1\times 2\times 4\times 5)\\
    &\quad\times\begin{pmatrix}\underbrace{1}_{3}\times\underbrace{2}_{6}\times\underbrace{1}_{9}\times\underbrace{4}_{12}\times\underbrace{5}_{15}\times\underbrace{2}_{18}\\\times\underbrace{7}_{21}\times\underbrace{8}_{24}\times\underbrace{1}_{27}\times\underbrace{1}_{30}\end{pmatrix}\pmod{9}.
    \end{aligned}
    $$
    
    The result of decomposing the expression $(32!)_3\bmod 9$ can likewise be divided into three parts:
    
    -   Complete blocks: the product of all integers between $1\sim 9$ that are not divisible by $3$, $\lfloor 32/9\rfloor=3$ blocks in total;
    -   The tail incomplete block: all integers not divisible by $3$ multiplied from $1$ all the way to $32\bmod 9$;
    -   The product of all integers divisible by $3$; comparing with the result of the second-to-last equality, this is exactly its first $\lfloor 32/3\rfloor=10$ terms, i.e. $(\lfloor 32/3\rfloor!)_3\bmod 9$.
    
    Simply solve the last parenthesis recursively; this transforms the original problem into a smaller problem.

From this, we can obtain the following recursive result:

???+ note "Recursive result"
    For a prime $p$ and positive integers $\alpha,n$, we have
    
    $$
    (n!)_p \equiv (\pm 1)^{\sum_{j\ge\alpha}\lfloor{n}/{p^j}\rfloor}\prod_{j\ge 0}F(\lfloor n/p^j\rfloor\bmod p^\alpha),
    $$
    
    where $F(m) = \prod_{1\le k\le m,\ k\perp p} k\bmod{p^\alpha}$ and the value of $\pm 1$ is the same as described above.

The implementation of the prime power modulus case is similar to the prime modulus case, only with some differences in details. Similar to the above, the preprocessing can also be done outside the function.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/factorial/fact-mod-pa.cpp:core"
    ```

The time complexity of preprocessing is $O(p^\alpha)$, and the time complexity of a single query is $O(\log_p n)$.

## Computation of the power

This section discusses the computation of the power $\nu_p(n!)$ of $p$ in the factorial $n!$, which can be used to compute the remainder of binomial coefficients. Because in a binomial coefficient, factorials appear in both the numerator and the denominator, whether the prime $p$ in the numerator and denominator can cancel each other becomes an important factor determining the final remainder.

### Legendre's formula

The power of the prime $p$ in the factorial $n!$ can be computed via Legendre's formula, and is related to the representation of $n$ in base $p$.

???+ note "Legendre's formula"
    For a positive integer $n$, the power $\nu_p(n!)$ of the prime $p$ contained in the factorial $n!$ is
    
    $$
    \nu_p(n!) = \sum_{i=1}^{\infty} \left\lfloor \dfrac{n}{p^i} \right\rfloor = \dfrac{n-S_p(n)}{p-1},
    $$
    
    where $S_p(n)$ is the sum of the digits of $n$ in base $p$. In particular, the power of $2$ in the factorial is $\nu_2(n!)=n-S_2(n)$.

??? note "Proof"
    Because
    
    $$
    n! = 1\times 2\times \cdots \times p\times \cdots \times 2p\times \cdots \times \lfloor n/p\rfloor p\times \cdots \times n.
    $$
    
    Here, the product of the multiples of $p$ is $p\times 2p\times \cdots \times \lfloor n/p\rfloor p=p^{\lfloor n/p\rfloor }\lfloor n/p\rfloor !$, and $\lfloor n/p\rfloor !$ may continue to contain multiples of $p$. So, for the power, we have the recurrence relation:
    
    $$
    \nu_p(n!) = \lfloor n/p\rfloor + \nu_p(\lfloor n/p\rfloor!).
    $$
    
    Expanding it gives Legendre's formula.
    
    To prove the second equality, first expand $n$ in base $p$, which amounts to writing it as the following sum:
    
    $$
    n = n_\ell p^{\ell} + \cdots + n_1 p + n_0 = \sum_{k=0}^\ell n_kp^k.
    $$
    
    Therefore, we have
    
    $$
    \begin{aligned}
    \nu_p(n!)
    &= \sum_{i=1}^{\ell}\left\lfloor\dfrac{n}{p^i}\right\rfloor 
    = \sum_{i=1}^\ell\sum_{k=i}^{\ell}n_kp^{k-i}
    = \sum_{k=1}^\ell n_k\sum_{i=1}^kp^{k-i} \\
    &= \sum_{k=1}^\ell n_k\dfrac{p^k-1}{p-1} 
    = \dfrac{\sum_{k=0}^\ell n_kp^k - \sum_{k=0}^\ell n_k}{p-1} 
    = \dfrac{n - S_p(n)}{p-1}.
    \end{aligned}
    $$

A reference implementation for finding the power of a prime in a factorial is as follows:

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/factorial/multiplicity.cpp:core"
    ```

Its time complexity is $O(\log n)$.

### Kummer's theorem

The result of taking a binomial coefficient modulo a number often forms a fractal structure; for example, the Sierpiński triangle can be obtained from binomial coefficients modulo $2$.

If analyzed carefully, whether $p$ divides a binomial coefficient is actually related to whether the subtraction of the upper and lower indices in base $p$ requires borrowing. This gives **Kummer's theorem**.

???+ note "Kummer's theorem"
    The power of the prime $p$ in the binomial coefficient $\dbinom{m}{n}$ is exactly the number of borrows needed when subtracting $n$ from $m$ in base $p$, i.e.
    
    $$
    \nu_p\left(\dbinom{m}{n}\right)=\frac{S_p(n)+S_p(m-n)-S_p(m)}{p-1}.
    $$
    
    In particular, the power of $2$ in the binomial coefficient is $\nu_2\left(\dbinom{m}{n}\right)=S_2(n)+S_2(m-n)-S_2(m)$.

??? note "Proof"
    First prove the following expression. To this end, using Legendre's formula, we have
    
    $$
    \begin{aligned}
    \nu_p\left(\dbinom{m}{n}\right)
    &=\nu_p(m!)-\nu_p(n!)-\nu_p((m-n)!)\\
    &=\sum_{i=1}^\infty\left(\left\lfloor\dfrac{m}{p^i}\right\rfloor-\left\lfloor\dfrac{n}{p^i}\right\rfloor-\left\lfloor\dfrac{m-n}{p^i}\right\rfloor\right)\\
    &=\frac{S_p(n)+S_p(m-n)-S_p(m)}{p-1}.
    \end{aligned}
    $$
    
    This expression can be understood as the number of borrows needed when subtracting $n$ from $m$ in base $p$. Because if there is a case of insufficiency requiring a borrow when computing the $i$-th digit (the lowest digit has index $1$), then the digits before the $i$-th digit in the subtraction result, $\left\lfloor\dfrac{m-n}{p^i}\right\rfloor$, are actually the digits before the $i$-th digit in $m$, $\left\lfloor\dfrac{m}{p^i}\right\rfloor$, minus one (i.e. the borrowed one), minus the digits before the $i$-th digit in $n$, $\left\lfloor\dfrac{n}{p^i}\right\rfloor$, so the difference
    
    $$
    \left\lfloor\dfrac{m}{p^i}\right\rfloor-\left\lfloor\dfrac{n}{p^i}\right\rfloor-\left\lfloor\dfrac{m-n}{p^i}\right\rfloor = 1
    $$
    
    if and only if a borrow occurred; otherwise, this difference is $0$. Therefore, the summation in the above expression can be understood as the number of times a borrow occurs. This gives the verbal statement of Kummer's theorem.

## Example problems

???+ example "Example [HDU 2973 - YAPTCHA](https://acm.hdu.edu.cn/showproblem.php?pid=2973)"
    Given $n$, compute
    
    $$
    \sum_{k=1}^n\left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor
    $$

??? note "Solution idea"
    If $3k+7$ is prime, then
    
    $$
    (3k+6)!\equiv-1\pmod{3k+7}
    $$
    
    Let $(3k+6)!+1=k(3k+7)$
    
    then
    
    $$
    \left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor=\left\lfloor k-\left\lfloor k-\frac{1}{3k+7}\right\rfloor\right\rfloor=1
    $$
    
    If $3k+7$ is not prime, then $(3k+7)\mid(3k+6)!$, i.e.
    
    $$
    (3k+6)!\equiv 0\pmod{3k+7}
    $$
    
    Let $(3k+6)!=k(3k+7)$; then
    
    $$
    \left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor=\left\lfloor k+\frac{1}{3k+7}-k\right\rfloor=0
    $$
    
    Therefore
    
    $$
    \sum_{k=1}^n\left\lfloor\frac{(3k+6)!+1}{3k+7}-\left\lfloor\frac{(3k+6)!}{3k+7}\right\rfloor\right\rfloor=\sum_{k=1}^n[3k+7\text{ is prime}]
    $$

??? example "Reference code"
    ```cpp
    --8<-- "docs/math/code/factorial/wilson_1.cpp"
    ```

## References

-   冯克勤．《初等数论及其应用》．
-   [Wilson's theorem - Wikipedia](https://en.wikipedia.org/wiki/Wilson%27s_theorem)
-   [Legendre's formula - Wikipedia](https://en.wikipedia.org/wiki/Legendre%27s_formula)

**This page is mainly translated from the blog post [Вычисление факториала по модулю](http://e-maxx.ru/algo/modular_factorial) and its English translation [Factorial modulo p](https://cp-algorithms.com/algebra/factorial-modulo.html). The Russian version is under the Public Domain + Leave a Link license; the English version is under the CC-BY-SA 4.0 license. The content has been modified.**
