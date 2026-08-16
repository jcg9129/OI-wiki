This page briefly introduces quicksort.

## Definition

Quicksort, also called partition-exchange sort, is a widely used sorting algorithm.

## Basic principle and implementation

### Process

Quicksort works by sorting an array using [divide and conquer](./divide-and-conquer.md).

Quicksort consists of three processes:

1.  Partition the sequence into two parts (the relative magnitude relationship must be guaranteed);
2.  Recurse into the two subsequences and perform quicksort on each;
3.  No merging is needed, because at this point the sequence is already fully sorted.

Unlike merge sort, the first step does not directly split into a front and back sequence; instead, the relative magnitude relationship must be guaranteed during the split. Specifically, the first step is to split the sequence into two parts, and then guarantee that all numbers in the first subsequence are smaller than all numbers in the second subsequence. To guarantee the average time complexity, a number $m$ is generally chosen at random to serve as the boundary between the two subsequences.

After that, maintain two pointers, $p$ in front and $q$ behind, and consider one by one whether the current number is placed in the position it should be (front or back). If the current number is not placed correctly—for example, if the back pointer $q$ encounters a number smaller than $m$—then we can swap the numbers at positions $p$ and $q$, and then move $p$ one step forward. Once the current number is placed correctly, move the pointers to continue processing, until the two pointers meet.

In fact, quicksort does not specify exactly how to implement the first step; there is more than one implementation method both for the process of choosing $m$ and for the process of partitioning.

The sequences in the third step are already sorted separately and all numbers in the first sequence are smaller than those in the second, so simply concatenating them is fine.

=== "C++"
    === "Iterative implementation[^ref2]"
        ```cpp
        struct Range {
          int start, end;
        
          Range(int s = 0, int e = 0) { start = s, end = e; }
        };
        
        template <typename T>
        void quick_sort(T arr[], const int len) {
          if (len <= 0) return;
          Range r[len];
          int p = 0;
          r[p++] = Range(0, len - 1);
          while (p) {
            Range range = r[--p];
            if (range.start >= range.end) continue;
            T mid = arr[range.end];
            int left = range.start, right = range.end - 1;
            while (left < right) {
              while (arr[left] < mid && left < right) left++;
              while (arr[right] >= mid && left < right) right--;
              std::swap(arr[left], arr[right]);
            }
            if (arr[left] >= arr[range.end])
              std::swap(arr[left], arr[range.end]);
            else
              left++;
            r[p++] = Range(range.start, left - 1);
            r[p++] = Range(left + 1, range.end);
          }
        }
        ```
    
    === "Recursive implementation"
        ```cpp
        template <typename T>
        int Partition(T A[], int low, int high) {
          int pivot = A[low];
          while (low < high) {
            while (low < high && pivot <= A[high]) --high;
            A[low] = A[high];
            while (low < high && A[low] <= pivot) ++low;
            A[high] = A[low];
          }
          A[low] = pivot;
          return low;
        }
        
        template <typename T>
        void QuickSort(T A[], int low, int high) {
          if (low < high) {
            int pivot = Partition(A, low, high);
            QuickSort(A, low, pivot - 1);
            QuickSort(A, pivot + 1, high);
          }
        }
        
        template <typename T>
        void QuickSort(T A[], int len) {
          QuickSort(A, 0, len - 1);
        }
        ```

=== "Python[^ref2]"
    ```python
    def quick_sort(alist, first, last):
        if first >= last:
            return
        mid_value = alist[first]
        low = first
        high = last
        while low < high:
            while low < high and alist[high] >= mid_value:
                high -= 1
            alist[low] = alist[high]
            while low < high and alist[low] < mid_value:
                low += 1
            alist[high] = alist[low]
        alist[low] = mid_value
        quick_sort(alist, first, low - 1)
        quick_sort(alist, low + 1, last)
    ```

## Properties

### Stability

Quicksort is an unstable sorting algorithm.

### Time complexity

The best-case and average-case time complexities of quicksort are $O(n\log n)$, and its worst-case time complexity is $O(n^2)$.

For the best case, the boundary value chosen each time is the median of the sequence, and the recurrence satisfied by the algorithm's time complexity is $T(n) = 2T(\dfrac{n}{2}) + \Theta(n)$; by the Master Theorem, $T(n) = \Theta(n\log n)$.

For the worst case, the boundary value chosen each time is the extremum of the sequence, and the recurrence satisfied by the algorithm's time complexity is $T(n) = T(n - 1) + \Theta(n)$; summing gives $T(n) = \Theta(n^2)$.

For the average case, the boundary value chosen each time can be regarded as uniformly random.

