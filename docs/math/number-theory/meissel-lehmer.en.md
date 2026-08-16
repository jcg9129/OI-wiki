author: Peanut-Tang, Early0v0, Vxlimo, GHLinZhengyu, 1196131597

The "Meissel–Lehmer algorithm" is an algorithm that can find the number of primes within $1\sim n$ in sublinear time complexity.

## Notation

$\left[x\right]$ denotes the result of taking the floor of $x$.  
$p_k$ denotes the $k$-th prime, $p_1=2$.  
$\pi\left(x\right)$ denotes the number of primes in the range $1\sim x$.  
$\mu\left(x\right)$ denotes the Möbius function.  
For a set $S$, $\# S$ denotes the size of the set $S$.  
$\delta\left(x\right)$ denotes the smallest prime factor of $x$.  
$P^+\left(x\right)$ denotes the largest prime factor of $x$.

## Computing π(x) with the Meissel–Lehmer algorithm

Define $\phi\left(x,a\right)$ as the number of positive integers less than $x$ all of whose prime factors are greater than $p_a$, i.e.:

$$
\phi\left(x,a\right)=\#\big\{n\le x\mid n\bmod p=0 \implies p>p_a\big\}\tag{1}
$$

Then define $P_k\left(x,a\right)$ as the number of positive integers less than $x$ that have exactly $k$ prime factors with multiplicity and all of whose prime factors are greater than $p_a$, i.e.:

$$
P_k\left(x,a\right)=\#\big\{n\le x\mid n=q_1q_2\cdots q_k \implies \forall i,q_i>p_a\big\}\tag{2}
$$

In particular, we define $P_0\left(x,a\right)=1$, so that:

$$
\phi\left(x,a\right)=P_0\left(x,a\right)+P_1\left(x,a\right)+\cdots+P_k\left(x,a\right)+\cdots
$$

This infinite sum can in fact be represented as a finite sum, because when $p_a^k>x$, we have $P_k\left(x,a\right)=0$.

Let $y$ be an integer satisfying $x^{1/3}\le y\le x^{1/2}$, and denote $a=\pi\left(y\right)$.

When $k\ge 3$, we have $P_1\left(x,a\right)=\pi\left(x\right)-a$ and $P_k\left(x,a\right)=0$, from which we can deduce:

$$
\pi\left(x\right)=\phi\left(x,a\right)+a-1-P_2\left(x,a\right)\tag{3}
$$

In this way, computing $\pi\left(x\right)$ can be transformed into computing $\phi\left(x,a\right)$ and $P_2\left(x,a\right)$.

## Computing P₂(x,a)

From equation $\left(2\right)$ we can deduce that $P_2\left(x,a\right)$ equals the number of prime pairs $\left(p,q\right)$ satisfying $y<p\le q$ and $pq\le x$.

First we note that $p\in \left[y+1,\sqrt{x}\right]$. In addition, for each $p$, we have $q\in\left[p,x/p\right]$. Therefore:

$$
P_2\left(x,a\right)=\sum_{y<p\le \sqrt{x}}{\left(\pi\left(\dfrac{x}{p}\right)-\pi\left(p\right)+1\right)}\tag{4}
$$

When $p\in \left[y+1,\sqrt{x}\right]$, we have $\dfrac{x}{p}\in \left[1,\dfrac{x}{y}\right]$. Therefore, we can sieve the interval $\left[1,\dfrac{x}{y}\right]$, and then for all primes $p\in \left[y+1,\sqrt{x}\right]$ compute $\pi\left(\dfrac{x}{p}\right)-\pi\left(p\right)+1$. To reduce the space complexity of the above algorithm, we can consider blocking, with block length $L$. If the block length $L=y$, then we can compute $P_2\left(x,a\right)$ in $O\left(\dfrac{x}{y}\log{\log{x}}\right)$ time complexity and $O\left(y\right)$ space complexity.

## Computing ϕ(x,a)

For $b\le a$, consider all positive integers not exceeding $x$ all of whose prime factors are greater than $p_{b-1}$. These numbers can be divided into two classes:

1.  those divisible by $p_b$;
2.  those not divisible by $p_b$.

There are $\phi\left(\dfrac{x}{p_b},b-1\right)$ numbers belonging to class $1$, and $\phi\left(x,b\right)$ numbers belonging to the second class.

Therefore we reach the conclusion:

> **Theorem $5.1$:** The function $\phi$ satisfies the following properties
>
> $$
> \phi\left(u,0\right)=\left[u\right]\tag{5}
> $$
>
> $$
> \phi\left(x,b\right)=\phi\left(x,b-1\right)-\phi\left(\dfrac{x}{p_b},b-1\right)\tag{6}
> $$

