author: Link-cute, Xeonacid, ouuan, Alphnia, Lyccrius

## Introduction

Before learning about the monotonic queue, let's first look at an example.

???+ note "Example"
    [Sliding Window](http://poj.org/problem?id=2823)
    
    The gist of this problem is: given an array of length $n$, program to output the maximum and minimum of every $k$ consecutive numbers.

The most brute-force idea is very simple: for each segment $i \sim i+k-1$ of the sequence, compare one by one to find the maximum (and minimum), with time complexity about $O(n \times k)$.

Clearly, this involves a large amount of repeated work; except for the first $k-1$ and the last $k-1$ numbers, each number is compared $k$ times, and in this problem $100\%$ of the data has $n \le 1000000$; when $k$ is slightly larger, it will clearly TLE.

This is where the monotonic queue comes in.

## Definition

As the name suggests, the key points of a monotonic queue are "monotonic" and "queue".

"Monotonic" refers to the "pattern" of the elements—increasing (or decreasing).

"Queue" means the elements can only be operated on from the front and back of the queue.

Ps. The "queue" in a monotonic queue differs somewhat from a normal queue, as mentioned later.

## Example analysis

### Explanation

With the concept of "monotonic queue" above, it is easy to think of using a monotonic queue for optimization.

What is required is the maximum (minimum) of every $k$ consecutive numbers; clearly, when a number enters the range in which we want to "find" the maximum, if this number is larger than the numbers before it (which entered the queue earlier), then obviously the earlier numbers will leave the queue before this number and can no longer be the maximum.

That is—when the above condition is satisfied, we can "pop" the earlier numbers and then truly push this number onto the back of the queue.

This is equivalent to maintaining a decreasing queue, which conforms to the definition of a monotonic queue and reduces the number of repeated comparisons; not only that, since the maintained queue is within the query range and is decreasing, the front of the queue must be the maximum within that query region, so when outputting we only need to output the front of the queue.

It is obvious that in such an algorithm, each number only needs to enter and leave the queue once, so the time complexity is reduced to $O(n)$.

And since the length of the query interval is fixed, a value beyond the query range, no matter how large, cannot be output; therefore we also need a site array to record the position in the original array of the $i$-th number in the queue, in order to pop the out-of-range front of the queue.

### Process

For example, if we construct a monotonically increasing queue, it goes as follows:

The original sequence is:

```text
1 3 -1 -3 5 3 6 7
```

Because we must always maintain the queue to guarantee its **increasing** property, the following happens: (assuming $k = 3$)

| Operation                              | Queue state      |
| ------------------------------- | --------- |
| 1 enters the queue                            | `{1}`     |
| 3 is larger than 1, 3 enters                    | `{1 3}`   |
| -1 is smaller than all elements in the queue, so clear the queue and -1 enters       | `{-1}`    |
| -3 is smaller than all elements in the queue, so clear the queue and -3 enters       | `{-3}`    |
| 5 is larger than -3, directly enters                   | `{-3 5}`  |
| 3 is smaller than 5, 5 leaves, 3 enters               | `{-3 3}`  |
| -3 is already outside the window, so -3 leaves; 6 is larger than 3, 6 enters | `{3 6}`   |
| 7 is larger than 6, 7 enters                    | `{3 6 7}` |

???+ note "Example reference code"
    ```cpp
    --8<-- "docs/ds/code/monotonic-queue/monotonic-queue_1.cpp"
    ```

Ps. A major difference between the "queue" here and an ordinary queue is that it can be operated on from the back; the STL has a similar data structure, deque.

???+ note "Example 2 [Luogu P2698 Flowerpot S](https://www.luogu.com.cn/problem/P2698)"
    Given the coordinates of $N$ water drops, where $y$ is the drop's height and $x$ is the position where it falls onto the $x$-axis. Each drop falls at a speed of 1 unit of length per second. You need to place a flowerpot at some position on the $x$-axis so that from the first drop caught by the flowerpot to the last drop caught by the flowerpot, the time difference is at least $D$.
    We consider a drop caught as long as it falls onto the $x$-axis aligned with the edge of the flowerpot. Given the coordinates of the $N$ drops and the value of $D$, compute the minimum flowerpot width $W$. $1\leq N \leq 100000 , 1 \leq D \leq 1000000, 0 \leq x,y\leq 10^6$

After sorting all water drops by $x$-coordinate, the problem can be transformed into finding an interval with the smallest $x$-coordinate difference such that the difference between the maximum and minimum $y$-coordinate within this interval is at least $D$. We find this problem has similarities to the previous example, in that both are related to the maximum and minimum within an interval; but in this problem the size of the interval is uncertain, and moreover the interval size itself is the answer we are asked for.

We can still use two monotonic queues, one increasing and one decreasing, to maintain the maximum and minimum within $[L,R]$ as $R$ keeps moving backward; but now we find that if $L$ is fixed, then the maximum within $[L,R]$ only increases and the minimum only decreases, so letting $f(R) = \max[L,R]-\min[L,R]$, then $f(R)$ is an increasing function of $R$, so $f(R)\geq D \implies f(r)\geq D,R\lt r \leq N$. This shows that for each fixed $L$, the first $R$ to the right that satisfies the condition is the optimal answer.
So our overall solving process is: first fix $L$, move $R$ from front to back, and use two monotonic queues to maintain the extrema of $[L,R]$. When the first $R$ satisfying the condition is found, update the answer and move $L$ backward as well. As $L$ moves backward, both monotonic queues must pop their fronts in time. This way, until $R$ moves to the end, each element still enters and leaves the queue once, guaranteeing $O(n)$ time complexity.

???+ note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/monotonic-queue/monotonic-queue_2.cpp"
    ```
