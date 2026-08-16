## Definition

Prerequisite knowledge: [order and primitive root](./primitive-root.md).

The definition of the discrete logarithm is similar to that of the logarithm. Take a positive integer modulus $m$ that has a primitive root, and let one of its primitive roots be $g$. For an integer $a$ satisfying $(a,m)=1$, we know that there must exist a unique integer $0\leq k<\varphi(m)$ such that

$$
g^k\equiv a\pmod m
$$

We call this $k$ the discrete logarithm of $a$ to base $g$ modulo $m$, denoted $k=\operatorname{ind}_g a$, and when there is no confusion it can be denoted $\operatorname{ind} a$.

Obviously $\operatorname{ind}_g 1=0$ and $\operatorname{ind}_g g=1$.

## Properties

The properties of the discrete logarithm also have many similarities with those of the logarithm.

???+ note "Properties"
    Let $g$ be a primitive root modulo $m$, with $(a,m)=(b,m)=1$; then:
    
    1.  $\operatorname{ind}_g(ab)\equiv\operatorname{ind}_g a+\operatorname{ind}_g b\pmod{\varphi(m)}$
    
        and further $(\forall n\in\mathbf{N}),~~\operatorname{ind}_g a^n\equiv n\operatorname{ind}_g a\pmod{\varphi(m)}$
    2.  If $g_1$ is also a primitive root modulo $m$, then $\operatorname{ind}_g a\equiv\operatorname{ind}_{g_1}a \cdot \operatorname{ind}_g g_1\pmod{\varphi(m)}$
    3.  $a\equiv b\pmod m\iff \operatorname{ind}_g a=\operatorname{ind}_g b$

???+ note "Proof"
    1.  $g^{\operatorname{ind}_g(ab)}\equiv ab\equiv g^{\operatorname{ind}_g a}g^{\operatorname{ind}_g b}\equiv g^{\operatorname{ind}_g a+\operatorname{ind}_g b}\pmod m$
    2.  Let $x=\operatorname{ind}_{g_1}a$; then $a\equiv g_1^x\pmod m$. Also let $y=\operatorname{ind}_g g_1$; then $g_1\equiv g^y\pmod m$.
    
        So $a\equiv g^{xy}\pmod m$, i.e. $\operatorname{ind}_g a\equiv xy\equiv\operatorname{ind}_{g_1}a \cdot \operatorname{ind}_g g_1\pmod{\varphi(m)}$
    3.  Note that
    
        $$
        \begin{aligned}
            \operatorname{ind}_g a=\operatorname{ind}_g b&\iff \operatorname{ind}_g a\equiv\operatorname{ind}_g b\pmod{\varphi(m)}\\
            &\iff g^{\operatorname{ind}_g a}\equiv g^{\operatorname{ind}_g b}\pmod m\\
            &\iff a\equiv b\pmod m
        \end{aligned}
        $$

## Baby-step giant-step algorithm

