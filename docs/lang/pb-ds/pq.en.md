author: Xeonacid, ouuan, Ir1d, WAAutoMaton, Chrogeek, abc1763613206, Planet6174, i-Yirannn, opsiff, GoodCoder666

## `__gnu_pbds::priority_queue`

Attached: [Official documentation address——complexity and constant factor tests](https://gcc.gnu.org/onlinedocs/libstdc++/ext/pb_ds/pq_performance_tests.html#std_mod1)

```cpp
#include <ext/pb_ds/priority_queue.hpp>
using namespace __gnu_pbds;
__gnu_pbds::priority_queue<T, Compare, Tag, Allocator>
```

## Template formal parameters

-   `T`: the type of the stored element
-   `Compare`: provides a strict weak ordering comparison type
-   `Tag`: one of the five different heaps provided by `__gnu_pbds`; the Tag parameter defaults to `pairing_heap_tag`. The five are respectively:
    -   `pairing_heap_tag`: pairing heap
        The official documentation considers that among non-primitive elements (such as custom structs / `std::string` / `pair`), the pairing heap performs best
    -   `binary_heap_tag`: binary heap
        The official documentation considers that among primitive elements the binary heap performs best, but the author's tested performance was not that good
    -   `binomial_heap_tag`: binomial heap
        The binomial heap performs better than the binary heap in the merge operation, but the complexity of its operation of taking the heap-top element is higher than the binary heap
    -   `rc_binomial_heap_tag`: redundant-counter binomial heap
    -   `thin_heap_tag`: a tag whose complexity is the same as the Fibonacci heap except for the merge complexity
-   `Allocator`: the space allocator; since it rarely appears in OI, it is not explained here

Since this article is only provided for students learning algorithm competitions, for the latter four tags we only briefly introduce the complexity, and for the first one we introduce the member functions and usage.

After the author tested the basic operations of the heaps on their local Core i5 @3.1 GHz On macOS, combined with GNU's official complexity tests and Dijkstra tests, all indicate that:
at least for OIers, the other four tags besides the pairing heap are all useless; either useless, or the constant factor is so large that it is worse than `std`'s, and it may cause MLE, so here we only recommend using the default pairing heap. Similarly, the pairing heap is also better than `make_heap()` in the `algorithm` library.

## Construction methods

The namespace needs to be specified because the class name duplicates `std`'s.

```cpp
// __gnu_pbds::priority_queue<int>;
// __gnu_pbds::priority_queue<int, greater<int>>;
// __gnu_pbds::priority_queue<int, greater<int>, pairing_heap_tag>;
__gnu_pbds::priority_queue<int>::point_iterator id;  // point-type iterator
// a point_iterator is returned during both modify and push; the usage is explained in detail below
id = q.push(1);
```

## Member functions

-   `push()`: push an element into the heap, returning the iterator of the position of this element.
-   `pop()`: pop the heap-top element.
-   `top()`: return the heap-top element.
-   `size()` return the number of elements.
-   `empty()` return whether it is non-empty.
-   `modify(point_iterator, const key)`: modify the `key` at the iterator position to the passed-in `key`, and sort the underlying storage structure.
-   `erase(point_iterator)`: erase the key value at the iterator position from the heap.
-   `join(__gnu_pbds::priority_queue &other)`: merge `other` into `*this` and clear `other`.

The tag used determines the time complexity of each operation:

|                        | push                                | pop                                 | modify                              | erase                               | Join              |
| ---------------------- | ----------------------------------- | :---------------------------------- | ----------------------------------- | ----------------------------------- | ----------------- |
| `pairing_heap_tag`     | $O(1)$                              | worst $\Theta(n)$ amortized $\Theta(\log(n))$ | worst $\Theta(n)$ amortized $\Theta(\log(n))$ | worst $\Theta(n)$ amortized $\Theta(\log(n))$ | $O(1)$            |
| `binary_heap_tag`      | worst $\Theta(n)$ amortized $\Theta(\log(n))$ | worst $\Theta(n)$ amortized $\Theta(\log(n))$ | $\Theta(n)$                         | $\Theta(n)$                         | $\Theta(n)$       |
| `binomial_heap_tag`    | worst $\Theta(\log(n))$ amortized $O(1)$      | $\Theta(\log(n))$                   | $\Theta(\log(n))$                   | $\Theta(\log(n))$                   | $\Theta(\log(n))$ |
| `rc_binomial_heap_tag` | $O(1)$                              | $\Theta(\log(n))$                   | $\Theta(\log(n))$                   | $\Theta(\log(n))$                   | $\Theta(\log(n))$ |
| `thin_heap_tag`        | $O(1)$                              | worst $\Theta(n)$ amortized $\Theta(\log(n))$ | worst $\Theta(\log(n))$ amortized $O(1)$      | worst $\Theta(n)$ amortized $\Theta(\log(n))$ | $\Theta(n)$       |

## Example

```cpp
#include <algorithm>
#include <cstdio>
#include <ext/pb_ds/priority_queue.hpp>
#include <iostream>
using namespace __gnu_pbds;
// since this is aimed at OIers, this article uses the commonly used heap: pairing_heap_tag as an example
// for a better reading experience, define the macro as follows:
using pair_heap = __gnu_pbds::priority_queue<int>;
pair_heap q1;  // max-heap, pairing heap
pair_heap q2;
pair_heap::point_iterator id;  // an iterator

int main() {
  id = q1.push(1);
  // elements in the heap: [1];
  for (int i = 2; i <= 5; i++) q1.push(i);
  // elements in the heap:  [1, 2, 3, 4, 5];
  std::cout << q1.top() << std::endl;
  // output: 5;
  q1.pop();
  // elements in the heap: [1, 2, 3, 4];
  id = q1.push(10);
  // elements in the heap: [1, 2, 3, 4, 10];
  q1.modify(id, 1);
  // elements in the heap:  [1, 1, 2, 3, 4];
  std::cout << q1.top() << std::endl;
  // output: 4;
  q1.pop();
  // elements in the heap: [1, 1, 2, 3];
  id = q1.push(7);
  // elements in the heap: [1, 1, 2, 3, 7];
  q1.erase(id);
  // elements in the heap: [1, 1, 2, 3];
  q2.push(1), q2.push(3), q2.push(5);
  // elements in q1: [1, 1, 2, 3], elements in q2: [1, 3, 5];
  q2.join(q1);
  // no elements in q1, elements in q2: [1, 1, 1, 2, 3, 3, 5];
}
```

## Iterator invalidation guarantee of \_\_gnu\_pbds (invalidation\_guarantee)

In the above example and in some practice (such as using the pb-ds heap of this chapter to write algorithms such as single-source shortest paths), it is often necessary to save and use the heap's iterator (such as `__gnu_pbds::priority_queue<int>::point_iterator`, etc.).

But, for example, for different Tag parameters in `__gnu_pbds::priority_queue`, their underlying implementations are not the same, and the invalidation conditions of iterators are also different. According to the design of the \_\_gnu\_pbds library, there are the following three cases derived from top to bottom:

1.  Basic invalidation guarantee (basic\_invalidation\_guarantee): i.e. when the container is not modified, point-type iterators (point\_iterator), pointers, and references (key/value) **remain** valid.

2.  Point invalidation guarantee (point\_invalidation\_guarantee): i.e. after **modifying** the container, point-type iterators (point\_iterator), pointers, and references (key/value) **remain** valid as long as the corresponding element has not been deleted in the container.

3.  Range invalidation guarantee (range\_invalidation\_guarantee): i.e. after **modifying** the container, besides the characteristics of (2), any range-type iterator (including the return values of `begin()` and `end()`) is correct; the tags with range invalidation guarantee are `rb_tree_tag` and `splay_tree_tag` applicable to `__gnu_pbds::tree`, and `pat_trie_tag` applicable to `__gnu_pbds::trie`.

From running the following code, we can see that, except that `binary_heap_tag` is `basic_invalidation_guarantee` and its iterators will become invalid after modification, the rest are all `point_invalidation_guarantee`, which can achieve the requirement of point-type iterators (point\_iterator) not becoming invalid after modification.

```cpp
#include <iostream>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace __gnu_pbds;
#include <cxxabi.h>

template <typename T>
void print_invalidation_guarantee() {
  using gute = __gnu_pbds::container_traits<T>::invalidation_guarantee;
  cout << abi::__cxa_demangle(typeid(gute).name(), 0, 0, 0) << endl;
}

int main() {
  using pairing =
      __gnu_pbds::priority_queue<int, greater<int>, pairing_heap_tag>;
  using binary = __gnu_pbds::priority_queue<int, greater<int>, binary_heap_tag>;
  using binomial =
      __gnu_pbds::priority_queue<int, greater<int>, binomial_heap_tag>;
  using rc_binomial =
      __gnu_pbds::priority_queue<int, greater<int>, rc_binomial_heap_tag>;
  using thin = __gnu_pbds::priority_queue<int, greater<int>, thin_heap_tag>;
  print_invalidation_guarantee<pairing>();
  print_invalidation_guarantee<binary>();
  print_invalidation_guarantee<binomial>();
  print_invalidation_guarantee<rc_binomial>();
  print_invalidation_guarantee<thin>();
  return 0;
}
```
