Prerequisite: [Time complexity](./complexity.md)

This page introduces the basics of amortized complexity.

## Introduction

Amortized analysis is a technique for analyzing the performance of algorithms and dynamic data structures. It focuses not only on the cost of a single operation but also provides a more accurate assessment of overall performance by evaluating the average cost of a sequence of operations. Amortized analysis does not involve probability, and only guarantees the average time per operation for worst-case performance; it does not establish the system's average performance. In the worst case, amortized analysis spreads the cost of expensive operations over cheap operations, ensuring that the average cost of the overall operations stays within a reasonable range.

Amortized analysis usually adopts three main methods: aggregate analysis, the accounting method, and the potential method. Each has its own emphasis and applies to different scenarios, but their common goal is to optimize the overall worst-case performance of a data structure by balancing operation costs.

## Content

Consider a growable array, such as `vector` in C++, with an initial capacity of $m = 1$. Each time a new element is inserted, if the array is full, its size needs to be doubled, the elements of the original array are copied into the new array, and finally the new element is inserted.

Next, using the insertion operation of a dynamic array as an example, we analyze its amortized cost through the three methods: aggregate analysis, the accounting method, and the potential method.

### Aggregate analysis

Aggregate analysis computes the total cost of a sequence of operations and averages it over each operation, thereby deriving the amortized time complexity per operation.

Taking the dynamic array as an example, we first obtain the two key costs of the insertion operation:

-   If the array is not full, the cost of an insertion is $O(1)$.
-   If the array is full, the insertion requires expanding the array, and the cost of copying elements after expansion is $O(m)$, where $m$ is the current size of the array.

So, to compute the total cost of n insertions, we can split it into two parts:

1.  **Cost of the insertions**: the direct cost of inserting each new element is constant time $O(1)$; for $n$ operations, the total cost is $O(n)$.
2.  **Cost of array expansion**: each expansion involves copying the elements of the original array into the new array. These operations occur at the moments when the array size is $1, 2, 4, \ldots , 2^k$, where $2^k$ is the largest power less than or equal to $n$. The costs of the expansion operations are $1, 2, 4, \ldots , 2^{k-1}$ respectively, summing to $1 + 2 + 4 + \ldots  + 2^{k-1} = 2^k - 1$, which is the sum of a geometric series and equals $O(n)$.

Therefore, the total insertion cost of this array is $O(n)$, and the amortized cost per operation is $O(1)$. Even in the worst case, the average cost per insertion is still constant time.

### Accounting method

The accounting method pre-assigns a fixed amortized cost to each operation, ensuring that the total cost of all operations does not exceed the sum of these pre-assigned costs. The accounting method resembles a **prepayment** mechanism, in which lower-cost operations store part of the fee to pay for future high-cost operations.

Taking the dynamic array as an example, we can assign a fixed amortized cost to each insertion, ensuring that enough fee has been reserved by the time expansion is needed.

1.  **Fee assignment**:
    -   Suppose the actual cost of each insertion is $1$ and the amortized cost is set to $3$.
    -   Of these, $1$ is used for the current insertion, and $2$ is used for a possible future expansion.

2.  **Fee usage**:
    -   When the array is full, an expansion is needed, with an actual cost of $O(m)$, where $m$ is the current size of the array.
    -   Suppose the array holds $n$ elements before expansion. Since the latter half of the original array, $n/2$ elements, together prepaid $n$ units of amortized cost when inserted, this is exactly enough to pay for the cost of the expansion.

Here is a concrete example:

```text
Initial state:
arr    = [1, 2, 3, 4]  // initial array
amount = [2, 2, 2, 2]  // fee prepaid for each element

// First expansion: the array is full and needs to expand
arr    = [1, 2, 3, 4, null, null, null, null]  // array after expansion
amount = [2, 2, 0, 0, 0, 0, 0, 0]  // the fees of 3 and 4 pay for the expansion

// Continue inserting new elements until it is full again
arr    = [1, 2, 3, 4, 5, 6, 7, 8]  // continue filling the array
amount = [2, 2, 0, 0, 2, 2, 2, 2]  // newly inserted elements also prepay fees

// Second expansion: the array is full again and needs more space
arr    = [1, 2, 3, 4, 5, 6, 7, 8, null, null, null, null, null, null, null, null]  // array after expansion
amount = [2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  // the fees of 5, 6, 7, 8 pay for the expansion
```

