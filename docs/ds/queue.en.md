This page introduces data structures related to queues and their applications.

![](./images/queue.svg)

## Introduction

A queue is a list with the property that "an element that enters the queue earlier must leave the queue earlier". Because of this property, a queue is usually also called a first-in-first-out (FIFO) list.

## Implementation

### Simulating a queue with an array

Usually an array is used to simulate a queue, with two variables marking the head and tail of the queue.

```cpp
int q[SIZE], ql = 1, qr;
```

The code corresponding to the queue operations is as follows:

-   Insert an element: `q[++qr] = x;`
-   Delete an element: `ql++;`
-   Access the front: `q[ql]`
-   Access the back: `q[qr]`
-   Clear the queue: `ql = 1; qr = 0;`

??? example "[Luogu B3616 【Template】Queue](https://www.luogu.com.cn/problem/B3616) array-simulation reference implementation"
    ```cpp
    --8<-- "docs/ds/code/queue/queue_1.cpp"
    ```

### Simulating a queue with two stacks

There is also a less common method that uses two [stacks](./stack.md) to simulate a queue.

This method uses two stacks $F$ and $S$ to simulate a queue, where $F$ is the tail stack and $S$ represents the head stack, supporting push (insert at the tail) and pop (pop at the head) operations:

-   push: insert into stack $F$.
-   pop: if $S$ is non-empty, pop $S$; otherwise reverse the elements of $F$ and push them onto $S$ (which is actually popping and inserting one by one; after doing so the head and tail are reversed), then pop $S$.

It is easy to prove that each element enters/transfers/pops at most once, with amortized complexity $O(1)$.

??? example "[Luogu B3616 【Template】Queue](https://www.luogu.com.cn/problem/B3616) two-stack-simulation reference implementation"
    ```cpp
    --8<-- "docs/ds/code/queue/queue_2.cpp"
    ```

## The queue in the C++ STL

C++ provides a container `std::queue` in the STL; before use you need to include the `<queue>` header file.

???+ info "The definition of `queue` in the STL"
    ```cpp
    // clang-format off
    template<
        class T,
        class Container = std::deque<T>
    > class queue;
    ```
    
    `T` is the data type to be stored in the queue.
    
    `Container` is the underlying container type used to store elements. This container must provide the following functions with the usual semantics:
    
    -   `back()`
    -   `front()`
    -   `push_back()`
    -   `pop_front()`
    
    The STL containers `std::deque` and `std::list` satisfy these requirements. If not specified, `std::deque` is used as the underlying container by default.

The `queue` container in the STL provides a host of member functions to call. The more commonly used ones are:

-   Element access
    -   `q.front()` returns the front element
    -   `q.back()` returns the back element
-   Modification
    -   `q.push()` inserts an element at the tail
    -   `q.pop()` pops the front element
-   Capacity
    -   `q.empty()` whether the queue is empty
    -   `q.size()` returns the number of elements in the queue

In addition, `queue` also provides some operators. The more commonly used one is using the assignment operator `=` to assign to a `queue`; example:

```cpp
std::queue<int> q1, q2;

// insert 1 at the tail of q1
q1.push(1);

// assign q1 to q2
q2 = q1;

// output the front element of q2
std::cout << q2.front() << std::endl;
// output: 1
```

## Special queues

### Double-ended queue

A double-ended queue is a queue in which elements can be inserted or deleted at the head/tail. It is equivalent to a combination of the functions of a stack and a queue. Specifically, a double-ended queue supports 4 operations:

-   Insert an element at the head
-   Insert an element at the tail
-   Delete an element at the head
-   Delete an element at the tail

The way to simulate a double-ended queue with an array is the same as an ordinary queue.

Similarly, one can also use the idea of simulating a queue with two stacks to maintain a double-ended queue, but note that when one of the stacks is empty, alternately querying the head and the tail will cause the amortized analysis to fail. Consider moving, when balancing, only half of the elements of the non-empty stack into the empty stack, while maintaining the properties of the head and tail stacks; after this handling one can still achieve amortized constant-time insertion and deletion.

