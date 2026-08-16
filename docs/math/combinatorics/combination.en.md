## Introduction

Permutations and combinations are fundamental in combinatorics. A permutation refers to taking a specified number of elements from a given number of elements and arranging them in order; a combination refers to merely taking a specified number of elements from a given number of elements, without regard to order. The central problem of permutations and combinations is to study the total number of possible cases of permutations and combinations meeting given requirements. Permutations and combinations are closely related to classical probability theory.

In high-school elementary mathematics, permutations and combinations are mostly solved using methods such as tabulation and enumeration.

## Addition & multiplication principles

### Addition principle

There are $n$ classes of methods to complete a task, and $a_i(1 \le i \le n)$ denotes the number of methods in the $i$-th class. Then there are a total of $S=a_1+a_2+\cdots +a_n$ different methods to complete this task.

### Multiplication principle

Completing a task requires $n$ steps, and $a_i(1 \le i \le n)$ denotes the number of different methods for the $i$-th step. Then there are a total of $S = a_1 \times a_2 \times \cdots \times a_n$ different methods to complete this task.

## Basics of permutations and combinations

### Number of permutations

Taking any $m$ ($m\leq n$, both $m$ and $n$ are natural numbers, likewise below) elements from $n$ distinct elements and arranging them in a row in a certain order is called a permutation of $m$ elements taken from $n$ distinct elements; the number of all permutations of $m$($m\leq n$) elements taken from $n$ distinct elements is called the number of permutations of $m$ elements taken from $n$ distinct elements, denoted by the symbol $\mathrm A_n^m$ (or $\mathrm P_n^m$).

The formula for computing permutations is as follows:

$$
\mathrm A_n^m = n(n-1)(n-2) \cdots (n-m+1) = \frac{n!}{(n - m)!}
$$

$n!$ denotes the factorial of $n$, i.e. $6! = 1 \times 2 \times 3 \times 4 \times 5 \times 6$.

The formula can be understood this way: $n$ people select $m$ to line up ($m \le n$). The first position can be chosen from $n$ people, the second position from $n-1$, and so on, and the $m$-th (last) can be chosen from $n-m+1$, giving:

$$
\mathrm A_n^m = n(n-1)(n-2) \cdots (n-m+1) = \frac{n!}{(n - m)!}
$$

Full permutation: all $n$ people line up, and the queue length is $n$. The first position can be chosen from $n$ people, the second from $n-1$, and so on, giving:

$$
\mathrm A_n^n = n(n-1)(n-2) \cdots 3 \times 2 \times 1 = n!
$$

A full permutation is a special case of the number of permutations.

### Number of combinations

Taking any $m \leq n$ elements from $n$ distinct elements to form a set is called a combination of $m$ elements taken from $n$ distinct elements; the number of all combinations of $m \leq n$ elements taken from $n$ distinct elements is called the number of combinations of $m$ elements taken from $n$ distinct elements, denoted by the symbol $\dbinom{n}{m}$, read as "$n$ choose $m$".

Formula for computing the number of combinations:

$$
\dbinom{n}{m} = \frac{\mathrm A_n^m}{m!} = \frac{n!}{m!(n - m)!}
$$

How to understand the above formula? We consider $n$ people selecting $m$ ($m \le n$), without lining up, without regard to order. If order matters, then it is $\mathrm A_n^m$; if not, then we must divide out the repetitions—so how many repetitions are there? The same selected $m$ people still have a "full permutation", giving $m!$, so:

$$
\begin{aligned}
\dbinom{n}{m} \times m! &= \mathrm A_n^m\\
\dbinom{n}{m} &= \frac{\mathrm A_n^m}{m!} = \frac{n!}{m!(n-m)!}
\end{aligned}
$$

The number of combinations is also often denoted $\mathrm C_n^m$, i.e. $\displaystyle \mathrm C_n^m=\binom{n}{m}$. Nowadays the mathematical community generally adopts the notation $\dbinom{n}{m}$ rather than $\mathrm C_n^m$.

