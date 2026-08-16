author: Xeonacid, ksyx, Early0v0

## Stack

The STL [stack](../../ds/stack.md) (`std::stack`) is a last-in-first-out (Last In, First Out) container adapter that only supports querying or deleting the last-added element (the top element), does not support random access, and, in order to guarantee the strict ordering of data, does not support iterators.

### Header file

```cpp
#include <stack>
```

### Definition

```cpp
std::stack<TypeName> s;  // use the default underlying container deque, data type is TypeName
std::stack<TypeName, Container> s;  // use Container as the underlying container
std::stack<TypeName> s2(s1);        // copy s1 to construct s2
```

### Member functions

**All the following functions are of constant complexity**

-   `top()` access the top element (if the stack is empty, an error occurs here)
-   `push(x)` insert element x into the stack
-   `pop()` delete the top element
-   `size()` query the number of elements in the container
-   `empty()` ask whether the container is empty

### Simple example

```cpp
std::stack<int> s1;
s1.push(2);
s1.push(1);
std::stack<int> s2(s1);
s1.pop();
std::cout << s1.size() << " " << s2.size() << std::endl;  // 1 2
std::cout << s1.top() << " " << s2.top() << std::endl;    // 2 1
s1.pop();
std::cout << s1.empty() << " " << s2.empty() << std::endl;  // 1 0
```

## Queue

The STL [queue](../../ds/queue.md) (`std::queue`) is a first-in-first-out (First In, First Out) container adapter that only supports querying or deleting the first-added element (the front element), does not support random access, and, in order to guarantee the strict ordering of data, does not support iterators.

### Header file

```cpp
#include <queue>
```

### Definition

```cpp
std::queue<TypeName> q;  // use the default underlying container deque, data type is TypeName
std::queue<TypeName, Container> q;  // use Container as the underlying container

std::queue<TypeName> q2(q1);  // copy q1 to construct q2
```

### Member functions

**All the following functions are of constant complexity**

-   `front()` access the front element (if the queue is empty, an error occurs here)
-   `push(x)` insert element x into the queue
-   `pop()` delete the front element
-   `size()` query the number of elements in the container
-   `empty()` ask whether the container is empty

### Simple example

```cpp
std::queue<int> q1;
q1.push(2);
q1.push(1);
std::queue<int> q2(q1);
q1.pop();
std::cout << q1.size() << " " << q2.size() << std::endl;    // 1 2
std::cout << q1.front() << " " << q2.front() << std::endl;  // 1 2
q1.pop();
std::cout << q1.empty() << " " << q2.empty() << std::endl;  // 1 0
```

## Priority queue

The priority queue `std::priority_queue` is a kind of [heap](../../ds/heap.md), generally a [binary heap](../../ds/binary-heap.md).

### Header file

```cpp
#include <queue>
```

### Definition

```cpp
std::priority_queue<TypeName> q;             // data type is TypeName
std::priority_queue<TypeName, Container> q;  // use Container as the underlying container
std::priority_queue<TypeName, Container, Compare> q;
// use Container as the underlying container, use Compare as the comparison type

// by default use the underlying container vector
// comparison type less<TypeName> (in this case its top() returns the maximum value)
// if you want top() to return the minimum value, you can make the comparison type greater<TypeName>
// note: you cannot skip Container and directly pass in Compare

// starting from C++11, if you use a lambda function to customize Compare
// then you need to pass it in as a constructor parameter, for example:
auto cmp = [](const std::pair<int, int> &l, const std::pair<int, int> &r) {
  return l.second < r.second;
};
std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>,
                    decltype(cmp)>
    pq(cmp);
```

### Member functions

**All the following functions are of constant complexity**

-   `top()` access the heap-top element (at this time the priority queue cannot be empty)
-   `empty()` ask whether the container is empty
-   `size()` query the number of elements in the container

**All the following functions are of logarithmic complexity**

-   `push(x)` insert an element and sort the underlying container
-   `pop()` delete the heap-top element (at this time the priority queue cannot be empty)

### Simple example

```cpp
std::priority_queue<int> q1;
std::priority_queue<int, std::vector<int>> q2;
// after C++11 the space can be omitted
std::priority_queue<int, std::deque<int>, std::greater<int>> q3;
// q3 is a min-heap
for (int i = 1; i <= 5; i++) q1.push(i);
// elements in q1 :  [1, 2, 3, 4, 5]
std::cout << q1.top() << std::endl;
// output : 5
q1.pop();
// elements in the heap : [1, 2, 3, 4]
std::cout << q1.size() << std::endl;
// output : 4
for (int i = 1; i <= 5; i++) q3.push(i);
// elements in q3 :  [1, 2, 3, 4, 5]
std::cout << q3.top() << std::endl;
// output : 1
```
