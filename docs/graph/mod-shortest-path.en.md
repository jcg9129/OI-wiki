When problems of the form "given $n$ integers, find how many other integers these $n$ integers can piece together ($n$ integers can be taken repeatedly)", as well as "given $n$ integers, find the smallest (largest) integer that these $n$ integers cannot piece together", or "at least how many times do we need to piece together to obtain a number that is $p$ modulo $K$" appear, we can use the congruence shortest-path method.

The congruence shortest path uses congruence to construct some states, which can achieve the purpose of optimizing space complexity.

By analogy with the [difference constraints](./diff-constraints.md) method, these states constructed using congruence can be regarded as points in single-source shortest paths. The state transition of the congruence shortest path is usually of the form $f(i+y) = f(i) + y$, similar to $f(v) = f(u) +edge(u,v)$ in single-source shortest paths.

## Example problems

### Example problem 1

???+ note "[P3403 Elevator jump machine](https://www.luogu.com.cn/problem/P3403)"
    Problem summary: Given $x，y，z，h$, for $k \in [1,h]$, how many $k$ can satisfy $ax+by+cz=k$? ($0\leq a,b,c$, $1\le x,y,z\le 10^5$, $h\le 2^{63}-1$)

Without loss of generality, assume $x < y < z$.

Let $d_i$ be the lowest floor $p$ that can be reached using only **operation 2** and **operation 3** subject to $p\bmod x = i$, i.e. the smallest number congruent to $i$ modulo $x$ that can be obtained after **operation 2** and **operation 3**, used to compute the number of numbers in this congruence class that satisfy the condition.

We can obtain two states:

-   $i \xrightarrow{y} (i+y) \bmod x$

-   $i \xrightarrow{z} (i+z) \bmod x$

Note that we usually select the smallest number among a group of $a_i$ to take the modulus by, i.e. $x$ here, which can minimize the space complexity as much as possible (the residue system is smallest).

Then it is actually equivalent to executing the edge-building operations in the shortest path:

`add(i, (i+y) % x, y)`

`add(i, (i+z) % x, z)`

Next we only need to compute $d_0, d_1, d_2, \dots, d_{x-1}$; we only need to run the shortest path once to compute the corresponding $d_i$.

??? example "Implementation based on shortest path"
    ```cpp
    --8<-- "docs/graph/code/mod-shortest-path/mod-shortest-path_1.cpp"
    ```

But in fact there is no need to perform normal shortest-path solving; note that there are two special properties:

First, there are only two kinds of edge weights, and for each path, due to the commutativity of addition, the order of walking the two kinds of edge weights has no effect. Therefore we can consider doing the shortest path twice, each time building only one class of edge-weight edges;

Second, for a graph with only one class of edge weight, each point $u$ has one in-degree (from $(u-y) \bmod x$) and one out-degree (from $(u+y) \bmod x$), so the whole graph must consist of several cycles. And it can be proved that there are $\gcd(x,y)$ cycles of equal length in total.

???+ note "Proof"
    Let $d=\gcd(x,y)$, let $x=da,y=db$, so $\gcd(a,b)=1$.
    
    Consider walking $k$ steps starting from $u$, reaching $(u+ky) \bmod x$. If a cycle forms, then $ky \equiv 0 \pmod x$, i.e. $kb \equiv 0 \pmod a$.
    
    Since $\gcd(a,b)=1$, the smallest $k=a$, i.e. the cycle length is $a = \dfrac{x}{d}$. Since it starts from an arbitrary point, every possible cycle length is equal, and the number of cycles is $d$.

Moreover, the edge weights are positive, so after going around the cycle twice, we definitely cannot continue to relax. We just directly loop and update once. Processing this way is not limited by the complexity of the shortest path, and can achieve $O(x)$.

Same as the difference-constraints problem, when there is a set of solutions $\{a_1,a_2,\cdots,a_n\}$, $\{a_1+d,a_2+d,\cdots,a_n+d\}$ is also a set of solutions, so in this problem we let $i=1$ be the source point; at this time the $dis_{1}=1$ at the source point is the smallest within the known range, so the obtained solution is also a smallest set of solutions.

The answer is:

$$
\sum_{i=0}^{x-1}\left(\frac{h-d_i}{x} + 1\right)
$$

Adding 1 is because the floor where $d_i$ is located also counts once.

In the code implementation, note that the range of $h$ is $h \leq 2^{63}-1$, so before solving the shortest path the initial value of $d_i$ should be set to at least $2^{63}$, which exceeds the maximum value of `long long` in C++. So we can use `unsigned long long`, or first set $h \gets h - 1$ and then set the lowest floor to floor $0$; the rest of the code is unchanged.

??? example "Implementation based on cycle optimization"
    ```cpp
    --8<-- "docs/graph/code/mod-shortest-path/mod-shortest-path_2.cpp"
    ```

### Example problem 2

???+ note "[ARC084B Small Multiple](https://atcoder.jp/contests/arc084/tasks/arc084_b)"
    Problem summary: Given $n$, find the digit sum of the multiple of $n$ with the smallest digit sum. ($1\le n\le 10^5$)

This problem can be solved in $O(n\log^2 n)$ time using circular convolution to optimize the unbounded knapsack, but we hope to obtain a linear algorithm.

Observe that any positive integer can be obtained starting from $1$, executing the operations of multiplying by $10$ and adding $1$ in some order, and the number of add-$1$ operations is exactly the digit sum of this number. This hints at using the shortest path.

For all $0\le k\le n-1$, connect an edge of weight $0$ from $k$ to $10k$; connect an edge of weight $1$ from $k$ to $k+1$. (The numbers of the points are all in the sense of modulo $n$.)

Each multiple of $n$ corresponds to a path from point $1$ to point $0$ in this graph; just compute the shortest path from $1$ to $0$. Some paths are invalid (e.g. walking 10 edges of weight $1$ consecutively), but the answers produced by these paths are definitely not optimal and do not affect the answer.

The time complexity is $O(n)$.

## Exercises

[Luogu P3403 Elevator jump machine](https://www.luogu.com.cn/problem/P3403)

[Luogu P2662 Ranch fence](https://www.luogu.com.cn/problem/P2662)

[\[National Team Training\] Momo's equation](https://www.luogu.com.cn/problem/P2371)

[「NOIP2018」Currency system](https://loj.ac/problem/2951)

[AGC057D - Sum Avoidance](https://atcoder.jp/contests/agc057/tasks/agc057_d)

[「THUPC 2023 Preliminary」Knapsack](https://loj.ac/p/6872)
