## Introduction

This page lists some common optimization methods for dynamic programming (DP). So-called DP optimization refers to the fact that although many dynamic-programming problems easily yield a naive state-transition equation, directly computing it is often inefficient, so we need some techniques to reduce the time complexity.

These methods are closely connected, often contain similar ideas, and frequently need to be combined. Therefore, this article only makes a rough classification, focusing on introducing some of the most basic ideas.

## Optimizing with common techniques

The transitions of many dynamic-programming problems can be optimized with common algorithms and data structures.

This kind of technique has two common situations. In the first situation, the DP problem has the following state-transition equation:

$$
f(i) = F(a_i,\{f(j) : j < i\}).
$$

Here, the computation of the current state $f(i)$ depends on the current input $a_i$ and the states of the entire preceding sequence $\{f(j):j < i\}$. Therefore, we can maintain a data structure, treating each computation of $f(i)$ as a query operation; and after obtaining the current state $f(i)$, we can perform another modification operation to update this data structure for use in subsequent transitions.

In the second situation, the DP problem has the following state-transition equation:

$$
f(i,\cdot) = F(a_i,f(i-1,\cdot)).
$$

Here, each $f(i,\cdot)$ is an array or other relatively complex object. Therefore, although $f(i,\cdot)$ depends only on the single previous state, the complexity of a single transition is high, and it needs to be optimized with techniques such as data structures.

### Prefix-sum optimization of DP

