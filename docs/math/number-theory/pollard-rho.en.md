## Introduction

Given a positive integer $N \in \mathbf{N}_{+}$, try to quickly find one of its [nontrivial factors](basic.md).

Consider the naive algorithm. Factors are distributed in pairs, and all factors of $N$ can be divided into two blocks, namely $[2, \sqrt N]$ and $[\sqrt N+1,N)$. We only need to traverse the numbers in $[2, \sqrt N]$ once, and then based on division we can find at least two factors. The time complexity of this method is $O(\sqrt N)$.

When $N\ge10^{18}$, the running time of this algorithm is unacceptable to us, and we hope for a better algorithm. One idea is, through a random method, to guess whether a number is a factor of $N$; if we are lucky, we can find the answer in $O(1)$ time complexity, but for data with $N\ge10^{18}$, the probability of a successful guess is $\frac{1}{10^{18}}$, and the expected number of guesses is $10^{18}$. If we guess within $[2,\sqrt N]$, the success rate will be higher. We hope for a method to optimize the guessing.

## Naive algorithm

The simplest algorithm is to traverse from $[2, \sqrt N]$.

=== "C++"
    ```cpp
    vector<int> breakdown(int N) {
      vector<int> result;
      for (int i = 2; i * i <= N; i++) {
        if (N % i == 0) {  // if i divides N, then i is a prime factor of N.
          while (N % i == 0) N /= i;
          result.push_back(i);
        }
      }
      if (N != 1) {  // this means that after the operations, N is left with a prime
        result.push_back(N);
      }
      return result;
    }
    ```

=== "Python"
    ```python
    def breakdown(N):
        result = []
        for i in range(2, int(sqrt(N)) + 1):
            if N % i == 0:  # if i divides N, then i is a prime factor of N.
                while N % i == 0:
                    N //= i
                result.append(i)
        if N != 1:  # this means that after the operations, N is left with a prime
            result.append(N)
        return result
    ```

We can prove that all elements in `result` are exactly all the prime factors of `N`.

??? note "Proof that `result` contains all prime factors of $N$"
    First examine the change of `N`. When the loop for `i` ends, since the part `while(N % i == 0) N /= i` has just finished executing, `i` no longer divides `N`. Moreover, each time we remove a factor, we can guarantee that `N` still divides $N$. These two points guarantee that when the loop for `i` begins, `N` is a factor of $N$ and is not divisible by any integer less than `i`.
    
    Next prove that the elements in `result` are all factors of $N$. When the loop reaches `i`, the condition for storing `i` in `result` is `N % i == 0`, which shows that `i` divides `N`, and since `N` has been shown to be a factor of $N$, `i` is a factor of $N$. When the loop over `i` ends, if `N` is not one, it is also stored in `result`. At this point, by the earlier discussion, it must also be a factor of $N$.
    
    Next prove that the elements in `result` are all primes. Suppose there exists a composite number $K$ in `result`; then there must exist an `i` not exceeding $\sqrt K$ such that `i` is a factor of `K`. Such a $K$ cannot be stored in `result` as some `i` in the loop, because the first paragraph has shown that when the loop reaches $K$, `N` is not divisible by any `i` less than $K$. Such a $K$ also cannot be added after the loop ends, because the loop's exit condition is `i * i > N`, so all `i` not exceeding $\sqrt K$ have already been traversed, and as stated above, these `i` can never divide the current `N`, i.e. $K$.
    
    Finally prove that all prime factors of $N$ must appear in `result`. Suppose $p$ is a prime factor of $N$ but does not appear in `result`. By the above discussion, $p$ cannot be an `i` that appeared in the loop. Let `i` be the last `i` before exiting the loop; then `i` is strictly less than $p$, and the `N` after exiting the loop is not divisible by the previous `i`, so $p$ divides `N`. So the final `N` is greater than one, and by the above, it must be prime, so `N` equals $p$, and it will be added to `result` at the end, contradicting the assumption.

It is worth pointing out that if a prime table has already been built at the start, the time complexity will drop from $O(\sqrt N)$ to $O(\frac {\sqrt{N}} {\ln N})$. Go to the [sieve methods](./sieve.md) page to look up more information about building tables.

