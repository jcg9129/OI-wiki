author: i-Yirannn, Xeonacid, ouuan

## Introduction

`std::bitset` is a size-immutable container in the standard library that stores `0/1`. Strictly speaking, it does not belong to the STL.

??? note "bitset and STL"
    > The C++ standard library provides some special container classes, the so-called container adapters (stack, queue, priority queue). In addition, a few classes provide a container-like interface (for example, strings, bitsets, and valarrays). All these classes are covered separately.1 Container adapters and bitsets are covered in Chapter 12.
    >
    > The C++ standard library provides not only the containers for the STL framework but also some containers that fit some special needs and provide simple, almost self-explanatory, interfaces. You can group these containers into either the so-called container adapters, which adapt standard STL containers to fit special needs, or a bitset, which is a containers for bits or Boolean values. There are three standard container adapters: stacks, queues, and priority queues. In priority queues, the elements are sorted automatically according to a sorting criterion. Thus, the "next" element of a priority queue is the element with the "highest" value. A bitset is a bitfield with an arbitrary but fixed number of bits. Note that the C++ standard library also provides a special container with a variable size for Boolean values: vector.
    
    ——Excerpted from 《The C++ Standard Library 2nd Edition》
    
    From this, it seems that `bitset` does not belong to STL, but is a "Special Container" in the standard library. In fact, as a container, it does not satisfy the requirements of STL containers. Saying it is an adapter, it also does not depend on other STL containers as the underlying implementation.

Since memory addresses are addressed by byte, i.e. `byte`, rather than bit, i.e. `bit`, a variable of type `bool`, although it can only represent `0/1`, also occupies 1 byte of memory.

`bitset` uses a fixed optimization so that the eight bits of one byte can respectively store 8 bits of `0/1`.

For a 4-byte `int` variable, in the sense of only storing `0/1`, `bitset` occupies only $\frac{1}{32}$ of its space, and when computing some information, the time required is also $\frac 1{32}$ of it.

In some cases, `bitset` can optimize the running efficiency of a program. As for whether what it optimizes is complexity or the constant factor, it depends on the angle of computing complexity. Generally the complexity of `bitset` has the following notations: (let the original complexity be $O(n)$)

1.  $O(n)$, this notation considers that `bitset` completely does not optimize complexity.
2.  $O(\frac n{32})$, this notation is not very rigorous (a constant should not appear in the complexity), but it reflects that `bitset` can optimize the required time to $\frac 1{32}$.
3.  $O(\frac n w)$, where $w=32$ (the number of bits of the computer), this notation is relatively widely accepted.
4.  $O(\frac n {\log w})$, where $w$ is the size of an integer variable of the computer.

In addition, a specialization of `vector`, `vector<bool>`, has the same storage way as `bitset`, the difference being that it supports dynamically opening space, while `bitset`, like our general static array, is opened at compile time. However, `bitset` has some useful library functions, which are not only convenient, but can sometimes achieve SIMD and thereby reduce the constant factor. In addition, some behaviors of `vector<bool>` are inconsistent with `vector` (for example, for `std::vector<bool> vec`, `&vec[0] + i` is not equal to `&vec[i]`). Therefore, `vector<bool>` is generally not used.

## Usage

