If you have already studied knowledge related to complex numbers, please skip this page.

Studying complex numbers requires some vector foundation; if you have not studied vectors, please go to the [vector page](../math/linear-algebra/vector.md).

## Complex numbers

### Introduction

???+ note "Note"
    The introductory method below comes from the PEP high-school mathematics A edition, compulsory book two.

From the perspective of equations, whether a negative real number can be square-rooted is whether the equation $x^2+a=0 (a>0)$ has a solution, which can further be reduced to whether the equation $x^2+1=0$ has a solution.

Reviewing the existing process of extending number sets, one can see that each extension is closely related to a practical need. For example, to solve the problems of measuring the diagonal of a square, and of equations like $x^2-2=0$ having no solution in the set of rational numbers, people extended the set of rational numbers to the set of real numbers. After the number set was extended, the addition and multiplication defined in the set of real numbers are consistent with the addition and multiplication originally defined in the set of rational numbers, and both addition and multiplication satisfy commutativity and associativity, with multiplication satisfying distributivity over addition.

Following this idea, to solve the problem of equations like $x^2+1=0$ having no solution in the real number system, we envision introducing a new number $\mathrm{i}$, such that $x=\mathrm{i}$ is a solution of the equation $x^2+1=0$, i.e. such that $\mathrm{i}^2=-1$.

Thinking: adding the newly introduced number $\mathrm{i}$ to the set of real numbers, we hope that the number $\mathrm{i}$ and real numbers can still perform addition and multiplication like real numbers, and we hope both addition and multiplication satisfy commutativity and associativity, with multiplication satisfying distributivity over addition. Then, after the real number system is extended, what numbers does the resulting new number system consist of?

Following the above envisioning, multiplying a real number $b$ by $\mathrm{i}$ gives a result denoted $b\mathrm{i}$; adding a real number $a$ to $b\mathrm{i}$ gives a result denoted $a+b\mathrm{i}$. Noting that all real numbers and $\mathrm{i}$ can be written in the form $a+b\mathrm{i}(a,b\in \mathbf{R})$, these numbers are all in the extended new number set.

### Definition

We define numbers of the form $a+b\mathrm{i}$, where $a,b\in \mathbf{R}$, as **complex numbers**, where $\mathrm{i}$ is called the **imaginary unit**, and the set of all complex numbers is called the **set of complex numbers**, denoted $\mathbf{C}$.

A complex number is usually denoted $z$, i.e. $z=a+b\mathrm{i}$. This form is called the **algebraic form of a complex number**. Here $a$ is called the **real part** of the complex number $z$, denoted $\operatorname{Re}(z)$, and $b$ is called the **imaginary part** of the complex number $z$, denoted $\operatorname{Im}(z)$. Unless otherwise stated, $a,b\in \mathbf{R}$.

For a complex number $z$, it is a real number if and only if $b=0$; when $b\not = 0$, it is an imaginary number; and when $a=0$ and $b\not = 0$, it is a pure imaginary number.

The relationship among pure imaginary numbers, imaginary numbers, real numbers, and complex numbers is shown in the figure below.

![](./images/complex-relation.svg)

## Properties and operations

### Geometric meaning

We have learned that numbers of a form like $a+b\mathrm{i}$ are called complex numbers, and have given their definition and classification; we can also dig into deeper properties.

We placed all real numbers on the number line and found that the points on the number line correspond one-to-one with real numbers. We consider handling complex numbers this way as well.

First we define **equality of complex numbers**: two complex numbers $z_1=a+b\mathrm{i},z_2=c+d\mathrm{i}$ are equal if and only if $a=c$ and $b=d$.

This definition is very natural, and no further explanation is given here.

That is, we can use a unique ordered pair of real numbers $(a,b)$ to represent a complex number $z=a+b\mathrm{i}$. In this way, associating with the plane rectangular coordinate system, we can find that **the set of complex numbers corresponds one-to-one with the set of points in the plane rectangular coordinate system**. Good, we have found a geometric meaning of complex numbers.

Then this plane rectangular coordinate system is no longer ordinary, because the points in it have acquired special meaning—representing a complex number—so we call such a plane rectangular coordinate system the **complex plane**, the $x$-axis the **real axis**, and the $y$-axis the **imaginary axis**. We further say: **the set of complex numbers corresponds one-to-one with the set of all points in the complex plane**.