Example problem: [CF 1445C](https://codeforces.com/problemset/problem/1445/C)

## Pollard's Rho algorithm

### Introduction

The complexity of obtaining a nontrivial factor using the brute-force algorithm is $O(p)=O(\sqrt N)$, where $p$ is the smallest prime factor of $N$. And the Pollard-Rho algorithm to be introduced below is a randomized algorithm that can obtain a nontrivial factor in $O(\sqrt p)=O(N^{1/4})$ expected complexity (**note**! a nontrivial factor is not necessarily a prime factor).

Its core idea is that for a random self-map $f: \mathbb Z_p \rightarrow \mathbb Z_p$, starting from any point $x_1$ and iteratively computing $x_n = f(x_{n-1})$, we will enter a cycle in $O(\sqrt p)$ expected time. If we can find $x_i \equiv x_j \pmod p$, then $p$ divides $\gcd(|x_i-x_j|, N)$, and this greatest common divisor is a nontrivial factor of $N$.

To understand why the expected time to enter a cycle is $O(\sqrt p)$, we can draw inspiration from the birthday paradox.

### Birthday paradox

Without considering the birth year (assuming each year has 365 days), the question is: how many people at least must be in a room so that the probability of two of them having the same birthday reaches $50\%$?

Solution: Suppose a year has $n$ days and the room has $k$ people, numbered with the integers $1, 2,\dots, k$. Assume each person's birthday is uniformly distributed over the $n$ days, and the birthdays of two people are mutually independent.

Let the event that all $k$ people have distinct birthdays be event $A$; then the probability of event $A$ is

$$
P(A)=\prod_{i=0}^{k-1}\frac{n-i}{n}
$$

The probability that at least two people have the same birthday is $P(\overline A)=1-P(A)$. According to the problem, $P(\overline A)\ge\frac{1}{2}$, so we have

$$
P(A)=\prod_{i=0}^{k-1}\frac{n-i}{n} \le \frac{1}{2}
$$

By the inequality $1+x\le \mathrm{e}^x$, we obtain

$$
P(A) \le \prod_{i=1}^{k-1}\exp\left({-\frac{i}{n}}\right)=\exp \left({-\frac{k(k-1)}{2n}}\right)
$$

Therefore

$$
\exp\left({-\dfrac{k(k-1)}{2n}}\right) \le \frac{1}{2}\implies P(A) \le \frac{1}{2}
$$

Substituting $n=365$, we solve to get $k\geq 23$. So a room needs at least $23$ people for the probability of two of them having the same birthday to reach $50\%$, but this mathematical fact is quite counterintuitive, so it is called a paradox.

When $k>56$ and $n=365$, the probability of two people having the same birthday will be greater than $99\%$[^ref1]. Then, in the case where a year has $n$ days, when the room has $\frac{1}{2}(\sqrt{8n\ln 2+1}+1)\approx \sqrt{2n\ln 2}$ people, the probability that at least two people have the same birthday is approximately $50\%$.

Similarly, one can compute that when randomly and uniformly selecting a sequence of birthdays, the expected number of people needed to first obtain a repeated birthday is also $O(\sqrt n)$. Let this number of people be $X$; then

$$
E(X) = \sum_{x=1}^{n+1}P(X\ge x+1) = \sum_{x=0}^n\frac{n!}{(n-x)!n^x} = \sqrt{\frac{\pi n}{2}}-\frac13+o(1).
$$

This inspires us that if we can randomly select a sequence of numbers, the expected sampling size needed for a repeated number to appear is also $O(\sqrt n)$.

### Finding a factor using the greatest common divisor

Actually constructing a sequence of random numbers modulo $p$ is not realistic, because $p$ is exactly what we need to find. So, we generate a pseudo-random number sequence $\{x_i\}$ via $f(x)=(x^2+c)\bmod N$: randomly take an $x_1$, let $x_2=f(x_1),\ x_3=f(x_2),\ \dots,\ x_i=f(x_{i-1})$, where $c\in[1,N)$ is a randomly chosen constant.

The function chosen here is easy to compute and can often generate a fairly random sequence. But it is not completely random. For example, let $n=50,\ c=6,\ x_1=1$; the data generated by $f(x)$ is

$$
1, 7, 5, 31, 17, 45, 31, 17, 45, 31,\dots
$$

We can find that the data cycles among $31,17,45$ after $x_4$. If we arrange these numbers as in the figure below, we find that this image closely resembles a $\rho$, and the algorithm is therefore named rho.

![pollard-rho](./images/pollard-rho.svg)

More importantly, such a function does indeed provide a self-map on $\mathbb Z_p$. That is, it satisfies the property: if $x\equiv y\pmod p$, then $f(x)\equiv f(y)\pmod p$.

???+ note "Proof"
    If $x\equiv y\pmod p$, then $x^2+c\equiv y^2+c\pmod p$. Note that $f(x)=x^2+c-k_xN$, where $k_x$ is an integer depending on $x$, and $p|N$, so $f(x)=x^2+c\pmod p$, hence $f(x)=f(y)\pmod p$.

As a sequence obtained by repeatedly iterating a pseudo-random self-map on $\mathbb Z_p$, $\{x_n\bmod p\}$ will have a repetition in $O(\sqrt p)$ expected time. As long as we observe such a repetition $x_i\equiv x_j\pmod p$, we can find a nontrivial factor of $N$ based on $\gcd(|x_i-x_j|,N)$. Note that since $p$ is unknown, we have no way to directly determine the occurrence of a repetition; a simple determination method is exactly that $\gcd(|x_i-x_j|,N)$ is strictly greater than one.

This algorithm does not always succeed, because $\gcd(|x_i-x_j|,N)$ may equal $N$. That is, $x_i\equiv x_j\pmod N$. In this case, when $\{x_n\bmod p\}$ first repeats, $\{x_n\}$ happens to repeat as well. We do not obtain a nontrivial factor. Moreover, once $\{x_n\}$ starts cycling, there is no point in continuing to iterate, because afterwards it will only repeat this cycle. The algorithm should output a decomposition failure, and we need to change the $c$ chosen in $f(x)$ and re-decompose.

According to the above analysis, in theory, any function $f(x)$ that satisfies $\forall x \equiv y \pmod p, f(x) \equiv f(y) \pmod p$ and can guarantee a certain pseudo-randomness (for example, certain polynomial functions) can be used here. In practice, we mainly use $f(x)=x^2+c\ (c\neq 0,-2)$.[^pseudo]

### Implementation

The algorithm we need to implement should be able to quickly determine during the iteration process whether $\{x_n\bmod p\}$ has already repeated. Viewing $f$ as edges on a directed graph with $\mathbb Z_p$ as vertices, what we actually need to implement is a cycle-detection algorithm. We only change the equality check to checking whether $\gcd(|x_i-x_j|,N)$ is greater than one.

#### Floyd cycle detection

Suppose two people are racing, A is fast, and B is slow; after a certain amount of time, A will definitely meet B, and when they meet, A's total distance minus B's total distance must be a multiple of the cycle length.

Let $a=f(0),b=f(f(0))$, and each time update $a=f(a),b=f(f(b))$; we only need to check during the update process whether $a$ and $b$ are equal, and if they are equal, then a cycle has appeared.

Each time we let $d=\gcd(|x_i-x_j|,N)$ and check whether $d$ satisfies $1< d< N$; if so, we can directly return $d$. If $d=N$, then $\{x_i\}$ has already formed a cycle, and we cannot continue operating once a cycle is formed, so we directly return $N$ itself, and in subsequent operations adjust the random constant $c$ and re-decompose.

??? note "Pollard-Rho algorithm based on Floyd cycle detection"
    === "C++"
        ```cpp
        ll Pollard_Rho(ll N) {
          if (N == 4) return 2;  // because we jump two steps at the start, we need to special-case 4
          ll c = rand() % (N - 1) + 1;
          ll t = f(0, c, N);
          ll r = f(f(0, c, N), c, N);
          while (t != r) {
            ll d = gcd(abs(t - r), N);
            if (d > 1) return d;
            t = f(t, c, N);
            r = f(f(r, c, N), c, N);
          }
          return N;
        }
        ```
    
    === "Python"
        ```python
        import random
        
        
        def Pollard_Rho(N):
            if N == 4:
                return 2  # because we jump two steps at the start, we need to special-case 4
            c = random.randint(1, N - 1)
            t = f(0, c, N)
            r = f(f(0, c, N), c, N)
            while t != r:
                d = gcd(abs(t - r), N)
                if d > 1:
                    return d
                t = f(t, c, N)
                r = f(f(r, c, N), c, N)
            return N
        ```

#### Brent cycle detection

In fact, the Floyd cycle-detection algorithm can be improved by a constant factor. Brent cycle detection starts from $k=1$ and increments $k$; in the $k$-th round, it keeps A in place and moves B forward $2^k$ steps, and if B meets A during the process, then a cycle has been found, otherwise it teleports A to B's position and continues to the next round.

It can be proven[^brent] that the number of calls to $f$ needed before obtaining a cycle this way is never greater than that of the Floyd cycle-detection algorithm. The tests in the original paper show that the average time needed for Brent cycle detection is reduced by $24\%$ compared with Floyd cycle detection.

#### Doubling optimization

Whether it is Floyd cycle detection or Brent cycle detection, the number of iterations is $O(\sqrt p)$. But using $\gcd$ to check for a cycle at each iteration slows down the algorithm's running speed. We can reduce the number of $\gcd$ computations through multiplicative accumulation.

Simply put, if $\gcd(a,N)>1$, then $\gcd(ab\bmod N,N)=\gcd(ab,N)>1$ holds for any $b\in\mathbb N_+$. That is, if we compute $\gcd(\prod |x_i-x_j| \bmod N,N)>1$, then there must be a pair $(x_i,x_j)$ among them satisfying $\gcd(|x_i-x_j|,N)>1$. If this product becomes zero at some moment, the decomposition fails, and we exit and return $N$ itself.

If we compute $\gcd$ once every $k$ pairs, then the algorithm complexity is reduced to $O(\sqrt p+k^{-1}\sqrt p\log N)$, where $\log N$ is the cost of a single $\gcd$ computation. Note that when $k$ and $\log N$ are roughly of the same order, we can obtain an $O(\sqrt p)$ expected complexity. In specific implementations, $k=128$ is mostly chosen.

Here we provide an implementation of the Pollard-Rho algorithm with Brent cycle detection plus the doubling optimization.

??? note "Implementation"
    === "C++"
        ```cpp
        ll Pollard_Rho(ll x) {
          ll t = 0;
          ll c = rand() % (x - 1) + 1;
          ll s = t;
          int step = 0, goal = 1;
          ll val = 1;
          for (goal = 1;; goal <<= 1, s = t, val = 1) {
            for (step = 1; step <= goal; ++step) {
              t = f(t, c, x);
              val = val * abs(t - s) % x;
              // if val is 0, exit and re-decompose
              if (!val) return x;
              if (step % 127 == 0) {
                ll d = gcd(val, x);
                if (d > 1) return d;
              }
            }
            ll d = gcd(val, x);
            if (d > 1) return d;
          }
        }
        ```
    
    === "Python"
        ```python
        from random import randint
        from math import gcd
        
        
        def Pollard_Rho(x):
            c = randint(1, x - 1)
            s = t = f(0, c, x)
            goal = val = 1
            while True:
                for step in range(1, goal + 1):
                    t = f(t, c, x)
                    val = val * abs(t - s) % x
                    if val == 0:
                        return x  # if val is 0, exit and re-decompose
                    if step % 127 == 0:
                        d = gcd(val, x)
                        if d > 1:
                            return d
                d = gcd(val, x)
                if d > 1:
                    return d
                s = t
                goal <<= 1
                val = 1
        ```

#### Complexity

The expected number of iterations in the Pollard-Rho algorithm is $O(\sqrt p)$, where $p$ is the smallest prime factor of $N$. In the specific implementation, whether Floyd cycle detection or Brent cycle detection is used, if the doubling optimization is not used, the expected complexity is $O(\sqrt p\log N)$; after adding the doubling optimization, we can approximately obtain an $O(\sqrt p)$ expected complexity.

It is worth mentioning that the earlier analysis is based on a completely random self-map function, but the Pollard-Rho algorithm actually uses a pseudo-random function, so this algorithm does not have a rigorous complexity analysis, and in practice it usually runs quite fast.

#### Example problem: finding the largest prime factor of a number

Example problem: [P4718【模板】Pollard-Rho 算法](https://www.luogu.com.cn/problem/P4718)

For a number $n$, use the [Miller-Rabin algorithm](./prime.md#millerrabin-素性测试) to determine whether it is prime; if it is, we can directly return, otherwise use the Pollard-Rho algorithm to find a factor $p$, and remove the factor $p$ from $n$. Then recursively decompose $n$ and $p$, use Miller-Rabin to determine whether a prime factor appears, and update with max\_factor to find the largest prime factor. Because this problem's data is too large, the Floyd cycle-detection method is not enough, and here we adopt the doubling optimization method.

??? note "Implementation"
    ```cpp
    --8<-- "docs/math/code/pollard-rho/pollard-rho_1.cpp"
    ```

## References and links

[^ref1]: <https://en.wikipedia.org/wiki/Birthday_problem#Reverse_problem>

[^pseudo]: Menezes, Alfred J.; van Oorschot, Paul C.; Vanstone, Scott A. (2001). Handbook of Applied Cryptography. Section 3.11 and 3.12.

[^brent]: Brent, R. P. (1980), An improved Monte Carlo factorization algorithm, BIT Numerical Mathematics, 20(2): 176–184, doi:10.1007/BF01933190
