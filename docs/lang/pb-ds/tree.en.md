## `__gnu_pbds::tree`

Attached: [Official documentation address](https://gcc.gnu.org/onlinedocs/libstdc++/ext/pb_ds/tree_based_containers.html)

```cpp
#include <ext/pb_ds/assoc_container.hpp>  // because tree is defined here, this header file needs to be included
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
__gnu_pbds::tree<Key, Mapped, Cmp_Fn = std::less<Key>, Tag = rb_tree_tag,
                 Node_Update = null_tree_node_update,
                 Allocator = std::allocator<char>>
```

## Template formal parameters

-   `Key`: the type of the stored element; if you want to store multiple identical `Key` elements, you need to use a method similar to `std::pair` and `struct`, and use the `lower_bound` and `upper_bound` member functions for searching
-   `Mapped`: the mapping rule (Mapped-Policy) type; if you want to indicate that the associative container is a **set**, similar to storing elements in `std::set`, fill in `null_type` here (in lower versions of `g++` this is `null_mapped_type`); if you want to indicate that the associative container is a **set with values**, similar to storing elements in `std::map`, fill in the `Value` type similar to `std::map<Key, Value>` here
-   `Cmp_Fn`: the key comparison functor, such as `std::less<Key>`
-   `Tag`: choose which underlying data structure type to use; the default is `rb_tree_tag`. `__gnu_pbds` provides three different balanced trees, namely:
    -   `rb_tree_tag`: red-black tree, generally use this; the performance of the latter two is generally not as good as the red-black tree
    -   `splay_tree_tag`: splay tree
    -   `ov_tree_tag`: ordered vector tree, just an ordered structure implemented by `vector`, similar to using a sorted `vector` to implement a balanced tree; the performance depends on whether the data wants to break you
-   `Node_Update`: the policy used to update nodes; the default is `null_node_update`; if you want to use the `order_of_key` and `find_by_order` methods, you need to use `tree_order_statistics_node_update`
-   `Allocator`: the space allocator type

## Construction method

```cpp
__gnu_pbds::tree<std::pair<int, int>, __gnu_pbds::null_type,
                 std::less<std::pair<int, int>>, __gnu_pbds::rb_tree_tag,
                 __gnu_pbds::tree_order_statistics_node_update>
    trr;
```

## Member functions

-   `insert(x)`: insert an element `x` into the tree, returning `std::pair<point_iterator, bool>`, where the first element represents the iterator of the insertion position, and the second element represents whether the insertion succeeded.
-   `erase(x)`: delete an element/iterator `x` from the tree. If `x` is an iterator, return the iterator pointing to the next one after `x` (if `x` is `end()`, return `end()`); if `x` is a `Key`, return whether the deletion succeeded (if it does not exist, the deletion fails).
-   `order_of_key(x)`: return the number of elements strictly less than `x` (using `Cmp_Fn` as the comparison logic), i.e. the rank starting from $0$.
-   `find_by_order(x)`: return the iterator of the element corresponding to the rank compared by `Cmp_Fn`.
-   `lower_bound(x)`: return the iterator corresponding to the first element not less than `x` (using `Cmp_Fn` as the comparison logic).
-   `upper_bound(x)`: return the iterator corresponding to the first element strictly greater than `x` (using `Cmp_Fn` as the comparison logic).
-   `join(x)`: merge the `x` tree into the current tree, and the `x` tree is cleared (you must ensure that the **comparison functions** and **element types** of the two trees are the same).
-   `split(x,b)`: comparing with `Cmp_Fn`, those less than or equal to `x` belong to the current tree, and the rest belong to the `b` tree.
-   `empty()`: return whether it is empty.
-   `size()`: return the size.

???+ warning "Note"
    The `join(x)` function needs to guarantee that the value range of the keys of the merged-in tree and the value range of the keys of the merged-into tree are **disjoint** (that is, all values in the merged-in tree must all be greater than/less than all values in the current tree), otherwise a `join_error` exception will be thrown.
    
    If you want to merge two trees whose value ranges intersect, you need to insert the elements of one tree one by one into the other tree.

## Example

```cpp
// Common Header Simple over C++11
#include <iostream>
using namespace std;
using ll = long long;
using ull = unsigned long long;
using ld = long double;
using pii = pair<int, int>;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
__gnu_pbds::tree<pair<int, int>, __gnu_pbds::null_type, less<pair<int, int>>,
                 __gnu_pbds::rb_tree_tag,
                 __gnu_pbds::tree_order_statistics_node_update>
    trr;

int main() {
  int cnt = 0;
  trr.insert(make_pair(1, cnt++));
  trr.insert(make_pair(5, cnt++));
  trr.insert(make_pair(4, cnt++));
  trr.insert(make_pair(3, cnt++));
  trr.insert(make_pair(2, cnt++));
  // elements on the tree {(1,0), (2,4), (3,3), (4,2), (5,1)}

  auto it = trr.lower_bound(make_pair(2, 0));
  trr.erase(it);
  // elements on the tree {(1,0), (3,3), (4,2), (5,1)}

  // output the first of the element with rank 1 among ranks 0 1 2 3
  auto it2 = trr.find_by_order(1);
  cout << (*it2).first << endl;  // output: 3

  // output its rank
  int pos = trr.order_of_key(*it2);
  cout << pos << endl;  // output: 1

  // split trr according to it2
  decltype(trr) newtr;
  trr.split(*it2, newtr);
  for (auto i = newtr.begin(); i != newtr.end(); ++i) {
    cout << (*i).first << ' ';  // output: 4 5
  }
  cout << endl;

  // merge the newtr tree into the trr tree, and the newtr tree is cleared.
  trr.join(newtr);
  for (auto i = trr.begin(); i != trr.end(); ++i) {
    cout << (*i).first << ' ';  // output: 1 3 4 5
  }
  cout << endl;
  cout << newtr.size() << endl;  // output: 0

  return 0;
}
```

## References

-   [Tree-Based Containers](https://gcc.gnu.org/onlinedocs/libstdc++/ext/pb_ds/tree_based_containers.html)
-   [Implementation of the `join` function in GCC 14.1.0](https://gcc.gnu.org/onlinedocs/gcc-14.1.0/libstdc++/api/a18391_source.html#l00043)
-   [Implementation of the `erase` function in GCC 14.1.0](https://gcc.gnu.org/onlinedocs/gcc-14.1.0/libstdc++/api/a18211_source.html#l00043)
