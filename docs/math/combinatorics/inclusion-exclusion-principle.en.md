## Introduction

???+ note "Introductory example"
    Suppose in a class $10$ students like math, $15$ students like Chinese, and $21$ students like programming; how many students in the class like at least one subject?

Is it $10+15+21=46$? No, because some students may like both math and Chinese, or Chinese and programming, or even all three.

For convenience of exposition, we denote the sets of students who like Chinese, math, and programming by $A,B,C$ respectively; then the total number of students equals $|A\cup B\cup C|$. As just explained, if we directly add the numbers of elements of these three sets $|A|,|B|,|C|$, some elements will be counted repeatedly, so we need to subtract $|A\cap B|,|B\cap C|,|C\cap A|$; but this way, a small part is over-subtracted and needs to be added back, i.e. $|A\cap B\cap C|$. That is

$$
|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|B\cap C|-|C\cap A|+|A\cap B\cap C|
$$

![inclusion-exclusion principle - Venn diagram example](./images/incexcp.png)

Generalizing the above problem to the general case gives the familiar inclusion-exclusion principle.

## Definition

Suppose the elements in $U$ have $n$ different properties, and the $i$-th property is called $P_i$; the elements having property $P_i$ form the set $S_i$. Then

$$
\begin{aligned}
\left|\bigcup_{i=1}^{n}S_i\right|=&\sum_{i}|S_i|-\sum_{i<j}|S_i\cap S_j|+\sum_{i<j<k}|S_i\cap S_j\cap S_k|-\cdots\\
&+(-1)^{m-1}\sum_{a_i<a_{i+1} }\left|\bigcap_{i=1}^{m}S_{a_i}\right|+\cdots+(-1)^{n-1}|S_1\cap\cdots\cap S_n|
\end{aligned}
$$

That is

$$
\left|\bigcup_{i=1}^{n}S_i\right|=\sum_{m=1}^n(-1)^{m-1}\sum_{a_i<a_{i+1} }\left|\bigcap_{i=1}^mS_{a_i}\right|
$$

### Proof

For each element, use the binomial theorem to compute the number of times it appears. For an element $x$, suppose it appears in the sets $T_1,T_2,\cdots,T_m$; then its number of appearances is

$$
\begin{aligned}
Cnt=&|\{T_i\}|-|\{T_i\cap T_j|i<j\}|+\cdots+(-1)^{k-1}\left|\left\{\bigcap_{i=1}^{k}T_{a_i}|a_i<a_{i+1}\right\}\right|\\
&+\cdots+(-1)^{m-1}|\{T_1\cap\cdots\cap T_m\}|\\
=&\dbinom{m}{1}-\dbinom{m}{2}+\cdots+(-1)^{m-1}\dbinom{m}{m}\\
=&\dbinom{m}{0}-\sum_{i=0}^m(-1)^i\dbinom{m}{i}\\
=&1-(1-1)^m=1
\end{aligned}
$$

So each element appears exactly once, and merging them gives the union. Q.E.D.

### Complement

For the **union of sets** under the universe $U$, the inclusion-exclusion principle can be used to compute it, while the intersection of sets is obtained by subtracting the **union of complements** from the universe:

$$
\left|\bigcap_{i=1}^{n}S_i\right|=|U|-\left|\bigcup_{i=1}^n\overline{S_i}\right|
$$

Just use inclusion-exclusion on the right side.

Readers who have encountered inclusion-exclusion probably all know the above content, and are more concerned with its applications.

So next we give 3 example problems at different levels to demonstrate the applications of the inclusion-exclusion principle.

## Counting non-negative-integer solutions of a Diophantine equation

???+ note "Counting non-negative-integer solutions of a Diophantine equation"
    Given the Diophantine equation $\sum_{i=1}^nx_i=m$ and $n$ constraints $x_i\leq b_i$, where $m,b_i \in \mathbb{N}$. Find the number of non-negative-integer solutions of the equation.

### Without constraints

If there is no $x_i\leq b_i$ constraint, then the number of non-negative-integer solutions of the Diophantine equation $\sum_{i=1}^nx_i=m$ is $\dbinom{m+n-1}{n-1}$.

