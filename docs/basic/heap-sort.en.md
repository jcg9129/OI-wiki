This page briefly introduces heapsort.

## Definition

Heapsort is a sorting algorithm designed using the [binary heap](../ds/binary-heap.md) data structure. The data structure heapsort applies to is the array.

## Process

Heapsort is essentially selection sort built on a heap.

### Sorting

First build a max-heap, then take out the element at the top of the heap as the maximum, swap it with the element at the tail of the array, and maintain the heap property of the remaining heap;

Then take out the element at the top of the heap as the second largest, swap it with the second-to-last element of the array, and maintain the heap property of the remaining heap;

And so on; after the $(n-1)$-th operation, the entire array is sorted.

### Building a binary heap on an array

Starting from the root node, arrange the nodes of each level in the array one after another.

Thus, for the node at index `i` in the array, the corresponding parent node, left child node, and right child node are as follows:

```cpp
iParent(i) = (i - 1) / 2;
iLeftChild(i) = 2 * i + 1;
iRightChild(i) = 2 * i + 2;
```

## Properties

### Stability

Like selection sort, because of the position-swapping operation, it is an unstable sorting algorithm.

### Time complexity

The best-case, average-case, and worst-case time complexities of heapsort are all $O(n\log n)$.

### Space complexity

Since the heap can be built on the input array, this is an in-place algorithm.

## Implementation

=== "C++"
    ```cpp
    void sift_down(int arr[], int start, int end) {
      // Compute the indices of the parent node and the child node
      int parent = start;
      int child = parent * 2 + 1;
      while (child <= end) {  // only compare when the child index is within range
        // First compare the two children and pick the larger one
        if (child + 1 <= end && arr[child] < arr[child + 1]) child++;
        // If the parent is larger than the child, the adjustment is done; return directly
        if (arr[parent] >= arr[child])
          return;
        else {  // otherwise swap the parent and child, then compare the child with the grandchild
          swap(arr[parent], arr[child]);
          parent = child;
          child = parent * 2 + 1;
        }
      }
    }
    
    void heap_sort(int arr[], int len) {
      // Start sift down from the parent of the last node to complete heapify
      for (int i = (len - 1 - 1) / 2; i >= 0; i--) sift_down(arr, i, len - 1);
      // First swap the first element with the element just before the already-sorted ones,
      // then readjust (the elements before the one just adjusted), until sorting is finished
      for (int i = len - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        sift_down(arr, 0, i - 1);
      }
    }
    ```

=== "Python"
    ```python
    def sift_down(arr, start, end):
        # Compute the indices of the parent node and the child node
        parent = int(start)
        child = int(parent * 2 + 1)
        while child <= end:  # only compare when the child index is within range
            # First compare the two children and pick the larger one
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child += 1
            # If the parent is larger than the child, the adjustment is done; return directly
            if arr[parent] >= arr[child]:
                return
            else:  # otherwise swap the parent and child, then compare the child with the grandchild
                arr[parent], arr[child] = arr[child], arr[parent]
                parent = child
                child = int(parent * 2 + 1)
    
    
    def heap_sort(arr, len):
        # Start sift down from the parent of the last node to complete heapify
        i = (len - 1 - 1) / 2
        while i >= 0:
            sift_down(arr, i, len - 1)
            i -= 1
        # First swap the first element with the element just before the already-sorted ones,
        # then readjust (the elements before the one just adjusted), until sorting is finished
        i = len - 1
        while i > 0:
            arr[0], arr[i] = arr[i], arr[0]
            sift_down(arr, 0, i - 1)
            i -= 1
    ```

## External links

-   [Heapsort - Wikipedia, the free encyclopedia](https://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F)
