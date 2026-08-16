## `set`

`set` is an associative container, a sorted set containing objects of the key type; search, removal, and insertion have logarithmic complexity. `set` is usually implemented internally using a [red-black tree](../../ds/rbtree.md). The characteristics of a [balanced binary tree](../../ds/bst.md) make `set` very suitable for handling situations that need to simultaneously take into account search, insertion, and deletion.

Similar to a set in mathematics, elements with the same value will not appear in a `set`. If you need a set with identical elements, you need to use `multiset`. The usage of `multiset` is basically the same as the usage of `set`.

### Insertion and deletion operations

-   `insert(x)` inserts element x into the `set` when there is no equivalent element in the container.
-   `erase(x)` deletes **all** elements with value x, returning the number of deleted elements.
-   `erase(pos)` deletes the element with iterator pos; the iterator is required to be valid.
-   `erase(first,last)` deletes all elements with iterators in the range $[first,last)$.
-   `clear()` clears the `set`.

???+ note "The return value of the insert function"
    The return value type of the insert function is `pair<iterator, bool>`, where iterator is an iterator pointing to the inserted element (or to the element already in the container that equals the inserted value), and bool represents whether the element was inserted successfully; since the elements in a `set` have a uniqueness property, if there is already an element of equal value in the `set`, the insertion will fail and return false, otherwise the insertion succeeds and returns true; the insert in `map` is also like this.

### Iterators

`set` provides the following kinds of iterators:

1.  `begin()/cbegin()`   
    Return an iterator pointing to the first element, where `*begin = front`.
2.  `end()/cend()`   
    Return an iterator pointing to the placeholder at the end of the array; note that there is no element.
3.  `rbegin()/crbegin()`   
    Return a reverse iterator pointing to the first element of the reversed array, which can be understood as the last element of the forward container.
4.  `rend()/crend()`   
    Return an iterator pointing to the position after the last element of the reversed array, corresponding to the position before the front of the container, with no element.

Among the iterators listed above, those containing the character `c` are read-only iterators; you cannot modify the values of elements in the `set` through read-only iterators. If a `set` itself is read-only, then its general iterators and read-only iterators are completely equivalent. Read-only iterators have been supported since C++11.

### Search operations

-   `count(x)` returns the number of elements in the `set` with key x.
-   `find(x)` returns the iterator of the element when an element with key x exists in the `set`, otherwise returns `end()`.
-   `lower_bound(x)` returns an iterator pointing to the first element not less than the given key. If no such element exists, returns `end()`.
-   `upper_bound(x)` returns an iterator pointing to the first element greater than the given key. If no such element exists, returns `end()`.
-   `empty()` returns whether the container is empty.
-   `size()` returns the number of elements in the container.

???+ warning "The time complexity of `lower_bound` and `upper_bound`"
    The time complexity of `set`'s built-in `lower_bound` and `upper_bound` is $O(\log n)$.
    
    But using the `lower_bound` and `upper_bound` functions in the `algorithm` library to query elements in a `set` has time complexity $O(n)$.

???+ warning "The time complexity of `nth_element`"
    `set` does not provide a built-in `nth_element`. Using `nth_element` in the `algorithm` library to find the $k$-th largest element has time complexity $O(n)$.
    
    If you need to implement the $O(\log n)$ functionality of finding the $k$-th largest element that a balanced binary tree possesses, you need to hand-write a balanced binary tree or a weighted segment tree, or choose to use the balanced binary tree in the pb\_ds library.

### Usage examples

#### Using `set` in greedy algorithms

In greedy algorithms, we often need something like **finding and deleting the smallest element greater than or equal to a certain value**. This operation can be easily completed through `set`.

```cpp
// currently available elements
set<int> available;
// the value to be greater than or equal to
int x;

// find the smallest element greater than or equal to x
set<int>::iterator it = available.lower_bound(x);
if (it == available.end()) {
  // no such element exists, then perform the corresponding operation……
} else {
  // found such an element, remove it from the currently available elements
  available.erase(it);
  // perform the corresponding operation……
}
```

## `map`

`map` is an ordered key-value pair container; the keys of its elements are unique. Search, removal, and insertion operations have logarithmic complexity. `map` is usually implemented as a [red-black tree](../../ds/rbtree.md).

Imagine the following scenario: now we need to store some key-value pairs, for example storing student names corresponding to scores: `Tom 0`, `Bob 100`, `Alan 100`. But since array subscripts can only be non-negative integers, we cannot use names as subscripts to store them; at this time the simplest way is to use the `map` in STL.