Brief proof: stars and bars.

This is equivalent to having $m$ balls to distribute among $n$ boxes, allowing a box to be empty. This problem cannot be solved directly with a binomial coefficient.

So we add $n-1$ more balls; then the problem becomes selecting $n-1$ balls from a sequence of $m+n-1$ balls, and these $n-1$ balls partition the sequence into $n$ parts, which can be placed exactly one-to-one into the $n$ boxes. Then the number of ways to select $n-1$ balls from $m+n-1$ balls is $\dbinom{m+n-1}{n-1}$.

### Inclusion-exclusion model

Next we try to abstract the model of the inclusion-exclusion principle:

1.  Universe $U$: the non-negative-integer solutions of the Diophantine equation $\sum_{i=1}^nx_i=m$
2.  Element: variable $x_i$.
3.  Property: the property of $x_i$ is the condition $x_i$ satisfies, i.e. the condition $x_i\leq b_i$

Goal: the size of the set when all variables satisfy their corresponding property, i.e. $|\bigcap_{i=1}^nS_i|$.

This can be solved with $\left|\bigcap_{i=1}^{n}S_i\right|=|U|-\left|\bigcup_{i=1}^n\overline{S_i}\right|$. $|U|$ can be computed with a binomial coefficient, and the latter part is naturally expanded using the inclusion-exclusion principle.

Then the problem becomes finding the size of the intersection of some $\overline{S_{a_i}}$. Consider the meaning of $\overline{S_{a_i}}$: it represents the number of solutions with $x_{a_i}\geq b_{a_i}+1$. And the intersection represents satisfying these conditions simultaneously. Therefore, in the Diophantine equation corresponding to this intersection, some variables have a **lower-bound constraint**, while others have no constraint.

Can we eliminate these lower-bound constraints? Since we want non-negative-integer solutions, and the lower bounds of some variables are greater than $0$, we can directly **subtract this lower bound**, making the lower bounds of these variables become $0$, i.e. no lower bound. Therefore, for

$$
\left|\bigcap_{a_i<a_{i+1} }^{1\leq i\leq k}S_{a_i}\right|
$$

the Diophantine-equation form is

$$
\sum_{i=1}^nx_i=m-\sum_{i=1}^k(b_{a_i}+1)
$$

So this can also be computed with a binomial coefficient. This length-$k$ array $a$ amounts to enumerating subsets.

## HAOI2008 Coin Shopping

???+ note "HAOI2008 Coin Shopping"
    There are 4 denominations of coins, the denomination of the $i$-th being $C_i$. There are $n$ queries; each query gives the quantity $D_i$ of each kind of coin and a price $S$, and asks the number of ways to pay.
    
    $n\leq 10^3,S\leq 10^5$.

If done with a knapsack, the complexity is $O(4nS)$, which is unbearable. The most obvious feature of this problem is that there are only four kinds of coins. Abstracting the model, it actually asks us to find the number of non-negative-integer solutions of the equation $\sum_{i=1}^4C_ix_i=S,x_i\leq D_i$.

Using the same inclusion-exclusion approach, the property of $x_i$ is $x_i\leq D_i$. Applying the inclusion-exclusion formula, we finally need to solve

$$
\sum_{i=1}^4C_ix_i=S-\sum_{i=1}^kC_{a_i}(D_{a_i}+1)
$$

which is an unbounded knapsack problem. This problem can be preprocessed; counting the queries, the total complexity is $O(4S+2^4n)$.

??? note "Code implementation"
    ```cpp
    --8<-- "docs/math/code/inclusion-exclusion-principle/inclusion-exclusion-principle_1.cpp"
    ```

## Complete-graph subgraph coloring problem

The previous three problems are all forward applications of the inclusion-exclusion principle; this problem requires using the inclusion-exclusion principle for reverse analysis.