A simple method for computing $\phi\left(x,a\right)$ can be derived from this theorem: we repeatedly use equation $\left(7\right)$, until we finally obtain $\phi\left(u,0\right)$. This process can be viewed as creating a rooted binary tree starting from the root node $\phi\left(x,a\right)$; figure $1$ depicts this process. Through this method, we obtain the following formula:

$$
\phi\left(x,a\right)=\sum_{\substack{1\le n\le x\\ P^+\left(n\right)\le y}}{\mu\left(n\right)\left[x/n\right]}
$$

$$
\begin{gathered}
\begin{matrix}&&\phi\left(x,a\right)&&\\
&\swarrow&&\searrow&\\
&\phi\left(x,a-1\right)&&-\phi\left(\frac{x}{p_a},a-1\right)&\\
\swarrow&\downarrow&&\downarrow&\searrow\\
\phi\left(x,a-2\right)&\phi\left(\frac{x}{p_{a-1}},a-2\right)&&-\phi\left(\frac{x}{p_a},a-2\right)&\phi\left(\frac{x}{p_ap_{a-1}},a-2\right)\end{matrix}\\
\vdots\\
\end{gathered}
$$

The above figure shows the binary tree of the process of computing $\phi\left(x,a\right)$: the sum of the leaf node weights is exactly $\phi\left(x,a\right)$.

However, this requires computing too many things. Because $y\geq x^{1/3}$, just computing the numbers that are products of $3$ primes not exceeding $y$, if computed according to this method, will have at least $\dfrac{x}{\log^3 x}$ terms, which cannot meet our requirement on the complexity.

To limit the "growth" of this binary tree, we need to change the original termination condition. This is the original termination condition.

> **Termination condition $1$:** If $b=0$, do not call equation $\left(6\right)$ on the node $\mu\left(n\right)\phi\left(\dfrac xn,b\right)$ anymore.

We change it to a stronger termination condition:

> **Termination condition $2$:** If one of the following $2$ conditions is satisfied, do not call equation $\left(6\right)$ on the node $\mu\left(n\right)\phi\left(\dfrac xn,b\right)$ anymore:
>
> 1.  $b=0$ and $n\le y$;
> 2.  $n>y$.

Based on **termination condition $2$**, we divide the leaves on the original binary tree into two kinds:

1.  If a leaf node $\mu\left(n\right)\phi\left(\dfrac xn,b\right)$ satisfies $n\le y$, we call this kind of leaf node an **ordinary leaf**;
2.  If a leaf node $\mu\left(n\right)\phi\left(\dfrac xn,b\right)$ satisfies $n>y$ and $n=mp_b\left(m\le y\right)$, we call this kind of node a **special leaf**.

From this we obtain:

> **Theorem $5.2$:** We have:
>
> $$
> \phi\left(x,a\right)=S_0+S\tag{7}
> $$
>
> where $S_0$ denotes the contribution of the **ordinary leaves**:
>
> $$
> S_0=\sum_{n\le y}{\mu\left(n\right)\left[\dfrac xn\right]}\tag{8}
> $$
>
> $S$ denotes the contribution of the **special leaves**:
>
> $$
> S=\sum_{n/\delta\left(n\right)\le y\le n}{\mu\left(n\right)\phi\left(\dfrac{x}{n},\pi\left(\delta\left(n\right)\right)-1 \right)}\tag{9}
> $$

Computing $S_0$ can obviously be solved in $O\left(y\log{\log x}\right)$ time complexity; now we need to consider how to compute $S$.

## Computing S

We have:

$$
S=-\sum_{p\le y}{\ \sum_{\substack{\delta\left(m\right)>p\\ m\le y<mp}}{\mu\left(m\right)\phi\left(\dfrac{x}{mp},\pi\left(p\right)-1\right)}}\tag{10}
$$

We rewrite this equation as:

$$
S=S_1+S_2+S_3
$$

where:

$$
S_1=-\sum_{x^{1/3}<p\le y}{\ \sum_{\substack{\delta\left(m\right)>p\\ m\le y<mp}}{\mu\left(m\right)\phi\left(\dfrac{x}{mp},\pi\left(p\right)-1\right)}}
$$

$$
S_2=-\sum_{x^{1/4}<p\le x^{1/3}}{\ \sum_{\substack{\delta\left(m\right)>p\\ m\le y<mp}}{\mu\left(m\right)\phi\left(\dfrac{x}{mp},\pi\left(p\right)-1\right)}}
$$

