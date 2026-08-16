Prerequisite: [Sqrt decomposition](../ds/decompose.md).

Naive table lookup ("precomputed tables") refers to computing, during a contest, the answers corresponding to all possible inputs and saving them, then declaring an array in the code to hold the answers, so that you can simply output them directly.

Note that this technique only applies to problems where the value range of the input is not large (for example, the input is a single number and its range is very small); otherwise it may cause problems such as overly long code, MLE, or the table taking too long to precompute.

???+ note "Example"
    Define $f(x)$ as the number of $1$s in the binary representation of the integer $x$. Given a positive integer $n$ ($n\leq 10^9$), output $\sum_{i=1}^n f^2(i)$.

If we were to output $f(n)$ for every $n$, then besides possibly getting MLE, the code might also exceed the maximum code length limit, causing the compilation to fail.

We consider optimizing this answer table. Using the idea of [sqrt decomposition](../ds/decompose.md), we set a reasonable step $m$ (this step is generally determined by the code length), and for the $i$-th block we compute the value of:

$$
\sum_{k=\frac{n}{m}(i-1)+1}^{\frac{ni}{m}} f^2(k)
$$

Then, when outputting the answer, we handle it using the block idea. That is, the answer for whole blocks is computed from the precomputed values, and the answer for a non-whole block is computed by brute force.

Generally speaking, for such problems, computing a single function value $f(x)$ is fast, but a large number of function values need to be summed (or multiplied, or combined by some quickly-mergeable operation), and enumeration would exceed the time limit; when no standard approach can be found, a segmented lookup table is a good choice.

???+ note "Note"
    When the exponent in the problem above is not fixed but its range is small, a lookup table can also be considered.

### Examples

["BZOJ 3798" Special Primes](https://hydro.ac/p/bzoj-P3798): Count how many primes in the range $[l,r]$ can be decomposed into the sum of the squares of two positive integers.

["Luogu P1822" Magic Fingerprint](https://www.luogu.com.cn/problem/P1822)
