Prerequisite knowledge: [basic concepts of abstract algebra](./basic.md), [group theory](./group-theory.md)

## Introduction

**Ring theory** studies all kinds of rings.

The content of ring theory involved in this article is inseparable from the divisibility theory in number theory. First, analogous to the normal subgroups in group theory, this article first introduces the kernel of a ring homomorphism, which is called an ideal of the ring; in fact, this is the generalization of the concept of numbers in number theory to general rings. Then, considering generalizing concepts such as prime numbers, the Euclidean algorithm, and prime factorization on the ring of integers to general rings, we obtain the concepts of different types of integral domains.

Many conclusions in number theory still hold on other common rings. It can be said that part of the work of ring theory is discussing whether these conclusions in number theory can hold on general rings; if not, what kind of restrictions need to be imposed on the ring to make these conclusions hold.

???+ info "Notation"
    When no ambiguity arises, this article may omit the multiplication symbol of a ring, and will write the ring $(R,+,\cdot)$ as the ring $R$. In the ring $R$, the additive identity element is also called the zero, denoted $0$; the multiplicative identity element is also called the identity, denoted $1$.

??? warning "The definition of a ring in this article does not require an identity"
    Note that the definition of a ring in this article does not require an identity. Some articles require the definition of a ring to have an identity; in that case, the statements of some conclusions in this article need slight adjustment. For example, in this article an ideal can be defined based on a subring, but in other articles it may need to be defined based on an additive subgroup.

## Ideals

Similar to the case of groups, we can establish the concepts of subrings and ring homomorphisms.

???+ abstract "Subring"
    For a ring $(R,+,\cdot)$ and its subset $S$, if $(S,+,\cdot)$ is also a ring, then $S$ is called a **subring** of $R$.

???+ example "Example: the ring of integers $\mathbf Z$"
    For any integer $n$, $n\mathbf Z=\{nk:k\in\mathbf Z\}$ is a subring of $\mathbf Z$.

???+ abstract "Ring homomorphism"
    For rings $(R,+,\cdot)$ and $(S,\oplus,\odot)$, if $\pi$ preserves the addition and multiplication operations of the rings, i.e. for all $r_1,r_2\in R$, $\pi(r_1+r_2)=\pi(r_1)\oplus\pi(r_2)$ and $\pi(r_1\cdot r_2)=\pi(r_1)\odot\pi(r_2)$ hold, then the mapping $\pi:R\rightarrow S$ is called a **homomorphism** from the ring $R$ to the ring $S$.

??? info "The case where the definition of a ring requires an identity"
    If the definition of a ring requires an identity, then the definition of a ring homomorphism also often requires mapping the identity to the identity. For homomorphisms between non-zero rings with identity, this extra requirement merely guarantees that the homomorphism will not map the entire ring with identity to the zero.

???+ example "Example: the ring of integers $\mathbf Z$ (continued)"
    The mapping of taking modulo any non-zero integer $n$, i.e. $\pi:\mathbf Z\rightarrow\mathbf Z/n\mathbf Z$, where $\pi(a)=\bar a$, is a ring homomorphism.

