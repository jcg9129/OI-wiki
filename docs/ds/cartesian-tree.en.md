author: sshwy, zhouyuyang2002, StudyingFather, Ir1d, ouuan, Enter-tainer

## Introduction

A Cartesian tree is a binary tree in which each node consists of a key-value pair $(k,w)$. It is required that $k$ satisfies the property of a binary search tree (BST), and $w$ satisfies the heap property. If the $k,w$ key values of the Cartesian tree are fixed, and the $k$ are pairwise distinct and the $w$ are also pairwise distinct, then the structure of this Cartesian tree is unique. As in the figure below:

![eg](./images/cartesian-tree1.png)

(Figure from Wikipedia.)

The Cartesian tree above is equivalent to taking the array element values as the key $w$ and the array indices as the key $k$. We can see that this tree's key $k$ satisfies the BST property, and its key $w$ satisfies the min-heap property. At the same time, by the property of a binary search tree, we find that this special Cartesian tree has the property that the indices within a subtree form a contiguous interval.

When using a Cartesian tree in contests, the array index is commonly used as the key $k$ of the pair, with the array index $k$ satisfying the BST property.

When using $k,w$ below, by default $k$ satisfies the BST property and $w$ satisfies the heap property.

## Building a Cartesian tree with a monotonic stack

### Process

We consider inserting the elements into the current Cartesian tree in ascending order of $k$.

For a Cartesian tree, define the "right chain" as the chain formed by starting from the root and always going to the right child until reaching a leaf. Then after inserting a node, this node must be on the right chain. Because we insert in ascending order of $k$ (which satisfies the BST property), this newly inserted node must be at the **rightmost** end of the tree. This node cannot be a left child, nor does it have a right child.

So we perform the following process: compare the $w$ of the right-chain nodes with the current node $u$ from bottom to top; if we find a node $x$ on the right chain satisfying $w_x<w_u$, then attach $u$ to $x$'s right child, and $x$'s original right subtree becomes $u$'s left subtree.

The red-boxed part in the figure is the right chain we always maintain:

![build](./images/cartesian-tree2.png)

Clearly each number enters and leaves the right chain at most once (or, each point exists in the right chain for a contiguous period of time). This process can be maintained with a monotonic stack, where the stack maintains the nodes on the right chain of the current Cartesian tree. Once a point is no longer on the right chain, pop it. This way each point enters and leaves at most once, giving complexity $O(n)$.

???+ note "Cartesian trees and Treaps"
    In fact, a Treap is a kind of Cartesian tree, only that the $w$ values in a Treap are completely random. A Treap has a linear construction algorithm; if the keys $k$ are sorted beforehand, the above monotonic-stack algorithm can be used to complete the construction, though this is rarely done.

### C++ implementation

```cpp
// stk maintains the indices in the sequence corresponding to the nodes in the Cartesian tree
for (int i = 1; i <= n; i++) {
  int k = top;  // top is the stack top before the operation, k is the current stack top
  while (k > 0 && w[stk[k]] > w[i]) k--;  // maintain the nodes on the right chain
  if (k) rs[stk[k]] = i;  // stack-top element.right child := current element
  if (k < top) ls[i] = stk[k + 1];  // current element.left child := the previously popped element
  stk[++k] = i;                     // push the current element onto the stack
  top = k;
}
```

## Example

???+ note "[HDU 1506. Largest Rectangle in a Histogram](https://acm.hdu.edu.cn/showproblem.php?pid=1506)"
    There are $n$ positions, and the height at each position is $h_i$; find the largest sub-rectangle. As in the figure below:
    
    ![eg](./images/cartesian-tree3.png)
    
    The shaded part is the largest sub-rectangle in the figure.

??? note "Solution idea"
    Specifically, we take the index as the key $k$ and $h_i$ as the key $w$ satisfying the min-heap property, and build a Cartesian tree of $(i,h_i)$.
    
    This way we enumerate each node $u$ and take $w_u$ (i.e. node $u$'s height $h$) as the height of the largest sub-rectangle. Since the Cartesian tree we built satisfies the min-heap property, the heights of the nodes within $u$'s subtree are all greater than or equal to $u$. And we also know that the indices within $u$'s subtree form a contiguous interval. So we only need to know the size of the subtree, and then we can compute the area of the largest sub-rectangle of this interval. Just update the answer with the value computed at each point. Clearly this can be done in one DFS, so the complexity is $O(n)$.

??? note "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/cartesian-tree/cartesian-tree_1.cpp"
    ```

## References

[Cartesian tree - Wikipedia](https://zh.wikipedia.org/wiki/%E7%AC%9B%E5%8D%A1%E5%B0%94%E6%A0%91)
