autor: iamtwz, billchenchina, CBW2007, CCXXXI, chinggg, Enter-tainer, eyedeng, FFjet, gaojude, Great-designer, H-J-Granger, Henry-ZHR, hsfzLZH1, Ir1d, kenlig, Konano, ksyx, luoguyuntianming, Marcythm, Menci, NachtgeistW, ouuan, Peanut-Tang, qwqAutomaton, sshwy, StudyingFather, Tiphereth-A, TrisolarisHD, TRSWNCA, Xeonacid, Yuuko10032, Zhangjiacheng2006, Zhoier, Hszzzx, shenshuaijie, kfy666

## Introduction

**Fast exponentiation**, also called **binary exponentiation** or **exponentiation by squaring**, is a small trick for computing $a^n$ in $\Theta(\log n)$ time, whereas the brute-force computation requires $\Theta(n)$ time.

This trick can be applied in any scenario where the multiplication of $a$ is associative, such as exponentiation under a modulus, matrix powers, etc.; see the [applications](#applications) section below for details.

## Procedure

Computing the $n$-th power of $a$ means multiplying $n$ copies of $a$ together: $a^{n} = \underbrace{a \times a \cdots \times a}_{n\text{ copies of }a}$. However, when $n$ is too large or a single multiplication is too costly, this method is not very applicable. The idea of binary exponentiation is to split the task of exponentiation into smaller tasks according to the **binary representation** of the exponent.

???+ example "Example"
    Suppose we want to compute $3^{13}$. If we expand it into a chain of products, it requires $13-1=12$ multiplications. But because
    
    $$
    3^{13} = 3^{(1101)_2} = 3^8 \times 3^4 \times 3^1,
    $$
    
    as long as we can quickly compute $3^{1},3^{2},3^{4},3^{8}$, we can compute the value of $3^{13}$ with $2$ multiplications. Thus, we only need a fast method to compute the above sequence of $2^k$-th powers of $3$. This is easy, because any element in the sequence (except the first) is the square of its predecessor.
    
    Based on this analysis, the computation process for $3^{13}$ can be obtained as follows:
    
    $$
    \begin{aligned}
    3^1 &= 3, \\
    3^2 &= \left(3^1\right)^2 = 3^2 = 9, \\
    3^4 &= \left(3^2\right)^2 = 9^2 = 81, \\
    3^8 &= \left(3^4\right)^2 = 81^2 = 6561, \\
    3^{13} &= 6561 \times 81 \times 3 = 1594323.
    \end{aligned}
    $$
    
    In the process, only $5$ multiplications were performed.

This is the basic idea of fast exponentiation. As for the specific implementation, there are two common versions.

### Iterative version

Let the binary representation of $n$ be $(n_tn_{t-1}\cdots n_1n_0)_2$, that is,

$$
n = n_t2^t + n_{t-1}2^{t-1} + \cdots + n_12^1 + n_02^0,
$$

where $n_i\in\{0,1\}$. Then, we have

$$
\begin{aligned}
a^n & = a^{n_t2^t + n_{t-1}2^{t-1} + \cdots + n_12^1 + n_02^0}\\
& = a^{n_0 2^0} \times a^{n_1 2^1}\times \cdots \times a^{n_{t-1}2^{t-1}} \times a^{n_t2^t}.
\end{aligned}
$$

Note that only the terms with $n_i=1$ actually appear in the computation of the product.

Based on this expression, one can first compute in $\Theta(\log n)$ time the values of the $\Theta(\log n)$ powers of the form $2^k$ of $a$, then spend $\Theta(\log n)$ time selecting the powers corresponding to the binary bits equal to $1$ and multiplying them into the final result. This is the iterative-version implementation of fast exponentiation.

The pseudocode is as follows:

$$
\begin{array}{l}
\textbf{Algorithm }\text{FastPow}(a, n): \\
\textbf{Input. }\text{Base }a\text{ and exponent }n.\\
\textbf{Output. }\text{Power }a^n.\\
\textbf{Method.}\\
\begin{array}{ll}
1 & \textit{result}\gets\mathrm{Id}\\
2 & \textbf{while }n > 0\textbf{ do}\\
3 & \qquad \textbf{if }n \bmod 2 = 1\textbf{ then}\\
4 & \qquad \qquad \textit{result} \gets \textit{result}\cdot a\\
5 & \qquad \textbf{end if}\\
6 & \qquad a \gets a \cdot a\\
7 & \qquad n \gets n / 2\\
8 & \textbf{end while}\\
9 & \textbf{return }\textit{result}
\end{array}
\end{array}
$$

Computing fast exponentiation using this method requires $\Theta(\log n)$ multiplications.

### Recursive version

This process can likewise be implemented in a recursive form. Note that the binary expansion of the exponent $n$ can be written recursively as

$$
(n_tn_{t-1}\cdots n_1n_0)_2 = 2 \times (n_tn_{t-1}\cdots n_1)_2 + n_0.
$$

Therefore, the power $a^n$ can be computed recursively as

$$
a^n = \begin{cases}
1, & n = 0,\\
(a^{\lfloor n/2\rfloor})^2, & n > 0 \text{ and }n\text{ is even},\\
(a^{\lfloor n/2\rfloor})^2\cdot a, & n > 0 \text{ and }n\text{ is odd}.\\
\end{cases}
$$

This is the recursive-version implementation of fast exponentiation.

The pseudocode is as follows:

$$
\begin{array}{l}
\textbf{Algorithm }\text{FastPow}(a, n): \\
\textbf{Input. }\text{Base }a\text{ and exponent }n.\\
\textbf{Output. }\text{Power }a^n.\\
\textbf{Method.}\\
\begin{array}{ll}
1 & \textbf{if }n = 0\textbf{ then}\\
2 & \qquad \textbf{return }\mathrm{Id}\\
3 & \textbf{end if}\\
4 & \textit{result} \gets \text{FastPow}(a, n / 2) \\
5 & \textbf{if }n\bmod 2 = 0\textbf{ then}\\
6 & \qquad \textbf{return }\textit{result}\cdot\textit{result}\\
7 & \textbf{else}\\
8 & \qquad \textbf{return }\textit{result}\cdot\textit{result}\cdot a\\
9 & \textbf{end if}
\end{array}
\end{array}
$$

Computing fast exponentiation using this method requires $\Theta(\log n)$ recursions and likewise $\Theta(\log n)$ multiplications. Although the complexity is the same, since recursion itself has a certain overhead, in practice the iterative version is faster.

## Applications

### Exponentiation under a modulus

???+ example "[Luogu P1226 【模板】快速幂](https://www.luogu.com.cn/problem/P1226)"
    Given three integers $a,b,p$, find $a^b\bmod p$, where $p\ge 2$.

This is a very common application; for example, it can be used to compute the multiplicative inverse under a modulus. Since we know that the modulo operation does not interfere with multiplication, we only need to take the modulus during the computation.

First, we can directly implement the recursive method described above:

???+ note "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/binary-exponentiation/luogu-P1226-1.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/binary-exponentiation/luogu-P1226-1.py:core"
        ```

The second implementation method is non-recursive. It accumulates into the answer, during the loop, the powers corresponding to the binary bits equal to 1. Although the theoretical complexity of the two is the same, the second is faster in practice, because recursion incurs a certain overhead.

???+ note "Reference implementation"
    === "C++"
        ```cpp
        --8<-- "docs/math/code/binary-exponentiation/luogu-P1226-2.cpp:core"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/math/code/binary-exponentiation/luogu-P1226-2.py:core"
        ```

???+ warning "Note"
    -   The modulus is usually greater than $1$. In a very special case, the modulus $p$ may equal $1$, and then the case $b=0$ needs special consideration.
    -   When the exponent is very large, one needs to reduce the exponent using the [extended Euler's theorem](./number-theory/fermat.md#extended-eulers-theorem) before computing.

### Computing Fibonacci numbers

Based on the recurrence $F_n = F_{n-1} + F_{n-2}$ of the Fibonacci sequence, we can construct a $2\times 2$ matrix to represent the transformation from $F_i,F_{i+1}$ to $F_{i+1},F_{i+2}$. Then, when computing the $n$-th power of this matrix, using the idea of fast exponentiation, we can compute the result in $\Theta(\log n)$ time. For more details, see [Fibonacci sequence](./combinatorics/fibonacci.md); for the implementation of matrix fast exponentiation, see the implementation in [matrix-accelerated recurrence](../math/linear-algebra/matrix.md#matrix-accelerated-recurrence).

### Repeated permutation

???+ note "Problem statement"
    Given a sequence of length $n$ and a permutation, apply this permutation to the sequence $k$ times.

Simply take the $k$-th power of this permutation, then apply it to the sequence. The time complexity is $O(n \log k)$. For more details, see [composition of permutations](./permutation.md#复合).

???+ warning "Note"
    Building a graph from this permutation, then doing the $k$-th power on each cycle separately (in fact equivalent to taking $k$ modulo the cycle length), can solve this problem in $O(n)$ time complexity.

### Speeding up operations on point sets in geometry

???+ example "[HDU 4087 A Letter to Programmers](https://acm.hdu.edu.cn/showproblem.php?pid=4087)"
    Given $n$ points $p_i$ in three-dimensional space, we are required to apply $m$ operations to these points. There are 3 kinds of operations:
    
    1.  Shift the position of a point along some vector (Shift).
    2.  Scale the coordinates of a point proportionally (Scale).
    3.  Rotate around some straight line (Rotate).
    
    There is also a special operation, namely repeating some sequence of operations $k$ times (Repeat); the Repeat operation can be nested. Output the coordinates of each point after the operations end.

Referring to the content in [vectors and matrices](./linear-algebra/vector.md#vectors-and-matrices), each kind of operation can be represented by a transformation matrix, and a series of consecutive transformations can be represented by the product of matrices. One Repeat operation is equivalent to taking the $k$-th power of a matrix. In this way, one can compute the final matrix formed by the entire transformation sequence in $O(m \log k)$ time. Finally, applying it to the $n$ points gives an overall complexity of $O(n + m \log k)$.

### Counting fixed-length paths

???+ note "Problem statement"
    Given a directed graph (with edge weight 1), find the number of paths of length $k$ from $u$ to $v$ between any two points $u,v$.

We take the $k$-th power of the adjacency matrix $M$ of this graph; then $M_{i,j}$ represents the number of paths of length $k$ from $i$ to $j$. The complexity of this algorithm is $O(n^3 \log k)$. For details of this algorithm, see the [matrix](./linear-algebra/matrix.md#fixed-length-path-counting) page.

### Integer multiplication under a modulus

???+ note "Problem statement"
    Given non-negative integers $a,b$ and a positive integer $m$, compute $a\times b\bmod m$, where $a,b\le m\le 10^{18}$.

Just like the idea of binary exponentiation, this time we represent one of the multipliers as a sum of several integer powers of 2. Because when doing the operation of multiplying a number by 2 and taking the modulus, we can convert it into addition/subtraction operations to prevent integer overflow. This can solve the problem in $O (\log m)$ time complexity. The recursive method is as follows:

$$
a \cdot b = \begin{cases}
0 &\text{if }a = 0 \\
2 \cdot \frac{a}{2} \cdot b &\text{if }a > 0 \text{ and }a \text{ even} \\
2 \cdot \frac{a-1}{2} \cdot b + b &\text{if }a > 0 \text{ and }a \text{ odd}
\end{cases}
$$

But in actual use, this method is not efficient in time because it introduces greater computational complexity. In actual programming, one usually uses [fast multiplication](./number-theory/mod-arithmetic.md#fast-multiplication) to perform multiplication when the modulus is in the range of `long long`.

### High-precision fast exponentiation

Prerequisite skill: [big-integer multiplication](./bignum.md#multiplication)

???+ example "[Luogu P1045 \[NOIP 2003 普及组\] 麦森数](https://www.luogu.com.cn/problem/P1045)"
    Given an integer $P$ ($1000 < P < 3100000$), compute the number of digits of $2^P−1$ and its last $500$ digits (expressed as a decimal number), padding the high-order positions with 0 when there are fewer than $500$ digits.

??? note "Code implementation"
    ```cpp
    --8<-- "docs/math/code/binary-exponentiation/luogu-P1045.cpp"
    ```

## Preprocessed fast exponentiation with a fixed base

When the base $a$ is fixed, one can use the [block decomposition idea](../ds/decompose.md) to, after a certain amount of preprocessing time, answer a single power query in $O(1)$ time. This algorithm is also often called light-speed exponentiation. The procedure is as follows:

1.  Choose a number $s$, and preprocess the values of $a^0,a^1,\cdots,a^{s-1}$ and $a^0,a^s,\cdots,a^{\lfloor p/s\rfloor s}$ and store them in two arrays;
2.  For each query $a^b$, split $b$ into $\lfloor b/s\rfloor s+(b\bmod s)$; then $a^b=a^{\lfloor b/s\rfloor s}\cdot a^{b\bmod s}$, so the answer can be found in $O(1)$.

Assuming the range of the exponent $b$ is $[0,n]$, the block length $s$ is often chosen as $\sqrt{n}$ or a nearby power of $2$. Choosing $\sqrt{n}$ gives the optimal preprocessing complexity $O(\sqrt{n})$, while choosing a power of $2$ allows the use of bit operations to simplify the computation.

In particular, for the computation of powers under a modulus, the base $a$ being the same implies the requirement that the modulus $m$ also be the same. By the [extended Euler's theorem](./number-theory/fermat.md#extended-eulers-theorem), for any modulus $m$, the upper bound of the preprocessing exponent range is $n = 2\varphi(m)$; for a prime modulus $p$, the upper bound of the preprocessing range is $n = p - 1$. In both of these cases the preprocessing complexity is $O(\sqrt{m})$.

???+ example "Reference code"
    ```cpp
    --8<-- "docs/math/code/binary-exponentiation/pre-exp.cpp:core"
    ```

## Exercises

-   [UVa 1230 - MODEX](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3671)
-   [UVa 374 - Big Mod](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=310)
-   [UVa 11029 - Leading and Trailing](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1970)
-   [Codeforces - Parking Lot](http://codeforces.com/problemset/problem/630/I)
-   [SPOJ - The last digit](http://www.spoj.com/problems/LASTDIG/)
-   [SPOJ - Locker](http://www.spoj.com/problems/LOCKER/)
-   [SPOJ - Just add it](http://www.spoj.com/problems/ZSUM/)

**Part of the content of this page is translated from the blog post [Бинарное возведение в степень](http://e-maxx.ru/algo/binary_pow) and its English translation [Binary Exponentiation](https://cp-algorithms.com/algebra/binary-exp.html). The Russian version is under the Public Domain + Leave a Link license; the English version is under the CC-BY-SA 4.0 license.**