???+ note "Complete-graph subgraph coloring problem"
    A and B like to color graphs (not necessarily connected), and their rule is that adjacent nodes must be colored the same color. Today A and B play a game, for the $n$-order **complete graph** $G=(V,E)$. They define a valuation function $F(S)$, where $S$ is an edge set, $S\subseteq E$. The value of $F(S)$ is the total number of ways to color the graph $G'=(V,S)$ with $m$ colors. Their other rule is that if $|S|$ is odd, then A's score increases by $F(S)$, otherwise B's score increases by $F(S)$. Find the difference between A's and B's scores.

### Mathematical form

At first glance the algorithmic tendency of this problem is not obvious, so for tricky problems first abstract the mathematical form. The score difference is the parity symmetric difference, and we can use powers of -1 as coefficients. What we want is

$$
Ans=\sum_{S\subseteq E}(-1)^{|S|-1}F(S)
$$

### Inclusion-exclusion model

We treat "adjacent nodes colored the same color" as a property. Here we first do not obey the coloring rule, and assume we directly color the graph with $m$ colors. For the graph $G'=(V,S)$, we treat it as an **element**. The **property** $x_i=x_j$ means nodes $i,j$ are colored the same (note that this does not require an edge between $i,j$).

The **set** corresponding to the property $x_i=x_j$ is defined as $Q_{i,j}$, meaning all coloring schemes of graphs $G'$ satisfying this property; the size of the set is the number of coloring schemes satisfying this property, and the elements in the set correspond to all colored graphs $G'$ satisfying this property.

Back to the problem, "adjacent nodes must be colored the same color" can be understood as the intersection of several $Q$ sets. Therefore we can write

$$
F(S)=\left|\bigcap_{(i,j)\in S}Q_{i,j}\right|
$$

The meaning of the right side of the above expression is the number of coloring schemes such that for each edge $(i,j)$ in $S$, $x_i=x_j$ holds, which is exactly $F(S)$.

Doesn't it have a strong flavor of inclusion-exclusion? Since the inclusion-exclusion principle itself has no pair form, we map **all** edges $(i,j)$ onto $T=\frac{n(n+1)}{2}$ integers; assuming $(i,j)$ is mapped to $k,1\leq k\leq T$, and at the same time $Q_{i,j}$ is mapped to $Q_k$. Then the property $x_i=x_j$ is defined as $P_k$.

At the same time, $S$ can be represented as a set of several $k$s, i.e. $S\iff K=\{k_1,k_2,\cdots,k_m\}$. (That is, we establish an equivalence relation between the edge set and the number set.)

And $E$ corresponds to the set $M=\left\{1,2,\cdots,\frac{n(n+1)}{2}\right\}$. So then

$$
F(S)\iff F(\{ {k_i}\})=\left|\bigcap_{k_i}Q_{k_i}\right|
$$

### Reverse analysis

Then expanding the expression we want

$$
\begin{aligned}
Ans &= \sum_{K\subseteq M}(-1)^{|K|-1}\left|\bigcap_{k_i\in K}Q_{k_i}\right|\\
    &= \sum_{i}|Q_i|-\sum_{i<j}|Q_i\cap Q_j|+\sum_{i<j<k}|Q_i\cap Q_j\cap Q_k|-\cdots+(-1)^{T-1}\left|\bigcap_{i=1}^TQ_i\right|
\end{aligned}
$$

So the expanded form of the inclusion-exclusion principle appears; therefore we reverse-deduce this expression

$$
Ans=\left|\bigcup_{i=1}^TQ_i\right|
$$

Consider again the meaning of the right side of the equation: only one of the conditions $1\sim T$ needs to be satisfied, i.e. the number of coloring schemes in which two points are the same color (not necessarily adjacent)! And we know the universe of coloring schemes is $U$, obviously $|U|=m^n$. Converting to the complement, this is finding the number of coloring schemes in which all pairs are different colors, i.e. $A_m^n=\frac{m!}{(m-n)!}$. Therefore

$$
Ans=m^n-A_m^n
$$

To solve this problem, we first abstract the mathematical form of the problem, then start from the most informative condition in the problem, the definition of the $F(S)$ function, converting it into intersections, unions, and complements of sets. Then we convert the expression into the form of the inclusion-exclusion principle, and **reverse-deduce** the final result. This problem embodies precisely the reverse use of the inclusion-exclusion principle.