The number of combinations is also called the "binomial coefficient"; the binomial theorem below will explain the connection.

In particular, it is stipulated that when $m>n$, $\mathrm A_n^m=\dbinom{n}{m}=0$.

## Stars and bars

The stars and bars method is a technique for finding the number of ways to divide identical elements into groups in a class of problems, and can also be used to find the number of groups of solutions of a class of linear Diophantine equations.

### Number of positive-integer sums

Problem 1: Given $n$ **identical** elements, required to be divided into $k$ groups, guaranteeing that each group has at least one element, how many ways are there in total?

Consider taking $k - 1$ bars and inserting them into the $n - 1$ gaps formed pairwise between the $n$ elements.

Because the elements are identical, the answer is $\dbinom{n - 1}{k - 1}$.

Essentially this finds the number of groups of positive-integer solutions of $x_1+x_2+\cdots+x_k=n$.

### Number of non-negative-integer sums

Problem 2: What if the problem changes a bit and each group is allowed to be empty?

Obviously we cannot directly insert bars in this case, because it may happen that many bars are inserted into a single gap, which is very hard to count.

We consider creating conditions to transform it into the constrained Problem 1: first borrow $k$ elements, and insert bars into the $n + k - 1$ gaps formed by these $n + k$ elements; the answer is

$$
\binom{n + k - 1}{k - 1} = \binom{n + k - 1}{n}
$$

Although this is not a direct solution of the original problem, this expression is precisely the answer to the original problem, which can be understood as follows:

At the beginning we borrowed $k$ elements, used to guarantee that each group has at least one element; after inserting the bars, we then take these $k$ borrowed elements away from the $k$ groups. Because the elements are identical, the transformed cases and the pre-transformation cases can be put in one-to-one correspondence, so the answers are equal.

From this we can derive the formula of the stars and bars method: $\dbinom{n + k - 1}{n}$.

Essentially this finds the number of groups of non-negative-integer solutions of $x_1+x_2+\cdots+x_k=n$ (i.e. requiring $x_i \ge 0$).

### Number of sums with distinct lower bounds

Problem 3: If we extend one more step, requiring that for the $i$-th group, at least $a_i,\sum a_i \le n$ elements be allotted?

Essentially this finds the number of solutions of $x_1+x_2+\cdots+x_k=n$, where $x_i \ge a_i$.

By analogy with the unconstrained case, we borrow $\sum a_i$ elements to guarantee that the $i$-th group can be allotted at least $a_i$. That is, let

$$
x_i^{\prime}=x_i-a_i
$$

giving a new equation:

$$
\begin{aligned}
(x_1^{\prime}+a_1)+(x_2^{\prime}+a_2)+\cdots+(x_k^{\prime}+a_k)&=n\\
x_1^{\prime}+x_2^{\prime}+\cdots+x_k^{\prime}&=n-a_1-a_2-\cdots-a_k\\
x_1^{\prime}+x_2^{\prime}+\cdots+x_k^{\prime}&=n-\sum a_i
\end{aligned}
$$

where

$$
x_i^{\prime}\ge 0
$$

Then Problem 3 is transformed into Problem 2, and directly using the stars and bars formula gives the answer

$$
\binom{n - \sum a_i + k - 1}{n - \sum a_i}
$$

### Non-adjacent arrangements

Selecting $k$ from the $n$ natural numbers $1 \sim n$, the number of combinations in which no two of these $k$ numbers are adjacent is $\dbinom {n-k+1}{k}$.

## Binomial theorem

Before entering the advanced part of permutations and combinations, we first introduce a theorem closely related to the number of combinations—the binomial theorem.

The binomial theorem clarifies the coefficients of an expansion:

$$
(a+b)^n=\sum_{i=0}^n\binom{n}{i}a^{n-i}b^i
$$

The proof can use mathematical induction, using $\dbinom{n}{k}+\dbinom{n}{k-1}=\dbinom{n+1}{k}$ for the induction.

