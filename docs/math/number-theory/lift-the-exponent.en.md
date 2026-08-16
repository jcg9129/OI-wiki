## Content

The Lift the Exponent (LTE) lemma is a theorem that is relatively commonly used in elementary number theory.

Define $\nu_p(n)$ as the power of the prime factor $p$ in the standard factorization of the integer $n$, i.e. $\nu_p(n)$ satisfies $p^{\nu_p(n)}\mid n$ and $p^{\nu_p(n)+1}\nmid n$.

Because the content of the lifting-the-exponent lemma is rather long, we introduce it in three parts:

In the following, let $p$ be a prime, $x,y$ be integers satisfying $p\nmid x$ and $p\nmid y$, and $n$ be a positive integer.

### Part one

For all primes $p$ and integers $n$ satisfying $(n,p)=1$,

1.  If $p\mid x-y$, then:

    $$
    \nu_p\left(x^n-y^n\right)=\nu_p(x-y)
    $$

2.  If $p\mid x+y$, then for odd $n$:

    $$
    \nu_p\left(x^n+y^n\right)=\nu_p(x+y)
    $$

???+ note "Proof"
    If $p\mid x-y$, then it is not hard to find that $p\mid x-y\iff x\equiv y\pmod p$, so obviously we have:
    
    $$
    \sum_{i=0}^{n-1}x^iy^{n-1-i}\equiv nx^{n-1}\not\equiv 0\pmod p
    $$
    
    Then from $x^n-y^n=(x-y)\sum_{i=0}^{n-1}x^iy^{n-1-i}$ the proposition is proven.
    
    The proof method for the case $p\mid x+y$ is similar.

### Part two

If $p$ is an odd prime,

1.  If $p\mid x-y$, then:

    $$
    \nu_p\left(x^n-y^n\right)=\nu_p(x-y)+\nu_p(n)
    $$

2.  If $p\mid x+y$, then for odd $n$:

    $$
    \nu_p\left(x^n+y^n\right)=\nu_p(x+y)+\nu_p(n)
    $$

???+ note "Proof"
    If $p\mid x-y$, let $y=x+kp$; we only need to prove the case $p\mid n$.
    
    -   If $n=p$, then by the binomial theorem:
    
        $$
        \begin{aligned}
            \sum_{i=0}^{p-1}x^{p-1-i}y^i&=\sum_{i=0}^{p-1}x^{p-1-i}\sum_{j=0}^i\binom{i}{j}x^j(kp)^{i-j}\\
            &\equiv px^{p-1} \pmod{p^2}\\
        \end{aligned}
        $$
    
        so
    
        $$
        \nu_p\left(x^n-y^n\right)=\nu_p(x-y)+1
        $$
    -   If $n=p^a$, then by mathematical induction we obtain
    
        $$
        \nu_p\left(x^n-y^n\right)=\nu_p(x-y)+a
        $$
    
    Therefore the proposition is proven.
    
    The proof method for the case $p\mid x+y$ is similar.

### Part three

If $p=2$ and $p\mid x-y$,

1.  For odd $n$ (same as item 1 of part one):

    $$
    \nu_p\left(x^n-y^n\right)=\nu_p(x-y)
    $$

2.  For even $n$:

    $$
    \nu_p\left(x^n-y^n\right)=\nu_p(x-y)+\nu_p(x+y)+\nu_p(n)-1
    $$

In addition, for the above $x,y,n$, we have:

If $4\mid x-y$, then:

-   $\nu_2(x+y)=1$
-   $\nu_2\left(x^n-y^n\right)=\nu_2(x-y)+\nu_2(n)$

???+ note "Proof"
    We only need to prove the case where $n$ is even. Since in this case $p\nmid \dbinom{p}{2}$, we cannot use the method of part two to prove it.
    
    Let $n=2^a b$, where $a=\nu_p(n)$, $2\nmid b$, so
    
    $$
    \begin{aligned}
        \nu_p\left(x^n-y^n\right)&=\nu_p\left(x^{2^a}-y^{2^a}\right)\\
        &=\nu_p\left((x-y)(x+y)\prod_{i=1}^{a-1}\left(x^{2^i}+y^{2^i}\right)\right)
    \end{aligned}
    $$
    
    Noting that $2\mid x-y\implies 4\mid x^2-y^2$, so $(\forall i\geq 1),~~x^{2^i}+y^{2^i}\equiv 2\pmod 4$, and the above expression becomes:
    
    $$
    \nu_p\left(x^n-y^n\right)=\nu_p(x-y)+\nu_p(x+y)+\nu_p(n)-1
    $$
    
    Therefore the proposition is proven.

## References

1.  [Lifting-the-exponent lemma - Wikipedia](https://en.wikipedia.org/wiki/Lifting-the-exponent_lemma)
