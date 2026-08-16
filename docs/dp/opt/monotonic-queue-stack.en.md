author: liujiaxi123456, Marcythm, hsfzLZH1, Ir1d, greyqz, Anguei, billchenchina, Chrogeek, ChungZH

## Introduction

Prerequisites: [monotonic queue](../../ds/monotonic-queue.md), [monotonic stack](../../ds/monotonic-stack.md).

A monotonic queue is mainly used to maintain the interval extremum where the two-end pointers are monotonically non-decreasing, while a monotonic stack is mainly used to maintain the first number before/after that is greater/less than the current value.

???+ note "Note"
    -   To find the minimum, maintain a **monotonically increasing / non-decreasing** monotonic queue/stack, and vice versa.
    -   When maintaining monotonically increasing/decreasing, compare with **less-than-or-equal / greater-than-or-equal**; when maintaining monotonically non-decreasing / non-increasing, compare with **less-than / greater-than**.

## Specific steps of monotonic-queue optimization

-   Add the required elements: repeatedly add elements to the monotonic queue until the current element reaches the right boundary of the desired interval, so that all required elements are in the monotonic queue.
-   Pop out-of-bounds front: the monotonic queue essentially maintains the extremum of all inserted elements, but what we usually want is an interval extremum. So we pop the elements outside the left boundary to ensure the elements in the monotonic queue are all within the desired interval.
-   Get the extremum: just take the front of the queue as the answer.

## Specific steps of monotonic-stack optimization

-   Pop the invalid top: by comparing the current element with the top of the stack, pop the top that does not satisfy the monotonic-stack property. Taking a monotonically increasing stack as an example (i.e. the top is the largest, maintaining the minimum), pop all elements in the stack that are greater than or equal to the current element.
-   Add the current element: just push the current element onto the stack.

## Optimizing the multiple knapsack with a monotonic queue

???+ note "Problem statement"
    You have $n$ items; each item has weight $w_i$, value $v_i$, and quantity $k_i$. You have a knapsack with a weight capacity of $W$; now you are required to select items with as large a total value as possible without exceeding the weight limit and put them into the knapsack. Find the maximum value.

If you do not understand knapsack DP, please first read [knapsack DP](../knapsack.md). Let $f_{i,j}$ denote the maximum value of packing the first $i$ items into a knapsack of capacity $j$; the naive transition equation is

$$
f_{i,j}=\max_{k=0}^{k_i}(f_{i-1,j-k\times w_i}+v_i\times k)
$$

Time complexity $O(W\sum k_i)$.

Consider optimizing the transition of $f_i$. For convenience of description, let $g_{x,y}=f_{i,x\times w_i+y},g'_{x,y}=f_{i-1,x\times w_i+y}$, where $0\le y \lt w_i$; then the transition equation can be expressed as:

$$
g_{x,y}=\max_{k=0}^{k_i}(g'_{x-k,y}+v_i\times k)
$$

Let $G_{x,y}=g'_{x,y}-v_i\times x$. Then the equation can be expressed as:

$$
g_{x,y}=\max_{k=0}^{k_i}(G_{x-k,y})+v_i\times x
$$

This is now transformed into a classic monotonic-queue-optimization form. $G_{x,y}$ can be computed in $O(1)$, so for a fixed $y$ we can compute $g_{x,y}$ in $O\left( \left\lfloor \dfrac{W}{w_i} \right\rfloor \right)$ time. Therefore the complexity of finding all $g_{x,y}$ is $O\left( \left\lfloor \dfrac{W}{w_i} \right\rfloor \right)\times O(w_i)=O(W)$. Thus the total complexity of this transition is reduced to $O(nW)$.

In the implementation, we need to enumerate $y$ first, so that when enumerating $x$ we can use the monotonic queue for optimization; the monotonic queue stores $x-k$, not $k$, so when using it we need to obtain the corresponding $G_{x-k,y}$ via `f[last][q.front() * w[i] + y] - q.front() * v[i]`. It is not hard to see that $x-k\in [x - k_i,x]$, so when enumerating $x$ we need to delete the elements in the queue that are not within this range.

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/opt/monotonic-queue-stack/monotonic-queue-stack_2.cpp"
    ```

## Exercises

???+ note "Example [CF372C Watching Fireworks is Fun](http://codeforces.com/problemset/problem/372/C)"
    Problem summary: there are $n$ positions in a town, and $m$ fireworks to be set off. The time the $i$-th firework is set off is $t_i$, and the position it is set off at is $a_i$. If, when the firework is set off, you are at position $x$, then you gain $b_i-|a_i-x|$ happiness points.
    
    Initially you can be at any position, and each unit of time you can move no more than $d$ units of distance. Now you need to maximize the happiness you can obtain.

Let $f_{i,j}$ denote the maximum happiness you can obtain when your position is $j$ at the time the $i$-th firework is set off.

Write the state-transition equation: $f_{i,j}=\max\{f_{i-1,k}+b_i-|a_i-j|\}$, where $j-(t_{i}-t_{i-1})\times d\le k\le j+(t_{i}-t_{i-1})\times d$.

Try to transform it:

Since a fixed constant $b_i$ appears inside the $\max$, we can move it outside.

$f_{i,j}=\max\{f_{i-1,k}+b_i-|a_i-j|\}=\max\{f_{i-1,k}-|a_i-j|\}+b_i$

If the values of $i$ and $j$ are fixed, then the value of $|a_i-j|$ is also fixed, and this part can also be moved outside.

Finally, the expression becomes:

$$
f_{i,j}=\max\{f_{i-1,k}-|a_i-j|\}+b_i=\max\{f_{i-1,k}\}-|a_i-j|+b_i
$$

Next consider monotonic-queue optimization. Since the $\max$ in the final expression is only related to the maximum of a continuous segment of the previous state, when computing the state value for a new $i$ we only need to construct the original $f_{i-1}$ into a monotonic queue and maintain it, so that it can compute the value of $\max\{f_{i-1,k}\}$ in amortized $O(1)$ time, and thus compute the value of $f_{i,j}$ from the formula.

The total time complexity is $O(nm)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/dp/code/opt/monotonic-queue-stack/monotonic-queue-stack_1.cpp"
    ```

-   ["Luogu P1886" Sliding Window](https://loj.ac/problem/10175)
-   ["NOI2005" Magnificent Waltz](https://www.luogu.com.cn/problem/P2254)
-   ["SCOI2010" Stock Trading](https://loj.ac/problem/10183)