??? note "Brief proof"
    Since the insertion operation only contributes constant complexity, now consider the pop operation. Suppose initially there are $m$ elements in the queue; below we compute the time complexity of popping out all elements (regardless of head or tail). Then the complexity of the first balancing is $O(m)$. After that the two stacks each have $\frac{m}{2}$ elements. At this point we need $O(\frac{m}{2})$ time to empty one of the stacks, after which another balancing operation of complexity $O(\frac{m}{2})$ can be triggered, and so on, until all elements are popped. Therefore, the total complexity of doing this is
    
    $$
    T(m)=T\left(\frac{m}{2}\right)+O(m)
    $$
    
    By the master theorem, we solve $T(m)=O(m)$. So the total complexity of this maintenance method is still amortized constant.

??? example "[Luogu B3656 【Template】Double-Ended Queue 1](https://www.luogu.com.cn/problem/B3656) reference implementation"
    ```cpp
    --8<-- "docs/ds/code/queue/queue_3.cpp"
    ```

#### The double-ended queue in the C++ STL

C++ also provides a container `std::deque` in the STL; before use you need to include the `<deque>` header file.

??? info "The definition of `deque` in the STL"
    ```cpp
    // clang-format off
    template<
        class T,
        class Allocator = std::allocator<T>
    > class deque;
    ```
    
    `T` is the data type to be stored in the deque.
    
    `Allocator` is the allocator; it is not explained much here, and generally keeping the default is fine.

The `deque` container in the STL provides a host of member functions to call. The more commonly used ones are:

-   Element access
    -   `q.front()` returns the front element
    -   `q.back()` returns the back element
-   Modification
    -   `q.push_back()` inserts an element at the tail
    -   `q.pop_back()` pops the tail element
    -   `q.push_front()` inserts an element at the head
    -   `q.pop_front()` pops the front element
    -   `q.insert()` inserts an element before the specified position (pass in an iterator and an element)
    -   `q.erase()` deletes the element at the specified position (pass in an iterator)
-   Capacity
    -   `q.empty()` whether the queue is empty
    -   `q.size()` returns the number of elements in the queue

In addition, `deque` also provides some operators. The more commonly used ones are:

-   Using the assignment operator `=` to assign to a `deque`, similar to `queue`.
-   Using `[]` to access elements, similar to `vector`.

The `<queue>` header file also provides the priority queue `std::priority_queue`; since it is more similar to a [heap](./heap.md), it is not introduced much here.

#### The double-ended queue in Python

In Python, the double-ended queue container is provided by `collections.deque`.

An example is as follows:

???+ note "Implementation"
    ```python
    from collections import deque
    
    # create a new deque and initialize the content to [1, 2, 3]
    queue = deque([1, 2, 3])
    
    # insert element 4 at the tail
    queue.append(4)
    
    # insert element 0 at the head
    queue.appendleft(0)
    
    # access the queue
    # >>> queue
    # deque([0, 1, 2, 3, 4])
    ```

### Circular queue

Using an array to simulate a queue causes a problem: as time goes by, the whole queue moves toward the tail of the array, and once it reaches the very end of the array, even if there are free positions at the front of the array, performing another enqueue operation will cause overflow (this phenomenon where the array actually has free positions but an overflow occurs is called "false overflow").

The way to solve false overflow is to organize the array storing the queue elements in a circular manner, i.e. regard the position with array index 0 as the successor of the last position. (For the element with array index `x`, its successor is `(x + 1) % SIZE`.) This forms a circular queue.

## References

1.  [std::queue - zh.cppreference.com](https://zh.cppreference.com/w/cpp/container/queue)
2.  [std::deque - zh.cppreference.com](https://zh.cppreference.com/w/cpp/container/deque)
