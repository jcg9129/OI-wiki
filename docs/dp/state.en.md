## Introduction

Bitmask DP is a kind of dynamic programming that achieves state transitions by turning a set of states into an integer recorded in the DP state.

To achieve lower time complexity, one usually needs to find states with a lower number of states. Most problems use binary states, using an $n$-bit binary number to represent the situation of $n$ independent binary states.

Using bitmasking usually involves bit operations; for basic bit operations, see the [bit operations](../math/bit.md) page.

## Example 1

???+ note "[「SCOI2005」Mutual Non-Aggression](https://loj.ac/problem/2153)"
    Place $K$ kings on an $N\times N$ board ($1 \leq N \leq 9, 1 \leq K \leq N \times N$) so that they do not attack each other; how many placement schemes are there in total?
    
    A king can attack the cells adjacent to it in the eight directions—up, down, left, right, and the four diagonals—one cell each, for $8$ cells in total.

### Explanation

Let $f(i,j,l)$ denote the number of valid schemes for the first $i$ rows when the state of the $i$-th row is $j$ and $l$ kings have already been placed on the board.

For the state numbered $j$, we use the binary integer $sit(j)$ to represent the placement of kings: a binary bit of $sit(j)$ being $0$ means no king is placed at the corresponding position, and being $1$ means a king is placed there; we use $sta(j)$ to denote the number of kings in this state, i.e. the number of $1$s in the binary number $sit(j)$. For example, the state shown in the figure below can be represented by the binary number $100101$ (the left side of the board corresponds to the low bits of the binary), so $sit(j)=100101_{(2)}=37, sta(j)=3$.

![](./images/SCOI2005-互不侵犯.png)

Let the state of the current row be $j$ and the state of the previous row be $x$; we can obtain the following state-transition equation: $f(i,j,l) = \sum f(i-1,x,l-sta(j))$.

Let the state number of the previous row be $x$; while ensuring the current row and the previous row do not conflict, enumerate all possible $x$ to transition. The transition equation:

$$
f(i,j,l) = \sum f(i-1,x,l-sta(j))
$$

### Implementation

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/state/state_1.cpp"
    ```

## Example 2

???+ note "[\[POI2004\] PRZ](https://www.luogu.com.cn/problem/P5911)"
    There are $n$ people who need to cross a bridge; the $i$-th person has weight $w_i$ and takes time $t_i$ to cross. When crossing, these people are divided into several groups; only after all people in one group have crossed can the other groups cross. The bridge's maximum load is $W$; ask the shortest time for all these people to cross the bridge.
    
    $100\le W \le 400$, $1\le n\le 16$, $1\le t_i\le 50$, $10\le w_i\le 100$.

### Explanation

We use $S$ to denote a subset of the set formed by all people; let $t(S)$ denote the longest crossing time among the people in $S$, $w(S)$ denote the total weight of all people in $S$, and $f(S)$ denote the shortest time for all people in $S$ to cross the bridge; then:

$$
\begin{cases}
    f(\varnothing)=0,\\
    f(S)=\min\limits_{T\subseteq S;~w(T)\leq W}\left\{t(T)+f(S\setminus T)\right\}.
\end{cases}
$$

Note that here we cannot directly enumerate a set and then judge whether it is a subset; instead we should use [subset enumeration](../math/binary-set.md#traversing-the-submasks-of-all-masks), so that the time complexity is $O(3^n)$.

### Implementation

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/state/state_2.cpp"
    ```

## Exercises

-   [「NOI2001」Artillery Position](https://loj.ac/problem/10173)
-   [「USACO06NOV」Corn Fields](https://www.luogu.com.cn/problem/P1879)
-   [「Nine-Province Joint Exam 2018」A Pair of Wooden Chess](https://loj.ac/problem/2471)
