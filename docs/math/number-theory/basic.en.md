This article gives a brief introduction to the opening part of number theory.

## Divisibility

???+ note "Definition"
    Let $a,b\in\mathbf{Z}$, $a\ne 0$. If $\exists q\in\mathbf{Z}$ such that $b=aq$, then $b$ is said to be **divisible** by $a$, denoted $a\mid b$; $b$ not being divisible by $a$ is denoted $a\nmid b$.

Properties of divisibility:

-   $a\mid b\iff-a\mid b\iff a\mid-b\iff|a|\mid|b|$
-   $a\mid b\land b\mid c\implies a\mid c$
-   $a\mid b\land a\mid c\iff\forall x,y\in\mathbf{Z}, a\mid(xb+yc)$
-   $a\mid b\land b\mid a\implies b=\pm a$
-   Let $m\ne0$; then $a\mid b\iff ma\mid mb$.
-   Let $b\ne0$; then $a\mid b\implies|a|\le|b|$.
-   Let $a\ne0,b=qa+c$; then $a\mid b\iff a\mid c$.

### Divisors

???+ note "Definition"
    If $a\mid b$, then $b$ is called a **multiple** of $a$, and $a$ is called a **divisor** of $b$.

$0$ is a multiple of all non-$0$ integers. For an integer $b\ne0$, $b$ has only finitely many divisors.

Trivial divisors (trivial factors): for an integer $b\ne0$, $\pm1$, $\pm b$ are the trivial divisors of $b$. When $b=\pm1$, $b$ has only two trivial divisors.

For an integer $b\ne 0$, the other divisors of $b$ are called proper divisors (proper factors, non-trivial divisors, non-trivial factors).

Properties of divisors:

-   Let the integer $b\ne0$. As $d$ ranges over all divisors of $b$, $\dfrac{b}{d}$ also ranges over all divisors of $b$.
-   Let the integer $b\gt 0$; then as $d$ ranges over all positive divisors of $b$, $\dfrac{b}{d}$ also ranges over all positive divisors of $b$.

In specific problems, **unless otherwise stated, a divisor always refers to a positive divisor.**

## Division with remainder

???+ note "Remainder"
    Let $a,b$ be two given integers, $a\ne0$. Let $d$ be a given integer. Then there exists a unique pair of integers $q$ and $r$ satisfying $b=qa+r,d\le r<|a|+d$.

Regardless of the value of the integer $d$, $r$ is collectively called the remainder. $a\mid b$ is equivalent to $a\mid r$.

In general, $d$ is taken to be $0$, and then the equation $b=qa+r,0\le r<|a|$ is called division with remainder. The remainder $r$ here is called the least non-negative remainder.

The remainder also often has two other common choices:

-   Absolute least remainder: $d$ is taken to be the negative of half the absolute value of $a$. That is, $b=qa+r,-\dfrac{|a|}{2}\le r<|a|-\dfrac{|a|}{2}$.
-   Least positive remainder: $d$ is taken to be $1$. That is, $b=qa+r,1\le r<|a|+1$.

The remainder in division with remainder is only the least non-negative remainder. **Unless otherwise stated, the remainder always refers to the least non-negative remainder.**

Properties of the remainder:

-   The remainder after dividing any integer by a positive integer $a$ is definitely and only one of the $a$ numbers from $0$ to $(a-1)$.
-   $a$ consecutive integers, after being divided by a positive integer $a$, attain exactly the above $a$ remainders. In particular, there is definitely and only one number divisible by $a$.

## Greatest common divisor and least common multiple

For the definitions of the four terms common divisor, common multiple, greatest common divisor, and least common multiple, see [greatest common divisor](./gcd.md).

???+ warning "Warning"
    Some authors consider the greatest common divisor of $0$ and $0$ to be undefined, while other authors generally regard it as $0$. The implementation in the C++ STL adopts the latter, i.e. considers the greatest common divisor of $0$ and $0$ to be $0$[^gcdcpp].

The greatest common divisor has the following properties:

-   $(a_1,\dots,a_n)=(|a_1|,\dots,|a_n|)$;
-   $(a,b)=(b,a)$;
-   if $a\ne 0$, then $(a,0)=(a,a)=|a|$;
-   $(bq+r,b)=(r,b)$;
-   $(a_1,\dots,a_n)=((a_1,a_2),a_3,\dots,a_n)$. Furthermore $\forall 1<k<n-1,~(a_1,\dots,a_n)=((a_1,\dots,a_k),(a_{k+1},\dots,a_n))$;
-   for integers $a_1,\dots,a_n$ not all $0$ and a nonzero integer $m$, $(ma_1,\dots,ma_n)=|m|(a_1,\dots,a_n)$;
-   for integers $a_1,\dots,a_n$ not all $0$, if $(a_1,\dots,a_n)=d$, then $(a_1/d,\dots,a_n/d)=1$;
-   $(a^n,b^n)=(a,b)^n$.