## Inclusion-exclusion in number theory

Using the inclusion-exclusion principle, one can cleverly solve some number-theory problems.

### Using inclusion-exclusion to find the number of pairs with greatest common divisor $k$

Consider the following problem:

???+ note "Finding the number of pairs with greatest common divisor $k$"
    Let $1 \le x, y \le N$, and let $f(k)$ denote the number of ordered pairs $(x, y)$ with greatest common divisor $k$; find the values of $f(1)$ to $f(N)$.

This problem can of course be done using Euler's totient function or Möbius inversion, but none of these is as simple as using the inclusion-exclusion principle.

By the inclusion-exclusion principle, we know: first find all pairs with $k$ as a **common divisor**, then remove from them all pairs with a multiple of $k$ as a **common divisor**; the remaining pairs are those with $k$ as the **greatest common divisor**. That is, $f(k)=$ the number of pairs with $k$ as a **common divisor** $-$ the number of pairs with a multiple of $k$ as a **common divisor**.

Further, one can find that the number of pairs with a multiple of $k$ as a **common divisor** equals the sum of the numbers of pairs with a multiple of $k$ as the **greatest common divisor**. So we can write the following expression:

$$
f(k)= \lfloor (N/k) \rfloor ^2 - \sum_{i=2}^{i*k \le N} f(i*k)
$$

Since when $k>N/2$ we can directly compute $f(k)= \lfloor (N/k) \rfloor ^2$, we can go in reverse, computing from $f(N)$ down to $f(1)$. Thus, we complete this problem using the inclusion-exclusion principle.

```cpp
for (long long k = N; k >= 1; k--) {
  f[k] = (N / k) * (N / k);
  for (long long i = k + k; i <= N; i += k) f[k] -= f[i];
}
```

The time complexity of the above method is $O( \sum_{i=1}^{N} N/i)=O(N \sum_{i=1}^{N} 1/i)=O(N \log N)$.

As a bonus, here is triple experience for everyone to practice.

