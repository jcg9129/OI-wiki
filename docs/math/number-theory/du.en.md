author: hsfzLZH1, sshwy, StudyingFather, Marcythm

Du's sieve is used to handle the prefix-sum problem for a class of arithmetic functions. For an arithmetic function $f$, Du's sieve can compute $S(n)=\sum_{i=1}^{n}f(i)$ in sublinear time complexity.

## Algorithm idea

We try to construct a recurrence for $S(n)$ in terms of $S\left(\left\lfloor\frac{n}{i}\right\rfloor\right)$.

For any arithmetic function $g$, it must satisfy:

$$
\begin{aligned}
    \sum_{i=1}^{n}(f * g)(i) & =\sum_{i=1}^{n}\sum_{d \mid i}g(d)f\left(\frac{i}{d}\right)           \\
                             & =\sum_{i=1}^{n}g(i)S\left(\left\lfloor\frac{n}{i}\right\rfloor\right)
\end{aligned}
$$

where $f*g$ is the [Dirichlet convolution](./dirichlet.md#dirichlet-convolution) of the arithmetic functions $f$ and $g$.

???+ note "Brief proof"
    $g(d)f\left(\frac{i}{d}\right)$ contributes to all $i\leq n$, so changing the enumeration order, enumerate $d,\frac{i}{d}$ (corresponding to the new $i,j$ respectively)
    
    $$
    \begin{aligned}
        \sum_{i=1}^n\sum_{d \mid i}g(d)f\left(\frac{i}{d}\right) & =\sum_{i=1}^n\sum_{j=1}^{\left\lfloor n/i \right\rfloor}g(i)f(j) \\
                                                                 & =\sum_{i=1}^ng(i)\sum_{j=1}^{\left\lfloor n/i \right\rfloor}f(j) \\
                                                                 & =\sum_{i=1}^ng(i)S\left(\left\lfloor\frac{n}{i}\right\rfloor\right)
    \end{aligned}
    $$

Then we can obtain the recurrence:

$$
\begin{aligned}
    g(1)S(n) & = \sum_{i=1}^n g(i)S\left(\left\lfloor\frac{n}{i}\right\rfloor\right) - \sum_{i=2}^n g(i)S\left(\left\lfloor\frac{n}{i}\right\rfloor\right) \\
             & = \sum_{i=1}^n (f * g)(i) - \sum_{i=2}^n g(i)S\left(\left\lfloor\frac{n}{i}\right\rfloor\right)
\end{aligned}
$$

If we can construct an appropriate arithmetic function $g$ such that:

1.  $\sum_{i=1}^n(f * g)(i)$ can be computed quickly;
2.  the prefix sum of $g$ can be computed quickly, so as to use number-theoretic block decomposition to solve $\sum_{i=2}^ng(i)S\left(\left\lfloor\dfrac{n}{i}\right\rfloor\right)$.

then we can obtain $g(1)S(n)$ in a relatively short time.

???+ warning "Note"
    Regardless of whether the arithmetic function $f$ is a multiplicative function, as long as an appropriate arithmetic function $g$ can be constructed, one can consider using Du's sieve to find the prefix sum of $f$.
    
    For example, consider $f(n)=\mathrm{i}\varphi(n)$; obviously $f$ is not a multiplicative function, but one can take $g(n)=1$, so that:
    
    $$
    \sum_{k=1}^n (f*g)(k)=\mathrm{i}\frac{n(n+1)}{2}
    $$
    
    The time complexity of computing both $\sum_{k\leq m} (f*g)(k)$ and $\sum_{k \leq m} g(k)$ is $O(1)$, so one can consider using Du's sieve.

## Time complexity

Let $R(n)=\left\{\left\lfloor \dfrac{n}{k} \right\rfloor: k=2,3,\dots,n\right\}$. Using the [properties](./sqrt-decomposition.md#性质) of number-theoretic block decomposition, we know that for any $m\in R(n)$, we have $R(m)\subseteq R(n)$. That is to say, after using memoization, we only need to compute $S(k)$ once for all $k\in R(n)$ to obtain the values of $R(n)$. And the number of these points $|R(n)|=O(\sqrt{n})$.

Suppose the time complexity of computing $\sum_{i=1}^n(f * g)(i)$ and $\sum_{i=1}^n g(i)$ is both $O(1)$. Let the time complexity of computing $S(n)$ be $T(n)$; then:

$$
\begin{aligned}
    T(n) & = \sum_{k\in R(n)} T(k)\\
         & = \Theta(\sqrt n)+\sum_{k=1}^{\lfloor\sqrt n\rfloor} O(\sqrt k)+\sum_{k=2}^{\lfloor\sqrt n\rfloor} O\left(\sqrt{\dfrac{n}{k}}\right)\\
         & = O\left(\int_{0}^{\sqrt n} \left(\sqrt{x} + \sqrt{\dfrac{n}{x}}\right) \mathrm{d}x\right)\\
         & = O\left(n^{3/4}\right).
\end{aligned}
$$

If we can preprocess a part of $S(k)$, where $k=1,2,\dots,m$, $m\geq \lfloor\sqrt n\rfloor$. Let the time complexity of preprocessing be $T_0(m)$; then $T(n)$ at this point is:

$$
\begin{aligned}
    T(n) & = T_0(m)+\sum_{k\in R(n);k>m} T(k)\\
         & = T_0(m)+\sum_{k=1}^{\lfloor n/m \rfloor} O\left(\sqrt{\dfrac{n}{k}}\right)\\
         & = O\left(T_0(m)+\int_{0}^{n/m} \sqrt{\dfrac{n}{x}} \mathrm{d}x\right)\\
         & = O\left(T_0(m)+\dfrac{n}{\sqrt m}\right).
\end{aligned}
$$

If $T_0(m)=O(m)$ (such as with a linear sieve), by the AM–GM inequality: when $m=\Theta\left(n^{2/3}\right)$, $T(n)$ attains its minimum value $O\left(n^{2/3}\right)$.

??? failure "An example of a false proof"
    Let the complexity of computing $S(n)$ be $T(n)$; then:
    
    $$
    T(n)=\Theta\left(\sqrt{n}\right)+O\left(\sum_{i=2}^{\lfloor\sqrt{n}\rfloor} T\left(\left\lfloor\frac{n}{i}\right\rfloor\right)\right)
    $$
    
    $$
    \begin{aligned}
        T\left(\left\lfloor\frac{n}{i}\right\rfloor\right) & = \Theta\left(\sqrt{\frac{n}{i}}\right)+O\left(\sum_{j=2}^{\lfloor\sqrt{n/i}\rfloor} T\left(\left\lfloor\frac{n}{ij}\right\rfloor\right)\right) \\
                                                           & = O\left(\sqrt{\frac{n}{i}}\right)
    \end{aligned}
    $$
    
    where $O\left(\sum_{j=2}^{\lfloor\sqrt{n/i}\rfloor} T\left(\left\lfloor\dfrac{n}{ij}\right\rfloor\right)\right)$ is regarded as a higher-order infinitesimal and can thus be discarded. So:
    
    $$
    \begin{aligned}
        T(n) & = \Theta\left(\sqrt{n}\right)+O\left(\sum_{i=2}^{\lfloor\sqrt{n}\rfloor} \sqrt{\frac{n}{i}}\right) \\
             & = O\left(\sum_{i=1}^{\lfloor\sqrt{n}\rfloor} \sqrt{\frac{n}{i}}\right) \\
             & = O\left(\int_{0}^{\sqrt{n}}\sqrt{\frac{n}{x}}\mathrm{d}x\right) \\
             & = O\left(n^{3/4}\right)
    \end{aligned}
    $$
    
    ??? bug "Bug"
        The problem lies in the step "regarded as a higher-order infinitesimal and can thus be discarded". Substituting $T\left(\left\lfloor\dfrac{n}{i}\right\rfloor\right)$ into the expression for $T(n)$, we have:
        
        $$
        \begin{aligned}
            T(n) & = \Theta\left(\sqrt{n}\right)+O\left(\sum_{i=2}^{\lfloor\sqrt{n}\rfloor} \sqrt{\frac{n}{i}}\right)+O\left(\sum_{i=2}^{\lfloor\sqrt{n}\rfloor}\sum_{j=2}^{\lfloor\sqrt{n/i}\rfloor} T\left(\left\lfloor\frac{n}{ij}\right\rfloor\right)\right)\\
                 & = O\left(\sqrt{n}+\int_{0}^{\sqrt{n}}\sqrt{\frac{n}{x}}\mathrm{d}x\right)+O\left(\sum_{i=2}^{\lfloor\sqrt{n}\rfloor}\sum_{j=2}^{\lfloor\sqrt{n/i}\rfloor} T\left(\left\lfloor\frac{n}{ij}\right\rfloor\right)\right)\\
                 & = O\left(n^{3/4}\right)+O\left(\sum_{i=2}^{\lfloor\sqrt{n}\rfloor}\sum_{j=2}^{\lfloor\sqrt{n/i}\rfloor} T\left(\left\lfloor\frac{n}{ij}\right\rfloor\right)\right)\\
        \end{aligned}
        $$
        
        Consider the part $\displaystyle\sum_{i=2}^{\lfloor\sqrt{n}\rfloor}\sum_{j=2}^{\lfloor\sqrt{n/i}\rfloor} T\left(\left\lfloor\frac{n}{ij}\right\rfloor\right)$; it is not hard to find that:
        
        $$
        \begin{aligned}
            \sum_{i=2}^{\lfloor\sqrt{n}\rfloor}\sum_{j=2}^{\lfloor\sqrt{n/i}\rfloor} T\left(\left\lfloor\frac{n}{ij}\right\rfloor\right) & = \Omega\left(\sum_{i=2}^{\lfloor\sqrt{n}\rfloor} T\left(\left\lfloor\frac{n}{i}\cdot\left\lfloor\sqrt\frac{n}{i}\right\rfloor^{-1}\right\rfloor\right)\right) \\
                                                                                                                                         & = \Omega\left(\sum_{i=2}^{\lfloor\sqrt{n}\rfloor} T\left(\left\lfloor\sqrt\frac{n}{i}\right\rfloor\right)\right)
        \end{aligned}
        $$
        
        Since memoization is not introduced, the $T\left(\left\lfloor\sqrt{\dfrac{n}{i}}\right\rfloor\right)$ in the above expression is still $\Omega\left(\left(\dfrac{n}{i}\right)^{1/4}\right)$, and therefore the so-called "higher-order infinitesimal" part cannot be discarded.
        
        In fact, the sublinear time complexity of Du's sieve is guaranteed by memoization. Only after using memoization can it be guaranteed that the multiple-summation term does not appear.

## Example problems

### Problem 1

???+ note "[P4213【模板】杜教筛（Sum）](https://www.luogu.com.cn/problem/P4213)"
    Find the values of $S_1(n)= \sum_{i=1}^{n} \mu(i)$ and $S_2(n)= \sum_{i=1}^{n} \varphi(i)$, where $1\leq n<2^{31}$.

=== "Prefix sum of the Möbius function"
    We know:
    
    $$
    \epsilon = [n=1] = \mu * 1 = \sum_{d \mid n} \mu(d)
    $$
    
    $$
    \begin{aligned}
        S_1(n) & =\sum_{i=1}^n \epsilon (i)-\sum_{i=2}^n S_1 \left(\left\lfloor \frac n i \right\rfloor\right) \\
               & = 1-\sum_{i=2}^n S_1\left(\left\lfloor \frac n i \right\rfloor\right)
    \end{aligned}
    $$
    
    For the derivation of the time complexity, see the [Time complexity](#time-complexity) section.
    
    For larger values, one needs to use `map`/`unordered_map` to store their corresponding values, so that previously computed results can be used directly when needed later.

=== "Prefix sum of Euler's totient function"
    Of course one can also use Du's sieve to find the prefix sum of $\varphi (x)$, but a better method is to apply Möbius inversion.
    
    === "Möbius inversion"
        $$
        \begin{aligned}
            \sum_{i=1}^n \sum_{j=1}^n [\gcd(i,j)=1] & =\sum_{i=1}^n \sum_{j=1}^n \sum_{d \mid i,d \mid j} \mu(d)    \\
                                                    & =\sum_{d=1}^n \mu(d) {\left\lfloor \frac n d \right\rfloor}^2
        \end{aligned}
        $$
        
        Since what the problem asks for is $\sum_{i=1}^n \sum_{j=1}^i [\gcd(i,j)=1]$, we exclude the case $i=1,j=1$ and divide the result by $2$.
        
        We observe that as long as we find the prefix sum of the Möbius function, we can quickly compute the prefix sum of Euler's totient function. Time complexity $O\left(n^{\frac 2 3}\right)$.
    
    === "Du's sieve"
        Find $S(n)=\sum_{i=1}^n\varphi(i)$.
        
        Similarly, $\varphi * 1=\operatorname{id}$, so:
        
        $$
            \begin{aligned}
                S(n) & =\sum_{i=1}^n i - \sum_{i=2}^n S\left(\left\lfloor\frac{n}{i}\right\rfloor\right)    \\
                     & =\frac{1}{2}n(n+1) - \sum_{i=2}^n S\left(\left\lfloor\frac{n}{i}\right\rfloor\right)
            \end{aligned}
        $$

??? note "Code implementation"
    ```cpp
    --8<-- "docs/math/code/du/du_1.cpp"
    ```

### Problem 2

???+ note "[「LuoguP3768」简单的数学题](https://www.luogu.com.cn/problem/P3768)"
    Summary: find
    
    $$
    \sum_{i=1}^n\sum_{j=1}^ni\cdot j\cdot\gcd(i,j)\pmod p
    $$
    
    where $n\leq 10^{10},5\times 10^8\leq p\leq 1.1\times 10^9$, and $p$ is prime.

Using $\varphi * 1=\operatorname{id}$ to do Möbius inversion, it becomes:

$$
\sum_{d=1}^nF^2\left(\left\lfloor\frac{n}{d}\right\rfloor\right)\cdot d^2\varphi(d)
$$

where $F(n)=\dfrac{1}{2}n(n+1)$

Do number-theoretic block decomposition on $\sum_{d=1}^nF\left(\left\lfloor\dfrac{n}{d}\right\rfloor\right)^2$, and process the prefix sum of $d^2\varphi(d)$ with Du's sieve:

$$
f(n)=n^2\varphi(n)=(\operatorname{id}^2\varphi)(n)
$$

$$
S(n)=\sum_{i=1}^nf(i)=\sum_{i=1}^n(\operatorname{id}^2\varphi)(i)
$$

We need to construct a multiplicative function $g$ such that $f\times g$ and $g$ can have their sums computed quickly.

The prefix sum of $\varphi$ alone can be processed with the Du's sieve of $\varphi * 1$, but the $f$ here has an extra $\operatorname{id}^2$, so we convolve an $\operatorname{id}^2$ onto it to make it constant:

$$
S(n)=\sum_{i=1}^n\left(\left(\operatorname{id}^2\varphi\right) * \operatorname{id}^2\right)(i)-\sum_{i=2}^n\operatorname{id}^2(i)S\left(\left\lfloor\frac{n}{i}\right\rfloor\right)
$$

Simplify the convolution a bit:

$$
\begin{aligned}
    ((\operatorname{id}^2\varphi)* \operatorname{id}^2)(i) & =\sum_{d \mid i}\left(\operatorname{id}^2\varphi\right)(d)\operatorname{id}^2\left(\frac{i}{d}\right) \\
                                                           & =\sum_{d \mid i}d^2\varphi(d)\left(\frac{i}{d}\right)^2                                               \\
                                                           & =\sum_{d \mid i}i^2\varphi(d)=i^2\sum_{d \mid i}\varphi(d)                                            \\
                                                           & =i^2(\varphi*1)(i)=i^3
\end{aligned}
$$

Then simplify $S(n)$ a bit more:

$$
\begin{aligned}
    S(n) & =\sum_{i=1}^n\left((\operatorname{id}^2\varphi)* \operatorname{id}^2\right)(i)-\sum_{i=2}^n\operatorname{id}^2(i)S\left(\left\lfloor\frac{n}{i}\right\rfloor\right) \\
         & =\sum_{i=1}^ni^3-\sum_{i=2}^ni^2S\left(\left\lfloor\frac{n}{i}\right\rfloor\right)                                                                                  \\
         & =\left(\frac{1}{2}n(n+1)\right)^2-\sum_{i=2}^ni^2S\left(\left\lfloor\frac{n}{i}\right\rfloor\right)                                                                 \\
\end{aligned}
$$

Simply solve using block decomposition.

??? note "Code implementation"
    ```cpp
    --8<-- "docs/math/code/du/du_2.cpp"
    ```

### References

1.  任之洲，2016，《积性函数求和的几种方法》，2016 年信息学奥林匹克中国国家队候选队员论文
2.  [杜教筛的时空复杂度分析 - riteme.site](https://riteme.site/blog/2018-9-11/time-space-complexity-dyh-algo.html)
