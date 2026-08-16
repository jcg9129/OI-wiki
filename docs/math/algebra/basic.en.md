author: jifbt, billchenchina, Enter-tainer, Great-designer, iamtwz, ImpleLee, isdanni, Menci, ouuan, Tiphereth-A, warzone-oier, Xeonacid, c-forrest

This chapter will briefly introduce knowledge related to abstract algebra. At the current stage, the main content of algorithm competitions does not directly examine knowledge of abstract algebra, but the description of algorithms or the solutions to problems often involve some basic concepts of abstract functions, which enables readers who have mastered basic abstract algebra concepts to understand some algorithms more quickly. Therefore, this part of the content is not required knowledge for any contestant, but is only for reference by those readers who are interested or may benefit from it. At the same time, this chapter will avoid an overly comprehensive and overly deep introduction to knowledge of abstract algebra[^oi-wiki-not-wikipedia], and will focus on basic concepts and the parts most closely connected with other knowledge in OI. Readers who want to systematically learn abstract algebra knowledge should refer to a professional abstract algebra textbook.

To better help readers understand the possible gains of reading this part, we list some examples in algorithm competitions that may involve abstract algebra knowledge:

-   Many theorems of number theory and polynomials are special cases of conclusions in abstract algebra;
-   In data structures, structures such as the [segment tree](../../ds/seg.md) can maintain the information of a monoid, and the recurrence relations of many DP problems can be abstracted into such a monoid structure;
-   In combinatorics, the rigorous statement and proof of the [Pólya counting principle](../combinatorics/polya.md) require concepts related to group theory.

Based on this, this chapter will focus on introducing the basic knowledge that cannot be skipped and the parts directly related to these applications. As a start, this article introduces the basic concepts of groups, rings, and fields.

## Groups

The definition of a group is as follows.

???+ abstract "Group"
    Let $G$ be a non-empty set, on which there is a binary operation $\cdot:G\times G\rightarrow G$; if they satisfy the following properties, then $(G,\cdot)$ is called a **group**:
    
    1.  Associative property: for all $a,b,c\in G$, $a\cdot(b\cdot c)=(a\cdot b)\cdot c$ holds;
    2.  Has an identity element: there exists $e\in G$ such that for any $a\in G$, $a\cdot e = e\cdot a = a$ holds. Here, $e$ is called the **identity element** of $G$;
    3.  Existence of inverse elements: for all $a\in G$, there exists a corresponding $b\in G$ such that $a\cdot b=b\cdot a=e$. Here, $b$ is called the **inverse element** of $a$.

??? info "About the closure condition in the definition"
    The binary operation here implies the so-called closure condition, i.e. for any $a,b\in G$, we have $a\cdot b\in G$. Some articles list it separately.

???+ note "Basic properties of groups"
    For a group $(G,\cdot)$, the following properties always hold:
    
    1.  For any finite-length sequence $\{g_i\}_{i=1}^k\subseteq G$, the operation result of the product $g_1\cdot g_2\cdot\cdots\cdot g_k$ is independent of the way of adding parentheses;
    2.  The identity element $e$ is always unique;
    3.  For any element $a\in G$, its inverse $a^{-1}$ is also unique;
    4.  Cancellation law: for $a,b,c\in G$, if $a\cdot c=b\cdot c$ or $c\cdot a=c\cdot b$, then $a=b$.

Groups are quite common. Loosely speaking, all transformations that do not lose structure automatically constitute a group. Take several common types of groups as examples.