-   [Luogu P2398 GCD SUM](https://www.luogu.com.cn/problem/P2398)
-   [Luogu P2158\[SDOI2008\] 仪仗队](https://www.luogu.com.cn/problem/P2158)
-   [Luogu P1447\[NOI2010\] 能量采集](https://www.luogu.com.cn/problem/P1447)

### Using inclusion-exclusion to derive Euler's totient function

Consider the following problem:

???+ note "Euler's totient function formula"
    Find Euler's totient function $\varphi(n)$, where $\varphi(n)=|\{1\leq x\leq n|\gcd(x,n)=1\}|$.

Direct computation is $O(n\log n)$, using a linear sieve is $O(n)$, and using the Du sieve is $O(n^{\frac{2}{3}})$ (well, why should an introductory number-theory problem done with inclusion-exclusion drag in the Du sieve). Next we consider using inclusion-exclusion to derive the formula for Euler's totient function.

To determine whether two numbers are coprime, first factor into primes

$$
n=\prod_{i=1}^k{p_i}^{c_i}
$$

Then we require that for any $p_i$, $x$ is not a multiple of $p_i$, i.e. $p_i\nmid x$. Treating this as a property, the corresponding set is $S_i$; therefore we have

$$
\varphi(n)=\left|\bigcap_{i=1}^kS_i\right|=|U|-\left|\bigcup_{i=1}^k\overline{S_i}\right|
$$

The size of the universe is $|U|=n$, and $\overline{S_i}$ represents the set formed by $p_i\mid x$; obviously $|\overline{S_i}|=\frac{n}{p_i}$, and from this we deduce

$$
\left|\bigcap_{a_i<a_{i+1}}S_{a_i}\right|=\frac{n}{\prod p_{a_i}}
$$

Therefore we obtain

$$
\begin{aligned}
\varphi(n)&=n-\sum_{i}\frac{n}{p_i}+\sum_{i<j}\frac{n}{p_ip_j}-\cdots+(-1)^k\frac{n}{p_1p_2 \cdots p_k}\\
&=n\left(1-\frac{1}{p_1}\right)\left(1-\frac{1}{p_2}\right)\cdots\left(1-\frac{1}{p_k}\right)\\
&=n\prod_{i=1}^k\left(1-\frac{1}{p_i}\right)
\end{aligned}
$$

This is the mathematical expression of Euler's totient function.

## Generalization of the inclusion-exclusion principle

The inclusion-exclusion principle is commonly used in counting problems of sets; for two functions of a set $f(S),g(S)$, if

$$
f(S)=\sum_{T\subseteq S}g(T)
$$

then

$$
g(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}f(T)
$$

### Proof

Next we prove this briefly. We start from the right side of the equation:

$$
\begin{aligned}
&\sum_{T\subseteq S}(-1)^{|S|-|T|}f(T)\\
=&\sum_{T\subseteq S}(-1)^{|S|-|T|}\sum_{Q\subseteq T}g(Q)\\
=&\sum_{Q}g(Q)\sum_{Q\subseteq T\subseteq S}(-1)^{|S|-|T|}\\
\end{aligned}
$$

We find that the latter part of the summation is independent of $Q$, so we remove $Q$ from the latter part:

$$
=\sum_{Q}g(Q)\sum_{T\subseteq (S\setminus Q)}(-1)^{|S\setminus Q|-|T|}
$$

Denote the function of a set $P$ as $F(P)=\sum_{T\subseteq P}(-1)^{|P|-|T|}$, and simplify this function:

$$
\begin{aligned}
F(P)&=\sum_{T\subseteq P}(-1)^{|P|-|T|}\\
&=\sum_{i=0}^{|P|}\dbinom{|P|}{i}(-1)^{|P|-i}=\sum_{i=0}^{|P|}\dbinom{|P|}{i}1^i(-1)^{|P|-i}\\
&=(1-1)^{|P|}=0^{|P|}
\end{aligned}
$$

Therefore, the value of the original expression is

$$
\sum_{Q}g(Q)\sum_{T\subseteq (S\setminus Q)}(-1)^{|S\setminus Q|-|T|}=\sum_{Q}g(Q)F(S\setminus Q)=\sum_{Q}g(Q)\cdot 0^{|S\setminus Q|}
$$

Analyzing, we find that only when $|S\setminus Q|=0$ do we have $0^0=1$, in which case $Q=S$, and the contribution to the answer is $g(S)$; at other times $0^{|S\setminus Q|}=0$, contributing nothing to the answer. Thus we obtain

$$
\sum_{Q}g(Q)\cdot 0^{|S\setminus Q|}=g(S)
$$

In summary, the result is proved.

### Corollary

This form also has such a corollary. Under the universe $U$, for functions $f(S),g(S)$, if

$$
f(S)=\sum_{S\subseteq T}g(T)
$$

then

$$
g(S)=\sum_{S\subseteq T}(-1)^{|T|-|S|}f(T)
$$

This corollary is in fact the complement form, with a similar proof.

## DAG counting

???+ note "DAG counting"
    Count labeled directed acyclic graphs on $n$ points, modulo $10^9+7$. $n\leq 5\times 10^3$.

### Direct DP

Consider DP. Define $f[i,j]$ to denote the number of DAGs on $i$ points with $j$ points of in-degree $0$. Suppose after removing these $j$ points, $k$ points have in-degree $0$; then before removal these $k$ points are connected by edges to at least some of these $j$ points, i.e. $2^j-1$ cases; and these $j$ points, besides being connected to the $k$ points, can also be connected arbitrarily to the remaining points, i.e. $2^{i-j-k}$ cases. Therefore the equation is as follows:

$$
f[i,j]=\binom{i}{j}\sum_{k=1}^{i-j}(2^j-1)^k2^{(i-j-k)j}f[i-j,k]
$$

The complexity of computing the above is $O(n^3)$.

### Relaxing the constraint

The definition of the above DP, exactly $j$ points of in-degree $0$, is too strict, and can be relaxed to at least $j$ points of in-degree $0$. Directly define $f[i]$ to denote the number of DAGs on $i$ points. We can directly use inclusion-exclusion. Consider the $j$ points selected; these $j$ points can be connected arbitrarily to the remaining $i-j$ points, i.e. $\left(2^{i-j}\right)^j=2^{(i-j)j}$ cases:

$$
f[i]=\sum_{j=1}^i(-1)^{j-1}\binom{i}{j}2^{(i-j)j}f[i-j]
$$

The complexity of computing the above is $O(n^2)$.

## Min-max inclusion-exclusion

For a sequence $\{x_i\}$ satisfying a [total order](../order-theory.md#偏序集) relation and whose elements satisfy additivity/subtractivity, let its length be $n$, and let $S=\{1,2,3,\cdots,n\}$; then:

$$
\max_{i\in S}{x_i}=\sum_{T\subseteq S}{(-1)^{|T|-1}\min_{j\in T}{x_j}}
$$

$$
\min_{i\in S}{x_i}=\sum_{T\subseteq S}{(-1)^{|T|-1}\max_{j\in T}{x_j}}
$$

**Proof:** Consider making a mapping to the general inclusion-exclusion principle. For $x\in S$, suppose $x$ is the $k$-th smallest element. Then we define a mapping $f:x\mapsto \{1,2,\cdots,k\}$. Obviously this is a bijection.

Then it is easy to find that for $x,y\in S$, $f(\min(x,y))=f(x)\cap f(y)$, $f(\max(x,y))=f(x)\cup f(y)$. Therefore we obtain:

$$
\begin{aligned}
\left|f\left(\max_{i\in S}{x_i}\right)\right|
&= \left| \bigcup_{i\in S} f(x_i) \right|\\
&= \sum_{T\subseteq S}(-1)^{|T|-1} \left|\bigcap_{j\in T}f(x_j)\right|\\
&= \sum_{T\subseteq S}(-1)^{|T|-1} \left|f\left(\min_{j\in T}{x_j}\right)\right|\\
\end{aligned}
$$

Then map $\left|f\left(\max_{i\in S}{x_i}\right)\right|$ back to $\max_{i\in S}{x_i}$, and $\min$ is similar.

Q.E.D.

But you may feel this formula is very silly—the maximum can obviously be found directly. The reason min-max inclusion-exclusion is so important is that it also holds in expectation, i.e.:

$$
E\left(\max_{i\in S}{x_i}\right)=\sum_{T\subseteq S}{(-1)^{|T|-1}E\left(\min_{j\in T}{x_j} \right)}
$$

$$
E\left(\min_{i\in S}{x_i}\right)=\sum_{T\subseteq S}{(-1)^{|T|-1}E\left(\max_{j\in T}{x_j} \right)}
$$

**Proof:** We consider one method of computing expectation:

$$
E\left(\max_{i\in S}{x_i}\right)=\sum_{y}{P(y=x)\max_{j\in S}{y_j}}
$$

where $y$ is a sequence of length $n$.

We apply the previous formula to the $\max$ at the back:

$$
\begin{aligned}E\left(\max_{i\in S}{x_i}\right)&=\sum_{y}{P(y=x)\max_{j\in S}{y_j}}\\
&=\sum_{y}{P(y=x)\sum_{T\subseteq S}{(-1)^{|T|-1}\min_{j\in T}{y_j}}} \end{aligned}
$$

Swap the summation order:

$$
\begin{aligned}E\left(\max_{i\in S}{x_i}\right)
&=\sum_{y}{P(y=x)\sum_{T\subseteq S}{(-1)^{|T|-1}\min_{j\in T}{y_j}}}\\
&=\sum_{T\subseteq S}{(-1)^{|T|-1}\sum_y{P(y=x)\min_{j\in T}{y_j}}}\\
&=\sum_{T\subseteq S}{(-1)^{|T|-1}E\left(\min_{j\in T}{y_j}\right)} \end{aligned}
$$

$\min$ is similar.

Q.E.D.

There is an even stronger one:

$$
\underset{i\in S}{\operatorname{kthmax}{x_i}}=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\min_{j\in T}{x_j}}
$$

$$
\underset{i\in S}{\operatorname{kthmin}{x_i}}=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\max_{j\in T}{x_j}}
$$

$$
E\left(\underset{i\in S}{\operatorname{kthmax}{x_i}}\right)=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}E\left(\min_{j\in T}{x_j}\right)}
$$