At present there still does not exist a classical polynomial-time algorithm for the discrete logarithm problem (the input size of the discrete logarithm problem is the number of digits of the input data). In cryptography, based on this fact, people have designed many asymmetric encryption algorithms, such as [Ed25519](https://en.wikipedia.org/wiki/EdDSA#Ed25519).

In competitive programming, BSGS (baby-step giant-step) is commonly used to solve the discrete logarithm problem. Formally speaking, for $a,b,m\in\mathbf{Z}^+$, this algorithm can solve

$$
a^x \equiv b \pmod m
$$

in $O(\sqrt{m})$ time, where $a\perp m$. The solution $x$ of the equation satisfies $0 \le x < m$. (Note that $m$ is not necessarily prime.)

### Algorithm description

Let $x = A \left \lceil \sqrt m \right \rceil - B$, where $0\le A,B \le \left \lceil \sqrt m \right \rceil$; then we have $a^{A\left \lceil \sqrt m \right \rceil -B} \equiv b \pmod m$, and with a slight transformation, we have $a^{A\left \lceil \sqrt m \right \rceil} \equiv ba^B \pmod m$.

What we know is $a,b$, so we can first compute all the values of $ba^B$ on the right side of the equation by enumerating $B$, store them with a `hash`/`map`, and then compute $a^{A\left \lceil \sqrt m \right \rceil}$ one by one, enumerating $A$, looking for whether there is a $ba^B$ equal to it, from which we can obtain all $x$, $x=A \left \lceil \sqrt m \right \rceil - B$.

Note that both $A,B$ are less than $\left \lceil \sqrt m \right \rceil$, so the time complexity is $\Theta\left  (\sqrt m\right )$, and using a `map` adds a factor of $\log$.

??? note "Why is $a$ required to be coprime with $m$"
    Note that what we compute is $A,B$; we need to guarantee that from $a^{A\left \lceil \sqrt m \right \rceil} \equiv ba^B \pmod m$ we can deduce back to $a^{A\left \lceil \sqrt m \right \rceil -B} \equiv b \pmod m$. The latter is obtained by dividing both sides of the former by $a^B$, so we must have $a^B \perp m$, i.e. $a\perp m$.

## Extended BSGS algorithm

For $a,b,m\in\mathbf{Z}^+$, solve

$$
a^x\equiv b\pmod m
$$

where $a,m$ are not necessarily coprime.

When $(a, m)=1$, $a$ has an inverse modulo $m$, so BSGS can be used to solve it. So we try to make them coprime.

Specifically, let $d_1=(a, m)$. If $d_1\nmid b$, then the original equation has no solution. Otherwise we divide the equation by $d_1$, obtaining

$$
\frac{a}{d_1}\cdot a^{x-1}\equiv \frac{b}{d_1}\pmod{\frac{m}{d_1}}
$$

If $a$ and $\frac{m}{d_1}$ are still not coprime, divide again; let $d_2=\left(a, \frac{m}{d_1}\right)$. If $d_2\nmid \frac{b}{d_1}$, then the equation has no solution; otherwise divide by $d_2$ to obtain

$$
\frac{a^2}{d_1d_2}\cdot a^{x-2}≡\frac{b}{d_1d_2} \pmod{\frac{m}{d_1d_2}}
$$

Similarly, keep judging like this until $a\perp \dfrac{m}{d_1d_2\cdots d_k}$.

Let $D=\prod_{i=1}^kd_i$; then the equation becomes:

$$
\frac{a^k}{D}\cdot a^{x-k}\equiv\frac{b}{D} \pmod{\frac{m}{D}}
$$

Since $a\perp\dfrac{m}{D}$, we deduce $\dfrac{a^k}{D}\perp \dfrac{m}{D}$. Thus $\dfrac{a^k}{D}$ has an inverse, so we move it to the right side of the equation, and this is an ordinary BSGS problem. So after solving for $x-k$ and then adding $k$, we get the solution of the original equation.

Note that we cannot rule out the case where the solution is less than or equal to $k$, so before eliminating factors, do a $\Theta(k)$ enumeration and directly verify $a^i\equiv b \pmod m$; this avoids this situation.

## Fast discrete logarithm based on value-range preprocessing

The BSGS algorithm above has a single-query time complexity of $O(\sqrt m)$, which is inefficient when the number of queries is large. If the modulus for each query is a fixed prime $p$, we have a fast algorithm based on value-range preprocessing.

We already know $\operatorname{ind}_g(ab)\equiv\operatorname{ind}_g a+\operatorname{ind}_g b\pmod{p-1}$, so we can compute the discrete logarithm via the BSGS algorithm only for all primes, and the discrete logarithm of a composite number can be transformed via this formula into a sum of several known prime discrete logarithm values. At this point the complexity is still not optimal, so we consider preprocessing only a part of the discrete logarithms. Specifically, we preprocess the discrete logarithms of $1$ to $L = \lfloor\sqrt p\rfloor + 1$. Note that the BSGS block length $B$ here **cannot be taken** as $O(\sqrt{L})$, because the complexity of the BSGS preprocessing (inserting into the hash table) part is $O(B)$, while queries require $O(\pi(L))$ times in total, so the total time complexity is $O\left(B+\dfrac{\pi(L)p}{B}\right)$; in this case taking $B=O(\sqrt{\pi(L)p})$ is optimal. By the [prime number theorem](./prime.md) $\pi(n)\sim\dfrac{n}{\log n}$, the total preprocessing time complexity can be balanced to $O\left(\dfrac{p^{3/4}}{\log^{1/2} p}\right)$.

Next is how to find the answer. Suppose the current query is $\operatorname{ind}_g y$; if $y\le L$ then directly return, otherwise let $p=vy+r$, then $v=\left\lfloor\dfrac{p}{y}\right\rfloor<L$, $r=p\bmod y$, $y=\dfrac{p-r}{v}$, so

$$
\begin{aligned}
\operatorname{ind}_g y &\equiv \operatorname{ind}_g (p-r)-\operatorname{ind}_g v\\
&\equiv \operatorname{ind}_g (-r)-\operatorname{ind}_g v\\
&\equiv \operatorname{ind}_g (p-1)+\operatorname{ind}_g r-\operatorname{ind}_g v \pmod{p-1}.
\end{aligned}
$$

Noting that $\operatorname{ind}_g (p-1)=(p-1)/2$, we only need to recursively compute the discrete logarithm of $r$.

We can also consider another expression for $y$; noting that $p=vy+r=(v+1)y+r-y$, then $y=\dfrac{p-r+y}{v+1}$, so

$$
\operatorname{ind}_g y\equiv \operatorname{ind}_g (y-r)-\operatorname{ind}_g (v+1) \pmod{p-1}.
$$

We have $v+1 \le L$, so we only need to recursively compute the discrete logarithm of $y-r$.

Combining these two computation methods, we have $\min\{r,y-r\}\le \dfrac{y}{2}$, so recursively computing the smaller of the two achieves an $O(\log p)$ query complexity.

At this point we have obtained an algorithm with time complexity $O\left(\dfrac{p^{3/4}}{\log^{1/2} p}\right)-O(\log p)$.

??? example "[Luogu11175【模板】基于值域预处理的快速离散对数](https://www.luogu.com.cn/problem/P11175)"
    ```cpp
    --8<-- "docs/math/code/discrete-logarithm/discrete-logarithm-1.cpp"
    ```

## Exercises

-   [SPOJ MOD](https://www.spoj.com/problems/MOD/) template
-   [SDOI2013 随机数生成器](https://www.luogu.com.cn/problem/P3306)
-   [SGU261 Discrete Roots](https://codeforces.com/problemsets/acmsguru/problem/99999/261) template
-   [SDOI2011 计算器](https://loj.ac/problem/10214) template
-   [Luogu4195【模板】exBSGS/Spoj3105 Mod](https://www.luogu.com.cn/problem/P4195) template
-   [Codeforces - Lunar New Year and a Recursive Sequence](https://codeforces.com/contest/1106/problem/F)
-   [LOJ6542 离散对数](https://loj.ac/problem/6542) index calculus method, non-template

**Part of the content and code of this page is translated from the blog post [Дискретное извлечение корня](http://e-maxx.ru/algo/discrete_root) and its English translation [Discrete Root](https://cp-algorithms.com/algebra/discrete-root.html). The Russian version is under the Public Domain + Leave a Link license; the English version is under the CC-BY-SA 4.0 license.**

## References

1.  [Discrete logarithm - Wikipedia](https://en.wikipedia.org/wiki/Discrete_logarithm)
2.  潘承洞，潘承彪．初等数论．
3.  冯克勤．初等数论及其应用．