`map` overloads `operator[]`, and can use any type that defines `operator <` as a subscript (in `map` it is called `key`, i.e. the index):

```cpp
map<Key, T> yourMap;
```

Here, `Key` is the type of the key, and `T` is the type of the value; below is an example of using `map`:

```cpp
map<string, int> mp;
```

Elements with the same key will not exist in a `map`, while `multimap` allows multiple elements to have the same key. The usage of `multimap` is basically the same as the usage of `map`.

??? warning "Warning"
    Precisely because `multimap` allows multiple elements to have the same key, `multimap` does not provide a method to access its corresponding value given a key.

### Insertion and deletion operations

-   We can directly perform query or insertion operations through subscript access. For example `mp["Alan"]=100`.
-   Inserting a value of type `pair<Key, T>` into a `map` achieves the purpose of inserting an element, for example `mp.insert(pair<string,int>("Alan",100));`;
-   The `erase(key)` function deletes **all** elements with key `key`. The return value is the number of deleted elements.
-   `erase(pos)`: deletes the element with iterator pos; the iterator is required to be valid.
-   `erase(first,last)`: deletes all elements with iterators in the range $[first,last)$.
-   The `clear()` function clears the entire container.

???+ note "Points to note in subscript access"
    When accessing an element in a `map` using a subscript, if an element with the corresponding key does not exist in the `map`, a new element will be automatically inserted into the `map`, and its value will be set to the default value (for integers, the value is zero; for types with a default constructor, the default constructor will be called for initialization).
    
    When subscript access operations are too frequent, a large number of meaningless elements will appear in the container, affecting the efficiency of the `map`. Therefore, in general, it is recommended to use the `find()` function to find the element with a specific key.

### Query operations

-   `count(x)`: returns the number of elements in the container with key x. The complexity is $O(\log(size)+ans)$ (logarithmic complexity in the container size, plus the number of matches).
-   `find(x)`: if an element with key x exists in the container, returns the iterator of the element; otherwise returns `end()`.
-   `lower_bound(x)`: returns an iterator pointing to the first element not less than the given key.
-   `upper_bound(x)`: returns an iterator pointing to the first element greater than the given key. If all elements in the container are less than or equal to the given key, returns `end()`.
-   `empty()`: returns whether the container is empty.
-   `size()`: returns the number of elements in the container.

### Usage examples

#### Using `map` to store complex states

In searching, we sometimes need to store some relatively complex states (such as coordinates, values that cannot be discretized, strings, etc.) as well as answers related to them (such as the minimum number of steps to reach this state). `map` can be used to implement this functionality. The key is the state, and the value is the answer related to it. The following example shows how to use `map` to store states represented as `string`.

```cpp
// store states and corresponding answers
map<string, int> record;

// the newly searched state and corresponding answer
string status;
int ans;
// find whether the corresponding state has appeared before
map<string, int>::iterator it = record.find(status);
if (it == record.end()) {
  // this state has not been searched yet, add it to the state record
  record[status] = ans;
  // perform the corresponding operation……
} else {
  // this state has already been searched, perform the corresponding operation……
}
```

## Traversing a container

We can use iterators to traverse all elements of an associative container.

```cpp
set<int> s;
using si = set<int>::iterator;
for (si it = s.begin(); it != s.end(); it++) cout << *it << endl;
```

Note that after dereferencing the iterator of a `map`, we obtain a key-value pair of type `pair<Key, T>`.

In C++11, using a range-based for loop makes the code much more concise:

```cpp
set<int> s;
for (auto x : s) cout << x << endl;
```

For any associative container, the time complexity of traversing the container using iterators is $O(n)$.

## Custom comparison methods

The comparison function of `set` by default is `<` (if it is a non-built-in type, you need to [overload the `<` operator](../op-overload.md#comparison-operators)). However, in some special cases, we hope to customize the comparison method inside the `set`.

At this time, we can solve the problem by passing in a custom comparator.

Specifically, we need to define a class and [overload the `()` operator](../op-overload.md#function-call-operator) in this class.

For example, if we want to maintain a `set` that stores integers with larger values in front, we can implement it like this:

```cpp
struct cmp {
  bool operator()(int a, int b) const { return a > b; }
};

set<int, cmp> s;
```

For other associative containers, we can implement custom comparison in a similar way; we will not go into detail here.