Considering the knowledge of plane vectors we have studied, we find that the coordinate representation of a vector is also an ordered pair of real numbers $(a,b)$; obviously, the complex number $z=a+b\mathrm{i}$ corresponds to the point $Z(a,b)$ in the complex plane, then it also corresponds to the plane vector $\overrightarrow{OZ}=(a,b)$, so we find another geometric meaning of complex numbers: **the set of complex numbers corresponds one-to-one with the set of vectors in the complex plane (the real number $0$ corresponds to the zero vector)**.

Thus, transferring from the knowledge of vectors to complex numbers, we define the **modulus of a complex number** as the modulus of the vector corresponding to the complex number. The modulus of the complex number $z=a+b\mathrm{i}$ is $|z|=\sqrt{a^2+b^2}$.

So for convenience, we often call the complex number $z=a+b\mathrm{i}$ the point $Z$ or the vector $\overrightarrow {OZ}$, and stipulate that equal vectors represent the same complex number.

And from the knowledge of vectors we find that imaginary numbers cannot be compared in magnitude (but real numbers can).

### Addition and subtraction

For complex numbers $z_1=a+b\mathrm{i},z_2=c+d\mathrm{i}$, define the addition rule as follows:

$$
z_1+z_2=(a+c)+(b+d)\mathrm{i}
$$

Clearly, the sum of two complex numbers is still a complex number.

Considering the addition of vectors, we find that the addition of complex numbers conforms to the vector addition rule, which also proves the correctness of the geometric meaning of complex numbers.

One can likewise verify that the addition of complex numbers satisfies **commutativity** and **associativity**. That is:

$$
\begin{aligned}
z_1+z_2&=z_2+z_1\\
(z_1+z_2)+z_3&=z_1+(z_2+z_3)
\end{aligned}
$$

As the inverse operation of addition, subtraction can be derived through the addition rule and the definition of complex-number equality:

$$
z_1-z_2=(a-c)+(b-d)\mathrm{i}
$$

This likewise conforms to the subtraction of vectors.

### Multiplication, division, and conjugation

For complex numbers $z_1=a+b\mathrm{i},z_2=c+d\mathrm{i}$, define the multiplication rule as follows:

$$
\begin{aligned}
z_1z_2&=(a+b\mathrm{i})(c+d\mathrm{i})\\
&=ac+bc\mathrm{i}+ad\mathrm{i}+bd\mathrm{i}^2\\
&=(ac-bd)+(bc+ad)\mathrm{i}
\end{aligned}
$$

One can see that multiplying two complex numbers is similar to multiplying two polynomials, only one needs to replace $\mathrm{i}^2$ with $-1$ and combine the real and imaginary parts separately.

The multiplication of complex numbers is similar in form to the vector product of vectors.

It is easy to obtain that complex multiplication satisfies **commutativity**, **associativity**, and **distributivity over addition**, i.e.:

-   $z_1z_2=z_2z_1$
-   $(z_1z_2)z_3=z_1(z_2z_3)$
-   $z_1(z_2+z_3)=z_1z_2+z_1z_3$

Since it satisfies the operation laws, we can find that the **multiplication formulas in the real number field are equally applicable in the complex number field**.

Division is the inverse operation of multiplication; we can derive it:

$$
\begin{aligned}
\frac{a+b\mathrm{i}}{c+d\mathrm{i}}&=\frac{(a+b\mathrm{i})(c-d\mathrm{i})}{(c+d\mathrm{i})(c-d\mathrm{i})}\\
&=\frac{ac+bd}{c^2+d^2}+\frac{bc-ad}{c^2+d^2}\mathrm{i} &(c+d\mathrm{i}\not =0)
\end{aligned}
$$

Since vectors have no division, the relationship with vectors is not discussed here.

To make the denominator real, we multiplied by a $c-d\mathrm{i}$; this expression is very meaningful.

For a complex number $z=a+b\mathrm{i}$, $a-b\mathrm{i}$ is called the **complex conjugate** of $z$, usually denoted $\bar z$. We can find that if two complex numbers are conjugates of each other, then they are **symmetric about the real axis**.

For complex numbers $z,w$, the complex conjugate has the following properties

-   $z\cdot\bar{z}=|z|^2$
-   $\overline{\overline{z}}=z$
-   $\operatorname{Re}(z)=\dfrac{z+\bar{z}}{2}$, $\operatorname{Im}(z)=\dfrac{z-\bar{z}}{2}$
-   $\overline{z\pm w}=\bar{z}\pm\bar{w}$
-   $\overline{zw}=\bar{z}\bar{w}$
-   $\overline{z/w}=\bar{z}/\bar{w}$

