## Derangement

### Definition

A derangement is a permutation in which no element appears in its ordered position. That is, for a permutation $P$ of $1\sim n$, if $P_i\neq i$ holds, then $P$ is called a derangement of $n$.

For example, the derangements of three elements are $\{2,3,1\}$ and $\{3,1,2\}$. The derangements of four elements are $\{2,1,4,3\}$, $\{2,3,4,1\}$, $\{2,4,1,3\}$, $\{3,1,4,2\}$, $\{3,4,1,2\}$, $\{3,4,2,1\}$, $\{4,1,2,3\}$, $\{4,3,1,2\}$, and $\{4,3,2,1\}$. A derangement is a permutation with no fixed points, i.e. no cycle of length 1.

### Computation by the inclusion-exclusion principle

The universe $U$ is the set of permutations of $1\sim n$, with $|U|=n!$; let $S_i$ be the permutations among them satisfying $P_i\neq i$. Using knowledge of complements and the [inclusion-exclusion principle](./inclusion-exclusion-principle.md), the problem becomes finding:

$$
\begin{aligned}
\left|\bigcap_{i=1}^n S_i\right|
&=|U|-\left|\bigcup_{i=1}^n\overline{S_i}\right|\\
&=n!-\sum_{k=1}^n(-1)^{k-1}\sum_{a_i<a_{i+1}}\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|
\end{aligned}
$$

where the meaning of the summation is to take $a_1, a_2, \cdots, a_k$ from $1, 2, \cdots, n$ satisfying $a_i<a_{i+1}$. Then

$$
\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|
$$

represents the number of permutations in which $k$ numbers $a_1,a_2,\cdots,a_k$ satisfy $P_{a_i}=a_i$, while the positions of the remaining $n-k$ numbers are arbitrary, so:

$$
\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|=(n-k)!
$$

There are $\dbinom{n}{k}$ ways to choose these $k$ numbers; summing over them gives:

$$
\begin{aligned}
&\sum_{k=1}^n(-1)^{k-1}\sum_{a_i<a_{i+1}}\left|\bigcap_{i=1}^{k}\overline{S_{a_i}}\right|\\
=&\sum_{k=1}^n(-1)^{k-1}\dbinom{n}{k}(n-k)!\\
=&\sum_{k=1}^n(-1)^{k-1}\frac{n!}{k!}\\
=&n!\sum_{k=1}^n\frac{(-1)^{k-1} }{k!}
\end{aligned}
$$

Therefore, the number of derangements of $n$ elements is:

$$
D_n=n!-n!\sum_{k=1}^n\frac{(-1)^{k-1} }{k!}=n!\sum_{k=0}^n\frac{(-1)^k}{k!}
$$

The first few terms of the derangement sequence are $0,1,2,9,44,265$ ([OEIS A000166](http://oeis.org/A000166)).

### Computation by recurrence

Making the derangement problem concrete, consider the following problem:

There are $n$ distinct letters, numbered $1,2,3,4,5$; now we want to place these five letters in envelopes numbered $1,2,3,4,5$, requiring that the number of the envelope differs from the number of the letter. How many different placement methods are there?

Suppose we consider up to the $n$-th envelope; initially, temporarily place the $n$-th letter in the $n$-th envelope, then consider the recurrence of two cases:

-   the first $n-1$ envelopes are all misplaced;
-   among the first $n-1$ envelopes, one is not misplaced and the rest are all misplaced.

For the first case, the first $n-1$ envelopes are all misplaced: because the first $n-1$ are all already misplaced, the $n$-th letter only needs to be swapped with any one of the previous positions, giving a total of $D_{n-1}\times (n-1)$ cases.

For the second case, among the first $n-1$ envelopes one is not misplaced and the rest are all misplaced: the purpose of considering this case is that, if among the $n-1$ envelopes one is not misplaced, then swapping that not-misplaced one with $n$ yields a full derangement.

In other cases, it is impossible to turn it into a derangement of length $n$ through a single operation.

Thus we obtain that the number of derangements satisfies the recurrence relation:

$$
D_n=(n-1)(D_{n-1}+D_{n-2})
$$

Here we also give another recurrence relation:

$$
D_n=nD_{n-1}+{(-1)}^n
$$

### Other relations

The number of derangements has a simple rounding expression, whose growth rate differs from the factorial by only a constant:

$$
D_n=\left\lfloor\frac{n!}{\mathrm{e}} + \frac{1}{2}\right\rfloor
$$

As the number of elements increases, the probability $P$ of forming a derangement approaches:

$$
P=\lim_{n\to\infty}\frac{D_n}{n!}=\frac{1}{\mathrm{e}}
$$
