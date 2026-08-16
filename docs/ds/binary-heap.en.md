author: HeRaNO, Xeonacid, AzurIce

## Structure

Starting from the structure of a binary heap: it is a binary tree, and a complete binary tree, where each node stores an element (or, has a weight).

Heap property: a parent's weight is not less than its children's weights (a max-heap). Similarly, we can define a min-heap. This article takes a max-heap as an example.

By the heap property, the root stores the maximum value (the getmax operation is thus solved).

## Process

### Insertion

Insertion means inserting an element into the binary heap while ensuring it is still a complete binary tree after insertion.

The simplest method is to insert after the rightmost leaf of the bottom level.

If the bottom level is already full, add a new level.

After insertion, the heap property may not be satisfied?

**Sift up**: if this node's weight is greater than its parent's weight, swap them, and repeat this process until it is no longer the case or the root is reached.

It can be proven that after inserting and sifting up, no other node will fail to satisfy the heap property.

The time complexity of sifting up is $O(\log n)$.

![insertion operation of a binary heap](./images/binary_heap_insert.svg)

### Deletion

Deletion means deleting the largest element in the heap, i.e. deleting the root node.

But if we delete it directly, it becomes two heaps, which is hard to handle.

So we might as well consider the reverse process of insertion: try to move the root node to the last node and then delete it directly.

However, this is actually not easy to do; the method we usually adopt is to directly swap the root node with the last node.

Then directly delete the root node (which is now at the last node's position), but the new root node may not satisfy the heap property……

**Sift down**: among this node's children, find the largest, swap it with this node, and repeat this process until the bottom level.

It can be proven that after deleting and sifting down, no other node fails to satisfy the heap property.

Time complexity $O(\log n)$.

### Increasing the weight of some node

Clearly, after directly modifying it, one sift-up suffices, with time complexity $O(\log n)$.

## Implementation

We find that the several operations introduced above mainly rely on two cores: sifting up and sifting down.

Consider using a sequence $h$ to represent the heap. The two children of $h_i$ are $h_{2i}$ and $h_{2i+1}$, and $1$ is the root node:

![the heap structure of h](./images/binary-heap-array.svg)

Reference code:

```cpp
void up(int x) {
  while (x > 1 && h[x] > h[x / 2]) {
    std::swap(h[x], h[x / 2]);
    x /= 2;
  }
}

void down(int x) {
  while (x * 2 <= n) {
    t = x * 2;
    if (t + 1 <= n && h[t + 1] > h[t]) t++;
    if (h[t] <= h[x]) break;
    std::swap(h[x], h[t]);
    x = t;
  }
}
```

### Building a heap

Consider this problem: starting from an empty heap, insert $n$ elements, not caring about the order.

Inserting them one by one directly takes $O(n \log n)$ time; is there a better method?

#### Method one: sift up

Start from the root, proceeding in BFS order.

```cpp
void build_heap_1() {
  for (i = 1; i <= n; i++) up(i);
}
```

This approach is still equivalent to inserting one by one, only that the elements are placed in the array beforehand, which can improve the constant factor. Hence, in the worst case, the recurrence satisfied by the algorithm's time complexity is $T(n) = T(n - 1) + \Theta(\log n)$, and summing gives $T(n) = \Theta(n \log n)$.

#### Method two: sift down

This time we take a different idea, starting from the leaves and sifting down one by one.

```cpp
void build_heap_2() {
  for (i = n; i >= 1; i--) down(i);
}
```

Understood another way, each time we "merge" two already-adjusted heaps, which shows the correctness.

Note that leaf nodes need no adjustment, so we can start adjusting from about position $n/2$ of the sequence, which can improve the constant factor. Based on the understanding of merging two heaps each time, we can write the recurrence of the algorithm's time complexity $T(n) = 2T(\dfrac{n}{2}) + O(\log n)$; by the Master Theorem, $T(n) = \Theta(n)$.

The reason we can build a heap in $\Theta(n)$ is that the heap property is very weak, and the binary heap is not unique.

If it were a strong condition like sorting, it would be hard to say.

## Applications

### Opposing heaps

??? note "[SPOJ RMID2 - Running Median Again](https://www.spoj.com/problems/RMID2/)"
    Maintain a sequence, supporting two operations:
    
    1.  Insert an element into the sequence
    2.  Output and delete the median of the current sequence (if the sequence length is even, output the smaller median)

This problem can be further abstracted as: dynamically maintaining the $k$-th largest number of a sequence, where the value of $k$ may change.

For this kind of problem, we can use the technique of **opposing heaps** to solve it (which avoids the tedium of writing a weighted segment tree or BST).

Opposing heaps consist of a max-heap and a min-heap: the min-heap maintains the large values, i.e. the top $k$ largest values (including the $k$-th), and the max-heap maintains the small values, i.e. the other numbers smaller than the $k$-th largest number.

The data structure formed by these two heaps supports the following operations:

-   Maintenance: when the min-heap's size is less than $k$, continually take the top element of the max-heap and insert it into the min-heap until the min-heap's size equals $k$; when the min-heap's size is greater than $k$, continually take the top element of the min-heap and insert it into the max-heap until the min-heap's size equals $k$;
-   Insert an element: if the inserted element is greater than or equal to the top of the min-heap, insert it into the min-heap, otherwise insert it into the max-heap, then maintain the opposing heaps;
-   Query the $k$-th largest element: the top of the min-heap is the answer;
-   Delete the $k$-th largest element: delete the top of the min-heap, then maintain the opposing heaps;
-   $k$ value $+1/-1$: directly maintain the opposing heaps according to the new $k$ value.

Clearly, the time complexity of querying the $k$-th largest element is $O(1)$. Since after inserting, deleting, or adjusting the $k$ value, the min-heap's size differs from the expected $k$ value by at most $1$, each maintenance needs at most one adjustment of the elements in the max-heap and min-heap, so the time complexity of these operations is all $O(\log n)$.

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/binary-heap/binary-heap_1.cpp"
    ```

### Exercises

-   [SPOJ RMID - Running Median](https://www.spoj.com/problems/RMID)
-   [Luogu P1801 Black Box](https://www.luogu.com.cn/problem/P1801)
