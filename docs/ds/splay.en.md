This page briefly introduces how to maintain a binary search tree with a Splay tree.

## Definition

The **Splay tree**, or **spreading tree**, is a balanced binary search tree that, through the **splay operation**, continually rotates a certain node to the root node, so that the whole tree still satisfies the properties of a binary search tree, can complete insertion, search, and deletion operations in amortized $O(\log N)$ time, and stays balanced without degenerating into a chain.

The Splay tree was invented by Daniel Sleator and Robert Tarjan in 1985.

## Basic structure and operations

This section discusses the basic structure of the Splay tree and its core operations, the most important of which is the splay operation.

The Splay tree is a binary search tree; when searching for a certain value, it satisfies the property: the value of any node in the left subtree $<$ the value of the root node $<$ the value of any node in the right subtree.

### Maintaining information

This article uses arrays to simulate pointers to implement the Splay tree, and needs to maintain the following information:

|   rt  |    id   | fa\[i] | ch\[i]\[0/1] | val\[i] | cnt\[i] | sz\[i] |
| :---: | :-----: | :----: | :----------: | :-----: | :-----: | :----: |
| root node number | number of nodes already used | parent | left/right child numbers | node weight | number of occurrences of the weight | subtree size |

At initialization, just set all information to zero.

### Auxiliary operations

First are some simple auxiliary operations:

-   `dir(x)`: determine whether node $x$ is the left child or the right child of its parent node;
-   `push_up(x)`: after changing a node's position, update the information of node $x$ according to the information of its child nodes.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:aux"
    ```

### Rotation operation

To keep the Splay balanced, rotation operations need to be performed. The role of rotation is to move a certain node up by one position.

Rotation needs to guarantee:

-   The in-order traversal of the whole Splay is unchanged (the property of a binary search tree cannot be broken);
-   The information maintained by the affected nodes is still correct and valid;
-   `rt` must point to the root node after rotation.

Rotation in a Splay is divided into two kinds: left rotation and right rotation.

![](./images/splay-rotate.svg)

Observing the figure, we can see that if we want to move node $x$ (the $1$ in left rotation and the $2$ in right rotation) up by rotation, then the direction of rotation is uniquely determined by whether this node is the left or right child of its parent. Therefore, when implementing the rotation operation, we only need to pass in the node $x$ to be moved up.

Analyze the rotation steps specifically: (assume the node to be moved up is $x$, taking right rotation as an example)

1.  First, record the parent node $y$ of node $x$, and the parent node $z$ of $y$ (which may be empty), and record whether $x$ is the left child or the right child of $y$;
2.  Following the bottom-up order in the rotated tree, update in sequence: the left child of $y$ to the right child of $x$, the right child of $x$ to $y$, and if $z$ is non-empty, the child of $z$ to $x$;
3.  Following the same order, update in sequence: the parent node of the current left child of $y$ (if it exists) to $y$, the parent node of $y$ to $x$, and the parent node of $x$ to $z$;
4.  Maintain node information from bottom to top.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:rotate"
    ```

In the implementation of all functions, one should be careful not to modify the information of node $0$.

### Splay operation

The Splay tree requires that after accessing a node $x$, it be forcibly rotated to the root node. This operation is also called the splay operation.

Let the just-accessed node be $x$. To do the splay operation is to do a series of **splay steps** on $x$. Each time a splay step is done on $x$, the distance from $x$ to the root node becomes closer. Define $p$ as the parent node of $x$. There are three kinds of splay steps:

1.  **zig**: operate when $p$ is the root node. The Splay tree rotates according to the edge between $x$ and $p$. **zig** exists to handle the parity problem, and is executed as the last step of the splay operation only when $x$ has an odd depth at the start of the splay operation.

    ![splay-zig](./images/splay-zig.svg)

    That is, directly rotate $x$ right or left (figures 1, 2).

    ![Figure 1](./images/splay-rotate1.svg)![Figure 2](./images/splay-rotate2.svg)