The greatest common divisor also has the following properties related to coprimality:

-   if $b|ac$ and $(a,b)=1$, then $b\mid c$;
-   if $b|c$, $a|c$ and $(a,b)=1$, then $ab\mid c$;
-   if $(a,b)=1$, then $(a,bc)=(a,c)$;
-   if $(a_i,b_j)=1,~\forall 1\leq i\leq n,1\leq j\leq m$, then $\left(\prod_i a_i,\prod_j b_j\right)=1$. In particular, if $(a,b)=1$, then $(a^n,b^m)=1$;
-   for integers $a_1,\dots,a_n$, if $\exists v\in \mathbf{Z},~\prod_i a_i=v^m$ and $(a_i,a_j)=1,~\forall i\ne j$, then $\forall 1\leq i\leq n,~\sqrt[m]{a_i}\in\mathbf{Z}$.

The least common multiple has the following properties:

-   $[a_1,\dots,a_n]=[|a_1|,\dots,|a_n|]$;
-   $[a,b]=[b,a]$;
-   if $a\ne 0$, then $[a,1]=[a,a]=|a|$;
-   if $a\mid b$, then $[a,b]=|b|$;
-   $[a_1,\dots,a_n]=[[a_1,a_2],a_3,\dots,a_n]$. Furthermore $\forall 1<k<n-1,~[a_1,\dots,a_n]=[[a_1,\dots,a_k],[a_{k+1},\dots,a_n]]$;
-   if $a_i\mid m,~\forall 1\leq i\leq n$, then $[a_1,\dots,a_n]\mid m$;
-   $[ma_1,\dots,ma_n]=|m|[a_1,\dots,a_n]$;
-   $[a,b,c][ab,bc,ca]=[a,b][b,c][c,a]$;
-   $[a^n,b^n]=[a,b]^n$.

The greatest common divisor and least common multiple can be combined into many marvelous identities, such as:

-   $(a,b)[a,b]=|ab|$;
-   $(ab,bc,ca)[a,b,c]=|abc|$;
-   $\dfrac{(a,b,c)^2}{(a,b)(b,c)(a,c)}=\dfrac{[a,b,c]^2}{[a,b][b,c][a,c]}$.

These properties can all be proved through the definition or the [unique factorization theorem](#fundamental-theorem-of-arithmetic); among them, the proofs using the unique factorization theorem are easier to understand.

### Coprimality

???+ note "Definition"
    If $(a_1,a_2)=1$, then $a_1$ and $a_2$ are said to be **coprime** (**relatively prime**).
    
    If $(a_1,\ldots,a_k)=1$, then $a_1,\ldots,a_k$ are said to be **coprime** (**relatively prime**).

Multiple integers being coprime does not necessarily mean pairwise coprime. For example, $6$, $10$, and $15$ are coprime, but no two of them are coprime.

Properties of coprimality and the theory of the greatest common divisor: Bézout's identity. See [Bézout's identity](./bezouts.md).

### Euclidean algorithm

The Euclidean algorithm is an algorithm, also called Euclid's algorithm. See [greatest common divisor](./gcd.md).

## Primes and composites

For algorithms about primes, see [primes](./prime.md).

???+ note "Definition"
    Let the integer $p\ne0,\pm1$. If $p$ has no divisors other than the trivial divisors, then $p$ is called a **prime** (**irreducible number**).
    
    If an integer $a\ne0,\pm 1$ and $a$ is not a prime, then $a$ is called a **composite**.

$p$ and $-p$ are always both primes or both composites. **Unless otherwise stated, a prime always refers to a positive prime.**

If a factor of an integer is a prime, then this prime is called a prime factor (prime divisor) of that integer.

Simple properties of primes and composites:

-   An integer $a$ greater than $1$ is a composite, which is equivalent to $a$ being expressible as a product of integers $d$ and $e$ ($1<d,e<a$).
-   If a prime $p$ has a divisor $d$ greater than $1$, then $d=p$.
-   An integer $a$ greater than $1$ can always be expressed as a product of primes.
-   For a composite $a$, there must exist a prime $p\le\sqrt{a}$ such that $p\mid a$.
-   There are infinitely many primes.
-   All primes greater than $3$ can be expressed in the form $6n\pm 1$[^ref1].

