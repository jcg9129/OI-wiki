This page briefly introduces the greedy algorithm.

## Introduction

A greedy algorithm uses a computer to simulate the decision-making process of a "greedy" person. This person is extremely greedy: at every step they always pick the operation that is optimal according to some metric. Moreover, they are short-sighted, always looking only at what is immediately before them and never considering the effects it may cause later.

As you can imagine, the greedy method does not always obtain the optimal solution, so in general, when using a greedy method, you must make sure you can prove its correctness.

## Explanation

### Scope of application

The greedy algorithm is especially effective on problems with optimal substructure. Optimal substructure means the problem can be decomposed into subproblems to be solved, and the optimal solutions of the subproblems can be recursed to the optimal solution of the final problem. [^ref1]

### Proof

There are two ways to prove a greedy algorithm: proof by contradiction and induction. In general, a single problem uses only one of these methods for its proof.

1.  Proof by contradiction: if swapping any two elements / any two adjacent elements in a solution does not make the answer better, then we can conclude that the current solution is already optimal.
2.  Induction: first compute the optimal solution $F_1$ of the boundary case (e.g. $n = 1$), then prove that for every $n$, $F_{n+1}$ can be derived from $F_{n}$.

## Key points

### Common problem types

Among problems below the "advanced group" difficulty, there are two most common types of greedy.

-   "We sort XXX by some order, then select according to some order (e.g. from small to large)."
-   "We repeatedly take the largest/smallest thing in XXX and update XXX." (Sometimes "the largest/smallest thing in XXX" can be optimized, for example maintained with a priority queue.)

The difference between the two is that one is offline—process first, then select—while the other is online—process and select at the same time.

### The sorting approach

The common situation for the sorting method is that the input is an array containing a few (usually one or two) weights, and the optimal value is found by sorting and then traversing to simulate the computation.

### The regret approach

The idea is to accept the current option regardless of whether it is optimal, then make a comparison; if after the selection it is no longer optimal, then regret and discard this option; otherwise, formally accept it. Repeat this back and forth.

## Differences

### The difference from dynamic programming

The greedy algorithm differs from dynamic programming in that it makes a choice for each subproblem's solution and cannot backtrack. Dynamic programming, on the other hand, saves previous computation results and makes the current choice based on those previous results, having a backtracking capability.

## Detailed worked examples

### An example of the adjacent-swap method

???+ note "[NOIP 2012 The King's Game](https://www.luogu.com.cn/problem/P1080)"
    On the occasion of country H's National Day, the King invites n ministers to play a prize game. First, he has each minister write an integer on their left and right hands respectively, and the King himself also writes an integer on each of his left and right hands. Then he has these n ministers line up in a row, with the King standing at the very front of the line. Once lined up, all the ministers receive some gold coins rewarded by the King; the number of gold coins each minister receives is: the product of the numbers on the left hands of everyone in front of that minister, divided by the number on that minister's own right hand, then rounded down.
    
    The King does not want any one minister to receive an especially large reward, so he wants you to help rearrange the order of the line so that the minister who receives the most reward receives as little as possible. Note that the King's position is always at the very front of the line.

??? note "Solution idea"
    Let the numbers on the left and right hands of the $i$-th minister after sorting be $a_i, b_i$ respectively. Consider deriving the greedy strategy via the adjacent-swap method.
    
    Let $s$ denote the product of $a_i$ over all people in front of the $i$-th minister; then the reward of the $i$-th minister is $\dfrac{s} {b_i}$, and the reward of the $(i+1)$-th minister is $\dfrac{s \cdot a_i} {b_{i+1}}$.
    
    If we swap the $i$-th minister with the $(i+1)$-th minister, then now the reward of the $i$-th minister is $\dfrac{s} {b_{i+1}}$, and the reward of the $(i+1)$-th minister is $\dfrac{s \cdot a_{i+1}} {b_i}$.
    
    The state before swapping is better if and only if
    
    $$
    \max \left(\dfrac{s} {b_i}, \dfrac{s \cdot a_i} {b_{i+1}}\right)  < \max \left(\dfrac{s} {b_{i+1}}, \dfrac{s \cdot a_{i+1}} {b_i}\right)
    $$
    
    Factoring out the common $s$ and cancelling gives
    
    $$
    \max \left(\dfrac{1} {b_i}, \dfrac{a_i} {b_{i+1}}\right)  < \max \left(\dfrac{1} {b_{i+1}}, \dfrac{a_{i+1}} {b_i}\right)
    $$
    
    Then clearing the fractions gives
    
    $$
    \max (b_{i+1}, a_i\cdot b_i)  < \max (b_i, a_{i+1}\cdot b_{i+1})
    $$
    
    In the implementation we save the two input numbers in a struct and overload the operator:
    
    ```cpp
    struct uv {
      int a, b;
    
      bool operator<(const uv &x) const {
        return max(x.b, a * b) < max(b, x.a * x.b);
      }
    };
    ```

### An example of the regret method

???+ note "["USACO09OPEN" Work Scheduling](https://www.luogu.com.cn/problem/P2949)"
    John's workday starts at time $0$ and has $10^9$ units of time. In any unit of time, he can choose to complete any one of $N(1 \leq N \leq 10^5)$ jobs numbered $1$ to $N$. Job $i$ has a deadline $D_i(1 \leq D_i \leq 10^9)$, and completing it yields a profit of $P_i( 1\leq P_i\leq 10^9 )$. Given the profits and deadlines of the jobs, find the maximum profit John can obtain.

??? note "Solution idea"
    1.  First assume every job is done, sort the jobs by deadline, and enqueue them;
    2.  When deciding whether to do the `i`-th job, if its deadline meets the condition, compare it with the element of smallest reward in the queue; if the `i`-th job has a higher reward (regret), then `ans += a[i].p - q.top()`.  
        Use a priority queue (min-heap) to keep the smallest element at the front.
    3.  When `a[i].d<=q.size()`, this can be understood as: during the time span from 0 to `a[i].d` only `a[i].d` tasks can be done, and if `q.size()>=a[i].d`, it means the time to complete `q.size()` tasks is greater than or equal to the time `a[i].d`, so when the `i`-th task has a larger profit we should swap the smallest task out of the priority queue.

??? note "Reference code"
    === "C++"
        ```cpp
        --8<-- "docs/basic/code/greedy/greedy_1.cpp"
        ```
    
    === "Python"
        ```python
        --8<-- "docs/basic/code/greedy/greedy_1.py"
        ```

??? note "Complexity analysis"
    -   Space complexity: with $n$ input tasks, $n$ elements of the array $a$ are used, and the priority queue stores at most $n$ elements in the worst case, so the space complexity is $O(n)$.
    -   Time complexity: the time complexity of `std::sort` is $O(n\log n)$, and the time complexity of maintaining the priority queue is $O(n\log n)$; in summary, the time complexity is $O(n\log n)$.

## Exercises

-   [P1209 \[USACO1.3\] Barn Repair - Luogu](https://www.luogu.com.cn/problem/P1209)
-   [P2123 The Queen's Game - Luogu](https://www.luogu.com.cn/problem/P2123)
-   [Problems tagged greedy on LeetCode](https://leetcode-cn.com/tag/greedy/)

## References and notes

[^ref1]: [Greedy algorithm - Wikipedia, the free encyclopedia](https://zh.wikipedia.org/wiki/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95)
