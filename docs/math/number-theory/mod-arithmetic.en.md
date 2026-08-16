author: 383494, buuzzing, c-forrest, cr4c1an, Emp7iness, Enter-tainer, Great-designer, HeRaNO, jifbt, Kaiser-Yang, Koishilll, ksyx, Marcythm, Qiu-Quanzhi, Saisyc, sshwy, StarryReverie, StudyingFather, Tiphereth-A, Xeonacid, xyf007

In competitive programming, an important component of the number theory part is **modular arithmetic**, that is, performing various integer operations under a certain modulus. In addition to the basic four arithmetic operations and exponentiation, one can also conveniently perform operations such as taking logarithms, taking various roots, and computing factorials and binomial coefficients.

Modular arithmetic is common in various problems, and is not limited to the number theory part. The actual answer to many problems may be very large, exceeding the storage range of common integer variables. In this case, to avoid introducing big-integer arithmetic and outputting long numbers, problems often require the answer to be output modulo a number. This requires proficiency in various modular arithmetic techniques.

## Integer division and modulo operations in C/C++

In C/C++, integer division and modulo operations are inconsistent with the mathematically conventional modulo and division.

For all standard versions of C/C++, it is stipulated that in integer division:

1.  when the divisor is 0, the behavior is undefined;
2.  otherwise, the result of `(a / b) * b + a % b` equals `a`.

That is to say, the sign of the modulo operation depends on how the division rounds; and how the division rounds is implementation-defined (determined by the compiler).