The binomial theorem can also easily be extended to a polynomial form:

Let $n$ be a positive integer and $x_i$ be real numbers,

$$
(x_1 + x_2 + \cdots + x_t)^n = \sum_{\text{non-negative integer solutions of }n_1 + \cdots + n_t=n} \binom{n}{n_1,n_2,\cdots,n_t} x_1^{n_1}x_2^{n_2}\cdots x_t^{n_t}
$$

Here $\dbinom{n}{n_1,n_2,\cdots,n_t}$ is the multinomial coefficient, and its properties are also very similar:

$$
\sum{\binom{n}{n_1,n_2,\cdots,n_t}} = t^n
$$

## Advanced part of permutations and combinations

Next we introduce some variants of permutations and combinations.

### Number of permutations of a multiset | multinomial coefficient

Everyone please be sure to distinguish the **multinomial coefficient** from the **number of combinations of a multiset**! The two are completely different concepts!

A multiset refers to a generalized set containing repeated elements. Let $S=\{n_1\cdot a_1,n_2\cdot a_2,\cdots,n_k\cdot a_k\}$ denote the multiset composed of $n_1$ copies of $a_1$, $n_2$ copies of $a_2$, …, $n_k$ copies of $a_k$; the number of full permutations of $S$ is

$$
\frac{n!}{\prod_{i=1}^kn_i!}=\frac{n!}{n_1!n_2!\cdots n_k!}
$$

This amounts to dividing out the number of permutations of identical elements. Specifically, you can consider that you have $k$ kinds of distinct balls, with the number of each kind being $n_1,n_2,\cdots,n_k$ respectively, and $n=n_1+n_2+\ldots+n_k$. The number of full permutations of these $n$ balls is the **number of permutations of the multiset**. The number of permutations of a multiset is often called the **multinomial coefficient**. We can express the above using the notation of the multinomial coefficient:

$$
\binom{n}{n_1,n_2,\cdots,n_k}=\frac{n!}{\prod_{i=1}^kn_i!}
$$

One can see that $\dbinom{n}{m}$ is equivalent to $\dbinom{n}{m,n-m}$, only the latter is more cumbersome, so it is not used.

### Number of combinations of a multiset 1

Let $S=\{n_1\cdot a_1,n_2\cdot a_2,\cdots,n_k\cdot a_k\}$ denote the multiset composed of $n_1$ copies of $a_1$, $n_2$ copies of $a_2$, …, $n_k$ copies of $a_k$. Then for an integer $r(r<n_i,\forall i\in[1,k])$, the number of ways to select $r$ elements from $S$ to form a multiset is the **number of combinations of the multiset**. This problem is equivalent to the number of non-negative-integer solutions of $x_1+x_2+\cdots+x_k=r$, which can be solved by stars and bars, with the answer

$$
\binom{r+k-1}{k-1}
$$

### Number of combinations of a multiset 2

Consider this problem: let $S=\{n_1\cdot a_1,n_2\cdot a_2,\cdots,n_k\cdot a_k,\}$ denote the multiset composed of $n_1$ copies of $a_1$, $n_2$ copies of $a_2$, …, $n_k$ copies of $a_k$. Then for a positive integer $r$, the number of ways to select $r$ elements from $S$ to form a multiset.

This limits the number taken of each kind of element. Similarly, we can transform this problem into solving a constrained linear equation:

$$
\forall i\in [1,k],\ x_i\le n_i,\ \sum_{i=1}^kx_i=r
$$

So the inclusion-exclusion principle naturally comes to mind. The inclusion-exclusion model is as follows:

1.  Universe: the non-negative-integer solutions of $\displaystyle \sum_{i=1}^kx_i=r$.
2.  Property: $x_i\le n_i$.

So let the set satisfying property $i$ be $S_i$, and $\overline{S_i}$ denote the set not satisfying property $i$, i.e. the set satisfying $x_i\ge n_i+1$ (transformed into Problem 3 of stars and bars above). Then the answer is