2.  **zig-zig**: operate when $p$ is not the root node and $x$ and $p$ are both right children or both left children. The example figure below shows the case where $x$ and $p$ are both left children. The Splay tree first rotates according to the edge connecting $p$ with its parent node $g$, then rotates according to the edge connecting $x$ and $p$.

    ![splay-zig-zig](./images/splay-zig-zig.svg)

    That is, first rotate $p$ right or left, then rotate $x$ right or left (figures 3, 4).

    ![Figure 3](./images/splay-rotate3.svg)![Figure 4](./images/splay-rotate4.svg)

3.  **zig-zag**: operate when $p$ is not the root node and one of $x$ and $p$ is a right child and the other is a left child. The Splay tree first rotates according to the edge between $p$ and $x$, then rotates according to the newly generated resulting edge between $x$ and $g$.

    ![splay-zig-zag](./images/splay-zig-zag.svg)

    That is, rotate $x$ left then right, or right then left (figures 5, 6).

    ![Figure 5](./images/splay-rotate5.svg)![Figure 6](./images/splay-rotate6.svg)

???+ tip "Tip"
    Please try to simulate the $6$ rotation cases yourself to understand the basic idea of the splay operation.

Comparing the three splay steps, we can see that to distinguish which operation should be used at this time, the key is to judge whether $x$ is a child of the root node, and whether $x$ and its parent node are on the same side of their respective parent nodes.

The implementation provided here can specify any root node $z$ and move any node $x$ within its subtree up to $z$:

