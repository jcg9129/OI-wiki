author: sshwy, FFjet, qz-cqy

## Introduction

The Euclidean-like algorithm is content proposed by Hong Huadun in a camper exchange session at the 2016 Winter Camp. It is commonly used to solve summation problems for sequences (indexed by $i$) with a structure of the form

$$
\left\lfloor\dfrac{ai+b}{c}\right\rfloor.
$$

Its main idea is to use the recursive structure of fractions themselves to transform the problem into a smaller-scale problem and solve it recursively. Because the recursive structure of fractions has a direct [connection](./continued-fraction.md#finding-the-continued-fraction-representation) with the [Euclidean algorithm](./gcd.md#euclidean-algorithm), this summation method is also called the Euclidean-like algorithm.

Because methods such as [continued fractions](./continued-fraction.md) and the [Stern–Brocot tree](./stern-brocot.md) likewise characterize the recursive structure of fractions, problems that can be solved with the Euclidean-like algorithm can usually also be solved with these methods. Compared with these methods, the Euclidean-like algorithm is usually easier to understand, and its implementation is more concise.

## Euclidean-like algorithm

The simplest example is the summation problem:

$$
f(a,b,c,n)=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,
$$

where $a,b,c,n$ are all positive integers.

### Algebraic solution

First, taking $a,b$ modulo $c$ can simplify the problem, transforming it into the case $0\le a,b<c$:

$$
\begin{aligned}
f(a,b,c,n)&=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor\\
&=\sum_{i=0}^n\left\lfloor
\frac{\left(\left\lfloor\frac{a}{c}\right\rfloor c+(a\bmod c)\right)i+\left(\left\lfloor\frac{b}{c}\right\rfloor c+(b\bmod c)\right)}{c}\right\rfloor\\
&=\sum_{i=0}^n\left(\left\lfloor\frac{a}{c}\right\rfloor i+\left\lfloor\frac{b}{c}\right\rfloor+\left\lfloor\frac{\left(a\bmod c\right)i+\left(b\bmod c\right)}{c}
\right\rfloor\right)\\
&=\frac{n(n+1)}{2}\left\lfloor\frac{a}{c}\right\rfloor
+(n+1)\left\lfloor\frac{b}{c}\right\rfloor+f(a\bmod c,b\bmod c,c,n).
\end{aligned}
$$

Now, consider the transformed problem. Let

$$
m = \left\lfloor \frac{an+b}{c} \right\rfloor.
$$

Then, the original problem can be written as a double summation:

$$
\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor
=\sum_{i=0}^n\sum_{j=0}^{m-1}\left[j<\left\lfloor \frac{ai+b}{c} \right\rfloor\right].
$$

Exchange the summation order; this requires, for each $j$, computing the range of $i$ satisfying the condition. To this end, transform the condition:

$$
\begin{aligned}
&j<\left\lfloor \frac{ai+b}{c} \right\rfloor = \left\lceil \frac{ai+b+1}{c} \right\rceil-1\\
&\iff j + 1 < \left\lceil \frac{ai+b+1}{c} \right\rceil
\iff j+1< \frac{ai+b+1}{c} \\
&\iff \dfrac{cj+c-b-1}{a} < i
\iff \left\lfloor\dfrac{cj+c-b-1}{a}\right\rfloor < i.
\end{aligned}
$$

The transformation process repeatedly uses the properties of the [rounding functions](./basic.md#rounding-functions). Substituting the transformed condition, the original expression can be written as:

$$
\begin{aligned}
f(a,b,c,n)&=\sum_{j=0}^{m-1}
\sum_{i=0}^n\left[i>\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\
&=\sum_{j=0}^{m-1}\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\
&=nm-f\left(c,c-b-1,a,m-1\right).
\end{aligned}
$$

Let $(a',b',c',n')=(c,c-b-1,a,m-1)$; this returns us to the case $a'>c'$ discussed earlier.

Combining these two transformation steps, we can find that during the process, $(a,c)$ are repeatedly taken modulo and then swapped, until $a=0$. This is similar to performing the Euclidean division on $(a,c)$, which is also the origin of the name Euclidean-like algorithm. Its time complexity is $O(\log\min\{a,c\})$.

During the computation, the case $m=0$ may occur, at which point the inner recursion will have $n=-1$. This does not affect the final result. However, if we require terminating the algorithm directly when $m=0$ occurs, then the time complexity of the algorithm can be improved to $O(\log\min\{a,c,n\})$.

??? note "Explanation of the complexity"
    Using the similarity between this algorithm and the Euclidean algorithm, it is easy to show that its time complexity is $O(\log\min\{a,c\})$. Therefore, we only need to show that if the algorithm terminates when $m=0$, then its time complexity is also $O(\log n)$.
    
    Let $m=\lfloor(an+b)/c\rfloor$, and denote $S=mn$, $k=m/n$; they respectively correspond to the area of the lattice diagram and the slope of the line in the geometric intuition (see the next section). For sufficiently large $n$, approximately $k\doteq a/c$.
    
    Examine the changes of $S$ and $k$ during the algorithm. In the first step, when taking the modulus, $n$ remains unchanged, and $k$ approximately changes from $a/c$ to $(a\bmod c)/c$, which corresponds to the slope changing from $k$ to $k-\lfloor k\rfloor$, and $S$ also approximately becomes $(k-\lfloor k\rfloor)$ times its original value. In the second step, when swapping the horizontal and vertical coordinates, $S$ approximately remains unchanged, and $k$ becomes its reciprocal. Therefore, if after the two-step operation the pair $(k,S)$ becomes $(k',S')$, then we have $k'=(k-\lfloor k\rfloor)^{-1}$ and $S'=(k-\lfloor k\rfloor)S$.
    
    Because $1\le\lfloor k'\rfloor\le k'<\lfloor k'\rfloor+1$, after two rounds of recursive computation, the product shrinks by a factor of at least
    
    $$
    (k'-\lfloor k'\rfloor)(k-\lfloor k\rfloor) = 1-\dfrac{\lfloor k'\rfloor}{k'} < 1-\dfrac{\lfloor k'\rfloor}{\lfloor k'\rfloor+1} = \dfrac{1}{\lfloor k'\rfloor+1}\le \dfrac{1}{2}.
    $$
    
    Therefore, after at most $O(\log S)$ rounds, the algorithm must terminate. Because starting from the second round, the $S$ at the beginning of each round is always no more than the $S$ at the end of the previous round's modulus operation, and the latter is roughly $kn^2$ with $k<1$, we have $O(\log S)\subseteq O(\log n)$. This gives the above conclusion.

A reference implementation of the template problem is as follows:

??? example "Template problem implementation ([Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear))"
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-0.cpp:full-text"
    ```

### Geometric intuition

This algorithm can also be understood from a geometric perspective. The problems that the Euclidean-like algorithm can solve are mainly lattice-point counting problems below a line.

As shown in the leftmost part of the figure below, this summation is equivalent to counting the lattice points below the line

$$
y = \dfrac{ax+b}{c}
$$

and above the $x$-axis (not including the $x$-axis), with horizontal coordinate in $[0,n]$.

![](./images/euclidean-1.svg)

First, remove the integer parts of the slope and intercept. This step is equivalent to computing the number of blue points in the middle part of the figure above separately. When the slope and intercept are both integers, the blue points must form a trapezoidal array, that is, the lattice points in different columns form an arithmetic sequence, so the number of these points is easy to compute. After removing these points, the remaining lattice points are consistent in number with the red points in the rightmost part of the figure above. The problem is then transformed into the case where both the slope and the intercept are less than one. Because the height of the trapezoid is $n+1$ and the two base lengths are $\lfloor b/c\rfloor$ and $(\lfloor a/c\rfloor n+\lfloor b/c\rfloor)$ respectively, using the trapezoid area formula, this step can be summarized into the formula

$$
f(a,b,c,n) = f(a\bmod c,b\bmod c,c,n) + \dfrac{1}{2}(n+1)\left(\left\lfloor\dfrac{b}{c}\right\rfloor+\left(\left\lfloor\dfrac{a}{c}\right\rfloor n+\left\lfloor\dfrac{b}{c}\right\rfloor\right)\right).
$$

Then, flip the horizontal and vertical coordinate axes. As shown in the leftmost part of the figure below, the red points and blue points in the figure form a rectangular lattice with horizontal length $n$ and vertical length $m=\lfloor(an+b)/c\rfloor$. To compute the number of red points, we only need to compute the number of blue points, and then subtract the number of blue points from the number of the rectangular lattice. After flipping, the blue point lattice in the left half of the figure above becomes a red point lattice below some line. Moreover, after flipping, the slope is greater than one, which returns to the case already handled above.

![](./images/euclidean-2.svg)

The key is how to compute the equation of the line above the new red point lattice. Flipping the horizontal and vertical coordinate axes of the leftmost part of the figure above gives the middle part of the figure above. The line above the flipped red point lattice (the solid line in the middle part) does not correspond to the flipped pre-flip line (the solid line in the leftmost part), but is the result of translating the pre-flip line slightly to the upper left (the dashed line in the leftmost part). This is because, if we directly flip the line (the solid line in the leftmost part), we obtain the dashed line in the middle part, but by definition, the lattice points below it include the lattice points exactly on the line, which would lead to double-counting the lattice points on the line. To avoid this, we need to translate the line $y=(cx-b)/a$ obtained by flipping the line $y=(ax+b)/c$ slightly downward to obtain the line $y=(cx-b-1)/a$, so that the lattice below it is exactly the pre-flip blue point lattice.

There is another detail to handle. The intercept of the line in the middle part of the figure above is negative, which means we have not yet returned to the initial case. To make the intercept non-negative again, we only need to translate the line (the solid line in the middle part) one unit to the left. Doing so does not miss any lattice point, because the pre-flip blue point lattice has no point with vertical coordinate zero, so after flipping there is no point with horizontal coordinate zero. Finally, the line equation becomes $y=(cx+c-b-1)/a$; at the same time, the upper bound of the horizontal coordinate of the lattice also changes from $m$ to $m-1$. This step can be summarized into the formula

$$
f(a,b,c,n) = mn - f(c,c-b-1,a,m-1).
$$

This recursive algorithm works, mainly for two reasons:

-   First, the slope of the line repeatedly takes its fractional part and then its reciprocal, which is equivalent to computing the [continued fraction expansion](./continued-fraction.md#finding-the-continued-fraction-representation) of the line's slope $k=a/c$. Because the length of the continued fraction expansion of a rational fraction is $O(\log\min\{a,c\})$, this process must terminate after $O(\log\min\{a,c\})$ steps;
-   Second, because each time the coordinate axes are flipped, the slope of the line is less than one, so intuitively we should have $m<n$, that is, after one such round of iteration, the range of the horizontal coordinate keeps shrinking. The complexity calculation earlier shows, through rigorous analysis, that after every two rounds of iteration, $n$ is at most half of its original value, so this process must terminate after $O(\log n)$ steps.

This is also the reason why the complexity of the Euclidean-like algorithm when the slope is rational is $O(\log\min\{a,c,n\})$.

Using similar geometric intuition, the Euclidean-like algorithm can be generalized to the case where the slope is irrational; for the specific analysis, please refer to the example problems later.

### Example problems

???+ example "[【模板】类欧几里得算法](https://www.luogu.com.cn/problem/P5170)"
    Multiple queries. Given positive integers $a,b,c,n$, find
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    g(a,b,c,n) &= \sum_{i=0}^ni\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    h(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor^2.
    \end{aligned}
    $$

??? note "Solution 1"
    Similar to the derivation of $f$, we can obtain the recursive expressions for $g,h$.
    
    First, using the modulus, transform the problem into the case $0\le a,b<c$:
    
    $$
    \begin{aligned}
    g(a,b,c,n)
    &=g(a\bmod c,b\bmod c,c,n)+\left\lfloor\frac{a}{c}\right\rfloor\frac{n(n+1)(2n+1)}{6}+\left\lfloor\frac{b}{c}\right\rfloor\frac{n(n+1)}{2}, \\
    h(a,b,c,n)&=h(a\bmod c,b\bmod c,c,n)\\
    &\quad+2\left\lfloor\frac{b}{c}\right\rfloor f(a\bmod c,b\bmod c,c,n)
    +2\left\lfloor\frac{a}{c}\right\rfloor g(a\bmod c,b\bmod c,c,n)\\
    &\quad+\left\lfloor\frac{a}{c}\right\rfloor^2\frac{n(n+1)(2n+1)}{6}+\left\lfloor\frac{b}{c}\right\rfloor^2(n+1)
    +\left\lfloor\frac{a}{c}\right\rfloor\left\lfloor\frac{b}{c}\right\rfloor n(n+1).
    \end{aligned}
    $$
    
    Then, using the exchange of summation order, we can transform further. Similarly, let
    
    $$
    m = \left\lfloor \frac{an+b}{c} \right\rfloor.
    $$
    
    Then, for the sum $g$, we have
    
    $$
    \begin{aligned}
    g(a,b,c,n)&=\sum_{i=0}^ni\left\lfloor \frac{ai+b}{c} \right\rfloor\\
    &=\sum_{i=0}^n \sum_{j=0}^{m-1}i
    \left[j<\left\lfloor\frac{ai+b}{c}\right\rfloor\right] \\
    &=\sum_{j=0}^{m-1}\sum_{i=0}^n i\left[i>\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\
    &=\sum_{j=0}^{m-1}\dfrac{1}{2}\left(\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor+n+1\right)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\
    &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - \dfrac{1}{2}\sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor^2\\
    &=\dfrac{1}{2}mn(n+1) - \dfrac{1}{2}f(c,c-b-1,a,m-1) - \dfrac{1}{2}h(c,c-b-1,a,m-1).
    \end{aligned}
    $$
    
    For the sum $h$, we have
    
    $$
    \begin{aligned}
    h(a,b,c,n)&=\sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor^2\\
    &=\sum_{i=0}^n\sum_{j=0}^{m-1}(2j+1)\left[j<\left\lfloor\frac{ai+b}{c}\right\rfloor\right]\\
    &=\sum_{j=0}^{m-1}\sum_{i=0}^n(2j+1)\left[i>\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor \right]\\
    &=\sum_{j=0}^{m-1}(2j+1)\left(n-\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\right)\\
    &=nm^2 - \sum_{j=0}^{m-1}\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor - 2\sum_{j=0}^{m-1}j\left\lfloor\frac{cj+c-b-1}{a}\right\rfloor\\
    &=nm^2 - f(c,c-b-1,a,m-1) - 2g(c,c-b-1,a,m-1).
    \end{aligned}
    $$
    
    From the perspective of geometric intuition, these nonlinear sums are equivalent to assigning each point $(i,j)$ in the region a corresponding weight $w(i,j)$. Apart from these weights, the computation process of the rest is entirely consistent. For the choice of weights, in general, we have
    
    $$
    \sum_{i=0}^ni^r\left\lfloor \frac{ai+b}{c} \right\rfloor^s = \sum_{i=0}^n\sum_{j=0}^{m-1} i^r\left((j+1)^s-j^s\right)\left[j<\left\lfloor\frac{ai+b}{c}\right\rfloor\right].
    $$
    
    Another feature of this problem is that $g$ and $h$ interleave with each other during recursive computation. Therefore, we need to recurse on $(f,g,h)$ simultaneously as a triple.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-1.cpp"
    ```

???+ example "[\[清华集训 2014\] Sum](https://www.luogu.com.cn/problem/P5172)"
    Multiple queries. Given positive integers $n$ and $r$, find
    
    $$
    \sum_{d=1}^n(-1)^{\lfloor d\sqrt{r}\rfloor}.
    $$

??? note "Solution 1"
    If $r$ is a perfect square, then when $\sqrt{r}$ is even, the sum is $n$; otherwise, the sum alternates between $0$ and $-1$ depending on the parity of $n$. Below we consider the case where $r$ is not a perfect square.
    
    To apply the Euclidean-like algorithm, first transform the sum into a familiar form:
    
    $$
    \begin{aligned}
    \sum_{d=1}^n(-1)^{\lfloor d\sqrt{r}\rfloor} &= \sum_{d=1}^n\left(1 - 2(\lfloor d\sqrt{r}\rfloor\bmod 2)\right)\\
    &= n - 2\sum_{d=1}^n\left(\lfloor d\sqrt{r}\rfloor - 2\left\lfloor\dfrac{\lfloor d\sqrt{r}\rfloor}{2}\right\rfloor\right) \\
    &= n - 2\sum_{d=1}^n\lfloor d\sqrt{r}\rfloor + 4 \sum_{d=1}^n\left\lfloor\dfrac{d\sqrt{r}}{2}\right\rfloor\\
    &= n - 2f(n,1,0,1) + 4f(n,1,0,2)
    \end{aligned}
    $$
    
    where the function $f$ has the form
    
    $$
    f(a,b,c,n) = \sum_{i=1}^n\left\lfloor\dfrac{a\sqrt{r}+b}{c}i\right\rfloor.
    $$
    
    Unlike the algorithm in the main text, here the slope is no longer rational. Let the slope be
    
    $$
    k = \dfrac{a\sqrt{r}+b}{c}.
    $$
    
    Likewise, discuss two cases. If $k\ge 1$, then
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=1}^n \lfloor ki\rfloor = \sum_{i=1}^n \lfloor(k-\lfloor k\rfloor)i\rfloor + \lfloor k\rfloor \sum_{i=1}^ni\\
    &= \lfloor k\rfloor\dfrac{n(n+1)}{2} + f(a,b-c\lfloor k\rfloor,c,n).
    \end{aligned}
    $$
    
    The problem is transformed into the case where the slope is less than one. If $k<1$, then let $m=\lfloor nk\rfloor$; we have
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=1}^n \lfloor ki\rfloor = \sum_{i=1}^n\sum_{j=1}^m[j\le\lfloor ki\rfloor]\\
    &= \sum_{j=1}^m\sum_{i=1}^n[i>\lfloor k^{-1}j\rfloor] = nm - \sum_{j=1}^m\sum_{i=1}^n[i\le\lfloor k^{-1}j\rfloor].
    \end{aligned}
    $$
    
    In the derivation here, the condition for exchanging $i$ and $j$ is simpler than the case in the main text, because the line $y=kx$ has no lattice point other than the origin. The key is to write the exchanged sum in the form $f(a,b,c,n)$, which amounts to requiring $a',b',c'$ to satisfy
    
    $$
    k^{-1} = \dfrac{a'\sqrt{r}+b'}{c'}.
    $$
    
    This is not difficult; we only need to rationalize the denominator to obtain
    
    $$
    k^{-1} = \dfrac{c}{a\sqrt{r}+b} = \dfrac{ca\sqrt{r}-cb}{a^2r-b^2}.
    $$
    
    Therefore, we have
    
    $$
    a'=ca,~b'=-cb,~c'=a^2r-b^2.
    $$
    
    This shows
    
    $$
    f(a,b,c,n) = nm - f(ca,-cb,a^2r-b^2,m).
    $$
    
    To avoid integer overflow, we need to divide $a,b,c$ by their greatest common divisor each time. Because this computation process is entirely consistent with the process of computing the continued fraction of $k$, according to [continued fraction theory](./continued-fraction.md#quadratic-irrationals), as long as we ensure $\gcd(a,b,c)=1$, they must remain within the integer range during the computation. In addition, although $(a,b,c,n)$ will not overflow, under this problem's data range, $f(a,b,c,n)$ may exceed the range of a $64$-bit integer; natural overflow is fine and no extra handling is needed, and the final result must be in $[-n,n]$.
    
    Although the slope will not become zero, the complexity of the algorithm is still $O(\log n)$, which is easy to see from the earlier argument about the algorithm's complexity.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-2.cpp"
    ```

???+ example "[Fraction](https://www.luogu.com.cn/problem/P5179)"
    Given positive integers $a,b,c,d$, find, among all reduced fractions $p/q$ satisfying $a/b<p/q<c/d$, the one whose $(q,p)$ is lexicographically smallest.

??? note "Solution"
    This problem is also a classic application of the [Stern–Brocot tree](./stern-brocot.md); the related solution can be found [here](./continued-fraction.md#the-tree-of-continued-fractions). Because it depends only on the recursive structure of fractions, it can likewise be solved using a Euclidean-like method, so it can also be regarded as an application of the Euclidean-like algorithm.
    
    If there is at least one natural number between $a/b$ and $c/d$ (excluding the endpoints), we can directly take $(q,p)=(1,\lfloor a/b\rfloor+1)$. Otherwise, we must have
    
    $$
    \left\lfloor\dfrac{a}{b}\right\rfloor \le \dfrac{a}{b} <\dfrac{p}{q} <\dfrac{c}{d}\le\left\lfloor\dfrac{a}{b}\right\rfloor+1.
    $$
    
    From this inequality, we can see that the integer part of $p/q$ can be determined to be $\lfloor a/b\rfloor$; directly eliminate this integer part, and then take the reciprocal of the whole to determine its fractional part. This is exactly the [basic method](./continued-fraction.md#finding-the-continued-fraction-representation) of determining the continued fraction of $p/q$. If the final answer is $p/q$, then the time complexity of the algorithm is $O(\log\min\{p,q\})$.
    
    Here, there is a detail question, namely whether the lexicographically smallest fraction obtained after taking the reciprocal is the lexicographically smallest fraction before taking the reciprocal. In other words, among the fractions $p/q$ satisfying $a/b<p/q<c/d$, is the one with the smallest lexicographic order $(q,p)$ also the one with the smallest lexicographic order $(p,q)$. Suppose not; let $p/q$ be the one with the smallest lexicographic order $(q,p)$, but $r/s\neq p/q$ be the one with the smallest lexicographic order $(r,s)$. This must have $r<p$ and $q<s$. But this shows
    
    $$
    \dfrac{a}{b} < \dfrac{r}{s} < \dfrac{r}{q} < \dfrac{p}{q} < \dfrac{c}{d}.
    $$
    
    Therefore, $r/q$ is strictly smaller than the current solution under any lexicographic order. This contradicts the assumed condition. Therefore, the above algorithm is correct.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-3.cpp"
    ```

## Universal Euclidean algorithm

The derivation of the Euclidean-like algorithm discussed in the previous section is usually rather cumbersome, and the sums it can solve are mainly those that can be transformed into (weighted) lattice-point counting problems below a line. This section discusses a more general method, which further abstracts the above process and can therefore solve more problems. For this reason, this method is also called the universal Euclidean algorithm. It likewise uses the recursive structure of fractions to solve problems, but the idea of reducing problems is slightly different from that of the Euclidean-like algorithm.

Consider again the most classic summation problem:

$$
f(a,b,c,n)=\sum_{i=1}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,
$$

where $a,b,c,n$ are all positive integers.

### Problem transformation

Let the line segment with parameters $(a,b,c,n)$ be

$$
y = \frac{ax+b}{c},~0< x\le n.
$$

For this line segment, one can define a string $S$ composed of $U$ and $R$ as follows, also called an **operation sequence**:

-   The string is composed of exactly $n$ $R$'s and $m=\lfloor(an+b)/c\rfloor$ $U$'s;
-   The number of $U$'s before the $i$-th $R$ is exactly equal to $\lfloor(ai+b)/c\rfloor$, where $i=1,\cdots,n$.

From a geometric intuition, this roughly corresponds to starting from the origin, writing an $R$ each time we cross a vertical grid line to the right, and writing a $U$ each time we cross a horizontal grid line upward. As shown in the figure below:

![](./images/euclidean-universal.svg)

Of course, such a definition also needs to consider a series of special cases:

-   When passing through a lattice point (i.e. crossing upward and rightward simultaneously), we need to write $U$ first and then $R$;
-   At the beginning of the string, in addition to the number of upward grid-line crossings in the interval $(0,1]$, we also need to additionally supplement $\lfloor b/c\rfloor$ $U$'s;
-   At the end of the string, there cannot be extra $U$'s.

If there is anything unclear in the description of the geometric intuition, one can refer to the definition of the algebraic method above to aid understanding. The description of the geometric intuition helps to understand the algorithm process below.

The basic idea of the universal Euclidean algorithm is to regard both $U$ and $R$ in the operation sequence as elements within some [monoid](../algebra/basic.md#groups), regard the entire operation sequence as a product of elements within the monoid, and the final answer to the problem is related to this product.

For example, in this problem, we can define the state vector $v = (1,y,\sum y)$, representing the current state after undergoing several upward and rightward grid-line crossings starting from the origin. Here, the first component is a constant, the second component is the vertical coordinate $y$, and the third component is the sum we require. At the start, we have $v=(1,0,0)$. Each time we cross a grid line upward, the vertical coordinate increments by one, which is equivalent to right-multiplying the state vector by the matrix

$$
U = \begin{pmatrix}1 & 1 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}.
$$

Each time we cross a grid line to the right, the sum accumulates one vertical coordinate, which is equivalent to right-multiplying the state vector by the matrix

$$
R = \begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 0 & 1\end{pmatrix}.
$$

Therefore, the final state is the product $(1,0,0)S$, where $S$ is understood as the product of the above matrices. The desired answer is the third component of the final state.

Besides defining the elements of the monoid as matrices, we can also define them as the contribution of a segment of the operation sequence to the final result, and then define the product of operations as the merging of the contributions of two segments of operation sequences.

In this problem, we can define the contribution of each segment of the operation sequence as $(x,y,\sum y)$. To explain these notations rigorously, we can regard all these components as functions of the operation sequence, that is, for an operation sequence $S$, its contribution can be written as $(x(S),y(S),(\sum y)(S))$. Here, $x(S)$ and $y(S)$ correspond respectively to the number of $R$'s and $U$'s in the operation sequence $S$, that is, the number of rightward and upward grid-line crossings of the line segment. For the summation symbol in the last term, in general, we have the following definition: for a function $f(S)$ on the operation sequence, we can define $(\sum f)(S)$, or denoted $\sum_S f$, as the following expression:

$$
\sum_S f := \sum\{f(S_{[1,r]}):S_r=R\}.
$$

Here, $S_r$ is the $r$-th character in $S$, and $S_{[1,r]}$ is the prefix composed of the first $r$ characters in $S$. That is to say, this summation symbol can be regarded as summation over all prefixes of the operation sequence $S$ that end in $R$. For example, we have

$$
\sum_S 1 = x,~ \sum_S x = \dfrac{1}{2}x(x+1).
$$

For another example, $\sum y$ is the accumulation, in the operation sequence, of the number of previous upward grid-line crossings each time we cross a grid line to the right. For the entire operation sequence, the values of $y$ at all prefixes ending in $R$ are exactly all the values of $\lfloor(ai+b)/c\rfloor$ at $i=1,\cdots,n$. Therefore, the $\sum y$ computed for the entire operation sequence is exactly the quantity required in this problem.

At the start, we have $U=(0,1,0)$, $R=(1,0,0)$. Furthermore, we can define the product of two elements $(x_1,y_1,s_1)$ and $(x_2,y_2,s_2)$ as

$$
(x_1,y_1,s_1)\cdot (x_2,y_2,s_2) = (x_1+x_2,y_1+y_2,s_1+s_2+x_2y_1).
$$

Here, the result of merging the contribution in the last term can be obtained through the following computation:

$$
\sum_{S_1+S_2}y = \sum_{S_1}y + \sum_{S_2}(y+y_1) = \sum_{S_1}y + \sum_{S_2}y + y_1\sum_{S_2}1 = s_1+s_2+x_2y_1.
$$

It is easy to verify that this multiplication operation satisfies associativity and its identity element is $(0,0,0)$, so these elements form a monoid under this multiplication operation. The desired answer is the third component of the product.

Both of these methods can obtain the correct result. However, because the matrix operation retains more redundant information, its constant factor is large, so the second method is more practical when handling actual problems.

### Algorithm process

Unlike the overall reduction of the Euclidean-like algorithm, the universal Euclidean algorithm's method of reducing the problem is to merge these operations in batches. Denote the product of operations corresponding to the string as

$$
F(a,b,c,n,U,R).
$$

The specific reduction process is as follows:

-   When $b\ge c$, the beginning of the operation sequence has $\lfloor b/c\rfloor$ $U$'s; directly compute their product and remove these $U$'s from the operation sequence. At this point, the number of $U$'s before the $i$-th $R$ equals

    $$
    \left\lfloor\dfrac{ai+b}{c}\right\rfloor - \left\lfloor\dfrac{b}{c}\right\rfloor = \left\lfloor\dfrac{ai+(b\bmod c)}{c}\right\rfloor.
    $$

    Therefore, this is equivalent to changing the line segment parameters from $(a,b,c,n)$ to $(a,b\bmod c,c,n)$. So, for this case, we have

    $$
    F(a,b,c,n,U,R) = U^{\lfloor b/c\rfloor}F(a,b\bmod c,c,n,U,R).
    $$

-   When $a\ge c$, each $R$ in the operation sequence has at least $\lfloor a/c\rfloor$ $U$'s before it, which can be merged onto the $R$. That is, we can replace $R$ with $U^{\lfloor a/c\rfloor}R$. In the merged string, the number of $U$'s before the $i$-th $R$ equals

    $$
    \left\lfloor\dfrac{ai+b}{c}\right\rfloor - \left\lfloor\dfrac{a}{c}\right\rfloor i = \left\lfloor\dfrac{(a\bmod c)i+b}{c}\right\rfloor.
    $$

    Therefore, this is equivalent to changing the line segment parameters from $(a,b,c,n)$ to $(a\bmod c,b,c,n)$. So, for this case, we have

    $$
    F(a,b,c,n,U,R) = F(a\bmod c,b,c,n,U,U^{\lfloor a/c\rfloor}R).
    $$

-   For the remaining case, we need to flip the horizontal and vertical coordinates, which is basically swapping $U$ and $R$, except that the parameters of the flipped line segment need to be computed carefully. Combining with the definition of the operation sequence, we need to determine the coefficients $(a',b',c',n')$ such that in the pre-transformation operation sequence, the number of $R$'s before the $j$-th $U$ is exactly $\lfloor(a'j+b')/c'\rfloor$ and there are $n'$ $U$'s in total. By definition,

    $$
    n'=\left\lfloor\dfrac{an+b}{c}\right\rfloor = m,
    $$

    and the number of $R$'s before the $j$-th $U$ equals the largest $i$ such that

    $$
    \begin{aligned}
    \left\lfloor\dfrac{ai+b}{c}\right\rfloor < j 
    &\iff \dfrac{ai+b}{c} < j \iff i < \dfrac{cj-b}{a} \\
    &\iff i < \left\lceil\dfrac{cj-b}{a}\right\rceil = \left\lfloor\dfrac{cj-b - 1}{a}\right\rfloor + 1.
    \end{aligned}
    $$

    Therefore, $i = \lfloor(cj-b-1)/a\rfloor$. This derivation process is similar to the derivation of the Euclidean-like algorithm above, likewise using the properties of the floor and ceiling functions.

    There are two details to handle:

    -   The intercept term $-(b+1)/a$ is negative. Note that if we translate the line segment one unit to the left, we can make the intercept term non-negative again, because always $(c-b-1)/a\ge 0$. Therefore, we can extract the first segment $R^{\lfloor(c-b-1)/a\rfloor}U$ before swapping, and only swap the $U$'s and $R$'s in the remaining operation sequence;
    -   After swapping $U$ and $R$, there are extra $U$'s at the end. Therefore, before swapping $U$ and $R$, we need to first extract the last segment of $R$'s, and only swap the $U$'s and $R$'s in the remaining operation sequence. The number of $R$'s in this segment is $n-\lfloor(cm-b-1)/a\rfloor$.

    After removing several characters at the head and tail, the number of $R$'s before the $j$-th $U$ becomes:

    $$
    \left\lfloor\dfrac{c(j+1)-b-1}{a}\right\rfloor - \left\lfloor\dfrac{c-b-1}{a}\right\rfloor = \left\lfloor\dfrac{cj+(c-b-1)\bmod a}{a}\right\rfloor.
    $$

    Recall that the number of $U$'s in the pre-swap sequence is $m = \lfloor(an+b)/c\rfloor$. And the above operation of translating one unit to the left requires guaranteeing that there is at least one $U$ before swapping, that is, $m>0$. Using this condition, we can divide into two cases:

    -   For the case $m>0$, after handling the above two points, the operation sequence after swapping $U$ and $R$ is exactly the valid sequence corresponding to the line segment with parameters $(c,(c-b-1)\bmod a,a,m-1)$. So, we have

        $$
        F(a,b,c,n,U,R) = R^{\lfloor(c-b-1)/a\rfloor}UF(c,(c-b-1)\bmod a,a,m-1,R,U)R^{n-\lfloor(cm-b-1)/a\rfloor}.
        $$

    -   In particular, for the case $m=0$, the pre-swap operation sequence contains only $n$ $R$'s, no swap is needed, and we can directly return:

        $$
        F(a,b,c,n,U,R) = R^n.
        $$

        Unlike the Euclidean-like algorithm, this special case of the universal Euclidean algorithm needs to be handled separately, otherwise it cannot be computed correctly due to involving negative powers.

Using these discussions, we can solve the problem recursively.

Suppose the time complexity of a single multiplication of elements within the monoid is $O(1)$. Then, if the power computations of these elements during the process all use [fast exponentiation](../binary-exponentiation.md), the final algorithm complexity is $O(\log\max\{a,c\}+\log(b/c))$[^complexity].

??? note "Explanation of the complexity"
    Compared with the (Euclidean-like) Euclidean algorithm, the universal Euclidean algorithm only has the additional step of computing fast exponentiation. The complexity of the rest of the computation process is similar to that of the Euclidean-like algorithm, which has already been shown to be $O(\log\min\{a,c,n\})$. Now, we need to compute the total complexity of these fast exponentiations.
    
    Except for the first round of iteration, we always have $b<c$, so each of these iterations involves three fast-exponentiation computations, and the total complexity is:
    
    $$
    O\left(\log\left\lfloor\dfrac{a}{c}\right\rfloor+\log\left\lfloor\dfrac{c-b_1-1}{a_1}\right\rfloor+\log\left(n-\left\lfloor\dfrac{cm-b_1-1}{a_1}\right\rfloor\right)\right),
    $$
    
    where $a_1=a\bmod c$, $b_1=b\bmod c$ and $m=\lfloor(a_1n+b_1)/c\rfloor$. The latter two terms have the following estimates respectively:
    
    $$
    \begin{aligned}
    \dfrac{c-b_1-1}{a_1} &\le \dfrac{c}{a_1},\\
    n-\left\lfloor\dfrac{cm-b_1-1}{a_1}\right\rfloor &\le n - \dfrac{cm-b_1-1}{a_1} + 1 \\
    &\le n - \dfrac{c((a_1n+b_1)/c-1)-b_1-1}{a_1} +1 \\
    &= \dfrac{c+1}{a_1}+1.
    \end{aligned}
    $$
    
    Therefore, the complexity of both of these terms is $O(\log(c/a_1))$.
    
    In each round of iteration, the parameters of the line segment change from $(a,\cdot,c,\cdot)$ to $(c,\cdot,a\bmod c,\cdot)$, and the total time complexity of this round is
    
    $$
    O\left(\log\dfrac{a}{c}+\log\dfrac{c}{a\bmod c}\right).
    $$
    
    For all recursion rounds, these terms telescope, so the final total complexity is $O(\log a+\log c)=O(\log\max\{a,c\})$.
    
    Finally, adding the complexity $O(\log(b/c))$ of the fast exponentiation $U^{\lfloor b/c\rfloor}$ in the first round of iteration, we obtain the total complexity of $O(\log\max\{a,c\}+\log(b/c))$.

The process of the universal Euclidean algorithm can be written as a unified template; when handling a specific problem, one only needs to change the implementation of the template type `T`.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-4.cpp:euclidean"
    ```

Using the universal Euclidean algorithm, the implementation of the template problem can be obtained as follows:

??? example "Template problem implementation ([Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear))"
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-4.cpp:full-text"
    ```

### Example problems

???+ example "[【模板】类欧几里得算法](https://www.luogu.com.cn/problem/P5170)"
    Multiple queries. Given positive integers $a,b,c,n$, find
    
    $$
    \begin{aligned}
    f(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    g(a,b,c,n) &= \sum_{i=0}^ni\left\lfloor \frac{ai+b}{c} \right\rfloor,\\
    h(a,b,c,n) &= \sum_{i=0}^n\left\lfloor \frac{ai+b}{c} \right\rfloor^2.
    \end{aligned}
    $$

??? note "Solution 2"
    To apply the template of the universal Euclidean algorithm, first extract the $i=0$ term and consider it separately. For the remaining part, it can be regarded as computing $\sum y,\sum xy,\sum y^2$ respectively for the line segment with parameters $(a,b,c,n)$. As stated in the main text, there are two ways to convert the operation sequence into monoid elements.
    
    **Matrix operation**: The state vector is defined as $(1,x,y,xy,y^2,\sum y,\sum xy,\sum y^2)$. The initial state is $(1,0,0,0,0,0,0,0)$, and the two operations are respectively
    
    $$
    U =
    \begin{pmatrix}
    1 & 0 & 1 & 0 & 1 & 0 & 0 & 0 \\
    0 & 1 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 & 2 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 
    \end{pmatrix},~
    R = 
    \begin{pmatrix}
    1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 1 & 0 & 1 & 1 & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 
    \end{pmatrix}.
    $$
    
    The final answer is the last three components of the vector obtained by right-multiplying the initial state by the product of these operation matrices.
    
    The constant factor of this approach is huge, and it cannot pass this problem; the details are given here only to aid understanding.
    
    **Contribution merging**: The contribution of a segment of operation sequence is defined as $(x,y,\sum y,\sum xy,\sum y^2)$. The two operations are respectively
    
    $$
    U = (0,1,0,0,0),~ R = (1,0,0,0,0).
    $$
    
    When merging contributions, we have
    
    $$
    \begin{aligned}
    \sum_{S_1+S_2} y 
    &= \sum_{S_1}y + \sum_{S_2}(y+y_1) = \sum_{S_1}y + \sum_{S_2}y + x_2y_1,\\
    \sum_{S_1+S_2} xy
    &= \sum_{S_1}xy + \sum_{S_2}(x+x_1)(y+y_1) \\
    &= \sum_{S_1}xy + \sum_{S_2}xy + x_1\sum_{S_2}y + y_1\sum_{S_2}x + x_1y_1\sum_{S_2}1\\
    &= \sum_{S_1}xy + \sum_{S_2}xy + x_1\sum_{S_2}y + \dfrac{1}{2}x_2(x_2+1)y_1 + x_1x_2y_1,\\
    \sum_{S_1+S_2}y^2
    &= \sum_{S_1}y^2 + \sum_{S_2}(y+y_1)^2 \\
    &= \sum_{S_1}y^2 + \sum_{S_2}y^2 + 2y_1\sum_{S_2}y + y_1^2\sum_{S_2}1  \\
    &= \sum_{S_1}y^2 + \sum_{S_2}y^2 + 2y_1\sum_{S_2}y + x_2y_1^2.
    \end{aligned}
    $$
    
    This shows that we should define the multiplication of operations as
    
    $$
    \begin{aligned}
    &(x_1,y_1,s_1,t_1,u_1)\cdot(x_2,y_2,s_2,t_2,u_2)\\
    &= (x_1+x_2,y_1+y_2,s_1+s_2+x_2y_1,\\
    &\qquad t_1+t_2+x_1s_2+(1/2)x_2(x_2+1)y_1+x_1x_2y_1,\\
    &\qquad u_1+u_2+2y_1s_2+x_2y_1^2).
    \end{aligned}
    $$
    
    Although direct verification is rather cumbersome, the contribution vector defined above does form a monoid under this multiplication, with identity element $(0,0,0,0,0)$.
    
    For the general case, we have
    
    $$
    \begin{aligned}
    \sum_{S_1+S_2}x^ry^s &= \sum_{S_1}x^ry^s + \sum_{S_2}(x+x_1)^r(y+y_1)^s \\
    &= \sum_{S_1}x^ry^s + \sum_{i=0}^r\sum_{j=0}^s\binom{r}{i}\binom{s}{j}x_1^{r-i}y_1^{s-j}\sum_{S_2}x^iy^j.
    \end{aligned}
    $$
    
    As long as we maintain all the contributions of lower powers, we can compute the sum for the general case.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-5.cpp"
    ```

???+ example "[\[清华集训 2014\] Sum](https://www.luogu.com.cn/problem/P5172)"
    Multiple queries. Given positive integers $n$ and $r$, find
    
    $$
    \sum_{d=1}^n(-1)^{\lfloor d\sqrt{r}\rfloor}.
    $$

??? note "Solution 2"
    First, handle the case where $r$ is a perfect square separately, which is entirely consistent with the above and is omitted. Here, we only consider the case where $r$ is not a perfect square.
    
    There are many ways to apply the universal Euclidean algorithm to this problem. For example, we can define a linear transformation for each operation:
    
    $$
    U(x) = -x,~ R(x) = x + 1.
    $$
    
    The multiplication of operations is defined as the composition of linear transformations. Then, the final answer is the value at $x=0$ of the function obtained by composing the transformations corresponding to the operation sequence.
    
    We can also define its contribution for each segment of operation sequence. The contribution can be defined as $((-1)^y,\sum(-1)^y)$. Then, the two operations are respectively taken as
    
    $$
    U = (0,-1),~ R = (1,1).
    $$
    
    The merging of contributions is defined as
    
    $$
    (u_1,v_1)\cdot(u_2,v_2) = (u_1u_2,v_1+u_1v_2).
    $$
    
    It is easy to verify that under this multiplication, all operations form a monoid, with identity element $(0,1)$. The final answer is the second component of the product of all elements.
    
    These two methods are consistent, because if we write the linear transformation as $f(x)=u+vx$, then the change of the coefficients corresponding to the composition of linear transformations is exactly the above multiplication of operations. That is to say, these two monoids are isomorphic.
    
    In this problem, the parameters of the line segment are $(k,n)$, where $k\in\mathbf R$ is the slope of the line. Let the product corresponding to the operation sequence be $F(k,n,U,R)$. Then, we have the following recursive algorithm:
    
    -   If $k\ge 1$, then each $R$ in the operation sequence has at least $\lfloor k\rfloor$ $U$'s before it, so we have
    
        $$
        F(k,n,U,R) = F(k-\lfloor k\rfloor,n,U,U^{\lfloor k\rfloor} R).
        $$
    -   If $k<1$, then swap the $U$'s and $R$'s in the operation sequence and discard the trailing $U$ (i.e. the pre-swap $R$), so we have
    
        $$
        F(k,n,U,R) = F(k^{-1},m,R,U)R^{n-\lfloor k^{-1}m\rfloor}.
        $$
    
    In the algorithm, the iteration process of $k$ is actually finding the continued fraction expansion of $\sqrt{r}$. To this end, we can apply the [PQa algorithm](./pell-equation.md#pqa-algorithm). The process of finding the continued fraction and the iteration process of the universal Euclidean algorithm can be carried out simultaneously.
    
    Consistent with the case of the Euclidean-like algorithm, the complexity of the algorithm is still $O(\log n)$.
    
    ```cpp
    --8<-- "docs/math/code/euclidean/euclidean-6.cpp"
    ```

## Exercises

Template problems:

-   [Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)
-   [Luogu P5170【模板】类欧几里得算法](https://www.luogu.com.cn/problem/P5170)
-   [Luogu P5171 Earthquake](https://www.luogu.com.cn/problem/P5171)
-   [Luogu P5172 \[清华集训 2014\] Sum](https://www.luogu.com.cn/problem/P5172)
-   [Luogu P4132 \[BJOI2012\] 算不出的等式](https://www.luogu.com.cn/problem/P4132)
-   [LOJ 138. 类欧几里得算法](https://loj.ac/p/138)
-   [LOJ 6440. 万能欧几里得](https://loj.ac/p/6440)
-   [Luogu P5179 Fraction](https://www.luogu.com.cn/problem/P5179)
-   [Codeforces 1182 F. Maximum Sine](https://codeforces.com/problemset/problem/1182/F)

Application problems:

-   [Luogu P4433 \[COCI 2009/2010 #1\] ALADIN](https://www.luogu.com.cn/problem/P4433)
-   [AtCoder Beginner Contest 372 G - Ax + By < C](https://atcoder.jp/contests/abc372/tasks/abc372_g)
-   [AtCoder Beginner Contest 313 G - Redistribution of Piles](https://atcoder.jp/contests/abc313/tasks/abc313_g)
-   [AtCoder Beginner Contest 283 Ex - Popcount Sum](https://atcoder.jp/contests/abc283/tasks/abc283_h)
-   [Codeforces 1098 E. Fedya the Potter](https://codeforces.com/problemset/problem/1098/E)
-   [Codeforces 868 G. El Toll Caves](https://codeforces.com/problemset/problem/868/G)

## References and notes

[^complexity]: In the problems usually considered, $b$ is of the same order as $a$, and the term $O(\log(b/c))$ can be ignored. Moreover, if before calling the universal Euclidean algorithm we first perform a round of Euclidean-like algorithm's modulus to eliminate the influence of $b$, the fast-exponentiation complexity of this term can be avoided. This is actually because in usual problems, the initial form of $U$ is relatively special, and its powers have a simpler form that does not need to be computed via fast exponentiation. For example, in the example of the main text, the result of $U^{\lfloor b/a\rfloor}$ is exactly replacing the off-diagonal $1$ in $U$ with $\lfloor b/a\rfloor$, without needing fast exponentiation.
