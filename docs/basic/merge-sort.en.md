## Definition

Merge sort ([merge sort](https://en.wikipedia.org/wiki/Merge_sort)) is an efficient, comparison-based, stable sorting algorithm.

## Properties

Merge sort is based on the divide-and-conquer idea: it sorts segments of the array and then merges them. Its time complexity is $\Theta (n \log n)$ in the best, worst, and average cases, and its space complexity is $\Theta (n)$.

Merge sort can use only $\Theta (1)$ auxiliary space, but for convenience an auxiliary array of the same length as the original array is usually used.

## Process

### Merging

The most core part of merge sort is the merge process: merging two sorted arrays `a[i]` and `b[j]` into one sorted array `c[k]`.

Enumerate `a[i]` and `b[j]` from left to right, find the smallest value and place it into the array `c[k]`; repeat the process until one of `a[i]` and `b[j]` is empty, then place the remaining elements of the other array into `c[k]`.

To guarantee the stability of the sort, the head element of the front segment should be placed into `c[k]` as the minimum when it is less than or equal to the head element of the back segment (`a[i] <= b[j]`), not merely when it is less than it (`a[i] < b[j]`).

#### Implementation

=== "C/C++"
    === "Array implementation"
        ```cpp
        void merge(const int *a, size_t aLen, const int *b, size_t bLen, int *c) {
          size_t i = 0, j = 0, k = 0;
          while (i < aLen && j < bLen) {
            if (b[j] < a[i]) {  // <!> check b[j] < a[i] first, to guarantee stability
              c[k] = b[j];
              ++j;
            } else {
              c[k] = a[i];
              ++i;
            }
            ++k;
          }
          // At this point one array is empty and the other is not; merge the non-empty array into c
          for (; i < aLen; ++i, ++k) c[k] = a[i];
          for (; j < bLen; ++j, ++k) c[k] = b[j];
        }
        ```
    
    === "Pointer implementation"
        ```cpp
        void merge(const int *aBegin, const int *aEnd, const int *bBegin,
                   const int *bEnd, int *c) {
          while (aBegin != aEnd && bBegin != bEnd) {
            if (*bBegin < *aBegin) {
              *c = *bBegin;
              ++bBegin;
            } else {
              *c = *aBegin;
              ++aBegin;
            }
            ++c;
          }
          for (; aBegin != aEnd; ++aBegin, ++c) *c = *aBegin;
          for (; bBegin != bEnd; ++bBegin, ++c) *c = *bBegin;
        }
        ```
    
    You can also use the `merge` function from the `<algorithm>` library; its usage is the same as the pointer-style version above.

=== "Python"
    ```python
    def merge(a, b):
        i, j = 0, 0
        c = []
        while i < len(a) and j < len(b):
            # <!> check b[j] < a[i] first, to guarantee stability
            if b[j] < a[i]:
                c.append(b[j])
                j += 1
            else:
                c.append(a[i])
                i += 1
        # At this point one array is empty and the other is not; merge the non-empty array into c
        c.extend(a[i:])
        c.extend(b[j:])
        return c
    ```

### Implementing merge sort with divide and conquer

1.  When the array length is $1$, the array is already sorted and does not need to be decomposed further.

2.  When the array length is greater than $1$, the array is very likely not sorted. In this case, divide the array into two segments, then check whether each of the two arrays is sorted (using rule 1). If sorted, merge them into one sorted array; otherwise repeat rule 2 on the unsorted array, then merge.

Mathematical induction can prove that this process can turn an array into a sorted array.

To guarantee the complexity of the sort, the array is usually divided into two segments as equal in length as possible ($mid = \left\lfloor \dfrac{l + r}{2} \right\rfloor$).

#### Implementation

Note that the intervals represented by the code below are $[l, r)$, $[l, mid)$, and $[mid, r)$ respectively.

=== "C/C++"
    ```cpp
    void merge_sort(int *a, int l, int r) {
      if (r - l <= 1) return;
      // Decompose
      int mid = l + ((r - l) >> 1);
      merge_sort(a, l, mid), merge_sort(a, mid, r);
      // Merge
      int tmp[1024] = {};  // set the length of the tmp array (same as a) according to the actual
                           // situation, or use a vector; first put the merged result in tmp, then
                           // copy it back to array a
      merge(a + l, a + mid, a + mid, a + r, tmp + l);  // pointer-style merge
      for (int i = l; i < r; ++i) a[i] = tmp[i];
    }
    ```

=== "Python"
    ```python
    def merge_sort(a, ll, rr):
        if rr - ll <= 1:
            return
        # Decompose
        mid = (rr + ll) // 2
        merge_sort(a, ll, mid)
        merge_sort(a, mid, rr)
        # Merge
        a[ll:rr] = merge(a[ll:mid], a[mid:rr])
    ```

### Implementing merge sort with the doubling method

We know that when the array length is $1$, the array is already sorted.

Cut the whole array into segments of length $1$.

From left to right, merge two sorted segments of length $1$ one after another, obtaining a series of sorted segments of length $\le 2$;

From left to right, merge two sorted segments of length $\le 2$ one after another, obtaining a series of sorted segments of length $\le 4$;

From left to right, merge two sorted segments of length $\le 4$ one after another, obtaining a series of sorted segments of length $\le 8$;

……

Repeat the process until the array has only one sorted segment left, which is the sorted original array.

???+ note "Why $\le n$ instead of $= n$"
    The length of the array is very likely not $2^x$, in which case an incomplete segment may appear at the end, and it is possible for the last segment to be standalone.

#### Implementation

=== "C/C++"
    ```cpp
    void merge_sort(int *a, size_t n) {
      int tmp[1024] = {};  // set the length of the tmp array (same as a) according to the actual
                           // situation, or use a vector; first put the merged result in tmp, then
                           // copy it back to array a
      for (size_t seg = 1; seg < n; seg <<= 1) {
        for (size_t left1 = 0; left1 < n - seg;
             left1 += seg + seg) {  // n - seg: no need to merge if only one segment remains at the end
          size_t right1 = left1 + seg;
          size_t left2 = right1;
          size_t right2 = std::min(left2 + seg, n);  // <!> mind the boundary of the last segment
          merge(a + left1, a + right1, a + left2, a + right2,
                tmp + left1);  // pointer-style merge
          for (size_t i = left1; i < right2; ++i) a[i] = tmp[i];
        }
      }
    }
    ```

=== "Python"
    ```python
    def merge_sort(a):
        seg = 1
        while seg < len(a):
            for l1 in range(0, len(a) - seg, seg + seg):
                r1 = l1 + seg
                l2 = r1
                r2 = l2 + seg
                a[l1:r2] = merge(a[l1:r1], a[l2:r2])
        seg <<= 1
    ```

## Inversions

Related reading and reference implementation: [Inversions](../math/permutation.md#逆序数)

An inversion is an ordered pair $(i, j)$ with $i < j$ and $a_i > a_j$.

A sorted array has no inversions. In the merge operation of merge sort, each time the head element of the back segment is taken out as the current minimum, the total number of remaining elements in the front segment is the number of inversions the merge operation removes; hence the time complexity of counting inversions with merge sort is $\Theta (n \log n)$. In addition, counting inversions can also be solved with a Fenwick tree or segment tree, also in time complexity $O(n \log n)$; for a detailed explanation of this algorithm, see the corresponding description in [Fenwick tree](../ds/fenwick.md#global-inversions-global-2d-dominance). Reference implementations of both algorithms are in the [Inversions](../math/permutation.md#逆序数) section.

## External links

-   [Merge Sort - GeeksforGeeks](https://www.geeksforgeeks.org/merge-sort/)
-   [Merge sort - Wikipedia, the free encyclopedia](https://zh.wikipedia.org/wiki/%E5%BD%92%E5%B9%B6%E6%8E%92%E5%BA%8F)
-   [Inversion - Wikipedia, the free encyclopedia](https://zh.wikipedia.org/wiki/%E9%80%86%E5%BA%8F%E5%AF%B9)