1.  First record the parent node $w$ of the root node $z$, so that `fa[x] == w` can be used to judge that $x$ is already at the root node;
2.  Record the current parent node $y$ of $x$; if $y$ and $w$ are the same, it means $x$ has already reached the root node;
3.  Otherwise, use `fa[y] == w` to judge whether $y$ is the root node. If so, directly do the zig operation to rotate $x$; if not, use `dir(x) == dir(y)` to judge whether to use zig-zig or zig-zag, the former first rotating $y$ then rotating $x$, the latter directly rotating $x$ twice.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:splay"
    ```

The splay operation is the core operation of the Splay tree, and is also the key step by which its time complexity can be guaranteed. Be sure to guarantee that each time after accessing a node downward, a splay operation is performed.

In addition, the splay operation updates the information of all nodes on the path from the current node $x$ to the root node $z$ from bottom to top. It is precisely because of this that one can modify a non-root node, and then use the splay operation to move it up to the root to complete the information update of the whole tree.

### Time complexity

The complexity of doing $m$ splay operations on a Splay tree of size $n$ is $O((n+m)\log n)$, and the single amortized complexity is $O(\log n)$.

??? note "Complexity proof based on potential analysis"
    For this we only need to analyze the complexity of the three operations **zig**, **zig-zig**, and **zig-zag**. For this, we use the **potential analysis method**, deriving the amortized complexity of the operations by studying the change in potential. Assume $m$ splay operations were performed on a Splay tree containing $n$ nodes; it can be analyzed as follows:
    
    **Definitions**:
    
    1.  **Potential of a single node**: $w(x) = \log(\text{size}(x))$, where $\text{size}(x)$ denotes the size of the subtree rooted at node $x$.
    2.  **Potential of the whole tree**: $\varphi = \sum w(x)$, i.e. the sum of the potentials of all nodes in the tree; the initial potential satisfies $\varphi_0 \leq n \log n$.
    3.  **Amortized cost of the $i$-th operation**: $c_i = t_i + \varphi_i - \varphi_{i-1}$, where $t_i$ is the actual operation cost, and $\varphi_i$ and $\varphi_{i-1}$ are the potentials after and before the operation respectively.
    
    **Properties**:
    
    1.  If $p$ is the parent node of $x$, then $w(p) \geq w(x)$, i.e. the potential of the parent node is not smaller than the potential of the child node.
    
    2.  Since the subtree size of the root node remains unchanged before and after the operation, the potential of the root node is unchanged during the operation.
    
    3.  If $\text{size}(p)\ge\text{size}(x)+\text{size}(y)$, then $2w(p) - w(x) - w(y) \geq 2$.
    
    ??? note "Proof of property 3"
        By the mean inequality we have
        
        $$
        \begin{aligned}
        2w(p) - w(x) - w(y) 
        &= \log\dfrac{\text{size}(p)^2}{\text{size}(x)\cdot\text{size}(y)} \\
        &> \log\dfrac{\left(\text{size}(x)+\text{size}(y)\right)^2}{\text{size}(x)\cdot\text{size}(y)} \\
        &\ge \log 4 \\
        &= 2.
        \end{aligned}
        $$
    
    Next, perform potential analysis on the **zig**, **zig-zig**, and **zig-zag** operations separately. Let the potentials of node $x$ before and after the operation be $w(x)$ and $w'(x)$ respectively. The notation of the nodes is consistent with [above](#splay-operation).
    
    **zig**: by properties 1 and 2, we have $w(p) = w'(x)$, and $w'(x) \geq w'(p)$. From this, the amortized cost is
    
    $$
    \begin{aligned}
    c_i &= 1 + w'(x) + w'(p) - w(x) - w(p)\\
    &= 1 + w'(p) - w(x)\\
    &\leq 1 + w'(x) - w(x).
    \end{aligned}
    $$
    
    **zig-zig**: by properties 1 and 2, we have $w(g) = w'(x)$, and $w'(x) \geq w'(p)$, $w(x) \leq w(p)$. Because
    
    $$
    \begin{aligned}
    \text{size}'(x) 
    &= 3 + \text{size}(A) + \text{size}(B) + \text{size}(C) + \text{size}(D) \\
    &> (1 + \text{size}(A) + \text{size}(B)) + (1 + \text{size}(C) + \text{size}(D)) \\
    &= \text{size}(x) + \text{size}'(g),
    \end{aligned}
    $$
    
    by property 3 we obtain
    
    $$
    2 w'(x) - w(x) - w'(g) \geq 2.
    $$
    
    From this, the amortized cost is
    
    $$
    \begin{aligned}
    c_i &= 2 + w'(x) + w'(p) + w'(g) - w(x) - w(p) - w(g) \\
    &= 2 + w'(p) + w'(g) - w(x) - w(p) \\
    &\le (2 w'(x) - w(x) - w'(g)) + w'(p) + w'(g) - w(x) - w(p) \\
    &= 2(w'(x)-w(x)) + w'(p) - w(p) \\
    &\le 3(w'(x)-w(x)).
    \end{aligned}
    $$
    
    **zig-zag**: by properties 1 and 2, we have $w(g) = w'(x)$, and $w(p) \geq w(x)$. Because $\text{size}'(x)>\text{size}'(p)+\text{size}'(g)$, by property 3 we obtain
    
    $$
    2 \cdot w'(x) - w'(g) - w'(p) \geq 2.
    $$
    
    From this, the amortized cost is
    
    $$
    \begin{aligned}
    c_i &= 2 + w'(x) + w'(p) + w'(g) - w(x) - w(p) - w(g) \\
    &= 2 + w'(p) + w'(g) - w(x) - w(p) \\
    &\le (2w'(x) - w'(g) - w'(p)) + w'(p) + w'(g) - w(x) - w(p) \\
    &= 2w'(x) - w(x) - w(p) \\
    &\le 2(w'(x) - w(x)).
    \end{aligned}
    $$
    
    **A single splay operation**:
    
    Let $w^{(n)}(x)=(w^{(n-1)})'(x)$ and $w^{(0)}(x)=w(x)$. Suppose a splay operation accesses nodes $x_{1}, x_{2}, \cdots, x_{n}$ in sequence, and finally $x_{1}$ becomes the root node. This must go through several **zig-zig** and **zig-zag** operations and at most one **zig** operation; the amortized cost of the first two kinds of operations does not exceed $3(w'(x)-w(x))$, while the amortized cost of the last operation does not exceed $3(w'(x) - w(x))+1$, so the total amortized cost does not exceed
    
    $$
    3(w^{(n)}(x_1) - w^{(0)}(x_1)) + 1 \le 3\log n + 1.
    $$
    
    Therefore, the amortized complexity of a single splay operation is $O(\log n)$. Thus, the time complexity of insertion, query, deletion, and other operations based on splay is also amortized $O(\log n)$.
    
    **Conclusion**:
    
    After performing $m$ splay operations, the actual cost
    
    $$
    \begin{aligned}
    \sum_{i=1}^m t_i &= \sum_{i=1}^m \left(c_i + \varphi_{i-1} - \varphi_i \right) \\
    &= \sum_{i=1}^m c_i + \varphi_0 - \varphi_m \\
    &\le m(3\log n+1) + n\log n.
    \end{aligned}
    $$
    
    Therefore, the actual time complexity of $m$ splay operations is $O((m+n)\log n)$.

??? info "Why can the rebalancing operation of the Splay tree obtain $O(\log n)$ amortized complexity?"
    The naive rebalancing idea is to repeatedly perform rotation operations on a node to make it rise until it becomes the root node. The problem with this naive idea is that, for a chain-shaped tree where all child nodes are left (right) children, it is equivalent to repeatedly performing the **zig** operation, so the constant term $1$ in the amortized complexity of the **zig** operation will keep accumulating, causing the final amortized complexity to reach the $O(\log n+n)$ level. The design of the Splay tree's rebalancing operation avoids the constant accumulation in the case of consecutive **zig**s, so that in a complete splay operation, at most one single **zig** operation is performed, thereby optimizing the time complexity.

## Balanced-tree operations

This section discusses the methods of implementing common operations of a balanced tree based on the Splay tree. Among them, the more important ones are finding an element by value or by rank; they can find a specific element and move it up to the root node, for subsequent processing.

As an example, this section will discuss the implementation of the template problem [Ordinary Balanced Tree](https://loj.ac/problem/104).

### Searching by value

As a binary search tree, one can find the corresponding node by value $v$; just compare the value $v$ to be found with the value of the current node, and after finding it, move that element up to the root.

Note that there are often cases where the corresponding node does not exist in the tree. For such cases, record the last accessed node (i.e. $y$ in the implementation), and move $y$ up to the root. At this point, the value stored by node $y$ must be either the largest among all elements smaller than $v$ (i.e. the predecessor of $v$), or the smallest among all elements larger than $v$ (i.e. the successor of $v$). This is because the search process guarantees that the left subtree always stores values smaller than $v$, while the right subtree always stores values larger than $v$.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find"
    ```