### Argument and principal value of the argument

If we set the real unit $1$ as the horizontal positive direction and the imaginary unit $\mathrm{i}$ as the vertical positive direction, we obtain the complex plane from the rectangular-coordinate perspective.

The position representing a complex number $z$ can also be determined by means of polar coordinates $(r, \theta)$. As mentioned earlier, $r$ is the modulus of the complex number $z$.

The angle $\theta$ between the positive real axis and the vector corresponding to a **nonzero** complex number $z=x+\mathrm{i}y$ satisfies the relation:

$$
\tan \theta=\frac{y}{x}
$$

It is called the **argument** of the complex number $z$, denoted:

$$
\theta= \arg z
$$

Any **nonzero** complex number $z$ has infinitely many arguments, so $\arg z$ is in fact a set. Using a capitalized $\operatorname{Arg} z$ to denote **one particular value** among them, satisfying the condition:

$$
-\pi<\operatorname{Arg} z \le \pi
$$

$\operatorname{Arg} z$ is called the **principal value of the argument** or the **principal argument**. The argument is the principal value of the argument plus some integer number (which can be zero or a negative integer) of $2k\pi$, i.e. $\arg z = \{\operatorname{Arg} z + 2k\pi \mid k\in \mathbf Z\}$.

It should be noted that the sum of two principal values of the argument is not necessarily still a principal value of the argument, while the sum of two arguments is definitely still a valid argument.

The figure formed in the complex plane by complex numbers with modulus less than $1$ is called the **unit disk**. A complex number with modulus equal to $1$ is called a **unit complex number**, and the figure formed in the complex plane by all unit complex numbers is called the **unit circle**. Where no confusion arises, the unit circle is sometimes also abbreviated as the unit disk.

From the perspective of polar coordinates, the multiplication and division of complex numbers become very simple. For complex multiplication, the moduli multiply and the arguments add. For complex division, the moduli divide and the arguments subtract.

### Euler's formula

