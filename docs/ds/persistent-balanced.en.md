## Persistent rotation-free Treap

### Prerequisites

The **persistent balanced tree commonly used in OI** is generally the **persistent rotation-free Treap**, so it is recommended to first learn the [**rotation-free Treap**](./treap.md).

### Idea / Approach

For the rotation-free Treap, persistence can be achieved by copying the nodes passed on the path during the **Merge** and **Split** operations (generally copying in the **Split** operation, ensuring previous versions are not affected).

For the rotating Treap, while copying the nodes passed on the path, one also needs to copy the nodes affected by rotation (if such a node has already been copied in this operation, no further copy is needed); since a single rotation generally affects only two nodes, this does not increase its time complexity.

The above method is generally called path copying.

"All supportable operations can be completed through **Merge, Split, Newnode, Build**", and the **Build** operation is only used for construction and can be ignored, while **Newnode** (creating a new node) is the tool used for persistence.

Let's observe **Merge** and **Split**; we find that they are both top-down operations!

Therefore we can completely **refer to the persistent operations of a segment tree** to make it persistent.

### Persistence operations

**Persistence** is an operation on a **data structure**, i.e. retaining historical information so that previous historical versions can be invoked later.

For a **persistent segment tree**, each time a historical version is newly created, the **modification path along the way** is copied out.

Then for a persistent Treap (the version currently commonly used in domestic OI):

After copying a new version $X_{a+1}$ (the $(a+1)$-th version of node $X$) of a node $X_{a}$ (the $a$-th version of node $X$):

-   If some child node $Y$ does not need its information modified, then simply point $X_{a+1}$'s pointer directly at $Y_{a}$ (the $a$-th version of node $Y$).
-   Conversely, if $Y$ is to be modified, then when **recursing to the lower level**, **create** the new node $Y_{a+1}$ (the $(a+1)$-th version of node $Y$) to **store the new information**, and at the same time point $X_{a+1}$'s pointer at $Y_{a+1}$ (the $(a+1)$-th version of node $Y$).

### Persistence

Things needed:

-   A `struct` array storing the information of **each node** (generally called the `tree` array); (of course, masters who write the **pointer version** of a balanced tree can consider not using this array)

-   A **root-node array**, storing the *tree root* of each version; each time version information is queried, start from the **node stored in the root array**;

-   `split()` splitting **splits two trees out of the tree**

-   `merge()` merging **merges two trees according to random priorities**

-   `newNode()` creates a new node

-   `build()` builds the tree

#### Split

For the **split operation**, each time a path is split, **create a new node** pointing to the split path, and use `std::pair` to store the roots of the two newly split trees.

`split(x,k)` returns a `std::pair`;

meaning to put the first $k$ elements of the tree rooted at $x$ into **one tree**, and the remaining nodes form another tree, and return the roots of these two trees (first is the root of the first tree, second is that of the second tree).

-   If the $key$ of $x$'s **left subtree** $\geq k$, then **directly recurse into the left subtree**, and merge the second tree split from the left subtree with the current $x$'s **right subtree**.
-   Otherwise recurse into the **right subtree**.

```cpp
static std::pair<int, int> _split(int _x, int k) {
  if (_x == 0)
    return std::make_pair(0, 0);
  else {
    int _vs = ++_cnt;  // create a new node (the essence of persistence)
    _trp[_vs] = _trp[_x];
    std::pair<int, int> _y;
    if (_trp[_vs].key <= k) {
      _y = _split(_trp[_vs].leaf[1], k);
      _trp[_vs].leaf[1] = _y.first;
      _y.first = _vs;
    } else {
      _y = _split(_trp[_vs].leaf[0], k);
      _trp[_vs].leaf[0] = _y.second;
      _y.second = _vs;
    }
    _trp[_vs]._update();
    return _y;
  }
}
```

#### Merge

`merge(x,y)` returns the root of the merged tree.

Likewise implemented recursively. If **x's random priority** > **y's random priority**, then `merge(x_{rc},y)`, otherwise `merge(x,y_{lc})`.

