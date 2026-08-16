## Introduction

The pairing heap is a data structure supporting operations such as insertion, querying/deleting the minimum, merging, and modifying elements; it is a kind of mergeable heap. It has the advantages of high speed and simple structure, but because it is amortized complexity based on potential analysis, it cannot be made persistent.

## Definition

The pairing heap is a weighted multi-way tree satisfying the heap property (as shown below), i.e. the weight of each node is less than or equal to that of all its children (taking the min-heap as an example, likewise below).  
![](./images/pairingheap1.jpg)

We usually use the child-sibling representation to store a pairing heap (as shown below); all child nodes of a node form a singly linked list. Each node stores a pointer to its first child, i.e. the head node of the list, and a pointer to its right sibling.

This way is convenient for implementing the pairing heap and will also facilitate complexity analysis.

![](./images/pairingheap2.jpg)

```cpp
struct Node {
  T v;  // T is the weight type
  Node *child, *sibling;
  // child points to the node's first child, sibling points to the node's next sibling.
  // if the node has no child/next sibling, the pointer points to nullptr.
};
```

From the definition we can find that, compared with other common heap structures, the pairing heap maintains no extra tree-size, depth, rank, or similar information (a binary heap also maintains no extra information, but it guarantees the operation complexity by maintaining a strict complete binary tree structure), and any tree satisfying the heap property is a valid pairing heap; such a simple and highly flexible data structure lays the foundation for the pairing heap's excellent efficiency in practice; in contrast, the Fibonacci heap's terrible constant factor is precisely because it needs to maintain a lot of extra information.

The pairing heap guarantees its total complexity through a carefully designed sequence of operations; the original paper[^ref1] calls it "a Self Adjusting Heap". In this respect it is quite similar to the Splay tree (called "Self Adjusting Binary Tree" in the original paper).

## Process

### Querying the minimum

From the definition of the pairing heap, we can see that the weight of the pairing heap's root node must be the smallest, so just return the root node directly.

### Merging

The operation of merging two pairing heaps is very simple: first make the smaller of the two root nodes the new root node, then insert the larger root node as its child. (See the figure below)

![](./images/pairingheap3.jpg)

Note that a node's child list is sorted by insertion time, i.e. the rightmost node became the parent's child earliest, and the leftmost node became the parent's child most recently.

???+ note "Implementation"
    ```cpp
    Node* meld(Node* x, Node* y) {
      // if one is empty, directly return the other
      if (x == nullptr) return y;
      if (y == nullptr) return x;
      if (x->v > y->v) std::swap(x, y);  // after swap, x is the heap with the smaller weight, y the larger
      // set y as x's child
      y->sibling = x->child;
      x->child = y;
      return x;  // the new root node is x
    }
    ```

### Insertion

With merging in place, for insertion just regard the new element as a new pairing heap and merge it with the original heap.

### Deleting the minimum

The first point to mention is that the several operations above are all very lazy, doing no maintenance of the data structure at all, so we need to carefully design the delete-min operation to ensure the total complexity does not go wrong.

The root node is the minimum, so what we want to delete is the root node. Consider what happens after removing the root node: the root node's original children form a forest; but a pairing heap should be one tree, so we need to merge all these children together in some order.

A very natural idea is to use the `meld` function to merge the children one by one from left to right; the correctness of doing so is obvious, but it will cause the single-operation complexity to degrade to $O(n)$.

To guarantee the total amortized complexity, we need to use a "two-step" merging method:

1.  Pair up the children two by two, and use the `meld` operation to merge the two children paired together (see figure 1 below),
2.  Merge the newly produced heaps one by one **from right to left** (i.e. in the direction from old children to new children) (see figure 2 below).

![](./images/pairingheap4.jpg)

![](./images/pairingheap5.jpg)

First implement an auxiliary function `merges`, whose purpose is to merge all siblings of a node.

???+ note "Implementation"
    ```cpp
    Node* merges(Node* x) {
      if (x == nullptr || x->sibling == nullptr)
        return x;  // if the tree is empty or it has no next sibling, no merging is needed, return.
      Node* y = x->sibling;                // y is x's next sibling
      Node* c = y->sibling;                // c is the sibling after that
      x->sibling = y->sibling = nullptr;   // break them apart
      return meld(merges(c), meld(x, y));  // the core part
    }
    ```

The last statement is the core of this function; it is divided into three parts:

1.  `meld(x,y)` "pairs" x and y.
2.  `merges(c)` recursively merges c and its siblings.
3.  Merge the 2 new trees produced by the above 2 operations.

