## Entringer numbers

The Entringer number (Entringer number, [OEIS A008281](http://oeis.org/A008281)) $E(n,k)$ is the number of permutations of the $n+1$ numbers from $0$ to $n$ satisfying the following conditions:

-   the first element is $k$;
-   the element after the first element is smaller than the first element, the next element is larger than the previous element, the next element is smaller than the previous element…… and the size relationships of the following adjacent elements all satisfy such a rule.

The initial values of the Entringer numbers are:

$$
E(0,0)=1
$$

$$
E(n,0)=0
$$

There is a recurrence relation:

$$
E(n,k)=E(n,k-1)+E(n-1,n-k)
$$

## Seidel–Entringer–Arnold triangle

A number triangle formed by an appropriate arrangement of the Entringer numbers is called the Seidel–Entringer–Arnold triangle ([OEIS A008280](http://oeis.org/A008280)). This triangle is the Entringer numbers $E(n,k)$ arranged in "ox-plowing" order:

$$
\begin{aligned}
& E(0,0) \\
& E(1,0) \rightarrow E(1,1) \\
& E(2,2) \leftarrow E(2,1) \leftarrow E(2,0) \\
& E(3,0) \rightarrow E(3,1) \rightarrow E(3,2) \rightarrow E(3,3) \\
& E(4,4) \leftarrow E(4,3) \leftarrow E(4,2) \leftarrow E(4,1) \leftarrow E(4,0)
\end{aligned}
$$

That is:

$$
\begin{aligned}
& 1 \\
& 0 \rightarrow 1 \\
& 1 \leftarrow 1 \leftarrow 0 \\
& 0 \rightarrow 1 \rightarrow 2 \rightarrow 2 \\
& 5 \leftarrow 5 \leftarrow 4 \leftarrow 2 \leftarrow 0
\end{aligned}
$$

The advantage of arranging the Entringer numbers in this way is that it is consistent with its recurrence relation $E(n,k)=E(n,k-1)+E(n-1,n-k)$, which facilitates memorization and understanding.

The Entringer numbers have an exponential generating function:

$$
\sum_{m=0}^\infty\sum_{n=0}^\infty E\left(m+n,\frac{1}{2}\left(m+n+{(-1)}^{m+n}(n-m)\right)\right)\frac{x^m}{m!}\frac{x^n}{n!}=\frac{\cos x+\sin x}{\cos (x+y)}
$$

The coefficient distribution of this generating function is in fact a simple stretched deformation of the Seidel–Entringer–Arnold triangle above:

$$
\begin{array}{ccccc}
E(0,0) & E(1,1) & E(2,0) & E(3,3) & E(4,0) \\
E(1,0) & E(2,1) & E(3,2) & E(4,1) & \\
E(2,2) & E(3,1) & E(4,2) & & \\
E(3,0) & E(4,3) & & & \\
E(4,4) & & & &
\end{array}
$$

That is:

$$
\begin{aligned}
& 1\quad 1\quad 0\quad 2\quad 0\\
& 0\quad 1\quad 2\quad 2\\
& 1\quad 1\quad 4\\
& 0\quad 5\\
& 5
\end{aligned}
$$

## Zigzag permutations

A zigzag permutation is a permutation $c_1$ to $c_i$ of $1$ to $n$ such that the value of any element $c_i$ is not between $c_{i-1}$ and $c_{i+1}$.

For the number of zigzag permutations $Z_n$ ([OEIS A001250](http://oeis.org/A001250)), starting from $n=0$ we have:

$$
1, 1, 2, 4, 10, 32, 122, 544, \cdots
$$

For example, the alternating permutations for the first few $n$ are:

$$
\begin{aligned}
n=1: & \{1\}\\
n=2: & \{1,2\}, \{2,1\}\\
n=3: & \{1,3,2\}, \{2,1,3\}, \{2,3,1\}, \{3,1,2\}\\
n=4: & \{1,3,2,4\}, \{1,4,2,3\}, \{2,1,4,3\}, \{2,3,1,4\}, \{2,4,1,3\}, \\
& \{3,1,4,2\}, \{3,2,4,1\}, \{3,4,1,2\}, \{4,1,3,2\}, \{4,2,3,1\}
\end{aligned}
$$

## Alternating permutations and zigzag numbers

(Note the conceptual distinction from "derangement".)

For $n$ greater than $1$, each zigzag permutation reversed is still a zigzag permutation, and they can be paired up two by two, so the count must be even.

Here we give another pairing method: divide zigzag permutations into alternating permutations and reverse alternating permutations.

The first element of an alternating permutation is greater than the second element, with the size relationship:

$$
c_1>c_2<c_3>\cdots
$$

The first element of a reverse alternating permutation is less than the second element, with the size relationship:

$$
c_1<c_2>c_3<\cdots
$$

If we swap the positions of $1$ and $n$, swap the positions of $2$ and $n-1$, and so on, we can interchange the two sets of alternating permutations and reverse alternating permutations. Therefore, the numbers of alternating permutations and reverse alternating permutations are equal, being exactly half of the number of zigzag permutations.

For $n$ greater than $1$, denote:

$$
A_n=\frac{Z_n}{2}
$$

Define the initial values:

$$
A_0=A_1=1
$$

Here $A_n$ is called the zigzag number (Euler zigzag number, [OEIS A000111](http://oeis.org/A000111)); starting from $n=0$ we have:

$$
1, 1, 1, 2, 5, 16, 61, 272, \cdots
$$

Next let us try to solve for $A_n$.

From $1$ to $n$, selecting $k$ numbers to form a subset, there are $\dbinom{n}{k}$ ways of selection.

In this $k$-element subset, selecting a reverse alternating permutation $u$, there are $A_k$ ways of selection; subtracting this $k$-element subset from the universe, in the remaining $(n-k)$-element subset, selecting a reverse alternating permutation $v$, there are $A_{n-k}$ ways of selection.

Consider an $(n+1)$-element permutation $w$, taking $u$ inverted as the beginning, appending $n+1$, and then appending $v$. Then $w$ is necessarily a zigzag permutation, and any $(n+1)$-element zigzag permutation can be cut at $n+1$ to obtain the corresponding reverse alternating permutations $u$ and $v$, and different $(n+1)$-element zigzag permutations correspond to different $u$ and $v$.

Therefore we have the recurrence relation:

$$
2A_{n+1}=\sum_{k=0}^n \dbinom{n}{k} A_k A_{n-k}
$$

$$
2(n+1)\frac{A_{n+1}}{(n+1)!}=\sum_{k=0}^n \frac{A_k}{k!}\frac{A_{n-k}}{(n-k)!}
$$

When $n$ is $0$ this recurrence does not hold; the initial values $A_0$ and $A_1$ are both $1$.

As one can see, this is a convolution of exponential generating functions. Assuming the exponential generating function of $A_n$ is $y$, we have the differential equation:

$$
2\frac{\mathrm{d}y}{\mathrm{d}x}=y^2+1
$$

Adding $1$ on the right side of the equation is to handle the special case when $n$ is $0$. The general solution of this equation is:

$$
y=\tan\left(\frac{1}{2}x+C\right)
$$

After substituting the fact that the $0$-th term is $1$, we obtain the particular solution:

$$
y=\tan x+\sec x
$$

The tangent function is odd and the secant function is even; the sum of the two forms the generating function of the zigzag numbers.

## Relationship between Entringer numbers and zigzag numbers

By the definition of the Entringer numbers, the Entringer number $E(n,k)$ is the number of alternating permutations of $0$ to $n$ whose first element is $k$. Therefore, the Entringer numbers and the zigzag numbers do in fact have a relationship:

$$
A_n=E(n,n)
$$

There is also a reason for calling $A_n$ the "zigzag number": let $E_n$ be the Euler number and $B_n$ be the Bernoulli number.

When $n$ is even, the zigzag numbers with even index are also called "secant numbers" $S_n$ or "zig numbers". There is a relationship:

$$
A_n=(-1)^{n/2}E_n
$$

The first few terms are ([OEIS A000364](http://oeis.org/A000364)):

$$
1, 1, 5, 61, 1385, \cdots
$$

When $n$ is odd, the zigzag numbers with odd index are also called "tangent numbers" $T_n$ or "zag numbers". There is a relationship:

$$
A_n=\frac{(-1)^{(n-1)/2}2^{n+1}(2^{n+1}-1)B_{n+1}}{n+1}
$$

The first few terms are ([OEIS A000182](http://oeis.org/A000182)):

$$
1, 2, 16, 272, 7936, \cdots
$$

Thus, for the Taylor expansion at $x=0$, one can give the secant numbers and tangent numbers:

$$
\sec x=A_0+A_2\frac{x^2}{2!}+A_4\frac{x^4}{4!}+\cdots
$$

$$
\tan x=A_1x+A_3\frac{x^3}{3!}+A_5\frac{x^5}{5!}+\cdots
$$

Or written together:

$$
\sec x+\tan x=A_0+A_1x+A_2\frac{x^2}{2!}+A_3\frac{x^3}{3!}+A_4\frac{x^4}{4!}+A_5\frac{x^5}{5!}+\cdots
$$

which forms the generating function of the zigzag numbers.

## References and links

1.  [Alternating permutation - Wikipedia](https://en.wikipedia.org/wiki/Alternating_permutation)