???+ note "Euler's formula[^ref1]"
    For any real number $x$, we have
    
    $$
    \mathrm{e}^{\mathrm{i}x}=\cos x+\mathrm{i}\sin x
    $$
    
    After supplementing the definitions of the [complex exponential function and complex trigonometric functions](#exponential-and-trigonometric-functions), this formula can be generalized to all complex numbers.

### Exponential and trigonometric functions

For a complex number $z=x+\mathrm{i}y$, the function $f(z)=\mathrm{e}^x(\cos y+\mathrm{i}\sin y)$ satisfies $f(z_1+z_2)=f(z_1)f(z_2)$. From this we give the definition of the **complex exponential function**:

$$
\exp z=\mathrm{e}^x(\cos y+\mathrm{i}\sin y)
$$

The complex exponential function is completely consistent with the real exponential function on the set of real numbers. It has the following properties on the complex plane:

-   Modulus always positive: $|\exp z|=\exp x>0$.
-   Argument: $\arg(\exp z)=\{y + 2k\pi \mid k\in\mathbf Z\}$.
-   Addition theorem: $\exp (z_1+z_2)=\exp (z_1)\exp (z_2)$.
-   Periodicity: $\exp z$ is a periodic function with fundamental period $2\pi \mathrm{i}$. If the period of a function $f(z)$ is an integer multiple of some period, that period is called the **fundamental period**.

The definition of the **complex trigonometric functions** (also simply called **trigonometric functions**) is as follows:

$$
\cos z=\frac{\exp (\mathrm{i}z)+\exp (-\mathrm{i}z)}{2}
$$

$$
\sin z=\frac{\exp (\mathrm{i}z)-\exp (-\mathrm{i}z)}{2\mathrm{i}}
$$

If we take $z\in\mathbf{R}$, then by [Euler's formula](#eulers-formula) we have:

$$
\cos z=\operatorname{Re}\left(\mathrm{e}^{\mathrm{i}z}\right)
$$

$$
\sin z=\operatorname{Im}\left(\mathrm{e}^{\mathrm{i}z}\right)
$$

The complex trigonometric functions are completely consistent with the real trigonometric functions on the set of real numbers. They have the following properties on the complex plane:

-   Parity: the sine function is odd, and the cosine function is even.
-   Trigonometric identities: the usual trigonometric identities all hold, for example the sum of squares being $1$, or the sum-and-difference formulas for angles.
-   Periodicity: the sine and cosine functions have fundamental period $2\pi$.
-   Zeros: all the zeros of the real sine and real cosine functions constitute all the zeros of the complex sine and complex cosine functions. This generalization introduces no new zeros.
-   Unboundedness of modulus: the modulus of the complex sine and complex cosine functions can be greater than any given positive number, no longer restricted to within $1$ like the real sine and real cosine functions.

## Three forms of a complex number

By means of the rectangular-coordinate perspective and the polar-coordinate perspective, one can write three forms of a complex number.

The **algebraic form** of a complex number is used to represent any complex number.

$$
z=x+y\mathrm{i}
$$

The algebraic form is more convenient for computing the four operations of addition, subtraction, multiplication, and division of complex numbers.

The **trigonometric form** and **exponential form** of a complex number are used to represent nonzero complex numbers.

$$
z=r(\cos \theta +\mathrm{i}\sin \theta)=r \exp (\mathrm{i}\theta)
$$

These two forms are more convenient for computing the two operations of multiplication and division of complex numbers and the operations that follow. If one only uses functions seen in high school, one can use the trigonometric form. If the complex exponential function has been introduced, writing it in the equivalent exponential form is more convenient.

## Roots of unity

Consider the solutions of the equation $x^n=1$ in the complex sense. Obviously, there are $n$ such solutions, and these $n$ solutions are all called **$n$-th roots of unity**. According to knowledge of the complex plane, the $n$-th roots of unity divide the unit circle into $n$ equal parts.

Let $\omega_n=\exp\dfrac{2\pi \mathrm{i}}{n}$ (i.e. the unit complex number with argument $2\pi/n$); then the solution set of $x^n=1$ is represented as $\{\omega_n^k\mid k=0,1\cdots,n-1\}$, where,

$$
w_n^k = \exp\dfrac{2\pi k \mathrm{i}}{n} = \cos\dfrac{2\pi k}{n} + \mathrm{i}\sin\dfrac{2\pi k}{n}.
$$

Unless otherwise stated, the $n$-th root of unity in general discussion refers to the first solution counterclockwise starting from $1$, i.e. the above $\omega_n$; all other solutions can be represented by powers of $\omega_n$.

???+ tip "Why does mentioning the $n$-th root of unity usually refer specifically to the first one?"
    Mainly for convenience of application. All $n$-th roots of unity can be represented as powers of the first $n$-th root of unity $\omega_n$; moreover, for any $k < n$, the complex number $\omega_n$ is not a $k$-th root of unity.

### Primitive roots of unity

In fact, $\omega_n$ is not the only $n$-th root of unity satisfying such a property. The elements of the set

$$
\{\omega_n^k\mid 0\le k<n,~\gcd(n,k)=1\}
$$

are called **primitive $n$-th roots of unity**. According to the above expression, there are $\varphi(n)$ primitive $n$-th roots of unity in total, where $\varphi(n)$ is [Euler's totient function](./number-theory/euler-totient.md).

Any primitive root of unity $\omega$ has the same property as the above $\omega_n$: for any $0<k<n$, the $k$-th power of $\omega$ is not $1$, that is, $\omega$ is not a $k$-th root of unity. Therefore, by means of any primitive root of unity, one can generate all the roots of unity.

To understand the structure of primitive $n$-th roots of unity, one needs to consider the following property of roots of unity:

???+ note "Property"
    For integers $n$ and $k$, let $d=\gcd(n,k)$; then $\omega_n^k = \omega_{n/d}^{k/d}$.

??? note "Proof"
    By direct computation,
    
    $$
    w_n^k = \exp\dfrac{2\pi k\mathrm{i}}{n} = \exp\dfrac{2\pi (k/d)\mathrm{i}}{n/d} = \omega_{n/d}^{k/d}.
    $$

This shows that as long as $\gcd(n,k)\neq 1$, then $\omega_n^k$ is necessarily a (primitive) $\dfrac{n}{\gcd(n,k)}$-th root of unity. Therefore, a root of unity $\omega_n^k$ satisfying the aforementioned property must satisfy $\gcd(n,k)=1$. This is precisely why the primitive root of unity has the above definition.

In addition, as a simple corollary of these analyses, we have:

???+ note "Theorem"
    As $k$ ranges over the divisors of $n$, all primitive $k$-th roots of unity constitute exactly a partition of the $n$-th roots of unity. Moreover, for $\ell\perp n$, the map $x\mapsto x^\ell$ gives a bijection among the $n$-th roots of unity and keeps the above partition unchanged: it maps a primitive $k$-th root of unity, with $k\mid n$, still to a primitive $k$-th root of unity.

Although there are many choices of primitive roots of unity, since the first root $\omega_n$ has the simplest form, $\omega_n$ is still the most commonly used in competitive programming. For some scenarios, to improve computational efficiency, one can also consider using a [primitive root of unity](./number-theory/residue.md#单位根) under some modulus to replace $\omega_n$ in the complex number field.

## Complex numbers in programming languages

### Complex numbers in C

In the C99 standard, there is the `<complex.h>` header file.

In the `<complex.h>` header file, three types are provided: `double complex`, `float complex`, and `long double complex`.

The arithmetic operators '+', '-', '\*', and '/' can be used with any mixture of floating-point numbers and complex numbers. When one of the two operands of an expression is complex, the computed result is complex.

The header file `<complex.h>` provides the imaginary unit `I`; when this header file is included, the capital letter `I` cannot be used as a variable name.

For a single complex number, `<complex.h>` provides several operations: the `creal` function is used to extract the real part, the `cimag` function to extract the imaginary part, the `cabs` function to compute the modulus, and the `carg` function to compute the principal value of the argument.

All the functions have three versions according to type. For example, the `creal` function has three versions `creal`, `crealf`, `creall`, used to handle the corresponding `double`, `float`, and `long double` types. The one with nothing at the end handles the `double` type by default. All the following functions follow this rule, which will not be specially noted again.

The return values of these functions are all ordinary floating-point numbers. One can assign an ordinary floating-point number directly to a complex number, but one cannot assign a complex number directly to a floating-point number, and instead needs to use the above extraction operations.

The function `conj` is used to compute the complex conjugate; its return value is a complex number.

The function `cexp` computes the complex exponential, `clog` computes the principal value of the logarithm, `csin` computes the sine, `ccos` computes the cosine, and `ctan` computes the tangent.

The function `cpow` computes the power function, `csqrt` computes the square root, `casin` computes the arcsine, `cacos` computes the arccosine, and `catan` computes the arctangent. All of these functions compute the principal values of multi-valued functions.

### Complex numbers in C++

In C, `<ctype.h>` becomes `<cctype>` in C++, and almost all header files follow this naming rule.

But `<complex.h>` does not follow it; C++ has no `<ccomplex>` header file. C++'s complex numbers are directly in `<complex>`, and what it holds is completely different from C.

Very interesting. This is because `<complex>` already existed in the first version of C++, C++98, while C added it only in C99.

In C++, complex-number types are defined using `complex<float>`, `complex<double>`, and `complex<long double>`. Due to the polymorphism of object orientation, the names of the following functions are all unique, without needing an f or l suffix.

A complex-number object has member functions `real` and `imag`, which can access the real and imaginary parts.

A complex-number object has non-member functions `real`, `imag`, `abs`, `arg`, returning the real part, imaginary part, modulus, and argument.

A complex-number object also has non-member functions: `norm` for the square of the modulus, and `conj` for the complex conjugate.

A complex-number object also has non-member functions `exp`, `log` (the principal value of the logarithm with base $\mathrm{e}$), `log10` (the principal value of the logarithm with base 10, not present in C), `pow`, `sqrt`, `sin`, `cos`, `tan`, with meanings the same as in C.

In C++14 and later versions, the [literal operators `std::literals::complex_literals::""if, ""i, ""il`](https://en.cppreference.com/w/cpp/numeric/complex/operator%2522%2522i.html) are defined. For example, entering `100if`, `100i`, and `100il` will respectively return `std::complex<float>{0.0f, 100.0f}`, `std::complex<double>{0.0, 100.0}`, and `std::complex<long double>{0.0l, 100.0l}`. This allows us to conveniently write complex-number declarations of the form `auto z = 4.0 + 3i`.

## References and links

-   [Complex number - Wikipedia](https://en.wikipedia.org/wiki/Complex_number)
-   [Euler's formula - Wikipedia](https://en.wikipedia.org/wiki/Euler's_formula)
-   [Complex number arithmetic - cppreference.com](https://en.cppreference.com/w/c/numeric/complex)
-   [std::complex - cppreference.com](https://en.cppreference.com/w/cpp/numeric/complex)

[^ref1]: For more introduction to Euler's formula, one can refer to two videos: [Euler's formula and elementary group theory](https://www.bilibili.com/video/BV1fx41187tZ), [Overview of differential equations - Chapter 5: Understanding $\mathrm{e}^{\mathrm{i}\pi}$ in 3.14 minutes](https://www.bilibili.com/video/BV1G4411D7kZ).
