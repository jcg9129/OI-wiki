This page briefly introduces insertion sort.

## Definition

Insertion sort is a simple and intuitive sorting algorithm. It works by dividing the elements to be sorted into two parts, "sorted" and "unsorted", and each time selecting one element from the "unsorted" elements and inserting it into its correct position among the "sorted" elements.

An operation identical to insertion sort occurs when playing cards: you draw a card from the table, insert it into your hand according to its face value, and then draw the next card.

![insertion sort animate example](images/insertion-sort-animate.svg)

## Properties

### Stability

Insertion sort is a stable sorting algorithm.

### Time complexity

The best-case time complexity of insertion sort is $O(n)$, and it is very efficient when the sequence is almost sorted.

The worst-case and average-case time complexities of insertion sort are both $O(n^2)$.

## Implementation

### Pseudocode

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ elements.} \\
2 & \textbf{Output. } A\text{ will be sorted in nondecreasing order stably.} \\
3 & \textbf{Method. }  \\
4 & \textbf{for } i\gets 2\textbf{ to }n\\
5 & \qquad key\gets A[i]\\
6 & \qquad j\gets i-1\\
7 & \qquad\textbf{while }j>0\textbf{ and }A[j]>key\\
8 & \qquad\qquad A[j + 1]\gets A[j]\\
9 & \qquad\qquad j\gets j - 1\\
10 & \qquad A[j + 1]\gets key
\end{array}
$$

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/insertion-sort/insertion-sort_1.cpp"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/insertion-sort/insertion-sort_1.py:core"
    ```

=== "Java"
    ```java
    --8<-- "docs/basic/code/insertion-sort/insertion-sort_1.java"
    ```

## Binary insertion sort

Insertion sort can also have its performance optimized via binary search; the optimization effect is more noticeable when the number of elements to sort is large.

### Time complexity

Binary insertion sort has the same basic idea as direct insertion sort; binary insertion sort only optimizes the constant in the time complexity of insertion sort, so the optimized time complexity remains unchanged.

### Implementation

=== "C++"
    ```cpp
    void insertion_sort(int arr[], int len) {
      if (len < 2) return;
      for (int i = 1; i != len; ++i) {
        int key = arr[i];
        auto index = upper_bound(arr, arr + i, key) - arr;
        // Using memmove to move elements is faster than using a for loop; the time complexity is still O(n)
        memmove(arr + index + 1, arr + index, (i - index) * sizeof(int));
        arr[index] = key;
      }
    }
    ```
