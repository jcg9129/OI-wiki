Prerequisite: [Prefix sum](./prefix-sum.md)

???+ warning "Reminder"
    This page is not about [**radix sort**](./radix-sort.md).

This page briefly introduces counting sort.

## Definition

Counting sort is a linear-time sorting algorithm.

## Process

Counting sort works by using an extra array $C$, whose $i$-th element is the number of elements in the array to be sorted, $A$, whose value equals $i$; it then uses the array $C$ to place the elements of $A$ into their correct positions. [^ref1]

Its workflow consists of three steps:

1.  Count how many times each number occurs;
2.  Compute the [prefix sums](./prefix-sum.md) of the occurrence counts of each number;
3.  Using the prefix sums of the occurrence counts, compute the rank of each number from right to left.

### Why compute the prefix sums

Directly placing the elements of $A$ corresponding to the positive entries of $C$ into $A$ one by one cannot handle the case of duplicate elements.

By computing a prefix sum for each entry of the extra array $C$ and combining it with each entry's value, we can determine a unique rank for duplicate elements:

The value of each entry of the extra array $C$ is the number of duplicate elements under that key, and the prefix sum of that entry is the rank of the last of those duplicate elements.

If we place the elements according to the reverse order of $A$, then clearly the sorted array will preserve the original order of $A$ (for equal keys), giving a stable sorting algorithm.

![counting sort animate example](images/counting-sort-animate.svg)

## Properties

### Stability

Counting sort is a stable sorting algorithm.

### Time complexity

The time complexity of counting sort is $O(n+w)$, where $w$ denotes the size of the value range of the data to be sorted.

## Implementation

### Pseudocode

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ positive integers no greater than } w. \\
2 & \textbf{Output. } \text{Array }A\text{ after sorting in nondecreasing order stably.} \\
3 & \textbf{Method. }  \\
4 & \textbf{for }i\gets0\textbf{ to }w\\
5 & \qquad \textit{cnt}[i]\gets0\\
6 & \textbf{for }i\gets1\textbf{ to }n\\
7 & \qquad \textit{cnt}[A[i]]\gets\textit{cnt}[A[i]]+1\\
8 & \textbf{for }i\gets1\textbf{ to }w\\
9 & \qquad \textit{cnt}[i]\gets \textit{cnt}[i]+\textit{cnt}[i-1]\\
10 & \textbf{for }i\gets n\textbf{ downto }1\\
11 & \qquad B[\textit{cnt}[A[i]]]\gets A[i]\\
12 & \qquad \textit{cnt}[A[i]]\gets \textit{cnt}[A[i]]-1\\
13 & \textbf{return } B
\end{array}
$$

=== "C++"
    ```cpp
    --8<-- "docs/basic/code/counting-sort/counting-sort_1.cpp"
    ```

=== "Python"
    ```python
    --8<-- "docs/basic/code/counting-sort/counting-sort_1.py:core"
    ```

## References and notes

[^ref1]: [Counting sort - Wikipedia, the free encyclopedia](https://zh.wikipedia.org/wiki/%E8%AE%A1%E6%95%B0%E6%8E%92%E5%BA%8F)
