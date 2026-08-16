author: Ir1d, 0xis-cn

## Introduction

The **scapegoat tree** is a weight-balanced tree that maintains balance by relying on a rebuild operation. The scapegoat tree detects whether the tree has become unbalanced after an insertion or deletion operation; if unbalanced, it will perform a targeted rebuild to restore balance.

Generally, the scapegoat tree does not support interval operations and cannot be fully persistent; but it has the advantages of simple implementation and a small constant factor.

## Basic structure and operations

The core operations of the scapegoat tree are the rebuild, insertion, and deletion operations.

### Node information

The scapegoat tree needs to store the following information, used for the tree's self-balancing operations:

-   Structural information of the tree:
    -   `id`: the number of nodes already used;
    -   `rt`: the root node;
    -   `lc[x]`, `rc[x]`: the left and right child nodes;
    -   `tot[x]`: the size of the subtree rooted at $x$ (each node counts as $1$) [^tot-cnt];
    -   `tot_active`: the number of nodes in the whole tree that are not deleted (i.e. `cnt[x] != 0`).

When using a scapegoat tree to implement a balanced tree, the following information also needs to be stored:

-   Node information of the balanced tree:
    -   `val[x]`: the value stored at the node;
    -   `cnt[x]`: the count of the value stored at the node (may be $0$);
    -   `sz[x]`: the count of values stored in the subtree rooted at $x$.

To maintain node information, a `push_up` operation can be implemented:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:push-up"
    ```

Note the difference in the way `tot[x]` and `sz[x]` are updated.

### Rebuild operation

When the tree becomes unbalanced, a certain subtree needs to be rebuilt to make it as balanced as possible. The rebuild is divided into two steps:

-   Do an in-order traversal of the subtree to be rebuilt, storing all non-deleted nodes into a sequence;
-   Build the tree by binary division, i.e. take the midpoint as the root, recursively build the subtrees on the left and right sides, and update the node information.

The reference implementation is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:rebuild"
    ```

When building the tree, note to maintain the node information, including the information of leaf nodes.

The complexity of a single rebuild is $\Theta(|T_x|)$, so if a rebuild is performed on every insertion and deletion, the complexity will be unacceptable. The core idea of the scapegoat tree lies precisely in the choice of the rebuild timing, thereby realizing an amortized complexity of $O(\log n)$.

### Insertion operation

The insertion operation may cause the tree to become unbalanced. To judge the imbalance of the tree, a parameter $\alpha\in(0.5,1)$ needs to be introduced; the usual choice is between $0.7\sim 0.8$.

If the depth of the newly inserted node exceeds $\lfloor\log_{1/\alpha}|T|\rfloor$, where $|T|$ is the size of the updated tree, then during backtracking one needs to find the node where the imbalance occurred and rebuild it. At this point, the imbalance of the subtree rooted at $x$ is judged according to the following condition:

$$
\max\{|T_{\mathrm{left}(x)}|,|T_{\mathrm{right}(x)}|\} > \alpha\cdot |T_x|,
$$

where $\mathrm{left}(x)$ and $\mathrm{right}(x)$ are the left and right child nodes of $x$ respectively, and $|T_x|$ is the size of the subtree rooted at $x$.

The specific steps of the insertion operation are as follows:

-   First use the property of the binary search tree to find the position of the inserted value going down, recording the depth while descending;
-   If a node already exists, directly modify the node information, otherwise create a new node;
-   If the newly created node is too deep, backtrack from bottom to top to the root, update the node information, and record the first (or any one) node whose subtree is unbalanced;
-   If there is an unbalanced node, rebuild the subtree of the unbalanced node.

