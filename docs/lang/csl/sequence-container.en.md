author: MingqiHuang, Xeonacid, greyqz, i-Yirannn, ChenZ01

## `vector`

`std::vector` is a **memory-contiguous**, **variable-length** array (also called a list) data structure provided by STL. It can provide linear-complexity insertion and deletion, as well as constant-complexity random access.

### Why use `vector`

As an OIer, the pursuit of program efficiency is far higher than the pursuit of engineering-level stability, and `vector`, due to its dynamic handling of memory, has time efficiency lower than a static array in some cases, and it is even worse when the OJ server does not necessarily enable full optimization. So when normally storing data, `vector` is usually not chosen. Below are several excellent features of `vector`; in cases where these features are needed, `vector` can bring us great help.

#### `vector` can dynamically allocate memory

Many times we cannot open such a large space in advance (e.g.: preprocessing the divisors of all numbers in 1\~n). Although we can know that the total amount of data is at a space-permitting level, a single piece of data may still be very large; in this case we need `vector` to control the memory usage within an appropriate range. `vector` also supports dynamic expansion; this feature can come in handy when memory is very tight.

#### `vector` rewrites the comparison operators and assignment operator

`vector` overloads the six comparison operators, implemented in lexicographic order, which allows us to conveniently determine whether two containers are equal (complexity is linear in the container size). For example, we can use `vector<char>` to implement string comparison (of course, using `std::string` is still faster and more convenient). In addition, `vector` also overloads the assignment operator, making array copying more convenient.

#### Convenient initialization of `vector`

