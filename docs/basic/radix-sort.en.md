???+ warning "Reminder"
    This page is not about [**counting sort**](./counting-sort.md).

This page briefly introduces radix sort.

## Definition

Radix sort is a non-comparison sorting algorithm, originally used to solve the card-sorting problem. Radix sort splits the elements to be sorted into $k$ keys, and sorts by each key one by one to complete the sorting of all elements.

If the comparison proceeds in order from the $1$st key to the $k$-th key, the radix sort is called MSD (Most Significant Digit first) radix sort;

If the comparison proceeds in order from the $k$-th key to the $1$st key, the radix sort is called LSD (Least Significant Digit first) radix sort.

## Comparison of k-key elements

Below, $a_i$ denotes the $i$-th key of element $a$.

If an element has $k$ keys, then for two elements $a$ and $b$, the default comparison method is:

-   Compare the $1$st keys $a_1$ and $b_1$ of the two elements: if $a_1 < b_1$ then $a < b$, if $a_1 > b_1$ then $a > b$, and if $a_1 = b_1$ proceed to the next step;
-   Compare the $2$nd keys $a_2$ and $b_2$ of the two elements: if $a_2 < b_2$ then $a < b$, if $a_2 > b_2$ then $a > b$, and if $a_2 = b_2$ proceed to the next step;
-   ……
-   Compare the $k$-th keys $a_k$ and $b_k$ of the two elements: if $a_k < b_k$ then $a < b$, if $a_k > b_k$ then $a > b$, and if $a_k = b_k$ then $a = b$.

Examples:

-   If comparing natural numbers, align the natural numbers by their units digit and pad with $0$s toward the higher digits; then the $i$-th digit of a number counted from the left can serve as the $i$-th key;
-   If comparing strings based on lexicographic order, the $i$-th character of a string counted from the left can serve as the $i$-th key;
-   The default comparison methods of C++'s built-in `std::pair` and `std::tuple` are the same as above.

## MSD radix sort

Based on the comparison method for k-key elements, one can think: first compare the $1$st keys of all elements to determine the rough magnitude relationship among the elements; then, for **elements with the same $1$st key**, compare their $2$nd keys…… and so on.

Since the comparison proceeds in order from the $1$st key to the $k$-th key, the sorting algorithm derived from the above idea is called MSD (Most Significant Digit first) radix sort.

### Algorithm flow

Split the elements to be sorted into $k$ keys, first perform a stable sort on the $1$st key, then for each group of **elements with the same key** perform a stable sort on the $2$nd key (recursively)…… finally, for each group of **elements with the same key**, perform a stable sort on the $k$-th key.

In general, we by default consider radix sort to be stable, so in MSD radix sort we also only consider completing the inner sorting of keys with the help of a **stable algorithm** (usually counting sort).

For correctness, refer to the comparison of k-key elements above.

### Reference code

#### Sorting natural numbers

Below is C++ reference code that uses iterative MSD radix sort to sort elements within the `unsigned int` range; the values of $W$ and $\log_2 W$ can be adjusted (it is recommended to set $\log_2 W$ to $2^k$ to facilitate bit-operation optimization).

??? example "Reference code"
    ```cpp
    --8<-- "docs/basic/code/radix-sort/radix-sort_1.cpp:core"
    ```

#### Sorting strings

