author: linehk, persdre

Time complexity and space complexity are important standards for measuring the efficiency of an algorithm.

## Number of basic operations

The same algorithm runs at somewhat different speeds on different computers, and the actual running speed is hard to compute theoretically while being cumbersome to measure in practice. So what we usually consider is not the actual time an algorithm takes to run, but the number of basic operations the algorithm needs to perform.

On an ordinary computer, addition, subtraction, multiplication and division, accessing a variable (a variable of a primitive data type, the same below), assigning a value to a variable, and so on can all be regarded as basic operations.

Counting or estimating the number of basic operations can serve as a metric for judging how long an algorithm takes.

## Time complexity

### Definition

To measure how fast or slow an algorithm is, we must take the size of the data into account. The so-called data size generally refers to the number of input values, the number of vertices and edges of a graph given in the input, and so on. Generally speaking, the larger the data size, the longer the algorithm takes. When measuring the efficiency of an algorithm in competitive programming, what matters most is not how long it takes at some particular data size, but the trend by which its running time grows with the data size, that is, its **time complexity**.

### Introduction

The main reasons for considering the trend of running time with respect to data size are as follows:

1.  A modern computer can process hundreds of millions or more basic operations per second, so the data sizes we deal with are usually very large. If algorithm A takes $100n$ time on data of size $n$ while algorithm B takes $n^2$ time on data of size $n$, then algorithm B takes less time when the data size is smaller than $100$, but within one second algorithm A can process data of size in the millions, while algorithm B can only process data of size in the tens of thousands. When the algorithm is allowed to run longer, the influence of time complexity on the processable data size becomes even more pronounced, far exceeding the influence of the running time at the same data size.
2.  We use the number of basic operations to represent the running time of an algorithm, but different basic operations actually take different amounts of time; for example, addition and subtraction take far less time than division. Computing the time complexity while ignoring the differences between different basic operations, as well as the difference between one basic operation and ten basic operations, eliminates the influence of the differing times of basic operations.

Of course, the running time of an algorithm is not entirely determined by the input size, but is also related to the content of the input. Therefore, time complexity is further divided into several kinds, for example:

1.  Worst-case time complexity, that is, the time complexity corresponding to the input that takes the longest at each input size. In competitive programming, since the input can be arbitrarily given within the specified data range, to guarantee that an algorithm can pass any data within a certain data range, we generally consider the worst-case time complexity.
2.  Average (expected) time complexity, that is, the complexity of the average running time over all possible inputs at each input size (the complexity of the expected running time under random input).

The so-called "trend by which running time grows with data size" is a vague notion; we need the **asymptotic notation** introduced below to formally express time complexity.

## Definitions of asymptotic notation

Asymptotic notation is a standardized description of the order of a function. Simply put, asymptotic notation ignores the more slowly growing parts of a function as well as the coefficients of its terms (in time-complexity analysis the coefficients are generally called "constants"), while retaining the important part that can be used to indicate the growth trend of the function.

A simple way to remember it is that non-strict relations (with equality) use capital letters and strict relations (without equality) use lowercase letters: equality is $\Theta$, less-than is $O$, and greater-than is $\Omega$. Big $O$ and little $o$ were originally the Greek letter Omicron; since the glyph is the same, they can also be understood as the Latin capital $O$ and lowercase $o$.

In English, the roots "-micro-" and "-mega-" are often used to denote $10$ to the power of negative six (one millionth) and to the power of six (one million), and also mean "small" and "large". Small and large are also the meanings commonly denoted by the Greek letters Omicron and Omega.

### Big Θ notation

For functions $f(n)$ and $g(n)$, $f(n)=\Theta(g(n))$ if and only if $\exists c_1,c_2,n_0>0$ such that $\forall n \ge n_0, 0\le c_1\cdot g(n)\le f(n) \le c_2\cdot g(n)$.

That is, if the function $f(n)=\Theta(g(n))$, then we can find two positive numbers $c_1, c_2$ such that $f(n)$ is sandwiched between $c_1\cdot g(n)$ and $c_2\cdot g(n)$.

For example, $3n^2+5n-3=\Theta(n^2)$, where $c_1, c_2, n_0$ can be $2, 4, 100$ respectively. $n\sqrt {n} + n{\log^5 n} + m{\log m} +nm=\Theta(n\sqrt {n} + m{\log m} + nm)$, where $c_1, c_2, n_0$ can be $1, 2, 100$ respectively.