???+ example "Examples of groups"
    -   **Symmetric group**: all [permutations](../permutation.md) on a set $M$, i.e. bijections from $M$ to $M$ itself, constitute a group $S_M$ under the composition of mappings. The identity element is the identity transformation, and the inverse element is the inverse mapping (a bijection necessarily has an inverse mapping). If the set $M$ is finite with size $n$, it is also often denoted $S_n$, called the symmetric group of degree $n$.
    -   Space symmetry group (symmetry group): for a geometric figure, the totality of transformations that can make it coincide with itself also constitutes a group under the composition of mappings. This describes the spatial symmetry of this geometric figure. For specific examples, refer to [common space symmetry groups](../combinatorics/polya.md#common-symmetry-groups).
    -   Additive group of integers: the set of integers $\mathbf Z$ constitutes a group $(\mathbf Z,+)$ under the addition $+$ operation. The identity element is $0$, and the inverse element is the opposite number.
    -   Multiplicative group of integers modulo $n$: for a modulus $n$, the [congruence classes](../number-theory/basic.md#congruence-classes-and-residue-systems) corresponding to all integers coprime to $n$ constitute a group $((\mathbf Z/n\mathbf Z)^\times,\times)$ under the multiplication operation. The identity element is $\bar 1$, and the inverse element is exactly the [multiplicative inverse](../number-theory/inverse.md) modulo $n$ (the corresponding congruence class), whose existence is guaranteed by [Bézout's theorem](../number-theory/bezouts.md). For a specific structural analysis, refer to [the multiplicative group of integers modulo $n$](./ring-theory.md#application-the-multiplicative-group-of-integer-congruence-classes).
    -   General linear group: all $n$-dimensional invertible square matrices over a number field $F$ constitute a group $GL_n(F)$ under the multiplication operation. The identity element is the identity matrix, and the inverse element is the inverse matrix.

To better understand the definition of a group, it is useful to look at several examples that are not groups by comparison.

???+ example "Examples that are not groups"
    -   All mappings from $M$ to itself (not necessarily bijections) do not constitute a group. Because those mappings that are not bijections do not have inverse elements.
    -   The integers under multiplication do not constitute a group, because $2$ has no multiplicative inverse in the range of integers.
    -   The positive integers under addition do not constitute a group either, because the positive integers have no additive identity element.
    -   All non-zero congruence classes modulo $n$ often do not constitute a group in the multiplicative sense. For example, in $(\mathbf Z/6\mathbf Z)\setminus\{\overline 0\}$, $\overline 2\times\overline 3=\overline 0$ does not belong to this set, which means multiplication is not even a well-defined binary operation on this set (or in other words, it does not satisfy closure).

Sometimes, it is also necessary to discuss the properties of these more imperfect structures. Therefore, we can define the following concepts, which are broader than groups.

???+ abstract "Semigroup"
    For a non-empty set $G$ and a binary operation $\cdot$ on it, if this operation satisfies the associative property, then $(G,\cdot)$ is called a **semigroup**.

???+ abstract "Monoid"
    For a semigroup $(G,\cdot)$, if it also has an identity element, then $(G,\cdot)$ is called a **monoid**.

???+ example "Examples of monoids and semigroups"
    In the above examples, $(\mathbf N_+,+)$ is a semigroup, and $(\mathbf Z,\times)$ is a monoid.

Finally, the operations on many familiar groups, besides satisfying the associative property, also satisfy the commutative property. The structure of this kind of group is relatively simple; they are called Abelian groups, also called commutative groups.

???+ abstract "Abelian group"
    For a group $(G,\cdot)$, if the operation $\cdot$ also satisfies the commutative property, i.e. for all $a,b\in G$, $a\cdot b=b\cdot a$ holds, then $(G,\cdot)$ is called an **Abelian group** or **commutative group**.

???+ example "Examples of Abelian and non-Abelian groups"
    -   The additive group of integers $(\mathbf Z,+)$ is an Abelian group.
    -   When $n\ge3$, the symmetric group $S_n$ is not an Abelian group.

These are the basic definitions related to group theory. For more content on group theory, refer to [group theory](./group-theory.md) or related books.

## Rings

The definition of a ring is as follows.

???+ abstract "Ring"
    For a non-empty set $R$ and two binary operations $+:R\times R\rightarrow R$ and $\cdot:R\times R\rightarrow R$ on it, if they satisfy the following properties, then $(R,+,\cdot)$ is called a **ring**:
    
    1.  $(R,+)$ constitutes an Abelian group, whose identity element is denoted $0$, and the inverse element of an element $a\in R$ under $+$ is denoted $-a$.
    2.  $(R,\cdot)$ constitutes a semigroup, i.e. $\cdot$ satisfies the associative property.
    3.  Distributive property: for all $a,b,c\in R$, $a\cdot(b+c)=a\cdot b+a\cdot c$ and $(a+b)\cdot c=a\cdot c+b\cdot c$ hold.

For convenience of expression, these two binary operations $+$ and $\cdot$ are often called the addition and multiplication of this ring, and correspondingly, the additive identity element is called the **zero**, and the multiplicative identity element (if it exists) is called the **identity**. We should avoid confusion with the addition and multiplication in specific number sets, and with the natural numbers zero and one.

??? info "About whether the definition requires a multiplicative identity element"
    In some definitions, a ring must have a multiplicative identity element; correspondingly, one without a multiplicative identity element is called a **rng** (or pseudo-ring). When encountering it, we need to judge according to the context. This is exactly the definition adopted by Wikipedia[^ring-wiki].

The additive structure of a ring is quite simple, but the multiplicative structure is very primitive. Therefore, if we analogize with groups and make more requirements on multiplication, we can obtain the following related definitions.

???+ abstract "Ring with identity"
    For a ring $(R,+,\cdot)$, if it has an identity, i.e. there exists a multiplicative identity element, denoted $1$, then $(R,+,\cdot)$ is called a **ring with identity**.

???+ abstract "Division ring"
    For a non-zero ring with identity $(R,+,\cdot)$, if for all non-$0$ elements $a\in R$, there exists a multiplicative inverse (denoted $a^{-1}$), then $(R,+,\cdot)$ is called a **division ring**.

???+ abstract "Commutative ring"
    For a ring $(R,+,\cdot)$, if its multiplication satisfies the commutative property, then $(R,+,\cdot)$ is called a **commutative ring**.

An interesting point in the definition of a division ring here is that it regards $0$ as a special element in the multiplicative structure. This is because $0 = 0\cdot a = a\cdot 0$[^zero-multiplication]. That is to say, the additive identity element in a ring multiplied by any element yields itself. This way, it naturally will not have a multiplicative inverse, unless it is itself the multiplicative identity element. Such a ring is only the zero ring (see the example below).

The insight here is that when understanding the multiplicative structure of a general ring, we need to remove the influence of the additive identity element and examine $R\setminus\{0\}$. Based on this idea, we have the following definitions.

???+ abstract "Zero divisor"
    For a ring $(R,+,\cdot)$, if there exists $b\in R$ with $b\ne 0$ such that $a\cdot b=0$ or $b\cdot a=0$, then the non-zero element $a$ is called a **zero divisor**.

???+ abstract "Unit (invertible element)"
    For a ring $(R,+,\cdot)$, if an element $a$ has a multiplicative inverse, i.e. there exists $b\in R$ such that $a\cdot b=b\cdot a=1$, then the element $a\in R$ is called an **invertible element**, or a **unit**.

???+ warning "\"Unit\" and \"identity element\""
    Please do not confuse these two concepts. To avoid confusion, the abstract algebra part will use the name "invertible element" instead of "unit".

A zero divisor cannot be an invertible element, and an invertible element cannot be a zero divisor. But, a non-zero element can be neither a zero divisor nor an invertible element.

If a ring has no zero divisors, it means that the set of all non-zero elements is closed under the multiplication operation, i.e. $(R\setminus\{0\},\cdot)$ constitutes a semigroup. Furthermore, if we also require it to be a commutative monoid, we can obtain the definition of an integral domain.

???+ abstract "Integral domain"
    For a non-zero ring $(R,+,\cdot)$, if it is a commutative ring, has a multiplicative identity element, and has no zero divisors, then it is called an integral domain.

Although the elements in an integral domain do not necessarily have inverse elements, the characteristic of having no zero divisors is already sufficient to establish the cancellation law on an integral domain.

???+ note "Cancellation law of an integral domain"
    Let an integral domain $R$ have elements $a,b,c\in R$ with $a\neq 0$; if $ab=ac$, then necessarily $b=c$.

For a general ring with identity, if we only consider all its invertible elements, then we can likewise obtain a group structure. This is called the multiplicative group or unit group of the ring.

???+ abstract "Multiplicative group (unit group)"
    For a ring with identity $(R,+,\cdot)$, let $R^\times$ be the set of all invertible elements in $R$; then $(R^\times,\cdot)$ constitutes a group, called the **multiplicative group** or **unit group** of the ring with identity $R$.

Some of the simplest examples of rings are as follows.

???+ example "Examples of rings"
    -   Zero ring: the set $\{0\}$ constitutes a ring under the usual addition $+$ and multiplication $\times$, called the zero ring. It is the only ring with a single element, and also the only ring where the additive identity element and the multiplicative identity element are equal.
    -   Ring of integers: the set of integers $\mathbf Z$ and the addition $+$ and multiplication $\times$ usually defined on it constitute the ring $(\mathbf Z,+,\times)$. In fact, this is an integral domain, but it is not a division ring.
    -   Polynomial ring: for a ring $R$, we can define the [polynomial ring](./ring-theory.md#polynomial-ring) $R[x]$ on it. If $R$ is an integral domain, then this polynomial ring is necessarily an integral domain.
    -   Quaternions: analogous to complex numbers, we can consider the set $\mathbf H=\{a+b\mathrm{i}+c\mathrm{j}+d\mathrm{k}:a,b,c,d\in\mathbf R\}$, and define the addition and multiplication on it, where the multiplication of $\mathrm{i},\mathrm{j},\mathrm{k}$ satisfies
    
        $$
        \mathrm{i}^2=\mathrm{j}^2=\mathrm{k}^2=-1,\ \mathrm{i}\mathrm{j}=-\mathrm{j}\mathrm{i}=\mathrm{k},\ \mathrm{j}\mathrm{k}=-\mathrm{k}\mathrm{j}=\mathrm{i},\ \mathrm{k}\mathrm{i}=-\mathrm{i}\mathrm{k}=\mathrm{j}.
        $$
    
        Then we can verify that $\mathbf H$ constitutes a ring, and moreover, it is a non-commutative division ring.
    -   The subset $2\mathbf Z$ of the set of integers constitutes a ring under the usual addition and multiplication; it is a commutative ring with no zero divisors, but it does not have an identity.
    -   The integer congruence classes modulo $n$, $\mathbf Z/n\mathbf Z$, constitute a ring under the addition and multiplication of congruence classes; it is a commutative ring with an identity (i.e. $\bar 1$). Such a ring has zero divisors if and only if $n$ is composite. So, when $n$ is prime, the ring $(\mathbf Z/n\mathbf Z, +,\times)$ is an integral domain; moreover, at this time it is also a division ring, so it actually constitutes a field. Its multiplicative group $((\mathbf Z/n\mathbf Z)^\times,\times)$ is the multiplicative group of integers modulo $n$.
    -   Matrix ring: all $n$-dimensional square matrices over a ring $R$ constitute a ring $M_n(R)$ under matrix addition and multiplication. In general, this ring has zero divisors and is not a commutative ring.
    -   For all subsets $\mathcal P(A)$ of a set $A$, if we define the symmetric difference $\triangle$ and intersection $\cap$ of sets as its addition and multiplication operations respectively, then $(\mathcal P(A),\triangle,\cap)$ constitutes a ring. In general, this ring has an identity, has zero divisors, and is a commutative ring.

Of course, the discussion of the structure of rings goes far beyond these; to learn more content, refer to [ring theory](./ring-theory.md) or related books.

## Fields

A field is an algebraic structure with stronger properties than a ring. Specifically, a field is a commutative division ring. Of course, we can also write out its complete definition.

???+ abstract "Field"
    For a non-empty set $F$ and two binary operations $+:F\times F\rightarrow F$ and $\cdot:F\times F\rightarrow F$ on it, if they satisfy the following properties, then $(F,+,\cdot)$ is called a **field**:
    
    1.  $(F,+)$ constitutes an Abelian group, whose identity element is denoted $0$, and the inverse element of an element $a\in F$ under $+$ is denoted $-a$.
    2.  $(F\setminus\{0\},\cdot)$ constitutes an Abelian group, whose identity element is denoted $1$, and the inverse element of an element $a\in F\setminus\{0\}$ under $\cdot$ is denoted $a^{-1}$.

In other words, a field is an algebraic structure closed under all four operations of addition, subtraction, multiplication, and division.

Common examples of fields are as follows.

???+ example "Examples of fields"
    -   Number fields: the set of rational numbers $\mathbf Q$, the set of real numbers $\mathbf R$, and the set of complex numbers $\mathbf C$ all constitute fields under the usual addition and multiplication.
    -   Finite field: the set of integer congruence classes modulo a prime $p$, $\mathbf Z/p\mathbf Z$, constitutes a field under the addition and multiplication of congruence classes. Of course, besides this there are also other finite fields; their structure is uniquely determined by their size, and the size must be of the form of a prime power.
    -   **Fraction field**: let $(R,+,\cdot)$ be an integral domain; we can consider the set $Q$ formed by elements of the form $ab^{-1}$. Strictly speaking, on the set $R\times(R\setminus\{0\})$ we define the equivalence relation: $(a_1,b_1)\sim(a_2,b_2)$ if and only if $a_1b_2=a_2b_1$. Then, the set $Q$ is exactly the set formed by the equivalence classes under this relation $R\times(R\setminus\{0\})/\sim$, where the equivalence class in which $(a,b)$ lies is denoted $ab^{-1}$. If we define the operations on it as
    
        $$
        \begin{aligned}
        a_1b_1^{-1}+a_2b_2^{-1} &= (a_1\cdot b_2+a_2\cdot b_1)(b_1\cdot b_2)^{-1},\\
        (a_1b_1^{-1})\cdot(a_2b_2^{-1}) &= (a_1\cdot a_2)(b_1\cdot b_2)^{-1}
        \end{aligned}
        $$
    
        then $(Q,+,\cdot)$ constitutes a field, called the fraction field of $R$. For example, the field of rational numbers $(\mathbf Q,+,\times)$ is exactly the fraction field of the ring of integers $(\mathbf Z,+,\times)$.
    -   Quadratic field: it is extended from the field of rational numbers $\mathbf Q$ by adding $\sqrt d$, where $d\neq 0,1$ and has no square factor. For related content, refer to [quadratic field](../number-theory/quadratic.md).

Compared with a ring, a field has a very simple addition and multiplication structure. So, the structure of a field itself is often very simple. This makes the study of fields quite different from the study of rings; usually we turn to studying field extensions, and the corresponding Galois theory. In algorithm competitions, sometimes we need to compute over the field of rational numbers or over an extension field of a finite field. For content related to field theory, refer to [field theory](./field-theory.md) or related books.

## Application

Finally, taking the following problem as an example, we illustrate how abstract algebraic objects assist in analyzing specific problems.

???+ note "[[Template] \"Dynamic DP\" & dynamic tree divide and conquer (enhanced version)](https://www.luogu.com.cn/problem/P4751)"
    Given a tree of size $n$ with point weights, perform $m$ point weight modifications. After each modification, output the sum of the weights of the maximum weighted independent set on the tree. The problem is forced online.

???+ note "Idea analysis"
    This problem is a template for dynamic DP; a code implementation with correct complexity needs to use a [globally balanced binary tree](../../ds/global-bst.md), and specific sample code is also on the corresponding page. Here we only analyze the modeling process in combination with the scenario of this problem.
    
    To highlight the key points, here we temporarily do not consider the handling of the tree structure by the globally balanced binary tree, and instead consider the DP problem of the maximum weighted independent set on a chain. Consider each point on the chain $[1,n]$ in order; for point $i$ we can select ($1$) or not select ($0$). Let the optimal solutions of the subproblem on $[1,i]$ under these two cases be $f_{i,1}$ and $f_{i,0}$ respectively. So, we can write out the DP equation as
    
    $$
    \begin{aligned}
    f_{i,1}&=w_{i}+f_{i-1,0},\\
    f_{i,0}&=\max\{f_{i-1,1},f_{i-1,0}\}.
    \end{aligned}
    $$
    
    Its initial value is $(f_{0,1},f_{0,0})=(0,0)$, and the final answer is $\max\{f_{n,1},f_{n,0}\}$. To represent the influence of point $i$ on the final result, we only need to note that this recurrence relation can be written as
    
    $$
    (f_{i,1},f_{i,0})=g(f_{i-1,1},f_{i-1,0};w_i).
    $$
    
    This is a series of mappings from $\mathbf R^2$ to $\mathbf R^2$, which maps $(f_{i-1,1},f_{i-1,0})$ to $(f_{i,1},f_{i,0})$; described in the language of groups, these transformations constitute a monoid under the composition of mappings. This is exactly what a segment tree can maintain.
    
    But, if such a parameterized transformation $g(\cdot;w_i)$ has no special structure, a general mapping from $\mathbf R^2$ to $\mathbf R^2$ cannot possibly be described with finite-dimensional data. Here we need another observation, namely if on $\mathbf R\cup\{-\infty\}$ we define $\max$ as addition and $+$ as multiplication, then $\mathbf R\cup\{-\infty\}$ constitutes a structure similar to a ring, where $-\infty$ is the additive identity element and $0$ is the multiplicative identity element. But it is not a ring, because not all elements in it have additive inverses. Such a structure is called a semiring[^semiring]; here the semiring formed by $(\mathbf R\cup\{-\infty\},\max,+)$ is called the **tropical semiring**.
    
    Based on the tropical semiring $(R,\oplus,\otimes)$, we can define matrix multiplication on it. That is, for an $m\times n$ matrix $A=(a_{ij})$ and an $n\times p$ matrix $B=(b_{jk})$, we can define their product $AB$ as $(c_{ik})$, where each of its element entries equals
    
    $$
    c_{ik} = \bigoplus_{j=1}^n(b_{ij}\otimes c_{jk}) = \max_{1\le j\le n}\;(b_{ij}+c_{jk}).
    $$
    
    With these notations, we can regard the above recurrence relation as a linear transformation on the tropical semiring, and write it in matrix language as
    
    $$
    \left(\begin{matrix}f_{i,1}\\f_{i,0}\end{matrix}\right)
    =\left(\begin{matrix}-\infty&w_i\\0&0\end{matrix}\right)\left(\begin{matrix}f_{i-1,1}\\f_{i-1,0}\end{matrix}\right).
    $$
    
    From this, as long as we use a segment tree to maintain the product of these matrices on the tropical semiring, we can answer the dynamic DP problem on a chain with multiple modifications.
    
    Now return to the tree version of this problem. For a node $i$ on the tree, whose set of child nodes is denoted $S(i)$, the DP equation there is
    
    $$
    \begin{aligned}
    f_{i,1}&=w_i+\sum_{j\in S(i)}f_{j,0},\\
    f_{i,0}&=\sum_{j\in S(i)}\max\{f_{j,1},f_{j,0}\}.
    \end{aligned}
    $$
    
    First, transform the problem into the chain version through heavy-light decomposition. Let $h$ be the heavy child node of $i$; then the above recurrence equation can be written as
    
    $$
    \begin{aligned}
    f_{i,1}&=w_i+f_{h,0}+g_{i,1},\\
    f_{i,0}&=\max\{f_{j,0},f_{j,1}\}+g_{i,0},
    \end{aligned}
    $$
    
    where,
    
    $$
    \begin{aligned}
    g_{i,1}&=\sum_{j\in S(i),\ j\neq h}f_{j,0},\\
    g_{i,0}&=\sum_{j\in S(i),\ j\neq h}\max\{f_{j,1},f_{j,0}\}
    \end{aligned}
    $$
    
    summarize the contributions of the light child nodes. According to the description above, these transformations can all be written in the matrix form on the tropical semiring, so the whole problem can be maintained on the segment tree after heavy-light decomposition. But, directly using heavy-light decomposition plus a segment tree, a single modification is $O(\log^2n)$, so we need to use the globally balanced binary tree mentioned above to optimize to $O(\log n)$; of course we can also use LCT to maintain.
    
    The tropical semiring mentioned here and the above matrix operations are actually not rare. If we replace the $\max$ in the above text with $\min$, then the corresponding tropical semiring is often used in shortest-path problems. If the $n$-dimensional square matrix $A$ gives the (shortest) edge weights between two points of some graph with number of vertices $n$, then the element at $(i,j)$ of $A^k$ is exactly the shortest distance from point $i$ to point $j$ passing through at most $k$ edges; in particular, $A^n$ is exactly the distance matrix of this graph. Of course, in actual implementation we do not really brute-force compute this power of the matrix, but use the Floyd algorithm with complexity $O(n^3)$.

## References and notes

-   Dummitt, D.S. and Foote, R.M. (2004) Abstract Algebra. 3rd Edition, John Wiley & Sons, Inc.
-   [Tropical semiring - Wikipedia](https://en.wikipedia.org/wiki/Tropical_semiring)

[^oi-wiki-not-wikipedia]: Because [OI Wiki is not an encyclopedia](../../intro/what-oi-wiki-is-not.md#oi-wiki-is-not-an-encyclopedia).

[^ring-wiki]: [Ring (mathematics) - Wikipedia](https://en.wikipedia.org/wiki/Ring_%28mathematics%29)

[^zero-multiplication]: The derivation of this formula is $0\cdot a+0 = 0\cdot a = (0+0)\cdot a = 0\cdot a + 0\cdot a$, where the first and second equals signs are the definition of the additive identity element, the third equals sign is the distributive property, and the final implication is the cancellation law of addition. The other side of the multiplication is similar.

[^semiring]: A semiring is an algebraic structure obtained by relaxing the requirement in the definition of a ring with identity that the addition operation must have an inverse element, i.e. the additive structure is a commutative monoid and the multiplicative structure is a monoid. For more information, see [Wikipedia](https://en.wikipedia.org/wiki/Semiring).