Below is C++ reference code that uses iterative MSD radix sort to sort [null-terminated byte strings](https://zh.cppreference.com/w/cpp/string/byte) based on lexicographic order:

??? example "Reference code"
    ```cpp
    --8<-- "docs/basic/code/radix-sort/radix-sort_2.cpp:core"
    ```

Since the comparison of two strings can easily reach the $O(n)$ linear complexity, when it comes to sorting strings, MSD radix sort outperforms most comparison-based sorting algorithms in both time complexity and actual running time.

### Relationship with bucket sort

Prerequisite: [Bucket sort](./bucket-sort.md)

Bucket sort requires another sorting algorithm to complete the sorting of the elements within each bucket. But in fact, one can perfectly well continue to apply bucket sort to each bucket, until at some step the number of elements in a bucket is $\le 1$.

Therefore, another way to understand MSD radix sort is: bucket sort implemented with bucket sort.

And therefore, one optimization for the time constant of MSD radix sort can be proposed: if at some step the number of elements in a bucket is $\le B$ ($B$ is a constant you choose), then directly perform insertion sort and return, reducing the number of recursions.

## LSD radix sort

MSD radix sort compares in order from the $1$st key to the $k$-th key, which requires recursion or iteration to implement; its time constant is still rather large, and it is still somewhat inconvenient for comparing natural numbers.

By reversing the recursive operation—comparing in order from the $k$-th key to the $1$st key—we obtain LSD (Least Significant Digit first) radix sort, a sorting algorithm that can be completed without recursion.

### Algorithm flow

Split the elements to be sorted into $k$ keys, then first perform a stable sort on the $k$-th key of **all elements**, then a stable sort on the $(k-1)$-th key of **all elements**, then a stable sort on the $(k-2)$-th key of **all elements**…… and finally a stable sort on the $1$st key of **all elements**; this completes the stable sort of the entire sequence to be sorted.

![An example of the full flow of LSD radix sort](images/radix-sort-1.png "An example of the full flow of LSD radix sort")

LSD radix sort also needs the help of a **stable algorithm** to complete the inner sorting of keys. Likewise, counting sort is usually used.

The correctness of LSD radix sort can be found in [the solution to Exercise 8.3-3 of "Introduction to Algorithms (3rd edition)"](https://walkccc.github.io/CLRS/Chap08/8.3/#83-3), or refer to the explanation below:

### Correctness

Recall the comparison method for k-key elements:

-   If you want to compare the magnitude of two elements $a$ and $b$ just by $a_1$ and $b_1$, you need to know in advance the conclusion obtained by comparing $a_2$ and $b_2$, in order to handle the case $a_1 = b_1$;
-   And if you want to compare the magnitude of two elements $a$ and $b$ just by $a_2$ and $b_2$, you need to know in advance the conclusion obtained by comparing $a_3$ and $b_3$, in order to handle the case $a_2 = b_2$;
-   ……
-   And if you want to compare the magnitude of two elements $a$ and $b$ just by $a_{k-1}$ and $b_{k-1}$, you need to know in advance the conclusion obtained by comparing $a_k$ and $b_k$, in order to handle the case $a_{k-1} = b_{k-1}$;
-   $a_k$ and $b_k$ can be compared directly.

Now, reverse the order:

-   $a_k$ and $b_k$ can be compared directly;
-   And knowing the conclusion obtained by comparing $a_k$ and $b_k$, you can obtain the conclusion of comparing $a_{k-1}$ and $b_{k-1}$;
-   ……
-   And knowing the conclusion obtained by comparing $a_2$ and $b_2$, you can obtain the conclusion of comparing $a_1$ and $b_1$;
-   And knowing the conclusion obtained by comparing $a_1$ and $b_1$, you finally obtain the conclusion of comparing $a$ and $b$.

In this process, comparing and rearranging the order of elements for each key at the same time gives LSD radix sort.

### Pseudocode

$$
\begin{array}{ll}
1 & \textbf{Input. } \text{An array } A \text{ consisting of }n\text{ elements, where each element has }k\text{ keys.}\\
2 & \textbf{Output. } \text{Array }A\text{ will be sorted in nondecreasing order stably.} \\
3 & \textbf{Method. }  \\
4 & \textbf{for }i\gets k\textbf{ down to }1\\
5 & \qquad\text{sort }A\text{ into nondecreasing order by the }i\text{-th key stably}
\end{array}
$$

### Reference code

Below is the sorting of k-key elements implemented using LSD radix sort.

??? example "Reference code"
    ```cpp
    --8<-- "docs/basic/code/radix-sort/radix-sort_lsd.cpp:core"
    ```

In fact, it is not necessary to enumerate from back to front to make it a stable sort; it suffices to perform on the `cnt` array an operation equivalent to `std::exclusive_scan`.

???+ note "Example [Luogu P1177 【Template】Sorting](https://www.luogu.com.cn/problem/P1177)"
    Given $n$ positive integers, output them from small to large.
    
    ```cpp
    #include <algorithm>
    #include <iostream>
    #include <utility>
    
    void radix_sort(int n, int a[]) {
      int *b = new int[n];  // temporary space
      int *cnt = new int[1 << 8];
      int mask = (1 << 8) - 1;
      int *x = a, *y = b;
      for (int i = 0; i < 32; i += 8) {
        for (int j = 0; j != (1 << 8); ++j) cnt[j] = 0;
        for (int j = 0; j != n; ++j) ++cnt[x[j] >> i & mask];
        for (int sum = 0, j = 0; j != (1 << 8); ++j) {
          // equivalent to std::exclusive_scan(cnt, cnt + (1 << 8), cnt, 0);
          sum += cnt[j], cnt[j] = sum - cnt[j];
        }
        for (int j = 0; j != n; ++j) y[cnt[x[j] >> i & mask]++] = x[j];
        std::swap(x, y);
      }
      delete[] cnt;
      delete[] b;
    }
    
    int main() {
      std::ios::sync_with_stdio(false);
      std::cin.tie(nullptr);
      int n;
      std::cin >> n;
      int *a = new int[n];
      for (int i = 0; i < n; ++i) std::cin >> a[i];
      radix_sort(n, a);
      for (int i = 0; i < n; ++i) std::cout << a[i] << ' ';
      delete[] a;
      return 0;
    }
    ```

## Properties

### Stability

If the sorting of the inner keys is stable, then both MSD radix sort and LSD radix sort are stable sorting algorithms.

### Time complexity

Generally speaking, radix sort is faster than comparison-based sorting algorithms (such as quicksort). But because it requires additional memory space, when memory space is scarce an in-place algorithm (such as quicksort) may be a better choice. [^ref1]

In general, if the value range of each key is not large, [counting sort](./counting-sort.md) can be used as the inner sort, in which case the complexity is $O(kn+\sum\limits_{i=1}^k w_i)$, where $w_i$ is the size of the value range of the $i$-th key. If the key value range is very large, a comparison-based $O(nk\log n)$ sort can be used directly without needing radix sort.

### Space complexity

The space complexities of both MSD radix sort and LSD radix sort are $O(k+n)$.

## References and notes

[^ref1]: Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein.*Introduction to Algorithms*(3rd ed.). MIT Press and McGraw-Hill, 2009. ISBN 978-0-262-03384-8. "8.3 Radix sort", pp. 199.
