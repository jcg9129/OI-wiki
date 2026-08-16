## Introduction

What is a monotonic stack? As the name suggests, a monotonic stack is a stack structure that satisfies monotonicity. Compared with a monotonic queue, it only operates at one end.

For convenience of description, the following examples and pseudocode take maintaining a monotonically increasing stack of integers as an example.

## Process

### Insertion

When inserting an element into a monotonic stack, to maintain the stack's monotonicity, we need to pop the fewest elements while ensuring that after inserting this element at the top, the whole stack satisfies monotonicity.

For example, the elements in the stack from top to bottom are $\{0,11,45,81\}$.

![](images/monotonic-stack-before.svg)

When inserting the element $14$, to guarantee monotonicity we need to pop the elements $0,11$ in turn; after the operation the stack becomes $\{14,45,81\}$.

![](images/monotonic-stack-after.svg)

Described in pseudocode as follows:

???+ note "Implementation"
    ```text
    insert x
    while !sta.empty() && sta.top()<x
        sta.pop()
    sta.push(x)
    ```

### Use

Naturally, it is reading out an element from the top of the stack, which satisfies one end of the monotonicity.

For example, in the example, what is taken out is the minimum in the stack.

## Applications

??? note "[POJ3250 Bad Hair Day](http://poj.org/problem?id=3250)"
    There are $N$ cows lined up in a row from left to right, each cow having a height $h_i$; let there be $c_i$ cows between the $i$-th cow from the left and "the first cow to its right with height $≥h_i$", and find $\sum_{i=1}^{N} c_i$.

A relatively basic application is this problem, which is a simple application of a monotonic stack: record the position where each cow is popped; if it was never popped, take it as the farthest end, and with a little processing, the result required by the problem can be computed.

In addition, a monotonic stack can also be used to solve the RMQ problem offline.

We can sort all queries by right endpoint, and each time scan on the sequence from left to right up to the right endpoint of the current query, inserting the scanned elements into the monotonic stack. This way, each time we answer a query, the values stored in the monotonic stack are the decision points at positions $\le r$ that may become the answer, and these elements satisfy the monotonic property. At this point, the first element in the monotonic stack at a position $\ge l$ is the answer to the current query, and this process can be implemented with binary search. The time complexity of solving the RMQ problem with a monotonic stack is $O(q\log q + q\log n)$, and the space complexity is $O(n)$.

## Exercises

-   [Luogu P5788 【Template】Monotonic Stack](https://www.luogu.com.cn/problem/P5788)
-   [Luogu P1901 Launch Station](https://www.luogu.com.cn/problem/P1901)
