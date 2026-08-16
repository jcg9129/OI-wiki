## Definition

The greatest common divisor, commonly abbreviated as gcd.

A common divisor of a group of integers is a number that is simultaneously a divisor of every number in the group. $\pm 1$ is a common divisor of any group of integers.

The greatest common divisor of a group of integers is the largest one among all common divisors.

For integers $a,b$ not both $0$, their greatest common divisor is denoted $\gcd(a,b)$, and when there is no ambiguity it can be abbreviated as $(a,b)$.

For integers $a_1,\dots,a_n$ not all $0$, their greatest common divisor is denoted $\gcd(a_1,\dots,a_n)$, and when there is no ambiguity it can be abbreviated as $(a_1,\dots,a_n)$.

For the properties of the greatest common divisor and least common multiple, see [number theory basics](./basic.md#greatest-common-divisor-and-least-common-multiple).

So how do we find the greatest common divisor? We first consider the case of two numbers.

### Euclidean algorithm

#### Process

If we already know two numbers $a$ and $b$, how do we find their greatest common divisor?

Without loss of generality, suppose $a > b$.

We observe that if $b$ is a divisor of $a$, then $b$ is the greatest common divisor of the two.
Below we discuss the case where it does not divide evenly, i.e. $a = b \times q + r$, where $r < b$.

Through a proof we can obtain $\gcd(a,b)=\gcd(b,a \bmod b)$, as follows:

???+ note "Proof"
    Let $a=bk+c$; obviously $c=a \bmod b$. Let $d \mid a,~d \mid b$; then $c=a-bk, \frac{c}{d}=\frac{a}{d}-\frac{b}{d}k$.
    
    From the equation on the right, we can see that $\frac{c}{d}$ is an integer, i.e. $d \mid c$. So a common divisor of $a,b$ is also a common divisor of $b,a \bmod b$.
    
    We also need to prove the converse:
    
    Let $d \mid b,~d\mid (a \bmod b)$; as before, we can obtain the following equation $\frac{a\bmod b}{d}=\frac{a}{d}-\frac{b}{d}k,~\frac{a\bmod b}{d}+\frac{b}{d}k=\frac{a}{d}$.
    
    Because the equation on the left is obviously an integer, $\frac{a}{d}$ is also an integer, i.e. $d \mid a$. So a common divisor of $b,a\bmod b$ is also a common divisor of $a,b$.
    
    Since the common divisors of the two expressions are the same, the greatest common divisor is also the same.
    
    So we obtain the equation $\gcd(a,b)=\gcd(b,a\bmod b)$.

Since we have obtained $\gcd(a, b) = \gcd(b, r)$, and here the sizes of the two numbers do not increase, we have thus obtained a recursive method for the greatest common divisor of two numbers.

#### Implementation

=== "C++"
    ```cpp
    // Version 1
    int gcd(int a, int b) {
      if (b == 0) return a;
      return gcd(b, a % b);
    }
    
    // Version 2
    int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
    ```

=== "Java"
    ```java
    // Version 1
    public int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
    
    // Version 2
    public int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
    ```

=== "Python"
    ```python
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    ```

We just recurse until the case `b == 0` (i.e. `a % b == 0` at the previous step) and then return the value.

Based on the above recursive method, we can also write an iterative method:

=== "C++"
    ```cpp
    int gcd(int a, int b) {
      while (b != 0) {
        int tmp = a;
        a = b;
        b = tmp % b;
      }
      return a;
    }
    ```

=== "Java"
    ```java
    public int gcd(int a, int b) {
        while(b != 0) {
            int tmp = a;
            a = b;
            b = tmp % b;
        }
        return a;
    }
    ```

=== "Python"
    ```python
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    ```

The above algorithms can all be called the Euclidean algorithm.

Additionally, for C++17, we can use [`std::gcd`](https://en.cppreference.com/w/cpp/numeric/gcd) and [`std::lcm`](https://en.cppreference.com/w/cpp/numeric/lcm) in the [`<numeric>`](https://en.cppreference.com/w/cpp/header/numeric) header to find the greatest common divisor and least common multiple.

???+ warning "Note"
    In some compilers, in C++14 one can use the `std::__gcd(a,b)` function to find the greatest common divisor, but it serves only as a private helper function for `std::rotate`.[^1] Using this function may lead to unexpected problems, so it is generally not recommended.

If two numbers $a$ and $b$ satisfy $\gcd(a, b) = 1$, we say $a$ and $b$ are coprime.

#### Properties

What is the time efficiency of the Euclidean algorithm? Below we prove that when the input is two binary integers of length $n$, the time complexity of the Euclidean algorithm is $O(n)$. (In other words, in the default case where $a, b$ are of the same order, the time complexity is $O(\log\max(a, b))$.)

???+ note "Proof"
    When we find $\gcd(a,b)$, we encounter two cases:
    
    -   $a < b$, in which case $\gcd(a,b)=\gcd(b,a)$;
    -   $a \geq b$, in which case $\gcd(a,b)=\gcd(b,a \bmod b)$, and taking $a$ modulo will at least halve $a$. This means this process occurs at most $O(\log a) = O(n)$ times.
    
    After the first case occurs, the second case must occur; therefore the number of occurrences of the first case is definitely **no more than** the number of occurrences of the second case.
    
    Thus we recurse at most $O(n)$ times to obtain the result.

In fact, if we try to use the Euclidean algorithm to find the greatest common divisor of two adjacent terms of the [Fibonacci sequence](../combinatorics/fibonacci.md), it will make the algorithm reach its worst-case complexity.

### Subtraction-based Euclidean algorithm

Taking the modulus of large integers has a relatively high time complexity, while addition and subtraction have a low time complexity. For large integers, we can use addition and subtraction instead of multiplication and division to find the greatest common divisor.

#### Process

Given two numbers $a$ and $b$, find $\gcd(a,b)$.

Without loss of generality, suppose $a \ge b$. If $a = b$, then $\gcd(a,b)=a=b$.
Otherwise, $\forall d\mid a, d\mid b$, one can prove that $d\mid a-b$.

Therefore, **all** common factors of $a$ and $b$ are common factors of $a-b$ and $b$, so $\gcd(a,b) = \gcd(a-b, b)$.

#### Optimization by Stein's algorithm

If $a\gg b$, the $O(n)$ complexity of the subtraction-based algorithm will reach the worst case.

Consider an optimization: if $2\mid a,2\mid b$, then $\gcd(a,b) = 2\gcd\left(\dfrac a2, \dfrac b2\right)$.

Otherwise, if $2\mid a$ (the case $2\mid b$ is analogous), because the case $2\mid b$ has already been discussed, we have $2 \nmid b$. Therefore $\gcd(a,b)=\gcd\left(\dfrac a2,b\right)$.

The optimized algorithm (i.e. Stein's algorithm) has a time complexity of $O(\log n)$.

???+ note "Proof"
    If $2\mid a$ or $2\mid b$, each recursion at least halves one of $a,b$.
    
    Otherwise, $2\mid a-b$, returning to the previous case.
    
    The algorithm recurses at most $O(\log n)$ times.

#### Implementation

For the high-precision template, see [high-precision computation](../bignum.md).

High-precision computation needs to implement: subtraction, size comparison, left shift, right shift (which can be replaced by low-precision multiplication and division), and the number of trailing $0$s in binary (which can be computed brute-force by checking parity).

??? note "C++"
    ```cpp
    Big gcd(Big a, Big b) {
      if (a == 0) return b;
      if (b == 0) return a;
      // record the number of occurrences of the common factor 2 in a and b;
      // countr_zero denotes the number of trailing 0s in binary
      int atimes = countr_zero(a);
      int btimes = countr_zero(b);
      int mintimes = min(atimes, btimes);
      a >>= atimes;
      for (;;) {
        // the factor 2 among the common factors of a and b has already been counted;
        // afterwards a cannot possibly be even
        b >>= btimes;
        // ensure a<=b
        if (a > b) swap(a, b);
        b -= a;
        if (b == 0) break;
        btimes = countr_zero(b);
      }
      return a << mintimes;
    }
    ```

The above code references the implementations of C++17 `std::gcd` in [libstdc++](https://github.com/gcc-mirror/gcc/blob/1667962ae755db27965778b8c8c684c6c0c4da21/libstdc%2B%2B-v3/include/std/numeric#L173) and [MSVC](https://github.com/microsoft/STL/blob/9aca22477df4eed3222b4974746ee79129eb44e7/stl/inc/numeric#L591). In the data ranges of `unsigned int` and `unsigned long long`, if `countr_zero` can be computed extremely fast, then Stein's algorithm is faster than the Euclidean algorithm, but otherwise it may be slower than the Euclidean algorithm.

???+ note "About countr_zero"
    1.  gcc has the [built-in functions](../bit.md#gcc-built-in-functions) `__builtin_ctz` (32-bit) or `__builtin_ctzll` (64-bit) that can replace the `countr_zero` in the above code;
    2.  Starting from C++20, the header `<bit>` includes [`std::countr_zero`](https://en.cppreference.com/w/cpp/numeric/countr_zero);
    3.  If one does not use functions outside the standard library and cannot use the C++20 standard, the following code is an $O(1)$ implementation after preprocessing under the Word-RAM with multiplication model:
    
    ```cpp
    constexpr int loghash[64] = {0,  32, 48, 56, 60, 62, 63, 31, 47, 55, 59, 61, 30,
                                 15, 39, 51, 57, 28, 46, 23, 43, 53, 58, 29, 14, 7,
                                 35, 49, 24, 44, 54, 27, 45, 22, 11, 37, 50, 25, 12,
                                 38, 19, 41, 52, 26, 13, 6,  3,  33, 16, 40, 20, 42,
                                 21, 10, 5,  34, 17, 8,  36, 18, 9,  4,  2,  1};
    
    int countr_zero(unsigned long long x) {
      return loghash[(x & -x) * 0x9150D32D8EB9EFC0Ui64 >> 58];
    }
    ```
    
    As for high-precision computation, if the implementation is similar to `bitset`, then combined with the above implementation of `countr_zero` it can be done with time complexity `O(n / w)`. But if it is inconvenient to split by binary bit, then one can only brute-force determine the largest power-of-$2$ factor, and the time complexity depends on the implementation. For example:
    
    ```cpp
    // a binary Big implemented in little-endian order, requiring the ability to enumerate each element
    int countr_zero(Big a) {
      int ans = 0;
      for (auto x : a) {
        if (x != 0) {
          ans += 32;  // the bit length of each data type element
        } else {
          return ans + countr_zero(x);
        }
      }
      return ans;
    }
    
    // brute-force computation; if you need to use it, it is recommended to write it
    // directly into gcd to speed up the constant factor
    int countr_zero(Big a) {
      int ans = 0;
      while ((a & 1) == 0) {
        a >>= 1;
        ++ans;
      }
      return ans;
    }
    ```

For more discussion on the speed of `gcd` implementations, one can read [Fastest way to compute the greatest common divisor](https://lemire.me/blog/2013/12/26/fastest-way-to-compute-the-greatest-common-divisor/).

### Greatest common divisor of multiple numbers

So how do we find the greatest common divisor of multiple numbers? Obviously the answer must be a divisor of each number, so it must also be a divisor of every two adjacent numbers. We use induction, and can prove that each time we take out two numbers, find their answer, and put it back, it does not affect the required answer.

## Least common multiple

Next we introduce how to find the least common multiple (LCM).

### Definition

A common multiple of a group of integers is a number that is simultaneously a multiple of every number in the group. $0$ is a common multiple of any group of integers.

The least common multiple of a group of integers is the smallest one among all positive common multiples.

For integers $a,b$, their least common multiple is denoted $\operatorname{lcm}(a,b)$, and when there is no ambiguity it can be abbreviated as $[a,b]$.

For integers $a_1,\dots,a_n$, their least common multiple is denoted $\operatorname{lcm}(a_1,\dots,a_n)$, and when there is no ambiguity it can be abbreviated as $[a_1,\dots,a_n]$.

### Two numbers

Let $a = p_1^{k_{a_1}}p_2^{k_{a_2}} \cdots p_s^{k_{a_s}}$, $b = p_1^{k_{b_1}}p_2^{k_{b_2}} \cdots p_s^{k_{b_s}}$

We observe that for $a$ and $b$, their greatest common divisor equals

$p_1^{\min(k_{a_1}, k_{b_1})}p_2^{\min(k_{a_2}, k_{b_2})} \cdots p_s^{\min(k_{a_s}, k_{b_s})}$

and their least common multiple equals

$p_1^{\max(k_{a_1}, k_{b_1})}p_2^{\max(k_{a_2}, k_{b_2})} \cdots p_s^{\max(k_{a_s}, k_{b_s})}$

Since $k_a + k_b = \max(k_a, k_b) + \min(k_a, k_b)$

we obtain the conclusion $\gcd(a, b) \times \operatorname{lcm}(a, b) = a \times b$

To find the least common multiple of two numbers, one just needs to first find the greatest common divisor.

### Multiple numbers

We can observe that once we have found the $\gcd$ of two numbers, finding the least common multiple has $O(1)$ complexity. So for multiple numbers, there is actually no need to find a common greatest common divisor before processing. The most direct method is: once we compute the $\gcd$ of two numbers—perhaps while finding the $\gcd$ of multiple numbers, we put it into the sequence to continue solving with the following numbers—so we can simply transform, and directly put the least common multiple into the sequence.

## Extended Euclidean algorithm

The extended Euclidean algorithm (EXGCD) is commonly used to find a feasible solution of $ax+by=\gcd(a,b)$.

### Process

Let

$ax_1+by_1=\gcd(a,b)$

$bx_2+(a\bmod b)y_2=\gcd(b,a\bmod b)$

By the Euclidean theorem: $\gcd(a,b)=\gcd(b,a\bmod b)$

So $ax_1+by_1=bx_2+(a\bmod b)y_2$

And because $a\bmod b=a-(\lfloor\frac{a}{b}\rfloor\times b)$

So $ax_1+by_1=bx_2+(a-(\lfloor\frac{a}{b}\rfloor\times b))y_2$

$ax_1+by_1=ay_2+bx_2-\lfloor\frac{a}{b}\rfloor\times by_2=ay_2+b(x_2-\lfloor\frac{a}{b}\rfloor y_2)$

Because $a=a,b=b$, we have $x_1=y_2,y_1=x_2-\lfloor\frac{a}{b}\rfloor y_2$

Continuously substitute $x_2,y_2$ and recurse until $b$ is $0$, where the recursion returns $x=1,y=0$ to solve back up.

### Implementation

=== "C++"
    ```cpp
    int Exgcd(int a, int b, int &x, int &y) {
      if (!b) {
        x = 1;
        y = 0;
        return a;
      }
      int d = Exgcd(b, a % b, x, y);
      int t = x;
      x = y;
      y = t - (a / b) * y;
      return d;
    }
    ```

=== "Python"
    ```python
    def Exgcd(a, b):
        if b == 0:
            return a, 1, 0
        d, x, y = Exgcd(b, a % b)
        return d, y, x - (a // b) * y
    ```

The value returned by the function is $\gcd$; during this process we just compute $x,y$.

### Range analysis

The equation $ax+by=\gcd(a,b)$ has infinitely many solutions, and obviously some of them will overflow long long.  
Fortunately, if $b\not= 0$, the feasible solution found by the extended Euclidean algorithm must satisfy $|x|\le b,|y|\le a$.  
Below we give a proof of this property.

??? note "Proof"
    -   When $\gcd(a,b)=b$, $a\bmod b=0$, and the recursion must terminate at the next level.  
        We obtain $x_1=0,y_1=1$; obviously $a,b\ge 1\ge |x_1|,|y_1|$.
    -   When $\gcd(a,b)\not= b$, suppose $|x_2|\le (a\bmod b),|y_2|\le b$.  
        Because $x_1=y_2,y_1=x_2-{\left\lfloor\dfrac{a}{b}\right\rfloor}y_2$   
        we have $|x_1|=|y_2|\le b,|y_1|\le|x_2|+|{\left\lfloor\dfrac{a}{b}\right\rfloor}y_2|\le (a\bmod b)+{\left\lfloor\dfrac{a}{b}\right\rfloor}|y_2|$  
        $\le a-{\left\lfloor\dfrac{a}{b}\right\rfloor}b+{\left\lfloor\dfrac{a}{b}\right\rfloor}|y_2|\le a-{\left\lfloor\dfrac{a}{b}\right\rfloor}(b-|y_2|)$   
        $a\bmod b=a-{\left\lfloor\dfrac{a}{b}\right\rfloor}b\le a-{\left\lfloor\dfrac{a}{b}\right\rfloor}(b-|y_2|)\le a$   
        Therefore $|x_1|\le b,|y_1|\le a$ holds.

### Writing the extended Euclidean algorithm iteratively

First, when $x = 1$, $y = 0$, $x_1 = 0$, $y_1 = 1$, obviously we have:

$$
\begin{cases}
    ax + by     & = a \\
    ax_1 + by_1 & = b
\end{cases}
$$

holds.

Knowing $a\bmod b = a - (\lfloor \frac{a}{b} \rfloor \times b)$, below let $q = \lfloor \frac{a}{b} \rfloor$. Referring to the iterative method for finding gcd, each round of the iteration process can be expressed as:

$$
(a, b) \rightarrow (b, a - qb)
$$

Replacing $a$ in the iteration process with $ax + by = a$, and $b$ with $ax_1 + by_1 = b$, we obtain:

$$
\begin{aligned}
                & \begin{cases}
                      ax + by     & = a \\
                      ax_1 + by_1 & = b
                  \end{cases}                    \\
    \rightarrow & \begin{cases}
                      ax_1 + by_1               & = b      \\
                      a(x - qx_1) + b(y - qy_1) & = a - qb
                  \end{cases}
\end{aligned}
$$

From this we obtain the iterative method for exgcd.

Because the iterative method avoids recursion, the code will run a bit faster than the recursive code.

```cpp
int gcd(int a, int b, int& x, int& y) {
  x = 1, y = 0;
  int x1 = 0, y1 = 1, a1 = a, b1 = b;
  while (b1) {
    int q = a1 / b1;
    tie(x, x1) = make_tuple(x1, x - q * x1);
    tie(y, y1) = make_tuple(y1, y - q * y1);
    tie(a1, b1) = make_tuple(b1, a1 - q * b1);
  }
  return a1;
}
```

If you carefully observe $a_1$ and $b_1$, you will find that they take exactly the same values as in the iterative version of the Euclidean algorithm, and the following formulas hold at all times (before the while loop and at the end of each iteration): $x \cdot a +y \cdot b =a_1$ and $x_1 \cdot a +y_1 \cdot b= b_1$. Therefore, this algorithm certainly computes $\gcd$ correctly.

Finally we know that $a_1$ is the required $\gcd$, and we have $x \cdot a +y \cdot b = g$.

#### Matrix interpretation

For positive integers $a$ and $b$, one step of the Euclidean division, i.e. $\gcd(a,b)=\gcd(b,a\bmod b)$, is represented using matrices as

$$
\begin{bmatrix}
b\\a\bmod b
\end{bmatrix}
=
\begin{bmatrix}
0&1\\1&-\lfloor a/b\rfloor
\end{bmatrix}
\begin{bmatrix}
a\\b
\end{bmatrix}
$$

where the floor symbol $\lfloor c\rfloor$ denotes the largest integer not greater than $c$. We define the transformation $\begin{bmatrix}a\\b\end{bmatrix}\mapsto \begin{bmatrix}0&1\\1&-\lfloor a/b\rfloor\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}$.

It is easy to see that the Euclidean algorithm is just the repeated application of this transformation, giving

$$
\begin{bmatrix}
\gcd(a,b)\\0
\end{bmatrix}
=
\left(
\cdots 
\begin{bmatrix}
0&1\\1&-\lfloor a/b\rfloor
\end{bmatrix}
\begin{bmatrix}
1&0\\0&1
\end{bmatrix}
\right)
\begin{bmatrix}
a\\b
\end{bmatrix}
$$

Let

$$
\begin{bmatrix}
x_1&x_2\\x_3&x_4
\end{bmatrix}
=
\cdots 
\begin{bmatrix}
0&1\\1&-\lfloor a/b\rfloor
\end{bmatrix}
\begin{bmatrix}
1&0\\0&1
\end{bmatrix}
$$

then

$$
\begin{bmatrix}
\gcd(a,b)\\0
\end{bmatrix}
=
\begin{bmatrix}
x_1&x_2\\x_3&x_4
\end{bmatrix}
\begin{bmatrix}
a\\b
\end{bmatrix}
$$

satisfies $a\cdot x_1+b\cdot x_2=\gcd(a,b)$, which is the extended Euclidean algorithm. Note that multiplying by an identity matrix at the end does not affect the result, which hints that we can maintain a $2\times 2$ identity matrix at the start to write a more concise iterative method, such as

```cpp
int exgcd(int a, int b, int &x, int &y) {
  int x1 = 1, x2 = 0, x3 = 0, x4 = 1;
  while (b != 0) {
    int c = a / b;
    std::tie(x1, x2, x3, x4, a, b) =
        std::make_tuple(x3, x4, x1 - x3 * c, x2 - x4 * c, b, a - b * c);
  }
  x = x1, y = x2;
  return a;
}
```

This formulation is simpler compared to recursion.

## Applications

-   [10104 - Euclid Problem](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1045)
-   [GYM - (J) once upon a time](http://codeforces.com/gym/100963)
-   [UVa - 12775 - Gift Dilemma](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4628)

## References and links

[^1]: [libstdc++: std Namespace Reference](https://gcc.gnu.org/onlinedocs/libstdc++/libstdc++-html-USERS-4.4/a00978.html#a2686a128df5a576cb53a1ed5f674607)