$$
\left|\bigcap_{i=1}^kS_i\right|=|U|-\left|\bigcup_{i=1}^k\overline{S_i}\right|
$$

By the inclusion-exclusion principle, we have:

$$
\begin{aligned}
\left|\bigcup_{i=1}^k\overline{S_i}\right|
=&\sum_i\left|\overline{S_i}\right|
-\sum_{i,j}\left|\overline{S_i}\cap\overline{S_j}\right|
+\sum_{i,j,k}\left|\overline{S_i}\cap\overline{S_j}\cap\overline{S_k}\right|
-\cdots\\
&+(-1)^{k-1}\left|\bigcap_{i=1}^k\overline{S_i}\right|\\
=&\sum_i\binom{k+r-n_i-2}{k-1}
-\sum_{i,j}\binom{k+r-n_i-n_j-3}{k-1}+\sum_{i,j,k}\binom{k+r-n_i-n_j-n_k-4}{k-1}
-\cdots\\
&+(-1)^{k-1}\binom{k+r-\sum_{i=1}^kn_i-k-1}{k-1}
\end{aligned}
$$

Subtracting the above from the universe $\displaystyle |U|=\binom{k+r-1}{k-1}$ gives the number of combinations of the multiset

$$
Ans=\sum_{p=0}^k(-1)^p\sum_{A}\binom{k+r-1-\sum_{A} n_{A_i}-p}{k-1}
$$

where $A$ plays the role of enumerating subsets, satisfying $|A|=p,\ A_i<A_{i+1}$.

### Circular permutations

All $n$ people come to form a circle; the number of all such arrangements is denoted $\mathrm Q_n^n$. Consider an already-arranged circle among them; breaking it at different positions yields different queues.
So we have

$$
\mathrm Q_n^n \times n = \mathrm A_n^n \Longrightarrow \mathrm Q_n = \frac{\mathrm A_n^n}{n} = (n-1)!
$$

From this we obtain the formula for a partial circular permutation:

$$
\mathrm Q_n^r = \frac{\mathrm A_n^r}{r} = \frac{n!}{r \times (n-r)!}
$$

## Properties of binomial coefficients | binomial corollaries

Since binomial coefficients are very important in OI, here we introduce some properties of binomial coefficients.

$$
\binom{n}{m}=\binom{n}{n-m}\tag{1}
$$

This amounts to taking the complement of the selected set with respect to the universe, so the value is unchanged. (Symmetry)

$$
\binom{n}{k} = \frac{n}{k} \binom{n-1}{k-1}\tag{2}
$$

A recurrence derived from the definition.

$$
\binom{n}{m}=\binom{n-1}{m}+\binom{n-1}{m-1}\tag{3}
$$