Since `vector` overloads the `=` operator, we can conveniently perform whole-assignment operations on a `vector`. In addition, starting from C++11, `vector` also supports [list initialization](https://zh.cppreference.com/w/cpp/language/list_initialization), for example `vector<int> data {1, 2, 3};`.

### Usage of `vector`

Below we introduce common usages; for detailed content [please see the C++ documentation](https://zh.cppreference.com/w/cpp/container/vector).

#### Constructors

For examples, see the following code (assuming you have already `using`ed the relevant types of the `std` namespace):

```cpp
// 1. create an empty vector; constant complexity
vector<int> v0;
// 1+. this line of code can ensure constant time complexity when inserting the first 3 elements into the vector
v0.reserve(3);
// 2. create a vector with initial space 3, whose elements have the default value 0; linear complexity
vector<int> v1(3);
// 3. create a vector with initial space 3, whose elements have the default value 2; linear complexity
vector<int> v2(3, 2);
// 4. create a vector with initial space 3, whose elements have the default value 1,
// and use v2's space allocator; linear complexity
vector<int> v3(3, 1, v2.get_allocator());
// 5. create a copy vector v4 of v2, whose content elements are the same as v2; linear complexity
vector<int> v4(v2);
// 6. create a copy vector v5 of v4, whose content is {v4[1], v4[2]}; linear complexity
vector<int> v5(v4.begin() + 1, v4.begin() + 3);
// 7. move v2 to the newly created vector v6, no copy occurs; constant complexity; requires C++11
vector<int> v6(std::move(v2));  // or v6 = std::move(v2);
```

??? note "Test code"
    ```cpp
    // the following is test code; interested students can compile and run this code themselves.
    cout << "v1 = ";
    copy(v1.begin(), v1.end(), ostream_iterator<int>(cout, " "));
    cout << endl;
    cout << "v2 = ";
    copy(v2.begin(), v2.end(), ostream_iterator<int>(cout, " "));
    cout << endl;
    cout << "v3 = ";
    copy(v3.begin(), v3.end(), ostream_iterator<int>(cout, " "));
    cout << endl;
    cout << "v4 = ";
    copy(v4.begin(), v4.end(), ostream_iterator<int>(cout, " "));
    cout << endl;
    cout << "v5 = ";
    copy(v5.begin(), v5.end(), ostream_iterator<int>(cout, " "));
    cout << endl;
    cout << "v6 = ";
    copy(v6.begin(), v6.end(), ostream_iterator<int>(cout, " "));
    cout << endl;
    ```

We can use the above methods to construct a `vector`, which is enough for our use.

#### Element access

`vector` provides the following methods for element access

1.  `at()`

    `v.at(pos)` returns a reference to the element with subscript `pos` in the container. If the array is out of bounds, it throws an exception of type `std::out_of_range`.

2.  `operator[]`

    `v[pos]` returns a reference to the element with subscript `pos` in the container. It does not perform an out-of-bounds check.

3.  `front()`

    `v.front()` returns a reference to the first element.

4.  `back()`

    `v.back()` returns a reference to the last element.

5.  `data()`

    `v.data()` returns a pointer to the first element in the contiguous memory space that `v` uses internally to store data.

#### Iterators

vector provides the following kinds of [iterators](./iterator.md)

1.  `begin()/cbegin()`

    Return an iterator pointing to the first element, where `*begin = front`.

2.  `end()/cend()`

    Return an iterator pointing to the placeholder at the end of the container; note that there is no element.

3.  `rbegin()/crbegin()`

    Return a reverse iterator pointing to the first element of the reversed array, which can be understood as the last element of the forward container.

4.  `rend()/crend()`

    Return an iterator pointing to the position after the last element of the reversed array, corresponding to the position before the front of the container, with no element.

Among the iterators listed above, those containing the character `c` are read-only iterators; you cannot modify the values of elements in the `vector` through read-only iterators. If a `vector` itself is read-only, then its general iterators and read-only iterators are completely equivalent. Read-only iterators have been supported since C++11.

#### Length and capacity

`vector` has the following functions related to container length and capacity. Note that the length (size) of a `vector` refers to the number of valid elements, while the capacity (capacity) refers to the actual length of memory allocated; for relevant details see the implementation details introduction below.

**Length-related**:

-   `empty()` returns a `bool` value, i.e. `v.begin() == v.end()`, `true` for empty, `false` for non-empty.

-   `size()` returns the container length (number of elements), i.e. `std::distance(v.begin(), v.end())`.

-   `resize(n)` changes the length of the `vector` to `n`. If `n` is greater than the current length, elements are supplemented; if the elements to be supplemented are provided in the parameters, then the parameters are used, otherwise the default value is used; if `n` is less than the current length, then the first `n` elements are retained and the subsequent elements are deleted.

-   `max_size()` returns the maximum possible length of the container.

    **Capacity-related**:

-   `reserve()` makes the `vector` reserve a certain amount of memory space, avoiding unnecessary memory allocation and copying.

-   `capacity()` returns the capacity of the container, i.e. how many elements the current `vector` has already allocated space for.

-   `shrink_to_fit()` makes the capacity of the `vector` consistent with the length, removing the capacity of this `vector` that is not used.

### Element addition, deletion, and modification

-   `clear()` clears all elements
-   `insert()` supports inserting elements at a certain iterator position, and can insert multiple. **The complexity is linear rather than constant in the distance from `pos` to the end**
-   `erase()` deletes an element at a certain iterator or the elements in an interval, returning the last deleted iterator. The complexity is consistent with `insert`.
-   `push_back()` inserts an element at the end, with amortized complexity being **constant** and worst-case linear complexity.
-   `pop_back()` deletes the last element, constant complexity.
-   `swap()` swaps with another container; this operation is **constant complexity** rather than linear.

### Implementation details of `vector`

The underlying layer of `vector` is actually still a fixed-length array; the reason it can achieve dynamic expansion is that it adds operations to avoid quantity overflow. First, it needs to be pointed out that the number of elements (length) $n$ in a `vector` is inconsistent with the maximum number of elements (capacity) $N$ that its allocated memory can contain; `vector` stores these two quantities separately. When adding elements to a `vector`, if it finds $n>N$, then the container will allocate an array of size $2N$, then copy the old data from its original position to the new array, and then release the original memory. Although the asymptotic complexity of this operation is $O(n)$, it can be proved that its amortized complexity is $O(1)$. And deleting elements at the end and accessing elements are both still $O(1)$ overhead.
Therefore, as long as the size of the `vector` is estimated appropriately and `resize()` and `reserve()` are used well, the efficiency of `vector` will not have too large a gap with a fixed-length array.

### `vector<bool>`

The standard library specially provides a `vector` specialization for `bool`, where each "`bool`" occupies only 1 bit and supports dynamic growth. But the return value type of its `operator[]` is not `bool&` but `vector<bool>::reference`. Therefore, `vector<bool>` should be used with caution; you can consider using `deque<bool>` or `vector<char>` instead. And if you need to save space, please directly use [`bitset`](./bitset.md).

## `array` (C++11)

`std::array` is a **memory-contiguous**, **fixed-length** array data structure provided by STL. Its essence is a direct wrapper around the native array.

### Why use `array`

`array` is actually STL's wrapper around an array. Compared with `vector`, it sacrifices the dynamic expansion feature, but in exchange obtains performance almost identical to a native array (under the premise of full optimization). Therefore, if C++11 features can be used, almost all places where a native array can be used can directly replace the fixed-length array with `array`, and a dynamically-allocated array can be replaced with `vector`.

### Member functions

#### Implicitly defined member functions

| Function | Effect |
| ----------- | ----------------------------------- |
| `operator=` | Rewrites the corresponding element of `array` with each element from another `array` |

#### Element access

| Function | Effect |
| ------------ | -------------------- |
| `at` | Access the specified element, also performing an out-of-bounds check |
| `operator[]` | Access the specified element, **not** performing an out-of-bounds check |
| `front` | Access the first element |
| `back` | Access the last element |
| `data` | Return a pointer to the first element of the array in memory |

`at` throws `std::out_of_range` if it encounters the case `pos >= size()`.

#### Capacity

| Function | Effect |
| ---------- | ----------- |
| `empty` | Check whether the container is empty |
| `size` | Return the number of contained elements |
| `max_size` | Return the maximum number of containable elements |

Since each `array` is a fixed-size container, the value returned by `size()` equals the value returned by `max_size()`.

### Operations

| Function | Effect |
| ------ | -------- |
| `fill` | Fill the container with the specified value |
| `swap` | Swap contents |

**Note that swapping two `array`s is $\Theta(\text{size})$, rather than $O(1)$ as with regular STL containers.**

### Non-member functions

| Function | Effect |
| -------------- | ------------------- |
| `operator==` etc. | Compare the values in `array` in lexicographic order |
| `std::get` | Access an element of `array` |
| `std::swap` | Specialized `std::swap` algorithm |

Below is a usage example of `array`:

```cpp
// 1. create an empty array of length 3; constant complexity
std::array<int, 3> v0;
// 2. create an array with specified constants; constant complexity
std::array<int, 3> v1{1, 2, 3};

v0.fill(1);  // fill the array

// access the array
for (int i = 0; i != arr.size(); ++i) cout << arr[i] << " ";
```

## `deque`

`std::deque` is the [double-ended queue](../../ds/queue.md#double-ended-queue) data structure provided by STL. It can provide linear-complexity insertion and deletion, as well as constant-complexity random access.

### Usage of `deque`

Below we introduce common usages; for detailed content [please see the C++ documentation](https://zh.cppreference.com/w/cpp/container/deque). The iterator functions of `deque` are the same as `vector`, so they are not introduced in detail.

#### Constructors

See the following code (assuming you have already `using`ed the relevant types of the `std` namespace):

```cpp
// 1. define an empty int-type double-ended queue v0
deque<int> v0;
// 2. define an int-type double-ended queue v1 and set the initial size to 10; linear complexity
deque<int> v1(10);
// 3. define an int-type double-ended queue v2 and initialize it to ten 1s; linear complexity
deque<int> v2(10, 1);
// 4. copy the existing double-ended queue v1; linear complexity
deque<int> v3(v1);
// 5. create a copy deque v4 of v2, whose content is v4[0] to v4[2]; linear complexity
deque<int> v4(v2.begin(), v2.begin() + 3);
// 6. move v2 to the newly created deque v5, no copy occurs; constant complexity; requires C++11
deque<int> v5(std::move(v2));
```

#### Element access

Consistent with `vector`, but the underlying memory cannot be accessed. For its efficient element access speed, refer to the implementation details part.

-   `at()` returns a reference to the element at the specified position in the container, performing an out-of-bounds check, **constant complexity**.
-   `operator[]` returns a reference to the element at the specified position in the container. It does not perform an out-of-bounds check, **constant complexity**.
-   `front()` returns a reference to the first element.
-   `back()` returns a reference to the last element.

#### Iterators

Consistent with `vector`.

#### Length

Consistent with `vector`, but without the `reserve()` and `capacity()` functions. (Still has the `shrink_to_fit()` function.)

#### Element addition, deletion, and modification

Consistent with `vector`, and additionally has functions for adding elements to the head of the queue.

-   `clear()` clears all elements
-   `insert()` supports inserting elements at a certain iterator position, and can insert multiple. **The complexity is linear in the smaller of the distances from `pos` to the two ends**.
-   `erase()` deletes an element at a certain iterator or the elements in an interval, returning the last deleted iterator. The complexity is consistent with `insert`.
-   `push_front()` inserts an element at the head, **constant complexity**.
-   `pop_front()` deletes the head element, **constant complexity**.
-   `push_back()` inserts an element at the end, **constant complexity**.
-   `pop_back()` deletes the last element, **constant complexity**.
-   `swap()` swaps with another container; this operation is **constant complexity** rather than linear.

### Implementation details of `deque`

The usual underlying implementation of `deque` is multiple non-contiguous buffers, while the memory within a buffer is contiguous. And each buffer also records a head pointer and a tail pointer, used to mark the interval of valid data. When a buffer is filled, a new buffer is allocated before or after it to store more data. For a more detailed explanation, refer to [《STL Source Code Analysis》 deque implementation principle](https://www.cnblogs.com/q1076452761/p/16903229.html).

## `list`

`std::list` is the [doubly linked list](../../ds/linked-list.md) data structure provided by STL. It can provide linear-complexity random access, as well as constant-complexity insertion and deletion.

### Usage of `list`

The usage of `list` is basically the same as `deque`, but the complexity of addition/deletion operations and access is different. For detailed content [please see the C++ documentation](https://zh.cppreference.com/w/cpp/container/list). The functions of `list` related to iterators, length, and element addition/deletion/modification are the same as `deque`, so they are not introduced in detail.

#### Element access

Since the implementation of `list` is a linked list, it does not provide a random-access interface. If you need to access a middle element, you need to use iterators.

-   `front()` returns a reference to the first element.
-   `back()` returns a reference to the last element.

#### Operations

The `list` type also provides some STL algorithm functions implemented for its characteristics. Since these algorithms require [random access iterators](./iterator.md), `list` provides special implementations for convenient use. These algorithms include `splice()`, `remove()`, `sort()`, `unique()`, `merge()`, etc.

## `forward_list` (C++11)

`std::forward_list` is the [singly linked list](../../ds/linked-list.md) data structure provided by STL; compared with `std::list`, it reduces the space overhead.

### Usage of `forward_list`

The usage of `forward_list` is almost the same as `list`, but the iterators are only unidirectional, so its specific usage is not introduced in detail. For detailed content [please see the C++ documentation](https://zh.cppreference.com/w/cpp/container/forward_list)
