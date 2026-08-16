This page briefly introduces the uses of sorting.

## Understanding the characteristics of data

Using sorting to process data helps in understanding the characteristics of the data, facilitating our subsequent analysis and visualization. Take some everyday examples such as dictionaries and menus: if they were not arranged in a certain order, the time it takes people to find what they need would increase enormously.

Computers need to process large-scale data. After sorting, people can design the computer's subsequent processing flow according to the characteristics of the data and their needs.

## Reducing time complexity

Using sorting as preprocessing can reduce the time complexity required to solve a problem; it is usually a trade-off of space for time. If a sorted list needs to be analyzed many times, it is well worth spending the resources of sorting just once, because every subsequent analysis can then save a lot of time.

???+ note "Example: checking whether a given sequence has equal elements"
    Consider a sequence in which you need to check whether any elements are equal.
    
    A naive approach is to check every pair of numbers and determine whether the pair is equal. The time complexity is $O(n^2)$.
    
    We might as well first sort this list of numbers; afterward it is not hard to see that if there are two equal numbers, they must be at adjacent positions in the new sequence. Then it suffices to scan the new sequence once in $O(n)$.
    
    The total time complexity is the complexity of sorting, $O(n\log n)$.

## As preprocessing for searching

Sorting is the preprocessing work required by [binary search](./binary.md). Using binary search after sorting, one can find a specified element in a sequence in $O(\log n)$ time.