The recurrence of binomial coefficients (the formula expression of Pascal's triangle). We can use this formula to derive binomial coefficients in $O(n^2)$ complexity.

$$
\binom{n}{0}+\binom{n}{1}+\cdots+\binom{n}{n}=\sum_{i=0}^n\binom{n}{i}=2^n\tag{4}
$$

This is a special case of the binomial theorem. Taking $a=b=1$ gives the above.

$$
\sum_{i=0}^n(-1)^i\binom{n}{i}=[n=0]\tag{5}
$$

Another special case of the binomial theorem, obtained by taking $a=1, b=-1$. A special case of the expression is that when $n=0$ the answer is $1$.

$$
\sum_{i=0}^k \binom{n}{i}\binom{m}{k-i} = \binom{m+n}{k}\tag{6}
$$

An expression that splits binomial coefficients, used when handling certain data-structure problems. It is called [Vandermonde's identity](https://en.wikipedia.org/wiki/Vandermonde%27s_identity).

$$
\sum_{i=0}^n\binom{n}{i}^2=\binom{2n}{n}\tag{7}
$$

This is a special case of $(6)$, obtained by taking $n=k=m$.

$$
\sum_{i=0}^ni\binom{n}{i}=n2^{n-1}\tag{8}
$$

A weighted-sum expression, which can be proved by differentiating the polynomial function corresponding to $(4)$.

$$
\sum_{i=0}^ni^2\binom{n}{i}=n(n+1)2^{n-2}\tag{9}
$$

Similar to the above, it can be proved by differentiating a polynomial function.

$$
\sum_{l=0}^n\binom{l}{k} = \binom{n+1}{k+1}\tag{10}
$$

This can be proved by combinatorial analysis, considering one by one the number of $k+1$-subsets of $S=\{a_1, a_2, \cdots, a_{n+1}\}$; it is fairly commonly used in identity proofs. It is called the [hockey-stick identity](https://en.wikipedia.org/wiki/Hockey-stick_identity).

$$
\binom{n}{r}\binom{r}{k} = \binom{n}{k}\binom{n-k}{r-k}\tag{11}
$$

This can be proved from the definition.

$$
\sum_{i=0}^n\binom{n-i}{i}=F_{n+1}\tag{12}
$$

where $F$ is the Fibonacci sequence.

$$
\binom{n+k}{k}^2=\sum_{j=0}^k\binom{k}{j}^2\binom{n+2k-j}{2k}\tag{13}
$$

This can be proved via $(6)$. It is called [Li Shanlan's identity](https://en.wikipedia.org/wiki/Li_Shanlan_identity).

## Binomial inversion

Let $f_n$ denote the number of ways to form a specific structure using exactly $n$ distinct elements, and $g_n$ denote the total number of ways to select $i \geq 0$ elements from $n$ distinct elements to form a specific structure.

If $f_n$ is known and $g_n$ is sought, then obviously:

$$
g_n = \sum_{i = 0}^{n} \binom{n}{i} f_i
$$

If $g_n$ is known and $f_n$ is sought, then:

$$
f_n = \sum_{i = 0}^{n} \binom{n}{i} (-1)^{n-i} g_i
$$

The above process of finding $f_n$ from a known $g_n$ is called **binomial inversion**.

### Proof

Expanding $g_i$ in the inversion formula gives:

$$
\begin{aligned}
f_n &= \sum_{i = 0}^{n} \binom{n}{i} (-1)^{n-i} \left[\sum_{j = 0}^{i} \binom{i}{j} f_j\right] \\
&= \sum_{i = 0}^{n}\sum_{j = 0}^{i}\binom{n}{i}\binom{i}{j} (-1)^{n-i}f_j
\end{aligned}
$$

Enumerating $j$ first, then $i$, gives:

$$
\begin{aligned}
f_n &= \sum_{j = 0}^{n}\sum_{i = j}^{n}\binom{n}{i}\binom{i}{j} (-1)^{n-i}f_j \\
&= \sum_{j = 0}^{n}f_j\sum_{i = j}^{n}\binom{n}{i}\binom{i}{j} (-1)^{n-i}
\end{aligned}
$$

Using formula (11) of ["Properties of binomial coefficients | binomial corollaries"](#properties-of-binomial-coefficients-binomial-corollaries) gives:

$$
\begin{aligned}
f_n &= \sum_{j = 0}^{n}f_j\sum_{i = j}^{n}\binom{n}{j}\binom{n - j}{i - j} (-1)^{n-i} \\
&= \sum_{j = 0}^{n}\binom{n}{j}f_j\sum_{i = j}^{n}\binom{n - j}{i - j} (-1)^{n-i}
\end{aligned}
$$

Let $k = i - j$. Then $i = k + j$, and the above becomes:

$$
f_n = \sum_{j = 0}^{n}\binom{n}{j}f_j\sum_{k = 0}^{n - j}\binom{n - j}{k} (-1)^{n-j-k}1^{k}
$$

Using formula (5) of ["Properties of binomial coefficients | binomial corollaries"](#properties-of-binomial-coefficients-binomial-corollaries) gives:

$$
f_n = \sum_{j = 0}^{n}\binom{n}{j}f_j[n = j] = f_n
$$

Q.E.D.
