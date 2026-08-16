Prerequisites: [Basic concepts of abstract algebra](./basic.md), [Group theory](./group-theory.md), [Ring theory](./ring-theory.md)

## Introduction

**Field theory** is the theory concerning fields.

The field theory covered in this article is mainly the theory of field extensions. A field is an algebraic structure closed under addition, subtraction, multiplication, and division. Competitive programming often requires taking a modulus by a prime $p$, which amounts to performing operations in the finite field $\mathbf F_p$. Similar to the case of the real field $\mathbf R$, some problems are more conveniently solved by computing over a larger field (namely the complex field $\mathbf C$); a common example is using the [fast Fourier transform](../poly/fft.md) to speed up the multiplication of polynomials with real coefficients. Analogous operations can be performed for finite fields as well. Most readers are relatively unfamiliar with extensions of finite fields, so it is beneficial to understand the theory of extensions over general fields. At the end of the article, we give some algorithmic applications that require extending finite fields, and also briefly discuss the extensions over rings of integers that some of these applications may require.

Closely related to field theory is Galois theory. It connects field extensions with their automorphism groups, so that the properties of field extensions can be understood through the tools of group theory. Although this theory is often the core of the relevant algebra courses, it is quite far removed from the content of competitive programming, so this article does not introduce it in much detail. Interested readers should consult the relevant specialized books.

???+ info "Notation"
    Where no ambiguity arises, this article may omit the multiplication signs of rings and fields, and will write the ring $(R,+,\cdot)$ as the ring $R$ and the field $(F,+,\cdot)$ as the field $F$. The additive identity of a ring or field is called the zero element, and the multiplicative identity is called the unit. Moreover, throughout this article $p$ is always a prime, and $q$ is always a prime power, which can be written as $p^n$ where $n$ is a positive integer.

## Field extensions

Analogous to the case of groups and rings, one can establish the concepts of subfield and field homomorphism.

???+ abstract "Subfield"
    For a field $F$, if its subring $E$ is also a field, then $E$ is called a **subfield** of the field $F$.

Here, regardless of how the definitions of ring and subring treat the unit, the subfield $E$ necessarily contains the unit of the field $F$[^subfield-one].

???+ abstract "Field homomorphism"
    A ring homomorphism $\varphi:F\rightarrow E$ from a field $F$ to a field $E$ is also called a **field homomorphism** from the field $F$ to the field $E$.

??? info "How field homomorphisms treat the unit"
    If, unlike the definition in this article, ring homomorphisms are required to map the unit to the unit, then field homomorphisms naturally also require the unit to be mapped to the unit. Otherwise, the unit might also be mapped to the zero element.

Because a field has only trivial ideals, a field homomorphism either maps the entire field to the zero element, or is necessarily an embedding. This shows that the discussion of field homomorphisms can be reduced to the discussion of subfields.

In the case of fields, the smaller field is often the more familiar one, so one usually instead takes a subfield as the base point from which to examine a larger field. This is the concept of a field extension.

???+ abstract "Field extension"
    For a field $F$, if $F$ is a subfield of $E$, then the field $E$ is called an **extension** of the field $F$, also called an **extension field**, denoted $E/F$.

???+ info "Notation for field extensions"
    Although formally similar, the concept of a field extension has nothing to do with quotient rings, and the two should not be confused.

???+ example "Example"
    The complex field $\mathbf C$ is an extension of the real field $\mathbf R$, and the real field $\mathbf R$ is in turn an extension of the rational field $\mathbf Q$.

### Degree of a field extension

For a field extension $E/F$, the field $E$ is always a [linear space](../linear-algebra/vector-space.md) over the field $F$. The dimension of this linear space is the degree of the field extension.

???+ abstract "Degree of a field extension"
    The **degree** of a field extension $E/F$ is the dimension of $E$ viewed as a linear space over the field $F$, i.e. $\dim_F(E)$, denoted $[E:F]$. If the degree of the field extension is finite, the field extension is called a **finite extension**; otherwise it is called an **infinite extension**.

???+ example "Example"
    The degree $[\mathbf C:\mathbf R]$ of the field extension $\mathbf C/\mathbf R$ equals $2$, so it is a finite extension. The field extension $\mathbf R/\mathbf Q$ is an infinite extension.

The degree of a field extension satisfies the multiplicative principle.

???+ note "Theorem"
    Let $F\subseteq K\subseteq E$ all be fields; then the degrees of the extensions among them satisfy $[E:F]=[E:K][K:F]$.

??? note "Proof"
    For the case where the degree of extension is infinite, this is obvious; otherwise, if $\{\alpha_i\}$ is a basis of $E$ as a linear space over $K$, and $\{\beta_j\}$ is a basis of $K$ as a linear space over $F$, then one can verify that $\{\alpha_i\beta_j\}$ is a basis of $E$ as a linear space over $F$.

The case discussed in this article is mainly that of finite extensions of fields.

### Characteristic of a field

For the study of field extensions, there is a natural starting point, namely the smallest subfield containing the unit of the field $F$; this field is also called the **prime subfield** of the field $F$.

The structure of the prime subfield is uniquely determined by the properties of the unit of the field. The characteristic of a field summarizes precisely these properties.

???+ abstract "Characteristic of a field"
    The **characteristic** of a field $F$ is the smallest positive integer $n$ such that $n\cdot 1=0$ holds; if no such $n$ exists, the characteristic of the field $F$ is said to be $0$. Here, $n\cdot 1$ denotes the result of adding $n$ copies of the unit $1$. If the characteristic of the field $F$ is not $0$, then the field $F$ is said to be of **finite characteristic**.

The characteristic of a field can be understood through ring homomorphisms. The ring of integers $\mathbf Z$ is the closed structure obtained by starting from $0$ and $1$ and repeatedly applying addition, subtraction, multiplication, and so on. It can be regarded as a kind of "prototype": every ring containing a unit should "inherit" part of the structure of the ring of integers[^initial-object-ring]. Therefore, for a field $F$, one can consider the ring homomorphism $\varphi:\mathbf Z\rightarrow F$ with the requirement $\varphi(1)=1$. Such a ring homomorphism is uniquely determined; it maps $n\in\mathbf N_+$ to $n\cdot 1$, i.e. the sum of $n$ copies of the unit $1$. The image $\varphi(\mathbf Z)$ of this homomorphism is embedded in the field $F$, and is necessarily unital, commutative, and free of zero divisors, so it is an integral domain. Therefore, the kernel $\ker\varphi$ of the homomorphism is necessarily a prime ideal. The prime ideals of the ring of integers $\mathbf Z$ can only be of the form $(n)$ where $n=0$ or $n$ is prime. The $n$ so obtained is exactly the characteristic of the field.

The characteristic of a field determines the structure of the prime subfield:

1.  When the characteristic is $0$, the homomorphism $\varphi$ is injective, and the ring of integers $\mathbf Z$ is embedded in the field $F$. The rational field $\mathbf Q$, as the smallest field containing the ring of integers, must also be embeddable in the field $F$, and it is the prime subfield of the field $F$;
2.  When the characteristic is a prime $p$, the image $\mathbf Z/p\mathbf Z$ of the homomorphism $\varphi$ is embedded in the field $F$. In this case $\mathbf Z/p\mathbf Z$ is already a field, denoted $\mathbf F_p$, and it is the prime subfield of the field $F$.

These discussions in fact establish the following conclusion:

???+ note "Theorem"
    The characteristic of a field $F$ can only be $0$ or a prime $p$. The prime subfield corresponding to a field of characteristic $0$ is $\mathbf Q$, and the prime subfield corresponding to a field of prime characteristic $p$ is $\mathbf F_p$.

The $\mathbf Q$ and $\mathbf F_p$ in the theorem are also called **prime fields**, i.e. fields whose only subfield is themselves. A finite field is necessarily of finite characteristic, because a field of characteristic $0$ contains at least the subfield $\mathbf Q$.

Fields of finite characteristic and fields of characteristic zero often have different properties. For example, a field of finite characteristic has the following properties:

???+ note "Theorem"
    Let $F$ have characteristic $p$; then:
    
    1.  In the additive group of the field $F$, every nonzero element has order $p$, i.e. for all $x\in F$ we have $px=0$;
    2.  The "freshman's dream", i.e. for all $x,y\in F$ we have $(x+y)^p=x^p+y^p$. Furthermore, the map $x\mapsto x^p$ is an injective endomorphism of $F$, called the **Frobenius endomorphism**.

??? note "Proof"
    For the first property, it suffices to note that $px=(p1)x=0x=0$. For the second property, one only needs to note that in the binomial expansion of $(x+y)^p$, all terms other than $x^p$ and $y^p$ have coefficients that are multiples of $p$, so by the first property we have $(x+y)^p=x^p+y^p$. As for verifying that $x\mapsto x^p$ is an endomorphism, one only needs to further verify $(xy)^p=x^py^p$, which holds because multiplication in a field is commutative. Finally, a ring homomorphism between fields maps the unit to the unit, so it is necessarily injective.

Of course, for a finite field, the Frobenius endomorphism is necessarily also surjective, and hence is an automorphism of the field.

### Simple extension

Similar to the case of extending the real field to the complex field, many extensions can be accomplished by adjoining additional elements to a field and specifying their arithmetic properties. In the general case, to avoid the trouble caused by specifying arithmetic properties, one may consider, within a field extension $E/F$, the case of adjoining elements of $E\setminus F$ to $F$; in this case the rules for the operations of these additional elements with the elements of the field $F$ have already been determined within the larger field $E$.

???+ abstract "Field extension generated by a subset"
    Let $E/F$ be a field extension and $S\subseteq E$; then the **extension of the field $F$ generated by $S$** is the smallest subfield of $E$ that contains both $F$ and $S$, denoted $F(S)$.

The simplest case is naturally when the set $S$ contains only a few elements.

???+ abstract "Finitely generated extension"
    Let $E/F$ be a field extension; if there exists a finite set $S=\{\alpha_1,\cdots,\alpha_n\}\subseteq E$ such that $E=F(S)$ holds, then $E$ is called a **finitely generated extension** of the field $F$, also denoted $F(\alpha_1,\cdots,\alpha_n)$.

???+ abstract "Simple extension"
    Let $E/F$ be a field extension; if there exists $\alpha\in E$ such that $E=F(\alpha)$ holds, then the field $E$ is called a **simple extension** of the field $F$. Here, the element $\alpha$ is called a **primitive element** of this simple extension.

???+ example "Example"
    These examples are all obtained by adjoining elements of $\mathbf C$ to $\mathbf Q$.
    
    1.  For a squarefree integer $D\neq 0,1$, the quadratic field $\mathbf Q(\sqrt D)$ is the simple extension obtained by adjoining $\sqrt D\in\mathbf C\setminus\mathbf Q$ to the field $\mathbf Q$. Its degree of extension is $2$, because $\{1,\sqrt D\}$ forms a basis.
    2.  The field $\mathbf Q(\sqrt 2,\sqrt 3)$ is the extension obtained by adjoining $\sqrt 2$ and $\sqrt 3$ to the field $\mathbf Q$. Of course, $\mathbf Q(\sqrt 2,\sqrt 3)=\mathbf Q(\sqrt 2)(\sqrt 3)=\mathbf Q(\sqrt 3)(\sqrt 2)$, i.e. the final extension is independent of the order and manner in which the elements are adjoined. This is also a simple extension, because $\mathbf Q(\sqrt 2,\sqrt 3)=\mathbf Q(\sqrt 2+\sqrt 3)$. Its degree of extension is $4$, because $\{1,\sqrt 2,\sqrt 3,\sqrt 6\}$ forms a basis.
    3.  The field $\mathbf Q(\pi)$ is also a simple extension, where $\pi$ is the ratio of a circle's circumference to its diameter. It is an infinite extension, because $\mathbf Q[\pi]\subseteq \mathbf Q(\pi)$ already has a basis $\{1,\pi,\pi^2,\cdots\}$.
    4.  The field $\mathbf Q(\pi,\mathrm e)$ is a finitely generated extension, but not a simple extension. Here, $\pi$ is the ratio of a circle's circumference to its diameter, and $\mathrm e$ is the base of the natural logarithm.