Note that, as mentioned above, the merging direction in the second step has a requirement (merge from right to left); the implementation of this recursive function already guarantees this order. If the reader needs to implement an iterative version themselves, please be sure to guarantee this order, otherwise the complexity will lose its guarantee.

With the `merges` function, the `delete-min` operation is obvious.

???+ note "Implementation"
    ```cpp
    Node* delete_min(Node* x) {
      Node* t = merges(x->child);
      delete x;  // if memory reclamation is needed
      return t;
    }
    ```

### Decreasing the value of an element

To implement this operation, we need to add a "parent" pointer to the node; when a node has a left sibling, it points to the left sibling rather than the actual parent node; otherwise, it points to its parent node.

First the node definition is modified to:

???+ note "Implementation"
    ```cpp
    struct Node {
      LL v;
      int id;
      Node *child, *sibling;
      Node *father;  // new: parent pointer; if the node is the root, it points to the empty node nullptr
    };
    ```

The `meld` operation is modified to:

???+ note "Implementation"
    ```cpp
    Node* meld(Node* x, Node* y) {
      if (x == nullptr) return y;
      if (y == nullptr) return x;
      if (x->v > y->v) std::swap(x, y);
      if (x->child != nullptr) {  // new: maintain the parent pointer
        x->child->father = y;
      }
      y->sibling = x->child;
      y->father = x;  // new: maintain the parent pointer
      x->child = y;
      return x;
    }
    ```

The `merges` operation is modified to:

???+ note "Implementation"
    ```cpp
    Node *merges(Node *x) {
      if (x == nullptr) return nullptr;
      x->father = nullptr;  // new: maintain the parent pointer
      if (x->sibling == nullptr) return x;
      Node *y = x->sibling, *c = y->sibling;
      y->father = nullptr;  // new: maintain the parent pointer
      x->sibling = y->sibling = nullptr;
      return meld(merges(c), meld(x, y));
    }
    ```

Now let's consider how to implement the `decrease-key` operation.  
First we find that, after we decrease the weight of node `x`, the subtree rooted at `x` still satisfies the pairing-heap property, but the heap property may no longer hold between `x`'s parent and `x`.  
Therefore we cut out the whole subtree rooted at `x`; now both trees conform to the pairing-heap property, and then we merge them, completing the whole operation.

???+ note "Implementation"
    ```cpp
    // root is the heap's root, x is the node to operate on, v is the new weight; when calling, v <= x->v must be guaranteed
    // the return value is the new root node
    Node *decrease_key(Node *root, Node *x, LL v) {
      x->v = v;                 // update the weight
      if (x == root) return x;  // if x is the root, return directly
      // cut x out of fa's child nodes; here we need to discuss x's position.
      if (x->father->child == x) {
        x->father->child = x->sibling;
      } else {
        x->father->sibling = x->sibling;
      }
      if (x->sibling != nullptr) {
        x->sibling->father = x->father;
      }
      x->sibling = nullptr;
      x->father = nullptr;
      return meld(root, x);  // re-merge x and the root node
    }
    ```

## Complexity analysis

The pairing heap is simple in structure and implementation, but its time complexity analysis is not easy.

The original paper[^ref1] only analyzed the complexity to the extent that the `meld` and `delete-min` operations are both amortized $O(\log n)$, but proposed a conjecture that its operations all have the same complexity as the Fibonacci heap.

Unfortunately, it was later found that for a pairing heap that maintains no extra information, under a specific operation sequence, the amortized complexity lower bound of the `decrease-key` operation is at least $\Omega (\log \log n)$[^ref2].

Currently the better estimates of the complexity upper bound include: Iacono's $O(1)$ `meld` and $O(\log n)$ `decrease-key`[^ref3]; Pettie's $O(2^{2 \sqrt{\log \log n}})$ `meld` and `decrease-key`[^ref4]. Note that the aforementioned complexities are all amortized, so one cannot take the minimum of each result separately.

## References

[^ref1]: [The pairing heap: a new form of self-adjusting heap](http://www.cs.cmu.edu/~sleator/papers/pairing-heaps.pdf)

[^ref2]: [On the efficiency of pairing heaps and related data structures](https://dl.acm.org/doi/10.1145/320211.320214)

[^ref3]: [Improved upper bounds for pairing heaps](https://arxiv.org/abs/1110.4428)

[^ref4]: [Towards a Final Analysis of Pairing Heaps](http://web.eecs.umich.edu/~pettie/papers/focs05.pdf)

-   <https://en.wikipedia.org/wiki/Pairing_heap>
-   <https://brilliant.org/wiki/pairing-heap/>