## Fundamental theorem of arithmetic

???+ note "Fundamental lemma of arithmetic"
    Let $p$ be a prime and $p\mid a_1a_2$; then at least one of $p\mid a_1$ and $p\mid a_2$ holds.

The converse of the fundamental lemma of arithmetic, slightly modified, can also give another definition of a prime.

???+ note "Another definition of a prime"
    For an integer $p\ne 0,\pm 1$, if for any integers $a_1,a_2$ satisfying $p\mid a_1a_2$, $p\mid a_1$ or $p\mid a_2$ holds, then $p$ is called a prime.

??? tip "Tip"
    The motivation for this definition can be found in [prime ideals](../algebra/ring-theory.md#prime-ideal).

???+ note "Fundamental theorem of arithmetic (unique factorization theorem)"
    Let $a$ be a positive integer; then there must be a representation:
    
    $$
    a=p_1p_2\cdots p_s
    $$
    
    where $p_j(1\le j\le s)$ are primes. And, up to order, this representation is unique.

???+ note "Standard prime factorization"
    Merging the identical primes in the above representation, one obtains:
    
    $$
    a={p_1}^{\alpha_1}{p_2}^{\alpha_2}\cdots{p_s}^{\alpha_s},p_1<p_2<\cdots<p_s
    $$
    
    called the standard prime factorization of the positive integer $a$.

The fundamental theorem of arithmetic and the fundamental lemma of arithmetic, the two theorems are equivalent.

## Congruence

???+ note "Definition"
    Let the integer $m\ne0$. If $m\mid(a-b)$, then $m$ is called the **modulus**, $a$ is congruent to $b$ modulo $m$, and $b$ is a **residue** of $a$ modulo $m$. Denoted $a\equiv b\pmod m$.
    
    Otherwise, $a$ is not congruent to $b$ modulo $m$, and $b$ is not a residue of $a$ modulo $m$. Denoted $a\not\equiv b\pmod m$.
    
    Such an equation is called a congruence modulo $m$, or **congruence** for short.

By the properties of divisibility, the above congruence is also equivalent to $a\equiv b\pmod{(-m)}$.

In the following, unless otherwise stated, the modulus is always a **positive integer**.

The $b$ in the expression is a residue of $a$ modulo $m$, and this concept is entirely consistent with the remainder. By restricting the range of $b$, we correspondingly have the least non-negative residue, absolute least residue, and least positive residue of $a$ modulo $m$.

Properties of congruence:

-   Congruence is an [equivalence relation](../order-theory.md#二元关系), i.e. congruence has
    -   Reflexivity: $a\equiv a\pmod m$.
    -   Symmetry: if $a\equiv b\pmod m$, then $b\equiv a\pmod m$.
    -   Transitivity: if $a\equiv b\pmod m,b\equiv c\pmod m$, then $a\equiv c\pmod m$.
-   Linear operations: if $a,b,c,d\in\mathbf{Z},m\in\mathbf{N}^*,a\equiv b\pmod m,c\equiv d\pmod m$, then:
    -   $a\pm c\equiv b\pm d\pmod m$.
    -   $a\times c\equiv b\times d\pmod m$.
-   Let $f(x)=\sum_{i=0}^n a_ix^i$ and $g(x)=\sum_{i=0}^n b_ix^i$ be two integer-coefficient polynomials, $m\in\mathbf{N}^*$, and $a_i\equiv b_i\pmod m,~0\leq i\leq n$; then for any integer $x$, $f(x)\equiv g(x)\pmod m$. Furthermore, if $s\equiv t\pmod m$, then $f(s)\equiv g(t)\pmod m$.
-   If $a,b\in\mathbf{Z},k,m\in\mathbf{N}^*,a\equiv b\pmod m$, then $ak\equiv bk\pmod{mk}$.
-   If $a,b\in\mathbf{Z},d,m\in\mathbf{N}^*,d\mid a,d\mid b,d\mid m$, then when $a\equiv b\pmod m$ holds, $\dfrac{a}{d}\equiv\dfrac{b}{d}\left(\bmod\;{\dfrac{m}{d}}\right)$.
-   If $a,b\in\mathbf{Z},d,m\in\mathbf{N}^*,d\mid m$, then when $a\equiv b\pmod m$ holds, $a\equiv b\pmod d$.
-   If $a,b\in\mathbf{Z},d,m\in\mathbf{N}^*$, then when $a\equiv b\pmod m$ holds, $(a,m)=(b,m)$. If $d$ can divide $m$ and one of $a,b$, then $d$ must be able to divide the other of $a,b$.

There is also the property of the multiplicative inverse. See [multiplicative inverse](./inverse.md).

## Congruence classes and residue systems

For convenience of discussion, for sets $A,B$ and an element $r$, we introduce the following notation:

-   $r+A:=\{r+a:a\in A\}$;
-   $rA:=\{ra:a\in A\}$;
-   $A+B:=\{a+b:a\in A,b\in B\}$;
-   $AB:=\{ab:a\in A,b\in B\}$.

???+ note "Congruence class"
    For a nonzero integer $m$, divide all integers into $|m|$ pairwise disjoint sets such that any two numbers in the same set are congruent modulo $m$; we call each of these $|m|$ sets a **congruence class** or **residue class** modulo $m$. Use $r\bmod m$ to denote the congruence class modulo $m$ containing the integer $r$.
    
    It is not hard to prove that for any nonzero integer $m$, the above partition scheme must exist and be unique.

By the definition of a congruence class:

-   $r\bmod m=\{r+km:k\in\mathbf{Z}\}$;
-   $r\bmod m=s\bmod m\iff r\equiv s\pmod m$;
-   for any $r,s\in\mathbf{Z}$, either $r\bmod m=s\bmod m$, or $(r\bmod m)\cap (s\bmod m)=\varnothing$;
-   if $m_1\mid m$, then for any integer $r$, $r+m\mathbf{Z}\subseteq r+m_1\mathbf{Z}$.

Noting that congruence is an equivalence relation, a congruence class is the equivalence class of the congruence relation.

We denote the set of all congruence classes modulo $m$ by $\mathbf{Z}_m$, i.e.

$$
\mathbf{Z}_m:=\{r\bmod m:0\leq r<m\}
$$

It is not hard to find:

-   for any integer $a$, $a+\mathbf{Z}_m=\mathbf{Z}_m$;
-   for any integer $b$ coprime with $m$, $b\mathbf{Z}_m=\mathbf{Z}_m$.

By the definition of a [quotient group](../algebra/group-theory.md#quotient-group), $\mathbf{Z}_m=\mathbf{Z}/m\mathbf{Z}$, so sometimes we also use $\mathbf{Z}/m\mathbf{Z}$ to denote $\mathbf{Z}_m$.

By the [pigeonhole principle](../combinatorics/drawer-principle.md):

-   Taking any $m+1$ integers, two of them must be congruent modulo $m$.
-   There exist $m$ integers that are pairwise incongruent modulo $m$.

From this we give the definition of a complete residue system:

???+ note "(Complete) residue system"
    For $m$ integers $a_1,a_2,\dots,a_m$, if for any number $x$ there is exactly one number $a_i$ such that $x$ is congruent to $a_i$ modulo $m$, then these $m$ integers $a_1,a_2,\dots,a_m$ are called a **complete residue system** modulo $m$, or **residue system** for short.

We can also define, modulo $m$, the:

-   Least non-negative (complete) residue system: $0,\dots,m-1$;
-   Least positive (complete) residue system: $1,\dots,m$;
-   Absolute least (complete) residue system: $-\lfloor m/2\rfloor,\dots,-\lfloor -m/2\rfloor-1$;
-   Greatest non-positive (complete) residue system: $-m+1,\dots,0$;
-   Greatest negative (complete) residue system: $-m,\dots,-1$.

Unless otherwise stated, we generally use only the least non-negative residue system.

We note that the following proposition holds:

-   In any congruence class modulo $m$, taking any two integers $a_1,a_2$, $(a_1,m)=(a_2,m)$.

Consider the congruence class $r\bmod m$; if $(r,m)=1$, then all elements of this congruence class are coprime with $m$, which shows that we may perhaps learn the structure of the set formed by all integers coprime with $m$ in a similar way.

???+ note "Reduced congruence class"
    For a congruence class $r\bmod m$, if $(r,m)=1$, then this congruence class is called a **reduced congruence class** or **reduced residue class**.
    
    We denote the number of reduced residue classes modulo $m$ by $\varphi(m)$, called [Euler's totient function](./euler-totient.md).

We denote the set of all reduced congruence classes modulo $m$ by $\mathbf{Z}_m^*$, i.e.

$$
\mathbf{Z}_m^*:=\{r\bmod m:0\leq r<m,(r,m)=1\}
$$

???+ warning "Warning"
    For any integer $a$ and any integer $b$ coprime with $m$, $b\mathbf{Z}_m^*=\mathbf{Z}_m^*$, but $a+\mathbf{Z}_m^*$ is not necessarily $\mathbf{Z}_m^*$. This differs from $\mathbf{Z}_m$.

By the [pigeonhole principle](../combinatorics/drawer-principle.md):

-   Taking any $\varphi(m)+1$ integers coprime with $m$, two of them must be congruent modulo $m$.
-   There exist $\varphi(m)$ integers coprime with $m$ and pairwise incongruent modulo $m$.

From this we give the definition of a reduced residue system:

???+ note "Reduced residue system"
    For $t=\varphi(m)$ integers $a_1,a_2,\dots,a_t$, if $(a_i,m)=1,~\forall 1\leq i\leq t$, and for any number $x$ satisfying $(x,m)=1$ there is exactly one number $a_i$ such that $x$ is congruent to $a_i$ modulo $m$, then these $t$ integers $a_1,a_2,\dots,a_t$ are called a **reduced residue system** modulo $m$.

Similarly, we can also define concepts such as the least non-negative reduced residue system.

Unless otherwise stated, we generally use only the least non-negative reduced residue system.

### Composition of residue systems

For a positive integer $m$, we have the following theorems:

-   If $m=m_1m_2,~1\leq m_1,m_2$, let $Z_{m_1},Z_{m_2}$ be **complete** residue systems modulo $m_1,m_2$ respectively; then for any $a$ coprime with $m_1$,

    $$
    Z_m=aZ_{m_1}+m_1Z_{m_2}.
    $$

    is a **complete** residue system modulo $m$. Furthermore, if $m=\prod_{i=1}^k m_i,~1\leq m_1,m_2,\dots,m_k$, let $Z_{m_1},\dots,Z_{m_k}$ be **complete** residue systems modulo $m_1,\dots,m_k$ respectively; then:

    $$
    Z_m=\sum_{i=1}^k\left(\prod_{j=1}^{i-1}m_j\right)Z_{m_i}.
    $$

    is a **complete** residue system modulo $m$.

???+ note "Proof"
    It suffices to prove that for any $x,x'\in Z_{m_1}$, $y,y'\in Z_{m_2}$ satisfying $ax+m_1y\equiv ax'+m_1y'\pmod{m_1m_2}$,
    
    $$
    ax+m_1y=ax'+m_1y'.
    $$
    
    In fact, since $m_1\mid m_1m_2$, we have $ax+m_1y\equiv ax'+m_1y'\pmod{m_1}$, hence $ax\equiv ax'\pmod{m_1}$; since $(a,m_1)=1$, we have $x\equiv x'\pmod{m_1}$, hence $x=x'$.
    
    Further, $m_1y\equiv m_1y'\pmod{m_1m_2}$, so $y\equiv y'\pmod{m_2}$, i.e. $y=y'$.
    
    Therefore,
    
    $$
    ax+m_1y=ax'+m_1y'.
    $$

-   If $m=m_1m_2,~1\leq m_1,m_2,(m_1,m_2)=1$, let $Z_{m_1}^*,Z_{m_2}^*$ be **reduced** residue systems modulo $m_1,m_2$ respectively; then:

    $$
    Z_m^*=m_2Z_{m_1}^*+m_1Z_{m_2}^*.
    $$

    is a **reduced** residue system modulo $m$.

???+ tip "Tip"
    This theorem is equivalent to proving that Euler's totient function is a [multiplicative function](#multiplicative-function).

???+ note "Proof"
    Let $Z_{m_1},Z_{m_2}$ be complete residue systems modulo $m_1,m_2$ respectively; we have already proved that
    
    $$
    Z_m=m_2Z_{m_1}+m_1Z_{m_2}
    $$
    
    is a complete residue system modulo $m$. Let $M=\{a\in Z_m:(a,m)=1\}\subseteq Z_m$; obviously $M$ is a reduced residue system modulo $m$, so we only need to prove $M=Z_m^*$.
    
    Obviously $Z_m^*\subseteq Z_m$.
    
    Take any $m_2x+m_1y\in M$, where $x\in Z_{m_1}$ and $y\in Z_{m_2}$; we have $(m_2x+m_1y,m_1m_2)=1$, and since $(m_1,m_2)=1$,
    
    $$
    1=(m_2x+m_1y,m_1)=(m_2x,m_1)=(x,m_1),
    $$
    
    $$
    1=(m_2x+m_1y,m_2)=(m_1y,m_2)=(y,m_2).
    $$
    
    Therefore $x\in Z_{m_1}^*$ and $y\in Z_{m_2}^*$, i.e. $M\subseteq Z_m^*$.
    
    Take any $m_2x+m_1y\in Z_m^*$, where $x\in Z_{m_1}^*$ and $y\in Z_{m_2}^*$; we have $(x,m_1)=1$ and $(y,m_2)=1$, and since $(m_1,m_2)=1$,
    
    $$
    (m_2x+m_1y,m_1)=(m_2x,m_1)=(x,m_1)=1,
    $$
    
    $$
    (m_2x+m_1y,m_2)=(m_1y,m_2)=(x,m_2)=1,
    $$
    
    therefore $(m_2x+m_1y,m_1m_2)=1$, i.e. $Z_m^*\subseteq M$.
    
    In summary,
    
    $$
    Z_m^*=m_2Z_{m_1}^*+m_1Z_{m_2}^*.
    $$
    
    is a **reduced** residue system modulo $m$.

## Number-theoretic functions

A number-theoretic function (also called an arithmetic function) is a function whose domain is the positive integers. A number-theoretic function can also be regarded as a sequence.

### Multiplicative function

???+ note "Definition"
    In number theory, if a function $f(n)$ satisfies $f(1)=1$ and $f(xy)=f(x)f(y)$ for any coprime $x, y \in\mathbf{N}^*$, then $f(n)$ is a **multiplicative function**.
    
    In number theory, if a function $f(n)$ satisfies $f(1)=1$ and $f(xy)=f(x)f(y)$ for any $x, y \in\mathbf{N}^*$, then $f(n)$ is a **completely multiplicative function**.

#### Properties

If $f(x)$ and $g(x)$ are both multiplicative functions, then the following functions are also multiplicative functions:

$$
\begin{aligned}
h(x)&=f(x^p)\\
h(x)&=f^p(x)\\
h(x)&=f(x)g(x)\\
h(x)&=\sum_{d\mid x}f(d)g\left(\dfrac{x}{d}\right)
\end{aligned}
$$

For a positive integer $x$, let its unique prime factorization be $x=\prod p_i^{k_i}$, where $p_i$ are primes.

If $F(x)$ is a multiplicative function, then $F(x)=\prod F(p_i^{k_i})$.

If $F(x)$ is a completely multiplicative function, then $F(x)=\prod F(p_i^{k_i})=\prod F(p_i)^{k_i}$.

#### Examples

-   Unit function: $\varepsilon(n)=[n=1]$. (Completely multiplicative)
-   Identity function: $\operatorname{id}_k(n)=n^k$; $\operatorname{id}_{1}(n)$ is usually abbreviated as $\operatorname{id}(n)$. (Completely multiplicative)
-   Constant function: $1(n)=1$. (Completely multiplicative)
-   Divisor function: $\sigma_{k}(n)=\sum_{d\mid n}d^{k}$. $\sigma_{0}(n)$ is usually abbreviated as $d(n)$ or $\tau(n)$, and $\sigma_{1}(n)$ is usually abbreviated as $\sigma(n)$.
-   Euler's totient function: $\varphi(n)=\sum_{i=1}^n[(i,n)=1]$.
-   Möbius function: $\mu(n)=\begin{cases}1&n=1\\0&\exists d>1,d^{2}\mid n\\(-1)^{\omega(n)}&\text{otherwise}\end{cases}$, where $\omega(n)$ denotes the number of essentially distinct prime factors of $n$.

### Additive function

???+ note "Definition"
    In number theory, if a function $f(n)$ satisfies $f(1)=0$ and $f(xy)=f(x)+f(y)$ for any coprime $x, y \in\mathbf{N}^*$, then $f(n)$ is an **additive function**.
    
    In number theory, if a function $f(n)$ satisfies $f(1)=0$ and $f(xy)=f(x)+f(y)$ for any $x, y \in\mathbf{N}^*$, then $f(n)$ is a **completely additive function**.

???+ warning "Additive function"
    The additive function in this section refers to the additive function in number theory, and should be distinguished from the additive map in algebra.

#### Properties

For a positive integer $x$, let its unique prime factorization be $x=\prod p_i^{k_i}$, where $p_i$ are primes.

If $F(x)$ is an additive function, then $F(x)=\sum F(p_i^{k_i})$.

If $F(x)$ is a completely additive function, then $F(x)=\sum F(p_i^{k_i})=\sum F(p_i)\cdot k_i$.

#### Examples

For convenience of exposition, let the set of all primes be $\mathbf P$.

-   Multiplicity of $p$ in the prime factorization: $\nu_p(n) = \max\{k\in\mathbf N: p^k\mid n\}$, where $p\in\mathbf P$. (Completely additive)
-   Number of all prime factors: $\Omega(n)=\sum_{p \in\mathbf P} \nu_p(n)$. (Completely additive)
-   Number of distinct prime factors: $\omega(n)=\sum_{p \in\mathbf P} [p \mid n]$.
-   Sum of all prime factors: $a_0(n)=\sum_{p \in\mathbf P} \nu_p(n)\cdot p$. (Completely additive)
-   Sum of distinct prime factors: $a_1(n)=\sum_{p \in\mathbf P} [p \mid n] \cdot p$.

## Rounding functions

For a real number $x$, define the **floor function** and the **ceiling function** respectively as

$$
\lfloor x\rfloor = \max\{k\in\mathbf Z:k\le x\},~\lceil x\rceil = \min\{k\in\mathbf Z:k\ge x\}.
$$

Using the floor function, a real number can be decomposed into an integer part and a fractional part: $x = \lfloor x\rfloor + \{x\}$, where $\{x\}$ denotes the fractional part of $x$.

The rounding functions have the following basic properties: ($x\in\mathbf R,~n\in\mathbf Z$)

-   $x\in\mathbf Z \iff x = \lfloor x\rfloor = \lceil x\rceil$.
-   $\lceil x\rceil - \lfloor x\rfloor = [x\notin\mathbf Z]$.
-   $x - 1 < \lfloor x\rfloor \le x \le \lceil x\rceil < x + 1$.
-   $\lfloor -x\rfloor = -\lceil x\rceil,~\lceil -x\rceil = -\lfloor x\rfloor$.
-   $\lfloor x + n\rfloor = \lfloor x\rfloor + n,~\lceil x + n\rceil = \lceil x \rceil + n$.
-   Both $\lfloor x\rfloor$ and $\lceil x\rceil$ are weakly increasing functions of $x$.

Proving equalities about the floor (ceiling) function often uses the following equivalent forms: ($x\in\mathbf R,~n\in\mathbf Z$)

-   $\lfloor x\rfloor = n \iff n \le x < n + 1 \iff x - 1 < n \le x$.
-   $\lceil x\rceil = n \iff n - 1 < x \le n \iff x \le n < x + 1$.

Proving inequalities about the floor (ceiling) function often uses the following equivalent forms: ($x\in\mathbf R,~n\in\mathbf Z$)

-   $x < n \iff \lfloor x\rfloor < n$.
-   $n < x \iff n < \lceil x\rceil$.
-   $x \le n \iff \lceil x\rceil \le n$.
-   $n \le x \iff n \le \lfloor x\rfloor$.

Properties involving sums and differences are as follows: ($x,y\in\mathbf R$)

-   $\lfloor x\rfloor + \lfloor y\rfloor \le \lfloor x + y\rfloor \le \lfloor x\rfloor + \lfloor y\rfloor + 1$, with exactly one equality holding.
-   $\lceil x\rceil +\lceil y\rceil -1\leq \lceil x+y\rceil \leq \lceil x\rceil +\lceil y\rceil$, with exactly one equality holding.
-   $\lfloor|x - y|\rfloor \le |\lfloor x\rfloor - \lfloor y\rfloor| \le \lceil|x - y|\rceil$.
-   $\lfloor|x - y|\rfloor \le |\lceil x\rceil - \lceil y\rceil| \le \lceil|x-y|\rceil$.

Properties involving quotients are as follows: ($x\in\mathbf R,~n\in\mathbf Z,~m\in\mathbf Z_+$)

-   $\left\lceil\dfrac{n}{m}\right\rceil = \left\lfloor\dfrac{n+m-1}{m}\right\rfloor,~\left\lfloor\dfrac{n}{m}\right\rfloor = \left\lceil\dfrac{n-m+1}{m}\right\rceil$.
-   $\left\lfloor\dfrac{x + n}{m} \right\rfloor = \left\lfloor\dfrac{\lfloor x\rfloor + n}{m} \right\rfloor,~\left\lceil\dfrac{x + n}{m} \right\rceil = \left\lceil\dfrac{\lceil x\rceil + n}{m} \right\rceil$.
-   $\left\lfloor\dfrac{\lfloor x/n\rfloor}{m}\right\rfloor = \left\lfloor\dfrac{x}{nm}\right\rfloor,~\left\lceil\dfrac{\lceil x/n\rceil}{m}\right\rceil = \left\lceil\dfrac{x}{nm}\right\rceil$.
-   For $x > 0$, $\displaystyle\left\lfloor\dfrac{x}{m}\right\rfloor = \sum_{k=1}^{\lfloor x\rfloor}[m\mid k]$.

Among them, the second and third properties can both be regarded as direct corollaries of the following conclusion:

-   Let $f$ be a continuous increasing function such that whenever $f(x)\in\mathbf Z$, $x\in\mathbf Z$; then

    $$
    \lfloor f(x)\rfloor = \lfloor f(\lfloor x\rfloor)\rfloor,~ \lceil f(x)\rceil = \lceil f(\lceil x\rceil)\rceil.
    $$

    ??? note "Proof"
        By symmetry, it suffices to prove the first equality. If $x$ is an integer, the proposition is obvious. Otherwise, $\lfloor x\rfloor < x$. By the monotonicity of $f$ and the floor function, $\lfloor f(x)\rfloor \ge \lfloor f(\lfloor x\rfloor)\rfloor$. If equality does not hold, then let $y = \lfloor f(x)\rfloor$; it satisfies $\lfloor f(\lfloor x\rfloor)\rfloor < y \le \lfloor f(x)\rfloor$, which is equivalent to $f(\lfloor x\rfloor) < y \le f(x)$. By the continuity of $f$, there exists $\lfloor x\rfloor < x_0 \le x$ such that $f(x_0)=y$. Because $y\in\mathbf Z$, $x_0\in\mathbf Z$, which contradicts the definition of $\lfloor x\rfloor$. Therefore, equality holds, i.e. $\lfloor f(x)\rfloor = \lfloor f(\lfloor x\rfloor)\rfloor$.

Finally, here is a group of conclusions about summations involving rounding functions: ($x\in\mathbf R,~n\in\mathbf Z,~m\in\mathbf Z_+$)

-   $n = \left\lfloor\dfrac{n}{2}\right\rfloor + \left\lceil\dfrac{n}{2}\right\rceil$.
-   $n = \left\lfloor\dfrac{n}{m} \right\rfloor + \left\lfloor\dfrac{n+1}{m} \right\rfloor + \cdots + \left\lfloor\dfrac{n+m-1}{m} \right\rfloor$.
-   $n = \left\lceil\dfrac{n}{m} \right\rceil + \left\lceil\dfrac{n-1}{m} \right\rceil + \cdots + \left\lceil\dfrac{n-m+1}{m} \right\rceil$.
-   $\lfloor mx\rfloor = \lfloor x\rfloor + \left\lfloor x+\dfrac{1}{m}\right\rfloor + \cdots + \left\lfloor x+\dfrac{m-1}{m}\right\rfloor$.
-   $\lceil mx\rceil = \lceil x\rceil + \left\lceil x - \dfrac{1}{m}\right\rceil + \cdots + \left\lceil x - \dfrac{m-1}{m}\right\rceil$.
-   When $m\perp n$, $\displaystyle\sum_{k=1}^{m-1}\left\lfloor\dfrac{kn}{m}\right\rfloor=\dfrac{1}{2}(n-1)(m-1)$.
-   When $m\perp n$, $\displaystyle\sum_{k=1}^{m-1}\left\lceil\dfrac{kn}{m}\right\rceil=\dfrac{1}{2}(n+1)(m-1)$.

The derivations of these and even more general similar summations can be found on the [Euclidean-like algorithm](./euclidean.md) page.

More properties and applications of rounding functions can be found on the following pages:

-   Modulo operation: $n\bmod m = n - \left\lfloor\dfrac{n}{m}\right\rfloor m$. It can be used to [optimize integer modulo operations](./mod-arithmetic.md#related-algorithms).
-   Using Gauss's lemma to prove [quadratic reciprocity](./quad-residue.md#二次互反律).
-   [Number-theoretic block decomposition](./sqrt-decomposition.md), especially its property-proof part.
-   The [Legendre formula](./factorial.md#legendres-formula) for computing the power of a prime factor in a factorial.
-   [Beatty sequences](../game-theory/impartial-game.md#wythoffs-game), Rayleigh's theorem, and Wythoff's game.

## References and notes

-   Pan Chengdong, Pan Chengbiao. Elementary Number Theory. Peking University Press.
-   [Floor and ceiling functions - Wikipedia](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions)
-   Graham, Ronald L., Donald E. Knuth, and Oren Patashnik. "Concrete mathematics: a foundation for computer science." (1989).

[^ref1]: [Are all primes (past 2 and 3) of the forms 6n+1 and 6n-1?](https://primes.utm.edu/notes/faq/six.html)