These examples show that the properties of simple extensions can differ greatly. This depends on the properties of the adjoined element.

### Algebraic extension

In order to analyze all the situations that may arise when adjoining an element to a field, one may, in imitation of the earlier discussion of the characteristic of a field, examine the ring homomorphism from the polynomial ring $F[x]$ to the extension $E/F$. Here $F[x]$ plays the role of the ring of integers $\mathbf Z$ earlier: it is precisely the "prototype" of the structure closed under addition, subtraction, and multiplication obtained by adjoining an indeterminate $x$ to the field $F$[^polynomial-universal].

Let the ring homomorphism $\varphi:F[x]\rightarrow E$ satisfy that $\varphi$ restricted to $F$ is the identity map, and $\varphi(x)=\alpha$, i.e. the indeterminate is mapped to some element of the extension $E$. In this case, because the image $\varphi(F[x])=F[\alpha]$ is necessarily an integral domain, the kernel $\ker\varphi$ of the homomorphism is necessarily a prime ideal of the polynomial ring $F[x]$. The polynomial ring over a field is a principal ideal domain, so it necessarily has the form $(f(x))$, where $f(x)=0$ or $f(x)$ is an irreducible element of $F[x]$. We discuss this as follows:

1.  When the kernel $\ker\varphi=\{0\}$, the polynomial ring $F[x]$ is embedded in $E$, and its image $F[\alpha]$ is an integral domain. Therefore, the smallest field in $E$ containing both $F$ and $\alpha$ is the field of fractions of $F[\alpha]$, i.e. $F(\alpha)$. This notation can be interpreted either as the result of substituting $\alpha$ for the indeterminate in the field of rational fractions $F(x)$, or as the simple extension of the field $F$ generated by $\alpha$: these two interpretations give consistent results in this context;

2.  When the kernel $\ker\varphi=(f(x))$ and $f(x)$ is an irreducible element, then $\varphi(f(x))=f(\alpha)=0$ holds, i.e. $\alpha\in E$ is a root of the polynomial $f(x)$ over $F$. Because $F$ is a field, we may assume $f(x)$ is a monic polynomial. In this case the image of the homomorphism $\varphi$ is the field $F(\alpha)$, so we have

    $$
    F[x]/(f(x))\cong F(\alpha).
    $$

    This can further be divided into two cases:

    1.  If $f(x)$ is a first-degree polynomial, i.e. $f(x)=x-\alpha$, then $\alpha\in F$, so the extension $F(\alpha)=F$ is trivial;
    2.  In the remaining cases, $f(x)$ is an irreducible polynomial of degree greater than one, and $\alpha\in E\setminus F$; in this case the image $F[\alpha]$ is already a field containing $F$ and $\alpha$, so it is $F(\alpha)$, i.e. the extension of $F$ generated by $\alpha$, and $F(\alpha)\supset F$ is not trivial.

These discussions motivate the following definition:

???+ abstract "Algebraic and transcendental elements"
    For an extension $E/F$, if an element $\alpha\in E$ is a root of some nonzero polynomial $f(x)$ over $F$, then $\alpha$ is called an **algebraic element** over $F$; otherwise, the element $\alpha$ is called a **transcendental element** over $F$.

???+ abstract "Minimal polynomial"
    For an algebraic element $\alpha$ over the field $F$, the monic polynomial $f(x)$ of least degree having $\alpha$ as a root is called its **minimal polynomial**.

The minimal polynomial here is precisely the irreducible polynomial $f(x)$ in the earlier analysis. Of course, one can also directly prove that minimal polynomials are all irreducible. The minimality of the minimal polynomial $f(x)$ means that as long as a polynomial over the field $F$ has $\alpha$ as a root, it must factor out the factor $f(x)$.

