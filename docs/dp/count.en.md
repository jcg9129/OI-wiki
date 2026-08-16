**Counting DP** is a method that uses DP-like memoized search (with some difference from DP in the narrow sense, i.e. optimization problems), used to solve counting (as well as summation) problems.

## Basics

### Basic idea

A counting problem generally means finding the size of a set $S$. In OI, the size of $S$ can sometimes reach the order of $\Theta(n^n)$ or even $\Theta(2^{n!})$ (of course, it is generally taken modulo some fixed number), where $n$ is the problem size, so we cannot enumerate the elements of $S$ one by one.

If we can partition $S$ into several disjoint subsets, then the number of elements of $S$ equals the sum of the numbers of elements of these parts. If the counting of these subsets happens to be similar to the original problem, then we can solve it with a method similar to dynamic programming.

### Example

???+ note "Example"
    Given a positive integer $n$, find how many ways there are to partition $n$ into a sum of $k$ positive integers, where swapping positions counts as a different partition.

Let the set $S_{n,k}$ be the set of positive-integer tuples of the form $(a_1, \dots, a_k)$ where $a_1 + \dots + a_k = n$. If $a_k$ is fixed, we have the following derivation: because $a_1 + a_2 + \dots + a_{k-1} + a_k = n$, we have $a_1 + a_2 + \dots + a_{k-1} = n - a_k$. By the definition of $S_{n,k}$, $(a_1, a_2, \dots, a_{k-1}) \in S_{n - a_k, k - 1}$.

Since $a_1, a_2, \dots, a_k$ are positive integers, the range of $a_k$ is $[1, n - k + 1] \cap \mathbb Z$. Therefore, $S_{n,k}$ can be partitioned by $a_k$ into $n - k + 1$ subsets, where when $a_k = i$, this subset is:

$$
\{(L, i) \mid L \in S_{n-i,k-1}\}.
$$

The number of elements of this subset clearly equals that of $S_{n-i,k-1}$, and since $i$ differs, these subsets are pairwise disjoint. So:

$$
|S_{n,k}| = \sum_{i=1}^{n-k+1} |S_{n-i,k-1}|.
$$

Thus we can handle it with a DP-like method: let $f_{n,k}$ be $|S_{n,k}|$; then we have the state-transition equation:

$$
f_{n,k} = \sum_{i=1}^{n-k+1} f_{n-i,k-1}.
$$

Now it can be solved with the DP method.

### Similarities and differences with optimization DP

We can see that both counting DP and optimization DP find a value (a size value, an optimal value) within a range $\Omega$; this value is obtained by processing all elements of $\Omega$ once and then aggregating the processed values.

For example, for the 0-1 knapsack problem, the elements of $\Omega$ are the sets of all items in the knapsack; for a scheme $S$ in $\Omega$, we process $S$ once, and the result $w(S)$ of the processing is the total value of the items in $S$; over all obtained processed values, we take the maximum to get the answer to the problem.

For a counting problem, the elements of $\Omega$ are the sets $S$ whose element counts are to be computed; its processing turns all elements in $S$ into $1$, and then aggregates these $1$s by addition; because each element in $S$ corresponds to a $1$, the value obtained this way is the number of elements in $S$.

When the aggregation operation is max/min, we can divide $\Omega$ into any number of parts, as long as the union of these parts is $\Omega$, without the disjointness condition. But since a counting problem does not satisfy this condition, we need to divide $\Omega$ into several pairwise disjoint parts—this is the difference from optimization DP.

## Example

???+ note "Example"
    Given a positive integer $n$, find how many ways there are to partition $n$ into a sum of any number of positive integers, where swapping positions counts as the **same** partition.

### Solution 1

The elements of the set to be counted are multisets of positive integers whose sum is $n$. But this is clearly not easy to derive.