$$
E\left(\underset{i\in S}{\operatorname{kthmin}{x_i}}\right)=\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}E\left(\max_{j\in T}{x_j}\right)}
$$

It is stipulated that if $n< m$, then $\dbinom nm=0$.

**Proof:** Without loss of generality, suppose $\forall 1\le i<n,x_i\le x_{i+1}$. Then:

$$
\begin{aligned}
\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\min_{j\in T}{x_j}}
&=\sum_{i\in S}{x_i\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\left[x_i=\min_{j\in T}{x_j} \right]}}\\
&=\sum_{i\in S}{x_i\sum_{j=k}^n{\dbinom {n-i}{j-1}\dbinom {j-1}{k-1}(-1)^{j-k}}}
\end{aligned}
$$

And because there is a combinatorial identity: $\dbinom ab\dbinom bc=\dbinom ac\dbinom {a-c}{b-c}$, we have:

$$
\begin{aligned}
\sum_{T\subseteq S}{(-1)^{|T|-k}\dbinom {|T|-1}{k-1}\min_{j\in T}{x_j}}
&=\sum_{i\in S}{x_i\sum_{j=k}^n{\dbinom {n-i}{j-1}\dbinom {j-1}{k-1}(-1)^{j-k}}}\\
&=\sum_{i\in S}{x_i\sum_{j=k}^n{\dbinom {n-i}{k-1}\dbinom {n-i-k+1}{j-k}(-1)^{j-k}}}\\
&=\sum_{i\in S}{\dbinom {n-i}{k-1}x_i\sum_{j=k}^n{\dbinom {n-i-k+1}{j-k}(-1)^{j-k}}}\\
&=\sum_{i\in S}{\dbinom {n-i}{k-1}x_i\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}}
\end{aligned}
$$