The reference implementation is as follows:

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:insert"
    ```

Note that a single insertion causes at most one rebuild. If no node was added, or the added node is not too deep, or a rebuild has already been performed during this backtracking process, then there is no need to continue judging imbalance. Redundant rebuilds may cause efficiency loss [^insert-complexity]. The first unbalanced node during backtracking is the so-called "scapegoat".

### Deletion operation

The handling of the deletion operation is very simple. The deletion strategy of the scapegoat tree is "lazy deletion", i.e. when a node is empty, the node is not removed, but is left for subsequent handling.

Of course, if there are too many empty nodes in the tree, the access efficiency of the tree will drop greatly. Therefore, the scapegoat tree maintains two counts: the number of non-deleted nodes in the whole tree and the number of nodes actually used in the whole tree. For a chosen threshold [^threshold] $\alpha\in(0,1)$, when the ratio of the former to the latter drops below $\alpha$, a rebuild of the whole tree is performed, deleting all empty nodes during the rebuild.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:remove"
    ```

### Time complexity

The time complexity of accessing a node of a scapegoat tree of size $n$ is $O(\log n)$ per access, and the amortized time complexity of $\Theta(n)$ insertions and deletions is also $O(\log n)$ per operation.

This section only gives a brief argument for the time complexity of the scapegoat tree; for a detailed proof please refer to the original paper.

??? note "Argument for the time complexity of the scapegoat tree"
    Because of the lazy-deletion strategy, a scapegoat tree with $n$ non-deleted nodes may occupy $\alpha^{-1}n$ nodes. Since they differ only by a constant factor, this article does not distinguish between the number of non-deleted nodes and the number of occupied nodes of the scapegoat tree in its description, and uniformly calls it the "size of the tree".
    
    1.  **Access operation**: the complexity of the access operation is guaranteed because the height of a scapegoat tree of size $n$ is always $O(\log n)$.
    
        First, distinguish two concepts:
    
        -   $\alpha$-weight balance: at all nodes, the size of the subtree of the left and right child nodes does not exceed $\alpha$ times the size of the subtree at that node;
        -   $\alpha$-height balance: the height of the tree does not exceed $\lfloor\log_{1/\alpha}|T|\rfloor$, where $T$ is the size of the tree.
    
        $\alpha$-weight balance implies $\alpha$-height balance, because each time the depth of a child node increases by one, the size decreases to $\alpha$ times the original; the converse does not necessarily hold. More strictly, after each operation ends, the scapegoat tree is always $\alpha$-height balanced [^hei-bal], which guarantees the complexity of the access operation.
    
        Only the insertion operation changes the structure of the tree, so we only need to show that after each insertion operation, the scapegoat tree is still $\alpha$-height balanced. If the newly inserted node is too deep, causing the whole tree to no longer be $\alpha$-height balanced, then when backtracking from that node to the root, one will encounter at least one node, i.e. the "scapegoat", whose subtree is no longer $\alpha$-weight balanced. After rebuilding it, the height of the subtree will decrease by at least one, so the newly inserted node will no longer be too deep.
    2.  **Insertion operation**: the complexity of the insertion operation is amortized $O(\log n)$.
    
        Suppose after a certain insertion operation, a subtree rebuild occurs at node $x$, with time cost $\Theta(|T_x|)$. Because when node $x$ was just inserted, or just after it experienced the previous rebuild (of itself or an ancestor node), its left and right subtrees differ by at most one node. And before this rebuild, at node $x$ the following must hold
    
        $$
        \max\{|T_{\mathrm{left}(x)}|,|T_{\mathrm{right}(x)}|\} > \alpha\cdot |T_x|.
        $$
    
        This condition guarantees that the difference in size between the left and right subtrees is at least $(2\alpha-1)|T_x|$. Therefore, between these two rebuilds, $\Omega(|T_x|)$ nodes were inserted into subtree $T_x$.
    
        By amortized analysis [^alternative-analysis], if each time a node is inserted, we add $\Theta(1)$ potential to each node on the path from the root to that node (before the possible rebuild), then before the subtree rebuild at node $x$, $\Omega(|T_x|)$ potential must have already accumulated at node $x$, sufficient to pay off the cost $\Theta(|T_x|)$ of the subtree rebuild at $x$. Because the depth of the tree is $O(\log n)$, the potential added by a single insertion is $O(\log n)$; this shows that the total sum of potential added over $\Theta(n)$ insertion operations is $O(n\log n)$. From this, the total cost of subtree rebuilds is also $O(n\log n)$, and the amortized time complexity of a single insertion operation (including the rebuild) is $O(\log n)$.
    
        Note that the analysis does not assume that no other rebuild occurred inside subtree $T_x$ between the two rebuilds at node $x$. Therefore, as long as we only rebuild the subtree at nodes satisfying the imbalance condition, we can guarantee that the complexity is correct.
    3.  **Deletion operation**: the complexity of the deletion operation is also amortized $O(\log n)$.
    
        A rebuild caused by deletion results in the whole tree containing no empty nodes. And before a certain deletion causes a rebuild, there are already $\Theta(n)$ empty nodes in the whole tree, which means at least $\Theta(n)$ deletion operations have been performed. Because the addressing complexity of each deletion operation is $O(\log n)$, and the complexity of a single rebuild is $\Theta(n)$, the actual time cost of these $\Theta(n)$ deletion operations is
    
        $$
        \Theta(n)O(\log n)+\Theta(n)
        $$
    
        Therefore, the amortized complexity of a single deletion is $O(\log n)$.

