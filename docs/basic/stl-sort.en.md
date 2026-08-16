This page briefly introduces the sorting algorithms implemented in the C and C++ standard libraries.

Except for functions explicitly noted otherwise, the functions listed on this page are by default defined in the header `<algorithm>`.

## qsort

See: [`qsort`](https://zh.cppreference.com/w/c/algorithm/qsort), [`std::qsort`](https://zh.cppreference.com/w/cpp/algorithm/qsort)

This function is the [quicksort](./quick-sort.md) implemented by the C standard library, defined in `<stdlib.h>`. In the C++ standard library, this function is defined in `<cstdlib>`.

### The comparison function of qsort and bsearch

The qsort function has four parameters: the array name, the number of elements, the element size, and the comparison rule. The comparison rule is implemented by specifying a comparison function; specifying different comparison functions can achieve different sorting rules.

The parameters of the comparison function are restricted to two `const void` pointers. The return value is specified to be a positive number, a negative number, or 0.

One example way to write the comparison function is:

```c
int compare(const void *p1, const void *p2)  // comparison function for an int array
{
  int *a = (int *)p1;
  int *b = (int *)p2;
  if (*a > *b)
    return 1;  // returning a positive number means a is greater than b
  else if (*a < *b)
    return -1;  // returning a negative number means a is less than b
  else
    return 0;  // returning 0 means a and b are equivalent
}
```

Note: replacing the positive/negative return value with the difference of the two elements is a typical mistake, because it may cause overflow errors.

Below is an example of sorting a struct:

```c
struct eg  // example struct
{
  int e;
  int g;
};

int compare(const void *p1,
            const void *p2)  // comparison function for a struct eg array: sort by member e
{
  struct eg *a = (struct eg *)p1;
  struct eg *b = (struct eg *)p2;
  if (a->e > b->e)
    return 1;  // returning a positive number means a is greater than b
  else if (a->e < b->e)
    return -1;  // returning a negative number means a is less than b
  else
    return 0;  // returning 0 means a and b are equivalent
}
```

This also shows that equivalent does not mean equal; it only means that the two elements are equivalent under this comparison rule.

## std::sort

See: [`std::sort`](https://zh.cppreference.com/w/cpp/algorithm/sort)

Usage:

```cpp
// a[0] .. a[n - 1] is the sequence to be sorted
// sort a in place, arranging it in ascending order
std::sort(a, a + n);

// cmp is a custom comparison function
std::sort(a, a + n, cmp);
```

Note: the return value of sort's comparison function is true and false, using true and false to indicate the magnitude (order) relationship between two elements, which is entirely different in semantics from qsort's three-valued comparison function. For details, see the sort documentation given above.

If you want to simply rewrite sort as qsort while keeping the sort order the same overall (ignoring equivalent elements), you need to change returning true to -1 and returning false to 1.

The `std::sort` function is the more commonly used C++ library comparison function. The last parameter of this function is a binary comparison function; when the `cmp` function is not specified, it sorts in ascending order by default.

The old C++ standard only required its **average** time complexity to reach $O(n\log n)$. The C++11 standard and subsequent standards require its **worst-case** time complexity to reach $O(n\log n)$.

The C++ standard does not strictly require the implementation algorithm of this function; the specific implementation depends on the compiler. The implementations in both [libstdc++](https://github.com/mirrors/gcc/blob/master/libstdc++-v3/include/bits/stl_algo.h) and [libc++](http://llvm.org/svn/llvm-project/libcxx/trunk/include/algorithm) use [introsort](./quick-sort.md#introsort).

## std::nth\_element

See: [`std::nth_element`](https://zh.cppreference.com/w/cpp/algorithm/nth_element)

Usage:

```cpp
std::nth_element(first, nth, last);
std::nth_element(first, nth, last, cmp);
```

It rearranges the elements in `[first, last)` so that the element pointed to by `nth` is changed to the element that would appear at that position after `[first, last)` is sorted. All elements before this new `nth` element are less than or equal to all elements after the new `nth` element.

The implementation algorithm is an unfinished introsort.

For both of the above usages, the C++ standard requires its average time complexity to be $O(n)$, where n is `std::distance(first, last)`.

It is often used to build a [K-D Tree](../ds/kdt.md).

## std::stable\_sort

See: [`std::stable_sort`](https://zh.cppreference.com/w/cpp/algorithm/stable_sort)

Usage:

```cpp
std::stable_sort(first, last);
std::stable_sort(first, last, cmp);
```

Stable sort, guaranteeing that the relative positions of equal elements after sorting are the same as in the original sequence.

The time complexity is $O(n\log^2 n)$; when extra memory is available, the complexity is $O(n\log n)$.

## std::partial\_sort

See: [`std::partial_sort`](https://zh.cppreference.com/w/cpp/algorithm/partial_sort)

Usage:

```cpp
// mid = first + k
std::partial_sort(first, mid, last);
std::partial_sort(first, mid, last, cmp);
```

Sort the first `k` elements of the sequence in place in the order given by `cmp`; the order of the following elements is not guaranteed. When the `cmp` function is not specified, it sorts in ascending order by default.

Complexity: approximately $(\mathit{last}-\mathit{first})\log(\mathit{mid}-\mathit{first})$ applications of `cmp`.

Principle:

The idea of `std::partial_sort` is: perform a `make_heap()` operation on the elements in the range `[first, mid)` of the original container to build a max-heap, then compare each element in `[mid, last)` with `first`, ensuring the element at `first` is the maximum in the heap. If it is smaller than that maximum, swap the element positions and adjust the elements in `[first, mid)` to keep the max-heap order. After the comparisons, perform one heap-sort `sort_heap()` operation on the elements in `[first, mid)` to arrange them in increasing order. Note that heap order and increasing order are different.

## Custom comparison

See: [operator overloading](https://zh.cppreference.com/w/cpp/language/operators)

Built-in types (such as `int`) and user-defined structs allow customizing the comparison function used when calling the STL sorting functions. You can pass a function implementing a binary comparison as the last parameter when calling the function.

For a user-defined struct, before using an STL sorting function on it you must define at least one relational operator, or provide a binary comparison function when using the function. Defining `operator<` is usually recommended. [^note1]

Example:

```cpp
int a[1009], n = 10;
// ...
std::sort(a + 1, a + 1 + n);                  // sort in ascending order
std::sort(a + 1, a + 1 + n, greater<int>());  // sort in descending order
```

```cpp
struct data {
  int a, b;

  bool operator<(const data rhs) const {
    return (a == rhs.a) ? (b < rhs.b) : (a < rhs.a);
  }
} da[1009];

bool cmp(const data u1, const data u2) {
  return (u1.a == u2.a) ? (u1.b > u2.b) : (u1.a > u2.a);
}

// ...
std::sort(da + 1, da + 1 + 10);  // use the < operator defined in the struct, sort in ascending order
std::sort(da + 1, da + 1 + 10, cmp);  // use the cmp function for comparison, sort in descending order
```

### Strict weak ordering

See also: [Applications in C++ - Order theory](../math/order-theory.md#c-中的应用)

The operator used for sorting must satisfy a [strict weak ordering](../math/order-theory.md#二元关系), otherwise unpredictable situations will occur (such as runtime errors or incorrect sorting).

Common mistakes:

-   Using `<=` to define the less-than operator in sorting.
-   Reading, when calling the sort operator, an array whose external values may change (common in shortest-path algorithms).
-   Using the result of comparing the maximum/minimum of several numbers as the sort operator (such as the classic mistake in the Queen's Game / Production Scheduling problems).

## External links

-   [A discussion of applications of adjacent-swap sorting and issues to note](https://ouuan.github.io/浅谈邻项交换排序的应用以及需要注意的问题/)

## References and notes

[^note1]: Because most standard algorithms use `operator<` for comparison by default.
