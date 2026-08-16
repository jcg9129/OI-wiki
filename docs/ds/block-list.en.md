author: HeRaNO, konnyakuxzy, littlefrog

![./images/kuaizhuanglianbiao.png](./images/kuaizhuanglianbiao.png "./images/kuaizhuanglianbiao.png")

A block linked list roughly looks like this……

It is not hard to see that a block linked list is just a linked list where each node points to an array.
We divide the original array of length n into $\sqrt{n}$ nodes, each node corresponding to an array of size $\sqrt{n}$.
So we define the struct like this; the code is below.
Here `sqn` denotes `sqrt(n)`, i.e. $\sqrt{n}$, and `pb` denotes `push_back`, i.e. adding an element into this `node`.

???+ note "Implementation"
    ```cpp
    struct node {
      node* nxt;
      int size;
      char d[(sqn << 1) + 5];
    
      node() { size = 0, nxt = NULL, memset(d, 0, sizeof(d)); }
    
      void pb(char c) { d[size++] = c; }
    };
    ```

A block linked list should support at least: splitting, insertion, and search.
What is splitting? Splitting is splitting one `node` into two smaller `node`s, so as to keep the size of each `node` close to $\sqrt{n}$ (otherwise it may degenerate into an ordinary array). When the size of a `node` exceeds $2\times \sqrt{n}$, perform the split operation.

How is the split operation done? First create a new node, then `copy` the last $\sqrt{n}$ values of the node being split into the new node, then delete the last $\sqrt{n}$ values of the node being split (`size--`), and finally insert the new node after the node being split.

The complexity of all operations of a block linked list is $\sqrt{n}$.

One more thing to say.
As elements are inserted (or deleted), $n$ changes, and so does $\sqrt{n}$. Then the block size would change; do we have to maintain the block size every time?

Actually not; just set $\sqrt{n}$ to a fixed value. For example, if the range given by the problem is $10^6$, then set $\sqrt{n}$ to a constant of size $10^3$ and do not change it.

```cpp
list<vector<char>> orz_list;
```

## `rope` in libstdc++

### Introduction

The `rope` in libstdc++ also serves the role of a block linked list; it is implemented with a persistent balanced tree and can perform random access and insertion and deletion of elements.

Since `rope` is not truly implemented with a block linked list, its time complexity is not equivalent to that of a block linked list, but is equivalent to the complexity of a persistent balanced tree (i.e. $O(\log n)$).

You can introduce it with the following method:

```cpp
#include <ext/rope>
using namespace __gnu_cxx;
```

???+ warning "About library functions beginning with a double underscore"
    In OI, whether library functions beginning with a double underscore could be used was long uncertain; the [Supplementary Explanation on Programming Language Usage Restrictions in NOI-Series Activities](https://www.noi.cn/xw/2021-09-01/735729.shtml) released by CCF in 2021 mentions "library functions or macros beginning with an underscore are allowed, except for library functions and macros with explicitly forbidden operations." So `rope` can currently be used normally in OI.

### Basic operations

|             Operation            |               Effect              |
| :-----------------------: | :---------------------------: |
|       `rope<int> a`       | Initialize a `rope` (very similar to containers like `vector`) |
|      `a.push_back(x)`     |       Add element `x` at the end of `a`       |
|     `a.insert(pos, x)`    |   Add element `x` at position `pos` of `a`   |
|     `a.erase(pos, x)`     |  Delete `x` elements at position `pos` of `a`  |
|     `a.at(x)` or `a[x]`    |       Access the `x`-th element of `a`       |
| `a.length()` or `a.size()` |           Get the size of `a`          |

## Example

[POJ2887 Big String](http://poj.org/problem?id=2887)

Editorial:
A very simple template problem. The code is as follows:

```cpp
--8<-- "docs/ds/code/block-list/block-list_1.cpp"
```