Starting from the [C99](https://en.cppreference.com/w/c/language/operator_arithmetic) and [C++11](https://en.cppreference.com/w/cpp/language/operator_arithmetic) standard versions, it is stipulated that **the quotient rounds toward zero** (discarding the fractional part); the sign of the modulo is then the same as the dividend. From then on, the following assertions are guaranteed to be true:

```c
assert(5 % 3 == 2);
assert(5 % -3 == 2);
assert(-5 % 3 == -2);
assert(-5 % -3 == -2);
```

## Modular integer class

Modular arithmetic can be viewed as performing various operations on [congruence classes](./basic.md#congruence-classes-and-residue-systems) under a certain modulus. If we use a struct to represent a congruence class, and encapsulate the addition, subtraction, multiplication, and other operations between congruence classes as methods of the struct or operator overloads, then modular arithmetic can be naturally implemented as a modular integer class. Below we give a simple example, which supports addition, subtraction, multiplication, and fast exponentiation of $32$-bit signed integers under a modulus $M < 2^{30}$:

???+ example "A simple modular integer class"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/mod-arithmetic.cpp:core"
    ```

This implementation intentionally reduces the number of modulo operations, because the modulo operation is usually much more time-consuming than ordinary addition, subtraction, multiplication, or comparison operations. The code comments provide an equivalent and more direct implementation. The main idea of these simple optimizations is that when two integers in $[0,M)$ are added or subtracted, the result must fall within the interval $(-M,2M)$, so it can be adjusted back into the interval $[0,M)$ via one addition or subtraction. The exponentiation operation in this implementation uses the technique of [fast exponentiation](../binary-exponentiation.md#exponentiation-under-a-modulus).

In addition to these basic operations, one can also perform the following operations under various moduli:

-   [inverse](./inverse.md)
-   [division](./linear-equation.md)
-   [factorial](./factorial.md)
-   [binomial coefficient](./lucas.md)
-   [square root](./quad-residue.md#模意义下开平方)
-   [logarithm](./discrete-logarithm.md)
-   [root extraction](./residue.md#模意义下开方)

These operations are usually easier under a prime modulus. For a composite modulus, one often needs to use the extended version of the corresponding algorithm and the [Chinese Remainder Theorem](./crt.md). Most of these modular operations can be viewed as solving some kind of congruence equation. For the general method of solving congruence equations, one can refer to the [congruence equation](./congruence-equation.md) page.

## Related algorithms

This section will introduce several methods for optimizing modulo, multiplication, and fast exponentiation operations under a modulus. For the vast majority of problems, the simple implementation provided earlier is already efficient enough. However, when a problem has strict requirements on the constant factor of the algorithm, these optimization methods can come into play, further reducing the time overhead of the algorithm by reducing unnecessary computation and modulo operations.

### Fast multiplication

In primality testing and prime factorization, one often encounters multiplication modulo operations where the modulus is within the `long long` range. To avoid integer overflow problems during the computation, this section introduces a "fast multiplication" that can handle a modulus within the `long long` range, does not require `__int128`, and has $O(1)$ complexity. This algorithm requires that in the judging system, `long double` is represented as at least an $80$-bit extended-precision floating-point number[^long-double-80bit].

Suppose $0 \le a, b < m$, and we want to compute $ab\bmod m$. Note that:

$$
ab\bmod m=ab-\left\lfloor \dfrac{ab}m \right\rfloor m.
$$

Using the natural overflow of `unsigned long long`:

$$
ab\bmod m=ab-\left\lfloor \dfrac{ab}m \right\rfloor m=\left(ab-\left\lfloor \dfrac{ab}m \right\rfloor m\right)\bmod 2^{64}.
$$

As long as we can compute the quotient $\left\lfloor\dfrac{ab}m\right\rfloor$, the multiplication and subtraction operations in the rightmost expression can be computed directly using `unsigned long long`.

Next, we only need to consider how to compute $\left\lfloor\dfrac {ab}m\right\rfloor$. The solution is to first use `long double` to compute $\dfrac am$ and then multiply by $b$. Since `long double` is used, there will undoubtedly be precision errors. Assuming `long double` is represented as an $80$-bit extended-precision floating-point number (i.e. $1$ bit for the sign, $15$ bits for the exponent, and $64$ bits for the mantissa), then the maximum number of significant digits `long double` can precisely represent is $64$[^floating-format]. So $\dfrac am$ starts to be wrong from the $65$-th digit in the worst case, with an error range[^ld-mul-err] of $\left(-2^{-64},2^{-64}\right)$. Multiplying by $b$, this $64$-bit signed integer, the error range is $(-0.5,0.5)$. To simplify the subsequent discussion, we can first add $0.5$ and then round, and the final error range is $\{0,1\}$.

Finally, when substituting into the above expression for computation, we need to multiply by $-m$, so the final error range is $\{0,-m\}$. Because $m$ is within the `long long` range, when the result $r\in[0,m)$, directly return $r$, otherwise return $r+m$.

The code implementation is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i64-mul.cpp:ld-mul"
    ```

Nowadays, the C/C++ compilers equipped in the vast majority of judging systems already support the `__int128` type[^int128], so one can also directly promote the multiplier type to `__int128` before computing the modulo:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i64-mul.cpp:i128-mul"
    ```

Of course, the modulo operation of `__int128` is not fast. If further constant-factor optimization is needed, one can consider the methods introduced in the next two sections.

### Barrett reduction

As mentioned earlier, division and modulo operations are usually more time-consuming than other arithmetic operations. To reduce the overhead of modulo operations, there are some algorithms that can obtain the same result without directly doing the modulo. The Barrett reduction algorithm introduced in this section is one of them.

Let $m$ be a fixed modulus, and suppose we want to compute $a\bmod m$ multiple times for different $a > 0$. By division with remainder,

$$
z = a\bmod m = a - \left\lfloor\dfrac{a}{m}\right\rfloor m.
$$

The key is the computation of the quotient $\left\lfloor\dfrac{a}{m}\right\rfloor$. Let $R$ be some constant; then we have[^floor-barrett]

$$
\left\lfloor\dfrac{a}{m}\right\rfloor = \left\lfloor a\dfrac{R}{m} / R\right\rfloor \approx \left\lfloor a\left\lfloor\dfrac{R}{m}\right\rfloor/R\right\rfloor.
$$

If we choose $R = 2^k$, then $\left\lfloor\dfrac{R}{m}\right\rfloor$ in the right expression can be preprocessed, and the operation of dividing by $R$ can be performed via a shift operation. So, computing the quotient with the right expression requires only one multiplication and one shift operation. Substituting into the expression for $a\bmod m$, we obtain the estimate $z'$ of the desired remainder.

Now analyze the error of doing this. The [rounding function](./basic.md#rounding-functions) has the property: for $x > y > 0$, $\lfloor x\rfloor - \lfloor y\rfloor \le \lceil x - y\rceil$. So, the error

$$
\begin{aligned}
\Delta &= |z' - z| = m\left|\left\lfloor\dfrac{a}{m}\right\rfloor - \left\lfloor a\left\lfloor\dfrac{R}{m}\right\rfloor/R\right\rfloor\right|\\
&\le m\left\lceil a\left(\dfrac{R}{m} - \left\lfloor\dfrac{R}{m}\right\rfloor\right) /R\right\rceil \le m\left\lceil\dfrac{a}{R}\right\rceil.
\end{aligned}
$$

As long as $a \le R$, the error $\Delta$ does not exceed $m$. Since $z' \ge z$, the estimate $z'$ can only be $z$ or $z + m$. As long as, after obtaining the estimate, we subtract the extra $m$ when $z' \ge m$, we can guarantee that the answer is correct.

In the computation process of Barrett reduction, only two multiplications, one shift operation, and at most two subtractions are used to complete the integer modulo. But the improvement in efficiency is not without cost; in fact, the length of the intermediate variables involved in Barrett reduction is often longer than the length of the input variables. It is easy to see that the longest intermediate variable involved in Barrett reduction is $a\left\lfloor\dfrac{R}{m}\right\rfloor$. Let $\ell(x)$ be the length of the binary representation of the integer $x$. Then, we have

$$
\ell\left(a\left\lfloor\dfrac{R}{m}\right\rfloor\right) \approx \ell(a) + \ell(R) - \ell(m).
$$

Since the choice of $R$ needs to satisfy the condition $a < R$, this length is at least $2\ell(a) - \ell(m)$. But when a modulo is needed, generally $\ell(m)\le\ell(a)$, so the length of this intermediate variable may be greater than the input length $\ell(a)$. For example, if we need to take a $64$-bit integer modulo a $32$-bit integer, the intermediate variable actually needs a $64 \times 2 - 32 = 96$-bit integer.

One application scenario of Barrett reduction is computing the remainder of a product $ab\bmod m$. If one of the multipliers is fixed, for example when $b$ is fixed, we can perform an estimate similar to the above via

$$
ab\bmod m = ab - \left\lfloor a\left\lfloor\dfrac{bR}{m}\right\rfloor/R\right\rfloor m
$$

as long as we preprocess the value of $\left\lfloor\dfrac{bR}{m}\right\rfloor$. This case where $b$ is fixed is sometimes also called Shoup modular multiplication[^shoup].

The more common case is where neither $a$ nor $b$ is fixed. In this case, we need to first compute the value of $ab$, and then use Barrett reduction to obtain $ab\bmod m$. For example, when implementing multiplication under a modulus, we need to compute $ab\bmod m$ for $0 \le a,b < m$. In this case, the chosen $r$ needs to satisfy $ab < R$. According to the earlier analysis, the longest intermediate variable length involved in the computation process is $2\ell(ab)-\ell(m)$. When $\ell(a)\approx\ell(b)\approx\ell(m)$, this length is $3\ell(m)$. That is to say, if we want to use Barrett reduction to implement modular multiplication of $32$-bit integers, the intermediate variable needs a $96$-bit integer. This is also a limitation of Barrett reduction when actually applied in competitive programming.

As an example, a reference implementation of $32$-bit signed integer modular multiplication using Barrett reduction is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i32-mul.cpp:barrett"
    ```

The implementation requires 128-bit integers[^int128].

### Montgomery modular multiplication

The functionality of the Montgomery modular multiplication algorithm is very similar to that of the Barrett algorithm; it can likewise reduce the overhead of modulo operations in the modular integer computation process. Unlike the previous two algorithms, both of which approximately compute the quotient, Montgomery modular multiplication maps all integers to the Montgomery space, where the operations are relatively easy, thereby reducing the overall computation cost.

Let the modulus $m$ be odd, and choose $R = 2^k > m$. Then, the Montgomery form corresponding to the congruence class $a \bmod m$ is

$$
aR\bmod m.
$$

Because $R\perp m$, there is a bijection between the congruence class $a \bmod m$ and its Montgomery form $aR\bmod m$. Therefore, we can convert an integer to Montgomery form, perform several operations modulo $m$, and then convert the resulting Montgomery form back to an integer, and the result is always correct.

Using the Montgomery form, many modular integer operations can be conveniently performed. As just explained, to compare whether two congruence classes are the same, we only need to compare their Montgomery forms. Also, because

$$
(a+b)R\bmod m = ((aR\bmod m)\pm(bR\bmod m)) \bmod{m},
$$

the addition and subtraction of congruence classes correspond to the addition and subtraction of their Montgomery forms. But to compute the multiplication of congruence classes, we cannot directly multiply the two Montgomery forms. Because

$$
(ab)R\bmod m =  ((aR\bmod m)(bR\bmod m)R^{-1}) \bmod{m},
$$

when computing the multiplication of two Montgomery forms, we need to perform the following **Montgomery reduction** operation on their product $x$:

$$
\operatorname{REDC}: x \mapsto xR^{-1}\bmod m.
$$

Using this operation, the Montgomery form of the product $ab$ is $\operatorname{REDC}((aR\bmod m)(bR\bmod m))$. The Montgomery reduction operation is the core operation of Montgomery modular multiplication:

-   Converting $a$ to its Montgomery form is $\operatorname{REDC}((a\bmod m)(R^2\bmod m))$.
-   Converting the Montgomery form of $a$ back to $a\bmod m$ is $\operatorname{REDC}(aR\bmod m)$.
-   The Montgomery form corresponding to the modular inverse $a^{-1}\bmod m$ is $\operatorname{REDC}((aR\bmod m)^{-1}(R^3\bmod m))$.

Now discuss the implementation method of the Montgomery reduction operation $\operatorname{REDC}$. When computing $\operatorname{REDC}(x)$, we always assume $0 \le x < m^2$, which holds for all the above cases. Because $R\perp m$, by [Bézout's identity](./bezouts.md), there exist integers $R^{-1},m'$ such that

$$
RR^{-1} + mm' = 1.
$$

So, letting $q=\lfloor xm' / R\rfloor$, we have

$$
\begin{aligned}
xR^{-1} &= x\dfrac{1 - mm'}{R} \equiv \dfrac{x-xmm' + qmR}{R} = \dfrac{x - m(xm'\bmod R)}{R} \pmod{m}.
\end{aligned}
$$

Because $0 \le x < m^2 < mR$ and $0 \le xm'\bmod R < R$, we have

$$
-m < \dfrac{x - m(xm'\bmod R)}{R} < m.
$$

That is to say, this quotient and $xR^{-1}\bmod m$ differ by at most one $m$. As long as we add $m$ when the quotient is less than zero, we obtain $\operatorname{REDC}(x)$. Computing this quotient requires only two integer multiplications, one integer subtraction, and two bit operations (respectively taking the modulo with respect to $R=2^k$ and doing the division). Therefore, the Montgomery reduction operation can be performed efficiently.

To perform the Montgomery modular multiplication operation, we need to preprocess a series of constants. First, Montgomery reduction uses $m' = m^{-1}\bmod R$, which can be computed via the Newton–Hensel method introduced [below](#integer-class-modulo-a-power-of-2). Second, when reducing different operations to the Montgomery reduction operation, constants such as $R^2\bmod m$ are also involved. To obtain it, we need to compute $R\bmod m$ once, and adding it to itself gives $2R\bmod m$. Subsequently, regarding it as the Montgomery form of $2$, directly computing fast exponentiation gives $2^kR\bmod m = R^2\bmod m$.

As an example, the Montgomery modular multiplication implementation of $32$-bit signed integers is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/i32-mul.cpp:montgomery"
    ```

Compared with implementing modular multiplication via Barrett reduction, the computation of Montgomery modular multiplication involves multiple steps such as conversion, multiplication of Montgomery forms, and inverse conversion. Therefore, only when the number of modular operations between the conversion and inverse conversion is large enough can the cost of conversion and inverse conversion be amortized, thereby achieving higher overall efficiency. However, since the implementation of Montgomery modular multiplication involves only intermediate variables of length $2\ell(m)$, it is more flexible to implement. For example, modular multiplication of $32$-bit integers requires only $64$-bit intermediate variables. So, if one needs to implement a modular integer class for various number-theoretic computations, Montgomery modular multiplication is more suitable.

### Integer class modulo a power of 2

This section discusses the implementation of the modular integer class when the modulus is a power of $2$. In this special case, division and modulo operations can be implemented via bit operations, with very high computational efficiency. Both Barrett reduction and Montgomery modular multiplication use this characteristic of $2^e$ as the divisor and modulus to speed up the computation. In particular, when the modulus is exactly a special number such as $2^{32}$ or $2^{64}$, we can use an unsigned integer of the corresponding bit length combined with natural overflow to implement the modular integer class, without any explicit modulo operation. Even if the modulus is not exactly such, it can be transformed into these special modulus cases. For example, when the modulus is $2^{58}$, we can complete the intermediate computation under the modulus $2^{64}$, and finally take the result modulo $2^{58}$. In addition to the convenience of taking the modulo, the other operations of the modulo-$2^e$ integer class also have many special implementations. This section focuses on the implementation of the inverse and exponentiation operations.

First is the inverse operation: given an odd number $a$ and a modulus $m=2^e~(e > 2)$, we need to find $a^{-1}\bmod m$. Common methods for finding the inverse include the extended Euclidean algorithm and the fast exponentiation method. The process of the extended Euclidean algorithm involves taking the modulo with respect to a general modulus; the ordinary fast exponentiation method needs to compute $a^{\varphi(m)-1}\bmod{m}$, which requires $\Theta(e)$ integer multiplications. A more efficient method is the [Newton–Hensel method](../poly/newton.md). Specifically, consider applying the following conclusion:[^newton-hensel]

$$
mx \equiv 1 \pmod{2^e} \implies mx(2 - mx) \equiv 1\pmod{2^{2e}}.
$$

According to this expression, as long as we start from $x = 1$ and repeatedly apply $x \gets x(2-mx)$, we can obtain $m^{-1}\bmod R$ after $\lceil\log_2 e\rceil$ iterations.

As an example, a reference implementation of the modulo-$2^{32}$ integer inverse operation is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/mod-32-inv-pow.cpp:inv"
    ```

Next, discuss the exponentiation operation: given $x,a,b$ and a modulus $m=2^e~(e > 2)$, we need to find $xa^b\bmod m$, where $a$ is odd. According to the [analysis](./primitive-root.md#mod-pow-2) of the structure of integer multiplication modulo $2^e$, $a$ can always be written in the form $\pm g^{\ell}$[^mod-2-g], and the negative sign appears if and only if $a\equiv 3\pmod 4$. For this case, we can replace $a$ with $-a$, and multiply the final result by $(-1)^b$. Therefore, in the following we assume $a\equiv 1\pmod 4$ holds. In this case, the core idea of the algorithm is to write $a$ in the form $g^{L(a)}\bmod m$, and then use $xg^{bL(a)}\bmod m$ to compute the desired power.

Computing $L(a)$ is computing the discrete logarithm $\operatorname{ind}_ga$. Note that as long as $a\equiv 1\pmod 4$, $a$ can always be written in the following form:

$$
a \equiv (2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1) \pmod{m},
$$

where $1 < e_1 < e_2 < \cdots < e_s < e$. This is because directly expanding this product, we can find that the second-lowest bit equal to $1$ in the binary representation of $a$ is exactly the $e_1$-th bit (with index starting from $0$), and from this we can recursively find this representation. By the [properties](./discrete-logarithm.md#properties) of the discrete logarithm, we have

$$
4L(a) \equiv 4L(2^{e_1}+1) + 4L(2^{e_2}+1) + \cdots + 4L(2^{e_s}+1) \pmod{m}. 
$$

Since the modulus of the discrete logarithm equals the order $\delta_m(g)=2^{e-2}=m/4$, here we directly multiply the entire congruence by $4$ to ensure that the computation can be performed in the residue classes modulo $m$. From this, as long as we preprocess all $4L(2^d+1)$ for $1 < d < e$, we can quickly compute the value of $4L(a)$.

Conversely, from $L(a)$ it is also easy to obtain the value of $g^a\bmod{m}$. By the [binomial theorem](../combinatorics/combination.md#binomial-theorem), for $1 < d < e$, we have

$$
\begin{aligned}
(2^d+1)^{2^{e-d}} \equiv 1 \pmod{m},\quad
(2^d+1)^{2^{e-d-1}} \equiv 1 + 2^{e-1} \pmod{m},
\end{aligned}
$$

so $\delta_m(2^d+1) = 2^{e-d}$. By the property of the order, we have

$$
\delta_m(2^d+1) = \dfrac{\delta_m(g)}{\gcd(\delta_m(g), \operatorname{ind}_g(2^d+1))}.
$$

So, $\gcd(\delta_m(g), \operatorname{ind}_g(2^d+1)) = 2^{d-2}$. This shows that $L(2^d+1) = \operatorname{ind}_g(2^d+1) = 2^{d-2}r$, where $2\nmid r$. So, the lowest bit equal to $1$ in the binary representation of $4L(2^d+1)$ is exactly the $d$-th bit (with index starting from $0$). Therefore, we can likewise recursively decompose $4L(a)$ into a sum of the form $4L(2^d+1)$ via the binary representation. From this, we can obtain the value of $a$.

In the specific implementation, there are some points that can be further optimized. First, when decomposing $a$ into a product form, we still need to use division. It is more convenient to compute the decomposition of $a^{-1}$, i.e. to find $1 < e_1 < e_2 < \cdots < e_s < e$ such that

$$
a(2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1) \equiv 1 \pmod{m}
$$

holds. Again, $e_1$ is determined by finding the second-lowest bit equal to $1$, but to eliminate the factor $2^{e_1}+1$ from $a^{-1}$, we only need to multiply $a$ by $2^{e_1}+1$, which can be performed via bit operations. And because $4L(a^{-1})=-4L(a)$, when tallying $4L(a)$, we need to use subtraction instead of addition. Second, for a specially chosen base $g$, the iteration does not need to be carried out to $d = e-1$, but only to $d = \lceil e/2\rceil - 1$. To this end, we need to choose $g$ such that

$$
4L(2^{\lceil e/2\rceil} + 1) = 2^{\lceil e/2\rceil}.
$$

For $d \ge e / 2$, we have

$$
(2^d+1)^2 = 2^{2d} + 2^{d+1} + 1 \equiv 2^{d+1} + 1 \pmod{m}.
$$

So, inducting from $d = \lceil e/2\rceil$, we know that $L(2^d+1)=2^d$ holds for all $d \ge e/2$. Then, as long as $e/2 \le e_1 < e_2 < \cdots < e_s < e$, we have

$$
(2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1) \equiv 1 + 2^{e_1} + 2^{e_2} + \cdots + 2^{e_s} \pmod{m}
$$

as well as

$$
4L((2^{e_1}+1)(2^{e_2}+1)\cdots(2^{e_s}+1)) = 2^{e_1} + 2^{e_2} + \cdots + 2^{e_s}.
$$

Therefore, after handling all binary bits with $d < e/2$, we can directly obtain the discrete logarithm of the remaining part without computing bit by bit. After applying the first optimization, the entire exponentiation operation requires only $O(e)$ additions/subtractions and bit operations and $1$ multiplication operation; after applying the second optimization, we can save about half of the additions/subtractions and bit operations, but need $1$ additional multiplication operation.

As an example, a reference implementation of the modulo-$2^{32}$ integer exponentiation operation is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/mod-arithmetic/mod-32-inv-pow.cpp:pow"
    ```

The preprocessing of the discrete logarithm can be performed via the Pohlig–Hellman algorithm, and the base $g$ can be chosen as

$$
5^{\operatorname{ind}_5(2^{\lceil e/2\rceil})/2^{\lceil e/2\rceil - 2}}\bmod{2^e}.
$$

## References and notes

-   [Fast modular multiplication by orz - Codeforces](https://codeforces.com/blog/entry/96759)
-   [Barrett Reduction - Wikipedia](https://en.wikipedia.org/wiki/Barrett_reduction)
-   [Barrett Reduction - A41](https://encrypt.a41.io/primitives/modular-arithmetic/modular-reduction/barrett-reduction#cost-analysis-of-modular-multiplication)
-   [Barrett 约减原理及正确性证明 by Chen - 知乎专栏](https://zhuanlan.zhihu.com/p/690876166)
-   [Montgomery Multiplication - CP Algorithms](https://cp-algorithms.com/algebra/montgomery_multiplication.html)
-   [Montgomery 模乘 by Chen - 知乎专栏](https://zhuanlan.zhihu.com/p/645428404)
-   [Binary Exponentiation by Factoring - CP Algorithms](https://cp-algorithms.com/algebra/factoring-exp.html)
-   Barrett, Paul. "Implementing the Rivest Shamir and Adleman public key encryption algorithm on a standard digital signal processor." In Conference on the Theory and Application of Cryptographic Techniques, pp. 311-323. Berlin, Heidelberg: Springer Berlin Heidelberg, 1986.
-   Becker, Hanno, Vincent Hwang, Matthias J. Kannwischer, Bo-Yin Yang, and Shang-Yi Yang. "Neon NTT: Faster Dilithium, Kyber, and Saber on Cortex-A72 and Apple M1." IACR Transactions on Cryptographic Hardware and Embedded Systems (2022): 221-244.
-   Montgomery, Peter L. "Modular multiplication without trial division." Mathematics of computation 44, no. 170 (1985): 519-521.

[^long-double-80bit]: This applies to the GCC or Clang compilers on most 64-bit systems.

[^floating-format]: See [Double-precision floating-point format - Wikipedia](https://en.wikipedia.org/wiki/Double-precision_floating-point_format).

[^ld-mul-err]: Here we use the condition $a < m$, i.e. $a / m \in [0,1)$.

[^int128]: In current mainstream compilation environments, only MSVC on the Windows platform does not support the `__int128` type. If you need to write code compatible across multiple platforms, you can detect the MSVC compilation environment via the macro `_MSC_VER`, and under that condition include the [`<intrin.h>`](https://learn.microsoft.com/en-us/cpp/intrinsics/x64-amd64-intrinsics-list?view=msvc-170) header, using the built-in functions it provides (such as `_umul128`, etc.) to indirectly implement 128-bit integer operations (only available on 64-bit platforms).

[^floor-barrett]: Here $\left\lfloor\dfrac{r}{m}\right\rfloor$ can also be replaced by other integer estimates of $\dfrac{r}{m}$, such as the ceiling function $\left\lceil\dfrac{r}{m}\right\rceil$ and the round-half function $\left\lfloor\dfrac{r}{m}\right\rceil$, etc., as long as the error correction step for the estimate is adjusted accordingly.

[^shoup]: Shoup implemented this extension of Barrett reduction in his number-theoretic computation library [NTL](https://libntl.org/), hence the name.

[^newton-hensel]: Direct verification: from $mx \equiv 1 \pmod{2^e}$, we can set $mx = 1 + \lambda 2^e$; then $mx(2-mx) = (1+\lambda 2^e)(1-\lambda 2^e) = 1 - \lambda^2 2^{2e} \equiv 1\pmod{2^{2e}}$.

[^mod-2-g]: The page cited in the text only proves that $g$ can be taken as $5$. In fact, completely repeating that proof, one can show that $g$ can be taken as any integer congruent to $5$ modulo $8$. The method of choosing $g$ is discussed later.