???+ example "Example"
    1.  $\sqrt 2$ is an algebraic element over $\mathbf Q$, with minimal polynomial $x^2-2$.
    2.  $\sqrt 2$ is an algebraic element over $\mathbf R$, with minimal polynomial $x-\sqrt 2$.
    3.  $\pi$ is a transcendental element over $\mathbf Q$.
    4.  In general, an algebraic element over $\mathbf Q$ is called an **algebraic number**, and a transcendental element is called a **transcendental number**. In particular, if the minimal polynomial of an algebraic number is a monic polynomial, it is called an **algebraic integer**. The set of all algebraic integers in an algebraic extension forms a ring. For example, the algebraic integers in the quadratic field $\mathbf Q(\sqrt{D})$ form the quadratic integer ring $\mathbf Z[\omega]$. For the meaning of the notation here, see the [quadratic integer ring](./ring-theory.md#example-quadratic-integer-ring) page.

???+ abstract "Algebraic and transcendental extensions"
    For an extension $E/F$, if every element of the field $E$ is an algebraic element over $F$, then the field $E$ is called an **algebraic extension** over $F$; otherwise, the field $E$ is called a **transcendental extension** over $F$.

The result of a simple extension can be divided into two classes, depending on the properties of the adjoined element. When the adjoined element is transcendental, the simple extension is always isomorphic to the field of rational fractions. In this case, there is no possibility of further simplification. But when the adjoined element is algebraic, the simple extension is in fact $F[\alpha]$, i.e. the result of directly substituting $\alpha$ for the indeterminate $x$ in the polynomial ring $F[x]$. From an elementary viewpoint, compared with the transcendental case, the elements of the extension field can now have no denominators; this means that, analogous to the process of "rationalizing the denominator" in elementary arithmetic, this is always possible in a simple algebraic extension. Because the extension fields encountered in competitive programming are mainly simple algebraic extensions, the next section discusses their computation in more detail.

The importance of simple algebraic extensions is also reflected in the following theorem:

???+ note "Theorem"
    A field extension is a finite extension if and only if it is a finitely generated algebraic extension.

??? note "Proof"
    Let $F$ be a field and $E=F(\alpha_1,\cdots,\alpha_n)$ be a finitely generated algebraic extension over the field, i.e. the $\alpha_i$ are all algebraic elements over $F$. Let $E_i=F(\alpha_1,\cdots,\alpha_i)$, so $E_0=F$ and $E_n=E$. Note that $\alpha_i$ is necessarily an algebraic element over $E_{i-1}$, because the minimal polynomial of $\alpha_i$ over the field $F$ is also a polynomial over $E_{i-1}$; moreover, the degree of the minimal polynomial of $\alpha_i$ over $E_{i-1}$ is necessarily no greater than the degree of the minimal polynomial of $\alpha_i$ over the field $F$. Therefore, $[E_i:E_{i-1}]$ is necessarily finite, and by the multiplicative principle for degrees of field extensions, $[E:F]=\prod_{i=1}^n[E_i:E_{i-1}]$ is also finite. Conversely, starting from $E_0=F$, for the already constructed $E_i$, one can each time choose an element $\alpha_{i+1}$ from $E\setminus E_i$ and adjoin it to $E_i$, obtaining the extension field $E_{i+1}=E_i(\alpha_{i+1})$, until $E_n=E$. Because the degree of the extension keeps decreasing, this process necessarily terminates in finitely many steps. Therefore, a finite extension is necessarily a finitely generated algebraic extension.

This means that to understand the properties of finite extensions, it suffices to understand simple algebraic extensions, because a finite extension can always be obtained through finitely many simple algebraic extensions.

### Structure and computation of simple algebraic extensions

In this section, let $F$ be a number field, $E$ be an extension field of it, and $\alpha\in E\setminus F$ be an algebraic element over the field $F$. Let the minimal polynomial of $\alpha$ be $f(x)$, and suppose the polynomial $f(x)$ is a monic polynomial of degree $n$, i.e.

$$
f(x)=x^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,
$$

where $a_0,a_1,\cdots,a_{n-1}\in F$ and $f(x)$ is irreducible over $F$.

The isomorphism $F(\alpha)\cong F[x]/(f(x))$ shows that operations in the extension field $F(\alpha)$ are computations of polynomials modulo $f(x)$. By polynomial division with remainder, it suffices to consider the congruence classes of all polynomials of degree less than $n=\deg f(x)$. For these polynomials, a natural basis is $\{1,\alpha,\cdots,\alpha^{n-1}\}$. Therefore, we have the following conclusion:

???+ note "Theorem"
    Under the assumptions of this section, the extension field $F(\alpha)$ can be written as
    
    $$
    F(\alpha)=\{\lambda(\alpha)=\lambda_0+\lambda_1\alpha+\cdots+\lambda_{n-1}\alpha^{n-1}:\lambda_0,\lambda_1,\cdots,\lambda_{n-1}\in F\}.
    $$
    
    Here, $\lambda(x)$ ranges over all polynomials of degree less than $n$. Therefore, the degree of extension $[F(\alpha):F]=n$, i.e. the degree of the minimal polynomial of $\alpha$. In the extension field, the addition of elements $\lambda(\alpha)$ and $\mu(\alpha)$ is the addition of polynomials, i.e. adding coefficients at corresponding positions; the multiplication of elements $\lambda(\alpha)$ and $\mu(\alpha)$ gives a result that can be written as $\rho(\alpha)$, where $\rho(x)$ is the remainder of the product $\lambda(x)\mu(x)$ divided by $f(x)$.

Of course, as a field, one can also compute division of elements in $F(\alpha)$. By the multiplication process described in the theorem, this amounts to solving a [linear congruence equation](../number-theory/linear-equation.md) over the polynomial ring. Analogous to the approach for integers, to compute the quotient $\lambda(\alpha)/\mu(\alpha)$, one can first determine the multiplicative inverse of $\mu(\alpha)$, then multiply by $\lambda(\alpha)$. To compute the multiplicative inverse of $\mu(\alpha)$, it suffices to solve the congruence equation $\mu(x)\xi(x)\equiv 1\pmod{f(x)}$. This can be accomplished by the extended Euclidean algorithm.

Below, we understand the details of the computation through several concrete examples.

???+ example "Example"
    Consider the extension field $\mathbf Q(\alpha)$, where $\alpha$ is a root of the equation $x^3-2x-2=0$. We want to compute the value of
    
    $$
    \frac{1+\alpha}{1+\alpha+\alpha^2}.
    $$
    
    The first step is to compute the inverse of $1+\alpha+\alpha^2$, i.e. to solve the congruence equation
    
    $$
    (x^2+x+1)\xi(x)+(x^3-2x-2)\nu(x)=1.
    $$
    
    We apply the extended Euclidean algorithm to this. First perform the Euclidean division, giving the following process:
    
    $$
    \begin{aligned}
    x^3-2x-2 &= (x-1)(x^2+x+1)+(-2x-1),\\
    x^2+x+1 &= \left(-\frac12x-\frac14\right)(-2x-1)+\frac34,\\
    -2x-1 &= \left(-\frac{8}{3}x-\frac{4}{3}\right)\frac{3}{4}.
    \end{aligned}
    $$
    
    Then compute the coefficients in the congruence equation, giving
    
    $$
    \begin{aligned}
    \frac{3}{4}
    &=(x^2+x+1)+\left(\frac12x+\frac14\right)(-2x-1)\\
    &=(x^2+x+1)+\left(\frac12x+\frac14\right)\left((x^3-2x-2)-(x-1)(x^2+x+1)\right)\\
    &=\left(-\frac12x^2+\frac14x+\frac54\right)(x^2+x+1)+\left(\frac12x+\frac14\right)(x^3-2x-2).
    \end{aligned}
    $$
    
    Therefore, the solution of the equation is
    
    $$
    \xi(x)=-\frac23x^2+\frac13x+\frac53,\ \nu(x)=\frac23x+\frac13.
    $$
    
    This shows that the inverse of $1+\alpha+\alpha^2$ is
    
    $$
    -\frac23\alpha^2+\frac13\alpha+\frac53.
    $$
    
    The second step is to compute the product of the inverse and $1+\alpha$. For this, we have
    
    $$
    \begin{aligned}
    (1+\alpha)\left(-\frac23\alpha^2+\frac13\alpha+\frac53\right)
    &=-\frac23\alpha^3-\frac13\alpha^2+2\alpha+\frac53\\
    &=-\frac23(2\alpha+2)-\frac13\alpha^2+2\alpha+\frac53\\
    &=-\frac13\alpha^2+\frac23\alpha+\frac13.
    \end{aligned}
    $$
    
    This is the final answer.

In the example, only the condition that $\alpha$ is a root of the equation was used; it was not specified as any particular root. The polynomial $x^3-2x-2=0$ has one real root and a pair of conjugate complex roots in the complex field $\mathbf C$, and the extension fields obtained by adjoining any one of them to the rational field $\mathbf Q$ are isomorphic. That is to say, these three distinct roots are indistinguishable from an algebraic point of view.

In general, for an irreducible polynomial $f(x)$ over a field $F$, there are distinct roots $\alpha\neq\beta$ in the extension field, and these roots exhibit the same algebraic properties when making a simple extension of the field $F$ respectively; these roots are called **conjugate** to one another. The usual notion of conjugation over the complex field is precisely the special case of this concept for the field extension $\mathbf C/\mathbf R$.

???+ example "Example"
    Consider the extension field $\mathbf F_2(\alpha)$, where $\alpha$ is a root of the equation $x^2+x+1=0$. In general, for $a+b\alpha$ and $c+d\alpha$, we have the operation rules
    
    $$
    \begin{aligned}
    (a+b\alpha)+(c+d\alpha)&=(a+c)+(b+d)\alpha,\\
    (a+b\alpha)(c+d\alpha)&=ac+(ad+bc)\alpha+bd\alpha^2\\
    &=(ac+bd)+(ad+bc+bd)\alpha.
    \end{aligned}
    $$
    
    This provides operation rules similar to those over the complex field. Most readers are unfamiliar with such a root $\alpha$, but this does not prevent us from performing operations on the elements of such a field. In fact, $[\mathbf F_2(\alpha):\mathbf F_2]=2$, so as a linear space $|\mathbf F_2(\alpha)|=4$, i.e. what we obtain is a finite field of size $4$. As we will see shortly, all finite fields are constructed in this way.

In small-scale computations, the operation of taking the modulus of a monic polynomial $f(x)$ can usually be carried out by substituting

$$
x^n=-a_{n-1}x^{n-1}-\cdots-a_1x-a_0
$$

to reduce the degree of the target polynomial. Moreover, for low-degree extensions, one can often directly compute the operation rules for the coefficients, using an implementation similar to a complex-number class without having to compute the modulus and so on every time.

As an instance of a simple algebraic extension, one may refer to the [reference implementation](#reference-implementation) of finite fields below.

The algorithm described here can only handle cases where the degree of extension is relatively low in practice, which is sufficient for the vast majority of applications in competitive programming. For cases where the degree of extension is high enough to become a complexity bottleneck, one should adopt appropriate polynomial techniques ([fast Fourier transform](../poly/fft.md), [number-theoretic transform](../poly/ntt.md), [polynomial division and modulo](../poly/elementary-func.md#多项式除法--取模), [polynomial Euclidean](../poly/intro.md#因式分解和欧几里得), etc.) to speed up the computation.

### Splitting field

The above has given a detailed discussion of the structure of simple algebraic extensions. But such extensions are often not sufficient:

???+ example "Example"
    Consider the extension $\mathbf Q(\sqrt[3]{2})/\mathbf Q$. The minimal polynomial of the algebraic element $\sqrt[3]{2}$ over the field $\mathbf Q$ is $x^3-2$. In the complex field $\mathbf C$, the polynomial $x^3-2$ has three roots, namely $\sqrt[3]{2},\sqrt[3]{2}\omega,\sqrt[3]{2}\omega^2$, where $\omega=\mathrm{e}^{2\pi\mathrm{i}/3}$ is a primitive cube root of $1$. Although $\mathbf Q(\sqrt[3]{2})\cong\mathbf Q(\sqrt[3]{2}\omega)\cong\mathbf Q(\sqrt[3]{2}\omega^2)$, $\mathbf Q(\sqrt[3]{2})$ does not contain the other two roots, which makes an operation like $\sqrt[3]{2}+\sqrt[3]{2}\omega$ already impossible to carry out. To fully examine these three roots, one needs to make a further extension of the field $\mathbf Q(\sqrt[3]{2})$, i.e. extend to $\mathbf Q(\sqrt[3]{2},\sqrt[3]{2}\omega,\sqrt[3]{2}\omega^2)$.
    
    As explained earlier, to make such an extension, it suffices to make a simple extension for each element one by one. It should be noted that the minimal polynomial of $\sqrt[3]{2}\omega$ over the field $\mathbf Q$ and over the field $\mathbf Q(\sqrt[3]{2})$ are not the same: the former is $x^3-2\in\mathbf Q[x]$, while the latter is $x^2+\sqrt[3]{2}x+\sqrt[3]{4}\in \mathbf Q(\sqrt[3]{2})[x]$, because
    
    $$
    x^3-2 = (x-\sqrt[3]{2})(x^2+\sqrt[3]{2}x+\sqrt[3]{4}).
    $$
    
    The original minimal polynomial factors out a first-degree factor after the field is extended, so the minimal polynomial of the remaining roots has lower degree than the minimal polynomial over the original field. The process of continually extending the field is precisely the process of the polynomial continually "splitting". Therefore, at each simple extension, one needs to re-determine the minimal polynomial.

Adjoining all the roots of a polynomial to a field yields the splitting field of the polynomial.

???+ abstract "Split"
    Let $F$ be a field. If a polynomial $f(x)$ can be factored in $F[x]$ into a product of a sequence of first-degree factors, then the polynomial $f(x)$ is said to **split** over the field $F$.

???+ abstract "Splitting field"
    For a polynomial $f(x)$ over a field $F$, if an extension $E/F$ satisfies that $f(x)$ splits over the field $E$ but does not split over any proper subfield of $E$, then the field $E$ is called a **splitting field** of the polynomial $f(x)$.

It can be proved that, just like a simple extension, the splitting field of a given polynomial is uniquely determined up to isomorphism, independent of the specific method of construction. A splitting field is always a finite extension.

???+ abstract "Normal extension"
    For an algebraic extension $E/F$, if the minimal polynomial of every $\alpha\in E$ splits over $E$, then the field $E$ is called a **normal extension** of the field $F$.

Normal extensions play a fundamental role in Galois theory.

### Algebraically closed field

Most of the concepts of extensions mentioned earlier require, in principle, working within a field larger than the extension. Although for the case of simple extensions, the polynomial ring allows an extension of a field to be constructed without relying on a larger field, there is no such means for the general case. For the rational field $\mathbf Q$ and the real field $\mathbf R$, one can always assume that algebraic extensions are contained within the complex field $\mathbf C$. For finite fields, there is no analogous known field. In fact, for all fields there exists an algebraic closure, so that all algebraic extensions over the field can be assumed to take place within the algebraic closure. This completely resolves this problem.

???+ abstract "Algebraic closure"
    For a field $F$, if the field $\overline F$ is an algebraic extension of the field $F$, and all $f(x)\in F[x]$ split over $\overline F$, then the field $\overline F$ is called an **algebraic closure** of the field $F$.

The algebraic closure is a normal extension over the field. Its construction essentially amounts to adjoining the roots of all possible polynomials to the field. Moreover, like a splitting field, the algebraic closure of a given field is also unique up to isomorphism.

???+ note "Theorem"
    Every field $F$ has an algebraic closure.

??? note "Proof"
    The difficulty of the proof comes from set theory. Here we cite a proof due to Artin.
    
    The first part of the proof starts from $F$ and constructs an extension $K_1/F$ such that every polynomial over $F$ has at least one root in $K_1$. For the field $F$, consider the multivariate polynomial ring[^multi-poly-ring] $R=F[\cdots,x_f,\cdots]$, where the subscript of the indeterminate $x_f$ ranges over all monic polynomials over $F$. Then, the ideal generated by all $f(x_f)$ is denoted $I$. First, $I\neq R$, so a maximal ideal $M\supseteq I$ exists. Otherwise, if $1\in I$, there must exist finitely many monic polynomials $f_i$ over the field $F$ and corresponding elements $g_i$ of the ring $R$ such that $g_1f_1(x_{f_1})+\cdots+g_kf_k(x_{f_k})=1$ holds. Let $F(\alpha_1,\cdots,\alpha_k)$ be the algebraic extension obtained by adjoining to $F$ the roots $\alpha_i$ of $f_i(x)$; then in $F(\alpha_1,\cdots,\alpha_k)$, substituting $\alpha_i$ for each $x_{f_i}$ in the identity obtained above, and substituting $0$ for all other indeterminates $x_f$ appearing in the various $g_i$, we obtain the equation $0=1$ over $F(\alpha_1,\cdots,\alpha_k)$, a contradiction. Therefore, $I\neq R$, and the construction of the maximal ideal $M$ is valid. In this case the quotient ring $R/M$ is a field, denoted $K_1$, and every monic polynomial $f(x)$ over $F$ has a root $\overline{x_f}$ in $K_1$.
    
    The second part of the proof inductively obtains an algebraically closed field $K$ (see the definition below) containing $F$. Repeating the above construction, based on the field $K_i$ one can construct a field $K_{i+1}$ such that every polynomial over $K_i$ has at least one root in $K_{i+1}$. Moreover, $K_i$ is naturally embedded in $K_{i+1}$, so one can define their union $K=\bigcup_{i=1}^\infty K_i$. It is easy to verify that this is also a field, and the coefficients of any polynomial over $K$ must all be contained in some $K_i$, so one of its roots must appear in $K_{i+1}\subseteq K$. This shows that every polynomial over $K$ has at least one root over $K$, so $K$ is an algebraically closed field.
    
    Finally, let the set of all algebraic elements over $F$ in $K$ be denoted $\overline F$. It is obviously a field; because for any $\alpha,\beta\in\overline F$, we have $\alpha\pm\beta,\alpha\beta,\alpha/\beta\in F(\alpha,\beta)\subseteq\overline F$. It is also an algebraic extension of $F$, because its elements are all algebraic elements over $F$. For a polynomial $f(x)$ over $F$, all of its roots are algebraic elements over $F$, so they are also in $\overline F$, and hence it must factor into a product of first-degree factors. This shows that $\overline F$ is an algebraic closure over $F$.

???+ example "Example"
    1.  The algebraic closure of the real field $\mathbf R$ is the complex field $\mathbf C$.
    2.  The algebraic closure of the rational field $\mathbf Q$ is the set of all algebraic numbers (i.e. the algebraic elements in the field extension $\mathbf C/\mathbf Q$), denoted $\overline{\mathbf Q}$.

Every algebraic extension of an algebraic closure is trivial. Such a field is called an algebraically closed field.

???+ abstract "Algebraically closed field"
    If every non-constant polynomial $f(x)$ over a field $F$ has at least one root $\alpha\in F$, then the field $F$ is called an **algebraically closed field**.

In fact, it has the following equivalent definitions:

???+ note "Theorem"
    For a field $F$, the following properties are all equivalent:
    
    1.  The field $F$ is algebraically closed;
    2.  Every polynomial $f(x)$ over the field $F$ splits;
    3.  The only irreducible polynomials over the field $F$ are the first-degree polynomials;
    4.  The field $F$ has no nontrivial algebraic extension;
    5.  The field $F$ has no nontrivial finite extension;
    6.  The field $F$ is the algebraic closure of some field.

??? note "Proof"
    The equivalence of the first five properties is obvious; just examine the definitions. For the sixth, an algebraically closed field is obviously its own algebraic closure, because it has no nontrivial algebraic extension; conversely, we prove that the algebraic closure of a field $F$ must be an algebraically closed field. Let $\overline F$ be the algebraic closure of the field $F$, and $f(x)$ be a polynomial over $\overline F$. Let $\alpha$ be a root of $f(x)$ in the splitting field of $f(x)$, and let the set of nonzero coefficients of $f(x)$ be $S\subseteq\overline F$. Then, because $F(S)(\alpha)=F(S\cup\{\alpha\})$ is a finite extension, $\alpha$ must also be an algebraic element over $F$, so by the definition of algebraic closure, the minimal polynomial of $\alpha$ over $F$ splits over the field $\overline F$, so $\alpha\in\overline F$. This shows that every polynomial over $\overline F$ has at least one root.

Finally, the [fundamental theorem of algebra](../poly/fundamental.md)[^fundamental-algebra] states that $\mathbf C$ is an algebraically closed field. The irreducible polynomials over the real field $\mathbf R$ are at most quadratic, or equivalently, the algebraic extensions over it are at most quadratic extensions, precisely because the largest field obtainable through algebraic extension is $\mathbf C$.

### Separable extension

The concept of a splitting field guarantees that for any polynomial over a field, there is always an extension field that includes all its roots, and the splitting field gives precisely the smallest such extension field. The properties of a polynomial are closely connected with the properties of its splitting field. But if one wishes to study the properties of a polynomial through its splitting field, then a first problem to face is that the splitting field of a polynomial is independent of the multiplicities of the roots of the polynomial. Therefore, if possible, one should consider a "simplest representation" of the polynomial in some sense. Motivated by this, a polynomial that has no repeated roots even in the algebraic closure of the field is called a separable polynomial.

???+ abstract "Separable polynomial"
    For a polynomial $f(x)$ over a field $F$, if $f(x)$ has no repeated roots in the algebraic closure $\overline F$ of $F$, i.e. when it factors into a product of first-degree factors there are no repeated factors, then $f(x)$ is called **separable**.

Because one always extends to the algebraic closure of the field $F$ for the discussion, whether a polynomial is separable is in fact independent of the choice of the field $F$. But because the coefficients of the polynomial are in $F$, one should give a criterion that allows one to determine, over the field $F$, whether a polynomial is separable, without having to explicitly construct its extension field.

Readers familiar with analysis know that whether a polynomial function has a repeated root can be determined through its derivative: a repeated root of a polynomial function is also a root of its derivative. Although polynomials and polynomial functions are not identical concepts, the method for determining whether a polynomial function has a repeated root can be transferred analogously to polynomials. The derivative of a polynomial can be defined formally as follows:

???+ abstract "Formal derivative"
    The **(formal) derivative** of a polynomial
    
    $$
    f(x)=a_0+a_1x+a_2x^2+\cdots+a_{n-1}x^{n-1}+a_nx^n=\sum_{i=0}^na_ix^i
    $$
    
    over a field $F$, denoted $Df(x)$, is defined as the polynomial
    
    $$
    Df(x)=a_1+2a_2x+\cdots+(n-1)a_{n-1}x^{n-1}+na_nx^{n-1}=\sum_{i=1}^nia_ix^{i-1}.
    $$

This definition applies to polynomials over all fields, independent of any topological structure; the derivative operator $D$ here merely maps one polynomial to another. Moreover, one can verify by comparing coefficients that the common rules of differentiation, such as $D(f(x)g(x))=(Df(x))g(x)+f(x)(Dg(x))$, still hold for the formal derivative.

Furthermore, to check whether the polynomial $f(x)$ and its derivative $Df(x)$ have a common root in the splitting field, one need not explicitly construct this splitting field, but can instead determine it through their greatest common factor; this is because the roots of a polynomial always appear in its minimal polynomial, and a repeated root means the corresponding minimal polynomial factor is also repeated. Thus, the criterion for having a repeated root is as follows:

???+ note "Theorem"
    For a polynomial $f(x)$ over a field $F$, if $f(x)$ has a repeated root $\alpha$, then the derivative $Df(x)$ also has the same root $\alpha$. Furthermore, the necessary and sufficient condition for the polynomial $f(x)$ to be separable is that $f(x)$ and its derivative $Df(x)$ are coprime, i.e. $\gcd(f(x),Df(x))=1$.

??? note "Proof"
    First, because division with remainder is preserved in the extension field, and the result of the Euclidean algorithm is also independent of the choice of extension field, it suffices to discuss their common factor in the splitting field. Thus, let $\alpha$ be a root of $f(x)$ of multiplicity $k>1$; then in the splitting field there is a factorization $f(x)=(x-\alpha)^kg(x)$, so its derivative $Df(x)=k(x-\alpha)^{k-1}g(x)+(x-\alpha)^kDg(x)$ also has the root $\alpha$. Conversely, if $f(x)$ and $Df(x)$ both have the root $\alpha$, then for the factorization $f(x)=(x-\alpha)g(x)$ in the splitting field, we have $Df(x)=(x-\alpha)Dg(x)+g(x)$, so $\alpha$ is also a root of $g(x)$, and hence $\alpha$ is a repeated root of $f(x)$. This proves the first part of the theorem. Furthermore, the polynomial $f(x)$ having a repeated root $\alpha$ is equivalent to $x-\alpha$ being a factor of $\gcd(f(x),Df(x))$. So the polynomial $f(x)$ being inseparable is equivalent to $\gcd(f(x),Df(x))$ having degree at least one.

A polynomial over a field can always be factored into a product of several irreducible polynomials. Because (up to associates) distinct irreducible polynomials always have distinct roots, the repetition of roots is naturally connected to the repetition of the corresponding polynomial factors. So, if the factorization of a polynomial has no repeated irreducible factors, can one conclude that the polynomial is separable? In other words, are all irreducible polynomials separable? Unfortunately, in the general case, one cannot obtain an affirmative answer. The problem occurs in fields of finite characteristic.

For an irreducible polynomial $f(x)$ over a field $F$, the polynomial $\gcd(f(x),Df(x))$, as a factor of $f(x)$, can only be one of two cases, namely $1$ or $f(x)$. In the former case, the polynomial $f(x)$ is naturally separable; the problem occurs in the latter case. But since the definition of the derivative already guarantees that $Df(x)=0$ or $\deg Df(x)<\deg f(x)$, for the polynomial $f(x)$ to be a factor of $Df(x)$ can only mean $Df(x)=0$. This is possible in fields of finite characteristic.

For a field $F$ of characteristic $p$, if $Df(x)=0$, then all the nonzero coefficients of the polynomial can only occur in terms whose degree is exactly a multiple of $p$, i.e. the polynomial $f(x)$ can be written as

$$
f(x)=a_0+a_px^p+a_{2p}x^{2p}+\cdots+a_{(k-1)p}x^{(k-1)p}+a_{kp}x^{kp}.
$$

If there really exists a polynomial $f(x)$ over the field $F$ that is both irreducible and inseparable, then it can only have this form. But if every element of the field $F$ always has a $p$-th root, i.e. for each coefficient $a_{jp}$ there exists $b_j\in F$ such that $a_{jp}$ can be written in the form $b_j^p$, then, by the Frobenius endomorphism, we always have

$$
\begin{aligned}
f(x)&=a_0+a_px^p+a_{2p}x^{2p}+\cdots+a_{(k-1)p}x^{(k-1)p}+a_{kp}x^{kp}\\
&=b_0^p+b_1^px^p+b_2^px^{2p}+\cdots+b_{k-1}^px^{(k-1)p}+b_k^px^{kp}\\
&=\left(b_0+b_1x+b_2x+\cdots+b_{k-1}x^{k-1}+b_kx^k\right)^p.
\end{aligned}
$$

Therefore, there is no irreducible polynomial of this form over such a field $F$. Hence, over such a field, all irreducible polynomials are separable. Such a field is called a perfect field.

???+ abstract "Perfect field"
    If every irreducible polynomial over a field $F$ is a separable polynomial, then it is called a **perfect field**.

For a perfect field, the concept of a separable polynomial and the concept of a polynomial with no square factor in the unique factorization are identical.

???+ note "Theorem"
    Let the field $F$ be a perfect field; then a polynomial over $F$ is separable if and only if it can be written as a product of several distinct (up to associates) irreducible polynomials.

The discussion of this section is in fact already sufficient to give a method for removing repeated factors of a polynomial, which is a key step in polynomial factorization algorithms. But this is beyond the scope of this article; interested readers may consult the related material at the end of the article.

These discussions in fact also give a characterization of perfect fields:

???+ note "Theorem"
    A field $F$ is a perfect field if and only if the characteristic of the field $F$ is zero, or the characteristic of the field $F$ is $p$ and every element $x\in F$ has a $p$-th root (i.e. the Frobenius endomorphism is also an automorphism).

The rational field $\mathbf Q$ and the finite fields $\mathbf F_q$ to be discussed below are all perfect fields.

For the case where a field is not a perfect field, there indeed exist inseparable irreducible polynomials.

??? example "Example"
    Consider the polynomial $x^2-t$ over the field of rational fractions $\mathbf F_2(t)$ of $\mathbf F_2$. Because $\mathbf F_2(t)$ is the field of fractions of the unique factorization domain $\mathbf F_2[t]$, and $t$ is a prime element in $\mathbf F_2[t]$, applying Eisenstein's criterion to the prime element $t$ shows that $x^2-t$ is irreducible in $\mathbf F_2[t]$, and hence also irreducible in $\mathbf F_2(t)$. But its derivative is $0$, so $x^2-t$ is not separable. In fact, in the extension field $\mathbf F_2(t)(\sqrt t)$, it has the double root $\sqrt t$.

Finally, we return to the discussion of field extensions.

???+ abstract "Separable extension"
    For an algebraic extension $E/F$, if the minimal polynomial of every $\alpha\in E$ is a separable polynomial, then the field $E$ is called a **separable extension** of the field $F$.

Every algebraic extension over a perfect field is a separable extension. This can also serve as an equivalent definition of a perfect field.

If an algebraic extension is both a normal extension and a separable extension, it is also called a Galois extension. In a Galois extension, no irreducible polynomial has a repeated root, and the number of roots is exactly equal to the degree of the polynomial, so permutations of the roots can fully reflect the properties of the field extension and the polynomial. Such extensions provide the cornerstone for establishing Galois theory. Interested readers may consult the related material at the end of the article.

## Cyclotomic field

As a simple example of a field extension, this section discusses cyclotomic fields. Another simple example of a field extension is the [quadratic field](../number-theory/quadratic.md).

### Group of roots of unity

In the complex field $\mathbf C$, the roots of the polynomial $x^n=1$ are called **$n$-th roots of unity**. Denote $\zeta_n=\mathrm{e}^{2\pi\mathrm{i}/n}$. Then, all $n$-th roots of unity form the set $C_n=\{\zeta_n^k:k\in\mathbf Z\}$. Under multiplication, $C_n$ forms a cyclic group of order $n$, which can be denoted $\langle\zeta_n\rangle$, called the group of $n$-th roots of unity. The generators of the group $C_n$, i.e. those elements whose order is exactly $n$, are called **primitive $n$-th roots of unity**. The set of primitive $n$-th roots of unity $P_n=\{\zeta_n^k:k\in\mathbf Z,k\perp n\}$ has exactly $\varphi(n)$ elements; here, $\varphi(n)$ is the [Euler's totient function](../number-theory/euler-totient.md). Classifying the elements of the group of roots of unity $C_n$ according to their order gives the following decomposition:

$$
C_n=\bigcup_{d|n}P_d.
$$

Counting the elements on both sides gives the identity $n=\sum_{d\mid n}\varphi(d)$.

### Cyclotomic field

A cyclotomic field is the extension field obtained by adjoining roots of unity to the rational field.

???+ abstract "Cyclotomic field"
    The extension field $\mathbf Q(\zeta_n)$ obtained by adjoining the complex $n$-th root of unity $\zeta_n=\mathrm{e}^{2\pi\mathrm{i}/n}$ to the rational field $\mathbf Q$ is called the **$n$-th cyclotomic field**.

Because all $n$-th roots of unity form the cyclic group $\langle\zeta_n\rangle$ under multiplication, the cyclotomic field $\mathbf Q(\zeta_n)$ also includes all these $n$-th roots of unity. In fact, $\mathbf Q(\zeta_n)$ is precisely the splitting field of the polynomial $x^n-1$ over the field $\mathbf Q$.

???+ note "Theorem"
    The cyclotomic field $\mathbf Q(\zeta_n)$ is the splitting field of the polynomial $x^n-1$ over the rational field $\mathbf Q$.

??? note "Proof"
    Let $F$ be the splitting field of the polynomial $x^n-1$ over the rational field $\mathbf Q$. Because $\mathbf Q(\zeta_n)$ contains all complex roots of the polynomial $x^n-1$, we have $F\subseteq\mathbf Q(\zeta_n)$. Conversely, because $\zeta_n\in F$, we necessarily have $\mathbf Q(\zeta_n)=F$. This shows $F=\mathbf Q(\zeta_n)$.

This can serve as an equivalent definition of the cyclotomic field. In fact, adjoining any primitive $n$-th root of unity to the cyclotomic field yields $\mathbf Q(\zeta_n)$.

### Cyclotomic polynomial

The cyclotomic field $\mathbf Q(\zeta_n)$ is a simple algebraic extension over the rational field $\mathbf Q$. By the analysis above, such a field is always isomorphic to the quotient ring of some polynomial ring. To obtain such an isomorphism, one needs to analyze the minimal polynomial $f(x)$ of $\zeta_n$. Because $\zeta_n$ is a root of $x^n-1$, $f(x)$ must be some factor of $x^n-1$. This shows that one needs to examine the factorization of the polynomial $x^n-1$ within $\mathbf Q[x]$. By Gauss's lemma, it can necessarily be factored in $\mathbf Z[x]$ into a product of several irreducible monic polynomials.

Because $\mathbf Q(\zeta_n)$ is a splitting field, the polynomial $x^n-1$ has the factorization:

$$
x^n-1=\prod_{\zeta\in C_n}(x-\zeta)=\prod_{d\mid n}\prod_{\zeta\in P_d}(x-\zeta).
$$

Because roots of unity of different orders have different algebraic properties, they cannot be roots of the same irreducible polynomial. Therefore, to examine the minimal polynomial of $\zeta_n$, it suffices to consider the factor

$$
\Phi_n(x)=\prod_{\zeta\in P_n}(x-\zeta)
$$

in the above factorization. The minimal polynomial of the root of unity $\zeta_n$ must be a factor of $\Phi_n(x)$. Moreover, $\Phi_n(x)$ so defined has the following properties:

???+ note "Theorem"
    $\Phi_n(x)$ is a monic polynomial with integer coefficients, and is irreducible in $\mathbf Z[x]$.

??? note "Proof"
    By definition, $\Phi_n(x)$ is obviously a monic polynomial. First, we prove $\Phi_n(x)\in\mathbf Z[x]$. By Gauss's lemma, the polynomial $x^n-1$ has the same factorization in $\mathbf Z[x]$ and $\mathbf Q[x]$, and each factor is a monic polynomial with integer coefficients. In this factorization, each factor $f(x)$ is irreducible over $\mathbf Q[x]$ and splits over $\mathbf Q(\zeta_n)$; all of its roots are $n$-th roots of unity and must have the same order, so these roots must all belong to a single $P_d$ and cannot lie separately in different $P_d$. This means that each factor $f(x)$ is a factor of some $\Phi_d(x)$. Therefore, $\Phi_n(x)$ can be written as a product of several monic polynomials with integer coefficients, and is necessarily also a monic polynomial with integer coefficients.
    
    Next, we prove that $\Phi_n(x)$ is irreducible in $\mathbf Z[x]$. Suppose it has a factorization $f(x)g(x)$, with $f(x)$ irreducible in $\mathbf Z[x]$; then it suffices to prove that $f(x)$ contains all primitive $n$-th roots of unity. That is, let $\zeta$ be a root of $f(x)$; we prove that for all $k\perp n$, $\zeta^k$ is also a root of $f(x)$; since $k$ can always be factored into a product of primes, it suffices to prove that for all primes $p\perp n$, $\zeta^p$ is a root of $f(x)$. Suppose not; then $\zeta^p$ is a root of $g(x)$. Therefore, $\zeta$ is a common root of the polynomials $f(x)$ and $g(x^p)$ in $\mathbf Z[x]$. Because $f(x)$ is the minimal polynomial of $\zeta$ over $\mathbf Q$, we must have $f(x)$ dividing $g(x^p)$; i.e. there exists $h(x)\in\mathbf Z[x]$ such that $g(x^p)=f(x)h(x)$. Reducing both sides modulo $p$ gives the equation $\overline{g}(x^p)=\overline{f}(x)\overline{h}(x)$ over $\mathbf F_p[x]$. Using the Frobenius endomorphism, we obtain $\overline{g}(x)^p=\overline{f}(x)\overline{h}(x)$. Because $\mathbf F_p[x]$ is also a unique factorization domain, $\overline{g}(x)$ and $\overline{f}(x)$ must have a nontrivial common factor, so $x^n-\overline 1=\overline{f}(x)\overline{g}(x)$ is inseparable over $\mathbf F_p$. But because $p\perp n$, its formal derivative $nx^{n-1}$ is coprime to itself, which contradicts its being inseparable. Therefore, we can prove that $\zeta^p$ must still be a root of $f(x)$, so $f(x)$ contains all primitive $n$-th roots of unity, i.e. it is $\Phi_n(x)$.

This shows that it is the minimal polynomial of $\zeta_n$, also called the **$n$-th cyclotomic polynomial**. The definition above shows that it has $\varphi(n)$ complex roots, and these complex roots are precisely all the primitive $n$-th roots of unity; here, $\varphi(n)$ is the [Euler's totient function](../number-theory/euler-totient.md). This also shows that $\mathbf Q(\zeta_n)/\mathbf Q$ is an extension of degree $\varphi(n)$.

The ring of algebraic integers in the cyclotomic field $\mathbf Q(\zeta_n)$ is $\mathbf Z[\zeta_n]$. In addition, when $\varphi(n)=2$, the cyclotomic field is a [quadratic extension](../number-theory/quadratic.md). Specifically, $\mathbf Q(\zeta_4)$ is the quadratic field $\mathbf Q(\sqrt{-1})$; $\mathbf Q(\zeta_3)$ and $\mathbf Q(\zeta_6)$ are the same, both being the quadratic field $\mathbf Q(\sqrt{-3})$.

Using cyclotomic polynomials, the polynomial $x^n-1$ has the unique factorization in $\mathbf Z[x]$

$$
x^n-1=\prod_{d\mid n}\Phi_d(x).
$$

Therefore, $(x^d-1)\mid(x^n-1)$ if and only if $d\mid n$. Moreover, applying [Möbius inversion](../number-theory/mobius.md) to this expression gives

$$
\Phi_d(x)=\prod_{d\mid n}(x^d-1)^{\mu(n/d)}.
$$

Using this expression, one can recursively compute all cyclotomic polynomials. Here we give examples of the first few cyclotomic polynomials, to help readers become familiar with them.

???+ example "Cyclotomic polynomials"
    The first $10$ cyclotomic polynomials are as follows:
    
    $$
    \begin{aligned}
    \Phi_1(x) &= x-1,\\
    \Phi_2(x) &= x+1,\\
    \Phi_3(x) &= x^2+x+1,\\
    \Phi_4(x) &= x^2+1,\\
    \Phi_5(x) &= x^4+x^3+x^2+x+1,\\
    \Phi_6(x) &= x^2-x+1,\\
    \Phi_7(x) &= x^6+x^5+x^4+x^3+x^2+x+1,\\
    \Phi_8(x) &= x^4+1,\\
    \Phi_9(x) &= x^6+x^3+1,\\
    \Phi_{10}(x) &= x^4-x^3+x^2-x+1.
    \end{aligned}
    $$
    
    An interesting fact is that, although it appears the coefficients of these cyclotomic polynomials can only be $0$ and $\pm1$, for general $n$ this conclusion is false. The first counterexample occurs at $\Phi_{105}(x)$, and it can be proved that as $n$ increases, its coefficients can take arbitrarily large values.

Using the Möbius inversion formula above, one can summarize the following properties to simplify the computation of $\Phi_n(x)$:

???+ note "Properties"
    For the cyclotomic polynomial $\Phi_n(x)$, we have:
    
    1.  If a prime $p\mid n$, then $\Phi_{pn}(x)=\Phi_n(x^p)$;
    2.  If a prime $p\perp n$, then $\Phi_{pn}(x)=\dfrac{\Phi_n(x^p)}{\Phi_n(x)}$;
    3.  In particular, if $n$ is odd, then $\Phi_{2n}(x)=\Phi_n(-x)$;
    4.  For a prime $p$, $\Phi_{p}(x)=1+x+\cdots+x^{p-1}$;
    5.  In particular, $\Phi_{2^k}(x)=x^{2^{k-1}}+1$.

These properties show that, in the computation of cyclotomic polynomials, the focus is on the cases where the degree is a squarefree odd number. And for this case, one can add prime factors one by one using property two; each addition of a prime factor requires only one polynomial division.

Cyclotomic polynomials also have many other properties.

???+ note "Theorem"
    Let $\Phi_n(x)$ be the cyclotomic polynomial for $n>1$, whose degree is $\varphi(n)$. Then, we have:
    
    1.  The polynomial $\Phi_n(x)$ is a palindromic polynomial: its coefficient of the $j$-th degree term equals its coefficient of the $\varphi(n)-j$-th degree term, i.e. $\Phi_n(x)=x^{\varphi(n)}\Phi_n(1/x)$;
    2.  The coefficient of the $\varphi(n)-1$-th degree term of the polynomial equals the Möbius function $-\mu(n)$;
    3.  If $n$ is a prime power $p^k$, then $\Phi_n(1)=p$; otherwise, $\Phi_n(1)=1$;
    4.  Let $b>1$ and $p$ be a prime factor of $\Phi_n(b)$; then $p\mid n$, or $n$ is the order of $b$ in the multiplicative group $(\mathbf Z/p\mathbf Z)^\times$, and these two cases cannot occur simultaneously.

??? note "Proof"
    For the first three properties, one only needs to use Möbius inversion. For 1, directly examine the Möbius inversion form of $\Phi_n(x)$, i.e. $\Phi_d(x)=\prod_{d\mid n}(x^d-1)^{\mu(n/d)}$; for 2, let the coefficient of the $\varphi(n)-1$-th degree term of $\Phi_n(x)$ be $f(n)$; then comparing the coefficients of the $n-1$-th degree term on both sides of $x^n-1=\prod_{d\mid n}\Phi_d(x)$ shows that $\sum_{d\mid n}f(d)=-[n=1]$, then apply Möbius inversion; for 3, dividing both sides of $x^n-1=\prod_{d\mid n}\Phi_n(x)$ by $\Phi_1(x)=x-1$, then substituting $x=1$, gives $n=\prod_{d\mid n,d\neq 1}\Phi_n(1)$, then apply Möbius inversion.
    
    Below we prove the fourth property. First, if $n$ is the order of $b$ in the multiplicative group $(\mathbf Z/p\mathbf Z)^\times$, then $n$ is the smallest positive integer satisfying $p\mid b^n-1$, so $p\mid\Phi_n(b)$. Conversely, if $p\mid\Phi_n(b)$, then $b^n\equiv 1\pmod p$; but if $n$ is not the order of $b$ in the multiplicative group $(\mathbf Z/p\mathbf Z)^\times$, then letting its order be $k$, we must have $k\mid n$ and $p\mid\Phi_k(b)$. In this case, $\Phi_k(x)$ and $\Phi_n(x)$ have a common root $b$ in the field $\mathbf F_p$, which means $x^n-1$ has the repeated root $b$. This means $p\mid n$; otherwise, $x^n-1$ is coprime to its derivative, so it is separable over $\mathbf F_p$ and cannot have a repeated root. Therefore, a prime factor $p$ of $\Phi_n(b)$ has only two cases: $p\mid n$, or $n$ is the order of $b$ in the multiplicative group $(\mathbf Z/p\mathbf Z)^\times$. These two cases are mutually exclusive, because the latter implies $n\mid p-1$.

Cyclotomic polynomials can also be used to solve some number-theoretic and algebraic problems. For example, the length of the repeating period when a fraction is written as a decimal in some base is closely connected with cyclotomic polynomials. For these specific applications, interested readers may consult the material at the end of the article.

## Finite field

A **finite field**, also called a **Galois field**, is a field with only finitely many elements. The structure of a finite field is uniquely determined by its number of elements, and its number of elements must be a prime power.

???+ note "Theorem"
    A field of size $q$ exists if and only if $q$ has the form of a prime power $p^n$. Moreover, such a field is unique up to isomorphism, denoted $\mathbf F_q$. The prime $p$ is the characteristic of the field $\mathbf F_q$, and the positive integer $n$ is the degree of the field extension $\mathbf F_q/\mathbf F_p$. Finally, $\mathbf F_q$ is the splitting field of the polynomial $x^q-x$ over $\mathbf F_p$, and includes exactly the $q$ distinct roots of $x^q-x$.

??? note "Proof"
    Let the field $F$ be a finite field. The characteristic of the field $F$ must be finite, denoted $p$; so the field $F$ has the prime subfield $\mathbf F_p$. Moreover, the field $F$ must be a finite extension over $\mathbf F_p$, with degree of extension denoted $n$. As an $n$-dimensional vector space over $\mathbf F_p$, the field $F$ has $q=p^n$ elements. All the nonzero elements of the field $F$ form the group $F^\times$, whose order is $q-1$, so $x^{q-1}=1$. Therefore, all elements of $F=F^\times\cup\{0\}$ satisfy $x^q=x$, i.e. they are the $q$ distinct roots of the polynomial $x^q-x$. Therefore, in the field $F$ the polynomial $x^q-x$ has the factor $\prod_{\alpha\in F}(x-\alpha)$, but the degree of this factor is already $q$ and its leading coefficient equals $1$, so $x^q-x=\prod_{\alpha\in F}(x-\alpha)$. This shows that $x^q-x$ splits over $F$. For any field over which $x^q-x$ splits, since $x^q-x$ has $q$ distinct roots, it must have at least $q$ elements. This shows that $F$ is the smallest field over which $x^q-x$ can split, i.e. the splitting field of $x^q-x$. In sum, a finite field of size $q$ must be the splitting field of the polynomial $x^q-x$ over its prime subfield. Because the splitting field is unique up to isomorphism, a field of size $q$ must also be unique.
    
    Conversely, given a prime $p$ and its power $q=p^n$, we must show that the splitting field of the polynomial $x^q-x$ over $\mathbf F_p$ has exactly $q$ elements, in order to show that fields of every prime-power order $q$ exist. Because the splitting field of the polynomial $x^q-x$ over $\mathbf F_p$ always exists, we may let the set of all roots of the polynomial $x^q-x$ in this splitting field be $F$. Now we prove that $F$ is a field, so that it is the splitting field of the polynomial $x^q-x$ itself. But iterating the Frobenius endomorphism $n$ times shows that $x\mapsto x^q$ is also an endomorphism, so for any $\alpha,\beta\in F$ we have $(\alpha\pm\beta)^q=\alpha^q\pm\beta^q$, $(\alpha\beta)^q=\alpha^q\beta^q$, and $(\alpha^{-1})^q=(\alpha^q)^{-1}$. Therefore, the set $F$ is closed under addition, subtraction, multiplication, and division, and is a field. This shows that $F$ is the splitting field of the polynomial $x^q-x$ over $\mathbf F_p$.

???+ note "Corollary"
    In a finite field $\mathbf F_q$ ($q>2$), the sum of all nonzero elements is $0$, and the product is $-1$.

??? note "Proof"
    The nonzero elements of a finite field are exactly the $q-1$ roots of the polynomial $x^{q-1}-1$; apply Vieta's formulas.

In the prime field $\mathbf F_p$, the conclusion of this corollary about the product is precisely (part of) [Wilson's theorem](../number-theory/factorial.md#wilsons-theorem) in number theory.

### Multiplicative structure

The multiplicative group $\mathbf F^\times=\mathbf F\setminus\{0\}$ of a finite field is necessarily a cyclic group.

???+ note "Theorem"
    A finite subgroup of the multiplicative group of a field $F$ is necessarily a cyclic group.

??? note "Proof"
    Let $G$ be a subgroup of the multiplicative group of the field $F$ with $|G|=n$. Therefore, $G$ is a finite Abelian group. By the fundamental theorem of finite Abelian groups, the group $G$ has the invariant factor decomposition $C_{n_1}\times\cdots\times C_{n_s}$ with $n_1\mid\cdots\mid n_s$. So for all elements $x$ in $G$, we have $x^{n_s}=1$. That is, the elements of the group $G$ are all roots of the polynomial $x^{n_s}-1$ over the field $F$. But the polynomial $x^{n_s}-1$ has at most $n_s$ distinct roots, i.e. $n\le n_s$. But $n_s\le n$, so in fact $n_s=n$. This shows $G\cong C_{n_s}$, i.e. the group $G$ is a cyclic group.

???+ note "Corollary"
    The multiplicative group $\mathbf F_q^\times$ of a finite field $\mathbf F_q$ satisfies $\mathbf F_q^\times\cong C_{q-1}$.

The cyclic group $\mathbf F_q^\times$ has $\varphi(q-1)$ generators, which are called the primitive elements of the finite field; here, $\varphi(n)$ is the [Euler's totient function](../number-theory/euler-totient.md).

???+ abstract "Primitive element"
    A generator of the multiplicative group of a finite field $\mathbf F_q$ is called a **primitive element** of $\mathbf F_q$.

??? warning "The primitive element of a simple extension and the primitive element of a finite field are not the same"
    Although the primitive element of a simple extension and the primitive element of a finite field have the same name, the two are not the same. The primitive element of a simple extension is a generator of the corresponding simple extension, while the primitive element of a finite field is a generator of the corresponding multiplicative group (as a cyclic group). The primitive element of a finite field as a simple extension of its prime subfield is not necessarily a primitive element of the finite field itself. For example, in $\mathbf F_{25}\cong\mathbf F_5[x]/(x^2+x+1)$, $\overline x$ is a primitive element of the field extension, but is not a primitive element of the field $\mathbf F_{25}$, because its order is $3$.

??? warning "The primitive element in $\mathbf F_{q}$ and the primitive root modulo $q$ are also not the same"
    For a finite field $\mathbf F_{q}$ of odd characteristic, there always exists a [primitive root](./ring-theory.md#application-the-multiplicative-group-of-integer-congruence-classes) modulo $q$. But it should not be confused with the primitive element in the finite field $\mathbf F_{q}$. Although both are generators of the corresponding multiplicative structure as a cyclic group, $(\mathbf Z/q\mathbf Z)^\times$ and $\mathbf F_q$ are not the same when $q$ itself is not prime. For example, the order of the former is $\varphi(q)$ and the order of the latter is $q-1$, so the sizes of the two multiplicative groups are not the same.

Let $\alpha$ be a primitive element of the finite field $\mathbf F_q$. Then, for all $x\in\mathbf F_q$ there exists a unique natural number $k<q-1$ such that $x=\alpha^k$; this $k$ is called the **discrete logarithm** of the element $x$ over $\mathbf F_q$ with respect to the base $\alpha$. As in the case over $\mathbf F_p$, the [algorithms for discrete logarithm](../number-theory/discrete-logarithm.md) all have relatively high complexity.

Through multiplication, a primitive element can already generate all the nonzero elements of the field. This shows that a finite field, as an extension of its subfield, is necessarily a simple extension.

???+ note "Theorem"
    For a finite field $\mathbf F_q$, let $F$ be a subfield of $\mathbf F_q$; then $\mathbf F_q$ is a simple algebraic extension over $F$; and letting $\alpha$ be a primitive element of $\mathbf F_q$, we have $\mathbf F_q=F(\alpha)$.

The minimal polynomial of a primitive element is an irreducible polynomial over the subfield of the finite field.

### Containment relations

A subfield of a finite field is also a finite field. The containment relations among finite fields are also completely determined by their orders.

???+ note "Theorem"
    Let $\mathbf F_q$ and $\mathbf F_r$ be finite fields; then $\mathbf F_r$ is a subfield of $\mathbf F_q$ if and only if there exists $k$ such that $q=r^k$. In other words, $\mathbf F_{p^d}$ is a subfield of $\mathbf F_{p^n}$ if and only if $d\mid n$.

??? note "Proof"
    If $\mathbf F_r$ is a subfield of $\mathbf F_q$, then the two must have the same characteristic $p$. The field extensions $\mathbf F_q/\mathbf F_r$, $\mathbf F_r/\mathbf F_p$, and $\mathbf F_q/\mathbf F_p$ are all simple algebraic extensions; denoting their degrees of extension by $k,d,n$ respectively, the degrees of extension must satisfy $n=kd$. Moreover, $r=p^d$ and $q=p^n$, and $q=p^n=p^{kd}=(p^d)^k=r^k$ holds.
    
    Conversely, we prove that for all $d\mid n$, $\mathbf F_{p^d}$ is a subfield of $\mathbf F_{p^n}$. Denote $r=p^d$ and $q=p^n$. Let $F$ be the set of all roots of the equation $x^r-x=0$ in the finite field $\mathbf F_q$. Through the Frobenius endomorphism one can prove that the set $F$ must form a field; the key is to prove that there are exactly $r$ such roots, so that $F\cong\mathbf F_r$. Because $d\mid n$, we have $(p^d-1)\mid(p^n-1)$, so $(x^{p^d-1}-1)\mid(x^{p^n-1}-1)$, i.e. $(x^r-x)\mid (x^q-x)$. So $x^r-x$ splits over $\mathbf F_q$, and hence has $r$ distinct roots in $\mathbf F_q$. This shows that $F\cong\mathbf F_r$ is a subfield of $\mathbf F_q$.

This theorem shows that the containment relations of finite fields $\mathbf F_{p^n}$ correspond to the divisibility relations among the exponents $n$ in the orders $p^n$ of the fields. The lattice formed by all finite fields $\mathbf F_{p^n}$ of characteristic $p$ is also isomorphic to the lattice formed by the integers $n$ under divisibility. Of course, in order for operations such as the intersection of finite fields $\mathbf F_{p^n}$ to be meaningful, one needs to embed all fields of characteristic $p$ into the algebraic closure of $\mathbf F_p$.

???+ note "Theorem"
    Let $F$ be the algebraic closure of $\mathbf F_p$; then the set of roots of the polynomial $x^{p^n}-x$ in the field $F$ forms the finite field $\mathbf F_{p^n}$. Then, we have:
    
    1.  $F=\bigcup_{n=1}^\infty\mathbf F_{p^n}$, i.e. the algebraic closure of $\mathbf F_p$ is the union of all finite fields of characteristic $p$;
    2.  The lattice formed by all finite fields $\mathbf F_{p^n}$ of characteristic $p$ under containment is isomorphic to the lattice formed by the integers $n$ under divisibility. In particular, the intersection $\mathbf F_{p^n}\cap\mathbf F_{p^m}=\mathbf F_{p^{\gcd(n,m)}}$ of $\mathbf F_{p^n}$ and $\mathbf F_{p^m}$, and the smallest field $\mathbf F_{p^n}\mathbf F_{p^m}=\mathbf F_{p^{\operatorname{lcm}(n,m)}}$ containing both $\mathbf F_{p^n}$ and $\mathbf F_{p^m}$.

??? note "Proof"
    The key is to prove the first part, i.e. that $\bigcup_{n=1}^\infty\mathbf F_{p^n}$ is the algebraic closure of $F_p$. The second part is a simple corollary of the earlier theorem on subfields of finite fields.
    
    Note that, taking any $\alpha\in\bigcup_{n=1}^\infty\mathbf F_{p^n}$, there must exist $n\in\mathbf N_+$ such that $\alpha\in\mathbf F_{p^n}$ holds, so $\alpha$ is an algebraic element over $\mathbf F_p$; therefore, $\bigcup_{n=1}^\infty\mathbf F_{p^n}$ is an algebraic extension of $\mathbf F_p$. For any polynomial $f(x)$ of degree $m$ over $\mathbf F_p$, it has at most $m$ distinct roots $\{\alpha_i\}_{i=1}^m$ in the algebraic closure $F$. Let the degree of the minimal polynomial of the root $\alpha_i$ be $n_i$; then $\alpha_i$ must be contained in the field $\mathbf F_{p^{n_i}}$; therefore, all roots of $f(x)$ are in $\bigcup_{n=1}^\infty\mathbf F_{p^n}$, i.e. $f(x)$ splits over $\bigcup_{n=1}^\infty\mathbf F_{p^n}$. By the definition of algebraic closure, $\bigcup_{n=1}^\infty\mathbf F_{p^n}$ is the algebraic closure of $\mathbf F_p$.

### Automorphism group

Every subfield of a finite field $\mathbf F_q$ is a set of roots of a polynomial of the form $x^r-x$. In other words, they are all the fixed-point sets of some map $x\mapsto x^r$. This in fact reveals a deep correspondence between the subfields of a finite field and the subgroups of the automorphism group.

Every field of characteristic $p$ has the Frobenius endomorphism $\sigma_p:x\mapsto x^p$. For the case of a finite field $\mathbf F_q$, this is also an automorphism; this shows that finite fields $\mathbf F_q$ are all perfect fields. The automorphism group of the field $\mathbf F_q$ is precisely the cyclic group $\langle \sigma_p\rangle$ of order $n$, one of whose generators is the Frobenius endomorphism $\sigma_p$.

???+ note "Theorem"
    The automorphism group $\operatorname{Aut}(\mathbf F_q)=\langle\sigma_p\rangle$ of a finite field $\mathbf F_q$ is a cyclic group of order $n$, and the generator $\sigma_p$ is the Frobenius endomorphism $x\mapsto x^p$.

??? note "Proof"
    First, the Frobenius endomorphism $\sigma_p$ is an automorphism on the finite field $\mathbf F_q$, because an injection on a finite set is necessarily also a surjection. Therefore, $\sigma_p\in\operatorname{Aut}(\mathbf F_q)$.
    
    Then, the order of $\sigma_p$ is $n$. This is because for all $x\in\mathbf F_q$ we have $\sigma_p^n(x)=x^{p^n}=x$, so $x^{p^n}$ is the identity map; and for any $k<n$, $\sigma_p^k$ is not the identity map, otherwise the elements of $\mathbf F_q$ would all be roots of $x^{p^k}-x$, which is impossible.
    
    Finally, $\operatorname{Aut}(\mathbf F_q)$ has at most $n$ elements. Let $\alpha$ be a primitive element of $\mathbf F_q$; then an automorphism $\sigma\in \operatorname{Aut}(\mathbf F_q)$ is uniquely determined by its value $\sigma(\alpha)$ at $\alpha$. But $\sigma$ must map $\alpha$ to one of its conjugate elements; otherwise, $\alpha$ and $\sigma(\alpha)$ would no longer be roots of the same minimal polynomial. There are only $n$ such conjugate elements, which shows that $\operatorname{Aut}(\mathbf F_q)$ also has at most $n$ elements.
    
    Therefore, the $n$ elements in $\operatorname{Aut}(\mathbf F_q)$ are precisely $\langle\sigma_p\rangle$. The theorem is proved.

The subgroups of the automorphism group $\operatorname{Aut}(\mathbf F_q)$ correspond one-to-one with the subfields of the finite field $\mathbf F_q$.

???+ note "Theorem"
    Let $\mathbf F_q$ be a finite field, $\mathcal F$ be the set of all its subfields, and $\mathcal G$ be the set of all subgroups of its automorphism group $\operatorname{Aut}(\mathbf F_q)$. Then, we have:
    
    1.  For $F\in\mathcal F$, let $\operatorname{Aut}(\mathbf F_q/F)$ be the set of automorphisms in $\operatorname{Aut}(\mathbf F_q)$ that fix $F$, i.e. $\operatorname{Aut}(\mathbf F_q/F)=\{\sigma\in\operatorname{Aut}(\mathbf F_q):\forall x\in F(\sigma(x)=x)\}$; then $\operatorname{Aut}(\mathbf F_q/F)\le\operatorname{Aut}(\mathbf F_q)$;
    2.  For $G\in\mathcal G$, let $F^G$ be the intersection of the fixed-point sets of all automorphisms in $G$, i.e. $F^G=\{x\in\mathbf F_q:\forall\sigma\in G(\sigma(x)=x)\}$; then $F^G$ is a subfield of $\mathbf F_q$;
    3.  The map $F\rightarrow\operatorname{Aut}(\mathbf F_q/F)$ and the map $G\rightarrow F^G$ are mutual inverses, and are a one-to-one correspondence between $\mathcal F$ and $\mathcal G$;
    4.  This one-to-one correspondence maps the extension relation between subfields to the containment relation between subgroups, i.e. for any $F_1\subseteq F_2$, we have $\operatorname{Aut}(\mathbf F_q/F_2)\le\operatorname{Aut}(\mathbf F_q/F_1)$.

This conclusion is a special case of the fundamental theorem of general Galois theory, which connects field extensions with the content of group theory, so that problems of field extensions can be solved through the methods of group theory.

### Irreducible polynomials

Irreducible polynomials over a finite field $\mathbf F_q$ are very easy to determine. Because every irreducible polynomial of degree $n$ over the finite field $\mathbf F_q$ corresponds to an algebraic extension of degree $n$, and such an extension is unique, all the roots of all irreducible polynomials of degree $n$ can be found in $\mathbf F_{q^n}$. This shows that an irreducible polynomial of degree $n$ over $\mathbf F_q$ must be a factor of $x^{q^n}-x$. To determine all the irreducible polynomials of degree $n$ over the finite field $\mathbf F_q$, one needs to examine the factorization of $x^{q^n}-x$ over $\mathbf F_q$. This is quite similar to the case of cyclotomic polynomials.

The algebraic elements over $\mathbf F_q$ can be classified according to the degree of their minimal polynomial. Let $P_n$ be the set of algebraic elements whose minimal polynomial has degree exactly $n$; then

$$
\mathbf F_{q^n} = \bigcup_{d\mid n}P_d.
$$

This corresponds to the factorization

$$
x^{q^n}-x = \prod_{d|n}\prod_{\zeta\in P_d}(x-\zeta).
$$

Because an irreducible polynomial of degree $n$ has $n$ roots, and the minimal polynomials of these roots all have degree $n$, an irreducible polynomial of degree $n$ must be a factor of the polynomial

$$
\prod_{\zeta\in P_n}(x-\zeta) = \prod_{d\mid n}\left(x^{q^d}-x\right)^{\mu(n/d)};
$$

this expression is obtained by applying [Möbius inversion](../number-theory/mobius.md) to the previous factorization. Because the degree of this polynomial is

$$
\sum_{d\mid n}\mu(d)q^{n/d},
$$

the number of monic irreducible polynomials of degree $n$ over $\mathbf F_q$ is

$$
\frac1n\sum_{d\mid n}\mu(d)q^{n/d}.
$$

This is exactly the number of types of necklaces of length $n$ that can be strung from beads of $q$ colors, counted up to rotation ([proof](../combinatorics/polya.md#cyclic-group)), so it is also called the necklace polynomial.

???+ note "Theorem"
    Over a finite field $\mathbf F_q$ there exist irreducible polynomials of every degree.

Because irreducible polynomials over a finite field have a simple structure, this makes the factorization of polynomials over a finite field very easy. For example, to determine all the irreducible factors of degree $n$ of a given polynomial, it suffices to compute the greatest common factor of the given polynomial and $x^{q^n}-x$[^ddf]. Similarly, as long as a polynomial of degree $n$ is coprime to the polynomial $x^{q^k}-1$ for all $k<n$, one can conclude that this polynomial of degree $n$ is irreducible over $\mathbf F_q$.

It was pointed out earlier that a root of an irreducible polynomial over a finite field is not necessarily a primitive element of the corresponding extension field as a finite field. The minimal polynomial of a primitive element of a finite field $\mathbf F_q$ over its prime subfield $\mathbf F_p$ is also called a **primitive polynomial**[^prim-poly] over the field $\mathbf F_p$. Implementing an extension field with such a polynomial guarantees that $\overline x$ is necessarily a primitive element in the extension field. A primitive polynomial of degree $n$ over the field $\mathbf F_p$ can be obtained by factoring the cyclotomic polynomial $\Phi_n(x)$ over $\mathbf F_p$.

???+ note "Theorem"
    Let $p$ be a prime, $n$ a positive integer, and $p\perp n$. Also let $d$ be the order of the element $p$ in the multiplicative group $(\mathbf Z/n\mathbf Z)^\times$. Then, the cyclotomic polynomial $\Phi_n(x)$ factors over the field $\mathbf F_p$ into a product of $\dfrac{\varphi(n)}{d}$ primitive polynomials of degree $d$ over $\mathbf F_p$. In particular, the cyclotomic polynomial $\Phi_n(x)$ is irreducible over the field $\mathbf F_p$ if and only if $p$ is a primitive root modulo $n$.

??? note "Proof"
    If one notes that the roots of the $n$-th cyclotomic polynomial are all the primitive $n$-th roots of unity of $\mathbf F_p$, and the degree $d$ of the minimal polynomial of a primitive $n$-th root of unity is the number of its conjugates (including itself), which equals the length of its orbit under the automorphism group $\langle\sigma_p\rangle$, then one can see that $d$ is the orbit length of the cyclic subgroup of the map $\zeta^i\mapsto\zeta^{ip}$ in $\{\zeta^i:i\perp n\}$, i.e. the order of the element $p$ in the multiplicative group $(\mathbf Z/n\mathbf Z)^\times$. If one does not want to rely on Galois theory, one can also prove this by showing that $d$ is the smallest positive integer such that $(x^n-1)\mid(x^{p^d-1}-1)$ holds. The remaining conclusions are obvious.

Although irreducible polynomials are important for the implementation of finite fields, there is no good deterministic method for finding an irreducible polynomial of degree $n$ over a finite field $\mathbf F_q$. In general, one can use a randomized method to generate such an irreducible polynomial. Because among all monic polynomials of degree $n$, the proportion of irreducible polynomials is $\Theta(1/n)$, one can first randomly generate a monic polynomial of degree $n$ and then determine whether it is reducible. Doing so can find an irreducible polynomial after generating an expected $\Theta(n)$ monic polynomials. Of course, an irreducible polynomial generated in this way is not necessarily a primitive polynomial, and its coefficients are not necessarily simple. In practice, if the size of the finite field is given in advance, one can often find a primitive polynomial with simple coefficients by looking it up in a table[^list-prim-poly], which facilitates subsequent computation.

### Reference implementation

This section provides a naive implementation of a finite field, for reference only. The code implements the method of randomly generating an irreducible polynomial.

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/finite-field/finite-field_1.cpp"
    ```

The finite fields most used in cryptography are those of characteristic $2$. For such finite fields, one can store the elements of the field as 01 strings, and implement the operations in the field using bit operations.

## Applications

This section lists some applications of field extensions in competitive programming. The most important situation is when, in computing an arithmetic expression over a field, one needs to introduce in the intermediate process some elements that do not originally exist in the field, so that the direct computation becomes possible. Readers should be familiar with the situation of using complex numbers to solve real-number problems, which is an example of an extension over the real field; what readers may be relatively unfamiliar with is extensions over finite fields. So here we mainly discuss extensions over finite fields, especially extensions over the prime field $\mathbf F_p$.

In some situations, a field extension can reduce the complexity of the computation, and is therefore necessary, for example the [fast Fourier transform](../poly/fft.md) over the real field; in some situations, a field extension is merely one of many methods for solving a problem, and there is usually a method of similar complexity that avoids using a field extension, for example the computation of the Fibonacci sequence to be mentioned shortly. While understanding these applications, readers should compare the advantages and disadvantages of different methods, so as to be able to choose an appropriate method when solving problems.

### Fibonacci sequence

For the computation of the [Fibonacci sequence](../combinatorics/fibonacci.md), common methods include the $O(n)$ linear recurrence and the $O(\log n)$ matrix fast exponentiation. In fact, it can also be solved through the method of field extension, with the same time complexity $O(\log n)$. The Fibonacci sequence has the closed-form formula:

$$
f(n) = \frac{1}{\sqrt{5}}\left(\left(\frac{1+\sqrt{5}}{2}\right)^n-\left(\frac{1-\sqrt{5}}{2}\right)^n\right).
$$

Now we want to compute the value of $f(n)$ modulo a prime $p\neq 5$[^fib-p5]. To transform this problem into a computation over the finite field $\mathbf F_p$, the first thing to resolve is the meaning of $\sqrt 5$ in $\mathbf F_p$. From an algebraic point of view, it is the square root of the element $5$. Therefore, if a square root of $5$ exists in $\mathbf F_p$, i.e. when $5$ is a quadratic residue modulo $p$, one can directly compute its square root and substitute it into the computation; otherwise, one needs to compute in the extension field $\mathbf F_p(\sqrt 5)\cong\mathbf F_p[x]/(x^2-5)$.

Of course, when computing in the extension field, it is not necessary to adjoin $\sqrt 5$. For example, for the Fibonacci sequence, one can also let $\phi$ be a root of the polynomial $x^2-x-1$, so that $f(n)$ can be written as

$$
f(n)=\frac{\phi^n-(-\phi)^{-n}}{2\phi-1}=\frac{\phi^n-(1-\phi)^n}{2\phi-1}.
$$

If $5$ is not a quadratic residue modulo $p$, the polynomial $x^2-x-1$ is irreducible. In this case, one can compute in the extension field $\mathbf F_p(\theta)\cong\mathbf F_p[x]/(x^2-x-1)$, obtaining a result consistent with that above.

The method for computing the Fibonacci sequence can of course be generalized to other situations. But there is one point that should be noted: the irreducibility of a polynomial over a finite field is not consistent with that over the rational field. For example $x^4-10x^2+1$, which is irreducible over $\mathbf Q$, with corresponding splitting field $\mathbf Q(\sqrt 2+\sqrt 3)=\mathbf Q(\sqrt 2,\sqrt 3)$; but over $\mathbf F_p$, if neither $2$ nor $3$ is a quadratic residue modulo $p$, then it is a product of two irreducible polynomials, i.e. in the extension field $\mathbf F_p(\sqrt 2)$ the square root $\sqrt{3}$ already exists without needing a further extension.

### Generalizing to "extensions" over rings

As shown in the previous section, field extensions have all kinds of restrictions. For the computation of the Fibonacci sequence, the extension-field method alone can only solve the case where the modulus $p$ is prime and $5$ is not a quadratic residue modulo $p$. But it should be noted that, as the discussion in the [algebraic extension](#algebraic-extension) section shows, if one does not require division in the extended structure, then one can extend a ring[^ring-extension]. This section briefly discusses this method, taking the computation of the Fibonacci sequence modulo an arbitrary modulus $n$ as an example. Other common situations that do not involve too much division, including the computation of determinants, fast Fourier transform, etc., can all attempt to apply this method when necessary.

Let $m$ be an arbitrary positive integer and $f(n)$ be the $n$-th term of the Fibonacci sequence. The problem is to compute the value of $f(n)\bmod m$. In principle, one needs to compute over $\mathbf Z/m\mathbf Z$. But, as the previous section showed, under different moduli the reducibility of the polynomial $x^2-x-1$ and whether it has repeated roots are inconsistent, so the general term of the Fibonacci sequence may differ greatly. Moreover, if $\mathbf Z/m\mathbf Z$ itself is not a field, the extended elements often do not have a valid inverse (for example, modulo $5$, the denominator $\sqrt 5$ is directly zero). Despite all these problems, in fact, under the condition that the coefficients are taken modulo $m$, computing the constant term of the remainder

$$
(1-x)^n-x^n\mod{x^2-x-1}
$$

suffices. Comparing with the general-term formula above, the reasonableness of this approach is obvious: it seems to be computing the value of

$$
f(n)=\frac{(1-\phi)^n-\phi^n}{1-2\phi}
$$

in the "extension" $(\mathbf Z/m\mathbf Z)[x]/(x^2-x-1)$, where $\phi$ is a root of $x^2-x-1$.

Although not so obvious, this approach is also valid. Note that in the extension $\mathbf Q(\phi)\cong\mathbf Q[x]/(x^2-x-1)$ of the rational field, the general-term formula holds. This shows that, in $\mathbf Q[x]$,

$$
(1-x)^n-x^n \equiv f(n)(1-2x) \pmod{x^2-x-1}
$$

holds. This involves only polynomials with integer coefficients, so it also holds in $\mathbf Z[x]$. Written as division with remainder, taking the coefficients on both sides modulo $m$, we obtain an identity over $(\mathbf Z/m\mathbf Z)[x]$. This conclusion holds for any $m$.

In general, if some expression can be computed over an extension field of the rational field $\mathbf Q$, then one can always obtain a conclusion over $\mathbf Z[x]$ by clearing the denominators, and then taking the modulus $m$ gives a conclusion over $(\mathbf Z/m\mathbf Z)[x]$. The key to making this approach work is that the step of clearing the denominators should not cause "irreversible" consequences. For example, for the computation of the Fibonacci sequence, if instead of the constant term one uses the coefficient of the first-degree term, then because the coefficient has a factor of $2$, $2$ has no inverse when the modulus $m$ is even, and there is no way to recover the value of $f(n)$; for another example, again for the computation of the Fibonacci sequence, if one uses the general-term formula with the $(-\phi)^{-n}$ term, then the step of clearing the denominators introduces intractable factors, so one cannot draw the conclusion from the result after taking the remainder. Therefore, the choice of the computation process is the key to being able to apply this technique.

### Cipolla's algorithm

This is a typical example of using an extension field of a finite field for computation. For a quadratic residue $a$ modulo $p\neq 2$, we want to find its square root, i.e. an $x$ such that $x^2\equiv a\pmod p$ holds. Although this is a problem over $\mathbf F_p$, [Cipolla's algorithm](../number-theory/quad-residue.md#cipolla-算法) computes over the finite field $\mathbf F_{p^2}$. This section explains this algorithm using the language of field theory. For the elementary number-theoretic proof, refer to the given link.

Specifically, Cipolla's algorithm first chooses $r$ such that $r^2-a$ is a quadratic non-residue modulo $p$, which means $x^2-(r^2-a)$ is an irreducible polynomial. Therefore, letting $u=r^2-a$, one can consider the extension field $\mathbf F_p(\sqrt u)$. Because the Frobenius endomorphism can only map an element to its conjugate, and such a conjugate is unique in a quadratic extension, we have $(r-\sqrt u)^p=r+\sqrt u$. Therefore, $(r-\sqrt u)^{p+1}=(r+\sqrt u)(r-\sqrt u)=r^2-u=a$. So, to determine the square root, it suffices to compute $(r-\sqrt u)^{(p+1)/2}$. This value must lie in $\mathbf F_p$, because the splitting field of $x^2-a$ is $\mathbf F_p$ itself.

## Exercises

Finally, we list some problems that directly apply the content of this article, to deepen understanding. But note that much of the content is not a regular examination point in competitive programming.

-   Cyclotomic polynomials:
    -   [Luogu P1520 因式分解](https://www.luogu.com.cn/problem/P1520)
    -   [Gym102114C Call It What You Want](https://codeforces.com/gym/102114/problem/C)
-   Finite fields:
    -   [Luogu P3923 大学数学题](https://www.luogu.com.cn/problem/P3923)
    -   [\[COTS 2021\] 菜 Jelo](https://www.luogu.com.cn/problem/P11192)
    -   [CF1310F. Bad Cryptography](https://codeforces.com/problemset/problem/1310/F)
    -   [LOJ 178. 多项式求根](https://loj.ac/p/178)
-   Field extensions:
    -   [\[Oleksandr Kulkov Contest 2\] Problem A. Square Root Partitioning](https://codeforces.com/gym/102354/problem/A)
    -   [CF1103E. Radix Sum](https://codeforces.com/problemset/problem/1103/E)

## References and notes

-   Dummitt, D.S. and Foote, R.M. (2004) Abstract Algebra. 3rd Edition, John Wiley & Sons, Inc.
-   [Milne, J.S. Fields and Galois Theory.](https://www.jmilne.org/math/CourseNotes/FT.pdf)
-   [Factorization of polynomials - Wikipedia](https://en.wikipedia.org/wiki/Factorization_of_polynomials)
-   [Factorization of polynomials over finite fields - Wikipedia](https://en.wikipedia.org/wiki/Factorization_of_polynomials_over_finite_fields)
-   [Cyclotomic Polynomial - Wikipedia](https://en.wikipedia.org/wiki/Cyclotomic_polynomial)
-   [Brett Porter's Notes on Cyclotomic Polynomials](https://www.whitman.edu/documents/academics/majors/mathematics/2015/Final%20Project%20-%20Porter%2C%20Brett.pdf)
-   [Jordan Bell's Notes on Cyclotomic Polynomials](https://jordanbell.info/LaTeX/mathematics/cyclotomic/cyclotomic.pdf)
-   [Michel Waldschmidt. An introduction to the theory of finite fields](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/FiniteFields.pdf)
-   [Finite Field Arithmetic - Wikipedia](https://en.wikipedia.org/wiki/Finite_field_arithmetic)

[^subfield-one]: This is because the unit $1_E$ of the field $E$ must satisfy the relation $x^2-x=0$ over $F$, and the latter has only two roots $0_F$ and $1_F$ in the field $F$; since the definition of a field requires $1_E\neq 0_E$, we must have $1_E=1_F$ and $0_E=0_F$.

[^initial-object-ring]: In the language of category theory, this means $\mathbf Z$ is the [initial object](https://en.wikipedia.org/wiki/Initial_and_terminal_objects) of the category of unital rings.

[^polynomial-universal]: Strictly speaking, this refers to the [universal property](https://en.wikipedia.org/wiki/Polynomial_ring#Polynomial_evaluation) of the polynomial ring $R[x]$.

[^multi-poly-ring]: The polynomial ring here has infinitely many indeterminates. To define such a polynomial ring, one first defines monomials. Let the set of indeterminates be $X$; then a monomial over it is a function $\alpha:X\rightarrow\mathbf N$ that takes a nonzero value at only finitely many indeterminates, which can be denoted $x_{i_1}^{\alpha(i_i)}\cdots x_{i_k}^{\alpha(i_k)}$, where $i_1,\cdots,i_k$ are the indices of all the indeterminates at which $\alpha$ takes a nonzero value. A polynomial is a linear combination of all finitely many monomials. Under the correspondingly defined addition and multiplication, they become a ring. For the case of finitely many indeterminates, one can prove that this definition is consistent with the result obtained from the recursive definition in the [multivariate polynomial ring](./ring-theory.md#multivariate-polynomial-ring) section.

[^fundamental-algebra]: Although its name is the fundamental theorem of algebra, this result is not purely algebraic, because the construction of the real field requires a topological structure.

[^ddf]: This statement is not quite rigorous, because one will also obtain irreducible factors of degree $d\mid n$. But since an algorithmic implementation usually starts by separating factors of smaller degree, by the time one separates the irreducible polynomial factors of degree $n$, the smaller factors should already have been separated, so this statement is also acceptable.

[^prim-poly]: Do not confuse the name here with the primitive polynomial in polynomial theory (i.e. a polynomial whose coefficients have greatest common divisor one).

[^list-prim-poly]: For example, the appendix of [Hansen, T., & Mullen, G. L. (1992). Primitive polynomials over finite fields. Mathematics of computation, 59(200), 639-643](https://www.ams.org/journals/mcom/1992-59-200/S0025-5718-1992-1134730-7/S0025-5718-1992-1134730-7.pdf) provides such a list.

[^fib-p5]: When $p=5$, the characteristic equation $x^2-x-1=0$ of the Fibonacci sequence has the double root $x=3$, so in $\mathbf F_5$ the general-term formula of the Fibonacci sequence is $f(n)=n3^{n-1}$.

[^ring-extension]: The so-called extension over a ring usually has two meanings: one is a [generalization of group extensions](https://en.wikipedia.org/wiki/Algebra_extension), and the other is a [generalization of field extensions](https://en.wikipedia.org/wiki/Subring#Ring_extensions). This article means the second. More specifically, the extensions involved in this section are all [integral extensions](https://en.wikipedia.org/wiki/Integral_element#Integral_extensions) over commutative unital rings, which is the generalization of the concept of algebraic extensions over fields to commutative unital rings.
