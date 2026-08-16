This page briefly introduces sorting algorithms.

## Definition

A **sorting algorithm** is an algorithm that arranges a specific set of data in a certain order. Sorting algorithms are many and varied, and their properties mostly differ.

## Properties

### Stability

Stability refers to whether the relative order of equal elements changes after sorting.

An algorithm with the property of stability keeps records that originally have equal key values in their relative order; that is, if a sorting algorithm is stable, then when there are two records $R$ and $S$ with equal key values and $R$ appears before $S$ in the original list, $R$ will also be before $S$ in the sorted list.

Radix sort, counting sort, insertion sort, bubble sort, and merge sort are stable sorts.

Selection sort, heapsort, quicksort, and Shell sort are not stable sorts.

### Time complexity

Main page: [Complexity](./complexity.md)

Time complexity is used to measure the relationship between an algorithm's running time and the input size, usually denoted with $O$.

The simple way to compute complexity is generally to count the number of executions of "simple operations"; sometimes one can also directly count the number of nested loop levels for an approximate estimate.

Time complexity is divided into best-case time complexity, average-case time complexity, and worst-case time complexity. In OI contests, what generally needs to be considered is the worst-case time complexity, because it represents the lower bound of the algorithm's performance—no worse result will occur during judging.

The lower bound on the time complexity of comparison-based sorting algorithms is $O(n\log n)$.

Of course there are also ones that are not $O(n\log n)$. For example, the time complexity of [counting sort](./counting-sort.md) is $O(n+w)$, where $w$ denotes the size of the value range of the input data.

Below is a comparison of several sorting algorithms.

![comparison of several sorting algorithms](images/sort-intro-1.apng)

### Space complexity

Similar to time complexity, space complexity is used to describe the scale of an algorithm's space consumption. Generally speaking, the smaller the space complexity, the better the algorithm.

## External links

-   [Sorting algorithm - Wikipedia, the free encyclopedia](https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95)