This implementation allows specifying any node $z$ as the root node and searching by value within its subtree.

### Accessing by rank

Because the subtree-size information is recorded, the Splay tree can also access elements by rank, i.e. find the $k$-th smallest element in the tree.

Let $k$ be the remaining rank; the specific steps are as follows:

-   If the left subtree is non-empty and the remaining rank $k$ is not greater than the size of the left subtree, then search in the left subtree;
-   Otherwise, if $k$ is not greater than the size of the left subtree plus the root, then the root node is the one to find;
-   Otherwise, subtract the size of the left subtree and the root from $k$, and continue searching in the right subtree;
-   Move the finally found element up to the root.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:loc"
    ```

This implementation needs to guarantee that the rank $k$ does not exceed the tree size at the root $z$.

Operation $4$ in the template problem requires returning a value by rank; just directly call this method and return the value.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-kth"
    ```

### Merge operation

Sometimes it is necessary to merge two Splay trees.

Let the root nodes of the two trees be $x$ and $y$ respectively; then to guarantee that the result is still a binary search tree, we need to require that the maximum value in the $x$ tree is smaller than the minimum value in the $y$ tree. This condition can usually be satisfied, because the two trees are often split from a larger subtree.

The merge operation is as follows:

-   If one or both of $x$ and $y$ are empty trees, directly return the root node of the non-empty tree or the empty tree;
-   Otherwise, use `loc(y, 1)` to move the minimum value in the $y$ tree up to the root $y$, then set its left child (which must be empty at this point) to $x$, update the node information, and return node $y$.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:merge"
    ```

The split operation is similar. Therefore, the Splay tree can imitate the idea of the [rotation-free treap](./treap.md#rotation-free-treap) to do various operations, including interval operations. [Later](#sequence-operations) we will introduce a more Splay-tree-style method of handling interval operations.

### Insertion operation

The insertion operation is a relatively complex process. The specific steps are as follows: (assume the inserted value is $v$)

-   Similar to the process of searching by value, search down according to $v$ to the node storing $v$ or an empty node, recording the parent node $y$ during the process;
-   If there is a node $x$ storing $v$, directly update the information, otherwise create a new node $x$;
-   Do the splay operation to move the last node $x$ up to the root.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:insert"
    ```