## Balanced-tree operations

This section introduces the method of maintaining a multiset with a scapegoat tree.

Except for the operations introduced in the previous section, the remaining operations are all common operations of a balanced tree. However, because there may be empty nodes in the scapegoat tree, these operations also need to be adjusted accordingly.

### Querying the rank

Use the property of the binary search tree to search down for the node position, recording the number of values stored on the left side of the path during the process.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:find-rank"
    ```

### Querying the value by rank

Use the information of the number of values stored in the subtree recorded by the node to search down. Note that there may be nodes with a count of zero.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:find-kth"
    ```

### Querying the predecessor and successor

Just combine the above two functionalities.

???+ example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:pred-succ"
    ```

If you want to implement it directly, note to handle nodes with a count of zero.

### Reference implementation

At the end of this section, we give the reference implementation of the template problem [Ordinary Balanced Tree](https://loj.ac/p/104).

??? example "Reference implementation"
    ```cpp
    --8<-- "docs/ds/code/sgt/sgt.cpp:full-text"
    ```

## References

-   Galperin, Igal, and Ronald L. Rivest. "Scapegoat trees." Proceedings of the fourth annual ACM-SIAM Symposium on Discrete algorithms. 1993.
-   [Scapegoat Tree - Wikipedia](https://en.wikipedia.org/wiki/Scapegoat_tree)
-   [Scapegoat Tree - riteme's blog](https://riteme.site/blog/2016-4-6/scapegoat.html)

[^tot-cnt]: One can also count only the number of non-deleted nodes, in which case `tot_active` no longer needs to be counted, but the number of all occupied nodes `tot_max` needs to be counted, and the code can be adjusted accordingly.

[^insert-complexity]: According to the complexity analysis later, these efficiency losses only mean a larger constant factor, and the complexity is still correct. Because judging the tree depth may involve relatively many floating-point logarithm operations, code that does not judge the tree depth but only judges imbalance may be faster on some data.

[^threshold]: It need not be the same as the parameter chosen during the insertion operation above. Although the original paper made such an assumption, choosing a different parameter only leads to a change in the constant term of the complexity of a single operation, and the overall complexity is still correct.

[^hei-bal]: According to the original definition, $n$ refers to the number of non-deleted nodes, so it can only be guaranteed that the tree height does not exceed $\lfloor\log_{1/\alpha}n\rfloor+1$, which is called weak $\alpha$-height balance. Here the difference in this constant term is not scrutinized.

[^alternative-analysis]: Some articles simply analyze it as $\Omega(|T_x|)$ insertions corresponding to one rebuild, so the amortized complexity is $\dfrac{\Omega(|T_x|)O(\log n)+\Theta(|T_x|)}{\Omega(|T_x|)} = O(\log n)$. Such an approach can aid in understanding why the amortized complexity is correct, but it is not rigorous. This is because a single insertion may correspond to rebuilds of multiple ancestor nodes, so when a rebuild occurs at node $x$, the number of nodes in the subtree that did not cause a rebuild is not obviously $\Omega(|T_x|)$.
