An AA tree is a balanced tree structure used for efficiently storing and retrieving ordered data, introduced by Professor Arne Andersson in his 1993 paper "Balanced search trees made simple"; it is designed to reduce the number of different cases a red-black tree must consider. An AA tree can perform search, insertion, and deletion in $O(\log N)$ time. Below is an example of an AA tree.

![aa-tree-1](images/aa-tree-1.jpg)

An AA tree is a variant of the red-black tree; unlike a red-black tree, a red node in an AA tree can only be a right child. This causes an AA tree to simulate a 2-3 tree rather than a 2-3-4 tree, thereby greatly simplifying maintenance operations. The maintenance algorithm of a red-black tree needs to consider seven different cases to balance the tree correctly.

![red-black tree](images/aa-tree-2.svg)

Because a red node can only be a right child, an AA tree only needs to consider two cases.

![aa-tree](images/aa-tree-3.svg)

## Definition

An AA tree follows the same rules as a red-black tree, but adds a new rule, **namely that a red node cannot appear as a left child**.

1.  Each node can be red or black.
2.  The root node is always black.
3.  Leaf nodes (NULL) are always black.
4.  Both children of a red node must be black, i.e. there are no two adjacent red nodes.
5.  Every path from the root to a NULL node has the same number of black nodes.
6.  A red node can only be a right child.

## Balance maintenance

Each node of an AA tree maintains a **level** field, similar to how each node of a red-black tree maintains a color field ("RED" or "BLACK"). The level satisfies the following 5 conditions:

1. Every leaf node has level 1.

2. Every left child's level is its parent's level minus 1.

3. Every right child's level equals its parent's level or its parent's level minus 1.

4. Every right grandchild's level is strictly less than its grandparent's level.

5. Every node with level greater than 1 has two children.

![aa-tree-4](images/aa-tree-4.jpg)

### Horizontal link

A link where a child's level equals the parent's level is called a **horizontal link**, similar to a red link in a red-black tree. A single right horizontal link is allowed, but consecutive right horizontal links are not; left horizontal links are not allowed. These restrictions are stricter than those of a red-black tree, so the balancing process of an AA tree is programmatically much simpler than that of a red-black tree.

![aa-tree-5](images/aa-tree-5.jpg)

Insertion and deletion operations may temporarily cause the AA tree to lose balance (i.e. violate the AA-tree invariants). Restoring balance requires only two different operations: "**skew**" and "**split**". "Skew" is a right rotation of a subtree containing a left horizontal link to replace it with a subtree containing a right horizontal link. "Split" is a left rotation with a level increase to replace a subtree containing two or more consecutive right horizontal links with one containing two fewer consecutive right horizontal links. The implementations of balance-preserving insertion and deletion become more simplified by relying on the "skew" and "split" operations to modify the tree only when needed, rather than having the caller decide whether to "skew" or "split".

### split (left rotation)

Consecutive rightward horizontal links appear (three consecutive rightward children belong to the same level; node R and node X are both red nodes).

At this point, rotate node *T* left, treating the nodes with level less than or equal to this level as one subtree.

1.  The right child of the subtree root becomes the new subtree root;
2.  The original subtree root becomes the left child of the new subtree root;
3.  The new subtree root's level +1.

![aa-tree-split](images/aa-tree-split.svg)

???+ note "Pseudocode implementation"
    $$
    \begin{array}{ll}
    1 & \textbf{function } \text{split}(\text{root}) \\
    2 & \qquad \textbf{if } \text{root}\rightarrow\text{right}\rightarrow\text{right}\rightarrow\text{level} == \text{root}\rightarrow\text{level} \\
    3 & \qquad\qquad \text{rotate\_left}(\text{root}) \\
    4 & \textbf{end function}
    \end{array}
    $$

### skew (right rotation)

A leftward horizontal link appears (two consecutive leftward children belong to the same level).

Rotate node *T* right, treating the nodes with level less than or equal to this level as one subtree.

1.  The left child of the subtree root becomes the new subtree root;
2.  The original subtree root becomes the right child of the new subtree root.

