In STL, an iterator (Iterator) is an object used to access and inspect elements in an STL container; its behavior pattern is similar to a pointer, but it encapsulates some validity checks and provides a unified access format. Similar concepts exist in many other high-level languages, such as Python's `__iter__` function and C#'s `IEnumerator`.

## Basic usage

Iterators sound rather obscure; in fact, an iterator itself can be regarded as a data pointer. Iterators mainly support two operators: increment (`++`) and dereference (the unary `*` operator), where increment is used to move the iterator, and dereference can get or modify the element it points to.

The type of an iterator pointing to an element in some [STL container](./container.md) `container` is generally `container::iterator`.

Iterators can be used to traverse a container; for example, the following two for loops have the same effect:

```cpp
vector<int> data(10);

for (int i = 0; i < data.size(); i++)
  cout << data[i] << endl;  // access elements using subscripts

for (vector<int>::iterator iter = data.begin(); iter != data.end(); iter++)
  cout << *iter << endl;  // access elements using iterators
// after C++11, you can use auto iter = data.begin() to simplify the above code
```

???+ tip "The use of `auto` in competitions"
    Most contestants like to use `auto` instead of cumbersome iterator declarations. According to the [Supplementary explanation on the restriction of programming language use in NOI series activities](https://www.noi.cn/xw/2021-09-01/735729.shtml) released in September 2021, NOI series contests (including CSP J/S) will use **C++14** when judging, and this version already supports the `auto` keyword.

## Classification

In the definition of STL, iterators are divided into the following categories in order according to the operations they support:

-   InputIterator (input iterator): only requires support for copy, increment, and dereference access.
-   OutputIterator (output iterator): only requires support for copy, increment, and dereference assignment.
-   ForwardIterator (forward iterator): on the basis of InputIterator, supports multiple traversal dereference access of the iterator, and guarantees that the results of multiple accesses are consistent.
-   BidirectionalIterator (bidirectional iterator): on the basis of ForwardIterator, supports decrement (i.e. reverse access).
-   RandomAccessIterator (random access iterator): on the basis of BidirectionalIterator, supports addition/subtraction operations and comparison operations (i.e. random access).
-   ContiguousIterator (contiguous iterator): on the basis of RandomAccessIterator, requires that for a dereferenceable iterator `a + n`, `*(a + n)` is equivalent to `*(std::address_of(*a) + n)` (i.e. contiguous storage, where `a` is a contiguous iterator and `n` is an integer value).

    ContiguousIterator was formally introduced in C++17.

???+ tip "Why is the input iterator called the input iterator?"
    "Input" refers to "input can be obtained from the iterator", and "output" refers to "output can be made to the iterator".
    
    The agent of "input" and "output" is other parts of the program, not the iterator itself.

These classifications of iterators are not mutually exclusive. In fact, except for the output iterator, the iterators listed earlier all contain the iterators listed later. For example, in a place that requires a forward iterator, a bidirectional iterator can equally be used. Starting from the forward iterator, if these iterators also implement the functionality of the output iterator (i.e. allow write operations), they are called mutable iterators. From this, categories such as "mutable random access iterator" can be derived.

Different [STL containers](./container.md) support different iterator types, which needs attention when using them.

An array pointer satisfies all the requirements of a contiguous iterator (or a random access iterator, for versions up to and including C++14) and can be used as a contiguous iterator.

## Related functions

Many [STL functions](./algorithm.md) use iterators as parameters.

We can use `std::advance(it, n)` to move the iterator `it` backward `n` steps; if `n` is negative, it corresponds to moving forward, in which case the iterator must satisfy the bidirectional iterator, otherwise the behavior is undefined.

After C++11, we can use `std::next(it)` to obtain the successor of the forward iterator `it` (at this time the iterator `it` is unchanged), and `std::next(it, n)` to obtain the `n`-th successor of the forward iterator `it`.

After C++11, we can use `std::prev(it)` to obtain the predecessor of the bidirectional iterator `it` (at this time the iterator `it` is unchanged), and `std::prev(it, n)` to obtain the `n`-th predecessor of the bidirectional iterator `it`.

[STL containers](./container.md) generally support access starting from one end or both ends, as well as support for the [const qualifier](../const.md). For example, the container's `begin()` function can obtain an iterator pointing to the first element of the container, the `rbegin()` function can obtain a reverse iterator pointing to the last element of the container, the `cbegin()` function can obtain a const iterator pointing to the first element of the container, and the `end()` function can obtain an iterator pointing to the end of the container (the "end" is not the last element; it can be regarded as the successor of the last element; the predecessor of the "end" is the last element in the container, and it itself does not point to any element).

You can view more usages at [Iterator library - cppreference.com](https://en.cppreference.com/w/cpp/iterator).