```cpp
static int _merge(int _x, int _y) {
  if (_x == 0 || _y == 0)
    return _x ^ _y;
  else {
    if (_trp[_x].fix < _trp[_y].fix) {
      _trp[_x].leaf[1] = _merge(_trp[_x].leaf[1], _y);
      _trp[_x]._update();
      return _x;
    } else {
      _trp[_y].leaf[0] = _merge(_x, _trp[_y].leaf[0]);
      _trp[_y]._update();
      return _y;
    }
  }
}
```

## Persistent WBLT

### Prerequisites

The persistent WBLT is modified from the WBLT, so first learn the [WBLT](./wblt.md).

### Idea / Approach

Using the method of **path copying**, copy down the nodes **modified** in one operation, without affecting the previous nodes.

### Handling lazy tags

To handle lazy tags, we consider it this way: on a persistent WBLT, a point may have multiple parents, but the number of children can only be $0$ or $2$. The pushdown operation of pushing down lazy tags only affects its children; performing pushdown on a point has no effect on it; rather it is its children—its children may have more than one parent, and pushing its tag down to a child may cause, in another parent's version, an extra lazy tag that does not belong to that version, which is wrong; unless its child has only it as its single parent. So we should, when pushing down, copy the children once and apply the lazy tag to the new children.

### Implementing path copying

When performing path copying, we can define a refresh function that takes a reference to a node $p$, meaning to copy node $p$, producing a new node, and reassign it to $p$. The principle of using the refresh function is: if it is about to be modified, or the children it holds are about to change (rather than the information of its children being about to be modified), then refresh it, otherwise no need.

For static queries, no refresh is needed except for pushdown. If it is guaranteed that path copying is done for whatever operation, then the order of pushdown and refresh does not matter.

### A small optimization for the persistent WBLT

Here is an optimization. Observe that during pushdown two nodes need to be copied; one can write tag permanence, but as just said, if a child has only it as its single parent, no copy is needed. Targeting this property, an optimization can be made to reduce copying redundant nodes.

Consider recording how many parents each node has (considering that the root of each version has one parent), denoted $use$. Each time refresh is called, if $use\leq 1$ then no re-copy of the node is needed, otherwise create a new node and decrement $use$ by $1$, meaning the parent ran off with this child, so that the parent can freely modify the new node without affecting other versions. In addition, each time a node is copied, if the node has children, then the $use$ of the two children is incremented by $1$; when merging two subtrees, the returned node also has one parent's $use$ for the two children; when a node is deleted, both child nodes lose one parent: this can optimize some time and space.

### Code implementation

??? note "Full code (persistent literary balanced tree)"
    ```cpp
    --8<-- "docs/ds/code/persistent-balanced/persistent-wblt.cpp"
    ```

## Example problems

???+ note "[Luogu P3835 【Template】Persistent Balanced Tree](https://www.luogu.com.cn/problem/P3835)"
    You need to implement a data structure providing the following operations (initially the data structure has no data):
    
    1.  Insert the number $x$;
    2.  Delete the number $x$ (if there are multiple identical numbers, delete only one; if there is none, please ignore this operation);
    3.  Query the rank of the number $x$ (rank is defined as the number of numbers smaller than the current number + 1);
    4.  Query the number whose rank is $x$;
    5.  Find the predecessor of $x$ (the predecessor is defined as the largest number smaller than $x$; if it does not exist, output $-2\,147\,483\,647$);
    6.  Find the successor of $x$ (the successor is defined as the smallest number larger than $x$; if it does not exist, output $2\,147\,483\,647$).
    
    All the above operations are based on some historical version, and at the same time generate a new version (operations 3, 4, 5, 6 keep the original version unchanged). And the number of each version is the sequence number of the operation. In particular, the initial version number is 0.

This is the persistent version of the **Ordinary Balanced Tree** problem, with operations similar to that problem.

It just uses the persistent merge and split operations.

## Recommended practice problems

1.  [「Luogu P3919」Persistent Array (template problem)](https://www.luogu.com.cn/problem/P3919)

2.  [「Codeforces 702F」T-shirt](http://codeforces.com/problemset/problem/702/F)

3.  [「Luogu P5055」Persistent Literary Balanced Tree](https://www.luogu.com.cn/problem/P5055)

4.  [「Luogu P5350」Sequence](https://www.luogu.com.cn/problem/P5350)