If a multiset $T$ contains only positive integers $\le M$ and the sum of all elements of $T$ is $n$, we say $T \in S_{n, M}$. Consider the number of occurrences of $M$. It may be $k \in \left[0, \left\lfloor \dfrac nM \right\rfloor\right] \cap \mathbb Z$. So it can transition to $S_{n - kM, M - 1}$. Just sum them up. The complexity is $\Theta(n^2 \log n)$ (the $\log$ comes from the harmonic series caused by the range of $k$).

But this is still not good enough. Consider the following example:

$$
\begin{aligned}
f_{8, 3} &= {\color{red}f_{8, 2} + f_{5, 2} + f_{2, 2}} \\
f_{9, 3} &= {\color{blue}f_{9, 2} + f_{6, 2} + f_{3, 2} + f_{0, 2}} \\
f_{10, 3} &= {\color{green}f_{10, 2} + f_{7, 2} + f_{4, 2} + f_{1, 2}}\\
f_{11, 3} &= f_{11, 2} + {\color{red}f_{8, 2} + f_{5, 2} + f_{2, 2}}\\
f_{12, 3} &= f_{12, 2} + {\color{blue}f_{9, 2} + f_{6, 2} + f_{3, 2} + f_{0, 2}}\\
f_{13, 3} &= f_{13, 2} + {\color{green}f_{10, 2} + f_{7, 2} + f_{4, 2} + f_{1, 2}}\\
\end{aligned}
$$

By substituting equals, we get $f_{11, 3} = f_{11, 2} + f_{8, 3}$, $f_{12, 3} = f_{12, 2} + f_{9, 3}$, $f_{13, 3} = f_{13, 2} + f_{10, 3}$. Similarly we can obtain a general state-transition equation:

$$
f_{n, M} = f_{n, M - 1} + \begin{cases} f_{n - M, M} & n \ge M, \\ 0 & \text{otherwise}. \end{cases}
$$

Now the time complexity is $\Theta(n^2)$.

### Solution 2

Considering that a multiset $T$ of positive integers can always be obtained via the two operations "increment each element of $T$" and "add an element with value $1$ to $T$", and different operation sequences yield different results.

This way, the transition on $T$ can be turned into a transition on operation sequences. Consider the last operation in an operation sequence that partitions $n$ into $m$ numbers (all these operation sequences are denoted $B_{n,m}$): if it is a "1" operation, it does not add a number, but $\sum T$ increases by $m$. To make the final $\sum T = n$, the original $T$ (denoted $T'$) needs a sum of $n-m$. So $B_{n,m} \to B_{n-m,m}$; if it is a "2" operation, it adds a number and $\sum T$ increases by $1$. So $B_{n,m} \to B_{n-1,m-1}$.

The time complexity of doing this is still $\Theta(n^2)$.

### Solution 3

Consider dividing $T$ into a part $T_1$ greater than $\sqrt n$ and a part $T_2$ less than or equal to $\sqrt n$. $T_2$ can be found using Solution 1, and the number of $T_1$ can be found by slightly modifying Solution 2: consider changing the two operations to "increment each element of $T_1$" and "add an element with value $\lfloor \sqrt n \rfloor + 1$ to $T_1$". The state-transition equation is easy to write out.

Split $n$ into two parts $A$ and $B$. Enumerating one gives the other. Find the number of $T_1$ satisfying $\sum T_1 = A$ and the number of $T_2$ satisfying $\sum T_2 = B$, multiply them, and sum over all $A$ to get the final result.

Since in the process of computing the number of $T_1$, $M \le \sqrt n$, the time complexity of computing $T_1$ using Solution 1 is $\Theta(n^{3/2})$. Similarly, since in the process of computing the number of $T_2$, $|T_2| \le \dfrac{\sum T_2}{\sqrt n} \le \dfrac{n}{\sqrt n} = \sqrt n$, the time complexity of computing $T_2$ using Solution 2 is also $\Theta(n^{3/2})$. So the total time complexity is $\Theta(n^{3/2})$.