The process above shows that the amortized cost stored by each insertion is enough to pay for future expansions, thereby keeping the amortized cost of each operation at $O(1)$.

### Potential method

The potential method defines a potential function (usually denoted $\Phi$) that measures the **potential energy** of a data structure — the reserved resources in the system state that can be used to pay for future high-cost operations. The change in potential is used to balance the total cost of a sequence of operations, ensuring that the overall amortized cost of the algorithm stays within a reasonable range.

#### Principle

First, define the **state** $S$ as the state of the data structure at some moment, which may include information such as the number of elements, capacity, and pointers; define the initial state as $S_0$, i.e. the state when no operations have been performed.

Next, define the potential function $\Phi(S)$ that measures the potential of the data structure in state $S$, satisfying the following two properties:

1.  **Initial potential**: in the initial state $S_0$ of the data structure, the potential is $\Phi(S_0) = 0$.
2.  **Non-negativity**: in any state $S$, the potential is $\Phi(S) \geq 0$.

For each operation, its amortized cost $\hat{c}$ is defined as:

$$
\hat{c} = c + \Phi(S') - \Phi(S)
$$

where $c$ is the actual cost of the operation, and $S$ and $S'$ denote the states of the data structure before and after the operation respectively. This formula shows that the amortized cost equals the actual cost plus the change in potential. If the operation increases the potential (i.e. $\Phi(S') > \Phi(S)$), the amortized cost rises; if the operation consumes potential (i.e. $\Phi(S') < \Phi(S)$), the amortized cost falls.

We can use the potential function to analyze the total cost of a sequence of operations. Let $S_1, S_2, \dots, S_m$ be the sequence of states produced by $m$ operations starting from the initial state $S_0$, and let $c_i$ be the actual cost of the $i$-th operation; then the amortized cost $p_i$ of the $i$-th operation is:

$$
p_i = c_i + \Phi(S_i) - \Phi(S_{i-1})
$$

Therefore, the total time cost of $m$ operations is:

$$
\sum_{i=1}^m c_i = \sum_{i=1}^m p_i + \Phi(S_0) - \Phi(S_m)
$$

Since $\Phi(S) \geq \Phi(S_0)$, an upper bound on the total time cost is:

$$
\sum_{i=1}^m p_i \geq \sum_{i=1}^m c_i
$$

Therefore, if $p_i = O(T(n))$, then $O(T(n))$ is an upper bound on the amortized complexity.

#### Example: expansion analysis of a dynamic array

Taking the insertion operation of a dynamic array `vector` as an example, define the following potential function $\Phi(h)$:

$$
\Phi(h) = 2n - m
$$

where $n$ is the number of elements in the array and $m$ is the current capacity of the array. This potential function reflects the amount of remaining available space in the array, i.e. the difference between the current capacity and the space actually used.

1.  **Insertion (no expansion needed)**:
    -   **Operation cost**: $O(1)$, since only one element is inserted.
    -   **Change in potential**: after insertion, the number of elements increases by 1 and the potential increases by $2$.
        -   $\Phi(h') - \Phi(h) = 2(n + 1) - m - (2n - m) = 2$
    -   **Amortized cost**: $1 + 2 = 3$

2.  **Insertion (triggers expansion)**:
    -   Suppose the current capacity is $m = n$; inserting a new element triggers expansion, and the new capacity becomes $2n$.
    -   **Operation cost**: $O(n)$, since all elements must be copied into the new array and the new element inserted.
    -   **Change in potential**: after expansion, the capacity increases and the potential decreases, with a change of $2 - n$.
        -   $\Phi(h') - \Phi(h) = 2(n + 1) - 2n - (2n - n) = 2 - n$
    -   **Amortized cost**: $n + 1 + (2 - n) = 3$

The analysis above shows that although the actual cost of the expansion operation is high, the design of the potential function keeps the overall amortized cost at the constant level $O(1)$.

## Extended example: stack operations

Stack operations are one of the classic applications of amortized analysis. Suppose a stack `S` supports the following three operations:

| Operation        | Description       | Actual cost $c_i$            |
| ---------------- | ----------------- | ---------------------------- |
| `S.push(x)`      | push element x    | $1$                          |
| `S.pop()`        | pop the top element | $1$                        |
| `S.multi-pop(k)` | pop the top k elements | $O(\min{\lvert S\rvert, k})$ |

We analyze the amortized cost of these stack operations through the three methods: aggregate analysis, the accounting method, and the potential method.

### Aggregate analysis

Aggregate analysis computes the total cost of all operations and averages it over each operation to derive the amortized cost.

1.  For $n_{push}$ `push(x)` operations, each costs $O(1)$, so the total cost is $O(n_{push})$.
2.  For $n_{pop}$ `pop()` operations, each costs $O(1)$, so the total cost is $O(n_{pop})$.
3.  For $n_{multi-pop}$ `multi-pop(k)` operations, although each has an actual cost of $O(\min(\lvert S \rvert, k))$, the number of elements popped by these operations cannot exceed the number of elements previously pushed by `push(x)`, so the total cost is still bounded by $n_{push}$.

Since the total number of operations $n = n_{push} + n_{pop} + n_{multi-pop} \leq 2 \times n_{push}$, the total cost is $O(n_{push}) = O(n)$, and the amortized cost per operation is $O(n)/n = O(1)$.

### Accounting method

The accounting method reserves part of the fee for each `push(x)` operation to pay for future `pop()` or `multi-pop(k)` operations.

1.  **`S.push(x)`**: suppose the amortized cost of each `push(x)` is $2$, of which $1$ unit is for the current operation and another $1$ unit is stored as a fee to pay for a future `pop()` or `multi-pop(k)`.
2.  **`S.pop()`**: the actual cost is $1$, but since the earlier `push(x)` operation already prepaid $1$ unit of fee for it, the amortized cost is $0$.
3.  **`S.multi-pop(k)`**: the actual cost of each popped element is $1$, which can be paid by the fee prepaid by that element's earlier `push(x)`, so the amortized cost is $0$.

From the analysis above, the fee prepaid by a push operation is enough to pay for that element's future pop operation, so the amortized cost of each operation is $O(1)$.

### Potential method

The potential method defines a potential function to measure the state of the stack and uses the change in potential to balance operation costs.

1.  **Potential function**: let $\Phi(h)$ be the number of elements in the stack, i.e. $\Phi(h) = \lvert S \rvert$. Each element contributes $1$ unit of potential.
2.  **`S.push(x)`**: each `push(x)` increases the number of elements in the stack and the potential by $1$, so the amortized cost is $1 + 1 = 2$.
3.  **`S.pop()`**: each `pop()` decreases the number of elements in the stack and the potential by $1$, so the amortized cost is $1 - 1 = 0$.
4.  **`S.multi-pop(k)`**: `multi-pop(k)` pops $k$ elements and decreases the potential by $k$, so the amortized cost is $k - k = 0$.

With this potential function, the amortized cost of `push(x)` is $2$, while that of `pop()` and `multi-pop(k)` is $0$. Therefore, the amortized cost of all stack operations is $O(1)$.

## References

-   [Amortized Analysis - Wikipedia](https://en.wikipedia.org/wiki/Amortized_analysis)
-   [Cornell CS 3110 - Lecture 20: Amortized Analysis](https://www.cs.cornell.edu/courses/cs3110/2011sp/Lectures/lec20-amortized/amortized.htm)