### Big O notation

The $\Theta$ notation gives us both an upper and a lower bound of a function at once. If we know only the asymptotic upper bound of a function but not its asymptotic lower bound, we can use the $O$ notation. $f(n)=O(g(n))$ if and only if $\exists c,n_0$ such that $\forall n \ge n_0,0\le f(n)\le c\cdot g(n)$.

When studying time complexity we usually use the $O$ notation, because what we care about is generally the upper bound of a program's running time, not the lower bound of its running time.

Note that "upper bound" and "lower bound" here refer to the growth trend of the function, not to the algorithm. The upper bound of an algorithm's running time corresponds to the "worst-case time complexity", not to the big $O$ notation. So it is entirely feasible to use the $\Theta$ notation to express the worst-case time complexity; one could even say $\Theta$ is more precise than $O$. The main reasons for using the $O$ notation are, first, that we can sometimes only prove an upper bound on the time complexity but cannot prove its lower bound (this generally occurs with more complex algorithms and complexity analyses), and second, that $O$ is a little more convenient to type on a computer.

### Big Ω notation

Similarly, we use the $\Omega$ notation to describe the asymptotic lower bound of a function. $f(n)=\Omega(g(n))$ if and only if $\exists c,n_0$ such that $\forall n \ge n_0,0\le c\cdot g(n)\le f(n)$.

### Little o notation

If the $O$ notation is like a less-than-or-equal sign, then the $o$ notation is like a strict less-than sign.

Little $o$ notation is widely used in mathematical analysis: the Taylor expansion of a function at a point has a Peano remainder, and little $o$ notation is used to denote strict less-than, thereby carrying out asymptotic analysis of equivalent infinitesimals.

$f(n)=o(g(n))$ if and only if for every given positive number $c$, $\exists n_0$ such that $\forall n \ge n_0,0\le f(n)< c\cdot g(n)$.

### Little ω notation

If the $\Omega$ notation is like a greater-than-or-equal sign, then the $\omega$ notation is like a strict greater-than sign.

$f(n)=\omega(g(n))$ if and only if for every given positive number $c$, $\exists n_0$ such that $\forall n \ge n_0,0\le c\cdot g(n)< f(n)$.

![](images/order.png)

### Common properties

-   $f(n) = \Theta(g(n))\iff f(n)=O(g(n))\land f(n)=\Omega(g(n))$
-   $f_1(n) + f_2(n) = O(\max(f_1(n), f_2(n)))$
-   $f_1(n) \times f_2(n) = O(f_1(n) \times f_2(n))$
-   $\forall a \neq 1, \log_a{n} = O(\log_2 n)$. From the change-of-base formula, we know that any logarithmic function, whatever its base, has the same growth rate, so the base of the logarithm in an asymptotic time complexity is generally omitted.

## Simple examples of computing time complexity

### `for` loops

=== "C++"
    ```cpp
    int n, m;
    std::cin >> n >> m;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        for (int k = 0; k < m; ++k) {
          std::cout << "hello world\n";
        }
      }
    }
    ```

=== "Python"
    ```python
    n = int(input())
    m = int(input())
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, m):
                print("hello world")
    ```

=== "Java"
    ```java
    int n, m;
    n = input.nextInt();
    m = input.nextInt();
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < m; ++k) {
                System.out.println("hello world");
            }
        }
    }
    ```

If we take the magnitudes of the input values $n$ and $m$ as the data size, then the time complexity of the code above is $\Theta(n^2m)$.

### DFS

When performing a [DFS](../graph/dfs.md) on a graph with $n$ vertices and $m$ edges, since each vertex and each edge is visited only a constant number of times, the complexity is $\Theta(n+m)$.

## Which quantities are constants?

When we are going to perform some number of operations, how do we determine whether that number of operations affects the time complexity? For example:

=== "C++"
    ```cpp
    constexpr int N = 100000;
    for (int i = 0; i < N; ++i) {
      std::cout << "hello world\n";
    }
    ```

=== "Python"
    ```python
    N = 100000
    for i in range(0, N):
        print("hello world")
    ```

=== "Java"
    ```java
    final int N = 100000;
    for (int i = 0; i < N; ++i) {
        System.out.println("hello world");
    }
    ```

If the magnitude of $N$ is not regarded as the input size, then the time complexity of this code is $O(1)$.

When computing time complexity, which variables are regarded as the input size is very important, and all quantities unrelated to the input size are regarded as constants and can be treated as $1$ when computing the complexity.

