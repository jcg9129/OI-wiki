This page briefly introduces bucket sort.

## Definition

Bucket sort is a sorting algorithm suitable for cases where the data to be sorted has a large range of values but a fairly uniform distribution.

## Process

Bucket sort proceeds as follows:

1.  Set up a fixed number of arrays as empty buckets;
2.  Traverse the sequence and place the elements one by one into their corresponding buckets;
3.  Sort each non-empty bucket;
4.  Put the elements from the non-empty buckets back into the original sequence.

## Properties

### Stability

If a stable inner sort is used and the relative order of elements is not changed when inserting them into buckets, then bucket sort is a stable sorting algorithm.

Since each bucket holds few elements, insertion sort is generally used. In this case bucket sort is a stable sorting algorithm.

### Time complexity

The average time complexity of bucket sort is $O(n + n^2/k + k)$ (dividing the value range evenly into $n$ blocks + sorting + merging the elements back), which is $O(n)$ when $k\approx n$. [^ref1]

The worst-case time complexity of bucket sort is $O(n^2)$.

## Implementation

=== "C++"
    ```cpp
    constexpr int N = 100010;
    
    int n, w, a[N];
    vector<int> bucket[N];
    
    void insertion_sort(vector<int>& A) {
      for (int i = 1; i < A.size(); ++i) {
        int key = A[i];
        int j = i - 1;
        while (j >= 0 && A[j] > key) {
          A[j + 1] = A[j];
          --j;
        }
        A[j + 1] = key;
      }
    }
    
    void bucket_sort() {
      int bucket_size = w / n + 1;
      for (int i = 0; i < n; ++i) {
        bucket[i].clear();
      }
      for (int i = 1; i <= n; ++i) {
        bucket[a[i] / bucket_size].push_back(a[i]);
      }
      int p = 0;
      for (int i = 0; i < n; ++i) {
        insertion_sort(bucket[i]);
        for (int j = 0; j < bucket[i].size(); ++j) {
          a[++p] = bucket[i][j];
        }
      }
    }
    ```

=== "Python"
    ```python
    N = 100010
    w = n = 0
    a = [0] * N
    bucket = [[] for i in range(N)]
    
    
    def insertion_sort(A):
        for i in range(1, len(A)):
            key = A[i]
            j = i - 1
            while j >= 0 and A[j] > key:
                A[j + 1] = A[j]
                j -= 1
            A[j + 1] = key
    
    
    def bucket_sort():
        bucket_size = int(w / n + 1)
        for i in range(0, n):
            bucket[i].clear()
        for i in range(1, n + 1):
            bucket[int(a[i] / bucket_size)].append(a[i])
        p = 0
        for i in range(0, n):
            insertion_sort(bucket[i])
            for j in range(0, len(bucket[i])):
                a[p] = bucket[i][j]
                p += 1
    ```

## References and notes

[^ref1]: [Bucket sort - Wikipedia (English)](https://en.wikipedia.org/wiki/Bucket_sort#Average-case_analysis)
