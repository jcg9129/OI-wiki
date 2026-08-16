author: 0x03A6, abc1763613206, auuuu4, CCXXXI, Conless, Enter-tainer, fanenr, happyZYM, hsfzLZH1, iamtwz, LeverImmy, leverimmy, Lhcfl, Marcythm, RIvance, Tiphereth-A, trudbot, Xeniume, Xeonacid, YBYCS, yuhuoji

A red-black tree is a self-balancing binary search tree. Each node additionally stores a color field ("RED" or "BLACK"), used to ensure the tree stays balanced during insertion and deletion.

The red-black tree is a variant of the order-4 B-tree ([2-3-4 tree](https://en.wikipedia.org/wiki/2%E2%80%933%E2%80%934_tree)). [^gilbas1978]

## Properties

A valid red-black tree must obey the following four properties:

1.  A node is either red or black
2.  A NIL node (empty leaf node) is black
3.  The children of a red node are black
4.  Every path from the root node to a NIL node has the same number of black nodes

The figure below is a valid red-black tree:

![rbtree-example](images/rbtree-example.svg)

???+ note "Note"
    Some materials also add a fifth property, i.e. the root node must be black; this property requires that after completing an insertion, if the root node is red then dye it black, but since the operation of dyeing the root black can also be deferred to the deletion operation, this property is not necessarily satisfied (the code implementation given in this article satisfies this property). For rigor, here we also cite the [Wikipedia original text](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree#Properties) for explanation:
    
    > Some authors, e.g. Cormen & al.,[^cite_note-cormen2009-18]claim "the root is black" as fifth requirement; but not Mehlhorn & Sanders[^cite_note-mehlhorn2008-17]or Sedgewick & Wayne.[^cite_note-algs4-16]Since the root can always be changed from red to black, this rule has little effect on analysis. This article also omits it, because it slightly disturbs the recursive algorithms and proofs.

## Definition of the red-black tree class

```cpp
--8<-- "docs/ds/code/rbtree/rbtree.hpp:class-node1"
  // ...
--8<-- "docs/ds/code/rbtree/rbtree.hpp:class-node2"
```

???+ note "Note"
    In the storage of a red-black tree node, using an array to store child node pointers can improve code reuse.

## Operations

???+ note "Note"
    The insertion/deletion of a red-black tree has multiple implementation methods; this article adopts the implementation method of *Introduction to Algorithms*, dividing the balance maintenance after insertion into 3 cases and the balance maintenance after deletion into 4 cases.

Operations such as traversal, finding the minimum/maximum, searching for an element, computing the rank of an element, looking up an element by rank, and finding the predecessor/successor of a red-black tree are consistent with the [binary search tree](./bst.md), and are not repeated here.

In addition, in the code comments for insertion/deletion balance maintenance below, we make the following conventions:

-   Use `p` to indicate that node `p` is black;
-   Use `[p]` to indicate that node `p` is red;
-   Use `{p}` to indicate that node `p` is red or black;
-   Use `|p|` to indicate that node `p` is a NIL node or its color is black.

### Rotation

The rotation operation is the key to how most balanced trees can maintain balance; it can change the depth of local nodes without changing the in-order traversal result of a valid BST.

![rbtree-rotations](images/rbtree-rotate.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:rotate"
    ```

### Insertion

The insertion operation of a red-black tree is similar to that of an ordinary BST; for a red-black tree, the newly inserted node is initially red, and after completing the insertion, correction needs to be made according to the state of the inserted node and related nodes to satisfy the four properties mentioned above.

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-leaf"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-fixup1"
        // ...
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-fixup2"
    ```

### Balance maintenance after insertion

???+ note "Note"
    To deepen understanding, please verify for yourself whether property 4 is satisfied after balance maintenance.

Since the inserted node, if not the root node, must be red, insertion may violate property 3, and the balance needs to be maintained.

Let the inserted node be $n$, its parent node be $p$, its grandparent node be $g$, and its uncle node be $u$. By property 3, $g$ must be black.

We recursively maintain upward from the insertion position; if $p$ is black we can terminate, otherwise it is divided into 3 cases.

```cpp
--8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-aux1"
      // ...
--8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-aux2"
```

#### Insert case 1

Both $p$ and $u$ are red. At this point we only need to recolor.

![](images/rbtree-insert-case1.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-case1"
    ```

#### Insert case 2

$p$ is red, $u$ is black, and $p$'s direction differs from $n$'s direction.

At this point we need to rotate node $p$ to turn it into the third case.

![](images/rbtree-insert-case2.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-case2"
    ```

#### Insert case 3

$p$ is red, $u$ is black, and $p$'s direction is the same as $n$'s direction.

At this point we need to rotate node $g$ to turn $p$ into the root of the subtree, then swap the colors of $p$ and $g$.

![](images/rbtree-insert-case3.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:insert-case3"
    ```

### Deletion

The deletion operation of a red-black tree has a few more steps compared with an ordinary BST. Specifically:

-   If the node $n$ to be deleted has two child nodes, swap the data of $n$ and the minimum node $s$ in the right subtree, and set $n$ to $s$. At this point $n$ cannot have two child nodes.
-   If the node $n$ to be deleted has one child node $s$. By property 4, $s$ must be red, and further by property 3, $n$ must be black. So we only need to replace the pointer to $n$ in the parent node $p$ with the address of $s$, and replace $s$'s parent pointer with the address of $p$, and then dye $s$ black.
-   If the node $n$ to be deleted has no child nodes. If $n$ is the root node or $n$ is a red node, then delete it directly; otherwise deleting it directly will violate property 4, and the balance needs to be maintained.

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-leaf"
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-fixup1"
        // ...
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-fixup2"
    ```

### Balance maintenance after deletion

???+ note "Note"
    To deepen understanding, please verify for yourself whether property 4 is satisfied after balance maintenance.

From the discussion above, $n$ is a black leaf node and not the root node. Let $n$'s parent node be $p$, its sibling node be $s$, and its nephew nodes be $c$ and $d$.

The maintenance of deletion also recursively maintains upward from $n$; if $n$ is the root or $n$ is red we can terminate, otherwise it is divided into 4 cases.

```cpp
--8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-aux1"
      // Delete case 1
      // ...
      // Other cases
--8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-aux2"
      // ...
--8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-aux3"
```

#### Delete case 1

$s$ is red.

At this point we rotate $p$, turn $s$ into the subtree root node, then swap the colors of $s$ and $p$ to turn it into one of the other three cases.

![](images/rbtree-remove-case1.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case1"
    ```

#### Delete case 2

The color of $p$ is indeterminate, and $s$, $c$, $d$ are all black.

At this point we only need to dye $s$ red.

![](images/rbtree-remove-case2.svg)

Note that if $p$ is red it will violate property 3, but if $p$ is red it will exit the loop directly, so we dye it black at the end.

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case2"
    ```

#### Delete case 3

The color of $p$ is indeterminate, $s$ and $d$ are both black, and $c$ is red.

At this point we need to rotate $s$ so that $c$ becomes the root node of the subtree originally corresponding to $s$, and swap the colors of $s$ and $c$ to turn it into the fourth case.

![](images/rbtree-remove-case3.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case3"
    ```

#### Delete case 4

The colors of $p$ and $c$ are indeterminate, $s$ is black, and $d$ is red.

At this point we need to rotate $p$ so that $s$ becomes the root node of the subtree, swap the colors of $s$ and $p$, and dye $d$ black to terminate balance maintenance.

![](images/rbtree-remove-case4.svg)

???+ note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:delete-case4"
    ```

## Reference code

The following code is a set implemented with a red-black tree:

??? note "Implementation"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:full"
    ```

??? note "Example problems: [Luogu P3369 【Template】Ordinary Balanced Tree](https://www.luogu.com.cn/problem/P3369) and [Luogu P6136 【Template】Ordinary Balanced Tree (Data-Strengthened Version)](https://www.luogu.com.cn/problem/P6136)"
    ```cpp
    --8<-- "docs/ds/code/rbtree/rbtree.hpp:class"
    --8<-- "docs/ds/code/rbtree/rbtree_1.cpp:main"
    ```

## Relationship with the 2-3-4 tree

The 2-3-4 tree is an order-4 B-tree; like a general B-tree, the 2-3-4 tree can perform search, insertion, and deletion operations in $O(\log n)$ time. The nodes of a 2-3-4 tree are of three kinds: 2-nodes, 3-nodes, and 4-nodes, containing one, two, or three data elements respectively. All leaf nodes are at the same depth (the bottom level), and all data are stored in order.

The 2-3-4 tree and the red-black tree are isomorphic; any red-black tree uniquely corresponds to a 2-3-4 tree. The insertion and deletion operations on a 2-3-4 tree cause node expansion, splitting, and merging, corresponding to recoloring and rotation in a red-black tree. The figure below shows the red-black tree nodes corresponding to the 2-node, 3-node, and 4-node of a 2-3-4 tree. Note that the 3-node of a 2-3-4 tree corresponds to two cases in a red-black tree, the red node leaning left and leaning right, so a red-black tree may correspond to multiple 2-3-4 trees.

![2-3-4-tree-rbt-1](images/2-3-4-tree-rbt-1.svg)

The figure below shows a red-black tree and its corresponding 2-3-4 tree. Moving the red nodes in the red-black tree up to the left and right sides of the parent node, forming a B-tree node, yields the corresponding 2-3-4 tree. It can be found that the number of nodes of the red-black tree equals the number of nodes of the 2-3-4 tree.

![2-3-4-tree-rbt](images/2-3-4-tree-rbt-2.svg)

One can understand the insertion and deletion operations of a red-black tree by comparing with the 2-3-4 tree. [^234-vs-rbt]

## Usage in real engineering projects

Since the red-black tree is currently the in-memory balanced tree with the highest overall efficiency in mainstream industry, it is widely used in real engineering projects; here we list several real usage cases and give the corresponding source code links, so that readers can compare and learn.

### Linux

Source code:

-   [`linux/lib/rbtree.c`](https://elixir.bootlin.com/linux/latest/source/lib/rbtree.c)

All operations of the red-black tree in Linux are implemented using loop iteration, guaranteeing efficiency while also adding a large number of comments to ensure code readability; it is highly recommended that readers read and learn from it. The red-black tree is very widely used in the Linux kernel; here we list only a few classic cases.

-   [CFS non-real-time task scheduling](https://www.kernel.org/doc/html/latest/scheduler/sched-design-CFS.html)

    Linux's stable kernel versions after 2.6.24 use the new scheduler CFS; all non-real-time runnable processes are maintained with a red-black tree keyed on virtual runtime, to schedule all tasks more fairly and efficiently. CFS abandons the active/expired arrays and dynamic priority computation, no longer tracks the sleep time of tasks or distinguishes whether a task is interactive, but instead uses a red-black tree with keys computed based on time in scheduling to pick the next task, and determines the scheduling task priority according to the state of all tasks' CPU-time occupancy.

-   [epoll](https://man7.org/linux/man-pages/man7/epoll.7.html)

    epoll, whose full name is event poll, is an implementation of IO multiplexing in the Linux kernel, and is an improved version of the original poll/select. The implementation of epoll in Linux chooses to use a red-black tree to store file descriptors.

### Nginx

Source code:

-   [`nginx/src/core/ngx_rbtree.h`](https://github.com/nginx/nginx/blob/master/src/core/ngx_rbtree.h)
-   [`nginx/src/core/ngx_rbtree.c`](https://github.com/nginx/nginx/blob/master/src/core/ngx_rbtree.c)

The user-space timers in nginx are implemented through a red-black tree. In nginx, all timer nodes are maintained by a red-black tree; in each loop of the worker process, the `ngx_process_events_and_timers` function is called, and in that function the timer-handling function `ngx_event_expire_timers` is called; each time, this function continuously takes out the node with the smallest time value from the red-black tree, checks whether they have already timed out, and then executes their functions, until the time of the taken-out node has not timed out.

There are many public resources analyzing the source code of the red-black tree in nginx; readers can search and learn on their own.

### C++

Source code:

-   GNU libstdc++

    -   [`libstdc++-v3/include/bits/stl_tree.h`](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/bits/stl_tree.h)
    -   [`libstdc++-v3/src/c++98/tree.cc`](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/src/c%2B%2B98/tree.cc)

    In addition, `libstdc++` provides [`__gnu_cxx::rb_tree`](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/include/ext/rb_tree) in `<ext/rb_tree>`, which inherits from `std::_Rb_tree` and can be regarded as a type alias for external use. Note that this header file is **not** part of the C++ standard, so it is not recommended to use it unless necessary.

    The [`pb_ds`](../lang/pb-ds/tree.md) of `libstdc++` also provides a red-black tree.

-   LLVM libcxx
    -   [`libcxx/include/__tree`](https://github.com/llvm/llvm-project/blob/main/libcxx/include/__tree)

-   Microsoft STL
    -   [`stl/inc/xtree`](https://github.com/microsoft/STL/blob/main/stl/inc/xtree)

The internal data structure of `std::set` and `std::map` in most STLs is a red-black tree (such as the ones mentioned above). However, it is worth noting that the C++ standard does not stipulate that `std::set` and `std::map` must be implemented with a red-black tree, so one should not directly use the internal data structure of `std::set` and `std::map` in engineering projects.

### OpenJDK

Source code:

-   [`java.util.TreeMap<K, V>`](https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/TreeMap.java)
-   [`java.util.TreeSet<K, V>`](https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/TreeSet.java)
-   [`java.util.HashMap<K, V>`](https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/util/HashMap.java)

Both `TreeMap` and `TreeSet` in the JDK use a red-black tree as the underlying data structure. At the same time, after JDK 1.8, when the length of the linked list of each table entry in the internal hash table of `HashMap` exceeds 8, it also automatically converts to a red-black tree to improve lookup efficiency.

## References

-   Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).*Introduction to algorithms*. MIT press.
-   [Red-Black Tree - Wikipedia](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
-   [Red-Black Tree Visualization](https://www.cs.usfca.edu/~galles/visualization/RedBlack.html)

[^gilbas1978]: L. J. Guibas and R. Sedgewick, "A dichromatic framework for balanced trees,"*19th Annual Symposium on Foundations of Computer Science (sfcs 1978)*, Ann Arbor, MI, USA, 1978, pp. 8-21, doi:[10.1109/SFCS.1978.3](https://doi.org/10.1109%2FSFCS.1978.3).

[^cite_note-cormen2009-18]: <https://en.wikipedia.org/wiki/Red–black_tree#cite_note-Cormen2009-18>

[^cite_note-mehlhorn2008-17]: <https://en.wikipedia.org/wiki/Red–black_tree#cite_note-Mehlhorn2008-17>

[^cite_note-algs4-16]: <https://en.wikipedia.org/wiki/Red–black_tree#cite_note-Algs4-16>: 432–447

[^234-vs-rbt]: [This blog post](https://www.cnblogs.com/zhenbianshu/p/8185345.html) provides a detailed description.
