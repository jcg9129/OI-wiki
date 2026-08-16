This page briefly introduces selection sort.

## Definition

Selection sort is a simple and intuitive sorting algorithm. It works by finding, each time, the $i$-th smallest element (that is, the smallest element in $A_{i..n}$), and then swapping this element with the element at the $i$-th position of the array.

![selection sort animate example](images/selection-sort-animate.svg)

## Properties

### Stability

The stability of selection sort depends on its specific implementation.

If implemented with a linked list, since insertion and deletion at any position of a linked list are $O(1)$, there is no need for a swap (exchanging two elements) operation: each time, after selecting the smallest element from the unsorted part (if there are several, take the first one), insert it before the first element of the unsorted part; this guarantees stability.

If implemented with an array (the usual implementation in OI), since insertion and deletion at any position of an array are $O(n)$, one can only use swap to move an element of the unsorted part into the sorted part. The swap operation makes the array-implemented selection sort unstable.

The implementation examples given below are all based on swapping array elements, and are therefore all **unstable**.

### Time complexity

The best-case, average-case, and worst-case time complexities of selection sort are all $O(n^2)$.

## Implementation

### Pseudocode

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ elements.} \\
2 & \textbf{Output. } A\text{ will be sorted in nondecreasing order.} \\
3 & \textbf{Method. }  \\
4 & \textbf{for } i\gets 1\textbf{ to }n-1\\
5 & \qquad ith\gets i\\
6 & \qquad \textbf{for }j\gets i+1\textbf{ to }n\\
7 & \qquad\qquad\textbf{if }A[j]<A[ith]\\
8 & \qquad\qquad\qquad ith\gets j\\
9 & \qquad \text{swap }A[i]\text{ and }A[ith]\\
\end{array}
$$

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/selection-sort/selection-sort_1.cpp"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/selection-sort/selection-sort_1.py:core"
    ```

=== "Java"
    ```java
    // arr is indexed starting from 1
    static void selection_sort(int[] arr, int n) {
        for (int i = 1; i < n; i++) {
            int ith = i;
            for (int j = i + 1; j <= n; j++) {
                if (arr[j] < arr[ith]) {
                    ith = j;
                }
            }
            // swap
            int temp = arr[i];
            arr[i] = arr[ith];
            arr[ith] = temp;
        }
    }
    ```