Note that in theoretical discussions about time complexity, "the algorithm can solve a problem of any size" is a basic assumption (of course, in practice, since time and storage space are limited, problems that are too large cannot be solved). Therefore, being able to solve a problem of bounded data size in constant time (for example, precomputing the answer for every possible input within the data range) does not make an algorithm's time complexity $O(1)$.

## Master Theorem

We can use the Master Theorem to quickly obtain the complexity of a recursive algorithm.
The recurrence relation of the Master Theorem is as follows:

$$
T(n) = a T\left(\frac{n}{b}\right)+f(n)\qquad \forall n > b
$$

Then

$$
T(n) = \begin{cases}\Theta(n^{\log_b a}) & f(n) = O(n^{\log_b (a)-\epsilon}),\epsilon > 0 \\ \Theta(f(n)) & f(n) = \Omega(n^{\log_b (a)+\epsilon}),\epsilon\ge 0\\ \Theta(n^{\log_b a}\log^{k+1} n) & f(n)=\Theta(n^{\log_b a}\log^k n),k\ge 0 \end{cases}
$$

Note that the second case additionally requires the regularity condition to hold, namely $a f(n/b) \leq c f(n)$ for some constant $c < 1$ and sufficiently large $n$.

The idea of the proof is to decompose a problem of size $n$ into $a$ problems of size $(\frac{n}{b})$, then merge them one after another until reaching the top level. Each merge of subproblems costs $f(n)$ time.

??? note "Proof"
    Following the proof idea mentioned above, the detailed proof is as follows.
    
    For level $0$ (the top level), merging the subproblems costs $f(n)$ time.
    
    For level $1$ (the subproblems produced by the first division), there are $a$ subproblems in total, and merging each subproblem costs $f\left(\frac{n}{b}\right)$ time, so the merging costs $a f\left(\frac{n}{b}\right)$ time in total.
    
    Recursing level by level, we can write out the recursion tree as follows: ![](./images/master-theorem-proof.svg)
    
    This tree has height ${\log_b n}$ and $n^{\log_b a}$ leaves in total, so $T(n) = \Theta(n^{\log_b a}) + g(n)$, where $g(n) = \sum_{j = 0}^{\log_{b}{n - 1}} a^{j} f(n / b^{j})$.
    
    For the first case: $f(n) = O(n^{\log_b a-\epsilon})$, so $g(n) = O(n^{\log_b a})$.
    
    For the second case: first, $g(n) = \Omega(f(n))$; and since $a f(\dfrac{n}{b}) \leq c f(n)$, as long as $c$ is a sufficiently small positive number and $n$ is sufficiently large, we can derive $g(n) = O(f(n)$). Squeezing from both sides gives $g(n) = \Theta(f(n))$.
    
    For the third case: $f(n) = \Theta(n^{\log_b a})$, so $g(n) = O(n^{\log_b a} {\log n})$. The result for $T(n)$ follows obviously once $g(n)$ is obtained.

Below are a few examples illustrating how to use the Master Theorem.

1.  $T(n) = 2T\left(\frac{n}{2}\right) + 1$: then $a=2, b=2, {\log_2 2} = 1$, so $\epsilon$ can be taken in $(0, 1]$, satisfying the first case, hence $T(n) = \Theta(n)$.

2.  $T(n) = T\left(\frac{n}{2}\right) + n$: then $a=1, b=2, {\log_2 1} = 0$, so $\epsilon$ can be taken in $(0, 1]$, satisfying the second case, hence $T(n) = \Theta(n)$.

3.  $T(n) = T\left(\frac{n}{2}\right) + {\log n}$: then $a=1, b=2, {\log_2 1}=0$, so $k$ can be taken as $1$, satisfying the third case, hence $T(n) = \Theta(\log^2 n)$.

4.  $T(n) = T\left(\frac{n}{2}\right) + 1$: then $a=1, b=2, {\log_2 1} = 0$, so $k$ can be taken as $0$, satisfying the third case, hence $T(n) = \Theta(\log n)$.

## Amortized complexity

For details, see [Amortized complexity](./amortized-analysis.md).

## Space complexity

Similarly, the trend by which the space used by an algorithm varies with the input size can be measured by its **space complexity**.

## Computational complexity

This article mainly introduces complexity from the perspective of algorithm analysis. If you are interested, you can learn more in depth at [Computational complexity](../misc/cc-basic.md).