This implementation allows directly inserting a value into an empty tree. If you do not want to handle the empty tree, you can insert a dummy node into the tree in advance.

### Deletion operation

The deletion operation is also a relatively complex operation. The specific steps are as follows: (assume the deleted value is $v$)

-   First search for the node storing it by value $v$, and move it up to the root;
-   If there is no node storing it, directly return; (the previous step already did the splay operation)
-   Otherwise, update the node information;
-   If the obtained root node is an empty node, then merge the left and right subtrees as the new root node; note that before merging, the parent nodes of the roots of the two subtrees need to be updated to empty.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:remove"
    ```

### Querying the rank

Directly access the node by value $v$ (and move it up to the root), then return the corresponding value.

Note that when $v$ does not exist, the size relationship between the root returned by the method `find(rt, v)` and $v$ cannot be determined, and needs to be discussed separately.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-rank"
    ```

### Querying the predecessor

The predecessor is defined as the largest number smaller than $v$. The specific steps are as follows:

-   Access the node by value $v$ (and move it up to the root);
-   If the value at the root is smaller than $v$, then it must be the largest one, so directly return;
-   Otherwise, find the maximum value in the left subtree and move it up to the root.

The last step is equivalent to directly calling `loc(ch[rt][0], sz[ch[rt][0]])`, just omitting the unnecessary judgment.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-prev"
    ```

This implementation allows the predecessor to not exist, in which case it returns $-1$.

### Querying the successor

The successor is defined as the smallest number larger than $x$. The query method is similar to the predecessor, just replacing the maximum value of the left subtree with the minimum value of the right subtree, i.e. calling `loc(ch[rt][1], 1)`.

???+ example "Implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:find-next"
    ```

### Reference implementation