$$
S_3=-\sum_{p\le x^{1/4}}{\ \sum_{\substack{\delta\left(m\right)>p\\ m\le y<mp}}{\mu\left(m\right)\phi\left(\dfrac{x}{mp},\pi\left(p\right)-1\right)}}
$$

Note that the $m$ involved in the sums for computing $S_1,S_2$ are all primes; the proof is as follows:

> If this were not the case, because $\delta\left(m\right)>p>x^{1/4}$, we would have $m>p^2>\sqrt{x}$, which contradicts $m\le y$, so the original proposition holds.

Furthermore, when $mp>x^{1/2}\ge y$, we have $y\le mp$. Therefore we have:

$$
S_1=\sum_{x^{1/3}<p\le y}{\ \sum_{p<q\le y}{\phi\left(\dfrac{x}{pq},\pi\left(p\right)-1\right)}}
$$

$$
S_2=\sum_{x^{1/4}<p\le x^{1/3}}{\ \sum_{p<q\le y}{\phi\left(\dfrac{x}{pq},\pi\left(p\right)-1\right)}}
$$

### Computing S₁

Because:

$$
\dfrac{x}{pq}<x^{1/3}<p
$$

we have:

$$
\phi\left(\dfrac{x}{pq},\pi\left(p\right)-1\right)=1
$$

So the terms in the sum for computing $S_1$ are all $1$. So we actually need to compute the number of prime pairs $\left(p,q\right)$ satisfying $x^{1/3}<p<q\le y$.

Therefore:

$$
S_1=\dfrac{\left(\pi\left(y\right)-\pi\left(x^{1/3}\right)\right)\left(\pi\left(y\right)-\pi\left(x^{1/3}\right)-1\right)}{2}
$$

With this equation we can compute $S_1$ in $O\left(1\right)$ time.

### Computing S₂

We have:

$$
S_2=\sum_{x^{1/4}<p\le x^{1/3}}{\ \sum_{p<q\le y}{\phi\left(\dfrac{x}{pq},\pi\left(p\right)-1\right)}}
$$

We divide $S_2$ into two parts, $q>\dfrac x{p^2}$ and $q\le \dfrac x{p^2}$:

$$
S_2=U+V
$$

where:

$$
U=\sum_{x^{1/4}<p\le x^{1/3}}{\ \sum_{\substack{p<q<y\\q>x/p^2}}{\phi\left(\dfrac{x}{pq},\pi\left(p\right)-1 \right)}}
$$

$$
V=\sum_{x^{1/4}<p\le x^{1/3}}{\ \sum_{\substack{p<q<y\\q\le x/p^2}}{\phi\left(\dfrac{x}{pq},\pi\left(p\right)-1 \right)}}
$$

### Computing U

From $q>\dfrac x{p^2}$ we can obtain $p^2>\dfrac xq\le \dfrac xy,p>\sqrt{\dfrac xy}$, therefore:

$$
U=\sum_{\sqrt{x/y}<p\le x^{1/3}}{\ \sum_{\substack{p<q\le y\\q>x/p^2}}{\phi\left(\dfrac{x}{pq},\pi\left(p\right)-1 \right)}}
$$

Therefore:

$$
U=\sum_{\sqrt{x/y}<p\le x^{1/3}}{\#\left\{q\mid \dfrac x{p^2}<q\le y \right\}}
$$

Therefore:

$$
U=\sum_{\sqrt{x/y}<p\le x^{1/3}}{\left(\pi\left(y\right)-\pi\left(\dfrac{x}{p^2} \right) \right)}
$$

Because $\dfrac x{p^2}<y$, we can preprocess all $\pi\left(t\right)\left(t\le y\right)$, so that we can compute $U$ in $O\left(y\right)$ time complexity.

### Computing V

For each term in the sum for computing $V$, we have $p\le \dfrac{x}{pq}<x^{1/2}<p^2$. Therefore:

$$
\phi\left(\dfrac{x}{pq},\pi\left(p\right)-1 \right)=1+\pi\left(\dfrac{x}{pq} \right)-\left(\pi\left(p\right)-1\right)=2-\pi\left(p\right)+\pi\left(\dfrac{x}{pq} \right)
$$

So $V$ can be represented as:

$$
V=V_1+V_2
$$

where:

$$
V_1=\sum_{x^{1/4}<p\le x^{1/3}}{\ \sum_{p<q\le \min\left(x/p^2,y\right)}{\left(2-\pi\left(p\right)\right)}}
$$

$$
V_2=\sum_{x^{1/4}<p\le x^{1/3}}{\ \sum_{p<q\le \min\left(x/p^2,y\right)}{\pi\left(\dfrac{x}{pq} \right)}}
$$

After preprocessing $\pi\left(t\right)\left(t\le y\right)$ we can compute $V_1$ in $O\left(x^{1/3}\right)$ time complexity.

Consider how we speed up the process of computing $V_2$. We can split the contribution of $q$ into several intervals on which $\pi\left(\dfrac{x}{pq} \right)$ is a fixed value, so that we only need to compute the length of each interval and the change in $\pi\left(\dfrac{x}{pq} \right)$ from one interval to the next.

More precisely, we first divide $V_2$ into two parts, simplifying the complex condition $q\le \min\left(\dfrac x{p^2},y\right)$:

$$
V_2=\sum_{x^{1/4}<p\le \sqrt{x/y}}{\ \sum_{p<q\le y}{\pi\left(\dfrac{x}{pq} \right)}}+\sum_{\sqrt{x/y}<p\le x^{1/3}}{\ \sum_{p<q\le x/p^2}{\pi\left(\dfrac{x}{pq} \right)}}
$$

Then we rewrite this expression as:

$$
V_2=W_1+W_2+W_3+W_4+W_5
$$

where:

$$
W_1=\sum_{x^{1/4}<p\le x/y^2}{\ \sum_{p<q\le y}{\pi\left(\dfrac{x}{pq} \right)}}
$$

$$
W_2=\sum_{x/y^2<p\le \sqrt{x/y}}{\ \sum_{p<q\le \sqrt{x/p}}{\pi\left(\dfrac{x}{pq} \right)}}
$$

$$
W_3=\sum_{x/y^2<p\le \sqrt{x/y}}{\ \sum_{\sqrt{x/p}<q\le y}{\pi\left(\dfrac{x}{pq} \right)}}
$$

$$
W_4=\sum_{\sqrt{x/y}<p\le x^{1/3}}{\ \sum_{p<q\le \sqrt{x/p}}{\pi\left(\dfrac{x}{pq} \right)}}
$$

$$
W_5=\sum_{\sqrt{x/y}<p\le x^{1/3}}{\ \sum_{\sqrt{x/p}<q\le x/p^2}{\pi\left(\dfrac{x}{pq} \right)}}
$$

#### Computing W₁ and W₂

Computing these two values requires computing the value of $\pi\left(\dfrac{x}{pq} \right)$ satisfying $y<\dfrac{x}{pq}<x^{1/2}$. This can be sieved out in blocks over the interval $[1,\sqrt x]$. In each block we accumulate $\pi\left(\dfrac x{pq}\right)$ for all $(p,q)$ satisfying the condition.

#### Computing W₃

For each $p$, we divide $q$ into several intervals, each satisfying that their $\pi\left(\dfrac x{pq}\right)$ is a fixed value, and for each interval we can compute its contribution in $O(1)$. When we obtain a new $q$, we compute $\pi\left(\dfrac x{pq}\right)$ using the value table of $\pi(t)$ ($t\leq y$). The prime table within $y$ can give the $t$ such that $\pi(t)<\pi(t+1)=\pi\left(\dfrac x{pq}\right)$ holds. By analogy, we obtain the next value of $q$ that makes $\pi\left(\dfrac x{pq}\right)$ change.

#### Computing W₄

Compared with $W_3$, in $W_4$ the $q$ is smaller, so $\pi\left(\dfrac x{pq}\right)$ changes faster. In this case computing $W_4$ using the method for computing $W_3$ has no advantage. So we directly brute-force enumerate the pairs $(p,q)$ to compute $W_4$.

#### Computing W₅

We compute $W_5$ in the same way as computing $W_3$.

## Computing S₃

We use all primes less than $x^{1/4}$ to sieve out the interval $\left[1,\dfrac xy\right]$ once. When our sieve reaches $p_k$, we compute the value of $-\mu(m)\phi\left(\dfrac{x}{mp_k},k-1 \right)$ for all $m$ that are squarefree and satisfy $\delta(m)>p_k$. This sieve is performed in blocks; we maintain a binary tree during the sieve interval to maintain in real time the intermediate results after all primes have been sieved up to a given prime. In this way we can find, in only $O(\log x)$ time complexity, the number of numbers that have not been sieved when the sieve reaches a certain value.

## Time and space complexity of the algorithm

The time and space complexity is affected by the following $3$ processes:

1.  Computing $P_2\left(x,a\right)$;
2.  Computing $W_1,W_2,W_3,W_4,W_5$;
3.  Computing $S_3$.

### Complexity of computing P₂(x,y)

We already know that the time complexity of this process is $O\left(\dfrac{x}{y}\log{\log x}\right)$ and the space complexity is $O\left(y\right)$.

### Complexity of computing W₁,W₂,W₃,W₄,W₅

The time complexity of the block-length-$y$ sieve performed to compute $W_1,W_2$ is $O\left(\sqrt{x}\log{\log x}\right)$, and the space complexity is $O\left(y\right)$.

The time complexity needed to compute $W_1$ is:

$$
\pi\left(\dfrac{x}{y^2} \right)\pi\left(y\right)=O\left(\dfrac{x}{y\log^2 x} \right)
$$

The time complexity of computing $W_2$ is:

$$
O\left(\sum_{x/y^2<p\le \sqrt{x/y}}{\pi\left(\sqrt{\dfrac xp}\right)} \right)=O\left(\dfrac{x^{3/4}}{y^{1/4}\log^2 x} \right)
$$

Therefore, the time complexity of computing $W_3$ is:

$$
O\left(\sum_{x/y^2<p\le \sqrt{x/y}}{\pi\left(\sqrt{\dfrac xp}\right)} \right)=O\left(\dfrac{x^{3/4}}{y^{1/4}\log^2 x} \right)
$$

The time complexity of computing $W_4$ is:

$$
O\left(\sum_{\sqrt{x/y}<p\le x^{1/3}}{\pi\left(\sqrt{\dfrac xp}\right)} \right)=O\left(\dfrac{x^{2/3}}{\log^2 x} \right)
$$

The time complexity of computing $W_5$ is:

$$
O\left(\sum_{\sqrt{x/y}<p\le x^{1/3}}{\pi\left(\sqrt{\dfrac xp}\right)} \right)=O\left(\dfrac{x^{2/3}}{\log^2 x} \right)
$$

### Complexity of computing S₃

For preprocessing: since we need to quickly query the value of $\phi(u,b)$, we cannot use an ordinary sieve to find it in $O(1)$, but instead need to maintain a data structure so that the time complexity of each query is $O(\log x)$, so the time complexity is $O\left(\dfrac{x}{y}\log x\log\log x\right)$.

For summation: for each term in the sum for computing $S_3$, we query the above data structure, $O\left(\log x\right)$ queries in total. We also need to compute the number of terms in the sum, i.e. the number of leaves in the binary tree. All leaves have the form $\pm\phi\left(\dfrac{x}{mp_b},b-1\right)$, where $m\le y,b<\pi(x^{1/4})$. Therefore, the number of leaves is on the order of $O\left(y\pi\left(x^{1/4}\right)\right)$. So the total time complexity of computing $S_3$ is:

$$
O\left(\dfrac{x}{y}\log x\log\log x+yx^{1/4}\right)
$$

### Total complexity

The space complexity of this algorithm is $O\left(y\right)$, and the time complexity is:

$$
O\left(\dfrac{x}{y}\log{\log x}+\dfrac{x}{y}\log x\log{\log x}+x^{1/4}y+\dfrac{x^{2/3}}{\log^2{x}} \right)
$$

Taking $y=x^{1/3}\log^3{x}\log{\log x}$, we have the optimal time complexity $O\left(\dfrac{x^{2/3}}{\log^2 x}\right)$ and space complexity $O\left(x^{1/3}\log^3{x}\log{\log x}\right)$.

## Some improvements

Here we give improvement methods to reduce the constant factor of the algorithm and improve its practical efficiency.

-   In **termination condition $2$**, we can use a $z$ to replace $y$, where $z$ satisfies $z>y$. We can prove that this way the time complexity of computing $S_3$ can be optimized to:

    $$
    O\left(\dfrac{x}{z}\log x\log{\log x}+\dfrac{yx^{1/4}}{\log x}+z^{3/2} \right)
    $$

    This also provides a good method to check the computation by changing the value of $z$.

-   For clarity, when describing the algorithm we chose to split at $x^{1/4}$ to compute the sum $S$, but in fact we only need $p\le \dfrac{x}{pq}<p^2$ to compute it. We can use this point, and the asymptotic complexity remains unchanged.

-   Preprocessing with the first few primes $2,3,5$ can save even more time.

## References and further reading

This article is translated from: [Computing $\pi(x)$: the Meissel, Lehmer, Lagarias, Miller, Odlyzko method](https://dl.acm.org/doi/abs/10.1090/s0025-5718-96-00674-6)