Related page: [prefix sums](../../basic/prefix-sum.md#prefix-sums)

If the computation of the current state depends on the segment sums of previous states, then we can speed up the computation by maintaining prefix sums. Among these, a class of problems involving high-dimensional prefix sums is also called [SOS DP](../../basic/prefix-sum.md#special-case-sum-over-subsets-dp).

Exercises:

-   [Luogu P2513 \[HAOI2009\] Inversion Sequence](https://www.luogu.com.cn/problem/P2513)
-   [AtCoder Educational DP Contest M - Candies](https://atcoder.jp/contests/dp/tasks/dp_m)

### Monotonic-queue / monotonic-stack optimization of DP

Main page: [Monotonic-queue / monotonic-stack optimization](./monotonic-queue-stack.md)

If the current state depends on information such as the interval extremum of previous states, we can speed up the computation by maintaining a monotonic queue or monotonic stack.

### Segment-tree / Fenwick-tree optimization of DP

Related pages: [segment tree](../../ds/seg.md), [Fenwick tree](../../ds/fenwick.md)

If each state transition queries information such as the sum or extremum over some interval, or a single modification operation involves an interval update, we can speed up the computation by maintaining a segment tree or Fenwick tree.

Exercises:

-   [AtCoder Educational DP Contest Q - Flowers](https://atcoder.jp/contests/dp/tasks/dp_q)
-   [AtCoder Educational DP Contest W - Intervals](https://atcoder.jp/contests/dp/tasks/dp_w)
-   [Codeforces 115 E. Linear Kingdom Races](https://codeforces.com/problemset/problem/115/E)

### CDQ divide-and-conquer optimization of DP

Main page: [CDQ divide-and-conquer optimization of DP](../../misc/cdq-divide.md#cdq-分治优化-1d1d-动态规划的转移)

Similar to before, treat the entire DP process as a series of query and modification operations. For some problems, computing them sequentially is too costly; we can process the entire query-and-modification process offline and use CDQ divide and conquer to speed up the computation.

CDQ divide-and-conquer optimization of DP is also common in the following kinds of problems:

-   [Slope-optimization DP based on CDQ divide and conquer](./slope.md#optimizing-dp-with-binary-search-cdq-or-balanced-trees)
-   [Divide-and-conquer optimization of slope-monotonicity DP](./quadrangle.md#divide-and-conquer)

### Binary-lifting optimization of DP

Related page: [binary lifting](../../basic/binary-lifting.md)

In some problems, we need to set the state $f(i)$ as the result obtained after performing $2^i$ transitions starting from the initial state. It uses the idea of binary lifting to transform the original problem, so it is often called binary-lifting optimization of DP.

Sometimes, DP problems with a state-transition equation similar to

$$
f(i,j) = f(i-1,f(i-1,j))
$$

are also called binary-lifting (optimization) DP.

Exercises:

-   [Luogu P1081 \[NOIP 2012 Advanced Group\] Driving Trip](https://www.luogu.com.cn/problem/P1081)
-   [Luogu P1613 Running Away](https://www.luogu.com.cn/problem/P1613)
-   [Luogu P4739 \[CERC2017\] Donut Drone](https://www.luogu.com.cn/problem/P4739)

## Optimizing with problem structure

Many dynamic-programming problems have structural properties such as convexity and monotonicity; reasonably exploiting these properties allows fast solving.

### Slope-optimization DP

Main page: [slope optimization](./slope.md)

Similar to the optimization method introduced in the previous section, exploiting the convexity of the problem, we can speed up a single transition by maintaining a convex hull.

### Quadrangle-inequality optimization of DP

Main page: [quadrangle-inequality optimization](./quadrangle.md)

DP problems where the functions involved satisfy the quadrangle inequality often have some kind of decision monotonicity. Exploiting this property, there are many specialized methods to reduce the computational complexity. Common problem types include one-dimensional decision-monotonicity problems, interval-partition problems, and interval-merging problems.

### Slope Trick optimization of DP

Main page: [Slope Trick](./slope-trick.md)

In some problems, the difference (i.e. the slope) of the state function is easier to maintain during the state transition. This optimization also often requires the problem to be convex.

### WQS binary search / convex optimization of DP

Main page: [WQS binary search](./wqs-binary-search.md)

For an optimization DP problem with a count restriction, if the problem is easier to solve without the count restriction, and the optimal value is a convex function of that restriction, then we can simplify the computation via the WQS binary-search method.

## Optimizing with mathematical methods

The transitions of many dynamic-programming problems can be sped up with mathematical tools.

### Matrix-fast-exponentiation optimization of DP

Related page: [fast exponentiation](../../math/binary-exponentiation.md)

If the state-transition equation of a DP problem can be written in an autonomous form

$$
f(i) = F(f(i-1)),
$$

that is, the current state $f(i)$ depends only on the previous state $f(i-1)$ and not on other inputs, then we can directly speed up the computation via fast exponentiation

$$
f(n) = F^n(f(0))
$$

to obtain the final answer. Since a single operation $F$ can often be written in matrix form, this optimization method is often called matrix-fast-exponentiation optimization of DP. In fact, any transformation satisfying associativity (i.e. any element in a [monoid](../../math/algebra/basic.md#groups)) can apply this method for speedup.

Exercises:

-   [Luogu P1397 \[NOI2013\] Matrix Game](https://www.luogu.com.cn/problem/P1397)
-   [Luogu P3176 \[HAOI2015\] Splitting a Digit String](https://www.luogu.com.cn/problem/P3176)
-   [Codeforces 576 D. Flights for Regular Customers](https://codeforces.com/problemset/problem/576/D)
-   [Luogu P6772 \[NOI2020\] Gourmet](https://www.luogu.com.cn/problem/P6772)

### FFT optimization of DP

Related page: [FFT](../../math/poly/fft.md)

If the state-transition equation of a DP problem is in the form of a convolution, then we can consider using FFT to speed up the transition. Of course, depending on the specific problem, other polynomial techniques may also be used.

Exercises:

-   [Codeforces 553 E. Kyoya and Train](https://codeforces.com/contest/553/problem/E)
-   [Codeforces 1784 D. Wooden Spoon](https://codeforces.com/problemset/problem/1784/D)

### Lagrange-interpolation optimization of DP

Related page: [Lagrange interpolation](../../math/numerical/interp.md#lagrange-插值法)

The state function $f(i,j)$ of some DP problems is a degree-$k$ polynomial function of $j$. In this case, we can directly brute-force compute its values at $k+1$ points and find the expression of $f(i,\cdot)$ via Lagrange interpolation, thereby optimizing the transition or even directly obtaining the answer.

Exercises:

-   [Luogu P5223 Function](https://www.luogu.com.cn/problem/P5223)
-   [Luogu P4463 \[Training Team Mutual Test 2012\] calc](https://www.luogu.com.cn/problem/P4463)
-   [Luogu P5469 \[NOI2019\] Robot](https://www.luogu.com.cn/problem/P5469)

## Optimizing by simplifying the state

Besides optimizing the transition, we can also reduce the computational complexity by simplifying the state.

### DP of DP and DFA minimization

Main pages: [DP of DP](../dp-of-dp.md), [DFA minimization](../../misc/fsm.md#dfa-最小化)

The state function of some DP problems can be written in the form $f(i,x)$, but the transition of $x$ itself is relatively complex, possibly even depending on another DP problem. For this kind of problem, we can first build an automaton for the transition of state $x$, reduce the number of states via DFA minimization, and then perform the outer DP.

### State-design optimization of DP

Main page: [state-design optimization](./state.md)

Some special problems can greatly reduce the number of states through clever state design.

## Further reading

-   [A Hodgepodge of DP Optimization Methods by Alex Wei](https://www.cnblogs.com/alex-wei/p/DP_Involution.html)