![aa-tree-skew](images/aa-tree-skew.svg)

???+ note "Pseudocode implementation"
    $$
    \begin{array}{ll}
    1 & \textbf{function } \text{skew}(\text{root}) \\
    2 & \qquad \textbf{if } \text{root}\rightarrow\text{left}\rightarrow\text{level} == \text{root}\rightarrow\text{level} \\
    3 & \qquad\qquad \text{rotate\_right}(\text{root}) \\
    4 & \textbf{end function}
    \end{array}
    $$

## Operations on an AA tree

An AA tree is itself a binary search tree, so the search operation is the same as for other binary search trees. The insertion and deletion operations are the same as for an *AVL* tree: first insert or delete the key in the tree, then retreat back to the root along the search path and restructure the tree along the way.

### Insertion

???+ note "Pseudocode implementation"
    $$
    \begin{array}{ll}
    1 & \textbf{function } \text{insert}(\text{root}, \text{add}) \\
    2 & \qquad \textbf{if } \text{root} == \text{NULL} \\
    3 & \qquad\qquad \text{root} \gets \text{add} \\
    4 & \qquad \textbf{else if } \text{add}\rightarrow\text{key} < \text{root}\rightarrow\text{key} \qquad //\text{use} <= \text{if duplicates are allowed} \\ 
    5 & \qquad\qquad \text{insert}(\text{root}\rightarrow\text{left}, \text{add}) \\
    6 & \qquad \textbf{else if } \text{add}\rightarrow\text{key} > \text{root}\rightarrow\text{key} \\
    7 & \qquad\qquad \text{insert}(\text{root}\rightarrow\text{right}, \text{add}) \\
    8 & \qquad \textbf{end if} \\
    9 & \qquad \text{//if duplicates are not allowed, skew and split at each level} \\
    10 & \qquad \text{skew}(\text{root}); \\
    11 & \qquad \text{split}(\text{root}); \\
    12 & \textbf{end function}
    \end{array}
    $$

### Deletion

The deletion process is similar to that of other balanced binary trees: first convert the deletion of an internal node into the deletion of a leaf node. The specific method is to replace the internal node with its closest predecessor or successor node. Since all nodes with level greater than 1 in an AA tree have two children, the predecessor or successor node will be at level 1, and deleting a level-1 node is relatively simple.

???+ note "Pseudocode implementation"
    $$
    \begin{array}{ll}
    1 &  \text{//To rebalance the tree} \\
    2 &  \textbf{if} \ \text{root->left->level} < \text{root->level} -1 \ \textbf{or} \ \text{root->right->level} < \text{root->level} -1 \\
    3 &  \{ \\
    4 & \qquad \textbf{if} \ \text{root->right->level} > \text{--root->level} \\
    5 & \qquad \{ \\
    6 & \qquad\qquad \text{root->right->level} \gets \text{root->level} \\
    7 & \qquad \} \\
    8 & \qquad \text{skew}(\text{root}) \\
    9 & \qquad \text{skew}(\text{root->right}) \\
    10 & \qquad \text{skew}(\text{root->right->right}) \\
    11 & \qquad \text{split}(\text{root}) \\
    12 & \qquad \text{split}(\text{root->right}) \\
    13 &  \} \\
    \end{array}
    $$

## Performance

The performance of an AA tree is comparable to that of a red-black tree. Although an AA tree performs more rotation operations than a red-black tree, the AA tree's algorithm is simpler, ultimately resulting in similar performance. A red-black tree's performance is more consistent across various situations, while an AA tree tends to be flatter, giving it a slightly faster search speed.

## References

1.  [AA tree - Wikipedia](https://en.wikipedia.org/wiki/AA_tree)
2.  [Introduction to AA trees](https://iq.opengenus.org/aa-trees/)
3.  [AA tree - Visualization](https://kubokovac.eu/gnarley-trees/AAtree.html)
4.  [CMSC 420 Lecture 6: 2-3, Red-black, and AA trees](https://www.cs.umd.edu/class/fall2019/cmsc420-0201/Lects/lect06-aa.pdf)
