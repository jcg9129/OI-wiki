???+ warning "Note"
    The Eulerian number below refers specifically to the Eulerian number. Take care to distinguish it from the Euler number, and from Euler's number (referring to mathematical constants associated with Euler, such as $\gamma$ or $\mathrm{e}$).

In enumerative combinatorics, the **Eulerian number** is the **number** of permutations of the numbers from $1$ to $n$ in which exactly $m$ elements are greater than the previous element (permutations with $m$ "ascents"). It is defined as:

$$
A(n, m) = 
\left\langle 
\begin{matrix}
  n\\
  m - 1
\end{matrix}
\right\rangle
$$

For example, among the numbers from $1$ to $3$ there are a total of $4$ permutations in which exactly one element is greater than the previous one:

| Permutation | Adjacent elements satisfying the condition | Count |
| ----- | ----------- | -- |
| 1 2 3 | 1, 2 & 2, 3 | 2  |
| 1 3 2 | 1, 3        | 1  |
| 2 1 3 | 1, 3        | 1  |
| 2 3 1 | 2, 3        | 1  |
| 3 1 2 | 1, 2        | 1  |
| 3 2 1 |             | 0  |

So according to the definition of $A(n, m)$: if $n$ equals $3$ and $m$ equals $1$, the Eulerian number is $4$, meaning there are a total of $4$ permutations with $1$ element greater than the previous one.

For Eulerian numbers with relatively small values of $n$ and $m$, we can obtain the result directly:

| $A(n, m)$ | Permutations meeting the requirement | Count |
| --------- | -------------------------------------------- | -- |
| $A(1, 0)$ | $(1)$                                        | 1  |
| $A(2, 0)$ | $(2, 1)$                                     | 1  |
| $A(2, 1)$ | $(1, 2)$                                     | 1  |
| $A(3, 0)$ | $(3, 2, 1)$                                  | 1  |
| $A(3, 1)$ | $(1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2)$ | 4  |
| $A(3, 2)$ | $(1, 2, 3)$                                  | 1  |

## Formula

The Eulerian number can be computed by recurrence or recursion.

First, when $m \ge n$ or $n = 0$, there is no permutation satisfying the condition, i.e. the Eulerian number is $0$ in this case.

Second, when $m = 0$, only the descending permutation satisfies the condition, i.e. the Eulerian number is $1$ in this case.

Finally, consider inserting $n$ into a permutation of $n-1$ to obtain a permutation of $n$. Since inserting $n$ increases the number of ascents by at most $1$, $A(n, m)$ can be obtained by transitions only from $A(n-1, m-1)$ and $A(n-1, m)$.

Consider the position where $n$ is inserted: when $p_{i-1} < p_{i}$, if $n$ is inserted before $p_{i}$, i.e. $n$ is inserted into an "ascent", the number of ascents of the permutation is unchanged; in addition, if $n$ is inserted at the front of the permutation, the number of ascents is also unchanged; otherwise, if $n$ is inserted into the remaining positions, the number of ascents increases by $1$.

Consider the transition from $A(n-1, m-1)$ to $A(n, m)$; here we need the number of ascents to increase by $1$, so $n$ cannot be inserted into an "ascent" or at the front of the permutation, giving a total of $n - (m-1) - 1 = n-m$ ways.

Consider the transition from $A(n-1, m)$ to $A(n, m)$; here we need the number of ascents to remain unchanged, so $n$ can only be inserted into an "ascent" or at the front of the permutation, giving a total of $m+1$ ways.

In summary, we have

$$
A(n, m) = \begin{cases}
    0, & m > n \text{ or } n = 0, \\
    1, & m = 0, \\
    (n-m) \cdot A(n-1, m-1) + (m+1) \cdot A(n-1, m), & \text{otherwise}.
\end{cases}
$$

## Implementation

=== "C++"
    ```cpp
    int eulerianNumber(int n, int m) {
      if (m >= n || n == 0) return 0;
      if (m == 0) return 1;
      return (((n - m) * eulerianNumber(n - 1, m - 1)) +
              ((m + 1) * eulerianNumber(n - 1, m)));
    }
    ```

=== "Python"
    ```python
    def eulerianNumber(n, m):
        if m >= n or n == 0:
            return 0
        if m == 0:
            return 1
        return ((n - m) * eulerianNumber(n - 1, m - 1)) + (
            (m + 1) * eulerianNumber(n - 1, m)
        )
    ```

## Exercises

-   [CF1349F1 Slime and Sequences (Easy Version)](https://codeforces.com/problemset/problem/1349/F1)
-   [CF1349F2 Slime and Sequences (Hard Version)](https://codeforces.com/problemset/problem/1349/F2)
-   [UOJ 593. 新年的军队](https://uoj.ac/problem/593)
-   [P7511 三到六](https://www.luogu.com.cn/problem/P7511)
