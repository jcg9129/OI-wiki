## Introduction

Vandermonde's convolution is an expression that merges binomial coefficients, mainly applied to formula derivations in combinatorics.

## Vandermonde's convolution formula

$$
\sum_{i=0}^k\binom{n}{i}\binom{m}{k-i}=\binom{n+m}{k}
$$

### Proof

Consider proving it with the binomial theorem:

$$
\begin{aligned}
\sum_{k=0}^{n+m}\binom{n+m}{k}x^k&=(x+1)^{n+m}\\
&=(x+1)^n(x+1)^m\\
&=\sum_{r=0}^n\binom{n}{r}x^r\sum_{s=0}^m\binom{m}{s}x^s\\
&=\sum_{k=0}^{n+m}\sum_{r=0}^k\binom{n}{r}\binom{m}{k-r}x^k\\
\end{aligned}
$$

That is:

$$
\binom{n+m}{k}=\sum_{r=0}^k\binom{n}{r}\binom{m}{k-r}
$$

If we consider its combinatorial-meaning proof:

Taking $k$ numbers from a set of size $n+m$ can be equated to splitting the set of size $n+m$ into two sets of sizes $n$ and $m$ respectively, and then the number of ways to take $i$ numbers from $n$ and $k-i$ numbers from $m$. Since we already have the enumeration over $i$, we only need to consider one way of splitting, because different splittings are equivalent to one another.

## Corollaries

### Corollary 1 and its proof

$$
\sum_{i=-r}^{s}\binom{n}{r+i}\binom{m}{s-i}=\binom{n+m}{r+s}
$$

The proof is similar to that of the original formula.

### Corollary 2 and its proof

$$
\sum_{i=1}^n\binom{n}{i}\binom{n}{i-1}=\binom{2n}{n-1}
$$

Deriving from basic combinatorics knowledge, we have:

$$
\sum_{i=1}^n\binom{n}{i}\binom{n}{i-1}=\sum_{i=0}^{n-1}\binom{n}{i+1}\binom{n}{i}=\sum_{i=0}^{n-1}\binom{n}{n-1-i}\binom{n}{i}=\binom{2n}{n-1}
$$

### Corollary 3 and its proof

$$
\sum_{i=0}^n\binom{n}{i}^2=\binom{2n}{n}
$$

Deriving from basic combinatorics knowledge, we have:

$$
\sum_{i=0}^n\binom{n}{i}^2=\sum_{i=0}^n\binom{n}{i}\binom{n}{n-i}=\binom{2n}{n}
$$

### Corollary 4 and its proof

$$
\sum_{i=0}^m\binom{n}{i}\binom{m}{i}=\binom{n+m}{m}
$$

Deriving from basic combinatorics knowledge, we have:

$$
\sum_{i=0}^m\binom{n}{i}\binom{m}{i}=\sum_{i=0}^m\binom{n}{i}\binom{m}{m-i}=\binom{n+m}{m}
$$

Here $\binom{n+m}{m}$ is the fairly familiar number of ways of grid-path counting. So we can consider its combinatorial-meaning proof.

In a grid graph, going from $(0,0)$ to $(n,m)$ takes a total of $n+m$ steps. Suppose $(0,0)$ is at the upper-left corner of the grid, of which $n$ steps go down and $m$ steps go right; the number of ways is $\binom{n+m}{m}$.

From another perspective, we split the $n+m$ steps into two parts: first walk $n$ steps, then walk $m$ steps; then if among the $n$ steps $i$ steps go right, then among the $m$ steps $m-i$ steps go right, which proves the result.

## Exercises

-   [CF785D Anton and School - 2](https://codeforces.com/problemset/problem/785/D)

-   [Luogu P2791 幼儿园篮球题](https://www.luogu.com.cn/problem/P2791)

## References and notes

1.  [Vandermonde's Convolution Formula](https://www.cut-the-knot.org/arithmetic/algebra/VandermondeConvolution.shtml)
