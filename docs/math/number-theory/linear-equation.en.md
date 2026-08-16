This article discusses solving linear congruence equations.

## Basic concepts

Let $a,b,n$ be integers and $x$ be the unknown; then an equation of the form

$$
ax\equiv b\pmod n
$$

is called a **linear congruence equation**.

Solving a linear congruence equation requires finding all solutions $x$ in the interval $[0,n-1]$. Of course, adding or subtracting any multiple of $n$ from them is still a solution of the equation. In the sense of modulo $n$, these are all the solutions of this equation.

This article next introduces two approaches for solving linear congruence equations, using the inverse and the Diophantine equation respectively. In the general case, solving both the inverse and the Diophantine equation requires the [extended Euclidean algorithm](./gcd.md#extended-euclidean-algorithm), so these two approaches are in fact consistent.

## Solving with the inverse

First, consider the case where $a$ and $n$ are coprime, i.e. $\gcd(a,n)=1$. In this case, one can compute the [inverse](./inverse.md) $a^{-1}$ of $a$, and multiply both sides of the equation by $a^{-1}$, giving the unique solution of the equation:

$$
x \equiv ba^{-1} \pmod n.
$$

Next, consider the case where $a$ and $n$ are not coprime, i.e. $\gcd(a,n)=d>1$. In this case, the original equation does not necessarily have a solution. For example, $2x\equiv 1\pmod 4$ has no solution. Therefore, we need to consider two cases:

-   When $d$ does not divide $b$, the equation has no solution. For any $x$, the left side of the equation $ax$ is a multiple of $d$, but the right side of the equation $b$ is not a multiple of $d$. Therefore, they cannot differ by a multiple of $n$, because a multiple of $n$ is also necessarily a multiple of $d$. Therefore, the equation has no solution.

-   When $d$ divides $b$, one can divide all the parameters $a,b,n$ of the equation by $d$, obtaining a new equation:

    $$
    a'x \equiv b'\pmod{n'}.
    $$

    where $\gcd(a',n')=1$, that is, $a'$ and $n'$ are coprime. This case has already been solved above, so one can obtain a solution $x'$ of the equation by finding the inverse.

    Obviously, $x'$ is also a solution of the original equation. But this is not the only solution of the original equation. Since all the solutions of the transformed equation are

    $$
    \{x' + kn' : k\in\mathbf Z\}.
    $$

    those among these solutions that fall in the interval $[0,n-1]$ are all the solutions of the original equation in the interval $[0,n-1]$:

    $$
    x \equiv (x' + kn')\pmod{n},\quad k = 0, 1, \cdots, d-1.
    $$

Summarizing these two cases, the **number of solutions** of a linear congruence equation equals $d=\gcd(a,n)$ or $0$.

## Solving with the Diophantine equation

A linear congruence equation is equivalent to the [binary linear Diophantine equation](./bezouts.md#the-case-of-two-variables) in $x,y$:

$$
ax + ny = b.
$$

Using the discussion on the cited page, the equation has a solution if and only if $\gcd(a,n)\mid b$, and a general solution of this equation is

$$
\begin{aligned}
x &= x_0 + t\dfrac{n}{d},\\
y &= y_0 - t\dfrac{a}{d},
\end{aligned}
$$

where $d=\gcd(a,n)$ is their greatest common divisor and $t$ is any integer.

Furthermore, the general solution of the linear congruence equation is

$$
x \equiv \left(x_0+t\frac{n}{d}\right)\pmod{n},\quad t\in\mathbf Z.
$$

Taking $x_0$ modulo $n/d$ gives the least (non-negative) integer solution of the congruence equation, i.e. the $x'$ above.

## Reference implementation

The reference implementation provided in this section can obtain the least non-negative integer solution of a congruence equation. If no solution exists, it outputs $-1$.

???+ example "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/linear-equation/linear-equation.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/linear-equation/linear-equation.py:core"
        ```

## Exercises

-   [「NOIP2012」同余方程](https://loj.ac/problem/2605)

**This page is mainly translated from the blog post [Модульное линейное уравнение первого порядка](http://e-maxx.ru/algo/diofant_1_equation) and its English translation [Linear Congruence Equation](https://cp-algorithms.com/algebra/linear_congruence_equation.html). The Russian version is under the Public Domain + Leave a Link license; the English version is under the CC-BY-SA 4.0 license. The content has been modified.**