See [std::bitset - cppreference.com](https://en.cppreference.com/w/cpp/utility/bitset).

### Header file

```cpp
#include <bitset>
```

### Specifying the size

```cpp
std::bitset<1000> bs;  // a bitset with 1000 bits
```

### Constructors

-   `bitset()`: every bit is `false`.
-   `bitset(unsigned long val)`: set to the binary form of `val`.
-   `bitset(const string& str)`: set to the $01$ string `str`.

### Operators

-   `operator []`: access a specific bit of it.

-   `operator ==`/`operator !=`: compare whether the contents of two `bitset`s are completely the same.

-   `operator &`/`operator &=`/`operator |`/`operator |=`/`operator ^`/`operator ^=`/`operator ~`: perform bitwise and/or/xor/negation operations.

    Note: **`bitset` can only perform bit operations with `bitset`**; to perform bit operations with an integer, we must first convert the integer to a `bitset`.

-   `operator <<`/`operator >>`/`operator <<=`/`operator >>=`: perform binary left shift/right shift.

In addition, `bitset` also provides support for C++ stream IO, which means you can perform input/output through `cin/cout`.

### Member functions

-   `count()`: return the number of `true`.
-   `size()`: return the size of the `bitset`.
-   `test(pos)`: it has the same effect as `at()` in `vector`; the difference from the `[]` operator is the out-of-bounds check.
-   `any()`: return `true` if some bit is `true`, otherwise return `false`.
-   `none()`: return `true` if all bits are `false`, otherwise return `false`.
-   `all()`: return `true` if all bits are `true`, otherwise return `false`.
-   1.  `set()`: set the entire `bitset` to `true`.
    2.  `set(pos, val = true)`: set a certain bit to `true`/`false`.
-   1.  `reset()`: set the entire `bitset` to `false`.
    2.  `reset(pos)`: set a certain bit to `false`. Equivalent to `set(pos, false)`.
-   1.  `flip()`: flip every bit. ($0\leftrightarrow1$, equivalent to xor with a `bitset` that is all $1$)
    2.  `flip(pos)`: flip a certain bit.
-   `to_string()`: return the converted string representation.
-   `to_ulong()`: return the converted `unsigned long` representation (`long` is the same as `int` on NT and 32-bit POSIX systems, and the same as `long long` on 64-bit POSIX).
-   `to_ullong()`: (starting from **C++11**) return the converted `unsigned long long` representation.

In addition, libstdc++ has some relatively practical internal member functions[^bitset1]:

-   `_Find_first()`: return the subscript of the first `true` of the `bitset`; if there is no `true`, return the size of the `bitset`.
-   `_Find_next(pos)`: return the subscript of the first `true` after `pos` (positions with subscript strictly greater than `pos`); if there is no `true` after `pos`, return the size of the `bitset`.

## Applications

### [「LibreOJ β Round #2」Greedy can only pass the sample](https://loj.ac/problem/515)

This problem can be done with dp; the transition equation is very simple:

$f(i,j)$ denotes whether the sum of squares of the first $i$ numbers can be $j$; then $f(i,j)=\bigvee\limits_{k=a}^bf(i-1,j-k^2)$ (ored together).

But if done directly it is $O(n^5)$, which (seemingly) cannot pass.

We find that it can be optimized with `bitset`; just left shift and then or them together:

??? note "Submission record: [std::bitset](https://loj.ac/submission/395274)"
    ```cpp
    #include <bitset>
    #include <cstdio>
    #include <iostream>
    
    using namespace std;
    
    constexpr int N = 101;
    
    int n, a[N], b[N];
    bitset<N * N * N> f[N];
    
    int main() {
      int i, j;
    
      cin >> n;
    
      for (i = 1; i <= n; ++i) cin >> a[i] >> b[i];
    
      f[0][0] = 1;
    
      for (i = 1; i <= n; ++i) {
        for (j = a[i]; j <= b[i]; ++j) {
          f[i] |= (f[i - 1] << (j * j));
        }
      }
    
      cout << f[n].count();
    
      return 0;
    }
    ```

Since the implementation of libstdc++ packs `__CHAR_BIT__ * sizeof(unsigned long)` bits[^bitset2], which is $32$ on some platforms. So, we can hand-write a `bitset` (only needing to support the single operation of oring after left-shifting) that packs $64$ bits (`__CHAR_BIT__ * sizeof(unsigned long long)`) to further optimize:

??? note "Submission record: [hand-written bitset](https://loj.ac/submission/395619)"
    ```cpp
    #include <cstdio>
    #include <iostream>
    
    using namespace std;
    
    constexpr int N = 101;
    constexpr int W = 64;
    
    struct Bitset {
      unsigned long long a[N * N * N >> 6];
    
      void shiftor(const Bitset &y, int p, int l, int r) {
        int t = p - p / W * W;
        int tt = (t == 0 ? 0 : W - t);
        int to = (r + p) / W;
        int qaq = (p + W - 1) / W;
    
        for (int i = (l + p) / W; i <= to; ++i) {
          if (i - qaq >= 0) a[i] |= y.a[i - qaq] >> tt;
    
          a[i] |= ((y.a[i - qaq + 1] & ((1ull << tt) - 1)) << t);
        }
      }
    } f[N];
    
    int main() {
      int n, a, b, l = 0, r = 0, ans = 0;
    
      scanf("%d", &n);
    
      f[0].a[0] = 1;
    
      for (int i = 1; i <= n; ++i) {
        scanf("%d%d", &a, &b);
    
        for (int j = a; j <= b; ++j) f[i].shiftor(f[i - 1], j * j, l, r);
    
        l += a * a;
        r += b * b;
      }
    
      for (int i = l / W; i <= r / W; ++i)
        ans += __builtin_popcount(f[n].a[i] & 0xffffffffu) +
               __builtin_popcount(f[n].a[i] >> 32);
    
      printf("%d", ans);
    
      return 0;
    }
    ```

In addition, brute force with a few pruning added can also pass:

??? note "Submission record: [brute force with a few pruning added](https://loj.ac/submission/395673)"
    ```cpp
    #include <cstdio>
    #include <iostream>
    
    using namespace std;
    
    constexpr int N = 101;
    constexpr int W = 64;
    
    bool f[N * N * N];
    
    int main() {
      int n, i, j, k, a, b, l = 0, r = 0, ans = 0;
    
      scanf("%d", &n);
    
      f[0] = true;
    
      for (i = 1; i <= n; ++i) {
        scanf("%d%d", &a, &b);
        l += a * a;
        r += b * b;
    
        for (j = r; j >= l; --j) {
          f[j] = false;
    
          for (k = a; k <= b; ++k) {
            if (j - k * k < l - a * a) break;
    
            if (f[j - k * k]) {
              f[j] = true;
              break;
            }
          }
        }
      }
    
      for (i = l; i <= r; ++i) ans += f[i];
    
      printf("%d", ans);
    
      return 0;
    }
    ```

### [CF1097F Alex and a TV Show](https://codeforces.com/contest/1097/problem/F)

#### Problem statement

Given $n$ multisets, four operations:

1.  Set a certain multiset to a number.
2.  Set a certain multiset to the addition of two other multisets.
3.  Set a certain multiset to the $\gcd$ of one number chosen from each of two other multisets. That is: $A=\{\gcd(x,y)|x\in B,y\in C\}$.
4.  Query the count of a certain number in a certain multiset, **in the sense of modulo 2**.

The number of multisets is $10^5$, the number of operations is $10^6$, and the value range is $7000$.

#### Approach

Seeing "in the sense of modulo $2$", we can think of using `bitset` to maintain each multiset.

In this way, operation $1$ directly sets, operation $2$ is xor (because of modulo $2$), operation $4$ is a direct query, but.. what about operation $3$?

We can try to maintain the multiset formed by all the divisors of each multiset; in this way, operation $3$ is a direct bitwise and.

We can preprocess the `bitset` formed by the divisors of each number within the value range, so that operation $1$ is solved. Operation $2$ is still xor.

The problem now is how to obtain the count of a certain number in a multiset through the multiset formed by the divisors of that multiset.

Let the original multiset be $A$, and the multiset formed by its divisors be $A'$; we want to find the count of $x$ in $A$; deduce it a bit using [Möbius inversion](../../math/number-theory/mobius.md):

$$
\begin{aligned}&\sum\limits_{i\in A}[\frac i x=1]\\=&\sum\limits_{i\in A}\sum\limits_{d|\frac i x}\mu(d)\\=&\sum\limits_{d\in A',x|d}\mu(\frac d x)\end{aligned}
$$

Since it is in the sense of modulo $2$, $-1$ and $1$ are the same, so we only need to look at whether $\frac d x$ has a square factor. So, we can preprocess for each number within the value range the `bitset` formed by the positions among its multiples that, when divided by it, are square-free; when finding the answer, first bitwise-and and then `count()`.

In this way, the complexity of a single query is $O(\frac v w)$ ($v=7000,\,w=32$).

As for the preprocessing part, $O(v\sqrt v)$ or $O(v^2)$ preprocessing is relatively simple; the $\log$ preprocessing is as shown in the code below, with complexity being the harmonic series, so it is $O(v\log v)$.

??? note "Reference code"
    ```cpp
    #include <bitset>
    #include <cctype>
    #include <cmath>
    #include <cstdio>
    #include <iostream>
    
    using namespace std;
    
    int read() {
      int out = 0;
      char c;
      while (!isdigit(c = getchar()));
      for (; isdigit(c); c = getchar()) out = out * 10 + c - '0';
      return out;
    }
    
    constexpr int N = 100005;
    constexpr int M = 1000005;
    constexpr int V = 7005;
    
    bitset<V> pre[V], pre2[V], a[N], mu;
    int n, m, tot;
    char ans[M];
    
    int main() {
      int i, j, x, y, z;
    
      n = read();
      m = read();
    
      mu.set();
      for (i = 2; i * i < V; ++i) {
        for (j = 1; i * i * j < V; ++j) {
          mu[i * i * j] = 0;
        }
      }
      for (i = 1; i < V; ++i) {
        for (j = 1; i * j < V; ++j) {
          pre[i * j][i] = 1;
          pre2[i][i * j] = mu[j];
        }
      }
    
      while (m--) {
        switch (read()) {
          case 1:
            x = read();
            y = read();
            a[x] = pre[y];
            break;
          case 2:
            x = read();
            y = read();
            z = read();
            a[x] = a[y] ^ a[z];
            break;
          case 3:
            x = read();
            y = read();
            z = read();
            a[x] = a[y] & a[z];
            break;
          case 4:
            x = read();
            y = read();
            ans[tot++] = ((a[x] & pre2[y]).count() & 1) + '0';
            break;
        }
      }
    
      printf("%s", ans);
    
      return 0;
    }
    ```

### Combined with the Sieve of Eratosthenes

Due to the fast contiguous read/write efficiency of `bitset`, it is very suitable for making a prime table combined with the [Sieve of Eratosthenes](../../math/number-theory/sieve.md#埃拉托斯特尼筛法).

The way to use it is also very simple; we only need to replace the boolean array in the Sieve of Eratosthenes with a `bitset`.

??? note "Speed test"
    Using [Quick C++ Benchmarks](https://quick-bench.com) for testing, the compiler is `GCC 13.2`, and the compilation parameters are `-std=c++20 -O2`.
    
    | Algorithm | Function name |
    | ----------------------------- | ------------------------ |
    | Sieve of Eratosthenes + C-style boolean array, not storing the sieved-out primes | `Eratosthenes_CArray` |
    | Sieve of Eratosthenes + `vector<bool>`, not storing the sieved-out primes | `Eratosthenes_vector` |
    | Sieve of Eratosthenes + `bitset`, not storing the sieved-out primes | `Eratosthenes_bitset` |
    | Sieve of Eratosthenes + C-style boolean array, storing the sieved-out primes | `Eratosthenes_CArray_sp` |
    | Sieve of Eratosthenes + `vector<bool>`, storing the sieved-out primes | `Eratosthenes_vector_sp` |
    | Sieve of Eratosthenes + `bitset`, storing the sieved-out primes | `Eratosthenes_bitset_sp` |
    | Euler sieve + C-style boolean array | `Euler_CArray` |
    | Euler sieve + `vector<bool>` | `Euler_vector` |
    | Euler sieve + `bitset` | `Euler_bitset` |
    
    -   When the Sieve of Eratosthenes **stores** the sieved-out primes:
    
        -   The [test result](https://quick-bench.com/q/iQL9FhsZ6PVV81HKABsidRw8hB8) when $N=5 \times 10^7 + 1$:
    
            ![](./images/bitset-5e7sp.png)
        -   The [test result](https://quick-bench.com/q/pwEamEFUW-6nXeXEALRsYPd8FWI) when $N=10^8 + 1$:
    
            ![](./images/bitset-1e8sp.png)
    -   When the Sieve of Eratosthenes **does not store** the sieved-out primes:
    
        -   The [test result](https://quick-bench.com/q/rg2mCUxT02a44w9fWvHtZoNTJyU) when $N=5 \times 10^7 + 1$:
    
            ![](./images/bitset-5e7.png)
        -   The [test result](https://quick-bench.com/q/lusNWxWsR0VXoRBof7uBtqfvJuY) when $N=10^8 + 1$:
    
            ![](./images/bitset-1e8.png)
    
    From the test results, we know that:
    
    1.  The Sieve of Eratosthenes with time complexity $O(n \log \log n)$, after being optimized with `bitset` or `vector<bool>`, even outperforms the Euler sieve with time complexity $O(n)$;
    2.  The optimization effect of the Euler sieve after using `bitset` or `vector<bool>` is not obvious in most cases;
    3.  The optimization effect of `bitset` is slightly stronger than `vector<bool>`.

??? note "Reference code"
    Requires installing [google/benchmark](https://github.com/google/benchmark).
    
    ```cpp
    #include <benchmark/benchmark.h>
    #include <bits/stdc++.h>
    using namespace std;
    using u32 = uint32_t;
    using u64 = uint64_t;
    
    #define ERATOSTHENES_STORAGE_PRIME
    #define ENABLE_EULER
    constexpr u32 N = 5e7 + 1;
    
    #ifndef ERATOSTHENES_STORAGE_PRIME
    
    void Eratosthenes_CArray(benchmark::State &state) {
      static bool is_prime[N];
      for (auto _ : state) {
        fill(is_prime, is_prime + N, true);
        is_prime[0] = is_prime[1] = false;
        for (u32 i = 2; (u64)i * i < N; ++i)
          if (is_prime[i])
            for (u32 j = i * i; j < N; j += i) is_prime[j] = false;
        benchmark::DoNotOptimize(0);
      }
    }
    
    BENCHMARK(Eratosthenes_CArray);
    
    void Eratosthenes_vector(benchmark::State &state) {
      static vector<bool> is_prime(N);
      for (auto _ : state) {
        fill(is_prime.begin(), is_prime.end(), true);
        is_prime[0] = is_prime[1] = false;
        for (u32 i = 2; (u64)i * i < N; ++i)
          if (is_prime[i])
            for (u32 j = i * i; j < N; j += i) is_prime[j] = false;
        benchmark::DoNotOptimize(0);
      }
    }
    
    BENCHMARK(Eratosthenes_vector);
    
    void Eratosthenes_bitset(benchmark::State &state) {
      static bitset<N> is_prime;
      for (auto _ : state) {
        is_prime.set();
        is_prime.reset(0);
        is_prime.reset(1);
        for (u32 i = 2; (u64)i * i < N; ++i)
          if (is_prime[i])
            for (u32 j = i * i; j < N; j += i) is_prime.reset(j);
        benchmark::DoNotOptimize(0);
      }
    }
    
    BENCHMARK(Eratosthenes_bitset);
    
    #else
    
    void Eratosthenes_CArray_sp(benchmark::State &state) {
      static bool is_prime[N];
      for (auto _ : state) {
        vector<u32> prime;
        fill(is_prime, is_prime + N, true);
        is_prime[0] = is_prime[1] = false;
        for (u32 i = 2; (u64)i * i < N; ++i)
          if (is_prime[i])
            for (u32 j = i * i; j < N; j += i) is_prime[j] = false;
        for (u32 i = 2; i < N; ++i)
          if (is_prime[i]) prime.push_back(i);
        benchmark::DoNotOptimize(prime);
      }
    }
    
    BENCHMARK(Eratosthenes_CArray_sp);
    
    void Eratosthenes_vector_sp(benchmark::State &state) {
      static vector<bool> is_prime(N);
      for (auto _ : state) {
        vector<u32> prime;
        fill(is_prime.begin(), is_prime.end(), true);
        is_prime[0] = is_prime[1] = false;
        for (u32 i = 2; (u64)i * i < N; ++i)
          if (is_prime[i])
            for (u32 j = i * i; j < N; j += i) is_prime[j] = false;
        for (u32 i = 2; i < N; ++i)
          if (is_prime[i]) prime.push_back(i);
        benchmark::DoNotOptimize(prime);
      }
    }
    
    BENCHMARK(Eratosthenes_vector_sp);
    
    void Eratosthenes_bitset_sp(benchmark::State &state) {
      static bitset<N> is_prime;
      for (auto _ : state) {
        vector<u32> prime;
        is_prime.set();
        is_prime.reset(0);
        is_prime.reset(1);
        for (u32 i = 2; (u64)i * i < N; ++i)
          if (is_prime[i])
            for (u32 j = i * i; j < N; j += i) is_prime.reset(j);
        for (u32 i = 2; i < N; ++i)
          if (is_prime[i]) prime.push_back(i);
        benchmark::DoNotOptimize(prime);
      }
    }
    
    BENCHMARK(Eratosthenes_bitset_sp);
    
    #endif
    
    #ifdef ENABLE_EULER
    
    void Euler_CArray(benchmark::State &state) {
      static bool not_prime[N];
      for (auto _ : state) {
        vector<u32> prime;
        fill(not_prime, not_prime + N, false);
        not_prime[0] = not_prime[1] = true;
        for (u32 i = 2; i < N; ++i) {
          if (!not_prime[i]) prime.push_back(i);
          for (u32 pri_j : prime) {
            if (i * pri_j >= N) break;
            not_prime[i * pri_j] = true;
            if (i % pri_j == 0) break;
          }
        }
        benchmark::DoNotOptimize(prime);
      }
    }
    
    BENCHMARK(Euler_CArray);
    
    void Euler_vector(benchmark::State &state) {
      static vector<bool> not_prime(N);
      for (auto _ : state) {
        vector<u32> prime;
        fill(not_prime.begin(), not_prime.end(), false);
        not_prime[0] = not_prime[1] = true;
        for (u32 i = 2; i < N; ++i) {
          if (!not_prime[i]) prime.push_back(i);
          for (u32 pri_j : prime) {
            if (i * pri_j >= N) break;
            not_prime[i * pri_j] = true;
            if (i % pri_j == 0) break;
          }
        }
        benchmark::DoNotOptimize(prime);
      }
    }
    
    BENCHMARK(Euler_vector);
    
    void Euler_bitset(benchmark::State &state) {
      static bitset<N> not_prime;
      for (auto _ : state) {
        vector<u32> prime;
        not_prime.reset();
        not_prime.set(0);
        not_prime.set(1);
        for (u32 i = 2; i < N; ++i) {
          if (!not_prime[i]) prime.push_back(i);
          for (u32 pri_j : prime) {
            if (i * pri_j >= N) break;
            not_prime.set(i * pri_j);
            if (i % pri_j == 0) break;
          }
        }
        benchmark::DoNotOptimize(prime);
      }
    }
    
    BENCHMARK(Euler_bitset);
    
    #endif
    
    static void Noop(benchmark::State &state) {
      for (auto _ : state) benchmark::DoNotOptimize(0);
    }
    
    BENCHMARK(Noop);
    BENCHMARK_MAIN();
    ```

### Combined with tree blocking

`bitset` combined with tree blocking can solve a class of problems of finding the union of information of multiple paths on a tree; see [Data structures/Tree blocking](../../ds/tree-decompose.md) for details.

### Combined with Mo's algorithm

See [Miscellaneous/Mo's algorithm combined with bitset](../../misc/mo-algo-with-bitset.md) for details.

### Computing high-dimensional partial orders

See [FHR courseware](https://github.com/OI-wiki/libs/blob/master/lang/csl/FHR-分块bitset求高维偏序.pdf) for details.

## References and notes

[^bitset1]: [libstdc++: SGI STL extensions](https://gcc.gnu.org/onlinedocs/libstdc++/libstdc++-html-USERS-4.4/a00994.html#g32541eb0d6581b915af48b5a51006dff)

[^bitset2]: [libstdc++: std::bitset<\_Nb> Class Template Reference](https://gcc.gnu.org/onlinedocs/libstdc++/libstdc++-html-USERS-4.4/a00219.html)
