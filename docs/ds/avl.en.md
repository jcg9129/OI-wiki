An AVL tree is a balanced binary search tree. Because the introductions of AVL in various algorithm textbooks are very lengthy, many people have the impression that AVL trees are complex and impractical. But in fact, the principle of an AVL tree is simple, and its implementation is not complicated either.

## Properties

1.  An empty binary tree is an AVL tree.
2.  If T is an AVL tree, then its left and right subtrees are also AVL trees, and $|h(ls) - h(rs)| \leq 1$, where h is the height of its left and right subtrees.
3.  The tree height is $O(\log n)$.

Balance factor: right subtree height − left subtree height.

???+ note "Proof of the tree height"
    Let $f_n$ be the minimum number of nodes contained in an AVL tree of height $n$; then
    
    $$
    f_n=
    \begin{cases}
    1&(n=1)\\
    2&(n=2)\\
    f_{n-1}+f_{n-2}+1& (n>2)
    \end{cases}
    $$
    
    By the solution method for constant-coefficient non-homogeneous linear difference equations, $\{f_n+1\}$ is a Fibonacci sequence. Here the general term of $f_n$ is:
    
    $$
    f_n=\frac{5+2\sqrt{5}}{5}\left(\frac{1+\sqrt{5}}{2}\right)^n+\frac{5-2\sqrt{5}}{5}\left(\frac{1-\sqrt{5}}{2}\right)^n-1
    $$
    
    The Fibonacci sequence grows exponentially; for tree height $n$,
    
    $$
    n<\log_{\frac{1+\sqrt{5}}{2}} (f_n+1)<\frac{3}{2}\log_2 (f_n+1)
    $$
    
    Therefore the height of an AVL tree is $O(\log f_n)$, where $f_n$ is the number of nodes.

## Process

### Inserting a node

Similar to a BST (binary search tree), first perform a failed search to determine the insertion position, and after inserting the node, decide whether adjustment is needed based on the balance factor.

### Deleting a node

Deletion is similar to a BST: swap the node with its successor and then delete.

Deletion causes changes in the tree height and balance factors, and at this point one needs to adjust these changes along the path from the deleted node to the root.

### Balance maintenance

After inserting or deleting a node, property 2 of the AVL tree may be broken. Therefore, one needs to maintain the tree along the path from the inserted/deleted node to the root. If for some node property 2 is no longer satisfied, since we only inserted/deleted one node, the impact on the tree height does not exceed 1, so the absolute value of that node's balance factor is at most 2. By symmetry, here we only discuss the case where the left subtree's height is 2 greater than the right subtree's, i.e. $h(B)-h(E)=2$ in the figure below. At this point, we further discuss two cases based on the magnitude relationship between $h(A)$ and $h(C)$. Note that since we maintain balance bottom-up, property 2 is still satisfied for all descendants of node D.

![](./images/avl1.svg)

#### Case one: the height of A is not less than the height of C

Let $h(E)=x$; then

$$
\begin{cases}
    h(B)=x+2\\
    h(A)=x+1\\
    x\leq h(C)\leq x+1
\end{cases}
$$

where $h(C)\geq x$ is because node B satisfies property 2, so the difference between $h(C)$ and $h(A)$ does not exceed 1. At this point we perform a right rotation on node D (the rotation operation is the same as for other kinds of balanced binary search trees), as shown in the figure below.

![](./images/avl2.svg)

Clearly the heights of nodes A, C, E do not change, and

$$
\begin{cases}
    0\leq h(C)-h(E)\leq 1\\
    x+1\leq h'(D)=\max(h(C),h(E))+1=h(C)+1\leq x+2\\
    0\leq h'(D)-h(A)\leq 1
\end{cases}
$$

Therefore, after the rotation, nodes B and D also satisfy property 2.

#### Case two: the height of A is less than the height of C

Let $h(E)=x$; then, by the same reasoning as before,

$$
\begin{cases}
    h(B)=x+2\\
    h(C)=x+1\\
    h(A)=x
\end{cases}
$$

At this point we first perform a left rotation on node B, then a right rotation on node D, as shown in the figure below.

![](./images/avl3.svg)

Clearly the heights of nodes A, E do not change, and B's new right child and D's new left child are respectively C's original left and right children; then

$$
\begin{cases}
    x-1\leq h'(rs_B),h'(ls_D)\leq x\\
    0\leq h(A)-h'(rs_B)\leq 1\\
    0\leq h(E)-h'(ls_D)\leq 1\\
    h'(B)=\max(h(A),h'(rs_B))+1=x+1\\
    h'(D)=\max(h(E),h'(ls_D))+1=x+1\\
    h'(B)-h'(D)=0
\end{cases}
$$

Therefore, after the rotation, nodes B, C, D also satisfy property 2.

???+ note "Balance-maintenance operation: pseudocode"
    $$
    \begin{array}{ll}
    1 &  \textbf{function } \mathrm{MaintainBalance}(p) \\
    2 &  \qquad l \gets ls_p, r \gets rs_p \\
    3 &  \qquad \textbf{if } h(l)-h(r)=2 \\
    4 &  \qquad\qquad \textbf{if } h(ls_l) \ge h(rs_l) \\
    5 &  \qquad\qquad\qquad \mathrm{RightRotate}(p) \\
    6 &  \qquad\qquad \textbf{else} \\
    7 &  \qquad\qquad\qquad \mathrm{LeftRotate}(l) \\
    8 &  \qquad\qquad\qquad \mathrm{RightRotate}(p) \\
    9 &  \qquad \textbf{else if } h(l)-h(r)=-2 \\
    10 &  \qquad\qquad \textbf{if } h(ls_r) \le h(rs_r) \\
    11 &  \qquad\qquad\qquad \mathrm{LeftRotate}(p) \\
    12 &  \qquad\qquad \textbf{else} \\
    13 &  \qquad\qquad\qquad \mathrm{RightRotate}(r) \\
    14 &  \qquad\qquad\qquad \mathrm{LeftRotate}(p) \\
    \end{array}
    $$

As with other balanced binary search trees, information such as node height and subtree size in an AVL tree needs to be maintained during rotation.

## Other operations

The other operations of an AVL tree (Predecessor, Successor, Select, Rank, etc.) are the same as for an ordinary binary search tree.

## Reference code

The following code is a `Map` implemented with an AVL tree, i.e. an ordered, non-duplicate mapping:

??? note "Reference code"
    ```cpp
    --8<-- "docs/ds/code/avl-tree/AvlTreeMap.hpp"
    ```

## Other materials

At [AVL Tree Visualization](https://www.cs.usfca.edu/~galles/visualization/AVLtree.html), you can observe the process of an AVL tree maintaining balance.

[Wikipedia -- AVL tree](https://en.wikipedia.org/wiki/AVL_tree)