The [discussion](./group-theory.md#group-homomorphism) of the kernel and image of a group homomorphism can be almost verbatim transferred here. The (relative) size of the image of a homomorphism determines whether the homomorphism is surjective, and whether the kernel of a homomorphism is trivial or not determines whether the homomorphism is injective. The kernel of a ring homomorphism is defined as follows:

???+ abstract "Kernel of a homomorphism"
    The **kernel** of a homomorphism $\pi:R\rightarrow S$ from the ring $R$ to the ring $S$ is $\{r\in R:\pi(r)=0\}$, denoted $\ker\pi$, where $0$ is the additive identity element of $S$.

Obviously, both the kernel and the image of a ring homomorphism are subrings. Conversely, not all subrings can be the kernel of some ring homomorphism. A subring that can be the kernel of a ring homomorphism is called an ideal of the ring.

???+ abstract "Ideal"
    For a ring $R$ and its subring $I$, $I$ is called
    
    -   a **left ideal** of $R$, if for all $r\in R$, $rI\subseteq I$, where $rI=\{ra:a\in I\}$;
    -   a **right ideal** of $R$, if for all $r\in R$, $Ir\subseteq I$, where $Ir=\{ar:a\in I\}$;
    -   an **ideal**, if $I$ is both a left ideal and a right ideal of $R$.

Here we require the ideal $I$ to be closed under both left and right multiplication by the ring $R$. This condition is natural. Because the elements in an ideal are mapped to the zero in a ring homomorphism, and any number left- or right-multiplied by zero should equal zero, this is exactly the required closure. In addition, because the additive structure of a ring is an Abelian group, any subgroup is a normal subgroup; and the multiplicative structure of a ring is very primitive and will not impose additional restrictions on substructures. This shows that the condition of being closed under left and right multiplication is also sufficient.

???+ example "Example: the ring of integers $\mathbf Z$ (continued)"
    As an example, the previously mentioned subring $n\mathbf Z$ is actually an ideal of $\mathbf Z$. It is the set of all multiples of $n$. A multiple of $n$, multiplied by any integer, yields a multiple of $n$. In fact, all ideals of $\mathbf Z$ are of this form; such a ring is called a [principal ideal domain](#principal-ideal-domain). For a general ring, some ideals are not the set of multiples of a certain element; the existence of such general rings is exactly the original motivation for studying ideals (rather than simply studying multiples)[^ideal-history].

### Quotient ring

Like groups, based on the ideals of a ring, we can define the **quotient ring** on the set of all cosets (in the sense of the additive group). Consider the set

$$
R/I=\{a+I:a\in R\},
$$

where the coset $a+I=\{a+b:b\in I\}$. We can prove that if and only if $I$ is an ideal, the operations

$$
\begin{aligned}
(a+I)+(b+I)&=(a+b)+I,\\
(a+I)(b+I)&=(ab)+I
\end{aligned}
$$

are well-defined, i.e. the results of these operations are independent of the choice of representative elements in the cosets. Under these operations, $R/I$ constitutes a ring. Again consistent with the case of groups, we can establish the **first isomorphism theorem** of rings, and there exists a natural homomorphism from the ring to its quotient ring. These proofs show that the ideals of a ring and the normal subgroups of a group play the same role in the homomorphisms of the corresponding structures.

???+ note "First isomorphism theorem"
    Let $\pi:R\rightarrow S$ be a homomorphism from the ring $R$ to the ring $S$; then $\ker\pi$ is an ideal of $R$, and $R/\ker\pi\cong\pi(R)$ is a subring of $S$.

???+ abstract "Natural homomorphism"
    For a ring $R$ and its ideal $I$, the mapping $\pi:R\rightarrow R/I$ given by $\pi(r)=r+I$ is a surjective homomorphism from $R$ to $R/I$, called the **natural homomorphism** from the ring $R$ to the quotient ring $R/I$.

???+ example "Example: the ring of integers $\mathbf Z$ (continued)"
    As an example, the ring $\mathbf Z/n\mathbf Z$ formed by the congruence classes of integers modulo $n$ is the quotient ring obtained by $\mathbf Z$ modulo its ideal $n\mathbf Z$. This also explains the meaning of the symbol $\mathbf Z/n\mathbf Z$. The mapping of modulo $n$ mentioned above, $\pi:\mathbf Z\rightarrow\mathbf Z/n\mathbf Z$, is exactly the natural mapping mentioned here, and the corresponding kernel is exactly the ideal $n\mathbf Z$.

In the case of rings, the other isomorphism theorems also hold.

???+ note "Second isomorphism theorem"
    Let the ring $R$ have a subring $A$ and an ideal $B$; then $A+B=\{a+b:a\in A,b\in B\}$ is likewise a subring of $R$, while $A\cap B$ is an ideal of $A$, $B$ is an ideal of $A+B$, and $(A+B)/B\cong A/(A\cap B)$.

???+ note "Third isomorphism theorem"
    Let the ring $R$ have ideals $I,J$ with $I\subseteq J$; then $J/I$ is also an ideal of $R/I$, and $(R/I)/(J/I)\cong R/J$.

???+ note "Correspondence theorem"
    Let the ring $R$ have an ideal $I$; then there exists a bijection $\varphi:\mathcal S\rightarrow\mathcal T$ between all subrings of the ring $R$ containing $I$, $\mathcal S=\{S:I\subseteq S\subseteq R\}$, and all subgroups of the quotient group $R/I$, $\mathcal T=\{T:T\le R/I\}$, which maps $S\in\mathcal S$ to $S/I\in\mathcal T$. This bijection preserves the inclusion relation of subrings, and ideals of the ring $R$ are always mapped to ideals of $R/I$.

These theorems will play a fundamental role in discussing the structure of rings and ideals later.

### Operations on ideals

Various operations can be defined on the ideals of a ring. This is similar to how concepts such as the greatest common divisor and least common multiple can be defined on the divisibility structure of integers.

???+ abstract "Operations on ideals"
    Let the ring $R$ have ideals $I,J$; the following operations can be defined:
    
    -   **Sum** of ideals: $I+J=\{a+b:a\in I,b\in J\}$;
    -   **Product** of ideals: $IJ=\{\sum_{i=1}^na_ib_i:a_i\in I,b_i\in J\}$, i.e. the set formed by finite sums of all products of the form $ab$;
    -   **Intersection** of ideals: $I\cap J$.

It is easy to verify that the results of these operations are all still ideals of the ring.

???+ example "Example: the ring of integers $\mathbf Z$ (continued)"
    Consider the case of the ring of integers $\mathbf Z$. For ideals $n\mathbf Z$ and $m\mathbf Z$, we can obtain
    
    $$
    \begin{aligned}
    n\mathbf Z+m\mathbf Z&=\gcd(m,n)\mathbf Z,\\
    (n\mathbf Z)(m\mathbf Z)&=(mn)\mathbf Z,\\
    (n\mathbf Z)\cap(m\mathbf Z)&=\mathrm{lcm}(m,n)\mathbf Z.
    \end{aligned}
    $$

In general, for a ring $R$ and its ideals $I$ and $J$, we always have

$$
IJ\subseteq I\cap J\subseteq I,J\subseteq I+J.
$$

Using these definitions, we can generalize the Chinese remainder theorem of integers to general rings. But before that, we still need to further generalize concepts such as prime numbers and coprimality to general rings.

### Maximal ideal

Through the structure of the ideals of a ring, we can understand the properties of the ring.

A non-zero ring $R$ always has two trivial ideals, i.e. $\{0\}$ and $R$. If the ring $R$ is also commutative, then a ring with only these two ideals can and can only be a field[^simple-ring].

???+ note "Theorem"
    Let $R$ be a commutative non-zero ring with identity; then $R$ is a field if and only if $R$ has only the trivial ideals $\{0\}$ and $R$.

??? note "Proof"
    If $R$ is a field, then for any non-zero ideal $I$ we can take any non-zero element $a\in I$; thus, any element $r\in R$ in the field has $r=(ra^{-1})a\in (ra^{-1})I\subseteq I$, so $I=R$. Conversely, for any $a\in R$ with $a\neq 0$, we can verify that $aR=\{ar:r\in R\}$ is an ideal, which must equal $R$, so there exists $b\in R$ such that $ab=1$, which shows that $a$ has an inverse element, so $R$ is a field.

Here the condition of a commutative ring is necessary; otherwise, we need to simultaneously restrict both the left ideals and right ideals to be trivial to guarantee that the ring is a division ring.

The conclusion here can be generalized to the case where the ring itself is not a field. But, at this time we need to instead consider the quotient ring, and discuss the condition under which the quotient ring of a commutative non-zero ring with identity is a field. The quotient ring $R/I$ being a field means that the quotient ring $R/I$ has only trivial ideals; according to the correspondence theorem, there is no ideal in the original ring $R$ strictly between the modded-out ideal $I$ and the original ring $R$. Such an ideal $I$ is called a maximal ideal.

???+ abstract "Maximal ideal"
    For a ring $R$ and its ideal $M$, if $M\neq R$ and the only ideals of $R$ containing $M$ are $M$ and $R$, then the ideal $M$ is called a **maximal ideal**.

???+ note "Theorem"
    Let a commutative non-zero ring with identity $R$ have an ideal $M$; then the quotient ring $R/M$ is a field if and only if $M$ is a maximal ideal.

???+ example "Example: the ring of integers $\mathbf Z$ (continued)"
    For example, the ideal $n\mathbf Z$ in the ring of integers $\mathbf Z$ is a maximal ideal if and only if $n$ is prime. For a prime $p$, the quotient ring $\mathbf Z/p\mathbf Z$ is a field, also denoted $\mathbf F_p$.

Not all rings have maximal ideals, but a non-zero ring with identity always has maximal ideals.

???+ note "Theorem (Krull)"
    For an ideal $I\neq R$ of a non-zero ring with identity $R$, there is always a maximal ideal $M$ of $R$ such that $I\subseteq M$ holds.

??? note "Proof"
    The idea is to use Zorn's lemma. Examine the set $\mathcal S$ of all proper ideals of $R$ (i.e. ideals not equal to $R$) containing $I$. Because $I\in\mathcal S$, it is non-empty and forms a partially ordered set under the inclusion relation. For any chain $J_0\subseteq J_1\subseteq\cdots\subseteq J_n\subseteq\cdots$ in it, let their union be $J$; then it is easy to verify that this is also an ideal. Moreover, $J\neq R$, otherwise $1\in J$, i.e. there exists $n$ such that $1\in J_n$, which contradicts $J_n$ being a proper ideal. From this, by Zorn's lemma, there exists a maximal ideal $M\supseteq I$.

A maximal ideal, analogized to divisibility theory, is an irreducible element. This is because the inclusion relation of ideals is the divisibility relation of integers; having no ideal as a superset is equivalent to having no factor that can divide it. But, the concept of a maximal ideal is broader than an irreducible element, because not all ideals are principal ideals.

### Prime ideal

The condition of a field is more stringent than that of an integral domain. An ideal that can ensure the quotient ring is an integral domain is called a prime ideal, which is similar to the concept of prime numbers in divisibility theory.

???+ abstract "Prime ideal"
    For a commutative ring $R$ and its ideal $P$, if $P\neq R$ and for any elements $a,b\in R$ in the ring, whenever $ab\in P$ holds we always have $a\in P$ or $b\in P$, then the ideal $P$ is called a **prime ideal**.

This definition looks a bit abrupt, but comparing with [the definition of prime numbers](../number-theory/basic.md#fundamental-theorem-of-arithmetic), this definition of a prime ideal is also natural.

???+ note "Theorem"
    Let a commutative non-zero ring with identity $R$ have an ideal $P$; then the quotient ring $R/P$ is an integral domain if and only if $P$ is a prime ideal.

??? note "Proof"
    For a commutative non-zero ring with identity $R$, the quotient ring $R/P$ is an integral domain if and only if $R/P$ has no zero divisors. Denote the coset $a+P$ as $\bar a$. The quotient ring $R/P$ having no zero divisors is equivalent to $\bar a\bar b=\bar 0$ always implying $\bar a=\bar 0$ or $\bar b=\bar 0$. According to the correspondence theorem, this is equivalent to $ab\in P$ always implying $a\in P$ or $b\in P$.

In the ring of integers $\mathbf Z$, $n\mathbf Z$ is a maximal ideal and a prime ideal if and only if $n$ is prime. In a general commutative ring, a maximal ideal always implies a prime ideal, but of course the converse does not necessarily hold; this can be seen from the properties of their corresponding quotient rings.

???+ note "Theorem"
    For a commutative non-zero ring with identity $R$, its maximal ideal must be a prime ideal.

We will see later that only in those rings with good properties, sufficiently similar to the ring of integers, does the converse proposition hold.

### Principal ideal

Similar to the concept of a subgroup, in the discussion of rings we often need to consider the ideal generated by a certain subset.

???+ abstract "Ideal generated by a subset"
    For a non-zero ring with identity $R$ and its non-empty subset $A\subseteq R$, if $I$ is the smallest (by inclusion) among the ideals of $R$ containing $A$, then the ideal $I$ is called the **ideal generated by a subset $A$**, and is denoted $(A)$. At this time, $A$ is called the **generating set** of $(A)$.

???+ abstract "Principal ideal"
    The ideal generated by a single element $a\in R$ is called a **principal ideal**, denoted $(a)$. At this time, $a$ is called the **generator** of $(a)$.

For a set $A$, we can give the construction of the ideal it generates. First, we have the following definitions

$$
\begin{aligned}
RA&=\{r_1a_1+\cdots+r_na_n:r_i\in R,a_i\in A,n\in\mathbf Z\},\\
AR&=\{a_1r_1+\cdots+a_nr_n:r_i\in R,a_i\in A,n\in\mathbf Z\}.
\end{aligned}
$$

Actually they are respectively the left ideal and right ideal generated by $A$. Then, the ideal generated by the subset $A$ is $RAR$. For a commutative ring, all these defined structures are the same.

All ideals $n\mathbf Z$ in the ring of integers are principal ideals, often denoted $(n)$ below.

## Integral domain

An integral domain is a commutative non-zero ring with identity and no zero divisors. This concept is exactly the generalization of the ring of integers. But, the properties of a ring obtained this way are not necessarily good enough to allow every conclusion in the divisibility theory of integers to be copied over as is. To be able to generalize the conclusions in number theory, we can make further restrictions on an integral domain. Among them, the three most common types of integral domain are the Euclidean domain, the principal ideal domain, and the unique factorization domain; the former concept is strictly contained in the latter concept.

### Divisibility relation

First, here we generalize the relevant concepts in the divisibility theory of integers to general commutative rings.

???+ abstract "Divide"
    Let a commutative ring $R$ have elements $a,b\in R$; if there exists $x\in R$ satisfying $a=bx$, then $b$ is said to **divide** $a$, denoted $b\mid a$. At this time $b$ is called a **divisor** of $a$.

???+ abstract "Associate"
    Let a commutative ring $R$ have elements $a,b\in R$; if they differ only by an invertible element, i.e. there exists an invertible element $u\in R$ satisfying $a=bu$, then $a$ and $b$ are said to be **associate**.

The divisibility relation is a [partial order](../order-theory.md#二元关系) relation on the ring, and the associate relation is an equivalence relation on the ring. From the perspective of ideals, $a\mid b$ is equivalent to $(b)\subseteq (a)$, and $a$ and $b$ being associate is equivalent to $(a)=(b)$. Therefore, when discussing elements in a ring, we usually do not care about the differences between associate elements. Similar to the case of integers, the greatest common divisor of $a$ and $b$ in a commutative ring is defined as the infimum of $\{a,b\}$.

???+ abstract "Greatest common divisor"
    For a commutative ring $R$ and its elements $a,b\in R$, if there exists a non-zero element $d\in R$ satisfying $d\mid a$ and $d\mid b$, and for any $d'$ satisfying $d'\mid a$ and $d'\mid b$, $d'\mid d$ holds, then $d$ is called a **greatest common divisor** of $a$ and $b$, denoted $\gcd(a,b)$.

In an integral domain, the greatest common divisor is uniquely determined up to associates. The following discussion is restricted to integral domains.

In an integral domain, we can also establish a concept similar to prime numbers. In integer theory, prime numbers have two equivalent definitions, but in a general integral domain, these two definitions correspond to different concepts:

???+ abstract "Prime element"
    Let an integral domain $R$ have a non-zero element $p\in R$; if $(p)$ is a prime ideal, that is, $p$ is not an invertible element and $p\mid ab$ always implies $p\mid a$ or $p\mid b$, then $p$ is called a **prime element**.

???+ abstract "Irreducible element"
    Let an integral domain $R$ have a non-zero element $r\in R$; if $r$ is not an invertible element and for any $a,b\in R$ with $r=ab$, either $a$ or $b$ is an invertible element, then $r$ is called an **irreducible element**, or $r$ is said to be irreducible. Conversely, if $r=ab$ with $a,b\in R$ both not invertible elements, then $r$ is said to be reducible.

We can show that the principal ideal $(r)$ corresponding to an irreducible element $r$ is necessarily maximal among all principal ideals of the ring; but in a general integral domain, not all ideals are principal ideals, so the concepts of irreducible element and maximal ideal are not equivalent.

Similar to proving that in a principal ideal domain a prime ideal is necessarily a maximal ideal, we can generally prove the following conclusion:

???+ note "Theorem"
    Let $R$ be an integral domain; if $a\in R$ is a prime element, then $a$ is necessarily also an irreducible element.

??? note "Proof"
    Let $r\in R$ be a prime element, and $a,b\in R$ satisfy $r=ab$. Because $r$ is a prime element, without loss of generality assume $r\mid a$ holds; then $a=cr=cba$. Because the cancellation law holds on an integral domain, we have $1=bc$, so $b$ has an inverse element $c$. This shows that $r$ is an irreducible element.

Conversely, this conclusion does not hold.

??? example "Counterexample"
    In the quadratic integer ring $\mathbf Z[\sqrt{-5}]$, $3$ is an irreducible element, but $9=3\cdot 3=(2+\sqrt{-5})(2-\sqrt{-5})$, so it is not a prime element.
    
    Here we give the proof of this counterexample; readers unfamiliar with quadratic integer rings please first read the [quadratic integer ring](#example-quadratic-integer-ring) part. Let $N(\cdot)$ be the norm on the quadratic integer ring. For any factorization $3=ab$, we have $N(a)N(b)=N(3)=9$. If neither $a$ nor $b$ is an invertible element, then both $N(a)$ and $N(b)$ are greater than $1$, so we must have $N(a)=N(b)=3$. But there is no such element on $\mathbf Z[\sqrt{-5}]$, i.e. $x^2+5y^2=3$ has no integer solution. This shows that $3$ is an irreducible element. As for $3$ not being a prime element, we need to prove that $3$ cannot divide $2\pm\sqrt{-5}$, which is obvious.

### Euclidean domain

Related reading: [(extended) Euclidean algorithm](../number-theory/gcd.md), [Bézout's theorem](../number-theory/bezouts.md)

A Euclidean domain is an integral domain that allows the Euclidean algorithm to be performed.

???+ abstract "Euclidean domain"
    For an integral domain $R$, if there exists a mapping $N:R\setminus\{0\}\rightarrow\mathbf N$ satisfying that for any $a,b\in R$ with $b\neq 0$, there exist $q,r\in R$ such that $a=qb+r$ holds and $r=0$ or $N(r)<N(b)$, then the integral domain $R$ is called a **Euclidean domain** (ED). The mapping $N$ is called the norm of elements in the Euclidean domain.

??? info "Other equivalent definitions"
    The definition adopted in this article only defines the norm at non-zero elements. Different texts may handle the definition of a Euclidean domain differently. For example, some texts may additionally define $N(0)=0$; but the subsequent division with remainder does not use the value of $N(0)$, so this is irrelevant. As another example, the definition on [Wikipedia](https://en.wikipedia.org/wiki/Euclidean_domain) also requires the norm $N$ to satisfy the property: for any non-zero $a,b\in R$, $N(a)\le N(ab)$. But, it is easy to verify that if a Euclidean domain $R$ has a norm $N(\cdot)$ satisfying the properties required by the definition in this article, then we can define a norm $N'(a)=\min_{b\in R\setminus\{0\}} N(ab)$ so that it satisfies the additional property $N'(a)\le N'(ab)$. Therefore, these different definitions are all equivalent.

This definition is actually the generalization of division with remainder in integers. The existence of a norm makes it possible to measure the relative size of the remainder and the divisor. This way, when performing the Euclidean algorithm, the norm of the corresponding remainder is also continuously decreasing; because the norm takes values in the natural numbers, such a process must terminate when $r=0$. This way, we obtain the Euclidean algorithm on a Euclidean domain.

Being able to perform the Euclidean algorithm means that the greatest common divisor can be efficiently computed on a Euclidean domain. Completely analogous to the divisibility theory of integers, we can prove that the result of the Euclidean algorithm is necessarily the greatest common divisor, and Bézout's theorem holds, where the coefficients can be determined by the extended Euclidean algorithm.

???+ note "Theorem"
    For a Euclidean domain $R$ and its elements $a,b\in R$, the result $d$ obtained by performing the Euclidean algorithm on $a$ and $b$ is a greatest common divisor of $a$ and $b$, and there exist $x,y\in R$ such that $d=ax+by$ holds; conversely, any element of the form $ax+by$ is a multiple of $d$.

Note that in the language of ring theory, all elements of the form $ax+by$ are exactly the elements in the ideal $(a,b)$, and this theorem shows that $(a,b)$ is necessarily the principal ideal $(d)$.

In fact, ideals in a Euclidean domain are necessarily principal ideals.

???+ note "Theorem"
    Ideals in a Euclidean domain are necessarily principal ideals.

??? note "Proof"
    Let $R$ be a Euclidean domain, and $I$ be its ideal. If $I=\{0\}$, it is obviously a principal ideal. Let $I$ be a non-zero ideal. By definition, the ring $R$ has a norm $N(\cdot)$, so we can take the non-zero element $d$ in $I$ with the smallest norm. At this time, for any $a\in I$, we have $a=qd+r$ satisfying $r=0$ or $N(r)< N(d)$. And because $r=a-qd\in I$, so by the way $d$ is chosen we know $r=0$, that is $a=qd\in (d)$. This shows that $I$ must be a principal ideal.

### Principal ideal domain

An integral domain in which all ideals are principal ideals is called a principal ideal domain. This is a class of integral domains with quite good properties and is also very common. In these integral domains, the concept of an ideal in the ring is equivalent to the concept of a multiple in the integers.

???+ abstract "Principal ideal domain"
    For an integral domain $R$, if each of its ideals is a principal ideal, then it is called a **principal ideal domain** (PID).

Therefore, the last theorem of the previous section can be restated as follows:

???+ note "Theorem"
    A Euclidean domain is necessarily a principal ideal domain.

In a principal ideal domain, a maximal ideal is equivalent to an ideal generated by an irreducible element. Similar to how prime numbers and irreducible elements are equivalent in the integers, in a principal ideal domain these two concepts are also equivalent, so maximal ideals and prime ideals are also completely equivalent.

???+ note "Theorem"
    Let a principal ideal domain $R$ have a non-zero ideal $I$; then $I$ is a prime ideal if and only if $I$ is a maximal ideal.

??? note "Proof"
    We only need to prove that prime ideals are all maximal ideals. Let a principal ideal domain $R$ have a non-zero prime ideal $(p)$, and simultaneously have an ideal $(a)$ satisfying $(p)\subseteq(a)\subseteq R$. This shows $a\mid p$, so there exists $b\in R$ such that $p=ab$. But since $(p)$ is a prime ideal, $ab\in(p)$ means $a\in(p)$ or $b\in(p)$. If $a\in(p)$, it shows $(a)\subseteq (p)$, so $(a)=(p)$; if $b\in(p)$, it shows $b=cp$, so $p=acp$, and because $p\neq 0$, we have $1=ac$, i.e. $a$ has an inverse element $c$, so $(a)=R$. This shows that $(p)$ is a maximal ideal.

???+ note "Corollary"
    Let a principal ideal domain $R$ have a non-zero element $r$; then $r$ is a prime element if and only if $r$ is an irreducible element.

The analysis of Bézout's theorem in the previous section can be transferred to a principal ideal domain.

???+ note "Theorem"
    Let $R$ be a principal ideal domain, and $a,b\in R$ be non-zero elements. Let $d\in R$ be the generator of the ideal $(a,b)$. Then, the greatest common divisor of $a$ and $b$ is $d$, and it is unique up to associates; moreover, there exist $x,y\in R$ such that $ax+by=d$ holds.

That is to say, [Bézout's theorem](../number-theory/bezouts.md) still holds in a principal ideal domain. Both having a greatest common divisor, the biggest difference between a Euclidean domain and a principal ideal domain is that in the former, the greatest common divisor can be efficiently computed by the Euclidean algorithm, but in a principal ideal domain there is generally no such efficient algorithm.

### Unique factorization domain

A more general concept than a principal ideal domain is the unique factorization domain. The unique factorization theorem of integers is called the [fundamental theorem of arithmetic](../number-theory/basic.md#fundamental-theorem-of-arithmetic). A similar unique factorization theorem actually still holds in some integral domains that are not principal ideal domains. Such integral domains are called unique factorization domains.

???+ abstract "Unique factorization domain"
    For an integral domain $R$, if any non-zero and non-invertible element $r$ can be written in the form $r=p_1\cdots p_n$, where $p_1,\cdots,p_n$ are possibly repeated irreducible elements, and such a factorization is unique up to associates and rearrangement, then the integral domain $R$ is called a **unique factorization domain** (UFD).

The fundamental theorem of arithmetic shows that the ring of integers $\mathbf Z$ is a unique factorization domain.

The previous text gave a counterexample of an irreducible element that is not a prime element, where the involved integral domain $\mathbf Z[\sqrt{-5}]$ no longer satisfies the unique factorization theorem. But, in all unique factorization domains, irreducible elements and prime elements are equivalent.

???+ note "Theorem"
    For a unique factorization domain $R$ and its non-zero element $a\in R$, $a$ is a prime element if and only if $a$ is an irreducible element.

??? note "Proof"
    We only need to prove that irreducible elements are all prime elements. For an irreducible element $r$, if $r\mid ab$, then there exists $c\in R$ such that $ab=rc$ holds. Because $R$ is a unique factorization domain, we can factor $a,b,c\in R$ into products of irreducible elements. Comparing the left and right sides, according to the uniqueness of the factorization, $r$ must be associate to some irreducible factor of $a$ or $b$, so $r$ divides one of $a$ or $b$. This shows that $r$ is also a prime element.

All principal ideal domains are unique factorization domains.

???+ note "Theorem"
    A principal ideal domain is necessarily a unique factorization domain.

??? note "Proof"
    Let $R$ be a principal ideal domain, and $r\in R$ be neither the zero nor an invertible element. To show that $r$ can be uniquely factored into a product of a series of irreducible elements, we can divide it into two steps: first prove the existence of the factorization, then prove the uniqueness of the factorization.
    
    The existence of the factorization is relatively natural. If $r$ is already an irreducible element, there is no need to continue factoring; otherwise, there must exist $r_1r_2$ such that $r=r_1r_2$ and both $r_1,r_2$ are not invertible elements. Furthermore, if both $r_1$ and $r_2$ are irreducible elements, then there is no need to continue factoring; otherwise, for whichever of $r_1$ and $r_2$ is not an irreducible element, we can further factor it, so $r$ can be written as a product of more elements. From this, as long as the product is not all irreducible elements, we can continue the factorization process. The factorization must terminate after finitely many steps. Otherwise, the axiom of choice guarantees that we can take an infinitely-long chain of elements $\{r_{(i)}\}_{i=0}^\infty$ from $R$ satisfying $r_{(0)}=r$ and $r_{(i+1)}\mid r_{(i)}$ for all $i\in\mathbf N$, and these divisibility relations are all strict, i.e. there are no associate elements in the chain. In the language of ideals, this corresponds to a strictly infinitely-increasing sequence of ideals: $I_{0}\subset I_{1}\subset \cdots\subset I_{i}\subset\cdots\subset R$, where $I_i=(r_{(i)})$. It is easy to verify that the union of these ideals $I=\bigcup_{i=0}^\infty I_i$ is still an ideal, so it must be a principal ideal. Let $a$ be the generator of the principal ideal $I$; therefore, there exists $n\in\mathbf N$ satisfying $a\in I_n$. So, $I=(a)\subseteq I_n$. This shows that this strictly infinitely-increasing sequence of ideals does not exist, so the above factorization process must terminate within finitely many steps.
    
    Then prove the uniqueness of the factorization. We can induct on the number of factors in the factorization. The key step of the induction lies in verifying that if $r=p_1p_2\cdots p_n=q_1q_2\cdots q_m$ and $n\le m$, then $p_1$ must be associate to some $q_j$. Here we need to use the previous conclusion: in a principal ideal domain, irreducible elements are all prime elements. We know $p_1$ is an irreducible element in $R$, so it is also a prime element, so for the product on the right side we can inductively show that there must exist some element $q_j$ such that $p_1\mid q_j$. So, there exists $c\in R$ such that $q_j=p_1c$, and $q_j$ is an irreducible element, $p_1$ is also an irreducible element, so by definition $c$ can only be an invertible element, so $p_1$ is associate to $q_j$. This way we can use the cancellation law to cancel $p_1$ and $q_j$ on the left and right sides respectively, and multiply the associate element by which the two differ onto any remaining element. According to the induction hypothesis, the number of irreducible elements in $p_2\cdots p_n$ and $q_1\cdots q_{j-1}q_{j+1}\cdots q_m$ must be equal, and they are the same up to associates. The theorem is proved.

Finally, the existence of the greatest common divisor still holds on a unique factorization domain.

???+ note "Theorem"
    Let a unique factorization domain $R$ have non-zero elements $a,b\in R$, which can be factored into the form $a=up_1^{r_1}\cdots p_n^{r_n}$ and $b=vp_1^{s_1}\cdots p_n^{s_n}$, where $u,v$ are invertible elements, $p_1,\cdots,p_n$ are distinct irreducible elements, and $r_i,s_i$ are all natural numbers; then, a greatest common divisor of them is $d=p_1^{\min\{r_1,s_1\}}\cdots p_n^{\min\{r_n,s_n\}}$.

This actually shows that the property that the greatest common divisor exists is even weaker than the unique factorization theorem holding[^gcd-domain].

### Example: quadratic integer ring

Related reading: [quadratic field](../number-theory/quadratic.md)

The understanding of abstract algebra cannot be separated from examples. It was precisely because the study of Fermat's Last Theorem required studying the properties of a class of algebraic integers that ring theory as we know it today gradually developed[^ring-theory-history]. Here we discuss the simplest algebraic integers, namely quadratic integers. The proofs of many conclusions in this part require complex knowledge of algebraic number theory, so they are omitted.

A **quadratic integer** refers to a complex root of an integer-coefficient quadratic equation $\alpha^2+b\alpha+c=0$ with leading coefficient one. All quadratic integers can and can only have the form

$$
\alpha=a+b\omega,~(a,b\in\mathbf Z)
$$

where,

$$
\omega=\begin{cases}
\dfrac{1+\sqrt{D}}{2},& D\equiv 1\pmod 4,\\
\sqrt D,& D\equiv 2,3\pmod 4,
\end{cases}
$$

where $D$ has no square factor.

??? note "Analysis"
    According to the quadratic formula, we know that the root of this equation can necessarily be written as
    
    $$
    \alpha=\frac{-b\pm\sqrt{b^2-4c}}{2}.
    $$
    
    When $b=2k+1$ is odd, this root can be written as
    
    $$
    \alpha=-k-\frac{1\pm\sqrt{4(k^2+k-c)+1}}{2}.
    $$
    
    Otherwise, when $b=2k$ is even, this root can be written as
    
    $$
    \alpha=-k\pm\sqrt{k^2-c}.
    $$
    
    Thus we can inductively conclude that a quadratic integer must have the above form.

It is easy to verify that for such an $\omega$, the set $\mathbf Z[\omega]=\{a+b\omega:a,b\in\mathbf Z\}$ constitutes a ring. This is called a **quadratic integer ring**, and its fraction field is exactly the quadratic field $\mathbf Q(\sqrt D)$. When $D>0$, all quadratic integers are real numbers, so it is also called a **real quadratic integer ring**; when $D<0$, the quadratic integers other than the integers are complex numbers, so it is also called an **imaginary quadratic integer ring**.

All quadratic integer rings $\mathbf Z[\omega]$ are integral domains. Among them, when $D=-1$, $\mathbf Z[\sqrt{-1}]$ (or denoted $\mathbf Z[\mathrm{i}]$) is also called the Gaussian integer ring; when $D=-3$, $\mathbf Z\left[\dfrac{1+\sqrt{-3}}{2}\right]$ is called the Eisenstein integer ring.

For a quadratic integer $a+b\omega$, we can define its **conjugate** as $a+b\bar\omega$, where,

$$
\bar\omega=\begin{cases}
\dfrac{1-\sqrt{D}}{2},& D\equiv 1\pmod 4,\\
-\sqrt D,& D\equiv 2,3\pmod 4,
\end{cases}
$$

Note that because when $D>0$, a quadratic integer is a real number, the concept of conjugate here is not completely consistent with the concept of conjugate of complex numbers, but they are both special cases of the concept of conjugate of an algebraic element in field theory. Conjugate quadratic integers are roots of the same integer-coefficient quadratic equation.

On a quadratic integer ring we can define the **norm**

$$
\begin{aligned}
N(a+b\omega)&=(a+b\omega)(a+b\bar\omega)\\
&=\begin{cases}
a^2+ab+\dfrac{1-D}{4}b^2,& D\equiv 1\pmod 4,\\
a^2-Db^2,& D\equiv 2,3\pmod 4.
\end{cases}
\end{aligned}
$$

The norm of a quadratic integer is necessarily an integer. In particular, when $D<0$, the norm is necessarily a natural number. The norm preserves the multiplicative structure, i.e. $N(ab)=N(a)N(b)$.

The invertible elements (units) in a quadratic integer ring can and can only be those elements whose norm is $\pm1$. For the case of $D>0$, this is equivalent to considering the solutions of the [Pell equation](../number-theory/pell-equation.md) $x^2-Dy^2=\pm1$ or $x^2-Dy^2=\pm4$. For the case of $D<0$, it is easy to verify that, except for the two special cases where the invertible elements in the Gaussian integer ring $\mathbf Z[\rm{i}]$ are $\{\pm1,\pm\rm{i}\}$ and the invertible elements in the Eisenstein integer ring $\mathbf Z[\omega]$ are $\{\pm1,\pm\omega,\pm\omega^2\}$, the remaining invertible elements are only $\{\pm1\}$.

The norm $N(\alpha)$ defined on a quadratic integer ring can be used to prove that it is a Euclidean domain. For the case of $D>0$, we need to use its absolute value $|N(\alpha)|$ as the norm in the definition of a Euclidean domain. Using the norm obtained this way, we can prove that when $D<0$,

$$
D=-1,-2,-3,-7,-11
$$

or when $D>0$,

$$
D=2, 3, 5, 6, 7, 11, 13, 17, 19, 21, 29, 33, 37, 41, 57, 73
$$

the quadratic integer rings corresponding to these integers are Euclidean domains under modulo $|N(\cdot)|$. But, the norm in the definition of a Euclidean domain is not necessarily the norm defined above. For example, when $D=14,69$, the corresponding quadratic integer rings are also Euclidean domains, but a different norm needs to be used. For the case of $D<0$, we can prove that the cases given above are all the Euclidean domains among the quadratic integer rings.

Using more complex methods, we can also determine whether a certain quadratic integer ring is a principal ideal domain. We can prove that when $D<0$, only

$$
D=-1,-2,-3,-7,-11,-19,-43,-67,-163
$$

the corresponding quadratic integer rings are principal ideal domains. Comparing the above results, we know that cases such as $D=-19$ provide examples of principal ideal domains that are not Euclidean domains. When $D>0$, there is currently no complete result.

But, we can prove that in a quadratic integer ring, unique factorization domains and principal ideal domains are equivalent. The above results show that, for example, $\mathbf Z[\sqrt{-5}]$ is not a principal ideal domain, so it is also not a unique factorization domain. We have already actually proved through an example that it cannot be uniquely factored, i.e.

$$
9=3\times3=(2+\sqrt{-5})\times(2-\sqrt{-5}).
$$

Using the same example, we can show that the ideal $(3,2+\sqrt 5)$ is also not a principal ideal. We will see later that a simple example that is a unique factorization domain but not a principal ideal domain is the polynomial ring $\mathbf Z[x]$.

Although many quadratic integer rings are not unique factorization domains, they are all [Dedekind domains](https://en.wikipedia.org/wiki/Dedekind_domain). This means that all non-trivial ideals in a quadratic integer ring can be uniquely factored into a product of a series of prime ideals. But if the quadratic integer ring itself is not a principal ideal domain, these prime ideal factors do not necessarily correspond to prime elements, so the unique factorization theorem (i.e. factoring a number into a product of prime numbers) no longer holds: this is also the original motivation for studying ideals rather than numbers.

## Polynomial ring

Related reading: [Introduction to polynomial techniques](../poly/intro.md)

In algorithm competitions, we often encounter various operations of polynomials. Operations such as multiplication, inversion, and taking the remainder of polynomials can be regarded as generalizations of number operations to the polynomial ring. Using the language of abstract algebra, we can more quickly understand the properties of the relevant operations on the polynomial ring.

???+ abstract "Polynomial"
    For a non-zero commutative ring with identity $R$, a **polynomial** over $R$ refers to a formal sum
    
    $$
    \sum_{k=0}^{n}a_kx^k = a_0+a_1x+\cdots+a_{n-1}x^{n-1}+a_nx^n,
    $$
    
    where $n\in\mathbf N$, and for each $k$, $a_k\in R$. These $a_k$ are called the **coefficients** of the polynomial, and the corresponding $a_kx^k$ is called a **term** of the polynomial. The $k$ in the term $a_kx^k$ is called the **degree** of this term.
    
    A polynomial whose coefficients are all zero (i.e. the zero element) is called the **zero polynomial**, denoted $0$. For other polynomials, without loss of generality assume $a_n\neq 0$, i.e. $a_nx^n$ is the term with the highest degree among the terms with non-zero coefficients. At this time, the natural number $n$ is called the **degree** of the polynomial, and the term $a_nx^n$ in which it lies is called the **leading term**, and $a_n$ is also called the **leading coefficient**. A polynomial whose leading coefficient equals one (i.e. the identity) is called a **monic** polynomial. The degree of the zero polynomial is not specified, or is defined as $-\infty$.

The $x$ appearing in the polynomial notation is called the **indeterminate** of the polynomial. It itself has no meaning and no value range. Its existence is merely to mark the position of the coefficient through its exponent. So, a polynomial can also be written as a sequence over $R$

$$
(a_0,a_1,...,a_{n-1},a_n,0,0,\cdots).
$$

But, such a sequence can only have finitely many non-zero terms. If the coefficient sequences corresponding to two polynomials are the same, then the two polynomials are said to be equal. This is equivalent to their formal sums being completely consistent after padding the terms with zero coefficients. Below, we no longer distinguish the notation of the formal sum of equal polynomials: if necessary, readers can pad in the missing zeros in the coefficients on their own.

Sometimes we need to substitute an element in the ring into the indeterminate in a polynomial. For example, let $f(x)$ be a polynomial over $R$ and $a\in R$; then the result of substituting $a$ into the polynomial $f(x)$ is $f(a)$. Its meaning is: in the formal sum of the polynomial, replacing $x$ with $a$, we obtain an arithmetic expression in $R$, and $f(a)$ is the result of computing this expression in $R$.

??? info "\"Polynomial\" and \"polynomial function\""
    Readers should not confuse these two concepts. A polynomial is just a finite-length coefficient sequence; it does not automatically become a function. Although the operation of substituting a ring element into the indeterminate here does map a polynomial to a polynomial function, such a mapping is not necessarily injective. For example, $f(x)=x^p-x$ as a polynomial over the field $\mathbf F_p$ is obviously not equal to the zero polynomial; but $f(x)$ as a polynomial function $\mathbf F_p\rightarrow \mathbf F_p$ is identically zero (i.e. Fermat's little theorem). Although the two concepts are different, many concepts of polynomial functions can be generalized to the case of polynomials, for example we can imitate the differentiation, indefinite integral, composition, etc. of polynomial functions to define the (formal) [derivative](../poly/intro.md#导数), [indefinite integral](../poly/intro.md#导数), [composition](../poly/intro.md#复合), etc. of polynomials. These formal operations do not depend on any topological structure, but many operation rules still hold.

For polynomials

$$
\begin{aligned}
f(x)&=a_0+a_1x+\cdots+a_{n-1}x^{n-1}+a_nx^n,\\
g(x)&=b_0+b_1x+\cdots+b_{n-1}x^{n-1}+b_nx^n,
\end{aligned}
$$

the addition operation of polynomials is defined as

$$
f(x)+g(x) = (a_0+b_0)+(a_1+b_1)x+\cdots+(a_{n-1}+b_{n-1})x^{n-1}+(a_n+b_n)x^n,
$$

and the multiplication operation of polynomials is defined as

$$
f(x)g(x) = a_0b_0+(a_1b_0+a_0b_1)x+(a_2b_0+a_1b_1+a_0b_2)x^2+\cdots,
$$

where the coefficient of the $x^k$ term is $\sum_{i=0}^ka_{k-i}b_i$. Under the addition and multiplication operations defined this way, we can prove that all polynomials over $R$ constitute a ring, denoted $R[x]$.

The degree of a polynomial $f(x)$ is denoted $\deg f(x)$. Those polynomials of degree zero are constant polynomials; they and the zero polynomial are equivalent to the embedding of $R$ in $R[x]$. Obviously, $R$ has zero divisors if and only if $R[x]$ has zero divisors.

???+ note "Theorem"
    The polynomial ring $R[x]$ is an integral domain if and only if $R$ is an integral domain.

In the polynomial ring $R[x]$ over an integral domain $R$, the results of addition and multiplication satisfy

$$
\begin{aligned}
\deg(f(x)+g(x)) &\le \max\{\deg f(x),\deg g(x)\},\\
\deg(f(x)g(x)) &= \deg f(x) + \deg g(x).
\end{aligned}
$$

Here we set $\deg 0 = -\infty$. So, the invertible elements in the polynomial ring are necessarily those invertible elements among its constant polynomials. Any polynomial of degree one or above is not invertible.

The following discussion will be limited to polynomials over an integral domain.

???+ info "Convention"
    Below, we will use the two phrasings "polynomial over the ring $R$" and "polynomial in the polynomial ring $R[x]$" indistinguishably. For example, a polynomial being irreducible over the ring $R$ means the polynomial is irreducible in the polynomial ring $R[x]$. Moreover, if $R$ is a subring of $S$, then a polynomial over $R$ automatically becomes a polynomial over $S$; we no longer explain this further.

### Polynomial ring over a field

Among the polynomial rings over integral domains, the one with the simplest properties is of course the polynomial ring over a field. In the polynomial ring $F[x]$ over a field $F$, because the coefficients can be divided, we can define division with remainder. Without loss of generality, let the norm of a non-zero polynomial $f(x)$ be $N(f(x))=\deg f(x)$. Then, for a polynomial $f(x)$ and a non-zero polynomial $g(x)$ in $F[x]$, we can obviously perform division with remainder

$$
f(x)=g(x)q(x)+r(x),
$$

where $q(x),r(x)\in F[x]$, and $r(x)=0$ or $\deg r(x)<\deg g(x)$. This shows that polynomial rings over a field are all Euclidean domains.

???+ note "Theorem"
    The polynomial ring $F[x]$ over a field $F$ is a Euclidean domain, a principal ideal domain, and a unique factorization domain.

In algorithm competitions, due to computational precision reasons, what is often considered is the polynomial ring $\mathbf F_p[x]=(\mathbf Z/p\mathbf Z)[x]$, where the modulus $p$ is required to be prime. Such a ring allows operations such as the Euclidean algorithm. But, the polynomial ring $(\mathbf Z/n\mathbf Z)[x]$ corresponding to an arbitrary modulus $n$ is not even an integral domain.

Division with remainder holding means that the root of a polynomial always corresponds to a linear factor of it.

???+ abstract "Root"
    A **root** of a polynomial $f(x)$ refers to an element $\xi\in F$ such that $f(\xi)=0$ holds.

???+ note "Theorem"
    For a polynomial $f(x)$ over a field $F$ and an element $\xi\in F$ in the field, $\xi$ is a root of $f(x)$ if and only if $f(x)$ has a linear factor $(x-\xi)$.

??? note "Proof"
    Division with remainder shows that there exist $q(x),r(x)$ such that $f(x)=q(x)(x-\xi)+r(x)$ and $\deg r(x)<\deg(x-\xi)=1$. Therefore, $r(x)$ is a constant polynomial or the zero polynomial; let $r(x)=c$; then we must have $f(x)=q(x)(x-\xi)+c$. Substituting $x=\xi$, we have $0=a(\xi)=c$, i.e. $f(x)=q(x)(x-\xi)$.

The concept of a root can be generalized to the case of multiple roots.

???+ abstract "Multiple root"
    If a polynomial $f(x)$ has a factor $(x-\xi)^k$, and $(x-\xi)^{k+1}$ cannot divide $f(x)$, then $\xi$ is called a **root of multiplicity $k$** of $f(x)$. If $k>1$, then the root $\xi$ is called a **multiple root** of $f(x)$; if $k=1$, then the root $\xi$ is called a **simple root** of $f(x)$.

???+ note "Theorem"
    If a polynomial $f(x)$ over a field $F$ has (possibly repeated) roots $\xi_1,\cdots,\xi_k$, then it must have a factor $(x-\xi_1)\cdots(x-\xi_k)$. Furthermore, if a polynomial $f(x)$ over a field $F$ has degree $n$, then it has at most $n$ roots (counting multiplicity).

??? note "Proof"
    It suffices to note that $F[x]$ is a unique factorization domain.

Although polynomials over a field satisfy the unique factorization theorem, there is no general way to determine whether a given polynomial is reducible. The cases with relatively small degree are relatively easy. For example, all linear polynomials are irreducible polynomials. On special fields, all irreducible polynomials are linear polynomials. Such a field is called an [algebraically closed field](./field-theory.md#algebraically-closed-field). On such a field, all polynomials not identically equal to a non-zero constant have roots, so any polynomial of degree greater than one can be further factored. One such example is the field of complex numbers $\mathbf C$. And over the field of real numbers $\mathbf R$, there exist irreducible polynomials of degree two; over the field of rational numbers $\mathbf Q$, the structure of irreducible polynomials is even more complex. The [field theory](./field-theory.md) page has more discussion on polynomials over the field of rational numbers and finite fields.

The above conclusions are all about polynomials over a field. Polynomials over more general integral domains can often be transformed into such cases.

Below we consider the polynomial ring $R[x]$ over a unique factorization domain $R$. Directly performing operations in $R[x]$, because the coefficients often cannot be divided, many operations are restricted. It is useful to consider extending $R$ to its fraction field $F$, and then consider factoring the polynomial $f(x)$ in $R[x]$ in $F[x]$. We know $F[x]$ is a unique factorization domain, so we can deduce the factorization in $R[x]$ from the factorization of $f(x)$ in $F[x]$. Fortunately, such an idea is always feasible.

???+ note "Gauss's lemma"
    For a unique factorization domain $R$ and its fraction field $F$, if $f(x)\in R[x]$, then if in $F[x]$ $f(x)=A(x)B(x)$, then there must exist $s,t\in F$ such that $a(x)=sA(x)\in R[x]$, $b(x)=tB(x)\in R[x]$, and $f(x)=a(x)b(x)$. Therefore, if $f(x)$ is irreducible in $R[x]$, then it is irreducible in $F[x]$.

??? note "Proof"
    Let $f(x)\in R[x]$ be reducible in $F[x]$, and $f(x)=A(x)B(x)$. Let $r_a$ and $r_b$ be the least common multiples of the denominators of all coefficients in $A(x)$ and $B(x)$ respectively; then $\tilde a(x)=r_aA(x)$ and $\tilde b(x)=r_bB(x)$ are both polynomials over $R$. Let $r=r_ar_b$; then $rf(x)=\tilde a(x)\tilde b(x)$. If $r$ is an invertible element in $R$, then we can take the factorization $f(x)=(r^{-1}\tilde a(x))\tilde b(x)$, which obviously satisfies the requirements of the lemma.
    
    Otherwise, if $r$ has an irreducible factor $p$, here we want to prove that this factor can be cancelled on both sides of the equation, while guaranteeing that all coefficients are still in the integral domain $R$. Note that $p$ must also be a prime element, so $(p)$ is a prime ideal. Taking modulo $p$ on both the left and right sides of the equation, we obtain a polynomial over $(R/(p))[x]$: $0=\bar a(x)\bar b(x)$, where $\bar a$ and $\bar b$ are the polynomials after taking modulo. Because $R/(p)$ is an integral domain, $(R/(p))[x]$ is also an integral domain, so we can assume $\bar a(x)=0$. This shows that the coefficients of $\tilde a(x)$ can all divide $p$. Therefore, the factor $p$ can be directly cancelled on both sides of the equation.
    
    According to the definition of a unique factorization domain, $r$ has at most finitely many such irreducible factors, so after cancelling them finitely many times we reduce to the case where $r$ is an invertible element in $R$. The lemma is then proved.

???+ note "Corollary"
    For a unique factorization domain $R$ and its fraction field $F$, if $f(x)\in R[x]$ and all non-zero coefficients of $f(x)$ are coprime (i.e. the greatest common divisor is the identity in $R$), then $f(x)$ is irreducible in $R[x]$ if and only if $f(x)$ is irreducible in $F[x]$.

That is to say, the irreducible elements in the integer-coefficient polynomial ring $\mathbf Z[x]$ are all irreducible elements in $\mathbf Q[x]$. An effective method for determining whether an integer-coefficient polynomial is irreducible is Eisenstein's criterion. According to Gauss's lemma, it also provides a method for determining whether a rational-coefficient polynomial is irreducible.

???+ note "Eisenstein's criterion"
    Let a degree-$n$ integer-coefficient polynomial $f(x)=a_0+a_1x+\cdots+a_{n-1}x^{n-1}+a_nx^n$; if there exists a prime $p$ satisfying $p\mid a_i$ for all $i=0,1,\cdots,n-1$, and $p$ cannot divide $a_n$, and $p^2$ cannot divide $a_0$, then the polynomial $f(x)$ is irreducible over the field of rational numbers $\mathbf Q$. If $\gcd(a_0,a_1,\cdots,a_n)=1$, then the polynomial $f(x)$ is also irreducible over the ring of integers $\mathbf Z$.

??? note "Proof"
    Using Gauss's lemma, we know that if the polynomial $f(x)$ is reducible over the field of rational numbers $\mathbf Q$, then it is also reducible over the ring of integers $\mathbf Z$. Let $f(x)=b(x)c(x)$ be its factorization in $\mathbf Z[x]$. Taking modulo the prime $p$ on both the left and right sides of the equation, we obtain a factorization in $\mathbf F_p[x]$, $\overline{f}(x)=\overline{b}(x)\overline{c}(x)$. But the condition of the theorem shows that $\overline{f}(x)=x^n$, so there must exist an integer $m$ such that $\overline b(x)=x^m$ and $\overline c(x)=x^{n-m}$, where $0<m<n$. So, the constant terms $b_0$ and $c_0$ of the factors $b(x)$ and $c(x)$ are both multiples of $p$. So, the constant term $a_0=b_0c_0$ of $f(x)$ must be a multiple of $p^2$. This contradicts the given condition.

??? example "Examples"
    1.  The polynomial $x^3-2$ is irreducible in $\mathbf Q[x]$. Apply Eisenstein's criterion with $p=2$.
    2.  The polynomial $x^4+1$ is irreducible in $\mathbf Q[x]$. Otherwise, $(x+1)^4+1=x^4+4x^3+6x^2+4x+2$ is also reducible. But, applying Eisenstein's criterion with $p=2$, we know that the latter is not reducible.

For a unique factorization domain $R$, because the polynomial ring over the corresponding fraction field $F$ is a unique factorization domain, and Gauss's lemma shows that the factorizations of polynomials over the fraction field $F$ and polynomials over the original integral domain $R$ correspond to each other, so $R[x]$ is also a unique factorization domain. Therefore, we have the following theorem:

???+ note "Theorem"
    The polynomial ring $R[x]$ is a unique factorization domain if and only if $R$ is a unique factorization domain.

Here $\mathbf Z[x]$ provides an example of a unique factorization domain that is not necessarily a principal ideal domain. For example, in $\mathbf Z[x]$, $(2,x)$ is not a principal ideal.

There are many methods to extend the polynomial ring to a larger set. For example, for the polynomial ring $R[x]$ over an integral domain, we can extend it to its fraction field, denoted $R(x)$. This fraction field is often called the **field of rational fractions**, in which the basic form of an element is $\dfrac{f(x)}{g(x)}$, where $f(x)$ and $g(x)$ are both polynomials.

### Multivariate polynomial ring

The polynomial ring can be generalized to the case with multiple indeterminates. For a commutative ring with identity $R$, we can define the polynomial ring over $R$, i.e. the univariate polynomial ring $R[x]$. Furthermore, we can define the polynomial ring $R[x][y]$ over $R[x]$, which can be regarded as the bivariate polynomial ring $R[x,y]$ over $R$. From this, we can inductively define the $k$-variate polynomial ring $R[x_1,\cdots,x_k]$ over $R$. When $R$ is an integral domain, any multivariate polynomial ring over it is an integral domain; similarly, the property of a unique factorization domain can also be transferred to any multivariate polynomial ring.

### Formal power series ring

We can also consider the case where the formal sum can have arbitrarily many non-zero coefficients. A **formal power series** over a commutative ring with identity $R$ is defined as

$$
\sum_{k=0}^\infty a_kx^k=a_0+a_1x+a_2x^2+\cdots.
$$

Using the same way as the polynomial ring $R[x]$, we can define the addition and multiplication operations between power series. And, the formal power series at this time also constitutes a ring, denoted $R[[x]]$. The formal power series here do not need to consider their convergence or divergence, because in fact each formal power series is just its coefficient sequence, and is not endowed with more topological structure.

The structure of the formal power series ring is very interesting. In the polynomial ring over an integral domain, the invertible elements can only be constants. But, in the formal power series ring, we can have

$$
(1-x)^{-1}=\sum_{k=0}^\infty x^k=1+x+x^2+\cdots.
$$

This phenomenon is universal. As long as the constant term $a_0$ of a formal power series is an invertible element in $R$, then $\sum_{k=0}^\infty a_kx^k$ is also necessarily invertible. This is because if we set

$$
\left(\sum_{k=0}^\infty a_kx^k\right)\left(\sum_{k=0}^\infty b_kx^k\right)=1,
$$

then, listing the equations that the coefficients need to satisfy, we can recursively find the expression of $b_k$, which only involves the inverse of $a_0$.

On the formal power series ring we can define various operations, such as inversion, division, compositional inverse, formal derivative, elementary functions, etc.; see [Introduction to polynomial techniques](../poly/intro.md) for details.

### Formal Laurent series ring

The formal power series ring can be further extended so that it allows terms of negative degree. A **formal Laurent series** over a commutative ring with identity $R$ is defined as

$$
\sum_{k=N}^\infty a_kx^k,
$$

where $N\in\mathbf Z$. Therefore, a formal Laurent series can have finitely many terms of negative degree. Extending the previous addition and multiplication to formal Laurent series, we can obtain the formal Laurent series ring, denoted $R((x))$. If $F$ is a field, then $F((x))$ is also a field.

The formal Laurent series ring has applications in [Lagrange inversion](../poly/lagrange-inversion.md).

## Chinese remainder theorem

Related reading: [Chinese remainder theorem](../number-theory/crt.md)

In number theory, the Chinese remainder theorem is often used to solve systems of number-theoretic equations. For a general commutative ring with identity, we can likewise establish the Chinese remainder theorem. Each congruence equation is equivalent to specifying the image of the unknown in a certain quotient ring; then, the Chinese remainder theorem in a commutative ring with identity is equivalent to determining the element in the ring through these images in the quotient rings.

This discussion can be transformed into formal language. For a non-zero commutative ring with identity $R$ and its ideals $I_1,\cdots,I_n$, consider the ring homomorphism $\varphi:R\rightarrow R/I_1\times \cdots R/I_n$, which maps $r$ to $(r+I_1,\cdots,r+I_n)$. Here, $r+I_i$ is a coset, and $\times$ denotes the direct product of rings:

???+ abstract "Direct product"
    For rings $R_1$ and $R_2$, on the direct product $R_1\times R_2$ of their additive groups we can define multiplication as multiplying each component separately; then $R_1\times R_2$ becomes a ring, called the **direct product** of the rings $R_1$ and $R_2$, still denoted $R_1\times R_2$.

The kernel of the homomorphism $\varphi$ is $\ker\varphi=I_1\cap\cdots\cap I_n$. The question the Chinese remainder theorem answers is under what conditions such a mapping is surjective.

In the case of number theory, the theorem holds requires these moduli to be coprime. This condition can be generalized to the case of ring theory.

???+ abstract "Coprime (comaximal)"
    Let the ring $R$ have ideals $I$ and $J$; if $I+J=R$, then $I$ and $J$ are said to be **comaximal**.

For the case of a ring with identity, if we consider principal ideals $(a)$ and $(b)$, this condition is equivalent to there existing $x,y\in R$ such that $ax+by=1$, which is similar to Bézout's theorem when integers are coprime. Using this definition, we can completely imitate the case of the ring of integers to establish the **Chinese remainder theorem** on a commutative ring with identity.

???+ note "Chinese remainder theorem"
    Let a non-zero commutative ring with identity $R$ have ideals $I_1,\cdots,I_n$. If they are pairwise comaximal, then the ring homomorphism $\varphi$ defined above is surjective, and its kernel equals the product of these ideals $\ker\varphi=I_1\cap\cdots\cap I_n=I_1\cdots I_n$, therefore,
    
    $$
    R/(I_1\cdots I_n)=R/(I_1\cap\cdots\cap I_n)\cong R/I_1\times\cdots\times R/I_n.
    $$

??? note "Proof"
    The content of the theorem is rich, but there are only two conclusions that still need to be proved, i.e. $\varphi$ is surjective and $I_1\cap\cdots\cap I_n=I_1\cdots I_n$. The key lies in making good use of the comaximal condition.
    
    First prove the case $n=2$. Because the ideals $I_1$ and $I_2$ are comaximal, i.e. $I_1+I_2=R$, so the identity $1$ in $R$ can be written in the form $a_1+a_2$, where $a_i\in I_i$. Because $a_1\in I_1$ and $a_1=1-a_2\in 1+I_2$, so $\varphi(a_1)=(I_1,1+I_2)$; similarly, $\varphi(a_2)=(1+I_1,I_2)$. Therefore, $(\varphi(a_2),\varphi(a_1))$ plays a role similar to a "basis" in a vector space. So, for any image $(r_1+I_1,r_2+I_2)$, we can find a preimage $r_1a_2+r_2a_1$ under the homomorphism $\varphi$. This shows that $\varphi$ is surjective.
    
    We still need to prove $I_1\cap I_2=I_1I_2$. For a general ring we always have $I_1I_2\subseteq I_1\cap I_2$; the key lies in its reverse. For any $r\in I_1\cap I_2$, we have $r=r(a_1+a_2)=ra_1+ra_2\in I_1I_2$. So, $I_1\cap I_2\subseteq I_1I_2$ also holds. So, the required is proved.
    
    For the case $n>2$, we need to use mathematical induction. The key of the induction step lies in proving that for pairwise comaximal ideals $I_1,\cdots,I_n$, the ideals $I_1$ and $I_2\cdots I_n$ are always comaximal. Since $I_1$ is comaximal with $I_2,\cdots,I_n$, for each $i=2,\cdots,n$ there exist $a_i\in I_1$ and $b_i\in I_i$ such that $1=a_i+b_i$ holds. Therefore, $1=(a_2+b_2)\cdots(a_n+b_n)$ holds. So, $1\in (b_2\cdots b_n)+I_1\subseteq I_1+(I_2\cdots I_n)$. This shows that the ideals $I_1$ and $I_2\cdots I_n$ are comaximal.

### Application: Lagrange interpolation formula

Related reading: [Lagrange interpolation](../numerical/interp.md#lagrange-插值法), [fast polynomial interpolation](../poly/multipoint-eval-interpolation.md#多项式的快速插值)

The interpolation problem refers to: given a series of point values $\{(x_i,y_i)\}_{i=1}^n$, finding a polynomial $f(x)$ over a field $F$ such that it satisfies $f(x_i)=y_i$ for all $i=1,\cdots,n$. Of course we assume all $x_i$ are distinct. The Lagrange interpolation formula gives the general solution to this kind of problem.

For a polynomial $f(x)$ over a field $F$, the condition $f(x_i)=y_i$ is equivalent to $x_i$ being a root of the polynomial $f(x)-y_i$, so it is equivalent to $(x-x_i)\mid(f(x)-y_i)$, i.e. $f(x)\equiv y_i\pmod{x-x_i}$. So, the interpolation problem is equivalent to solving the system of congruence equations

$$
\begin{cases}
f(x)\equiv y_1&\pmod{x-x_1},\\
f(x)\equiv y_2&\pmod{x-x_2},\\
\cdots\\
f(x)\equiv y_n&\pmod{x-x_n}.
\end{cases}
$$

These linear polynomials $\{x-x_i\}_{i=1}^n$ are pairwise coprime. According to the Chinese remainder theorem, the solution to the problem should have the form

$$
f(x)=\sum_{i=1}^ny_iM_i(x),
$$

where $M_i(x)=m_i(x)\prod_{j\neq i}(x-x_j)$ and $M_i(x)\equiv 1\pmod{x-x_i}$. According to the equivalence derived above, this is equivalent to $M_i(x_i)=1$, i.e.

$$
m_i(x_i)\prod_{j\neq i}(x_i-x_j) = 1.
$$

It is useful to take $m_i(x)$ to be a constant polynomial, i.e.

$$
m_i(x) = \frac{1}{\prod_{j\neq i}(x_i-x_j)}.
$$

From this, we obtain the Lagrange interpolation formula

$$
f(x)=\sum_{i=1}^ny_i\frac{\prod_{j\neq i}(x-x_j)}{\prod_{j\neq i}(x_i-x_j)}.
$$

In general, generalizing this method, we can also derive the [Hermite interpolation formula](https://en.wikipedia.org/wiki/Hermite_interpolation), which allows restricting the values of several derivatives of the polynomial at each point.

### Application: the multiplicative group of integer congruence classes

Related reading: [primitive root](../number-theory/primitive-root.md), [fundamental theorem of finitely generated Abelian groups](./group-theory.md#classification-theorem)

As an application of the Chinese remainder theorem and content related to group theory, here we discuss the structure of the multiplicative group of integers modulo $n$. This section omits the overline notation of congruence classes.

The **multiplicative group of integers modulo $n$** refers to $(\mathbf Z/n\mathbf Z)^\times$, i.e. the multiplicative group (also called the unit group) of the invertible elements in the quotient ring $\mathbf Z/n\mathbf Z$. The order of the group $(\mathbf Z/n\mathbf Z)^\times$ is $\varphi(n)$, because the necessary and sufficient condition for the existence of an inverse element is being coprime to $n$. Here $\varphi(n)$ is the [Euler function](../number-theory/euler-totient.md). Moreover, the group $(\mathbf Z/n\mathbf Z)^\times$ is always an Abelian group.

According to the fundamental theorem of arithmetic, the modulus $n$ can be factored into a product of powers of different primes:

$$
n=p_1^{\alpha_1}\cdots p_s^{\alpha_s}.
$$

It is easy to verify that for the ideals of the ring of integers, the condition that the ideals are comaximal is equivalent to the generators of the ideals being coprime. So, applying the Chinese remainder theorem we can obtain

$$
\mathbf Z/n\mathbf Z\cong\mathbf Z/p_1^{\alpha_1}\mathbf Z\times\cdots\times\mathbf Z/p_s^{\alpha_s}\mathbf Z.
$$

The isomorphism of rings means that the corresponding multiplicative structures are also isomorphic, so

$$
(\mathbf Z/n\mathbf Z)^\times\cong(\mathbf Z/p_1^{\alpha_1}\mathbf Z)^\times\times\cdots\times(\mathbf Z/p_s^{\alpha_s}\mathbf Z)^\times.
$$

This shows that $\varphi(n)=\varphi(p_1^{\alpha_1})\cdots\varphi(p_n^{\alpha_n})$, i.e. the Euler function is a multiplicative function.

Therefore, to study the case of a general modulus, we only need to consider the case where the prime power $p^k$ is the modulus. For the case of a prime power, we need to consider the two cases of $p=2$ and $p$ being an odd prime separately:

-   For the case of $p=2$, direct verification shows $(\mathbf Z/2\mathbf Z)^\times\cong C_1$ and $(\mathbf Z/4\mathbf Z)^\times\cong C_2$. For the case of $k\ge3$, we have $(\mathbf Z/2^k\mathbf Z)^\times\cong C_2\times C_{2^{k-2}}$.

    ??? note "Proof"
        Directly computing using the binomial theorem, we know
        
        $$
        \begin{aligned}
        5^{2^{k-2}}=(1+2^2)^{2^{k-2}}&\equiv 1\pmod {2^k},\\
        5^{2^{k-3}}=(1+2^2)^{2^{k-3}}&\equiv 1+2^{k-1}\pmod {2^k}.
        \end{aligned}
        $$
        
        So, $5$ is an element of order $2^{k-2}$ in $(\mathbf Z/2^k\mathbf Z)^\times$. At the same time, $-1$ and $5^{2^{k-3}}$ are two different elements of order two, so $-1\notin\langle 5\rangle$. So, the intersection of $\langle-1\rangle$ and $\langle 5\rangle$ is trivial, so according to the second isomorphism theorem we know
        
        $$
        (\mathbf Z/2^k\mathbf Z)^\times\cong\langle-1\rangle\times\langle 5\rangle\cong C_2\times C_{2^{k-2}}.
        $$
-   For the case of $p$ being odd, we can prove that $(\mathbf Z/p^k\mathbf Z)^\times$ is isomorphic to the cyclic group $C_{\varphi(p^k)}$.

    ??? note "Proof"
        To prove that $(\mathbf Z/p^k\mathbf Z)^\times$ is a cyclic group, using the fundamental theorem of finite Abelian groups we know that we only need to prove that each of its Sylow $q$-subgroups is a cyclic group. First, for the Sylow $p$-subgroup, direct computation shows
        
        $$
        \begin{aligned}
        (1+p)^{p^{k-1}} &\equiv 1\pmod{p^k},\\
        (1+p)^{p^{k-2}} &\equiv 1+p^{k-1}\pmod{p^k}.
        \end{aligned}
        $$
        
        Therefore, $(1+p)$ is an element of order $p^{k-1}$. That is to say, the unique Sylow $p$-subgroup of $(\mathbf Z/p^k\mathbf Z)^\times$ is the cyclic group $\langle 1+p\rangle$.
        
        For the other Sylow $q$-subgroups ($q\neq p$), we can transform them into the case $k=1$ through a group homomorphism. Consider the group homomorphism $\varphi:(\mathbf Z/p^k\mathbf Z)^\times\rightarrow(\mathbf Z/p\mathbf Z)^\times$, which maps the coset $r+p^k\mathbf Z$ to the coset $r+p\mathbf Z$. The size of the kernel of this mapping is $p^{k-1}$, so restricting the mapping $\varphi$ to a Sylow $q$-subgroup ($q\neq p$) of $(\mathbf Z/p^k\mathbf Z)^\times$, the kernel of the restricted mapping is trivial, so this Sylow $q$-subgroup is isomorphic to the image of the mapping, i.e. a Sylow $q$-subgroup of $(\mathbf Z/p\mathbf Z)^\times$. Therefore, we only need to prove that the Sylow $q$-subgroups of $(\mathbf Z/p\mathbf Z)^\times$ are all cyclic groups.
        
        Finally, prove that the Sylow $q$-subgroups of $(\mathbf Z/p\mathbf Z)^\times$ are all cyclic groups. Because $(\mathbf Z/p\mathbf Z)^\times$ is a finite Abelian group, we can factor it by invariant factors into
        
        $$
        C_{n_1}\times\cdots\times C_{n_r}.
        $$
        
        Here, $n_1\mid n_2\mid \cdots \mid n_r$. So, in each direct product factor there are $n_1$ elements whose order divides $n_1$. If $r>1$, then there must be strictly more than $n_1$ elements satisfying the equation $x^{n_1}=1$. But, $\mathbf Z/p\mathbf Z$ is a field, and a degree-$n_1$ polynomial over a field has at most $n_1$ roots, so $r=1$. That is to say, $(\mathbf Z/p\mathbf Z)^\times\cong C_{p-1}$.
        
        This way we prove $(\mathbf Z/p^k\mathbf Z)^\times\cong C_{p^{k-1}}\times C_{p-1}=C_{\varphi(p^{k})}$.

The structure of the multiplicative group for the case of a general modulus is thereby also determined. From the existing results we know that the multiplicative group of integers modulo $n$ is a cyclic group if and only if the modulus $n$ takes

$$
1,2,4,p^k,2p^k
$$

where $p$ is an odd prime; otherwise, the multiplicative group of integers modulo $n$ necessarily has a subgroup $C_2\times C_2$ and cannot be a cyclic group. When the multiplicative group is a cyclic group, the generator of the multiplicative group is called the **primitive root** of this modulus. Therefore, the theorem here gives exactly the necessary and sufficient condition for the existence of a primitive root.

Of course, the analysis of the structure of the multiplicative group implies more information than the condition for the existence of a primitive root. It clearly reflects the orders of different elements in the multiplicative group. In the group $(\mathbf Z/n\mathbf Z)^\times$, an element $x$ satisfying $x^k=1$, i.e. a solution of the congruence equation $x^k\equiv 1\pmod n$, is called a **$k$-th root of unity modulo $n$**; an element with order exactly $k$ is called a **primitive $k$-th root of unity modulo $n$**. Using the structure of the multiplicative group, the existence and number of these roots of unity can be precisely computed. Finally, the least common multiple of the orders of all elements in the group $(\mathbf Z/n\mathbf Z)^\times$, i.e. the smallest positive integer $k$ such that $x^k=1$ for all $x\in (\mathbf Z/n\mathbf Z)^\times$, expressed as a function of $n$, is exactly the [Carmichael function](../number-theory/primitive-root.md#carmichael-函数). Its series of properties can all be obtained from the structure of the multiplicative group.

## References and notes

-   Dummitt, D.S. and Foote, R.M. (2004) Abstract Algebra. 3rd Edition, John Wiley & Sons, Inc.
-   [Quadratic integer - Wikipedia](https://en.wikipedia.org/wiki/Quadratic_integer)
-   [Formal power series - Wikipedia](https://en.wikipedia.org/wiki/Formal_power_series)
-   [Multiplicative group of integers modulo $n$ - Wikipedia](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n)

[^ideal-history]: <https://en.wikipedia.org/wiki/Ideal_(ring_theory)#History>

[^simple-ring]: Consistent with the case of groups, such a ring is called a **simple ring**. A commutative simple ring can only be a field; the case of a non-commutative simple ring is much more complex.

[^gcd-domain]: An integral domain in which the greatest common divisor exists is called a [GCD domain](https://en.wikipedia.org/wiki/GCD_domain).

[^ring-theory-history]: A brief history of ring theory can be seen [here](https://mathshistory.st-andrews.ac.uk/HistTopics/Ring_theory/).