When $i=n-k+1$:

$$
\dbinom {n-i}{k-1}\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}=1
$$

Otherwise:

$$
\dbinom {n-i}{k-1}\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}=0
$$

So:

$$
\sum_{i\in S}{\dbinom {n-i}{k-1}x_i\sum_{j=0}^{n-i-k+1}{\dbinom {n-i-k+1}j(-1)^{j}}}=\underset{i\in S}{\operatorname{kthmax}}{x_i}
$$

The remaining three are similar.

Q.E.D.

Based on min-max inclusion-exclusion, we can also obtain the following formula:

$$
\underset{i\in S}{\operatorname{lcm}}{x_i}=\prod_{T\subseteq S}{\left(\gcd_{j\in T}{x_j} \right)^{(-1)^{|T|-1}}}
$$

Because $\operatorname{lcm},\gcd,a^{1},a^{-1}$ correspond respectively to $\max,\min,+,-$, that is, it amounts to doing a min-max inclusion-exclusion on the exponents, so it is naturally correct.

## PKUWC2018 Random Walk

???+ note "[PKUWC2018 Random Walk](https://loj.ac/problem/2542)"
    Given a tree with $n$ points, you start from $x$; each time you choose an edge incident to the current point uniformly at random and walk across it.
    
    There are $Q$ queries. Each query gives a set $S$, and asks: if starting from $x$ and walking randomly until every point in the point set $S$ has been passed at least once, the expected number of steps walked.
    
    In particular, point $x$ (the start point) is regarded as having been passed once at the very beginning.
    
    Take modulo $998244353$.
    
    $1\le n\le 18,1\le Q\le 5000,1\le |S|\le n$.

The expected number of steps walked is also the walking time. So let the random variable $x_i$ denote the time of first reaching node $i$. Then what we want is

$$
E\left(\max_{i\in S}x_i\right)
$$

Using min-max inclusion-exclusion, we obtain

