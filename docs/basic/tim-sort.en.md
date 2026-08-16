This page introduces Tim sort (Timsort), a hybrid, stable sorting algorithm.

## Introduction

Timsort was designed by Python core developer Tim Peters in 2002 and applied in the Python language. It cleverly combines the advantages of insertion sort and merge sort, precisely optimizing for the orderedness within a dataset, and is especially suited for handling datasets containing many partially sorted subsequences. Since Python version 2.3, Timsort has been chosen as the default sorting algorithm of the Python standard library, and it is widely used in other programming environments—for example, it is used in Java SE 7 to sort arrays of non-primitive objects.

## Steps

The core idea of Timsort is to improve sorting efficiency by identifying and exploiting the orderedness already present in a dataset; it mainly includes the following steps:

1.  **Identify runs**: Scan the array to be sorted and identify ordered contiguous subsequences (runs).
2.  **Extend runs**: If an identified run's length is less than `MIN_RUN`, use insertion sort to extend it.
3.  **Merge runs**: Timsort maintains a special stack and uses a specific merging strategy to merge the runs already on the stack into larger ordered sequences.

### Identifying runs

First, Timsort scans the array from left to right and identifies contiguous ordered sequences; these ordered sequences are called runs:

-   **Ascending run**: If the latter element is greater than or equal to the former element, continue extending the run.
-   **Descending run**: If the latter element is less than the former element, continue extending the run, and then reverse the run into ascending order.

### Extending runs

To improve sorting efficiency for small-scale data, Timsort introduces a minimum run length `MIN_RUN`. Its value is generally computed dynamically based on the length of the array to be sorted, usually between $32$ and $64$.

-   If an identified run's length is greater than or equal to `MIN_RUN`, no extra operation is needed and the run is directly pushed onto the stack.
-   If an identified run's length is less than `MIN_RUN`, use binary insertion sort to insert the subsequent elements into the run until the run's length reaches `MIN_RUN`, and then push it onto the stack.

### Merging runs

In Timsort, the merge sort is managed and controlled through a **stack**. The stack holds the ordered runs that have been identified, and the merging of runs on the stack is controlled by specific merge rules whose purpose is to maintain the balance and stability of the sequence during merging.

#### Merge rules

Timsort is a stable sorting algorithm, i.e. identical elements retain their original relative order after sorting. To ensure this, Timsort only merges adjacent, contiguous runs when merging, and does not directly merge non-adjacent runs. This is because there may be identical elements between non-adjacent runs, and merging them directly could very likely disturb their relative order.

At the same time, to ensure the balance of merging, Timsort introduces specific merge rules. Before each merge operation, the algorithm checks the top three runs X, Y, and Z on the stack to ensure the following two conditions are satisfied:

-   **Condition one**: `len(Z) > len(Y) + len(X)`
-   **Condition two**: `len(Y) > len(X)`

If the top three runs on the stack do not satisfy the above conditions, Timsort merges Y with the smaller of X and Z, and then checks the conditions again. Once the conditions are satisfied, it continues searching for a new run, adds it to the stack, and begins the next round of merging.

![Merge Rules](./images/tim-sort-1.png)

#### Merge optimization

To improve efficiency and reduce space overhead when merging runs of different lengths, Timsort, before merging, precisely locates the range of elements that need to be processed via binary search, and only merges the parts that need to move. The specific method is:

1.  **Determine insertion points**: Use binary search to find the insertion position of the first element of the second run within the first run, and the insertion position of the last element of the first run within the second run. This narrows the range that needs to be merged, processing only the elements that need to move.

2.  **Temporary buffer**: The traditional in-place merge algorithm is too inefficient and requires a large number of element moves. To reduce this overhead, Timsort uses a temporary buffer, copying the shorter run into the buffer and then gradually copying elements from the buffer back into the original array.

For example, suppose there are two runs A and B, respectively:

-   Run A: $[1, 2, 3, 6, 10]$
-   Run B: $[4, 5, 7, 9, 12, 14, 17]$

Through binary search, we can determine:

-   Element $4$ should be inserted at the fourth position of Run A.
-   Element $10$ should be inserted at the fifth position of Run B.

Therefore, the first $3$ elements of Run A and the last $3$ elements of Run B are already in the correct positions and need no processing. We only need to merge $[6, 10]$ of Run A and $[4, 5, 7, 9]$ of Run B; the merging process is shown in the figure below:

![Timsort Merge](./images/tim-sort-2.apng)

#### Galloping mode

To further improve merge efficiency, Timsort introduces **galloping mode**. In the standard merge process, the algorithm compares the elements of the two runs one by one and puts the smaller element into the result array. However, if one side's run has a large number of consecutive elements smaller than the current element of the other side, comparing them one by one causes unnecessary overhead.

To solve this problem, Timsort sets a threshold `Min_Gallop` (default value $7$). When the number of consecutive winning comparisons of elements from one side's run reaches `Min_Gallop`, the algorithm enters galloping mode to quickly locate element positions. The specific steps are as follows:

1.  **Exponential search**: Starting from the current position, the algorithm searches within one side's run with exponentially increasing step sizes $(1, 2, 4, 8, \dots)$ until it finds an interval such that the target element lies within it.
2.  **Binary search**: Once the interval containing the target element is determined, the algorithm uses binary search within that interval to precisely locate the position of the target element.

In this way, Timsort can skip a large number of unnecessary comparisons, quickly process consecutive smaller (or larger) elements in one side's run, and move them in bulk into the merged result.

However, galloping mode is not more efficient in all situations. Under certain data distributions, galloping mode may lead to more comparisons. For this reason, Timsort adopts a dynamic-adjustment strategy:

-   **Threshold adjustment**: Maintain a variable `Min_Gallop` parameter. When galloping mode performs well (i.e. elements are selected from the same run many times in a row), `Min_Gallop` decreases by $1$, encouraging continued use of galloping mode; when galloping mode performs poorly (frequently switching between the two runs), `Min_Gallop` increases by $1$, reducing the frequency of using galloping mode.

By dynamically adjusting the value of `Min_Gallop`, the algorithm can strike a balance between the normal merge mode and galloping mode according to the actual data. For partially ordered or highly ordered data, galloping mode can significantly improve efficiency, making Timsort's performance approach $O(n)$; for random data, the algorithm gradually leans toward using normal merging, thereby guaranteeing an $O(n \log n)$ time complexity.

## Complexity

The time complexity of Timsort depends on the orderedness of the data:

-   **Best case**: $O(n)$
    -   When the data is already sorted or nearly sorted, the runs identified by the algorithm have lengths close to $n$, the number of merges decreases, and the complexity approaches $O(n)$.
-   **Worst case**: $O(n \log n)$
    -   When the data is completely unordered, each run's length is close to $1$, so $O(\log n)$ merges are needed, each merge costing $O(n)$, for a total complexity of $O(n \log n)$.

**Proof**:

-   **Identifying and extending runs**:
    -   Identifying runs requires one linear traversal of the array, with complexity $O(n)$.
    -   Extending runs using insertion sort also requires a linear traversal of the array, with complexity $O(n)$.

-   **Merging runs**:
    -   The total number of merge operations is related to the total number of runs; in the worst case the number of runs is `n / MIN_RUN`, and since `MIN_RUN` is a constant, the number of runs can be regarded as $O(n)$.
    -   The number of merges needed for $O(n)$ runs is $O(\log n)$, and each merge operation costs $O(n)$, so the total complexity of the merge operations is $O(n \log n)$.

As for space complexity, since Timsort roughly requires an additional $O(n)$ space to store the stack and the temporary buffer, the total space complexity is $O(n)$.

## Implementation

???+ note "Pseudocode implementation"
    $$
    \begin{array}{ll}
    1 & nRemaining \gets \text{array length} \\
    2 & minRun \gets \text{choose a suitable MinRun value}(nRemaining) \\
    3 & startIndex \gets 0 \\
    4 & \textbf{while } nRemaining > 0 \ \textbf{do} \\
    5 & \qquad runLength \gets \text{identify run}(array, startIndex, nRemaining) \\
    6 & \qquad \textbf{if } runLength < minRun \ \textbf{then} \\
    7 & \qquad \qquad extendLength \gets \min(minRun, nRemaining) \\
    8 & \qquad \qquad \text{extend the interval } [startIndex, startIndex + extendLength - 1] \text{ using insertion sort}\\
    9 & \qquad \qquad runLength \gets extendLength \\
    10 & \qquad \textbf{end if} \\
    11 & \qquad \text{push run } (startIndex, runLength) \text{ onto the stack} \\
    12 & \qquad \textbf{call } \text{mergeCollapse(stack)} \ \text{to check and merge the runs on the stack} \\
    13 & \qquad startIndex \gets startIndex + runLength \ \text{update the start position} \\
    14 & \qquad nRemaining \gets nRemaining - runLength \ \text{update the remaining length} \\
    15 & \textbf{end while} \\
    16 & \textbf{call } \text{mergeForceCollapse(stack)} \ \text{to do the final merge of all runs on the stack} \\
    \end{array}
    $$

## References

1.  [Timsort](https://en.wikipedia.org/wiki/Timsort)
2.  [On the Worst-Case Complexity of TimSort](https://drops.dagstuhl.de/opus/volltexte/2018/9467/pdf/LIPIcs-ESA-2018-4.pdf)
3.  [Original Explanation by Tim Peters](https://github.com/python/cpython/blob/main/Objects/listsort.txt)
4.  [Java implementation](https://cs.android.com/android/platform/superproject/main/+/main:libcore/ojluni/src/main/java/java/util/TimSort.java)
5.  [C implementation](https://github.com/python/cpython/blob/main/Objects/listobject.c)