??? note "Proof"
    Below we prove that the algorithm's time complexity in this case is $O(n\log n)$.
    
    **Lemma 1:** When quicksorting an array of $n$ elements, suppose the total number of comparisons during the partitioning of elements is $X$; then the time complexity of quicksort is $O(n + X)$.
    
    Since in each element-partitioning process an element is chosen as the boundary, the element-partitioning process occurs at most $n$ times. And since the number of comparisons and the number of other basic operations in the element-partitioning process are of the same order of magnitude, the total time complexity is $O(n + X)$.
    
    Let $a_i$ be the $i$-th smallest number in the original array, define $A_{i,j}$ as $\{ a_i, a_{i+1}, \dots, a_j \}$, and let $X_{i,j}$ be a discrete random variable taking value $0$ or $1$ indicating whether $a_i$ and $a_j$ are compared during the sorting process.
    
    Clearly the boundary value chosen each time is different, and elements are only compared with the boundary value, so the total number of comparisons is
    
    $$
    \begin{aligned} X = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n X_{i,j} \end{aligned}
    $$
    
    By linearity of expectation,
    
    $$
    \begin{aligned} E[X] & = E \left[ \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n X_{i,j} \right] \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n E[X_{i,j}] \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n P(a_i\ \text{and}\ a_j\ \text{are compared}) \end{aligned}
    $$
    
    **Lemma 2:** The necessary and sufficient condition for $a_i$ and $a_j$ to be compared is that $a_i$ or $a_j$ is the first boundary value chosen from the set $A_{i,j}$.
    
    First prove necessity, i.e. if neither $a_i$ nor $a_j$ is the first boundary value chosen from the set $A_{i,j}$, then $a_i$ is not compared with $a_j$.
    
    If neither $a_i$ nor $a_j$ is the first boundary value chosen from the set $A_{i,j}$, then there must exist an $x$ with $i < x < j$ such that $a_x$ is the first boundary value chosen from $A_{i,j}$. In the partition with $a_x$ as the boundary value, $a_i$ and $a_j$ are partitioned into two different subsequences of the array, so afterward $a_i$ and $a_j$ will certainly not be compared. And because elements are only compared with the boundary value, $a_i$ and $a_j$ were not compared before or during this partition. So $a_i$ is not compared with $a_j$.
    
    Then prove sufficiency, i.e. if $a_i$ or $a_j$ is the first boundary value chosen from the set $A_{i,j}$, then $a_i$ and $a_j$ are compared.
    
    Without loss of generality, assume $a_i$ is the first boundary value chosen from the set $A_{i,j}$. Since no other number in $A_{i,j}$ has been chosen as a boundary value, all elements of $A_{i,j}$ are in the same subsequence of the array. In the partition with $a_i$ as the boundary value, $a_i$ is compared with all elements in the current subsequence, so $a_i$ is compared with $a_j$.
    
    Consider computing $P(a_i\ \text{and}\ a_j\ \text{are compared})$. Before some element of $A_{i,j}$ is chosen as a boundary value, all elements of $A_{i,j}$ are in the same subsequence of the array. So each element of $A_{i,j}$ is equally likely to be the first chosen as a boundary value. Since $A_{i,j}$ has $j - i + 1$ elements, by Lemma 2,
    
    $$
    P(a_i \text{ and } a_j \text{ are compared}) = P(a_i \text{ or } a_j \text{ is the first boundary value chosen from } A_{i,j}) = \dfrac{2}{j-i+1}
    $$
    
    So
    
    $$
    \begin{aligned} E[X] & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n P(a_i\ \text{and}\ a_j\ \text{are compared}) \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {j = i + 1} ^ n \dfrac{2}{j - i + 1} \\ & = \sum \limits _ {i = 1} ^ {n - 1} \sum \limits _ {k = 2} ^ {n - i + 1} \dfrac{2}{k} \\ & = \sum \limits _ {i = 1} ^ {n - 1} O(\log n) \\ & = O(n \log n) \end{aligned}
    $$
    
    From this, the expected time complexity of quicksort is $O(n \log n)$.

In practice, the worst case is almost impossible to reach, and the memory access of quicksort follows the principle of locality, so in most cases quicksort performs substantially better than other $O(n \log n)$ sorting algorithms such as heapsort. [^ref1]

## Optimization

### The naive optimization idea