$$
E\left(\max_{i\in S}x_i\right)
=E\left(\sum_{T\subseteq S}(-1)^{|T|-1}\min_{i\in T}x_i\right)
=\sum_{T\subseteq S}(-1)^{|T|-1}E\left(\min_{i\in T}x_i\right)
$$

For a set $T\in[n]$, consider finding $F(T)=E(\min_{i\in T}x_i)$.

Consider the meaning of $E(\min_{i\in T}x_i)$: it is the expected time of first reaching some point in $T$. Let $f(i)$ denote the expected time of first reaching some node in $T$, starting from node $i$.

-   For $i\in T$, $f(i)=0$.
-   For $i\notin T$, $f(i)=1+\frac{1}{\text{deg}(i)}\sum_{(i,j)\in E}f(j)$.

If we directly use Gaussian elimination, the complexity is $O(n^3)$. Then computing $F(T)$ for each $T$ has total complexity $O(2^nn^3)$, which is unacceptable. We use the technique of elimination on a tree.

Suppose the root is $1$, and the parent of node $u$ is $p_u$. For a leaf node $i$, $f(i)$ is only related to $i$'s parent (or possibly $f(i)=0$, which is even better). Therefore we can express $f(i)$ in the form $f(i)=A_i+B_if(p_i)$, where $A_i,B_i$ can be quickly computed.

For a non-leaf node $i$, consider its children sequence $j_1,\cdots,j_k$. Since $f(j_e)=A_{j_e}+B_{j_e}f(i)$, we obtain

$$
f(i)=1+\frac{1}{\deg(i)}\sum_{e=1}^k\left(A_{j_e}+B_{j_e}f(i)\right)+\frac{f(p_i)}{\deg(i)}
$$

Then transforming a bit we obtain

$$
f(i)=\frac{\deg(i)+\sum_{e=1}^kA_{j_e}}{\deg(i)-\sum_{e=1}^kB_{j_e}}+
\frac{f(p_i)}{\deg(i)-\sum_{e=1}^kB_{j_e}}
$$

So we have also written $f(i)$ in the form $A_i+B_if(p_i)$. This can be pushed back all the way to the root. And the root has no parent. That is,

$$
f(1)=\frac{\deg(1)+\sum_{e=1}^kA_{j_e}}{\deg(1)-\sum_{e=1}^kB_{j_e}}
$$

Solving this equation gives us $f(1)$, and pushing once more from top to bottom gives $f(i)$ for each point. Then $F(T)=f(x)$. The time complexity is $O(n)$.

In this way, we can compute $F(T)$ for each $T$, with time complexity $O(2^nn)$.

Back to the inclusion-exclusion part, we know $E(\max_{i\in S}x_i)=\sum_{T\subseteq S}(-1)^{|T|-1}F(T)$.

Let $F'(T)=(-1)^{|T|-1}F(T)$; then we further obtain $E(\max_{i\in S}x_i)=\sum_{T\subseteq S}F'(T)$. Therefore we can use FMT (also called subset prefix sum, or the FWT-or transform) to compute $E(\max_{i\in S}x_i)$ for each $S$ in $O(2^nn)$ time, so that queries can be answered in $O(1)$.

### Exercises

-   [ABC331- G - Collect Them All](https://atcoder.jp/contests/abc331/tasks/abc331_g)
-   [Luogu P4707 重返现世](https://www.luogu.com.cn/problem/P4707)

## References

[A Brief Exploration of the Inclusion-Exclusion Principle - Wang Di](https://github.com/OI-wiki/libs/blob/master/%E9%9B%86%E8%AE%AD%E9%98%9F%E5%8E%86%E5%B9%B4%E8%AE%BA%E6%96%87/%E5%9B%BD%E5%AE%B6%E9%9B%86%E8%AE%AD%E9%98%9F2013%E8%AE%BA%E6%96%87%E9%9B%86.pdf), 2013 Informatics Olympiad China National Team Candidate Members Paper Collection

[Counting Labeled DAGs Series of Problems - Cyhlnj](https://www.cnblogs.com/cjoieryl/p/10078167.html)
