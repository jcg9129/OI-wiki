This page briefly introduces bubble sort.

## Definition

Bubble sort is a simple sorting algorithm. During the execution of the algorithm, smaller elements slowly "float" to the top of the sequence like bubbles, which is why it is called bubble sort.

## Process

It works by checking two adjacent elements each time, and swapping them if the preceding element and the following element satisfy the given ordering condition. When there are no adjacent elements left to swap, the sort is complete.

After $i$ passes, the last $i$ items of the sequence are necessarily the largest $i$ items, so bubble sort needs to scan the array at most $n-1$ times to finish sorting.

## Properties

### Stability

Bubble sort is a stable sorting algorithm.

### Time complexity

When the sequence is already fully sorted, bubble sort only needs to traverse the array once without performing any swaps, giving a time complexity of $O(n)$.

In the worst case, bubble sort performs $\frac{(n-1)n}{2}$ swaps, giving a time complexity of $O(n^2)$.

The average time complexity of bubble sort is $O(n^2)$.

## Implementation

### Pseudocode

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ elements.} \\
2 & \textbf{Output. } A\text{ will be sorted in nondecreasing order stably.} \\
3 & \textbf{Method. }  \\
4 & flag\gets True\\
5 & \textbf{while }flag\\
6 & \qquad flag\gets False\\
7 & \qquad\textbf{for }i\gets1\textbf{ to }n-1\\
8 & \qquad\qquad\textbf{if }A[i]>A[i + 1]\\
9 & \qquad\qquad\qquad flag\gets True\\
10 & \qquad\qquad\qquad \text{Swap } A[i]\text{ and }A[i + 1]
\end{array}
$$

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/bubble-sort/bubble-sort_1.cpp"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/bubble-sort/bubble-sort_1.py:core"
    ```

=== "Java"
    ```java
    // Assume the array size is n + 1; bubble sort starts from array index 1
    static void bubble_sort(int[] a, int n) {
        boolean flag = true;
        while (flag) {
            flag = false;
            for (int i = 1; i < n; i++) {
                if (a[i] > a[i + 1]) {
                    flag = true;
                    int t = a[i];
                    a[i] = a[i + 1];
                    a[i + 1] = t;
                }
            }
        }
    }
    ```