If you implement quicksort merely according to the basic idea described above (or directly copy a template), you will most likely not pass the template problem [P1177 【Template】Quicksort](https://www.luogu.com.cn/problem/P1177). This is because there is adversarial data that can degrade naive quicksort to $O(n^2)$.

So we need to optimize the naive quicksort idea. The three more common optimization ideas are as follows[^ref3].

-   Choose the boundary element (i.e. the comparison pivot) of the two subsequences using the **median-of-three** method (i.e. take the median of the first, last, and middle elements). This avoids the degradation caused by extreme data (such as an ascending or descending sequence);
-   When the sequence is short, using **insertion sort** is more efficient;
-   After each pass, **gather the elements equal to the boundary element around the boundary element**, which avoids the degradation caused by extreme data (such as most elements in the sequence being equal).

Several relatively mature quicksort optimization methods are listed below.

### Three-way quicksort

#### Definition

Three-way quicksort (3-way Radix Quicksort) is a hybrid of quicksort and [radix sort](./radix-sort.md). Its algorithmic idea is based on the solution of the [Dutch national flag problem](https://en.wikipedia.org/wiki/Dutch_national_flag_problem).

#### Process

Unlike the original quicksort, after randomly choosing the partition point $m$, three-way quicksort divides the sequence to be sorted into three parts: less than $m$, equal to $m$, and greater than $m$. Doing this achieves the effect of gathering the elements equal to the boundary element around the boundary element.

#### Properties

Three-way quicksort is far more efficient than the original quicksort when handling arrays containing many duplicate values. Its best-case time complexity is $O(n)$.

#### Implementation

Three-way quicksort is very simple to implement; a C++ implementation of three-way quicksort is given below.

=== "C++"
    ```cpp
    // The template parameter T denotes the element type, which must define the less-than (<) operation
    template <typename T>
    // arr is the array to be sorted, len is the array length
    void quick_sort(T arr[], const int len) {
      if (len <= 1) return;
      // Randomly choose the pivot
      const T pivot = arr[rand() % len];
      // i: index of the element currently being processed
      // arr[0, j): stores elements less than pivot
      // arr[k, len): stores elements greater than pivot
      int i = 0, j = 0, k = len;
      // Complete one pass of three-way quicksort, dividing the sequence into:
      // elements less than pivot | elements equal to pivot | elements greater than pivot
      while (i < k) {
        if (arr[i] < pivot)
          swap(arr[i++], arr[j++]);
        else if (pivot < arr[i])
          swap(arr[i], arr[--k]);
        else
          i++;
      }
      // Recursively quicksort the two subsequences
      quick_sort(arr, j);
      quick_sort(arr + k, len - k);
    }
    ```

=== "Python[^ref2]"
    ```python
    def quick_sort(arr, l, r):
        if l >= r:
            return
        random_index = random.randint(l, r)
        pivot = arr[random_index]
        arr[l], arr[random_index] = arr[random_index], arr[l]
        i = l + 1
        j = l
        k = r + 1
        while i < k:
            if arr[i] < pivot:
                arr[i], arr[j + 1] = arr[j + 1], arr[i]
                j += 1
                i += 1
            elif arr[i] > pivot:
                arr[i], arr[k - 1] = arr[k - 1], arr[i]
                k -= 1
            else:
                i += 1
        arr[l], arr[j] = arr[j], arr[l]
        quick_sort(arr, l, j - 1)
        quick_sort(arr, k, r)
    ```

### Introsort

#### Definition

Introsort (introspective sort)[^ref4] is a combination of quicksort and [heapsort](./heap-sort.md), invented by David Musser in 1997. Introsort is actually an optimization of quicksort that guarantees a worst-case time complexity of $O(n\log n)$.

#### Properties

Introsort limits the maximum recursion depth of quicksort to $\lfloor \log_2n \rfloor$, and switches to heapsort when the limit is exceeded. This both preserves the locality of memory access of quicksort and prevents quicksort's performance from degrading to $O(n^2)$ in certain cases.

#### Implementation

Since June 2000, the implementation of the `sort()` function in SGI C++ STL's `stl_algo.h` has used the introsort algorithm.

## Finding the k-th largest number in linear time

In the code examples below, the $k$-th largest number is defined as the number at the $k$-th position (indexed from 0) when the sequence is arranged in ascending order.

To find the $k$-th largest number (the k-th order statistic), the simplest method is to sort first and then directly find the element at the $k$-th-largest position. The time complexity of doing this is $O(n\log n)$, which is quite uneconomical for this problem.

We can solve this problem using the idea of quicksort. Consider the partitioning process of quicksort. After the "partition" of quicksort ends, the sequence $A_{p} \cdots A_{r}$ is divided into $A_{p} \cdots A_{q}$ and $A_{q+1} \cdots A_{r}$; at this point we can decide, based on the relationship between the number of left elements ($q - p + 1$) and $k$, whether to recurse only on the left or only on the right.

Like quicksort, the time complexity of this method depends on the boundary value chosen at each partition. If the boundary value is chosen at random, it can be proven that in expectation the program's time complexity is $O(n)$.

### Implementation (C++)

```cpp
// The template parameter T denotes the element type, which must define the less-than (<) operation
template <typename T>
// arr is the array to search, rk is the rank to look up (starting from 0), len is the array length
T find_kth_element(T arr[], int rk, const int len) {
  if (len <= 1) return arr[0];
  // Randomly choose the pivot
  const T pivot = arr[rand() % len];
  // i: index of the element currently being processed
  // arr[0, j): stores elements less than pivot
  // arr[k, len): stores elements greater than pivot
  int i = 0, j = 0, k = len;
  // Complete one pass of three-way quicksort, dividing the sequence into:
  // elements less than pivot | elements equal to pivot | elements greater than pivot
  while (i < k) {
    if (arr[i] < pivot)
      swap(arr[i++], arr[j++]);
    else if (pivot < arr[i])
      swap(arr[i], arr[--k]);
    else
      i++;
  }
  // Depending on the rank sought and the positions of the two dividing lines, recurse into different intervals to find the k-th largest number
  // If there are more elements less than pivot than k, then the k-th largest element must be an element less than pivot
  if (rk < j) return find_kth_element(arr, rk, j);
  // Otherwise, if the elements less than pivot and equal to pivot together still number fewer than k,
  // then the k-th largest element must be an element greater than pivot
  else if (rk >= k)
    return find_kth_element(arr + k, rk - k, len - k);
  // Otherwise, pivot is the k-th largest element
  return pivot;
}
```

### Improvement: median of medians

The median of medians provides a deterministic method for choosing the boundary value during the partitioning process, thereby allowing the algorithm for finding the $k$-th largest number to achieve linear time complexity even in the worst case.

The flow of this algorithm is as follows:

1.  Divide the entire sequence into $\left \lfloor \dfrac{n}{5} \right \rfloor$ groups, each group containing no more than 5 elements;
2.  Find the median of each group of elements (since the number of elements is small, an algorithm such as [insertion sort](./insertion-sort.md) can be used directly).
3.  Find the median of the medians of these $\left \lfloor \dfrac{n}{5} \right \rfloor$ groups. Use that element as the boundary value at each partition in the aforementioned algorithm.

#### Proof of time complexity

Below we prove that the worst-case time complexity of this algorithm is $O(n)$. Let $T(n)$ be the amount of computation needed to solve the problem when the problem size is $n$.

First analyze the first two steps—partitioning and finding the medians. Since the number of elements within each group after partitioning is very small, the time complexity of finding the median of one group of elements can be regarded as $O(1)$. Therefore, the time complexity of finding the medians of all $\left \lfloor \dfrac{n}{5} \right \rfloor$ groups is $O(n)$.

Next analyze the third step—the recursion. This step makes two recursive calls: the first is to find the median of the group medians, whose cost is clearly $T(\dfrac{n}{5})$; the second is to enter the left part or right part of the boundary value. According to the partition element we chose, the medians of $\dfrac{1}{2} \times \left \lfloor \dfrac{n}{5} \right \rfloor = \left \lfloor \dfrac{n}{10} \right \rfloor$ groups of elements are smaller than the boundary value; among these groups, elements even smaller than their median are also certainly smaller than the boundary value, so the whole sequence has at least $3 \times \left \lfloor \dfrac{n}{10} \right \rfloor = \left \lfloor \dfrac{3n}{10} \right \rfloor$ elements smaller than the boundary value. Similarly, the whole sequence also has at least $\left \lfloor \dfrac{3n}{10} \right \rfloor$ elements greater than the boundary value. Therefore, the left or right side of the boundary value has at most $\dfrac{7n}{10}$ elements, and the upper bound of the time cost of this recursion is $T(\dfrac{7n}{10})$.

In summary, we can write the following inequality:

$$
T(n) \leq T(\dfrac{n}{5}) + T(\dfrac{7n}{10}) + O(n)
$$

Assume $T(n) = O(n)$ holds when the problem size is small enough. By definition, we then have $T(n) \leq cn$, where $c$ is a positive constant. Substituting all the $T(n)$ on the right side of the inequality:

$$
\begin{aligned}
T(n) & \leq T(\dfrac{n}{5}) + T(\dfrac{7n}{10}) + O(n)\\
     & \leq \dfrac{cn}{5} + \dfrac{7cn}{10} + O(n)\\
     & \leq \dfrac{9cn}{10} + O(n)\\
     & = O(n)
\end{aligned}
$$

At this point we have proven that this algorithm also has $O(n)$ time complexity in the worst case.

## References and notes

[^ref1]: [The Locality Principle in the C++ Performance Juicer - I'm Root lee !](http://irootlee.com/juicer_locality/)

[^ref2]: [Algorithm Implementation/Sorting/Quicksort - Wikibooks, the free textbook](https://zh.wikibooks.org/wiki/%E7%AE%97%E6%B3%95%E5%AE%9E%E7%8E%B0/%E6%8E%92%E5%BA%8F/%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F)

[^ref3]: [Three quicksorts and quicksort optimizations](https://blog.csdn.net/insistGoGo/article/details/7785038)

[^ref4]: [introsort](https://en.wikipedia.org/wiki/Introsort)