At the end of this section, we give the reference implementation of the template problem [Ordinary Balanced Tree](https://loj.ac/problem/104).

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-1.cpp:full-text"
    ```

## Sequence operations

The Splay tree can also be applied to sequences, used to maintain interval information. Compared with the segment tree, the Splay tree has a larger constant factor, but supports more complex sequence operations, such as interval reversal. As mentioned above, the Splay tree also supports split and merge operations, so it can imitate the [rotation-free treap](./treap.md#rotation-free-treap) to perform interval operations, which is not discussed too much here. This section mainly discusses the method of implementing interval operations based on the splay operation.

A Splay tree built from a sequence has the following properties:

-   The in-order traversal of the Splay tree corresponds to the left-to-right traversal of the original sequence;
-   A node on the Splay tree represents an element of the original sequence;
-   A subtree on the Splay tree represents an interval of the original sequence.

Because of the splay operation, the Splay subtree representing a certain interval can be quickly extracted.

As an example, this section will discuss the implementation of the template problem [Literary Balanced Tree](https://loj.ac/problem/105).

### Building the tree from a sequence

Before operating, the Splay tree needs to be built from the given sequence. According to the characteristics of the Splay tree, directly build a chain with only left children. The time complexity is $O(n)$.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:build"
    ```

The final splay operation updates the node information from bottom to top. For the convenience of the interval operations later, two sentinel nodes are added on the left and right sides of the sequence.

### Interval reversal

Taking interval reversal as an example, one can understand the method of interval operations: (let the interval be $[L,R]$)

-   First move node $L-1$ up to the root node, then in its right subtree, move node $R+1$ up to the root of the right subtree;
-   At this point, let $x$ be the left child of the right child of the root node; then the subtree rooted at $x$ corresponds to the interval $[L,R]$;
-   Operate on the interval $[L,R]$ at $x$, and apply a lazy tag;
-   Push down the tag once at $x$, then use the splay operation to move $x$ up to the root.

The operation needed in the first step is the "access by rank" in the balanced-tree operations above, because the label of an element is its rank. Because it involves the management of lazy tags, its implementation is slightly different from above.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:reverse"
    ```

The splay operation in the last step is not to guarantee the correctness of the complexity, but to update the node information. Because the splay operation involves the left and right child nodes of node $x$, the tag at node $x$ needs to be pushed down once beforehand. Of course, for the interval reversal operation alone, the reversal of a subinterval does not affect ancestor nodes, so it is also correct to omit this step. The implementation here retains these two lines to illustrate the operation method in the general case.

### Lazy-tag management

First, the auxiliary functions `lazy_reverse(x)` and `push_down(x)` are needed. The former swaps the left and right children and updates the lazy tag; the latter pushes the tag down.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:push-down"
    ```

Then, we only need to push down the tag when passing a node downward. The operations required by the template problem are relatively simple; only the operation of searching by rank (i.e. `loc`) involves accessing nodes downward. Note that the tag needs to be pushed down **before** the function accesses a new node each time.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:push-down-lazy"
    ```

Because all lazy tags of the passed path have already been removed when accessing nodes downward, there is no longer any need to handle lazy tags when using the splay operation to move a node up. However, the one node of the interval operation should be handled carefully: because it is likewise on the path of the splay operation, but was just operated on, there may be an as-yet-unpushed tag, which needs to be pushed down first and then the splay operation done, just as done above.

### Reference implementation

At the end of this section, we give the reference implementation of the template problem [Literary Balanced Tree](https://loj.ac/problem/105).

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/splay/splay-2.cpp:full-text"
    ```

## Exercises

These problems are all bare Splay trees maintaining a binary search tree:

-   [【Template】Ordinary Balanced Tree](https://loj.ac/problem/104)
-   [【Template】Literary Balanced Tree](https://loj.ac/problem/105)
-   [「HNOI2002」Turnover Statistics](https://loj.ac/problem/10143)
-   [「HNOI2004」Pet Adoption Center](https://loj.ac/problem/10144)

The Splay tree also appears in more complex application scenarios:

-   [「Cerc2007」robotic sort](https://www.luogu.com.cn/problem/P4402)
-   [「HNOI2011」Bracket Repair / 「JSOI2011」Bracket Sequence](https://www.luogu.com.cn/problem/P3215)
-   [Fake Balanced Tree (tree of trees)](https://loj.ac/problem/106)
-   [BZOJ 2827 Thousand Mountains, Birds Vanish](https://hydro.ac/p/bzoj-P2827)
-   [「Lydsy1706 Monthly Contest」k-th Smallest Value Query](https://hydro.ac/p/bzoj-P4923)
-   [POJ3580 SuperMemo](http://poj.org/problem?id=3580)

## References and notes

Part of the content of this article is cited from the algocode algorithm blog; special thanks!
